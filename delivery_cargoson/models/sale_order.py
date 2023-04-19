from odoo import models, fields, api

import logging
logger = logging.getLogger(__name__)


# noinspection DuplicatedCode,PyProtectedMember
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    cargoson_collection_date = fields.Date('Collection date', related='cargoson_shipping_options_id.collection_date')

    cargoson_frigo = fields.Boolean('Goods are temperature sensitive', related='cargoson_shipping_options_id.frigo')
    cargoson_adr = fields.Boolean('Shipment is hazardous (ADR)', related='cargoson_shipping_options_id.adr')
    cargoson_collection_prenotification = fields.Boolean('Call the collection contact before loading', related='cargoson_shipping_options_id.collection_prenotification')
    cargoson_collection_with_tail_lift = fields.Boolean('Collection should be performed with a tail-lift truck', related='cargoson_shipping_options_id.collection_with_tail_lift')
    cargoson_delivery_prenotification = fields.Boolean('Call the delivery contact before loading', related='cargoson_shipping_options_id.delivery_prenotification')
    cargoson_delivery_with_tail_lift = fields.Boolean('Delivery should be performed with a tail-lift truck', related='cargoson_shipping_options_id.delivery_with_tail_lift')
    cargoson_delivery_return_document = fields.Boolean('Customer expects signed documents to be returned', related='cargoson_shipping_options_id.delivery_return_document')
    cargoson_delivery_to_private_person = fields.Boolean(
        'Delivery contact is a private person',
        related='cargoson_shipping_options_id.delivery_to_private_person',
        help='Indicates whether the goods will be delivered to a private person instead of a company')

    cargoson_package_type = fields.Selection(string='Package type', related='cargoson_shipping_options_id.package_type')
    cargoson_package_qty = fields.Integer('Package quantity', default=1, related='cargoson_shipping_options_id.package_qty')

    cargoson_selected_carrier_id = fields.Integer('Carrier ID', related='cargoson_shipping_options_id.selected_carrier_id')
    cargoson_selected_carrier_name = fields.Char('Carrier name', related='cargoson_shipping_options_id.selected_carrier_name')
    cargoson_selected_service_id = fields.Integer('Service ID', related='cargoson_shipping_options_id.selected_service_id')
    cargoson_selected_price = fields.Monetary('Price', related='cargoson_shipping_options_id.selected_price')

    cargoson_shipping_options_id = fields.Many2one('cargoson.shipping.options')
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
            record.cargoson_shipping_options_id.unlink()

    def _remove_delivery_line(self):
        super()._remove_delivery_line()
        self._cargoson_reset_options()
