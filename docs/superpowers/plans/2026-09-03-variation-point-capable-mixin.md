# VariationPointCapable Mixin Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the `Identifiable.variationPoint` kept-deviation with a standard-conformant `VariationPointCapable` mixin, anchored on the 337 XSD variant classes (inherited by subclasses), so VARIATION-POINT round-trips only for classes where the AUTOSAR schema allows it.

**Architecture:** The XSD declares VARIATION-POINT once per *anchor* class (e.g. `PORT-PROTOTYPE` group) and concrete subclasses inherit the slot via `group ref` ([TPS_GST_00200]). We mirror this: one mixin (`VariationPointCapable`) holds the field + get/set; each anchor class adds the mixin to its bases; Python inheritance reproduces the XSD group-ref semantics. Reader/writer gate on `isinstance(obj, VariationationPointCapable)` at the single existing call site. `Identifiable` reverts to spec Table 4.4 exactly.

**Tech Stack:** Python 3.8-compatible typing (`Optional`, `TYPE_CHECKING`), pytest, lxml/ET parser-writer, black (200), ruff/flake8.

**Spec basis** (`autosar/R23-11/markdown/AUTOSAR_FO_TPS_GenericStructureTemplate.md`):
- §7.2.1 [TPS_GST_00199]: {PartClass} aggregates a VariationPoint
- §7.2.5 [TPS_GST_00195]: capability comes from the annotated meta-model, relaxed by the XSD
- constr_2638: no variation points in non-variant roles
- XSD ground truth: `autosar/R23-11/xsd/AUTOSAR_00052.xsd` — 337 anchor blocks; `IDENTIFIABLE` group has NO VARIATION-POINT; `PORT-PROTOTYPE` group does (l.92820)

**Verified facts this plan relies on:**
- Anchors: `PORT-PROTOTYPE` yes / `P-PORT-PROTOTYPE` no / `R-PORT-PROTOTYPE` no (inherit) · `AR-PACKAGE` yes (not an Identifiable!) · `TIMING-DESCRIPTION` yes · `STRUCTURED-REQ` yes · `TRACEABLE` no · `POST-BUILD-VARIANT-CRITERION` **no** · `IDENTIFIABLE` no
- Single parser call site: `src/armodel/parser/arxml_parser.py:1238-1242`; single generic writer call site: `src/armodel/writer/arxml_writer.py:1240-1241`
- `setStructuredReq` (writer l.2243-2274) suppresses the generic write and emits VARIATION-POINT **last** (XSD sequence, constr_2599) — this pattern is correct and MUST be preserved
- `StructuredReq(Traceable)` — anchor is `StructuredReq` itself, not `Traceable` (`src/armodel/models/M2/MSR/Documentation/BlockElements/RequirementsTracing.py:100`)
- `PortPrototype(AtpPrototype, ABC)` at `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py:339`; `ARPackage(CollectableElement)` at `.../GeneralTemplateClasses/ARPackage.py:359`
- Cycle constraint: `VariantHandling/__init__.py` imports `ARElement` from `ARPackage.py` at runtime → the mixin MUST live in a module that imports nothing at runtime (abc/typing only)

---

### Task 1: Baseline verification

**Files:** none (read-only)

**Step 1: Run the full suite and record the state**

Run: `cd /Users/ray/Workspace/py-armodel && python -m pytest -q 2>&1 | tail -5`
Expected: `1 failed, 8343 passed` — the single failure is the pre-existing `PortInterfaceBlueprintMapping` import issue. Any other failure = stop, fix environment first.

Run: `npm run lint && npm run black-check`
Expected: both clean.

---

### Task 2: Extract the 337 XSD anchors to a tracked artifact

**Files:**
- Create: `scripts/extract_vp_anchors.py`
- Create (generated): `docs/superpowers/plans/vp_anchors.txt`

**Step 1: Write the extraction script**

```python
import re
import sys

XSD = "autosar/R23-11/xsd/AUTOSAR_00052.xsd"

SPECIAL = {
    "AR-PACKAGE": "ARPackage",
}


def to_class_name(kebab: str) -> str:
    if kebab in SPECIAL:
        return SPECIAL[kebab]
    return "".join(part.capitalize() for part in kebab.split("-"))


def main() -> int:
    lines = open(XSD).read().split("\n")
    anchors, current = [], None
    for line in lines:
        m = re.search(r'<xsd:(complexType|group) name="([A-Z0-9-]+)"', line)
        if m:
            current = m.group(2)
        if 'name="VARIATION-POINT"' in line and current:
            anchors.append(current)
    with open("docs/superpowers/plans/vp_anchors.txt", "w") as f:
        for name in anchors:
            f.write("%s -> %s\n" % (name, to_class_name(name)))
    print("anchors:", len(anchors))
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

**Step 2: Run it**

Run: `python scripts/extract_vp_anchors.py`
Expected: `anchors: 337` and `docs/superpowers/plans/vp_anchors.txt` exists.

**Step 3: Commit**

```bash
git add scripts/extract_vp_anchors.py docs/superpowers/plans/vp_anchors.txt
git commit -m "chore: extract 337 VARIATION-POINT XSD anchors"
```

---

### Task 3: Mixin unit tests (Red)

**Files:**
- Create: `tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_VariationPointCapable.py`

**Step 1: Write the failing tests**

```python
import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint


class TestVariationPointCapable:
    def test_default_is_none(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

        class Probe(VariationPointCapable):
            pass

        assert Probe().getVariationPoint() is None

    def test_round_trip_and_none_noop(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

        class Probe(VariationPointCapable):
            pass

        probe = Probe()
        vp = VariationPoint()
        assert probe.setVariationPoint(vp) is probe
        assert probe.getVariationPoint() is vp
        probe.setVariationPoint(None)
        assert probe.getVariationPoint() is vp
```

**Step 2: Run to verify failure**

Run: `python -m pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_VariationPointCapable.py -v`
Expected: FAIL — `ModuleNotFoundError: ... VariationPointCapable`

---

### Task 4: Implement the mixin (Green)

**Files:**
- Create: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/VariationPointCapable.py`

**Step 1: Write the mixin** — this module deliberately imports nothing at runtime except `abc`/`typing` (cycle constraint: `VariantHandling/__init__.py` imports `ARPackage.py` at runtime; anchor classes in `ARPackage.py`/`Components/__init__.py` will import this mixin at runtime):

```python
from abc import ABC
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint


class VariationPointCapable(ABC):
    variationPoint: Optional["VariationPoint"] = None

    def getVariationPoint(self) -> Optional["VariationPoint"]:
        return self.variationPoint

    def setVariationPoint(self, value: Optional["VariationPoint"]) -> "VariationPointCapable":
        if value is not None:
            self.variationPoint = value
        return self
```

The class-level default avoids any `__init__`, so adding the mixin to an anchor's bases never perturbs cooperative `super().__init__(parent, short_name)` chains or explicit `ARObject.__init__(self)` calls.

**Step 2: Run the tests to green**

Run: `python -m pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_VariationPointCapable.py -v`
Expected: 2 passed.

**Step 3: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/VariationPointCapable.py tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_VariationPointCapable.py
git commit -m "feat: add VariationPointCapable mixin"
```

---

### Task 5: Capability matrix tests (Red for anchoring)

**Files:**
- Modify: `tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_VariationPointCapable.py`

**Step 1: Add the matrix tests** — capability must come *through inheritance* exactly like the XSD group refs:

```python
class TestVariationPointCapabilityMatrix:
    def test_pr_port_capable_via_port_prototype(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PRPortPrototype

        assert issubclass(PRPortPrototype, VariationPointCapable)

    def test_ar_package_capable(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArPackage import ARPackage
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

        assert issubclass(ARPackage, VariationPointCapable)

    def test_structured_req_capable(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import StructuredReq

        assert issubclass(StructuredReq, VariationPointCapable)

    def test_post_build_variant_criterion_not_capable(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import PostBuildVariantCriterion

        assert not issubclass(PostBuildVariantCriterion, VariationPointCapable)
```

**Step 2: Run to verify failure**

Run: `python -m pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_VariationPointCapable.py -v`
Expected: matrix tests FAIL (`issubclass` False); mixin tests still pass.

---

### Task 6: Anchor the pilot classes (Green)

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py:339` — `class PortPrototype(AtpPrototype, ABC):` → `class PortPrototype(AtpPrototype, VariationPointCapable, ABC):` + runtime import of the mixin at the top of the file (import order in `models/**` is cycle-sensitive — see AGENTS.md; place the import with the other GeneralTemplateClasses imports)
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ARPackage.py:359` — `class ARPackage(CollectableElement):` → `class ARPackage(CollectableElement, VariationPointCapable):` + import. Cycle check for this specific file first: mixin module imports nothing at runtime → safe.
- Modify: `src/armodel/models/M2/MSR/Documentation/BlockElements/RequirementsTracing.py:100` — `class StructuredReq(Traceable):` → `class StructuredReq(Traceable, VariationPointCapable):` + import

**Step 1:** Apply the three edits. Do NOT touch `Identifiable` yet (existing VP tests keep passing via the old path).

**Step 2:** Run matrix tests
Run: `python -m pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_VariationPointCapable.py -v`
Expected: all PASS.

Run: `python -m pytest tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate -q`
Expected: no regression (MRO smoke via existing tests).

**Step 3:** Commit

```bash
git add -A src/armodel/models tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_VariationPointCapable.py
git commit -m "feat: anchor VariationPointCapable on PortPrototype/ARPackage/StructuredReq"
```

---

### Task 7: Writer gate (Red → Green)

**Files:**
- Test: `tests/test_armodel/writer/test_identifiable.py` (audit first — read l.1-120 to see which class `obj` is; if it is a non-anchor, move that test to an anchor class)
- Create: `tests/test_armodel/writer/test_variation_point_capability.py`
- Modify: `src/armodel/writer/arxml_writer.py:1240-1241`

**Step 1: Write the failing writer test**

```python
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint, PostBuildVariantCriterion
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _round_trip(value):
    src = tempfile.mktemp(suffix=".arxml")
    dst = tempfile.mktemp(suffix=".arxml")
    try:
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("Pkg")
        pkg.addElement(value)
        ARXMLWriter().save(src, document)
        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(src, document_2)
        ARXMLWriter().save(dst, document_2)
        return open(dst).read()
    finally:
        import os
        for path in (src, dst):
            if os.path.exists(path):
                os.remove(path)


class TestVariationPointWriterGate:
    def test_capable_class_writes_variation_point(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PRPortPrototype

        port = PRPortPrototype(None, "Port")
        port.setVariationPoint(VariationPoint())
        xml = _round_trip(port)
        assert "VARIATION-POINT" in xml

    def test_non_capable_class_never_writes_variation_point(self):
        criterion = PostBuildVariantCriterion(None, "Criterion")
        xml = _round_trip(criterion)
        assert "VARIATION-POINT" not in xml
```

(If `PostBuildVariantCriterion(None, "Criterion")` needs a package parent for `addElement`, create it via `pkg.createPostBuildVariantCriterion` or set the parent to the pkg — adjust to whatever the existing writer tests do for ARElements.)

**Step 2: Run to verify failure** — the non-capable test PASSES today only because `PostBuildCriterion` has no way to hold a VP; write a capable-but-suppressed probe instead if needed. The real Red: assert the gate exists by testing a non-anchor **Identifiable** subclass that can still hold VP today (any concrete class not in `docs/superpowers/plans/vp_anchors.txt`, e.g. `SymbolProps`-style Referrable or an anchor-less Identifiable — pick one from the artifacts and assert `"VARIATION-POINT" not in xml` after `setVariationPoint`; today that FAILS because `writeIdentifiable` writes unconditionally).

**Step 3: Implement the gate** in `arxml_writer.py:1240-1241`:

```python
        if write_variation_point and isinstance(identifiable, VariationPointCapable):
            self.writeVariationPoint(element, identifiable.getVariationPoint())
```

Add `VariationPointCapable` to the writer's model imports. Keep the `write_variation_point` parameter — `setStructuredReq` (l.2247) depends on it; the trailing explicit write at l.2274 stays.

**Step 4:** Run writer VP tests
Run: `python -m pytest tests/test_armodel/writer/test_identifiable.py tests/test_armodel/writer/test_writer_documentation_block.py tests/test_armodel/writer/test_writer_variation_point.py tests/test_armodel/writer/test_variation_point_capability.py -v`
Expected: all PASS (StructuredReq keeps working via its trailing write; `test_writer_documentation_block.py:68,149` covers it).

**Step 5:** Commit

```bash
git add src/armodel/writer/arxml_writer.py tests/test_armodel/writer/
git commit -m "feat: writer emits VARIATION-POINT only for VariationPointCapable"
```

---

### Task 8: Parser gate (Red → Green)

**Files:**
- Test: `tests/test_armodel/parser/test_arxml_parser_variation_point.py` (audit the criterion branch at l.81)
- Modify: `src/armodel/parser/arxml_parser.py:1238-1242`

**Step 1: Red.** `readIdentifiable` currently reads VARIATION-POINT blindly — after Task 6 a fixture VP on a non-capable class still populates it. Add a test: parse `tests/test_armodel/parser/data/VariationPoint.arxml`, assert the `PostBuildVariantCriterion` VP is **not** populated and a warning was logged (use the parser's warning mechanism — locate it first with `rg -n 'def warning|logger.warning' src/armodel/parser/arxml_parser.py | head`).

**Step 2: Implement the gate** in `arxml_parser.py:1238-1242`:

```python
        variation_point_element = self.find(element, "VARIATION-POINT")
        if variation_point_element is not None:
            if isinstance(identifiable, VariationPointCapable):
                identifiable.setVariationPoint(self.readVariationPoint(variation_point_element, VariationPoint()))
            else:
                self.logger.warning("VARIATION-POINT on non-variant element <%s> ignored" % self.getTagName(element))
```

Add the runtime import of `VariationPointCapable` (same cycle-safety reasoning as Task 6).

**Step 3: Green.** Run: `python -m pytest tests/test_armodel/parser/test_arxml_parser_variation_point.py tests/test_armodel/parser/test_port_prototype_annotations.py -v` — all PASS.

**Step 4:** Commit

```bash
git add src/armodel/parser/arxml_parser.py tests/test_armodel/parser/test_arxml_parser_variation_point.py
git commit -m "feat: parser reads VARIATION-POINT only for VariationPointCapable"
```

---

### Task 9: Mass anchoring (mechanical, batched)

**Files:** the anchor class files listed by mapping `docs/superpowers/plans/vp_anchors.txt` names to Python classes.

**Step 1:** Generate the work list — resolve each mapped class name to its defining file:

```bash
python3 - <<'EOF'
import re, subprocess
unresolved = []
for line in open("docs/superpowers/plans/vp_anchors.txt"):
    kebab, cls = line.strip().split(" -> ")
    out = subprocess.run(["grep", "-rl", "-E", r"class %s\(" % cls, "src/armodel/models"], capture_output=True, text=True).stdout.strip()
    if out:
        print("%s %s" % (cls, out))
    else:
        unresolved.append((kebab, cls))
print("UNRESOLVED:", unresolved)
EOF
```

**Step 2: Resolve every UNRESOLVED entry by hand** (name-map misses, e.g. `AdaptiveSwcInternalBehavior` spelling, acronym classes like `IEEE-1722-…`/`J1939-…`, classes not yet implemented). For not-yet-implemented classes: skip and note them in the commit message — they inherit capability when they are implemented and anchored.

**Step 3:** Edit anchors batch-by-batch (grouped by file, ~40 files). Pattern per class: add `, VariationPointCapable` before any `ABC` base + one import per file. Batches: (a) GeneralTemplateClasses, (b) SWComponentTemplate, (c) SystemTemplate, (d) CommonStructure, (e) BswModuleTemplate + ECUC*, (f) remainder.

After each batch:
Run: `python -m pytest tests/test_armodel/models -q`
Expected: PASS (MRO regressions surface immediately).

**Step 4:** Full suite + commit

```bash
python -m pytest -q 2>&1 | tail -3
git add src/armodel/models
git commit -m "feat: anchor VariationPointCapable on all 337 XSD variant classes"
```

---

### Task 10: Remove variationPoint from Identifiable

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py` — delete l.263-269 (deviation comment + checklist rows), l.295-296 (field), l.482-495 (get/set); replace the deviation block with a resolved note pointing at the mixin
- Modify: `tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_Identifiable.py:285-300, 460-475` — delete the two VP test bodies
- Modify: `tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py:393-399` — the `PostBuildVariantCriterion.setVariationPoint/getVariationPoint` test relies on the Identifiable field and breaks here (`PostBuildVariantCriterion` is NOT an anchor); convert it to a not-capable assertion: `pytest.raises(AttributeError)` on `setVariationPoint`, or `assert not issubclass(PostBuildVariantCriterion, VariationPointCapable)`
- Modify: `src/armodel/models/M2/MSR/Documentation/BlockElements/RequirementsTracing.py:136-137` — checklist rows: "(inherited from Identifiable" → "(inherited from VariationPointCapable"

**Step 1:** Make the four edits. `rg -n 'setVariationPoint|getVariationPoint' src/` afterwards must show only the mixin, parser, writer, and `RequirementsTracing` checklist.

**Step 2:** Run: `python -m pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure tests/test_armodel/models/M2/MSR/Documentation/BlockElements -q`
Expected: PASS.

**Step 3:** Commit

```bash
git add src/armodel/models tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure
git commit -m "refactor: Identifiable reverts to spec; VP capability moves to mixin"
```

---

### Task 11: Per-class Rule 0020 verification (XSD ↔ markdown, one class at a time)

Verify **Rule 0020** (the skill rule added with this plan) against reality for **every
refactored class** in `docs/superpowers/plans/vp_anchors.txt` — one class at a time. For each
class, gather both sources' evidence, compare, and record the verdict. Deviations are
written to a report; they either amend Rule 0020 or become accepted-deviation rows.

**Files:**
- Create: `scripts/verify_vp_rule.py` — prints the per-class evidence for steps A/B
- Create: `docs/superpowers/plans/vp_capability_audit_report.md` — the deviation report (append one row per class)

**Per-class procedure (repeat for each class, one by one):**

**Step A — XSD evidence.** Run `python scripts/verify_vp_rule.py <ClassName>` (or by hand):
locate the class's `<xsd:complexType name="<CLASS-UPPER-KEBAB">` / `<xsd:group name="…">`
in `autosar/R23-11/xsd/AUTOSAR_00052.xsd`; confirm it contains
`<xsd:element name="VARIATION-POINT">` (direct anchor) or arrives via an ancestor's
`group ref` (inherited). Copy the annotation's provenance line
`Applicable for: <WholeClass>.<role>` and `mmt.qualifiedName="<Class>.variationPoint"`.

**Step B — Markdown evidence.** Grep the R23-11 markdown corpus for the Rule 0020
trigger: an attribute row with `Kind = aggr`, the class in the Type column, and
`atpVariation` + `<role>.variationPoint.shortLabel` in the Note
(`rg '<ClassName>' autosar/R23-11/markdown/AUTOSAR_*_TPS_*.md` then eyeball the
containing table row). Record the file, table id, and the `WholeClass.role` pair.

**Step C — Compare & verdict.**

| Verdict | Condition |
|---|---|
| PASS | Markdown trigger `WholeClass.role` matches the XSD `Applicable for:` (direct anchor), or capability is inherited from an anchored ancestor (XSD group ref proves it) |
| DEVIATION `provenance-mismatch` | Both sides exist but name different `WholeClass.role` pairs |
| DEVIATION `no-markdown-trigger` | XSD anchor exists but no `Kind=aggr` + `atpVariation` row found anywhere in the markdown corpus |
| DEVIATION `no-xsd-anchor` | Markdown trigger row exists but the class (and its whole ancestor chain) has no VARIATION-POINT in the XSD — Rule 0020 over-predicts |
| NOTE `name-unmapped` | Anchor name maps to no Python class yet (not a rule deviation; implementation gap from Task 9 Step 2) |

**Step D — Report row.** Append to `docs/superpowers/plans/vp_capability_audit_report.md`:

```markdown
| <ClassName> | <direct anchor / inherited via <Ancestor> / absent> | `<Applicable for: X.y>` | <file + Table N.M + `Whole.role`> | PASS / DEVIATION:<category> / NOTE:<category> |
```

**Step E — Batch commit.** After each batch (same batch split as Task 9 a–f), commit
the report so far:

```bash
git add scripts/verify_vp_rule.py docs/superpowers/plans/vp_capability_audit_report.md
git commit -m "test: Rule 0020 per-class verification batch <x> (<n> classes)"
```

**Completion gate:**
- 100% of mapped classes have a report row (337 minus name-unmapped).
- Every `DEVIATION no-xsd-anchor` / `no-markdown-trigger` / `provenance-mismatch`
  row is either (a) fixed by amending Rule 0020 in `.agents/skills/sync-autosar-class/rules.md`
  (then re-verify the affected classes), or (b) accepted by the user as an
  `accepted-deviation` row in the report.
- Present the deviation summary to the user before Task 13 stamps anything.

**Helper script sketch** (`scripts/verify_vp_rule.py <ClassName>` — evidence printer,
verdict stays human):

```python
import re
import sys

XSD = "autosar/R23-11/xsd/AUTOSAR_00052.xsd"
KEBAB = sys.argv[1] if len(sys.argv) > 1 else sys.exit("usage: verify_vp_rule.py <KEBAB-CLASS-NAME>")

lines = open(XSD).read().split("\n")
current, direct = None, False
for i, line in enumerate(lines):
    m = re.search(r'<xsd:(complexType|group) name="([A-Z0-9-]+)"', line)
    if m:
        current = m.group(2)
    if current == KEBAB and 'name="VARIATION-POINT"' in line:
        direct = True
        block = "\n".join(lines[i:i + 6])
        prov = re.search(r"Applicable for: (.*)", block)
        qn = re.search(r'mmt.qualifiedName="([^"]+)"', block)
        print("XSD: DIRECT anchor at line", i + 1)
        print("XSD: Applicable for:", prov.group(1) if prov else "?")
        print("XSD: qualifiedName:", qn.group(1) if qn else "?")
if not direct:
    print("XSD: no direct VARIATION-POINT in group", KEBAB, "- check ancestor group refs")
```

---

### Task 12: Fixture audit (decision gate — ask the user)

**Files:** read-only audit of `tests/test_armodel/parser/data/VariationPoint.arxml` and any other fixture carrying VARIATION-POINT.

**Step 1:** `rg -l 'VARIATION-POINT' tests --glob '*.arxml'` then for each hit, check the enclosing element against `docs/superpowers/plans/vp_anchors.txt`.

**Step 2:** If any fixture carries VARIATION-POINT on a now-non-capable class (known candidate: `PostBuildVariantCriterion` in `VariationPoint.arxml`, exercised by `test_arxml_parser_variation_point.py:81`): STOP and present the conflict to the user. Project rules forbid editing fixtures to force an outcome; the options are (a) the class is genuinely an anchor and the XSD extraction missed a group indirection, or (b) the test asserts the new warning behavior (Task 8 already redirects it), or (c) user decides otherwise.

---

### Task 13: Docs, deviation tracker, final verification

**Files:**
- Modify: `docs/examples/method_deviation_by_class_v2.md` — mark the `Identifiable` variationPoint deviation RESOLVED (mixin), same style as the resolved entries
- Modify: `docs/plan/sync-todo/Group1.md` — if the `Identifiable` row carries the "Stamp withheld until per-class placement is resolved" note, replace with the resolution
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py` — checklist: the stamp blocker comment is gone; add `# Spec verified: R23-11` **only after 9b-style user confirmation** (never self-stamp)

**Step 1:** Full gates

```bash
python -m pytest -q 2>&1 | tail -3
npm run lint
npm run black-check
```
Expected: `1 failed, N passed` (pre-existing import issue only), lint clean, black clean.

Run: `python scripts/run_tests.py --integration` (29-file round-trip contract)
Expected: PASS.

**Step 2:** Commit docs

```bash
git add docs/
git commit -m "docs: record VariationPointCapable resolution of Identifiable VP deviation"
```

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-09-03-variation-point-capable-mixin.md`. Two execution options:

1. **Subagent-Driven (this session)** — fresh subagent per task, review between tasks, fast iteration
2. **Parallel Session (separate)** — open a new session with executing-plans, batch execution with checkpoints
