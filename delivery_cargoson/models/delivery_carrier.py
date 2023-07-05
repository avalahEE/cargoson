from odoo import models, fields, api, _
from odoo.exceptions import UserError
from urllib.parse import urljoin
from .schema import AvailablePrices, PriceRequestShipment, Order
from .schema.price_request_shipment import (
    PriceRequestShipmentRows_AttributesItem,
    PriceRequestShipmentRows_AttributesItemPackage_Type
)
from .schema.order import (
    OrderRows_AttributesItem,
    OrderRows_AttributesItemPackage_Type,
    OrderOptions,
    OrderDocuments_AttributesItem,
    OrderRows_AttributesItemAdr_Rows_AttributesItem
)

import json
import math
import requests
import traceback
import logging
logger = logging.getLogger(__name__)


# noinspection PyProtectedMember,PyMethodMayBeStatic
class ProviderCargoson(models.Model):
    _inherit = 'delivery.carrier'

    delivery_type = fields.Selection(selection_add=[
        ('cargoson', 'Cargoson')
    ], ondelete={'cargoson': lambda recs: recs.write({'delivery_type': 'fixed', 'fixed_price': 0})})

    cargoson_api_url = fields.Char(string='Cargoson API URL', default='https://www.cargoson.com/api')
    cargoson_api_key = fields.Char(string='Cargoson API key', default='NotConfigured')
    cargoson_test_api_url = fields.Char(
        string='Cargoson Test API URL', default='https://cargoson-staging.herokuapp.com/api')
    cargoson_test_api_key = fields.Char(string='Cargoson Test API key', default='NotConfigured')
    cargoson_no_carrier = fields.Boolean(string='No Carrier', default=False)

    cargoson_parcel_machine_country_ids = fields.Many2many(
        'res.country',
        'delivery_carrier_cargoson_country_rel', 'carrier_id', 'country_id',
        'Enabled parcel machine regions')

    def cargoson_rate_shipment(self, order):
        logger.info('Cargoson: rate shipment for: %s', order.name)
        collection_address = order.get_cargoson_collection_address()
        delivery_address = order.get_cargoson_delivery_address()
        return self._cargoson_rate_shipment(
            order.name, collection_address, delivery_address, order.cargoson_delivery_weight,)

    def _cargoson_rate_shipment(self, document_name, collection_address, delivery_address, weight, width=0, height=0, depth=0):
        logger.info('Cargoson: rate shipment for: %s (weight=%s)', document_name, weight)
        logger.info('Cargoson package dimensions from shipping wizard: width: %s, height: %s, depth: %s, weight: %s', width, height, depth, weight)

        if (width, height, depth) == (0, 0, 0):
            wizard = self.env['choose.delivery.carrier'].search([], order='id desc', limit=1)
            width = wizard.cargoson_width
            height = wizard.cargoson_height
            depth = wizard.cargoson_depth

        if weight <= 0:
            raise UserError(_('The combined weight of the shipment must be greater than zero.'))

        carrier = self._match_address(delivery_address)
        if not carrier:
            return {
                'success': False,
                'price': 0.0,
                'error_message': _('Error: this delivery method is not available for this address.'),
                'warning_message': False
            }

        self._cargoson_validate_address(collection_address)
        self._cargoson_validate_address(delivery_address)

        cargoson_options = self.env.context.get('cargoson', None)
        if not cargoson_options:
            return {
                'success': False,
                'price': 0.0,
                'error_message': False,
                'warning_message': False
            }

        package_type = cargoson_options.get('package_type')
        if not package_type:
            return {
                'success': False,
                'price': 0.0,
                'error_message': _('Package type is required'),
                'warning_message': _('Please select package type')
            }

        package_qty = cargoson_options.get('package_qty', 0)
        if package_qty < 1:
            return {
                'success': False,
                'price': 0.0,
                'error_message': _('Package quantity must be greater than 0'),
                'warning_message': False
            }

        logger.info('_cargoson_rate_shipment: Cargoson package %s dimensions: %s',
                    document_name, {'width': width, 'height': height, 'depth': depth, 'weight': weight})

        package = PriceRequestShipmentRows_AttributesItem(
            weight=math.ceil(weight),
            width=math.ceil(width),
            length=math.ceil(depth),
            height=math.ceil(height),
            package_type=PriceRequestShipmentRows_AttributesItemPackage_Type.from_dict(package_type),
            quantity=package_qty,
            description='Goods with {} package'.format(package_type)
        )

        collection_date = cargoson_options.get('collection_date')
        if not collection_date:
            collection_date = fields.Date.today()

        price_request = PriceRequestShipment(
            collection_date=collection_date.isoformat(),
            collection_postcode=collection_address.zip,
            collection_country=collection_address.country_id.code,
            delivery_postcode=delivery_address.zip,
            delivery_country=delivery_address.country_id.code,
            collection_with_tail_lift=cargoson_options.get('collection_with_tail_lift', False),
            collection_prenotification=cargoson_options.get('collection_prenotification', False),
            delivery_with_tail_lift=cargoson_options.get('delivery_with_tail_lift', False),
            delivery_prenotification=cargoson_options.get('delivery_prenotification', False),
            delivery_return_document=cargoson_options.get('delivery_return_document', False),
            delivery_to_private_person=cargoson_options.get('delivery_to_private_person', False),
            frigo=cargoson_options.get('frigo', False),
            adr=cargoson_options.get('adr', False),
            rows_attributes=[package]
        )
        result = self.cargoson_api_post('freightPrices/list', price_request.as_dict(), AvailablePrices)
        if result:
            return {
                'success': True,
                'price': 0.0,
                'error_message': False,
                'warning_message': False,
                'cargoson': result,
            }

        return {
            'success': False,
            'price': 0.0,
            'error_message': _('Error: failed to query available prices from Cargoson'),
            'warning_message': False
        }

    def cargoson_send_shipping(self, pickings):
        res = []
        for picking in pickings:
            res += self._cargoson_send_shipping(picking)
        return res

    def cargoson_get_tracking_link(self, picking):
        if picking.cargoson_shipping_id:
            return picking.cargoson_shipping_id.tracking_url
        return False

    def cargoson_cancel_shipment(self, pickings):
        for picking in pickings:
            if picking.cargoson_shipping_id:
                cargoson_ref = picking.cargoson_shipping_id.reference
                try:
                    if cargoson_ref:
                        self.cargoson_api_delete(f'bookings/{cargoson_ref}')

                    picking.cargoson_shipping_id.sudo().unlink()
                    picking.write({
                        'carrier_tracking_ref': '',
                        'carrier_price': 0.0
                    })
                    if picking.cargoson_shipping_options_id:
                        picking.cargoson_shipping_options_id.sudo().unlink()

                except Exception as err:
                    raise UserError(_('Could not cancel shipment %s: %s', cargoson_ref, err))

    def _cargoson_send_shipping(self, picking):
        logger.info('_cargoson_send_shipping: Cargoson sending shipment %s', picking.name)
        if not picking.cargoson_shipping_options_id:
            logger.info('_cargoson_send_shipping: Cargoson shipping_options_id not available')
            return [{'exact_price': 0, 'tracking_number': False}]

        collection_address = picking.get_cargoson_collection_address()
        delivery_address = picking.get_cargoson_delivery_address()
        self._cargoson_validate_address(collection_address)
        self._cargoson_validate_address(delivery_address)

        weight = picking.weight
        opts = picking.cargoson_shipping_options_id

        width = opts.cargoson_width
        height = opts.cargoson_height
        depth = opts.cargoson_depth

        adr_row_attrs = None
        if opts.adr:
            adr_row_attrs = OrderRows_AttributesItemAdr_Rows_AttributesItem(
                adr_un=opts.ADR_UN,
                adr_group=opts.ADR_GROUP,
                adr_class=opts.ADR_CLASS,
                adr_neq=opts.ADR_NEQ,
                adr_description=opts.ADR_DESCRIPTION
            )

        logger.info('Wizard adr_row_attrs: %s', adr_row_attrs.as_dict() if isinstance(adr_row_attrs, OrderRows_AttributesItemAdr_Rows_AttributesItem) else [])
        logger.info('_cargoson_send_shipping: Cargoson package %s dimensions: %s', picking.name,
                    {'weight': weight, 'width': width, 'height': height, 'depth': depth})
        package = OrderRows_AttributesItem(
            weight=math.ceil(weight),
            width=math.ceil(width),
            length=math.ceil(depth),
            height=math.ceil(height),
            package_type=OrderRows_AttributesItemPackage_Type.from_dict(opts.package_type),
            quantity=opts.package_qty,
            description='Goods with {} package'.format(opts.package_type),
            adr_rows_attributes=[adr_row_attrs] if isinstance(adr_row_attrs, OrderRows_AttributesItemAdr_Rows_AttributesItem) else []
        )
        # TODO: add optional adr rows to package
        order_options = OrderOptions(direct_booking_service_id=None)
        if not self.cargoson_no_carrier:
            order_options = OrderOptions(direct_booking_service_id=opts.selected_service_id)
            # order_attribs = OrderDocuments_AttributesItem() # TODO: attach cmr / waybill

        order = Order(
            customer_reference=picking.name,

            collection_date=picking.scheduled_date.isoformat(),
            collection_company_name=collection_address.display_name,
            collection_address_row_1=collection_address.street,
            collection_address_row_2=collection_address.street2 or None,
            collection_city=collection_address.city,
            collection_postcode=collection_address.zip,
            collection_country=collection_address.country_id.code,
            collection_contact_name=collection_address.name,
            collection_contact_phone=collection_address.mobile or collection_address.phone,
            collection_contact_email=collection_address.email or None,

            delivery_company_name=delivery_address.display_name,
            delivery_address_row_1=delivery_address.street,
            delivery_address_row_2=delivery_address.street2 or None,
            delivery_city=delivery_address.city,
            delivery_postcode=delivery_address.zip,
            delivery_country=delivery_address.country_id.code,
            delivery_contact_name=delivery_address.name,
            delivery_contact_phone=delivery_address.mobile or delivery_address.phone,
            delivery_contact_email=delivery_address.email or None,

            # delivery options
            collection_with_tail_lift=opts.collection_with_tail_lift,
            collection_prenotification=opts.collection_prenotification,
            delivery_with_tail_lift=opts.delivery_with_tail_lift,
            delivery_prenotification=opts.delivery_prenotification,
            delivery_return_document=opts.delivery_return_document,
            delivery_to_private_person=opts.delivery_to_private_person,
            frigo=opts.frigo,
            options=order_options,

            rows_attributes=[package]
        )

        result = self.cargoson_api_post('queries', order.as_dict())  # FIXME: obtain result schema from vendor

        if (
            not isinstance(result, dict) or
            not bool(result.get('reference')) or
            len(result.get('errors', list())) > 0 or
            result.get('query_status') != 'created' or
            result.get('booking_status') != 'created' and
            not self.cargoson_no_carrier
        ):
            raise UserError(_('Failed to create direct booking for courier service "%s"', opts.selected_carrier_name))

        if result:
            id = result.get('id')
            if id:
                cmr_url = self._cargoson_get_self_service_url('/bookings/%s/cmr' % id)
                picking.message_post(body=_('CMR document: %s') % cmr_url)

                waybill_url = self._cargoson_get_self_service_url('/bookings/%s/consignment_note' % id)
                picking.message_post(body=_('e-Waybill: %s') % waybill_url)

                customs_url = self._cargoson_get_self_service_url('/bookings/%s/declaration_summary.pdf' % id)
                picking.message_post(body=_('Customs declaration: %s') % customs_url)

                if opts.adr:
                    dgd_url = self._cargoson_get_self_service_url('/bookings/%s/dgd' % id)
                    picking.message_post(body=_('DGD document: %s') % dgd_url)

        tracking_url = result.get('tracking_url')
        label_url = result.get('label_url')
        cargoson_ref = result.get('reference')
        tracking_number = result.get('tracking_reference') or result.get('carrier_reference')

        cargoson_shipping = self.env['cargoson.shipping'].sudo().create({
            'stock_picking_id': picking.id,
            'delivery_carrier_id': picking.carrier_id.id,
            'reference': cargoson_ref,
            'tracking_url': tracking_url,
            'tracking_code': tracking_number,
            'label_url': label_url,
            'token': result.get('token'),
            'status': 'pending',
        })
        picking.write(dict(cargoson_shipping_id=cargoson_shipping.id))
        if tracking_url:
            picking.message_post(body=_('Tracking URL has been updated: %s', tracking_url))
        if tracking_number:
            picking.message_post(body=_('Tracking Code has been updated: %s', tracking_number))
        if label_url:
            picking.message_post(body=_('Label URL has been updated: %s', label_url))

        task_update_booking = self.env['cargoson.queue.task'].sudo().create({
            'name': f'Fetch booking data: {cargoson_ref}',
            'res_id': cargoson_shipping.id,
            'res_name': 'cargoson.shipping',
            'method': 'update_booking_data',
        })

        task_fetch_label = self.env['cargoson.queue.task'].sudo().create({
            'name': f'Fetch label PDF: {cargoson_ref}',
            'res_id': cargoson_shipping.id,
            'res_name': 'cargoson.shipping',
            'method': 'fetch_label',
        })

        # try to update booking data immediately
        task_update_booking.execute(cargoson_shipping)

        # try to update label immediately
        task_fetch_label.execute(cargoson_shipping)

        return [{
            'exact_price': opts.selected_price,

            # NOTE: this returns the cargoson reference if the actual tracking number is not yet available
            'tracking_number': cargoson_shipping.tracking_code or cargoson_ref
        }]

    def cargoson_api_get(self, path, params, schema_class=None):
        self.ensure_one()
        url = self._cargoson_get_api_url(path)
        try:
            log_request = 'GET: {}\nHEADERS: {}\n\n{}\n'.format(url, self._cargoson_get_headers(), json.dumps(params))
            self.log_xml(log_request, path)

            response = requests.get(url, params=params, headers=self._cargoson_get_headers())

            log_response = 'URL: {}\n\n{}\n'.format(url, response.text)
            self.log_xml(log_response, path)

            data = response.json()
            if schema_class is None:
                return data
            return schema_class.from_dict(data)
        except Exception as err:
            logger.error(err)
            self.log_xml('URL: {}\nERROR: {}\n\n{}\n'.format(url, err, traceback.format_exc()), path)

    def cargoson_api_post(self, path, data, schema_class=None):
        self.ensure_one()
        url = self._cargoson_get_api_url(path)
        try:
            json_data = json.dumps(data)
            log_request = 'POST: {}\nHEADERS: {}\n\n{}\n'.format(url, self._cargoson_get_headers(), json_data)
            self.log_xml(log_request, path)

            response = requests.post(url, json_data, json=True, headers=self._cargoson_get_headers())
            logger.info('response for cargoson_api_post: %s', response.text)
            log_response = 'URL: {}\nSTATUS:{}\n\n{}\n'.format(url, response.status_code, response.text)
            self.log_xml(log_response, path)
            logger.info(log_response)

            data = response.json()
            if schema_class is None:
                return data
            return schema_class.from_dict(data)
        except Exception as err:
            logger.error(err)
            self.log_xml('URL: {}\nERROR: {}\n\n{}\n'.format(url, err, traceback.format_exc()), path)

    def cargoson_api_delete(self, path, schema_class=None):
        self.ensure_one()
        url = self._cargoson_get_api_url(path)
        try:
            log_request = 'DELETE: {}\nHEADERS: {}\n\n'.format(url, self._cargoson_get_headers())
            self.log_xml(log_request, path)

            response = requests.delete(url, json=True, headers=self._cargoson_get_headers())
            log_response = 'URL: {}\n\n{}\n'.format(url, response.text)
            self.log_xml(log_response, path)

            data = response.json()
            if schema_class is None:
                return data
            return schema_class.from_dict(data)
        except Exception as err:
            logger.error(err)
            self.log_xml('URL: {}\nERROR: {}\n\n{}\n'.format(url, err, traceback.format_exc()), path)

    def _cargoson_get_api_url(self, path):
        return urljoin(self._cargoson_get_api_base_url(), path)

    def _cargoson_get_api_base_url(self):
        self.ensure_one()
        url = self.cargoson_api_url if self.prod_environment else self.cargoson_test_api_url
        if not url.endswith('/'):
            url += '/'
        return url

    def _cargoson_get_headers(self):
        self.ensure_one()
        token = self.cargoson_api_key if self.prod_environment else self.cargoson_test_api_key
        if not token:
            raise UserError(_('Cargoson API key not configured'))

        headers = {
            'Content-Type': 'application/json;charset=utf-8',
            'Accept': 'application/json',
            'Authorization': 'Token {0}'.format(token)
        }

        return headers

    def _cargoson_convert_weight(self, weight):
        weight_uom_id = self.env['product.template']._get_weight_uom_id_from_ir_config_parameter()
        return weight_uom_id._compute_quantity(weight, self.env.ref('uom.product_uom_kgm'), round=False)

    def _cargoson_validate_address(self, partner_id):
        if not partner_id.zip:
            raise UserError(_('Contact "%s" must have a ZIP code', partner_id.name))
        if not partner_id.country_id:
            raise UserError(_('Contact "%s" must have a country', partner_id.name))
        if not partner_id.phone and not partner_id.mobile:
            raise UserError(_('Contact "%s" must have a phone number', partner_id.name))
        return True

    def action_cargoson_queue(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'cargoson.queue.task',
            'view_id': self.env.ref('delivery_cargoson.view_cargoson_queue_task_tree').id,
            'view_mode': 'list',
            'target': 'current',
            'name': _('Cargoson Queue'),
            'domain': [],
        }

    # def action_cargoson_event_log(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'cargoson.log',
    #         'view_id': self.env.ref('delivery_cargoson.view_cargoson_log_tree').id,
    #         'view_mode': 'list',
    #         'target': 'current',
    #         'name': _('Cargoson Event Log'),
    #         'domain': [],
    #     }

    PREDEFINED_PACKAGE_DIMENSIONS = {
        'EUR': {'width': 120, 'depth': 80},
        'FIN': {'width': 120, 'depth': 100},
        'HPL': {'width': 80, 'depth': 60},
    }

    @staticmethod
    def get_package_dimensions(package_type):
        return ProviderCargoson.PREDEFINED_PACKAGE_DIMENSIONS.get(package_type, {'width': 0, 'depth': 0})

    def _cargoson_get_self_service_url(self, path):
        base_url = self._cargoson_get_api_base_url()
        if base_url.endswith('/api'):
            base_url = base_url[:-3]
        if not base_url.endswith('/'):
            base_url += '/'
        logger.info('_cargoson_get_self_service_url: %s', urljoin(base_url, path))
        return urljoin(base_url, path)
