# Weather Skill Decision Log

## Decision 1: Weather Is Not A Primary Product Surface
- Decision:
  - Do not treat weather as a standalone StyleSnap feature.
- Why:
  - The product focus remains personal wardrobe and outfit recommendation quality.
- Alternatives Rejected:
  - Expanding the UX into a weather-first flow.
- Future Extension:
  - Weather remains a hidden-but-explainable input to recommendation scoring.

## Decision 2: Default To Location Before Manual City Input
- Decision:
  - Do not require manual city entry by default. Use browser geolocation first and reveal city input only as fallback.
- Why:
  - It reduces friction and keeps weather contextual rather than user-driven.
- Alternatives Rejected:
  - City input as the default entry point.
- Future Extension:
  - A saved preferred city can be introduced later without changing the skill contract.

## Decision 3: Use Mock Weather In Phase 3
- Decision:
  - Implement only a local mock weather provider.
- Why:
  - Phase 3 is about stable interfaces and recommendation inputs, not external API integration.
- Alternatives Rejected:
  - Integrating a live provider now
- Future Extension:
  - Add real providers behind the same service contract in later phases.

## Decision 4: Default To Geolocation With Mock Resolution
- Decision:
  - Resolve current city from browser coordinates using a mock coordinate resolver.
- Why:
  - It preserves the location-first user flow without adding real geocoding infrastructure.
- Alternatives Rejected:
  - Real reverse geocoding
  - IP-based resolution
- Future Extension:
  - Replace the mock resolver with a real geocoding adapter later.

## Decision 5: Skip Multi-Day Forecasts
- Decision:
  - Return only one current weather snapshot.
- Why:
  - Outfit recommendation needs a simple same-day signal first.
- Alternatives Rejected:
  - Daily forecast arrays
  - Hourly forecast timelines
- Future Extension:
  - Add forecast support only when product requirements need it.

## Decision 6: Weather Skill Must Output Outfit Context
- Decision:
  - Return outfit-aware context alongside raw weather.
- Why:
  - Recommendation logic should consume a higher-level decision input than raw numbers alone.
- Alternatives Rejected:
  - Returning only raw weather fields
- Future Extension:
  - Phase 4 can plug this context directly into scoring and explanation logic.

## Decision 7: Weather Remains A Recommendation Input
- Decision:
  - Keep weather display secondary and compact.
- Why:
  - The product focus stays on clothing and later outfit selection.
- Alternatives Rejected:
  - Expanding the page into a weather dashboard
- Future Extension:
  - Use temperature, rain, UV, and wind as explicit scoring inputs in Phase 4.
