from odoo import fields, models

class Task(models.Model):
    _name = 'task.tracker'
    _description = 'Task Tracker'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')