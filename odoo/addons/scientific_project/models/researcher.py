from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ScientificResearcher(models.Model):
    _name = 'scientific.researcher'
    _description = 'Researcher'
    # _inherit = 'res.users'
    user_id = fields.Many2one('res.users', string='User')
    name = fields.Char(string='Name', required=True)
    type = fields.Selection([('student', 'Student'), ('professor', 'Professor'), ('researcher', 'Researcher')], string='Type')
    title = fields.Char(string='Title')
    affiliation = fields.Char(string='Affiliation')
    specialization = fields.Char(string='Specialization')
    tags = fields.Many2many('scientific.tags', string='Tags')
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


    @api.model_create_multi
    def create(self, vals_list):
        """Create researcher with proper error handling for user creation"""
        researchers = super(ScientificResearcher, self).create(vals_list)
        users = self.env['res.users']

        for researcher in researchers:
            # Only create user if email is provided and no user is linked
            if researcher.email and not researcher.user_id:
                try:
                    # Check if user with this email already exists
                    existing_user = users.search([('email', '=', researcher.email)], limit=1)
                    if existing_user:
                        researcher.write({'user_id': existing_user.id})
                    else:
                        # Generate unique login
                        base_login = researcher.email or researcher.name.lower().replace(' ', '_')
                        login = base_login
                        counter = 1
                        while users.search([('login', '=', login)], limit=1):
                            login = f'{base_login}{counter}'
                            counter += 1

                        user_vals = {
                            'name': researcher.name,
                            'login': login,
                            'email': researcher.email,
                        }
                        user = users.create(user_vals)
                        researcher.write({'user_id': user.id})
                except Exception as e:
                    # Log error but don't fail researcher creation
                    researcher.message_post(
                        body=f'Warning: Could not create user account: {str(e)}'
                    )

        return researchers

    @api.constrains('email')
    def _check_email(self):
        """Validate email format"""
        import re
        for record in self:
            if record.email:
                if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', record.email):
                    raise ValidationError('Invalid email format!')
class ScientificResearcherTags(models.Model):

    _name = 'scientific.tags'
    _description = 'Researcher Tags'

    name = fields.Char(string='Name', required=True)
    researcher_ids = fields.Many2many('scientific.researcher', string='Researchers')
    color = fields.Integer(string='Color Index')