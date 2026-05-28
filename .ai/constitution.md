# StyleSnap Project Constitution

## Project Goal
- Build a portfolio-ready web demo named `StyleSnap`.
- Deliver an AI outfit assistant that turns a personal wardrobe into daily outfit recommendations.
- Prioritize the end-to-end MVP loop: wardrobe digitization, metadata extraction, weather-aware recommendation, explainable scoring, and presentable UI.

## MVP Scope
- Single-user local demo experience.
- Wardrobe upload, mock AI clothing analysis, clothing CRUD, demo seed data.
- Mock weather retrieval with replaceable provider interface.
- Rule-based outfit recommendation with 2-3 explainable results.
- Mobile-first frontend pages for landing, wardrobe, add/edit item, recommendation input, and recommendation result.
- Backend APIs for clothes, weather, and outfit recommendation.

## Non-Goals
- Virtual try-on.
- Social or community features.
- Ecommerce, payments, or affiliate links.
- Multi-user auth or permissions.
- Deep learning recommendation systems.
- Hard dependency on external AI or weather vendors for MVP.

## Technical Constraints
- Monorepo layout rooted at `stylesnap/`.
- Frontend: React, Vite, TypeScript, TailwindCSS, React Router, Zustand or React Context.
- Backend: FastAPI, Python 3.11+, Pydantic, SQLAlchemy 2, SQLite in local development.
- Keep adapters replaceable for future PostgreSQL/Supabase, real weather APIs, and real AI services.
- Do not introduce large new dependencies without a clear need recorded in spec and decision log.

## Product and UX Principles
- Mobile-first and screenshot-friendly.
- Card-based layout with clear information hierarchy.
- Weather informs recommendation but must not dominate the experience.
- Use realistic demo data so the main product loop is runnable without uploads or API keys.

## Security and Privacy Principles
- Treat clothing images and wardrobe metadata as user-private data.
- Never hardcode API keys or secrets.
- Do not log full uploaded file paths or user preference text unnecessarily.
- Validate category, style, occasion, and file upload constraints.
- Keep CORS narrow and environment-aware.
- MVP must not send wardrobe data to third-party AI services by default.

## Testing and Acceptance Principles
- Spec is the source of truth for implementation.
- Each feature must have a `03-test-plan.md` before code changes begin.
- Tests or manual acceptance steps are required before marking a task complete.
- If tests fail, stop and fix before starting the next task.
- Each task must end with changed files, test result, and remaining risks.

## Delivery Workflow
- Every feature lives under `specs/changes/<feature-name>/`.
- Before coding, read `.ai/constitution.md`, `.ai/repo-map.md`, and the relevant spec set, then write an `Implementation Plan`.
- Task size limits:
  - No more than 8 file changes per task.
  - No more than 600 lines of diff per task.
  - Do not mix frontend, backend, database, and deployment concerns in one task.
- Update relevant spec files after each meaningful implementation step.
- Perform Spec Conformance Review, Architecture Review, and Security/Regression Review at the end of each phase.

## Code Style Principles
- Prefer small, focused files and explicit service boundaries.
- Avoid unrelated refactors during feature delivery.
- Use stable error shapes for API responses.
- Use comments sparingly and only where logic is non-obvious.
- Preserve replaceable interfaces for AI and weather integrations.

## AI and Recommendation Principles
- MVP AI behavior is mock or template-based, but service interfaces must be production-replaceable.
- Clothing recognition must allow manual correction by the user.
- Recommendation scoring must be explainable and deterministic.
- LLM-style reasoning in MVP should come from templates, not opaque model calls.

## Documentation Principles
- README must explain product value, target users, user flow, AI capability design, recommendation logic, privacy notes, and roadmap.
- Each phase must leave behind decision logs, review notes, and lessons learned.
