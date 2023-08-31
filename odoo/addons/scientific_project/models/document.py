from odoo import models, fields

class ScientificDocument(models.Model):
    _name = 'scientific.document'
    _description = 'Document'

    project_id = fields.Many2one('scientific.project', string='Project')
    task_id = fields.Many2one('scientific.task', string='Task')
    title = fields.Char(string='Title', required=True)
    file_name = fields.Char(string='File Name')
    file = fields.Binary(string='File')
    document_type = fields.Selection([('research_paper', 'Research Paper'), ('report', 'Report'), ('proposal', 'Proposal'), ('ethical_approval', 'Ethical Approval'), ('experimental_protocol', 'Experimental Protocol')], string='Type')
    author_ids = fields.Many2many('scientific.researcher', string='Authors')
    description = fields.Text(string='Description')
    version = fields.Char(string='Version')
    status = fields.Selection([('draft', 'Draft'), ('submitted', 'Submitted'), ('approved', 'Approved'), ('published', 'Published')], string='Status')
    # file_path = fields.Char(string='File Path/URL')
    creation_date = fields.Date(string='Creation Date')
    last_modified_date = fields.Date(string='Last Modified Date')
    review_date = fields.Date(string='Review Date')
    confidentiality_level = fields.Selection([('public', 'Public'), ('internal', 'Internal'), ('confidential', 'Confidential')], string='Confidentiality Level')
    associated_experiment_id = fields.Many2many('scientific.experiment', string='Associated Experiment/Task')
    keywords = fields.Char(string='Keywords')
    comments = fields.Text(string='Comments/Notes')
