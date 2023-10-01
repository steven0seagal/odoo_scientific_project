from odoo import models, fields

class ScientificSchedule(models.Model):
    _name = 'scientific.schedule'
    _description = 'Schedule'

    equipment_id = fields.Many2one('scientific.equipment', string='Equipment')
    researcher_id = fields.Many2one('scientific.researcher', string='Researcher')
    start_time = fields.Datetime(string='Start Time')
    end_time = fields.Datetime(string='End Time')
    notes = fields.Text(string='Notes')
    experiment_id = fields.Many2one('scientific.experiment', string='Experiment')
