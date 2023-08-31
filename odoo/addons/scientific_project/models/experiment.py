from odoo import models, fields

class ScientificExperiment(models.Model):
    _name = 'scientific.experiment'
    _description = 'Experiment'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    status = fields.Selection([('planning', 'Planning'), ('in_progress', 'In Progress'), ('completed', 'Completed')], string='Status')
    results = fields.Text(string='Results')
    project_id = fields.Many2many('scientific.project', string='Project')