{
    'name': 'App One',
    'author': 'Islam mohamed',
    'depends': ['base', 'sale', 'mail', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'data/property_sequence.xml',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'wizerd/change_wizerd_view.xml',

    ],

    'application': True,

}
