.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

================================
Sale Order Installation Transfer
================================

Enables transferring SOs to another Odoo installation


Configuration
=============
Define the following system parameters in the source installation that define
how to access the target installation, as well as what partner will be the 
owner of the created Sale Orders:

* sale_order_installation_transfer.url (e.g. https://example.com)
* sale_order_installation_transfer.port (e.g. 8069)
* sale_order_installation_transfer.database (e.g. live)
* sale_order_installation_transfer.username
* sale_order_installation_transfer.password
* sale_order_installation_transfer.customer_vat (e.g. FI12345678)

Create an user account matching those credentials in the target installation.
It is recommended to give as few access rights to the new account as possible
(i.e. Sale Order creation, and related necessary rights)

odoorpc python library is used for the transfer, so it needs to be installed
on the source installation server.

Usage
=====
* Go to Sale Order tree view, select some sales and click Action -> Transfer

Known issues / Roadmap
======================
- Multi-UoM currently not supported, the module assumes the use of Unit(s)

Credits
=======

Contributors
------------

* Timo Talvitie <timo.talvitie@tawasta.fi>

Maintainer
----------

This module is maintained by Oy Tawasta OS Technologies Ltd.
