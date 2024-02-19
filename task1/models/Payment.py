from odoo import models, fields, api

class PaymentTask(models.Model):
    _name = 'task.one'
    _description = 'Paid or unpaid'

    sale_order_id = fields.Many2one('sale.order', string='Sales Order')

    paid_or_unpaid = fields.Selection(
        [('paid', 'Paid'), ('unpaid', 'Unpaid')],
        string='Paid or Unpaid',
        default='unpaid',
    )

    customer_or_company = fields.Selection(
        [('customer', 'Customer'), ('company', 'Company')],
        string='Customer or Company',
        default='Company',
        invisible=True
    )

    def open_order_lines(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sales Order',
            'res_model': 'sale.order',
            'res_id': self.sale_order_id.id,
            'view_mode': 'form',
            'target': 'current',
        }