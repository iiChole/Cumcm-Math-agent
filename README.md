# CUMCM Skills

本仓库采用“统一建模能力 + 独立论文交付”的架构。题号 A/B/C 只作为弱先验，不限制方法调用。

## Skills

### `cumcm-modeling`

负责 CUMCM A、B、C 题的证据盘点、结构拆题、基础模型 M0、方法路由、模型递进、求解、独立验证与可复现性检查。方法按数学结构组织，后续将把现有 B 题 Skill 的通用能力和可复用方法迁入此处。

### `cumcm-paper-delivery`

负责与题型无关的摘要、论文叙事、图表、LaTeX 工程、编译检查、代码附件和最终质量门。

## 推荐组合

```text
完整解题：cumcm-modeling + cumcm-paper-delivery
只做建模：cumcm-modeling
只做论文或 LaTeX：cumcm-paper-delivery
```

## 重构状态

当前处于第四阶段：通用建模工作流已完成抽取，B 题中的统计推断、决策优化、离散优化和多阶段决策已整理为跨题型方法卡，同时建立了 B 题弱先验画像。原 B 题内容仍保留在旧目录，尚未删除。迁移台账见 [REFACTOR_BASELINE.md](REFACTOR_BASELINE.md)。
