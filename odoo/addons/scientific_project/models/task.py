from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class ScientificTask(models.Model):
    _name = 'scientific.task'
    _description = 'Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'priority desc, end_date, id'

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text(string='Description', tracking=True)
    assigned_to_ids = fields.Many2many('scientific.researcher', string='Assigned to', tracking=True)
    start_date = fields.Date(string='Start Date', tracking=True)
    end_date = fields.Date(string='End Date', tracking=True)
    status = fields.Selection([
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='todo', tracking=True)

    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Urgent')
    ], string='Priority', default='1', tracking=True)

    project_id = fields.Many2one('scientific.project', string='Project', tracking=True)
    experiment_id = fields.Many2one('scientific.experiment', string='Related Experiment')

    document_id = fields.Many2many('scientific.document', string='Documents', tracking=True)
    notes = fields.Text(string='Notes')

    # Computed fields
    duration_days = fields.Integer(string='Duration (Days)', compute='_compute_duration_days', store=True)
    is_overdue = fields.Boolean(string='Overdue', compute='_compute_is_overdue')
    days_remaining = fields.Integer(string='Days Remaining', compute='_compute_days_remaining')
    assigned_count = fields.Integer(string='Assigned Users', compute='_compute_assigned_count', store=True)
    progress = fields.Selection([
        ('not_started', 'Not Started'),
        ('on_track', 'On Track'),
        ('at_risk', 'At Risk'),
        ('overdue', 'Overdue'),
        ('completed', 'Completed')
    ], string='Progress', compute='_compute_progress')

    @api.depends('start_date', 'end_date')
    def _compute_duration_days(self):
        """Calculate task duration in days"""
        for record in self:
            if record.start_date and record.end_date:
                delta = record.end_date - record.start_date
                record.duration_days = delta.days
            else:
                record.duration_days = 0

    @api.depends('end_date', 'status')
    def _compute_is_overdue(self):
        """Check if task is overdue"""
        for record in self:
            if record.end_date and record.status not in ['done', 'cancelled']:
                record.is_overdue = record.end_date < date.today()
            else:
                record.is_overdue = False

    @api.depends('end_date', 'status')
    def _compute_days_remaining(self):
        """Calculate days remaining until due date"""
        for record in self:
            if record.end_date and record.status not in ['done', 'cancelled']:
                delta = record.end_date - date.today()
                record.days_remaining = delta.days
            else:
                record.days_remaining = 0

    @api.depends('assigned_to_ids')
    def _compute_assigned_count(self):
        """Count assigned researchers"""
        for record in self:
            record.assigned_count = len(record.assigned_to_ids)

    @api.depends('status', 'end_date', 'start_date')
    def _compute_progress(self):
        """Calculate task progress status"""
        today = date.today()
        for record in self:
            if record.status == 'done':
                record.progress = 'completed'
            elif record.status == 'cancelled':
                record.progress = 'not_started'
            elif not record.start_date or not record.end_date:
                record.progress = 'not_started'
            elif record.end_date < today:
                record.progress = 'overdue'
            elif record.start_date > today:
                record.progress = 'not_started'
            else:
                # Calculate if at risk (less than 20% time remaining)
                total_days = (record.end_date - record.start_date).days
                days_passed = (today - record.start_date).days
                if total_days > 0:
                    percent_complete = (days_passed / total_days) * 100
                    if percent_complete > 80:
                        record.progress = 'at_risk'
                    else:
                        record.progress = 'on_track'
                else:
                    record.progress = 'on_track'

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """Validate that end date is after start date"""
        for record in self:
            if record.start_date and record.end_date:
                if record.end_date < record.start_date:
                    raise ValidationError('End date must be after start date!')

    def action_todo(self):
        """Set task status to todo"""
        self.status = 'todo'

    def action_in_progress(self):
        """Set task status to in progress"""
        self.status = 'in_progress'
        if not self.start_date:
            self.start_date = date.today()

    def action_done(self):
        """Set task status to done"""
        self.status = 'done'
        self.message_post(body='Task has been completed.')

    def action_cancelled(self):
        """Set task status to cancelled"""
        self.status = 'cancelled'
