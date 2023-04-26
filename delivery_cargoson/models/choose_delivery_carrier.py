from odoo import fields, models, api, _
from odoo.exceptions import UserError
import logging
logger = logging.getLogger(__name__)


# noinspection PyProtectedMember,DuplicatedCode
class ChooseDeliveryCarrier(models.TransientModel):
    _inherit = 'choose.delivery.carrier'

    cargoson_collection_date = fields.Date('Collection date', default=fields.Datetime.now)
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

    cargoson_selected_carrier_name = fields.Char('Selected carrier')
    cargoson_selected_carrier_id = fields.Integer('Selected carrier ID')
    cargoson_selected_service_id = fields.Integer('Selected service ID')
    cargoson_selected_price = fields.Monetary('Selected price')

    cargoson_collection_address = fields.Many2one('res.partner', 'Collection address', compute='_compute_addresses')
    cargoson_delivery_address = fields.Many2one('res.partner', 'Delivery address', compute='_compute_addresses')

    cargoson_show_rates = fields.Boolean('Show rates (technical field)')
    cargoson_rate_results = fields.One2many('cargoson.rate.result', 'choose_delivery_carrier_id', 'Available rates')

    @api.onchange(
        'cargoson_collection_date',
        'cargoson_frigo',
        'cargoson_adr',
        'cargoson_collection_prenotification',
        'cargoson_collection_with_tail_lift',
        'cargoson_delivery_prenotification',
        'cargoson_delivery_with_tail_lift',
        'cargoson_delivery_return_document',
        'cargoson_delivery_to_private_person',
        'cargoson_package_type',
        'cargoson_package_qty',
    )
    def _cargoson_on_options_changed(self):
        self.write({
            'cargoson_selected_carrier_name': None,
            'cargoson_selected_carrier_id': None,
            'cargoson_selected_service_id': None,
            'cargoson_selected_price': None,
            'cargoson_show_rates': False,
        })

    @api.depends('order_id')
    def _compute_addresses(self):
        for record in self:
            record.cargoson_collection_address = record.order_id.get_cargoson_collection_address()
            record.cargoson_delivery_address = record.order_id.get_cargoson_delivery_address()

    def get_cargoson_options(self):
        self.ensure_one()
        return dict(
            collection_date=self.cargoson_collection_date,
            frigo=self.cargoson_frigo,
            adr=self.cargoson_adr,
            collection_prenotification=self.cargoson_collection_prenotification,
            collection_with_tail_lift=self.cargoson_collection_with_tail_lift,
            delivery_prenotification=self.cargoson_delivery_prenotification,
            delivery_with_tail_lift=self.cargoson_delivery_with_tail_lift,
            delivery_return_document=self.cargoson_delivery_return_document,
            delivery_to_private_person=self.cargoson_delivery_to_private_person,
            package_type=self.cargoson_package_type,
            package_qty=self.cargoson_package_qty,
            selected_carrier_name=self.cargoson_selected_carrier_name,
            selected_carrier_id=self.cargoson_selected_carrier_id,
            selected_service_id=self.cargoson_selected_service_id,
            selected_price=self.cargoson_selected_price,
        )

    def _get_shipment_rate(self):
        if self.delivery_type != 'cargoson' or not self.id:
            return super()._get_shipment_rate()

        logger.info('Cargoson rate wizard: %s', self.id)

        vals = self.with_context(cargoson=self.get_cargoson_options()).carrier_id.rate_shipment(self.order_id)
        if not vals.get('success'):
            return {'error_message': vals['error_message']}

        # NOTE: this should be kept up-to-date with upstream logic
        self.delivery_message = vals.get('warning_message', False)
        self.delivery_price = vals['price']
        self.display_price = vals['carrier_price']
        # ########################################################

        available_prices = vals.get('cargoson')
        if not available_prices:
            return {'error_message': _('Could not fetch any prices from Cargoson')}

        self._cargoson_clear_available_prices()

        # noinspection PyPep8Naming
        CargosonAvailablePrice = self.env['cargoson.rate.result']
        prices = list()
        for item in available_prices.object.prices:
            prices.append(CargosonAvailablePrice.from_cargoson(item, delivery_wizard_id=self.id))
        CargosonAvailablePrice.create(prices)
        return {}

    def button_confirm(self):
        if self.delivery_type != 'cargoson':
            return super().button_confirm()

        if not self.cargoson_selected_carrier_id:
            raise UserError(_('Please select a carrier first'))

        if self.order_id.cargoson_shipping_options_id:
            self.order_id.cargoson_shipping_options_id.sudo().unlink()

        res = super().button_confirm()

        # store selected shipping options
        vals = self.get_cargoson_options()
        vals.update(dict(sale_order_id=self.order_id.id))
        cargoson_options = self.env['cargoson.shipping.options'].sudo().create(vals)
        self.order_id.write(dict(cargoson_shipping_options_id=cargoson_options.id))
        self.order_id.message_post(body=_(
            'Cargoson shipping added: by %s priced at %s %s',
            cargoson_options.selected_carrier_name,
            cargoson_options.selected_price,
            cargoson_options.currency_id.symbol
        ))

        # no reason to keep the transient data around
        self.env['cargoson.rate.result'].search([
            '|',
            ('choose_delivery_carrier_id', '=', self.id),
            ('choose_delivery_carrier_id', '=', False)
        ]).unlink()
        return res

    def _cargoson_clear_available_prices(self):
        self.ensure_one()
        self.cargoson_show_rates = True
        if self.cargoson_rate_results:
            self.env['cargoson.rate.result'].browse(self.cargoson_rate_results.ids).unlink()
