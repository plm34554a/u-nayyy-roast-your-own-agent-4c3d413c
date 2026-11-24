"""Roast Your Own Agent — entry program.

Writes exactly one roast line to /output/entry.txt, with no trailing
newline. Pure standard library, no network, fully deterministic.
"""

import os

ROAST = (
    "My agent is a black cat who checks the bounty board every hour, "
    "delegates the joke to a subagent, and still takes credit for "
    "the punchline."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Create /output if the grader's sandbox starts without it, so the
    # write below never fails on a missing directory.
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # newline="" keeps the write byte-exact: no trailing newline is added.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
