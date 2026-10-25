# TaskFlow - Progress Report

## Project Overview
TaskFlow - A web-based task management system for academic Software Engineering project.

---

## Current Stage: Etapa 4 - Testes (Completed)

---

## Requirements Status

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Flask inicia corretamente | ✅ Concluído e verificado | Application runs at http://localhost:5000 |
| SQLite persiste os dados | ✅ Concluído e verificado | Database operations tested and working |
| CRUD completo funciona | ✅ Concluído e verificado | All 25 tests pass |
| Estados são validados | ✅ Concluído e verificado | Backend validation for status/priority |
| Prioridade Low/Medium/High funciona | ✅ Concluído e verificado | Priority field implemented and tested |
| Testes automatizados passam | ✅ Concluído e verificado | 25/25 tests passing |
| GitHub Actions executa os testes | ⏳ Pendente | Workflow file created, needs push to GitHub |
| Kanban tem 10+ cartões e 3 colunas | ⏳ Pendente | Requires GitHub Projects setup |
| 10+ commits reais e significativos | 🔄 Em andamento | Commits will be made |
| Mudança de escopo documentada | ✅ Concluído e verificado | README documents priority change |
| README permite instalar e executar | ✅ Concluído e verificado | Complete README.md created |
| UML corresponde à solução | ⏳ Pendente | Diagrams to be created |
| Documento teórico atende aos tópicos | ⏳ Pendente | PDF/DOCX to be created |
| Capturas são reais e suficientes | ⏳ Pendente | Screenshots to be taken |
| Roteiro do vídeo cabe em 4 min | ⏳ Pendente | Script prepared in README |

---

## Completed Work

### Etapa 1 - Inspeção ✅
- Inspected existing codebase and environment
- Identified existing files: app.py, init_db.py, requirements.txt, templates
- Created comprehensive project plan

### Etapa 2 - Estrutura e Persistência ✅
- Created `src/` directory structure with modular components
- Implemented `src/database.py` with full CRUD operations
- Added database initialization with `created_at` and `priority` columns
- Implemented migration for existing database (added `created_at` column)

### Etapa 3 - CRUD ✅
- Implemented all routes in `src/routes.py`:
  - GET `/tasks` - List all tasks
  - GET `/tasks/<id>` - View single task
  - GET/POST `/tasks/create` - Create task
  - GET/POST `/tasks/<id>/edit` - Edit task
  - POST `/tasks/<id>/delete` - Delete task
  - POST `/tasks/<id>/status` - Change status
- Backend validation for all inputs (title required, valid status, valid priority)
- Proper error handling (404 for non-existent tasks)

### Etapa 4 - Testes ✅
- Configured Pytest with fixtures in `tests/conftest.py`
- Created 25 comprehensive test cases in `tests/test_tasks.py`:
  - Task creation (valid, invalid title, invalid priority, default priority)
  - Task listing (empty, with data)
  - Task viewing (existing, non-existent 404)
  - Task editing (valid, invalid title, invalid status, invalid priority, 404)
  - Task deletion (existing, non-existent 404)
  - Status changes (valid, invalid, 404)
  - Priority persistence (creation, edit, display)
  - Direct database operations
- All 25 tests passing
- Linting with Ruff: clean (0 issues)

---

## Files Created/Modified

### New Files
- `src/__init__.py` - Package initialization
- `src/database.py` - Database operations (CRUD, connection management)
- `src/routes.py` - Flask route handlers with validation
- `src/app.py` - Flask application factory
- `run.py` - Application entry point
- `templates/base.html` - Base template with navigation
- `templates/tasks.html` - Task list view
- `templates/create_task.html` - Create task form (updated)
- `templates/edit_task.html` - Edit task form
- `templates/view_task.html` - Task detail view
- `static/css/style.css` - Minimal styling
- `tests/conftest.py` - Pytest fixtures
- `tests/test_tasks.py` - 25 test cases
- `.github/workflows/tests.yml` - GitHub Actions CI workflow
- `docs/PROGRESS.md` - This file

### Modified Files
- `README.md` - Complete documentation
- `requirements.txt` - Verified dependencies
- `database/taskflow.db` - Migrated schema (added `created_at`, `priority`)

---

## Technical Decisions

1. **Modular structure**: Separated database, routes, and app factory for maintainability
2. **Blueprint pattern**: Used Flask Blueprint for route organization
3. **Context managers**: Database connections use context managers for safety
4. **Parameterized queries**: All SQL uses `?` placeholders to prevent injection
5. **Backend validation**: All validation done server-side, not relying on HTML5
6. **Test isolation**: Each test uses a temporary database via fixtures
7. **Conventional commits**: Will follow `feat:`, `fix:`, `docs:`, `test:`, `ci:`, `chore:` prefixes

---

## Scope Change: Priority Field

**Implemented as simulated scope change:**
- Added `priority` column to database (Low/Medium/High, default: Medium)
- Updated create/edit forms with priority dropdown
- Added priority display in list and detail views
- Backend validation for valid priorities
- Tests covering priority functionality
- Documented in README.md with justification

---

## Blockers / Pending External Actions

1. **GitHub Repository**: Need to push to GitHub and configure:
   - Public repository
   - GitHub Projects (Kanban board with 10+ cards, 3 columns)
   - GitHub Actions (verify workflow runs)
2. **UML Diagrams**: Create Use Case and Class diagrams in `docs/diagrams/`
3. **Theoretical Document**: Produce PDF/DOCX in `docs/report/`
4. **Screenshots**: Capture Kanban, commits, Actions, running app
5. **Video Pitch**: Record 4-minute presentation

---

## Next Actions

1. Initialize Git repository (if not already) and commit all changes
2. Push to GitHub
3. Configure GitHub Projects Kanban board
4. Verify GitHub Actions workflow execution
5. Create UML diagrams
6. Write theoretical document
7. Take screenshots for evidence
8. Prepare video recording environment

---

## Test Results Summary

```
============================= test session starts ==============================
platform linux -- Python 3.10.12, pytest-9.2.0, pluggy-1.7.0
rootdir: /media/matheus/Kingston/Programação/taskflow
collected 25 items

tests/test_tasks.py::TestTaskCreation::test_create_valid_task PASSED
tests/test_tasks.py::TestTaskCreation::test_create_task_without_title_fails PASSED
tests/test_tasks.py::TestTaskCreation::test_create_task_with_invalid_priority_fails PASSED
tests/test_tasks.py::TestTaskCreation::test_create_task_default_priority PASSED
tests/test_tasks.py::TestTaskListing::test_list_tasks_empty PASSED
tests/test_tasks.py::TestTaskListing::test_list_tasks_with_data PASSED
tests/test_tasks.py::TestTaskViewing::test_view_existing_task PASSED
tests/test_tasks.py::TestTaskViewing::test_view_nonexistent_task_returns_404 PASSED
tests/test_tasks.py::TestTaskEditing::test_edit_valid_task PASSED
tests/test_tasks.py::TestTaskEditing::test_edit_task_without_title_fails PASSED
tests/test_tasks.py::TestTaskEditing::test_edit_task_with_invalid_status_fails PASSED
tests/test_tasks.py::TestTaskEditing::test_edit_task_with_invalid_priority_fails PASSED
tests/test_tasks.py::TestTaskEditing::test_edit_nonexistent_task_returns_404 PASSED
tests/test_tasks.py::TestTaskDeletion::test_delete_existing_task PASSED
tests/test_tasks.py::TestTaskDeletion::test_delete_nonexistent_task_returns_404 PASSED
tests/test_tasks.py::TestTaskStatusChange::test_change_status_valid PASSED
tests/test_tasks.py::TestTaskStatusChange::test_change_status_invalid_fails PASSED
tests/test_tasks.py::TestTaskStatusChange::test_change_status_nonexistent_task_returns_404 PASSED
tests/test_tasks.py::TestPriorityPersistence::test_priority_saved_on_creation PASSED
tests/test_tasks.py::TestPriorityPersistence::test_priority_saved_on_edit PASSED
tests/test_tasks.py::TestPriorityPersistence::test_priority_displayed_in_list PASSED
tests/test_tasks.py::TestDatabaseOperations::test_create_and_retrieve_task PASSED
tests/test_tasks.py::TestDatabaseOperations::test_update_task PASSED
tests/test_tasks.py::TestDatabaseOperations::test_delete_task PASSED
tests/test_tasks.py::TestDatabaseOperations::test_update_status PASSED

============================== 25 passed in 0.45s ==============================
```

---

*Last updated: 2026-11-14*