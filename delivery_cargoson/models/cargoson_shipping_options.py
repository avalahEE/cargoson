from odoo import fields, models, api, _
import logging
from .delivery_carrier import ProviderCargoson
logger = logging.getLogger(__name__)


# noinspection DuplicatedCode
class CargosonShippingOptions(models.Model):
    _name = 'cargoson.shipping.options'
    _description = 'Cargoson shipping options'

    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company, required=True)
    currency_id = fields.Many2one(related='company_id.currency_id', readonly=True)

    # Set only if the options came from a sale.order
    sale_order_id = fields.Many2one('sale.order', 'Sale Order')

    # Set when options are assigned to stock.picking
    picking_id = fields.Many2one('stock.picking', 'Delivery Order')

    collection_date = fields.Date('Collection date')
    frigo = fields.Boolean('Goods are temperature sensitive')
    adr = fields.Boolean('Shipment is hazardous (ADR)')
    collection_prenotification = fields.Boolean('Call the collection contact before loading')
    collection_with_tail_lift = fields.Boolean('Collection should be performed with a tail-lift truck')
    delivery_prenotification = fields.Boolean('Call the delivery contact before loading')
    delivery_with_tail_lift = fields.Boolean('Delivery should be performed with a tail-lift truck')
    delivery_return_document = fields.Boolean('Customer expects signed documents to be returned')
    delivery_to_private_person = fields.Boolean(
        'Delivery contact is a private person',
        help='Indicates whether the goods will be delivered to a private person instead of a company')

    package_type = fields.Selection([
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
        ], string='Package type')
    package_qty = fields.Integer('Package quantity', default=1)

    selected_carrier_name = fields.Char('Carrier name')
    selected_carrier_id = fields.Integer('Carrier ID')
    selected_service_id = fields.Integer('Service ID')
    selected_price = fields.Monetary('Price')

    width = fields.Float(compute="_onchange_cargoson_package_type", required=False)
    height = fields.Float(required=False)
    depth = fields.Float(compute="_onchange_cargoson_package_type", required=False)

    is_fixed_width = fields.Boolean(compute='_compute_fixed_dimensions')
    is_fixed_height = fields.Boolean(compute='_compute_fixed_dimensions')
    is_fixed_depth = fields.Boolean(compute='_compute_fixed_dimensions')

    @api.onchange('package_type')
    @api.depends('package_type')
    def _onchange_cargoson_package_type(self):
        package_dimensions = ProviderCargoson.get_package_dimensions(self.package_type)
        self.width = package_dimensions.get('width', 0)
        self.depth = package_dimensions.get('depth', 0)

    @api.depends('package_type')
    def _compute_fixed_dimensions(self):
        package_dimensions = ProviderCargoson.get_package_dimensions(self.package_type)
        self.is_fixed_width = package_dimensions.get('width', 0) != 0
        self.is_fixed_height = False  # As height was not specified in predefined dimensions
        self.is_fixed_depth = package_dimensions.get('depth', 0) != 0
