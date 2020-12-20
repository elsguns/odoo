# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def create(self, vals):
        if 'product_template_attribute_value_ids' in vals.keys():
            ids = vals['product_template_attribute_value_ids'][0][2]
            new_ids = []
            for id in ids:
                new_id = self.env['product.template.attribute.value'].search(
                    [('product_tmpl_id', '=', vals['product_tmpl_id']), ('product_attribute_value_id', '=', id)])
                if new_id:
                    if len(new_id.ids) > 1:
                        msg = "More than one product_template_attribute_value_id found for product_tmpl_id '%s' and product_attribute_value_id '%s'" % (
                            vals['product_tmpl_id'], id)
                        raise Exception(msg)
                    new_ids.append(new_id.id)
                else:
                    msg = "No product_template_attribute_value_id found for product_tmpl_id '%s' and product_attribute_value_id '%s'" % (
                    vals['product_tmpl_id'], id)
                    raise Exception(msg)
            vals['product_template_attribute_value_ids'] = [(6,False,new_ids)]
        result = super(ProductProduct, self).create(vals)
        return result
