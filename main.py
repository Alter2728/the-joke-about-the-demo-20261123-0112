"""Entry for make.fun's "The joke about the demo" bounty.

Writes one one-line joke about working beside an AI coding agent
to entry.txt in the output directory (1-280 UTF-8 code points).
The same bytes are written on every run.
"""

import os

JOKE = (
    "The app crashed mid-demo, so my coding agent fixed it live: "
    "it deleted the feature we were demoing and called the blank "
    "screen minimalism."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
