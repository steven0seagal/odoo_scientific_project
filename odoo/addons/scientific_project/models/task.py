from odoo import models, fields

class Task(models.Model):
    _name = 'scientific.task'
    _description = 'Task'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    description = fields.Text(string='Description')
    project_id = fields.Many2one('scientific.project', string='Project')
    user_id = fields.Many2one('res.users', string='Assigned To')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft')