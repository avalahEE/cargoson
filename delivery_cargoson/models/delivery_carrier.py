from odoo import models, fields, _
from odoo.exceptions import UserError
from urllib.parse import urljoin
from .schema import AvailablePrices, PriceRequestShipment
from .schema.price_request_shipment import PriceRequestShipmentRows_AttributesItem, PriceRequestShipmentRows_AttributesItemPackage_Type

import json
import math
import requests
import traceback
import logging
logger = logging.getLogger(__name__)


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

    # TODO
    # cargoson_send_shipping - Send the package to the service provider - POST /queries
    # cargoson_get_tracking_link - Ask the tracking link to the service provider
    # cargoson_cancel_shipment - Cancel a shipment
    #
    # Some delivery carriers require a prefix to be sent in order to use custom
    # packages (ie not official ones). This optional method will return it as a string.
    # _cargoson_get_default_custom_package_code

    def cargoson_rate_shipment(self, order):
        carrier = self._match_address(order.partner_shipping_id)
        if not carrier:
            return {
                'success': False,
                'price': 0.0,
                'error_message': _('Error: this delivery method is not available for this address.'),
                'warning_message': False
            }

        if not order.partner_shipping_id.zip:
            raise UserError(_("Selected delivery contact must have a ZIP code"))
        if not order.partner_shipping_id.country_id:
            raise UserError(_("Selected delivery contact must have a country"))

        package_type = self.env.context.get('cargoson_package_type')
        if not package_type:
            return {
                'success': False,
                'price': 0.0,
                'error_message': _("Package type is required"),
                'warning_message': _("Please select package type")
            }

        package_qty = self.env.context.get('cargoson_package_qty', 0)
        if package_qty < 1:
            return {
                'success': False,
                'price': 0.0,
                'error_message': _("Package quantity must be greater than 0"),
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

        collection_date = self.env.context.get('cargoson_collection_date')
        if not collection_date:
            collection_date = fields.Date.today()
        logger.info(repr(collection_date))

        price_request = PriceRequestShipment(
            collection_date=collection_date.isoformat(),
            collection_postcode='12345',  # TODO
            collection_country='EE',  # TODO
            delivery_postcode=order.partner_shipping_id.zip,
            delivery_country=order.partner_shipping_id.country_id.code,
            collection_with_tail_lift=self.env.context.get('cargoson_collection_with_tail_lift', False),
            collection_prenotification=self.env.context.get('cargoson_collection_prenotification', False),
            delivery_with_tail_lift=self.env.context.get('cargoson_delivery_with_tail_lift', False),
            delivery_prenotification=self.env.context.get('cargoson_delivery_prenotification', False),
            delivery_return_document=self.env.context.get('cargoson_delivery_return_document', False),
            delivery_to_private_person=self.env.context.get('cargoson_delivery_to_private_person', False),
            frigo=self.env.context.get('cargoson_frigo', False),
            adr=self.env.context.get('cargoson_adr', False),
            rows_attributes=[package]
        )
        result = self._cargoson_api_post('freightPrices/list', price_request.as_dict(), AvailablePrices)
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
        for p in pickings:
            res = res + [{'exact_price': p.carrier_id.fixed_price,
                          'tracking_number': False}]
        return res

    def cargoson_get_tracking_link(self, picking):
        return False

    def cargoson_cancel_shipment(self, pickings):
        raise NotImplementedError()

    # def _cargoson_api_get(self, path):
    #     pass

    def _cargoson_api_post(self, path, data, schema_class=None):
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

    # noinspection PyProtectedMember
    def _cargoson_convert_weight(self, weight):
        weight_uom_id = self.env['product.template']._get_weight_uom_id_from_ir_config_parameter()
        return weight_uom_id._compute_quantity(weight, self.env.ref('uom.product_uom_kgm'), round=False)
