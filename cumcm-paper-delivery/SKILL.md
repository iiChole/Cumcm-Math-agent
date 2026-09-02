---
name: cumcm-paper-delivery
description: 为 CUMCM 数学建模成果提供与题型无关的论文与工程交付，包括摘要、论文叙事、图表、LaTeX、编译检查、代码附件、页数检查和最终质量门；不负责选择题型建模方法。
---

# CUMCM Paper Delivery

本 Skill 接收已经建立的模型、结果和验证证据，将其整理为可读、可编译、可复现的竞赛论文工程。它独立于 A/B/C 题，可服务任何题型。

## 交付主线

1. 根据已验证的模型内容组织摘要、问题分析、模型章节、结果叙事和模型评价。
2. 用图表表达机理、变量关系、方案比较、阈值和验证结果，避免装饰性图表。
3. 按用户模板或官方模板生成 LaTeX 工程；没有模板时才使用本 Skill 的骨架。
4. 编译并检查日志、引用、公式溢出、字体、图表越界和页面结构。
5. 保证正文只使用验证后的数值和恰当的结论等级，并使代码、数据路径、随机种子和运行说明足以重现关键结果。
6. 交付前执行质量门，清理临时缓存和无关文件。

## 参考资料路由

- 论文结构和叙事：读取 [references/paper-structure.md](references/paper-structure.md)。
- 图表设计：第二阶段暂读旧资料 [references/visualization.md](../references/visualization.md)，后续迁入本 Skill。
- LaTeX 与 ZIP：第二阶段暂读旧资料 [references/latex-delivery.md](../references/latex-delivery.md)，后续迁入本 Skill。
- 最终检查：第二阶段暂读旧资料 [references/quality-gates.md](../references/quality-gates.md)，后续拆分后迁入本 Skill。

## 工程资源

- 默认模板第二阶段仍位于旧路径 `../assets/paper_skeleton.tex`；迁移完成后归档到本 Skill 的 `assets/`。
- 初始化和验证脚本第二阶段仍位于旧路径 `../scripts/`；迁移完成后归档到本 Skill 的 `scripts/`。

## 边界

本 Skill 不根据题号选择模型，不替代 `cumcm-modeling` 的证据盘点、算法选择、求解和数学验证。若关键简化缺少依据、最优性结论缺少对应验证、论文数值与验证后结果不一致，或论文内容存在其他模型缺陷，应返回建模阶段修正，而不是用写作或排版掩盖问题。
