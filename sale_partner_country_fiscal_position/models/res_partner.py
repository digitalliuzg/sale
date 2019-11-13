from odoo import api, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    @api.model_create_multi
    def create(self, vals_list):
        """Creates a partner with a Fiscal Position based on country_id"""
        for vals in vals_list:
            if vals.get('country_id') and not vals.get('property_account_position_id'):
                account_position_with_vat = self.env['ir.model.data'].search([
                    ('module', '=', 'l10n_fi_liikekirjuri'),
                    ('model', '=', 'account.fiscal.position'),
                    ('name', 'like', 'account_position_with_vat'),
                ], limit=1)

                account_position_y = self.env['ir.model.data'].search([
                    ('module', '=', 'l10n_fi_liikekirjuri'),
                    ('model', '=', 'account.fiscal.position'),
                    ('name', 'like', 'account_position_y'),
                ], limit=1)

                account_position_ey = self.env['ir.model.data'].search([
                    ('module', '=', 'l10n_fi_liikekirjuri'),
                    ('model', '=', 'account.fiscal.position'),
                    ('name', 'like', 'account_position_ey'),
                ], limit=1)

                if int(vals['country_id']) == self.env['res.country'].search(
                        [('id', '=', self.env.ref('base.fi').id)]).id:
                    vals['property_account_position_id'] = self.env.ref(
                        account_position_with_vat.complete_name).id
                elif int(vals['country_id']) in self.env.ref(
                        'base.europe').country_ids.ids:
                    vals['property_account_position_id'] = self.env.ref(
                        account_position_y.complete_name).id
                else:
                    vals['property_account_position_id'] = self.env.ref(
                        account_position_ey.complete_name).id

        return super(ResPartner, self).create(vals_list)
