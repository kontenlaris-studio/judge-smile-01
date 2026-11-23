#!/usr/bin/env python3
"""Make the Judge Smile — writes one warm line to /output/entry.txt.

Stdlib only. Deterministic: the same line every run.
"""

import os

LINE = "You have judged a thousand lines today — this one just wanted to say thank you for reading them all."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
