# -*- coding: utf-8 -*-
from openerp import fields, models


class SaleOrder(models.Model):

    _inherit = 'sale.order'
    
    date_installation_transfer = fields.Datetime(
        string='Transfer Date',
        help='Date when sale information has been transferred to another '
             'Odoo installation'
    )
