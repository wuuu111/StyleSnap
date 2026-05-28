# Project Skeleton Context

## Why This Change Exists
`project-skeleton` turns the Phase 0 governance into runnable project structure. The goal is not product capability yet, but a clean, verifiable foundation that can accept later wardrobe, weather, and recommendation features without rework.

## User Problem
Without a stable frontend and backend skeleton, later phases would mix infrastructure work with product behavior, which increases risk, breaks task boundaries, and makes testing unreliable.

## Product Link
This change is the first runnable phase in the StyleSnap delivery chain:

`project governance -> project skeleton -> wardrobe core -> weather module -> recommendation engine -> frontend recommendation flow -> portfolio polish`

## Phase 1 Scope
- Backend FastAPI app bootstrap
- SQLite connection bootstrap
- Health check route and test
- Frontend React/Vite/Tailwind/Router bootstrap
- Placeholder pages and shared navigation
- Root development docs and config placeholders

## Out of Scope
- Clothing CRUD
- Weather API implementation
- Recommendation engine
- AI analysis logic
- Final UI polish
