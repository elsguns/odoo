# -*- coding: utf-8 -*-
{
    'name': "product_variant_migration",

    'summary': """
        Product variant migration""",

    'description': """
        In older versions of Odoo a product variant linked to product attribute values directly, 
        while now to product.template.attribute.value ids.
        This module translates attribute_value_ids to product_template_attribute_value_ids during product.product import.
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
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
