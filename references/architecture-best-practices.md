# Architecture Best Practices

## Scope

Use this file for architecture-level refactor decisions.

## Decision Baseline

1. Treat architecture choice as a trade-off, not a default ideology.
2. Prefer simpler architecture that satisfies current constraints.
3. Escalate complexity only with clear operational/product evidence.

## Modular Monolith

### When To Prefer

1. Single product team or tightly coupled domain changes
2. Need fast iteration without distributed-systems overhead
3. Early-stage systems that do not need independent service scaling yet

### Guidance

1. Keep strict module boundaries inside one deployable unit.
2. Enforce dependency direction and clear domain ownership.

### Sources

- Martin Fowler, Monolith First:
  - https://martinfowler.com/bliki/MonolithFirst.html
- Spring Modulith reference (modular monolith support):
  - https://docs.spring.io/spring-modulith/reference/

## Microservices

### When To Prefer

1. Clear bounded contexts with independent scaling/release needs
2. Strong platform maturity (observability, CI/CD, SRE ownership)
3. Organization can operate distributed systems reliably

### Guidance

1. Decompose by business capability, not by technical layers.
2. Require strong service contracts, observability, and failure isolation.
3. Measure latency/error/cost overhead before and after decomposition.

### Sources

- Azure architecture styles (microservices and other styles):
  - https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/
- Martin Fowler microservices trade-offs:
  - https://martinfowler.com/articles/microservice-trade-offs.html

## Reliability / Security / Operations Baseline

### Guidance

1. Evaluate architecture changes against operational pillars.
2. Keep reliability and security requirements explicit in refactor decisions.

### Sources

- AWS Well-Architected Framework:
  - https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html

## Frontend Architecture Note (Micro-Frontends)

Use micro-frontends only when multiple teams and release autonomy justify the complexity.

### Source

- AWS prescriptive guidance for micro-frontend architecture:
  - https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/introduction.html

## Refactor Decisions To Record

For each architecture-impacting refactor, explicitly record:

1. Chosen architecture style and rejected alternatives
2. Expected benefit and measurable success criteria
3. Operational impact (deployment, observability, incident response)
4. Rollback strategy
