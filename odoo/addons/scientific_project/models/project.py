from odoo import models, fields

class Project(models.Model):
    _name = 'scientific.project'
    _description = 'Scientific Project'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    description = fields.Text(string='Description')
    tasks = fields.One2many('scientific.task', 'project_id', string='Tasks')

