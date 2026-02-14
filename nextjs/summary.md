# nextjs Distilled Best Practices

## Key Decisions

- Keep App Router boundaries explicit and colocate route-related logic.
- Prefer server-side data-fetching boundaries where possible to reduce client complexity.
- Use Route Handlers as explicit API boundaries within Next.js apps.

## Usage

- Use these distilled points as refactor constraints before touching code.
- Validate each adopted point with tests and regression gates.
