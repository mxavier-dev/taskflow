"""Database connection and operations for TaskFlow."""

import os
import sqlite3
from contextlib import contextmanager
from typing import Any

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..', 'database', 'taskflow.db')


def get_db_path() -> str:
    """Return the absolute path to the database file."""
    return os.path.abspath(DATABASE_PATH)


@contextmanager
def get_db_connection():
    """Provide a database connection with automatic cleanup."""
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


def init_db() -> None:
    """Initialize the database with the tasks table."""
    os.makedirs(os.path.dirname(get_db_path()), exist_ok=True)

    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'Pending',
                priority TEXT DEFAULT 'Medium',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()


def add_priority_column() -> None:
    """Add priority column to existing tasks table if it doesn't exist."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('ALTER TABLE tasks ADD COLUMN priority TEXT DEFAULT "Medium"')
            conn.commit()
        except sqlite3.OperationalError:
            # Column already exists
            pass


def create_task(title: str, description: str, status: str = 'Pending', priority: str = 'Medium') -> int:
    """Create a new task and return its ID."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO tasks (title, description, status, priority) VALUES (?, ?, ?, ?)',
            (title, description, status, priority)
        )
        conn.commit()
        return cursor.lastrowid


def get_all_tasks() -> list[dict[str, Any]]:
    """Retrieve all tasks ordered by creation date (newest first)."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks ORDER BY created_at DESC')
        return [dict(row) for row in cursor.fetchall()]


def get_task_by_id(task_id: int) -> dict[str, Any] | None:
    """Retrieve a single task by ID."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        row = cursor.fetchone()
        return dict(row) if row else None


def update_task(task_id: int, title: str, description: str, status: str, priority: str) -> bool:
    """Update a task. Returns True if task was found and updated."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE tasks SET title = ?, description = ?, status = ?, priority = ? WHERE id = ?',
            (title, description, status, priority, task_id)
        )
        conn.commit()
        return cursor.rowcount > 0


def delete_task(task_id: int) -> bool:
    """Delete a task. Returns True if task was found and deleted."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        return cursor.rowcount > 0


def update_task_status(task_id: int, status: str) -> bool:
    """Update only the status of a task."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (status, task_id))
        conn.commit()
        return cursor.rowcount > 0