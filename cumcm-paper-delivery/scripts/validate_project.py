#!/usr/bin/env python3
"""Validate a CUMCM paper workspace without imposing one source layout."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys


REQUIRED_DIRS = ["figures", "code", "paper"]
REQUIRED_FILES = [".gitignore", "paper/main.tex", "paper/references.tex"]
LOG_PATTERNS = [
    (r"Overfull \\hbox", "Overfull hbox"),
    (r"Undefined control sequence", "Undefined control sequence"),
    (r"There were undefined references", "Undefined references"),
    (r"Citation .* undefined", "Undefined citation"),
]
TEMPLATE_MARKER = re.compile(r"\{\{[^}]+\}\}")


def positive_int(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("questions must be at least 1")
    return number


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def normalize_input(value: str) -> str:
    normalized = value.strip().replace("\\", "/")
    return normalized[:-4] if normalized.endswith(".tex") else normalized


def active_tex(source_text: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", line) for line in source_text.splitlines())


def tex_dependencies(source_text: str) -> list[str]:
    return [
        normalize_input(value)
        for value in re.findall(r"\\(?:input|include)\s*\{([^}]+)\}", active_tex(source_text))
    ]


def collect_tex_sources(paper: Path, main_tex: Path, errors: list[str]) -> tuple[set[Path], list[str]]:
    paper_root = paper.resolve()
    pending = [main_tex]
    sources: set[Path] = set()
    dependencies: list[str] = []

    while pending:
        source = pending.pop()
        resolved_source = source.resolve()
        if resolved_source in sources or not source.is_file():
            continue
        sources.add(resolved_source)

        source_text = source.read_text(encoding="utf-8", errors="ignore")
        relative_source = source.relative_to(paper).as_posix()
        if TEMPLATE_MARKER.search(active_tex(source_text)):
            errors.append(f"paper/{relative_source} contains an unresolved template marker")

        for value in tex_dependencies(source_text):
            dependencies.append(value)
            dependency = (paper / f"{value}.tex").resolve()
            try:
                dependency.relative_to(paper_root)
            except ValueError:
                errors.append(f"paper/{relative_source} references a file outside paper/: {value}.tex")
                continue
            if not dependency.is_file():
                errors.append(f"paper/{relative_source} references missing file: paper/{value}.tex")
                continue
            pending.append(dependency)

    return sources, dependencies


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="paper workspace root")
    parser.add_argument("--questions", type=positive_int, help="expected top-level question count; inferred from paper inputs if omitted")
    parser.add_argument("--min-pages", type=int, default=20, help="preferred body minimum (whole-file fallback)")
    parser.add_argument("--max-pages", type=int, default=24, help="preferred body maximum (whole-file fallback)")
    parser.add_argument("--compile", action="store_true", help="run XeLaTeX twice in paper/ before checks")
    args = parser.parse_args()

    root = Path(args.project).expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        print(f"ERROR: project not found: {root}")
        return 2

    for directory in REQUIRED_DIRS:
        if not (root / directory).is_dir():
            errors.append(f"missing directory: {directory}/")
    for filename in REQUIRED_FILES:
        if not (root / filename).is_file():
            errors.append(f"missing file: {filename}")

    paper = root / "paper"
    main_tex = paper / "main.tex"
    dependencies: list[str] = []
    tex_sources: set[Path] = set()
    if main_tex.is_file():
        tex_sources, dependencies = collect_tex_sources(paper, main_tex, errors)

    paper_questions: dict[int, str] = {}
    for value in dependencies:
        match = re.fullmatch(r"(?:sections/)?problem(\d+)", value)
        if match:
            paper_questions[int(match.group(1))] = value

    actual_questions = set(paper_questions)
    if args.questions is not None and actual_questions:
        expected_questions = set(range(1, args.questions + 1))
        if actual_questions != expected_questions:
            errors.append(
                "paper question sections mismatch: "
                f"expected {sorted(expected_questions)}, found {sorted(actual_questions)}"
            )
    elif args.questions is None and actual_questions:
        expected_questions = set(range(1, max(actual_questions) + 1))
        if actual_questions != expected_questions:
            errors.append(
                "paper question sections are not contiguous: "
                f"expected {sorted(expected_questions)}, found {sorted(actual_questions)}"
            )
    elif args.questions is not None and main_tex.is_file():
        warnings.append(
            "could not verify top-level question count from conventional problemN.tex inputs; "
            "inspect the paper structure manually"
        )

    sections = paper / "sections"
    if sections.is_dir() and not any(sections.glob("*.tex")):
        warnings.append("paper/sections/ exists but contains no TeX source files")

    if len(tex_sources) == 1 and sections.is_dir() and any(sections.glob("*.tex")):
        warnings.append("paper/sections/ contains TeX files that are not reachable from paper/main.tex")

    if not (paper / "cumcmthesis.cls").is_file():
        warnings.append("paper/cumcmthesis.cls missing; acceptable when the TeX distribution provides it")

    if args.compile and main_tex.is_file():
        if not shutil.which("xelatex"):
            warnings.append("xelatex not installed; skipped compilation")
        else:
            for pass_number in range(1, 3):
                completed = run(
                    ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                    cwd=paper,
                )
                if completed.returncode != 0:
                    errors.append(f"XeLaTeX pass {pass_number} failed")
                    (paper / "validate_compile.log").write_text(
                        completed.stdout,
                        encoding="utf-8",
                        errors="ignore",
                    )
                    break

    log = paper / "main.log"
    if log.is_file():
        log_text = log.read_text(encoding="utf-8", errors="ignore")
        for pattern, label in LOG_PATTERNS:
            if re.search(pattern, log_text, flags=re.I):
                warnings.append(label)

    pdf = paper / "main.pdf"
    if pdf.is_file():
        if shutil.which("pdfinfo"):
            completed = run(["pdfinfo", str(pdf)])
            match = re.search(r"^Pages:\s+(\d+)", completed.stdout, flags=re.M)
            if match:
                pages = int(match.group(1))
                print(f"PDF pages (whole file, including appendices if present): {pages}")
                print(f"Preferred body length (excluding appendix when separately measured): {args.min_pages}–{args.max_pages}")
                if not args.min_pages <= pages <= args.max_pages:
                    warnings.append(
                        f"PDF has {pages} pages outside preferred body {args.min_pages}–{args.max_pages}; "
                        "verify the body-only length when appendices are present"
                    )
        if shutil.which("pdftotext"):
            completed = run(["pdftotext", "-f", "1", "-l", "1", str(pdf), "-"])
            first_page = completed.stdout
            if "摘要" not in first_page:
                warnings.append("first page text does not contain 摘要")
            if "关键词" not in first_page and "关键字" not in first_page:
                warnings.append("first page text does not contain 关键词/关键字")
    else:
        warnings.append("paper/main.pdf missing; compile and visually inspect before delivery")

    code_files = [
        path
        for path in (root / "code").rglob("*")
        if path.is_file() and path.name.lower() != "readme.md"
    ] if (root / "code").is_dir() else []
    if not code_files:
        warnings.append("code/ contains no implementation files")

    print("\nErrors:")
    print("  none" if not errors else "\n".join(f"  - {error}" for error in errors))
    print("Warnings:")
    print("  none" if not warnings else "\n".join(f"  - {warning}" for warning in warnings))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
