---
name: cumcm-problem
description: CUMCM 工作流兼容路由入口：按任务加载通用建模、B 题画像和论文交付 Skill。适用于需要统一进入本仓库能力的请求；不在此入口重复维护建模或排版正文。
---

# CUMCM 路由入口

这是仓库的兼容入口。先判断用户需要建模、论文交付，还是两者都需要，再加载对应 Skill；不要把 B 题经验机械套用于 A/C 题。

## 路由规则

- 完整建模、读题、证据盘点、模型建立、算法选择、求解、验证或可复现性：加载 [`cumcm-modeling`](cumcm-modeling/SKILL.md)。
- 题号明确为 B，或需要 B 题遗漏检查、评分关注点和常见失分点：在建模 Skill 基础上按需加载 [`problem-b` 画像](cumcm-modeling/references/profiles/problem-b.md)。画像只提供路由先验，不限制方法。
- 摘要、论文叙事、图表、LaTeX、编译、代码附件、页数检查、ZIP 或最终交付：加载 [`cumcm-paper-delivery`](cumcm-paper-delivery/SKILL.md)。
- 同时要求“解题并交付论文”：同时加载 `cumcm-modeling` 与 `cumcm-paper-delivery`；先完成并验证模型，再生成论文工程。

## 方法选择

方法按数学结构路由，而不是按题号路由。需要统计、优化、离散决策、多阶段决策、连续优化或机理几何方法时，读取 `cumcm-modeling/references/routing.md` 及其指向的方法卡。

## 兼容期说明

阶段 7 已完成逐项对比、行为验证和引用审计。新任务优先使用两个独立 Skill 的路径；旧论文正文、模板副本和脚本已删除，`COMPACT.md` 与 `REFACTOR_BASELINE.md` 仅作 B 题兼容和迁移追溯。
