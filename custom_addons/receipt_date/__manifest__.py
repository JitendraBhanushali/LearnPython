# -*- coding: utf-8 -*-

{
    'name': 'Receipt Date',
    'version': '1.0.0',
    'summary': 'Purchase Order Receipt Date',
    'sequence': -100,
    'description': """This is a First Purchase Order Receipt Date""",
    'category': '',
    'author': "Intechual Solutions",
    'website': '',
    'images': [],
    'depends': ['mail', 'purchase'],
    'data': [
        'views/purchase_portal_template_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_frontend': [

            'receipt_date/static/src/js/calendar_action_button.js',
            'receipt_date/static/src/xml/calendar_view.xml',
        ],
    },
    'license': 'LGPL-3',
}
