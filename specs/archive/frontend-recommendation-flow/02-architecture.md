# Frontend Recommendation Flow Architecture

## Page Structure
- `RecommendationPage`
  - page intro and layout shell
  - `WeatherContextPanel`
  - `RecommendationForm`
  - `OutfitResultsSection`
    - `OutfitResultCard[]`
  - empty or error states when needed

## Planned Components

### WeatherContextPanel
- Owns weather acquisition UX presentation:
  - location CTA
  - loading state
  - fallback city input
  - rendered weather summary
- Uses existing `weatherApi.ts` service only through page callbacks or passed handlers.

### RecommendationForm
- Owns occasion, target style, and preference inputs.
- Receives current values, change handlers, submit handler, and disabled/loading state as props.
- Does not call fetch directly.

### OutfitResultCard
- Displays one recommendation in a polished card.
- Includes:
  - rank label
  - total score badge
  - tag-like summary metadata
  - item grid
  - score breakdown
  - reasoning panel
  - warning list

### ScoreBreakdown
- Displays the five score dimensions.
- Uses simple progress bars and numeric labels.
- No chart library.

### ReasoningPanel
- Splits summary, weather fit, style match, color harmony, occasion fit, and preference fit into readable blocks.

### WarningList
- Shows warnings as a compact alert section.
- Shows a safe “no obvious risk” state when warnings are empty.

### OutfitItemGrid
- Shows recommendation items by role.
- Displays image when available; otherwise shows clean placeholder.

### EmptyState / ErrorState
- Reusable presentation blocks for:
  - no weather yet
  - recommendation failure
  - insufficient wardrobe
  - no result found

## State Management
- Keep state local to `RecommendationPage`.
- Use prop-based composition instead of adding a global store.
- Continue centralized API access in:
  - `frontend/src/services/weatherApi.ts`
  - `frontend/src/services/recommendationApi.ts`

## Dependency Strategy
- Do not add a UI component library.
- Reuse Tailwind utility patterns already present in the repo.
- Reuse existing `PageHeader` and `WeatherCard` only if their responsibilities still fit; otherwise split the current weather presentation into a recommendation-specific panel.

## Backend Interaction Boundary
- Keep the recommendation API contract unchanged.
- Backend changes are allowed only if a response typing issue or error mapping issue is discovered during implementation.
- No scoring or algorithm changes in Phase 5.
