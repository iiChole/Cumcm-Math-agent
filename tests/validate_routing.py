#!/usr/bin/env python3
"""Check the stage-8 routing contract and referenced skill resources."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "cumcm-modeling/SKILL.md",
    "cumcm-modeling/references/artifact-contract.md",
    "cumcm-modeling/scripts/validate_reports.py",
    "cumcm-modeling/references/routing.md",
    "cumcm-modeling/references/profiles/problem-b.md",
    "cumcm-modeling/references/methods/inverse-problems.md",
    "cumcm-modeling/references/methods/mechanism-geometry.md",
    "cumcm-modeling/references/methods/statistics-inference.md",
    "cumcm-modeling/references/methods/optimization-decision.md",
    "cumcm-modeling/references/methods/discrete-optimization.md",
    "cumcm-modeling/references/methods/multistage-decision.md",
    "cumcm-paper-delivery/SKILL.md",
    "cumcm-paper-delivery/references/abstract-and-narrative.md",
    "cumcm-paper-delivery/references/paper-structure.md",
    "cumcm-paper-delivery/references/latex-delivery.md",
    "cumcm-paper-delivery/references/quality-gates.md",
    "cumcm-paper-delivery/assets/paper-template/main.tex",
    "cumcm-paper-delivery/scripts/init_project.py",
    "cumcm-paper-delivery/scripts/validate_project.py",
]


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise SystemExit(f"FAIL: {label}: missing {needle!r}")


def main() -> int:
    missing = [p for p in REQUIRED_FILES if not (ROOT / p).is_file()]
    if missing:
        raise SystemExit("FAIL: missing routing resources: " + ", ".join(missing))

    root = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    modeling = (ROOT / "cumcm-modeling/SKILL.md").read_text(encoding="utf-8")
    routing = (ROOT / "cumcm-modeling/references/routing.md").read_text(encoding="utf-8")
    paper = (ROOT / "cumcm-paper-delivery/SKILL.md").read_text(encoding="utf-8")

    for needle in ("cumcm-modeling", "problem-b", "cumcm-paper-delivery"):
        require(root, needle, "root router")
    for needle in ("inverse", "mechanism", "geometry", "statistics", "optimization", "multistage", "discrete-optimization"):
        require(routing, needle, "modeling routing")
    require(root, "同时加载 `cumcm-modeling` 与 `cumcm-paper-delivery`", "hybrid route")
    require(modeling, "三个核心报告", "modeling artifact contract")
    require(modeling, "references/artifact-contract.md", "modeling artifact routing")
    require(paper, "本 Skill 聚焦论文叙事、工程结构、编译和交付质量", "paper scope")
    require(paper, "论文写作可以直接使用用户提供的模型", "paper input flexibility")
    require(paper, "references/quality-gates.md", "paper quality gate")

    print(f"PASS: {len(REQUIRED_FILES)} routing resources present")
    print("PASS: hybrid, pure-B, cross-type, and paper-only route contracts verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
