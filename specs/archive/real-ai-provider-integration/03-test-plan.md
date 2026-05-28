# Real AI Provider Integration Test Plan

## Backend Tests
- mock stylist provider returns stable structure
- deepseek stylist selection falls back when no API key
- deepseek stylist provider falls back on timeout
- deepseek stylist provider falls back on invalid JSON
- recommendation API works with `STYLIST_PROVIDER=mock`
- recommendation API works with `STYLIST_PROVIDER=deepseek` and no key
- recommendation API returns `ai_metadata`
- recommendation API keeps stable `recommended_outfits` shape
- valid AI reorder reorders the top looks
- invalid AI reorder preserves original ordering
- mock vision provider still returns expected tags
- clothes analyze API still works through provider abstraction
- incomplete non-mock vision config falls back to mock
- invalid image reference handling remains stable

## Regression Verification
- `cd backend && .venv/bin/python -m pytest`
- `cd frontend && npm run build`

## Manual Acceptance
- recommendation flow still works unchanged in the frontend
- Add Item analyze still works unchanged in the frontend
- no API key or raw image payload is exposed in docs or code

## Exit Criteria
- backend tests pass
- frontend build passes
- fallback behavior is verified
- provider metadata is stable and additive
