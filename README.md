# Coverage-Gated Refactor Skill

A Codex skill for full-project refactors with strict safety gates, partition-based step loading, and source-backed best-practice research.

## Design Philosophy

1. Split oversized files first.
2. Refactor by domain/module boundaries, not random line cuts.
3. Use tests as the behavior contract before and after each slice.
4. Enforce module coverage gates (target: 90%+).
5. Run frontend, backend, language, and docs in one governed pipeline.
6. Load guidance step-by-step from partition folders, not all at once.
7. If user says "do not stop", execute continuously unless hard-blocked.

## Partition Packs

This skill uses these folders:

1. `./fornt`
2. `./backend`
3. `./python`
4. `./typescript`
5. `./nextjs`

Each folder contains:

1. `index.md`
2. `summary.md`
3. `sources/*.md` (downloaded URL snapshots + distilled point)

## Step Loading Order

1. Read `partition-loader.md`.
2. Detect partitions from repo evidence.
3. Load only matching packs (`fornt/backend/python/typescript/nextjs`).
4. Read each matched `summary.md` first.
5. Open only required `sources/*.md` files for current module decisions.

## How To Install

```bash
mkdir -p ~/.codex/skills/coverage-gated-refactor
cp SKILL.md ~/.codex/skills/coverage-gated-refactor/SKILL.md
cp partition-loader.md ~/.codex/skills/coverage-gated-refactor/partition-loader.md
mkdir -p ~/.codex/skills/coverage-gated-refactor/agents
cp agents/openai.yaml ~/.codex/skills/coverage-gated-refactor/agents/openai.yaml
for d in fornt backend python typescript nextjs; do
  mkdir -p ~/.codex/skills/coverage-gated-refactor/$d
  cp -R "$d"/* ~/.codex/skills/coverage-gated-refactor/$d/
done
```

## How To Use

Prompt examples:

1. `Use coverage-gated-refactor. Detect partitions and load only matching packs first.`
2. `Refactor all modules. Do not stop.`
3. `Use source snapshots in fornt/backend/python/typescript/nextjs to justify design decisions.`
4. `Keep module coverage above 90% and run full regression after each module.`

## Expected Behavior

1. Detect partition evidence first.
2. Load packs in steps and keep context scoped.
3. Reference local source snapshots when choosing architecture and code patterns.
4. Run test-gated refactor slices with continuous regression checks.
5. Finish only when selected scope, tests, and docs are all green.

## Multilingual

<details>
<summary>中文（Chinese）</summary>

这是一个覆盖率门禁重构 Skill，支持按分区分步加载：`./fornt ./backend ./python ./typescript ./nextjs`。

### 设计原则

1. 先拆大文件。
2. 按业务边界拆分。
3. 先测后改，改后再测。
4. 模块覆盖率门禁 90%+。
5. 前后端与文档同步推进。
6. 必须分步加载分区包，不允许一次性全量加载。
7. 用户说“不要停”时连续执行到完成（除硬阻塞外）。

### 使用方式

1. 先读取 `partition-loader.md`。
2. 识别项目分区后，按需加载对应目录。
3. 先读 `summary.md`，再按需打开 `sources/*.md`。
4. 每个模块重构前用本地来源快照提炼规则并映射到代码动作。

### 关键承诺

1. 没有门禁不推进。
2. 没有来源依据不推进。
3. 用户要求“不要停”时，不做可选确认中断。

</details>
