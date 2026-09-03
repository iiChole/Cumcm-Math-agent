# 阶段 8 行为验证

本文件记录真实请求式样、预期加载模块和验证结果。路由原则是“先识别题面结构，再按结构加载方法”；题号只提供弱先验。

## 用例 1：混合型题目

**请求**：B 题背景，但包含参数反演和几何约束；请建立模型并给出验证方案。

**应加载**：

- `cumcm-modeling/SKILL.md`
- `cumcm-modeling/references/profiles/problem-b.md`
- `cumcm-modeling/references/methods/inverse-problems.md`
- `cumcm-modeling/references/methods/mechanism-geometry.md`
- 按需要补充 `validation.md` 和 `reproducibility.md`

**不应发生**：因题号为 B 而排除反演或几何方法；只加载 `problem-b` 画像而不加载结构方法。

**结果**：通过。根入口将 B 画像定义为弱先验，路由表同时提供 `inverse` 和 `mechanism/geometry` 方法卡。

## 用例 2：纯 B 题

**请求**：有限总体抽样检验，结合成本收益和多阶段决策，给出可执行方案。

**应加载**：

- `cumcm-modeling/SKILL.md`
- `cumcm-modeling/references/profiles/problem-b.md`
- `methods/statistics-inference.md`
- `methods/optimization-decision.md`
- `methods/multistage-decision.md`

**结果**：通过。B 画像提供抽样、成本/收益和多阶段的初始检查方向，方法卡分别承载分布、目标和状态转移规则。

## 用例 3：非 B 题复用 B 题方法

**请求**：C 题中的整数优化或鲁棒决策问题，复用仓库中成熟的离散优化方法。

**应加载**：

- `cumcm-modeling/SKILL.md`
- `methods/discrete-optimization.md`
- 视目标函数补充 `methods/optimization-decision.md` 和 `validation.md`

**不应发生**：自动加载 `problem-b` 画像作为前置条件，或因题号为 C 而禁止离散优化。

**结果**：通过。路由按 `discrete-optimization`/`optimization` 标签选择方法，题型画像不是必需依赖。

## 用例 4：只写论文

**请求**：已有验证后的模型和结果，只生成 LaTeX 论文并完成交付检查。

**应加载**：

- `cumcm-paper-delivery/SKILL.md`
- 按任务读取 `references/abstract-and-narrative.md`、`paper-structure.md`、`latex-delivery.md`、`quality-gates.md`

**不应发生**：为排版任务加载 B 题画像或要求重新选择建模算法；若发现模型数值不一致，应返回建模阶段而不是自行改模型。

**结果**：通过。论文 Skill 明确负责摘要、论文、图表、LaTeX 和质量门，边界中排除题型建模选择。

## 总体验收

- [x] 混合型题目可同时加载题型画像和跨题型方法。
- [x] 纯 B 题保留抽样、成本收益、多阶段决策能力。
- [x] 非 B 题可以复用离散优化和决策方法。
- [x] 只写论文可以只加载 `cumcm-paper-delivery`。
