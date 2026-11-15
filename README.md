# 🚀 TaskFlow

A lightweight task management web application developed with Python and Flask as part of an academic Software Engineering project. The project focuses on agile development practices, software quality, automated testing, and continuous integration.

## 📌 Overview

TaskFlow is a web-based application that allows users to manage tasks through complete CRUD operations (Create, Read, Update, and Delete).

The application uses SQLite for data persistence and Flask to handle application logic and HTTP requests. Its development follows an agile workflow supported by GitHub Projects, automated testing, and GitHub Actions.

This project was developed for the academic assignment **"Building an Agile Project on GitHub: From Management to Quality Control."**

## ✨ Features

- 📝 **Task creation:** Create tasks with a title, description, and priority.
- 📋 **Task listing:** View all registered tasks, including their current status and priority.
- 🔎 **Task details:** Access complete information about an individual task.
- ✏️ **Task editing:** Update task information, status, and priority.
- 🗑️ **Task deletion:** Remove tasks with confirmation.
- 🔄 **Status management:** Track tasks through three statuses: Pending, In Progress, and Completed.
- 🛡️ **Input validation:** Validate user input on the backend.
- 💾 **Data persistence:** Store task information using SQLite.
- 🎯 **Priority management:** Classify tasks as Low, Medium, or High.

## 🛠️ Technologies

| Component | Technology |
|---|---|
| 🐍 Programming Language | Python 3.11+ |
| ⚙️ Backend Framework | Flask 3.x |
| 🗄️ Database | SQLite |
| 🎨 Frontend | HTML5 and CSS3 |
| 🧪 Automated Testing | Pytest |
| 🔁 Continuous Integration | GitHub Actions |
| 🔍 Code Quality | Ruff |
| 🌐 Version Control | Git and GitHub |

## 📁 Project Structure

```text
taskflow/
├── run.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── database.py
│   └── routes.py
├── templates/
│   ├── base.html
│   ├── tasks.html
│   ├── create_task.html
│   ├── edit_task.html
│   └── view_task.html
├── static/
│   └── css/
│       └── style.css
├── tests/
│   ├── conftest.py
│   └── test_tasks.py
├── docs/
│   ├── PROGRESS.md
│   ├── diagrams/
│   ├── screenshots/
│   └── report/
└── .github/
    └── workflows/
        └── tests.yml
```

## ⚡ Getting Started

### 📋 Prerequisites

Make sure the following tools are installed:

- Python 3.11 or higher
- pip
- Git

### 📥 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mxavier-dev/taskflow.git
   cd taskflow
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:

   **Linux/macOS**
   ```bash
   source .venv/bin/activate
   ```

   **Windows**
   ```powershell
   .venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### ▶️ Running the Application

Start the application with:

```bash
python run.py
```

By default, the application is available at:

```text
http://127.0.0.1:5000
```

The SQLite database is initialized automatically by the application.

## 🧪 Automated Tests

TaskFlow uses **Pytest** to verify application behavior and help prevent regressions.

Run the complete test suite:

```bash
pytest -v
```

To generate a coverage report, install `pytest-cov` if it is not already included in the project dependencies:

```bash
pip install pytest-cov
pytest --cov=src tests/
```

### 📊 Test Coverage

The current test suite contains 25 tests covering the following areas:

| Test Area | Number of Tests |
|---|---:|
| Task Creation | 4 |
| Task Listing | 2 |
| Task Viewing | 2 |
| Task Editing | 5 |
| Task Deletion | 2 |
| Task Status Management | 3 |
| Priority Persistence | 3 |
| Database Operations | 4 |
| **Total** | **25** |

## 🔄 Continuous Integration

The project uses **GitHub Actions** to automate quality checks whenever changes are pushed to the `main` branch or a pull request targets it.

The workflow performs the following steps:

1. 📦 Checks out the repository.
2. 🐍 Sets up the Python environment.
3. 📥 Installs project dependencies.
4. 🧪 Executes automated tests using Pytest.
5. 🔍 Runs Ruff to check code quality.

Workflow execution results are available in the repository's **Actions** tab.

## 📌 Agile Project Management

TaskFlow development is organized using a Kanban board through GitHub Projects.

The board uses three workflow stages:

- 📝 **To Do:** Tasks that have not started.
- 🔄 **In Progress:** Tasks currently being developed.
- ✅ **Done:** Completed tasks.

The board contains at least 10 development cards, providing visibility into project progress, task organization, and scope management.

## 🔀 Scope Change: Task Priority

An additional requirement was introduced during development to simulate a real-world scope change.

**Initial scope:** Tasks included a title, description, and status.

**Change request:** Add a priority attribute to help users identify and organize tasks according to their importance.

**Implementation:**

1. 🗂️ Registered the change as a new Kanban card.
2. 🗄️ Added a `priority` field to the SQLite database.
3. 🎯 Defined the accepted priority levels: `Low`, `Medium`, and `High`.
4. 🛡️ Implemented backend validation for priority values.
5. ✏️ Updated task creation and editing forms.
6. 📋 Added priority information to task listings and detail views.
7. 🧪 Created automated tests to verify priority behavior.
8. 📚 Updated the project documentation.

Existing records are assigned a default priority of `Medium` to maintain compatibility with the database change.

This change demonstrates how requirements can evolve during development and how version control, task tracking, and automated testing help manage those changes.

## 📐 UML Diagrams

The project's UML diagrams are available in `docs/diagrams/`:

- 👤 **Use Case Diagram:** Represents the interactions between the user and the application.
- 🏗️ **Class Diagram:** Represents the main structural elements of the system and their relationships.

These diagrams support the understanding of the system's requirements and structure.

## 📚 Academic Documentation

The theoretical report is available in `docs/report/` and covers:

- Project description and initial scope.
- Agile methodology and project organization.
- The importance of software modeling.
- UML diagrams and their relevance.
- Scope change justification and impact.
- Automated testing and continuous integration.
- Evidence of project management and development activities.

## ⚠️ Limitations

TaskFlow was intentionally designed with a limited scope to meet the academic requirements.

Current limitations include:

- No user authentication or authorization.
- Single-user application.
- No production deployment configuration.
- Minimal frontend, focused on application functionality.
- SQLite as the only supported database.

## 📄 License

This project was developed for academic purposes as part of a Software Engineering assignment.

## 👨‍💻 Author

**Matheus Xavier**

Computer Science Student
