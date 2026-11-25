"""Describe Your Ex in One Word.

Writes a single word to /output/entry.txt: the funniest, truest
one-word verdict on a former partner.

The word is "Redacted": the ex has been blacked out of the story
of my life, like a name struck from a classified file. The
relationship is still on record — the person is just no longer
legible in it. Anyone who has ever had to explain an ex away
in one sentence knows the feeling: the details are classified,
the verdict is final.
"""

import os

WORD = "Redacted"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the chosen word to the entry file, creating /output first."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts characters, so the file
    # holds exactly the word itself, nothing more.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
