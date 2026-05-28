# Frontend Recommendation Flow Test Plan

## Frontend Verification
- `cd frontend && npm run build`

## Backend Regression Verification
- `cd backend && .venv/bin/python -m pytest`

## Manual Acceptance
- Recommendation page loads correctly
- `Use my location` button is visible in the initial state
- Successful geolocation shows weather context
- Denied or failed geolocation reveals city fallback
- City fallback fetch renders weather context
- Occasion, target style, and preference inputs render correctly
- Clicking `Generate Outfits` renders recommendation results
- 2-3 outfit cards are shown when results exist
- Each card shows:
  - outfit items
  - score
  - score breakdown
  - reasoning
  - warnings
- Regenerate action triggers another recommendation request
- Weather loading state is clear
- Recommendation loading state is clear
- Recommendation error state is clear
- Insufficient wardrobe state links users to wardrobe
- Wardrobe page still works
- Landing page recommendation link still works

## Optional Testing Scope
- If no existing frontend test framework is present, do not add one just for Phase 5.

## Exit Criteria
- Frontend build passes
- Backend regression suite passes
- Recommendation page feels presentable for screenshots and recording
