# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    po_count = fields.Integer(string="PO Count", compute='_compute_po_count')
    po_id = fields.Many2one(
        comodel_name="purchase.order",
        string="Purchase Order",
        copy=False)

    def _compute_po_count(self):
        for order in self:
            order.po_count = len(order.po_id)

            # print("This is po_id-----", order.po_id)
            # print("This is po_count-----", order.po_count)
            # print("This is order-----", order)


    def action_view_po(self):
        # print(">>>>>>>>>>>>self", self)
        # print(">>>>>>>>>>>>po_id", self.po_id)

        po_id = self.po_id
        # print("Add PO id name----", po_id)

        action = self.env['ir.actions.actions']._for_xml_id('purchase.purchase_rfq')

        # print("This is a action ===", action)
        # print("This is a condition----", len(po_id) > 1)
        # print("This is a Equal Condition", len(po_id) == 1)
        if len(po_id) > 1:
            action['domain'] = [('id', 'in', po_id.id)]
        elif len(po_id) == 1:
            form_view = [(self.env.ref('purchase.purchase_order_form').id, 'form')]
            # print("This is a form---", form_view)

            if 'views' in action:
                action['views'] = form_view + [(state, view) for state, view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = po_id.id
            # print("This is action ----", action)

        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action

    def action_create_purchase_order(self):
        # print("-----")
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
        # print("This is a create_po", create_po_order_line)

        po = self.env['purchase.order'].create({
            "partner_id": self.partner_id.id,
            'order_line': create_po_order_line,

        })
        self.po_id = po.id
        # print("This is a main po_id----", self.po_id)



