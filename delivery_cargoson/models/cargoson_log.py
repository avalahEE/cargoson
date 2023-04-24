from odoo import fields, models
import json
import logging
logger = logging.getLogger(__name__)


class CargosonLog(models.Model):
    _name = 'cargoson.log'
    _description = 'Cargoson event log'

    delivery_carrier_id = fields.Many2one(
        'delivery.carrier', string='Delivery carrier', ondelete='cascade', required=True)

    sale_order_id = fields.Many2one('sale.order', 'Sale Order')
    picking_id = fields.Many2one('stock.picking', 'Delivery Order')

    type = fields.Char('Type', required=True)
    message = fields.Text('Log message')
    status = fields.Selection([
            ('success', 'Success'),
            ('warning', 'Warning'),
            ('error', 'Error'),
        ], string='Status', required=True)

    # custom data in JSON format that can be passed along with the log entry
    json_data = fields.Text('Data')

    def get_data(self):
        self.ensure_one()
        if not self.json_data:
            return None
        return json.loads(self.json_data)
