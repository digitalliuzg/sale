# -*- coding: utf-8 -*-


from odoo import api, models, _
from datetime import datetime


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def onchange_partner_id_warning(self):

        res = super(SaleOrder, self).onchange_partner_id_warning()

        warning = {}

        title = _("Warning for %s") % self.partner_id.name
        message = "%s" % _("Customer has late unpaid invoice(s).")

        today = datetime.now().date()

        invoices = self.partner_id.invoice_ids.search([
            ('state', '!=', 'paid'),
            ('date_due', '<', today),
            ('partner_id', '=', self.partner_id.id)
        ])

        warning = {
            'title': title,
            'message': message,
        }

        if invoices:
            return {'warning': warning}
        else:
            return res
