from odoo import models, fields, _
from odoo.exceptions import UserError

import logging
logger = logging.getLogger(__name__)


# noinspection PyProtectedMember
class StockPicking(models.Model):
    _inherit = 'stock.picking'

    cargoson_shipping_options_id = fields.Many2one('cargoson.shipping.options')

    def send_to_shipper(self):
        self.ensure_one()

        if not self.carrier_id or self.carrier_id.delivery_type != 'cargoson':
            return super().send_to_shipper()

        # Cargoson shipping options configured - continue the regular Delivery Carrier flow
        if self.cargoson_shipping_options_id:
            return super().send_to_shipper()

        logger.info('self.sale_id = %s', self.sale_id)
        logger.info('self.sale_id.cargoson_shipping_options_id = %s', self.sale_id.cargoson_shipping_options_id)

        if self.sale_id and self.sale_id.delivery_set and self.sale_id.cargoson_shipping_options_id:
            self.sale_id.cargoson_shipping_options_id.write({
                'picking_id': self.id,
            })
            self.write({
                'cargoson_shipping_options_id': self.sale_id.cargoson_shipping_options_id.id,
            })
        else:
            # TODO: launch shipping wizard
            raise UserError(_('Not implemented yet'))

        # If we have a previously configured shipment on sale.order - use the default flow
        logger.info('send to shipper: sale_id=%s', self.sale_id)
        super().send_to_shipper()

        # TODO: log additional data from cargoson into chatter

    def _pre_action_done_hook(self):
        if self.env.context.get('skip_cargoson_shipping_wizard'):
            return True

        res = super()._pre_action_done_hook()
        if res is not True:
            return res

        needs_input = self.browse()
        for picking in self:
            if picking.carrier_id and picking.carrier_id.delivery_type == 'cargoson' and not picking.sale_id:
                needs_input |= picking

        if len(needs_input) > 0:
            return needs_input._action_generate_cargoson_shipping_wizard()
        return True

    def _action_generate_cargoson_shipping_wizard(self):
        view = self.env.ref('delivery_cargoson.view_cargoson_shipping_wizard')
        return {
            'name': _('Add a shipping method'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'cargoson.shipping.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': dict(self.env.context, default_pick_ids=[(4, p.id) for p in self]),
        }

    def get_cargoson_collection_address(self):
        self.ensure_one()
        return self.picking_type_id.warehouse_id.partner_id

    def get_cargoson_delivery_address(self):
        self.ensure_one()
        return self.partner_id
