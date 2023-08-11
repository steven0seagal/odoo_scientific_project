from odoo import models, fields

class ScientificPublication(models.Model):
    _name = 'scientific.publication'
    _description = 'Publication'

    title = fields.Char(string='Title', required=True)
    authors_ids = fields.Many2many('scientific.researcher', string='Authors')
    journal_conference = fields.Char(string='Journal/Conference')
    doi = fields.Char(string='DOI')
    project_id = fields.Many2one('scientific.project', string='Project')
    experiment_ids = fields.Many2many('scientific.experiment', string='Experiments')
    task_ids = fields.Many2many('scientific.task', string='Tasks')