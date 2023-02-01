# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "This is a Hospital Patient Appointment Model"
    _rec_name = 'name'

    name = fields.Char(string="Sequence", tracking=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", ondelete='restrict', tracking=True)
    gender = fields.Selection(related='patient_id.gender', tracking=True)
    appointment_time = fields.Datetime(string="Appointment Time", tracking=True, default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", tracking=True, default=fields.Date.context_today)
    ref = fields.Char(string="Ref", tracking=True)
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancel')], string="Status", default="draft")
    doctor_id = fields.Many2one('res.users', string="Doctor")
    operation = fields.Many2one('hospital.operation', string="Operation")
    pharmacy_lines_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string="Pharmacy Lines")

    # Patient name
    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    # Rainbow man effect
    def action_test(self):
        print("Button")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Thank you...:)',
                'type': 'rainbow_man',
            }
        }

    # Buttons
    def action_in_consultation(self):
        for rec in self:
            if rec.state == 'draft':
                rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    # def action_cancel(self):
    #     for rec in self:
    #         rec.state = 'cancel'

    def action_cancel(self):
        action = self.env.ref('hospital.action_cancel_appointment').read()[0]
        return action

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    # Create a sequence for hospital patient
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super(HospitalAppointment, self).create(vals)

    # Override the unlink method (Delete)
    def unlink(self):
        for rec in self:
            if rec.state != 'draft':
                raise ValidationError(_("You can only delete a appointment in draft state"))
            return super(HospitalAppointment, self).unlink()


class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "This is a hospital patient appointment pharmacy lines"

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string="Quantity", default=1)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
