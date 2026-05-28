# Project Skeleton Review Checklist

## Spec Conformance Review
- Does the backend contain only skeleton work and not feature logic?
- Does the frontend contain only placeholder pages and shared shell work?
- Are run commands and test commands documented?
- Is the Phase 1 output aligned with the declared scope?

## Architecture Review
- Are routers thin and isolated?
- Is database setup separated from app bootstrap?
- Is frontend route structure clear enough for future feature expansion?
- Is the API client isolated from page components?

## Security and Regression Review
- Are API URLs and database URLs configurable instead of hardcoded secrets?
- Is CORS described as local-development-friendly rather than production-open?
- Did Phase 1 avoid introducing product data flows or privacy leaks?
- Are placeholder docs unlikely to mislead future phases?
