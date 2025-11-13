from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ScientificExperiment(models.Model):
    _name = 'scientific.experiment'
    _description = 'Experiment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'start_date desc, name'

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date', tracking=True)
    end_date = fields.Date(string='End Date', tracking=True)
    status = fields.Selection([
        ('planning', 'Planning'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='planning', tracking=True)
    project_id = fields.Many2one('scientific.project', string='Project', tracking=True)
    introduction = fields.Text(string='Introduction')
    hypothesis = fields.Text(string='Hypothesis', tracking=True)
    results = fields.Text(string='Results')
    conclusion = fields.Text(string='Conclusion')
    methodology = fields.Text(string='Methodology')
    report_created = fields.Boolean(string='Report Created', default=False, tracking=True)
    notes = fields.Text(string='Notes')
    document_id = fields.Many2many('scientific.document', string='Document')
    assigned_to_ids = fields.Many2many('scientific.researcher', string='Assigned to', tracking=True)
    equipment_ids = fields.Many2many('scientific.equipment', string='Equipment')

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