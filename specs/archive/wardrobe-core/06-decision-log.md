# Wardrobe Core Decision Log

## Decision 1: Use Mock AI Instead of Real Vision
- Decision:
  - Implement `POST /api/clothes/analyze` with deterministic keyword rules.
- Why:
  - Phase 2 needs editable metadata suggestions without external dependencies or privacy leakage.
- Alternatives Rejected:
  - Calling a real multimodal API
  - Shipping without analyze support at all
- Future Extension:
  - Replace `ai_vision_service.py` with a true vision adapter while keeping the same schema contract.

## Decision 2: Avoid Real File Storage in Phase 2
- Decision:
  - Use `image_url` strings only and do not implement upload persistence.
- Why:
  - The goal is wardrobe metadata management, not storage infrastructure.
- Alternatives Rejected:
  - Local file upload handling
  - Object storage integration
- Future Extension:
  - Add upload endpoints and object storage adapters later without changing clothing metadata fields.

## Decision 3: Keep the App Single-User for MVP
- Decision:
  - Store all wardrobe data in one local SQLite dataset.
- Why:
  - Multi-user isolation is out of scope and would add auth and data ownership complexity unrelated to the MVP loop.
- Alternatives Rejected:
  - Adding login and per-user tables now
- Future Extension:
  - Add ownership fields and auth boundaries when multi-user support becomes a real product need.

## Decision 4: Seed Demo Clothes Through Backend Bootstrap
- Decision:
  - Insert demo wardrobe rows on startup only when the clothes table is empty.
- Why:
  - The demo should be immediately usable without manual setup.
- Alternatives Rejected:
  - Manual seed commands only
  - Frontend-only mock wardrobe data
- Future Extension:
  - Move to explicit seed management if the dataset grows or environments need different fixtures.
