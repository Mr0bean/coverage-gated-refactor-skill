# Partition Loader

## Required Step Loading Order

1. Detect repository partitions from code and config evidence.
2. Load `./fornt/index.md` if frontend is detected.
3. Load `./nextjs/index.md` if Next.js is detected.
4. Load `./backend/index.md` if backend is detected.
5. Load `./python/index.md` if Python is detected.
6. Load `./typescript/index.md` if TypeScript is detected.
7. For each loaded pack, read `summary.md` first, then only needed `sources/*.md`.

## Output Requirement

For each run, output:
- detected partitions
- loaded packs
- source files consulted
- adopted practices mapped to implementation actions
