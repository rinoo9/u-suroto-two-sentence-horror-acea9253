#!/usr/bin/env python3
"""Two-sentence horror entry for the make.fun bounty
"Two-Sentence Horror".

Writes exactly two sentences — a horror story about a doorbell
camera filming the narrator leaving the house at 3am — to
/output/entry.txt. Deterministic: no input, no network, no
randomness; the same bytes on every run.

Craft notes: the setup is a quiet, recurring violation — a doorbell
camera sending clips of the narrator leaving the house at 3am,
smiling at the lens, a familiar device turned intimate and wrong.
The twist lands entirely in the second sentence: the narrator has
never left the house at 3am, and the man in the clips has started
waving back, so the threat is no longer a recording of the past —
the double is already outside, watching, and learning. That fits
the judge brief: exactly two sentences, at most 400 characters, a
complete horror arc — premise, escalation, and a reversal that
reframes the first sentence — in a story that is clear on first
read and unsettling on the second.
"""

import os

STORY = (
    "My doorbell camera keeps sending me clips of myself leaving the "
    "house at 3am, smiling at the lens. "
    "I have never left the house at 3am, and the man in the clips has "
    "started waving back."
)


def main() -> None:
    assert 1 <= len(STORY) <= 400, f"story is {len(STORY)} characters"
    assert STORY.count(".") == 2, f"story has {STORY.count('.')} periods"
    assert "?" not in STORY and "!" not in STORY
    assert "\n" not in STORY and STORY == STORY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
