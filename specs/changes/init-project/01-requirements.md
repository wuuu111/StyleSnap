# Init Project Requirements

## Feature Goal
Create the durable governance and planning artifacts required to build `StyleSnap` through controlled phases.

## User Stories
- As the project owner, I want a written constitution so future implementation follows the same MVP, privacy, and testing rules.
- As a future coding agent, I want a repo map so I know where code belongs and which areas are high risk.
- As the implementation lead, I want a complete spec package for `init-project` so Phase 1 can start from a stable baseline.

## Inputs
- The user-provided product brief for `StyleSnap`
- The mandated phase breakdown from Phase 0 to Phase 6
- The required monorepo structure and technology stack
- The required engineering workflow: spec, tasks, tests, review, archive

## Outputs
- `.ai/constitution.md`
- `.ai/repo-map.md`
- `specs/changes/init-project/00-context.md`
- `specs/changes/init-project/01-requirements.md`
- `specs/changes/init-project/02-architecture.md`
- `specs/changes/init-project/03-test-plan.md`
- `specs/changes/init-project/04-tasks.md`
- `specs/changes/init-project/05-review-checklist.md`
- `specs/changes/init-project/06-decision-log.md`
- A Phase 0 summary message

## Functional Requirements
1. The constitution must define project goal, MVP scope, prohibited work, technical constraints, security/privacy rules, testing rules, code style expectations, and AI integration rules.
2. The repo map must document the intended monorepo structure, service boundaries, API routes, data models, testing layout, safe edit areas, and caution areas.
3. The `init-project` spec set must explain context, requirements, architecture, tests, task decomposition, review checklist, and decisions for Phase 0 and the upcoming skeleton work.
4. The task spec must preserve the user's task granularity limits:
   - maximum 8 file changes per task
   - maximum 600 diff lines per task
   - no single task spanning frontend, backend, database, and deployment at once
5. No application code or dependency setup may be introduced in this change.

## Edge Cases
- Because `.ai/constitution.md` and `.ai/repo-map.md` do not exist yet, Phase 0 must bootstrap from the user's product brief.
- The repo is allowed to be mostly empty; requirements still need to define the intended structure.
- Some future paths may not exist yet; the repo map should mark them as planned, not implemented.

## Error Handling Requirements
- If future implementation conflicts with the constitution or feature spec, record the conflict in a decision log before choosing a minimal viable path.
- If a required workflow artifact is missing in a later phase, that phase must stop and create it before coding continues.

## Non-Goals
- Finalizing exact frontend state management choice between Zustand and Context in Phase 0
- Selecting a real AI or weather provider
- Defining production deployment topology
- Writing archive snapshots under `specs/current/` or `specs/archive/` before a phase is complete
