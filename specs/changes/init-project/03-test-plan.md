# Init Project Test Plan

## Test Objective
Verify that Phase 0 creates the required governance and spec artifacts without leaking into implementation work.

## Verification Scope
- File existence
- Required section coverage
- Phase boundary compliance

## Checks

### 1. File Existence Checks
- Verify these files exist:
  - `.ai/constitution.md`
  - `.ai/repo-map.md`
  - `specs/changes/init-project/00-context.md`
  - `specs/changes/init-project/01-requirements.md`
  - `specs/changes/init-project/02-architecture.md`
  - `specs/changes/init-project/03-test-plan.md`
  - `specs/changes/init-project/04-tasks.md`
  - `specs/changes/init-project/05-review-checklist.md`
  - `specs/changes/init-project/06-decision-log.md`

### 2. Content Sanity Checks
- `constitution.md` includes:
  - project goal
  - MVP scope
  - non-goals
  - security/privacy principles
  - testing principles
- `repo-map.md` includes:
  - frontend and backend directory intent
  - API surface
  - planned data models
  - safe-to-edit and caution areas
- The `init-project` spec set includes all required sections for context, requirements, architecture, tests, tasks, review, and decisions.

### 3. Boundary Checks
- Confirm no `frontend/` application files were created.
- Confirm no `backend/` application files were created.
- Confirm no package manager or Python runtime dependency files were added in this phase.

## Manual Validation Commands
- `find /Users/wuuu/Documents/StyleSnap/.ai /Users/wuuu/Documents/StyleSnap/specs/changes/init-project -maxdepth 2 -type f | sort`
- `sed -n '1,120p' /Users/wuuu/Documents/StyleSnap/.ai/constitution.md`
- `sed -n '1,160p' /Users/wuuu/Documents/StyleSnap/.ai/repo-map.md`
- `sed -n '1,200p' /Users/wuuu/Documents/StyleSnap/specs/changes/init-project/04-tasks.md`

## Failure Conditions
- Any required file is missing.
- Any spec file is a placeholder with missing sections.
- Any application code or runtime dependency scaffolding appears in Phase 0.

## Exit Criteria
- All required files exist.
- All files contain substantive content aligned to the user brief.
- Phase 0 remains documentation-only.
