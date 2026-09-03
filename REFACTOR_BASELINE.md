# CUMCM Skills 重构基线

本文件记录重构开始前的内容归属和恢复点。第一阶段只冻结现状，不迁移或删除知识内容。

## Git 恢复点

- `pre-refactor-cumcm-b`：远端 `main` 提交 `b548b38` 的基线。
- `pre-refactor-cumcm-b-worktree`：包含重构前本地未提交修改的工作树快照。
- 未提交差异另存于：`/tmp/cumcm-pre-refactor-working-tree.patch`。

## 重构前文件清单

| 文件 | 当前职责 | 后续归属 | 迁移策略 |
|---|---|---|---|
| `SKILL.md` | B 题 Skill 总入口、通用工作流、B 题方法、论文交付 | `cumcm-modeling/SKILL.md`、`cumcm-b` 题型画像、`cumcm-paper-delivery/SKILL.md` | 按知识单元拆分，保留原规则 |
| `COMPACT.md` | B 题常驻硬约束 | Core 与 Delivery 的约束分片 | 不直接作为全局硬约束 |
| `references/workflow.md` | B 题端到端工作流 | `cumcm-core/references/` | 提取通用流程 |
| `references/model-selection.md` | 模型与算法选择 | `cumcm-core/references/methods/`、`cumcm-b` | 通用选型上移，B 题案例保留 |
| `references/expert-rubric-guidance.md` | B 题专家讲评与评分偏好 | `cumcm-modeling/references/profiles/problem-b.md` | 保留为弱先验 |
| `references/paper-writing.md` | 论文结构、叙事、摘要、附录 | `cumcm-paper-delivery/references/` | 拆分论文结构与叙事 |
| `references/visualization.md` | 图表与视觉规范 | `cumcm-paper-delivery/references/` | 原文迁移 |
| `references/latex-delivery.md` | LaTeX、编译、ZIP 交付 | `cumcm-paper-delivery/references/` | 原文迁移并修复路径问题 |
| `references/quality-gates.md` | 数学、验证、摘要、排版终检 | Core 与 Delivery | 按检查对象拆分 |
| `assets/paper_skeleton.tex` | 默认论文模板 | `cumcm-paper-delivery/assets/` | 与写作规范对齐后迁移 |
| `assets/cumcmthesis.cls` | 本地 LaTeX 类文件 | `cumcm-paper-delivery/assets/` 或保留为用户模板 | 先确认是否纳入发布包 |
| `scripts/init_project.py` | 初始化论文工程 | `cumcm-paper-delivery/scripts/` | 修正资源路径后迁移 |
| `scripts/validate_project.py` | 论文工程验证 | `cumcm-paper-delivery/scripts/` | 修复工作目录、页数和代码检测 |
| `agents/openai.yaml` | B 题 Skill UI 元数据 | 各新 Skill 的独立元数据 | 按 Skill 重写 |

## 迁移原则

1. 先复制、对比、验证，再删除旧文件。
2. 题型画像提供路由先验，不限制方法调用。
3. 原有公式、算法适用条件、验证底线和常见陷阱不得无依据删减。
4. 论文规范与数学建模规范分开维护。

## 第三阶段迁移记录

以下内容已复制并泛化到 `cumcm-modeling/references/`，旧文件仍保留：

| 原知识单元 | 新文件 | 状态 |
|---|---|---|
| 来源优先级、事实—假设—推断 | `evidence-inventory.md` | 已复制并跨题型泛化 |
| 每问要素、主线识别、后续问题预判 | `problem-decomposition.md` | 已复制并跨题型泛化 |
| 最小可行模型 M0、结构化简、集中模型块 | `baseline-model.md` | 已复制并跨题型泛化 |
| 现实修正、M0→M1 触发条件、创新优先级 | `model-progression.md` | 已复制并跨题型泛化 |
| 算法选型优先级和高级算法边界 | `algorithm-selection.md` | 已复制并跨题型泛化 |
| 理论/数值/数据验证和真实灵敏度分析 | `validation.md` | 已复制并跨题型泛化 |
| 数据、代码、参数和结果追踪 | `reproducibility.md` | 已复制并跨题型泛化 |

B 题专属抽样、生产决策、多阶段决策及评分偏好已在第四阶段整理为跨题型方法卡与 B 题弱先验画像；旧文件仍保留，待后续逐项对比后再决定是否删除。

## 第四阶段迁移记录

| 原知识单元 | 新文件 | 状态 |
|---|---|---|
| 有限总体抽检、二项/超几何、精确检验、OC 曲线 | `cumcm-modeling/references/methods/statistics-inference.md` | 已提取并泛化 |
| 期望成本/收益、统一决策指标、不确定性决策 | `cumcm-modeling/references/methods/optimization-decision.md` | 已提取并泛化 |
| 枚举、支配剪枝、结构化降复杂度 | `cumcm-modeling/references/methods/discrete-optimization.md` | 已提取并泛化 |
| 动态规划、MDP、状态转移和序贯决策 | `cumcm-modeling/references/methods/multistage-decision.md` | 已提取并泛化 |
| B 题常见结构、评分关注点、不可机械套用边界 | `cumcm-modeling/references/profiles/problem-b.md` | 已建立弱先验画像 |

## 第五阶段迁移记录

| 原知识单元 | 新文件 | 状态 |
|---|---|---|
| 论文结构、模型章节边界、代码附录 | `cumcm-paper-delivery/references/paper-structure.md` | 已迁移并改为题型无关 |
| 摘要、问题分析、结果叙事、模型评价 | `cumcm-paper-delivery/references/abstract-and-narrative.md` | 已从 `paper-writing.md` 拆分迁移 |
| 图表、Overview 图、配色与表格 | `cumcm-paper-delivery/references/visualization.md` | 已迁移 |
| LaTeX 模板优先级、编译、工程结构、ZIP | `cumcm-paper-delivery/references/latex-delivery.md` | 已迁移并修复资源路径 |
| 论文终检 | `cumcm-paper-delivery/references/quality-gates.md` | 已迁移为交付范围清单 |
| 默认模板与类文件 | `cumcm-paper-delivery/assets/paper_skeleton.tex`、`cumcm-paper-delivery/assets/cumcmthesis.cls` | 已复制，旧资源保留 |
| 工程初始化与验证 | `cumcm-paper-delivery/scripts/init_project.py`、`cumcm-paper-delivery/scripts/validate_project.py` | 已复制并改为题型无关 |

## 第六阶段迁移记录

| 入口 | 状态 |
|---|---|
| 根目录 `SKILL.md` | 已改为兼容路由，仅负责在 `cumcm-modeling`、B 题画像和 `cumcm-paper-delivery` 之间分流 |
| 根目录 `agents/openai.yaml` | 已更新为 CUMCM Skills Router 元数据 |
| 旧 `references/`、`assets/`、`scripts/` | 兼容期继续保留，待行为验证与引用审计后清理 |
