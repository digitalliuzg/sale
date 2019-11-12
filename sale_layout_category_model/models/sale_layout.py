# -*- coding: utf-8 -*-


from odoo import fields, models
from itertools import groupby


class SaleLayoutCategory(models.Model):

    _name = 'sale_layout.category'
    _order = 'sequence, id'

    name = fields.Char('Name', required=True)
    sequence = fields.Integer('Sequence', required=True, default=10)
    subtotal = fields.Boolean('Add subtotal', default=True)
    separator = fields.Boolean('Add separator', default=True)
    pagebreak = fields.Boolean('Add pagebreak', default=False)


def grouplines(self, ordered_lines, sortkey):
    """Return lines from a specified invoice or sale order grouped
    by category"""
    grouped_lines = []
    for key, valuesiter in groupby(ordered_lines, sortkey):
        group = {}
        group['category'] = key
        group['lines'] = list(v for v in valuesiter)

        if 'subtotal' in key and key.subtotal is True:
            group['subtotal'] = sum(line.price_subtotal for line in
                                    group['lines'])
        grouped_lines.append(group)

    return grouped_lines


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    def sale_layout_lines(self, invoice_id=None, context=None):
        """
        Returns invoice lines from a specified invoice ordered by
        sale_layout_category sequence. Used in sale_layout module.
        :Parameters:
            -'invoice_id' (int): specify the concerned invoice.
        """
        ordered_lines = self.browse(invoice_id, context=context).\
            invoice_line_ids
        # We chose to group first by category model and, if not present,
        # by invoice name
        sortkey = lambda x: x.sale_layout_cat_id \
            if x.sale_layout_cat_id else ''

        return grouplines(self, ordered_lines, sortkey)


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    def sale_layout_lines(self, order_id=None, context=None):
        """
        Returns order lines from a specified sale ordered by
        sale_layout_category sequence. Used in sale_layout module.
        :Parameters:
            -'order_id' (int): specify the concerned sale order.
        """
        ordered_lines = self.browse(order_id, context=context).order_line
        sortkey = lambda x: x.sale_layout_cat_id \
            if x.sale_layout_cat_id else ''

        return grouplines(self, ordered_lines, sortkey)
