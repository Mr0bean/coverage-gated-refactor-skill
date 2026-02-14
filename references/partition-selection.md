# Partition Selection

## Purpose

Detect repository partitions before loading best-practice references.
Load only the relevant packs to keep context focused.

## Detection Order

1. Frontend partition
2. Backend partition
3. Language partition
4. Architecture partition

## Detection Signals

### Frontend

- Next.js / React:
  - `package.json` includes `next` and `react`
  - `app/` or `pages/` exists
- Vue / Nuxt:
  - `package.json` includes `vue` or `nuxt`
  - `nuxt.config.*` exists
- Angular:
  - `angular.json` exists

### Backend

- Node + Express:
  - `package.json` includes `express`
- Node + NestJS:
  - `package.json` includes `@nestjs/core`
- Python + FastAPI:
  - `pyproject.toml`/`requirements*.txt` includes `fastapi`
- Java + Spring Boot:
  - `pom.xml` or `build.gradle*` includes `spring-boot`

### Language

- TypeScript: `tsconfig.json`
- Python: `pyproject.toml`/`requirements*.txt`
- Go: `go.mod`
- Java: `pom.xml`/`build.gradle*`

### Architecture

- Modular monolith:
  - single deployable app + clear module boundaries
- Microservices:
  - multiple service deploy units, service-specific build/deploy configs
- Clean/Hexagonal hints:
  - folders like `domain`, `application`, `infrastructure`, `adapters`, `ports`

## Reference Pack Mapping

- Any frontend detected -> load `references/frontend-best-practices.md`
- Any backend detected -> load `references/backend-best-practices.md`
- Any language detected -> load `references/language-best-practices.md`
- Any architecture style detected -> load `references/architecture-best-practices.md`
- Always load at execution planning time -> `references/research-checklist.md`

## Output Requirement

For every run, produce a partition map table:

- partition
- detection evidence (file paths)
- selected reference packs
- unresolved ambiguity
