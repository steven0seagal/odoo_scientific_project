from odoo import models, fields

class ScientificEquipment(models.Model):
    _name = 'scientific.equipment'
    _description = 'Equipment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name, location'

    name = fields.Char(string='Name', required=True, tracking=True,
                       help="Equipment name or model")
    equipment_type = fields.Char(string='Type', tracking=True,
                                  help="Type or category of equipment")
    location = fields.Char(string='Location', tracking=True,
                           help="Physical location of the equipment")
    status = fields.Selection([
        ('available', 'Available'),
        ('in_use', 'In Use'),
        ('maintenance', 'Maintenance')
    ], string='Status', default='available', tracking=True, required=True,
       help="Current operational status")
    maintenance_schedule = fields.Date(string='Maintenance Schedule', tracking=True,
                                        help="Next scheduled maintenance date")
    notes = fields.Text(string='Notes', tracking=True)
    care_taker_id = fields.Many2one('scientific.researcher', string='Care Taker', tracking=True,
                                     help="Person responsible for equipment maintenance")
    document_id = fields.Many2many('scientific.document', string='Document')
    experiment_id = fields.Many2many('scientific.experiment', string='Experiment')

    # SQL Constraints
    _sql_constraints = [
        ('name_location_unique', 'UNIQUE(name, location)',
         'Equipment with this name already exists at this location!'),
    ]