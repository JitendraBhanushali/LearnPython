# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    seller_limit = fields.Integer(string='Delay alert contract outdated', config_parameter='dairy.seller_limit')
