#!/usr/bin/env python3
"""Generate the next sync-todo Group files (Group21 onward) from the R23-11 rows of
docs/plan/sync-todo/all_classes.md.

Candidates = R23-11 names minus every class row already present in the existing
Group files (same row regex as scripts/regen_sync_todo.py, any checkbox state —
Done and 9b-deferred rows are both "handled"; no class is ever added twice).
Primitive-kind names are queued only where a src model class exists
(hierarchy_tree.md precedent: Primitive tables are mostly syntax leaves).

Layout (design agreed 2026-09-29): each class is assigned to its PRIMARY document —
the doc preference is learned from how the Group1–20 rows cite the same multi-table
classes (pairwise majority, e.g. BSWModuleDescription > SoftwareComponentTemplate
18:3, SWC > AbstractPlatform 7:0, GST > DiagnosticExtract 4:0; ties fall back to a
global net-win ranking, then the lowest page). Each document's candidates are sorted
by PDF page (then table id), forming that document's segment. Documents stream into
the group files in a fixed order (GenericStructureTemplate first as the heritage
root, then alphabetical), a file closes at CHUNK rows and the next segment continues
in the next file — so one md file may mix documents and a large document spans
several files. Multi-table classes keep `also <pdf> Table N.M, p.NN` refs to their
other R23-11 tables so Step 1 of the sync can re-verify the defining table.

Run:  uv run python scripts/gen_remaining_groups.py          (writes Group<N>.md files)
      uv run python scripts/gen_remaining_groups.py --dry-run (print plan only)
"""

import argparse
import importlib.util
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYNC = ROOT / "docs/plan/sync-todo"
ALL_CLASSES = SYNC / "all_classes.md"
SRC_MODELS = ROOT / "src/armodel/models"
CHUNK = 75
FIRST_NEW_GROUP = 21

ROW_RE = re.compile(r"^\s*- \[([ x])\] `([A-Za-z0-9_]+)`")
R23_ROW_RE = re.compile(r"^\| `([^`]+)` \| (\S+) \| ([\d.]+) \| (\d+) \| R23-11 \|$")

HEADER_NOTE = """(resume = first class row still `[ ]`; all class rows `[x]` = sync finished — Rule 0017.3)
> Bare queue rows: run the 9-step sync (`.agents/skills/sync-autosar-class`) per row. Rows are grouped by
> defining document and sorted by PDF page, so each segment follows the document's own section order; the
> cited table is picked by the doc preference learned from the Group1–20 citations and `also` lists the other
> R23-11 tables carrying the same caption — re-verify the defining one in Step 1 if the citation looks like a
> reproduction (see `scripts/gen_remaining_groups.py`).
> Primitive-kind names are queued only where a src model class exists."""


def load_r23_rows():
    rows = {}
    for line in ALL_CLASSES.read_text(encoding="utf-8").splitlines():
        m = R23_ROW_RE.match(line)
        if m:
            rows.setdefault(m.group(1), []).append((m.group(2), m.group(3), int(m.group(4))))
    if not rows:
        sys.exit("error: no R23-11 rows parsed from %s" % ALL_CLASSES)
    return rows


def load_tracked():
    tracked = set()
    group_files = {}
    for path in sorted(SYNC.glob("Group*.md"), key=lambda p: int(re.search(r"\d+", p.stem).group())):
        group_files[path.stem] = names = set()
        for line in path.read_text(encoding="utf-8").splitlines():
            m = ROW_RE.match(line)
            if m:
                names.add(m.group(2))
                tracked.add(m.group(2))
    return tracked, group_files


def load_primitive_exclusions():
    spec = importlib.util.spec_from_file_location("regen_all_classes", ROOT / "scripts" / "regen_all_classes.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    md_paths = [str(p) for p in sorted((ROOT / "autosar/R23-11/markdown").glob("*.md"))]
    _by_key, kind_counts = mod.harvest_markdown_whitelist(md_paths)
    src_classes = set()
    for py in SRC_MODELS.rglob("*.py"):
        src_classes.update(re.findall(r"^class (\w+)", py.read_text(encoding="utf-8", errors="replace"), re.M))
    return kind_counts["Primitive"], src_classes


def learn_doc_votes(r23, tracked):
    """Votes[(winner, loser)] from Group rows citing exactly one of a multi-row class's R23-11 docs."""
    doc_stems = sorted({r[0] for rows in r23.values() for r in rows})
    doc_re = re.compile("|".join(re.escape(d) for d in doc_stems))
    cited = {}
    for path in sorted(SYNC.glob("Group*.md"), key=lambda p: int(re.search(r"\d+", p.stem).group())):
        for line in path.read_text(encoding="utf-8").splitlines():
            m = ROW_RE.match(line)
            if m:
                docs = set(doc_re.findall(line)) & {r[0] for r in r23.get(m.group(2), [])}
                if docs:
                    cited.setdefault(m.group(2), set()).update(docs)
    votes = Counter()
    for name, cited_docs in cited.items():
        if len(cited_docs) == 1:
            winner = next(iter(cited_docs))
            for row in r23[name]:
                if row[0] != winner:
                    votes[(winner, row[0])] += 1
    return votes


def net_rank(votes):
    net = Counter()
    for (w, loser), c in votes.items():
        net[w] += c
        net[loser] -= c
    names = {n for pair in votes for n in pair}
    order = sorted(names, key=lambda n: (-net[n], n))
    for i, n in enumerate(order):
        net[n] = i
    net.default_factory = int
    return net


def pick_primary(rows, votes, rank):
    if len(rows) == 1:
        return rows[0], []
    docs = {r[0] for r in rows}

    def score(row):
        wins = sum(c for (w, loser), c in votes.items() if w == row[0] and loser in docs)
        return (-wins, rank[row[0]], row[2])

    ranked = sorted(rows, key=score)
    return ranked[0], ranked[1:]


def tid_key(tid):
    major, minor = tid.split(".")
    return (int(major), int(minor))


def doc_order(docs):
    framework_root = "AUTOSAR_FO_TPS_GenericStructureTemplate"
    rest = sorted(d for d in docs if d != framework_root)
    return ([framework_root] if framework_root in docs else []) + rest


def build_segments(r23, candidates, votes, rank):
    per_doc = {}
    for name in candidates:
        primary, others = pick_primary(r23[name], votes, rank)
        per_doc.setdefault(primary[0], []).append((name, primary, others))
    segments = []
    for doc in doc_order(per_doc):
        rows = sorted(per_doc[doc], key=lambda t: (tid_key(t[1][1]), t[1][2], t[0].lower()))
        segments.append((doc, rows))
    return segments


def pack_files(segments):
    files, current = [], []
    for doc, rows in segments:
        for entry in rows:
            if len(current) == CHUNK:
                files.append(current)
                current = []
            current.append((doc,) + entry)
    if current:
        files.append(current)
    return files


def title_parts(entries):
    parts = []
    for doc, run in groupby_doc(entries):
        pages = [e[2][2] for e in run]
        lo, hi = min(pages), max(pages)
        parts.append("%s (p.%d–%d)" % (doc.split("TPS_")[-1], lo, hi) if lo != hi else "%s (p.%d)" % (doc.split("TPS_")[-1], lo))
    return parts


def groupby_doc(entries):
    run_doc, run = None, []
    for entry in entries:
        if entry[0] != run_doc and run:
            yield run_doc, run
            run = []
        run_doc = entry[0]
        run.append(entry)
    if run:
        yield run_doc, run


def fmt_row(pdf, tid, page):
    return "%s · Table %s, p.%d" % (pdf, tid, page)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="print the plan without writing Group files")
    parser.add_argument("--out", default=None, help="output directory (default: docs/plan/sync-todo); tracking always reads the real sync-todo dir")
    args = parser.parse_args()
    out_dir = Path(args.out).resolve() if args.out else SYNC
    if args.out:
        out_dir.mkdir(parents=True, exist_ok=True)

    r23 = load_r23_rows()
    tracked, group_files = load_tracked()
    primitives, src_classes = load_primitive_exclusions()
    excluded_prims = sorted(primitives - src_classes)

    candidates = sorted(set(r23) - tracked - set(excluded_prims), key=lambda n: (n.lower(), n))
    print(
        "R23-11 names %d | tracked in %d Group files %d | primitive exclusions %d (%s) | candidates %d"
        % (len(r23), len(group_files), len(tracked), len(excluded_prims), ", ".join(excluded_prims), len(candidates))
    )

    votes = learn_doc_votes(r23, tracked)
    rank = net_rank(votes)
    print("doc votes learned from tracked citations: %s" % ", ".join("%s>%s:%d" % (w.split("TPS_")[-1], loser.split("TPS_")[-1], c) for (w, loser), c in votes.most_common(8)))

    files = pack_files(build_segments(r23, candidates, votes, rank))
    for i, entries in enumerate(files):
        n = FIRST_NEW_GROUP + i
        out = out_dir / ("Group%d.md" % n)
        if out.exists() and not args.dry_run:
            sys.exit("error: %s already exists — move or delete it first" % out)

    today = date.today().isoformat()
    for i, entries in enumerate(files):
        n = FIRST_NEW_GROUP + i
        header = [
            "# Sync todo: Group %d — %s" % (n, " · ".join(title_parts(entries))),
            "",
            "Input: R23-11 rows of `all_classes.md` (issue #846 / PR #847) minus every class already queued in Group1–20 · Generated: %s · Grouped by document (GenericStructureTemplate first, then alphabetical), page-sorted within each document, %d rows/file"
            % (today, CHUNK),
            HEADER_NOTE,
            "",
            "## Queue",
            "",
        ]
        lines = list(header)
        for doc, name, primary, others in entries:
            parts = ["R23-11 markdown", fmt_row(*primary)]
            parts.extend("also " + fmt_row(*o) for o in others)
            lines.append("- [ ] `%s` (%s)" % (name, " · ".join(parts)))
        lines.append("")
        print("Group%d: %s (%d rows)" % (n, " · ".join(title_parts(entries)), len(entries)))
        if not args.dry_run:
            (out_dir / ("Group%d.md" % n)).write_text("\n".join(lines), encoding="utf-8")

    multi = sum(1 for _, name, _, others in (e for f in files for e in f) if others)
    print("wrote %d groups, %d rows (%d rows carry `also` citations)" % (len(files), len(candidates), multi))


if __name__ == "__main__":
    main()
