from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class Project(models.Model):
    _name = 'scientific.project'
    _description = 'Scientific Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    start_date = fields.Date(string='Start Date', tracking=True)
    end_date = fields.Date(string='End Date', tracking=True)
    description = fields.Text(string='Description', tracking=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)
    document_id = fields.Many2many('scientific.document', string='Documents', tracking=True)
    funding = fields.Many2many('scientific.funding', string='Funding')
    principal_investigator_id = fields.Many2one('scientific.researcher', string='Principal Investigator', tracking=True)
    collaborators_ids = fields.Many2many('scientific.researcher', string='Collaborators')
    notes = fields.Text(string='Notes')

    # Computed fields
    experiment_count = fields.Integer(string='Experiments', compute='_compute_experiment_count', store=True)
    task_count = fields.Integer(string='Tasks', compute='_compute_task_count', store=True)
    publication_count = fields.Integer(string='Publications', compute='_compute_publication_count', store=True)
    completion_percentage = fields.Float(string='Completion %', compute='_compute_completion_percentage', store=True)
    days_remaining = fields.Integer(string='Days Remaining', compute='_compute_days_remaining')
    is_overdue = fields.Boolean(string='Overdue', compute='_compute_is_overdue')
    total_budget = fields.Float(string='Total Budget', compute='_compute_budget', store=True)

    # Relations for computed fields
    experiment_ids = fields.One2many('scientific.experiment', 'project_id', string='Experiments')
    task_ids = fields.One2many('scientific.task', 'project_id', string='Tasks')
    publication_ids = fields.One2many('scientific.publication', 'project_id', string='Publications')

    @api.depends('experiment_ids')
    def _compute_experiment_count(self):
        """Compute the number of experiments"""
        for record in self:
            record.experiment_count = len(record.experiment_ids)

    @api.depends('task_ids')
    def _compute_task_count(self):
        """Compute the number of tasks"""
        for record in self:
            record.task_count = len(record.task_ids)

    @api.depends('publication_ids')
    def _compute_publication_count(self):
        """Compute the number of publications"""
        for record in self:
            record.publication_count = len(record.publication_ids)

    @api.depends('task_ids.status')
    def _compute_completion_percentage(self):
        """Calculate completion percentage based on completed tasks"""
        for record in self:
            if record.task_ids:
                completed = len(record.task_ids.filtered(lambda t: t.status == 'done'))
                record.completion_percentage = (completed / len(record.task_ids)) * 100
            else:
                record.completion_percentage = 0.0

    @api.depends('end_date')
    def _compute_days_remaining(self):
        """Calculate days remaining until end date"""
        for record in self:
            if record.end_date:
                delta = record.end_date - date.today()
                record.days_remaining = delta.days
            else:
                record.days_remaining = 0

    @api.depends('end_date', 'status')
    def _compute_is_overdue(self):
        """Check if project is overdue"""
        for record in self:
            if record.end_date and record.status not in ['done', 'cancelled']:
                record.is_overdue = record.end_date < date.today()
            else:
                record.is_overdue = False

    @api.depends('funding.amount')
    def _compute_budget(self):
        """Calculate total budget from funding sources"""
        for record in self:
            record.total_budget = sum(record.funding.mapped('amount'))

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """Validate that end date is after start date"""
        for record in self:
            if record.start_date and record.end_date:
                if record.end_date < record.start_date:
                    raise ValidationError('End date must be after start date!')

    def action_draft(self):
        """Set project status to draft"""
        self.status = 'draft'

    def action_in_progress(self):
        """Set project status to in progress"""
        self.status = 'in_progress'

    def action_done(self):
        """Set project status to done"""
        self.status = 'done'

    def action_cancelled(self):
        """Set project status to cancelled"""
        self.status = 'cancelled'

    def action_view_experiments(self):
        """Smart button action to view experiments"""
        return {
            'name': 'Experiments',
            'type': 'ir.actions.act_window',
            'res_model': 'scientific.experiment',
            'view_mode': 'tree,form',
            'domain': [('project_id', '=', self.id)],
            'context': {'default_project_id': self.id}
        }

    def action_view_tasks(self):
        """Smart button action to view tasks"""
        return {
            'name': 'Tasks',
            'type': 'ir.actions.act_window',
            'res_model': 'scientific.task',
            'view_mode': 'tree,form',
            'domain': [('project_id', '=', self.id)],
            'context': {'default_project_id': self.id}
        }

    def action_view_publications(self):
        """Smart button action to view publications"""
        return {
            'name': 'Publications',
            'type': 'ir.actions.act_window',
            'res_model': 'scientific.publication',
            'view_mode': 'tree,form',
            'domain': [('project_id', '=', self.id)],
            'context': {'default_project_id': self.id}
        }





