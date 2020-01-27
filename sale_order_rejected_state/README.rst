.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===============================================
Sale Order Reject-state and added functionality
===============================================

Sale order can be set to Rejected-state after which fields turn to
readonly-state. Rejected Sale orders can be set to draft again if needed.

Reason for rejecting a sale order is needed to give which is assigned to order's
appropriate field. Setting sale order's state to draft again will change that
field's value to False.

Configuration
=============
No special configuration needed.

Usage
=====
Install from Apps

Known issues / Roadmap
======================
Module does not interfere with Sale Order's internal logic.

Credits
=======

Contributors
------------

* Aleksi Savijoki <aleksi.savijoki@tawasta.fi>
* Timo Kekäläinen <timo.kekalainen@tawasta.fi>
* Valtteri Lattu <valtteri.lattu@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
