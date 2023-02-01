# -*- coding: utf-8 -*-

{
    'name': 'Dairy',
    'version': '1.0.0',
    'summary': 'Dairy',
    'sequence': -100,
    'description': """This is for Dairy Shop""",
    'category': '',
    'author': "Intechual Solutions",
    'website': '',
    'images': [],
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/buyer_view.xml',
        'view/seller_view.xml',
        'view/menu.xml',
        'view/res_partner_view.xml',
        'view/res_config_settings_view.xml',
        'view/template.xml',
        'reports/ir_actions_dairy_buyer_report.xml',
        'reports/ir_actions_dairy_buyer_report_template.xml',
        'reports/ir_actions_dairy_seller_report.xml',
        'reports/ir_actions_dairy_seller_report_template.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
}