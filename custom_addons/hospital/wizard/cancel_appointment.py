# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime
from datetime import date
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "This is a Hospital Cancel Appointment Wizard"

    # Default Get Function for Current Date and active_id
    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['date_cancel'] = datetime.date.today()
        if self.env.context.get('active_id'):
            res['appointment_id'] = self.env.context.get('active_id')
        return res

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment",
                                     domain=[('state', '=', 'draft'), ('priority', 'in', ('0', '1', False))])
    reason = fields.Text(string="Reason")
    date_cancel = fields.Date(string="Cancellation Date")

    # Cancel button action
    def action_cancel(self):
        cancel_days = self.env['ir.config_parameter'].sudo().get_param('hospital.cancel_days')
        print("cancel_days====", cancel_days)
        allowed_date = self.appointment_id.booking_date - relativedelta(days=int(cancel_days))
        print("allowed_date", allowed_date)
        if allowed_date < date.today():
            raise ValidationError(_("Sorry This action is not valid because the appointment policy is not satisfy"))
        self.appointment_id.state = 'cancel'

    # if self.appointment_id.booking_date == fields.Date.today():

    # return
