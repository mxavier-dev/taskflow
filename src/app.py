"""TaskFlow - Main Flask application."""

import os

from flask import Flask

from src.database import add_priority_column, init_db
from src.routes import bp as tasks_bp


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

    # Initialize database
    init_db()
    add_priority_column()

    # Register blueprints
    app.register_blueprint(tasks_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)