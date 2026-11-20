# TaskFlow — Project Progress

**Last reviewed:** 2026-11-20
**Repository:** https://github.com/mxavier-dev/taskflow
**Default branch:** `main`

## 1. Project Overview

TaskFlow is a web-based task management application developed with Python, Flask, and SQLite for the Software Engineering assignment **“Building an Agile Project on GitHub: From Management to Quality Control.”**

The application provides CRUD operations for tasks, status management, backend validation, and task priority.

## 2. Repository Audit Snapshot

The following information was checked against the public repository on November 20, 2026:

| Item | Observed state | Evidence / Notes |
|---|---|---|
| Repository visibility | ✅ Public | GitHub repository metadata |
| Default branch | ✅ `main` | Repository metadata |
| Commits | ✅ 12 | Commit history |
| Issues | ✅ 13 | Includes Issue #13 for task priority |
| GitHub Projects | ⚠️ Partially verified | User-provided screenshot showed 12 cards, all in Done |
| Kanban columns | ⚠️ Present in screenshot | To Do, In Progress, Done; no cards shown in the first two columns |
| Automated test functions | ✅ 27 in source | Counted `def test_*` in `tests/test_tasks.py` |
| Latest observed Actions run | ✅ Success | Run from 2026-11-15, commit `17a1268` |
| UML source files | ⚠️ Present, need review | `class.puml` and `use_case.puml` |
| Academic report | ⏳ Not found | No report file/directory in current repository tree |
| Evidence screenshots | ⏳ Not found | No screenshots directory/files in current repository tree |
| Presentation video | ⏳ Pending | Must be recorded and shared separately |

**Audit limitation:** the GitHub connector can inspect repository files, Issues, commits, and Actions, but it cannot inspect the GitHub Projects board directly. The Kanban assessment above is based on the screenshot supplied by the project owner.

## 3. Application Implementation

### Completed features

- [x] Flask application factory in `src/app.py`.
- [x] SQLite connection management and database initialization.
- [x] Task creation.
- [x] Task listing.
- [x] Individual task details.
- [x] Task editing.
- [x] Task deletion.
- [x] Status management: `Pending`, `In Progress`, `Completed`.
- [x] Priority management: `Low`, `Medium`, `High`.
- [x] Backend validation for title, status, and priority.
- [x] Default priority of `Medium`.
- [x] Database migration to add the priority column to existing databases.
- [x] Migration of legacy Portuguese status values to English.
- [x] Parameterized SQL queries.
- [x] Pytest fixtures using an isolated test database.

### Application entry point

Run the application from the repository root with:

```bash
python -m src.app
```

The previous README referenced `python run.py`, but no `run.py` file exists in the current repository tree. The README has been corrected to use the available entry point.

## 4. Automated Testing and CI

### Test inventory

The current `tests/test_tasks.py` file contains 27 test functions:

| Test area | Count |
|---|---:|
| Task creation | 4 |
| Task listing | 2 |
| Task viewing | 2 |
| Task editing | 5 |
| Task deletion | 2 |
| Status management | 3 |
| Priority persistence/display | 3 |
| Database operations | 4 |
| Validation functions | 2 |
| **Total** | **27** |

Run locally with:

```bash
pytest -v
```

### GitHub Actions

- [x] Workflow file exists: `.github/workflows/tests.yml`.
- [x] Triggered on pushes to `main`.
- [x] Triggered on pull requests targeting `main`.
- [x] Sets up Python 3.11.
- [x] Installs `requirements.txt`.
- [x] Runs Pytest.
- [x] Installs Ruff and runs `ruff check .`.
- [x] Latest observed run (November 15, 2026) completed with conclusion `success`.

The successful run predates the current documentation update. A new run should be checked after these documentation changes are pushed.

## 5. Scope Change — Task Priority

The initial scope covered task title, description, and status. Priority was introduced during development as a simulated scope change.

Implemented behavior:

- [x] Added the `priority` field to the SQLite task model.
- [x] Added the values `Low`, `Medium`, and `High`.
- [x] Set `Medium` as the default priority.
- [x] Added backend validation.
- [x] Added priority selection to task creation and editing forms.
- [x] Displayed priority in the task list and detail view.
- [x] Added automated tests for priority behavior.

Tracking:

- [x] Issue #13 exists: [adicionar prioridade às tarefas (Low, Medium e High)](https://github.com/mxavier-dev/taskflow/issues/13).
- [ ] Add a description explaining the reason for the change.
- [ ] Add acceptance criteria to Issue #13.
- [ ] Confirm that Issue #13 is represented in the GitHub Projects board.

**Audit note:** Issue #13 was closed, but its body was empty during the review. The code implements the feature, but the Issue itself needs descriptive content to provide adequate evidence of scope management.

## 6. Agile Project Management

- [x] GitHub Projects board created.
- [x] Three columns were visible in the supplied screenshot: To Do, In Progress, and Done.
- [x] At least 10 cards: 12 were visible in the screenshot.
- [ ] Review the distribution of cards based on the actual state of each task.
- [ ] Confirm Issue #13 is linked to the project board.

The screenshot showed all 12 cards in Done. This is not automatically incorrect if every represented activity is complete, but the board does not show work moving through the three stages. Do not move cards artificially just to fill columns.

## 7. UML and Modeling

Files present:

- [x] `docs/diagrams/use_case.puml`
- [x] `docs/diagrams/class.puml`

Pending review:

- [ ] Revise the class diagram to match the actual architecture.
- [ ] Check consistency between the use case diagram and implemented features.
- [ ] Render the PlantUML files as PNG or SVG for inclusion in the academic report.

**Identified mismatch:** the class diagram represents FlaskApp, Database, Routes, and templates as classes. In the code, the application is organized around modules/functions, a Flask application factory, a Blueprint, and Jinja templates. The current class diagram should not be treated as final until corrected.

## 8. Academic Deliverables

| Deliverable | Status |
|---|---|
| Public GitHub repository | ✅ Complete |
| Application with CRUD | ✅ Implemented |
| Scope change implemented | ✅ Implemented |
| GitHub Issues and commits | ✅ Present |
| GitHub Projects board with 10+ cards | ⚠️ Screenshot confirms 12; all in Done |
| GitHub Actions workflow | ✅ Configured; latest observed run succeeded |
| Automated tests | ✅ 27 test functions in source |
| Use case diagram | ⚠️ Source exists; review/render pending |
| Class diagram | ⚠️ Source exists; revision/render pending |
| Theoretical report (PDF/DOCX) | ⏳ Pending |
| Evidence screenshots | ⏳ Pending |
| Video pitch (up to 4 minutes) | ⏳ Pending |

## 9. Next Actions — Recommended Order

1. **Complete Issue #13:** add the change rationale and acceptance criteria; verify its association with the project board.
2. **Correct the class diagram:** represent the real Flask modules, application factory, Blueprint/routes, database operations, and templates accurately.
3. **Render both UML diagrams:** export PNG or SVG versions for the report.
4. **Capture evidence:** Kanban board, commit history, Issues, successful Actions run, and application screens.
5. **Write the theoretical report:** project scope, agile method, modeling, UML, scope change, testing/CI, results, and evidence.
6. **Record the video pitch:** up to four minutes, demonstrating the application and explaining the workflow and scope change.
7. **Run tests and CI again:** confirm the final repository state after all changes are committed.

## 10. Audit and Documentation Notes

- The previous README stated 25 tests; the source contains 27 test functions. The count has been corrected.
- The previous progress file contained obsolete statements that GitHub Actions, the Kanban board, and UML files were still pending. Those statements have been replaced with the observed state.
- The previous README instructed users to run `python run.py`; the current repository does not contain that file. The command has been corrected to `python -m src.app`.
- The README and this progress report describe repository state as observed on November 20, 2026. Recheck the GitHub Actions status and project board after subsequent changes.
