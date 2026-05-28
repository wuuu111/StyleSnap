# Weather Module Context

## Why This Change Exists
Weather is a decision input for StyleSnap, not the product itself. Users care about whether a look is too warm, too light, too exposed to rain, or missing sun protection. A lightweight weather module gives the later recommendation engine the context it needs to make those decisions.

## Why Weather Matters To StyleSnap
- Temperature affects whether tops, outerwear, and layering should be preferred.
- Rain probability affects shoes, outerwear, and rain suitability rules.
- Wind and UV add practical constraints that later recommendation reasoning can surface.

## How It Supports Phase 4
- Phase 4 recommendation scoring will consume stable weather data directly.
- Weather data must already be normalized and predictable before scoring logic is added.
- The frontend recommendation page needs a weather context block before outfit results are introduced.

## Phase 3 Scope
- Mock weather response schema and API
- Replaceable weather service abstraction
- Frontend weather API client
- Weather card UI on the recommendation page

## Phase 3 Boundary
- No real weather provider
- No API key usage
- No multi-day forecast
- No outfit generation
- No AI explanation logic
