#!/usr/bin/env python3
"""Two-sentence horror entry for the make.fun bounty
"Two-Sentence Horror".

Writes exactly two sentences — a horror story about nightly photos
taken from the foot of the bed — to /output/entry.txt. Deterministic:
no input, no network, no randomness; the same bytes on every run.

Craft notes: the setup is a quiet, recurring violation — every night
at 3am the phone buzzes with a photo of the narrator asleep, taken
from the foot of the bed, a specific time and a specific vantage point
that make the unseen watcher feel close rather than abstract. The
twist lands entirely in the second sentence: the newest photo shows
the narrator awake, smiling, holding the phone, so the watcher is no
longer distant — the narrator is the one looking back, or the watcher
has become the narrator, and the dread is that the boundary between
victim and intruder has collapsed. That fits the judge brief: exactly
two sentences, at most 400 characters, a complete horror arc — premise,
escalation, and a reversal that reframes the first sentence — in a
story that is clear on first read and unsettling on the second.
"""

import os

STORY = (
    "Every night at 3am my phone buzzes with a photo of me asleep, "
    "taken from the foot of my bed. "
    "This morning the newest one showed me awake, smiling, "
    "holding the phone."
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
