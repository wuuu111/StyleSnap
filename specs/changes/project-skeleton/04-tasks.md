# Project Skeleton Tasks

## Task 1: Phase 1 Spec Bootstrap

### Scope
Create the `project-skeleton` spec package so implementation remains spec-driven.

### Files
- `specs/changes/project-skeleton/00-context.md`
- `specs/changes/project-skeleton/01-requirements.md`
- `specs/changes/project-skeleton/02-architecture.md`
- `specs/changes/project-skeleton/03-test-plan.md`
- `specs/changes/project-skeleton/04-tasks.md`
- `specs/changes/project-skeleton/05-review-checklist.md`
- `specs/changes/project-skeleton/06-decision-log.md`

### Acceptance Criteria
- The spec package defines scope, architecture, tests, tasks, review, and decisions for Phase 1.

## Task 2: Backend Skeleton

### Scope
Create the backend app shell and its first test.

### Files
- `backend/requirements.txt`
- `backend/pytest.ini`
- `backend/app/main.py`
- `backend/app/database.py`
- `backend/app/routers/health.py`
- `backend/app/schemas/errors.py`
- `backend/app/tests/conftest.py`
- `backend/app/tests/test_health.py`

### Acceptance Criteria
- `pytest` passes
- `GET /health` works
- No business endpoints are added

## Task 3: Frontend Skeleton

### Scope
Create the frontend shell with routing, Tailwind, and placeholder pages.

### Files
- Frontend config files
- `frontend/src/main.tsx`
- `frontend/src/App.tsx`
- `frontend/src/components/*`
- `frontend/src/pages/*`
- `frontend/src/services/apiClient.ts`
- `frontend/src/types/api.ts`
- `frontend/src/utils/classNames.ts`

### Acceptance Criteria
- Frontend installs successfully
- The app can build or run locally
- Placeholder routes and navigation render cleanly

## Task 4: Root Docs and Config

### Scope
Document how to run the monorepo and add local env placeholders.

### Files
- `README.md`
- `.env.example`
- `docker-compose.yml`
- `.ai/repo-map.md`
- `specs/changes/init-project/06-decision-log.md`
- `specs/changes/project-skeleton/06-decision-log.md`

### Acceptance Criteria
- Run commands are documented
- Repo map reflects actual skeleton structure
- Key decisions are recorded
