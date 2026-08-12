#!/usr/bin/env python3
"""Print a JSON summary of staged changes, or the working tree when empty."""

from __future__ import annotations

import json
import subprocess
from collections import Counter


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], check=True, text=True, capture_output=True
    ).stdout


def name_status(*args: str) -> tuple[Counter[str], list[str]]:
    counts: Counter[str] = Counter()
    paths: list[str] = []
    for line in git(*args).splitlines():
        fields = line.split("\t")
        status = fields[0][0]
        counts[status] += 1
        paths.extend(fields[1:])
    return counts, paths


def summary(counts: Counter[str], paths: list[str]) -> dict[str, object]:
    return {
        "files": {
            "created": counts["A"],
            "modified": counts["M"],
            "moved": counts["R"],
            "deleted": counts["D"],
        },
        "paths": paths,
        "touched_directories": sorted(
            {path.rsplit("/", 1)[0] if "/" in path else "." for path in paths}
        ),
    }


def working_tree_summary() -> dict[str, object]:
    counts: Counter[str] = Counter()
    paths: list[str] = []
    entries = git("status", "--short", "-z").split("\0")
    for entry in entries:
        if not entry:
            continue
        status, path = entry[:2], entry[3:]
        code = next((value for value in status if value not in {" ", "?"}), "?")
        counts[code] += 1
        paths.append(path)
    return summary(counts, paths)


def main() -> None:
    staged_counts, staged_paths = name_status("diff", "--cached", "--name-status", "-M")
    if staged_paths:
        print(json.dumps({"staged": True, **summary(staged_counts, staged_paths)}, indent=2))
        return

    print(json.dumps({"staged": False, "working_tree": working_tree_summary()}, indent=2))


if __name__ == "__main__":
    main()
