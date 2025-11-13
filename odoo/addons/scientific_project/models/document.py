from odoo import models, fields, api
from odoo.exceptions import ValidationError
import base64

class ScientificDocument(models.Model):
    _name = 'scientific.document'
    _description = 'Document'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'creation_date desc, title'

    project_id = fields.Many2many('scientific.project', string='Project')
    task_id = fields.Many2one('scientific.task', string='Task')
    title = fields.Char(string='Title', required=True, tracking=True)
    file_name = fields.Char(string='File Name')
    file = fields.Binary(string='File', attachment=True, tracking=True)
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
    ], string='Confidentiality Level', default='internal', tracking=True,
       help="Public: Accessible to everyone\nInternal: Accessible to team members\nConfidential: Restricted access")
    associated_experiment_id = fields.Many2many('scientific.experiment', string='Associated Experiment/Task')
    keywords = fields.Char(string='Keywords')
    comments = fields.Text(string='Comments/Notes')

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

    @api.constrains('file', 'file_size')
    def _check_file_constraints(self):
        """Validate file size and type"""
        MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
        ALLOWED_DOCUMENT_EXTENSIONS = [
            'pdf', 'doc', 'docx', 'txt', 'odt',
            'xls', 'xlsx', 'ods', 'csv',
            'ppt', 'pptx', 'odp',
            'zip', 'tar', 'gz',
            'png', 'jpg', 'jpeg', 'gif', 'bmp', 'svg',
        ]

        for record in self:
            if record.file:
                # Check file size
                if record.file_size > MAX_FILE_SIZE:
                    raise ValidationError(
                        f"File size ({record.file_size / (1024*1024):.2f} MB) "
                        f"exceeds maximum allowed size ({MAX_FILE_SIZE / (1024*1024)} MB)"
                    )

                # Check file extension if filename is provided
                if record.file_name:
                    file_ext = record.file_name.split('.')[-1].lower()
                    if file_ext not in ALLOWED_DOCUMENT_EXTENSIONS:
                        raise ValidationError(
                            f"File type '.{file_ext}' is not allowed.\n"
                            f"Allowed types: {', '.join(ALLOWED_DOCUMENT_EXTENSIONS)}"
                        )

    @api.constrains('creation_date', 'review_date')
    def _check_date_range(self):
        """Validate that review date is not before creation date"""
        for record in self:
            if record.creation_date and record.review_date:
                if record.review_date < record.creation_date:
                    raise ValidationError(
                        "Review date cannot be earlier than creation date.\n"
                        f"Creation: {record.creation_date}\n"
                        f"Review: {record.review_date}"
                    )

    def write(self, vals):
        """Update last modified date automatically"""
        if not vals.get('last_modified_date'):
            vals['last_modified_date'] = fields.Date.today()
        return super(ScientificDocument, self).write(vals)
