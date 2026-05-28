# Init Project Architecture

## Architecture Objective
Define the repository contract and execution model that later phases will implement. This phase creates documentation boundaries, not runtime code.

## Documentation Layers
- `.ai/constitution.md`
  - Long-lived rules that apply across all changes.
- `.ai/repo-map.md`
  - Current and planned repository structure plus edit-risk notes.
- `specs/changes/init-project/*`
  - Active spec for project bootstrap and Phase 1 entry criteria.

## Planned Runtime Architecture
- Frontend:
  - React SPA built with Vite and TypeScript
  - Route-driven pages for landing, wardrobe, add/edit item, recommendation input, and result
  - Shared API service layer for backend communication
  - Light global state for wardrobe data and recommendation results
- Backend:
  - FastAPI app with thin routers and service-driven business logic
  - SQLAlchemy models plus Pydantic schemas
  - Replaceable weather and AI services behind explicit interfaces
  - Stable JSON error envelope for API failures
- Data:
  - SQLite for MVP local development
  - Future path to PostgreSQL or Supabase through model and service discipline

## Service Boundaries
- `ai_vision_service`
  - Inputs: uploaded image metadata or file reference
  - Outputs: inferred clothing tags and constraints
  - MVP mode: deterministic mock analyzer
- `clothing_service`
  - Inputs: clothing create/update requests
  - Outputs: validated clothing records and seed setup hooks
- `weather_service`
  - Inputs: city string
  - Outputs: normalized weather snapshot
  - MVP mode: mock provider with adapter seam for real provider later
- `recommendation_service`
  - Inputs: wardrobe items, weather snapshot, occasion, target style, preference text
  - Outputs: ranked outfits with score breakdown, reasoning, and warnings
- `llm_service`
  - Inputs: structured recommendation reasoning payload
  - Outputs: human-readable explanation
  - MVP mode: template renderer

## Data Flow for Main MVP Loop
1. User uploads an item or starts from demo wardrobe data.
2. Frontend calls analyze API to receive mock tags.
3. User confirms or edits tags and saves the clothing item.
4. Wardrobe page fetches and filters saved items.
5. User submits city, occasion, target style, and preference text.
6. Backend fetches mock weather through `weather_service`.
7. Backend builds outfit candidates from wardrobe inventory.
8. Recommendation scoring functions rank candidates.
9. Template explanation logic returns human-readable reasoning and warnings.
10. Frontend renders 2-3 screenshot-friendly recommendation cards.

## State Management Direction
- Keep frontend state minimal and page-oriented.
- Persist authoritative data in backend APIs, not client-only mocks.
- Store recommendation request/result state centrally enough to support moving between input and result pages.

## Extension Points
- Swap SQLite for PostgreSQL/Supabase without changing frontend contracts.
- Replace mock AI analyzer with multimodal model adapter.
- Replace template reasoning with an LLM-backed explainer.
- Replace mock weather with real provider adapters.

## Phase 0 Constraint
This architecture is descriptive only. No frontend, backend, database, or deployment code is created in this phase.
