from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class ScientificExperiment(models.Model):
    _name = 'scientific.experiment'
    _description = 'Experiment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

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
    document_id = fields.Many2many('scientific.document', string='Documents')
    assigned_to_ids = fields.Many2many('scientific.researcher', string='Assigned to', tracking=True)
    equipment_ids = fields.Many2many('scientific.equipment', string='Equipment')
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Critical')
    ], string='Priority', default='1')

    # Computed fields
    duration_days = fields.Integer(string='Duration (Days)', compute='_compute_duration_days', store=True)
    is_overdue = fields.Boolean(string='Overdue', compute='_compute_is_overdue')
    assigned_researcher_count = fields.Integer(string='Researchers', compute='_compute_assigned_count', store=True)
    equipment_count = fields.Integer(string='Equipment', compute='_compute_equipment_count', store=True)
    completion_status = fields.Char(string='Status Summary', compute='_compute_completion_status')

    @api.depends('start_date', 'end_date')
    def _compute_duration_days(self):
        """Calculate experiment duration in days"""
        for record in self:
            if record.start_date and record.end_date:
                delta = record.end_date - record.start_date
                record.duration_days = delta.days
            else:
                record.duration_days = 0

    @api.depends('end_date', 'status')
    def _compute_is_overdue(self):
        """Check if experiment is overdue"""
        for record in self:
            if record.end_date and record.status not in ['completed', 'cancelled']:
                record.is_overdue = record.end_date < date.today()
            else:
                record.is_overdue = False

    @api.depends('assigned_to_ids')
    def _compute_assigned_count(self):
        """Count assigned researchers"""
        for record in self:
            record.assigned_researcher_count = len(record.assigned_to_ids)

    @api.depends('equipment_ids')
    def _compute_equipment_count(self):
        """Count required equipment"""
        for record in self:
            record.equipment_count = len(record.equipment_ids)

    @api.depends('status', 'report_created')
    def _compute_completion_status(self):
        """Generate completion status summary"""
        for record in self:
            if record.status == 'completed' and record.report_created:
                record.completion_status = 'Complete with Report'
            elif record.status == 'completed':
                record.completion_status = 'Complete (No Report)'
            elif record.status == 'in_progress':
                record.completion_status = 'In Progress'
            else:
                record.completion_status = record.status.title() if record.status else 'Not Started'

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """Validate that end date is after start date"""
        for record in self:
            if record.start_date and record.end_date:
                if record.end_date < record.start_date:
                    raise ValidationError('End date must be after start date!')

    def action_planning(self):
        """Set experiment status to planning"""
        self.status = 'planning'

    def action_in_progress(self):
        """Set experiment status to in progress"""
        self.status = 'in_progress'

    def action_completed(self):
        """Set experiment status to completed"""
        self.status = 'completed'

    def action_cancelled(self):
        """Set experiment status to cancelled"""
        self.status = 'cancelled'

    def action_create_report(self):
        """Mark report as created"""
        self.report_created = True
        self.message_post(body='Experiment report has been created.')

    def action_clone_experiment(self):
        """Clone this experiment"""
        self.ensure_one()
        new_experiment = self.copy({
            'name': f'{self.name} (Copy)',
            'status': 'planning',
            'report_created': False,
            'results': '',
            'conclusion': '',
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'scientific.experiment',
            'res_id': new_experiment.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def action_view_researchers(self):
        """Smart button action to view assigned researchers"""
        return {
            'name': 'Researchers',
            'type': 'ir.actions.act_window',
            'res_model': 'scientific.researcher',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.assigned_to_ids.ids)],
        }

    def action_view_equipment(self):
        """Smart button action to view equipment"""
        return {
            'name': 'Equipment',
            'type': 'ir.actions.act_window',
            'res_model': 'scientific.equipment',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.equipment_ids.ids)],
        }
