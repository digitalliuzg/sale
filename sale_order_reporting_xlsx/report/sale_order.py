# -*- coding: utf-8 -*-


import logging
import textwrap
from odoo.report import report_sxw
from odoo.tools.translate import _
from odoo.tools import html2plaintext

_logger = logging.getLogger(__name__)

try:
    from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx
except ImportError:
    _logger.debug("report_xlsx not installed, Excel export non functional")

    class ReportXlsx(object):
        def __init(self, *args, **kwargs):
            pass

class SaleOrderXlsx(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, objects):
        workbook.set_properties({
            'comments': 'Createed with Python and XlsxWriter from Odoo 10.0'})
        sheet = workbook.add_worksheet(_('Sale Order'))
        sheet.set_landscape()
        sheet.set_zoom(60)
        sheet.fit_to_pages(1, 0)
        sheet.set_column(0, 1, 20)
        sheet.set_column(2, 10, 30)
        sheet.set_column(11, 11, 80)
        sheet.set_column(12, 12, 30)
        bold = workbook.add_format({'bold': True})
        title_style = workbook.add_format({'bold': True,
                                           'bg_color': '#CCE4FD',
                                           'bottom': 1})
        sheet_title = [_('Customer'),
                    _('Invoice Address'),
                    _('Delivery Address'),
                    _('Sale Order'),
                    _('Procountor Invoice number'),
                    _('Price (VAT 0%)'),
                    _('Price (VAT 24%)'),
                    _('Notes'),
                    _('Project'),
                    _('Sale Order Product type dimension'),
                    _('Invoice status'),
                    _('Internal message'),
                    _('Odoo invoice number'),
                    ]

        sheet.set_row(0, None, None, {'collapsed': 1})
        sheet.write_row(1, 0, sheet_title, title_style)
        sheet.freeze_panes

        message = ''

        ROW_H = 30

        i = 2
        for o in objects:
            message = ''
            ROW_H = 30
            j = 0
            msg_len = 0
            project_dimension = ''
            product_type_dimension = ''
            sheet.write(i, 0, o.partner_id.name or '', bold)
            sheet.write(i, 1, o.partner_invoice_id.name or '', bold)
            sheet.write(i, 2, o.partner_shipping_id.name or '', bold)
            sheet.write(i, 3, o.name or '', bold)

            procountors = ''
            k = 0

            if o.invoice_ids and (o.invoice_ids.mapped('procountor_number') != []):
                for procountor in o.invoice_ids.mapped('procountor_number'):
                    if procountor == 0:
                        continue
                    procountors += procountor
                    k += 1
                    if k == len(o.invoice_ids.mapped('procountor_number')):
                        break
                    procountors += '\n' + "test"
            sheet.write(i, 4, procountors or '', bold)

            sheet.write(i, 5, o.amount_untaxed or 0, bold)
            sheet.write(i, 6, o.amount_total or 0, bold)
            sheet.write(i, 7, o.note or '', bold)
            if o.related_project_id:
                for tag in o.related_project_id.tag_ids:
                    if tag.analytic_dimension_id.code == 'projektit':
                        project_dimension = tag.name
            sheet.write(i, 8, project_dimension  or '', bold)

            one_product_dimension = []

            for line in o.order_line:
                if line.analytic_tag_ids:
                    for tag in line.analytic_tag_ids:
                        if tag.analytic_dimension_id.code == 'tuotelajit':
                            one_product_dimension.append(tag.name)
            one_product_dimension = list(dict.fromkeys(one_product_dimension))
            if len(one_product_dimension) == 1:
                product_type_dimension = one_product_dimension[0]
            sheet.write(i, 9, product_type_dimension or '', bold)
            sheet.write(i, 10, o.invoice_status or '', bold)

            for msg in o.message_ids:
                if msg.message_type == 'comment':
                    msg_len += 1
            for msg in o.message_ids:
                if msg.message_type == 'comment':
                    while j < msg_len:
                        ROW_H += 45
                        for x in range(1, 10):
                            if len(html2plaintext(msg.body)) > 70*x:
                                ROW_H += 10

                        if msg_len == 1:
                            message += _('Note by: ') + msg.author_id.name + \
                            '\n' + _('Date: ') + msg.date + '\n' + _('Comment: ') \
                            + '\n'.join(textwrap.wrap(html2plaintext(msg.body)))
                            break
                        j += 1
                        if j == msg_len:
                            message += _('Note by: ') + msg.author_id.name + '\n' \
                            + _('Date: ') + msg.date + '\n' + _('Comment: ') + \
                            '\n'.join(textwrap.wrap(html2plaintext(msg.body)))
                            break
                        else:
                            message += _('Note by: ') + msg.author_id.name + '\n' \
                            + _('Date: ') + msg.date + '\n' + _('Comment: ') + \
                            '\n'.join(textwrap.wrap(html2plaintext(msg.body))) + '\n' + 10*'-' + '\n'

            sheet.set_row(i, ROW_H, None)
            sheet.write(i, 11, message or '', bold)

            invoices = ''
            k = 0

            if o.invoice_ids:
                for invoice in o.invoice_ids.mapped('number'):
                    invoices += invoice
                    k += 1
                    if k == len(o.invoice_ids.mapped('number')):
                        break
                    invoices += '\n'
            sheet.write(i, 12, invoices or '', bold)
            i += 1

SaleOrderXlsx('report.sale.order.xlsx', 'sale.order',
                parser=report_sxw.rml_parse)

