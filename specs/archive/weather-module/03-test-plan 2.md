# Weather Module Test Plan

## Backend Automated Tests
- `GET /api/weather` returns weather for a known city
- Empty `city` returns `INVALID_INPUT`
- City normalization handles spaces and case differences
- Unknown city returns fallback data
- Response schema shape stays stable
- `GET /health` regression still passes
- Clothes API regression still passes indirectly through full backend test run

## Frontend Manual Tests
- Open recommendation page
- Enter a city
- Click `Check Weather`
- Confirm weather card renders
- Confirm unknown city still renders fallback weather
- Confirm loading state renders during request
- Confirm error state renders for empty input

## Verification Commands
- `cd backend && .venv/bin/python -m pytest`
- `cd frontend && npm run build`

## Exit Criteria
- Backend tests pass
- Frontend build passes
- Recommendation page can fetch and display weather data without outfit results
