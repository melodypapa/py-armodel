# AREnum Value → XSD Value Renaming Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rename every diverging `AREnum` literal value string to the exact spelling used by its counterpart simpleType in the bundled R23-11 XSD — value strings only; no API, structure, parser, or writer architecture changes.

**Architecture:** A one-shot migration script rewrites class-level constant value strings (e.g. `CAUTION = "caution"` → `CAUTION = "CAUTION"`) in place, keeping constant names, comments, tuple order, and class structure untouched. Because the parser/writer `*_XML_MAP` tables key off the old camelCase values, their keys are regenerated from the same rename mapping — the only collateral edit, and it is mechanical. Tests asserting old literal strings are updated.

**Tech Stack:** Python 3.8-compatible code, stdlib `re`/`ast` for tooling, pytest.

---

## Scope boundaries (explicit)

**In scope:**
- Changing the *value strings* of AREnum subclass constants to the XSD enumeration spellings.
- Regenerating `*_XML_MAP` keys in `arxml_parser.py` / `arxml_writer.py` (they would otherwise look up renamed values and return `None`, silently dropping those fields).
- Updating tests that assert the old value strings.

**Out of scope (deliberately):**
- Adding missing XSD literals to any class (42 classes have some — untouched).
- The 10 empty-stub `IEEE1722Tp*` enums (XSD counterparts exist but they have zero constants — nothing to rename).
- Deleting/refactoring the `*_XML_MAP` mechanism, `_readEnumToken`, or any call site.
- Renaming or removing any constant, comment, or tuple.
- The 70 XSD value enums with no AREnum class at all (unmodeled — sync-queue territory).

## Measured current state (2026-10-06 audit, R23-11 XSD `src/armodel/validation/schemas/R23-11/AUTOSAR_00052.xsd`)

- 273 `AREnum` subclasses under `src/armodel/models/`; **43** already value-equal to XSD; **230** diverge. Of the 230: **220** have constants to rename; **10** are empty `IEEE1722Tp*` stubs (no constants — skipped). **0** have no XSD counterpart (an earlier kebab conversion without digit-boundary rules misclassified 14; the fixed `kebab()` below resolves e.g. `J1939` → `J-1939`, `Aes3` → `AES-3`).
- Name mapping: class `NoteTypeEnum` → kebab `NOTE-TYPE-ENUM` → simpleType `NOTE-TYPE-ENUM` or `NOTE-TYPE-ENUM--SIMPLE` (all value enums are `--SIMPLE`).
- No class has a value absent from the XSD, so every rename target is well-defined.
- XSD spelling quirks that the renames must honor exactly (they are what XSD-valid arxml contains): double-hyphen tokens `J-1939-NM--AAC`…`J-1939-NM--SVCA` and `AUTO-IP--DOIP` / `LINK-LOCAL--DOIP`; the merged token `AUTO-IPDHCPV-4` (Ipv4AddressSourceEnum; currently a *missing* literal, out of scope); dual spellings in `CalprmAxisCategoryEnum` (`COM-AXIS` vs `COM_AXIS`, out of scope to add).
- Full mismatch inventory reproducible with the Task 1 script; a planning-time snapshot lives at `/tmp/enum_audit.json`.

## Repo conventions that bind the executor

- Work in a **fresh worktree + branch off `origin/main`** (`feature/enum-xsd-value-rename`). NEVER commit to the user's in-flight branch (`feature/g19-9b-repairs`).
- Python 3.8 typing only (`typing.Optional[T]`, `typing.cast`); no `T | None`.
- Black at **200 chars**; verify `uv run black --version` is **24.8.0** first (26.x reformats 35 unrelated files).
- Do NOT re-sort imports in `src/armodel/models/**`, `arxml_parser.py`, `arxml_writer.py`.
- `uv run pytest ...` / `npm run lint` (includes mypy — must stay green).
- Conventional commits.
- **Test convention (this PR onward):** model enum values in tests are expressed as `EnumClass.CONSTANT`; plain strings are reserved for XML wire-format fixtures, constant↔literal pin-tests, and intentionally invalid values.

## File Structure

| File | Action |
|---|---|
| `scripts/rename_enum_values.py` | Create — one-shot value rename driven by the XSD |
| `src/armodel/models/M2/**/*.py` (~90 files) | Modify (script) — constant value strings only |
| `src/armodel/writer/arxml_writer.py` | Modify (script) — regenerate `*_XML_MAP` keys |
| `src/armodel/parser/arxml_parser.py` | Modify (script) — regenerate `*_XML_MAP` keys |
| `tests/test_armodel/**` (~30 files) | Modify — old literal strings → new |

---

### Task 1: Worktree setup

**Files:** none (git only)

- [ ] **Step 1: Create worktree off origin/main**

```bash
cd /Users/ray/Workspace
git -C py-armodel fetch origin
git worktree add py-armodel-wt-enumval -b feature/enum-xsd-value-rename py-armodel/origin/main
```

- [ ] **Step 2: Prepare venv**

```bash
cd /Users/ray/Workspace/py-armodel-wt-enumval
uv sync --extra pytest
uv pip install black==24.8.0
uv run black --version          # expect 24.8.0
uv run pytest tests/test_armodel/models -x -q --no-coverage   # green baseline
```

All later steps run inside `/Users/ray/Workspace/py-armodel-wt-enumval`.

---

### Task 2: Migration script (values only)

**Files:**
- Create: `scripts/rename_enum_values.py`

- [ ] **Step 1: Write the script**

The script computes, per AREnum class, a rename map `{old_value: xsd_value}` (only where they differ) and applies plain string replacements inside that class's source block. It also rewrites the `super().__init__(...)` tuple entries — but since the tuple references constants (`NoteTypeEnum.CAUTION`) whose *names* are unchanged, tuples need no edit in the common case; the script verifies tuple integrity anyway. Finally it regenerates `*_XML_MAP` keys in parser and writer from the union of all rename maps (old key → new key, value/token side untouched).

```python
"""Rename AREnum literal values to the R23-11 XSD enumeration spellings.

Value strings ONLY: constant names, comments, tuple order, and class
structure are untouched. Also regenerates *_XML_MAP keys in the parser and
writer whose keys reference renamed values.
"""
import os
import re

XSD_PATH = os.path.join("src", "armodel", "validation", "schemas", "R23-11", "AUTOSAR_00052.xsd")
MODELS_DIR = os.path.join("src", "armodel", "models")
MAP_FILES = [
    os.path.join("src", "armodel", "parser", "arxml_parser.py"),
    os.path.join("src", "armodel", "writer", "arxml_writer.py"),
]

SKIP_CLASSES = {
    # IEEE-1722 empty stubs: XSD counterparts exist but they define zero constants (nothing to rename)
    "IEEE1722TpAafAes3DataTypeEnum", "IEEE1722TpAafFormatEnum", "IEEE1722TpAafNominalRateEnum",
    "IEEE1722TpAcfCanMessageTypeEnum", "IEEE1722TpCrfPullEnum", "IEEE1722TpCrfTypeEnum",
    "IEEE1722TpRvfColorSpaceEnum", "IEEE1722TpRvfFrameRateEnum", "IEEE1722TpRvfPixelDepthEnum",
    "IEEE1722TpRvfPixelFormatEnum",
}


def kebab(name):
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "-", name)
    s = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", "-", s)
    s = re.sub(r"(?<=[A-Za-z])(?=\d)", "-", s)
    s = re.sub(r"(?<=\d)(?=[A-Za-z])", "-", s)
    return s.upper()


def load_xsd_enums(path):
    xsd = open(path, encoding="utf-8").read()
    enums = {}
    for n, body in re.findall(r'<xsd:simpleType name="([^"]+)">(.*?)</xsd:simpleType>', xsd, re.S):
        if "xsd:enumeration" in body and not n.endswith("--SUBTYPES-ENUM"):
            enums[n] = re.findall(r'<xsd:enumeration value="([^"]*)"', body)
    return enums


def class_renames(block, xsvals):
    """Return {old_value: new_value} for constants in this class block."""
    renames = {}
    for n, v in re.findall(r'\n    ([A-Z][A-Z0-9_]*) = "([^"]*)"', block):
        if v in xsvals or v in renames.values():
            continue
        # match by constant name, hyphen/underscore-insensitive (XSD has
        # double-hyphen tokens like J-1939-NM--AAC / AUTO-IP--DOIP)
        norm = re.sub(r"[^A-Z0-9]", "", n)
        for xv in xsvals:
            if re.sub(r"[^A-Z0-9]", "", xv) == norm:
                renames[v] = xv
                break
        else:
            raise RuntimeError("%s: no XSD value matches constant %s = %r" % (block.split("(")[0], n, v))
    return renames


def main():
    xsd = load_xsd_enums(XSD_PATH)
    all_renames = {}  # old -> new, across every class (old values are unique per class; collisions across classes are harmless for map keys)
    for root, _, files in os.walk(MODELS_DIR):
        for fn in files:
            if not fn.endswith(".py"):
                continue
            path = os.path.join(root, fn)
            src = open(path, encoding="utf-8").read()
            orig = src
            for m in re.finditer(r"class (\w+)\(AREnum\):", src):
                cls = m.group(1)
                if cls in SKIP_CLASSES:
                    continue
                base = kebab(cls)
                xsvals = None
                for cand in (base, base + "--SIMPLE"):
                    if cand in xsd:
                        xsvals = xsd[cand]
                        break
                if xsvals is None:
                    continue
                start = m.start()
                nxt = re.search(r"\nclass ", src[m.end():])
                end = m.end() + nxt.start() if nxt else len(src)
                block = src[start:end]
                renames = class_renames(block, xsvals)
                if not renames:
                    continue
                all_renames.update(renames)
                new_block = block
                for old, new in sorted(renames.items(), key=lambda kv: -len(kv[0])):
                    new_block = new_block.replace('"%s"' % old, '"%s"' % new)
                src = src[:start] + new_block + src[end:]
            if src != orig:
                open(path, "w", encoding="utf-8").write(src)
                print("rewrote", path)

    for path in MAP_FILES:
        src = open(path, encoding="utf-8").read()
        orig = src
        for old, new in sorted(all_renames.items(), key=lambda kv: -len(kv[0])):
            src = src.replace('"%s":' % old, '"%s":' % new)
        if src != orig:
            open(path, "w", encoding="utf-8").write(src)
            print("regenerated map keys in", path)
    print("total renames:", len(all_renames))


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it and spot-check**

```bash
cd /Users/ray/Workspace/py-armodel-wt-enumval
python scripts/rename_enum_values.py
```

Expected: ~90 model files rewritten, both `arxml_parser.py` and `arxml_writer.py` get map-key regenerations, ~500+ individual renames. Then spot-check `git diff` on at least 5 classes of different shapes (`NoteTypeEnum`, small; `LEnum`, ~120 values; `BindingTimeEnum`, map-covered; `DiagnosticResponseToEcuResetEnum`, diagnostic map-covered; `SwImplPolicyEnum`).

- [ ] **Step 3: Verify no stale old values remain in constants**

```bash
python scripts/rename_enum_values.py   # second run: "total renames" must drop to 0 further changes (idempotent)
git diff --stat | tail -3
```

- [ ] **Step 4: Format and run the unit suite to gauge damage**

```bash
uv run black src/armodel/models/
uv run pytest tests/test_armodel --no-coverage -q 2>&1 | tail -10
```

Expected: failures are old-literal assertions only (Task 4); no NameError/AttributeError (those would mean a broken edit).

- [ ] **Step 5: Commit**

```bash
git add -A src scripts/rename_enum_values.py
git commit -m "feat: rename AREnum literal values to R23-11 XSD spellings"
```

---

### Task 3: Round-trip sanity check

**Files:** none (verification only)

- [ ] **Step 1: Parse → write → re-parse an integration file exercising a map-covered enum**

```bash
uv run python - <<'EOF'
from armodel.AUTOSAR import AUTOSAR
from armodel.parser import ARXMLParser
from armodel.writer import ARXMLWriter
import glob, tempfile, os

parser = ARXMLParser(options={"warning": True})
writer = ARXMLWriter()
for f in sorted(glob.glob("tests/integration_tests/test_files/*.arxml")):
    doc = AUTOSAR.getInstance()
    AUTOSAR.setARRelease("R23-11")
    doc.clear()
    parser.load(f, doc)
    out = tempfile.mktemp(suffix=".arxml")
    writer.save(out, doc)
    doc2 = AUTOSAR.getInstance()
    doc2.clear()
    parser.load(out, doc2)
    writer.save(out + ".2", doc2)
    a, b = open(out).read(), open(out + ".2").read()
    assert a == b, "round-trip unstable: " + f
    os.remove(out); os.remove(out + ".2")
print("all integration files round-trip stable")
EOF
```

Expected: `all integration files round-trip stable` (the integration suite itself also covers this; this targets the map-covered fields explicitly).

- [ ] **Step 2: No commit** — pure verification gate before Task 4.

---

### Task 4: Repair dependent tests

**Files:**
- Modify: tests under `tests/test_armodel/` (drive from failures; expected hot spots: `tests/test_armodel/writer/test_writer_documentation_block.py`, `tests/test_armodel/models/M2/MSR/Documentation/BlockElements/test_OasisExchangeTable.py`, `tests/test_armodel/models/M2/MSR/AsamHdo/Constraints/test_GlobalConstraints.py`, `tests/test_armodel/models/M2/MSR/DataDictionary/test_DataDefProperties.py`, `tests/test_armodel/writer/test_writer_not_available_value_specification.py`, `tests/test_armodel/parser/test_arxml_parser_handlers.py`, `tests/test_armodel/parser/test_diagnostic_ecu_reset_class.py`, `tests/test_armodel/writer/test_writer_diagnostic_ecu_reset_class.py`)

- [ ] **Step 1: Bulk-replace unambiguous camelCase literals in tests**

Long camelCase values are collision-free; run per pair and eyeball the diff:

```bash
for pair in "codeGenerationTime CODE-GENERATION-TIME" "linkTime LINK-TIME" "preCompileTime PRE-COMPILE-TIME" "systemDesignTime SYSTEM-DESIGN-TIME" "notAvailable NOT-AVAILABLE" "notDefined NOT-DEFINED" "notValid NOT-VALID" "measurementPoint MEASUREMENT-POINT" "communicationInterEcu COMMUNICATION-INTER-ECU" "communicationIntraPartition COMMUNICATION-INTRA-PARTITION" "interPartitionIntraEcu INTER-PARTITION-INTRA-ECU" "newlineIfNecessary NEWLINE-IF-NECESSARY" "noNewline NO-NEWLINE" "refAll REF-ALL" "refNone REF-NONE" "refNonStandard REF-NON-STANDARD" "dependant DEPENDANT" "descendant DESCENDANT"; do
  set -- $pair
  grep -rl "\"$1\"\|'$1'" tests/ | xargs -r sed -i '' "s/\"$1\"/\"$2\"/g; s/'$1'/'$2'/g"
done
```

Do **NOT** blind-replace short generic words (`"full"`, `"none"`, `"open"`, `"closed"`, `"const"`, `"fixed"`, `"standard"`, `"queued"`, `"tip"`, `"caution"`, `"hint"`...) — fix those files individually from the failure list (the definitive old→new list is computed by `scripts/rename_enum_values.py`; add `--dump` printing of `all_renames` if needed).

This sed is for contexts that must remain strings (XML fixtures, pin-tests, invalid values). Model-construction/assertion sites should be converted to enum constants per Step 2 instead of receiving the new literal here.

- [ ] **Step 2: Prefer enum constants over new literals at repaired sites**

**Rule: whenever a repair touches a site that constructs or asserts a model enum value, replace the string with the enum constant instead of re-typing the new literal.**

```python
# before (broken by rename)
prototype.setSwCalibrationAccess(SwCalibrationAccessEnum().setValue("readOnly"))
assert prototype.getSwCalibrationAccess().getValue() == "readWrite"

# after — use the constant, not the new string
prototype.setSwCalibrationAccess(SwCalibrationAccessEnum().setValue(SwCalibrationAccessEnum.READ_ONLY))
assert prototype.getSwCalibrationAccess().getValue() == SwCalibrationAccessEnum.READ_WRITE
```

Three carve-outs where the string stays:
1. XML wire-format fixtures in parser/writer tests (`<SW-IMPL-POLICY>QUEUED</SW-IMPL-POLICY>` inside raw-XML strings) — serialized output, not the model value.
2. Contract pin-tests asserting a constant equals its literal (e.g. `assert SwImplPolicyEnum.CONST == "CONST"`) — deliberately string-based; update the spelling, keep the string form.
3. Intentionally invalid values fed to `setValue` in leniency tests — no constant exists.

Known-ambiguous values (76 strings are claimed by >1 enum, e.g. `none`, `KEEP`, `queued`, `always`, `in`, `standard`, `full`, `TOP`, `readOnly`): these must be resolved from the field under test's declared enum, not by global sed. Post-rename UPPER-KEBAB strings are mostly self-identifying, which is why this task runs after Task 2.

Rationale: constants make the suite rename-proof — a future XSD spelling change becomes a model-only edit.

- [ ] **Step 3: Full unit battery**

```bash
uv run pytest tests/ --no-coverage -q 2>&1 | tail -5
```

Expected: 0 failures.

- [ ] **Step 4: Commit**

```bash
git add tests/
git commit -m "test: align enum value expectations with XSD spellings"
```

---

### Task 5: Quality battery

- [ ] **Step 1: Format + lint + types**

```bash
npm run black
npm run lint     # flake8 syntax + ruff + mypy — must be green
```

- [ ] **Step 2: Full suite incl. coverage (CI parity)**

```bash
uv run python scripts/run_tests.py
```

Expected: full battery green.

- [ ] **Step 3: Regen sync reports only if the toolchain flags drift**

```bash
uv run python scripts/regen_sync_todo.py --write   # only if it reports changes; review diff
```

---

### Task 6: Update the `sync-autosar-class` skill rules

**Files:**
- Modify: `.agents/skills/sync-autosar-class/rules.md` (the `.claude/skills/` path is the same file via hardlink — edit either; note `.claude/skills/` itself is untracked, `.agents/` is the tracked copy)

**Why a task:** the current Rule 0011 mandates the *opposite* convention ("member value is the camelCase `mmt.qualifiedName` … write UPPERCASE only in test XML fixtures"). Landing the enum PR without this update would make every subsequent sync re-introduce camelCase values. Ship it in the same PR so rules and code flip together. (Do not edit rules.md on the user's in-flight branch outside this worktree.)

- [ ] **Step 1: Replace Rule 0010 and Rule 0011 with:**

```markdown
## Rule 0010 — Enums Inherit `AREnum` *(formerly Rule 11)*

Every enum inherits `AREnum` (not `Enum`, `str`+`Enum`, `IntEnum`, …), imported from
`…GenericTemplateClasses.PrimitiveTypes`. The body has members with string values, each
value being the **exact XSD enumeration-facet spelling** (see Rule 0011).

---

## Rule 0011 — Enum Specification Sync *(formerly Rule 12)*

- Locate the enum's spec `Enumeration` table; members 1:1 with the `Literal` rows — no
  extra, no missing. Placeholder shapes keep the right count with wrong values — verify
  each value against the `Literal` column (`mmt.qualifiedName`).
- Member **name**: spec literal → UPPER_SNAKE (`derivedFrom` → `DERIVED_FROM`).
- Member **value**: the **exact enumeration facet of the XSD `--SIMPLE` simpleType**
  (`src/armodel/validation/schemas/R23-11/AUTOSAR_00052.xsd`) — for R23-11 classes this
  is UPPER-KEBAB (`DERIVED_FROM = "DERIVED-FROM"`, `NoteTypeEnum.CAUTION = "CAUTION"`).
  The spec PDF/markdown literal (often camelCase) is the source for the member **name**,
  never the value. Find the simpleType by converting the class name to kebab-case with
  digit-boundary rules (`J1939` → `J-1939`, `Aes3` → `AES-3`), then try `<NAME>` and
  `<NAME>--SIMPLE`. Reproduce XSD spelling quirks verbatim — double-hyphen tokens
  (`J-1939-NM--AAC`, `AUTO-IP--DOIP`) and merged tokens (`AUTO-IPDHCPV-4`) are what
  XSD-valid arxml contains. The writer serializes the member value **verbatim** — there
  is no camelCase↔token translation step.
- Class docstring: the spec `Note` **verbatim from the markdown** (do not paraphrase).
  Each member has an inline comment citing the literal's description + Tags
  (`atp.EnumerationLiteralIndex=N`).
- **Tests use enum constants, not strings:** read and set via members
  (`MyEnum().setValue(MyEnum.MEMBER_NAME)`, assert `getValue() == MyEnum.MEMBER_NAME`).
  Plain strings are reserved for (a) XML wire-format fixtures in parser/writer tests,
  (b) constant↔literal pin-tests (`assert MyEnum.MEMBER == "<facet>"`), and (c)
  intentionally invalid values in leniency tests.
- A synced enum defines `__init__(self)` passing the tuple to `AREnum` in XSD facet
  order, so `MyEnum()` is instantiable.
```

- [ ] **Step 2: Sweep rules.md for stale echoes of the old convention** and fix each:

```bash
grep -n "member value\|mmt.qualifiedName\|UPPERCASE\|camelCase" .agents/skills/sync-autosar-class/rules.md
```

Known spots (verify each in context before editing): the test-guidance bullet near the
top ("To set an enum attribute, construct an instance (`MyEnum().setValue(MyEnum.MEMBER)`)
… read back with `getValue() == 4`") — keep the construct-the-instance guidance, drop any
"assert with the camelCase literal" phrasing; and the Rule 0009/0012 mentions of the
`AREnum` literal comment (unchanged — comments still cite `atp.EnumerationLiteralIndex`).

- [ ] **Step 3: Commit**

```bash
git add .agents/skills/sync-autosar-class/rules.md
git commit -m "docs: sync-autosar-class Rule 0010/0011 — enum values use XSD facet spellings"
```

---

### Task 7: Ship

- [ ] **Step 1: Push branch and open issue + PR** (repo convention: one issue + one PR via `gh`, PR closes the issue)

```bash
git push -u origin feature/enum-xsd-value-rename
gh issue create --title "Rename AREnum literal values to R23-11 XSD spellings" --body "<216 classes renamed value-strings only; XML_MAP keys regenerated; 14 no-XSD enums and 42 missing-literal classes explicitly out of scope>"
gh pr create --title "feat: rename AREnum literal values to XSD spellings (R23-11)" --body "Closes #<issue>"
```

- [ ] **Step 2: Watch CI** (`gh pr checks --watch`); fix regressions on the branch.

- [ ] **Step 3: Clean up the worktree only after the user merges** (verify merged into origin/main, then `git worktree remove` + delete local branch).

---

## Execution outcome (2026-10-06)

Executed inline; shipped as issue #951 / PR #952 (7 commits, CI green, MERGEABLE). Final state: 548 value renames across ~220 classes, XML_MAP keys regenerated (incl. the abstract-parser copy the plan missed), ARList TYPE attribute made verbatim (parser .lower()/writer .upper() pair removed), ~285 test files repaired, Rule 0010/0011 rewritten. Battery 20,335/0 after rebase onto G20/G29 merges. Plan deviations: test repair used strict enum-context matching after two value-level passes proved unsafe (option keys, short names, language codes, free-string fields collide with old enum values); constants conversion skips pin-test lines (carve-out 2).
