"""Pytest configuration and fixtures for TaskFlow tests."""

import os
import sys
import tempfile

import pytest

# Add project root to path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'src'))


@pytest.fixture
def test_db_path():
    """Create a temporary database file for testing."""
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as f:
        db_path = f.name
    yield db_path
    # Cleanup
    if os.path.exists(db_path):
        os.unlink(db_path)


@pytest.fixture
def app(test_db_path):
    """Create a Flask app configured for testing."""
    # Override database path for testing
    import src.database as db_module
    from src.app import create_app
    from src.database import add_priority_column, init_db
    original_path = db_module.DATABASE_PATH
    db_module.DATABASE_PATH = test_db_path

    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    with app.app_context():
        init_db()
        add_priority_column()

    yield app

    # Restore original path
    db_module.DATABASE_PATH = original_path


@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()


@pytest.fixture
def sample_task(app):
    """Create a sample task in the database."""
    from src.database import create_task
    with app.app_context():
        task_id = create_task('Test Task', 'Test Description', 'Pending', 'Medium')
        return task_id