# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    po_count = fields.Integer(string="PO Count", compute='_compute_po_count')
    po_id = fields.Many2one(
        comodel_name="purchase.order",
        string="Purchase Order",
        copy=False)

    # count the purchase order
    def _compute_po_count(self):
        for order in self:
            order.po_count = len(order.po_id)

    # action view purchase order
    def action_view_po(self):
        self.ensure_one()
        po_id = self.po_id
        action = self.env['ir.actions.actions']._for_xml_id('purchase.purchase_rfq')
        if len(po_id) > 1:
            action['domain'] = [('id', 'in', po_id.id)]
        elif len(po_id) == 1:
            form_view = [(self.env.ref('purchase.purchase_order_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state, view) for state, view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = po_id.id
        else:
            action = {'type': 'ir.actions.act_window_close'}

        return action

    # create a purchase order
    def action_create_purchase_order(self):
        create_po_order_line = []
        for line in self.order_line:
            create_po_order_line.append((0, 0, {
                'name': line.name,
                'display_type': line.display_type,
                'product_id': line.product_id.id,
                'price_unit': line.price_unit,
                'product_qty': line.product_uom_qty,
                'product_uom': line.product_uom.id,
            }))
        po = self.env['purchase.order'].create({
            "partner_id": self.partner_id.id,
            'order_line': create_po_order_line,

        })

        # Message Add
        po.message_post_with_view(
            'mail.message_origin_link',
            values={'self': po, 'origin': self},
            subtype_id=self.env.ref('mail.mt_note').id)

        self.po_id = po.id
