

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class SaleOrder(models.Model):

    # 1. Private attributes
    _inherit = 'sale.order'

    # 2. Fields declaration
    migrated = fields.Boolean('Migrated')
    migrated_date = fields.Datetime('Migration Date')
    migrated_comment = fields.Char('Migration Comment')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
