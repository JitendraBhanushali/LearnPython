# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.purchase.controllers import portal
from odoo import http
from odoo.http import request
from datetime import datetime
from pytz import timezone, UTC




class PurchaseOrderReceiptDate(portal.CustomerPortal):

    @http.route()
    def portal_my_purchase_order_update_dates(self, order_id=None, access_token=None, **kw):
        """
        User update scheduled date on purchase order line.

        """
        print("Self------", self)

        res = super(PurchaseOrderReceiptDate, self).portal_my_purchase_order_update_dates(order_id=None, access_token=None)

        update_date = kw.get('receipt_date')
        print("update_date---", update_date)

        # new_date = datetime.strptime(update_date, '%m/%d/%Y %I:%M:%S %p') #.astimezone(UTC).replace(tzinfo=None)

        new_date = datetime.strptime(update_date, '%m/%d/%Y %I:%M %p') #.astimezone(UTC).replace(tzinfo=None)
        print("This is a new date>>>>>>>>", new_date)

        local_time = timezone(request.env.user.tz or request.env.context.get('tz') or 'UTC').localize(new_date).astimezone(UTC).replace(tzinfo=None)
        print("local_time", local_time)

        update_time = datetime.strftime(local_time, "%Y-%m-%d %H:%M:%S")
        print("update_time", update_time)

        search_order = request.env['purchase.order'].search([("id", "=", order_id)])
        if search_order and local_time :
            search_order.write({"date_planned": update_time})
            return request.redirect(f"/my/purchase/{order_id}/?access_token={access_token}")

        return res















# # new_date = datetime.strptime(update_date, '%m/%d/%Y %I:%M %p').astimezone(UTC).replace(tzinfo=None)
#         print("This is a new date>>>>>>>>", new_date)


        # local_tz = pytz.timezone(request.env.context.get('tz') or request.env.user.tz)
        # print("local_tz----", local_tz) #Localtime zone of user

        # new_date = datetime.strptime(update_date, '%m/%d/%Y %I:%M %p')
        # new_date = datetime.strptime(update_date, '%m/%d/%Y %I:%M%S %p').replace(tzinfo=UTC)    #Naive Error

        # local_time = pytz.utc.localize(new_date).astimezone(local_tz).replace(tzinfo=None)
        # print("local_time", local_time)

        # utc_time = local_time.astimezone(pytz.utc) # convert to UTC time
        # print("utc_time", utc_time)
        # print('Current TimeZone:', utc_time.strftime('%m/%d/%Y %I:%M:%S %p'))
        #
        # new_time = utc_time.strftime('%m/%d/%Y %I:%M:%S')
        # print("new_time", new_time)





# import pytz
# from datetime import datetime
#
# user_input = "2023-01-30 12:00:00" # user input in local time
# local_tz = pytz.timezone("Asia/Kolkata") # example local timezone

# local_time = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")

# local_time = local_tz.localize(local_time, is_dst=None)
# utc_time = local_time.astimezone(pytz.utc) # convert to UTC time
#
# # store UTC time in backend