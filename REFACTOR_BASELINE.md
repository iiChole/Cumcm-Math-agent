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
| `references/workflow.md` | B 题端到端工作流 | `cumcm-modeling/references/` | 提取通用流程 |
| `references/model-selection.md` | 模型与算法选择 | `cumcm-modeling/references/methods/`、B 题画像 | 通用选型上移，B 题案例保留 |
| `references/expert-rubric-guidance.md` | B 题专家讲评与评分偏好 | `cumcm-modeling/references/profiles/problem-b.md` | 保留为弱先验 |
| `references/paper-writing.md` | 论文结构、叙事、摘要、附录 | `cumcm-paper-delivery/references/` | 拆分论文结构与叙事 |
| `references/visualization.md` | 图表与视觉规范 | `cumcm-paper-delivery/references/` | 原文迁移 |
| `references/latex-delivery.md` | LaTeX、编译、ZIP 交付 | `cumcm-paper-delivery/references/` | 原文迁移并修复路径问题 |
| `references/quality-gates.md` | 数学、验证、摘要、排版终检 | Core 与 Delivery | 按检查对象拆分 |
| 原 `assets/paper_skeleton.tex` | 默认论文模板 | `cumcm-paper-delivery/assets/paper-template/` | 对应当前多文件模板资源 |
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

以下内容已复制并泛化到 `cumcm-modeling/references/`，阶段 7 审计后旧正文已删除：

| 原知识单元 | 新文件 | 状态 |
|---|---|---|
| 来源优先级、事实—假设—推断 | `evidence-inventory.md` | 已复制并跨题型泛化 |
| 每问要素、主线识别、后续问题预判 | `problem-decomposition.md` | 已复制并跨题型泛化 |
| 最小可行模型 M0、结构化简、集中模型块 | `baseline-model.md` | 已复制并跨题型泛化 |
| 现实修正、M0→M1 触发条件、创新优先级 | `model-progression.md` | 已复制并跨题型泛化 |
| 算法选型优先级和高级算法边界 | `algorithm-selection.md` | 已复制并跨题型泛化 |
| 理论/数值/数据验证和真实灵敏度分析 | `validation.md` | 已复制并跨题型泛化 |
| 数据、代码、参数和结果追踪 | `reproducibility.md` | 已复制并跨题型泛化 |

B 题专属抽样、生产决策、多阶段决策及评分偏好已在第四阶段整理为跨题型方法卡与 B 题弱先验画像；原重复正文已在阶段 7 审计后删除。

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
| 图表、Overview 图、配色与表格 | `cumcm-paper-delivery/references/visualization.md` | 已迁移，旧正文已删除 |
| LaTeX 模板优先级、编译、工程结构、ZIP | `cumcm-paper-delivery/references/latex-delivery.md` | 已迁移并修复资源路径，旧正文已删除 |
| 论文终检 | `cumcm-paper-delivery/references/quality-gates.md` | 已迁移为交付范围清单，旧正文已删除 |
| 默认模板与类文件 | `cumcm-paper-delivery/assets/paper-template/`、`cumcm-paper-delivery/assets/cumcmthesis.cls` | 当前采用分章节模板 |
| 工程初始化与验证 | `cumcm-paper-delivery/scripts/init_project.py`、`cumcm-paper-delivery/scripts/validate_project.py` | 已迁移并改为题型无关，旧脚本已删除 |

## 第六阶段迁移记录

| 入口 | 状态 |
|---|---|
| 根目录 `SKILL.md` | 已改为兼容路由，仅负责在 `cumcm-modeling`、B 题画像和 `cumcm-paper-delivery` 之间分流 |
| 根目录 `agents/openai.yaml` | 已更新为 CUMCM Skills Router 元数据 |
| 旧论文 `references/`、`assets/`、`scripts/` | 已完成引用审计并删除重复正文；`COMPACT.md` 和本台账保留作兼容/追溯 |

## 第七阶段审计记录

| 检查项 | 结果 | 证据 |
|---|---|---|
| 旧文件逐项归属 | 通过 | 本表“后续归属”与第三至第五阶段迁移表已覆盖旧 `references/`、`assets/`、`scripts/` |
| 原公式与规则保留 | 通过 | 建模硬约束、M0/递进/验证规则在 `cumcm-modeling`；摘要、图表、LaTeX 和交付规则在 `cumcm-paper-delivery`；B 题专属经验在 `profiles/problem-b.md` |
| 旧引用审计 | 通过 | 新入口与 Skill 不再引用已删除旧路径；仅本台账保留历史文件名用于追溯 |
| 新 Skill 独立加载 | 通过 | 两个 Skill 均有独立 `SKILL.md`、`agents/openai.yaml`；论文 Skill 的资源和脚本均使用自身相对路径 |
| 重复正文清理 | 通过 | 复制、对比、验证完成后删除旧论文参考资料、模板副本和初始化/验证脚本；`COMPACT.md` 非重复正文，继续保留 |
| 变更可恢复 | 通过 | 删除发生在 Git 工作树中，可通过阶段 1 标签 `pre-refactor-cumcm-b` 恢复旧版本 |

### 旧章节 → 新模块映射

| 原文件/章节 | 新模块 | 原规则是否保留 | 泛化处理 |
|---|---|---|---|
| `workflow.md`：赛题输入检查 | `cumcm-modeling/references/evidence-inventory.md` | 保留来源优先级、数据质量和事实/假设区分 | 从 B 题扩展到 A/B/C |
| `workflow.md`：结构拆题与主线 | `problem-decomposition.md` | 保留每问要素、主线和后续问题预判 | 去除固定四问假设 |
| `workflow.md`：M0 与先化简再求解 | `baseline-model.md` | 保留定义、假设、适用条件、集中模型块和结构化简 | 改为所有数学结构适用 |
| `workflow.md`：求解、验证、现实修正 | `algorithm-selection.md`、`validation.md`、`model-progression.md` | 保留算法适配、独立验证和复杂化触发条件 | 按任务阶段拆分维护 |
| `workflow.md`：论文同步写作与成稿 | `cumcm-paper-delivery/references/` | 保留模型章节、图表、摘要和终检要求 | 从建模 Skill 下沉到独立交付 Skill |
| `model-selection.md`：选择原则与高级算法边界 | `algorithm-selection.md` | 保留问题结构优先、精确方法优先和启发式禁令 | 跨题型泛化 |
| `model-selection.md`：高频结构与方法 | `routing.md` 与 `methods/*.md` | 保留统计、几何、反演、优化、决策和数值方法边界 | 由按题号改为按数学结构路由 |
| `model-selection.md`：创新优先级 | `model-progression.md` | 保留关键量重定义、化简、推广、不确定性和阈值 | 跨题型泛化 |
| `model-selection.md`：常见错误 | 各方法卡、`validation.md` | 保留相关不等于因果、正态近似、目标遗漏、±5% 灵敏度、滥用 GA/PSO、只报 R² 等禁令 | 下沉到最相关的方法与验证模块 |
| `expert-rubric-guidance.md`：2021–2025 经验 | `profiles/problem-b.md` | 保留数据统计、几何定位、空间覆盖、生产决策和机理反演检查项 | 作为弱先验，不绑定年份方法 |
| `expert-rubric-guidance.md`：评分偏好与使用方式 | `profiles/problem-b.md` | 保留可执行方案、统一指标、化简、一般化、不确定性决策和遗漏检查 | 不作为强制评分模板 |
| `paper-writing.md`：总体结构 | `paper-structure.md` | 保留默认章节骨架 | 服从用户/官方模板，不预设固定问数 |
| `paper-writing.md`：摘要 | `abstract-and-narrative.md` | 保留首段、分问动机—方法—结果—验证、首页和关键词规则 | 从 B 题扩展到所有题型 |
| `paper-writing.md`：问题重述、分析、假设、符号 | `paper-structure.md`、`abstract-and-narrative.md` | 保留背景/要求、逐问分析、逐条假设和符号单位表 | 去除固定四问标题要求 |
| `paper-writing.md`：模型建立与求解 | `paper-structure.md`、`abstract-and-narrative.md` | 保留动机、定义、推导、模型汇总、求解、结果、验证节奏 | 与建模正确性边界分离 |
| `paper-writing.md`：结果、评价、附录、句法 | `abstract-and-narrative.md` | 保留现象—原因—意义、缺陷—影响—改进、代码附录和因果句法 | 题型无关 |
| `visualization.md`：设计原则与 Overview | `cumcm-paper-delivery/references/visualization.md` | 保留图表问题导向、问题/模型/信息三层和反馈结构 | 不固定四问 |
| `visualization.md`：图形、创意表达、配色、表格 | 同上 | 保留图形映射、策略相图、多层对比、路径信息、低饱和配色和总结表 | 题型无关 |
| `latex-delivery.md`：模板、工程、编译、日志、页面、代码、ZIP | `cumcm-paper-delivery/references/latex-delivery.md` | 保留全部交付规则 | 路径改为论文 Skill 内部相对路径 |
| `quality-gates.md`：数学、递进、算法、验证 | `cumcm-modeling` 的基础模型、递进、算法和验证资料 | 保留全部建模门禁 | 从论文终检拆回建模质量层 |
| `quality-gates.md`：摘要、图表、页面、可复现 | `cumcm-paper-delivery/references/quality-gates.md` | 保留全部交付门禁 | 与建模正确性检查解耦 |
| 原 `assets/paper_skeleton.tex`、`cumcmthesis.cls` | `cumcm-paper-delivery/assets/paper-template/` 与 `assets/cumcmthesis.cls` | 提供多文件模板与类文件 | 题号和问题数量由当前任务确定 |
| `scripts/init_project.py`、`validate_project.py` | `cumcm-paper-delivery/scripts/` | 保留初始化和验证行为 | 修复资源根路径并改为题型无关 |
| `COMPACT.md` 各硬约束 | `cumcm-modeling`、`cumcm-paper-delivery`、`profiles/problem-b.md` | 规则已迁入；原文件暂留作兼容与追溯 | 不再作为全局单一入口 |

## 第八阶段行为验证记录

行为用例和可执行契约检查位于 [`tests/behavior-routing.md`](tests/behavior-routing.md) 与 [`tests/validate_routing.py`](tests/validate_routing.py)。四类请求均已覆盖：

| 用例 | 预期行为 | 结果 |
|---|---|---|
| B 题背景 + 参数反演 + 几何约束 | 同时加载 B 画像、`inverse` 和 `mechanism/geometry` | 通过 |
| 纯 B 题抽样 + 成本收益 + 多阶段 | 保留 B 题先验，并加载 statistics/optimization/multistage 方法卡 | 通过 |
| C 题整数优化/鲁棒决策 | 不依赖 B 画像，直接复用 discrete/optimization 方法 | 通过 |
| 只写论文与 LaTeX 交付 | 只加载 `cumcm-paper-delivery` 及其交付参考 | 通过 |

自动契约测试检查根路由、方法标签、边界声明和所有必要资源存在性；它不替代真实赛题上的数学正确性验证。
