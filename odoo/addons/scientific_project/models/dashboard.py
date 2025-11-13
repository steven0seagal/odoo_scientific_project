from odoo import models, fields, api
from datetime import date, timedelta


class ScientificDashboard(models.TransientModel):
    """Dashboard for Scientific Project Manager - aggregates key metrics"""
    _name = 'scientific.dashboard'
    _description = 'Scientific Project Dashboard'

    # Project Statistics
    total_projects = fields.Integer(string='Total Projects', compute='_compute_project_stats')
    active_projects = fields.Integer(string='Active Projects', compute='_compute_project_stats')
    completed_projects = fields.Integer(string='Completed Projects', compute='_compute_project_stats')
    overdue_projects = fields.Integer(string='Overdue Projects', compute='_compute_project_stats')

    # Task Statistics
    total_tasks = fields.Integer(string='Total Tasks', compute='_compute_task_stats')
    my_tasks = fields.Integer(string='My Tasks', compute='_compute_task_stats')
    overdue_tasks = fields.Integer(string='Overdue Tasks', compute='_compute_task_stats')
    completed_this_week = fields.Integer(string='Completed This Week', compute='_compute_task_stats')

    # Experiment Statistics
    total_experiments = fields.Integer(string='Total Experiments', compute='_compute_experiment_stats')
    active_experiments = fields.Integer(string='Active Experiments', compute='_compute_experiment_stats')
    completed_experiments = fields.Integer(string='Completed Experiments', compute='_compute_experiment_stats')

    # Publication Statistics
    total_publications = fields.Integer(string='Total Publications', compute='_compute_publication_stats')
    published_this_year = fields.Integer(string='Published This Year', compute='_compute_publication_stats')
    in_review = fields.Integer(string='In Review', compute='_compute_publication_stats')

    # Resource Statistics
    total_researchers = fields.Integer(string='Total Researchers', compute='_compute_resource_stats')
    available_equipment = fields.Integer(string='Available Equipment', compute='_compute_resource_stats')

    @api.depends_context('uid')
    def _compute_project_stats(self):
        """Compute project statistics"""
        for record in self:
            Project = self.env['scientific.project']

            record.total_projects = Project.search_count([])
            record.active_projects = Project.search_count([('status', 'in', ['draft', 'in_progress'])])
            record.completed_projects = Project.search_count([('status', '=', 'done')])
            record.overdue_projects = Project.search_count([
                ('is_overdue', '=', True),
                ('status', 'not in', ['done', 'cancelled'])
            ])

    @api.depends_context('uid')
    def _compute_task_stats(self):
        """Compute task statistics"""
        for record in self:
            Task = self.env['scientific.task']
            today = date.today()
            week_start = today - timedelta(days=today.weekday())

            record.total_tasks = Task.search_count([])

            # My tasks - assigned to current user
            current_researcher = self.env['scientific.researcher'].search([
                ('user_id', '=', self.env.uid)
            ], limit=1)

            if current_researcher:
                record.my_tasks = Task.search_count([
                    ('assigned_to_ids', 'in', [current_researcher.id]),
                    ('status', 'not in', ['done', 'cancelled'])
                ])
            else:
                record.my_tasks = 0

            record.overdue_tasks = Task.search_count([
                ('is_overdue', '=', True),
                ('status', 'not in', ['done', 'cancelled'])
            ])

            record.completed_this_week = Task.search_count([
                ('status', '=', 'done'),
                ('write_date', '>=', week_start)
            ])

    @api.depends_context('uid')
    def _compute_experiment_stats(self):
        """Compute experiment statistics"""
        for record in self:
            Experiment = self.env['scientific.experiment']

            record.total_experiments = Experiment.search_count([])
            record.active_experiments = Experiment.search_count([
                ('status', 'in', ['planning', 'in_progress'])
            ])
            record.completed_experiments = Experiment.search_count([('status', '=', 'completed')])

    @api.depends_context('uid')
    def _compute_publication_stats(self):
        """Compute publication statistics"""
        for record in self:
            Publication = self.env['scientific.publication']
            current_year = date.today().year

            record.total_publications = Publication.search_count([])
            record.published_this_year = Publication.search_count([
                ('status', '=', 'published'),
                ('publication_date', '>=', '%s-01-01' % current_year)
            ])
            record.in_review = Publication.search_count([
                ('status', 'in', ['submitted', 'under_review'])
            ])

    @api.depends_context('uid')
    def _compute_resource_stats(self):
        """Compute resource statistics"""
        for record in self:
            record.total_researchers = self.env['scientific.researcher'].search_count([])
            record.available_equipment = self.env['scientific.equipment'].search_count([
                ('status', '=', 'available')
            ])

    def action_view_my_projects(self):
        """Open my projects view"""
        current_researcher = self.env['scientific.researcher'].search([
            ('user_id', '=', self.env.uid)
        ], limit=1)

        domain = []
        if current_researcher:
            domain = ['|',
                ('principal_investigator_id', '=', current_researcher.id),
                ('collaborators_ids', 'in', [current_researcher.id])
            ]

        return {
            'name': 'My Projects',
            'type': 'ir.actions.act_window',
            'res_model': 'scientific.project',
            'view_mode': 'kanban,tree,form',
            'domain': domain,
            'context': {'search_default_in_progress': 1}
        }

    def action_view_my_tasks(self):
        """Open my tasks view"""
        current_researcher = self.env['scientific.researcher'].search([
            ('user_id', '=', self.env.uid)
        ], limit=1)

        domain = []
        if current_researcher:
            domain = [('assigned_to_ids', 'in', [current_researcher.id])]

        return {
            'name': 'My Tasks',
            'type': 'ir.actions.act_window',
            'res_model': 'scientific.task',
            'view_mode': 'tree,kanban,form',
            'domain': domain,
            'context': {'search_default_in_progress': 1}
        }

    def action_view_overdue_tasks(self):
        """Open overdue tasks view"""
        return {
            'name': 'Overdue Tasks',
            'type': 'ir.actions.act_window',
            'res_model': 'scientific.task',
            'view_mode': 'tree,form',
            'domain': [('is_overdue', '=', True), ('status', 'not in', ['done', 'cancelled'])],
        }

    def action_view_active_experiments(self):
        """Open active experiments view"""
        return {
            'name': 'Active Experiments',
            'type': 'ir.actions.act_window',
            'res_model': 'scientific.experiment',
            'view_mode': 'tree,form',
            'domain': [('status', 'in', ['planning', 'in_progress'])],
        }

    def action_view_publications(self):
        """Open publications view"""
        return {
            'name': 'Publications',
            'type': 'ir.actions.act_window',
            'res_model': 'scientific.publication',
            'view_mode': 'kanban,tree,form',
        }
