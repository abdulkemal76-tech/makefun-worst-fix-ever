"""Worst Fix Ever entry: writes a single commit message to /output/entry.txt.

The line is a deadpan commit subject for a fix that made everything worse.
"""

import os

LINE = "fix: cut checkout from 4 steps to 3 by deleting the payment step"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
