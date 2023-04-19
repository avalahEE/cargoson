from odoo import models, fields, api, _
from odoo.exceptions import UserError
from urllib.parse import urljoin
from .schema import AvailablePrices, PriceRequestShipment, Order
from .schema.price_request_shipment import (
    PriceRequestShipmentRows_AttributesItem,
    PriceRequestShipmentRows_AttributesItemPackage_Type
)

import json
import math
import requests
import traceback
import logging
logger = logging.getLogger(__name__)


# noinspection PyProtectedMember
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

    # TODO
    # cargoson_send_shipping - Send the package to the service provider - POST /queries
    # cargoson_get_tracking_link - Ask the tracking link to the service provider
    # cargoson_cancel_shipment - Cancel a shipment
    #
    # Some delivery carriers require a prefix to be sent in order to use custom
    # packages (ie not official ones). This optional method will return it as a string.
    # _cargoson_get_default_custom_package_code

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

        if not collection_address.zip:
            raise UserError(_('Collection contact must have a ZIP code'))
        if not collection_address.country_id:
            raise UserError(_('Collection contact must have a country'))

        if not delivery_address.zip:
            raise UserError(_('Selected delivery contact must have a ZIP code'))
        if not delivery_address.country_id:
            raise UserError(_('Selected delivery contact must have a country'))

        cargoson_options = self.env.context.get('cargoson', dict())

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
        for picking in pickings:
            self._cargoson_send_shipping(picking)

        res = []
        for picking in pickings:
            res = res + [{'exact_price': picking.carrier_id.fixed_price,
                          'tracking_number': False}]
        return res

    def cargoson_get_tracking_link(self, picking):
        logger.info('!!!! cargoson_get_tracking_link')
        return False

    def cargoson_cancel_shipment(self, pickings):
        logger.info('!!!! cargoson_cancel_shipment')
        raise NotImplementedError()

    def _cargoson_send_shipping(self, picking):
        sale_order = picking.sale_id
        if not sale_order:
            raise UserError(_('Cannot send %s with this method - missing Sale Order reference', picking.name))

        collection_address = sale_order.get_cargoson_collection_address()
        delivery_address = sale_order.get_cargoson_delivery_address()
        weight = self._cargoson_convert_weight(picking.shipping_weight)
        logger.info('Cargoson: send shipment for: %s (weight=%s)', picking.name, weight)

        # TODO
        # order = Order(
        #     collection_date=sale_order.cargoson_collection_date.isoformat(),
        #     collection_postcode=collection_address.zip,
        #     collection_country=collection_address.country_id.code,
        #     delivery_postcode=delivery_address.zip,
        #     delivery_country=delivery_address.country_id.code,
        #     collection_with_tail_lift=sale_order.cargoson_collection_with_tail_lift,
        #     collection_prenotification=sale_order.cargoson_collection_prenotification,
        #     delivery_with_tail_lift=sale_order.cargoson_delivery_with_tail_lift,
        #     delivery_prenotification=sale_order.cargoson_delivery_prenotification,
        #     delivery_return_document=sale_order.cargoson_delivery_return_document,
        #     delivery_to_private_person=sale_order.cargoson_delivery_to_private_person,
        #     frigo=sale_order.cargoson_frigo,
        #     # adr=sale_order.cargoson_adr,
        #     rows_attributes=[]
        # )

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
