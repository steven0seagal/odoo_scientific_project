from odoo import models, fields

class ScientificResearcher(models.Model):
    _name = 'scientific.researcher'
    _description = 'Researcher'
    # _inherit = 'res.partner'
    name = fields.Char(string='Name', required=True)
    type = fields.Selection([('student', 'Student'), ('professor', 'Professor'), ('researcher', 'Researcher')], string='Type')
    title = fields.Char(string='Title')
    affiliation = fields.Char(string='Affiliation')
    specialization = fields.Char(string='Specialization')
    tags = fields.Many2many('scientific.researcher.tags', string='Tags')
    image = fields.Binary(string='Image')
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    city = fields.Char(string='City')
    zip_code = fields.Char(string='Zip Code')
    country = fields.Char(string='Country')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')

    comment = fields.Text(string='Comment')
    projects = fields.Many2many('scientific.project', string='Projects')
    tasks = fields.Many2many('scientific.task', string='Tasks')
    experiments = fields.Many2many('scientific.experiment', string='Experiments')
    documents = fields.Many2many('scientific.document', string='Documents')
class ScientificResearcherTags(models.Model):
    _name = 'scientific.researcher.tags'
    _description = 'Researcher Tags'

    name = fields.Char(string='Name', required=True)
    researcher_ids = fields.Many2many('scientific.researcher', string='Researchers')
    color = fields.Integer(string='Color Index')