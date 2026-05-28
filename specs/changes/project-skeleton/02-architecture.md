# Project Skeleton Architecture

## Objective
Set up a thin but clean application shell so later phases can add feature logic without restructuring the repo.

## Backend Shape
- `app/main.py`
  - Creates the FastAPI application
  - Registers CORS middleware
  - Includes the health router
  - Creates database tables on startup only for existing model metadata
- `app/database.py`
  - Resolves database URL from environment
  - Exposes SQLAlchemy engine, session factory, base model class, and a table initialization helper
- `app/routers/health.py`
  - Contains only the `/health` endpoint
- `app/schemas/errors.py`
  - Defines the reusable error response contract
- `app/tests/`
  - Uses FastAPI test client against the real app object

## Frontend Shape
- `src/main.tsx`
  - Bootstraps React and router
- `src/App.tsx`
  - Defines route table and shared shell
- `src/components/AppShell.tsx`
  - Shared layout and navigation
- `src/components/PageHeader.tsx`
  - Simple reusable page heading block
- `src/pages/*.tsx`
  - Placeholder route screens with clear next-step messaging
- `src/services/apiClient.ts`
  - Base API helper with environment-based backend URL
- `src/types/api.ts`
  - Shared frontend API primitives

## Data and State
- No feature state yet.
- Frontend remains mostly static except route navigation.
- Backend initializes SQLite infrastructure but stores no product data yet.

## Integration Boundary
- Frontend and backend are independently runnable.
- Health check proves backend bootability.
- API client placeholder proves frontend can be wired to backend later without route refactors.

## Extension Points
- Add routers per domain under `backend/app/routers/`
- Add feature schemas and models without changing app bootstrap
- Replace placeholder frontend pages with feature pages while keeping route identities stable
