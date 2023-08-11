from odoo import models, fields

class ScientificPartner(models.Model):
    _name = 'scientific.partner'
    _description = 'Partner'

    name = fields.Char(string='Name', required=True)
    partner_type = fields.Selection([('university', 'University'), ('industry', 'Industry'), ('government', 'Government')], string='Type')
    contact_information = fields.Char(string='Contact Information')

