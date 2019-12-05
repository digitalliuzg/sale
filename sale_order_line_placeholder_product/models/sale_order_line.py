from odoo import api, fields, models


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    old_product_id = fields.Text(string="Old Product Id", default="")

    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):

        if self._origin.product_id.additional_code:
            self.old_product_id = self._origin.name
        else:
            self.old_product_id = ""

        res = super(SaleOrderLine, self).product_id_change()

        if self.old_product_id:
            nextline = "\n"
        else:
            nextline = ""

        if self.product_id.description_sale:
            self.name = "%s\n%s%s%s" % (
                self.product_id.name, self.product_id.description_sale,
                nextline, self.old_product_id
            )
        elif self.product_id:
            self.name = "%s%s%s" % (
                self.product_id.name, nextline,
                self.old_product_id
            )

        return res
