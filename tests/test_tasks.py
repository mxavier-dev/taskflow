"""Automated tests for TaskFlow application."""



class TestTaskCreation:
    """Tests for creating tasks."""

    def test_create_valid_task(self, client):
        """Test creating a task with valid data."""
        response = client.post('/tasks/create', data={
            'title': 'Test Task',
            'description': 'Test Description',
            'priority': 'High'
        }, follow_redirects=True)

        assert response.status_code == 200
        assert b'Task created successfully' in response.data
        assert b'Test Task' in response.data

    def test_create_task_without_title_fails(self, client):
        """Test that creating a task without title fails validation."""
        response = client.post('/tasks/create', data={
            'title': '',
            'description': 'Test Description',
            'priority': 'Medium'
        }, follow_redirects=True)

        assert response.status_code == 400
        assert b'Title is required' in response.data

    def test_create_task_with_invalid_priority_fails(self, client):
        """Test that creating a task with invalid priority fails."""
        response = client.post('/tasks/create', data={
            'title': 'Test Task',
            'description': 'Test Description',
            'priority': 'Invalid'
        }, follow_redirects=True)

        assert response.status_code == 400
        assert b'Invalid priority' in response.data

    def test_create_task_default_priority(self, client):
        """Test that priority defaults to Medium when not specified."""
        response = client.post('/tasks/create', data={
            'title': 'Test Task',
            'description': 'Test Description'
        }, follow_redirects=True)

        assert response.status_code == 200
        assert b'Medium' in response.data


class TestTaskListing:
    """Tests for listing tasks."""

    def test_list_tasks_empty(self, client):
        """Test listing tasks when database is empty."""
        response = client.get('/tasks')
        assert response.status_code == 200
        assert b'No tasks found' in response.data

    def test_list_tasks_with_data(self, client, sample_task):
        """Test listing tasks with existing data."""
        response = client.get('/tasks')
        assert response.status_code == 200
        assert b'Test Task' in response.data
        assert b'Test Description' in response.data


class TestTaskViewing:
    """Tests for viewing individual tasks."""

    def test_view_existing_task(self, client, sample_task):
        """Test viewing an existing task."""
        response = client.get(f'/tasks/{sample_task}')
        assert response.status_code == 200
        assert b'Test Task' in response.data
        assert b'Test Description' in response.data

    def test_view_nonexistent_task_returns_404(self, client):
        """Test viewing a non-existent task returns 404."""
        response = client.get('/tasks/99999')
        assert response.status_code == 404


class TestTaskEditing:
    """Tests for editing tasks."""

    def test_edit_valid_task(self, client, sample_task):
        """Test editing a task with valid data."""
        response = client.post(f'/tasks/{sample_task}/edit', data={
            'title': 'Updated Task',
            'description': 'Updated Description',
            'status': 'In Progress',
            'priority': 'High'
        }, follow_redirects=True)

        assert response.status_code == 200
        assert b'Task updated successfully' in response.data
        assert b'Updated Task' in response.data

    def test_edit_task_without_title_fails(self, client, sample_task):
        """Test that editing a task without title fails."""
        response = client.post(f'/tasks/{sample_task}/edit', data={
            'title': '',
            'description': 'Updated Description',
            'status': 'Pending',
            'priority': 'Medium'
        }, follow_redirects=True)

        assert response.status_code == 400
        assert b'Title is required' in response.data

    def test_edit_task_with_invalid_status_fails(self, client, sample_task):
        """Test that editing with invalid status fails."""
        response = client.post(f'/tasks/{sample_task}/edit', data={
            'title': 'Test Task',
            'description': 'Test Description',
            'status': 'Invalid Status',
            'priority': 'Medium'
        }, follow_redirects=True)

        assert response.status_code == 400
        assert b'Invalid status' in response.data

    def test_edit_task_with_invalid_priority_fails(self, client, sample_task):
        """Test that editing with invalid priority fails."""
        response = client.post(f'/tasks/{sample_task}/edit', data={
            'title': 'Test Task',
            'description': 'Test Description',
            'status': 'Pending',
            'priority': 'Invalid'
        }, follow_redirects=True)

        assert response.status_code == 400
        assert b'Invalid priority' in response.data

    def test_edit_nonexistent_task_returns_404(self, client):
        """Test editing a non-existent task returns 404."""
        response = client.post('/tasks/99999/edit', data={
            'title': 'Test',
            'description': 'Test',
            'status': 'Pending',
            'priority': 'Medium'
        })
        assert response.status_code == 404


class TestTaskDeletion:
    """Tests for deleting tasks."""

    def test_delete_existing_task(self, client, sample_task):
        """Test deleting an existing task."""
        response = client.post(f'/tasks/{sample_task}/delete', follow_redirects=True)

        assert response.status_code == 200
        assert b'Task deleted successfully' in response.data

        # Verify task is gone
        response = client.get(f'/tasks/{sample_task}')
        assert response.status_code == 404

    def test_delete_nonexistent_task_returns_404(self, client):
        """Test deleting a non-existent task returns 404."""
        response = client.post('/tasks/99999/delete')
        assert response.status_code == 404


class TestTaskStatusChange:
    """Tests for changing task status."""

    def test_change_status_valid(self, client, sample_task):
        """Test changing task status to valid value."""
        response = client.post(f'/tasks/{sample_task}/status', data={
            'status': 'In Progress'
        }, follow_redirects=True)

        assert response.status_code == 200
        assert b'Status updated successfully' in response.data

    def test_change_status_invalid_fails(self, client, sample_task):
        """Test that changing to invalid status fails."""
        response = client.post(f'/tasks/{sample_task}/status', data={
            'status': 'Invalid'
        }, follow_redirects=True)

        assert response.status_code == 200
        assert b'Invalid status' in response.data

    def test_change_status_nonexistent_task_returns_404(self, client):
        """Test changing status of non-existent task returns 404."""
        response = client.post('/tasks/99999/status', data={
            'status': 'Pending'
        })
        assert response.status_code == 404


class TestPriorityPersistence:
    """Tests for priority field persistence."""

    def test_priority_saved_on_creation(self, client):
        """Test that priority is saved when creating a task."""
        for priority in ['Low', 'Medium', 'High']:
            response = client.post('/tasks/create', data={
                'title': f'Task {priority}',
                'description': 'Description',
                'priority': priority
            }, follow_redirects=True)
            assert response.status_code == 200
            assert priority.encode() in response.data

    def test_priority_saved_on_edit(self, client, sample_task):
        """Test that priority is updated when editing a task."""
        response = client.post(f'/tasks/{sample_task}/edit', data={
            'title': 'Test Task',
            'description': 'Test Description',
            'status': 'Pending',
            'priority': 'High'
        }, follow_redirects=True)

        assert response.status_code == 200
        assert b'High' in response.data

    def test_priority_displayed_in_list(self, client):
        """Test that priority is displayed in task list."""
        client.post('/tasks/create', data={
            'title': 'Priority Test',
            'description': 'Test',
            'priority': 'High'
        }, follow_redirects=True)

        response = client.get('/tasks')
        assert response.status_code == 200
        assert b'High' in response.data


class TestDatabaseOperations:
    """Direct database operation tests."""

    def test_create_and_retrieve_task(self, app):
        """Test creating and retrieving a task directly via database."""
        from src.database import create_task, get_all_tasks, get_task_by_id

        with app.app_context():
            task_id = create_task('Direct DB Task', 'Direct Description', 'Pending', 'Low')
            assert task_id > 0

            task = get_task_by_id(task_id)
            assert task is not None
            assert task['title'] == 'Direct DB Task'
            assert task['priority'] == 'Low'

            tasks = get_all_tasks()
            assert len(tasks) >= 1

    def test_update_task(self, app):
        """Test updating a task directly via database."""
        from src.database import create_task, get_task_by_id, update_task

        with app.app_context():
            task_id = create_task('Original', 'Description', 'Pending', 'Medium')
            result = update_task(task_id, 'Updated', 'New Description', 'Completed', 'High')
            assert result is True

            task = get_task_by_id(task_id)
            assert task['title'] == 'Updated'
            assert task['status'] == 'Completed'
            assert task['priority'] == 'High'

    def test_delete_task(self, app):
        """Test deleting a task directly via database."""
        from src.database import create_task, delete_task, get_task_by_id

        with app.app_context():
            task_id = create_task('To Delete', 'Description', 'Pending', 'Medium')
            result = delete_task(task_id)
            assert result is True

            task = get_task_by_id(task_id)
            assert task is None

    def test_update_status(self, app):
        """Test updating only status."""
        from src.database import create_task, get_task_by_id, update_task_status

        with app.app_context():
            task_id = create_task('Status Test', 'Description', 'Pending', 'Medium')
            result = update_task_status(task_id, 'In Progress')
            assert result is True

            task = get_task_by_id(task_id)
            assert task['status'] == 'In Progress'


class TestValidationFunctions:
    """Tests for validation functions."""

    def test_is_valid_status(self):
        """Test status validation function."""
        from src.database import is_valid_status
        assert is_valid_status('Pending') is True
        assert is_valid_status('In Progress') is True
        assert is_valid_status('Completed') is True
        assert is_valid_status('Invalid') is False
        assert is_valid_status('') is False

    def test_is_valid_priority(self):
        """Test priority validation function."""
        from src.database import is_valid_priority
        assert is_valid_priority('Low') is True
        assert is_valid_priority('Medium') is True
        assert is_valid_priority('High') is True
        assert is_valid_priority('Invalid') is False
        assert is_valid_priority('') is False