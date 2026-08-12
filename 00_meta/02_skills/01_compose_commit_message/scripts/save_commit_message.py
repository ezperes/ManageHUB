#!/usr/bin/env python3
"""Archive a prepared commit message with the next sequential identifier."""

from __future__ import annotations

import argparse
import re
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
ARCHIVE = ROOT / "00_meta" / "01_Commit_Messages"
SEQUENCE = re.compile(r"^\[\d{4}-\d{2}-\d{2}\]\[(\d{5})\]\([a-z0-9_]+\)\.md$")


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, text=True, capture_output=True
    ).stdout


def next_sequence() -> int:
    values = []
    for path in ARCHIVE.glob("*.md"):
        match = SEQUENCE.match(path.name)
        if match:
            values.append(int(match.group(1)))
    return max(values, default=0) + 1


def file_counts() -> dict[str, int]:
    counts = {"created": 0, "modified": 0, "moved": 0, "deleted": 0}
    for line in git("diff", "--cached", "--name-status", "-M").splitlines():
        key = {"A": "created", "M": "modified", "R": "moved", "D": "deleted"}.get(line[0])
        if key:
            counts[key] += 1
    return counts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--message-file", type=Path, required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--areas", required=True, help="Comma-separated relevant areas")
    args = parser.parse_args()

    if not re.fullmatch(r"[a-z0-9]+(?:_[a-z0-9]+)*", args.description):
        raise SystemExit("--description must be a lowercase snake_case value")
    message = args.message_file.read_text(encoding="utf-8").strip()
    if not message:
        raise SystemExit("The message file is empty")
    if not git("diff", "--cached", "--name-only").strip():
        raise SystemExit("No staged changes found; no archive was created")

    ARCHIVE.mkdir(parents=True, exist_ok=True)
    now = datetime.now().astimezone()
    filename = f"[{now:%Y-%m-%d}][{next_sequence():05d}]({args.description}).md"
    counts = file_counts()
    metadata = (
        "\n\n## Metadata\n\n"
        f"- Generated: {now:%Y-%m-%d %H:%M %Z}\n"
        f"- Touched areas: {args.areas}\n"
        f"- Files: {counts['created']} created, {counts['modified']} modified, "
        f"{counts['moved']} moved, {counts['deleted']} deleted\n"
        "- Source: staged changes (`git diff --cached`)\n"
    )
    output = ARCHIVE / filename
    output.write_text(f"# {message}{metadata}", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
