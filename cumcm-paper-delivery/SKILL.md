---
name: cumcm-paper-delivery
description: 为 CUMCM 数学建模成果提供与题型无关的论文与工程交付，包括摘要、论文叙事、图表、LaTeX 工程组织、编译检查、代码附件、页数检查和最终质量门。
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

## 必须产出

完整论文交付必须包含可编译的论文入口、参考文献、所需类文件与全部正文源文件。内容上应具备摘要、问题重述与分析、假设与符号、各问模型建立与求解、验证、模型评价和必要附录；源文件组织服从用户或官方模板。

没有指定模板时，根据论文规模和修改方式选择结构：完整长论文、反复迭代或协作编辑默认使用 `paper/sections/`，并至少按顶层问题拆分；短篇、一次性交付或已有单文件模板可以保留单文件。多文件工程使用稳定语义文件名，具体选择标准与默认布局见 [references/paper-structure.md](references/paper-structure.md)。

论文写作可以直接使用用户提供的模型、结果、代码、表格或其他已验证材料。每项关键数值和结论应标明可追溯来源；来源之间存在矛盾时，先澄清或修正来源再继续写作。

## 参考资料路由

按任务读取必要资料，不要一次加载全部文件：

- 论文结构与模型章节边界：读取 [references/paper-structure.md](references/paper-structure.md)。
- 摘要、问题分析、结果叙事和模型评价：读取 [references/abstract-and-narrative.md](references/abstract-and-narrative.md)。
- 图表与 overview 图：读取 [references/visualization.md](references/visualization.md)。
- LaTeX 工程、编译、代码附件与 ZIP：读取 [references/latex-delivery.md](references/latex-delivery.md)。
- 交付前终检：读取 [references/quality-gates.md](references/quality-gates.md)。

## 工程资源

- 默认的中等粒度多文件模板位于 `assets/paper-template/`；用户提供的模板和 `.cls` 优先级更高。
- 使用 `scripts/init_project.py` 创建工程，用 `scripts/validate_project.py` 做结构、编译和基础交付检查。

## 边界

本 Skill 聚焦论文叙事、工程结构、编译和交付质量。若关键简化缺少依据、最优性结论缺少对应验证、论文数值与来源不一致，或论文内容存在其他模型缺陷，应返回相应来源修正，再继续组织论文。
