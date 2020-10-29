#-*- coding: utf-8 -*-

from odoo import models, fields, api


class PosCategory(models.Model):
    _inherit = 'pos.category'

    product_category_id = fields.Many2one('product.category', 'Product Category')
    product_public_category_id = fields.Many2one('product.public.category', 'Product Public Category')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.onchange('pos_categ_id')
    def _onchange_pos_category(self):
        if self.pos_categ_id:
            if self.pos_categ_id.product_category_id:
                self.categ_id = self.pos_categ_id.product_category_id
            if self.pos_categ_id.product_public_category_id and self.pos_categ_id.product_public_category_id not in self.public_categ_ids:
                self.public_categ_ids = [(4, self.pos_categ_id.product_public_category_id.id)]
