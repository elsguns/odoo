#-*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pos_categ_singular_name = fields.Char(string='PoS Category Singular Name',related="pos_categ_id.singular_name", readonly=False)

    def name_get(self):
        res = super(ProductTemplate, self).name_get()
        res2 = []
        for name_tuple in res:
            product = self.browse(name_tuple[0])

            name = product.name
            if product.pos_categ_singular_name:
                name = product.pos_categ_singular_name + " " + name
            if product.product_brand_id.name:
                name = product.product_brand_id.name + " " + name
            res2.append((
                name_tuple[0],
                name
            ))

        return res2


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def name_get(self):
        res = super(ProductProduct, self).name_get()
        res2 = []
        for name_tuple in res:
            product = self.browse(name_tuple[0])

            if product.default_code:
                name = product.default_code
                if product.pos_categ_singular_name:
                    name = product.pos_categ_singular_name + " " + name
                if product.product_brand_id.name:
                    name = product.product_brand_id.name + " " + name
            else:
                name = product.product_tmpl_id.display_name

            res2.append((
                name_tuple[0],
                name
            ))

        return res2
