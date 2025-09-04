from odoo import models, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.depends('name', 'default_code')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.name or ''