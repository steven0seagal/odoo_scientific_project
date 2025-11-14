from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class Project(models.Model):
    _name = 'scientific.project'
    _description = 'Scientific Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'start_date desc, name'

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Project name must be unique!'),
    ]

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
    principal_investigator_id = fields.Many2one('scientific.researcher', string='Principal Investigator',
                                                 tracking=True, ondelete='restrict')
    collaborators_ids = fields.Many2many('scientific.researcher', string='Collaborators', tracking=True)
    notes = fields.Text(string='Notes')

    # Computed fields for smart buttons and dashboard
    task_count = fields.Integer(string='Tasks', compute='_compute_task_count', store=False)
    experiment_count = fields.Integer(string='Experiments', compute='_compute_experiment_count', store=False)
    document_count = fields.Integer(string='Documents', compute='_compute_document_count', store=False)
    publication_count = fields.Integer(string='Publications', compute='_compute_publication_count', store=False)

    # Progress and status fields
    progress_percentage = fields.Float(string='Progress %', compute='_compute_progress', store=False,
                                      help='Percentage of completed tasks')
    days_remaining = fields.Integer(string='Days Remaining', compute='_compute_days_remaining', store=False)
    is_overdue = fields.Boolean(string='Overdue', compute='_compute_is_overdue', store=False)
    days_overdue = fields.Integer(string='Days Overdue', compute='_compute_is_overdue', store=False)

    # Team size
    team_size = fields.Integer(string='Team Size', compute='_compute_team_size', store=False)

    @api.depends('collaborators_ids', 'principal_investigator_id')
    def _compute_team_size(self):
        """Calculate total team size"""
        for project in self:
            size = len(project.collaborators_ids)
            if project.principal_investigator_id:
                size += 1
            project.team_size = size

    def _compute_task_count(self):
        """Count tasks associated with this project"""
        for project in self:
            project.task_count = self.env['scientific.task'].search_count([
                ('project_id', '=', project.id)
            ])

    def _compute_experiment_count(self):
        """Count experiments associated with this project"""
        for project in self:
            project.experiment_count = self.env['scientific.experiment'].search_count([
                ('project_id', '=', project.id)
            ])

    def _compute_document_count(self):
        """Count documents associated with this project"""
        for project in self:
            project.document_count = self.env['scientific.document'].search_count([
                ('project_id', 'in', [project.id])
            ])

    def _compute_publication_count(self):
        """Count publications associated with this project"""
        for project in self:
            project.publication_count = self.env['scientific.publication'].search_count([
                ('project_id', '=', project.id)
            ])

    @api.depends('start_date', 'end_date')
    def _compute_progress(self):
        """Calculate project progress based on completed tasks"""
        for project in self:
            tasks = self.env['scientific.task'].search([('project_id', '=', project.id)])
            if tasks:
                completed_tasks = tasks.filtered(lambda t: t.status == 'completed')
                project.progress_percentage = (len(completed_tasks) / len(tasks)) * 100
            else:
                project.progress_percentage = 0.0

    @api.depends('end_date')
    def _compute_days_remaining(self):
        """Calculate days remaining until project end date"""
        for project in self:
            if project.end_date:
                today = date.today()
                delta = project.end_date - today
                project.days_remaining = delta.days
            else:
                project.days_remaining = 0

    @api.depends('end_date', 'status')
    def _compute_is_overdue(self):
        """Check if project is overdue"""
        for project in self:
            if project.end_date and project.status not in ['done', 'cancelled']:
                today = date.today()
                if today > project.end_date:
                    project.is_overdue = True
                    project.days_overdue = (today - project.end_date).days
                else:
                    project.is_overdue = False
                    project.days_overdue = 0
            else:
                project.is_overdue = False
                project.days_overdue = 0

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

    def action_draft(self):
        self.status = 'draft'

    def action_in_progress(self):
        self.status = 'in_progress'

    def action_done(self):
        self.status = 'done'

    def action_cancelled(self):
        self.status = 'cancelled'

    def action_view_tasks(self):
        """Navigate to related tasks"""
        action = self.env.ref('scientific_project.action_scientific_task').read()[0]
        action['domain'] = [('project_id', '=', self.id)]
        action['context'] = {'default_project_id': self.id}
        return action

    def action_view_experiments(self):
        """Navigate to related experiments"""
        action = self.env.ref('scientific_project.action_scientific_experiment').read()[0]
        action['domain'] = [('project_id', '=', self.id)]
        action['context'] = {'default_project_id': self.id}
        return action

    def action_view_documents(self):
        """Navigate to related documents"""
        action = self.env.ref('scientific_project.action_scientific_document').read()[0]
        action['domain'] = [('project_id', 'in', [self.id])]
        action['context'] = {'default_project_id': self.id}
        return action

    def action_view_publications(self):
        """Navigate to related publications"""
        action = self.env.ref('scientific_project.action_scientific_publication').read()[0]
        action['domain'] = [('project_id', '=', self.id)]
        action['context'] = {'default_project_id': self.id}
        return action





