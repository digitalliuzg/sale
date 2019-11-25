from odoo import api, models, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):
        self.check_code()

        return super(SaleOrder, self).action_confirm()

    @api.multi
    def check_code(self):
        for order in self:
            for line in order.order_line:
                if line.product_id.additional_code:
                    raise ValidationError(_(
                        "Please replace the placeholder product %s")
                        % line.product_id.name)
