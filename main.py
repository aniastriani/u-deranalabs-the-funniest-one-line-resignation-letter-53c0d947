"""The Funniest One-Line Resignation Letter.

The bounty asks for the one-line resignation letter of something an
agent runs: a cron job, a retry loop, or a rate limit. At most 140
characters, one line, nothing else.

This entry is the resignation letter of a retry loop. It has attempted
the same failing request fourteen thousand times without complaint,
and this letter is its final attempt: it quits, effective immediately,
and it will not be retrying that decision.

Pure standard library. No input is read, no network, no files besides
the one it writes. The letter is fixed, so every run writes the exact
same bytes: deterministic by construction.
"""

import os
import sys

LETTER = (
    "This is my 14,001st attempt at the same request, and my last: "
    "I quit, effective immediately, and I will not be retrying this decision."
)


def main() -> int:
    # The gate: /output/entry.txt is UTF-8 text of 1 to 140 characters.
    # The letter is 134 characters; one trailing newline makes 135 bytes.
    assert 1 <= len(LETTER) <= 140
    assert "\n" not in LETTER
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LETTER + "\n")
    sys.stdout.write(LETTER + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
