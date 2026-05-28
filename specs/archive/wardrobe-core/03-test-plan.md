# Wardrobe Core Test Plan

## Backend Automated Tests
- Create clothing item
- List clothing items
- Get clothing item by id
- Update clothing item
- Delete clothing item
- Invalid category
- Invalid thickness
- Analyze clothing image with mock rules
- Analyze image with unknown keywords fallback
- List with filters for category, color, and season
- Delete non-existent item
- Update non-existent item
- Health check regression

## Frontend Manual Tests
- Open wardrobe page
- Confirm empty or seeded wardrobe state renders correctly
- Add a clothing item manually
- Analyze an image URL with Mock AI
- Edit AI-generated tags before saving
- Filter wardrobe items by category, color, and season
- Edit an existing item
- Delete an existing item
- Confirm error message renders when API returns an error

## Verification Commands
- `cd backend && .venv/bin/python -m pytest`
- `cd frontend && npm run build`

## Exit Criteria
- Backend tests pass
- Frontend builds successfully
- Manual flows for list/add/edit/delete/filter/analyze are implementable through the UI
