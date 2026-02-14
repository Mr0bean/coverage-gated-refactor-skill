# Frontend Best Practices

## Scope

Use this file when frontend partitions are detected.

## Next.js + React

### Practices

1. Keep route structure explicit and domain-oriented in `app/`.
2. Prefer Server Components by default; use Client Components only for interactivity and browser APIs.
3. Keep data fetching close to route boundaries and avoid duplicated fetch chains.
4. Use Route Handlers for backend-like endpoints owned by the frontend app boundary.
5. Keep React components pure and move side effects to controlled effect hooks.
6. Lift and centralize state only when multiple siblings depend on the same source of truth.

### Primary Sources

- Next.js project structure:
  - https://nextjs.org/docs/app/getting-started/project-structure
- Next.js data fetching:
  - https://nextjs.org/docs/app/building-your-application/data-fetching
- Next.js route handlers:
  - https://nextjs.org/docs/app/building-your-application/routing/route-handlers
- React component purity:
  - https://react.dev/learn/keeping-components-pure
- React shared state guidance:
  - https://react.dev/learn/sharing-state-between-components

## Vue + Nuxt

### Practices

1. Follow Vue official style guide naming and SFC organization.
2. Keep Nuxt file-system routing and app directory conventions clean and predictable.
3. Place composables/utilities by domain and avoid circular dependency graphs.

### Primary Sources

- Vue style guide:
  - https://vuejs.org/style-guide/
- Nuxt directory structure:
  - https://nuxt.com/docs/guide/directory-structure/app

## Angular

### Practices

1. Follow official style guide for feature grouping, naming, and separation.
2. Prefer feature-area boundaries over technical-layer sprawl.

### Primary Sources

- Angular style guide:
  - https://angular.dev/style-guide

## Refactor Decisions To Record

For each frontend module refactor, explicitly record:

1. Component boundary decision
2. State ownership decision
3. Data-fetching boundary decision
4. Routing/API boundary decision
