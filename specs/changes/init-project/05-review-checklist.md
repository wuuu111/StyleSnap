# Init Project Review Checklist

## Spec Conformance Review
- Does the constitution reflect the project goal and MVP scope from the user brief?
- Does the repo map reflect the intended monorepo structure and API surface?
- Do the `init-project` spec files cover context, requirements, architecture, tests, tasks, and decisions?
- Is Phase 0 limited to documentation work only?
- Are future phase boundaries explicit enough to prevent scope drift?

## Architecture Review
- Are frontend and backend responsibilities separated clearly?
- Are AI, weather, clothing, and recommendation services defined as replaceable modules?
- Does the architecture avoid premature complexity for auth, multi-user behavior, or external providers?
- Is the data flow for the MVP loop understandable and testable?
- Are extension points clear without over-designing implementation details?

## Security and Regression Review
- Does the constitution prohibit hardcoded secrets and uncontrolled third-party data sharing?
- Are privacy risks around uploaded clothing images documented?
- Are validation and stable error response requirements captured?
- Does any file accidentally introduce application code, runtime config, or dependency setup in Phase 0?
- Could any documented boundary mislead future phases into unsafe CORS or logging behavior?

## Completion Review
- Are there any placeholders, contradictions, or vague statements left in the docs?
- Are any future decisions still open and, if so, are they recorded in the decision log?
- Can Phase 1 start from these files without guessing project intent?
