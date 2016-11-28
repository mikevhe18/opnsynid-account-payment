# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class PaymentOrder(models.Model):
    _name = 'payment.order'
    _inherit = [
        'payment.order',
        'mail.thread'
    ]
