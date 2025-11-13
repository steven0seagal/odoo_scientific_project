from odoo import models, fields, api
from odoo.exceptions import ValidationError
import base64
import mimetypes

class ScientificDocument(models.Model):
    _name = 'scientific.document'
    _description = 'Document'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'creation_date desc, id desc'

    project_id = fields.Many2many('scientific.project', string='Project')
    task_id = fields.Many2one('scientific.task', string='Task')
    title = fields.Char(string='Title', required=True, tracking=True)
    file_name = fields.Char(string='File Name')
    file = fields.Binary(string='File', attachment=True, tracking=True)
    file_size = fields.Float(string='File Size (MB)', compute='_compute_file_size', store=True)
    document_type = fields.Selection([
        ('research_paper', 'Research Paper'),
        ('report', 'Report'),
        ('proposal', 'Proposal'),
        ('ethical_approval', 'Ethical Approval'),
        ('experimental_protocol', 'Experimental Protocol')
    ], string='Type', tracking=True)
    author_ids = fields.Many2many('scientific.researcher', string='Authors', tracking=True)
    description = fields.Text(string='Description')
    version = fields.Char(string='Version', default='1.0')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('published', 'Published')
    ], string='Status', default='draft', tracking=True)
    creation_date = fields.Date(string='Creation Date', default=fields.Date.today)
    last_modified_date = fields.Date(string='Last Modified Date')
    review_date = fields.Date(string='Review Date')
    confidentiality_level = fields.Selection([
        ('public', 'Public'),
        ('internal', 'Internal'),
        ('confidential', 'Confidential')
    ], string='Confidentiality Level', default='internal', tracking=True)
    associated_experiment_id = fields.Many2many('scientific.experiment', string='Associated Experiment/Task')
    keywords = fields.Char(string='Keywords')
    comments = fields.Text(string='Comments/Notes')

    # File upload security constants
    MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
    ALLOWED_DOCUMENT_TYPES = {
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'text/plain',
        'application/vnd.ms-excel',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/vnd.ms-powerpoint',
        'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        'text/csv',
        'application/zip',
        'application/x-zip-compressed',
    }

    @api.depends('file')
    def _compute_file_size(self):
        """Calculate file size in MB"""
        for record in self:
            if record.file:
                try:
                    file_data = base64.b64decode(record.file)
                    record.file_size = len(file_data) / (1024 * 1024)  # Convert to MB
                except Exception:
                    record.file_size = 0.0
            else:
                record.file_size = 0.0

    @api.constrains('file', 'file_name', 'file_size')
    def _check_file_upload_security(self):
        """Validate file uploads for security"""
        for record in self:
            if record.file:
                # Check file size
                if record.file_size > (self.MAX_FILE_SIZE / (1024 * 1024)):
                    raise ValidationError(
                        f'File size ({record.file_size:.2f} MB) exceeds maximum allowed size '
                        f'of {self.MAX_FILE_SIZE / (1024 * 1024)} MB. '
                        f'Please upload a smaller file or compress it.'
                    )

                # Check file type if filename is provided
                if record.file_name:
                    # Get MIME type from filename
                    mime_type, _ = mimetypes.guess_type(record.file_name)

                    if mime_type:
                        # Check against allowed types
                        if mime_type not in self.ALLOWED_DOCUMENT_TYPES:
                            raise ValidationError(
                                f'File type "{mime_type}" is not allowed. '
                                f'Allowed types: PDF, Word, Excel, PowerPoint, Text, CSV, ZIP. '
                                f'Executable files and scripts are not permitted for security reasons.'
                            )

                    # Additional check for dangerous extensions
                    dangerous_extensions = [
                        '.exe', '.bat', '.cmd', '.com', '.pif', '.scr', '.vbs',
                        '.js', '.jar', '.msi', '.app', '.deb', '.rpm', '.sh',
                        '.ps1', '.psm1', '.py', '.rb', '.pl', '.php'
                    ]
                    file_ext = record.file_name.lower()[-5:] if len(record.file_name) > 5 else record.file_name.lower()

                    for ext in dangerous_extensions:
                        if file_ext.endswith(ext):
                            raise ValidationError(
                                f'Files with extension "{ext}" are not allowed for security reasons. '
                                f'Executable files and scripts cannot be uploaded.'
                            )

    @api.constrains('creation_date', 'review_date')
    def _check_dates(self):
        """Ensure review date is after creation date"""
        for record in self:
            if record.creation_date and record.review_date:
                if record.review_date < record.creation_date:
                    raise ValidationError('Review date cannot be before creation date')

    @api.model
    def create(self, vals):
        """Set last modified date on creation"""
        vals['last_modified_date'] = fields.Date.today()
        return super().create(vals)

    def write(self, vals):
        """Update last modified date on any change"""
        vals['last_modified_date'] = fields.Date.today()
        return super().write(vals)
