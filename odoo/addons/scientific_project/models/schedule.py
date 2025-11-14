from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ScientificSchedule(models.Model):
    _name = 'scientific.schedule'
    _description = 'Schedule'
    _order = 'start_time desc'

    equipment_id = fields.Many2one('scientific.equipment', string='Equipment', required=True)
    researcher_id = fields.Many2one('scientific.researcher', string='Researcher', required=True)
    start_time = fields.Datetime(string='Start Time', required=True)
    end_time = fields.Datetime(string='End Time', required=True)
    notes = fields.Text(string='Notes')
    experiment_id = fields.Many2one('scientific.experiment', string='Experiment')

    @api.constrains('start_time', 'end_time')
    def _check_time_range(self):
        """Validate that end time is not before start time"""
        for record in self:
            if record.start_time and record.end_time:
                if record.end_time <= record.start_time:
                    raise ValidationError(
                        "End time must be after start time.\n"
                        f"Start: {record.start_time}\n"
                        f"End: {record.end_time}"
                    )

    @api.constrains('equipment_id', 'start_time', 'end_time')
    def _check_equipment_availability(self):
        """Check if equipment is available for the requested time slot"""
        for record in self:
            if record.equipment_id and record.start_time and record.end_time:
                # Search for overlapping schedules
                overlapping = self.search([
                    ('id', '!=', record.id),
                    ('equipment_id', '=', record.equipment_id.id),
                    '|',
                    '&', ('start_time', '<=', record.start_time), ('end_time', '>', record.start_time),
                    '&', ('start_time', '<', record.end_time), ('end_time', '>=', record.end_time),
                ], limit=1)

                if overlapping:
                    raise ValidationError(
                        f"Equipment '{record.equipment_id.name}' is already booked for this time period.\n"
                        f"Conflicting booking: {overlapping.start_time} - {overlapping.end_time}\n"
                        f"Booked by: {overlapping.researcher_id.name}"
                    )
