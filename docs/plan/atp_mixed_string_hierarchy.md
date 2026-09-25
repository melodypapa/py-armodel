# `<<atpMixedString>>` class hierarchy — reference

Status date: 2026-09-25 · Corpus: R23-11 (CP_TPS + FO_TPS markdown; XSD `AUTOSAR_00052.xsd`)
Scope: all 42 classes the R23-11 corpus stereotypes `<<atpMixedString>>`, their spec
`Base` rows, the correct Python parent under the repo's two standing rules, and the
current sync state. Use this as the map for fixing wrong parents (Rule 0001.2) and for
queueing the missing classes.

## Design rules (decided 2026-09-25)

1. **`AtpMixedString` is an interface-level mixin — `AtpMixedString(ABC)` — NOT a
   metamodel class.** Evidence: 0 spec Base rows in the whole R23-11 corpus ever list
   `AtpMixedString`; the XSD applies the stereotype to 83 constructs spread over ≥4
   unrelated hierarchies. It is a *capability* ("has mixed text content"), not a
   taxonomy ("is-a"). Rejected alternative: `AtpMixedString(ARObject)` as parent of
   `FormulaExpression` — breaks down on `EcucQueryExpression` (Base = plain `ARObject`,
   not in the Formula family): it would force a fabricated taxonomy edge or leave the
   capability unexpressed. (This was tried and reverted same day.)
2. **Direct parent = most-derived class from the spec `Base` row** (Rule 0001.2). A
   Base row like `ARObject , FormulaExpression , SwSystemconstDependentFormula` is a
   derivation SET — anchor only the most-derived class; the ancestors arrive
   transitively. Never list `AtpMixedString` on a class whose chain already provides
   it.
3. **Mixin mechanics:** `AtpMixedString` has no `__init__`; a class-level
   `mixedString = None` default is the fallback for classes whose `__init__` chain
   bypasses it (`Referrable.__init__` calls `ARObject.__init__` directly — e.g.
   `TimingConditionFormula(Referrable, AtpMixedString)`). Accessors
   `getMixedString`/`setMixedString` have no spec rows (stereotype-inherent).
4. **Serialization:** the mixed text is the element's text content
   (`[TPS_XMLSPR_00047]` §3.2.4.2); reader `readMixedStringText` → `setMixedString`,
   writer `writeMixedStringText` ← `getMixedString`.

## The mixin and the FormulaExpression family (Python chains)

```
AtpMixedString(ABC)                                   ← capability mixin, no ARObject base
│
├─ FormulaExpression(ARObject, AtpMixedString, ABC)   ← abstract, FormulaLanguage
│  │   spec Base: ARObject · FMXF "Table C.5" (pp.73-74, caption-after-content) — STAMPED R23-11
│  │
│  └─ SwSystemconstDependentFormula(FormulaExpression, ABC)   ← abstract, VariantHandling
│     │   spec Base: ARObject , FormulaExpression · GST Table 7.10, p.240 — STAMPED R23-11
│     │
│     ├─ ConditionByFormula(SwSystemconstDependentFormula)    ← concrete, VariantHandling
│     │     spec Base: ARObject , FE , SSCDF · GST Table 7.5, p.231 — Steps 1-8 done, Step 9 re-run pending
│     │
│     ├─ AttributeValueVariationPoint(SwSystemconstDependentFormula, ABC)  ← abstract
│     │     spec Base: ARObject , FE , SSCDF · GST Table 7.2 — STAMPED (re-parent applied 2026-09-25; formal 9b verbatim re-diff owed)
│     │
│     ├─ BlueprintFormula(SwSystemconstDependentFormula)      ← NOT YET IN SRC (queued Group8)
│     │     spec Base: ARObject , FE , SSCDF
│     │
│     ├─ FMFormulaByFeaturesAndSwSystemconsts(SwSystemconstDependentFormula)   ← NOT IN SRC (queued)
│     ├─ FMConditionByFeaturesAndSwSystemconsts(SwSystemconstDependentFormula) ← NOT IN SRC (queued)
│     └─ (FMConditionByFeaturesAndAttributes / FMFormulaByFeaturesAndAttributes —
│        FMXF Table 7.1-7.4 blocks are caption-shifted; resolve exact chain at their Step 1)
│
├─ CompuGenericMath(FormulaExpression)                ← WRONG TODAY: (ARObject)
│     spec Base: ARObject , FormulaExpression · CP SWCT — fix pending
├─ EcucConditionFormula(FormulaExpression)            ← WRONG TODAY: (ARObject)
│     spec Base: ARObject , FormulaExpression · CP ECUC — fix pending
├─ EcucParameterDerivationFormula(FormulaExpression)  ← WRONG TODAY: (ARObject)
│     spec Base: ARObject , FormulaExpression · CP ECUC — fix pending
├─ TimingConditionFormula(FormulaExpression)          ← WRONG TODAY: (Referrable, AtpMixedString)
│     spec Base: ARObject , FormulaExpression · CP TimingExtensions Table 3.8, p.35
│     XSD complexType (00052 L123490): AR-OBJECT + FORMULA-EXPRESSION groups only —
│     NO SHORT-NAME; dropping Referrable removes parent/short_name (no fixture fallout)
├─ TDEventOccurrenceExpressionFormula(FormulaExpression)  ← WRONG TODAY: (Referrable, AtpMixedString)
│     spec Base: ARObject , FormulaExpression · CP TimingExtensions Table 3.51
└─ SingleLanguageUnitNames(FormulaExpression)         ← WRONG TODAY: (ARLiteral)
      spec Base: ARObject , FormulaExpression · CP SWCT — fix pending
```

## The non-Formula stereotyped classes

These carry the stereotype directly on a `Base: ARObject` class — they list the mixin
themselves (`(ARObject, AtpMixedString, ...)`), there is no stereotyped ancestor to
inherit from.

```
AtpMixedString(ABC)
├─ EcucQueryExpression(ARObject, AtpMixedString)          ← TODAY: (ARObject); mixin pending sync
│     spec Base: ARObject · CP ECUC Table 2.40 (XSD: group only, no own complexType)
├─ EmphasisText(ARObject, AtpMixedString)                 ← TODAY: (ARObject)
│     spec Base: ARObject · MSR DataDictionary (InlineTextElements)
├─ IndexEntry(ARObject, AtpMixedString)                   ← TODAY: (ARObject)
│     spec Base: ARObject · MSR DataDictionary (InlineTextElements)
└─ MixedContentFor*(ARObject, AtpMixedString, ABC)        ← doc-model abstract bases
   │    spec Base: ARObject (all MixedContentFor* variants)
   ├─ MixedContentForLongName       — IN SRC (ARObject, ABC); mixin pending
   ├─ MixedContentForParagraph      — IN SRC (ARObject, ABC); mixin pending
   ├─ MixedContentForOverviewParagraph — NOT IN SRC
   ├─ MixedContentForPlainText         — NOT IN SRC
   ├─ MixedContentForVerbatim          — NOT IN SRC
   └─ MixedContentForUnitNames         — NOT IN SRC
```

Plain (non-stereotyped) doc-model bases for orientation: `LanguageSpecific(ARObject)`
(abstract), `WhitespaceControlled(ARObject)` (abstract) — they appear in doc-class Base
rows but carry no `<<atpMixedString>>` stereotype themselves.

### Documentation text model (chains via MixedContentFor*)

| Class | spec Base row | src today | state |
|---|---|---|---|
| `LLongName` | ARObject, LanguageSpecific, MixedContentForLongName | `(MixedContentForLongName, LanguageSpecific)` | ✔ chain correct |
| `SingleLanguageLongName` | ARObject, MixedContentForLongName | `(MixedContentForLongName)` | ✔ chain correct |
| `LParagraph` | (via MixedContentForParagraph) | `(MixedContentForParagraph, LanguageSpecific)` | ✔ chain correct |
| `SlParagraph` | ARObject, MixedContentForParagraph | `(MixedContentForParagraph, LanguageSpecific)` | ✔ chain correct |
| `LOverviewParagraph` | ARObject, LanguageSpecific, MixedContentForOverviewParagraph | `(LanguageSpecific)` | ⚠ missing MixedContentForOverviewParagraph base |
| `LPlainText` | ARObject, LanguageSpecific, MixedContentForPlainText, WhitespaceControlled | `(LanguageSpecific)` | ⚠ missing 2 bases |
| `LVerbatim` | ARObject, LanguageSpecific, MixedContentForVerbatim, WhitespaceControlled | `(LanguageSpecific)` | ⚠ missing 2 bases |

### AttributeValueVariationPoint concrete subclasses (derivation sets → most-derived = AVP)

`AbstractNumericalVariationPoint`, `NumericalValueVariationPoint`,
`LimitValueVariationPoint`, `BooleanValueVariationPoint`,
`FloatValueVariationPoint`, `IntegerValueVariationPoint`,
`PositiveIntegerValueVariationPoint`, `UnlimitedIntegerValueVariationPoint`,
`TimeValueValueVariationPoint` — all in src, all ✔ (subclass AVP / AbstractNumerical).

`AbstractEnumerationValueVariationPoint` — spec Base
`ARObject , AttributeValueVariationPoint , FE , SSCDF` → parent `AttributeValueVariationPoint`;
NOT IN SRC (queued Group8).

## Findings / action list (priority order)

1. **Wrong parents → re-parent to `FormulaExpression`** (5): `CompuGenericMath`,
   `EcucConditionFormula`, `EcucParameterDerivationFormula`, `TimingConditionFormula`
   (drop `Referrable` — XSD-confirmed no SHORT-NAME; parser `getShortName`/`readReferrable`
   and writer `writeReferrable` go with it), `TDEventOccurrenceExpressionFormula` (same).
2. **Wrong parent → re-base to `ARLiteral`→? / add mixin**: `SingleLanguageUnitNames`
   (spec Base `ARObject , FormulaExpression`, currently `(ARLiteral)` — re-parent to
   FormulaExpression and reconcile the ARLiteral value API at its drift pass).
3. **Add the mixin** (Base = plain ARObject, stereotyped): `EcucQueryExpression`,
   `EmphasisText`, `IndexEntry`, `MixedContentForLongName`, `MixedContentForParagraph`.
4. **Missing doc-model bases** (bigger change set): `MixedContentForOverviewParagraph`,
   `MixedContentForPlainText`, `MixedContentForVerbatim`, `MixedContentForUnitNames`,
   `SlOverviewParagraph`; re-parent `LOverviewParagraph`/`LPlainText`/`LVerbatim`.
5. **Queued (unsynced)**: `BlueprintFormula`, `FMConditionByFeaturesAndAttributes`,
   `FMConditionByFeaturesAndSwSystemconsts`, `FMFormulaByFeaturesAndAttributes`,
   `FMFormulaByFeaturesAndSwSystemconsts`, `AbstractEnumerationValueVariationPoint` —
   their Group8 rows carry the dependency order (parents before dependents).

Every re-parent above follows Rule 0001.2; each touched class needs its checklist/test
revisit (Rule 0012.3 drift pass) and 9b confirmation before its row is stamped.
