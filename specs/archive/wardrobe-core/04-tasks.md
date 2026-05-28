# Wardrobe Core Tasks

## Task 1: Backend Model and Schema
- Add `ClothingItem` SQLAlchemy model
- Add validated Pydantic schemas for clothes and analyze payloads
- Preserve stable error response shape

## Task 2: Clothes CRUD API
- Add clothes router under `/api/clothes`
- Implement create, list, get by id, update, and delete
- Add list filters for category, color, and season

## Task 3: Mock AI Analyze Service
- Implement keyword-based analyze logic
- Add fallback metadata for unknown inputs
- Expose `POST /api/clothes/analyze`

## Task 4: Backend Tests
- Add CRUD, analyze, validation, filter, and regression tests
- Verify each new test fails before implementation and passes after

## Task 5: Frontend Wardrobe Page
- Replace placeholder wardrobe screen with real list view
- Add loading, empty, error, and filter UI
- Add clothing item card component

## Task 6: Add Item Flow
- Add route and page for clothing creation
- Add analyze action and editable form fields
- Save item and return to wardrobe page

## Task 7: Edit/Delete/Filter UI
- Add edit route and page
- Add delete action
- Wire list filters to API client

## Task 8: Demo Seed Data and README Update
- Add demo seed bootstrap
- Update README and repo map
- Document Mock AI and demo wardrobe behavior

## Task 9: Review and Archive
- Run phase verification commands
- Update `specs/current/`
- Archive `wardrobe-core`
- Add `lessons-learned.md`
