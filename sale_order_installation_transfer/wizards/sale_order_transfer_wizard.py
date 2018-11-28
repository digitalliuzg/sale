# -*- coding: utf-8 -*-
from openerp import models, fields, api, exceptions, _
from datetime import datetime
import odoorpc


class SaleOrderTransferWizard(models.TransientModel):

    _name = 'sale.order.transfer.wizard'

    @api.multi
    def validate_connection(self):

        ir_config = self.env['ir.config_parameter']
        errors = []

        # Catch both cases: the config parameter is not yet set or it has been
        # deleted
        if ir_config.get_param(
            'sale_order_installation_transfer.url', False) in [False, '-']:
            errors.append(_('Installation URL missing from system parameters'))

        if ir_config.get_param(
            'sale_order_installation_transfer.port', False) in [False, '-']:
            errors.append(_('Installation port missing from system parameters'))

        if ir_config.get_param(
            'sale_order_installation_transfer.database', False) in [False, '-']:
            errors.append(_('Database name missing from system parameters'))

        if ir_config.get_param(
            'sale_order_installation_transfer.username', False) in [False, '-']:
            errors.append(_('Username missing from system parameters'))

        if ir_config.get_param(
            'sale_order_installation_transfer.password', False) in [False, '-']:
            errors.append(_('Password missing from system parameters'))

        if errors:
            msg = '\n'.join(errors) or False
            raise exceptions.except_orm(_('Error'), msg)

    @api.multi
    def prepare_sale_order(self, target_odoo):

        target_res_partner = target_odoo.env['res.partner']
        args = [('vat', '=', self.target_customer_vat)]
        matching_partners = target_res_partner.search(args)

        if not matching_partners:
            msg = _('No customer found with VAT %s') % self.target_customer_vat
            raise exceptions.except_orm(_('Error'), msg)
        elif len(matching_partners) > 1:
            msg = _('Multiple customers found with VAT %s') \
                % self.target_customer_vat
            raise exceptions.except_orm(_('Error'), msg)
        else:
            partner_id = matching_partners[0]

        return {
            'partner_id': partner_id
        }

    @api.multi
    def prepare_sale_order_line(self, target_odoo, line, sale_id):

        target_product = target_odoo.env['product.product']
        args = [('default_code', '=', line.product_id.default_code)]
        matching_products = target_product.search(args)

        if not matching_products:
            msg = _('No product found with internal reference %s') \
                % line.product_id.default_code
            raise exceptions.except_orm(_('Error'), msg)
        elif len(matching_products) > 1:
            msg = _('Multiple products found with internal reference %s') \
                % line.product_id.default_code
            raise exceptions.except_orm(_('Error'), msg)
        else:
            product_id = matching_products[0]        

        return {
            'order_id': sale_id,
            'product_id': product_id,
            'product_uom_qty': line.product_uom_qty,  # NOTE: default UOM used
            'sequence': line.sequence,
            'name': line.name
        }

    @api.multi
    def transfer_sale_orders(self):
        self.ensure_one()
        self.validate_connection()

        selected_sale_ids = self._context.get('active_ids', [])

        ir_config = self.env['ir.config_parameter']

        url = ir_config.get_param(
            'sale_order_installation_transfer.url'
        )

        port = ir_config.get_param(
            'sale_order_installation_transfer.port'
        )

        username = ir_config.get_param(
            'sale_order_installation_transfer.username'
        )

        dbname = ir_config.get_param(
            'sale_order_installation_transfer.database'
        )

        password = ir_config.get_param(
            'sale_order_installation_transfer.password'
        )

        target_odoo = odoorpc.ODOO(url, port=port)
        target_odoo.login(dbname, username, password)
        target_sale_order = target_odoo.env['sale.order']
        target_sale_order_line = target_odoo.env['sale.order.line']

        # Go through all the SOs selected by the user
        for sale in self.env['sale.order'].browse(selected_sale_ids):

            # Create the sale
            sale_vals = self.prepare_sale_order(target_odoo)
            sale_res = target_sale_order.create(sale_vals)

            # Create lines for the sale
            for line in sale.order_line:
                line_vals = self.prepare_sale_order_line(target_odoo,
                                                         line,
                                                         sale_res)
                target_sale_order_line.create(line_vals)

            # Mark the sale as transferred
            sale.date_installation_transfer = datetime.now()

        # Show the same wizard in different state
        self.state = 'step_results'
        return {
            'type': 'ir.actions.act_window',
            'name': _('Transfer Sale Orders'),
            'res_model': 'sale.order.transfer.wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'views': [(False, 'form')],
            'target': 'new',
        }

    @api.model
    def _get_default_target_url(self):
        return self.env['ir.config_parameter'].get_param(
            'sale_order_installation_transfer.url', '-')

    @api.model
    def _get_default_target_username(self):
        return self.env['ir.config_parameter'].get_param(
            'sale_order_installation_transfer.username', '-')

    @api.model
    def _get_default_target_customer_vat(self):
        return self.env['ir.config_parameter'].get_param(
            'sale_order_installation_transfer.customer_vat', '-')        

    state = fields.Selection(
        selection=[('step_information', 'Information'),
                   ('step_results', 'Results')],
        string='State',
        default='step_information'
    )

    target_url = fields.Char(
        string='Target installation',
        default=_get_default_target_url,
        help='Target where the sales information will be transferred',
    )

    target_username = fields.Char(
        string='User account',
        default=_get_default_target_username,
        help='User account to transfer with'
    )

    target_customer_vat = fields.Char(
        string='Customer VAT',
        default=_get_default_target_customer_vat,
        help='The partner with this VAT will be used as the customer',
        required=True,
    )
