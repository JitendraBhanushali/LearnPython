# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import pytz
from datetime import datetime




class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'



    # Update a record
    def write(self, vals):
        print("This is a vals----", vals)


        date_planned = vals.get('date_planned')
        print("date_planned", date_planned)

        if date_planned is not None:
            value = datetime.strptime(date_planned, "%Y-%m-%d %H:%M:%S")
            print("convert_date", value)

            # # work
            tz_user = pytz.timezone(self.env.context.get('tz') or self.env.user.tz)
            print("tz_user", tz_user)

            new_date = pytz.utc.localize(value).astimezone(tz_user).replace(tzinfo=None)
            print("new_date", new_date)

            update_time = datetime.strftime(new_date, "%Y-%m-%d %H:%M:%S")
            print("update_time", update_time)

            if date_planned:
                self.message_post(body=_('Receipt date Updated :- %s <i class="fa fa-long-arrow-right"/> %s',self.date_planned,update_time), message_type='comment', subtype_xmlid="mail.mt_comment")

        return super(PurchaseOrder, self).write(vals)







        # return super(PurchaseOrder, self).write(vals)















# tz_user = pytz.timezone(self.env.context.get('tz') or self.env.user.tz)
        # print("tz_user", tz_user)
        #
        # new_date = pytz.utc.localize(convert_date).astimezone(tz_user).replace(tzinfo=None)
        # print("new_date", new_date)
        #