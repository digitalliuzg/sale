# -*- coding: utf-8 -*-
from odoo import models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    def _get_sale_order_line(self, vals=None):
        """ Overrides SO line matching.
        When creating a new invoice using analytic account, no matching
        SO line is searched/matched """
        result = dict(vals or {})

        return result
