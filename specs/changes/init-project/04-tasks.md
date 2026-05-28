# Init Project Tasks

## Task 1: Create Durable Governance Files

### Scope
Create the two long-lived project context files under `.ai/`.

### Files
- `.ai/constitution.md`
- `.ai/repo-map.md`

### Acceptance Criteria
- The constitution defines project scope, tech constraints, privacy/security, testing, and AI integration principles.
- The repo map describes intended structure, service boundaries, API routes, data models, and edit-risk guidance.
- No application code is introduced.

## Task 2: Create Init-Project Spec Context and Requirements

### Scope
Create the context and requirements docs for the bootstrap phase.

### Files
- `specs/changes/init-project/00-context.md`
- `specs/changes/init-project/01-requirements.md`

### Acceptance Criteria
- The context doc explains why this phase exists and what it enables.
- The requirements doc defines outputs, constraints, edge cases, and non-goals.
- The docs align with the user-provided StyleSnap brief.

## Task 3: Create Init-Project Architecture and Test Plan

### Scope
Describe the intended system architecture and the verification approach for Phase 0.

### Files
- `specs/changes/init-project/02-architecture.md`
- `specs/changes/init-project/03-test-plan.md`

### Acceptance Criteria
- The architecture doc defines frontend, backend, service, and data boundaries without writing code.
- The test plan defines file checks, content checks, and phase-boundary checks.

## Task 4: Create Task Breakdown, Review Checklist, and Decision Log

### Scope
Capture controlled execution rules for future phases.

### Files
- `specs/changes/init-project/04-tasks.md`
- `specs/changes/init-project/05-review-checklist.md`
- `specs/changes/init-project/06-decision-log.md`

### Acceptance Criteria
- Task breakdown respects the user's maximum file-change and diff-size limits.
- Review checklist covers spec conformance, architecture, and security/regression review.
- Decision log records bootstrap decisions and known future follow-ups.

## Task 5: Verify Phase 0 and Publish Summary

### Scope
Confirm the file set exists and summarize the boundary of the phase.

### Files
- No file edits required unless verification reveals a gap.

### Acceptance Criteria
- Required files exist.
- The phase remains documentation-only.
- A Phase 0 summary is produced with created files, main decisions, MVP boundary, and next phase.

## Phase 1 Entry Conditions
- `.ai/constitution.md` and `.ai/repo-map.md` are present.
- `specs/changes/init-project/*` is complete.
- Phase 1 starts by re-reading these files and producing an Implementation Plan before scaffold work.
