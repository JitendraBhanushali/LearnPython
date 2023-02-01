# Main
# This is how to create a order in another model

    #     def action_create_purchase_order(self):
    #         po = self.env['purchase.order'].create({
    #             "partner_id": self.partner_id.id,
    #         })
    #         for line in self.order_line:
    #             po_line = self.env['purchase.order.line'].create({
    #                 'order_id': po.id,
    #                 'name': 'name',
    #                 'product_id': line.product_id.id,
    #                 'price_unit': line.price_unit,
    #                 'product_qty': line.product_uom_qty,
    #                 'product_uom': line.product_uom.id,
    #             })


# Practice

# print("name----", self.order_line.name)
# print("product_id----", self.order_line.product_id.id)
# print("price_unit----", self.order_line.price_unit)


#     # 'order_line': [(0, 0, {
#     #         'name': self.order_line.name,
#     #         'product_id': self.order_line.product_id.id,
#     #     }),
#     #     (0, 0, {
#     #         'name': self.order_line.name,
#     #         'product_id': self.order_line.product_id.id,
#     # })]
#     # 'order_line': [(0, 0, {
#     #     'name': self.order_line.name,
#     #     'product_id': self.order_line.product_id.id,
#     #     'price_unit': self.order_line.price_unit,
#     #     'product_qty': self.order_line.product_uom_qty,
#     #     'product_uom': self.order_line.product_uom.id,
#     # })]
