"""Rule-based audit for Rule 0023 legacy-format checklist classes.

For every class whose method-parity checklist is legacy format (rows ending at the
`test` column), audit it against its spec table with the checks automation can do:

- Rule 0002 / 0001.3 — field-to-spec cross-check in BOTH directions (spec attributes
  missing in the model; model members absent from the table) + Base-chain presence.
- Rule 0022 — quota shape vs spec multiplicity (0..1 -> Optional[T], 0..* -> List[T], 1 -> T).
- Rule 0001.7 — reader/writer coverage per spec member (parser calls the mutator,
  writer calls the getter).
- Rule 0003 — trailing `# type:` comments instead of PEP 526 annotated members.
- Rule 0012 — class docstring vs the spec `Note` (whitespace-collapsed compare; soft flag).
- Rule 0023 — the stale `Spec verified` / `XSD verified` marker itself.

Verdicts: DRIFT (hard finding — re-sync priority), REVIEW (soft finding), FORMAT-ONLY
(members/coverage match; only the format + marker re-run is owed). This audit is
informational: it never fails a checker by itself and never stamps anything.

Spec source: markdown tables anchored by the `| Class | <Name> |` / `| Enumeration | <Name> |`
header cell (trailing-caption layout — attribute rows sit under the `| Attribute |` /
`| Literal |` header of the same block). R23-11 corpus first, R4.3.1 fallback.
"""

import ast
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = ROOT / "src" / "armodel" / "models"
PARSER_PATH = ROOT / "src" / "armodel" / "parser" / "arxml_parser.py"
WRITER_PATH = ROOT / "src" / "armodel" / "writer" / "arxml_writer.py"
CORPORA = [
    ("R23-11", ROOT / "autosar" / "R23-11" / "markdown"),
    ("R4.3.1", ROOT / "autosar" / "R4.3.1" / "markdown"),
]

LEGACY_BLOCK_RE = re.compile(r"#\s*(\w+)\s+method parity checklist:")
LEGACY_ROW_RE = re.compile(r"^\s*#\s*\[[xX—]\]\s+\S+\s+\[[x—]\]\s+impl\s+\[[x—]\]\s+docstring\s+\[[x—]\]\s+test\s*$")
LEGACY_STAMP_RE = re.compile(r"#\s*((?:Spec|XSD) verified:[^\n]*)")
SIX_COL_ROW_RE = re.compile(r"#\s*\[[xX—]\]\s+\S+\s+\[[x—]\]\s+impl\s+\[[x—]\]\s+docstring\s+\[[x—]\]\s+test\s+\[[x—]\]\s+reader")

GLYPH_RE = re.compile(r"glyph\[[^\]]*\]")


def collect_legacy_blocks() -> List[Tuple[str, str, Optional[str]]]:
    """(file-relative, class, stale-marker text) for every legacy-format checklist."""
    results: List[Tuple[str, str, Optional[str]]] = []
    for path in sorted(MODELS_DIR.rglob("*.py")):
        current: Optional[str] = None
        stamp: Optional[str] = None
        has_legacy = False
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            block = LEGACY_BLOCK_RE.search(line)
            if block:
                if current is not None and has_legacy:
                    results.append((str(path.relative_to(ROOT)), current, stamp))
                current, stamp, has_legacy = block.group(1), None, False
            elif current is not None:
                if SIX_COL_ROW_RE.match(line):
                    has_legacy = False  # a 6-column row anywhere in the block: current format
                stamp_match = LEGACY_STAMP_RE.search(line)
                if stamp_match and stamp is None:
                    stamp = stamp_match.group(1).strip()
                elif LEGACY_ROW_RE.match(line):
                    has_legacy = True
        if current is not None and has_legacy:
            results.append((str(path.relative_to(ROOT)), current, stamp))
    return results


def clean_cell(text: str) -> str:
    text = GLYPH_RE.sub("", text)
    return text.strip()


def demangle_name(text: str) -> str:
    """Markdown line-wrapping inserts spaces inside camelCase names — remove all whitespace."""
    return re.sub(r"\s+", "", GLYPH_RE.sub("", text))


def parse_row(line: str) -> List[str]:
    return [clean_cell(c) for c in line.strip().strip("|").split("|")]


class SpecTable:
    def __init__(self):
        self.release: Optional[str] = None
        self.file: Optional[str] = None
        self.kind: Optional[str] = None  # Class | Enumeration
        self.attributes: List[Tuple[str, str, str]] = []  # (name, multiplicity, kind)
        self.name_only_attributes: List[Tuple[str, str, str]] = []
        self._literal_header_seen = False
        self.attribute_notes: Dict[str, str] = {}
        self.literal_notes: Dict[str, str] = {}
        self.table_id: Optional[str] = None
        self.literals: List[str] = []
        self.base_row: Optional[str] = None
        self.note: Optional[str] = None


def build_caption_index(names: set) -> Dict[str, List[Tuple[str, str, str]]]:
    """name -> [(release, md-relative-file, table_id)] from `Table N.M: <Name>` captions."""
    index: Dict[str, List[Tuple[str, str, str]]] = {}
    caption_re = re.compile(r"^Table (\d+\.\d+): (.+?)\s*$")
    for release, corpus in CORPORA:
        if not corpus.is_dir():
            continue
        for md in sorted(corpus.glob("*.md")):
            for line in md.read_text(encoding="utf-8", errors="replace").splitlines():
                m = caption_re.match(line.strip())
                if not m:
                    continue
                name = demangle_name(m.group(2))
                if name in names:
                    index.setdefault(name, []).append((release, str(md.relative_to(ROOT)), m.group(1)))
    return index


def build_spec_index(names: set) -> Dict[str, List[Tuple[str, int, str]]]:
    """name -> [(release, line_no, kind)] over both corpora (single scan)."""
    index: Dict[str, List[Tuple[str, int, str]]] = {}
    for release, corpus in CORPORA:
        if not corpus.is_dir():
            continue
        for md in sorted(corpus.glob("*.md")):
            for line_no, line in enumerate(md.read_text(encoding="utf-8", errors="replace").splitlines()):
                if not line.startswith("|"):
                    continue
                cells = parse_row(line)
                if len(cells) < 2 or cells[0] not in ("Class", "Enumeration"):
                    continue
                name = demangle_name(cells[1])
                if name in names:
                    index.setdefault(name, []).append((release, (md, line_no), cells[0]))
    return index


MULT_RE = re.compile(r"^(?:\d+\.\.[\d*+]|\*|-)$")
META_LABELS = {"Package", "Note", "Base", "Aggregated by", "Attribute", "Literal", "Type", "Mult.", "Kind", "Description"}


def extract_table(md: Path, line_no: int, kind: str, literal_header_seen: bool = False, table_name: str = "") -> SpecTable:
    """Capture every pipe row between this Class/Enumeration header row and the next
    header row or caption — page-split tables continue without repeating the header
    (trailing-caption layout), so rows are classified by shape, not by an Attribute header."""
    table = SpecTable()
    table.kind = kind
    table._literal_header_seen = literal_header_seen
    lines = md.read_text(encoding="utf-8", errors="replace").splitlines()
    seen_attribute_header = False
    caption_re = re.compile(r"^Table (\d+\.\d+): " + re.escape(table_name))
    for line in lines[line_no + 1 :]:
        if not line.startswith("|"):
            m = caption_re.match(line.strip())
            if m:
                if table.table_id is None:
                    table.table_id = m.group(1)
                break
            continue
        cells = parse_row(line)
        if not cells:
            continue
        head = cells[0]
        if head in ("Class", "Enumeration") and len(cells) > 1 and demangle_name(cells[1]) != "":
            break  # next table block begins
        if head == "Attribute":
            seen_attribute_header = True
            continue
        if head == "Literal":
            table._literal_header_seen = True
            continue
        if head == "Abbreviation":
            break
        if head in ("Package", "Base", "Aggregated by", "Note"):
            if head == "Base" and len(cells) > 1 and table.base_row is None:
                table.base_row = cells[1]
            elif head == "Note" and len(cells) > 1 and table.note is None:
                table.note = cells[1]
            continue
        if head in ("Type", "Mult.", "Kind", "Literal", "Description") and not seen_attribute_header and kind == "Class":
            continue
        name = re.sub(r"\((ordered|unordered)\)", "", demangle_name(head))
        if not name or re.fullmatch(r"[-_]+", name) or name in META_LABELS:
            continue
        mult = re.sub(r"\s+", "", cells[2]) if len(cells) > 2 and MULT_RE.match(re.sub(r"\s+", "", cells[2])) else None
        if kind == "Enumeration":
            if table._literal_header_seen and mult is None and len(cells) >= 2 and name not in table.literals:
                if (name[0].islower() or name[0] in "-_") and not name.startswith("[") and name != "Abbreviation":
                    table.literals.append(name)
                    if len(cells) >= 2 and cells[1]:
                        table.literal_notes[name] = cells[1]
            continue
        row_kind = cells[3].strip() if len(cells) > 3 and cells[3].strip() and MULT_RE.match(mult or "") else ""
        note_cell = cells[4].strip() if len(cells) > 4 and mult is not None else ""
        if mult is not None:
            if not any(a[0] == name and a[1] == mult for a in table.attributes):
                table.attributes.append((name, mult, row_kind))
                if note_cell:
                    table.attribute_notes[name] = note_cell
        elif name[0].islower():
            # 3-column render (name | type | note): kept separately — page-split
            # continuations of UNRELATED tables also render name-only rows, so these
            # are used only when the class has no typed (5-column) rows at all.
            if not any(a[0] == name for a in table.name_only_attributes):
                table.name_only_attributes.append((name, "", ""))
    if not table.attributes and table.name_only_attributes:
        table.attributes = table.name_only_attributes
    return table


def merge_tables(tables: List[SpecTable]) -> SpecTable:
    merged = SpecTable()
    merged.kind = tables[0].kind if tables else None
    for t in tables:
        for name, mult, row_kind in t.attributes:
            existing = next((a for a in merged.attributes if a[0] == name), None)
            if existing is None:
                merged.attributes.append((name, mult, row_kind))
            elif not existing[1] and mult:
                merged.attributes[merged.attributes.index(existing)] = (name, mult, row_kind)
        for lit in t.literals:
            if lit not in merged.literals:
                merged.literals.append(lit)
        for name, note in t.attribute_notes.items():
            merged.attribute_notes.setdefault(name, note)
        for name, note in t.literal_notes.items():
            merged.literal_notes.setdefault(name, note)
        if merged.base_row is None:
            merged.base_row = t.base_row
        if merged.note is None:
            merged.note = t.note
        if merged.table_id is None:
            merged.table_id = t.table_id
    return merged


def locate_spec(index, name) -> Tuple[Optional[SpecTable], Optional[str]]:
    hits = index.get(name) or []
    for release in ("R23-11", "R4.3.1"):
        blocks = [(md, line_no, kind) for rel, (md, line_no), kind in hits if rel == release]
        if not blocks:
            continue
        tables = []
        literal_header_seen = False
        for md, line_no, kind in blocks:
            t = extract_table(md, line_no, kind, literal_header_seen, table_name=name)
            literal_header_seen = t._literal_header_seen
            t.release = release
            t.file = str(md.relative_to(ROOT))
            tables.append(t)
        merged = merge_tables(tables)
        merged.release = release
        merged.file = str(blocks[0][0].relative_to(ROOT))
        return merged, merged.file
    return None, None


def class_audit(src_path: Path, class_name: str) -> Dict:
    tree = ast.parse(src_path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            break
    else:
        return {"found": False}

    info: Dict = {"found": True, "bases": [], "members": {}, "legacy_type_comments": 0, "methods": set(), "enum_literals": [], "docstring": None, "is_enum": False}
    info["bases"] = [ast.unparse(b) for b in node.bases]
    info["docstring"] = ast.get_docstring(node)
    if any(b == "AREnum" or b.endswith("Enum") and b in ("AREnum",) for b in info["bases"]):
        info["is_enum"] = True
    info["is_enum"] = "AREnum" in info["bases"]

    for stmt in node.body:
        if isinstance(stmt, ast.Assign) and stmt.type_comment is not None:
            info["legacy_type_comments"] += 1
        if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
            target = stmt.targets[0].id
            if isinstance(stmt.value, ast.Constant) and isinstance(stmt.value.value, str) and target.isupper():
                info["enum_literals"].append((stmt.value.value, target))
        if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
            info["methods"].add(stmt.name)
            for sub in ast.walk(stmt):
                if isinstance(sub, ast.AnnAssign) and isinstance(sub.target, ast.Attribute) and isinstance(sub.target.value, ast.Name) and sub.target.value.id == "self":
                    info["members"][sub.target.attr] = ast.unparse(sub.annotation)
                elif isinstance(sub, ast.Assign) and sub.type_comment is not None:
                    info["legacy_type_comments"] += 1
    return info


def annotation_shape(annotation: str) -> str:
    if annotation.startswith("Optional["):
        return "optional"
    if annotation.startswith("List["):
        return "list"
    return "plain"


def accessor_name(member: str) -> str:
    return member[:1].upper() + member[1:] if member else member


def accessor_variants(member: str) -> List[str]:
    acc = accessor_name(member)
    variants = {acc}
    if acc.endswith("ies"):
        variants.add(acc[:-3] + "y")
    if acc.endswith("s"):
        variants.add(acc[:-1])
    return sorted(variants)


def rw_flags(member: str, methods: set, parser_text: str, writer_text: str):
    accs = accessor_variants(member)
    has_accessor = any(f"{p}{a}" in methods for a in accs for p in ("get", "set", "add", "create"))
    mutator = any(re.search(r"\.(?:set|add|create)%s\b" % re.escape(a), parser_text) for a in accs)
    getter = any(re.search(r"\.get%s\b" % re.escape(a), writer_text) for a in accs)
    return has_accessor, mutator, getter


def model_name_candidates(name: str, kind: str, mult: str) -> set:
    cands = {name}
    if kind == "ref":
        cands.add(name + "Ref")
    elif kind == "iref":
        cands.add(name + "IRef")
    if mult in ("0..*", "1..*", "*") or mult == "":
        plural_variants = {c + "s" for c in cands}
        plural_variants |= {c[:-1] + "ies" for c in cands if c.endswith("y")}
        cands |= plural_variants
    return cands


def expected_shape(mult: str) -> Optional[str]:
    if mult == "0..1":
        return "optional"
    if mult in ("0..*", "1..*"):
        return "list"
    if mult == "1":
        return "plain"
    return None


def build_dump() -> List[Dict]:
    """Full per-class data for the Rule 0023 re-sync rewriter."""
    blocks = collect_legacy_blocks()
    parser_text = PARSER_PATH.read_text(encoding="utf-8", errors="replace")
    writer_text = WRITER_PATH.read_text(encoding="utf-8", errors="replace")
    names = {cls for _, cls, _ in blocks}
    index = build_spec_index(names)
    caption_index = build_caption_index(names)

    dump: List[Dict] = []
    for file_rel, cls, stamp in blocks:
        info = class_audit(ROOT / file_rel, cls)
        entry: Dict = {
            "file": file_rel,
            "class": cls,
            "found": info.get("found", False),
            "stale_marker": stamp,
            "bases": info.get("bases", []),
            "members": info.get("members", {}),
            "methods": sorted(info.get("methods", set())),
            "is_enum": info.get("is_enum", False),
            "docstring": info.get("docstring"),
        }
        if info["found"] and not info["is_enum"]:
            entry["enum_literals"] = info["enum_literals"]
        table, table_file = locate_spec(index, cls)
        if table is not None:
            if table.table_id is None:
                for rel, md_rel, tid in caption_index.get(cls, []):
                    if rel == table.release:
                        table.table_id = tid
                        if md_rel == table.file:
                            break
            entry.update(
                {
                    "release": table.release,
                    "md_file": str(table.file),
                    "table_id": table.table_id,
                    "kind": table.kind,
                    "class_note": table.note,
                    "base_row": table.base_row,
                    "spec_attributes": [{"name": n, "mult": mult, "kind": kd, "note": table.attribute_notes.get(n, "")} for n, mult, kd in table.attributes],
                    "spec_literals": [{"name": lit, "note": table.literal_notes.get(lit, "")} for lit in table.literals],
                }
            )
            if not info["is_enum"] and info["found"]:
                for attr in entry["spec_attributes"]:
                    name, mult, kd = attr["name"], attr["mult"], attr["kind"]
                    cands = model_name_candidates(name, kd, mult)
                    model_member = next((m for m in info["members"] if m in cands), None)
                    attr["model_member"] = model_member
                    if model_member:
                        attr["annotation"] = info["members"][model_member]
                        _, mut, get = rw_flags(model_member, set(info["methods"]), parser_text, writer_text)
                        attr["mutator_covered"] = mut
                        attr["getter_covered"] = get
        dump.append(entry)
    return dump


def main() -> int:
    if len(sys.argv) > 2 and sys.argv[1] == "--dump":
        import json

        data = build_dump()
        Path(sys.argv[2]).write_text(json.dumps(data, indent=1), encoding="utf-8")
        print(f"dumped {len(data)} classes to {sys.argv[2]}")
        return 0

    blocks = collect_legacy_blocks()
    parser_text = PARSER_PATH.read_text(encoding="utf-8", errors="replace")
    writer_text = WRITER_PATH.read_text(encoding="utf-8", errors="replace")

    names = {cls for _, cls, _ in blocks}
    index = build_spec_index(names)

    report: List[Tuple[str, str, str, List[str]]] = []  # (verdict, file, class, findings)
    for file_rel, cls, stamp in blocks:
        findings: List[str] = []
        src_path = ROOT / file_rel
        info = class_audit(src_path, cls)
        if not info["found"]:
            report.append(("DRIFT", file_rel, cls, ["class not found in source"]))
            continue

        if stamp:
            findings.append(f"R0023 stale marker: {stamp}")

        table, table_file = locate_spec(index, cls)
        if table is None:
            findings.append("no Class/Enumeration table in R23-11 or R4.3.1 corpora (arbitration/skip precedent applies)")
            report.append(("REVIEW", file_rel, cls, findings))
            continue
        findings.append(f"spec: {table.release} {table_file} ({table.kind})")

        if table.kind == "Enumeration":
            spec_literals = table.literals
            src_values = [v for v, _ in info["enum_literals"]]

            def tok(v):
                return v.upper().replace("-", "_").lstrip("_")

            missing = [lit for lit in spec_literals if lit not in src_values and tok(lit) not in {tok(v) for v in src_values}]
            extra = [v for v in src_values if v not in spec_literals and tok(v) not in {tok(lit) for lit in spec_literals}]
            same_cardinality = len(spec_literals) == len(src_values) and len(missing) == len(extra)
            if missing and not same_cardinality:
                findings.append(f"R0002 missing literals: {missing}")
            if extra and not same_cardinality:
                findings.append(f"R0002 extra literals: {extra}")
            token_mapped = [lit for lit in spec_literals if lit not in src_values and tok(lit) in {tok(v) for v in src_values}]
            if token_mapped:
                findings.append(f"enum literal value token-map differs from spec display form: {token_mapped} (XSD arbitration — review)")
            if spec_literals and src_values and spec_literals != src_values:
                order_ok = [v for v in src_values if v in spec_literals] == [lit for lit in spec_literals if lit in src_values]
                if not order_ok:
                    findings.append("R0001.11 literal order differs from spec display order")
        else:
            matched: Dict[str, str] = {}
            for name, mult, kind in table.attributes:
                cands = model_name_candidates(name, kind, mult)
                hit = next((m for m in info["members"] if m in cands), None)
                if hit is None:
                    findings.append(f"R0002 spec attr missing in model: {name} (mult {mult}, kind {kind or 'attr'})")
                    continue
                matched[name] = hit

            spec_hits = set(matched.values())
            extra = [m for m in info["members"] if m not in spec_hits]
            if extra:
                findings.append(f"R0019 model members not in table (legacy-combine candidates): {extra}")

            for name, mult, kind in table.attributes:
                member = matched.get(name)
                if member is None:
                    continue
                want = expected_shape(mult) if mult else None
                got = annotation_shape(info["members"][member])
                if want and got != want:
                    findings.append(f"R0022 {member}: mult {mult} wants {want}, model has {got} ({info['members'][member]})")

                has_accessor, mutator_covered, getter_covered = rw_flags(member, info["methods"], parser_text, writer_text)
                if has_accessor and not mutator_covered:
                    findings.append(f"R0001.7 {member}: no reader call of set/add/create{member}")
                if has_accessor and not getter_covered:
                    findings.append(f"R0001.7 {member}: no writer call of get{member}")

            if table.base_row:
                chain = [demangle_name(t) for t in table.base_row.split(",")]
                py_base = info["bases"][0].split("[")[0] if info["bases"] else ""
                py_base_simple = py_base.split(".")[-1]
                if py_base_simple not in chain and py_base_simple != cls:
                    findings.append(f"R0001.2 base {py_base_simple} not in spec Base chain {chain}")

        if info["legacy_type_comments"]:
            findings.append(f"R0003 {info['legacy_type_comments']} trailing `# type:` member declarations")

        if table.note and info["docstring"]:
            norm_note = re.sub(r"\s+", " ", GLYPH_RE.sub("", table.note)).strip()
            norm_doc = re.sub(r"\s+", " ", info["docstring"]).strip()
            if norm_note and norm_doc and norm_note not in norm_doc:
                findings.append("R0012 class docstring differs from spec Note (review verbatim)")

        hard = any(f.startswith(("R0002", "R0001.7", "R0022")) for f in findings)
        soft = [f for f in findings if not (f.startswith("R0023") or f.startswith("spec:"))]
        verdict = "DRIFT" if hard else ("FORMAT-ONLY" if not soft else "REVIEW")
        report.append((verdict, file_rel, cls, findings))

    order = {"DRIFT": 0, "REVIEW": 1, "FORMAT-ONLY": 2}
    report.sort(key=lambda r: (order[r[0]], r[1], r[2]))
    counts: Dict[str, int] = {}
    for verdict, _, _, _ in report:
        counts[verdict] = counts.get(verdict, 0) + 1

    print("=== Rule 0023 legacy-checklist audit (skill-rule based) ===")
    print(f"audited: {len(report)} | " + " | ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    for verdict, file_rel, cls, findings in report:
        print(f"\n[{verdict}] {cls} ({file_rel})")
        for f in findings:
            print(f"    - {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
