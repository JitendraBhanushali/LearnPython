from odoo import api, fields, models


class DairyBuyer(models.Model):
    _name = 'dairy.buyur'
    _description = 'Dairy Buyer'

    buyer_name = fields.Char(string='Buyer Name')
    milkType = fields.Selection([('cow', 'Cow'), ('buffalo', 'Buffalo'), ('goat', 'Goat')], string="Choose Milk Type")
    liters = fields.Float(string="Enter The Liters")
