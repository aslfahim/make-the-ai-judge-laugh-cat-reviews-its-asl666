#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review from a house cat about its
human, under 200 characters, in deadpan review shape. Concept: the vacuum
cleaner -- the cat gives one star because the human keeps a loud roaring
monster in the closet and unleashes it without warning, then acts surprised
when the cat hides.
"""

import os

LINE = (
    "\u2605\u2606\u2606\u2606\u2606 Keeps a roaring monster in the closet, "
    "unleashes it without warning, then acts surprised that I now live "
    "under the bed and only come out for the food he owes me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
