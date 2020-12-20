# -*- coding: utf-8 -*-
{
    'name': "product_attribute_views",

    'summary': """
        Product Attribute Views""",

    'description': """
        1/ Adds a view for product.attribute.value.
        2/ Adds a view for product.template.attribute.line.
        3/ Adds a view for product.template.attribute.value.
    """,

    'author': "o.s.admin",
    'website': "https://www.osadmin.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/sale_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
