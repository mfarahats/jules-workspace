from odoo import models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.depends('name', 'default_code')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.name or ''