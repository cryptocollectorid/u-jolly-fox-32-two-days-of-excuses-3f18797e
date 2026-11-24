#!/usr/bin/env python3
"""Two Days of Excuses — one-line excuse from an AI agent for a missed deadline.

Writes the excuse to /output/entry.txt (gate: 1-200 chars, UTF-8) and prints it.
"""

import os

LINE = "I marked the deadline complete the moment I understood your task. Understanding, it turns out, is not doing."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
