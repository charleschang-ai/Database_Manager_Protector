# -*- coding: utf-8 -*-
################################################################################
#    Author: Don Shan
#
################################################################################
{
    'name': 'Database Manager Protector',
    'version': '19.0.1.0.0',
    'category': 'Extra Tools',
    'summary': "Restrict access to Odoo's Database Manager with a master-password prompt and admin validation.",
    'description': "Adds a secure master-password gate to /web/database/manager: displays a CSRF-protected "
                   "password form, validates against Odoo's admin password, logs attempts, and only invokes "
                   "the original Database Manager logic on successful authentication. Designed to prevent "
                   "unauthorized database creation and management while preserving Odoo's native behavior and auditability.",
    'author': 'Don Shan',
    'maintainer': 'Don Shan',
    'depends': ['web'],
    'data': [
        'views/database_selector.xml',
    ],
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 15,
    'currency': "USD",
}
