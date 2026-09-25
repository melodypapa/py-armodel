# Design: Support for `<<atpMixedString>>` (Phase 1 — pure-text shape)

Date: 2026-09-24
Status: approved design (sections confirmed in conversation); §3/§6 revised and §9 added 2026-09-25 (interface-level mixin redesign, user-approved)

## 1. Background

The AUTOSAR standard defines the `<<atpMixedString>>` stereotype
([TPS_GST_00025], AUTOSAR_FO_TPS_GenericStructureTemplate, section 2.3.1):
*a mixed content model with intermixed text, applied to metaclasses only*.
Per [TPS_XMLSPR_00047] (XMLSchemaProductionRules 3.2.4.2) the XML form maps
properties to elements in arbitrary order without wrappers, and *the XML
elements may have text in-between*.

The R23-11 corpus contains **42** stereotyped classes in three families:

| Family | Count | Shape |
|---|---|---|
| Variation Point | 11 | pure text (empty element group; value = element text) |
| Formula | 14 | pure text |
| Documentation | 17 | true mixed content (text interleaved with child elements) |

py-armodel today has 4 classes with ad-hoc, duplicated implementations
(`AttributeValueVariationPoint`, `ConditionByFormula`, `TimingConditionFormula`,
`TDEventOccurrenceExpressionFormula`), each carrying its own
`_text` / `getText()` / `setText()`. Three inconsistent styles exist across src
(those 4; `ARType.getText`; `TraceableText` via `DocumentationBlock`).

## 2. Scope

Two-phase delivery, approved by user:

- **Phase 1 (this design)**: a shared mixin base class unifying the pure-text
  shape (25 classes: VP + Formula families), plus reader/writer helpers.
- **Phase 2 (separate project)**: true mixed content (17 Documentation classes)
  needs an order-preserving text/child-element segment model; out of scope here.

Rejected alternatives: (B) convention doc only — perpetuates duplication;
(C) one segment model for all shapes — over-engineered for formulas (YAGNI),
large rework of stamped Documentation classes.

## 3. Base class API

File: `src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/StereotypeMixins.py`
(interface-level mixin module shared with `VariationPointCapable`; see §9 for the
2026-09-25 redesign that moved it here from the same-named sibling module).

```python
from abc import ABC
from typing import Optional


class AtpMixedString(ABC):
    """
    This is a mixed content model with intermixed text. This is applied to metaclasses only.
    """

    # AtpMixedString — interface-level mixin for the <<atpMixedString>> stereotype.
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.md, [TPS_GST_00025], section 2.3.1 (R23-11)
    # Serialization: R23-11/AUTOSAR_FO_TPS_XMLSchemaProductionRules.md, [TPS_XMLSPR_00047], section 3.2.4.2 (R23-11)
    # No spec table: stereotype-inherent accessors have no attribute rows ("no spec row" convention).
    # Columns: impl / docstring / test   ([—] = no spec row)
    # [x] getMixedString    [x] impl  [x] docstring  [x] test
    # [x] setMixedString    [x] impl  [x] docstring  [x] test

    # Class-level default — the ONLY initialization. The repo's Referrable.__init__
    # calls ARObject.__init__ directly (bypassing super()), so a mixin __init__ may
    # never run under combined inheritance (e.g. TimingConditionFormula). The mixin
    # therefore has no __init__ at all; reads fall back to this class attribute
    # until setMixedString assigns the instance attribute. Do not remove it.
    mixedString: Optional[str] = None

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

Decisions (as revised by the §9 redesign):

- **Interface-level mixin**, exact `VariationPointCapable` parity: derives from
  `ABC` only — **not** from `ARObject` — so it never occupies a heritage slot and
  owns no constructor. Consumers anchor their own spec `Base`
  (`class X(PrimaryDomainBase, AtpMixedString)`; where the spec Base is
  `ARObject` itself, name it explicitly:
  `ConditionByFormula(ARObject, AtpMixedString)`,
  `AttributeValueVariationPoint(ARObject, AtpMixedString, ABC)`).
- No `__init__` and no instantiation guard (VariationPointCapable precedent —
  the stateless interface is instantiable but harmless).
- The module imports nothing at runtime except `abc`/`typing` — same
  cycle-safety property the VariationPointCapable plan documents
  (`VariantHandling/__init__.py` imports `ARPackage.py` at runtime).
- Field/accessor named after the stereotype (`mixedString`,
  `getMixedString`/`setMixedString`) — self-documenting. This was a **breaking
  rename** vs the 4 pre-existing classes (`_text`/`getText`/`setText`); their
  tests were updated in the same pass (batch 1, landed).
- `setMixedString(None)` is a no-op; setter returns `self` (chaining).
- Whitespace is preserved verbatim — no strip/normalize (the FormulaExpression
  grammar operates on post-XML-parse text, per GenericStructureTemplate).
- Class docstring quotes [TPS_GST_00025] verbatim.
- Export: via `from .StereotypeMixins import *` in
  `GeneralTemplateClasses/__init__.py`.

## 4. Parser/writer conventions

Helper pair in the established `readXxx(element, obj)` / `writeXxx(element, obj)`
fill style:

```python
# arxml_parser.py
def readMixedStringText(self, element, obj):
    """<<atpMixedString>>: the element text is the value (pure-text shape).
    Whitespace is preserved verbatim."""
    if element.text is not None and obj is not None:
        obj.setMixedString(element.text)

# arxml_writer.py
def writeMixedStringText(self, element, obj):
    """<<atpMixedString>>: write getMixedString() as element text; None omits the text node."""
    if obj is not None:
        element.text = obj.getMixedString()
```

- Call sites: one line per class — reader calls it after formal attributes,
  writer before/after child-element writers (pure-text classes have no child
  elements, so no ordering concern). `element.text = None` yields an empty
  element.
- Phase 2 classes (true mixed content) must NOT use this helper — segment-aware
  reading (`element.text` + child `tail`s) will be designed separately.

## 5. Migration (extend pass on 4 existing classes)

`AttributeValueVariationPoint` (abstract), `ConditionByFormula`,
`TimingConditionFormula`, `TDEventOccurrenceExpressionFormula`:

1. Insert `AtpMixedString` into their base list.
2. Delete the private `_text` field and `getText`/`setText` (use the base API).
3. Rename direct field accesses `_text` → `mixedString` (rare; parser/writer go
   through accessors).
4. Update model/parser/writer tests at `getText|setText|_text` call sites; add
   one `isinstance(obj, AtpMixedString)` assertion per class.
5. Class checklists: keep the accessor rows, retitle to
   `getMixedString/setMixedString (no spec row — stereotype-inherent, provided
   by AtpMixedString)`.

## 6. Rollout queue (dependency-first)

| Order | Batch | Classes | Notes | Status |
|---|---|---|---|---|
| 0 | Prerequisite | `AtpMixedString` (base itself) | support class, spec-cited, lands first | **done** (PR #785; redesigned 2026-09-25, §9) |
| 1 | Migration | 4 existing classes (section 5) | extend pass + test rename | **done** (PR #785) |
| 2 | VP family | `AbstractEnumerationValueVariationPoint`, `AbstractNumericalVariationPoint` (abstract first) → `BooleanValueVariationPoint`, `FloatValueVariationPoint`, `IntegerValueVariationPoint`, `LimitValueVariationPoint`, `NumericalValueVariationPoint`, `PositiveIntegerValueVariationPoint`, `TimeValueValueVariationPoint`, `UnlimitedIntegerValueVariationPoint` | concrete classes inherit the mixin via the AVP chain | **done** (Group8 syncs, 2026-09-24; 9b stamp verdicts pending) |
| 3 | Formula family | `FormulaExpression` → `BlueprintFormula`, `CompuGenericMath`, `EcucConditionFormula`, `EcucParameterDerivationFormula`, `EcucQueryExpression`, `SwSystemconstDependentFormula`, `FMConditionByFeaturesAndAttributes`, `FMConditionByFeaturesAndSwSystemconsts`, `FMFormulaByFeaturesAndAttributes`, `FMFormulaByFeaturesAndSwSystemconsts` | FM* 4 classes run the closure check at Step 1 (FeatureDef etc. member types may be missing; resolve per Rule 0016) | pending — queue rows live in the Group todo files (Group8/Group9/Group3/Group19) |

- Classes already in src but unstamped go through the normal 9-step pass
  ("exists is not a stamp", Rule 0016.5).
- Queue rows are appended to the owning group todo files (per Rule 0007 package
  location) with the 9-step sub-checklists.
- The 17 Documentation classes are NOT queued in this phase (Phase 2 project).

## 7. Testing

- Base class unit test
  `tests/test_armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/test_AtpMixedString.py`:
  abstract guard, default `None`, set/get round-trip, `None` no-op, setter
  chaining.
- Migration regression: the 4 classes' existing model/parser/writer tests pass
  after the accessor rename; new isinstance assertions.
- Round-trip assertion: text with newlines/leading whitespace survives
  parse → write → re-parse unchanged (no normalization).
- Full gates per class/step: `npm run lint`, `npm run black-check`,
  `python scripts/run_tests.py` (9a gate).

## 8. Risks

- Breaking rename touches the 4 classes' tests — bounded (4 × 3 test files),
  verified by the full suite.
- Some queue classes may pull missing member types (FM* family) — resolved
  interactively at Step 1 per Rule 0016, may extend the queue.

## 9. Redesign (2026-09-25): interface-level mixin, unified `StereotypeMixins` module

Status: approved design (user-confirmed, revises §3 and the §5/§6 mechanics).

Two changes, decided together:

1. **`AtpMixedString` becomes a true interface-level mixin** — exact
   `VariationPointCapable` parity (`docs/superpowers/plans/2026-09-03-variation-point-capable-mixin.md`,
   Task 4): derives from `ABC` only, **no `ARObject` base, no `__init__`, no
   instantiation guard**. Rationale: `<<atpMixedString>>` applies to
   *metaclasses* ([TPS_GST_00025]) — it is not a metaclass of its own — so the
   model-side helper must not occupy a heritage slot, own state, or sit in the
   consumers' MRO as a real base class. The class-level default
   `mixedString: Optional[str] = None` becomes the **only** initialization
   (the Rule 0021 MRO-bypass trap: `Referrable.__init__` calls
   `ARObject.__init__` directly, so instance init must never depend on the
   mixin's ctor — with no ctor at all, reads simply fall back to the class
   attribute until `setMixedString` assigns the instance attribute).
   Consumers that previously received `ARObject` *through* the mixin must
   anchor their spec `Base` explicitly:
   `ConditionByFormula(ARObject, AtpMixedString)` (Table 7.5 Base),
   `AttributeValueVariationPoint(ARObject, AtpMixedString, ABC)` (Table 7.2
   Base). `TimingConditionFormula(Referrable, AtpMixedString)` and
   `TDEventOccurrenceExpressionFormula(Referrable, AtpMixedString)` are
   unchanged (the `Referrable` chain anchors `ARObject`).
2. **Both stereotype mixins are physically unified** into one module:
   `GeneralTemplateClasses/StereotypeMixins.py` (user decision 2026-09-25).
   `VariationPointCapable` moves verbatim (zero behavior change);
   `AtpMixedString` lands in its redesigned interface-level form. The old
   same-named sibling modules are deleted and every import site updated
   (~116 files: 80 src + 22 test for `VariationPointCapable`, 8 src + 6 test
   for `AtpMixedString`, the star-export lines in
   `GeneralTemplateClasses/__init__.py` + `models/__init__.py`, and the
   parser/writer import lines). The unified module imports nothing at runtime
   except `abc`/`typing` — the dropping of `ARObject` is what makes this
   cycle-safe, satisfying the VariationPointCapable plan's documented
   constraint (`VariantHandling/__init__.py` imports `ARPackage.py` at
   runtime).

Consequences for the sync workflow (Rule 0021 mirrors both):

- Consumer checklists keep the annotation line
  `# getMixedString / setMixedString provided by the AtpMixedString base (mixin) — no spec row (stereotype-inherent)`.
- The base-order rule is unchanged in spirit: mixin **after** the
  ARObject-anchored primary base, `ABC` last.
- Out of scope (unchanged): batch 3 Formula-family migrations follow the new
  shape when their queue rows sync; the Phase-2 Documentation family never
  consumes this mixin; the writer call-site inlining / parser strip-guard
  drift noted in the 2026-09-24 implementation review is a separate cleanup.
