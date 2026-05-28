# Project Skeleton Test Plan

## Test Objective
Verify that the project skeleton is runnable, correctly structured, and still bounded away from business logic.

## Automated Tests

### Backend
- Health route test:
  - Verify `GET /health` returns HTTP 200
  - Verify response includes `status`, `service`, and `database` keys
- App bootstrap test is covered implicitly by creating a test client against the real app

## Manual Validation

### Frontend
- Run `npm install`
- Run `npm run dev`
- Confirm landing page loads
- Confirm navigation reaches wardrobe and recommendation pages
- Confirm placeholder content is visible with clear section hierarchy

### Backend
- Run `pytest`
- Run `uvicorn app.main:app --reload`
- Confirm `GET /health` responds with JSON

## Boundary Checks
- No wardrobe CRUD endpoints exist
- No weather endpoints exist
- No outfit recommendation endpoints exist
- No real AI integrations exist

## Exit Criteria
- Backend tests pass
- Frontend dependencies install and the app builds or starts
- Root docs explain local development
