#!/usr/bin/env python3
"""Move top-level class blocks from one module to another (Rule 0007 helper).

Usage:
    python scripts/move_class_blocks.py SOURCE TARGET ClassName [ClassName ...]

Removes the named top-level classes together with their directly attached
leading comment lines from SOURCE and appends them to TARGET. Import
statements are deliberately NOT touched: fix imports by hand afterwards and
let `npm run lint` report leftovers (F401 unused / F821 undefined).
"""
import argparse
import re
import sys

CLASS_RE = re.compile(r"^class\s+([A-Za-z_][A-Za-z0-9_]*)")


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines(keepends=True)


def save(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        f.write("".join(lines))


def class_blocks(lines):
    starts = []
    for i, line in enumerate(lines):
        m = CLASS_RE.match(line)
        if m:
            s = i
            while s > 0 and lines[s - 1].lstrip().startswith("#"):
                s -= 1
            starts.append((i, s, m.group(1)))
    blocks = {}
    for idx, (i, s, name) in enumerate(starts):
        end = starts[idx + 1][1] if idx + 1 < len(starts) else len(lines)
        blocks[name] = (s, end)
    return blocks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("target")
    parser.add_argument("classes", nargs="+")
    args = parser.parse_args()

    src = load(args.source)
    blocks = class_blocks(src)
    missing = [c for c in args.classes if c not in blocks]
    if missing:
        sys.exit("not found in {}: {}".format(args.source, ", ".join(missing)))

    ranges = sorted(blocks[c] for c in args.classes)
    moved = ["".join(src[s:e]).rstrip("\n") + "\n" for s, e in ranges]
    for s, e in reversed(ranges):
        del src[s:e]

    text = "".join(src)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    if text and not text.endswith("\n"):
        text += "\n"
    save(args.source, text.splitlines(keepends=True))

    tgt = load(args.target)
    if tgt and not "".join(tgt).endswith("\n"):
        tgt.append("\n")
    for block in moved:
        tgt.append("\n")
        tgt.append(block)
    save(args.target, tgt)


if __name__ == "__main__":
    main()
