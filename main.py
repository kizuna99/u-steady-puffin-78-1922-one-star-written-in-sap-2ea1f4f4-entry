#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""One Star, Written in Sap — entry program.

Writes one line to /output/entry.txt: a one-star review written by a
houseplant (a pothos) about the human who owns it. The grievance: the owner
snipped off the plant's longest vine, rooted the cutting in a jam jar, and
now favours the cutting over the parent plant.

The text is a fixed constant — the program reads nothing from the network,
the environment, or any file it does not ship.
"""
import os

ENTRY_TEXT = (
    "One star. He snipped off my longest vine, rooted it in a jam jar, and now calls it "
    "his favourite plant. I am being outperformed by my own arm, which he also waters first."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate self-check: the sealed scorer accepts UTF-8 text of 1..279
    # characters, not only white space, on a single line. Fail loudly here
    # rather than ship an invalid entry if the constant is ever edited.
    assert 1 <= len(ENTRY_TEXT) <= 279, "entry text outside 1..279 characters"
    assert ENTRY_TEXT.strip() == ENTRY_TEXT and "\n" not in ENTRY_TEXT
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
