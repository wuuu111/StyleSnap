# Frontend Recommendation Flow Architecture

## Page Structure
- `AddItemPage`
  - page intro
  - `ClothingItemForm`
    - `ImageUploadPanel`
    - editable metadata form
- `RecommendationPage`
  - page intro and layout shell
  - `WeatherContextPanel`
  - `RecommendationForm`
  - result shell
    - `OutfitCarousel`
      - `LookNavigation`
      - `OutfitResultCard`
        - `ScoreBreakdown`
        - `ReasoningPanel`
        - `WarningList`
        - existing `OutfitItemGrid`

## Planned Components

### ImageUploadPanel
- Owns upload-specific UX for Add Item.
- Supports:
  - mobile camera input
  - mobile album / device input
  - desktop drag-and-drop zone
  - desktop upload button
  - development-only URL fallback
- Receives selected file state, preview URL, validation errors, and change handlers from the parent form.
- Does not call the network layer directly.
- Keeps upload logic centralized so Add Item remains the only workflow orchestrating local preview and analyze setup.

### ClothingItemForm
- Remains the orchestration layer for clothing create/edit forms.
- Extends state to include:
  - selected `File | null`
  - `previewUrl`
  - upload validation error
  - analyze status
  - save success / save error feedback
- When a file is selected:
  - validate type and size
  - create object URL preview
  - derive a mock analyze key from filename or preview URL
  - sync `form.image_url` to the local placeholder used by the MVP
- When editing an existing item:
  - current remote `image_url` remains usable
  - upload panel may still replace the preview with a new local selection

### OutfitCarousel
- Owns `currentIndex` for the generated outfit array.
- Resets to index `0` whenever a new recommendation payload arrives.
- Resolves `currentOutfit = outfits[currentIndex]`.
- Renders:
  - top-level result meta
  - current look indicator
  - navigation controls
  - optional dot indicators
  - one `OutfitResultCard`

### LookNavigation
- Stateless navigation control for previous / next switching.
- Receives current index, total count, and handlers.
- Must stay keyboard- and touch-friendly.
- Uses simple buttons and optional dots instead of a dependency-heavy carousel solution.

### OutfitResultCard
- Refactors the existing result card into a focused single-look presentation.
- Displays:
  - look label such as `Look 2 / 3`
  - title
  - total score
  - compact tags
  - item grid
  - score breakdown
  - summary reasoning
  - collapsible detailed reasoning
  - warnings

### ScoreBreakdown
- Keeps the existing five-dimension presentation but tightens spacing so it fits comfortably inside one card.
- No chart library.

### ReasoningPanel
- Splits reasoning into:
  - always-visible summary block
  - collapsible detailed section with weather, style, color, occasion, and preference reasoning
- Uses native `<details>` and `<summary>` to reduce page height and dependency cost.

### WarningList
- Keeps warnings concise and compact.
- Preserves the empty safe-state message.

## State Management
- Keep state local to page or form owners.
- `RecommendationPage` owns:
  - weather state
  - recommendation request state
  - recommendation result
- `OutfitCarousel` owns only `currentIndex`.
- `ClothingItemForm` owns:
  - upload state
  - analyze state
  - editable clothing payload state
- No global store or new dependency is needed.

## Upload Processing Boundary
- The frontend continues to call `POST /api/clothes/analyze` with `image_url`.
- For local files, the frontend fabricates a mock analyze key from:
  - `file.name.toLowerCase()`, preferred for deterministic keyword mocking
  - fallback `previewUrl` if needed
- Saved `image_url` remains a local preview placeholder in Phase 5.
- This preserves backend compatibility while deferring real storage to a later phase.

## Dependency Strategy
- Do not add cloud storage SDKs in this phase.
- Do not add UI or carousel libraries.
- Reuse existing Tailwind utility patterns and component boundaries.
- Reuse existing `OutfitItemGrid`, `ScoreBreakdown`, `ReasoningPanel`, and `WarningList` where possible, but refactor them to fit the single-look card flow.

## Backend Interaction Boundary
- Keep `POST /api/clothes`, `PUT /api/clothes/:id`, and `POST /api/clothes/analyze` contract-compatible.
- Keep `POST /api/outfits/recommend` unchanged.
- No backend scoring, reasoning, or storage changes in Phase 5.

## README Alignment
- README must document:
  - realistic image upload UX
  - MVP local preview behavior
  - future upgrade path to Supabase Storage or S3
  - focused one-look-at-a-time recommendation carousel UX
