# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
from odoo import exceptions
import logging
_logger = logging.getLogger(__name__)


class SaleOrderWizardRejected(models.TransientModel):

    _name = 'sale.order.wizard.reject'
    _description = 'Reject Sale Order'

    reason_for_rejection = fields.Char(
        string='Reason for Rejection'
    )

    @api.multi
    def update_rejection_reason(self):
        self.ensure_one()
        if not self.reason_for_rejection:
            raise exceptions.ValidationError(
                _('Fill in the required information!'))
        _logger.debug('Update Sale Order %s' % self.reason_for_rejection)

        active_id = self._context['active_id']

        current_sale = self.env['sale.order'].\
            browse(active_id)

        vals = {}
        if self.reason_for_rejection:
            vals['rejection_reason'] = self.reason_for_rejection
            vals['state'] = 'rejected'
        if vals:
            current_sale.update(vals)
        return True
