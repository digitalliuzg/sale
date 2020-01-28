# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
from lxml import etree
import simplejson


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    state = fields.Selection(
        selection_add=[('rejected', _('Rejected'))]
    )

    rejection_reason = fields.Char(
        string="Reason for Rejection"
    )

    @api.multi
    def action_draft(self):
        orders = self.filtered(
            lambda s: s.state in ['rejected', 'cancel', 'sent'])
        orders.write({
            'rejection_reason': False,
            'state': 'draft',
            'procurement_group_id': False,
        })
        return super(SaleOrder, self).action_draft()

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False,
                        submenu=False):
        res = super(SaleOrder, self).fields_view_get(view_id=view_id,
                                                     view_type=view_type,
                                                     toolbar=toolbar,
                                                     submenu=submenu)

        if view_type in ['search', 'tree'] or not view_id:
            return res

        context = self._context or {}

        if context.get('active_id', False) and \
                self.browse(context.get('active_id')).state == 'rejected':
            if view_type == 'form':
                doc = etree.XML(res['arch'])
                for node in doc.xpath("//field"):
                    node.set('readonly', '1')
                    node.set('modifiers', simplejson.dumps({"readonly": True}))

                res['arch'] = etree.tostring(doc)

        return res
