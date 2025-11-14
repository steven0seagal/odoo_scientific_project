from odoo import models, fields, api

class ScientificPublication(models.Model):
    _name = 'scientific.publication'
    _description = 'Publication'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'publication_date desc, title'

    title = fields.Char(string='Title', required=True, tracking=True)
    authors_ids = fields.Many2many('scientific.researcher', string='Authors', tracking=True)
    journal_conference = fields.Char(string='Journal/Conference', tracking=True)
    publication_type = fields.Selection([
        ('journal', 'Journal Article'),
        ('conference', 'Conference Paper'),
        ('book_chapter', 'Book Chapter'),
        ('thesis', 'Thesis/Dissertation'),
        ('preprint', 'Preprint'),
        ('poster', 'Poster'),
    ], string='Type', default='journal', tracking=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('revision', 'Revision Required'),
        ('accepted', 'Accepted'),
        ('published', 'Published'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', tracking=True)
    doi = fields.Char(string='DOI', help='Digital Object Identifier')
    url = fields.Char(string='URL')
    publication_date = fields.Date(string='Publication Date', tracking=True)
    submission_date = fields.Date(string='Submission Date')
    acceptance_date = fields.Date(string='Acceptance Date')
    impact_factor = fields.Float(string='Impact Factor', digits=(5, 3))
    citation_count = fields.Integer(string='Citation Count', default=0)
    abstract = fields.Text(string='Abstract')
    keywords = fields.Char(string='Keywords')
    project_id = fields.Many2one('scientific.project', string='Project', ondelete='set null', tracking=True)
    experiment_ids = fields.Many2many('scientific.experiment', string='Related Experiments')
    task_ids = fields.Many2many('scientific.task', string='Related Tasks')
    notes = fields.Text(string='Notes')