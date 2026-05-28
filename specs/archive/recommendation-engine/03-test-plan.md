# Recommendation Engine Test Plan

## Backend Automated Tests
- Recommend outfit success with city weather source
- Recommend outfit success with location weather source
- Return 2-3 outfits when enough clothes exist
- Score breakdown contains all score dimensions
- `weather_fit_score` works for warm, cool/cold, and rainy cases
- `style_match_score` works for direct and adjacent style matches
- `color_harmony_score` works for neutral/high-harmony combinations
- `occasion_fit_score` works for commuting/class/casual signals
- `user_preference_score` works for:
  - empty preference
  - `不想太正式`
  - `想显高`
  - `想保暖`
  - `舒服`
- Empty wardrobe handling
- Missing mandatory wardrobe categories handling
- Rainy weather warning generation
- Cold weather warning generation
- Health regression
- Clothes CRUD regression through full backend test run
- Weather Skill regression through full backend test run

## Frontend Manual Tests
- Open recommendation page
- Load weather context by location or city fallback
- Select occasion
- Select target style
- Enter optional preference text
- Click `Generate Outfits`
- Confirm basic recommendation preview renders
- Confirm API error state renders when wardrobe is insufficient
- Confirm wardrobe and weather flows remain usable

## Verification Commands
- `cd backend && .venv/bin/python -m pytest`
- `cd frontend && npm run build`

## Exit Criteria
- Backend tests pass with recommendation and regression coverage
- Frontend build passes
- Recommendation page can call the new API and render a minimal result preview
