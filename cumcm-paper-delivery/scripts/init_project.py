#!/usr/bin/env python3
"""Create a reproducible CUMCM paper workspace."""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = ROOT / "assets" / "paper-template"

GITIGNORE = """*.fls
*.fdb_latexmk
*.xdv
*.toc
*.bbl
*.blg
*.aux
*.log
*.out
*.synctex.gz
__pycache__/
*.pyc
.DS_Store
"""

CODE_README = """# code\n\n按实际问题或功能拆分脚本，例如 `q1_*.py`、`q2_*.py` 和 `plot_*.py`。\n\n运行时固定随机种子，并输出正文中的关键结果；在此记录依赖、输入路径和运行顺序。\n"""


def positive_int(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("questions must be at least 1")
    return number


def chinese_number(number: int) -> str:
    digits = "零一二三四五六七八九"
    if number < 10:
        return digits[number]
    if number < 20:
        return "十" + (digits[number % 10] if number % 10 else "")
    if number < 100:
        return digits[number // 10] + "十" + (digits[number % 10] if number % 10 else "")
    return str(number)


def copy_if_missing(source: Path, destination: Path) -> None:
    if not destination.exists():
        shutil.copy2(source, destination)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", help="paper workspace root")
    parser.add_argument("--questions", type=positive_int, help="number of top-level questions; required for the default template")
    parser.add_argument("--tex-template", help="optional user-provided main.tex to preserve")
    parser.add_argument("--cls", help="optional user-provided cumcmthesis.cls to preserve")
    args = parser.parse_args()

    out = Path(args.output).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    for directory in ("figures", "results", "code", "paper"):
        (out / directory).mkdir(parents=True, exist_ok=True)

    paper = out / "paper"

    if args.tex_template:
        tex_source = Path(args.tex_template).expanduser().resolve()
        copy_if_missing(tex_source, paper / "main.tex")
    else:
        if args.questions is None:
            parser.error("--questions is required when using the default template")

        sections = paper / "sections"
        sections.mkdir(parents=True, exist_ok=True)

        if not (paper / "main.tex").exists():
            main_text = (TEMPLATE_ROOT / "main.tex").read_text(encoding="utf-8")
            problem_inputs = "\n".join(
                f"\\input{{sections/problem{number}}}"
                for number in range(1, args.questions + 1)
            )
            main_text = main_text.replace("{{PROBLEM_INPUTS}}", problem_inputs)
            (paper / "main.tex").write_text(main_text, encoding="utf-8")

        for name in ("frontmatter.tex", "validation.tex", "evaluation.tex", "appendix.tex"):
            copy_if_missing(TEMPLATE_ROOT / "sections" / name, sections / name)

        problem_template = (TEMPLATE_ROOT / "problem-section.tex.tpl").read_text(encoding="utf-8")
        for number in range(1, args.questions + 1):
            destination = sections / f"problem{number}.tex"
            if not destination.exists():
                content = problem_template.replace("{{PROBLEM_CN}}", chinese_number(number))
                destination.write_text(content, encoding="utf-8")

    copy_if_missing(TEMPLATE_ROOT / "references.tex", paper / "references.tex")

    class_source = Path(args.cls).expanduser().resolve() if args.cls else (ROOT / "assets" / "cumcmthesis.cls")
    class_destination = paper / "cumcmthesis.cls"
    if class_source.is_file():
        copy_if_missing(class_source, class_destination)

    gitignore = out / ".gitignore"
    if not gitignore.exists():
        gitignore.write_text(GITIGNORE, encoding="utf-8")

    code_readme = out / "code" / "README.md"
    if not code_readme.exists():
        code_readme.write_text(CODE_README, encoding="utf-8")

    if args.tex_template:
        print(f"Created CUMCM paper workspace from the provided template: {out}")
    else:
        print(f"Created CUMCM paper workspace for {args.questions} top-level questions: {out}")
    print(f"Paper entry: {paper / 'main.tex'}")
    if not class_destination.exists():
        print("Note: cumcmthesis.cls was not provided; copy the user's or official class before compiling.")


if __name__ == "__main__":
    main()
