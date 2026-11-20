# 🚀 TaskFlow

A lightweight task management web application built with Python and Flask for an academic Software Engineering project. The project demonstrates CRUD development, agile project organization, automated testing, and continuous integration.

## 📌 Overview

TaskFlow allows users to create, view, update, and delete tasks. Each task has a title, an optional description, a status, a priority, and a creation timestamp.

The application uses Flask for its web layer and SQLite for persistence. The project is managed with Git and GitHub, with a Kanban board in GitHub Projects and automated quality checks through GitHub Actions.

**Academic assignment:** *Building an Agile Project on GitHub: From Management to Quality Control.*

## ✨ Features

- 📝 Create tasks with a title, description, and priority.
- 📋 List all tasks, including status and priority.
- 🔎 View an individual task and its details.
- ✏️ Edit task information, status, and priority.
- 🗑️ Delete tasks with a confirmation prompt.
- 🔄 Track task status: `Pending`, `In Progress`, and `Completed`.
- 🎯 Set task priority: `Low`, `Medium`, or `High`.
- 🛡️ Validate required fields and allowed status/priority values on the backend.
- 💾 Persist task data in SQLite.
- 🔧 Migrate legacy status values and add the priority column to existing databases.

## 🛠️ Technologies

| Component | Technology |
|---|---|
| Programming Language | Python 3.11+ |
| Web Framework | Flask 3.1 |
| Database | SQLite |
| Frontend | HTML5, CSS3, Jinja |
| Automated Tests | Pytest |
| Continuous Integration | GitHub Actions |
| Linting | Ruff |
| Version Control | Git and GitHub |

## 📁 Project Structure

```text
taskflow/
├── .github/
│   └── workflows/
│       └── tests.yml
├── docs/
│   ├── PROGRESS.md
│   └── diagrams/
│       ├── class.puml
│       └── use_case.puml
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── database.py
│   └── routes.py
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── base.html
│   ├── create_task.html
│   ├── edit_task.html
│   ├── tasks.html
│   └── view_task.html
├── tests/
│   ├── conftest.py
│   └── test_tasks.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

The SQLite database file is created automatically under `database/taskflow.db` when the application initializes. The directory/database file is generated at runtime and is not part of the tracked source tree.

## ⚡ Getting Started

### Prerequisites

- Python 3.11 or higher
- pip
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mxavier-dev/taskflow.git
   cd taskflow
   ```

2. Create and activate a virtual environment:

   **Linux/macOS**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   **Windows PowerShell**
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

### Run the application

From the repository root, run:

```bash
python -m src.app
```

Then open http://127.0.0.1:5000 in your browser.

The application initializes the SQLite database when the Flask app is created. The built-in development server is intended for local academic use, not production deployment.

## 🧪 Automated Tests

Run the test suite from the repository root:

```bash
pytest -v
```

The current test file contains **27 test functions**. The tests cover:

| Test Area | Tests |
|---|---:|
| Task creation | 4 |
| Task listing | 2 |
| Task viewing | 2 |
| Task editing | 5 |
| Task deletion | 2 |
| Status management | 3 |
| Priority persistence and display | 3 |
| Database operations | 4 |
| Validation functions | 2 |
| **Total** | **27** |

These are test cases present in the repository. Test execution results should be checked in the local test run or the corresponding GitHub Actions run.

## 🔄 Continuous Integration

The workflow at `.github/workflows/tests.yml` is configured to run on pushes to `main` and pull requests targeting `main`.

It performs the following steps:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs dependencies from `requirements.txt`.
4. Runs `pytest -v`.
5. Installs Ruff and runs `ruff check .`.

The latest workflow run visible during the repository review (November 15, 2026) completed successfully. Check the repository's Actions tab for the status of newer runs.

## 📌 Agile Project Management

Project activities are tracked through GitHub Issues and a GitHub Projects Kanban board.

The board has three workflow columns:

- **To Do:** work that has not started.
- **In Progress:** work currently being performed.
- **Done:** completed work.

The board screenshot reviewed during the latest audit showed 12 cards, all in **Done**. The board therefore contains more than the required 10 cards, but the screenshot does not demonstrate work distributed across the three stages. Cards should reflect the actual state of work rather than being moved only to populate columns.

The repository had 12 commits and 13 Issues at the time of this review. The project board and issue history provide traceability for planning and development activities.

## 🔀 Scope Change: Task Priority

The initial task model focused on title, description, and status. During development, task priority was added as a scope change to make it possible to distinguish tasks by importance.

The implemented priority values are:

- `Low`
- `Medium`
- `High`

The change is implemented across the database, backend validation, task creation/editing forms, task list, and task detail view. New tasks default to `Medium`, and the database initialization routine adds the priority column to existing databases when necessary.

The change is tracked in [Issue #13](https://github.com/mxavier-dev/taskflow/issues/13). **Note:** at the time of this review, the Issue was closed but had no description. Add the change rationale and acceptance criteria to the Issue so it serves as complete project-management evidence.

## 📐 UML Diagrams

PlantUML source files are stored in `docs/diagrams/`:

- `use_case.puml` — user interactions with the application.
- `class.puml` — intended structural representation.

**Documentation limitation:** the class diagram currently models `FlaskApp`, `Database`, `Routes`, and templates as classes. The implementation uses a Flask application factory, Python modules/functions, a Blueprint, and Jinja templates. The class diagram must be revised to accurately represent the implemented architecture before it is used as final academic evidence.

The diagrams are currently available as PlantUML source; rendered image exports should be added if required by the report.

## 📚 Academic Deliverables

The repository currently contains the PlantUML source diagrams and this progress report. The following deliverables were not present in the repository during the latest review and remain to be completed:

- Theoretical report in PDF or DOCX.
- Screenshots of the Kanban board, commit history, successful Actions run, and running application.
- Final video presentation (up to four minutes).

## ⚠️ Limitations

- No user authentication or authorization.
- Designed as a small, single-user academic application.
- No production deployment configuration.
- Minimal frontend focused on core functionality.
- SQLite is the only supported database.
- The Flask development server and fallback development secret key are not suitable for production.

## 📄 License

This project is distributed under the [MIT License](LICENSE).

## 👨‍💻 Author

**Matheus Xavier**
Computer Science Student
