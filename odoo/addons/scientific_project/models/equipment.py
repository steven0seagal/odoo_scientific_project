from odoo import models, fields

class ScientificEquipment(models.Model):
    _name = 'scientific.equipment'
    _description = 'Equipment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name, location'

    _sql_constraints = [
        ('name_location_unique', 'UNIQUE(name, location)',
         'Equipment with this name already exists at this location!'),
    ]

    name = fields.Char(string='Name', required=True, tracking=True)
    equipment_type = fields.Char(string='Type', tracking=True)
    location = fields.Char(string='Location', tracking=True)
    status = fields.Selection([
        ('available', 'Available'),
        ('in_use', 'In Use'),
        ('maintenance', 'Maintenance'),
        ('retired', 'Retired')
    ], string='Status', default='available', tracking=True)
    maintenance_schedule = fields.Date(string='Maintenance Schedule', tracking=True)
    notes = fields.Text(string='Notes')
    care_taker_id = fields.Many2one('scientific.researcher', string='Care Taker', tracking=True)
    document_id = fields.Many2many('scientific.document', string='Document')
    experiment_id = fields.Many2many('scientific.experiment', string='Experiment')