# Wardrobe Core Requirements

## Feature Goal
Implement the core wardrobe experience so a user can manage clothing items and receive editable mock AI metadata suggestions.

## User Stories
- As a user, I can add a clothing item to my wardrobe.
- As a user, I can view all clothing items in my wardrobe.
- As a user, I can filter wardrobe items by category, color, and season.
- As a user, I can edit an existing clothing item.
- As a user, I can delete a clothing item.
- As a user, I can submit an image URL to a mock AI analyzer and get suggested tags.
- As a user, I can modify the mock AI tags before saving the item.
- As a user, I can see demo clothing items even before adding my own wardrobe.

## Functional Requirements
1. The backend must persist `ClothingItem` records with the specified fields.
2. The backend must expose clothes CRUD APIs:
   - `POST /api/clothes`
   - `GET /api/clothes`
   - `GET /api/clothes/{id}`
   - `PUT /api/clothes/{id}`
   - `DELETE /api/clothes/{id}`
3. `GET /api/clothes` must support `category`, `color`, and `season` filters.
4. The backend must expose `POST /api/clothes/analyze` using mock logic only.
5. The backend must return stable error envelopes for invalid input and missing records.
6. The frontend wardrobe page must show loading, empty, populated, and error states.
7. The frontend must let users add, edit, and delete clothing items.
8. The frontend add flow must allow analyzing an image URL and editing returned tags before save.
9. Demo seed data must be inserted once and not duplicated on every startup.

## Required Fields and Validation
- Required on create:
  - `name`
  - `category`
  - `color`
  - `thickness`
- `category` allowed values:
  - `top`
  - `pants`
  - `outerwear`
  - `shoes`
  - `hat`
  - `bag`
  - `accessory`
- `thickness` allowed values:
  - `thin`
  - `medium`
  - `thick`
- `image_url` may be blank for manual entries but analyze requests require a non-empty URL.

## Edge Cases
- Empty wardrobe returns an empty list and frontend empty state.
- Invalid `category` returns `INVALID_INPUT`.
- Invalid `thickness` returns `INVALID_INPUT`.
- Missing required fields return validation errors in stable envelope form.
- Empty analyze `image_url` returns `INVALID_INPUT`.
- Deleting a missing item returns `NOT_FOUND`.
- Updating a missing item returns `NOT_FOUND`.
- Unknown analyze keywords return fallback metadata instead of failing.

## Non-Goals
- Real AI image recognition
- Weather module
- Outfit recommendation module
- User login
- Multi-user data isolation
- Real file upload storage or object storage integration
