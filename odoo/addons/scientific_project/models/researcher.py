from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ScientificResearcher(models.Model):
    _name = 'scientific.researcher'
    _description = 'Researcher'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    user_id = fields.Many2one('res.users', string='User', tracking=True)
    name = fields.Char(string='Name', required=True, tracking=True,
                       help="Full name of the researcher")
    type = fields.Selection([
        ('student', 'Student'),
        ('professor', 'Professor'),
        ('researcher', 'Researcher')
    ], string='Type', tracking=True, help="Type of researcher")
    title = fields.Char(string='Title', help="Academic or professional title")
    affiliation = fields.Char(string='Affiliation', help="Institution or organization")
    specialization = fields.Char(string='Specialization')
    tags = fields.Many2many('scientific.tags', string='Tags')
    image = fields.Binary(string='Image', attachment=True)
    image_size = fields.Integer(string='Image Size (bytes)', compute='_compute_image_size', store=True)
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    city = fields.Char(string='City')
    zip_code = fields.Char(string='Zip Code')
    country = fields.Char(string='Country')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email', tracking=True, help="Valid email address required for account creation")

    comment = fields.Text(string='Comment')
    projects = fields.Many2many('scientific.project', string='Projects')
    tasks = fields.Many2many('scientific.task', string='Tasks')
    experiments = fields.Many2many('scientific.experiment', string='Experiments')
    documents = fields.Many2many('scientific.document', string='Documents')

    # SQL Constraints
    _sql_constraints = [
        ('email_unique', 'UNIQUE(email)', 'Email address must be unique!'),
        ('user_id_unique', 'UNIQUE(user_id)', 'User account already linked to another researcher!'),
    ]

    @api.depends('image')
    def _compute_image_size(self):
        """Compute the size of the uploaded image"""
        for record in self:
            if record.image:
                try:
                    record.image_size = len(base64.b64decode(record.image))
                except Exception:
                    record.image_size = 0
            else:
                record.image_size = 0

    @api.constrains('email')
    def _check_email_valid(self):
        """Validate email format"""
        for record in self:
            if record.email:
                # RFC 5322 simplified email pattern
                pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if not re.match(pattern, record.email):
                    raise ValidationError(f"Invalid email address: {record.email}")

    @api.constrains('image', 'image_size')
    def _check_image_constraints(self):
        """Validate image size and format"""
        MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5MB
        ALLOWED_IMAGE_FORMATS = ['png', 'jpeg', 'jpg', 'gif', 'bmp', 'webp']

        for record in self:
            if record.image:
                # Check size
                if record.image_size > MAX_IMAGE_SIZE:
                    raise ValidationError(
                        f"Image size ({record.image_size / (1024*1024):.2f} MB) "
                        f"exceeds maximum allowed size of {MAX_IMAGE_SIZE / (1024*1024)} MB"
                    )

                # Validate image format
                try:
                    image_data = base64.b64decode(record.image)
                    image_format = imghdr.what(None, h=image_data)
                    if image_format not in ALLOWED_IMAGE_FORMATS:
                        raise ValidationError(
                            f"Invalid image format '{image_format}'. "
                            f"Allowed formats: {', '.join(ALLOWED_IMAGE_FORMATS)}"
                        )
                except Exception as e:
                    if "Invalid image format" in str(e):
                        raise
                    raise ValidationError(f"Failed to validate image: {str(e)}")

    @api.model_create_multi
    def create(self, vals_list):
        """Create researcher with proper error handling for user creation"""
        researchers = super(ScientificResearcher, self).create(vals_list)
        users = self.env['res.users'].sudo()

        for researcher in researchers:
            # Skip user creation if user_id already set
            if researcher.user_id:
                continue

            # Validate email is present
            if not researcher.email:
                raise ValidationError(
                    f"Email address is required for researcher '{researcher.name}' to create user account"
                )

            # Generate unique login based on email
            base_login = researcher.email.lower()
            login = base_login
            counter = 1
            while users.search([('login', '=', login)], limit=1):
                login = f"{base_login}.{counter}"
                counter += 1

            # Generate secure random password
            alphabet = string.ascii_letters + string.digits + string.punctuation
            temp_password = ''.join(secrets.choice(alphabet) for i in range(16))

            try:
                # Determine user group based on researcher type
                group_ref = 'scientific_project.group_scientific_user'
                if researcher.type == 'professor':
                    group_ref = 'scientific_project.group_scientific_manager'

                user_vals = {
                    'name': researcher.name,
                    'login': login,
                    'email': researcher.email,
                    'password': temp_password,
                    'groups_id': [(6, 0, [self.env.ref(group_ref).id])],
                }
                user = users.create(user_vals)
                researcher.write({'user_id': user.id})

                # Send password reset email to new user
                user.with_context(create_user=True).action_reset_password()

            except Exception as e:
                # Clean up researcher if user creation fails
                researcher.unlink()
                raise ValidationError(f"Failed to create user account for '{researcher.name}': {str(e)}")

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
    _order = 'name'

    name = fields.Char(string='Name', required=True, help="Unique tag name")
    researcher_ids = fields.Many2many('scientific.researcher', string='Researchers')
    color = fields.Integer(string='Color Index', default=0)

    # SQL Constraints
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Tag name must be unique!'),
    ]