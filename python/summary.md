# python Distilled Best Practices

## Key Decisions

- Use PEP 8 consistency and explicit typing for stable public interfaces.
- During refactor, lock down schema and function signatures with tests + type hints.
- Avoid implicit side effects across modules; keep boundaries explicit.

## Usage

- Use these distilled points as refactor constraints before touching code.
- Validate each adopted point with tests and regression gates.
