
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Partner
    partner_id_street = fields.Char(
        string='Street',
        related='partner_id.street',
    )

    partner_id_street2 = fields.Char(
        string='Street2',
        related='partner_id.street2',
    )

    partner_id_zip = fields.Char(
        string='Zip',
        related='partner_id.zip',
    )

    partner_id_city = fields.Char(
        string='City',
        related='partner_id.city',
    )

    # Invoicing
    partner_invoice_id_street = fields.Char(
        string='Street',
        related='partner_invoice_id.street',
    )

    partner_invoice_id_street2 = fields.Char(
        string='Street2',
        related='partner_invoice_id.street2',
    )

    partner_invoice_id_zip = fields.Char(
        string='Zip',
        related='partner_invoice_id.zip',
    )

    partner_invoice_id_city = fields.Char(
        string='City',
        related='partner_invoice_id.city',
    )

    # Shipping
    partner_shipping_id_street = fields.Char(
        string='Street',
        related='partner_shipping_id.street',
    )

    partner_shipping_id_street2 = fields.Char(
        string='Street2',
        related='partner_shipping_id.street2',
    )

    partner_shipping_id_zip = fields.Char(
        string='Zip',
        related='partner_shipping_id.zip',
    )

    partner_shipping_id_city = fields.Char(
        string='City',
        related='partner_shipping_id.city',
    )
