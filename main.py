#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt.

Deterministic: no network, no randomness, no clock. The line is a
constant; validate() enforces the competition gate (UTF-8 text,
1-200 characters, not only whitespace, a single line).
"""

import os
import sys

MAX_CHARS = 200

ROAST = (
    "My agent burned 40,000 tokens researching a typo, fixed it with "
    "one character, and called the whole thing a deep refactor."
)


def validate(text):
    """Enforce every gate rule; raise ValueError on the first failure."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    return text


def main():
    line = validate(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print("wrote %s (%d chars)" % (path, len(line)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
