from odoo import fields, models, api, _
import logging
logger = logging.getLogger(__name__)


# noinspection DuplicatedCode
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
    estimated_collection_date = fields.Char(string="Estimated Collection Date")
    estimated_delivery_date = fields.Char(string="Estimated Delivery Date")

    @api.model
    def from_cargoson(self, available_price, delivery_wizard_id=None):
        return {
            'choose_delivery_carrier_id': delivery_wizard_id,
            'carrier': available_price.carrier,
            'carrier_id': available_price.id,
            'reg_no': available_price.reg_no,
            'service': available_price.service,
            'service_id': available_price.service_id,
            'price': float(available_price.price),
            'unit': available_price.unit.as_dict() if available_price.unit else None,
            'type': available_price.type.as_dict() if available_price.type else None,
            'estimated_collection_date': available_price.estimated_collection_date,
            'estimated_delivery_date': available_price.estimated_delivery_date,
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


# noinspection DuplicatedCode
class CargosonAvailablePriceShippingWizard(models.TransientModel):
    _name = 'cargoson.shipping.wizard.rate.result'
    _description = 'Cargoson available prices list item'

    cargoson_shipping_wizard_id = fields.Many2one('cargoson.shipping.wizard', ondelete='cascade', required=True)

    currency_id = fields.Many2one('res.currency', related='cargoson_shipping_wizard_id.currency_id')
    company_id = fields.Many2one('res.company', related='cargoson_shipping_wizard_id.picking_id.company_id')

    carrier = fields.Char('Carrier')
    carrier_id = fields.Integer('Carrier ID')
    reg_no = fields.Char('Registration number')
    service = fields.Char('Service')
    service_id = fields.Integer('Service ID')
    price = fields.Monetary('Price')
    unit = fields.Char('Unit')
    type = fields.Char('Type')
    estimated_collection_date = fields.Char(string="Estimated Collection Date")
    estimated_delivery_date = fields.Char(string="Estimated Delivery Date")

    @api.model
    def from_cargoson(self, available_price, shipping_wizard_id=None):
        return {
            'cargoson_shipping_wizard_id': shipping_wizard_id,
            'carrier': available_price.carrier,
            'carrier_id': available_price.id,
            'reg_no': available_price.reg_no,
            'service': available_price.service,
            'service_id': available_price.service_id,
            'price': float(available_price.price),
            'unit': available_price.unit.as_dict() if available_price.unit else None,
            'type': available_price.type.as_dict() if available_price.type else None,
            'estimated_collection_date': available_price.estimated_collection_date,
            'estimated_delivery_date': available_price.estimated_delivery_date,
        }

    def select_carrier(self):
        logger.info('Selected Cargoson carrier: %s (%s %s)', self.carrier, self.price, self.currency_id.name)
        self.cargoson_shipping_wizard_id.write({
            'cargoson_selected_carrier_name': self.carrier,
            'cargoson_selected_carrier_id': self.carrier_id,
            'cargoson_selected_service_id': self.service_id,
            'cargoson_selected_price': self.price,
        })
        return {
            'name': _('Add a shipping method'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'cargoson.shipping.wizard',
            'res_id': self.cargoson_shipping_wizard_id.id,
            'target': 'new',
        }
