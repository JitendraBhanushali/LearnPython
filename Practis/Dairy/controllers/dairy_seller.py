from odoo import http
from odoo.http import request


class Seller(http.Controller):
    # Seller Controller Created
    @http.route('/dairy/seller/', website=True, auth='public')
    def dairy_seller(self, **kw):
        return "Hello Sellers ...!"
