from odoo import models, fields, api, _
from odoo.exceptions import UserError

import logging
logger = logging.getLogger(__name__)


# noinspection PyProtectedMember
class StockPicking(models.Model):
    _inherit = 'stock.picking'

    cargoson_shipping_options_id = fields.Many2one('cargoson.shipping.options')
    cargoson_shipping_id = fields.Many2one('cargoson.shipping')

    cargoson_reference = fields.Char(related='cargoson_shipping_id.reference')
    cargoson_tracking_url = fields.Text('Cargoson Tracking', related='cargoson_shipping_id.tracking_url')
    cargoson_tracking_code = fields.Char(related='cargoson_shipping_id.tracking_code')
    cargoson_label_url = fields.Text(related='cargoson_shipping_id.label_url')
    cargoson_label_fetched = fields.Datetime(related='cargoson_shipping_id.label_fetched')
    cargoson_label_pdf = fields.Binary(related='cargoson_shipping_id.label_pdf')
    cargoson_status = fields.Selection(related='cargoson_shipping_id.status')

    cargoson_collection_date = fields.Date(related='cargoson_shipping_options_id.collection_date')

    cargoson_frigo = fields.Boolean(related='cargoson_shipping_options_id.frigo')
    cargoson_adr = fields.Boolean(related='cargoson_shipping_options_id.adr')
    cargoson_collection_prenotification = fields.Boolean(related='cargoson_shipping_options_id.collection_prenotification')
    cargoson_collection_with_tail_lift = fields.Boolean(related='cargoson_shipping_options_id.collection_with_tail_lift')
    cargoson_delivery_prenotification = fields.Boolean(related='cargoson_shipping_options_id.delivery_prenotification')
    cargoson_delivery_with_tail_lift = fields.Boolean(related='cargoson_shipping_options_id.delivery_with_tail_lift')
    cargoson_delivery_return_document = fields.Boolean(related='cargoson_shipping_options_id.delivery_return_document')
    cargoson_delivery_to_private_person = fields.Boolean(
        related='cargoson_shipping_options_id.delivery_to_private_person',
        help='Indicates whether the goods will be delivered to a private person instead of a company')

    cargoson_package_type = fields.Selection(related='cargoson_shipping_options_id.package_type')
    cargoson_package_qty = fields.Integer(related='cargoson_shipping_options_id.package_qty')
    cargoson_selected_carrier_id = fields.Integer(related='cargoson_shipping_options_id.selected_carrier_id')
    cargoson_selected_carrier_name = fields.Char(related='cargoson_shipping_options_id.selected_carrier_name')
    cargoson_selected_service_id = fields.Integer(related='cargoson_shipping_options_id.selected_service_id')
    cargoson_selected_price = fields.Monetary(
        related='cargoson_shipping_options_id.selected_price', currency_field='cargoson_currency_id')
    cargoson_currency_id = fields.Many2one(related='cargoson_shipping_options_id.currency_id', readonly=True)

    cargoson_collection_address = fields.Many2one('res.partner', 'Collection address', compute='_compute_addresses')
    cargoson_delivery_address = fields.Many2one('res.partner', 'Delivery address', compute='_compute_addresses')

    @api.depends('cargoson_selected_carrier_id')
    def _compute_addresses(self):
        for record in self:
            record.cargoson_collection_address = record.get_cargoson_collection_address()
            record.cargoson_delivery_address = record.get_cargoson_delivery_address()

    def send_to_shipper(self):
        self.ensure_one()

        if not self.carrier_id or self.carrier_id.delivery_type != 'cargoson':
            return super().send_to_shipper()

        # Cargoson shipping options configured - continue the regular Delivery Carrier flow
        if self.cargoson_shipping_options_id:
            return super().send_to_shipper()

        if self.sale_id and self.sale_id.delivery_set and self.sale_id.cargoson_shipping_options_id:
            self.sale_id.cargoson_shipping_options_id.write({
                'picking_id': self.id,
            })
            self.write({
                'cargoson_shipping_options_id': self.sale_id.cargoson_shipping_options_id.id,
            })
        else:
            raise UserError(_(
                'Cargoson is set as the carrier for transfer %s.\n\n'
                'Please configure Cargoson parameters before validating.',
                self.name
            ))

        # If we have a previously configured shipment on sale.order - use the default flow
        super().send_to_shipper()

    # def _pre_action_done_hook(self):
    #     if self.env.context.get('skip_cargoson_shipping_wizard'):
    #         return True
    #
    #     res = super()._pre_action_done_hook()
    #     if res is not True:
    #         return res
    #
    #     if len(self) > 1:
    #         raise UserError(_('Cargoson shipping cannot be applied to multiple transfers at once'))
    #     # TODO: more complex user interface to handle multiple pickings at once
    #
    #     needs_input = self.browse()
    #     for picking in self:
    #         if (
    #             picking.carrier_id and picking.carrier_id.delivery_type == 'cargoson'
    #             and not picking.cargoson_shipping_options_id
    #         ):
    #             needs_input |= picking
    #
    #     if len(needs_input) > 0:
    #         return needs_input.action_cargoson_shipping_wizard()
    #     return True

    def action_cargoson_shipping_wizard(self):
        self.ensure_one()
        view = self.env.ref('delivery_cargoson.view_cargoson_shipping_wizard')
        return {
            'name': _('Add a shipping method'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'cargoson.shipping.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': dict(
                self.env.context,
                default_picking_id=self.id,
                default_carrier_id=self.carrier_id.id),
        }

    def get_cargoson_collection_address(self):
        self.ensure_one()
        return self.picking_type_id.warehouse_id.partner_id

    def get_cargoson_delivery_address(self):
        self.ensure_one()
        return self.partner_id
