# Weather Module Decision Log

## Decision 1: Use Mock Weather In Phase 3
- Decision:
  - Implement only a local mock weather provider.
- Why:
  - Phase 3 is about stable interfaces and recommendation inputs, not external API integration.
- Alternatives Rejected:
  - Integrating a live provider now
- Future Extension:
  - Add real providers behind the same service contract in later phases.

## Decision 2: Skip Multi-Day Forecasts
- Decision:
  - Return only one current weather snapshot.
- Why:
  - Outfit recommendation needs a simple same-day signal first.
- Alternatives Rejected:
  - Daily forecast arrays
  - Hourly forecast timelines
- Future Extension:
  - Add forecast support only when product requirements need it.

## Decision 3: Skip Geolocation
- Decision:
  - Require explicit city input instead of device location.
- Why:
  - It avoids permissions, browser complexity, and hidden behavior during MVP.
- Alternatives Rejected:
  - Browser geolocation
  - IP-based inference
- Future Extension:
  - Add optional location detection later if it materially improves the user flow.

## Decision 4: Weather Remains A Recommendation Input
- Decision:
  - Keep weather display secondary and compact.
- Why:
  - The product focus stays on clothing and later outfit selection.
- Alternatives Rejected:
  - Expanding the page into a weather dashboard
- Future Extension:
  - Use temperature, rain, UV, and wind as explicit scoring inputs in Phase 4.
