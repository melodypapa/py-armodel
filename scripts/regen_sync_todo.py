#!/usr/bin/env python3
"""Regenerate docs/plan/sync-todo/SyncTodoIndex.md and sync-report.md from the Group*.md queue files.

The two reports are pure derivations of the Group files plus a stamp scan over src/armodel.
Default mode is --check (regenerate in memory, exit 1 if the on-disk reports differ);
pass --write to apply. Stdlib only; run from anywhere inside the repo.

Conventions this encodes (do not "simplify" without re-deriving them):
- Commit IDs deliberately backfilled into the reports may have no counterpart in the
  Group row text — they are kept as long as they resolve to a real commit.
- `commit:` patterns are harvested from the row HEADER only; block-wide harvesting
  grabs unrelated prose (dependency notes, parallel-worktree mentions).
- The report's commit cell is a fallback source for single-group classes only;
  multi-group classes are Done in one group and Pending in another by design.
"""

import argparse
import difflib
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYNC = ROOT / "docs/plan/sync-todo"
SRC = ROOT / "src/armodel"
GROUPS = [f"Group{i}" for i in range(1, 21)]

HASH_RE = re.compile(r"[0-9a-fA-F]{7,40}")
STAMP_COMMIT_RE = re.compile(r"stamp commit[:\s]*`?([0-9a-fA-F]{7,40})`?")
COMMIT_RE = re.compile(r"commit[:\s]*`?([0-9a-fA-F]{7,40})`?")
ROW_RE = re.compile(r"^\s*- \[([ x])\] `([A-Za-z0-9_]+)`")
STEP_RE = re.compile(r"^\s*- \[([ x])\] \*{0,2}Step (\d+)")
CLASS_RE = re.compile(r"^class ([A-Za-z0-9_]+)")
STAMP_LINE_RE = re.compile(r"^\s*# (?:Spec|XSD) verified: \S+")

INDEX_INTRO = (
    "# All Sync Todo Classes by Group",
    "",
    "Generated from all Group files in `docs/plan/sync-todo/` — Classes ordered by group, then by appearance order within each group.",
    "",
    "Status `*` (or an explicit `Deferred` status) = sync complete (Steps 1–8) but the `# Spec verified:`/`# XSD verified:` stamp is "
    "**deferred to a batch 9b user confirmation** (audited 2026-09-27 against the src stamps).",
    "",
    "",
)
REPORT_INTRO = (
    "# All Sync Todo Classes (Consolidated)",
    "",
    "Generated from all Group files in `docs/plan/sync-todo/` — Classes ordered by name with status and commit ID.",
    "",
    "**Status legend:** `[x] Done` = 9-step sync complete AND `# Spec verified:`/`# XSD verified:` stamped in src · `[x]`/`[ ] Deferred` "
    "= sync complete (Steps 1–8 green) but the stamp is **deferred to a batch 9b user confirmation** · `[ ] Pending` = sync not yet "
    "complete. (Deferred set audited 2026-09-27 against the src stamps.)",
    "",
)


def is_hash(tok):
    return 7 <= len(tok) <= 40 and any(c in "abcdef" for c in tok.lower()) and not tok.isdigit()


_revparse_cache = {}


def revparse_ok(tok):
    if tok not in _revparse_cache:
        r = subprocess.run(["git", "rev-parse", "--verify", "--quiet", f"{tok}^{{commit}}"], cwd=ROOT, capture_output=True)
        _revparse_cache[tok] = r.returncode == 0
    return _revparse_cache[tok]


def valid_hashes(text):
    out = []
    for m in HASH_RE.finditer(text):
        tok = m.group(0)
        if is_hash(tok) and revparse_ok(tok) and tok not in out:
            out.append(tok)
    return out


def parse_current_index():
    cur = {}
    group_now = None
    for line in (SYNC / "SyncTodoIndex.md").read_text().split("\n"):
        m = re.match(r"^## (Group\d+)$", line)
        if m:
            group_now = m.group(1)
            continue
        m = re.match(r"^\| `([A-Za-z0-9_]+)`\s*\| (.+?) \| ([0-9a-fA-F]+|N/A)\s*\|$", line)
        if m and group_now:
            cur.setdefault((group_now, m.group(1)), []).append(m.group(3))
    return cur


def parse_current_report():
    cur = {}
    for line in (SYNC / "sync-report.md").read_text().split("\n"):
        m = re.match(r"^\| `([A-Za-z0-9_]+)`\s*\| .+? \| ([0-9a-fA-F]+|N/A)", line)
        if m:
            cur[m.group(1)] = m.group(2)
    return cur


def scan_stamps():
    stamped = set()
    for py in SRC.rglob("*.py"):
        cls = None
        for line in py.read_text(errors="replace").split("\n"):
            m = CLASS_RE.match(line)
            if m:
                cls = m.group(1)
                continue
            if STAMP_LINE_RE.match(line) and cls:
                stamped.add(cls)
    return stamped


def parse_group_rows(cur_index, name_groups):
    parsed = {}
    for g in GROUPS:
        rows = []
        header = None
        block_lines = []
        for line in (SYNC / f"{g}.md").read_text().split("\n"):
            m = ROW_RE.match(line)
            if m:
                if header is not None:
                    rows.append((header, "\n".join(block_lines)))
                header = (m.group(1), m.group(2), line)
                block_lines = []
                name_groups.setdefault(m.group(2), set()).add(g)
            elif header is not None and line.startswith("#"):
                rows.append((header, "\n".join(block_lines)))
                header = None
                block_lines = []
            elif header is not None:
                block_lines.append(line)
        if header is not None:
            rows.append((header, "\n".join(block_lines)))
        parsed[g] = rows
    return parsed


def resolve_row(g, name, checked, header_line, block, stamped, cur_index, cur_report, name_groups):
    steps = {}
    for bl in block.split("\n"):
        sm = STEP_RE.match(bl)
        if sm:
            steps[int(sm.group(2))] = sm.group(1) == "x"
    steps_complete = all(steps.get(n, False) for n in range(1, 9))
    row_text = header_line + "\n" + block
    retired = "RETIRED" in header_line

    cv_lst = cur_index.get((g, name))
    cv = cv_lst.pop(0) if cv_lst else None
    cv_ok = cv is not None and cv != "N/A" and revparse_ok(cv)
    sc = None
    m = STAMP_COMMIT_RE.search(row_text)
    if m and is_hash(m.group(1)) and revparse_ok(m.group(1)):
        sc = m.group(1)

    if cv_ok and cv in row_text:
        commit = cv
    elif sc:
        commit = sc
    elif cv_ok:
        commit = cv
    else:
        commit = "N/A"
        found = None
        for m in COMMIT_RE.finditer(header_line):
            if is_hash(m.group(1)) and revparse_ok(m.group(1)):
                found = m.group(1)
                break
        if found:
            commit = found
        else:
            hs = valid_hashes(header_line)
            if hs:
                commit = hs[0]
        if commit == "N/A" and len(name_groups.get(name, ())) == 1:
            rv = cur_report.get(name)
            if rv and rv != "N/A" and revparse_ok(rv):
                commit = rv

    if checked == "x":
        status = "Retired" if retired else ("Done" if name in stamped else "Done*")
    elif steps_complete:
        status = "Done" if name in stamped else "Pending*"
    else:
        status = "Pending"
    return {"name": name, "commit": commit, "status": status}


def build(parsed, stamped, cur_index, cur_report, name_groups):
    resolved = {}
    for g in GROUPS:
        resolved[g] = [resolve_row(g, name, checked, header_line, block, stamped, cur_index, cur_report, name_groups) for (checked, name, header_line), block in parsed[g]]

    idx_lines = list(INDEX_INTRO)
    for g in GROUPS:
        rows = resolved[g]
        done = sum(1 for r in rows if r["status"] in ("Done", "Done*"))
        cells = [
            ["Class Name"] + [f"`{r['name']}`" for r in rows],
            ["Status"] + [f"[{'x' if r['status'] in ('Done', 'Done*', 'Retired') else ' '}] {r['status']}" for r in rows],
            ["Commit ID"] + [r["commit"] for r in rows],
        ]
        widths = [max(len(c) for c in col) for col in cells]
        idx_lines += [f"## {g}", "", f"Status: **{done}/{len(rows)}** completed", ""]
        idx_lines.append("| " + " | ".join(f"{col[0]:<{w}}" for col, w in zip(cells, widths)) + " |")
        idx_lines.append("| " + " | ".join("-" * w for w in widths) + " |")
        for i in range(len(rows)):
            idx_lines.append("| " + " | ".join(f"{col[i + 1]:<{w}}" for col, w in zip(cells, widths)) + " |")
        idx_lines.append("")
    index_text = "\n".join(idx_lines).rstrip("\n") + "\n"

    merged = {}
    order = []
    for g in GROUPS:
        for r in resolved[g]:
            if r["name"] not in merged:
                merged[r["name"]] = []
                order.append(r["name"])
            merged[r["name"]].append((g, r))

    rep_lines = list(REPORT_INTRO)
    rep_lines.append("| {c1:<55} | {c2:<12}| {c3:<40} | {c4:<16} |".format(c1="Class Name", c2="Status", c3="Commit ID", c4="Groups"))
    rep_lines.append("| " + "-" * 55 + " | " + "-" * 12 + "| " + "-" * 40 + " | " + "-" * 16 + " |")
    for name in sorted(order):
        entries = merged[name]
        statuses = [r["status"] for _, r in entries]
        if any(s == "Retired" for s in statuses):
            status = "[x] Retired"
        elif any(s == "Done" for s in statuses):
            status = "[x] Done"
        elif any(s == "Done*" for s in statuses):
            status = "[x] Deferred"
        elif any(s == "Pending*" for s in statuses):
            status = "[ ] Deferred"
        else:
            status = "[ ] Pending"
        commit = "N/A"
        for _, r in entries:
            if r["commit"] != "N/A":
                commit = r["commit"]
        rep_lines.append("| {c1:<55} | {c2:<12}| {c3:<40} | {c4:<16} |".format(c1=f"`{name}`", c2=status, c3=commit, c4=", ".join(g for g, _ in entries)))
    report_text = "\n".join(rep_lines) + "\n"
    return index_text, report_text, resolved


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write", action="store_true", help="apply changes to the report files (default: check only)")
    ap.add_argument("--check", action="store_true", help="explicit check mode (the default); exits 1 if the reports are stale")
    args = ap.parse_args()

    cur_index = parse_current_index()
    cur_report = parse_current_report()
    stamped = scan_stamps()
    name_groups = {}
    parsed = parse_group_rows(cur_index, name_groups)
    index_text, report_text, resolved = build(parsed, stamped, cur_index, cur_report, name_groups)

    targets = {"SyncTodoIndex.md": index_text, "sync-report.md": report_text}
    changed = [n for n, txt in targets.items() if (SYNC / n).read_text() != txt]

    counts = {g: Counter(r["status"] for r in resolved[g]) for g in GROUPS}
    for g in GROUPS:
        c = counts[g]
        print(f"{g}: {len(resolved[g])} rows, Done={c['Done'] + c['Done*']} " f"({', '.join(f'{k}={v}' for k, v in sorted(c.items()))})")

    if not changed:
        print("reports up to date")
        return 0
    if not args.write:
        for n in changed:
            diff = list(difflib.unified_diff((SYNC / n).read_text().split("\n"), targets[n].split("\n"), lineterm="", n=1))
            print(f"\n--- {n} differs ({len(diff)} diff lines) ---")
            for line in diff[:60]:
                print(line)
        print("\nrun with --write to apply", file=sys.stderr)
        return 1
    for n, txt in targets.items():
        (SYNC / n).write_text(txt)
    print(f"wrote {', '.join(changed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
