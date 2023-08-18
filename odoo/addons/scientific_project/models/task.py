from odoo import models, fields



class ScientificTask(models.Model):
    _name = 'scientific.task'
    _description = 'Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, track_visibility='onchange')
    description = fields.Text(string='Description', track_visibility='onchange')
    assigned_to_ids = fields.Many2many('scientific.researcher', string='Assigned to', track_visibility='onchange')
    start_date = fields.Date(string='Start Date', track_visibility='onchange')
    end_date = fields.Date(string='End Date', track_visibility='onchange')
    status = fields.Selection(
        [('planning', 'Planning'), ('in_progress', 'In Progress'), ('completed', 'Completed'),('cancelled', 'Cancelled')], string='Status', default='planning', track_visibility='onchange')
    project_id = fields.Many2one('scientific.project', string='Project', track_visibility='onchange')

    document_id = fields.Many2one('scientific.document', string='Document', track_visibility='onchange')
