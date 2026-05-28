# Weather Module Review Checklist

## Spec Conformance
- Does the API require `city`?
- Does the frontend show a real weather card?
- Does unknown city fallback still return stable fields?
- Is weather kept as a supporting module rather than the main experience?

## Architecture
- Are schema, router, and service boundaries clear?
- Is the weather provider replaceable?
- Is frontend weather fetch logic centralized?
- Is the response shape suitable for Phase 4 scoring inputs?

## Security and Regression
- Are there no real API keys?
- Are there no third-party network requests?
- Is city input validated?
- Does health check still work?
- Does wardrobe functionality remain unaffected?
- Is error formatting still unified?
