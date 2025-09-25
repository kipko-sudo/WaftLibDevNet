# -*- coding: utf-8 -*-
{
    "name": "HR Employee Documents (Notebook Tab)",
    "summary": "Add a Documents tab on Employees with attachment lines.",
    "version": "16.0.1.0.0",
    "category": "Human Resources/Employees",
    "depends": ["hr", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_employee_documents_views.xml",
    ],
    "application": False,
    "license": "LGPL-3",
}
