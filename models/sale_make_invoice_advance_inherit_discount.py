from odoo import fields, models


class InvoiceDiscount(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    additional_discount = fields.Float(string="Additional Discount")

    def _create_invoices(self, sale_orders):
        invoices = super()._create_invoices(sale_orders)
        for invoice in invoices:
            self._add_discount_line(invoice)
        return invoices

    def _add_discount_line(self, invoice):

        """This function is used to create a new line with Additional Discount field
        on the account.move.line model"""

        account_move_line = self.env['account.move.line']

        vals = {
            'name': 'Additional Discount',
            'move_id': invoice.id,
            'price_unit': -self.additional_discount,  # Negative value for discount
            'quantity': 1.0,
        }

        account_move_line.create(vals)

