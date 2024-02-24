from odoo import models, fields, api

class Tag(models.Model):
    _name = 'tag'


    name = fields.Char()
    active = fields.Boolean(default=True)
    print_record = fields.Integer(comute="action_search", string="print id")
    property_id = fields.Many2one('property')


    def action_search(self):
        for rec in self:
            res = self.env['property'].search_count([('bedroom','=','5')])
            self.print_record = res
            print("task action")


