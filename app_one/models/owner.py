from odoo import models, fields, api

class Owner(models.Model):
    _name = 'owner'
    _description = 'Owner Property'
    _inherit = ['mail.thread','mail.activity.mixin']


    name = fields.Char()
    phone = fields.Char()
    address = fields.Char(tracking=1)



    @api.model
    def create_record(self,vals):
        record_copy = self.env['owner'].search([('name','=','ahmed ali')])
        print_id = record_copy.browse(record_copy)
        print(print_id)
        record_copy.copy()


