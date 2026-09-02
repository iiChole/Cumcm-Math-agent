# 建模路由

路由顺序是“先确认问题结构，再选择方法”，不是“先按 A/B/C 题号分配算法”。题型只影响初始检查优先级，不能成为方法边界。

## 工作流参考

| 当前任务 | 读取 |
|---|---|
| 有题面、附件或外部资料 | [evidence-inventory.md](evidence-inventory.md) |
| 需要拆分多问并寻找主线 | [problem-decomposition.md](problem-decomposition.md) |
| 尚未形成可靠的基础模型 | [baseline-model.md](baseline-model.md) |
| 需要从理想到现实、特例到一般 | [model-progression.md](model-progression.md) |
| 需要决定具体求解方式 | [algorithm-selection.md](algorithm-selection.md) |
| 已经产生关键结论或数值结果 | [validation.md](validation.md) |
| 需要用代码复现结果 | [reproducibility.md](reproducibility.md) |

## 初始识别标签

- `mechanism`：守恒、物理过程、几何约束、微分方程。
- `geometry`：具有形状、尺寸、方向或边界的对象，以及覆盖、遮挡、碰撞、相交和可见性。
- `statistics`：抽样、分布、检验、置信区间和参数估计。
- `prediction`：回归、分类、时间序列和未知样本预测。
- `optimization`：成本/收益、资源配置、方案选择和风险决策。
- `continuous-optimization`：连续时间、空间或参数上的极值，以及非线性约束和低维可行流形。
- `multistage`：状态转移、序贯决策、动态规划或 MDP。
- `inverse`：由观测反演参数、隐变量或机理量。
- `numerical`：积分、求根、非线性最小二乘或大规模数值求解。
- `uncertainty`：误差传播、鲁棒性、风险边界和策略切换。

## 方法卡

按标签读取对应方法卡：

| 标签 | 方法卡 |
|---|---|
| `mechanism`、`geometry` | [methods/mechanism-geometry.md](methods/mechanism-geometry.md) |
| `statistics` | [methods/statistics-inference.md](methods/statistics-inference.md) |
| `optimization` | [methods/optimization-decision.md](methods/optimization-decision.md) |
| `continuous-optimization` | [methods/continuous-optimization.md](methods/continuous-optimization.md) |
| `discrete-optimization` | [methods/discrete-optimization.md](methods/discrete-optimization.md) |
| `multistage` | [methods/multistage-decision.md](methods/multistage-decision.md) |

题型弱先验：A 题可读取 [profiles/problem-a.md](profiles/problem-a.md)，B 题可读取 [profiles/problem-b.md](profiles/problem-b.md)。画像只提供初始检查方向、评分关注点和失分风险，不排除其他方法。

## 路由规则

1. 先按题面结构打标签，再读取对应方法资料。
2. 一个问题可以加载多个标签；不要因为 A/B/C 题号排除方法。
3. 题型画像只提供常见结构和失分点，不提供算法禁令。
4. 方法资料必须说明适用条件、不可滥用场景、验证要求和可组合方法。
5. 如果问题结构尚未明确，返回证据盘点和结构拆题，不要凭算法名称猜测模型。
6. 如果多个方法都可用，优先比较可解释性、可验证性、计算成本和误差来源。

## 组合示例

- “由观测估计物理参数后制定方案”：`mechanism + inverse + optimization + uncertainty`。
- “预测需求并安排多阶段库存”：`prediction + multistage + optimization`。
- “抽样估计质量并决定是否生产”：`statistics + optimization + uncertainty`。
- “空间覆盖并考虑测量误差”：`mechanism + geometry + continuous-optimization + numerical + uncertainty`。

没有专用方法卡的标签继续使用通用工作流参考；不要因为资料尚未拆分就改按题号选择方法。
