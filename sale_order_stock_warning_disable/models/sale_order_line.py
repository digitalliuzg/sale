# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class SaleOrderLine(osv.osv):

    _inherit = 'sale.order.line'

    def product_id_change_with_wh(self, cr, uid, ids, pricelist, product, qty=0,
            uom=False, qty_uos=0, uos=False, name='', partner_id=False,
            lang=False, update_tax=True, date_order=False, packaging=False, fiscal_position=False, flag=False, warehouse_id=False, context=None):

        res = super(SaleOrderLine, self).product_id_change_with_wh(cr, uid, ids, pricelist, product, qty,
            uom, qty_uos, uos, name, partner_id, lang, update_tax, date_order, packaging, fiscal_position, flag, warehouse_id, context)

        # If a warning was added to dictionary in sale_stock, remove it before returning
        res.pop('warning', None)

        return res