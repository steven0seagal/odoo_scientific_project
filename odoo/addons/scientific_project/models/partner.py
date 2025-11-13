from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ScientificPartner(models.Model):
    _name = 'scientific.partner'
    _description = 'Research Partner/Collaborator'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    name = fields.Char(string='Organization Name', required=True, tracking=True)

    partner_type = fields.Selection([
        ('university', 'University'),
        ('research_institute', 'Research Institute'),
        ('industry', 'Industry Partner'),
        ('government', 'Government Agency'),
        ('ngo', 'NGO'),
        ('hospital', 'Hospital/Medical Center'),
        ('funding_agency', 'Funding Agency'),
        ('other', 'Other')
    ], string='Type', default='university', required=True)

    # Contact Information
    contact_person = fields.Char(string='Contact Person')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    website = fields.Char(string='Website')

    # Address
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street 2')
    city = fields.Char(string='City')
    state = fields.Char(string='State/Province')
    zip_code = fields.Char(string='ZIP Code')
    country = fields.Char(string='Country')

    # Collaboration Details
    collaboration_type = fields.Selection([
        ('research', 'Research Collaboration'),
        ('funding', 'Funding Partner'),
        ('equipment', 'Equipment Sharing'),
        ('data', 'Data Sharing'),
        ('publication', 'Co-Publication'),
        ('consulting', 'Consulting'),
        ('other', 'Other')
    ], string='Collaboration Type')

    status = fields.Selection([
        ('prospect', 'Prospect'),
        ('active', 'Active Partner'),
        ('inactive', 'Inactive'),
        ('former', 'Former Partner')
    ], string='Status', default='active', tracking=True)

    # Relationships
    project_ids = fields.Many2many('scientific.project', string='Projects',
                                   relation='scientific_project_partner_rel',
                                   column1='partner_id', column2='project_id')
    researcher_ids = fields.Many2many('scientific.researcher', string='Contact Researchers')

    # Agreement Details
    agreement_start_date = fields.Date(string='Agreement Start Date')
    agreement_end_date = fields.Date(string='Agreement End Date')
    agreement_document = fields.Binary(string='Agreement Document', attachment=True)
    agreement_file_name = fields.Char(string='Agreement File Name')

    # Additional Info
    specialization = fields.Text(string='Specialization/Expertise')
    notes = fields.Text(string='Internal Notes')
    active = fields.Boolean(string='Active', default=True)

    # Computed fields
    project_count = fields.Integer(string='Projects Count', compute='_compute_project_count', store=True)
    is_agreement_active = fields.Boolean(string='Agreement Active', compute='_compute_is_agreement_active')

    @api.depends('project_ids')
    def _compute_project_count(self):
        for record in self:
            record.project_count = len(record.project_ids)

    @api.depends('agreement_start_date', 'agreement_end_date')
    def _compute_is_agreement_active(self):
        today = fields.Date.today()
        for record in self:
            if record.agreement_start_date and record.agreement_end_date:
                record.is_agreement_active = record.agreement_start_date <= today <= record.agreement_end_date
            else:
                record.is_agreement_active = False

    @api.constrains('email')
    def _check_email_format(self):
        """Validate email format"""
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        for record in self:
            if record.email and not re.match(email_pattern, record.email):
                raise ValidationError(f"Invalid email format: {record.email}")

    @api.constrains('agreement_start_date', 'agreement_end_date')
    def _check_agreement_dates(self):
        """Ensure agreement end date is after start date"""
        for record in self:
            if record.agreement_start_date and record.agreement_end_date:
                if record.agreement_end_date < record.agreement_start_date:
                    raise ValidationError('Agreement end date cannot be before start date')

