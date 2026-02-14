# Coverage-Gated Refactor Skill

A Codex skill for full-project refactors with strict safety gates, partition-aware loading, and source-backed best-practice research.

## Design Philosophy

1. Split oversized files first to reduce structural risk.
2. Refactor by module boundaries, not random line-based cuts.
3. Build test evidence before and after each refactor slice.
4. Require strong module coverage (target: 90%+) before deep changes.
5. Cover frontend, backend, and related docs in one workflow.
6. Detect frontend/backend/language/architecture partitions first, then load only relevant guidance.
7. If the user says "do not stop", execute continuously end-to-end unless hard-blocked.

## Workflow (High Level)

1. Detect technology partitions and load scoped reference packs.
2. Enumerate refactor candidates for user scope selection.
3. Build/repair baseline test and coverage pipeline.
4. Run per-partition best-practice research from primary sources.
5. For each selected module: write tests first and hit coverage gate.
6. Refactor in safe slices and run tests after each slice.
7. Run full regression after each module.
8. Update documentation to match the new structure.
9. Finish only when all selected modules and historical tests pass.

## How To Use

### 1. Install Skill

```bash
mkdir -p ~/.codex/skills/coverage-gated-refactor
cp SKILL.md ~/.codex/skills/coverage-gated-refactor/SKILL.md
mkdir -p ~/.codex/skills/coverage-gated-refactor/agents
cp agents/openai.yaml ~/.codex/skills/coverage-gated-refactor/agents/openai.yaml
mkdir -p ~/.codex/skills/coverage-gated-refactor/references
cp -R references/* ~/.codex/skills/coverage-gated-refactor/references/
```

### 2. Start A Task

Use prompts like:

1. `Use coverage-gated-refactor. Detect partitions and enumerate all refactor candidates first.`
2. `Refactor all modules. Do not stop.`
3. `Research best practices for each detected partition from official docs before refactoring.`
4. `Keep module coverage above 90% and run full regression after each module.`

### 3. Expected Behavior

1. The agent detects frontend/backend/language/architecture partitions and loads only relevant references.
2. The agent lists candidates first and supports "all modules" scope.
3. The agent performs source-backed best-practice research before each module plan.
4. The agent runs tests before refactor and after each refactor slice.
5. The agent keeps going without optional confirmation when user says "do not stop".
6. The agent updates docs and reports final completion with evidence.

## Notes

1. This skill enforces process discipline, not business-logic redesign by default.
2. If no tests exist, the agent should establish a runnable test baseline first.
3. Hard blockers (missing credentials, broken environment, external outages) are the only valid pause points when user requires nonstop execution.

## Multilingual

<details>
<summary>中文（Chinese）</summary>

这是一个用于“覆盖率门禁重构”的 Codex Skill，适用于全项目、分模块、可验证的重构执行。

### 设计思路

1. 先拆超大文件，再处理次级模块。
2. 按业务边界拆分，不按行数硬切。
3. 每次重构必须有测试证据，先测后改，改后再测。
4. 模块级覆盖率目标 90%+（优先 statements/lines）。
5. 前端、后端、文档一体化推进。
6. 先识别前端/后端/语言/架构分区，再按需加载对应规则与最佳实践。
7. 用户说“不要停”时，必须连续执行到完成，除非硬阻塞。

### 使用方式

1. 按上方安装命令将 `SKILL.md`、`agents/openai.yaml` 和 `references/` 放到 `~/.codex/skills/coverage-gated-refactor/`。
2. 在任务中明确要求：
   - 先识别分区并按需加载
   - 再枚举重构候选
   - 指定“全部重构”或模块范围
   - 指定“不要停”
   - 指定覆盖率门禁（90%+）
3. 预期执行顺序：
   - 候选枚举
   - 基线测试
   - 模块测例补齐并达标
   - 分片重构与回归
   - 全量回归通过后完成

### 关键承诺

1. 有门禁才推进，无门禁不重构。
2. 有调研证据才推进（官方来源优先）。
3. 用户要求“不要停”时，不做可选确认中断。
4. 完成标准是“全部选中模块完成 + 历史测试全绿 + 文档同步”。

</details>
