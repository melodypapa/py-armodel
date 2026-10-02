"""Rule 0023 mechanical re-sync applier.

Consumes the dump produced by `audit_legacy_checklists.py --dump` and rewrites each
queued class in place:

- removes the stale `# Spec verified:` / `# XSD verified:` marker (Rule 0023 — goes first),
- converts the legacy 4-column checklist to the current 6-column format (impl / docstring /
  test / reader / writer / release), with reader/writer columns from the audit's coverage
  flags and the per-row release token,
- wipes and rewrites the class docstring and every member's inline `__init__` comment and
  getter/setter docstrings verbatim from the spec `Note` (Rule 0012), appending the
  None-no-op sentence on guarded setters/adders,
- drops the `__init__` docstring (Rule 0012.2.5.2 — inline comments only),
- for AREnum classes: rewrites the class docstring and the per-literal comments.

Writes no stamps. Everything outside the touched spans stays byte-identical.
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

ROOT = Path(__file__).resolve().parent.parent
TEST_DIRS = [ROOT / "tests" / "test_armodel"]

SETTER_NOOP = "A None value is a no-op and does not overwrite an existing {member}."
ADD_NOOP = "A None value is a no-op and does not append to {member}."
QUOTE = '"""'


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def accessor_names(member: str) -> List[str]:
    acc = member[:1].upper() + member[1:] if member else member
    names = {acc}
    if acc.endswith("ies"):
        names.add(acc[:-3] + "y")
    if acc.endswith("s"):
        names.add(acc[:-1])
    return sorted(names)


def find_class_span(lines: List[str], class_name: str) -> Optional[int]:
    pattern = re.compile(r"^class %s[(:]" % re.escape(class_name))
    for i, line in enumerate(lines):
        if pattern.match(line):
            return i
    return None


def span_end(lines: List[str], start: int) -> int:
    for j in range(start + 1, len(lines)):
        if lines[j].strip() and not lines[j].startswith((" ", "\t", ")", "#")) and not lines[j].startswith("@"):
            return j
    return len(lines)


def replace_docstring(lines: List[str], def_idx: int, content: Optional[str], indent: str) -> None:
    """Replace (or insert/remove) the docstring of the def/class at def_idx.

    content is emitted in the repo's 3-line form ('\"\"\"' / content lines / '\"\"\"') with
    every line at `indent`; None removes the docstring entirely."""
    open_idx = None
    for j in range(def_idx + 1, min(def_idx + 6, len(lines))):
        stripped = lines[j].strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            break
        if stripped.startswith(QUOTE):
            open_idx = j
        break
    if open_idx is None:
        if content is None:
            return
        block = [indent + QUOTE] + [indent + ln for ln in content.split("\n")] + [indent + QUOTE]
        lines[def_idx + 1 : def_idx + 1] = block
        return
    single_line = lines[open_idx].strip().endswith(QUOTE) and len(lines[open_idx].strip()) > 3
    if single_line:
        if content is None:
            del lines[open_idx]
            return
        close_idx = open_idx
    else:
        close_idx = None
        for j in range(open_idx + 1, len(lines)):
            if QUOTE in lines[j]:
                close_idx = j
                break
        if close_idx is None:
            return
        if content is None:
            del lines[open_idx : close_idx + 1]
            return
    block = [indent + QUOTE] + [indent + ln for ln in content.split("\n")] + [indent + QUOTE]
    lines[open_idx : close_idx + 1] = block


def replace_leading_comment(lines: List[str], member_idx: int, new_text: str) -> None:
    start = member_idx
    while start - 1 >= 0 and lines[start - 1].strip().startswith("#"):
        start -= 1
    indent = re.match(r"\s*", lines[member_idx]).group(0)
    lines[start:member_idx] = [f"{indent}# {new_text}"]


def build_checklist(entry: Dict, spec_line: str, rw_flags: Dict[str, tuple], rel: str) -> List[str]:
    cls = entry["class"]
    methods = set(entry.get("methods", []))
    rows = [f"# {cls} method parity checklist:", spec_line, "# Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)"]
    rows.append("# [x] __init__" + " " * 4 + f"[x] impl  [x] docstring  [x] test  [—] reader  [—] writer  {rel}")
    for attr in entry.get("spec_attributes", []):
        member = attr.get("model_member")
        if not member:
            continue
        _, mutator, getter = rw_flags.get(member, (True, False, False))
        accs = accessor_names(member)
        getter_row = next((a for a in accs if f"get{a}" in methods), None)
        setter_row = next((a for a in accs if any(f"{p}{a}" in methods for p in ("set", "add", "create"))), None)
        reader_col = "[x] reader" if (setter_row and mutator) else "[—] reader"
        writer_col = "[x] writer" if (getter_row and getter) else "[—] writer"
        if getter_row:
            rows.append(f"# [x] get{getter_row}".ljust(34) + f"[x] impl  [x] docstring  [x] test  {reader_col}  {writer_col}  {rel}")
        if setter_row:
            verb = next((v for v in ("add", "create", "set") if f"{v}{setter_row}" in methods))
            rows.append(f"# [x] {verb}{setter_row}".ljust(34) + f"[x] impl  [x] docstring  [x] test  {reader_col}  {writer_col}  {rel}")
    return rows


def has_test(cls: str) -> bool:
    for d in TEST_DIRS:
        if not d.is_dir():
            continue
        for tf in d.rglob("test_*.py"):
            try:
                if cls in tf.read_text(encoding="utf-8", errors="replace"):
                    return True
            except OSError:
                continue
    return False


def checklist_span(lines: List[str], start: int, end: int, cls: str):
    """(start, end_exclusive, spec_line) of the consecutive comment block beginning at
    the class's parity-checklist header, else (None, None, None)."""
    cl_start = None
    for j in range(start, end):
        if re.match(r"\s*#\s*%s method parity checklist:" % re.escape(cls), lines[j]):
            cl_start = j
            break
    if cl_start is None:
        return None, None, None
    cl_end = cl_start
    spec_line = None
    for j in range(cl_start + 1, end):
        if lines[j].lstrip().startswith("#"):
            if "# Spec:" in lines[j] and spec_line is None:
                spec_line = lines[j].strip()
            cl_end = j
        else:
            break
    return cl_start, cl_end, spec_line


def process_class(entry: Dict) -> Dict:
    file_path = ROOT / entry["file"]
    cls = entry["class"]
    src = file_path.read_text(encoding="utf-8")
    lines = src.split("\n")
    start = find_class_span(lines, cls)
    if start is None:
        return {"class": cls, "status": "class-not-found"}
    end = span_end(lines, start)
    indent = re.match(r"\s*", lines[start]).group(0) + "    "

    cl_start, cl_end, spec_line = checklist_span(lines, start, end, cls)
    if spec_line:
        rw_flags = {attr["model_member"]: (True, attr.get("mutator_covered", False), attr.get("getter_covered", False)) for attr in entry.get("spec_attributes", []) if attr.get("model_member")}
        rel = entry.get("release", "R23-11")
        new_block = build_checklist(entry, spec_line, rw_flags, rel)
        if not has_test(cls):
            new_block = [row.replace("[x] test", "[ ] test") for row in new_block]
        lines[cl_start : cl_end + 1] = [f"{indent}# {c}" if not c.startswith("#") else f"{indent}{c}" for c in new_block]
        end = span_end(lines, start)

    note = norm(entry.get("class_note") or "")
    if note:
        replace_docstring(lines, start, note, indent)
        end = span_end(lines, start)

    methods = entry.get("methods", [])
    for attr in entry.get("spec_attributes", []):
        member = attr.get("model_member")
        if not member:
            continue
        accs = accessor_names(member)
        note_text = norm(attr.get("note") or "")
        pat = re.compile(r"^\s*self\.%s\s*:" % re.escape(member))
        for j in range(start, end):
            if pat.match(lines[j]):
                if note_text:
                    replace_leading_comment(lines, j, note_text)
                    end = span_end(lines, start)
                break
        getter = next((f"get{a}" for a in accs if f"get{a}" in methods), None)
        if getter and note_text:
            gi = next((j for j in range(start, end) if re.match(r"\s*def %s\(" % re.escape(getter), lines[j])), None)
            if gi is not None:
                replace_docstring(lines, gi, note_text, re.match(r"\s*", lines[gi]).group(0) + "    ")
                end = span_end(lines, start)
        for verb in ("set", "add", "create"):
            m_name = next((f"{verb}{a}" for a in accs if f"{verb}{a}" in methods), None)
            if m_name and note_text:
                mi = next((j for j in range(start, end) if re.match(r"\s*def %s\(" % re.escape(m_name), lines[j])), None)
                if mi is not None:
                    noop = (ADD_NOOP if verb == "add" else SETTER_NOOP).format(member=member)
                    guarded = "if value is not None" in "\n".join(lines[mi : mi + 40])
                    replace_docstring(lines, mi, f"{note_text}\n{noop}" if guarded else note_text, re.match(r"\s*", lines[mi]).group(0) + "    ")
                    end = span_end(lines, start)

    init_idx = next((j for j in range(start, end) if re.match(r"\s*def __init__\(", lines[j])), None)
    if init_idx is not None:
        for j in range(init_idx + 1, min(init_idx + 4, end)):
            if lines[j].strip().startswith(QUOTE):
                replace_docstring(lines, init_idx, None, indent)
                break

    new_src = "\n".join(lines)
    if new_src != src:
        file_path.write_text(new_src, encoding="utf-8")
        return {"class": cls, "status": "rewritten"}
    return {"class": cls, "status": "unchanged"}


def process_enum(entry: Dict) -> Dict:
    file_path = ROOT / entry["file"]
    cls = entry["class"]
    src = file_path.read_text(encoding="utf-8")
    lines = src.split("\n")
    start = find_class_span(lines, cls)
    if start is None:
        return {"class": cls, "status": "class-not-found"}
    end = span_end(lines, start)
    indent = re.match(r"\s*", lines[start]).group(0) + "    "

    cl_start, cl_end, spec_line = checklist_span(lines, start, end, cls)
    if spec_line:
        rel = entry.get("release", "R23-11")
        new_block = [
            f"# {cls} method parity checklist:",
            spec_line,
            "# Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)",
            "# [x] __init__" + " " * 4 + f"[x] impl  [x] docstring  [x] test  [—] reader  [—] writer  {rel}",
            "# (no methods) — serialized as an attribute value on the consuming class",
        ]
        lines[cl_start : cl_end + 1] = [f"{indent}{c}" for c in new_block]
        end = span_end(lines, start)

    note = norm(entry.get("class_note") or "")
    if note:
        replace_docstring(lines, start, note, indent)
        end = span_end(lines, start)

    literal_notes = {norm(lit["name"]): norm(lit["note"]) for lit in entry.get("spec_literals", [])}
    pat = re.compile(r'^(\s*)([A-Za-z_][A-Za-z0-9_]*)\s*=\s*"([^"]*)"')
    for j in range(start, end):
        m = pat.match(lines[j])
        if not m:
            continue
        note_text = literal_notes.get(m.group(3))
        if note_text:
            replace_leading_comment(lines, j, note_text)

    new_src = "\n".join(lines)
    if new_src != src:
        file_path.write_text(new_src, encoding="utf-8")
        return {"class": cls, "status": "rewritten"}
    return {"class": cls, "status": "unchanged"}


def main() -> int:
    dump_path = sys.argv[1]
    only_files = set(sys.argv[2:]) if len(sys.argv) > 2 else None
    entries = json.loads(Path(dump_path).read_text(encoding="utf-8"))
    results = []
    for entry in entries:
        if not entry.get("found", False):
            results.append({"class": entry["class"], "status": "no-source"})
            continue
        if entry.get("release") is None:
            results.append({"class": entry["class"], "status": "no-spec-table (arbitration pending)"})
            continue
        if only_files and entry["file"] not in only_files:
            continue
        if entry.get("is_enum"):
            results.append(process_enum(entry))
        else:
            results.append(process_class(entry))
    for r in results:
        print(f"[{r['status']}] {r['class']}")
    from collections import Counter

    print("\n" + str(Counter(r["status"] for r in results)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
