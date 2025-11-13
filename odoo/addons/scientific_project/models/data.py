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
        ('analysis', 'Analysis Results'),
        ('images', 'Images/Figures'),
        ('code', 'Code/Scripts'),
        ('other', 'Other')
    ], string='Type', default='raw_data', tracking=True)

    file_format = fields.Char(string='File Format')
    file_size = fields.Float(string='Size (MB)')
    storage_location = fields.Char(string='Storage Location', help='Physical or cloud storage location')

    access_level = fields.Selection([
        ('private', 'Private'),
        ('team', 'Team Only'),
        ('organization', 'Organization'),
        ('public', 'Public')
    ], string='Access Level', default='team', tracking=True)

    status = fields.Selection([
        ('draft', 'Draft'),
        ('validated', 'Validated'),
        ('archived', 'Archived'),
        ('deleted', 'Deleted')
    ], string='Status', default='draft', tracking=True)

    version = fields.Char(string='Version', default='1.0')
    checksum = fields.Char(string='Checksum/Hash', help='MD5 or SHA256 hash for data integrity')

    project_id = fields.Many2one('scientific.project', string='Project', tracking=True)
    experiment_id = fields.Many2one('scientific.experiment', string='Experiment')
    researcher_id = fields.Many2one('scientific.researcher', string='Owner', tracking=True)

    document_ids = fields.Many2many('scientific.document', string='Related Documents')

    upload_date = fields.Datetime(string='Upload Date', default=fields.Datetime.now)
    validation_date = fields.Date(string='Validation Date')
    archive_date = fields.Date(string='Archive Date')

    metadata = fields.Text(string='Metadata', help='Additional metadata in JSON format')
    notes = fields.Text(string='Notes')

    # Computed fields
    age_days = fields.Integer(string='Age (Days)', compute='_compute_age_days')
    is_recent = fields.Boolean(string='Recent', compute='_compute_is_recent')

    @api.depends('upload_date')
    def _compute_age_days(self):
        """Calculate age of dataset in days"""
        from datetime import datetime
        for record in self:
            if record.upload_date:
                delta = datetime.now() - record.upload_date
                record.age_days = delta.days
            else:
                record.age_days = 0

    @api.depends('age_days')
    def _compute_is_recent(self):
        """Check if dataset was uploaded recently (within 30 days)"""
        for record in self:
            record.is_recent = record.age_days <= 30

    @api.constrains('file_size')
    def _check_file_size(self):
        """Validate file size is positive"""
        for record in self:
            if record.file_size and record.file_size < 0:
                raise ValidationError('File size cannot be negative!')

    def action_validate(self):
        """Mark data as validated"""
        self.status = 'validated'
        self.validation_date = fields.Date.today()
        self.message_post(body='Dataset has been validated.')

    def action_archive_data(self):
        """Archive dataset"""
        self.status = 'archived'
        self.archive_date = fields.Date.today()
        self.message_post(body='Dataset has been archived.')

    def action_create_backup(self):
        """Create backup of dataset"""
        self.message_post(body='Backup creation initiated.')
        # Implementation would depend on actual backup system
        return True