
##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2018 Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

{
    'name': 'Sale Order to Purchase Request',
    'summary': "Create Purchase Requests of sold products and BOM components",
    'category': 'Sales',
    'version': '12.0.1.1.1',
    'website': 'https://github.com/Tawasta/sale',
    'author': 'Oy Tawasta Technologies Ltd.',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'mrp_bom_raw_material_quantities',
        'purchase_request_analytic_account_location',
        'sale_order_project_location_in_header',
    ],
    'data': [
        'views/sale_config_settings.xml',
        'views/sale_order.xml',
    ],
}
