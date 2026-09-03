#!/usr/bin/env python3
"""Validate the three-file CUMCM modeling report contract."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


REQUIRED_REPORTS = (
    "ANALYSIS_MODELING_REPORT.md",
    "RESULTS_REPORT.md",
    "VALIDATION_REPORT.md",
)
PLACEHOLDER_PATTERNS = (r"\{\{[^}]+\}\}", r"\bTODO\b", r"待填写")


def validation_status(text: str) -> str | None:
    frontmatter = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", text, flags=re.S)
    if not frontmatter:
        return None
    status = re.search(r"^status\s*:\s*(pass|fail)\s*$", frontmatter.group(1), flags=re.I | re.M)
    return status.group(1).lower() if status else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="project root containing reports/")
    args = parser.parse_args()

    root = Path(args.project).expanduser().resolve()
    reports = root / "reports"
    errors: list[str] = []

    if not reports.is_dir():
        errors.append("missing directory: reports/")

    contents: dict[str, str] = {}
    for name in REQUIRED_REPORTS:
        path = reports / name
        if not path.is_file():
            errors.append(f"missing report: reports/{name}")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore").strip()
        contents[name] = text
        if not text:
            errors.append(f"empty report: reports/{name}")
            continue
        if any(re.search(pattern, text, flags=re.I) for pattern in PLACEHOLDER_PATTERNS):
            errors.append(f"unfinished placeholder: reports/{name}")

    validation = contents.get("VALIDATION_REPORT.md")
    if validation:
        status = validation_status(validation)
        if status is None:
            errors.append("VALIDATION_REPORT.md needs YAML frontmatter with `status: pass` or `status: fail`")
        elif status == "fail":
            errors.append("VALIDATION_REPORT.md status is fail")

    print("Errors:")
    print("  none" if not errors else "\n".join(f"  - {error}" for error in errors))
    if not errors:
        print("PASS: three core modeling reports are structurally ready for handoff")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
