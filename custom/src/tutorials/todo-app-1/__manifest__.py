{
    "name": "Todo App",
    "summary": "Simple to-do list manager",
    "version": "1.0",
    "category": "Productivity",
    "author": "You",
    "depends": ["base"],
    "data": [
        'security/ir.model.access.csv',
        "views/todo_views.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "sequence": 1,
}
