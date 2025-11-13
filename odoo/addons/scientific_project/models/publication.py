from odoo import models, fields, api

class ScientificPublication(models.Model):
    _name = 'scientific.publication'
    _description = 'Publication'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'publication_date desc, id desc'

    title = fields.Char(string='Title', required=True, tracking=True)
    abstract = fields.Text(string='Abstract')
    authors_ids = fields.Many2many('scientific.researcher', string='Authors', tracking=True)
    journal_conference = fields.Char(string='Journal/Conference', tracking=True)
    doi = fields.Char(string='DOI', help='Digital Object Identifier')
    url = fields.Char(string='URL', help='Publication URL')
    publication_date = fields.Date(string='Publication Date', tracking=True)
    submission_date = fields.Date(string='Submission Date')
    acceptance_date = fields.Date(string='Acceptance Date')

    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('revision', 'Revision Required'),
        ('accepted', 'Accepted'),
        ('published', 'Published'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft', required=True, tracking=True)

    publication_type = fields.Selection([
        ('journal', 'Journal Article'),
        ('conference', 'Conference Paper'),
        ('book', 'Book'),
        ('chapter', 'Book Chapter'),
        ('poster', 'Poster'),
        ('thesis', 'Thesis'),
        ('preprint', 'Preprint'),
        ('report', 'Technical Report')
    ], string='Type', default='journal')

    impact_factor = fields.Float(string='Impact Factor')
    citations_count = fields.Integer(string='Citations', default=0)

    project_id = fields.Many2one('scientific.project', string='Related Project', ondelete='set null')
    experiment_ids = fields.Many2many('scientific.experiment', string='Related Experiments')
    task_ids = fields.Many2many('scientific.task', string='Related Tasks')
    document_ids = fields.Many2many('scientific.document', string='Attachments')

    keywords = fields.Char(string='Keywords', help='Comma-separated keywords')
    notes = fields.Text(string='Internal Notes')

    # Computed fields
    author_count = fields.Integer(string='Number of Authors', compute='_compute_author_count', store=True)

    @api.depends('authors_ids')
    def _compute_author_count(self):
        for record in self:
            record.author_count = len(record.authors_ids)

    @api.constrains('submission_date', 'acceptance_date', 'publication_date')
    def _check_dates(self):
        """Ensure dates are in logical order"""
        for record in self:
            if record.submission_date and record.acceptance_date:
                if record.acceptance_date < record.submission_date:
                    raise models.ValidationError('Acceptance date cannot be before submission date')
            if record.acceptance_date and record.publication_date:
                if record.publication_date < record.acceptance_date:
                    raise models.ValidationError('Publication date cannot be before acceptance date')