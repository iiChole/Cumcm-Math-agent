# CUMCM Skills

本仓库采用“统一建模能力 + 独立论文交付”的架构。题号 A/B/C 只作为弱先验，不限制方法调用。

## Skills

### `cumcm-modeling`

负责 CUMCM A、B、C 题的证据盘点、结构拆题、基础模型 M0、方法路由、模型递进、求解、独立验证与可复现性检查。完整任务生成三个核心报告：`ANALYSIS_MODELING_REPORT.md`、`RESULTS_REPORT.md` 和 `VALIDATION_REPORT.md`。

### `cumcm-paper-delivery`

负责与题型无关的摘要、论文叙事、图表、LaTeX 工程、编译检查、代码附件和最终质量门。完整长论文默认按顶层问题拆分到 `paper/sections/`；已有模板可以保持原有文件组织，并可直接使用用户提供的已验证材料。

## 推荐组合

```text
完整解题：cumcm-modeling + cumcm-paper-delivery
只做建模：cumcm-modeling
只做论文或 LaTeX：cumcm-paper-delivery
```

## 建模报告检查

```bash
python cumcm-modeling/scripts/validate_reports.py <项目目录>
```

## 论文工程初始化与检查

例如为四问赛题创建论文工程：

```bash
python cumcm-paper-delivery/scripts/init_project.py <项目目录> --questions 4
python cumcm-paper-delivery/scripts/validate_project.py <项目目录> --questions 4 --compile
```

论文检查覆盖内容结构、`\input{}` 引用、编译日志、PDF 页面和代码附件，并兼容单文件与多文件工程。建模报告与论文工程分别检查，行为测试见 `tests/validate_artifacts.py`。
