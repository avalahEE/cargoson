from odoo import fields, models, api, _
import logging
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
        ], string='Package type')
    package_qty = fields.Integer('Package quantity', default=1)

    selected_carrier_name = fields.Char('Carrier name')
    selected_carrier_id = fields.Integer('Carrier ID')
    selected_service_id = fields.Integer('Service ID')
    selected_price = fields.Monetary('Price')
