from odoo import fields, models, api, _
from odoo.exceptions import UserError
import logging
logger = logging.getLogger(__name__)


class ChooseDeliveryCarrier(models.TransientModel):
    _inherit = 'choose.delivery.carrier'

    cargoson_collection_date = fields.Date('Collection date')
    cargoson_frigo = fields.Boolean('Goods are temperature sensitive')
    cargoson_adr = fields.Boolean('Shipment is hazardous (ADR)')
    cargoson_collection_prenotification = fields.Boolean('Call the collection contact before loading')
    cargoson_collection_with_tail_lift = fields.Boolean('Collection should be performed with a tail-lift truck')
    cargoson_delivery_prenotification = fields.Boolean('Call the delivery contact before loading')
    cargoson_delivery_with_tail_lift = fields.Boolean('Delivery should be performed with a tail-lift truck')
    cargoson_delivery_return_document = fields.Boolean('Customer expects signed documents to be returned')
    cargoson_delivery_to_private_person = fields.Boolean(
        'Delivery contact is a private person',
        help='Indicates whether the goods will be delivered to a private person instead of a company')

    cargoson_package_type = fields.Selection([
        ('EUR', 'EUR'),
        ('CTN', 'CTN'),
        ('FIN', 'FIN'),
        ('HPL', 'HPL'),
        ('QPL', 'QPL'),
        ('LOAD', 'LOAD'),
        ('PLD', 'PLD'),
        ('PXL', 'PXL'),
        ('PLL', 'PLL'),
        ('TBE', 'TBE'),
        ('CLL', 'CLL'),
        ('RLL', 'RLL'),
        ('20DC', '20DC'),
        ('40DC', '40DC'),
        ('40HC', '40HC'),
    ], string='Package type', default='EUR')
    cargoson_package_qty = fields.Integer('Package quantity', default=1)

    cargoson_rate_results = fields.One2many('cargoson.rate.result', 'choose_delivery_carrier_id', 'Available rates')
    cargoson_selected_carrier_name = fields.Char('Selected carrier')
    cargoson_selected_carrier_id = fields.Integer('Selected carrier ID')
    cargoson_selected_service_id = fields.Integer('Selected service ID')
    cargoson_selected_price = fields.Monetary('Selected price')

    def get_cargoson_options(self):
        self.ensure_one()
        return dict(
            cargoson_collection_date=self.cargoson_collection_date,
            cargoson_frigo=self.cargoson_frigo,
            cargoson_adr=self.cargoson_adr,
            cargoson_collection_prenotification=self.cargoson_collection_prenotification,
            cargoson_collection_with_tail_lift=self.cargoson_collection_with_tail_lift,
            cargoson_delivery_prenotification=self.cargoson_delivery_prenotification,
            cargoson_delivery_with_tail_lift=self.cargoson_delivery_with_tail_lift,
            cargoson_delivery_return_document=self.cargoson_delivery_return_document,
            cargoson_delivery_to_private_person=self.cargoson_delivery_to_private_person,
            cargoson_package_type=self.cargoson_package_type,
            cargoson_package_qty=self.cargoson_package_qty,
        )

    def _get_shipment_rate(self):
        if self.delivery_type != 'cargoson' or not self.id:
            return super()._get_shipment_rate()  # noqa

        vals = self.with_context(**self.get_cargoson_options()).carrier_id.rate_shipment(self.order_id)
        if not vals.get('success'):
            return {'error_message': vals['error_message']}

        # NOTE: this should be kept up-to-date with upstream logic
        self.delivery_message = vals.get('warning_message', False)
        self.delivery_price = vals['price']
        self.display_price = vals['carrier_price']
        self.write({'cargoson_rate_results': [(5, 0, 0)]})

        available_prices = vals.get('cargoson')
        if not available_prices:
            return {'error_message': _('Could not fetch any prices from Cargoson')}

        # noinspection PyPep8Naming
        CargosonAvailablePrice = self.env['cargoson.rate.result']
        prices = list()
        for item in available_prices.object.prices:
            prices.append(CargosonAvailablePrice.from_cargoson(self.id, item))
        CargosonAvailablePrice.create(prices)
        return {}

    def button_confirm(self):
        res = super().button_confirm()

        # update selected values on SaleOrder
        vals = self.get_cargoson_options()
        vals.update({
            'cargoson_selected_carrier_name': self.cargoson_selected_carrier_name,
            'cargoson_selected_carrier_id': self.cargoson_selected_carrier_id,
            'cargoson_selected_service_id': self.cargoson_selected_service_id,
            'cargoson_selected_price': self.cargoson_selected_price,
        })
        self.order_id.write(vals)

        # no reason to keep the transient data around
        self.env['cargoson.rate.result'].search([
            '|',
            ('choose_delivery_carrier_id', '=', self.id),
            ('choose_delivery_carrier_id', '=', False)
        ]).unlink()
        return res
