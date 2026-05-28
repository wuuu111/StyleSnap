# Project Skeleton Decision Log

## Decision 1: Create a Dedicated Phase 1 Spec Package
- Decision:
  - Add `specs/changes/project-skeleton/` before writing runtime code.
- Why:
  - The constitution requires every feature to have its own spec package.
- Alternatives Rejected:
  - Reusing `init-project` as the only active spec.
- Future Impact:
  - Later phases should create their own change specs instead of overloading previous ones.

## Decision 2: Keep Backend and Frontend Independently Runnable
- Decision:
  - Backend and frontend are scaffolded as separate apps with their own run commands.
- Why:
  - This matches the monorepo design and keeps feature integration incremental.
- Alternatives Rejected:
  - Single-process or server-rendered bootstrap.
- Future Impact:
  - API contracts become the stable interface between apps.

## Decision 3: Health Endpoint Is the Only Runtime Capability
- Decision:
  - Implement only `/health` in Phase 1.
- Why:
  - It verifies app boot, routing, and test setup without leaking into feature delivery.
- Alternatives Rejected:
  - Adding placeholder business endpoints that would need rewriting later.
- Future Impact:
  - Phase 2 can add wardrobe APIs on top of the verified app shell.

## Decision 4: Keep Generated Runtime Artifacts Out of Versioned Source
- Decision:
  - Add a root `.gitignore` and clean build, cache, environment, and SQLite artifacts from the visible project tree.
- Why:
  - Phase 1 should leave behind source skeleton only, not local machine residue.
- Alternatives Rejected:
  - Treating generated files as part of the scaffold.
- Future Impact:
  - Later phases can verify locally without polluting the repo state.

## Decision 5: Use Configurable Local Defaults for Integration
- Decision:
  - Keep backend database URL, CORS origins, and frontend API base URL environment-configurable with local-safe defaults.
- Why:
  - This preserves clean app boundaries while keeping the skeleton runnable immediately.
- Alternatives Rejected:
  - Hardcoding absolute machine-specific values.
- Future Impact:
  - Phase 2+ can extend the same env contract without route rewrites.
