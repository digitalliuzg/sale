# -*- coding: utf-8 -*-


from odoo import api, fields, models


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'
    _order = 'order_id, categ_sequence, sale_layout_cat_id, sequence, id'

    sale_layout_cat_id = fields.Many2one(
        'sale_layout.category',
        string='Section'
    )

    categ_sequence = fields.Integer(
        related='sale_layout_cat_id.sequence',
        string='Layout Sequence',
        store=True
    )

    #  Store is intentionally set in order to keep the "historic" order.

    def _prepare_order_line_invoice_line(self, cr, uid, line,
                                         account_id=False, context=None):
        """Save the layout when converting to an invoice line."""
        invoice_vals = super(SaleOrderLine, self).\
            _prepare_order_line_invoice_line(cr, uid, line,
                                             account_id=account_id,
                                             context=context)
        if line.sale_layout_cat_id:
            invoice_vals['sale_layout_cat_id'] = line.sale_layout_cat_id.id
        if line.categ_sequence:
            invoice_vals['categ_sequence'] = line.categ_sequence
        return invoice_vals

    @api.multi
    def _prepare_invoice_line(self, qty):
        """
        Prepare the dict of values to create the
        new invoice line for a sales order line.
        :param qty: float quantity to invoice
        """
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        if self.sale_layout_cat_id:
            res['sale_layout_cat_id'] = self.sale_layout_cat_id.id
        return res
