# Frontend Recommendation Flow Tasks

## Task 1: Re-open Phase 5 Change Spec
- Restore an active `frontend-recommendation-flow` change set under `specs/changes/`
- Update requirements, architecture, tests, tasks, and decision log for upload UX and outfit carousel scope

## Task 2: Build Centralized Image Upload Panel
- Create `frontend/src/components/upload/ImageUploadPanel.tsx`
- Support:
  - mobile camera input
  - mobile album / file input
  - desktop drag-and-drop
  - desktop upload button
  - URL fallback for demo use only
- Keep upload logic out of page-level duplication

## Task 3: Refactor ClothingItemForm Around Upload States
- Replace URL-first entry with upload-first layout
- Add local preview generation with `URL.createObjectURL`
- Validate file type and size before analyze
- Support initial, selected, preview, analyzing, editable result, success, save error, and invalid file states
- Continue sending contract-compatible `image_url` to create and analyze calls

## Task 4: Preserve Clothes API Compatibility
- Keep existing frontend service calls intact
- Use mock image keys derived from local uploads instead of integrating storage
- Ensure create and edit flows still work with existing payload shapes

## Task 5: Build Outfit Carousel
- Create `frontend/src/components/outfit/OutfitCarousel.tsx`
- Show one current look at a time
- Reset to the first look on new result payloads
- Display candidate meta and current look indicator

## Task 6: Build Look Navigation
- Create `frontend/src/components/outfit/LookNavigation.tsx`
- Add previous / next actions and optional dots
- Keep controls touch-friendly and dependency-free

## Task 7: Refactor Outfit Result Presentation
- Move outfit-focused UI into:
  - `frontend/src/components/outfit/OutfitResultCard.tsx`
  - `frontend/src/components/outfit/ScoreBreakdown.tsx`
  - `frontend/src/components/outfit/ReasoningPanel.tsx`
  - `frontend/src/components/outfit/WarningList.tsx`
- Keep item grid readable without creating a long page

## Task 8: Collapse Detailed Reasoning By Default
- Use native disclosure UI
- Keep summary reasoning always visible
- Make score breakdown compact

## Task 9: Integrate Carousel Into RecommendationPage
- Replace stacked result mapping with one-look-at-a-time rendering
- Preserve loading, error, empty, and insufficient-wardrobe states
- Preserve regenerate behavior

## Task 10: Responsive Polish And Documentation
- Verify upload and result layout at phone, tablet, and desktop widths
- Update README with upload UX and outfit carousel UX
- Leave backend APIs and storage architecture unchanged for this phase
