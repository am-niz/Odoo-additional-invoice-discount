# -*- coding: utf-8 -*-
{
    'name': "Invoice Addtional Discount",

    'summary': "Additional Disocount option adding on create invoice wizard",

    'description': """
Additional Disocount option adding on create invoice wizard
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_make_invoice_advance_inherit_discount_views.xml',
    ],
    "application": True,
    "sequence": -99,
}

