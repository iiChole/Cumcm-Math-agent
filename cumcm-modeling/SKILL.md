---
name: cumcm-modeling
description: 统一处理全国大学生数学建模竞赛 A、B、C 题的证据盘点、结构拆题、模型建立、算法选择、求解、验证与可复现性检查；按数学结构路由方法，不因题号限制算法。不要负责论文排版、LaTeX 编译或 ZIP 交付。
---

# CUMCM Modeling

这是所有 CUMCM 题型共用的建模 Skill。A/B/C 题标签只提供弱先验，不能作为方法边界；同一问题可以组合机理、统计、预测、优化、反演和数值方法。

## 工作主线

1. 盘点题面、附件、用户资料和来源等级，区分事实、假设与推断。
2. 按每一问识别输入、输出、未知量、决策变量、目标、约束和与前问的联系。
3. 先建立可解释的最小可行基础模型 M0，再根据失效证据或现实条件递进到修正模型。
4. 根据数学结构选择方法，而不是根据熟悉的算法反推模型；先化简，再求解。
5. 对关键结论进行至少两类验证，并保留独立于主求解链的交叉验证。
6. 固定随机种子、记录参数和数据路径，使关键结果可重现。

## 方法路由

先读取 [references/routing.md](references/routing.md)，再按当前任务选择参考资料，不要一次加载全部文件：

- 有赛题、附件、评分提示或外部资料时，读取 [references/evidence-inventory.md](references/evidence-inventory.md)。
- 分析完整赛题或多问关系时，读取 [references/problem-decomposition.md](references/problem-decomposition.md)。
- 建立首个可行模型时，读取 [references/baseline-model.md](references/baseline-model.md)。
- 放宽假设、处理现实因素或衔接后续问题时，读取 [references/model-progression.md](references/model-progression.md)。
- 选择或审查求解算法时，读取 [references/algorithm-selection.md](references/algorithm-selection.md)。
- 产生关键结果或审查可信度时，读取 [references/validation.md](references/validation.md)。
- 编写或审查计算代码时，读取 [references/reproducibility.md](references/reproducibility.md)。
- 涉及物理/几何对象、连续极值、抽样推断、成本收益、离散优化或多阶段决策时，读取 `references/routing.md` 指向的对应方法卡；不要按题号排除方法。
- 题号明确且需要完整解题或高风险复核时，可读取对应题型画像作为遗漏检查；画像不能覆盖题面结构。

## 建模硬约束

- 目标函数、约束、状态方程或联立条件必须完整；重要模型推导后集中汇总。
- 关键关系必须有可复核的推导；不能用最终公式代替对象定义、假设和中间依据。
- 精确归约要说明等价依据；近似要说明误差、收敛依据或适用范围，并在可计算时用完整模型或代表性小例交叉核验。
- 单位、边界、可辨识性和适用范围必须说明。
- 小规模问题不滥用启发式算法；高级算法必须有计算瓶颈或独立验证理由。
- 灵敏度分析不能只机械改变参数 ±5%，应寻找阈值、稳定区间或误差传播。
- 复杂模型需要基础模型失效的证据。

## 与论文交付的边界

本 Skill 输出模型、算法、数值结果和验证依据。需要摘要、图表、LaTeX、编译或最终交付时，另行加载 `cumcm-paper-delivery`。

## 建模终检五问

提交给论文交付模块前，应能清楚回答：为什么这样定义、为什么模型成立、为什么算法与结构匹配、模型何时失效且结果为何可信，以及最终实际应采取什么行动。若答案只能从代码或调试日志中猜测，建模尚未完成。
