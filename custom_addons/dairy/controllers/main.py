# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInherit(WebsiteSale):

    @http.route()
    def shop(self, **post):

        print("This is a self===", self)

        # res = super(WebsiteSaleInherit, self).shop(**post)
        # print("This is a res=====", res)

        pricelist_context = request.env.context
        print("Context====> ", pricelist_context)

        user = request.env.user
        print("This is a user partner_id====", user.partner_id)
        print("This is a user partner_id name====", user.partner_id.name)
        u_pl = user.partner_id.property_product_pricelist
        print("This is a user partner_id property_product_pricelist====", u_pl)

        search_pricelist = request.env['website'].search([])
        print("search_pricelist=====", search_pricelist)
        pl = search_pricelist.pricelist_id
        print("search_pricelist pricelist_id=====", pl)

        if u_pl != pl:
            print("Price list is not same")
            search_pricelist.write({"pricelist_id": u_pl})

        return super(WebsiteSaleInherit, self).shop(**post)
        # return res







    # @http.route()
    # def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
    #     res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', min_price=0.0, max_price=0.0,
    #                                                ppg=False, **post)
    #     pricelist_context = request.env.context
    #     print("Context====> ", pricelist_context)
    #
    #     return res