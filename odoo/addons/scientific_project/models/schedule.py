from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ScientificSchedule(models.Model):
    _name = 'scientific.schedule'
    _description = 'Schedule'
    _order = 'start_time desc'

    equipment_id = fields.Many2one('scientific.equipment', string='Equipment', required=True,
                                     help="Equipment being scheduled")
    researcher_id = fields.Many2one('scientific.researcher', string='Researcher', required=True,
                                     help="Researcher who reserved the equipment")
    start_time = fields.Datetime(string='Start Time', required=True,
                                  help="Reservation start time")
    end_time = fields.Datetime(string='End Time', required=True,
                                help="Reservation end time")
    notes = fields.Text(string='Notes')
    experiment_id = fields.Many2one('scientific.experiment', string='Experiment',
                                     help="Associated experiment")

    @api.constrains('start_time', 'end_time')
    def _check_time_range(self):
        """Validate that end time is not before start time"""
        for record in self:
            if record.start_time and record.end_time:
                if record.end_time < record.start_time:
                    raise ValidationError(
                        "End time cannot be earlier than start time.\n"
                        f"Start: {record.start_time}\n"
                        f"End: {record.end_time}"
                    )

    @api.constrains('equipment_id', 'start_time', 'end_time')
    def _check_equipment_availability(self):
        """Check if equipment is already scheduled for the requested time"""
        for record in self:
            if record.equipment_id and record.start_time and record.end_time:
                # Check for overlapping reservations
                overlapping = self.search([
                    ('id', '!=', record.id),
                    ('equipment_id', '=', record.equipment_id.id),
                    '|',
                    '&',
                    ('start_time', '<=', record.start_time),
                    ('end_time', '>', record.start_time),
                    '&',
                    ('start_time', '<', record.end_time),
                    ('end_time', '>=', record.end_time),
                ])
                if overlapping:
                    raise ValidationError(
                        f"Equipment '{record.equipment_id.name}' is already scheduled "
                        f"during the requested time period.\n"
                        f"Conflicting reservation by: {overlapping[0].researcher_id.name}"
                    )
