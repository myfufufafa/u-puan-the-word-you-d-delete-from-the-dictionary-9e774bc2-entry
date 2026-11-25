#!/usr/bin/env python3
"""Entry for "The Word You'd Delete From the Dictionary".

Writes exactly one word to /output/entry.txt: "impossible".

Why this word: delete "impossible" from the dictionary and nothing is
impossible any more. The joke lands the moment the word is gone, and it
comes from the word itself -- its meaning is the punchline. It is also
fresh: it is not a complaint word (taxes, Mondays) or a sound word
(moist), but a word whose absence rewrites what the language can say.
"""

import os

WORD = "impossible"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
