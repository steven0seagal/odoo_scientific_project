from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

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
    project_id = fields.Many2one('scientific.project', string='Project', tracking=True, ondelete='cascade')
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

    # Computed fields
    duration_days = fields.Integer(string='Duration (days)', compute='_compute_duration', store=False)
    researcher_count = fields.Integer(string='Researchers', compute='_compute_researcher_count', store=False)
    completion_status = fields.Char(string='Completion', compute='_compute_completion_status', store=False)
    days_remaining = fields.Integer(string='Days Remaining', compute='_compute_days_remaining', store=False)

    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        """Calculate experiment duration"""
        for experiment in self:
            if experiment.start_date and experiment.end_date:
                delta = experiment.end_date - experiment.start_date
                experiment.duration_days = delta.days
            else:
                experiment.duration_days = 0

    def _compute_researcher_count(self):
        """Count assigned researchers"""
        for experiment in self:
            experiment.researcher_count = len(experiment.assigned_to_ids)

    @api.depends('introduction', 'methodology', 'results', 'conclusion')
    def _compute_completion_status(self):
        """Calculate completion status based on filled sections"""
        for experiment in self:
            sections_filled = sum([
                1 if experiment.introduction else 0,
                1 if experiment.methodology else 0,
                1 if experiment.results else 0,
                1 if experiment.conclusion else 0,
            ])
            experiment.completion_status = f"{sections_filled}/4 sections"

    @api.depends('end_date')
    def _compute_days_remaining(self):
        """Calculate days remaining until experiment end"""
        for experiment in self:
            if experiment.end_date:
                today = date.today()
                delta = experiment.end_date - today
                experiment.days_remaining = delta.days
            else:
                experiment.days_remaining = 0

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