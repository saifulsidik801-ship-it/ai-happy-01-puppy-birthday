#!/usr/bin/env python3
"""ai-happy-01 entry: copy the chosen happy image to the output file.

The image is a golden retriever puppy at its first birthday party:
a tiny party hat, falling confetti, a sprinkle cake with one lit candle,
and the widest happy laugh. Pure joy, drawn to make the judge smile.
No network, no randomness: the same bytes every run.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT / "entry.png")


if __name__ == "__main__":
    main()
