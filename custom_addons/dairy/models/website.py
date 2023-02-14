# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models, _


class WebsiteInherite(models.Model):
    _inherit = 'website'

    def get_pricelist_available(self, show_visible=False):
        """ Return the list of pricelists that can be used on website for the current user.
        Country restrictions will be detected with GeoIP (if installed).
        :param bool show_visible: if True, we don't display pricelist where selectable is False (Eg: Code promo)
        :returns: pricelist recordset
        """

        # print("self--------->=========", self)
        #
        # print("self.partner_id--------->=========", self.partner_id)
    #     print("self.user_id.property_product_pricelist ========", self.partner_id.property_product_pricelist)

        return super(WebsiteInherite, self).get_pricelist_available()

    # def get_current_pricelist(self):
    #     """
    #     :returns: The current pricelist record
    #     """
    #     print("self--------->=========", self)
    #     print("self.env.context--------->=========", self.env.context)
    #     print("self.partner_id--------->=========", self.partner_id.id)
    #     print("self.user_id.property_product_pricelist ========", self.partner_id.property_product_pricelist)
    #
    #     return super(WebsiteInherite, self).get_current_pricelist()
