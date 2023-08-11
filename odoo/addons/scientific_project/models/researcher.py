from odoo import models, fields

class ScientificResearcher(models.Model):
    _name = 'scientific.researcher'
    _description = 'Researcher'

    name = fields.Char(string='Name', required=True)
    title = fields.Char(string='Title')
    affiliation = fields.Char(string='Affiliation')
    contact_information = fields.Char(string='Contact Information')
    specialization = fields.Char(string='Specialization')