# Recommendation Engine Context

## Why This Change Exists
The recommendation engine is the core AI product capability in StyleSnap. Wardrobe CRUD and Weather Skill only become product value when the system can turn them into explainable outfit decisions grounded in clothes the user already owns.

## Why Recommendation Is Core To StyleSnap
- It connects wardrobe metadata, weather constraints, occasion intent, target style, and user preference into one decision loop.
- It turns static inventory into actionable daily outfit suggestions.
- It is the differentiator that makes the demo feel like an AI product rather than a data-entry tool.

## Why MVP Uses Rules Instead Of Complex Models
- Existing wardrobe and weather data are already structured enough for deterministic heuristics.
- Rule-based scoring is easier to test, explain, and debug during MVP.
- It keeps the recommendation contract stable before any future LLM or ranking-model upgrade.

## Why Explainability Matters
- Users need to understand why a look is suitable for the day, not just see a score.
- Explainable reasoning makes portfolio value clearer because the recommendation logic is inspectable.
- Warning output makes missing wardrobe coverage visible instead of hiding recommendation weaknesses.

## Phase 4 Scope
- Recommendation request and response schemas
- Outfit candidate generation from current wardrobe data
- Rule-based scoring across weather, style, color, occasion, and preference
- Template reasoning and warning generation
- `POST /api/outfits/recommend`
- Minimal frontend integration for triggering the API and previewing results

## Phase 4 Boundary
- No real LLM reasoning
- No real AI vision dependency
- No virtual try-on
- No ecommerce or shopping suggestions
- No user profiling or learned ranking
