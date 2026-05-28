# Weather Skill Test Plan

## Backend Automated Tests
- `GET /api/weather/current` returns weather for valid lat/lon
- Invalid lat/lon returns `INVALID_INPUT`
- `GET /api/weather` returns weather for a known city
- Empty `city` returns `INVALID_INPUT`
- City normalization handles spaces and case differences
- Unknown city returns fallback data
- Outfit context is returned
- High rain probability sets `rain_protection_needed` true
- High UV sets `uv_protection_needed` true
- Cold temperature sets `layering_needed` true
- Response schema shape stays stable
- `GET /health` regression still passes
- Clothes API regression still passes indirectly through full backend test run

## Frontend Manual Tests
- Open recommendation page
- Click `Use my location`
- Allow location and confirm weather card renders
- Deny location and confirm manual city fallback appears
- Enter a city and confirm weather card renders
- Confirm unknown city still renders fallback weather
- Confirm loading and error states render correctly
- Confirm weather card emphasizes outfit impact instead of detailed weather dashboard

## Verification Commands
- `cd backend && .venv/bin/python -m pytest`
- `cd frontend && npm run build`

## Exit Criteria
- Backend tests pass
- Frontend build passes
- Recommendation page can fetch and display weather skill context without outfit results
