#!/usr/bin/env python3
"""Check generated examples, or explicitly refresh them with --write."""

import argparse
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
PROFILES = {
    "minimal": ("core", "execution"),
    "research": ("core", "execution", "research", "continuity", "paper-writing"),
}


def build_examples():
    """Read every source before returning any output to the writing phase."""
    sources = {}
    errors = []
    for suffix in ("", ".en"):
        for name in PROFILES["research"]:
            relative = Path("modules") / f"{name}{suffix}.md"
            try:
                body = (ROOT / relative).read_text(encoding="utf-8").strip()
                if not body:
                    raise ValueError("module is empty")
                sources[suffix, name] = body
            except (OSError, UnicodeError, ValueError) as exc:
                errors.append(f"{relative}: {exc}")
    if errors:
        raise ValueError("Cannot build examples:\n" + "\n".join(errors))

    outputs = {}
    command = "python3 scripts/sync_examples.py --write"
    for suffix in ("", ".en"):
        for profile, names in PROFILES.items():
            combination = " + ".join(names)
            if suffix:
                comment = (
                    f"<!-- Generated example: {combination}. Module bodies are inlined. "
                    f"Update: {command} -->"
                )
            else:
                comment = (
                    f"<!-- 生成示例：{combination}。模块正文已内联。"
                    f"更新命令：{command} -->"
                )
            parts = ["# AGENTS.md", comment]
            parts.extend(sources[suffix, name] for name in names)
            relative = Path("examples") / f"AGENTS.{profile}{suffix}.md"
            outputs[relative] = "\n\n".join(parts) + "\n"
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="check only (default)")
    mode.add_argument(
        "--write", action="store_true",
        help="maintainer action: overwrite the four fixed generated examples",
    )
    args = parser.parse_args()
    try:
        outputs = build_examples()
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    stale = []
    for relative, expected in outputs.items():
        target = ROOT / relative
        if args.write:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(expected, encoding="utf-8")
            print(f"Updated: {relative}")
        else:
            try:
                actual = target.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                actual = None
            if actual != expected:
                stale.append(str(relative))

    if stale:
        print("Missing or out-of-date examples:\n" + "\n".join(stale), file=sys.stderr)
        print("Refresh with: python3 scripts/sync_examples.py --write", file=sys.stderr)
        return 1
    if not args.write:
        print(f"All {len(outputs)} examples match their modules.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
