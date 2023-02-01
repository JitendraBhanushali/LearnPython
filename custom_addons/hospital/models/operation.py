# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class HospitalOperation(models.Model):
    _name = "hospital.operation"
    _description = "This is a Hospital Operation Model"
    _log_access = False
    _rec_name = 'operation_name'

    doctor_id = fields.Many2one('res.users', string='Doctor')
    operation_name = fields.Char(string="Name")

    # Create name while rec name is not given
    # @api.model
    # def name_create(self, name):
    #     return self.create({'operation_name': name}).name_get()[0]