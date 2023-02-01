# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertyTypes(models.Model):
    _name = "estate.property.types"
    _description = "Estate Propertys Types"

    partner_id = fields.Many2one('res.partner', string='Buyer')
    user_id = fields.Many2one('res.users', string='Salesperson', index=True,
                              default=lambda self: self.env.user)

