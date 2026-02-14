# backend Distilled Best Practices

## Key Decisions

- Keep controller/handler thin and move business logic to services/modules.
- Decompose only after validating operational trade-offs (latency, observability, release complexity).
- Apply reliability and security baselines as hard constraints during structural refactor.

## Usage

- Use these distilled points as refactor constraints before touching code.
- Validate each adopted point with tests and regression gates.
