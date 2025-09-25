# -*- coding: utf-8 -*-

{
    'name': 'Real Estate',
    'version': '1.0',
    'author': 'Telvin',
    'license': 'LGPL-3',
    'category': 'Sales',
    'summary': 'Real Estate Management System',
    'sequence': -200,
    'description': """
This module contains all the common features of a real estate management system
    """,
    'depends': ["base"],
    'data': [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/menu_items.xml',
        'views/property_type_view.xml',
        'views/property_tag.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {},
}
