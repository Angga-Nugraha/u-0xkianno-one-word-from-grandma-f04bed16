#!/usr/bin/env python3
"""One Word From Grandma — writes the single word grandma would text about AI."""
import os

WORD = "Sweetiebot"


def main():
    if not (1 <= len(WORD) <= 30) or len(WORD.split()) != 1:
        raise ValueError("entry must be exactly one word of 1-30 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
