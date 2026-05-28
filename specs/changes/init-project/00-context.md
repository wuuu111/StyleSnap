# Init Project Context

## Why This Change Exists
`init-project` establishes the project governance, scope boundaries, and initial implementation plan for `StyleSnap`. The repository currently has no durable project context files, so the first change must define how future phases are designed, implemented, reviewed, and archived.

## User Problem
The product aims to help students and early-career users decide what to wear using clothes they already own. Before code is written, the project needs a stable source of truth so the MVP does not drift into unrelated features such as virtual try-on, community feeds, or ecommerce.

## Product Link
This change belongs to the bootstrap chain that enables every later product feature:

`project governance -> project skeleton -> wardrobe digitization -> weather module -> recommendation engine -> portfolio polish`

## Why Phase 0 Comes First
- The user explicitly requires spec-first development.
- The repo needs durable principles before implementation starts.
- Later phases depend on consistent task size limits, testing rules, and review checkpoints.

## Success Definition
Phase 0 succeeds when the repository contains:
- Project constitution and repo map files under `.ai/`
- A complete `init-project` spec set under `specs/changes/init-project/`
- Clear Phase 1 boundaries without any premature product code

## Out of Scope
- Frontend or backend scaffolding
- Database initialization
- API implementation
- UI design implementation
- Real or mock business logic
