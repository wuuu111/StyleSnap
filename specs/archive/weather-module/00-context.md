# Weather Skill Context

## Why This Change Exists
Weather is a decision input for StyleSnap, not the product itself. Users care about whether a look is too warm, too light, too exposed to rain, or missing sun protection. The weather capability therefore needs to behave like an internal skill that provides outfit-aware context rather than like a standalone weather lookup feature.

## Why Weather Matters To StyleSnap
- Temperature affects whether tops, outerwear, and layering should be preferred.
- Rain probability affects shoes, outerwear, and rain suitability rules.
- Wind and UV add practical constraints that later recommendation reasoning can surface.

## How It Supports Phase 4
- Phase 4 recommendation scoring will consume both weather data and outfit-ready weather context.
- Weather data must already be normalized and predictable before scoring logic is added.
- The recommendation page needs a weather context block before outfit results are introduced.

## Phase 3 Scope
- Mock weather skill schemas and APIs
- Replaceable weather service abstraction
- Mock coordinate-to-city resolver
- Frontend location-first weather skill integration
- Compact weather context card on the recommendation page

## Phase 3 Boundary
- No real weather provider
- No API key usage
- No multi-day forecast
- No outfit generation
- No AI explanation logic
