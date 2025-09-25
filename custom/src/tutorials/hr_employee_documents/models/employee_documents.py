# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    # Main O2M for the document tab
    document_ids = fields.One2many(
        "hr.employee.document.line",
        "employee_id",
        string="Documents",
    )


class HrEmployeeDocumentLine(models.Model):
    _name = "hr.employee.document.line"
    _description = "Employee Document Line"
    _rec_name = "doc_name"

    employee_id = fields.Many2one(
        "hr.employee",
        string="Employee",
        required=True,
        readonly=True,
        ondelete="cascade",
        index=True,
    )
    doc_name = fields.Char(string="Name")
    attachment_ids = fields.Many2many(
        "ir.attachment",
        "hr_employee_line_attachment_rel",
        "line_id",
        "attachment_id",
        string="Document",
        help="Attach one or more files to this line.",
    )

    @api.model
    def create(self, vals):
        """
        Re-bind attachments after create so files uploaded on an unsaved line
        get a proper (res_model, res_id) and are readable by other users.
        """
        rec = super().create(vals)
        if rec.attachment_ids:
            rec.attachment_ids.write({
                "res_model": self._name,
                "res_id": rec.id,
            })
        return rec
