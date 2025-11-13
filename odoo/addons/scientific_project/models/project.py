from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class Project(models.Model):
    _name = 'scientific.project'
    _description = 'Scientific Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'start_date desc, id desc'

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
    document_id = fields.Many2many('scientific.document', string='Document', tracking=True)
    funding = fields.Many2many('scientific.funding', string='Funding')
    principal_investigator_id = fields.Many2one('scientific.researcher', string='Principal Investigator', tracking=True)
    collaborators_ids = fields.Many2many('scientific.researcher', string='Collaborators')
    notes = fields.Text(string='Notes')

    # Computed fields
    task_ids = fields.One2many('scientific.task', 'project_id', string='Tasks')
    experiment_ids = fields.One2many('scientific.experiment', 'project_id', string='Experiments')
    publication_ids = fields.One2many('scientific.publication', 'project_id', string='Publications')
    data_management_ids = fields.One2many('scientific.data_management', 'project_id', string='Data')

    task_count = fields.Integer(string='Task Count', compute='_compute_counts', store=True)
    experiment_count = fields.Integer(string='Experiment Count', compute='_compute_counts', store=True)
    publication_count = fields.Integer(string='Publication Count', compute='_compute_counts', store=True)
    data_count = fields.Integer(string='Data Count', compute='_compute_counts', store=True)

    days_remaining = fields.Integer(string='Days Remaining', compute='_compute_days_remaining')
    is_overdue = fields.Boolean(string='Is Overdue', compute='_compute_is_overdue')
    completion_percentage = fields.Float(string='Completion %', compute='_compute_completion_percentage', store=True)
    total_budget = fields.Float(string='Total Budget', compute='_compute_budget', store=True)

    @api.depends('task_ids', 'experiment_ids', 'publication_ids', 'data_management_ids')
    def _compute_counts(self):
        for project in self:
            project.task_count = len(project.task_ids)
            project.experiment_count = len(project.experiment_ids)
            project.publication_count = len(project.publication_ids)
            project.data_count = len(project.data_management_ids)

    @api.depends('end_date')
    def _compute_days_remaining(self):
        today = date.today()
        for project in self:
            if project.end_date:
                delta = project.end_date - today
                project.days_remaining = delta.days
            else:
                project.days_remaining = 0

    @api.depends('end_date', 'status')
    def _compute_is_overdue(self):
        today = date.today()
        for project in self:
            project.is_overdue = (
                project.end_date and
                project.end_date < today and
                project.status not in ['done', 'cancelled']
            )

    @api.depends('task_ids.status')
    def _compute_completion_percentage(self):
        for project in self:
            tasks = project.task_ids
            if tasks:
                completed = len(tasks.filtered(lambda t: t.status == 'completed'))
                project.completion_percentage = (completed / len(tasks)) * 100
            else:
                project.completion_percentage = 0.0

    @api.depends('funding.budget_amount')
    def _compute_budget(self):
        for project in self:
            project.total_budget = sum(project.funding.mapped('budget_amount'))

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """Ensure end date is after start date"""
        for project in self:
            if project.start_date and project.end_date:
                if project.end_date < project.start_date:
                    raise ValidationError('End date cannot be before start date')

    def action_draft(self):
        self.status = 'draft'

    def action_in_progress(self):
        self.status = 'in_progress'

    def action_done(self):
        self.status = 'done'

    def action_cancelled(self):
        self.status = 'cancelled'

    def action_view_tasks(self):
        """Smart button action to view project tasks"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tasks',
            'res_model': 'scientific.task',
            'view_mode': 'tree,form,kanban',
            'domain': [('project_id', '=', self.id)],
            'context': {'default_project_id': self.id}
        }

    def action_view_experiments(self):
        """Smart button action to view project experiments"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Experiments',
            'res_model': 'scientific.experiment',
            'view_mode': 'tree,form,kanban',
            'domain': [('project_id', '=', self.id)],
            'context': {'default_project_id': self.id}
        }

    def action_view_publications(self):
        """Smart button action to view project publications"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Publications',
            'res_model': 'scientific.publication',
            'view_mode': 'tree,form,kanban',
            'domain': [('project_id', '=', self.id)],
            'context': {'default_project_id': self.id}
        }





