from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ScientificTask(models.Model):
    _name = 'scientific.task'
    _description = 'Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'start_date desc, name'

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text(string='Description', tracking=True)
    assigned_to_ids = fields.Many2many('scientific.researcher', string='Assigned to', tracking=True)
    start_date = fields.Date(string='Start Date', tracking=True)
    end_date = fields.Date(string='End Date', tracking=True)
    status = fields.Selection([
        ('planning', 'Planning'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='planning', tracking=True)
    project_id = fields.Many2one('scientific.project', string='Project', tracking=True)
    document_id = fields.Many2many('scientific.document', string='Document', tracking=True)
    notes = fields.Text(string='Notes', tracking=True)

    @api.constrains('start_date', 'end_date')
    def _check_date_range(self):
        """Validate that end date is not before start date"""
        for record in self:
            if record.start_date and record.end_date:
                if record.end_date < record.start_date:
                    raise ValidationError(
                        "End date cannot be earlier than start date.\n"
                        f"Start: {record.start_date}\n"
                        f"End: {record.end_date}"
                    )