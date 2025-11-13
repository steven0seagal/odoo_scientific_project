from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Project(models.Model):
    _name = 'scientific.project'
    _description = 'Scientific Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'start_date desc, name'

    name = fields.Char(string='Name', required=True, tracking=True,
                       help="Unique project identifier")
    start_date = fields.Date(string='Start Date', tracking=True, required=True,
                              help="Project start date")
    end_date = fields.Date(string='End Date', tracking=True,
                           help="Expected project completion date")
    description = fields.Text(string='Description', tracking=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True, required=True)
    document_id = fields.Many2many('scientific.document', string='Document', tracking=True)
    funding = fields.Many2many('scientific.funding', string='Funding')
    principal_investigator_id = fields.Many2one('scientific.researcher', string='Principal Investigator',
                                                 tracking=True, required=True,
                                                 help="Lead researcher responsible for the project")
    collaborators_ids = fields.Many2many('scientific.researcher', string='Collaborators', tracking=True)
    notes = fields.Text(string='Notes')

    # SQL Constraints
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Project name must be unique!'),
    ]

    @api.constrains('start_date', 'end_date')
    def _check_date_range(self):
        """Validate that end date is not before start date"""
        for record in self:
            if record.start_date and record.end_date:
                if record.end_date < record.start_date:
                    raise ValidationError(
                        "End date cannot be earlier than start date.\n"
                        f"Start: {record.start_date}\n"
                        f"End: {record.end_date}"
                    )
    def action_draft(self):
        self.status = 'draft'

    def action_in_progress(self):
        self.status = 'in_progress'

    def action_done(self):
        self.status = 'done'

    def action_cancelled(self):
        self.status = 'cancelled'





