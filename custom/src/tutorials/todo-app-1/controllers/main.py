from odoo import http
from odoo.http import request, Response
import json

class TodoAPI(http.Controller):

    # ✅ List all tasks
    @http.route('/api/todo/tasks', type='http', auth='user', methods=['GET'], csrf=False)
    def get_tasks(self, **kwargs):
        tasks = request.env['todo.task'].sudo().search([])
        data = [
            {
                "id": t.id,
                "name": t.name,
                "priority": t.priority,
                "is_done": t.is_done,
                "user_id": t.user_id.id if t.user_id else False,
            }
            for t in tasks
        ]
        return Response(json.dumps(data), content_type="application/json", status=200)

    # ✅ Create a task
    @http.route('/api/todo/tasks', type='json', auth='user', methods=['POST'], csrf=False)
    def create_task(self, **kwargs):
        task = request.env['todo.task'].sudo().create({
            "name": kwargs.get("name"),
            "priority": kwargs.get("priority", "0"),
            "user_id": kwargs.get("user_id"),
        })
        return {"id": task.id, "name": task.name}

    # ✅ Update a task
    @http.route('/api/todo/tasks/<int:task_id>', type='json', auth='user', methods=['PUT'], csrf=False)
    def update_task(self, task_id, **kwargs):
        task = request.env['todo.task'].sudo().browse(task_id)
        if not task.exists():
            return {"error": "Task not found"}
        task.write(kwargs)
        return {"success": True, "id": task.id}

    # ✅ Delete a task
    @http.route('/api/todo/tasks/<int:task_id>', type='json', auth='user', methods=['DELETE'], csrf=False)
    def delete_task(self, task_id, **kwargs):
        task = request.env['todo.task'].sudo().browse(task_id)
        if not task.exists():
            return {"error": "Task not found"}
        task.unlink()
        return {"success": True}
    
class AuthAPI(http.Controller):

    @http.route('/api/auth/login', type='json', auth='public', methods=['POST'], csrf=False)
    def login(self, **kwargs):
        login = kwargs.get('login')
        password = kwargs.get('password')
        if not login or not password:
            return {"error": "Missing login or password"}

        uid = request.env['res.users'].sudo()._check_credentials(login, password)
        if not uid:
            return {"error": "Invalid credentials"}

        # Generate API key for the user
        user = request.env['res.users'].sudo().browse(uid)
        token = user._generate_api_key()  # Odoo internal method
        return {"token": token}