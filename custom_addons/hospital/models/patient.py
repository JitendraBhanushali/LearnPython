# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import date
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "This is a Hospital Patient Model"
    _rec_name = 'name'

    name = fields.Char(string="Name", tracking=True)
    date_of_birth = fields.Date(string="Date of Birth")
    ref = fields.Char(string="Ref", tracking=True)
    # age = fields.Integer(string="Age", compute='_compute_age', inverse='_inverse_compute_age', tracking=True)
    age = fields.Integer(string="Age", compute='_compute_age', inverse='_inverse_compute_age', search='_search_age',
                         tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'other')], string="Select Gender",
                              tracking=True, default="male")
    active = fields.Boolean(string="Active", default="True")
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string="Tags")
    appointment_count = fields.Integer(string="Appointment Count", compute="_compute_appointment_count", store=True)
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string="Appointments id")
    parent = fields.Char(string="Parent")
    marital_status = fields.Selection([('single', 'Single'), ('married', 'Married')], string="Marital Status",
                                      tracking=True)
    partner_name = fields.Char(string="Partner Name")

    # Store the compute file depends is required
    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])

    # Calculate The Age
    @api.depends('date_of_birth')
    def _compute_age(self):
        # print("Print----------", self)
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    # Edit age and change the age
    @api.depends('age')
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            rec.date_of_birth = today - relativedelta(years=rec.age)

    # Non store searchable comput field age
    def _search_age(self, operator, value):
        date_of_birth = date.today() - relativedelta(years=value)
        start_of_year = date_of_birth.replace(day=1, month=1)
        end_of_year = date_of_birth.replace(day=31, month=12)
        # print("date_of_birth>>>>>>", date_of_birth)
        # print("start_of_year>>>>>>>>>>", start_of_year)
        # print("end_of_year====>>>", end_of_year)
        return [('date_of_birth', '>=', start_of_year), ('date_of_birth', '<=', end_of_year)]

    # Check the date of birth is valid or not
    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.date.today():
                raise ValidationError(_("Entered Birth Date is not acceptable :)"))

    # On delete check the appointment
    @api.ondelete(at_uninstall=False)
    def _check_appointmnets(self):
        for rec in self:
            if rec.appointment_ids:
                raise ValidationError(_("You can not delete a patient with appointment :)"))

    # Add a ref in appointment field
    def name_get(self):
        return [(record.id, "[%s] - %s" % (record.ref, record.name)) for record in self]

    # Create a sequence for hospital patient
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    # Update a record
    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)

    # Override the copy Method
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = _("%s (copy)", self.name)
        return super(HospitalPatient, self).copy(default)

    # Tree view groupby button action
    def action_test(self):
        print("Clicked=======")
        return
