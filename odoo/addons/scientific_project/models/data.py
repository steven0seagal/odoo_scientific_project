from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ScientificDataManagement(models.Model):
    _name = 'scientific.data_management'
    _description = 'Data Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc, id desc'

    name = fields.Char(string='Dataset Name', required=True, tracking=True)
    description = fields.Text(string='Description')

    data_type = fields.Selection([
        ('raw_data', 'Raw Data'),
        ('processed_data', 'Processed Data'),
        ('analysis_results', 'Analysis Results'),
        ('metadata', 'Metadata'),
        ('images', 'Images/Figures'),
        ('sequences', 'Sequences'),
        ('other', 'Other')
    ], string='Data Type', default='raw_data', required=True)

    file_attachment = fields.Binary(string='Data File', attachment=True)
    file_name = fields.Char(string='File Name')
    file_size = fields.Float(string='File Size (MB)', compute='_compute_file_size', store=True)

    storage_location = fields.Char(string='Storage Location', help='Physical or cloud storage location')
    storage_path = fields.Char(string='Storage Path', help='Full path to data')

    access_level = fields.Selection([
        ('public', 'Public'),
        ('internal', 'Internal'),
        ('restricted', 'Restricted'),
        ('confidential', 'Confidential')
    ], string='Access Level', default='internal', required=True, tracking=True)

    version = fields.Char(string='Version', default='1.0')

    # Relationships
    project_id = fields.Many2one('scientific.project', string='Project', ondelete='cascade')
    experiment_id = fields.Many2one('scientific.experiment', string='Experiment', ondelete='set null')
    researcher_id = fields.Many2one('scientific.researcher', string='Data Owner', tracking=True)

    # Dates
    collection_date = fields.Date(string='Collection Date')
    upload_date = fields.Date(string='Upload Date', default=fields.Date.today)
    expiry_date = fields.Date(string='Expiry Date', help='Data retention policy expiry')

    # Metadata
    metadata = fields.Text(string='Metadata', help='Additional structured metadata (JSON format)')
    keywords = fields.Char(string='Keywords')

    # Status
    status = fields.Selection([
        ('draft', 'Draft'),
        ('validated', 'Validated'),
        ('archived', 'Archived'),
        ('deprecated', 'Deprecated')
    ], string='Status', default='draft', tracking=True)

    checksum = fields.Char(string='Checksum', help='File integrity checksum (MD5/SHA256)')

    # Computed field
    is_expired = fields.Boolean(string='Expired', compute='_compute_is_expired')

    @api.depends('file_attachment')
    def _compute_file_size(self):
        for record in self:
            if record.file_attachment:
                # Approximate size in MB
                record.file_size = len(record.file_attachment) / (1024 * 1024)
            else:
                record.file_size = 0.0

    @api.depends('expiry_date')
    def _compute_is_expired(self):
        today = fields.Date.today()
        for record in self:
            record.is_expired = record.expiry_date and record.expiry_date < today

    @api.constrains('version')
    def _check_version_format(self):
        """Validate version format"""
        import re
        version_pattern = r'^\d+\.\d+(\.\d+)?$'
        for record in self:
            if record.version and not re.match(version_pattern, record.version):
                raise ValidationError('Version must be in format X.Y or X.Y.Z (e.g., 1.0 or 1.0.1)')