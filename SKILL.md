---
name: coverage-gated-refactor
description: "Drive full-project modular refactors with a strict pipeline: prioritize splitting oversized files, enumerate candidates for user scope selection, raise per-module test coverage to at least 90 percent with verified runnable tests, refactor frontend and backend in slices with immediate regression checks, update related documentation, and finish only when all selected modules plus historical tests pass."
---

# Coverage Gated Refactor

## Overview

Run refactors as a gated engineering workflow, not as ad-hoc edits.  
Keep behavior stable by proving parity with tests at every step.

## Workflow

### 0. Capture Refactor Goal And Scope (Mandatory)

1. Require the user to describe the refactor goal first (why this refactor is needed).
2. Require the user to choose scope before planning:
   - frontend
   - backend
   - other modules
   - all modules (frontend + backend + other)
3. If user chooses `all`, execute full-scope workflow without skipping areas.
4. Convert the user goal into success criteria and keep it in progress reports.

### 1. Build Refactor Candidate Map (Mandatory)

1. Inventory code by module boundaries, file size, coupling, churn risk, and bug density.
2. Prioritize oversized files and modules first; make large-file decomposition the default first wave.
3. Enumerate refactor candidates as a user-facing list.
4. For each candidate, include:
   - Why it should be refactored
   - Expected benefit
   - Estimated risk
   - Suggested order
5. Present options to user:
   - Select specific modules
   - Select all modules
6. If user says “all”, execute full list without skipping.

### 2. Autonomous Execution Rule (Mandatory)

1. If user explicitly requires full autonomous execution, continue end-to-end without pausing for optional confirmation.
2. If user explicitly says "do not stop" or equivalent, do not pause for stage handoffs, progress approvals, or reconfirmation prompts.
   - 硬规则：用户明确要求“不要停”时，不得中途停下来询问、确认或等待批准，必须连续执行到全部任务完成（除非遇到无法自行解决的硬阻塞）。
3. Execute continuously in one run until all selected scope and all gates are completed.
4. Ask questions only for hard blockers that cannot be resolved from repository context.
5. Keep executing module by module until all selected scope is completed and all gates pass.

### 3. Baseline and Test Infrastructure

1. Add missing scripts (`test`, `test:coverage`, optional `test:watch`).
2. Run historical test suite and collect baseline pass/fail + coverage numbers.
3. Fix broken imports, aliases, mocks, and environment issues so tests are runnable.
4. Record baseline report before writing new tests.

### 4. Best-Practice Research Before Each Module Refactor

For each selected module, before coding:

1. Search current best practices relevant to that module type and stack.
2. Prefer official docs, framework guides, and primary sources.
3. Extract a short “adopted practices” list and map it to the module plan.
4. Keep behavior-compatible decisions unless user requested behavior change.

### 5. Module Test Gate (At Least 90 Percent)

For each selected module:

1. Write contract tests and regression tests for critical behavior.
2. Cover:
   - Input validation
   - Error handling
   - Output schema
   - Side effects and integration points
3. Raise module coverage to at least 90 percent (statements and lines preferred).
4. Execute tests and verify they are actually runnable and stable.
5. Do not start module refactor until module test gate is green.

### 6. Refactor Module in Safe Slices

For each selected module:

1. Perform no-op extraction first (move code without behavior changes).
2. Apply deeper structural changes in bounded slices.
3. After each slice:
   - Run module tests
   - Run relevant integration tests
4. If failures appear, fix immediately before continuing.

### 7. Full Regression Gate After Each Module

After finishing one module:

1. Re-run historical full test suite.
2. Re-run full coverage check.
3. Confirm no regressions before starting next module.

### 8. Completion Gate

Declare refactor complete only when all are true:

1. All selected modules are refactored.
2. Frontend and backend selected scope is both completed.
3. Every selected module meets test gate.
4. Historical full test suite passes.
5. No unresolved regression remains.
6. Related documentation is updated to match the new structure and behavior.
7. Final summary delivered to user.

Then explicitly notify user that refactor is completed.

## Coverage Policy

1. Module-level gate: at least 90 percent coverage before refactor.
2. Prefer statements and lines both at or above gate.
3. Use stricter threshold if user asks.
4. Treat red tests as hard stop.

## Full-Stack And Docs Scope

1. Include frontend and backend modules in the same gated workflow when scope is “all”.
2. Refactor docs that describe touched modules, interfaces, or workflows.
3. Validate docs are consistent with renamed files, extracted modules, and updated commands.

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

1. Refactor goal: user-stated purpose and success criteria.
2. User scope: frontend/backend/other/all.
3. Candidate map: listed modules and default order.
4. Baseline: tests X pass / Y fail, coverage S/B/F/L.
5. Module gate: module name, coverage, test status.
6. Refactor progress: completed module list and next module.
7. Final gate: full historical tests pass/fail and completion decision.
8. Docs sync: updated docs list and validation result.

## Do Not

1. Do not skip refactor-goal capture and scope selection.
2. Do not skip module enumeration and user scope confirmation.
3. Do not start module refactor before module test gate.
4. Do not claim “fully guaranteed” behavior parity without evidence.
5. Do not use destructive git commands unless explicitly requested.
6. Do not weaken or bypass tests to hit target numbers.
7. Do not stop midway when user asked for full autonomous completion, unless hard-blocked.
8. Do not stop when user explicitly says "do not stop"; finish the entire pipeline in one continuous execution unless truly hard-blocked.
9. 硬规则：当用户说“不要停”时，必须一口气做完，不得中断回问；仅在确实无法自行处理的硬阻塞下才可暂停并说明原因。
