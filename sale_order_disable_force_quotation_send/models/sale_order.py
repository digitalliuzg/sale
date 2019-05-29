# -*- coding: utf-8 -*-
from odoo import models, api


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def force_quotation_send(self):
        # Disable force quotation send completely
        return True
