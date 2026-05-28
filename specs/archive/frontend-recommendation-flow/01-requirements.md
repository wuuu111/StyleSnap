# Frontend Recommendation Flow Requirements

## Feature Goal
Convert the existing recommendation page into a polished, portfolio-ready front-end flow that uses the stable Phase 4 recommendation API.

## User Stories
- As a user, I can complete the full recommendation flow from one page.
- As a user, I can try location-based weather first and fall back to manual city input if needed.
- As a user, I can choose my occasion, target style, and preference before generating outfits.
- As a user, I can see 2-3 visually structured outfit results with score breakdown, reasoning, and warnings.
- As a user, I can regenerate the recommendation without re-entering all inputs.

## Functional Requirements
1. The recommendation page must present:
   - page intro
   - weather context section
   - recommendation form
   - recommendation results section
2. The page title should read:
   - `今天穿什么？`
3. The page subtitle should communicate:
   - StyleSnap combines wardrobe, weather, occasion, and target style into daily recommendations.
4. Weather flow must remain location-first.
5. If location is denied or fails, city fallback must be available.
6. The recommendation form must include:
   - `occasion`
   - `target_style`
   - `preference_text`
7. The page must call the existing `POST /api/outfits/recommend` API without changing the backend contract.
8. The page must display 2-3 recommended outfits when results exist.
9. Each outfit card must show:
   - rank label such as `Look 1`
   - total score
   - summary
   - item list or item grid
   - score breakdown
   - reasoning sections
   - warnings
10. The page must support a regenerate action:
   - keeps the same weather source and form values
   - triggers the same API again
11. Loading, error, empty, and insufficient-wardrobe states must be explicit.
12. The page must remain mobile-first and screenshot-friendly.

## State Requirements
- Initial weather state:
  - explain why location helps
  - offer `Use my location`
  - offer manual city entry path
- Weather loading state:
  - explicit loading copy
- Weather failure state:
  - clear fallback path
- Recommendation loading state:
  - clear in-progress copy or button state
- Recommendation error state:
  - clear failure message
- Empty result state:
  - explain that no suitable look was found
- Insufficient wardrobe state:
  - explain the wardrobe needs at least a top and pants
  - include navigation action to wardrobe

## Non-Goals
- No recommendation algorithm rewrite
- No backend scoring changes
- No real LLM integration
- No virtual try-on
- No community or ecommerce features
- No complex animation system
- No large UI library introduction by default
