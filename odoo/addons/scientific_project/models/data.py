from odoo import models, fields

class ScientificDataManagement(models.Model):
    _name = 'scientific.data_management'
    _description = 'Data Management'

    data_type = fields.Selection([('raw_data', 'Raw Data'), ('processed_data', 'Processed Data')], string='Type')
    storage_location = fields.Char(string='Storage Location')
    access_controls = fields.Char(string='Access Controls')
    project_id = fields.Many2one('scientific.project', string='Project')