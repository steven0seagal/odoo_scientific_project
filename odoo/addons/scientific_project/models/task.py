from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class ScientificTask(models.Model):
    _name = 'scientific.task'
    _description = 'Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'end_date, id desc'

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text(string='Description', tracking=True)
    assigned_to_ids = fields.Many2many('scientific.researcher', string='Assigned to', tracking=True)
    start_date = fields.Date(string='Start Date', tracking=True)
    end_date = fields.Date(string='End Date', tracking=True)
    status = fields.Selection(
        [('planning', 'Planning'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')],
        string='Status', default='planning', tracking=True)
    project_id = fields.Many2one('scientific.project', string='Project', tracking=True, ondelete='cascade')

    document_id = fields.Many2many('scientific.document', string='Document', tracking=True)
    notes = fields.Text(string='Notes', tracking=True)

    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Urgent')
    ], string='Priority', default='1')

    # Computed fields
    assigned_count = fields.Integer(string='Assigned Researchers', compute='_compute_assigned_count', store=True)
    days_remaining = fields.Integer(string='Days Remaining', compute='_compute_days_remaining')
    is_overdue = fields.Boolean(string='Is Overdue', compute='_compute_is_overdue')

    @api.depends('assigned_to_ids')
    def _compute_assigned_count(self):
        for task in self:
            task.assigned_count = len(task.assigned_to_ids)

    @api.depends('end_date')
    def _compute_days_remaining(self):
        today = date.today()
        for task in self:
            if task.end_date:
                delta = task.end_date - today
                task.days_remaining = delta.days
            else:
                task.days_remaining = 0

    @api.depends('end_date', 'status')
    def _compute_is_overdue(self):
        today = date.today()
        for task in self:
            task.is_overdue = (
                task.end_date and
                task.end_date < today and
                task.status not in ['completed', 'cancelled']
            )

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """Ensure end date is after start date"""
        for task in self:
            if task.start_date and task.end_date:
                if task.end_date < task.start_date:
                    raise ValidationError('End date cannot be before start date')

    @api.constrains('assigned_to_ids')
    def _check_assigned_researchers(self):
        """Ensure at least one researcher is assigned"""
        for task in self:
            if task.status == 'in_progress' and not task.assigned_to_ids:
                raise ValidationError('At least one researcher must be assigned to an in-progress task')