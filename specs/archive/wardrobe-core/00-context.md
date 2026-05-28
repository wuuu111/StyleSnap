# Wardrobe Core Context

## Why This Change Exists
The wardrobe is the data foundation of StyleSnap. Without a structured personal wardrobe, the app cannot produce outfit recommendations grounded in clothes the user actually owns.

## Why Wardrobe Is Core to StyleSnap
- It converts a vague styling problem into a usable inventory.
- It creates the metadata the recommendation engine will depend on later.
- It lets the MVP demonstrate AI-assisted value before outfit generation is added.

## How It Supports Later Recommendation Work
- Recommendation scoring needs category, color, season, temperature, and occasion metadata.
- Weather-aware logic later depends on clothing warmth and rain suitability fields.
- Style matching later depends on clean storage of `style_tags`, `season_tags`, and `occasion_tags`.

## Phase 2 Scope
- Clothing item data model and persistence
- Clothes CRUD API
- Mock AI analyze API for clothing metadata suggestions
- Demo seed wardrobe data
- Frontend wardrobe listing, add flow, edit flow, delete flow, and filters

## Phase 2 Boundaries
- This phase only manages clothing data and mock metadata generation.
- It does not implement weather retrieval, outfit generation, or recommendation scoring.
- It does not implement real image upload or object storage.
