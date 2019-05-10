# -*- coding: utf-8 -*-


from odoo import api, fields, models


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def _get_picking_state(self):
        for order in self:
            if len(order.picking_ids) != 0:
                for picking_id in order.picking_ids:
                    for pick in picking_id:
                        if pick.state == 'done':
                            order.has_been_delivered = True

    @api.multi
    def _value_search(self,operator,value):
        recs = self.search([]).filtered(lambda x:x.has_been_delivered is False)
        if recs:
            return [('id','in',[x.id for x in recs])]

    has_been_delivered = fields.Boolean(
        string='Delivered',
        compute=_get_picking_state,
        search='_value_search'
        )
