# noinspection PyStatementEffect
{
    'name': 'Cargoson Shipping',
    'description': 'Send your packages through Cargoson',
    'category': 'Inventory/Delivery',
    'version': '1.0.0',
    'author': 'Avatud Lahendused',
    'website': 'https://www.avalah.ee',

    # TODO: pick an appropriate license
    'license': 'Other proprietary',

    'depends': [
        'delivery',
        'mail',
    ],
    'data': [
        'security/security.xml',
        # 'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
