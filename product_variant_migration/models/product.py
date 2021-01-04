# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def create(self, vals):
        if 'product_template_attribute_value_ids' in vals.keys():
            product_tmpl_id = self.env['product.template'].search([('id', '=', vals['product_tmpl_id'])])
            if product_tmpl_id:
                product_tmpl_external_id = self.env['ir.model.data'].search(
                    [('res_id', '=', vals['product_tmpl_id']), ('model', '=', 'product.template')])
                product_tmpl = "%s (%s, %s)" % (product_tmpl_id.name, product_tmpl_id.id, product_tmpl_external_id.name)
                # _logger.info("PRODUCT_TMPL_ID = %s" % (product_tmpl))

                ids = vals['product_template_attribute_value_ids'][0][2]
                new_ids = []
                for id in ids:
                    product_attribute_value_id = self.env['product.attribute.value'].search([('id', '=', id)])
                    if product_attribute_value_id:
                        product_attribute_value_external_id = self.env['ir.model.data'].search(
                            [('res_id', '=', id), ('model', '=', 'product.attribute.value')])
                        product_attribute_value = "%s (%s, %s)" % (
                        product_attribute_value_id.name, product_attribute_value_id.id,
                        product_attribute_value_external_id.name)
                        # _logger.info("product_attribute_value_id = %s" % (product_attribute_value))

                        new_id = self.env['product.template.attribute.value'].search(
                            [('product_tmpl_id', '=', vals['product_tmpl_id']),
                             ('product_attribute_value_id', '=', id)])
                        # _logger.info(
                        #     "product_attribute_value_id %s = product_template_attribute_value_id %s" % (id, new_id.id))
                        if new_id:
                            if len(new_id.ids) > 1:
                                msg = "ERROR: More than one product_template_attribute_value_id found for product_tmpl_id '%s' and product_attribute_value_id '%s'" % (
                                    product_tmpl, product_attribute_value)
                                _logger.error(msg)
                                raise Exception(msg)

                            new_ids.append(new_id.id)
                        else:
                            msg = "ERROR: No product_template_attribute_value_id found for product_tmpl_id '%s' and product_attribute_value_id '%s'" % (
                                product_tmpl, product_attribute_value)
                            _logger.error(msg)
                            new_ids = []
                            break
                    else:
                        _logger.error("ERROR: No product attribute value found for id %s" % (id))
                        new_ids = []
                        break

                if len(new_ids) == len(ids):
                    vals['product_template_attribute_value_ids'] = [(6, False, new_ids)]
                    return super(ProductProduct, self).create(vals)
            else:
                _logger.error("ERROR: No product template found for id %s" % (vals['product_tmpl_id']))
