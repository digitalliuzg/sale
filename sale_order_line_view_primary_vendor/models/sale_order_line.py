# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    # Related/computed helper fields here
    primary_vendor_id = fields.Many2one(
        comodel_name='res.partner',
        related='product_id.primary_vendor_id',
        store=True,
    )
