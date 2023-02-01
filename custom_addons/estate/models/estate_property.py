# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "CRM Recurring revenue plans"


    name = fields.Many2one('res.partner', string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Post Code")
    date_availability = fields.Date(string="Date", default=lambda self: fields.Datetime.now())
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms", default="2")
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer()
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Select Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], string="Select Side")
    state = fields.Selection([('new', 'New'), ('offer', 'Offer'), ('received', 'Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')], string="Select State")
    total_area = fields.Integer(string="Total Area", compute="_compute_total_area")
    active = fields.Boolean(string="Active", default=True)

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for line in self:
            line.total_area = line.living_area + line.garden_area