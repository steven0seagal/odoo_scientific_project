from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ScientificPartner(models.Model):
    _name = 'scientific.partner'
    _description = 'Partner/Collaborator'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    name = fields.Char(string='Name', required=True, tracking=True)
    partner_type = fields.Selection([
        ('university', 'University'),
        ('research_institute', 'Research Institute'),
        ('industry', 'Industry'),
        ('government', 'Government'),
        ('non_profit', 'Non-Profit'),
        ('individual', 'Individual'),
        ('other', 'Other')
    ], string='Type', default='university', tracking=True)

    # Contact Information
    contact_person = fields.Char(string='Contact Person')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    website = fields.Char(string='Website')

    # Address
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    city = fields.Char(string='City')
    state = fields.Char(string='State')
    zip = fields.Char(string='ZIP')
    country = fields.Char(string='Country')

    # Collaboration Details
    collaboration_start_date = fields.Date(string='Collaboration Start')
    collaboration_end_date = fields.Date(string='Collaboration End')
    collaboration_status = fields.Selection([
        ('potential', 'Potential'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('completed', 'Completed')
    ], string='Status', default='potential', tracking=True)

    description = fields.Text(string='Description')
    areas_of_expertise = fields.Text(string='Areas of Expertise')
    notes = fields.Text(string='Notes')

    # Relations
    project_ids = fields.Many2many('scientific.project', string='Related Projects')
    document_ids = fields.Many2many('scientific.document', string='Shared Documents')
    researcher_ids = fields.Many2many('scientific.researcher', string='Contact Researchers')

    # Computed fields
    project_count = fields.Integer(string='Projects', compute='_compute_project_count', store=True)
    active_projects = fields.Integer(string='Active Projects', compute='_compute_active_projects', store=True)
    is_active = fields.Boolean(string='Active', compute='_compute_is_active')

    @api.depends('project_ids')
    def _compute_project_count(self):
        """Count total projects"""
        for record in self:
            record.project_count = len(record.project_ids)

    @api.depends('project_ids.status')
    def _compute_active_projects(self):
        """Count active projects"""
        for record in self:
            record.active_projects = len(record.project_ids.filtered(lambda p: p.status == 'in_progress'))

    @api.depends('collaboration_status')
    def _compute_is_active(self):
        """Check if collaboration is active"""
        for record in self:
            record.is_active = record.collaboration_status == 'active'

    @api.constrains('email')
    def _check_email(self):
        """Validate email format"""
        import re
        for record in self:
            if record.email:
                if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', record.email):
                    raise ValidationError('Invalid email format!')

    @api.constrains('collaboration_start_date', 'collaboration_end_date')
    def _check_dates(self):
        """Validate collaboration dates"""
        for record in self:
            if record.collaboration_start_date and record.collaboration_end_date:
                if record.collaboration_end_date < record.collaboration_start_date:
                    raise ValidationError('End date must be after start date!')

    def action_view_projects(self):
        """View related projects"""
        return {
            'name': 'Projects',
            'type': 'ir.actions.act_window',
            'res_model': 'scientific.project',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.project_ids.ids)],
        }

    def action_view_active_projects(self):
        """View active projects"""
        active_project_ids = self.project_ids.filtered(lambda p: p.status == 'in_progress')
        return {
            'name': 'Active Projects',
            'type': 'ir.actions.act_window',
            'res_model': 'scientific.project',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', active_project_ids.ids)],
        }

