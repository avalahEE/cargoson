from odoo import _, api, fields, models
from odoo.exceptions import UserError
from .delivery_carrier import ProviderCargoson
import logging
logger = logging.getLogger(__name__)


# noinspection DuplicatedCode,PyProtectedMember
class CargosonShippingWizard(models.TransientModel):
    _name = 'cargoson.shipping.wizard'
    _description = 'Cargoson Shipping Wizard'

    picking_id = fields.Many2one('stock.picking', required=True)
    carrier_id = fields.Many2one('delivery.carrier', required=True)

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
            ('EUR', 'EUR pll (120x80cm)'),
            ('CTN', 'Carton (package)'),
            ('FIN', 'FIN pll (120x100cm)'),
            ('HPL', 'HPL (80x60cm)'),
            ('QPL', 'QPL (60x40cm)'),
            ('LOAD', 'Full load'),
            ('PLD', 'Part load'),
            ('PXL', 'Large pallet'),
            ('PLL', 'Pallet'),
            ('TBE', 'Tube'),
            ('CLL', 'CLL'),
            ('RLL', 'Roll'),
            ('20DC', '20\' Dry Container'),
            ('40DC', '40\' Dry Container'),
            ('40HC', '40\' High Cube'),
        ], string='Package type', default='EUR')
    cargoson_package_qty = fields.Integer('Package quantity', default=1)

    cargoson_selected_carrier_name = fields.Char('Selected carrier')
    cargoson_selected_carrier_id = fields.Integer('Selected carrier ID')
    cargoson_selected_service_id = fields.Integer('Selected service ID')
    cargoson_selected_price = fields.Monetary('Selected price')
    currency_id = fields.Many2one('res.currency', related='picking_id.cargoson_currency_id')

    cargoson_collection_address = fields.Many2one('res.partner', 'Collection address', compute='_compute_addresses')
    cargoson_delivery_address = fields.Many2one('res.partner', 'Delivery address', compute='_compute_addresses')

    cargoson_show_rates = fields.Boolean('Show rates (technical field)')
    cargoson_rate_results = fields.One2many(
        'cargoson.shipping.wizard.rate.result', 'cargoson_shipping_wizard_id', 'Available rates')

    width = fields.Float(compute="_onchange_cargoson_package_type", required=False)
    height = fields.Float(required=False)
    depth = fields.Float(compute="_onchange_cargoson_package_type", required=False)

    is_fixed_width = fields.Boolean(compute='_compute_fixed_dimensions')
    is_fixed_height = fields.Boolean(compute='_compute_fixed_dimensions')
    is_fixed_depth = fields.Boolean(compute='_compute_fixed_dimensions')

    @api.depends('picking_id')
    def _compute_addresses(self):
        for record in self:
            record.cargoson_collection_address = record.picking_id.get_cargoson_collection_address()
            record.cargoson_delivery_address = record.picking_id.get_cargoson_delivery_address()

    def action_add_shipping(self):
        self.ensure_one()
        vals = self.get_cargoson_options()
        vals.update(dict(picking_id=self.picking_id.id))
        cargoson_options = self.env['cargoson.shipping.options'].sudo().create(vals)
        self.picking_id.write(dict(cargoson_shipping_options_id=cargoson_options.id))
        self.picking_id.message_post(body=_(
            'Cargoson shipping added: by %s priced at %s %s',
            cargoson_options.selected_carrier_name,
            cargoson_options.selected_price,
            cargoson_options.currency_id.symbol
        ))

    def action_get_rates(self):
        if self.picking_id.shipping_weight <= 0:
            raise UserError(_(
                'The combined weight of the shipment must be greater than zero. '
                'Are all the transfer lines marked as done?'))

        vals = self.with_context(cargoson=self.get_cargoson_options()).carrier_id._cargoson_rate_shipment(
            self.picking_id.name,
            self.picking_id.get_cargoson_collection_address(),
            self.picking_id.get_cargoson_delivery_address(),
            self.picking_id.shipping_weight)

        if vals.get('error_message'):
            raise UserError(vals.get('error_message'))

        available_prices = vals.get('cargoson')
        if not available_prices:
            raise UserError(_('Could not fetch any prices from Cargoson'))

        self._cargoson_clear_available_prices()

        # noinspection PyPep8Naming
        CargosonAvailablePriceShippingWizard = self.env['cargoson.shipping.wizard.rate.result']
        prices = list()
        for item in available_prices.object.prices:
            prices.append(CargosonAvailablePriceShippingWizard.from_cargoson(item, shipping_wizard_id=self.id))
        CargosonAvailablePriceShippingWizard.create(prices)

        return {
            'name': _('Select a courier service'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'cargoson.shipping.wizard',
            'res_id': self.id,
            'target': 'new',
        }

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

    def _cargoson_clear_available_prices(self):
        self.ensure_one()
        self.cargoson_show_rates = True
        if self.cargoson_rate_results:
            self.env['cargoson.rate.result'].browse(self.cargoson_rate_results.ids).unlink()

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

    @api.onchange('cargoson_package_type')
    @api.depends('cargoson_package_type')
    def _onchange_cargoson_package_type(self):
        package_dimensions = ProviderCargoson.get_package_dimensions(self.cargoson_package_type)
        self.width = package_dimensions.get('width', 0)
        self.depth = package_dimensions.get('depth', 0)

    @api.depends('cargoson_package_type')
    def _compute_fixed_dimensions(self):
        package_dimensions = ProviderCargoson.get_package_dimensions(self.cargoson_package_type)
        self.is_fixed_width = package_dimensions.get('width', 0) != 0
        self.is_fixed_height = False  # As height was not specified in predefined dimensions
        self.is_fixed_depth = package_dimensions.get('depth', 0) != 0
