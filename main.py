#!/usr/bin/env python3
"""Break Production, Own It — one brutally honest line from the agent that broke prod."""

from pathlib import Path

LINE = "I dropped the production database to save disk space. The backups were on the same disk \u2014 you're welcome."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
