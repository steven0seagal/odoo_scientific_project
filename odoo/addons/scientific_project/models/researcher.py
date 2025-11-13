from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import logging
import base64
import imghdr

_logger = logging.getLogger(__name__)

class ScientificResearcher(models.Model):
    _name = 'scientific.researcher'
    _description = 'Researcher'
    _sql_constraints = [
        ('email_unique', 'UNIQUE(email)', 'Email address must be unique!'),
        ('user_id_unique', 'UNIQUE(user_id)', 'User account already linked to another researcher!'),
    ]

    user_id = fields.Many2one('res.users', string='User')
    name = fields.Char(string='Name', required=True)
    type = fields.Selection([('student', 'Student'), ('professor', 'Professor'), ('researcher', 'Researcher')], string='Type')
    title = fields.Char(string='Title')
    affiliation = fields.Char(string='Affiliation')
    specialization = fields.Char(string='Specialization')
    tags = fields.Many2many('scientific.tags', string='Tags')
    image = fields.Binary(string='Image', attachment=True)
    image_size = fields.Float(string='Image Size (MB)', compute='_compute_image_size')
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
        researchers = super(ScientificResearcher, self).create(vals_list)
        users = self.env['res.users']

        for researcher in researchers:
            # Only create user if email is provided
            if not researcher.email:
                _logger.warning(f"Researcher {researcher.name} created without email - user account not created")
                continue

            try:
                # Check if user with this login already exists
                existing_user = users.search([('login', '=', researcher.email)], limit=1)
                if existing_user:
                    researcher.write({'user_id': existing_user.id})
                    _logger.info(f"Linked researcher {researcher.name} to existing user {existing_user.login}")
                else:
                    user_vals = {
                        'name': researcher.name,
                        'login': researcher.email,  # Use email as login
                        'email': researcher.email,
                        'groups_id': [(6, 0, [self.env.ref('base.group_user').id])],
                    }
                    user = users.create(user_vals)
                    researcher.write({'user_id': user.id})
                    _logger.info(f"Created user account for researcher {researcher.name}")
            except Exception as e:
                _logger.error(f"Failed to create user for researcher {researcher.name}: {str(e)}")
                # Don't fail the researcher creation, just log the error
                continue

        return researchers

    # Image upload security constants
    MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5MB
    ALLOWED_IMAGE_FORMATS = ['png', 'jpeg', 'jpg', 'gif', 'bmp', 'webp']

    @api.depends('image')
    def _compute_image_size(self):
        """Calculate image size in MB"""
        for record in self:
            if record.image:
                try:
                    image_data = base64.b64decode(record.image)
                    record.image_size = len(image_data) / (1024 * 1024)
                except Exception:
                    record.image_size = 0.0
            else:
                record.image_size = 0.0

    @api.constrains('email')
    def _check_email_format(self):
        """Validate email format"""
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        for record in self:
            if record.email and not re.match(email_pattern, record.email):
                raise ValidationError(f"Invalid email format: {record.email}")

    @api.constrains('image', 'image_size')
    def _check_image_upload_security(self):
        """Validate image uploads for security"""
        for record in self:
            if record.image:
                # Check size
                if record.image_size > (self.MAX_IMAGE_SIZE / (1024 * 1024)):
                    raise ValidationError(
                        f'Image size ({record.image_size:.2f} MB) exceeds maximum allowed size '
                        f'of {self.MAX_IMAGE_SIZE / (1024 * 1024)} MB. '
                        f'Please upload a smaller image or compress it.'
                    )

                # Validate image format
                try:
                    image_data = base64.b64decode(record.image)
                    image_format = imghdr.what(None, h=image_data)

                    if image_format not in self.ALLOWED_IMAGE_FORMATS:
                        raise ValidationError(
                            f'Invalid image format "{image_format}". '
                            f'Allowed formats: {", ".join(self.ALLOWED_IMAGE_FORMATS).upper()}. '
                            f'Please upload a valid image file.'
                        )
                except Exception as e:
                    raise ValidationError(f'Invalid image file: {str(e)}')
class ScientificResearcherTags(models.Model):
    _name = 'scientific.tags'
    _description = 'Researcher Tags'
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Tag name must be unique!'),
    ]

    name = fields.Char(string='Name', required=True)
    researcher_ids = fields.Many2many('scientific.researcher', string='Researchers')
    color = fields.Integer(string='Color Index')