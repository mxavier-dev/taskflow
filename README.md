# TaskFlow

A web-based task management system developed using agile methodologies for an academic Software Engineering project.

## Project Description

TaskFlow is a simple web application for managing tasks with full CRUD operations (Create, Read, Update, Delete). It was built as part of the "Building an Agile Project on GitHub: From Management to Quality Control" academic assignment.

## Academic Objective

This project demonstrates:
- Agile methodology (Kanban) applied to software development
- Software modeling with UML diagrams
- Automated testing with Pytest
- Continuous Integration with GitHub Actions
- Scope change management
- Version control with meaningful commits

## Features

- **Create tasks** with title, description, and priority (Low/Medium/High)
- **List all tasks** with status and priority indicators
- **View task details** with full information
- **Edit tasks** including title, description, status, and priority
- **Delete tasks** with confirmation
- **Change task status** (Pending → In Progress → Completed)
- **Backend validation** for all inputs
- **SQLite persistence** with automatic database initialization
- **Priority field** (added as scope change simulation)

## Technologies

| Layer | Technology |
|-------|------------|
| Language | Python 3.11+ |
| Backend | Flask 3.x |
| Database | SQLite (built-in) |
| Frontend | HTML5 + CSS3 (minimal) |
| Testing | Pytest |
| CI/CD | GitHub Actions |
| Linting | Ruff |
| Version Control | Git + GitHub |

## Project Structure

```
taskflow/
├── run.py                    # Application entry point
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .gitignore               # Git ignore rules
├── src/
│   ├── __init__.py
│   ├── app.py               # Flask application factory
│   ├── database.py          # Database operations
│   └── routes.py            # Route handlers
├── templates/
│   ├── base.html            # Base template
│   ├── tasks.html           # Task list
│   ├── create_task.html     # Create task form
│   ├── edit_task.html       # Edit task form
│   └── view_task.html       # Task detail view
├── static/
│   └── css/
│       └── style.css        # Styling
├── tests/
│   ├── conftest.py          # Pytest fixtures
│   └── test_tasks.py        # Test cases
├── docs/
│   ├── PROGRESS.md          # Progress tracking
│   ├── diagrams/            # UML diagrams
│   ├── screenshots/         # Evidence screenshots
│   └── report/              # Theoretical document
└── .github/
    └── workflows/
        └── tests.yml        # CI workflow
```

## Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/taskflow.git
   cd taskflow
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   # .venv\Scripts\activate   # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python run.py
```

The application will be available at `http://localhost:5000`

## Running Tests

```bash
# Run all tests with verbose output
pytest -v

# Run with coverage (if coverage is installed)
pytest --cov=src tests/
```

## GitHub Actions (CI)

The CI pipeline runs automatically on:
- Push to `main` branch
- Pull requests to `main` branch

The workflow:
1. Checks out the code
2. Sets up Python 3.11
3. Installs dependencies from `requirements.txt`
4. Runs the test suite with Pytest
5. Runs Ruff for code quality checks

View workflow runs in the **Actions** tab on GitHub.

## Kanban Board

The project is managed using GitHub Projects with a Kanban board containing three columns:
- **To Do** - Planned work
- **In Progress** - Currently being worked on
- **Done** - Completed work

The board contains at least 10 cards representing development tasks, including the scope change for priority management.

## Scope Change: Task Priority

**Original scope**: Tasks had only title, description, and status.

**Change request**: Add priority field (Low/Medium/High) to help users identify critical tasks.

**Implementation**:
1. Created Kanban card for the change
2. Added `priority` column to SQLite database with default value "Medium"
3. Updated backend validation to accept only valid priorities
4. Modified forms (create/edit) to include priority dropdown
5. Added priority display in task list and detail views
6. Created tests for priority functionality
7. Updated documentation

This change was implemented as a real scope change with proper tracking and migration (existing tasks get default priority).

## Commits

The repository contains meaningful commits following Conventional Commits format:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation
- `test:` for tests
- `ci:` for CI configuration
- `chore:` for maintenance

## UML Diagrams

Located in `docs/diagrams/`:
- **Use Case Diagram** - Shows user interactions with the system
- **Class Diagram** - Shows the database and service layer structure

## Theoretical Document

The academic report (PDF/DOCX) is in `docs/report/` and covers:
- Project description and initial scope
- Agile methodology applied
- Importance of software modeling
- UML diagrams with explanations
- Scope change justification and impact
- Automated testing explanation
- GitHub evidence (Kanban, commits, Actions)

## Limitations

- No authentication/authorization (academic scope)
- Single-user design
- No deployment configuration
- Minimal frontend (focus on backend/engineering practices)
- SQLite only (no PostgreSQL/MySQL support)

## License

This project is for academic purposes only.

## Author

Matheus Xavier - Software Engineering Student