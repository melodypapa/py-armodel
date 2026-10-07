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

  DOC      `__init__` carries no docstring (Rule 0012.2.4). A `Tags:`/`Stereotypes:`
           tail in a class / `__init__` member / accessor docstring is **expected**
           and reported as INFO — the spec `Note` is copied verbatim including the
           tail (Rule 0012.2.5.3), and ~1000 stamped sites do the same.

  SPECLINE the `# Spec:` line is in canonical Rule 0002 form for a single-corpus
           class, or the R4.3.1-fallback form, or an explicit dual-line combine
           case (Rule 0019).

  STAMP    `# Spec verified:` / `# XSD verified:` is present iff every row is
           `[x]`. A marker over unfinished rows certifies work that was never
           done (Rule 0012.1); a finished checklist without a marker is the
           normal state of a class awaiting its 9b gate.

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


def check_stamp(rep: Report, blk_lines: Sequence[str]) -> None:
    spec_ver = [x for x in blk_lines if x.startswith("# Spec verified:")]
    xsd_ver = [x for x in blk_lines if x.startswith("# XSD verified:")]
    markers = spec_ver + xsd_ver
    if len(markers) > 1:
        rep.fail("STAMP", "%d provenance markers in one block (%s) — exactly one is allowed" % (len(markers), "; ".join(markers)))
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


@lru_cache(maxsize=None)
def _reaches(side: str, fn: str, targets: frozenset) -> bool:
    """Does `fn` call one of `targets`, directly or via <= _REACH_DEPTH helpers?

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
        cur, depth = frontier.pop()
        if depth >= _REACH_DEPTH:
            continue
        for nxt in graph.get(cur, ()):
            if nxt in targets:
                return True
            if nxt not in seen:
                seen.add(nxt)
                frontier.append((nxt, depth + 1))
    return False


def _reaches_any(side: str, entry_points: Sequence[str], targets: Set[str]) -> Optional[str]:
    """The first entry point that reaches one of `targets`, directly or transitively."""
    frozen = frozenset(targets)
    for fn in entry_points:
        if _reaches(side, fn, frozen):
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
        how = "directly calls" if want_r & pcalls[hit] else "reaches (within %d calls) %s" % (_REACH_DEPTH, ", ".join(sorted(want_r)))
        rep.ok("BASE", "reader entry point %s %s" % (hit, how))
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
        how = "directly calls" if want_w & wcalls[hit] else "reaches (within %d calls) %s" % (_REACH_DEPTH, ", ".join(sorted(want_w)))
        rep.ok("BASE", "writer entry point %s %s" % (hit, how))
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
    check_docs(rep, node, blk_lines, enum)
    check_base(rep, cls, node, enum)
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
