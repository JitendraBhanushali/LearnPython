from odoo import api, fields, models


class DairySeller(models.Model):
    _name = 'dairy.seller'
    _description = 'Dairy Seller'

    seller_name = fields.Char(string='Seller Name')
    milkType = fields.Selection([('cow', 'Cow'), ('buffalo', 'Buffalo'), ('goat', 'Goat')], string="Choose Milk Type")
    liters = fields.Float(string="Enter The Liters")