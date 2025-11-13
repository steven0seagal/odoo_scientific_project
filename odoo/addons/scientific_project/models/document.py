from odoo import models, fields, api
from odoo.exceptions import ValidationError
import base64
import mimetypes

class ScientificDocument(models.Model):
    _name = 'scientific.document'
    _description = 'Document'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'creation_date desc, title'

    project_id = fields.Many2many('scientific.project', string='Project')
    task_id = fields.Many2one('scientific.task', string='Task', tracking=True)
    title = fields.Char(string='Title', required=True, tracking=True,
                        help="Document title")
    file_name = fields.Char(string='File Name', tracking=True)
    file = fields.Binary(string='File', attachment=True)
    file_size = fields.Integer(string='File Size (bytes)', compute='_compute_file_size', store=True)
    document_type = fields.Selection([
        ('research_paper', 'Research Paper'),
        ('report', 'Report'),
        ('proposal', 'Proposal'),
        ('ethical_approval', 'Ethical Approval'),
        ('experimental_protocol', 'Experimental Protocol')
    ], string='Type', tracking=True)
    author_ids = fields.Many2many('scientific.researcher', string='Authors', tracking=True)
    description = fields.Text(string='Description')
    version = fields.Char(string='Version', default='1.0', tracking=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('published', 'Published')
    ], string='Status', default='draft', tracking=True, required=True,
       help="Document review status")
    creation_date = fields.Date(string='Creation Date', default=fields.Date.context_today, tracking=True)
    last_modified_date = fields.Date(string='Last Modified Date', tracking=True)
    review_date = fields.Date(string='Review Date', tracking=True)
    confidentiality_level = fields.Selection([
        ('public', 'Public'),
        ('internal', 'Internal'),
        ('confidential', 'Confidential')
    ], string='Confidentiality Level', default='internal', tracking=True, required=True,
       help="Public: Anyone can view; Internal: Organization only; Confidential: Restricted access")
    associated_experiment_id = fields.Many2many('scientific.experiment', string='Associated Experiment/Task')
    keywords = fields.Char(string='Keywords', help="Comma-separated keywords for searchability")
    comments = fields.Text(string='Comments/Notes')

    # Allowed document types
    ALLOWED_DOCUMENT_MIMETYPES = [
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
    ]

    MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB

    @api.depends('file')
    def _compute_file_size(self):
        """Compute the size of the uploaded file"""
        for record in self:
            if record.file:
                try:
                    record.file_size = len(base64.b64decode(record.file))
                except Exception:
                    record.file_size = 0
            else:
                record.file_size = 0

    @api.constrains('file', 'file_size', 'file_name')
    def _check_file_constraints(self):
        """Validate file size and type"""
        for record in self:
            if record.file and record.file_size > self.MAX_FILE_SIZE:
                raise ValidationError(
                    f"File size ({record.file_size / (1024*1024):.2f} MB) "
                    f"exceeds maximum allowed size ({self.MAX_FILE_SIZE / (1024*1024)} MB)"
                )

            # Validate file type based on extension
            if record.file and record.file_name:
                mimetype, _ = mimetypes.guess_type(record.file_name)
                if mimetype and mimetype not in self.ALLOWED_DOCUMENT_MIMETYPES:
                    raise ValidationError(
                        f"File type '{mimetype}' is not allowed. "
                        f"Allowed types: PDF, Word, Excel, PowerPoint, Text, CSV, ZIP"
                    )

    @api.constrains('creation_date', 'review_date')
    def _check_date_range(self):
        """Validate date ranges"""
        for record in self:
            if record.creation_date and record.review_date:
                if record.review_date < record.creation_date:
                    raise ValidationError(
                        "Review date cannot be earlier than creation date.\n"
                        f"Creation: {record.creation_date}\n"
                        f"Review: {record.review_date}"
                    )
