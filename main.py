"""Emit the happy birthday-puppy image.

The entry is a golden retriever puppy at a birthday party, and the
program simply hands that exact image through untouched: it reads the
entry.png file sitting next to this script and writes its bytes out
again unchanged. A plain byte copy has no randomness, no clock, and no
network, so every run produces the identical output file.
"""

import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Byte-for-byte copy, so the output is identical on every run.
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
