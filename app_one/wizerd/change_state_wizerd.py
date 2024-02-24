from odoo import fields, models


class ChangeState(models.TransientModel):
    _name = 'change.state'



    property_id = fields.Many2one('property')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
    ])
    reason = fields.Char()


    def action_confirm(self):
        print("insert confirm")


