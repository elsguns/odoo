# -*- coding: utf-8 -*-
# from odoo import http


# class ProductCategoryDefaults(http.Controller):
#     @http.route('/product_category_defaults/product_category_defaults/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_category_defaults/product_category_defaults/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_category_defaults.listing', {
#             'root': '/product_category_defaults/product_category_defaults',
#             'objects': http.request.env['product_category_defaults.product_category_defaults'].search([]),
#         })

#     @http.route('/product_category_defaults/product_category_defaults/objects/<model("product_category_defaults.product_category_defaults"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_category_defaults.object', {
#             'object': obj
#         })
