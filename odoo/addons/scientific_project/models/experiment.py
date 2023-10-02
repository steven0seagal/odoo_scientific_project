from odoo import models, fields

class ScientificExperiment(models.Model):
    _name = 'scientific.experiment'
    _description = 'Experiment'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    status = fields.Selection([('planning', 'Planning'), ('in_progress', 'In Progress'), ('completed', 'Completed')], string='Status')
    project_id = fields.Many2one('scientific.project', string='Project')
    introduction = fields.Text(string='Introduction')
    hypothesis = fields.Text(string='Hypothesis')
    results = fields.Text(string='Results')
    conclusion = fields.Text(string='Conclusion')
    methodology = fields.Text(string='Methodology')
    raport_created = fields.Boolean(string='Raport Created',default=False)
    notes = fields.Text(string='Notes')
    document_id = fields.Many2many('scientific.document', string='Document')
    assigned_to_ids = fields.Many2many('scientific.researcher', string='Assigned to')
    equipment_ids = fields.Many2many('scientific.equipment', string='Equipment')