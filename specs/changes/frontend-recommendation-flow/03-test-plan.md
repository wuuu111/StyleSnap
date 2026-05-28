# Frontend Recommendation Flow Test Plan

## Frontend Verification
- `cd frontend && npm run build`

## Backend Regression Verification
- `cd backend && pytest`

## Manual Acceptance

### Add Item Upload Manual Tests
- Mobile narrow screen shows `拍照添加` and `从相册选择`
- Desktop shows upload area and local file upload entry
- Selecting an image shows a preview
- Non-image file shows `请上传图片文件，且大小不超过 5MB。`
- Image larger than 5MB shows `请上传图片文件，且大小不超过 5MB。`
- Clicking `Mock AI Analyze` after selection generates editable metadata
- User can edit tags and other fields after analyze
- Saving succeeds and the new item appears in wardrobe
- Save error state is visible if create fails
- Development URL fallback remains available but is not the main entry point

### Outfit Carousel Manual Tests
- Generating 2-3 recommendations shows only Look 1 by default
- Clicking `Next` moves to Look 2
- Clicking `Previous` returns to Look 1
- Look indicator stays correct, such as `Look 2 / 3`
- The page no longer stacks all Looks vertically
- Detailed reasoning is collapsed by default and does not over-extend page height
- Mobile layout has no horizontal scrolling
- Desktop result card height remains readable and focused

### Existing Recommendation Flow Regression
- Recommendation page loads correctly
- `Use my location` button is visible in the initial state
- Successful geolocation shows weather context
- Denied or failed geolocation reveals city fallback
- City fallback fetch renders weather context
- Occasion, target style, and preference inputs render correctly
- Clicking `Generate Outfits` renders recommendation results
- Regenerate action triggers another recommendation request
- Weather loading state is clear
- Recommendation loading state is clear
- Recommendation error state is clear
- Insufficient wardrobe state links users to wardrobe
- Wardrobe page still works
- Landing page recommendation link still works

## Optional Testing Scope
- If no existing frontend test framework is present, do not add one just for Phase 5.
- If a browser-based manual pass is available, use responsive emulation for narrow mobile, tablet, and desktop widths.

## Exit Criteria
- Frontend build passes
- Backend regression suite passes
- Add Item upload UX works on mobile and desktop layouts
- Recommendation result area shows one Look at a time
- README and spec accurately describe the MVP upload/storage boundary
