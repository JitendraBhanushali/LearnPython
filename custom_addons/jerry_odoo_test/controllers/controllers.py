# -*- coding: utf-8 -*-
# from odoo import http


# class JerryOdooTest(http.Controller):
#     @http.route('/jerry_odoo_test/jerry_odoo_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jerry_odoo_test/jerry_odoo_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('jerry_odoo_test.listing', {
#             'root': '/jerry_odoo_test/jerry_odoo_test',
#             'objects': http.request.env['jerry_odoo_test.jerry_odoo_test'].search([]),
#         })

#     @http.route('/jerry_odoo_test/jerry_odoo_test/objects/<model("jerry_odoo_test.jerry_odoo_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jerry_odoo_test.object', {
#             'object': obj
#         })
