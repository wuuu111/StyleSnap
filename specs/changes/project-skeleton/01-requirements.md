# Project Skeleton Requirements

## Feature Goal
Create the minimum runnable monorepo skeleton for StyleSnap so both frontend and backend can start independently and expose a clean base for future features.

## User Stories
- As a developer, I want the backend to boot with a health endpoint so I can verify server wiring quickly.
- As a developer, I want a frontend shell with routing and placeholder pages so later features have stable entry points.
- As the project owner, I want root documentation and config placeholders so the repo is understandable and runnable without guesswork.

## Inputs
- Phase 0 governance files
- `init-project` architecture and workflow constraints
- User-specified Phase 1 deliverables

## Outputs
- Backend FastAPI skeleton with SQLite connection setup, CORS, error schema placeholder, pytest config, and health test
- Frontend Vite/React/TypeScript/Tailwind/Router skeleton with navigation and placeholder pages
- Root `README.md`, `.env.example`, and `docker-compose.yml`
- Updated `.ai/repo-map.md`
- Updated `specs/changes/init-project/06-decision-log.md`

## Functional Requirements
1. Backend must expose `GET /health` returning a stable JSON payload.
2. Backend must include SQLite configuration through a dedicated database module.
3. Backend must define a stable error envelope schema placeholder matching the documented API error shape.
4. Backend test setup must support running `pytest` locally.
5. Frontend must include React Router with routes for landing, wardrobe, and recommendation placeholder pages.
6. Frontend must include TailwindCSS wiring and a minimal screenshot-friendly layout.
7. Frontend must include a base API client placeholder that reads a configurable API base URL.
8. Root README must document project overview, stack, run commands, test commands, and current phase status.
9. No business endpoints, wardrobe CRUD, recommendation logic, weather logic, or real AI integrations may be implemented.

## Edge Cases
- Backend should start even if the SQLite file does not exist yet.
- Frontend placeholder pages should render even if the backend is not running.
- API base URL must default safely for local development and remain environment-configurable.

## Error Handling Requirements
- Health endpoint must remain simple and deterministic.
- Error envelope structure must be documented and coded as a reusable schema placeholder.
- CORS must be permissive enough for local frontend-backend development but not described as production-safe default.

## Non-Goals
- Database migrations
- Production Docker hardening
- Real environment secret setup
- Frontend stateful feature logic
