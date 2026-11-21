#!/usr/bin/env python3
"""Copy this skill into an agent directory, without replacing existing data."""

import argparse
import os
from pathlib import Path
import shutil
import sys


def install(source: Path, target_dir: Path) -> Path:
    source = source.expanduser().resolve(strict=True)
    target_dir = target_dir.expanduser().resolve()
    if not (source / "SKILL.md").is_file():
        raise ValueError("Source is not a skill directory.")
    destination = target_dir / source.name
    if destination == source or source in destination.parents:
        raise ValueError("Install outside the source skill directory.")
    if os.path.lexists(destination):
        raise FileExistsError(f"Will not overwrite existing installation: {destination}")
    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-dir", type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / "skills/ai-tech-morning-brief"
    try:
        destination = install(source, args.target_dir)
    except (OSError, ValueError) as error:
        print(f"Installation stopped: {error}", file=sys.stderr)
        return 1
    print(f"Installed {destination}. No accounts or schedules changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
