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
    OrderDocuments_AttributesItem
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

    cargoson_parcel_machine_country_ids = fields.Many2many(
        'res.country',
        'delivery_carrier_cargoson_country_rel', 'carrier_id', 'country_id',
        'Enabled parcel machine regions')

    def cargoson_rate_shipment(self, order):
        collection_address = order.get_cargoson_collection_address()
        delivery_address = order.get_cargoson_delivery_address()

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

        weight = self._cargoson_convert_weight(order._get_estimated_weight())
        logger.info('Cargoson: rate shipment for: %s (weight=%s)', order.name, weight)

        package = PriceRequestShipmentRows_AttributesItem(
            weight=math.ceil(weight),
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
        logger.info('!!!! cargoson_cancel_shipment')
        raise NotImplementedError()

    def _cargoson_send_shipping(self, picking):
        if not picking.cargoson_shipping_options_id:
            return

        collection_address = picking.get_cargoson_collection_address()
        delivery_address = picking.get_cargoson_delivery_address()
        self._cargoson_validate_address(collection_address)
        self._cargoson_validate_address(delivery_address)

        weight = self._cargoson_convert_weight(picking.shipping_weight)
        opts = picking.cargoson_shipping_options_id

        logger.info('Cargoson: send shipment for: %s (weight=%s)', picking.name, weight)
        logger.info(opts)

        package = OrderRows_AttributesItem(
            weight=math.ceil(weight),
            package_type=OrderRows_AttributesItemPackage_Type.from_dict(opts.package_type),
            quantity=opts.package_qty,
            description='Goods with {} package'.format(opts.package_type)
        )
        # TODO: add optional adr rows to package

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

            # documents_attributes=[],

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

        logger.info('request = %s', order.as_dict())
        result = self.cargoson_api_post('queries', order.as_dict())  # FIXME: obtain result schema from vendor
        logger.info('response = %s', result)

        if (
            not isinstance(result, dict) or
            not bool(result.get('reference')) or
            len(result.get('errors', list())) > 0 or
            result.get('query_status') != 'created' or
            result.get('booking_status') != 'created'
        ):
            # TODO: log error in cargoson.log
            raise UserError(_('Failed to create direct booking for courier service "%s"', opts.selected_carrier_name))

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

        # update booking data immediately
        cargoson_shipping.update_booking_data()

        self.env['cargoson.queue.task'].sudo().create({
            'name': 'Fetch booking data',
            'res_id': cargoson_shipping.id,
            'res_name': 'cargoson.shipping',
            'method': 'update_booking_data',
        })

        self.env['cargoson.queue.task'].sudo().create({
            'name': 'Fetch label PDF',
            'res_id': cargoson_shipping.id,
            'res_name': 'cargoson.shipping',
            'method': 'fetch_label',
        })

        return [{
            'exact_price': opts.selected_price,

            # NOTE: this returns the cargoson reference if the actual tracking number is not yet available
            'tracking_number': cargoson_shipping.tracking_code or cargoson_ref
        }]

    def cargoson_api_get(self, path, params, schema_class=None):
        self.ensure_one()
        url = self._cargoson_get_api_url(path)
        try:
            log_request = 'URL: {}\nHEADERS: {}\n\n{}\n'.format(url, self._cargoson_get_headers(), json.dumps(params))
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
            log_request = 'URL: {}\nHEADERS: {}\n\n{}\n'.format(url, self._cargoson_get_headers(), json_data)
            self.log_xml(log_request, path)

            # logger.info('CARGOSON POST: %s', json.dumps(data, indent=4))
            response = requests.post(url, json_data, json=True, headers=self._cargoson_get_headers())

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
