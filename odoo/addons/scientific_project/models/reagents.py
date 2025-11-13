from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ScientificReagent(models.Model):
    _name = 'scientific.reagent'
    _description = 'Reagent'
    _order = 'name, location'

    name = fields.Char(string='Reagent', required=True)
    type = fields.Char(string='Type')
    location = fields.Char(string='Location')
    status = fields.Selection([
        ('available', 'Available'),
        ('not_available', 'Not available'),
        ('in_delivery', 'In delivery'),
        ('depleted', 'Depleted')
    ], string='Status', default='available')
    amount = fields.Float(string='Amount', default=0.0)
    units = fields.Char(string='Units', default='ml')
    experiment_id = fields.Many2one('scientific.experiment', string='Experiment')
    notes = fields.Text(string='Notes')

    @api.constrains('amount')
    def _check_amount(self):
        """Validate that amount is not negative"""
        for record in self:
            if record.amount < 0:
                raise ValidationError("Amount cannot be negative!")

