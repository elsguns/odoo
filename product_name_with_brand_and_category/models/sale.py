from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # def _website_product_id_change(self, order_id, product_id, qty=0):
    #     values = super(SaleOrder, self)._website_product_id_change(order_id, product_id, qty)
    #
    #     if values.get('pos_categ_id_filter'):
    #         values['pos_categ_id_filter'] = values['pos_categ_id_filter'].id
    #     if values.get('product_brand_id_filter'):
    #         values['product_brand_id_filter'] = values['product_brand_id_filter'].id
    #
    #     return values


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_brand_id_filter = fields.Many2one(
        'product.brand',
        string='Brand Filter',
        help='Select a brand to filter product selection'
    )
    pos_categ_id_filter = fields.Many2one(
        'pos.category',
        string='PoS Category Filter',
        help='Select a pos category to filter product selection'
    )

    @api.onchange('product_brand_id_filter')
    def onchange_product_brand_id_filter(self):
        res = {}
        if self.product_brand_id_filter:
            res['domain'] = {'product_id': [('product_brand_id.id', '=', self.product_brand_id_filter.id)]}
        else:
            res['domain'] = {'product_id': []}
        return res

    @api.onchange('pos_categ_id_filter')
    def onchange_pos_categ_id_filter(self):
        res = {}
        if self.pos_categ_id_filter:
            res['domain'] = {'product_id': [('pos_categ_id.id', '=', self.pos_categ_id_filter.id)]}
        else:
            res['domain'] = {'product_id': []}
        return res

    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        if self.product_id:
            self.product_brand_id_filter = self.product_id.product_brand_id
            self.pos_categ_id_filter = self.product_id.pos_categ_id
        return res
