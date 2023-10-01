from odoo import models, fields

class ScientificReagent(models.Model):
    _name = 'scientific.reagent'
    _description = 'Reagent'


    name = fields.Char(string='Reagent', required=True)
    type = fields.Char(string='Type')
    location  = fields.Char(string='Location')
    status = fields.Selection([('available', 'Available'), ('not_available', 'Not available'), ('in_delivery', 'In delivery')], string='Status')
    amount = fields.Integer(string='Amount')
    units = fields.Char(string='Units')
    experiment_id = fields.Many2one('scientific.experiment', string='Experiment')
    notes = fields.Text(string='Notes')

