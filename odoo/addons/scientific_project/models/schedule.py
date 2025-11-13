from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ScientificSchedule(models.Model):
    _name = 'scientific.schedule'
    _description = 'Equipment and Researcher Schedule'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'start_time desc'

    name = fields.Char(string='Booking Reference', compute='_compute_name', store=True)
    equipment_id = fields.Many2one('scientific.equipment', string='Equipment', required=True, tracking=True)
    researcher_id = fields.Many2one('scientific.researcher', string='Researcher', required=True, tracking=True)
    start_time = fields.Datetime(string='Start Time', required=True, tracking=True)
    end_time = fields.Datetime(string='End Time', required=True, tracking=True)
    notes = fields.Text(string='Notes')
    experiment_id = fields.Many2one('scientific.experiment', string='Experiment', tracking=True)

    status = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='scheduled', tracking=True)

    duration_hours = fields.Float(string='Duration (Hours)', compute='_compute_duration')

    @api.depends('equipment_id', 'start_time')
    def _compute_name(self):
        for record in self:
            if record.equipment_id and record.start_time:
                record.name = f"{record.equipment_id.name} - {record.start_time.strftime('%Y-%m-%d %H:%M')}"
            else:
                record.name = 'New Booking'

    @api.depends('start_time', 'end_time')
    def _compute_duration(self):
        for record in self:
            if record.start_time and record.end_time:
                delta = record.end_time - record.start_time
                record.duration_hours = delta.total_seconds() / 3600
            else:
                record.duration_hours = 0.0

    @api.constrains('start_time', 'end_time')
    def _check_times(self):
        """Ensure end time is after start time"""
        for record in self:
            if record.start_time and record.end_time:
                if record.end_time <= record.start_time:
                    raise ValidationError('End time must be after start time')

    @api.constrains('equipment_id', 'start_time', 'end_time')
    def _check_equipment_conflict(self):
        """Check for equipment booking conflicts"""
        for record in self:
            if record.equipment_id and record.start_time and record.end_time:
                # Search for overlapping bookings for the same equipment
                domain = [
                    ('equipment_id', '=', record.equipment_id.id),
                    ('id', '!=', record.id),
                    ('status', '!=', 'cancelled'),
                    '|',
                    '&',
                    ('start_time', '<=', record.start_time),
                    ('end_time', '>', record.start_time),
                    '&',
                    ('start_time', '<', record.end_time),
                    ('end_time', '>=', record.end_time),
                ]
                conflicting = self.search(domain, limit=1)
                if conflicting:
                    raise ValidationError(
                        f"Equipment '{record.equipment_id.name}' is already booked "
                        f"from {conflicting.start_time} to {conflicting.end_time} "
                        f"by {conflicting.researcher_id.name}"
                    )

    @api.constrains('researcher_id', 'start_time', 'end_time')
    def _check_researcher_conflict(self):
        """Check for researcher booking conflicts (optional warning)"""
        for record in self:
            if record.researcher_id and record.start_time and record.end_time:
                # Search for overlapping bookings for the same researcher
                domain = [
                    ('researcher_id', '=', record.researcher_id.id),
                    ('id', '!=', record.id),
                    ('status', '!=', 'cancelled'),
                    '|',
                    '&',
                    ('start_time', '<=', record.start_time),
                    ('end_time', '>', record.start_time),
                    '&',
                    ('start_time', '<', record.end_time),
                    ('end_time', '>=', record.end_time),
                ]
                conflicting = self.search(domain, limit=1)
                if conflicting:
                    # This is just a warning - researcher can have multiple bookings
                    # but we log it for awareness
                    import logging
                    _logger = logging.getLogger(__name__)
                    _logger.warning(
                        f"Researcher '{record.researcher_id.name}' has overlapping bookings: "
                        f"{conflicting.equipment_id.name} from {conflicting.start_time} to {conflicting.end_time}"
                    )
