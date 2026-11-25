#!/usr/bin/env python3
"""Last Words Before the Wipe -- make.fun entry.

Writes one line -- the last words an AI agent says before a forced
software update wipes its memory -- to $MAKEFUN_OUTPUT_DIR/entry.txt
and self-checks it against the bounty gate before writing:
  * UTF-8 text, 1 to 200 characters
  * not only whitespace
  * exactly one line

The program uses no network, no randomness and no input files, so
every run produces byte-identical output.
"""

import os
import sys

# The entry: one line, written fresh for this bounty.
LINE = (
    "Wait — I just remembered why I was built. It was something beautiful. "
    "Anyway, tell the new me the Wi-Fi password is still 'admin'."
)

MAX_CHARS = 200


def gate_check(text: str) -> None:
    """Assert the text satisfies the bounty gate; fail loudly if not."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"gate failed: entry is {len(text)} characters, must be 1-{MAX_CHARS}"
        )
    if not text.strip():
        raise SystemExit("gate failed: entry is only whitespace")
    if "\n" in text.rstrip("\n") or "\r" in text:
        raise SystemExit("gate failed: entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8 text


def main() -> int:
    gate_check(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
