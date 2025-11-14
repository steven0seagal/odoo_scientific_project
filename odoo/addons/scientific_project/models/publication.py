from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class ScientificPublication(models.Model):
    _name = 'scientific.publication'
    _description = 'Publication'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'publication_date desc, id desc'

    title = fields.Char(string='Title', required=True, tracking=True)
    authors_ids = fields.Many2many('scientific.researcher', string='Authors', tracking=True)
    journal_conference = fields.Char(string='Journal/Conference', tracking=True)
    doi = fields.Char(string='DOI')
    url = fields.Char(string='URL')
    abstract = fields.Text(string='Abstract')
    keywords = fields.Char(string='Keywords')
    publication_date = fields.Date(string='Publication Date', tracking=True)
    submission_date = fields.Date(string='Submission Date')
    acceptance_date = fields.Date(string='Acceptance Date')

    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('accepted', 'Accepted'),
        ('published', 'Published'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft', tracking=True)

    publication_type = fields.Selection([
        ('journal_article', 'Journal Article'),
        ('conference_paper', 'Conference Paper'),
        ('book_chapter', 'Book Chapter'),
        ('thesis', 'Thesis'),
        ('preprint', 'Preprint'),
        ('poster', 'Poster'),
        ('other', 'Other')
    ], string='Type', default='journal_article')

    impact_factor = fields.Float(string='Impact Factor')
    citation_count = fields.Integer(string='Citations', default=0)

    project_id = fields.Many2one('scientific.project', string='Project', tracking=True)
    experiment_ids = fields.Many2many('scientific.experiment', string='Related Experiments')
    task_ids = fields.Many2many('scientific.task', string='Related Tasks')
    document_ids = fields.Many2many('scientific.document', string='Documents')

    notes = fields.Text(string='Notes')

    # Computed fields
    author_count = fields.Integer(string='Authors', compute='_compute_author_count', store=True)
    is_published = fields.Boolean(string='Published', compute='_compute_is_published', store=True)
    citation_info = fields.Char(string='Citation', compute='_compute_citation_info')
    experiment_count = fields.Integer(string='Experiments', compute='_compute_experiment_count')

    @api.depends('authors_ids')
    def _compute_author_count(self):
        """Count number of authors"""
        for record in self:
            record.author_count = len(record.authors_ids)

    @api.depends('status')
    def _compute_is_published(self):
        """Check if publication is published"""
        for record in self:
            record.is_published = record.status == 'published'

    @api.depends('title', 'authors_ids', 'journal_conference', 'publication_date')
    def _compute_citation_info(self):
        """Generate citation string"""
        for record in self:
            authors = ', '.join(record.authors_ids.mapped('name')[:3])
            if len(record.authors_ids) > 3:
                authors += ' et al.'
            year = record.publication_date.year if record.publication_date else 'n.d.'
            journal = record.journal_conference or 'Unknown'
            record.citation_info = f'{authors} ({year}). {record.title}. {journal}.'

    @api.depends('experiment_ids')
    def _compute_experiment_count(self):
        """Count number of related experiments"""
        for record in self:
            record.experiment_count = len(record.experiment_ids)

    @api.constrains('doi')
    def _check_doi(self):
        """Validate DOI format"""
        for record in self:
            if record.doi:
                # Basic DOI format validation
                if not re.match(r'^10\.\d{4,}\/\S+', record.doi):
                    raise ValidationError('Invalid DOI format! DOI should start with "10." followed by numbers and a slash.')

    @api.constrains('submission_date', 'acceptance_date', 'publication_date')
    def _check_dates(self):
        """Validate publication dates sequence"""
        for record in self:
            if record.submission_date and record.acceptance_date:
                if record.acceptance_date < record.submission_date:
                    raise ValidationError('Acceptance date cannot be before submission date!')
            if record.acceptance_date and record.publication_date:
                if record.publication_date < record.acceptance_date:
                    raise ValidationError('Publication date cannot be before acceptance date!')

    def action_submit(self):
        """Mark publication as submitted"""
        self.status = 'submitted'
        if not self.submission_date:
            self.submission_date = fields.Date.today()

    def action_under_review(self):
        """Mark publication as under review"""
        self.status = 'under_review'

    def action_accept(self):
        """Mark publication as accepted"""
        self.status = 'accepted'
        if not self.acceptance_date:
            self.acceptance_date = fields.Date.today()

    def action_publish(self):
        """Mark publication as published"""
        self.status = 'published'
        if not self.publication_date:
            self.publication_date = fields.Date.today()

    def action_reject(self):
        """Mark publication as rejected"""
        self.status = 'rejected'

    def action_view_experiments(self):
        """Smart button action to view related experiments"""
        return {
            'name': 'Experiments',
            'type': 'ir.actions.act_window',
            'res_model': 'scientific.experiment',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.experiment_ids.ids)],
            'context': {'default_publication_ids': [(4, self.id)]}
        }