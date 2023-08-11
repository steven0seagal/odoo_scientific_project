from odoo import models, fields

class ScientificFunding(models.Model):
    _name = 'scientific.funding'
    _description = 'Funding'

    source = fields.Char(string='Source', required=True)
    budget = fields.Float(string='Budget')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    project_id = fields.Many2one('scientific.project', string='Project')