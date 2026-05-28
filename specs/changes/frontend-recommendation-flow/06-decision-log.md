# Frontend Recommendation Flow Decision Log

## Decision 1: Replace URL-First Add Item UX With Upload-First UX
- Decision:
  - Make local image selection the primary Add Item entry point and demote manual `image_url` input to a development fallback.
- Why:
  - Real wardrobe products start from user-owned photos, not pasted URLs.
  - URL-first entry makes the workflow feel like an engineering demo instead of a consumer-facing product.
- Alternatives Rejected:
  - Keeping `image_url` as the default visible control
  - Hiding local upload until a future phase
- Future Extension:
  - Real uploaded assets can later replace the local preview placeholder without changing the page-level UX.

## Decision 2: Prioritize Camera And Album Entry On Mobile
- Decision:
  - Mobile upload UX must foreground `拍照添加` and `从相册选择`.
- Why:
  - Mobile is the most natural environment for wardrobe capture.
  - Camera and album flows map directly to how users digitize clothing in real life.
  - `capture="environment"` provides a pragmatic rear-camera hint without adding native dependencies.
- Alternatives Rejected:
  - A generic file picker only flow
  - A URL-only or text-input-first mobile flow
- Future Extension:
  - Later phases can add multi-image capture or cropping without changing this entry model.

## Decision 3: Provide Drag-And-Drop And File Upload On Desktop
- Decision:
  - Desktop must emphasize drag-and-drop and device upload instead of camera language.
- Why:
  - Desktop usage patterns center on local files, not immediate camera capture.
  - Drag-and-drop reduces friction during bulk or repeated wardrobe entry.
- Alternatives Rejected:
  - Reusing the same mobile-first copy on desktop
  - Forcing desktop users through a URL field first
- Future Extension:
  - Future storage integration can upload the same selected files without redesigning the desktop panel.

## Decision 4: Keep Upload Processing Local In Phase 5
- Decision:
  - Use local preview URLs and mock analyze keys instead of integrating Supabase Storage or S3.
- Why:
  - Phase 5 is a UX polish phase, not a storage infrastructure phase.
  - Local preview is enough to validate the workflow while preserving the stable clothes API.
  - Real storage would add backend and deployment scope unrelated to the targeted UX improvements.
- Alternatives Rejected:
  - Introducing object storage during frontend polish
  - Blocking upload UX improvements until storage exists
- Future Extension:
  - Replace the local placeholder `image_url` with a real uploaded asset URL in a dedicated storage phase.

## Decision 5: Present Recommendation Results As A Single Look Carousel
- Decision:
  - Show one Look card at a time with explicit navigation instead of stacking all generated outfits vertically.
- Why:
  - The stacked layout becomes too long and weakens comparison between Looks.
  - A focused single-card view is easier to read, easier to record, and better for portfolio screenshots.
  - Mobile screens benefit from bounded vertical content.
- Alternatives Rejected:
  - Rendering all Looks in one long column
  - Moving results into tabs without previous / next navigation cues
- Future Extension:
  - Additional comparison affordances can later build on the same single-look container.

## Decision 6: Avoid A Third-Party Carousel Dependency
- Decision:
  - Implement the result switcher with local state and simple buttons.
- Why:
  - The interaction is small, deterministic, and easy to implement without a heavy dependency.
  - Avoiding a carousel library reduces bundle cost, styling conflicts, and maintenance overhead.
- Alternatives Rejected:
  - Adding a large carousel package for basic previous / next behavior
- Future Extension:
  - If future phases need gestures or autoplay, the current API surface can still wrap a richer implementation later.
