---
name: cumcm-problem
description: CUMCM 工作流路由入口：按任务加载通用建模、B 题画像和论文交付 Skill，支持独立建模、独立论文交付和完整竞赛流程。
---

# CUMCM 路由入口

先判断用户需要建模、论文交付，还是两者都需要，再加载对应 Skill；B 题画像只作为弱先验，方法仍由题目的数学结构决定。

## 路由规则

- 完整建模、读题、证据盘点、模型建立、算法选择、求解、验证或可复现性：加载 [`cumcm-modeling`](cumcm-modeling/SKILL.md)。
- 题号明确为 B，或需要 B 题遗漏检查、评分关注点和常见失分点：在建模 Skill 基础上按需加载 [`problem-b` 画像](cumcm-modeling/references/profiles/problem-b.md)。画像只提供路由先验，不限制方法。
- 摘要、论文叙事、图表、LaTeX、编译、代码附件、页数检查、ZIP 或最终交付：加载 [`cumcm-paper-delivery`](cumcm-paper-delivery/SKILL.md)。
- 同时要求“解题并交付论文”：同时加载 `cumcm-modeling` 与 `cumcm-paper-delivery`；先完成并验证模型，再生成论文工程。

## 方法选择

方法按数学结构路由，而不是按题号路由。需要统计、优化、离散决策、多阶段决策、连续优化或机理几何方法时，读取 `cumcm-modeling/references/routing.md` 及其指向的方法卡。

## 使用约定

- 完整建模任务由 `cumcm-modeling` 生成 `ANALYSIS_MODELING_REPORT.md`、`RESULTS_REPORT.md` 和 `VALIDATION_REPORT.md`。
- 论文任务由 `cumcm-paper-delivery` 生成可编译的 `paper/` 工程；完整长论文默认按顶层问题拆分，已有模板保持其文件组织。输入可以是建模报告，也可以是用户提供的其他已验证材料。
- 完整竞赛流程依次完成建模验证与论文交付，两部分分别执行各自的质量检查。
