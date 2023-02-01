from odoo import api, fields, models
from datetime import datetime, timedelta


class DairySeller(models.Model):
    _name = 'dairy.seller'
    _description = 'Dairy Seller'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    name = fields.Char(string="Order Sequence", tracking=True)
    customer_id = fields.Many2one('res.partner', string='Name', tracking=True, required=True)
    email = fields.Char(string='Email', related='customer_id.email')
    customer_type = fields.Selection([('seller', 'seller'), ('buyer', 'buyer')], string="Choose Customer Type",
                                     tracking=True, default='seller')

    milk_taker = fields.Many2one('res.users', string='Milk Taker', tracking=True, required=True)
    milkType = fields.Selection([('cow', 'Cow'), ('buffalo', 'Buffalo'), ('goat', 'Goat')], string="Choose Milk Type",
                                tracking=True, )
    liters = fields.Float(string="Enter The Liters", tracking=True, )
    date = fields.Datetime(string="Creation Date", tracking=True, default=fields.Datetime.now)
    price = fields.Integer(string="Enter Price", tracking=True, )
    active = fields.Boolean(string="Active", default=True)
    total = fields.Float(string="Total", compute="_total", store=True, readonly=True)
    mail_sent = fields.Boolean("Email Sent", default=False)

    @api.depends('liters', 'price')
    def _total(self):
        for rec in self:
            rec.total = rec.liters * rec.price

    # Create a sequence for Dairy Orders
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('dairy.seller')
        return super(DairySeller, self).create(vals)

    # Find Weekly customer who's mail_sent False and send mail to Customer
    @api.model
    def send_email_cron(self):
        print("=========This is a Email Cron=======")
        mail_send_true = []

        for rec in self.search([('mail_sent', '=', False), ('date', '<', fields.Date.today())]):

            start_day = fields.Datetime.today() - timedelta(days=7 + datetime.today().weekday())
            # print("This is a Starting week day ======> ", start_day)

            end_day = fields.Datetime.today() - timedelta(days=datetime.today().weekday())
            # print("This is a new Week monday ========> ", end_day)

            if end_day > rec.date > start_day:
                rec.send_email()
                rec.mail_sent = 'True'
                mail_send_true.append(rec.id)
        if mail_send_true:
            self.send_email_to_admin(mail_send_true)

    def send_email(self):
        report_template_id = self.env.ref('dairy.dairy_customer_email_template')
        print("If user 70 self.id ===> ", self.id)
        report_template_id.send_mail(self.id, force_send=True)

    def send_email_to_admin(self, mail_send_true):
        report_template_id = self.env.ref('dairy.dairy_customer_weekly_report_email_template')
        print("If report_template_id ===> ", report_template_id)
        print("If mail_send_true ===> ", mail_send_true)

        import base64
        report = self.env.ref('dairy.action_report_for_admin_dairy')
        report_service = report.report_name
        attachments = []
        res, format = report._render_qweb_pdf(report_service, mail_send_true)
        res = base64.b64encode(res)
        res_name = 'report.' + report_service
        ext = "." + format
        if not res_name.endswith(ext):
            res_name += ext
        attachments.append((res_name, res))
        attachment_ids = []
        Attachment = self.env['ir.attachment']
        for attachment in attachments:
            attachment_data = {
                'name': attachment[0],
                'datas': attachment[1],
                'type': 'binary',
                'res_model': self._name,
                'res_id': mail_send_true[0],
            }
            attachment_ids.append(Attachment.create(attachment_data).id)
        message = self.env['mail.message'].create({
            'subject': 'Dairy sellery weekly report',
            'body': 'Please find attached report file',
            'author_id': self.env.user.partner_id.id,
            'email_from': 'info@intechualsoluions.com',
            'reply_to': 'info@intechualsoluions.com',
            'attachment_ids': [(6, 0, attachment_ids)],
        })

        mail_fattura = self.env['mail.mail'].sudo().with_context(wo_bounce_return_path=True).create({
            'mail_message_id': message.id,
            'email_to': 'admin@inechualsolutions.com',
        })
        # report_template_id.send_mail(mail_send_true, force_send=True)

    # Print Button
    def action_print_customer_report(self):
        return self.env.ref("dairy.action_report_dairy").report_action(self)
        # print("Hellooooooo................:) <<<<< Your Report is Printed >>>>>>")

    # Email Button
    def action_send_email_customer_report(self):
        print("<<<<< Your Report is Send >>>>>>")
        template = self.env.ref("dairy.dairy_customer_email_template")
        # print("<<<<< Your template >>>>>>", template)
        for rec in self:
            template.send_mail(rec.id)

    def action_save_record(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Record Save Successfully',
                'type': 'rainbow_man',
            }
        }

# Practice work
# @api.models
# def send_email_cron(self):
# print("Hellooooooo................:)")
# today = datetime.today()
# tasks = self.env['dairy.seller'].search([('date', '=',today)])
# email_from = self.env['dairy.seller'].search([('id','=',1)])
# email_to = tasks.customer_id.email
# values = {
#     'email_from': email_from,
#     'email_to': email_to,
#     'auto_delete': False,
#     'models': 'dairy.seller',
# }
# send_mail = self.env['mail.mail'].sudo().create(values)
# send_mail.send()

# for rec in self.search([]):
# return rec.action_send_email_customer_report()


# ===============================================
#
# subject = "Customer Report"
# dairy_customer = self.customer_id.email
# report_template_id = self.env.ref('dairy.dairy_customer_email_template').id
# report_template_values = {
#     'subject': subject,
#     'email_to': dairy_customer,
#     'auto_delete': False,
#     'models': 'dairy.seller',
# }
# report_template = report_template_id.create(report_template_values)
# template = self.env.ref('<module>.<template_id>')
# template.send_mail(self.id, force_send=True)

# report_template.send(force_send=True)
# report_template_id.send()


# +++++++++++++++++++++++++++++++++++++++++++++
# for rec in self.search([('mail_sent', '=',False), (datetime.now()-timedelta(days=7), '<', 'date', '<', datetime.now())]):
# mail_not_sent = self.env['dairy.seller'].sudo().search([('mail_sent', '=', False),('date', '<', datetime.now())])
# for rec in mail_not_sent:

#     if rec.date < datetime.now():
#         print("Date =========>",rec.date)

# date_time = (datetime.now() - timedelta(days=7))
# print("Date_time ==============",date_time)
#     if rec.mail_sent == 'False':
#         print("Mail_sent is False============",rec.mail_sent)
#         rec.send_email()

# print("Mail_sent is True Now===========",rec.mail_sent )


# ==========================Week Days Count Logic==================================
#         for rec in self.search([('mail_sent', '=', False), ('date', '<', fields.Date.today())]):
#             # print("Fields Date=========>", rec.date)
#             # print("Report Generated date=====>", rec.date)
#             # print("Calculated Week Day =======> ", fields.Datetime.today() - timedelta(days=7 + datetime.today().weekday()))
#             # print("If Condition week day minus:=====", rec.date > fields.Datetime.today() - timedelta(days=7 + datetime.today().weekday()))
#
#             start_day = fields.Datetime.today() - timedelta(days=7 + datetime.today().weekday())
#             # print("This is a Starting week day ======> ", start_day)
#
#             end_day = fields.Datetime.today() - timedelta(days=datetime.today().weekday())
#             # print("This is a new Week monday ========> ", end_day)
#
#             if end_day > rec.date > start_day:
#
#                 # print("This is a week days from monday to sunday=====>", rec.date)
#
#                 # rec.send_email()
#                 # rec.mail_sent = 'True'
#                 mail_send_true.append(rec.id)
#                 print("Added---------- ====", mail_send_true)
#         print("Added email send true Record Id's ====", mail_send_true)
#                 # print("Email Send Successfully")
#                 # print("Email Sent is =====>", rec.mail_sent)
