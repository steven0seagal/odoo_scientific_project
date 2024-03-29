from odoo import models, fields,api

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
        researchers = super(ScientificResearcher, self).create(vals_list)
        users = self.env['res.users']

        for researcher in researchers:
            user_vals = {
                'name': researcher.name,
                'login': researcher.name,
                'email': researcher.email,
                # Add other user fields as needed
            }
            user = users.create(user_vals)
            researcher.write({'user_id': user.id})

        return researchers
class ScientificResearcherTags(models.Model):

    _name = 'scientific.tags'
    _description = 'Researcher Tags'

    name = fields.Char(string='Name', required=True)
    researcher_ids = fields.Many2many('scientific.researcher', string='Researchers')
    color = fields.Integer(string='Color Index')