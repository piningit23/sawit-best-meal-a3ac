#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun entry.

Writes one sentence (<=200 characters) about the best meal ever had
to /output/entry.txt. The sentence is a single, concrete, personal
memory: a late-night bowl of mie ayam from a Yogyakarta street cart.
"""

import os

SENTENCE = (
    "The best meal I ever had was a 2 a.m. bowl of steaming mie ayam "
    "from a Yogyakarta street cart, its broth so rich I forgave the "
    "friend who dragged me out of bed for it."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text and not text.isspace()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
