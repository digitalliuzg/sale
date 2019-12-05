##############################################################################
#
#    Copyright 2017 Tawasta OS Technologies
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Customer Contact for Sale Orders',
    'category': 'Sales',
    'version': '12.0.1.0.4',
    'installable': True,
    'author': 'Oy Tawasta Technologies Ltd.',
    'license': 'AGPL-3',
    'website': 'https://github.com/Tawasta/sale',
    'depends': [
        'res_partner_recursion',
        'sale',
    ],
    'data': [
        'views/account_invoice.xml',
        'views/sale_order.xml',
    ],
}
