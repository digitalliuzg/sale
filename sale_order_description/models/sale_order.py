# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    description = fields.Text(
        string='Description',
        help='Internal notes'
    )

    @api.multi
    def _prepare_invoice(self):
        vals = super(SaleOrder, self)._prepare_invoice()

        vals['description'] = self.description

        return vals
