from odoo import models, fields

class ScientificPartner(models.Model):
    _name = 'scientific.partner'
    _description = 'Partner/Collaborator'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Partner name must be unique!'),
    ]

    name = fields.Char(string='Partner Name', required=True, tracking=True)
    partner_type = fields.Selection([
        ('university', 'University'),
        ('industry', 'Industry Partner'),
        ('government', 'Government Agency'),
        ('research_institute', 'Research Institute'),
        ('ngo', 'NGO/Non-Profit'),
        ('individual', 'Individual Collaborator'),
    ], string='Type', default='university', tracking=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('potential', 'Potential'),
    ], string='Status', default='active', tracking=True)
    country = fields.Char(string='Country')
    city = fields.Char(string='City')
    website = fields.Char(string='Website')
    contact_person = fields.Char(string='Contact Person')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    collaboration_type = fields.Selection([
        ('research', 'Research Collaboration'),
        ('funding', 'Funding Partner'),
        ('data_sharing', 'Data Sharing'),
        ('equipment', 'Equipment Sharing'),
        ('advisory', 'Advisory Role'),
    ], string='Collaboration Type')
    start_date = fields.Date(string='Partnership Start Date')
    end_date = fields.Date(string='Partnership End Date')
    project_ids = fields.Many2many('scientific.project', string='Related Projects')
    notes = fields.Text(string='Notes')
    active = fields.Boolean(string='Active', default=True)

