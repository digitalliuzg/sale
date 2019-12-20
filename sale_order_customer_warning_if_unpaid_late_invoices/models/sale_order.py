# -*- coding: utf-8 -*-
from odoo import api, models, _
from datetime import datetime


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def onchange_partner_id_warning(self):
        res = super(SaleOrder, self).onchange_partner_id_warning()
        today = datetime.now().date()
        title = _("Warning for %s") % self.partner_id.name

        invoices = self.partner_id.invoice_ids.search([
            ('state', '=', 'open'),
            ('date_due', '<', today),
            ('partner_id', '=', self.partner_id.id)
        ])

        if len(invoices) == 1:
            message = _("Customer has one late unpaid invoice.")
        else:
            message = _("Customer has %s late unpaid invoices.") % len(invoices)

        warning = {
            'title': title,
            'message': message,
        }

        if invoices:
            return {'warning': warning}
        else:
            return res
