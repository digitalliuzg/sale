# -*- coding: utf-8 -*-
from odoo import models, api, fields


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    # Related/computed helper fields here
    partner_id = fields.Many2one(
        string='Customer',
        comodel_name='res.partner',
        related='order_id.partner_id',
        store=True,
    )

    destination_country_id = fields.Many2one(
        string='Destination',
        comodel_name='res.country',
        related='order_id.partner_shipping_id.country_id',
        store=True,
    )
