from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ScientificDataManagement(models.Model):
    _name = 'scientific.data_management'
    _description = 'Data Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'upload_date desc, name'

    name = fields.Char(string='Dataset Name', required=True, tracking=True)
    description = fields.Text(string='Description')
    data_type = fields.Selection([
        ('raw_data', 'Raw Data'),
        ('processed_data', 'Processed Data'),
        ('analysis_results', 'Analysis Results'),
        ('metadata', 'Metadata'),
    ], string='Type', default='raw_data', tracking=True)
    file = fields.Binary(string='Data File', attachment=True)
    file_name = fields.Char(string='File Name')
    file_size = fields.Integer(string='File Size (bytes)', compute='_compute_file_size', store=True)
    format = fields.Selection([
        ('csv', 'CSV'),
        ('xlsx', 'Excel'),
        ('json', 'JSON'),
        ('xml', 'XML'),
        ('hdf5', 'HDF5'),
        ('other', 'Other'),
    ], string='Format', default='csv')
    version = fields.Char(string='Version', default='1.0')
    storage_location = fields.Char(string='Storage Location', help='Physical or cloud storage location')
    access_level = fields.Selection([
        ('public', 'Public'),
        ('internal', 'Internal'),
        ('restricted', 'Restricted'),
        ('confidential', 'Confidential'),
    ], string='Access Level', default='internal', tracking=True)
    upload_date = fields.Date(string='Upload Date', default=fields.Date.today, tracking=True)
    last_modified = fields.Datetime(string='Last Modified', default=fields.Datetime.now)
    project_id = fields.Many2one('scientific.project', string='Project', ondelete='cascade', tracking=True)
    experiment_id = fields.Many2one('scientific.experiment', string='Experiment', ondelete='set null')
    researcher_id = fields.Many2one('scientific.researcher', string='Uploaded By', default=lambda self: self.env.user.id)
    notes = fields.Text(string='Notes')

    @api.depends('file')
    def _compute_file_size(self):
        """Compute file size"""
        import base64
        for record in self:
            if record.file:
                try:
                    record.file_size = len(base64.b64decode(record.file))
                except Exception:
                    record.file_size = 0
            else:
                record.file_size = 0