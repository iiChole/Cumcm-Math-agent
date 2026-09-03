#!/usr/bin/env python3
"""Exercise modeling-report and paper-project contracts independently."""
from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
REPORT_VALIDATOR = ROOT / "cumcm-modeling" / "scripts" / "validate_reports.py"
PAPER_INIT = ROOT / "cumcm-paper-delivery" / "scripts" / "init_project.py"
PAPER_VALIDATOR = ROOT / "cumcm-paper-delivery" / "scripts" / "validate_project.py"
QUESTION_COUNT = 4


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def test_three_report_contract(temporary: Path) -> None:
    project = temporary / "modeling-project"
    reports = project / "reports"
    reports.mkdir(parents=True)
    (reports / "ANALYSIS_MODELING_REPORT.md").write_text(
        "# 分析与建模报告\n\n各问题的对象、变量、假设、完整推导、求解方案和代码接口。\n",
        encoding="utf-8",
    )
    (reports / "RESULTS_REPORT.md").write_text(
        "# 结果报告\n\n实际算法配置、收敛信息、最终数值、单位、精度和输出路径。\n",
        encoding="utf-8",
    )
    (reports / "VALIDATION_REPORT.md").write_text(
        "---\nstatus: pass\n---\n\n# 验证报告\n\n关键结论已经完成独立复核。\n",
        encoding="utf-8",
    )

    accepted = run(str(REPORT_VALIDATOR), str(project))
    require(accepted.returncode == 0, f"three core reports were rejected\n{accepted.stdout}")

    (reports / "RESULTS_REPORT.md").unlink()
    rejected = run(str(REPORT_VALIDATOR), str(project))
    require(rejected.returncode == 1, "missing core report was accepted")
    require("missing report" in rejected.stdout, "missing report was not explained")


def test_paper_contract(temporary: Path) -> None:
    project = temporary / "paper-project"
    initialized = run(str(PAPER_INIT), str(project), "--questions", str(QUESTION_COUNT))
    require(initialized.returncode == 0, f"paper initializer failed\n{initialized.stdout}")
    require(not (project / "reports").exists(), "paper initializer created modeling reports")
    require(not (project / "example.tex").exists(), "legacy flat paper entry was generated")

    expected = [
        "paper/main.tex",
        "paper/references.tex",
        "paper/sections/frontmatter.tex",
        "paper/sections/problem4.tex",
        "paper/sections/validation.tex",
        "paper/sections/evaluation.tex",
        "paper/sections/appendix.tex",
    ]
    for relative in expected:
        require((project / relative).exists(), f"paper initializer omitted {relative}")

    accepted = run(str(PAPER_VALIDATOR), str(project), "--questions", str(QUESTION_COUNT))
    require(accepted.returncode == 0, f"paper-only project was rejected\n{accepted.stdout}")

    main_tex = project / "paper" / "main.tex"
    original_main = main_tex.read_text(encoding="utf-8")
    main_tex.write_text(
        original_main.replace("\\input{sections/problem4}\n", ""),
        encoding="utf-8",
    )
    mismatched = run(str(PAPER_VALIDATOR), str(project), "--questions", str(QUESTION_COUNT))
    require(mismatched.returncode == 1, "question-count mismatch was accepted")
    require("question sections mismatch" in mismatched.stdout, "question-count mismatch was not explained")
    main_tex.write_text(original_main, encoding="utf-8")

    (project / "paper" / "sections" / "problem4.tex").unlink()
    rejected = run(str(PAPER_VALIDATOR), str(project), "--questions", str(QUESTION_COUNT))
    require(rejected.returncode == 1, "missing paper section was accepted")
    require("references missing file" in rejected.stdout, "missing paper section was not explained")


def test_single_file_template_contract(temporary: Path) -> None:
    template = temporary / "provided-template.tex"
    template.write_text(
        "\\documentclass{article}\n"
        "\\begin{document}\n"
        "\\begin{abstract}摘要。\\end{abstract}\n"
        "\\section{问题重述}\n"
        "\\section{问题一的模型建立与求解}\n"
        "\\section{问题二的模型建立与求解}\n"
        "\\section{模型检验与评价}\n"
        "\\end{document}\n",
        encoding="utf-8",
    )

    project = temporary / "single-file-project"
    initialized = run(str(PAPER_INIT), str(project), "--tex-template", str(template))
    require(initialized.returncode == 0, f"single-file initializer failed\n{initialized.stdout}")
    require(not (project / "paper" / "sections").exists(), "provided template was forcibly split")

    accepted = run(str(PAPER_VALIDATOR), str(project), "--questions", "2")
    require(accepted.returncode == 0, f"valid single-file template was rejected\n{accepted.stdout}")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="cumcm-contracts-") as directory:
        temporary = Path(directory)
        test_three_report_contract(temporary)
        test_paper_contract(temporary)
        test_single_file_template_contract(temporary)

    print("PASS: report, multi-file paper, and single-file paper contracts verified independently")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
