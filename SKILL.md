---
name: coverage-gated-refactor
description: "Drive full-project modular refactors with step-by-step partition loading from ./fornt ./backend ./python ./typescript ./nextjs, store source URLs as local markdown snapshots, distill best practices, enforce 90 percent coverage gates, and execute autonomously end-to-end when requested."
---

# Coverage Gated Refactor

## Overview

Run refactors as a gated engineering workflow, not as ad-hoc edits.
Keep behavior stable by proving parity with tests at every step.

This skill must load guidance in partitions, not all at once.

## Mandatory Folder Layout

Use these partition packs:

1. `./fornt` (frontend generic)
2. `./backend` (backend + architecture)
3. `./python` (python language)
4. `./typescript` (typescript language)
5. `./nextjs` (next.js framework)

Each partition pack contains:

1. `index.md` (load rule + file list)
2. `summary.md` (distilled key practices)
3. `sources/*.md` (downloaded source snapshots + distilled key point)

## Step-By-Step Loading (Mandatory)

Always follow this order:

1. Read `partition-loader.md`.
2. Detect repository partitions from code evidence.
3. Load matching packs only:
   - frontend -> `./fornt/index.md`
   - backend -> `./backend/index.md`
   - python -> `./python/index.md`
   - typescript -> `./typescript/index.md`
   - nextjs -> `./nextjs/index.md`
4. For each loaded pack:
   - read `summary.md` first
   - then open only needed `sources/*.md`
5. Record loaded pack list and source files used in the execution log.

Do not bulk-load irrelevant packs.

## Workflow

### 0. Partition Detection And Evidence Map (Mandatory)

1. Detect stack signals from repository files before planning.
2. Build a partition evidence table:
   - partition
   - evidence files
   - loaded pack path
   - selected source md files
3. If ambiguous, run targeted source retrieval and record assumptions.

### 1. Build Refactor Candidate Map (Mandatory)

1. Inventory code by module boundaries, file size, coupling, churn risk, and bug density.
2. Prioritize oversized files and modules first; large-file decomposition is default first wave.
3. Enumerate refactor candidates as a user-facing list.
4. For each candidate, include:
   - why refactor
   - expected benefit
   - estimated risk
   - suggested order
5. Support both scope modes:
   - selected modules
   - all modules
6. If user says "all", execute full list without skipping.

### 2. Autonomous Execution Rule (Mandatory)

1. If user explicitly requires full autonomous execution, continue end-to-end without pausing for optional confirmation.
2. If user explicitly says "do not stop" or equivalent, do not pause for stage handoffs, progress approvals, or reconfirmation prompts.
   - 中文硬规则：用户明确要求“不要停”时，不得中途停下来询问、确认或等待批准，必须连续执行到全部任务完成（除非遇到无法自行解决的硬阻塞）。
3. Execute continuously in one run until all selected scope and all gates are completed.
4. Ask questions only for hard blockers that cannot be resolved from repository context.

### 3. Baseline And Test Infrastructure

1. Add missing scripts (`test`, `test:coverage`, optional `test:watch`).
2. Run historical test suite and collect baseline pass/fail + coverage numbers.
3. Fix broken imports, aliases, mocks, and environment issues so tests are runnable.
4. Record baseline report before writing new tests.

### 4. Source-Backed Research Gate Per Partition (Mandatory)

Before each module refactor:

1. Use loaded partition packs as first-class guidance.
2. For each relevant module, cite at least:
   - one framework/platform source snapshot (`sources/*.md`)
   - one language source snapshot (`sources/*.md`)
   - one architecture/back-end source snapshot (`sources/*.md`)
3. Map distilled practices to concrete implementation choices.
4. Record source file paths and retrieval dates in logs/docs.
5. Keep behavior-compatible decisions unless user explicitly requests behavior change.

### 5. Module Test Gate (At Least 90 Percent)

For each selected module:

1. Write contract tests and regression tests for critical behavior.
2. Cover:
   - input validation
   - error handling
   - output schema
   - side effects and integration points
3. Raise module coverage to at least 90 percent (statements and lines preferred).
4. Execute tests and verify they are runnable and stable.
5. Do not start module refactor until module test gate is green.

### 6. Refactor Module In Safe Slices

For each selected module:

1. Perform no-op extraction first (move code without behavior changes).
2. Apply deeper structural changes in bounded slices.
3. After each slice:
   - run module tests
   - run relevant integration tests
4. If failures appear, fix immediately before continuing.

### 7. Full Regression Gate After Each Module

After finishing one module:

1. Re-run historical full test suite.
2. Re-run full coverage check.
3. Confirm no regressions before starting next module.

### 8. Completion Gate

Declare refactor complete only when all are true:

1. all selected modules are refactored
2. frontend and backend selected scope is both completed
3. every selected module meets test gate
4. historical full test suite passes
5. no unresolved regression remains
6. related documentation is updated to match new structure and behavior
7. final summary delivered to user

Then explicitly notify user that refactor is completed.

## Coverage Policy

1. Module-level gate: at least 90 percent coverage before refactor.
2. Prefer statements and lines both at or above gate.
3. Use stricter threshold if user asks.
4. Treat red tests as hard stop.

## Source Snapshot Policy

1. All canonical URLs must be stored as local markdown under partition `sources/`.
2. Each source file must include:
   - URL
   - retrieval time
   - fetch status
   - distilled key point
   - extracted source snapshot
3. When refreshing source snapshots, keep file names stable and update retrieval time.

## Bilingual Comment Standard

When adding non-trivial comments in tests and refactor code, write concise bilingual comments:

```ts
// Validate input shape before writing data.
// 写入数据前校验输入结构。
```

Rules:

1. Keep comments short and technical.
2. Avoid repeating obvious code.
3. Add bilingual comments only where logic is not self-evident.
4. Preserve existing project comment style if already defined.

## Progress Reporting Template

Use this concise status format while executing:

1. partition map: detected partitions + evidence
2. loaded packs: which of `fornt/backend/python/typescript/nextjs`
3. source files used: exact `sources/*.md` paths
4. candidate map: modules and default order
5. user scope: selected modules or all
6. baseline: tests X pass / Y fail, coverage S/B/F/L
7. module gate: module coverage + test status
8. refactor progress: completed modules and next module
9. final gate: full historical tests pass/fail
10. docs sync: updated files and validation result

## Do Not

1. Do not skip partition detection and evidence mapping.
2. Do not load irrelevant partition packs.
3. Do not skip module enumeration and user scope confirmation.
4. Do not start module refactor before module test gate.
5. Do not claim "fully guaranteed" behavior parity without evidence.
6. Do not use destructive git commands unless explicitly requested.
7. Do not weaken or bypass tests to hit target numbers.
8. Do not stop midway when user asked for full autonomous completion, unless hard-blocked.
9. Do not stop when user explicitly says "do not stop"; finish the entire pipeline in one continuous execution unless truly hard-blocked.
10. 中文硬规则：当用户说“不要停”时，必须一口气做完，不得中断回问；仅在确实无法自行处理的硬阻塞下才可暂停并说明原因。
