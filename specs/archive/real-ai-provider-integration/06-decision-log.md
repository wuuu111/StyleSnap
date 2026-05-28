# Real AI Provider Integration Decision Log

## Decision 1: Keep Rule-Based Ranking As The Source Of Truth
- Decision:
  - the LLM enhances reasoning and optional rerank only after deterministic recommendation selection
- Why:
  - this keeps recommendations grounded in actual wardrobe items and preserves explainability

## Decision 2: Default To Mock Providers
- Decision:
  - both stylist and vision remain `mock` by default
- Why:
  - local demo stability and testability matter more than always-on provider dependency

## Decision 3: Use DeepSeek For Text-Only Stylist Enhancement
- Decision:
  - DeepSeek receives structured clothing and context metadata, not raw images
- Why:
  - this reduces privacy exposure and keeps the integration simpler than full multimodal rollout

## Decision 4: Fall Back Instead Of Failing Core APIs
- Decision:
  - provider failures should degrade gracefully to mock/template behavior
- Why:
  - AI enhancement should never break the main recommendation or analyze user flow

## Decision 5: Vision Provider Is Abstracted Before Real Rollout
- Decision:
  - refactor analyze behind a provider interface now, but keep real vision as a later integration step
- Why:
  - this preserves architecture clarity without taking on image-storage and privacy complexity in the same phase
