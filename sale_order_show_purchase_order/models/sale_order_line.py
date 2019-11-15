# -*- coding: utf-8 -*-


from odoo import api, fields, models


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def _get_purchase_ids(self):
        if self.procurement_group_id:
            proc_group = self.procurement_group_id.procurement_ids
            self.purchase_order_ids = proc_group.mapped('purchase_id')

    purchase_order_ids = fields.Many2many(
        compute=_get_purchase_ids,
        comodel_name='purchase.order',
        string='Purchase Orders'
        )
