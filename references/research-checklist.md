# Research Checklist

## Purpose

Ensure best-practice research is deep enough before refactor execution.

## Minimum Research Depth (Mandatory)

For each refactor run:

1. Frontend partition: at least 2 primary sources if frontend exists.
2. Backend partition: at least 2 primary sources if backend exists.
3. Language partition: at least 1 primary source per detected language.
4. Architecture partition: at least 2 primary sources.
5. At least one source per partition must be current official documentation when available.

## Source Priority

1. Official framework/runtime/language docs
2. Official cloud/platform architecture docs
3. Primary architecture literature (for trade-off discussion)

## Research Output Format

Produce and keep this table in execution logs/docs:

| Partition | Source URL | Why This Source | Adopted Practice | Refactor Impact |
| --- | --- | --- | --- | --- |

## Adoption Rules

1. Every adopted practice must map to a concrete code/test/doc action.
2. If two sources conflict, document the conflict and chosen policy.
3. Prefer compatibility-preserving choices unless user requests behavior change.
4. Avoid cargo-cult checklists; keep only practices justified by current repository context.

## Completion Requirement

Research gate is complete only when:

1. Source minimums are met.
2. Adopted practices are explicitly mapped to module plans.
3. Verification date is recorded.
