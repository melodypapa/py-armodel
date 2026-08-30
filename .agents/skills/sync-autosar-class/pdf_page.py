#!/usr/bin/env python3
"""Find the AUTOSAR spec table (markdown/PDF) page number for a model class.

The AUTOSAR markdown tables carry no page numbers; the PDF must be opened only to
read the `p.NN` page used in the `# Spec:` checklist line. This script locates the
spec table header (`Table N.M: ClassName`) in the PDF(s) and prints the page number.

Usage:
  python pdf_page.py <ClassName>                 # search every autosar/R*/pdf/*.pdf (R23-11, R4.3.1, ...)
  python pdf_page.py <ClassName> --pdf PATH      # search a single PDF
  python pdf_page.py --table 13.24 [--pdf PATH]  # search by table id instead
  python pdf_page.py <ClassName> --refresh       # ignore the cached index

Output (one line per match):
  <release>/<pdf filename> | Table <N.M>: <ClassName> | p.<page>

A per-PDF text index is cached in `.pdf_table_cache.json` at the repo root (shared by
every copy of this script), keyed by the PDF's mtime, so repeated lookups do not
re-scan the PDFs.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

_REPO_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
CACHE_FILE = os.path.join(_REPO_ROOT, ".pdf_table_cache.json")
AUTOSAR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "autosar")


def _pypdf_text(reader, page_index):
    page = reader.pages[page_index]
    return page.extract_text() or ""


def scan_pdf(pdf_path):
    """Return {table_id: (class_name, page_number, title_line)} for the PDF."""
    from pypdf import PdfReader

    reader = PdfReader(pdf_path)
    tables = {}
    for i in range(len(reader.pages)):
        text = _pypdf_text(reader, i)
        if "Table" not in text:
            continue
        for m in re.finditer(r"Table\s+(\d+\.\d+)\s*:\s*([A-Za-z0-9][A-Za-z0-9_\-]*)", text):
            tid, cls = m.group(1), m.group(2)
            if tid not in tables:
                tables[tid] = [cls, i + 1, "Table %s: %s" % (tid, cls)]
    return tables


def load_cached_index():
    if os.path.exists(CACHE_FILE):
        try:
            return json.load(open(CACHE_FILE, encoding="utf-8"))
        except (ValueError, OSError):
            return {}
    return {}


def save_cached_index(index):
    try:
        json.dump(index, open(CACHE_FILE, "w", encoding="utf-8"), indent=1)
    except OSError:
        pass


def get_pdf_tables(pdf_path, refresh=False):
    index = load_cached_index()
    mtime = os.path.getmtime(pdf_path)
    entry = index.get(pdf_path)
    if not refresh and entry is not None and entry.get("mtime") == mtime and "tables" in entry:
        return entry["tables"]
    tables = scan_pdf(pdf_path)
    index[pdf_path] = {"mtime": mtime, "tables": tables}
    save_cached_index(index)
    return tables


def collect_pdfs(explicit_pdf=None):
    if explicit_pdf:
        if os.path.exists(explicit_pdf):
            return [explicit_pdf]
        sys.exit("error: PDF not found: %s" % explicit_pdf)
    pdf_dirs = []
    if os.path.isdir(AUTOSAR_DIR):
        for release in sorted(os.listdir(AUTOSAR_DIR)):
            pdf_dir = os.path.join(AUTOSAR_DIR, release, "pdf")
            if os.path.isdir(pdf_dir):
                pdf_dirs.append(pdf_dir)
    if not pdf_dirs:
        sys.exit("error: no autosar/R*/pdf directory found under %s" % AUTOSAR_DIR)
    pdfs = []
    for pdf_dir in pdf_dirs:
        pdfs.extend(sorted(os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if f.endswith(".pdf")))
    return pdfs


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("name", nargs="?", help="class name (or table id with --table)")
    parser.add_argument("--table", dest="by_table", action="store_true", help="treat NAME as a table id (e.g. 13.24)")
    parser.add_argument("--pdf", dest="pdf", default=None, help="path to a single PDF")
    parser.add_argument("--refresh", action="store_true", help="rescan PDFs, ignoring the cached index")
    args = parser.parse_args()

    if not args.name:
        parser.error("a class name (or --table with a table id) is required")

    pdfs = collect_pdfs(args.pdf)
    matches = []
    for pdf in pdfs:
        tables = get_pdf_tables(pdf, refresh=args.refresh)
        for tid, (cls, page, title) in tables.items():
            if args.by_table:
                if tid == args.name:
                    matches.append((pdf, title, page))
            else:
                if cls == args.name:
                    matches.append((pdf, title, page))

    if not matches:
        sys.exit("no spec table found for %r in %s" % (args.name, ", ".join(os.path.relpath(p, AUTOSAR_DIR) for p in pdfs)))

    for pdf_path, title, page in matches:
        print("%s/%s | %s | p.%d" % (os.path.basename(os.path.dirname(os.path.dirname(pdf_path))), os.path.basename(pdf_path), title, page))


if __name__ == "__main__":
    main()
