# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api


class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "This is a Hospital Patient Tag Model"

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    color = fields.Integer(string='Color')
    sequence = fields.Integer(string='Sequence')

    # SQL Constrain
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'This name is already exits :)'),
        ('check_sequence', 'check(sequence > 0)', 'Sequence is not given :)')
    ]

    # Override the copy Method
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = self.name + " (copy)"
        return super(PatientTag, self).copy(default)
