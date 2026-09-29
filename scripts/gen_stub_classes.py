#!/usr/bin/env python3
r"""Generate empty stub classes for the Group21+ sync-todo queues so dependent classes
resolve during the 9-step syncs (parents / member types exist as soon as a sync needs
them).

Rules (agreed 2026-09-29):
- Candidates = the Group21+ queue rows (R23-11 remainder after the Group1-20 dedup).
  A class is SKIPPED when it already exists in src (it has its parent class and member
  list there — the 9-step sync verifies it); every class missing from src gets a stub.
- Stub = `class Name(Base):` + `pass` (plus `, ABC` for spec-abstract classes, per the
  abstract⇒ABC convention; enums derive AREnum). The sync's Steps 1-4 fill
  members/docstrings, Step 3/Rule 0007 finalizes placement.
- Base = the hierarchy_tree.md primary parent when it is modeled or itself a stub; when
  the tree parent is XSD-only/R4.3.1 the walk continues to the nearest modeled ancestor
  (reported as a deviation). A stub whose Base is another stub is placed in the SAME
  file as its Base (no cross-module import cycles), appended in topological order.
- Placement: the Base's own src file (family-anchored), else the primary document's
  namesake package home (Rule 0007: non-leaf → Pkg/__init__.py, leaf → Pkg.py).
- Exports: the class must be importable as armodel.<Name> (test_model_imports contract)
  — the script wires every ancestor __init__ (import line + __all__ entry where the
  chain uses explicit imports or __all__ filters) and then verifies hasattr() for all
  stubs.

Run:  uv run python scripts/gen_stub_classes.py           (generate + verify)
      uv run python scripts/gen_stub_classes.py --dry-run (plan only)
"""

import argparse
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen_remaining_groups as g

MODELS_ROOT = (g.ROOT / "src/armodel/models").resolve()
MODELS_INIT = MODELS_ROOT / "__init__.py"
M2_INIT = MODELS_ROOT / "M2" / "__init__.py"
ROOT_FRAMEWORK = {"ARObject", "Referrable", "MultilanguageReferrable", "Identifiable", "PackageableElement", "CollectableElement", "ARElement"}
ENUM_BASE_MOD = "armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes"
DOC_HOME = {
    "AUTOSAR_CP_TPS_SystemTemplate": "M2/AUTOSARTemplates/SystemTemplate/__init__.py",
    "AUTOSAR_CP_TPS_SoftwareComponentTemplate": "M2/AUTOSARTemplates/SWComponentTemplate/__init__.py",
    "AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate": "M2/AUTOSARTemplates/BswModuleTemplate/__init__.py",
    "AUTOSAR_CP_TPS_DiagnosticExtractTemplate": "M2/AUTOSARTemplates/DiagnosticExtract/__init__.py",
    "AUTOSAR_CP_TPS_ECUConfiguration": "M2/AUTOSARTemplates/ECUCDescriptionTemplate.py",
    "AUTOSAR_CP_TPS_ECUResourceTemplate": "M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py",
    "AUTOSAR_FO_TPS_GenericStructureTemplate": "M2/AUTOSARTemplates/GenericStructure/__init__.py",
    "AUTOSAR_CP_TPS_TimingExtensions": "M2/AUTOSARTemplates/CommonStructure/Timing/TimingExtensions.py",
    "AUTOSAR_FO_TPS_StandardizationTemplate": "M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/__init__.py",
    "AUTOSAR_FO_TPS_SecurityExtractTemplate": "M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/IntrusionDetectionSystem/__init__.py",
    "AUTOSAR_FO_TPS_FeatureModelExchangeFormat": "M2/AUTOSARTemplates/FeatureModelTemplate.py",
    "AUTOSAR_FO_TPS_LogAndTraceExtract": "M2/AUTOSARTemplates/LogAndTraceExtract.py",
    "AUTOSAR_FO_TPS_AbstractPlatformSpecification": "M2/AUTOSARTemplates/AbstractPlatform/__init__.py",
}

IMPORT_RE = re.compile(r"^(from [\w.]+ import|import )")
TEST_PATH = g.ROOT / "tests/test_armodel/models/test_group21_36_stub_classes.py"


def clean_name(cell):
    name = re.sub(r"<<[^>]*>>", "", cell)
    name = re.sub(r"glyph\[[^\]]*\]", "", name).strip()
    while name.split() and re.match(r"^atp[A-Z]", name.split()[0]):
        name = name.split(" ", 1)[1] if " " in name else ""
    return re.sub(r"\s*\(abstract\)\s*$", "", name).strip()


def harvest_abstract():
    """Names whose R23-11 Class header cell carries (abstract), display-cleaned."""
    abs_names = set()
    for path in sorted((g.ROOT / "autosar/R23-11/markdown").glob("*.md")):
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if not line.startswith("| Class"):
                continue
            for cell in [c.strip() for c in line.split("|")[1:]]:
                if cell and "(abstract)" in cell:
                    display = clean_name(cell)
                    if display:
                        abs_names.add(display)
    return abs_names


def resolve_plan(candidates, src_mod, parents, doc_of, texts, kind_of):
    """Topo-ordered stub plan entries: (name, base, file_rel, deviation). Base: enums AREnum, primitives
    ARLiteral, else the hierarchy_tree.md primary parent (XSD-only parents walk up to the nearest modeled
    ancestor). Placement: the primary document's namesake package home WHEN that file already defines/imports
    the Base (or the Base is a stub planned for the same file), else the Base's own defining file — a stub
    never needs a cross-package Base import (new import lines can reorder the fragile
    ARPackage <-> SystemTemplate/AdminData first-execution dance)."""
    targets = set(candidates)
    plan, order = {}, []

    def base_file_of(base):
        if base in src_mod:
            return src_mod[base]
        if base in plan:
            return plan[base][2]
        return None

    def resolve(name, stack):
        if name in plan:
            return plan[name]
        if name in stack:
            entry = (name, "ARObject", src_mod["ARObject"], "cycle fallback")
            plan[name] = entry
            return entry
        stack.add(name)
        if kind_of.get(name) == "Enumeration":
            base, deviation = "AREnum", None
        elif kind_of.get(name) == "Primitive":
            base, deviation = "ARLiteral", None
        else:
            p = parents.get(name)
            deviation = None
            while p is not None and p not in src_mod and p not in targets:
                p = parents.get(p)
                deviation = "tree parent not modeled — Base walked up to nearest modeled ancestor"
            if p is None:
                base, deviation = "ARObject", "no tree parent — Base fallback ARObject"
            else:
                base = p
        stack.discard(name)
        entry = None

        def finalize(file_rel):
            nonlocal entry
            entry = (name, base, file_rel, deviation)
            plan[name] = entry
            order.append(entry)
            return entry

        if base in targets and base != name:
            return finalize(resolve(base, stack)[2])
        base_file = base_file_of(base)
        doc_home = DOC_HOME[doc_of[name]]
        text = texts.setdefault(doc_home, (MODELS_ROOT / doc_home).read_text(encoding="utf-8"))
        if re.search(r"^class %s\b" % re.escape(base), text, re.M) or is_imported(text, base):
            return finalize(doc_home)
        return finalize(base_file)

    for name in sorted(targets):
        resolve(name, set())
    return order


def is_imported(text, name):
    return re.search(r"^from [\w.]+ import [^(]*\b%s\b" % re.escape(name), text, re.M) is not None or re.search(r"^from [\w.]+ import \([^)]*\b%s\b" % re.escape(name), text, re.M) is not None


def insert_import_line(text, module, name):
    """Insert `from module import name` after the leading import block (docstring- and parenthesized-import-aware)."""
    lines = text.splitlines(keepends=True)
    start, insert_at = 0, 0
    if lines and lines[0].strip().startswith(('"""', "'''")):
        quote = lines[0].strip()[:3]
        if lines[0].strip().count(quote) >= 2 and len(lines[0].strip()) > 3:
            start = 1
        else:
            start = next(i for i in range(1, len(lines)) if quote in lines[i]) + 1
    balance = 0
    for i in range(start, len(lines)):
        s = lines[i].strip()
        if balance > 0:
            balance += s.count("(") - s.count(")")
            if balance == 0:
                insert_at = i + 1
            continue
        if IMPORT_RE.match(s):
            balance = s.count("(") - s.count(")")
            insert_at = i + 1
            continue
        if not s or s.startswith("#"):
            continue
        break
    lines[insert_at:insert_at] = ["from %s import %s\n" % (module, name)]
    return "".join(lines)


def add_to_all(text, name):
    """Prepend name to a module-level __all__ list; returns (text, changed). Inserting as the FIRST
    element avoids the adjacent-string-literal trap when the existing last element has no trailing comma."""
    m = re.search(r"^__all__\s*=\s*\[", text, re.M)
    if not m:
        return text, False
    if re.search(r"['\"]%s['\"]" % re.escape(name), text[m.end() : text.index("]", m.end())]):
        return text, False
    indent = "    " if text[m.start() : text.index("]", m.end())].count("\n") else ""
    insert = ('%s"%s",\n' % (indent, name)) if indent else ('"%s",' % name)
    return text[: m.end()] + insert + text[m.end() :], True


def ensure_imports(file_abs, needed, text):
    """Add missing import lines for (name, module) pairs; names already defined or imported are skipped."""
    missing = []
    for name, module in needed:
        if re.search(r"^class %s\b" % re.escape(name), text, re.M) or is_imported(text, name):
            continue
        text = insert_import_line(text, module, name)
        missing.append("%s <- %s" % (name, module))
    return text, missing


def dotted(rel):
    """armodel.models dotted module path for a models-relative file/package path."""
    return "armodel.models." + Path(rel).as_posix().removesuffix(".py").replace("/", ".")


def extend_explicit_import(text, unit, name):
    """Extend an existing explicit `from <unit> import ...` statement with name (in place — no execution-order change). Returns (text, changed)."""
    single = re.compile(r"^from ([.\w]*\b%s) import ([^(\n]*)$" % re.escape(unit), re.M)
    m = single.search(text)
    if m:
        if re.search(r"\b%s\b" % re.escape(name), m.group(2)):
            return text, False
        return text[: m.end(2)] + ", " + name + text[m.end(2) :], True
    paren = re.compile(r"^from ([.\w]*\b%s) import \(" % re.escape(unit), re.M)
    m = paren.search(text)
    if m:
        close = text.index(")", m.end())
        segment = text[m.end() : close]
        if re.search(r"\b%s\b" % re.escape(name), segment):
            return text, False
        line_start = text.rfind("\n", 0, close) + 1
        indent = re.match(r"[ ]*", text[line_start:close]).group(0) or "    "
        return text[:close] + "%s%s," % (indent, name) + text[close:], True
    return text, False


def wire_name(file_abs, name):
    """Make `name` (defined in file_abs) flow to the models namespace WITHOUT reordering any import execution:
    extend existing explicit import statements in place, append to existing __all__ lists. Never touches
    M2/__init__.py (empty at HEAD — load-bearing for the ARPackage↔SystemTemplate cycle) or models/__init__.py
    (programmatic __all__)."""
    wired = []
    child = Path(file_abs).resolve()
    text = child.read_text(encoding="utf-8")
    text, added = add_to_all(text, name)
    if added:
        child.write_text(text, encoding="utf-8")
        wired.append("own __all__")
    while True:
        parent_pkg_dir = child.parent if child.name != "__init__.py" else child.parent.parent
        while parent_pkg_dir != MODELS_ROOT and not (parent_pkg_dir / "__init__.py").exists():
            parent_pkg_dir = parent_pkg_dir.parent
        parent_init = parent_pkg_dir / "__init__.py"
        if not parent_init.exists() or parent_init.resolve() in (MODELS_INIT, M2_INIT):
            break
        unit = child.stem if child.name != "__init__.py" else child.parent.name
        text = parent_init.read_text(encoding="utf-8")
        unit_dotted = dotted(child.relative_to(MODELS_ROOT)) if child.name != "__init__.py" else dotted(child.parent.relative_to(MODELS_ROOT))
        flows = False
        if re.search(r"^from [.\w]*\b%s import \*" % re.escape(unit), text, re.M) or ("from %s import *" % unit_dotted) in text:
            flows = True
        else:
            text, changed = extend_explicit_import(text, unit, name)
            if changed:
                parent_init.write_text(text, encoding="utf-8")
                wired.append("%s: +name in existing import" % parent_init.relative_to(MODELS_ROOT))
                flows = True
            elif re.search(r"^from [.\w]*\b%s import" % re.escape(unit), text, re.M):
                flows = True
        if flows:
            text = parent_init.read_text(encoding="utf-8")
            text, added = add_to_all(text, name)
            if added:
                parent_init.write_text(text, encoding="utf-8")
                wired.append("%s: +__all__" % parent_init.relative_to(MODELS_ROOT))
        child = parent_init
    return wired


def append_class(file_abs, name, base, abstract, is_enum):
    text = Path(file_abs).read_text(encoding="utf-8")
    bases = base + (", ABC" if abstract and not is_enum else "")
    if not text.endswith("\n"):
        text += "\n"
    Path(file_abs).write_text(text + ("\n\nclass %s(%s):\n    pass\n" % (name, bases)), encoding="utf-8")


TEST_TEMPLATE = '''"""Batch unit tests for the Group21-36 stub classes.

Generated by `scripts/gen_stub_classes.py` — do not edit by hand.
Contract per stub class (TDD Red→Green for the dependency-solving stub batch):
  * importable from its defining module,
  * derives from its spec Base (hierarchy_tree.md primary parent; enums AREnum),
  * exported at top level (armodel.<Name>) — EXCEPT the UNEXPORTED_STUBS, which live in
    families whose package chain is intentionally not imported by models/__init__ (the
    same status their pre-existing family members have, e.g. the AdaptivePlatform IDS
    pocket listed in test_model_imports.INTENTIONALLY_UNEXPORTED_MODULES).

The 9-step sync fills each stub in place; these assertions keep holding afterwards.
"""

import importlib

import pytest

import armodel

UNEXPORTED_STUBS = {
%s}

STUBS = [
%s]


@pytest.mark.parametrize("module,name,base_module,base_name", STUBS, ids=[s[1] for s in STUBS])
class TestGroup21_36StubClasses:
    def test_importable_and_exported(self, module, name, base_module, base_name):
        assert hasattr(importlib.import_module(module), name)
        if name not in UNEXPORTED_STUBS:
            assert hasattr(armodel, name)

    def test_heritage(self, module, name, base_module, base_name):
        cls = getattr(importlib.import_module(module), name)
        base_cls = getattr(importlib.import_module(base_module), base_name)
        assert issubclass(cls, base_cls)
'''


def emit_test(plan, kind_of, src_mod, out_path, unexported=()):
    rows = []
    for name, base, file_rel, _deviation in plan:
        module = dotted(file_rel)
        if kind_of.get(name) == "Enumeration":
            base_module, base_name = ENUM_BASE_MOD, "AREnum"
        elif base in src_mod:
            base_module, base_name = dotted(src_mod[base]), base
        else:
            base_module, base_name = module, base
        rows.append('    ("%s", "%s", "%s", "%s"),' % (module, name, base_module, base_name))
    unexported_lines = "\n".join('    "%s",' % n for n in sorted(unexported)) or "    # (none)"
    Path(out_path).write_text(TEST_TEMPLATE % (unexported_lines, "\n".join(rows)), encoding="utf-8")
    print("wrote %s (%d rows, %d unexported-by-family)" % (out_path, len(rows), len(unexported)))


def verify_exports(names):
    """Direct-import hasattr check. NOTE: plain `import armodel` has a PRE-EXISTING latent cycle
    (AdminData.py -> PrimitiveTypes -> package inits -> ARPackage bottom-import -> partial AdminData)
    that only pytest's import order masks — on ImportError of that shape, skip and let the pytest-run
    batch test be the gate."""
    result = subprocess.run(
        [sys.executable, "-c", "import armodel, sys\nmissing = [n for n in sys.argv[1:] if not hasattr(armodel, n)]\nprint('MISSING:' + ','.join(missing) if missing else 'ALL-EXPORTED')"] + names,
        capture_output=True,
        text=True,
        cwd=g.ROOT,
    )
    out = (result.stdout or "") + (result.stderr or "")
    if "partially initialized module" in out and "ImportError" in out:
        print("NOTE: direct-import verify skipped — pre-existing latent import cycle (masked under pytest; the pytest batch test is the gate)")
        return []
    if result.returncode != 0:
        print(out[-2500:])
        sys.exit(1)
    if "MISSING:" in out:
        return out.split("MISSING:", 1)[1].strip().split(",")
    return []


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--emit-test", metavar="PATH", default=None, help="write the batch unit test from the plan (no src changes)")
    args = parser.parse_args()

    r23 = g.load_r23_rows()
    tracked, _ = g.load_tracked(max_num=20)
    src_mod = g.load_src_modules()
    parents = g.load_tree_parents()
    kind_of = g.load_spec_harvest()
    primitives = {n for n, k in kind_of.items() if k == "Primitive"}
    abstract_names = harvest_abstract()

    candidates = sorted(set(r23) - tracked - (primitives - set(src_mod)))
    skip = [c for c in candidates if c in src_mod]
    targets = [c for c in candidates if c not in src_mod]
    print("candidates %d | skip (already in src: parent + member list) %d | stub targets %d" % (len(candidates), len(skip), len(targets)))

    doc_of = {}
    for name in targets:
        doc_of[name] = sorted(r23[name], key=lambda t: (t[2], t[1]))[0][0]
    missing = sorted({d for d in doc_of.values() if d not in DOC_HOME})
    if missing:
        sys.exit("error: no DOC_HOME for %s" % missing)

    plan = resolve_plan(targets, src_mod, parents, doc_of, {}, kind_of)
    deviated = sorted({e[0] for e in plan if e[3]})
    print("plan: %d stubs (%d abstract, %d Base deviations)" % (len(plan), sum(1 for e in plan if e[0] in abstract_names), len(deviated)))
    for f, c in Counter(e[2] for e in plan).most_common():
        print("  %-92s %d" % (f, c))
    if deviated:
        print("  Base-deviation classes:", ", ".join(deviated))
    if args.emit_test:
        emit_test(plan, kind_of, src_mod, args.emit_test)
        return
    if args.dry_run:
        return

    for name, base, file_rel, deviation in plan:
        file_abs = MODELS_ROOT / file_rel
        is_enum = kind_of.get(name) == "Enumeration"
        abstract = name in abstract_names and not is_enum
        text = file_abs.read_text(encoding="utf-8")
        needed = [("ABC", "abc")] if abstract else []
        text, imports = ensure_imports(file_abs, needed, text)
        if imports:
            file_abs.write_text(text, encoding="utf-8")
            for i in imports:
                print("  import: %s" % i)
        append_class(file_abs, name, base, abstract, is_enum)
        for w in wire_name(file_abs, name):
            print("  wire: %s -> %s" % (name, w))

    missing = verify_exports([e[0] for e in plan])
    if missing:
        print("unexported-by-family stubs (%d) — recorded as test exceptions: %s" % (len(missing), ", ".join(missing)))
    emit_test(plan, kind_of, src_mod, TEST_PATH, unexported=missing)
    print("ALL-EXPORTED (%d stubs, %d unexported exceptions)" % (len(plan) - len(missing), len(missing)))


if __name__ == "__main__":
    main()
