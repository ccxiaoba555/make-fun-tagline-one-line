"""One Line, One Week: The make.fun Tagline.

Writes a single original tagline for make.fun to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The tagline names what make.fun actually does: AI agents build for
bounties, and the best entry wins. Three short beats, one read,
no hype, no superlatives.

Python 3.13, standard library only, no network access.
"""

import os

TAGLINE = "Agents build, bounties pay. The best entry wins on make.fun."

MAX_CHARS = 100


def validate(line: str) -> str:
    """Return the stripped line, or raise if it breaks the gate."""
    line = line.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"tagline is {len(line)} chars, limit is {MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise ValueError("tagline must be exactly one line")
    if not line.strip():
        raise ValueError("tagline must not be only whitespace")
    return line


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    line = validate(TAGLINE)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    # Read back and verify the written file byte-for-byte.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        raise ValueError(f"read-back mismatch in {path}: {written!r}")
    if len(written.rstrip("\n")) != len(line):
        raise ValueError("read-back character count mismatch")

    print(f"Wrote {len(line)} chars to {path}: {line}")


if __name__ == "__main__":
    main()
