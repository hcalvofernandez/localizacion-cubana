# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2013-2017 Scnet  All Rights Reserved.
#                         Hanoi Calvo Fernandez <scnetisla@gmail.com>


{
    'name' : 'Cuba - Contabilidad para TCP',
    'version' : '1.0',
    'author' : 'Hanoi Calvo',
    'website' : 'http://scnet.cu',
    'category': 'Localization',
    'sequence': 2,
    'summary': 'Nomenclador de cuentas para el TCP',
    'description': """
Nomenclador de cuentas para el TCP.
========================================

    * Definicion del modulo:
        * nomenclador general de cuentas cubanas
        * nomenclador general de cuentas cubanas para pequeñas y medianas empresas
        * nomenclador general de cuentas cubanas para asociaciones
    * define las cuentas temporales para ventas y compras
    * define las cuentas temporales para impuestos
    * define la posicion fiscal cubana para el TCP 
""",
   "depends" : ["account", "base_vat", "base_iban"],
    "data" : [
        'data/res_currency_data.yml',
        'data/res_country_state_data.xml',
        'data/account_account_type_data.xml',
        'data/l10n_cu_tcp_chart_data.xml',
        'data/account_account_template_data.xml',
        'data/account_tax_data.xml',
        'data/account_fiscal_position_template_data.xml',
        'data/account_chart_template_data.xml',
        'data/account_chart_template_data.yml',
    ],
    'demo': [

    ],
    'test': [

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
