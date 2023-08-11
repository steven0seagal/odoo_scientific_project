from odoo import models, fields

class ScientificEquipment(models.Model):
    _name = 'scientific.equipment'
    _description = 'Equipment'

    name = fields.Char(string='Name', required=True)
    equipment_type = fields.Char(string='Type')
    location = fields.Char(string='Location')
    status = fields.Selection([('available', 'Available'), ('in_use', 'In Use'), ('maintenance', 'Maintenance')], string='Status')
    maintenance_schedule = fields.Date(string='Maintenance Schedule')