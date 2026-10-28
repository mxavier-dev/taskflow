"""Flask routes for TaskFlow application."""

from flask import Blueprint, abort, flash, redirect, render_template, request, url_for

from src.database import (
    VALID_PRIORITIES,
    VALID_STATUSES,
    create_task,
    delete_task,
    get_all_tasks,
    get_task_by_id,
    is_valid_priority,
    is_valid_status,
    update_task,
    update_task_status,
)

bp = Blueprint('tasks', __name__)


@bp.route('/')
def index():
    """Home page - redirect to tasks list."""
    return redirect(url_for('tasks.list_tasks'))


@bp.route('/tasks')
def list_tasks():
    """Display all tasks."""
    tasks = get_all_tasks()
    return render_template('tasks.html', tasks=tasks)


@bp.route('/tasks/create', methods=['GET', 'POST'])
def create_task_route():
    """Create a new task."""
    if request.method == 'GET':
        return render_template('create_task.html', priorities=VALID_PRIORITIES)

    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    priority = request.form.get('priority', 'Medium')

    # Backend validation
    if not title:
        flash('Title is required.', 'error')
        return render_template('create_task.html', priorities=VALID_PRIORITIES), 400

    if not is_valid_priority(priority):
        flash('Invalid priority.', 'error')
        return render_template('create_task.html', priorities=VALID_PRIORITIES), 400

    create_task(title, description, 'Pending', priority)
    flash('Task created successfully!', 'success')
    return redirect(url_for('tasks.list_tasks'))


@bp.route('/tasks/<int:task_id>')
def view_task(task_id: int):
    """View a single task."""
    task = get_task_by_id(task_id)
    if task is None:
        abort(404, description="Task not found")
    return render_template('view_task.html', task=task)


@bp.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id: int):
    """Edit an existing task."""
    task = get_task_by_id(task_id)
    if task is None:
        abort(404, description="Task not found")

    if request.method == 'GET':
        return render_template('edit_task.html', task=task, statuses=VALID_STATUSES, priorities=VALID_PRIORITIES)

    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    status = request.form.get('status', 'Pending')
    priority = request.form.get('priority', 'Medium')

    # Backend validation
    if not title:
        flash('Title is required.', 'error')
        return render_template('edit_task.html', task=task, statuses=VALID_STATUSES, priorities=VALID_PRIORITIES), 400

    if not is_valid_status(status):
        flash('Invalid status.', 'error')
        return render_template('edit_task.html', task=task, statuses=VALID_STATUSES, priorities=VALID_PRIORITIES), 400

    if not is_valid_priority(priority):
        flash('Invalid priority.', 'error')
        return render_template('edit_task.html', task=task, statuses=VALID_STATUSES, priorities=VALID_PRIORITIES), 400

    if update_task(task_id, title, description, status, priority):
        flash('Task updated successfully!', 'success')
    else:
        flash('Failed to update task.', 'error')

    return redirect(url_for('tasks.list_tasks'))


@bp.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task_route(task_id: int):
    """Delete a task."""
    task = get_task_by_id(task_id)
    if task is None:
        abort(404, description="Task not found")

    if delete_task(task_id):
        flash('Task deleted successfully!', 'success')
    else:
        flash('Failed to delete task.', 'error')

    return redirect(url_for('tasks.list_tasks'))


@bp.route('/tasks/<int:task_id>/status', methods=['POST'])
def change_status(task_id: int):
    """Change task status."""
    task = get_task_by_id(task_id)
    if task is None:
        abort(404, description="Task not found")

    status = request.form.get('status', 'Pending')
    if not is_valid_status(status):
        flash('Invalid status.', 'error')
        return redirect(url_for('tasks.list_tasks'))

    if update_task_status(task_id, status):
        flash('Status updated successfully!', 'success')
    else:
        flash('Failed to update status.', 'error')

    return redirect(url_for('tasks.list_tasks'))