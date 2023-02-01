# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInherit(WebsiteSale):

    @http.route()
    def shop(self, **post):

        print("This is a self===", self)

        res = super(WebsiteSaleInherit, self).shop(**post)
        print("This is a res=====", res)

        pricelist_context = request.env.context
        print("Context====> ", pricelist_context)


        # for rec in pricelist_context:
        #     print("Rec", rec)


        user = request.env.user
        print("This is a user partner_id====", user.partner_id)
        print("This is a user partner_id name====", user.partner_id.name)
        print("This is a user partner_id property_product_pricelist====", user.partner_id.property_product_pricelist)


        return res







    # @http.route()
    # def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
    #     res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', min_price=0.0, max_price=0.0,
    #                                                ppg=False, **post)
    #     pricelist_context = request.env.context
    #     print("Context====> ", pricelist_context)
    #
    #     return res