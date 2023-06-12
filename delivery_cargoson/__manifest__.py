# noinspection PyStatementEffect
{
    'name': 'Cargoson Shipping',
    'description': 'Send your packages through Cargoson',
    'category': 'Inventory/Delivery',
    'version': '1.0.6',
    'author': 'Avatud Lahendused',
    'website': 'https://www.avalah.ee',
    'license': 'Other proprietary',

    'depends': [
        'delivery',
        'mail',
        'sale_stock',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'data/cron.xml',

        'views/delivery_cargoson.xml',
        'views/choose_delivery_carrier_views.xml',
        'views/cargoson_queue_task_views.xml',
        'views/cargoson_shipping_wizard_views.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': True,
}
