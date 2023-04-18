from odoo import models, fields


# noinspection DuplicatedCode
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

    cargoson_selected_carrier_name = fields.Char('Selected carrier')
    cargoson_selected_carrier_id = fields.Integer('Selected carrier ID')
    cargoson_selected_service_id = fields.Integer('Selected service ID')
    cargoson_selected_price = fields.Monetary('Selected price')

    def get_cargoson_collection_address(self):
        self.ensure_one()
        if hasattr(self, 'warehouse_id'):
            return self.warehouse_id.partner_id
        else:
            return self.company_id.partner_id

    def get_cargoson_delivery_address(self):
        self.ensure_one()
        return self.partner_shipping_id
