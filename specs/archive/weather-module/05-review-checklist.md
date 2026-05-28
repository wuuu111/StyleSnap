# Weather Skill Review Checklist

## Spec Conformance
- Does the frontend prefer location before manual city input?
- Does the API return both weather and outfit context?
- Does unknown city fallback still return stable fields and context?
- Is weather kept as a supporting skill rather than the main experience?

## Architecture
- Are schema, router, and service boundaries clear?
- Is the weather provider replaceable?
- Is frontend weather fetch logic centralized?
- Is the response shape suitable for Phase 4 scoring inputs?
- Is outfit context separated cleanly from raw weather data?

## Security and Regression
- Are there no real API keys?
- Are there no third-party network requests?
- Are city and location inputs validated?
- Does health check still work?
- Does wardrobe functionality remain unaffected?
- Is error formatting still unified?
