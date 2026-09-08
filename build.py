#!/usr/bin/env python3
"""Assemble index.html from the editable pieces in src/.

Edit the files in src/sections/ (one file per slide), or src/head.html /
src/foot.html for the shared shell, then run:

    python build.py

Sections are ordered by filename, so the leading number (00-, 01-, ...)
controls the running order. index.html is generated: do not edit it by hand,
your changes there will be overwritten on the next build.
"""
import pathlib

BASE = pathlib.Path(__file__).resolve().parent
SRC = BASE / "src"
SECTIONS = SRC / "sections"


def read(p):
    return p.read_text(encoding="utf-8").strip("\n")


def build():
    head = read(SRC / "head.html")
    foot = read(SRC / "foot.html")
    files = sorted(SECTIONS.glob("*.html"))
    if not files:
        raise SystemExit("No section files found in src/sections/")

    sections = [read(f) for f in files]
    out = head + "\n\n" + "\n\n".join(sections) + "\n\n" + foot + "\n"

    (BASE / "index.html").write_text(out, encoding="utf-8")
    print(f"Built index.html from {len(files)} sections:")
    for f in files:
        print(f"  {f.name}")


if __name__ == "__main__":
    build()
