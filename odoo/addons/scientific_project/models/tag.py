from odoo import models, fields


class ScientificResearcherTags(models.Model):
    _name = 'scientific.tags'
    _description = 'Researcher Tags'

    name = fields.Char(string='Name', required=True)
    researcher_ids = fields.Many2many('scientific.researcher', string='Researchers')
    color = fields.Integer(string='Color Index')