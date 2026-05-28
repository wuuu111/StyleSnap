# Init Project Decision Log

## Decision 1: Bootstrap Phase 0 from the User Brief
- Decision:
  - Use the user-provided StyleSnap project brief as the initial source of truth because no local governance files existed yet.
- Why:
  - Phase 0 exists specifically to convert that brief into durable repository artifacts.
- Alternatives Rejected:
  - Waiting for existing repo docs that do not exist.
  - Scaffolding code first and documenting later.
- Future Impact:
  - Phase 1 and later phases must treat the newly created `.ai/*` and active spec files as the baseline context.

## Decision 2: Keep Phase 0 Documentation-Only
- Decision:
  - Do not create frontend, backend, database, or deployment code in this phase.
- Why:
  - The user explicitly required spec-first execution and a hard stop after governance and spec setup.
- Alternatives Rejected:
  - Creating placeholder project folders with starter code.
  - Adding package manifests early for convenience.
- Future Impact:
  - Phase 1 owns all runtime scaffolding and must begin with a fresh Implementation Plan.

## Decision 3: Define Replaceable Service Boundaries Early
- Decision:
  - Document `ai_vision_service`, `llm_service`, `weather_service`, `clothing_service`, and `recommendation_service` in Phase 0.
- Why:
  - The MVP must use mocks now but stay replaceable later.
- Alternatives Rejected:
  - Embedding mock logic directly inside routers or components.
  - Deferring service boundary decisions until after scaffolding.
- Future Impact:
  - Phase 1 and later phases should preserve thin routers and explicit adapters.

## Decision 4: Preserve Narrow MVP Scope
- Decision:
  - Exclude virtual try-on, community, ecommerce, auth complexity, and real-provider dependencies from the initial delivery target.
- Why:
  - The demo's value is the complete recommendation loop, not breadth.
- Alternatives Rejected:
  - Designing for speculative features before validating the main flow.
- Future Impact:
  - Any future expansion beyond the MVP must go through a new change spec and decision log entry.

## Known Technical Debt
- Exact frontend state management choice remains open between Zustand and React Context.
- Exact local file upload storage path is intentionally deferred to Phase 1 or Phase 2.
- Exact production deployment path remains deferred until the app flow exists.

## Phase 1 Follow-Up Note
- Outcome:
  - Phase 1 created a dedicated `project-skeleton` change spec instead of reusing `init-project`.
- Why it matters:
  - This preserves the spec-per-feature workflow defined in the constitution and keeps future archive boundaries clean.
