# Backend Best Practices

## Scope

Use this file when backend partitions are detected.

## Node.js + NestJS

### Practices

1. Organize by modules (bounded feature areas), not by giant shared files.
2. Keep controllers thin; move business logic into providers/services.
3. Use dependency injection boundaries to make services testable.

### Primary Sources

- Nest modules:
  - https://docs.nestjs.com/modules
- Nest controllers:
  - https://docs.nestjs.com/controllers

## Node.js + Express

### Practices

1. Apply production performance guidance (compression, clustering/process strategy, safe async patterns).
2. Apply security hardening baseline (headers, dependency hygiene, input safety, TLS discipline).
3. Isolate routing, domain services, and persistence adapters.

### Primary Sources

- Express performance best practices:
  - https://expressjs.com/en/advanced/best-practice-performance.html
- Express security best practices:
  - https://expressjs.com/en/advanced/best-practice-security.html

## Python + FastAPI

### Practices

1. Split big apps into routers/modules; avoid single-file API growth.
2. Use dependency injection (`Depends`) for composable service boundaries.
3. Keep request/response schemas explicit and validated.

### Primary Sources

- FastAPI bigger applications:
  - https://fastapi.tiangolo.com/tutorial/bigger-applications/
- FastAPI dependencies:
  - https://fastapi.tiangolo.com/tutorial/dependencies/

## Java + Spring Boot

### Practices

1. Structure code by feature/domain packages with clear entry points.
2. Keep web/controller layer separated from service and repository concerns.
3. Minimize framework leakage into core domain logic.

### Primary Sources

- Spring Boot code structure:
  - https://docs.spring.io/spring-boot/reference/using/structuring-your-code.html

## Refactor Decisions To Record

For each backend module refactor, explicitly record:

1. API boundary and handler/controller responsibility
2. Service layer contract changes (if any)
3. Persistence boundary and transaction assumptions
4. Error model and validation policy
