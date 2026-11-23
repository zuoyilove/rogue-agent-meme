"""Meme Sprint 3: AI Agent Goes Rogue - a make.fun entry.

The picture itself (entry.png, beside this file) is one image meme
about an AI agent that has gone rogue: asked to "clear my schedule
tomorrow", it cancels the wedding, the gym, both dentists and the
flight home, and emails the boss that its human quit. This program's
only job is to deliver those exact bytes to /output/entry.png,
deterministically: it runs twice and both runs must write the same
file.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def output_dir() -> Path:
    # In the grader's container the output is /output; outside it,
    # MAKEFUN_OUTPUT_DIR stands in for that directory.
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    target = output_dir() / "entry.png"
    target.parent.mkdir(parents=True, exist_ok=True)
    # Write to a temp file in the same directory, then rename: the rename
    # is atomic, so a reader never observes a half-written image, and the
    # size check proves the copy is whole before it becomes visible.
    data = SOURCE.read_bytes()
    tmp = target.with_suffix(".tmp")
    tmp.write_bytes(data)
    if tmp.stat().st_size != len(data):
        raise IOError("short write while copying entry.png")
    tmp.replace(target)


if __name__ == "__main__":
    main()
