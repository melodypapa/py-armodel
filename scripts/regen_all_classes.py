#!/usr/bin/env python3
"""Regenerate docs/plan/sync-todo/all_classes.md — the alphabetical index of every
class / enumeration / primitive table in the AUTOSAR spec corpora under `autosar/`,
with the owning PDF, table id and 1-based PDF page per release.

Method (mirrors `.agents/skills/sync-autosar-class/pdf_page.py` and the
hierarchy_tree.md regeneration):
  1. Harvest the whitelist of spec type names from the markdown corpora: the header
     cell of a type table is `| Class |`, `| Enumeration |` or `| Primitive |` and the
     next cell carries the name (docling repeats it 4x; `(abstract)` suffixes and
     `<<...>>` / docling `glyph[...]` stereotype prefixes are stripped). Continuation
     tables (`| Base |`, `| Attribute |`, `| Package |`, ...) are ignored. Names are
     compared space-free so mangled markdown tokens ("Multidimensiona lTime") still
     match; the space-free last token is added too (stereotype-prefixed cells).
  2. Scan every release PDF for `Table N.M: <Name>` captions (first page per table id,
     cached in `.pdf_table_cache.json` shared with pdf_page.py) and keep the captions
     whose name is in the release whitelist. Captions whose single-token capture is
     truncated by PDF text extraction ("ArraySpeci fication") get a rescue pass: the
     full caption tail is re-read from the PDF page and space-free matched.

Scope: R23-11 (all 15 TPS PDFs), R4.3.1 (11 TPS PDFs; RS_*/TR_* are not class specs),
R3.2.3 (5 template PDFs). R4.4.0 (xsd-only) and autosar/ECUC (markdown-only) carry no
PDF, so no page numbers exist for them — they are out of scope.

Known corpus limitation: autosar/R3.2.3 PDFs mostly carry no `Table N.M:` captions
(only AUTOSAR_SoftwareComponentTemplate and AUTOSAR_ECU_Configuration do), so R3.2.3
rows are partial even where its markdown has class tables.

The rescue pass needs pypdf, which is not a project dependency:
  uv run --with pypdf python scripts/regen_all_classes.py

Output goes to stdout (diagnostics) and docs/plan/sync-todo/all_classes.md. Do not edit
the generated file by hand.
"""

import glob
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_FILE = os.path.join(REPO_ROOT, "docs", "plan", "sync-todo", "all_classes.md")
PDF_PAGE_HELPER = os.path.join(REPO_ROOT, ".agents", "skills", "sync-autosar-class", "pdf_page.py")

RELEASES = [
    ("R23-11", "autosar/R23-11/markdown/*.md", "autosar/R23-11/pdf/*.pdf"),
    ("R4.3.1", "autosar/R4.3.1/markdown/AUTOSAR_TPS_*.md", "autosar/R4.3.1/pdf/AUTOSAR_TPS_*.pdf"),
    ("R3.2.3", "autosar/R3.2.3/markdown/*.md", "autosar/R3.2.3/pdf/*.pdf"),
]

TYPE_HEADER_KINDS = ("Class", "Enumeration", "Primitive")

LIGATURES = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi", "\ufb04": "ffl", "\ufb05": "st", "\ufb06": "st"}


def normkey(name):
    for lig, ascii_pair in LIGATURES.items():
        name = name.replace(lig, ascii_pair)
    key = re.sub(r"<<[^>]*>>", "", name)
    key = re.sub(r"glyph\[[^\]]*\]", "", key)
    key = key.replace("(abstract)", "")
    return re.sub(r"\s+", "", key)


def last_token_key(name):
    cleaned = re.sub(r"glyph\[[^\]]*\]", "", name).replace("(abstract)", "").strip()
    tokens = cleaned.split()
    return normkey(tokens[-1]) if tokens else ""


def cell_at(row, index):
    cells = row.split("|")
    return cells[index].strip() if index < len(cells) else ""


def first_name_cell(row):
    cells = [c.strip() for c in row.split("|")[1:]]
    for cell in cells[1:]:
        if cell:
            return cell
    return ""


def clean_display(name):
    display = re.sub(r"glyph\[[^\]]*\]", "", re.sub(r"<<[^>]*>>", "", name)).strip()
    while display.split() and re.match(r"^atp[A-Z]", display.split()[0]):
        display = display.split(" ", 1)[1] if " " in display else ""
    return re.sub(r"\s*\(abstract\)\s*$", "", display).strip()


def harvest_markdown_whitelist(md_paths):
    """Return (key->display dict) from markdown type tables; keys are normkey + last-token variants."""
    by_key = {}
    kind_counts = {kind: set() for kind in TYPE_HEADER_KINDS}
    merged_re = re.compile(r"^(%s)\s+([A-Za-z0-9_\-]+)$" % "|".join(TYPE_HEADER_KINDS))
    for path in md_paths:
        with open(path, encoding="utf-8", errors="replace") as f:
            lines = f.read().splitlines()
        for line in lines:
            if not line.startswith("|"):
                continue
            cell = first_name_cell(line)
            merged = merged_re.match(cell_at(line, 1))
            if merged:
                display, kind = merged.group(2), merged.group(1)
            else:
                kind = cell_at(line, 1)
                if kind not in TYPE_HEADER_KINDS or not cell:
                    continue
                display = clean_display(cell)
                if not display:
                    continue
            kind_counts[kind].add(display)
            source = cell if not merged else display
            for key in (normkey(source), last_token_key(source)):
                if key and key not in by_key:
                    by_key[key] = display
    return by_key, kind_counts


def load_pdf_helper():
    sys.path.insert(0, os.path.dirname(PDF_PAGE_HELPER))
    import pdf_page

    return pdf_page


def rescue_caption_name(pdf_path, tid, page, helper):
    """Re-read the full caption tail from the PDF page (single-token captures get truncated)."""
    try:
        from pypdf import PdfReader
    except ImportError:
        return None
    reader = helper.CACHED_READERS.get(pdf_path)
    if reader is None:
        reader = PdfReader(pdf_path)
        helper.CACHED_READERS[pdf_path] = reader
    text = reader.pages[page - 1].extract_text() or ""
    m = re.search(r"Table\s+%s\s*:\s*([^\n]+)" % re.escape(tid), text)
    return m.group(1).strip() if m else None


def scan_release_pdfs(pdf_paths, by_key, helper):
    """Return (rows, rescued, unmatched) for whitelisted captions; rows are (class, pdf_stem, tid, page)."""
    rows, rescued, unmatched = [], [], {}
    for pdf_path in pdf_paths:
        tables = helper.get_pdf_tables(pdf_path)
        pdf_stem = os.path.splitext(os.path.basename(pdf_path))[0]
        for tid, (cls, page, _title) in tables.items():
            key = normkey(cls)
            if key in by_key:
                rows.append((by_key[key], pdf_stem, tid, page))
                continue
            tail = rescue_caption_name(pdf_path, tid, page, helper)
            if tail and normkey(tail) in by_key:
                display = by_key[normkey(tail)]
                rows.append((display, pdf_stem, tid, page))
                rescued.append((display, pdf_stem, tid, page, cls))
                continue
            unmatched.setdefault(cls, []).append("%s Table %s" % (pdf_stem, tid))
    return rows, rescued, unmatched


def main():
    helper = load_pdf_helper()
    helper.CACHED_READERS = {}
    release_order = {name: i for i, (name, _m, _p) in enumerate(RELEASES)}
    release_rows = {}
    for release, md_glob, pdf_glob in RELEASES:
        md_paths = sorted(glob.glob(os.path.join(REPO_ROOT, md_glob)))
        pdf_paths = sorted(glob.glob(os.path.join(REPO_ROOT, pdf_glob)))
        if not md_paths or not pdf_paths:
            sys.exit("error: empty corpus for %s (md=%d, pdf=%d)" % (release, len(md_paths), len(pdf_paths)))
        by_key, kind_counts = harvest_markdown_whitelist(md_paths)
        rows, rescued, unmatched = scan_release_pdfs(pdf_paths, by_key, helper)
        release_rows[release] = rows
        print(
            "%s: %d md files -> %d whitelist names (Class %d / Enumeration %d / Primitive %d); "
            "%d pdf files -> %d caption rows (%d rescued)"
            % (
                release,
                len(md_paths),
                len(kind_counts["Class"]) + len(kind_counts["Enumeration"]) + len(kind_counts["Primitive"]),
                len(kind_counts["Class"]),
                len(kind_counts["Enumeration"]),
                len(kind_counts["Primitive"]),
                len(pdf_paths),
                len(rows),
                len(rescued),
            )
        )
        for display, pdf_stem, tid, page, captured in rescued:
            print("  rescued: %s (%s captured as %r) -> %s Table %s p.%d" % (display, captured, captured, pdf_stem, tid, page))
        if unmatched:
            print("  captions not in whitelist (review for missed classes):")
            for cls in sorted(unmatched):
                print("    %s -> %s" % (cls, ", ".join(sorted(unmatched[cls])[:3])))

    header = [
        "# All AUTOSAR spec classes — alphabetical index",
        "",
        "Generated by `scripts/regen_all_classes.py` from the spec corpora under `autosar/` — do not edit by hand.",
        "",
        "Method: type-table names (header cells `| Class |` / `| Enumeration |` / `| Primitive |`) are harvested from",
        "the markdown corpora and matched against the `Table N.M:` captions extracted from the release PDFs; the page",
        "is the table's first PDF page (same convention and cache as `.agents/skills/sync-autosar-class/pdf_page.py`).",
        "",
        "Scope: R23-11 (15 TPS PDFs), R4.3.1 (11 TPS PDFs — RS_*/TR_* docs are not class specs), R3.2.3 (5 template",
        "PDFs, mostly caption-less → partial). `autosar/R4.4.0/` (xsd-only) and `autosar/ECUC/` (markdown-only) have",
        "no PDF, so no page numbers exist for them.",
        "",
        "Sorted by class name (A→Z, case-insensitive), then release (R23-11, R4.3.1, R3.2.3).",
        "",
    ]
    stats = ["| Release | Rows | Distinct names |", "| ------- | ---- | -------------- |"]
    sorted_rows = []
    for release, _md_glob, _pdf_glob in RELEASES:
        rows = sorted(set(release_rows[release]))
        distinct = {r[0] for r in rows}
        stats.append("| %s | %d | %d |" % (release, len(rows), len(distinct)))
        sorted_rows.extend((cls, pdf_stem, tid, page, release) for cls, pdf_stem, tid, page in rows)
    sorted_rows.sort(key=lambda r: (r[0].lower(), r[0], release_order[r[4]]))

    lines = header + stats + ["", "| Class | PDF | Table | Page | Release |", "| ----- | --- | ----- | ---- | ------- |"]
    for cls, pdf_stem, tid, page, release in sorted_rows:
        lines.append("| `%s` | %s | %s | %d | %s |" % (cls, pdf_stem, tid, page, release))
    lines.append("")
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("wrote %s (%d rows)" % (os.path.relpath(OUT_FILE, REPO_ROOT), len(sorted_rows)))


if __name__ == "__main__":
    main()
