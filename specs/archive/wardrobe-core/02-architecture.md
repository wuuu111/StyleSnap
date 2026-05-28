# Wardrobe Core Architecture

## Backend Components

### ClothingItem Data Model
- SQLAlchemy model stored in SQLite
- Uses JSON columns for `style_tags`, `season_tags`, and `occasion_tags`
- Stores created and updated timestamps

### Pydantic Schemas
- Base clothing payload schema with validation for category and thickness
- Create/update request schemas
- Read response schema
- Analyze request and analyze response schemas
- Error response schema reusing the global envelope structure

### Routers
- `health.py` remains unchanged for regression safety
- New `clothes.py` router handles CRUD and analyze endpoints under `/api/clothes`

### Services
- `clothing_service.py`
  - CRUD orchestration
  - filter handling
  - seed bootstrap
  - missing-record handling
- `ai_vision_service.py`
  - keyword-based mock analyzer
  - deterministic fallback item

## Frontend Components

### Wardrobe Page
- Fetches wardrobe items
- Displays filters, empty state, loading state, and error state
- Hosts delete actions and links to add/edit flows

### Add Item Page
- Accepts `image_url`
- Calls mock analyze endpoint
- Shows editable form fields
- Saves a new clothing item

### Edit Item Page
- Fetches item by id
- Reuses the same form fields as add flow
- Updates an existing item

### Item Card Component
- Displays image, name, category, color, tags, thickness, and temperature range
- Exposes edit and delete actions

## Frontend API Client
- Centralize wardrobe requests in `frontend/src/services/clothesApi.ts`
- Reuse the base `apiFetch` helper from Phase 1

## State Management
- Keep state local to pages and shared form component
- No global store needed yet
- Shared form state lives inside a reusable `ClothingItemForm` component

## Demo Seed Data Strategy
- Seed on backend startup through `clothing_service.seed_demo_clothes`
- Guard with an existence check so seed rows are inserted once
- Keep seed metadata representative of later recommendation needs

## Extension Points
- Replace `ai_vision_service.py` with a multimodal provider later without changing the router contract
- Replace blank `image_url` handling with real upload flow later
- Feed the persisted wardrobe model directly into future recommendation services
