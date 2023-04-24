from odoo import fields, models
from .cargoson_queue import TaskResult
import logging
logger = logging.getLogger(__name__)


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

    status = fields.Selection([
            ('pending', 'Pending'),
            ('success', 'Success'),
            ('error', 'Error'),
        ], string='Status', required=True)

    booking_data = fields.Text('Booking data')  # in json

    def update_booking_data(self):
        """
            Updates booking info until label URL is set.
            Asynchronously called by queue task system.

            :return: TaskResult
        """
        pass

    def fetch_label(self):
        """
            Tries to fetch label_url and stores it locally.
            Asynchronously called by queue task system.

            :return: TaskResult
        """
        pass
