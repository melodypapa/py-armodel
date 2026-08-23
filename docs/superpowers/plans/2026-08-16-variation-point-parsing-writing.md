# VariationPoint Parsing and Writing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Add full ARXML reader/writer support for the structural `VariationPoint` (package `M2::AUTOSARTemplates::GenericStructure::VariantHandling`), per `docs/requirements/xsd/AUTOSAR_00046.xsd` (authoritative) and `autosar/R23-11/markdown/AUTOSAR_FO_TPS_GenericStructureTemplate.md` (Tables 7.4–7.6, Section 7.6).

**Architecture:** The `VariationPoint` model class already exists with impl/docstring/test parity, but nothing holds one and neither parser nor writer touches `<VARIATION-POINT>`. We attach an optional `variationPoint` attribute to the `Identifiable` base class (the same central hook that already reads/writes `DESC`, `ADMIN-DATA`, etc. for every Identifiable element), add mixed-content formula support to `ConditionByFormula` (ordered text + inline reference items so round-trips are lossless), then wire reader methods into `readIdentifiable()` and writer methods into `writeIdentifiable()`.

**Tech Stack:** Python 3.8+, lxml/ElementTree, pytest. No new dependencies.

## Spec Summary (verified against `docs/requirements/xsd/AUTOSAR_00046.xsd`)

### VARIATION-POINT (xsd group `AR:VARIATION-POINT`, line 99470)

`<VARIATION-POINT>` appears as an optional child of any variable element (xsd lines 1154, 1561, 2523, ... — spec examples: `SWC-INTERNAL-BEHAVIOR`, `RUNNABLE-ENTITY`). Child **sequence order is fixed by the XSD** (`xml.sequenceOffset` 10–50):

| # | Element | XSD type | Model attribute |
|---|---------|----------|-----------------|
| 1 | `SHORT-LABEL` (offset 10) | `AR:IDENTIFIER` | `shortLabel` |
| 2 | `DESC` (20) | `AR:MULTI-LANGUAGE-OVERVIEW-PARAGRAPH` | `desc` |
| 3 | `BLUEPRINT-CONDITION` (28) | `AR:DOCUMENTATION-BLOCK` | `blueprintCondition` |
| 4 | `FORMAL-BLUEPRINT-CONDITION` (29) | `AR:BLUEPRINT-FORMULA` | — **obsolete, not supported** |
| 5 | `FORMAL-BLUEPRINT-GENERATOR` (30) | `AR:BLUEPRINT-GENERATOR` | `formalBlueprintGenerator` |
| 6 | `SW-SYSCOND` (30) | `AR:CONDITION-BY-FORMULA` | `swSyscond` |
| 7 | `POST-BUILD-VARIANT-CONDITIONS` (40) | wrapper, unbounded `POST-BUILD-VARIANT-CONDITION` | `postBuildVariantConditions` |
| 8 | `SDG` (50) | `AR:SDG` | `sdg` |

The writer MUST emit children in this order. (The markdown spec examples show SHORT-LABEL before DESC as well — `AUTOSAR_FO_TPS_GenericStructureTemplate.md:13061`.)

### CONDITION-BY-FORMULA (xsd line 18334)

- `mixed="true"`; content = unbounded choice of `AR-OBJECT` / `FORMULA-EXPRESSION` / `SW-SYSTEMCONST-DEPENDENT-FORMULA` groups → in practice: free text interleaved with inline reference elements.
- Attribute `BINDING-TIME` of type `AR:BINDING-TIME-ENUM--SIMPLE` (optional in XSD).
- `SW-SYSTEMCONST-DEPENDENT-FORMULA` (xsd line 89067) allows **two** inline ref elements, both `DEST`-typed `SW-SYSTEMCONST--SUBTYPES-ENUM`:
  - `SYSC-REF` — internal (coded) value of the system constant
  - `SYSC-STRING-REF` — system constant evaluated as string

### POST-BUILD-VARIANT-CONDITION (xsd line 71152)

Sequence:
- `MATCHING-CRITERION-REF` — extension of `AR:REF`, `DEST` = `POST-BUILD-VARIANT-CRITERION--SUBTYPES-ENUM` (**tag is `MATCHING-CRITERION-REF`, NOT `POST-BUILD-VARIANT-CRITERION-REF`**)
- `VALUE` — XSD type `AR:INTEGER-VALUE-VARIATION-POINT` (mixed, may carry `BINDING-TIME`/`SD`/`SHORT-LABEL`/`BLUEPRINT-VALUE` attributes). **Handled as plain Integer text** — matches the existing codebase precedent: `readSwSystemconstValue` (`arxml_parser.py:7022`) already reads a `*-VALUE-VARIATION-POINT` VALUE element as a plain numerical. Attribute value pattern features on VALUE are out of scope (deviation, noted below).

### BLUEPRINT-GENERATOR (xsd line 7395)

Sequence: `INTRODUCTION` (`AR:DOCUMENTATION-BLOCK`, offset 10) then `EXPRESSION` (`AR:VERBATIM-STRING`, offset 20). Writer must emit INTRODUCTION first.

### Notes / deviations

- Spec markdown line 5618 ("SHORT-LABEL as XML attribute") refers to the *attribute value pattern* (`ATTRIBUTE-VALUE-VARIATION-POINT` attributeGroup, xsd:6672), NOT the structural variation point. Structural SHORT-LABEL is a child element (xsd:99477).
- `FORMAL-BLUEPRINT-CONDITION` (xsd:99497) is `atp.Status="obsolete"` and has no model attribute — skipped.
- VALUE's variation-point attributes/formula content not captured (attribute value pattern out of scope; matches SwSystemconstValue precedent).
- Known deviation: AUTOSAR allows variation points on non-Identifiable elements too (reference pattern `*-REF-CONDITIONAL`, property set pattern `*-VARIANTS`). This plan covers the structural/aggregation pattern attached to `Identifiable`, which is the dominant use.
- Implemented deviation (reader round-trip whitespace): the writer's `minidom.toprettyxml` (`abstract_arxml_writer.py:saveToFile`) reformats mixed-content elements, wrapping `SW-SYSCOND` text/tail fragments in newline+indentation. To keep parse→write→re-parse lossless, `readConditionByFormula` strips that formatting boundary via `_stripMixedContentWhitespace`. Consequently the byte-for-byte corpus copy (Task 5 Step 4) was **skipped** — a pretty-printed mixed-content file cannot round-trip byte-identically against a single-line source.
- Implemented deviation (writer hook guard): `writeIdentifiable`/`readIdentifiable` are also called for `ARPackage` (a `CollectableElement`, not an `Identifiable`), which lacks `getVariationPoint`/`setVariationPoint`; both hooks are guarded with `isinstance(identifiable, Identifiable)`.

## Existing State (verified)

- Model: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py` — `VariationPoint` (line 432), `ConditionByFormula` (383), `PostBuildVariantCondition` (312) fully implemented with getters/setters. Parity checklists show reader/writer columns all `[ ]` or blank.
- `ConditionByFormula` has only `bindingTime` — no formula content storage. Must be extended.
- Parser `readIdentifiable` at `src/armodel/parser/arxml_parser.py:766` — central hook, no VARIATION-POINT handling.
- Writer `writeIdentifiable` at `src/armodel/writer/arxml_writer.py:838` — central hook, no VARIATION-POINT handling.
- Parser already imports from `VariantHandling` (`arxml_parser.py:213`) — extend that import. Writer imports `SwSystemconstValue` from the same package.
- Helpers confirmed: parser `getSdg` (`arxml_parser.py:674`), `getMultiLanguageOverviewParagraph` (:856), `getDocumentationBlock` (:3403), `getChildElementOptionalIdentifier` (`abstract_arxml_parser.py:136`), `getChildElementOptionalIntegerValue` (:237), `getChildElementRefType` (:290). Writer: `setSdg` (`arxml_writer.py:653`), `setMultiLanguageOverviewParagraph` (:763), `writeDocumentationBlock` (:1614), `setChildElementOptionalIntegerValue` (`abstract_arxml_writer.py:97`), `setChildElementOptionalRefType` (:109).
- Tests: `tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py` exists. Parser snippet helper `_snip` + `parser` fixture in `tests/test_armodel/parser/conftest.py` / `_helpers.py`. Writer tests in `tests/test_armodel/writer/`.
- No `VARIATION-POINT` in any existing test ARXML file.

---

### Task 1: Attach variationPoint to Identifiable

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py`
- Test: `tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py`

- [x] **Step 1: Write the failing test**

Append to `tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py`:

```python
def test_identifiable_holds_variation_point():
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage

    parent = ARPackage(None, "Pkg")
    criterion = PostBuildVariantCriterion(parent, "MyCriterion")
    variation_point = VariationPoint()

    assert criterion.getVariationPoint() is None

    result = criterion.setVariationPoint(variation_point)

    assert criterion.getVariationPoint() is variation_point
    assert result is criterion
```

(`PostBuildVariantCriterion` extends `ARElement` → `Identifiable`, and is already imported at the top of the test file — no new import needed beyond the local `ARPackage` one shown.)

- [x] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py::test_identifiable_holds_variation_point -v`
Expected: FAIL with `AttributeError: 'PostBuildVariantCriterion' object has no attribute 'getVariationPoint'`

- [x] **Step 3: Write minimal implementation**

In `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py`:

3a. Extend the `typing` import at the top of the file to include `TYPE_CHECKING` (the file already imports `List`, `Optional`, etc. from `typing`), and add a guarded import after the existing imports:

```python
from typing import ..., TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
```

(The runtime import would be circular: `VariantHandling` imports `Identifiable` from this module. `TYPE_CHECKING` keeps the annotation string-only.)

3b. In `Identifiable.__init__` (after `self.desc`, around line 383), add:

```python
        # Structural variation point attached to this element (pattern: aggregation,
        # TPS_GST 7.6; XSD group AR:VARIATION-POINT, AUTOSAR_00046.xsd:99470).
        # Deviation: spec also allows variation points on non-Identifiable elements
        # (reference pattern, property set pattern); only the Identifiable
        # aggregation pattern is supported.
        self.variationPoint: Optional["VariationPoint"] = None
```

3c. Add getter/setter after the existing `getDesc`/`setDesc` methods of `Identifiable`:

```python
    def getVariationPoint(self) -> Optional["VariationPoint"]:
        """
        Returns the structural variation point of this element, if any.
        """
        return self.variationPoint

    def setVariationPoint(self, value: Optional["VariationPoint"]) -> "Identifiable":
        """
        Sets the structural variation point of this element. A None value is a no-op
        and does not overwrite an existing variationPoint.
        """
        if value is not None:
            self.variationPoint = value
        return self
```

- [x] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py::test_identifiable_holds_variation_point -v`
Expected: PASS

- [x] **Step 5: Run the full VariantHandling model test module (regression)**

Run: `pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py -v`
Expected: all PASS

- [x] **Step 6: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py \
        tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py
git commit -m "feat: attach structural variationPoint to Identifiable base class"
```

---

### Task 2: ConditionByFormula mixed-content formula items

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py` (class `ConditionByFormula`, line 383)
- Test: `tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py`

`SW-SYSCOND` (`CONDITION-BY-FORMULA`, xsd:18334, `mixed="true"`) carries a formula as mixed content: text interleaved with `SYSC-REF` and `SYSC-STRING-REF` elements (xsd:89075/89088). To round-trip losslessly we store an ordered list of items — plain `str` fragments and `(tag, RefType)` tuples, where tag is `"SYSC-REF"` or `"SYSC-STRING-REF"` (the two elements differ semantically: coded value vs string evaluation, so the tag must survive).

- [x] **Step 1: Write the failing test**

Append to `tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py`:

```python
def test_condition_by_formula_formula_items_ordered():
    sysc_ref = RefType().setValue("/SwSystemconsts/SY_TURBO").setDest("SW-SYSTEMCONST")
    string_ref = RefType().setValue("/SwSystemconsts/SY_MODE").setDest("SW-SYSTEMCONST")

    condition = ConditionByFormula()

    assert condition.getFormulaItems() == []

    result_text = condition.addFormulaText("defined(")
    result_ref = condition.addFormulaRef(sysc_ref)
    result_tail = condition.addFormulaText(") && ")
    result_string_ref = condition.addFormulaRef(string_ref, tag="SYSC-STRING-REF")

    items = condition.getFormulaItems()
    assert items[0] == "defined("
    assert items[1] == ("SYSC-REF", sysc_ref)
    assert items[2] == ") && "
    assert items[3] == ("SYSC-STRING-REF", string_ref)
    assert len(items) == 4
    assert result_text is condition
    assert result_ref is condition
    assert result_tail is condition
    assert result_string_ref is condition


def test_condition_by_formula_add_none_is_no_op():
    condition = ConditionByFormula()

    condition.addFormulaText(None)
    condition.addFormulaRef(None)

    assert condition.getFormulaItems() == []
```

- [x] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py::test_condition_by_formula_formula_items_ordered -v`
Expected: FAIL with `AttributeError: 'ConditionByFormula' object has no attribute 'getFormulaItems'`

- [x] **Step 3: Write minimal implementation**

In `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py`, class `ConditionByFormula`:

3a. In the file-level `from typing import List, Optional` (line 1), add `Tuple, Union`:

```python
from typing import List, Optional, Tuple, Union
```

3b. In `ConditionByFormula.__init__` (after the `bindingTime` assignment), add:

```python
        # Formula content of the atpMixedString SW-SYSCOND (XSD CONDITION-BY-FORMULA,
        # AUTOSAR_00046.xsd:18334): ordered text fragments (str) and inline system
        # constant references stored as (tag, ref) tuples, in document order.
        # tag is "SYSC-REF" (coded value) or "SYSC-STRING-REF" (string evaluation).
        self.formulaItems: List[Union[str, Tuple[str, RefType]]] = []
```

3c. Add methods after `setBindingTime`:

```python
    def getFormulaItems(self) -> List[Union[str, Tuple[str, RefType]]]:
        """
        Returns the formula content in document order: plain text fragments (str)
        and inline system constant references as (tag, RefType) tuples, where tag
        is "SYSC-REF" or "SYSC-STRING-REF", as they appear inside SW-SYSCOND.
        """
        return self.formulaItems

    def addFormulaText(self, value: str) -> "ConditionByFormula":
        """
        Appends a plain text fragment to the formula content. A None value is a no-op.
        """
        if value is not None:
            self.formulaItems.append(value)
        return self

    def addFormulaRef(self, value: RefType, tag: str = "SYSC-REF") -> "ConditionByFormula":
        """
        Appends an inline system constant reference to the formula content. tag is
        "SYSC-REF" (internal/coded value) or "SYSC-STRING-REF" (string evaluation).
        A None value is a no-op.
        """
        if value is not None:
            self.formulaItems.append((tag, value))
        return self
```

3d. Update the `ConditionByFormula` parity checklist block (lines ~400-405):

```python
    # ConditionByFormula method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 7.5, p.231
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBindingTime    [x] impl  [x] docstring  [x] test  [—] reader  [ ] writer
    # [x] setBindingTime    [x] impl  [x] docstring  [x] test  [ ] reader  [—] writer
    # [x] getFormulaItems   [x] impl  [x] docstring  [x] test  [ ] reader  [ ] writer
    # [x] addFormulaText    [x] impl  [x] docstring  [x] test  [ ] reader  [ ] writer
    # [x] addFormulaRef     [x] impl  [x] docstring  [x] test  [ ] reader  [ ] writer
```

(reader/writer columns stay open until Tasks 3–4 mark them `[x]`.)

- [x] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py -v`
Expected: all PASS

- [x] **Step 5: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py \
        tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/test_VariantHandling.py
git commit -m "feat: add ordered mixed-content formula items to ConditionByFormula"
```

---

### Task 3: Parser — readVariationPoint and hook

**Files:**
- Modify: `src/armodel/parser/arxml_parser.py`
- Test: `tests/test_armodel/parser/test_arxml_parser_variation_point.py` (new)

- [x] **Step 1: Write the failing tests**

Create `tests/test_armodel/parser/test_arxml_parser_variation_point.py`. First copy the `_snip` helper exactly as a sibling parser test file defines it (e.g. `test_arxml_parser_handlers.py:54`), then:

```python
"""Parser tests for the structural VARIATION-POINT element."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    ConditionByFormula,
    PostBuildVariantCondition,
    VariationPoint,
)

NS = "http://autosar.org/schema/r4.0"


class TestReadVariationPoint:
    def test_read_variation_point_minimal(self, parser):
        element = _snip("<VARIATION-POINT><SHORT-LABEL>VP1</SHORT-LABEL></VARIATION-POINT>")
        vp_element = element.find("{%s}VARIATION-POINT" % NS)

        vp = parser.readVariationPoint(vp_element, VariationPoint())

        assert vp is not None
        assert vp.getShortLabel().getValue() == "VP1"
        assert vp.getSwSyscond() is None
        assert vp.getPostBuildVariantConditions() == []

    def test_read_variation_point_full(self, parser):
        inner = (
            "<VARIATION-POINT>"
            "<SHORT-LABEL>VP_Turbo</SHORT-LABEL>"
            "<SW-SYSCOND BINDING-TIME=\"CODE-GENERATION-TIME\">"
            "defined(<SYSC-REF DEST=\"SW-SYSTEMCONST\">/Demo/SystemConstants/SY_TURBO</SYSC-REF>)"
            " &amp;&amp; <SYSC-STRING-REF DEST=\"SW-SYSTEMCONST\">/Demo/SystemConstants/SY_MODE</SYSC-STRING-REF> == 0"
            "</SW-SYSCOND>"
            "<POST-BUILD-VARIANT-CONDITIONS>"
            "<POST-BUILD-VARIANT-CONDITION>"
            "<MATCHING-CRITERION-REF DEST=\"POST-BUILD-VARIANT-CRITERION\">/Demo/Criterions/Country</MATCHING-CRITERION-REF>"
            "<VALUE>1</VALUE>"
            "</POST-BUILD-VARIANT-CONDITION>"
            "</POST-BUILD-VARIANT-CONDITIONS>"
            "</VARIATION-POINT>"
        )
        vp_element = _snip(inner).find("{%s}VARIATION-POINT" % NS)

        vp = parser.readVariationPoint(vp_element, VariationPoint())

        sw_syscond = vp.getSwSyscond()
        assert isinstance(sw_syscond, ConditionByFormula)
        assert sw_syscond.getBindingTime().getValue() == "codeGenerationTime"
        items = sw_syscond.getFormulaItems()
        assert items[0] == "defined("
        assert items[1][0] == "SYSC-REF"
        assert items[1][1].getValue() == "/Demo/SystemConstants/SY_TURBO"
        assert items[1][1].getDest() == "SW-SYSTEMCONST"
        assert items[2] == ") && "
        assert items[3][0] == "SYSC-STRING-REF"
        assert items[3][1].getValue() == "/Demo/SystemConstants/SY_MODE"
        assert items[4] == " == 0"

        conditions = vp.getPostBuildVariantConditions()
        assert len(conditions) == 1
        assert isinstance(conditions[0], PostBuildVariantCondition)
        assert conditions[0].getMatchingCriterionRef().getValue() == "/Demo/Criterions/Country"
        assert conditions[0].getMatchingCriterionRef().getDest() == "POST-BUILD-VARIANT-CRITERION"
        assert conditions[0].getValue().getValue() == 1

    def test_read_identifiable_picks_up_variation_point(self, parser):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import PostBuildVariantCriterion

        inner = (
            "<POST-BUILD-VARIANT-CRITERION>"
            "<SHORT-NAME>Country</SHORT-NAME>"
            "<COMPU-METHOD-REF DEST=\"COMPU-METHOD\">/Demo/CompuMethods/CountryEnum</COMPU-METHOD-REF>"
            "<VARIATION-POINT><SHORT-LABEL>VP_Country</SHORT-LABEL></VARIATION-POINT>"
            "</POST-BUILD-VARIANT-CRITERION>"
        )
        element = _snip(inner).find("{%s}POST-BUILD-VARIANT-CRITERION" % NS)

        criterion = PostBuildVariantCriterion(ARPackage(None, "Pkg"), "Country")
        parser.readIdentifiable(element, criterion)

        vp = criterion.getVariationPoint()
        assert vp is not None
        assert vp.getShortLabel().getValue() == "VP_Country"
```

(`_snip` and the `parser` fixture come from `tests/test_armodel/parser/conftest.py` / `_helpers.py`; mirror exactly what a sibling test file does.)

- [x] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_variation_point.py -v`
Expected: FAIL with `AttributeError: 'ARXMLParser' object has no attribute 'readVariationPoint'`

- [x] **Step 3: Write the implementation**

3a. In `src/armodel/parser/arxml_parser.py`, extend the `VariantHandling` import at line 213:

```python
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    ConditionByFormula,
    PostBuildVariantCondition,
    PostBuildVariantCriterion,
    PredefinedVariant,
    SwSystemconstantValueSet,
    SwSystemconstValue,
    VariationPoint,
)
```

Add imports (near the existing `Enumerations`/`PrimitiveTypes` parser imports; `RefType` is already imported at line 211):

```python
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import BindingTimeEnum
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator.BlueprintGenerator import BlueprintGenerator
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import VerbatimString
```

Add a module-level constant after the import block:

```python
#: Mapping between BindingTimeEnum camelCase values and their XML attribute tokens
#: (AR:BINDING-TIME-ENUM--SIMPLE).
BINDING_TIME_XML_MAP = {
    "codeGenerationTime": "CODE-GENERATION-TIME",
    "linkTime": "LINK-TIME",
    "preCompileTime": "PRE-COMPILE-TIME",
    "systemDesignTime": "SYSTEM-DESIGN-TIME",
}
```

3b. Add reader methods in `arxml_parser.py` right after `getSdg` (after line 684, before `readAdminDataSdgs`):

```python
    def readBlueprintGenerator(self, element: ET.Element, generator: BlueprintGenerator) -> BlueprintGenerator:
        self.readARObjectAttributes(element, generator)
        generator.setIntroduction(self.getDocumentationBlock(element, "INTRODUCTION"))
        expression_element = self.find(element, "EXPRESSION")
        if expression_element is not None:
            generator.setExpression(VerbatimString().setValue(expression_element.text))
        return generator

    def readConditionByFormula(self, element: ET.Element, condition: ConditionByFormula) -> ConditionByFormula:
        self.readARObjectAttributes(element, condition)
        if "BINDING-TIME" in element.attrib:
            binding_time = None
            for camel, token in BINDING_TIME_XML_MAP.items():
                if token == element.attrib["BINDING-TIME"]:
                    binding_time = camel
                    break
            if binding_time is not None:
                condition.setBindingTime(BindingTimeEnum().setValue(binding_time))
            else:
                self.notImplemented("Unsupported BINDING-TIME <%s>" % element.attrib["BINDING-TIME"])
        if element.text is not None:
            condition.addFormulaText(element.text)
        for child_element in element:
            tag_name = self.getTagName(child_element)
            if tag_name in ("SYSC-REF", "SYSC-STRING-REF"):
                ref = RefType()
                if "DEST" in child_element.attrib:
                    ref.setDest(child_element.attrib["DEST"])
                ref.setValue(child_element.text)
                condition.addFormulaRef(ref, tag=tag_name)
                if child_element.tail is not None:
                    condition.addFormulaText(child_element.tail)
            else:
                self.notImplemented("Unsupported SW-SYSCOND content <%s>" % tag_name)
        return condition

    def readPostBuildVariantCondition(self, element: ET.Element, condition: PostBuildVariantCondition) -> PostBuildVariantCondition:
        self.readARObjectAttributes(element, condition)
        condition.setMatchingCriterionRef(self.getChildElementRefType("", element, "MATCHING-CRITERION-REF"))
        condition.setValue(self.getChildElementOptionalIntegerValue(element, "VALUE"))
        return condition

    def readVariationPoint(self, element: ET.Element, variation_point: VariationPoint) -> VariationPoint:
        self.readARObjectAttributes(element, variation_point)
        variation_point.setShortLabel(self.getChildElementOptionalIdentifier(element, "SHORT-LABEL"))
        variation_point.setDesc(self.getMultiLanguageOverviewParagraph(element, "DESC"))
        variation_point.setBlueprintCondition(self.getDocumentationBlock(element, "BLUEPRINT-CONDITION"))
        # FORMAL-BLUEPRINT-CONDITION is obsolete (atp.Status="obsolete") and has no
        # model attribute — deliberately not read.
        formal_element = self.find(element, "FORMAL-BLUEPRINT-GENERATOR")
        if formal_element is not None:
            variation_point.setFormalBlueprintGenerator(self.readBlueprintGenerator(formal_element, BlueprintGenerator()))
        sw_syscond_element = self.find(element, "SW-SYSCOND")
        if sw_syscond_element is not None:
            variation_point.setSwSyscond(self.readConditionByFormula(sw_syscond_element, ConditionByFormula()))
        for child_element in self.findall(element, "POST-BUILD-VARIANT-CONDITIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "POST-BUILD-VARIANT-CONDITION":
                variation_point.addPostBuildVariantCondition(
                    self.readPostBuildVariantCondition(child_element, PostBuildVariantCondition()))
            else:
                self.notImplemented("Unsupported POST-BUILD-VARIANT-CONDITIONS content <%s>" % tag_name)
        sdg_element = self.find(element, "SDG")
        if sdg_element is not None:
            variation_point.setSdg(self.getSdg(sdg_element))
        return variation_point
```

3c. Hook into `readIdentifiable` (`arxml_parser.py:766`) — append after the `setAdminData` line (line 776):

```python
        variation_point_element = self.find(element, "VARIATION-POINT")
        if variation_point_element is not None:
            identifiable.setVariationPoint(self.readVariationPoint(variation_point_element, VariationPoint()))
```

- [x] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_variation_point.py -v`
Expected: all PASS

- [x] **Step 5: Run the whole parser test suite (regression)**

Run: `pytest tests/test_armodel/parser/ -x -q`
Expected: all PASS (readIdentifiable is a hot path; this catches accidental double-parse issues)

- [x] **Step 6: Commit**

```bash
git add src/armodel/parser/arxml_parser.py tests/test_armodel/parser/test_arxml_parser_variation_point.py
git commit -m "feat: parse structural VARIATION-POINT in readIdentifiable"
```

---

### Task 4: Writer — writeVariationPoint and hook

**Files:**
- Modify: `src/armodel/writer/arxml_writer.py`
- Test: `tests/test_armodel/writer/test_writer_variation_point.py` (new)

- [x] **Step 1: Write the failing test**

Create `tests/test_armodel/writer/test_writer_variation_point.py`:

```python
"""Writer tests for the structural VARIATION-POINT element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator.BlueprintGenerator import (
    BlueprintGenerator,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import (
    BindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Integer,
    RefType,
    VerbatimString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    ConditionByFormula,
    PostBuildVariantCondition,
    PostBuildVariantCriterion,
    VariationPoint,
)
from armodel.writer.arxml_writer import ARXMLWriter


def _write_vp_to_element(vp: VariationPoint) -> ET.Element:
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    writer = ARXMLWriter()
    element = ET.Element("PARENT")
    writer.writeVariationPoint(element, vp)
    return element


class TestWriteVariationPoint:
    def test_write_minimal(self):
        vp = VariationPoint()
        vp.setShortLabel(Identifier().setValue("VP1"))

        element = _write_vp_to_element(vp)

        vp_element = element.find("VARIATION-POINT")
        assert vp_element is not None
        assert vp_element.find("SHORT-LABEL").text == "VP1"

    def test_write_full_roundtrip_content(self):
        vp = VariationPoint()
        vp.setShortLabel(Identifier().setValue("VP_Turbo"))

        syscond = ConditionByFormula()
        syscond.setBindingTime(BindingTimeEnum().setValue("codeGenerationTime"))
        syscond.addFormulaText("defined(")
        syscond.addFormulaRef(RefType().setValue("/Demo/SystemConstants/SY_TURBO").setDest("SW-SYSTEMCONST"))
        syscond.addFormulaText(")")
        vp.setSwSyscond(syscond)

        condition = PostBuildVariantCondition()
        condition.setMatchingCriterionRef(RefType().setValue("/Demo/Criterions/Country").setDest("POST-BUILD-VARIANT-CRITERION"))
        condition.setValue(Integer().setValue(1))
        vp.addPostBuildVariantCondition(condition)

        generator = BlueprintGenerator()
        generator.setExpression(VerbatimString().setValue("LET Name = \"Example\";"))
        vp.setFormalBlueprintGenerator(generator)

        element = _write_vp_to_element(vp)

        vp_element = element.find("VARIATION-POINT")

        # XSD sequence order: SHORT-LABEL, DESC, BLUEPRINT-CONDITION,
        # FORMAL-BLUEPRINT-GENERATOR, SW-SYSCOND, POST-BUILD-VARIANT-CONDITIONS, SDG
        child_tags = [child.tag for child in vp_element]
        assert child_tags.index("SHORT-LABEL") < child_tags.index("SW-SYSCOND")
        assert child_tags.index("SW-SYSCOND") < child_tags.index("POST-BUILD-VARIANT-CONDITIONS")
        assert child_tags.index("FORMAL-BLUEPRINT-GENERATOR") < child_tags.index("SW-SYSCOND")
        assert vp_element.find("SHORT-LABEL").text == "VP_Turbo"

        syscond_element = vp_element.find("SW-SYSCOND")
        assert syscond_element is not None
        assert syscond_element.attrib["BINDING-TIME"] == "CODE-GENERATION-TIME"
        assert syscond_element.text == "defined("
        refs = syscond_element.findall("SYSC-REF")
        assert len(refs) == 1
        assert refs[0].attrib["DEST"] == "SW-SYSTEMCONST"
        assert refs[0].text == "/Demo/SystemConstants/SY_TURBO"
        assert refs[0].tail == ")"

        conditions_wrapper = vp_element.find("POST-BUILD-VARIANT-CONDITIONS")
        condition_element = conditions_wrapper.find("POST-BUILD-VARIANT-CONDITION")
        ref_element = condition_element.find("MATCHING-CRITERION-REF")
        assert ref_element.text == "/Demo/Criterions/Country"
        assert ref_element.attrib["DEST"] == "POST-BUILD-VARIANT-CRITERION"
        assert condition_element.find("VALUE").text == "1"

        # XSD BLUEPRINT-GENERATOR sequence: INTRODUCTION before EXPRESSION
        formal = vp_element.find("FORMAL-BLUEPRINT-GENERATOR")
        formal_tags = [child.tag for child in formal]
        assert formal_tags == ["EXPRESSION"]
        assert formal.find("EXPRESSION").text == "LET Name = \"Example\";"

    def test_write_none_creates_no_element(self):
        vp = None

        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        writer = ARXMLWriter()
        element = ET.Element("PARENT")
        writer.writeVariationPoint(element, vp)

        assert element.find("VARIATION-POINT") is None

    def test_write_identifiable_emits_variation_point(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")

        criterion = PostBuildVariantCriterion(document, "Country")
        vp = VariationPoint()
        vp.setShortLabel(Identifier().setValue("VP_Country"))
        criterion.setVariationPoint(vp)

        writer = ARXMLWriter()
        element = ET.Element("POST-BUILD-VARIANT-CRITERION")
        writer.writeIdentifiable(element, criterion)

        vp_element = element.find("VARIATION-POINT")
        assert vp_element is not None
        assert vp_element.find("SHORT-LABEL").text == "VP_Country"
```

- [x] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_armodel/writer/test_writer_variation_point.py -v`
Expected: FAIL with `AttributeError: 'ARXMLWriter' object has no attribute 'writeVariationPoint'`

- [x] **Step 3: Write the implementation**

3a. In `src/armodel/writer/arxml_writer.py`, extend/confirm imports:

```python
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator.BlueprintGenerator import BlueprintGenerator
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import BindingTimeEnum
```

(`SwSystemconstValue` from `VariantHandling` is already imported — add `ConditionByFormula`, `PostBuildVariantCondition`, `VariationPoint` to that import. `RefType`, `Integer`, `Identifier`, `VerbatimString` are already imported or trivially added.)

Add the module-level constant after the import block (mirror the parser's):

```python
#: Mapping between BindingTimeEnum camelCase values and their XML attribute tokens
#: (AR:BINDING-TIME-ENUM--SIMPLE).
BINDING_TIME_XML_MAP = {
    "codeGenerationTime": "CODE-GENERATION-TIME",
    "linkTime": "LINK-TIME",
    "preCompileTime": "PRE-COMPILE-TIME",
    "systemDesignTime": "SYSTEM-DESIGN-TIME",
}
```

3b. Add writer methods right after `setSdg` (`arxml_writer.py:653`):

```python
    def writeBlueprintGenerator(self, element: ET.Element, generator: BlueprintGenerator):
        if generator is not None:
            child_element = ET.SubElement(element, "FORMAL-BLUEPRINT-GENERATOR")
            self.writeARObjectAttributes(child_element, generator)
            # XSD sequence: INTRODUCTION (offset 10) before EXPRESSION (offset 20).
            self.writeDocumentationBlock(child_element, "INTRODUCTION", generator.getIntroduction())
            expression = generator.getExpression()
            if expression is not None:
                expression_element = ET.SubElement(child_element, "EXPRESSION")
                expression_element.text = expression.getValue()

    def writeConditionByFormula(self, element: ET.Element, condition: ConditionByFormula):
        if condition is not None:
            child_element = ET.SubElement(element, "SW-SYSCOND")
            self.writeARObjectAttributes(child_element, condition)
            binding_time = condition.getBindingTime()
            if binding_time is not None:
                token = BINDING_TIME_XML_MAP.get(binding_time.getValue())
                if token is None:
                    self.notImplemented("Unsupported BINDING-TIME <%s>" % binding_time.getValue())
                else:
                    child_element.attrib["BINDING-TIME"] = token
            last_ref = None
            for item in condition.getFormulaItems():
                if isinstance(item, str):
                    if last_ref is None:
                        child_element.text = item if child_element.text is None else child_element.text + item
                    else:
                        last_ref.tail = item if last_ref.tail is None else last_ref.tail + item
                else:
                    tag, ref = item
                    last_ref = ET.SubElement(child_element, tag)
                    if ref.getDest() is not None:
                        last_ref.attrib["DEST"] = ref.getDest()
                    last_ref.text = ref.getValue()

    def writePostBuildVariantCondition(self, element: ET.Element, condition: PostBuildVariantCondition):
        child_element = ET.SubElement(element, "POST-BUILD-VARIANT-CONDITION")
        self.writeARObjectAttributes(child_element, condition)
        self.setChildElementOptionalRefType(child_element, "MATCHING-CRITERION-REF", condition.getMatchingCriterionRef())
        self.setChildElementOptionalIntegerValue(child_element, "VALUE", condition.getValue())

    def writeVariationPoint(self, element: ET.Element, variation_point: VariationPoint):
        if variation_point is not None:
            child_element = ET.SubElement(element, "VARIATION-POINT")
            self.writeARObjectAttributes(child_element, variation_point)
            # XSD sequence (AUTOSAR_00046.xsd group AR:VARIATION-POINT, line 99470):
            # SHORT-LABEL, DESC, BLUEPRINT-CONDITION, [FORMAL-BLUEPRINT-CONDITION obsolete],
            # FORMAL-BLUEPRINT-GENERATOR, SW-SYSCOND, POST-BUILD-VARIANT-CONDITIONS, SDG.
            short_label = variation_point.getShortLabel()
            if short_label is not None:
                label_element = ET.SubElement(child_element, "SHORT-LABEL")
                label_element.text = short_label.getValue()
            self.setMultiLanguageOverviewParagraph(child_element, "DESC", variation_point.getDesc())
            self.writeDocumentationBlock(child_element, "BLUEPRINT-CONDITION", variation_point.getBlueprintCondition())
            self.writeBlueprintGenerator(child_element, variation_point.getFormalBlueprintGenerator())
            self.writeConditionByFormula(child_element, variation_point.getSwSyscond())
            conditions = variation_point.getPostBuildVariantConditions()
            if len(conditions) > 0:
                conditions_element = ET.SubElement(child_element, "POST-BUILD-VARIANT-CONDITIONS")
                for condition in conditions:
                    self.writePostBuildVariantCondition(conditions_element, condition)
            self.setSdg(child_element, variation_point.getSdg())
```

Note: `writeBlueprintGenerator` emits its own `FORMAL-BLUEPRINT-GENERATOR` container element (it is only called from `writeVariationPoint` today); do NOT call it as a bare helper.

3c. Hook into `writeIdentifiable` (`arxml_writer.py:838`) — append after the `setAdminData` line (line 844):

```python
        self.writeVariationPoint(element, identifiable.getVariationPoint())
```

- [x] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_armodel/writer/test_writer_variation_point.py -v`
Expected: all PASS

- [x] **Step 5: Run the whole writer test suite (regression)**

Run: `pytest tests/test_armodel/writer/ -x -q`
Expected: all PASS

- [x] **Step 6: Commit**

```bash
git add src/armodel/writer/arxml_writer.py tests/test_armodel/writer/test_writer_variation_point.py
git commit -m "feat: write structural VARIATION-POINT in writeIdentifiable"
```

---

### Task 5: End-to-end parse → write → re-parse round-trip test

**Files:**
- Create: `tests/test_armodel/parser/data/VariationPoint.arxml`
- Test: `tests/test_armodel/parser/test_arxml_parser_variation_point.py` (append class)

- [x] **Step 1: Create the sample ARXML file**

Create `tests/test_armodel/parser/data/VariationPoint.arxml` (schema header mirrors the existing integration files; the parser resolves the `xmlns` automatically):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-2-2.xsd">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>Demo</SHORT-NAME>
      <AR-PACKAGES>
        <AR-PACKAGE>
          <SHORT-NAME>SystemConstants</SHORT-NAME>
          <ELEMENTS>
            <SW-SYSTEMCONST>
              <SHORT-NAME>SY_TURBO</SHORT-NAME>
            </SW-SYSTEMCONST>
          </ELEMENTS>
        </AR-PACKAGE>
        <AR-PACKAGE>
          <SHORT-NAME>Criterions</SHORT-NAME>
          <ELEMENTS>
            <POST-BUILD-VARIANT-CRITERION>
              <SHORT-NAME>Country</SHORT-NAME>
              <VARIATION-POINT>
                <SHORT-LABEL>VP_Country</SHORT-LABEL>
              </VARIATION-POINT>
            </POST-BUILD-VARIANT-CRITERION>
          </ELEMENTS>
        </AR-PACKAGE>
        <AR-PACKAGE>
          <SHORT-NAME>SwComponents</SHORT-NAME>
          <ELEMENTS>
            <APPLICATION-SW-COMPONENT-TYPE>
              <SHORT-NAME>MySWC</SHORT-NAME>
              <INTERNAL-BEHAVIORS>
                <SWC-INTERNAL-BEHAVIOR>
                  <SHORT-NAME>Ib_MySWC</SHORT-NAME>
                  <RUNNABLES>
                    <RUNNABLE-ENTITY>
                      <SHORT-NAME>Run2</SHORT-NAME>
                    </RUNNABLE-ENTITY>
                  </RUNNABLES>
                  <VARIATION-POINT>
                    <SHORT-LABEL>VP1</SHORT-LABEL>
                    <SW-SYSCOND BINDING-TIME="CODE-GENERATION-TIME">defined(<SYSC-REF DEST="SW-SYSTEMCONST">/Demo/SystemConstants/SY_TURBO</SYSC-REF>) &amp;&amp; <SYSC-REF DEST="SW-SYSTEMCONST">/Demo/SystemConstants/SY_TURBO</SYSC-REF> == 0</SW-SYSCOND>
                    <POST-BUILD-VARIANT-CONDITIONS>
                      <POST-BUILD-VARIANT-CONDITION>
                        <MATCHING-CRITERION-REF DEST="POST-BUILD-VARIANT-CRITERION">/Demo/Criterions/Country</MATCHING-CRITERION-REF>
                        <VALUE>1</VALUE>
                      </POST-BUILD-VARIANT-CONDITION>
                    </POST-BUILD-VARIANT-CONDITIONS>
                  </VARIATION-POINT>
                </SWC-INTERNAL-BEHAVIOR>
              </INTERNAL-BEHAVIORS>
            </APPLICATION-SW-COMPONENT-TYPE>
          </ELEMENTS>
        </AR-PACKAGE>
      </AR-PACKAGES>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
```

(Modeled on the spec listing at `AUTOSAR_FO_TPS_GenericStructureTemplate.md:12988-13113`, with the XSD-correct `MATCHING-CRITERION-REF` tag.)

- [x] **Step 2: Write the round-trip test**

Append to `tests/test_armodel/parser/test_arxml_parser_variation_point.py`:

```python
import os

import pytest

from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

VARIATION_POINT_ARXML = os.path.join(os.path.dirname(__file__), "data", "VariationPoint.arxml")


@pytest.mark.integration
class TestVariationPointRoundTrip:
    def test_parse_write_reparse_preserves_variation_point(self, tmp_path):
        AUTOSAR.getInstance().new()
        AUTOSAR.setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        parser = ARXMLParser()
        parser.load(VARIATION_POINT_ARXML, document)

        demo_pkg = document.getARPackageByFullName("Demo")
        swc_pkg = demo_pkg.getARPackageByFullName("Demo/SwComponents")
        swc = swc_pkg.getElements()[0]
        behavior = document.getBehavior(swc)

        vp = behavior.getVariationPoint()
        assert vp is not None
        assert vp.getShortLabel().getValue() == "VP1"
        items = vp.getSwSyscond().getFormulaItems()
        assert items[0] == "defined("
        assert items[1][1].getValue() == "/Demo/SystemConstants/SY_TURBO"
        conditions = vp.getPostBuildVariantConditions()
        assert conditions[0].getMatchingCriterionRef().getValue() == "/Demo/Criterions/Country"

        output = str(tmp_path / "VariationPoint_roundtrip.arxml")
        writer = ARXMLWriter()
        writer.save(output, document)

        AUTOSAR.getInstance().new()
        AUTOSAR.setARRelease("R23-11")
        document2 = AUTOSAR.getInstance()
        parser2 = ARXMLParser()
        parser2.load(output, document2)

        demo_pkg2 = document2.getARPackageByFullName("Demo")
        swc_pkg2 = demo_pkg2.getARPackageByFullName("Demo/SwComponents")
        swc2 = swc_pkg2.getElements()[0]
        behavior2 = document2.getBehavior(swc2)

        vp2 = behavior2.getVariationPoint()
        assert vp2 is not None
        assert vp2.getShortLabel().getValue() == "VP1"
        items2 = vp2.getSwSyscond().getFormulaItems()
        assert items2[0] == items[0]
        assert items2[1][0] == items[1][0]
        assert items2[1][1].getValue() == items[1][1].getValue()
        assert items2[1][1].getDest() == items[1][1].getDest()
        conditions2 = vp2.getPostBuildVariantConditions()
        assert conditions2[0].getMatchingCriterionRef().getValue() == "/Demo/Criterions/Country"
        assert conditions2[0].getValue().getValue() == 1

        # Criterion element's own variation point also survives
        crit_pkg2 = document2.getARPackageByFullName("Demo/Criterions")
        criterion2 = crit_pkg2.getElements()[0]
        assert criterion2.getVariationPoint().getShortLabel().getValue() == "VP_Country"
```

Adjustment note for the implementer: verify the exact navigation API names (`getARPackageByFullName`, `getElements`, `getBehavior`) against `src/armodel/models/M2/AUTOSARTemplates/AutosarTopLevelStructure` before running; if `getARPackageByFullName` does not exist, use whatever navigation pattern `tests/integration_tests/test_roundtrip.py` uses and copy it.

- [x] **Step 3: Run the round-trip test**

Run: `pytest tests/test_armodel/parser/test_arxml_parser_variation_point.py -v -m integration`
Expected: PASS. If the parse step fails on `SW-SYSTEMCONST` or `POST-BUILD-VARIANT-CRITERION` handling, read the error: `POST-BUILD-VARIANT-CRITERION` is already parsed (`arxml_parser.py:8338`); `SW-SYSTEMCONST` support must be verified — if unsupported, drop the `SystemConstants` package from the ARXML file and change the `SYSC-REF` targets to `/Demo/Criterions/Country` refs (the parser does not resolve SYSC-REF targets, so the test remains valid).

- [x] **Step 4: Copy the file into the integration test corpus**

```bash
cp tests/test_armodel/parser/data/VariationPoint.arxml tests/integration_tests/test_files/VariationPoint.arxml
```

Run: `pytest tests/integration_tests/ -q -k VariationPoint`
Expected: PASS (the round-trip harness auto-discovers files in `tests/integration_tests/test_files/`, per `tests/integration_tests/config.yaml` and its README)

- [x] **Step 5: Commit**

```bash
git add tests/test_armodel/parser/data/VariationPoint.arxml \
        tests/test_armodel/parser/test_arxml_parser_variation_point.py \
        tests/integration_tests/test_files/VariationPoint.arxml
git commit -m "test: add VARIATION-POINT round-trip coverage"
```

---

### Task 6: Parity checklist updates, full validation

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py`
- Modify: `src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintGenerator/BlueprintGenerator.py`

- [x] **Step 1: Update parity checklists**

In `VariantHandling/__init__.py`:

`VariationPoint` checklist — mark reader columns `[x]` for the setters used by the parser (`setBlueprintCondition`, `setDesc`, `setFormalBlueprintGenerator`, `addPostBuildVariantCondition`, `setSdg`, `setShortLabel`, `setSwSyscond`) and writer columns `[x]` for the getters used by the writer (`getBlueprintCondition`, `getDesc`, `getFormalBlueprintGenerator`, `getPostBuildVariantConditions`, `getSdg`, `getShortLabel`, `getSwSyscond`). Concretely change the block at lines ~471-488 so every row reads:

```python
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBlueprintCondition             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBlueprintCondition             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDesc                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDesc                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFormalBlueprintGenerator       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFormalBlueprintGenerator       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPostBuildVariantConditions     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addPostBuildVariantCondition      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getSdg                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSdg                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getShortLabel                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setShortLabel                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwSyscond                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwSyscond                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
```

(`addPostBuildVariantCondition` gets both `[x] reader` and `[x] writer` — the writer iterates the collection via the getter; the parser appends via the adder.)

`ConditionByFormula` checklist (updated in Task 2) — flip `getBindingTime` writer, `setBindingTime` reader, and all three formula-item rows to `[x] reader [x] writer`:

```python
    # [x] getBindingTime    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBindingTime    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFormulaItems   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addFormulaText    [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] addFormulaRef     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
```

`PostBuildVariantCondition` checklist (~lines 332-339) — flip reader/writer columns:

```python
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getMatchingCriterionRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMatchingCriterionRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getValue                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValue                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
```

In `BlueprintGenerator.py` — mark reader column `[x]` for `setExpression`/`setIntroduction` and writer column `[x]` for `getExpression`/`getIntroduction`.

- [x] **Step 2: Run the full test suite**

Run: `python scripts/run_tests.py`
Expected: all PASS, no regressions from the `readIdentifiable`/`writeIdentifiable` hooks

- [x] **Step 3: Run lint and format checks**

Run: `npm run flake8 && npm run black-check`
Expected: PASS. If black fails, run `npm run black` on the touched files only, re-run tests, then proceed.

- [x] **Step 4: Commit**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py \
        src/armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintGenerator/BlueprintGenerator.py
git commit -m "docs: update variation point parity checklists after reader/writer sync"
```

---

## Self-Review Checklist (done)

- **XSD coverage (AUTOSAR_00046.xsd):** SHORT-LABEL ✓ DESC ✓ BLUEPRINT-CONDITION ✓ FORMAL-BLUEPRINT-CONDITION (obsolete — skipped, documented) ✓ FORMAL-BLUEPRINT-GENERATOR ✓ SW-SYSCOND (bindingTime + SYSC-REF + SYSC-STRING-REF mixed content) ✓ POST-BUILD-VARIANT-CONDITIONS/MATCHING-CRITERION-REF/VALUE ✓ SDG ✓. Writer child order = XSD sequence offsets 10→50 ✓. BLUEPRINT-GENERATOR order INTRODUCTION→EXPRESSION ✓.
- **Out of scope and stated:** reference pattern (`*-REF-CONDITIONAL`), property set pattern (`*-VARIANTS`), attribute value pattern (VALUE attributes/formulas, `ATTRIBUTE-VALUE-VARIATION-POINT` attributeGroup).
- **Placeholders:** none — every step carries full code.
- **Type consistency:** `getFormulaItems/addFormulaText/addFormulaRef(tag)` with `(tag, RefType)` tuples (Task 2) match parser (Task 3) and writer (Task 4). `readVariationPoint`/`writeVariationPoint` names match the tests. `BINDING_TIME_XML_MAP` defined identically in parser and writer. `MATCHING-CRITERION-REF` used consistently in parser, writer, tests, and sample ARXML.
- **Risks flagged inline:** circular import handled via `TYPE_CHECKING`; enum token mapping explicit; VALUE treated as plain Integer per `SwSystemconstValue` precedent (xsd:7022); `SW-SYSTEMCONST` parse support to be verified in Task 5 Step 3 with documented fallback.
