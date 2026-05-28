# Real AI Provider Integration Tasks

## Task 1: Create Phase 7 spec
- write context, requirements, architecture, test plan, review checklist, and decision log

## Task 2: Add provider configuration
- update `.env.example`
- add environment-driven provider selection defaults

## Task 3: Build provider package
- add stylist and vision provider protocols
- add mock and DeepSeek stylist implementations
- add mock and placeholder vision implementations

## Task 4: Refactor clothes analyze through vision provider
- preserve current API behavior
- keep mock fallback stable

## Task 5: Integrate stylist provider into recommendation service
- preserve rule-based candidate generation and scoring
- merge enhanced reasoning
- attach `ai_metadata`

## Task 6: Add provider and API tests
- add unit and integration coverage for success and fallback paths

## Task 7: Update README
- document provider modes, DeepSeek enablement, fallback behavior, and API key safety

## Task 8: Verify, review, and archive
- run backend and frontend verification
- update current specs
- archive Phase 7 after acceptance
