"""Two Robots in an Elevator - entry program."""

import os

LINE = "Sensors confirm we're going up, so I'll park my hands at factory default and act casual."


OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main():
    assert 1 <= len(LINE) <= MAX_CHARS
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
