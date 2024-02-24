from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property'

    name = fields.Char(required=True, size=4)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_selling_date = fields.Date()
    is_late = fields.Boolean()
    expected_price = fields.Float(digits=(0, 5))
    selling_price = fields.Float()
    bedroom = fields.Integer()
    ref = fields.Char(default='New', readonly=1)
    living_area = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    dff =fields.Float(compute="_compute_dff", store=1)
    owner_id = fields.Many2one('owner', string="Owner")
    owner_address = fields.Char(related='owner_id.address', readonly=0)
    owner_phone = fields.Char(related='owner_id.phone', readonly=0)
    tag_ids = fields.Many2many('tag')
    garden_area = fields.Integer()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('closed', 'Closed'),
        ('eat', 'Eat'),
        ('sold', 'Sold')

    ])
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], default='east')

    _sql_constraints = [
        ('unique_name', 'unique("name")', 'Please insert Name')
    ]



    def eat_action(self):
        for rec in self:
            rec.write({
                'state': 'eat'
            })

    def action_draft(self):
        for rec in self:
            rec.state = "draft"
    def action_closed(self):
        for rec in self:
            rec.state = "closed"

    def action_pending(self):
        for rec in self:
            rec.write({
                'state': 'pending'
            })

    @api.depends('expected_price', 'selling_price','owner_id.phone')
    def _compute_dff(self):
        for rec in self:
            print('change done')
            rec.dff = rec.expected_price - rec.selling_price



    @api.constrains('bedroom')
    def _check_bedroom_zero(self):
        for rec in self:
            if rec.bedroom == 0:
                raise ValidationError("please add bedroom number")

    def check_expected_selling_date(self):
        property_ids = self.search([])
        for rec in property_ids:
            if rec.expected_selling_date and rec.expected_selling_date < fields.date.today():
                rec.is_late = True


    @api.model
    def create(self, vals):
        res = super(Property, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('property_sqe')
        return res

    def action_open_change_state_wizard(self):
        action = self.env['ir.actions.server']._for_xml_id('app_one.change_state_wizard_action')
        action['context'] = {'default_property_id': self.id}
        return action






