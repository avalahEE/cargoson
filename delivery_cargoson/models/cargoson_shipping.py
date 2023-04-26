from odoo import fields, models, _
from .cargoson_queue import TaskResult
import json
import base64
import requests
import logging
logger = logging.getLogger(__name__)

MAX_TRIES = 20


class CargosonShipping(models.Model):
    _name = 'cargoson.shipping'
    _description = 'Shipping info for a booking in Cargoson'

    stock_picking_id = fields.Many2one('stock.picking', string='Delivery Order', ondelete='cascade', required=True)
    delivery_carrier_id = fields.Many2one(
        'delivery.carrier', string='Delivery carrier', ondelete='cascade', required=True)

    reference = fields.Char('Cargoson Reference')
    token = fields.Char('Cargoson Token')

    tracking_url = fields.Text('Tracking URL')
    tracking_code = fields.Char('Tracking Code')

    label_url = fields.Text('Label URL')
    label_fetched = fields.Datetime('Label saved at')
    label_pdf = fields.Binary(attachment=True)

    status = fields.Selection([
            ('pending', 'Pending'),
            ('success', 'Success'),
            ('error', 'Error'),
        ], string='Shipping Status', required=True)

    booking_data = fields.Text('Booking data')  # in json

    def update_booking_data(self, task):
        """
            Updates booking info until label URL is set.
            Asynchronously called by queue task system.

            :return: TaskResult
        """
        self.ensure_one()

        if not self.stock_picking_id:
            logger.error('Cannot update booking data: no stock.picking reference')
            return TaskResult.ERR

        if task.num_tries > MAX_TRIES:
            logger.warning('Giving up on updating booking data for: %s', self.reference)
            self.stock_picking_id.message_post(body=_('Giving up on updating booking data for: %s', self.reference))
            return TaskResult.ERR

        # noinspection PyPep8Naming
        Cargoson = self.delivery_carrier_id

        # FIXME: obtain result schema from vendor
        booking_data = Cargoson.cargoson_api_get(f'bookings/{self.reference}', [])
        # logger.info('booking = %s', booking_data)

        if not isinstance(booking_data, dict):
            # TODO: log error in cargoson.log
            logger.warning(_('Booking data unavailable. Cargoson reference: %s', self.reference))
            return TaskResult.RETRY

        if booking_data.get('latest_status') != 'booked':
            # TODO: log error in cargoson.log
            logger.warning(_(
                'Booking shipping was not successful: "%s"', booking_data.get('carrier_response_message')))
            return TaskResult.RETRY

        vals = dict()
        self._update_parameter('tracking_url', vals, booking_data.get('tracking_url'), name='Tracking URL')
        self._update_parameter('label_url', vals, booking_data.get('label_url'), name='Label URL')
        self._update_parameter(
            'tracking_code', vals,
            booking_data.get('tracking_reference') or booking_data.get('carrier_reference'),
            name='Tracking Code')
        vals['booking_data'] = json.dumps(booking_data)
        self.write(vals)

        if self.tracking_url and self.label_url and self.tracking_code:
            self.stock_picking_id.write(dict(carrier_tracking_ref=self.tracking_code))
            self.stock_picking_id.message_post(body=_(
                'Delivery booking successful for shipment %s (%s)', self.tracking_code, self.reference))
            self.write(dict(status='success'))
            logger.info('Booking data complete: %s', self.reference)
            return TaskResult.OK

        return TaskResult.RETRY

    def fetch_label(self, task):
        """
            Tries to fetch label_url and stores it locally.
            Asynchronously called by queue task system.

            :return: TaskResult
        """
        if not self.stock_picking_id:
            logger.error('Cannot attach label: no stock.picking reference')
            return TaskResult.ERR

        if task.num_tries > MAX_TRIES:
            logger.warning('Giving up on fetching label for: %s', self.reference)
            self.stock_picking_id.message_post(body=_('Giving up on fetching label for: %s', self.reference))
            return TaskResult.ERR

        if not self.label_url:
            return TaskResult.RETRY

        try:
            response = requests.get(self.label_url)
            content_type = response.headers.get('Content-Type')
            if content_type != 'application/pdf':
                logger.warning('Fetching label for %s: expected PDF, received: %s', self.reference, content_type)
                return TaskResult.RETRY

            self.label_pdf = base64.b64encode(response.content)
            self.label_fetched = fields.Datetime.now()
            logger.info('Downloaded PDF data: %s bytes', len(self.label_pdf))

            log_message = _('Cargoson shipping label created: %s', self.reference)
            log_attachments = [(f'{self.reference}.pdf', response.content)]
            self.stock_picking_id.message_post(body=log_message, attachments=log_attachments)
            return TaskResult.OK
        except Exception as err:
            logger.info('Failed to fetch label: %s', err)
            return TaskResult.RETRY

    def _update_parameter(self, key, vals, value, name=None):
        if not value:
            return

        if not name:
            name = key

        if value and not getattr(self, key):
            msg = _('%s has been updated: %s', name, value)
            logger.info(msg)
            if self.stock_picking_id:
                self.stock_picking_id.message_post(body=msg)
        vals[key] = value
