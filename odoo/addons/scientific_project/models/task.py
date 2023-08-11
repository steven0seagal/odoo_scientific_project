from odoo import models, fields



class ScientificTask(models.Model):
    _name = 'scientific.task'
    _description = 'Task'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    assigned_to_ids = fields.Many2many('scientific.researcher', string='Assigned to')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    status = fields.Selection(
        [('planning', 'Planning'), ('in_progress', 'In Progress'), ('completed', 'Completed'),('cancelled', 'Cancelled')], string='Status')
    project_id = fields.Many2one('scientific.project', string='Project')

    document_id = fields.Many2one('scientific.document', string='Document')
