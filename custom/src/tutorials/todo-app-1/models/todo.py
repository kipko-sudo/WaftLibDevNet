from odoo import models, fields, api
from datetime import date

class Todo(models.Model):
    _name = "todo.task"
    _description = "To-Do Task"

    name = fields.Char("Task", required=True)
    is_done = fields.Boolean("Done?")
    active = fields.Boolean("Active", default=True)
    due_date = fields.Date("Due Date")
    priority = fields.Selection([
        ("0", "Low"),
        ("1", "Normal"),
        ("2", "High"),
    ], string="Priority", default="1")
    user_id = fields.Many2one("res.users", string="Assigned To")
    stage = fields.Selection([
        ("new", "New"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ], string="Stage", default="new")

    is_overdue = fields.Boolean(
        "Overdue",
        compute="_compute_is_overdue",
        store=True
    )
    subtask_ids = fields.One2many("todo.subtask", "task_id", string="Subtasks")

    done_subtask_count = fields.Integer(
        string="Completed Subtasks",
        compute="_compute_done_subtask_count",
        store=False
    )

    total_subtask_count = fields.Integer(
        string="Total Subtasks",
        compute="_compute_total_subtask_count",
        store=False
    )

    @api.depends("subtask_ids.is_done")
    def _compute_done_subtask_count(self):
        for task in self:
            task.done_subtask_count = sum(1 for s in task.subtask_ids if s.is_done)

    @api.depends("subtask_ids")
    def _compute_total_subtask_count(self):
        for task in self:
            task.total_subtask_count = len(task.subtask_ids)

    @api.depends('due_date', 'is_done')
    def _compute_is_overdue(self):
        today = date.today()
        for task in self:
            task.is_overdue = bool(task.due_date and task.due_date < today and not task.is_done)

class TodoSubtask(models.Model):
    _name = "todo.subtask"
    _description = "Subtask for a To-Do task"

    name = fields.Char("Subtask", required=True)
    is_done = fields.Boolean("Done?")
    task_id = fields.Many2one("todo.task", string="Parent Task", ondelete="cascade")
