from odoo import fields, models, api, _
import logging
logger = logging.getLogger(__name__)


class CargosonAvailablePrice(models.TransientModel):
    _name = 'cargoson.rate.result'
    _description = 'Cargoson available prices list item'

    choose_delivery_carrier_id = fields.Many2one('choose.delivery.carrier', ondelete='cascade', required=True)
    currency_id = fields.Many2one('res.currency', related='choose_delivery_carrier_id.order_id.currency_id')
    company_id = fields.Many2one('res.company', related='choose_delivery_carrier_id.order_id.company_id')

    carrier = fields.Char('Carrier')
    carrier_id = fields.Integer('Carrier ID')
    reg_no = fields.Char('Registration number')
    service = fields.Char('Service')
    service_id = fields.Integer('Service ID')
    price = fields.Monetary('Price')
    unit = fields.Char('Unit')
    type = fields.Char('Type')

    @api.model
    def from_cargoson(self, parent_id, available_price):
        return {
            'choose_delivery_carrier_id': parent_id,
            'carrier': available_price.carrier,
            'carrier_id': available_price.id,
            'reg_no': available_price.reg_no,
            'service': available_price.service,
            'service_id': available_price.service_id,
            'price': float(available_price.price),
            'unit': available_price.unit.as_dict() if available_price.unit else None,
            'type': available_price.type.as_dict() if available_price.type else None,
        }

    def select_carrier(self):
        logger.info('Selected Cargoson carrier: %s (%s %s)', self.carrier, self.price, self.currency_id.name)
        self.choose_delivery_carrier_id.write({
            'cargoson_selected_carrier_name': self.carrier,
            'cargoson_selected_carrier_id': self.carrier_id,
            'cargoson_selected_service_id': self.service_id,
            'cargoson_selected_price': self.price,
            'display_price': self.price,
            'delivery_price': self.price,
        })
        return {
            'name': _('Add a shipping method'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'choose.delivery.carrier',
            'res_id': self.choose_delivery_carrier_id.id,
            'target': 'new',
        }
