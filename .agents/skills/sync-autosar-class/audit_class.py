#!/usr/bin/env python3
"""Mechanical pre-stamp audit for one AUTOSAR model class.

Usage:
    python audit_class.py <ClassName> [<ClassName> ...]   # explicit classes
    python audit_class.py --file <path-to-src.py> [...]    # restrict the search
    python audit_class.py --all                           # every class in the tree
    python audit_class.py <ClassName> --json              # machine-readable

What it checks, and why each check is mechanical (a human should not have to
eyeball these — see Rule 0024 / 0025 in rules.md):

  BLOCK    the `# <Class> method parity checklist:` block is ONE contiguous run
           of comment lines that starts above `__init__` and ends before it, and
           every 6-column `[x] <method>` row in the class lives inside it.
           Catches accessor rows relocated into the `__init__` body — a shape a
           `[x]`-everything checklist renders indistinguishable from correct.

  ROWS     the block's rows equal the class's methods, in source order (AST, not
           text). Catches missing and extra rows.

  BASE     the reader/writer pair for the class calls the reader/writer helper of
           one of its model bases, so inherited `AR:AR-OBJECT` / `AR:REFERRABLE` /
           `AR:IDENTIFIABLE` state (S/T, UUID, SHORT-NAME-FRAGMENTS) round-trips.
           Rule 0013.1 forbids calling it *twice*; this catches never calling it
           at all, which is the same silent data loss in the other direction.

  MEMBER   the reader/writer pair for the class reaches the reader/writer helper
           of every class it aggregates (`List[M]` / `Optional[M]` members in
           `__init__`/`clear`, `createXxx` results, and mixin class-level
           members such as `VariationPointCapable.variationPoint`). A shared
           helper's existence is not evidence an aggregator calls it (Rule
           0001.7): a member whose helper is unreachable from the entry point
           is silently dropped on round-trip. Members with no helper of their
           own (inline emission per Rule 0025) only warn.

  DOC      `__init__` carries no docstring (Rule 0012.2.4). A `Tags:`/`Stereotypes:`
           tail in a class / `__init__` member / accessor docstring is **expected**
           and reported as INFO — the spec `Note` is copied verbatim including the
           tail (Rule 0012.2.5.3), and ~1000 stamped sites do the same.

  SPECLINE the `# Spec:` line is in canonical Rule 0002 form for a single-corpus
           class, or the R4.3.1-fallback form, or an explicit dual-line combine
           case (Rule 0019).

  SPEC-BASE the model class derives the most-derived base named by the spec
           table's Base row. An under-derived class (DefItem on ARObject where
           Table 9.16 ends in Referrable) silently drops the inherited
           SHORT-NAME from its XML while every checklist row reads [x].

  STAMP    `# Spec verified:` / `# XSD verified:` is present iff every row is
           `[x]`. A marker over unfinished rows certifies work that was never
           done (Rule 0012.1); a finished checklist without a marker is the
           normal state of a class awaiting its 9b gate. The marker must also
           sit immediately after the (last) `# Spec:` citation line — a
           displaced marker (after `# Columns:`, after the rows, or above the
           citation) is how independent stamping passes drift apart.

Exit code 0 when no FAIL, 1 otherwise. INFO/WARN never fail the run.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set, Tuple

_REPO_ROOT = Path(__file__).resolve().parents[3]
MODELS_DIR = Path("src/armodel/models")
PARSER = Path("src/armodel/parser/arxml_parser.py")
WRITER = Path("src/armodel/writer/arxml_writer.py")
# The shared base helpers (`readARObject` / `writeARObject` and friends) live on
# the abstract classes, so helper *existence* has to consider both modules —
# otherwise an `ARObject` subclass looks like it has no inherited level to call.
ABSTRACT_PARSER = Path("src/armodel/parser/abstract_arxml_parser.py")
ABSTRACT_WRITER = Path("src/armodel/writer/abstract_arxml_writer.py")

ROW_RE = re.compile(r"^#\s*\[([ x—])\]\s+(\S+)\s+\[([ x—])\]\s*impl\s+\[([ x—])\]\s*docstring\s+\[([ x—])\]\s*test\s+\[([ x—])\]\s*reader\s+\[([ x—])\]\s*writer\s+(\S+)\s*$")
ANY_ROW_RE = re.compile(r"^#\s*\[[ x—]\]\s+(\S+)\s+\[([ x—])\]\s*impl\s+\[([ x—])\]\s*docstring\s+\[([ x—])\]\s*test\b")
HEADER_RE_TMPL = r"^\s*#\s+{}\s+method parity checklist:\s*$"

RELEASE_TOKEN = r"\((?:R23-11|R4\.3\.1)\)"


class Report:
    def __init__(self) -> None:
        self.rows: List[Tuple[str, str, str]] = []  # (level, code, message)

    def fail(self, code: str, msg: str) -> None:
        self.rows.append(("FAIL", code, msg))

    def warn(self, code: str, msg: str) -> None:
        self.rows.append(("WARN", code, msg))

    def info(self, code: str, msg: str) -> None:
        self.rows.append(("INFO", code, msg))

    def ok(self, code: str, msg: str) -> None:
        self.rows.append(("ok", code, msg))

    @property
    def failed(self) -> bool:
        return any(lvl == "FAIL" for lvl, _, _ in self.rows)

    def as_dict(self) -> Dict[str, object]:
        return {
            "failures": [m for lvl, _, m in self.rows if lvl == "FAIL"],
            "warnings": [m for lvl, _, m in self.rows if lvl == "WARN"],
            "info": [m for lvl, _, m in self.rows if lvl == "INFO"],
        }


# --------------------------------------------------------------------------- #
# source loading
# --------------------------------------------------------------------------- #


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def find_source_files(classes: Sequence[str], explicit: Optional[Path], as_all: bool) -> List[Path]:
    if explicit is not None:
        return [explicit]
    if as_all:
        return sorted(MODELS_DIR.rglob("*.py"))
    out: List[Path] = []
    for cls in classes:
        for path in sorted(MODELS_DIR.rglob("*.py")):
            if re.search(r"^\s*class\s+" + re.escape(cls) + r"\b", read(path), re.M):
                out.append(path)
                break
    return out


def resolve_targets(classes: Sequence[str], explicit: Optional[Path], as_all: bool) -> List[Tuple[str, Path]]:
    """Pair every class with the file that actually defines it, one target each."""
    out: List[Tuple[str, Path]] = []
    if as_all:
        for p in sorted(MODELS_DIR.rglob("*.py")):
            for c in iter_classes(p):
                out.append((c, p))
        return out
    paths = [explicit] if explicit is not None else find_source_files(classes, None, False)
    seen: Set[Tuple[str, str]] = set()
    for cls in classes:
        for p in paths:
            if p is None:
                continue
            if re.search(r"^\s*class\s+" + re.escape(cls) + r"\b", read(p), re.M):
                if (cls, str(p)) not in seen:
                    seen.add((cls, str(p)))
                    out.append((cls, p))
                break
    return out


def parse_module(path: Path) -> Tuple[str, List[str], ast.Module]:
    text = read(path)
    return text, text.splitlines(), ast.parse(text)


def class_node(tree: ast.Module, name: str) -> Optional[ast.ClassDef]:
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == name:
            return node
    return None


def base_names(node: ast.ClassDef) -> List[str]:
    out: List[str] = []
    for b in node.bases:
        if isinstance(b, ast.Name):
            out.append(b.id)
        elif isinstance(b, ast.Attribute):
            out.append(b.attr)
        elif isinstance(b, ast.Call):  # e.g. VariationPointCapable mixin call
            if isinstance(b.func, ast.Name):
                out.append(b.func.id)
    return out


def is_enum(node: ast.ClassDef) -> bool:
    return "AREnum" in base_names(node)


# --------------------------------------------------------------------------- #
# checklist block extraction
# --------------------------------------------------------------------------- #


def class_start(lines: Sequence[str], cls: str) -> int:
    pat = re.compile(r"^\s*class\s+" + re.escape(cls) + r"\b")
    for i, line in enumerate(lines):
        if pat.match(line):
            return i
    return -1


def class_end(lines: Sequence[str], start: int) -> int:
    """End of the class body.

    The class's own methods are indented *deeper* than the `class` line, so the
    end is the next line at the class's own indent (or shallower) that starts a
    new definition. Stopping at the first `def` would truncate the body before
    `__init__` and silently disable the BLOCK check.
    """
    cls_indent = len(lines[start]) - len(lines[start].lstrip())
    pat = re.compile(r"\s*(?:class\s|def\s|@|async\s+def\s)")
    for i in range(start + 1, len(lines)):
        line = lines[i]
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        if indent <= cls_indent and pat.match(line):
            return i
    return len(lines)


def init_line(lines: Sequence[str], start: int, end: int) -> int:
    for i in range(start, end):
        if re.match(r"^\s*def\s+__init__\s*\(", lines[i]):
            return i
    return -1


def collect_block(lines: Sequence[str], cls: str) -> Optional[Tuple[int, int, List[str]]]:
    """Return (start, end_exclusive, stripped_lines) of the checklist block."""
    hdr = re.compile(HEADER_RE_TMPL.format(re.escape(cls)))
    hits = [i for i, line in enumerate(lines) if hdr.match(line)]
    if not hits:
        return None
    if len(hits) > 1:
        # caller reports the duplicate
        return (hits[0], hits[0], [])
    i = hits[0]
    j = i
    out: List[str] = []
    while j < len(lines):
        line = lines[j]
        if line.strip() == "":
            k = j + 1
            while k < len(lines) and lines[k].strip() == "":
                k += 1
            if k < len(lines) and lines[k].lstrip().startswith("#"):
                j = k
                continue
            break
        if line.lstrip().startswith("#"):
            out.append(line.strip())
            j += 1
            continue
        break
    return (i, j, out)


# --------------------------------------------------------------------------- #
# checks
# --------------------------------------------------------------------------- #


def check_block(rep: Report, cls: str, lines: Sequence[str], start: int, end: int) -> None:
    hdr = re.compile(HEADER_RE_TMPL.format(re.escape(cls)))
    hdrs = [i for i in range(start, end) if hdr.match(lines[i])]
    if not hdrs:
        rep.fail("BLOCK", "no `# %s method parity checklist:` header in the class body" % cls)
        return
    if len(hdrs) > 1:
        rep.fail("BLOCK", "%d checklist headers in the class body (lines %s) — exactly one is allowed" % (len(hdrs), ", ".join(str(h + 1) for h in hdrs)))
    blk = collect_block(lines, cls)
    assert blk is not None
    b_start, b_end, blk_lines = blk
    init = init_line(lines, start, end)
    if init == -1:
        rep.warn("BLOCK", "no `__init__` found; cannot prove the block sits above it")
    else:
        if b_start > init:
            rep.fail("BLOCK", "checklist block starts at line %d, AFTER `__init__` (line %d) — the block belongs above the constructor" % (b_start + 1, init + 1))
        elif b_end > init:
            rep.fail("BLOCK", "checklist block runs to line %d, past `__init__` (line %d) — the block must be one contiguous run above the constructor" % (b_end, init + 1))
        else:
            rep.ok("BLOCK", "checklist block is one contiguous run (lines %d-%d) above `__init__` (line %d)" % (b_start + 1, b_end, init + 1))

    in_block = set(range(b_start, b_end))
    strays: List[Tuple[int, str]] = []
    for i in range(start, end):
        if i in in_block:
            continue
        m = ANY_ROW_RE.match(lines[i].strip())
        if m:
            strays.append((i + 1, m.group(1)))
    if strays:
        rep.fail(
            "BLOCK",
            "checklist row(s) outside the block: %s — accessor rows must live in the checklist block, not scattered through the class body"
            % ", ".join("line %d (`%s`)" % (ln, nm) for ln, nm in strays),
        )
    else:
        rep.ok("BLOCK", "no checklist rows scattered outside the block")


def check_rows(rep: Report, cls: str, node: ast.ClassDef, blk_lines: Sequence[str]) -> None:
    methods = [n.name for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    rows: List[str] = []
    unparsed: List[str] = []
    for line in blk_lines:
        m = ANY_ROW_RE.match(line)
        if not m:
            continue
        rm = ROW_RE.match(line)
        if rm:
            rows.append(rm.group(2))
        else:
            unparsed.append(m.group(1))
    if unparsed:
        rep.fail("ROWS", "row(s) not in the 6-column format (impl/docstring/test/reader/writer/release): %s" % ", ".join(unparsed))
    if rows != methods:
        missing = [m for m in methods if m not in rows]
        extra = [r for r in rows if r not in methods]
        detail = []
        if missing:
            detail.append("missing from checklist: %s" % ", ".join(missing))
        if extra:
            detail.append("not a method: %s" % ", ".join(extra))
        if not detail and rows:
            detail.append("checklist order %s != source order %s" % (rows, methods))
        if detail:
            rep.fail("ROWS", "%d method(s) vs %d checklist row(s) — %s" % (len(methods), len(rows), "; ".join(detail)))
    else:
        rep.ok("ROWS", "checklist == methods, %d rows in source order" % len(rows))


def check_spacing(rep: Report, lines: Sequence[str], start: int, end: int) -> None:
    """Rule 0008: every `__init__` attribute block must be separated by a blank line.

    Black and ruff cap the *maximum* blank lines, never a *minimum*, so glued-together
    fields pass every other check in this file. That is why this reads the raw text:
    the AST cannot see blank lines at all.
    """
    init = init_line(lines, start, end)
    if init == -1:
        return
    stop = init + 1
    while stop < end and not re.match(r"^\s{4}def\s", lines[stop]):
        stop += 1
    attr = re.compile(r"^\s+self\.\w+\s*[:=]")
    offenders: List[str] = []
    prev: Optional[int] = None
    for i in range(init + 1, stop):
        if not attr.match(lines[i]):
            continue
        if prev is not None and not any(not lines[j].strip() for j in range(prev + 1, i)):
            offenders.append(lines[prev].strip())
        prev = i
    if offenders:
        rep.fail("SPACING", "Rule 0008: `__init__` attribute blocks must be separated by a blank line; %d glued pair(s), first: %s" % (len(offenders), offenders[0]))
    else:
        rep.ok("SPACING", "`__init__` attribute blocks are blank-line separated")


def _docstring_of(node: ast.ClassDef, name: str) -> Optional[str]:
    for fn in node.body:
        if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)) and fn.name == name:
            return ast.get_docstring(fn)
    return None


def check_doc_tail(rep: Report, node: ast.ClassDef, lines: Sequence[str], start: int, end: int) -> None:
    """Rule 0012.2.5.3: a `Tags:`/`Stereotypes:` tail belongs at *every* level.

    The spec `Note` is copied verbatim, tail included, onto the `__init__` comment, the
    getter and the setter. A tail that reaches the comment but not the accessors is
    still a verbatim-fidelity defect, and one no existing check can see.
    """
    # Two patterns on purpose. A docstring's tail sits on an inner line, so the
    # presence test must not be `$`-anchored (that was a real false-positive bug:
    # it failed every accessor whose tail was followed by a Returns: block).
    # The content pattern is only ever applied to a single comment line.
    tail_line = re.compile(r"\b(?:Tags|Stereotypes):(.*)$")
    tail_any = re.compile(r"\b(?:Tags|Stereotypes):")
    init = init_line(lines, start, end)
    if init == -1:
        return
    stop = init + 1
    while stop < end and not re.match(r"^\s{4}def\s", lines[stop]):
        stop += 1
    semantic: List[str] = []
    schema: List[str] = []
    for i in range(init + 1, stop):
        m = re.match(r"^\s+self\.(\w+)\s*[:=]", lines[i])
        if not m:
            continue
        comment = ""
        j = i - 1
        while j > init and lines[j].strip().startswith("#"):
            comment = lines[j].strip() + " " + comment
            j -= 1
        tm = tail_line.search(comment)
        if not tm:
            continue
        member = m.group(1)
        acc = member[0].upper() + member[1:]
        names = [n for n in ("get" + acc, "set" + acc, "add" + acc) if any(isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef)) and f.name == n for f in node.body)]
        for n in names:
            doc = _docstring_of(node, n) or ""
            if tail_any.search(doc):
                continue
            # atp.* / Stereotypes: carry meaning (enum indexes, stereotypes, split
            # keys) and are part of the verbatim Note, so dropping them is a real
            # fidelity defect. xml.* is schema plumbing — the accessor's job is the
            # value, not the sequence offset — so that one only warns.
            bucket = semantic if ("atp." in tm.group(1) or "Stereotypes" in comment) else schema
            bucket.append("%s.%s" % (node.name, n))
    if semantic:
        rep.fail("DOCTAIL", "Rule 0012.2.5.3: the `atp.`/`Stereotypes:` tail is part of the verbatim Note and is kept on the `__init__` comment but missing from %d accessor docstring(s): %s" % (len(semantic), ", ".join(semantic[:4])))
    if schema:
        rep.warn("DOCTAIL", "%d accessor docstring(s) omit the `xml.*` schema tags carried by their `__init__` comment (cosmetic, not spec fidelity): %s" % (len(schema), ", ".join(schema[:4])))
    if not semantic and not schema:
        rep.ok("DOCTAIL", "`Tags:`/`Stereotypes:` tails reach every accessor docstring")


@lru_cache(maxsize=None)
def _spec_tables() -> Dict[str, Dict[str, List[str]]]:
    """{corpus: {document: {table id: [captions]}}} built from the markdown corpus.

    Table ids are only unique *within* a document — E.38 is `EnumerationMappingTable`
    in GenericStructureTemplate and `Referrable` in SoftwareComponentTemplate — so a
    citation can only be validated as a (document, table id) pair.
    """
    out: Dict[str, Dict[str, List[str]]] = {}
    for corpus in ("R23-11", "R4.3.1"):
        base = _REPO_ROOT / "autosar" / corpus / "markdown"
        docs: Dict[str, List[str]] = {}
        if not base.is_dir():
            out[corpus] = {}
            continue
        for path in sorted(base.glob("*.md")):
            found: Dict[str, List[str]] = {}
            for m in re.finditer(r"^#{0,3}\s*Table\s+([0-9A-Z]+\.[0-9]+):\s*(.+)$", path.read_text(encoding="utf-8", errors="replace"), re.M):
                found.setdefault(m.group(1), []).append(m.group(2).strip())
            docs[path.stem] = found
        out[corpus] = docs
    return out


_CITATION_RE = re.compile(r"AUTOSAR_(?:(CP|FO|AP)_TPS_)?(\w+)\.pdf.*?Table\s+([0-9A-Z]+\.[0-9]+)")


def check_citation(rep: Report, cls: str, blk_lines: Sequence[str]) -> None:
    """Rule 0002: the `# Spec:` citation must name a table that really defines this class.

    A citation is the only pointer from code back to the spec, so a dangling one makes
    the whole class unverifiable. Aliases and cross-document reproductions are reported
    as warnings rather than failures — they are legitimate, just not the defining table.
    """
    specs = [x for x in blk_lines if x.startswith("# Spec:")]
    if not specs:
        return
    line = specs[0]
    if "xsd" in line:  # XSD-only class: no PDF table by definition
        rep.ok("CITATION", "XSD-only class — provenance is the schema, not a PDF table")
        return
    m = _CITATION_RE.search(line)
    if not m:
        rep.info("CITATION", "`# Spec:` line not in the `<pdf>, Table N.M` form — confirm the citation by hand")
        return
    platform, template, table_id = m.group(1), m.group(2), m.group(3)
    corpus = "R4.3.1" if platform is None else "R23-11"
    doc = f"AUTOSAR_{platform}_TPS_{template}" if platform else f"AUTOSAR_TPS_{template}"
    docs = _spec_tables().get(corpus) or {}
    if doc not in docs:
        rep.info("CITATION", "cited document %s is not in the %s corpus — verify the citation by hand" % (doc, corpus))
        return
    if table_id not in docs[doc]:
        rep.fail("CITATION", "`# Spec:` cites %s, Table %s, but that document has no such table — the citation cannot be verified" % (doc, table_id))
        return
    captions = docs[doc][table_id]
    # A src name that is the spec caption plus a disambiguating prefix is a recorded
    # rename (ARList for `List`), not a mis-citation.
    if any(cls.lower() in c.lower() or cls.lower().endswith(c.lower()) for c in captions):
        rep.ok("CITATION", "Table %s of %s defines %s" % (table_id, doc, cls))
        return
    # The caption is a different class. Either this class is documented elsewhere (a
    # reproduction or a recorded rename) or the citation is simply wrong.
    for other, tables in docs.items():
        for tid, caps in tables.items():
            if any(cls.lower() == c.lower() for c in caps):
                rep.warn("CITATION", "Table %s of %s is captioned %s, not %s — %s is defined in %s Table %s (recorded rename or cross-document reproduction; prefer the defining table)" % (table_id, doc, "/".join(captions), cls, cls, other, tid))
                return
    rep.fail("CITATION", "`# Spec:` cites %s, Table %s, captioned %s — that table does not define %s and no other table in the corpus does either" % (doc, table_id, "/".join(captions), cls))


@lru_cache(maxsize=None)
def _spec_base_rows() -> Dict[Tuple[str, str, str], Optional[Tuple[str, ...]]]:
    """{(corpus, doc, table id): Base-row class names} extracted from the corpus.

    Page-split rendering repeats a table's caption around page-break images and
    may split the body into several '|' blocks. Each block is attributed to the
    NEAREST caption (the page-split layout always puts a table's body adjacent to
    one of its own captions), and a table id's Base row is the merge of its
    attributed blocks' rows. Tables with no attributed Base row map to None.
    """
    out: Dict[Tuple[str, str, str], Optional[Tuple[str, ...]]] = {}
    caption_re = re.compile(r"^#{0,3}\s*Table\s+([0-9A-Z]+\.[0-9]+):\s*(.+)$")
    for corpus in ("R23-11", "R4.3.1"):
        base = _REPO_ROOT / "autosar" / corpus / "markdown"
        if not base.is_dir():
            continue
        for path in sorted(base.glob("*.md")):
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            blocks: List[Tuple[int, int]] = []
            i = 0
            while i < len(lines):
                if lines[i].lstrip().startswith("|"):
                    j = i
                    while j < len(lines) and lines[j].lstrip().startswith("|"):
                        j += 1
                    blocks.append((i, j))
                    i = j
                else:
                    i += 1
            caps: List[Tuple[int, str]] = []
            for k, line in enumerate(lines):
                m = caption_re.match(line)
                if m:
                    caps.append((k, m.group(1)))
            attributed: Dict[str, List[str]] = {}
            for b_start, b_end in blocks:
                if not caps:
                    break
                mid = (b_start + b_end - 1) / 2
                pos, table_id = min(caps, key=lambda c: abs(c[0] - mid))
                for line in lines[b_start:b_end]:
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    if cells and cells[0].lower() == "base":
                        for cell in cells[1:]:
                            for n in cell.split(","):
                                n = n.strip()
                                if n and n != "-" and n not in attributed.setdefault(table_id, []):
                                    attributed[table_id].append(n)
            for table_id, names in attributed.items():
                out[(corpus, path.stem, table_id)] = tuple(names) if names else None
    return out


def _late_binds() -> Dict[str, List[str]]:
    """Classes rebased at import time via `ClassName.__bases__ = (...)`.

    The ARElement late-bind (ARPackage.py) gives classes like AclPermission their
    real base only at runtime — invisible to a pure AST base walk, which makes an
    under-derived verdict a false positive for every late-bound class."""
    out: Dict[str, List[str]] = {}
    for p in MODELS_DIR.rglob("*.py"):
        try:
            t = ast.parse(read(p))
        except SyntaxError:
            continue
        for n in ast.walk(t):
            if not isinstance(n, ast.Assign) or len(n.targets) != 1:
                continue
            target = n.targets[0]
            if not (isinstance(target, ast.Attribute) and target.attr == "__bases__" and isinstance(target.value, ast.Name)):
                continue
            value = n.value
            names = []
            if isinstance(value, ast.Tuple):
                names = [e.id for e in value.elts if isinstance(e, ast.Name)]
            elif isinstance(value, ast.Name):
                names = [value.id]
            if names:
                out.setdefault(target.value.id, names)
    return out


def _ancestor_closure(cls: str, base_map: Dict[str, List[str]]) -> Set[str]:
    seen: Set[str] = set()
    frontier = list(base_map.get(cls, []))
    while frontier:
        b = frontier.pop(0)
        if b in seen:
            continue
        seen.add(b)
        frontier.extend(base_map.get(b, []))
    return seen


def _most_derived(candidates: Set[str], base_map: Dict[str, List[str]]) -> Optional[str]:
    """The candidate that has all the others as ancestors, or None when ambiguous."""
    best: Optional[str] = None
    for c in candidates:
        others = candidates - {c}
        if others <= _ancestor_closure(c, base_map):
            return c
        if best is None or len(_ancestor_closure(c, base_map) & candidates) > len(_ancestor_closure(best, base_map) & candidates):
            best = c
    return best


def check_spec_base(rep: Report, cls: str, blk_lines: Sequence[str], enum: bool) -> None:
    """Rule 0001.2, mechanical: the model class must derive the most-derived base
    the spec table's Base row names.

    The round-trip tests and the field↔spec cross-check are blind to a wrong base:
    an under-derived class (DefItem modeled on plain ARObject where Table 9.16's
    Base row ends in Referrable) silently drops the inherited SHORT-NAME from its
    XML — and its checklist can still read all-[x]. The Base row lists the whole
    inheritance chain flattened; the most-derived name in it that is modeled in
    the repo is what the class must actually inherit from. The row may flatten a
    multi-inheritance chain the linear repo model cannot express exactly — the
    most-derived pick is then best-effort, and the FAIL is the prompt to decide
    the layout, not a mechanical verdict. Page-split attribution of the row is
    heuristic too; triage belongs in the audit baseline, not in silent skips."""
    if enum:
        return
    specs = [x for x in blk_lines if x.startswith("# Spec:")]
    if not specs or "xsd" in specs[0]:
        return
    m = _CITATION_RE.search(specs[0])
    if not m:
        return
    platform, template, table_id = m.group(1), m.group(2), m.group(3)
    corpus = "R4.3.1" if platform is None else "R23-11"
    doc = f"AUTOSAR_{platform}_TPS_{template}" if platform else f"AUTOSAR_TPS_{template}"
    row = _spec_base_rows().get((corpus, doc, table_id))
    if row is None:
        rep.info("SPEC-BASE", "Table %s of %s carries no readable Base row — base verified by 9b eye check" % (table_id, doc))
        return
    base_map = _model_base_map()
    if _is_value_carried(cls, base_map):
        return
    modeled = {n for n in row if n in base_map}
    if not modeled:
        rep.info("SPEC-BASE", "Base row %s names no modeled class — base verified by 9b eye check" % ", ".join(row))
        return
    spec_top = _most_derived(modeled, base_map)
    if spec_top is None:
        rep.warn("SPEC-BASE", "Base row %s has no unambiguous most-derived modeled class — verify by hand" % ", ".join(sorted(modeled)))
        return
    # Late-bound classes get their real base only at import time; judge them by
    # the effective chain, not the AST declaration.
    late = _late_binds().get(cls)
    effective_map = dict(base_map)
    if late:
        effective_map[cls] = late
    chain = {cls} | _ancestor_closure(cls, effective_map)
    reachable = chain & modeled
    if not reachable:
        rep.fail("SPEC-BASE", "%s derives none of the spec Base row's modeled classes %s — the inheritance chain (e.g. Referrable's SHORT-NAME) is silently absent" % (cls, ", ".join(sorted(modeled))))
        return
    model_top = _most_derived(reachable, effective_map)
    if model_top == spec_top:
        rep.ok("SPEC-BASE", "derives %s — the most-derived modeled class of the Base row" % model_top)
    elif model_top in _ancestor_closure(spec_top, base_map) | {spec_top}:
        rep.fail("SPEC-BASE", "%s derives %s but the Base row's most-derived modeled class is %s — under-derived; %s's inherited members (SHORT-NAME, UUID, …) never serialize" % (cls, model_top, spec_top, spec_top))
    else:
        rep.warn("SPEC-BASE", "%s derives %s, outside the Base row's modeled set %s — over-derivation or recorded deviation; verify by hand" % (cls, model_top, ", ".join(sorted(modeled))))


def check_stamp(rep: Report, blk_lines: Sequence[str]) -> None:
    spec_ver = [x for x in blk_lines if x.startswith("# Spec verified:")]
    xsd_ver = [x for x in blk_lines if x.startswith("# XSD verified:")]
    markers = spec_ver + xsd_ver
    if len(markers) > 1:
        rep.fail("STAMP", "%d provenance markers in one block (%s) — exactly one is allowed" % (len(markers), "; ".join(markers)))
        # Stop here: with two markers the block's provenance is ambiguous, so it is
        # meaningless to go on and report the first one as a clean certification.
        return
    # Rule 0012.1 adjacency: the marker sits immediately after the (last) `# Spec:`
    # citation line, before `# Columns:` and the rows. A wrapped citation (`# Spec:`
    # followed by a non-`key:` comment line) counts as part of the citation, so the
    # scan skips continuation lines — a continuation is anything that is neither a
    # `# Something:` key line nor a checklist row. Dual-corpus classes (Rule 0019)
    # list all their `# Spec:` lines first, so keying on the LAST one is correct.
    spec_idx = [i for i, x in enumerate(blk_lines) if x.startswith("# Spec:")]
    if markers and spec_idx:
        key_like = re.compile(r"^#\s*[A-Za-z][A-Za-z0-9 .\-]*:\s")  # `# Columns:`, the marker itself, ...
        row_like = re.compile(r"^#\s*\[[ x—]\]")
        j = spec_idx[-1] + 1
        while j < len(blk_lines) and not key_like.match(blk_lines[j]) and not row_like.match(blk_lines[j]):
            j += 1  # wrapped continuation of the citation itself
        if j >= len(blk_lines) or not (blk_lines[j].startswith("# Spec verified:") or blk_lines[j].startswith("# XSD verified:")):
            rep.fail(
                "STAMP",
                "Rule 0012.1: the marker must sit immediately after the (last) `# Spec:` line — this marker is displaced (expected at block line %d, found at %d); move it up so the citation reads Spec → marker → Columns → rows"
                % (j + 1 if j < len(blk_lines) else len(blk_lines) + 1, blk_lines.index(markers[0]) + 1),
            )
            return
    ticks = [ROW_RE.match(x).group(1) for x in blk_lines if ROW_RE.match(x)]
    all_x = bool(ticks) and all(t == "x" for t in ticks)
    any_open = any(t != "x" for t in ticks)
    if markers and any_open:
        rep.fail("STAMP", "provenance marker present while %d checklist row(s) are not `[x]` — a marker certifies finished work" % sum(1 for t in ticks if t != "x"))
    elif markers and not all_x:
        rep.warn("STAMP", "marker present but the checklist has no `[x]` rows to certify")
    elif not markers and all_x:
        rep.info("STAMP", "checklist fully `[x]` with no marker — normal state before the 9b gate; stamp only after explicit user confirmation")
    elif not markers:
        rep.info("STAMP", "no marker, checklist incomplete — correct for an unsynced class")
    else:
        rep.ok("STAMP", "marker `%s` with all %d rows `[x]`" % (markers[0].lstrip("# ").strip(), len(ticks)))


def check_specline(rep: Report, cls: str, blk_lines: Sequence[str]) -> None:
    specs = [x for x in blk_lines if x.startswith("# Spec:")]
    if not specs:
        rep.fail("SPECLINE", "no `# Spec:` citation line in the block")
        return
    if len(specs) > 1:
        rep.ok("SPECLINE", "dual `# Spec:` line (%d citations) — combine case per Rule 0019" % len(specs))
        return
    line = specs[0]
    if re.search(r"^(R23-11|R4\.3\.1)/", line):
        rep.warn(
            "SPECLINE",
            "`# Spec:` uses the Rule-0019 corpus prefix `%s` — only a combine-case class carries that; a single-corpus class cites the PDF name directly" % line[len("# Spec: ") :].split("/")[0],
        )
    if re.search(r"\s" + RELEASE_TOKEN + r"\s*$", line):
        rep.warn(
            "SPECLINE", "`# Spec:` ends with a bare `%s` suffix — a single-corpus class takes the release from the marker, not the citation" % re.search(r"(" + RELEASE_TOKEN + r")\s*$", line).group(1)
        )
    if re.search(r"\.pdf\s+" + RELEASE_TOKEN + r",", line):
        rep.ok("SPECLINE", "`# Spec:` uses the R4.3.1-fallback form (release after the PDF name)")
    elif not re.search(r"^(R\d|R4)", line.split(",")[-1].strip()):
        rep.ok("SPECLINE", "`# Spec:` is in canonical single-corpus form")
    else:
        rep.info("SPECLINE", "`# Spec:` — confirm the citation form against Rule 0002 for this class")


def check_docs(rep: Report, node: ast.ClassDef, blk_lines: Sequence[str], enum: bool) -> None:
    """`__init__` must have no docstring (Rule 0012.2.4) — that is the only failure
    here.

    A `Tags:` / `Stereotypes:` tail is **expected**: the spec `Note` is copied
    verbatim including the tail, at every level (Rule 0012.2.5.3). It is reported
    as `INFO` so a reviewer can see it, never as something to strip.
    """
    tail = re.compile(r"\b(?:Tags|Stereotypes):")
    where: List[str] = []
    cls_doc = ast.get_docstring(node) or ""
    if tail.search(cls_doc):
        where.append("class")
    has_init_doc = False
    for fn in [n for n in node.body if isinstance(n, ast.FunctionDef)]:
        if fn.name == "__init__":
            if ast.get_docstring(fn) is not None:
                has_init_doc = True
            continue
        d = ast.get_docstring(fn) or ""
        if tail.search(d):
            where.append("`%s`" % fn.name)
    if has_init_doc:
        rep.fail("DOC", "`__init__` has a docstring — the class Note belongs in the class docstring only (Rule 0012.2.4)")
    if where:
        rep.info(
            "DOC", "`Tags:`/`Stereotypes:` tail kept verbatim in %d place(s) (%s) — expected per Rule 0012.2.5.3, nothing to fix" % (len(where), ", ".join(where[:4]) + ("…" if len(where) > 4 else ""))
        )
    else:
        rep.ok("DOC", "no `Tags:`/`Stereotypes:` tail present (fine — the tail is kept when the spec Note has one)")
    if not has_init_doc:
        rep.ok("DOC", "`__init__` has no docstring")


@lru_cache(maxsize=None)
def collect_calls(path: Path) -> Dict[str, Set[str]]:
    """Map function name -> set of attribute/method names it calls.

    Cached: a whole-tree sweep calls this once per run, and re-parsing the
    20k-line parser/writer for every class is what made repo-wide audits
    quadratic.
    """
    out: Dict[str, Set[str]] = {}
    if not path.exists():
        return out
    tree = ast.parse(read(path))
    for n in ast.walk(tree):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            calls: Set[str] = set()
            for c in ast.walk(n):
                if isinstance(c, ast.Call):
                    f = c.func
                    if isinstance(f, ast.Attribute):
                        calls.add(f.attr)
                    elif isinstance(f, ast.Name):
                        calls.add(f.id)
            out[n.name] = calls
    return out


@lru_cache(maxsize=None)
def _model_base_map() -> Dict[str, List[str]]:
    out: Dict[str, List[str]] = {}
    for p in MODELS_DIR.rglob("*.py"):
        try:
            t = ast.parse(read(p))
        except SyntaxError:
            continue
        for n in ast.walk(t):
            if isinstance(n, ast.ClassDef):
                out.setdefault(n.name, base_names(n))
    return out


@lru_cache(maxsize=None)
def known_helper_names(*paths: Path) -> Set[str]:
    """Every reader/writer helper name reachable from these modules, including
    the ones inherited from the abstract base classes."""
    names: Set[str] = set()
    for p in paths:
        if not p.exists():
            continue
        try:
            tree = ast.parse(read(p))
        except SyntaxError:
            continue
        for n in ast.walk(tree):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                names.add(n.name)
    return names


def _state_bases(cls: str, base_map: Dict[str, List[str]], known: Set[str]) -> List[str]:
    """Ancestors of `cls` that own a `read<Name>` helper — i.e. the levels that
    carry inherited state (S/T, UUID, SHORT-NAME-FRAGMENTS). Mixins and abstract
    placeholders (`ABC`, `VariationPointCapable`, `PackageableElement`, …) have
    no such helper and are correctly ignored."""
    out: List[str] = []
    seen: Set[str] = {cls}
    frontier = list(base_map.get(cls, []))
    while frontier:
        b = frontier.pop(0)
        if b in seen:
            continue
        seen.add(b)
        if ("read" + b) in known:
            out.append(b)
        frontier.extend(base_map.get(b, []))
    return out


def _camel_segments(name: str) -> List[str]:
    return [p for p in re.findall(r"[A-Z][a-z0-9]*|[a-z0-9]+", name) if len(p) > 2]


def _entry_points(mc: Dict[str, Set[str]], primaries: Sequence[str], hooks: Sequence[str], cls: str) -> List[str]:
    """The function that owns reading/writing this class.

    A class is reached either through a dedicated helper or inline from its
    aggregator, and the repo's naming is not uniform: the writer helper may be
    `writeXxx` *or* `setXxx` (`setDoIpEntity`), the reader helper `readXxx` *or*
    `getXxx` (`getTpPort`). A dedicated helper is preferred; otherwise fall back
    to functions that construct/reach the class, then to aggregator functions
    whose name mentions it (`writeEthernetPhysicalChannelVlan` for `VlanConfig`,
    emitted through the parent's `getVlan`).
    """
    for prim in primaries:
        if prim in mc:
            return [prim]
    hits = {fn for fn, calls in mc.items() if any(h in calls for h in hooks)}
    if hits:
        return sorted(hits)
    segments = _camel_segments(cls)
    # the leading token is the class's distinguishing name ("Vlan" in
    # VlanConfig); later tokens like "Config" are too generic to match on
    lead = segments[0] if segments else cls
    named = sorted(fn for fn in mc if fn not in primaries and lead in fn)
    return named


# How far a reader/writer may delegate before we stop crediting it with the
# inherited level. Measured against the tree: reachability saturates at 3 hops —
# depth 5 and unbounded find nothing extra — so a deeper walk would only make the
# check more permissive without surfacing another real gap.
_REACH_DEPTH = 3
# Member dispatch nests deeper than base-helper delegation ("Dispatch nests — a
# subtype that itself aggregates is its own dispatcher", Rule 0001.7): the System
# chapter path alone is 4 hops (readSystem → readSystemDocumentations →
# readSystemDocumentation → readSwComponentDocumentationElement → createChapter).
# Member targets are member-name-specific (unlike the generic readARObject), so a
# deeper walk stays safe here.
_MEMBER_REACH_DEPTH = 6


@lru_cache(maxsize=None)
def _reaches(side: str, fn: str, targets: frozenset, depth: int = _REACH_DEPTH) -> bool:
    """Does `fn` call one of `targets`, directly or via <= `depth` helpers?

    Delegation is normal in this codebase (a reader for a concrete class often
    calls a helper for a base class, which is what calls readIdentifiable), so a
    purely single-hop check reports inherited state as dropped when it is in fact
    preserved — the false positive that made 93 classes look defective.
    """
    if fn in targets:
        return True
    graph = collect_calls(PARSER) if side == "parser" else collect_calls(WRITER)
    seen = {fn}
    frontier = [(fn, 0)]
    while frontier:
        cur, d = frontier.pop()
        if d >= depth:
            continue
        for nxt in graph.get(cur, ()):
            if nxt in targets:
                return True
            if nxt not in seen:
                seen.add(nxt)
                frontier.append((nxt, d + 1))
    return False


def _reaches_any(side: str, entry_points: Sequence[str], targets: Set[str], depth: int = _REACH_DEPTH) -> Optional[str]:
    """The first entry point that reaches one of `targets`, directly or transitively."""
    frozen = frozenset(targets)
    for fn in entry_points:
        if _reaches(side, fn, frozen, depth):
            return fn
    return None


def check_base(rep: Report, cls: str, node: ast.ClassDef, enum: bool) -> None:
    if enum:
        rep.ok("BASE", "enum — serialized as an attribute value, no reader/writer pair of its own")
        return
    base_map = _model_base_map()
    pcalls = collect_calls(PARSER)
    wcalls = collect_calls(WRITER)
    if not pcalls or not wcalls:
        rep.warn("BASE", "parser/writer source not found — skipped")
        return
    known = known_helper_names(PARSER, ABSTRACT_PARSER)
    bases = _state_bases(cls, base_map, known)
    if not bases:
        rep.info("BASE", "no ancestor owns a `read<Name>` helper — no inherited level to call")
        return
    want_r = {"read" + b for b in bases}
    want_w = {"write" + b for b in bases}
    if "ARType" in bases:
        # ARLiteral-family primitives carry no XML element of their own; their
        # value (and the T timestamp) is read/written through the typed leaf
        # helper getChildElementOptional<Cls> / setChildElementOptional<Cls>,
        # which calls readARType / writeARType on the instance itself. Such a
        # class has no read<Cls> / write<Cls> entry point of its own, and its
        # leading class-name token is generic (e.g. "Category" in
        # "CategoryString"), so the entry-point trace below matches unrelated
        # functions and reports a false failure (NameToken, Integer, Boolean,
        # Float, RefType all fail the same way). Mirror the AREnum exemption:
        # pass when the typed leaf pair exists, warn (never fail) otherwise so
        # an attribute/text-carried primitive is not blocked — Rule 0013.2.
        known_w = known_helper_names(WRITER, ABSTRACT_WRITER)
        r_name = "getChildElementOptional" + cls
        w_name = "setChildElementOptional" + cls
        if r_name in known or w_name in known_w:
            rep.ok("BASE", "ARLiteral leaf pair %s/%s present — value serialized via the typed leaf helper (T preserved by readARType/writeARType)" % (r_name, w_name))
        else:
            rep.warn("BASE", "ARLiteral %s has no dedicated %s/%s leaf pair — verify it is attribute/text-carried or add the pair (Rule 0013.2)" % (cls, r_name, w_name))
        return

    # Entry-point confidence matters as much as reachability. A helper literally
    # named read<Cls>/write<Cls>/get<Cls>/set<Cls> is this class's own reader, so a
    # miss there is a real defect. Anything found by matching the class-name token
    # is a guess — the token is generic ("Access" in "AccessCount" matches
    # readAccessCountSets, a different class), so a miss proves nothing and must
    # not block. Guessed-but-unconfirmed is reported as a warning instead.
    confirmed_r = [f for f in ("read" + cls, "get" + cls) if f in pcalls]
    confirmed_w = [f for f in ("write" + cls, "set" + cls) if f in wcalls]
    r_pts = _entry_points(pcalls, ("read" + cls, "get" + cls), (cls, "create" + cls, "get" + cls), cls)
    w_pts = _entry_points(wcalls, ("write" + cls, "set" + cls), ("get" + cls, "set" + cls, "create" + cls), cls)

    hit = _reaches_any("parser", confirmed_r or r_pts, want_r)
    if hit:
        if want_r & pcalls[hit]:
            rep.ok("BASE", "reader entry point %s directly calls %s" % (hit, ", ".join(sorted(want_r))))
        else:
            # Say what was actually verified. This walk proves the call exists in the
            # subtree; it does NOT prove the call receives *this* instance, so a base
            # helper applied to some other object would also satisfy it. `TimeSynchronization`
            # is the known case: the tree reaches readARObject, yet S/T do not survive the
            # round-trip. Treat an indirect pass as a prompt to hand-verify, not a proof.
            rep.warn("BASE", "reader entry point %s reaches %s within %d calls, but indirectly — confirm the base helper is applied to THIS instance (an indirect hit can target another object, which silently drops S/T)" % (hit, "/".join(sorted(want_r)), _REACH_DEPTH))
    elif confirmed_r:
        rep.fail(
            "BASE",
            "no reader entry point calls a base reader helper (expected one of {%s}; entry points tried: %s) — inherited `S`/`T`, UUID and SHORT-NAME-FRAGMENTS are silently dropped on round-trip"
            % (", ".join(sorted(want_r)), ", ".join(confirmed_r[:4])),
        )
    elif r_pts:
        rep.warn(
            "BASE",
            "%s has no reader of its own; the name-matched candidate(s) %s do not reach {%s} — confirm by hand that the aggregator reading it calls a base helper (Rule 0025)"
            % (cls, ", ".join(r_pts[:3]), "/".join(sorted(want_r))),
        )
    else:
        rep.warn("BASE", "no reader entry point found for %s — verify the aggregator that builds it calls %s" % (cls, "/".join(sorted(want_r))))

    hit = _reaches_any("writer", confirmed_w or w_pts, want_w)
    if hit:
        if want_w & wcalls[hit]:
            rep.ok("BASE", "writer entry point %s directly calls %s" % (hit, ", ".join(sorted(want_w))))
        else:
            rep.warn("BASE", "writer entry point %s reaches %s within %d calls, but indirectly — confirm the base helper is applied to THIS instance" % (hit, "/".join(sorted(want_w)), _REACH_DEPTH))
    elif confirmed_w:
        rep.fail(
            "BASE",
            "no writer entry point calls a base writer helper (expected one of {%s}; entry points tried: %s) — reader/writer asymmetry drops inherited state on round-trip"
            % (", ".join(sorted(want_w)), ", ".join(confirmed_w[:4])),
        )
    elif w_pts:
        rep.warn(
            "BASE",
            "%s has no writer of its own; the name-matched candidate(s) %s do not reach {%s} — confirm by hand that the aggregator emitting it calls a base helper (Rule 0025)"
            % (cls, ", ".join(w_pts[:3]), "/".join(sorted(want_w))),
        )
    else:
        rep.warn("BASE", "no writer entry point found for %s — verify the aggregator that emits it calls %s" % (cls, "/".join(sorted(want_w))))


# --------------------------------------------------------------------------- #
# MEMBER — Rule 0001.7: the aggregator must dispatch to every member class
# --------------------------------------------------------------------------- #

_TYPING_CONTAINERS = {"Optional", "List", "Dict", "Set", "Tuple", "Union", "Callable", "Type", "Sequence", "Iterable", "Final", "ClassVar"}
# Value-carried roots: a class whose base chain reaches one of these is serialized
# as element text or an attribute value (Rule 0013.2) and has no member helper to
# dispatch to — refs (`RefType`), enums, literals, primitives. `RefType` breaks the
# chain rule (it derives from `ARObject`, not the literal family) but is carried as
# an element's text + DEST attribute via getChildElementOptionalRefType; TRefType/
# IRefType inherit from it and are covered transitively.
_VALUE_CARRIED_ROOTS = {"ARLiteral", "AREnum", "ARType", "RefType"}

# Capability aliases: a mixin-sourced member may be dispatched through the
# capability helper instead of the member's own — `readVariationPointCapable`
# reads the VARIATION-POINT element and calls setVariationPoint internally, so
# reaching it is as good as reaching readVariationPoint (Rule 0025 naming).
_MEMBER_ALIASES = {("parser", "VariationPoint"): ("readVariationPointCapable",), ("writer", "VariationPoint"): ("writeVariationPointCapable",)}


@lru_cache(maxsize=None)
def _xsd_text() -> str:
    p = _REPO_ROOT / "autosar" / "R23-11" / "xsd" / "AUTOSAR_00052.xsd"
    return read(p) if p.exists() else ""


@lru_cache(maxsize=None)
def _xsd_group_declares(cls: str, element: str) -> str:
    """Does the class's UPPER_SNAKE element group in the R23-11 XSD declare `element`?

    Returns "declares" | "lacks" | "unmapped". The mixin capability is applied
    repo-wide in the model, but the XSD decides per class whether it is active
    (Rule 0015: the schema is the serialization source of truth) — so a missing
    dispatch only fails when the schema actually allows the element.
    """
    text = _xsd_text()
    if not text:
        return "unmapped"
    upper = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", cls).upper()
    m = re.search(r'<xsd:group name="%s">' % re.escape(upper), text)
    if not m:
        return "unmapped"
    end = text.find("</xsd:group>", m.end())
    return "declares" if element in text[m.end():end] else "lacks"


@lru_cache(maxsize=None)
def _model_class_stored() -> Dict[str, Tuple[Tuple[str, str], ...]]:
    """(member type, attribute cap) pairs from class-level annotated defaults.

    The mixin pattern (Rule 0020/0021) declares members as class-level annotated
    defaults — `VariationPointCapable.variationPoint: Optional[VariationPoint] = None`
    — which never appear in a concrete class's `__init__`; without this map a mixin
    capability is invisible to the member check, and the exact shape that silently
    dropped VARIATION-POINT on `BswVariableAccess` passes unnoticed. Storage — not
    lookup getters — defines membership."""
    out: Dict[str, Tuple[Tuple[str, str], ...]] = {}
    for p in MODELS_DIR.rglob("*.py"):
        try:
            t = ast.parse(read(p))
        except SyntaxError:
            continue
        for n in ast.walk(t):
            if isinstance(n, ast.ClassDef):
                pairs: List[Tuple[str, str]] = []
                for item in n.body:
                    if isinstance(item, ast.AnnAssign):
                        target = item.target.id if isinstance(item.target, ast.Name) else None
                        cap = (target[0].upper() + target[1:]) if target else None
                        for tn in _annotation_type_names(item.annotation):
                            pairs.append((tn, cap or tn))
                out.setdefault(n.name, tuple(pairs))
    return out


@lru_cache(maxsize=None)
def _model_class_accessors() -> Dict[str, Tuple[Tuple[str, str], ...]]:
    """(member type, accessor name) pairs from accessor method annotations.

    A `get*` return or `set*`/`add*` parameter typed with the member names the
    exact call the parser/writer makes — however the attribute is spelled
    (`self.data_constr_rule` is read through `getDataConstrRules`). These refine
    the dispatch evidence for stored members; they never create members."""
    out: Dict[str, Tuple[Tuple[str, str], ...]] = {}
    for p in MODELS_DIR.rglob("*.py"):
        try:
            t = ast.parse(read(p))
        except SyntaxError:
            continue
        for n in ast.walk(t):
            if isinstance(n, ast.ClassDef):
                pairs: List[Tuple[str, str]] = []
                for fn in n.body:
                    if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        continue
                    if fn.name.startswith(("get", "create")) and fn.returns is not None:
                        for tn in _annotation_type_names(fn.returns):
                            pairs.append((tn, fn.name))
                    elif fn.name.startswith(("set", "add")) and len(fn.args.args) > 1 and fn.args.args[1].annotation is not None:
                        for tn in _annotation_type_names(fn.args.args[1].annotation):
                            pairs.append((tn, fn.name))
                out.setdefault(n.name, tuple(pairs))
    return out


def _annotation_type_names(ann: Optional[ast.expr]) -> List[str]:
    """Inner type names of an annotation: `X`, `Optional[X]`, `List[X]`, quoted `"X"`."""
    if isinstance(ann, ast.Constant) and isinstance(ann.value, str):
        return [ann.value] if ann.value.isidentifier() else []
    if isinstance(ann, ast.Name):
        return [ann.id]
    if isinstance(ann, ast.Attribute):
        return [ann.attr]
    if isinstance(ann, ast.Subscript):
        return _annotation_type_names(ann.slice)
    if isinstance(ann, ast.Tuple):
        out: List[str] = []
        for elt in ann.elts:
            out.extend(_annotation_type_names(elt))
        return out
    return []


def _is_value_carried(cls: str, base_map: Dict[str, List[str]]) -> bool:
    seen: Set[str] = set()
    frontier = [cls]
    while frontier:
        cur = frontier.pop()
        if cur in _VALUE_CARRIED_ROOTS:
            return True
        if cur in seen:
            continue
        seen.add(cur)
        frontier.extend(base_map.get(cur, []))
    return False


def _member_candidates(node: ast.ClassDef, base_map: Dict[str, List[str]]) -> Dict[str, Set[str]]:
    """Every aggregated member class of `node` mapped to the accessor names it is
    read/written through ({member: {accessorName, ...}}).

    Membership comes from STORAGE: `__init__`/`clear` annotated assignments
    (attribute-cap fallback), base-chain class-level defaults (`_model_class_stored`
    — the mixin pattern), and `createXxx` return types (registry aggregators).
    Accessor methods (`_model_class_accessors`, own + base chain) then name the
    exact calls the reader/writer makes — however the attribute is spelled
    (`self.data_constr_rule` is read through `getDataConstrRules`). Lookup-style
    getters never create members."""
    caps: Dict[str, Set[str]] = {}
    for fn in node.body:
        if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)) and fn.name.startswith("create") and fn.returns is not None:
            for tn in _annotation_type_names(fn.returns):
                caps.setdefault(tn, set()).add(fn.name)
    for n in ast.walk(node):
        if isinstance(n, ast.AnnAssign):
            target = n.target
            attr = target.attr if isinstance(target, ast.Attribute) else (target.id if isinstance(target, ast.Name) else None)
            cap = attr[0].upper() + attr[1:] if attr else None
            for tn in _annotation_type_names(n.annotation):
                caps.setdefault(tn, set()).add(cap or tn)
    seen: Set[str] = {node.name}
    frontier = list(base_map.get(node.name, []))
    while frontier:
        b = frontier.pop(0)
        if b in seen:
            continue
        seen.add(b)
        for tn, cap in _model_class_stored().get(b, ()):
            caps.setdefault(tn, set()).add(cap)
        frontier.extend(base_map.get(b, []))
    for cls_or_base in [node.name] + [b for b in _all_bases(node.name, base_map)]:
        for tn, acc in _model_class_accessors().get(cls_or_base, ()):
            if tn in caps:
                caps[tn].add(acc)
    out: Dict[str, Set[str]] = {}
    for name, cs in caps.items():
        if name in _TYPING_CONTAINERS or name not in base_map or _is_value_carried(name, base_map):
            continue
        out[name] = cs
    return out


def _all_bases(cls: str, base_map: Dict[str, List[str]]) -> List[str]:
    seen: Set[str] = set()
    frontier = list(base_map.get(cls, []))
    while frontier:
        b = frontier.pop(0)
        if b in seen:
            continue
        seen.add(b)
        frontier.extend(base_map.get(b, []))
    return list(seen)


def check_members(rep: Report, cls: str, node: ast.ClassDef, enum: bool) -> None:
    """Rule 0001.7, mechanical: a shared helper's existence is not evidence an
    aggregator calls it. Every aggregated member class's reader/writer helper must
    be reachable from the class's own reader/writer entry point — the same
    confirmed-vs-guessed entry-point semantics as BASE, at the deeper dispatch
    nesting members legitimately use.

    Reader-side coverage accepts helper dispatch OR inline construction (the
    parser calling the model's `create<Member>` factory or constructing the member
    directly). Writer-side inline emission is mechanically invisible — getters
    carry no member name — so a writer FAIL is a hand-verify prompt, exactly like
    BASE's indirect-reach warnings."""
    base_map = _model_base_map()
    if enum or _is_value_carried(cls, base_map):
        rep.ok("MEMBER", "value-carried type — serialized as text/attribute value, no member dispatch of its own")
        return
    members = _member_candidates(node, base_map)
    if not members:
        rep.ok("MEMBER", "no aggregated member classes")
        return
    pcalls = collect_calls(PARSER)
    wcalls = collect_calls(WRITER)
    if not pcalls or not wcalls:
        rep.warn("MEMBER", "parser/writer source not found — skipped")
        return
    known_r = known_helper_names(PARSER, ABSTRACT_PARSER)
    known_w = known_helper_names(WRITER, ABSTRACT_WRITER)
    confirmed_r = [f for f in ("read" + cls, "get" + cls) if f in pcalls]
    confirmed_w = [f for f in ("write" + cls, "set" + cls) if f in wcalls]
    r_pts = confirmed_r or _entry_points(pcalls, ("read" + cls, "get" + cls), (cls, "create" + cls, "get" + cls), cls)
    w_pts = confirmed_w or _entry_points(wcalls, ("write" + cls, "set" + cls), ("get" + cls, "set" + cls, "create" + cls), cls)

    for side, entry_pts, confirmed, known_fns, verb in (("parser", r_pts, confirmed_r, known_r, "reader"), ("writer", w_pts, confirmed_w, known_w, "writer")):
        have, lack = [], []
        for m, maccs in members.items():
            pref = "read" if side == "parser" else "write"
            alt = "get" if side == "parser" else "set"
            # Reader side: building the member inline is legitimate coverage too —
            # through the model's create factory (`documentation.createChapter`), by
            # constructing it directly (`AnyInstanceRef()`), or via the attribute's
            # mutators (`props.setCrcFlags`). Writer side: emission always goes
            # through a model accessor (`props.getCrcFlags()`, `getDataConstrRules`)
            # even when the element is emitted inline — those accessor names are the
            # evidence for otherwise-invisible inline emission.
            mutators = tuple(a for a in maccs if a.startswith(("set", "add"))) if side == "parser" else ()
            getters = tuple(a for a in maccs if a.startswith("get")) if side == "writer" else ()
            extra = ((m, "create" + m) + mutators + getters) if side == "parser" else (mutators + getters)
            targets = {t for t in (pref + m, alt + m) + _MEMBER_ALIASES.get((side, m), ()) + extra if t in known_fns or t in extra}
            if not targets:
                lack.append(m)
            else:
                have.append((m, targets))
        if lack:
            rep.warn(
                "MEMBER",
                "%d aggregated member class(es) of %s own no %s helper — inline emission is legitimate (Rule 0025 naming); verify their attributes are covered: %s"
                % (len(lack), cls, verb, ", ".join(sorted(lack)[:6])),
            )
        if not entry_pts:
            rep.warn("MEMBER", "no %s entry point found for %s — cannot verify dispatch of %d member class(es): %s" % (verb, cls, len(have), ", ".join(sorted(m for m, _ in have)[:6])))
            continue
        if not have:
            rep.ok("MEMBER", "%s dispatch — no %s-helper members to verify (%d member(s) are inline-emitted or value-carried)" % (verb, verb, len(lack)))
            continue
        reached_direct: List[str] = []
        reached_indirect: List[str] = []
        missing: List[str] = []
        dormant: List[str] = []
        for m, targets in have:
            frozen = frozenset(targets)
            hit_fn = _reaches_any(side, entry_pts, set(targets), _MEMBER_REACH_DEPTH)
            if hit_fn is None:
                # The mixin capability is applied repo-wide in the model but the XSD
                # decides per class whether the element exists at all (Rule 0015) —
                # a missing dispatch on a group that lacks the element is a dormant
                # capability, warned not failed.
                if m == "VariationPoint" and _xsd_group_declares(cls, "VARIATION-POINT") in ("lacks", "unmapped"):
                    dormant.append(m)
                else:
                    missing.append(m)
            elif frozen & collect_calls(PARSER if side == "parser" else WRITER)[hit_fn]:
                reached_direct.append(m)
            else:
                reached_indirect.append(m)
        if dormant:
            rep.warn(
                "MEMBER",
                "%s does not dispatch %s (mixin capability) but the class's XSD group does not declare VARIATION-POINT / is unmapped — capability dormant, confirm the schema lookup: %s"
                % (verb, ", ".join(sorted(dormant)), cls),
            )
        if missing:
            detail = ", ".join(sorted(missing)[:8])
            if confirmed:
                rep.fail(
                    "MEMBER",
                    "%s entry point(s) %s never dispatch to %d aggregated member class helper(s): %s — the member's elements are silently dropped on round-trip (Rule 0001.7)"
                    % (verb, ", ".join(confirmed[:3]), len(missing), detail),
                )
            else:
                rep.warn(
                    "MEMBER",
                    "%s name-matched candidate(s) %s do not reach %d member helper(s): %s — confirm by hand that the aggregator dispatches them (Rule 0001.7)"
                    % (verb, ", ".join(entry_pts[:3]), len(missing), detail),
                )
            continue
        note = ", ".join(reached_direct[:6]) if reached_direct else ", ".join(reached_indirect[:6])
        shape = "directly" if reached_direct and not reached_indirect else ("indirectly (via shared helpers)" if reached_indirect and not reached_direct else "directly + indirectly")
        if len(have) - len(dormant) > 0:
            rep.ok("MEMBER", "%s dispatch reaches all %d aggregated member class helper(s) (%s): %s" % (verb, len(have) - len(dormant), shape, note))


def check_pattern(rep: Report, node: ast.ClassDef) -> None:
    """Rule 0028, mechanical: an `ARLiteral` subclass whose docstring carries
    `xml.xsd.pattern=` must declare a `PATTERN` class attribute — a declared
    `PATTERN = None` does not count (the runtime check stays off), and classes
    outside the `ARLiteral` family (`Numerical`/`ARType` numerics, Rule 0028
    point 4) are not reported."""
    doc = ast.get_docstring(node) or ""
    if "xml.xsd.pattern=" not in doc:
        return
    base_map = _model_base_map()
    if node.name in base_map:
        seen: Set[str] = {node.name}
        frontier = list(base_map[node.name])
        while frontier:
            b = frontier.pop(0)
            if b in seen:
                continue
            seen.add(b)
            frontier.extend(base_map.get(b, []))
        if "ARLiteral" not in seen:
            return
    for stmt in node.body:
        if isinstance(stmt, ast.Assign):
            names = [t.id for t in stmt.targets if isinstance(t, ast.Name)]
            value = stmt.value
        elif isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
            names = [stmt.target.id]
            value = stmt.value
        else:
            continue
        if "PATTERN" not in names:
            continue
        if isinstance(value, ast.Constant) and value.value is None:
            continue
        return
    rep.warn(
        "PATTERN",
        "Rule 0028: docstring carries xml.xsd.pattern but no PATTERN attribute is declared — add the XSD-facet regex (an inherited attribute from a pattern-declaring base satisfies the rule; verify by hand) — Numerical/ARType numeric subclasses are exempt (Rule 0028 point 4): do not add PATTERN to them",
    )


# --------------------------------------------------------------------------- #
# driver
# --------------------------------------------------------------------------- #


def audit_one(cls: str, path: Path) -> Report:
    rep = Report()
    try:
        text, lines, tree = parse_module(path)
    except SyntaxError as exc:
        rep.fail("PARSE", "cannot parse %s: %s" % (path, exc))
        return rep
    node = class_node(tree, cls)
    if node is None:
        rep.fail("FIND", "class %s not found in %s" % (cls, path))
        return rep
    start = class_start(lines, cls)
    end = class_end(lines, start)
    enum = is_enum(node)
    blk = collect_block(lines, cls)
    if blk is None:
        rep.fail("BLOCK", "no `# %s method parity checklist:` header in the class body" % cls)
        return rep
    _, _, blk_lines = blk
    check_block(rep, cls, lines, start, end)
    check_rows(rep, cls, node, blk_lines)
    check_stamp(rep, blk_lines)
    check_specline(rep, cls, blk_lines)
    check_citation(rep, cls, blk_lines)
    check_spec_base(rep, cls, blk_lines, enum)
    check_docs(rep, node, blk_lines, enum)
    check_spacing(rep, lines, start, end)
    check_doc_tail(rep, node, lines, start, end)
    check_base(rep, cls, node, enum)
    check_members(rep, cls, node, enum)
    check_pattern(rep, node)
    return rep


def iter_classes(path: Path) -> List[str]:
    try:
        tree = ast.parse(read(path))
    except SyntaxError:
        return []
    return [n.name for n in tree.body if isinstance(n, ast.ClassDef)]


SYMBOL = {"FAIL": "x", "WARN": "!", "INFO": "i", "ok": "."}


def render(name: str, path: Path, rep: Report) -> str:
    out = ["%s  (%s)" % (name, path)]
    width = max((len(c) for _, c, _ in rep.rows), default=0)
    for lvl, code, msg in rep.rows:
        out.append("  %s %-*s %s" % (SYMBOL.get(lvl, "?"), width, code, msg))
    n_fail = sum(1 for lvl, _, _ in rep.rows if lvl == "FAIL")
    n_warn = sum(1 for lvl, _, _ in rep.rows if lvl == "WARN")
    out.append("  => %s" % ("PASS" if not n_fail else "FAIL (%d failure(s))" % n_fail) + ("" if not n_warn else ", %d warning(s)" % n_warn))
    return "\n".join(out)


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Mechanical pre-stamp audit for AUTOSAR model classes.")
    ap.add_argument("classes", nargs="*", help="class names to audit")
    ap.add_argument("--file", type=Path, help="restrict the source search to one file")
    ap.add_argument("--all", action="store_true", help="audit every class in the models tree")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args(argv)

    if not args.classes and not args.all and args.file is None:
        ap.error("give one or more class names, or --all, or --file")

    targets: List[Tuple[str, Path]] = resolve_targets(args.classes, args.file, args.all)
    if not targets:
        print("no matching class definitions found", file=sys.stderr)
        return 1

    results: Dict[str, object] = {}
    failed = 0
    for cls, p in targets:
        rep = audit_one(cls, p)
        results[cls] = rep.as_dict()
        if rep.failed:
            failed += 1
        if not args.json:
            print(render(cls, p, rep))
            print()
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print("audited %d class(es); %d with failures" % (len(targets), failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
