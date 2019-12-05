
from odoo import models, fields


class ResPartner(models.Model):

    _inherit = 'res.partner'

    info_verification_date = fields.Date('Partner info verified on')
