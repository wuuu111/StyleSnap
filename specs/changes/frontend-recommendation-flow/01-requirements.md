# Frontend Recommendation Flow Requirements

## Feature Goal
Update Phase 5 so the wardrobe intake flow feels like a real product and the recommendation result area stays focused, compact, and mobile-friendly.

## User Stories
- As a user, I can add clothing by taking a photo or choosing a local image instead of pasting a URL.
- As a mobile user, I can quickly capture a garment with the rear camera or pick one from my album.
- As a desktop user, I can drag and drop or upload an image from my device.
- As a user, I can preview the selected image before running mock AI analysis.
- As a user, I can edit the generated metadata before saving the item.
- As a user, I can review one recommended Look at a time instead of scrolling through a long stacked result list.
- As a user, I can switch between generated Looks without losing context.

## Functional Requirements
1. The Add Item flow must replace manual `image_url` entry as the primary visual entry point.
2. The Add Item page must provide a centralized image upload experience:
   - mobile-first camera entry
   - mobile album / local file entry
   - desktop drag-and-drop upload area
   - desktop upload button
   - development-only image URL fallback
3. Mobile upload UX must expose:
   - `拍照添加`
   - `从相册选择`
4. Mobile camera input must use:
   - `<input type="file" accept="image/*" capture="environment" />`
5. Desktop upload UX must communicate:
   - `Upload clothing image`
   - `Drag and drop an image here, or click to upload`
   - `Upload from device`
   - `Use image URL for demo`
6. The Add Item page must validate file input before analysis:
   - file MIME type starts with `image/`
   - file size is `<= 5MB`
7. Invalid files must show:
   - `请上传图片文件，且大小不超过 5MB。`
8. When a local image is selected, the frontend must:
   - generate a preview via `URL.createObjectURL(file)`
   - display the preview before save
   - pass a mock image identifier to the existing analyze API
9. Phase 5 must not introduce real object storage.
10. The existing clothes API contract must remain valid:
   - frontend may still send `image_url`
   - upload handling stays local in the MVP
11. Mock analyze integration may derive `image_url` from:
   - `file.name.toLowerCase()`
   - or the generated preview URL
12. The Add Item page must support these explicit states:
   - initial state
   - image selected state
   - preview state
   - analyzing state
   - analysis result editable form
   - save success
   - save error
   - unsupported file type error
13. The recommendation page must keep weather-first input flow and existing recommendation API usage.
14. Recommendation results must no longer stack all Looks vertically.
15. Recommendation results must render as a single focused Look card with navigation:
   - `Look 1 of 3`
   - previous / next controls
   - or equivalent tab-like look switching
16. Only one Look may be visible at a time.
17. Each Look card must show:
   - look title
   - total score
   - outfit tags
   - item grid
   - score breakdown
   - summary reasoning
   - collapsible detailed reasoning
   - warnings
18. Detailed reasoning must not make the page long by default.
19. The recommendation page must keep regenerate behavior with the existing recommendation API.
20. The page must remain responsive across phone, tablet, and desktop.

## Responsive Requirements

### Add Item
- Mobile:
  - large buttons
  - single-column layout
  - preview above the form
  - comfortable field spacing
- Tablet:
  - stacked or hybrid layout is acceptable as long as upload actions stay prominent
- Desktop:
  - upload and preview panel on the left
  - editable metadata form on the right
  - drag-and-drop area is visible without scrolling far

### Recommendation
- Mobile:
  - input and result areas stack vertically
  - current Look card is single-column
  - navigation stays clear below the card
  - no horizontal scrolling
- Desktop:
  - input panel may remain on the left
  - current Look card stays on the right
  - result area avoids a long vertical list of multiple Looks

## Non-Goals
- No real cloud storage integration in Phase 5
- No real AI vision integration in Phase 5
- No carousel library introduction
- No recommendation API contract rewrite
- No clothes API contract rewrite
- No upload logic duplicated across multiple pages

## Rationale Summary
- `image_url` is not a realistic first-touch UX for wardrobe intake, so it becomes a fallback instead of the hero action.
- Mobile needs camera and album entry because garment capture is often immediate and device-native.
- Desktop needs drag-and-drop and file upload because “take a photo” is not the dominant desktop behavior.
- A single-Look carousel avoids the long-page problem and improves comparison, screenshots, and recordings.
- Third-party carousel dependencies are unnecessary for a simple indexed result switcher and would add avoidable weight and complexity.
- Local preview is sufficient for MVP validation while keeping backend contracts stable until a later storage phase.
