from odoo import models, fields, api

class CategoryInherit(models.Model):
    _inherit = 'product.category'

    code = fields.Char(string="Code", size=5)


class ProductInherit(models.Model):
    _inherit = 'product.product'

    code_id = fields.Char(string="Codex", related='categ_id.code')


    @api.model
    def create(self, vals):
        if 'categ_id' in vals:
            category = self.env['product.category'].browse(vals['categ_id'])
            code_details = str(category.code)

        sequence_id = self.env['ir.sequence'].next_by_code('product.sequences')
        vals['default_code'] = code_details + sequence_id
        return super(ProductInherit, self).create(vals)
