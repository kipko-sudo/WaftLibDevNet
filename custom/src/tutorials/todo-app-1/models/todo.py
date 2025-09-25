from odoo import models, fields

class Todo(models.Model):
    _name = "todo.task"
    _description = "To-Do Task"

    name = fields.Char("Task", required=True)
    is_done = fields.Boolean("Done?")
    active = fields.Boolean("Active", default=True)
    due_date = fields.Date("Due Date")
    priority = fields.Selection(
        [
            ("0", "Low"),
            ("1", "Normal"),
            ("2", "High"),
        ],
        string="Priority",
        default="1",
    )
    user_id = fields.Many2one("res.users", string="Assigned To")