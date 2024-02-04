from odoo import models, fields, api

class CategoryInherit(models.Model):
    _inherit = 'product.category'

    code = fields.Char(string="Code", size=5)
    sequence_id = fields.Many2one('ir.sequence')

    @api.model
    def generate_sequence(self, category_name):
        sequence_code = f'category_{category_name}_sequence'
        sequence_prefix = self.code
        sequence = self.env['ir.sequence'].create({
            'name': sequence_code,
            'code': sequence_code,
            'prefix': sequence_prefix,
            'padding': 4,
        })
        new_category = self.create({
            'name': category_name,
            'code': f'cat_{category_name}',
            'sequence_id': sequence.id,
        })
        return sequence

    def button_generate_sequence(self):
        category_name = 'New Category'
        generated_sequence = self.generate_sequence(category_name)
        self.sequence_id = generated_sequence


class ProductInherit(models.Model):
    _inherit = 'product.product'


    @api.model
    def create(self, vals):
        if 'categ_id' in vals:
            category = self.env['product.category'].browse(vals['categ_id'])
            sequence_number = str(category.sequence_id.next_by_id())

            vals['default_code'] = sequence_number

        return super(ProductInherit, self).create(vals)
