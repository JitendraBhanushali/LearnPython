# # -*- coding: utf-8 -*-
# from odoo import http
# from odoo.http import request
# from odoo.addons.website_sale.controllers.main import WebsiteSale
#
#
# class WebsiteSaleInherit(WebsiteSale):
#
#     @http.route()
#     def shop(self, **post):
#
#         res = super(WebsiteSaleInherit, self).shop(**post)
#         pricelist_context = request.env.context
#         print("Context====> ", pricelist_context)
#
#         return res
#
#
#
#
#
#
#
#     # @http.route()
#     # def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
#     #     res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', min_price=0.0, max_price=0.0,
#     #                                                ppg=False, **post)
#     #     pricelist_context = request.env.context
#     #     print("Context====> ", pricelist_context)
#     #
#     #     return res