from odoo import models, fields, _

import logging
logger = logging.getLogger(__name__)


# noinspection PyProtectedMember
class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def send_to_shipper(self):
        self.ensure_one()

        if not self.carrier_id or self.carrier_id.delivery_type != 'cargoson':
            return super().send_to_shipper()

        # TODO: populate cargoson options from sale_id if it exists, otherwise launch a wizard

        # If we have a previously configured shipment on sale.order - use the default flow
        logger.info('send to shipper: sale_id=%s', self.sale_id)
        super().send_to_shipper()

        # for record in self:
        #     # TODO: log additional data from cargoson into chatter
        #     pass

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
