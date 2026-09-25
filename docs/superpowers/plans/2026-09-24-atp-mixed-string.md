# atpMixedString Phase 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the `AtpMixedString` mixin base unifying the pure-text `<<atpMixedString>>` shape, migrate the 4 existing classes to it, and queue the remaining 21 pure-text classes.

**Architecture:** Mixin base `AtpMixedString(ARObject)` (same pattern as `VariationPointCapable`) provides `mixedString` + `getMixedString()/setMixedString()`; parser/writer get `readMixedStringText`/`writeMixedStringText` helpers for future queue classes; existing 4 classes are renamed onto the base API (breaking rename, tests updated in same pass). Spec: `docs/superpowers/specs/2026-09-24-atp-mixed-string-design.md`.

**Tech Stack:** Python 3.8-compatible typing (`typing.Optional`), pytest, xml.etree.ElementTree, Black at 200 chars.

> **Status 2026-09-25:** Tasks 1–8 landed (PR #785 + the Group8 VP-family syncs; queue rows via the
> Group8 dependency audit). The snippets below show the originally drafted `__init__(self, parent)`
> API — what actually landed (and what §9 of the design now mandates) is the no-parent,
> class-level-default form; then the 2026-09-25 redesign moved the mixin to interface level in
> `StereotypeMixins.py` (Tasks 9–15 below).

**Environment:** uv-managed repo. Run tests via `uv run pytest ...`. Gates per task end: `npm run lint` (flake8+ruff), `npm run black` (format), full suite `uv run python scripts/run_tests.py --no-coverage`. Do NOT re-sort imports in `src/armodel/models/**`, parser, writer (I001 intentionally disabled). Do not commit `.venv`.

---

### Task 1: `AtpMixedString` base class (TDD)

**Files:**
- Create: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/AtpMixedString.py`
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/__init__.py`
- Test: `tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_AtpMixedString.py`

- [x] **Step 1: Write the failing test**

```python
import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AtpMixedString import AtpMixedString


class _Parent(ARObject):
    pass


class _Mixed(AtpMixedString):
    def __init__(self):
        super().__init__(_Parent())


def test_abstract_guard():
    with pytest.raises(TypeError):
        AtpMixedString(_Parent())


def test_default_none_and_round_trip():
    m = _Mixed()
    assert m.getMixedString() is None
    assert m.setMixedString("A and\n B ").getMixedString() == "A and\n B "
    assert isinstance(m, AtpMixedString)


def test_none_noop_and_chaining():
    m = _Mixed()
    m.setMixedString("keep")
    assert m.setMixedString(None) is m
    assert m.getMixedString() == "keep"
```

- [x] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_AtpMixedString.py -q`
Expected: FAIL / collection error — `ModuleNotFoundError: AtpMixedString`

- [x] **Step 3: Write the implementation**

```python
from typing import Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class AtpMixedString(ARObject):
    """
    This is a mixed content model with intermixed text. This is applied to metaclasses only.
    """

    # AtpMixedString — implementation support base for the <<atpMixedString>> stereotype.
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.md, [TPS_GST_00025], section 2.3.1 (R23-11)
    # Serialization: R23-11/AUTOSAR_FO_TPS_XMLSchemaProductionRules.md, [TPS_XMLSPR_00047], section 3.2.4.2 (R23-11)
    # No spec table: stereotype-inherent accessors have no attribute rows ("no spec row" convention).
    # Columns: impl / docstring / test   ([—] = no spec row)
    # [ ] __init__          [ ] impl  [ ] docstring  [ ] test
    # [ ] getMixedString    [ ] impl  [ ] docstring  [ ] test
    # [ ] setMixedString    [ ] impl  [ ] docstring  [ ] test

    def __init__(self, parent):
        if type(self) is AtpMixedString:
            raise TypeError("AtpMixedString is an abstract class.")
        super().__init__(parent)

        # The unqualified text content mixed into the element (<<atpMixedString>>).
        # Whitespace is preserved verbatim (no strip/normalize).
        self.mixedString: Optional[str] = None

    def getMixedString(self) -> Optional[str]:
        """The unqualified text content mixed into the element (<<atpMixedString>>)."""
        return self.mixedString

    def setMixedString(self, value: Optional[str]) -> "AtpMixedString":
        """
        The unqualified text content mixed into the element (<<atpMixedString>>).
        A None value is a no-op and does not clear previously set text.
        """
        if value is not None:
            self.mixedString = value
        return self
```

Add to `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/__init__.py`:

```python
from .AtpMixedString import *
```

- [x] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_AtpMixedString.py -q`
Expected: 3 passed

- [x] **Step 5: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/AtpMixedString.py src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/__init__.py tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_AtpMixedString.py
git commit -m "feat: add AtpMixedString mixin base for <<atpMixedString>>"
```

---

### Task 2: Parser/writer helpers

**Files:**
- Modify: `src/armodel/parser/arxml_parser.py` (add method near other readXxx helpers, e.g. after `readStringValue`)
- Modify: `src/armodel/writer/arxml_writer.py` (add method near other writeXxx helpers)
- Test: `tests/test_armodel/parser/test_mixed_string_text.py` (covers both helpers)

- [x] **Step 1: Write the failing test**

```python
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AtpMixedString import AtpMixedString
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class _Parent(ARObject):
    pass


class _Mixed(AtpMixedString):
    def __init__(self):
        super().__init__(_Parent())


def test_read_mixed_string_text():
    e = ET.Element("COND-BY-FORMULA")
    e.text = "A and B"
    m = _Mixed()
    ARXMLParser().readMixedStringText(e, m)
    assert m.getMixedString() == "A and B"


def test_read_none_text_noop():
    e = ET.Element("COND-BY-FORMULA")
    m = _Mixed()
    ARXMLParser().readMixedStringText(e, m)
    assert m.getMixedString() is None


def test_write_mixed_string_text_and_omit():
    m = _Mixed()
    m.setMixedString("X or Y")
    e = ET.Element("COND")
    ARXMLWriter().writeMixedStringText(e, m)
    assert e.text == "X or Y"

    m2 = _Mixed()
    e2 = ET.Element("COND")
    ARXMLWriter().writeMixedStringText(e2, m2)
    assert e2.text is None
```

- [x] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_armodel/parser/test_mixed_string_text.py -q`
Expected: FAIL — `AttributeError: 'ARXMLParser' object has no attribute 'readMixedStringText'`

- [x] **Step 3: Implement both helpers**

In `arxml_parser.py`:

```python
    def readMixedStringText(self, element, obj):
        """<<atpMixedString>>: the element text is the value (pure-text shape).
        Whitespace is preserved verbatim."""
        if element.text is not None and obj is not None:
            obj.setMixedString(element.text)
```

In `arxml_writer.py`:

```python
    def writeMixedStringText(self, element, obj):
        """<<atpMixedString>>: write getMixedString() as element text; None omits the text node."""
        if obj is not None:
            element.text = obj.getMixedString()
```

- [x] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_armodel/parser/test_mixed_string_text.py -q`
Expected: 3 passed

- [x] **Step 5: Commit**

```bash
git add src/armodel/parser/arxml_parser.py src/armodel/writer/arxml_writer.py tests/test_armodel/parser/test_mixed_string_text.py
git commit -m "feat: add readMixedStringText/writeMixedStringText helpers"
```

---

### Task 3: Migrate `ConditionByFormula`

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py:315-355` (class + `_text`/`getText`/`setText` removal)
- Modify: `src/armodel/parser/arxml_parser.py:1286` (`condition.setText(element.text)`)
- Modify: `src/armodel/writer/arxml_writer.py:1164` (`text = condition.getText()`)
- Test: `tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py`, `tests/test_armodel/parser/test_arxml_parser_variation_point.py`, `tests/test_armodel/writer/test_writer_variation_point.py`

- [x] **Step 1: Update tests to the new API first (Red)**

In all 3 test files replace `condition_by_formula.setText(` / `.getText()` occurrences for ConditionByFormula objects with `setMixedString(` / `getMixedString()`. Locate them:

```bash
grep -n "setText\|getText" tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py tests/test_armodel/parser/test_arxml_parser_variation_point.py tests/test_armodel/writer/test_writer_variation_point.py
```

Add one assertion to the ConditionByFormula model test:

```python
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AtpMixedString import AtpMixedString
assert isinstance(condition_by_formula, AtpMixedString)
```

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py -q`
Expected: FAIL — `AttributeError: 'ConditionByFormula' object has no attribute 'setMixedString'`

- [x] **Step 2: Migrate the model**

In `VariantHandling/__init__.py`: change `class ConditionByFormula(ARObject):` → `class ConditionByFormula(AtpMixedString):` (add import `from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AtpMixedString import AtpMixedString` respecting existing import style); delete `self._text: Optional[str] = None` (line ~335) and the `getText`/`setText` methods (~347-355).

- [x] **Step 3: Migrate parser/writer call sites**

Parser line 1286: `condition.setText(element.text)` → `self.readMixedStringText(element, condition)` (confirm the element variable in scope is the one whose `.text` was read). Writer line 1164: `text = condition.getText()` → `text = condition.getMixedString()` (keep surrounding `if text is not None:` logic unchanged).

- [x] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py tests/test_armodel/parser/test_arxml_parser_variation_point.py tests/test_armodel/writer/test_writer_variation_point.py -q`
Expected: all passed

- [x] **Step 5: Commit**

```bash
git add -u src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py src/armodel/parser/arxml_parser.py src/armodel/writer/arxml_writer.py tests/
git commit -m "feat: migrate ConditionByFormula onto AtpMixedString"
```

---

### Task 4: Migrate `AttributeValueVariationPoint`

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/AttributeValueVariationPoints/__init__.py:15-119`
- Modify: `src/armodel/parser/arxml_parser.py:3043` (`avp.setText(element.text)`)
- Modify: `src/armodel/writer/arxml_writer.py:4305` (`text = avp.getText()`)
- Test: `tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/AttributeValueVariationPoints/test_AttributeValueVariationPoints.py`, `tests/test_armodel/parser/test_arxml_parser_variation_point.py`, `tests/test_armodel/writer/test_writer_variation_point.py`

- [x] **Step 1: Update tests to the new API first (Red)**

In all 3 test files replace `setText(` / `getText()` occurrences for AttributeValueVariationPoint objects with `setMixedString(` / `getMixedString()`. Locate them:

```bash
grep -n "setText\|getText" tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/AttributeValueVariationPoints/test_AttributeValueVariationPoints.py tests/test_armodel/parser/test_arxml_parser_variation_point.py tests/test_armodel/writer/test_writer_variation_point.py
```

Add one assertion to the model test:

```python
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AtpMixedString import AtpMixedString
assert isinstance(avp, AtpMixedString)
```

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/AttributeValueVariationPoints/test_AttributeValueVariationPoints.py -q`
Expected: FAIL — no attribute `setMixedString`

- [x] **Step 2: Migrate the model**

`class AttributeValueVariationPoint(ARObject, ABC):` → `class AttributeValueVariationPoint(AtpMixedString, ABC):`; delete `self._text: Optional[str] = None` (~L53) and `getText`/`setText` (~L111-119). AVP is abstract (`ABC`); keep its `__init__` guard and `super().__init__(parent, short_name)` signature — only the `_text` init line goes.

- [x] **Step 3: Migrate parser/writer call sites**

Parser L3043: `avp.setText(element.text)` → `self.readMixedStringText(element, avp)`. Writer L4305: `text = avp.getText()` → `text = avp.getMixedString()`.

- [x] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/ tests/test_armodel/parser/test_arxml_parser_variation_point.py tests/test_armodel/writer/test_writer_variation_point.py -q`
Expected: all passed

- [x] **Step 5: Commit**

```bash
git add -u src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/AttributeValueVariationPoints/__init__.py src/armodel/parser/arxml_parser.py src/armodel/writer/arxml_writer.py tests/
git commit -m "feat: migrate AttributeValueVariationPoint onto AtpMixedString"
```

---

### Task 5: Migrate `TimingConditionFormula`

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition.py:250-301`
- Modify: `src/armodel/parser/arxml_parser.py:3352` (`tcf.setText(element.text)`)
- Modify: `src/armodel/writer/arxml_writer.py:4527` (`text = tcf.getText()`)
- Test: `tests/test_armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/test_TimingConditionFormula.py`, `tests/test_armodel/parser/test_arxml_parser_timing_condition_formula.py`, `tests/test_armodel/writer/test_writer_timing_condition_formula.py`

- [x] **Step 1: Update tests to the new API first (Red)** — rename `setText`/`getText` → `setMixedString`/`getMixedString` in the 3 test files; add `isinstance(tcf, AtpMixedString)`.

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/test_TimingConditionFormula.py -q`
Expected: FAIL — no attribute `setMixedString`

- [x] **Step 2: Migrate the model**

`class TimingConditionFormula(Referrable):` → `class TimingConditionFormula(Referrable, AtpMixedString):`; delete `self._text: Optional[str] = None` (~L291) and `getText`/`setText` (~L293-301).

- [x] **Step 3: Migrate parser/writer call sites**

Parser L3352: `tcf.setText(element.text)` → `self.readMixedStringText(element, tcf)`. Writer L4527: `text = tcf.getText()` → `text = tcf.getMixedString()`.

- [x] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/test_TimingConditionFormula.py tests/test_armodel/parser/test_arxml_parser_timing_condition_formula.py tests/test_armodel/writer/test_writer_timing_condition_formula.py -q`
Expected: all passed

- [x] **Step 5: Commit**

```bash
git add -u src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition.py src/armodel/parser/arxml_parser.py src/armodel/writer/arxml_writer.py tests/
git commit -m "feat: migrate TimingConditionFormula onto AtpMixedString"
```

---

### Task 6: Migrate `TDEventOccurrenceExpressionFormula`

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingDescription/TimingDescriptionEvents/TDEventOccurrenceExpression.py:15-70`
- Modify: `src/armodel/parser/arxml_parser.py:3340` (`formula.setText(element.text)`)
- Modify: `src/armodel/writer/arxml_writer.py:4516` (`text = formula.getText()`)
- Test: `tests/test_armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingDescription/TimingDescriptionEvents/test_TDEventOccurrenceExpressionFormula.py`, `tests/test_armodel/parser/test_parser_timing_descriptions.py`, `tests/test_armodel/writer/test_writer_timing_descriptions.py`

- [x] **Step 1: Update tests to the new API first (Red)** — rename in the 3 test files (grep `setText\|getText` there; only TDEventOccurrenceExpressionFormula-related sites change); add `isinstance` assertion.

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingDescription/TimingDescriptionEvents/test_TDEventOccurrenceExpressionFormula.py -q`
Expected: FAIL — no attribute `setMixedString`

- [x] **Step 2: Migrate the model**

`class TDEventOccurrenceExpressionFormula(Referrable):` → `class TDEventOccurrenceExpressionFormula(Referrable, AtpMixedString):`; delete `self._text: Optional[str] = None` (~L51) and its `getText`/`setText` methods.

- [x] **Step 3: Migrate parser/writer call sites**

Parser L3340: `formula.setText(element.text)` → `self.readMixedStringText(element, formula)`. Writer L4516: `text = formula.getText()` → `text = formula.getMixedString()`.

- [x] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/ tests/test_armodel/parser/test_parser_timing_descriptions.py tests/test_armodel/writer/test_writer_timing_descriptions.py -q`
Expected: all passed

- [x] **Step 5: Commit**

```bash
git add -u src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingDescription/TimingDescriptionEvents/TDEventOccurrenceExpression.py src/armodel/parser/arxml_parser.py src/armodel/writer/arxml_writer.py tests/
git commit -m "feat: migrate TDEventOccurrenceExpressionFormula onto AtpMixedString"
```

---

### Task 7: Queue the remaining 21 pure-text classes

**Files:**
- Modify: the owning group todo files under `docs/plan/sync-todo/` (locate via index)

- [x] **Step 1: Locate owning group per package**

```bash
grep -n "VariantHandling\|Timing\|GenericStructure" docs/plan/sync-todo/SyncTodoIndex.md
```

VP family (11 classes, package `GenericStructure/VariantHandling/...`) and VariantHandling formulas follow the Group file owning GenericStructure; Timing formulas follow the Group owning CommonStructure Timing. Append rows in dependency order (see spec §6).

- [x] **Step 2: Append rows with 9-step sub-checklists**

Row template (one per class, dependency-first; class in backticks, base noted after the dash):

```markdown
- [ ] `BooleanValueVariationPoint` — AttributeValueVariationPoint subclass — CP_TPS_SoftwareComponentTemplate Table (locate at Step 1)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
```

Order: `AbstractEnumerationValueVariationPoint`, `AbstractNumericalVariationPoint` (abstract first) → `BooleanValueVariationPoint`, `FloatValueVariationPoint`, `IntegerValueVariationPoint`, `LimitValueVariationPoint`, `NumericalValueVariationPoint`, `PositiveIntegerValueVariationPoint`, `TimeValueValueVariationPoint`, `UnlimitedIntegerValueVariationPoint` → `FormulaExpression` → `BlueprintFormula`, `CompuGenericMath`, `EcucConditionFormula`, `EcucParameterDerivationFormula`, `EcucQueryExpression`, `SwSystemconstDependentFormula`, `FMConditionByFeaturesAndAttributes`, `FMConditionByFeaturesAndSwSystemconsts`, `FMFormulaByFeaturesAndAttributes`, `FMFormulaByFeaturesAndSwSystemconsts`. Classes already having rows anywhere are skipped (no duplicates). FM* rows carry a note: "closure check at Step 1 (FeatureDef etc. may be missing; Rule 0016)".

- [x] **Step 3: Commit**

```bash
git add docs/plan/sync-todo/
git commit -m "docs: queue 21 pure-text atpMixedString classes"
```

---

### Task 8: Full gates + wrap-up

- [x] **Step 1: Format + lint**

```bash
npm run black
npm run lint
```

Expected: black reformats 0 or few files (then re-run gates); ruff "All checks passed!"

- [x] **Step 2: Full suite**

```bash
uv run python scripts/run_tests.py --no-coverage
```

Expected: all tests passed, 0 failed (integration round-trip included)

- [x] **Step 3: Report summary**

Report: commits list, 4 migrated classes, base + helpers added, 21 classes queued. Phase 2 (Documentation mixed content) remains a separate project.

---

## Redesign tasks (2026-09-25): interface-level mixin + unified `StereotypeMixins` module

Approved design revision: `docs/superpowers/specs/2026-09-24-atp-mixed-string-design.md` §9.
Pattern reference: `docs/superpowers/plans/2026-09-03-variation-point-capable-mixin.md` (Task 4 — the
canonical interface-level mixin: `ABC`, class-level default, no `__init__`, module imports nothing
at runtime). User decision: physically unify both mixins into
`GeneralTemplateClasses/StereotypeMixins.py`; the old same-named sibling modules are deleted.

### Task 9: Update the design doc + this plan (docs first)

- [x] **Step 1: Design doc** — §3 API replaced with the interface-level form; §6 batch
      statuses recorded; §9 redesign section added.
- [x] **Step 2: Plan doc** — Tasks 1–8 ticked with the landed-state note; these redesign
      tasks appended.
- [x] **Step 3: Commit** — `docs: atpMixedString redesign — interface-level mixin + StereotypeMixins unification (design + plan)`.

### Task 10: Create `StereotypeMixins.py`, delete the old mixin modules

**Files:**
- Create: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/StereotypeMixins.py`
- Delete: `.../GeneralTemplateClasses/VariationPointCapable.py`, `.../GeneralTemplateClasses/AtpMixedString.py`
- Modify: `.../GeneralTemplateClasses/__init__.py` (star exports)
- Modify: `src/armodel/models/__init__.py` (star exports)

- [x] **Step 1: Write the module** — `VariationPointCapable` moved verbatim
      (TYPE_CHECKING import of `VariationPoint`, class-level default, get/set);
      `AtpMixedString` in its interface-level form (`ABC`, no `ARObject`, no
      `__init__`/guard, class-level default as the only init, accessors verbatim).
      Module imports nothing at runtime except `abc`/`typing`.
- [x] **Step 2: Repoint the star exports** — `GeneralTemplateClasses/__init__.py`:
      `from .StereotypeMixins import *  # noqa: F403`; `models/__init__.py`:
      `from armodel.models...GeneralTemplateClasses.StereotypeMixins import *  # noqa: F403`.
- [x] **Step 3: Delete the two old modules** (after Task 11 repoints their importers).
- [x] **Step 4: Commit** — `feat: unify stereotype mixins into StereotypeMixins.py`.

### Task 11: Repoint all import sites (mechanical, no re-sorting)

~116 sites: 80 src + 22 test files importing `VariationPointCapable`, 8 src + 6 test
importing `AtpMixedString`, plus `arxml_parser.py:443/446` and `arxml_writer.py:335/350`.

- [x] **Step 1: Sed the module path** in src/ and tests/:
      `GeneralTemplateClasses.VariationPointCapable` → `GeneralTemplateClasses.StereotypeMixins`,
      `GeneralTemplateClasses.AtpMixedString` → `GeneralTemplateClasses.StereotypeMixins`,
      and the relative `from .VariationPointCapable import *` / `from .AtpMixedString import *`
      forms. Never re-sort imports (repo rule).
- [x] **Step 2: Merge duplicate import lines** in the 4 files that imported both mixins
      (parser, writer, `models/__init__.py`, `GeneralTemplateClasses/__init__.py`) — one
      `StereotypeMixins` import each, preserving position (no re-sort).
- [x] **Step 3: Verify zero stale references**: grep for
      `GeneralTemplateClasses.VariationPointCapable`, `GeneralTemplateClasses.AtpMixedString`,
      `from .VariationPointCapable`, `from .AtpMixedString` across src/ tests/ → 0 hits.
- [x] **Step 4: Smoke**: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure -q --no-cov` green.

### Task 12: Consumer base fixes (ARObject was previously supplied by the mixin)

**Files:**
- `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py`
- `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/AttributeValueVariationPoints/__init__.py`

- [x] **Step 1:** `class ConditionByFormula(AtpMixedString):` →
      `class ConditionByFormula(ARObject, AtpMixedString):` (spec Base = ARObject, Table 7.5).
- [x] **Step 2:** `class AttributeValueVariationPoint(AtpMixedString, ABC):` →
      `class AttributeValueVariationPoint(ARObject, AtpMixedString, ABC):` (spec Base, Table 7.2).
- [x] **Step 3:** Unchanged by design: `TimingConditionFormula(Referrable, AtpMixedString)`,
      `TDEventOccurrenceExpressionFormula(Referrable, AtpMixedString)`, the 9-member AVP subclass
      chain. Verify each changed class's `super().__init__()` chain initializes every field
      exactly once (Rule 0001.2) — the MRO becomes `Cls → ARObject → AtpMixedString → ABC`.
- [x] **Step 4:** Run the VariantHandling + Timing test files — green.

### Task 13: Tests (Red → Green)

**Files:**
- `tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_AtpMixedString.py`
- `tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_VariationPointCapable.py` (imports only)
- `tests/test_armodel/parser/test_mixed_string_text.py` (imports only)

- [x] **Step 1: Rewrite `test_AtpMixedString.py`** — drop `test_abstract_guard`; probe
      subclass with no custom `__init__`; keep default/round-trip/None-no-op/whitespace-verbatim
      tests; add interface-shape assertions (`assert not issubclass(AtpMixedString, ARObject)`,
      `assert issubclass(AtpMixedString, ABC)`); add a capability-matrix test class
      (VariationPointCapable precedent): positives for `AttributeValueVariationPoint`,
      `ConditionByFormula`, `TimingConditionFormula`, `TDEventOccurrenceExpressionFormula`,
      `NumericalValueVariationPoint`; negatives for the Phase-2 boundary:
      `DocumentationBlock`, `LParagraph`, `MultiLanguageParagraph` must NOT be `AtpMixedString`.
- [x] **Step 2: Update imports** in `test_VariationPointCapable.py` +
      `test_mixed_string_text.py` to `StereotypeMixins` (adjust the probe there if it leaned
      on ARObject-via-mixin).
- [x] **Step 3: Full targeted run** — mixin tests, VariantHandling, Timing, parser
      test_mixed_string_text — green.

### Task 14: Rule 0021 (both skill mirrors, byte-identical) + Group8.md notes

- [x] **Step 1:** `.agents/skills/sync-autosar-class/rules.md` + `.claude/...` — Rule 0021:
      new module path `StereotypeMixins.py`; MRO-bypass bullet rewritten (no `__init__` at all —
      class-level default is the only init); base-order examples updated
      (`ConditionByFormula(ARObject, AtpMixedString)`, `AttributeValueVariationPoint(ARObject, AtpMixedString, ABC)`;
      Referrable combos unchanged); dated redesign note; "mixin does not extend ARObject".
- [x] **Step 2:** `docs/plan/sync-todo/Group8.md` — dated notes on the two pending-confirmation
      rows whose class statements change (`AttributeValueVariationPoint`, `ConditionByFormula`):
      9b review covers the interface-level shape.
- [x] **Step 3: Commit** — `docs: Rule 0021 + Group8 notes for the StereotypeMixins redesign`.

### Task 15: Full gates

- [x] **Step 1:** `npm run lint` + `npm run black-check` clean.
- [x] **Step 2:** `uv run pytest tests/test_armodel/ -q --no-cov` (baseline 11,904) +
      integration round-trip `uv run python scripts/run_tests.py --no-coverage`.
- [x] **Step 3: Report** — commits, unified module, consumer base fixes, test matrix.
