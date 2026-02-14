# Language Best Practices

## Scope

Use this file for language-specific refactor constraints.

## TypeScript

### Practices

1. Keep strict type checking enabled for refactor safety.
2. Prefer explicit domain types over broad `any`/implicit structural drift.
3. Separate API DTOs from internal domain models.
4. Use narrow utility types and avoid unreadable type-level overengineering.

### Primary Sources

- TypeScript Handbook:
  - https://www.typescriptlang.org/docs/handbook/intro.html
- TSConfig strict mode:
  - https://www.typescriptlang.org/tsconfig#strict

## Python

### Practices

1. Follow PEP 8 naming/layout consistency for maintainability.
2. Add type hints for public interfaces touched by refactors.
3. Keep modules cohesive and explicit about side effects.

### Primary Sources

- PEP 8:
  - https://peps.python.org/pep-0008/
- Python typing module:
  - https://docs.python.org/3/library/typing.html

## Go

### Practices

1. Favor simple, clear packages with small public surfaces.
2. Keep error handling explicit and contextual.
3. Align names and API shapes with Effective Go conventions.

### Primary Sources

- Effective Go:
  - https://go.dev/doc/effective_go
- Go Code Review Comments:
  - https://go.dev/wiki/CodeReviewComments

## Java

### Practices

1. Keep package and class boundaries stable during refactor.
2. Use consistent naming and formatting conventions project-wide.
3. Keep business logic independent from transport/framework details.

### Primary Sources

- Oracle Java code conventions (legacy but still a baseline reference):
  - https://www.oracle.com/java/technologies/javase/codeconventions-contents.html

## Refactor Decisions To Record

For each language-sensitive refactor, explicitly record:

1. Type-system impact
2. Public API compatibility impact
3. Lint/static analysis expectations
4. Test fixture and mock adaptation
