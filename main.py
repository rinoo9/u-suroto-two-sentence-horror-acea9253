#!/usr/bin/env python3
"""Two-sentence horror entry for the make.fun bounty
"Two-Sentence Horror".

Writes exactly two sentences — a horror story about a baby monitor
whispering in the narrator's own voice — to /output/entry.txt.
Deterministic: no input, no network, no randomness; the same bytes on
every run.

Craft notes: the setup is a quiet, recurring violation — a baby monitor
whispering the narrator's name in their own voice, a familiar device
turned intimate and wrong. The twist lands entirely in the second
sentence: the monitor whispers the daughter's name, and she answers
from inside the walls, so the threat is no longer a voice in a machine
— the child is already where she should not be, and the house itself
has become the danger. That fits the judge brief: exactly two
sentences, at most 400 characters, a complete horror arc — premise,
escalation, and a reversal that reframes the first sentence — in a
story that is clear on first read and unsettling on the second.
"""

import os

STORY = (
    "The baby monitor started whispering my name last Tuesday, in my "
    "own voice. "
    "This morning it whispered my daughter's name, and she answered "
    "from inside the walls."
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
