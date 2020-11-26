#-*- coding: utf-8 -*-

from odoo import api, fields, models, _


class PosCategory(models.Model):
    _inherit = 'pos.category'

    singular_name = fields.Char(string='Singular Name')