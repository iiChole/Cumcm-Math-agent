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

当前已完成第四至第七阶段：通用建模工作流、跨题型方法卡、B 题弱先验画像、独立论文交付模块和根目录兼容路由已建立；重复的旧论文正文、模板副本和脚本已在引用审计后删除。`COMPACT.md` 与迁移台账仍保留用于兼容和追溯。迁移台账见 [REFACTOR_BASELINE.md](REFACTOR_BASELINE.md)。
