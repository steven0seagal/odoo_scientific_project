# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError, AccessError
import re
import secrets
import string


class ResearcherInvitationWizard(models.TransientModel):
    """Wizard for inviting new researchers to join the system.

    This wizard allows administrators and managers to send invitations
    to potential researchers, automatically creating user accounts and
    sending welcome emails with login credentials.

    Access Control:
        - Admin (base.group_system): Can invite to all roles
        - Manager (group_scientific_manager): Can invite to all roles
        - Others: No access
    """
    _name = 'researcher.invitation.wizard'
    _description = 'Researcher Invitation Wizard'

    name = fields.Char(
        string='Full Name',
        required=True,
        help="Full name of the researcher being invited"
    )
    email = fields.Char(
        string='Email',
        required=True,
        help="Valid email address for sending the invitation"
    )
    type = fields.Selection([
        ('manager', 'Scientific Project Manager'),
        ('pi', 'Principal Investigator'),
        ('researcher', 'Scientific Project User'),
        ('technician', 'Lab Technician'),
        ('viewer', 'Scientific Project Viewer')
    ],
        string='Role',
        required=True,
        default='researcher',
        help="Role to assign to the invited researcher"
    )
    title = fields.Char(
        string='Title',
        help="Academic or professional title (e.g., Dr., Prof., MSc.)"
    )
    affiliation = fields.Char(
        string='Affiliation',
        help="Institution or organization"
    )
    specialization = fields.Char(
        string='Specialization',
        help="Field of specialization or research area"
    )
    message = fields.Text(
        string='Personal Message',
        help="Optional personal message to include in the invitation email"
    )

    @api.constrains('email')
    def _check_email_valid(self):
        """Validate email format using RFC 5322 pattern"""
        for wizard in self:
            if wizard.email:
                # RFC 5322 simplified email pattern
                pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if not re.match(pattern, wizard.email):
                    raise ValidationError(f"Invalid email address: {wizard.email}")

    @api.constrains('type')
    def _check_role_permission(self):
        """Check if user has permission to invite to specific roles.

        Only admins and managers can send invitations to all roles.
        """
        for wizard in self:
            user = self.env.user

            # Check if user is admin or manager
            is_admin = user.has_group('base.group_system')
            is_manager = user.has_group('scientific_project.group_scientific_manager')

            if not (is_admin or is_manager):
                raise AccessError(
                    "Only administrators and managers can send researcher invitations."
                )

    def action_send_invitation(self):
        """Send invitation and create researcher account.

        This method:
        1. Validates the invitation data
        2. Creates a new researcher record
        3. Creates a user account with appropriate role
        4. Sends an invitation email with login credentials

        Returns:
            dict: Action to close the wizard or show success message
        """
        self.ensure_one()

        # Check permissions
        user = self.env.user
        is_admin = user.has_group('base.group_system')
        is_manager = user.has_group('scientific_project.group_scientific_manager')

        if not (is_admin or is_manager):
            raise AccessError(
                "You do not have permission to send invitations. "
                "Only administrators and managers can invite researchers."
            )

        # Check if email already exists
        existing_researcher = self.env['scientific.researcher'].sudo().search([
            ('email', '=', self.email)
        ], limit=1)

        if existing_researcher:
            raise ValidationError(
                f"A researcher with email {self.email} already exists in the system.\n"
                f"Researcher: {existing_researcher.name}"
            )

        # Check if user with this email already exists
        existing_user = self.env['res.users'].sudo().search([
            ('login', '=', self.email.lower())
        ], limit=1)

        if existing_user:
            raise ValidationError(
                f"A user account with email {self.email} already exists.\n"
                f"User: {existing_user.name}"
            )

        try:
            # Prepare researcher values
            researcher_vals = {
                'name': self.name,
                'email': self.email,
                'type': self.type,
                'title': self.title,
                'affiliation': self.affiliation,
                'specialization': self.specialization,
            }

            # Create researcher record (this will auto-create user via create method)
            researcher = self.env['scientific.researcher'].sudo().create(researcher_vals)

            # Get the created user
            if not researcher.user_id:
                raise ValidationError("Failed to create user account for the researcher.")

            # Send custom invitation email if personal message provided
            if self.message:
                self._send_custom_invitation_email(researcher)

            # Return success notification
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Invitation Sent!',
                    'message': f'Invitation sent to {self.name} ({self.email}). '
                              f'A user account has been created and password reset email has been sent.',
                    'type': 'success',
                    'sticky': False,
                }
            }

        except ValidationError:
            raise
        except Exception as e:
            raise ValidationError(
                f"Failed to send invitation: {str(e)}\n\n"
                "Please check the information and try again."
            )

    def _send_custom_invitation_email(self, researcher):
        """Send a custom invitation email with personal message.

        Args:
            researcher: The researcher record that was created
        """
        if not researcher.user_id:
            return

        # Get email template with sudo to ensure access
        template = self.env.ref('scientific_project.email_template_researcher_invitation',
                               raise_if_not_found=False)

        if template:
            # Prepare context with custom message
            ctx = {
                'researcher_name': researcher.name,
                'inviter_name': self.env.user.name,
                'personal_message': self.message,
                'role': dict(self._fields['type'].selection).get(self.type),
                'login_url': self.env['ir.config_parameter'].sudo().get_param('web.base.url'),
            }

            # Send email with sudo to ensure proper access rights
            template.sudo().with_context(ctx).send_mail(
                researcher.id,
                force_send=True,
                email_values={'email_to': researcher.email}
            )

    def action_cancel(self):
        """Cancel the invitation wizard"""
        return {'type': 'ir.actions.act_window_close'}
