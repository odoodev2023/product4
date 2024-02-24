from odoo import models, fields, api



class Property(models.Model):
    _inherit = 'sale.order'



    def action_confirm(self):
        res = super('sale.order').action_confirm()
        print('inherit Test')
        return res