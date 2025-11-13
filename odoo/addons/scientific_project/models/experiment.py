from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class ScientificExperiment(models.Model):
    _name = 'scientific.experiment'
    _description = 'Experiment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'start_date desc, id desc'

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
    project_id = fields.Many2one('scientific.project', string='Project', ondelete='cascade')
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
    reagent_ids = fields.Many2many('scientific.reagents', string='Reagents')

    # Computed fields
    duration_days = fields.Integer(string='Duration (Days)', compute='_compute_duration_days')
    days_remaining = fields.Integer(string='Days Remaining', compute='_compute_days_remaining')
    is_overdue = fields.Boolean(string='Is Overdue', compute='_compute_is_overdue')
    assigned_researcher_count = fields.Integer(string='Researchers Assigned', compute='_compute_researcher_count', store=True)
    equipment_count = fields.Integer(string='Equipment Count', compute='_compute_equipment_count', store=True)

    @api.depends('start_date', 'end_date')
    def _compute_duration_days(self):
        for experiment in self:
            if experiment.start_date and experiment.end_date:
                delta = experiment.end_date - experiment.start_date
                experiment.duration_days = delta.days
            else:
                experiment.duration_days = 0

    @api.depends('end_date')
    def _compute_days_remaining(self):
        today = date.today()
        for experiment in self:
            if experiment.end_date:
                delta = experiment.end_date - today
                experiment.days_remaining = delta.days
            else:
                experiment.days_remaining = 0

    @api.depends('end_date', 'status')
    def _compute_is_overdue(self):
        today = date.today()
        for experiment in self:
            experiment.is_overdue = (
                experiment.end_date and
                experiment.end_date < today and
                experiment.status not in ['completed', 'cancelled']
            )

    @api.depends('assigned_to_ids')
    def _compute_researcher_count(self):
        for experiment in self:
            experiment.assigned_researcher_count = len(experiment.assigned_to_ids)

    @api.depends('equipment_ids')
    def _compute_equipment_count(self):
        for experiment in self:
            experiment.equipment_count = len(experiment.equipment_ids)

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """Ensure end date is after start date"""
        for experiment in self:
            if experiment.start_date and experiment.end_date:
                if experiment.end_date < experiment.start_date:
                    raise ValidationError('End date cannot be before start date')

    @api.constrains('hypothesis')
    def _check_hypothesis(self):
        """Ensure hypothesis is provided for experiments in progress"""
        for experiment in self:
            if experiment.status == 'in_progress' and not experiment.hypothesis:
                raise ValidationError('A hypothesis must be defined before starting the experiment')