from odoo import models, fields, api

import logging
logger = logging.getLogger(__name__)


# noinspection DuplicatedCode,PyProtectedMember
class SaleOrder(models.Model):
    _inherit = 'sale.order'

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
    ], string='Package type')
    cargoson_package_qty = fields.Integer('Package quantity', default=1)

    cargoson_selected_carrier_name = fields.Char('Carrier name')
    cargoson_selected_carrier_id = fields.Integer('Carrier ID')
    cargoson_selected_service_id = fields.Integer('Service ID')
    cargoson_selected_price = fields.Monetary('Price')

    cargoson_collection_address = fields.Many2one('res.partner', 'Collection address', compute='_compute_addresses')
    cargoson_delivery_address = fields.Many2one('res.partner', 'Delivery address', compute='_compute_addresses')

    @api.depends('cargoson_selected_carrier_id')
    def _compute_addresses(self):
        for record in self:
            record.cargoson_collection_address = record.get_cargoson_collection_address()
            record.cargoson_delivery_address = record.get_cargoson_delivery_address()

    @api.depends('order_line')
    def _compute_delivery_state(self):
        super()._compute_delivery_state()
        for record in self:
            if not record.delivery_set:
                record._cargoson_reset_options()

    def get_cargoson_collection_address(self):
        self.ensure_one()
        if hasattr(self, 'warehouse_id'):
            return self.warehouse_id.partner_id
        else:
            return self.company_id.partner_id

    def get_cargoson_delivery_address(self):
        self.ensure_one()
        return self.partner_shipping_id

    def _cargoson_reset_options(self):
        for record in self:
            record.write({
                'cargoson_collection_date': False,
                'cargoson_frigo': False,
                'cargoson_adr': False,
                'cargoson_collection_prenotification': False,
                'cargoson_collection_with_tail_lift': False,
                'cargoson_delivery_prenotification': False,
                'cargoson_delivery_with_tail_lift': False,
                'cargoson_delivery_return_document': False,
                'cargoson_delivery_to_private_person': False,
                'cargoson_package_type': False,
                'cargoson_package_qty': False,
                'cargoson_selected_carrier_name': False,
                'cargoson_selected_carrier_id': False,
                'cargoson_selected_service_id': False,
                'cargoson_selected_price': False,
            })

    def _remove_delivery_line(self):
        super()._remove_delivery_line()
        self._cargoson_reset_options()
