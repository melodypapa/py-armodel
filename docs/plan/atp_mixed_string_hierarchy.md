# `<<atpMixedString>>` class hierarchy — reference

Status date: 2026-09-25 · Corpus: R23-11 (CP_TPS + FO_TPS markdown; XSD `AUTOSAR_00052.xsd`)
Scope: all 42 classes the R23-11 corpus stereotypes `<<atpMixedString>>`, their spec
`Base` rows, the correct Python parent under the repo's two standing rules, and the
current sync state. Use this as the map for fixing wrong parents (Rule 0001.2) and for
queueing the missing classes.

> **Verification method:** every Base row below was read from the markdown with the
> `| Class | <<atpMixedString>> <Name> |` header row as the identity anchor (the FMXF
> and appendix tables render captions AFTER their content block — a bare line-number
> grep can pick up a neighboring shifted block; 2026-09-25 this misread briefly
> attributed `ARObject , FormulaExpression` to SingleLanguageUnitNames).

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

## Complete hierarchy — all 42 `<<atpMixedString>>` classes

Legend: ✔ in src, parent correct · ✱ FIXED 2026-09-25 (drift note in checklist) ·
⚙ re-parent/fix pending · ❑ NOT IN SRC (queued) · secondary bases (multiple
inheritance) noted in brackets. Every Base row markdown-verified via the class-header
anchor.

### 1. FormulaExpression family (14)

```
AtpMixedString(ABC)  ← capability mixin (no ARObject base)
│
└─ FormulaExpression(ARObject, AtpMixedString, ABC)  [abstract · FormulaLanguage] ✔ STAMPED
   │   Base: ARObject · FMXF Table C.5, pp.73-74 (caption-after-content)
   │
   ├─ CompuGenericMath  [concrete · DataDefProperties.py] ✱ FIXED (was ARObject)
   │     Base: ARObject , FormulaExpression · CP SWCT Table 5.60
   ├─ EcucConditionFormula  [concrete · ECUCParameterDefTemplate.py] ✱ FIXED (was ARObject)
   │     Base: ARObject , FormulaExpression · CP ECUC Table 2.43
   ├─ EcucParameterDerivationFormula  [concrete · ECUCParameterDefTemplate.py] ✱ FIXED (was ARObject)
   │     Base: ARObject , FormulaExpression · CP ECUC
   ├─ TimingConditionFormula  [concrete · TimingCondition.py] ✱ FIXED (was Referrable, AtpMixedString)
   │     Base: ARObject , FormulaExpression · CP TimingExtensions Table 3.8, p.35
   │     [XSD: no SHORT-NAME — Referrable dropped, parser/writer updated]
   ├─ TDEventOccurrenceExpressionFormula  [concrete · TDEventOccurrenceExpression.py] ✱ FIXED (was Referrable, AtpMixedString)
   │     Base: ARObject , FormulaExpression · CP TimingExtensions Table 3.51
   │
   └─ SwSystemconstDependentFormula(FormulaExpression, ABC)  [abstract · VariantHandling] ✔ STAMPED
      │   Base: ARObject , FormulaExpression · GST Table 7.10, p.240
      │
      ├─ ConditionByFormula(SwSystemconstDependentFormula)  [concrete] ✔ Steps 1-8 done
      │     Base: ARObject , FE , SSCDF · GST Table 7.5, p.231 — Step 9 re-run pending
      ├─ AttributeValueVariationPoint(SwSystemconstDependentFormula, ABC)  [abstract] ✔ STAMPED
      │   Base: ARObject , FE , SSCDF · GST Table 7.2  (see subtree 2 below)
      ├─ BlueprintFormula(SwSystemconstDependentFormula)  ❑ queued Group8
      │   Base: ARObject , FE , SSCDF
      ├─ FMFormulaByFeaturesAndSwSystemconsts(SwSystemconstDependentFormula)  ❑ queued
      │   Base: ARObject , FE , SSCDF · FMXF Table 7.3
      │   │
      │   └─ FMConditionByFeaturesAndSwSystemconsts  ❑ queued
      │         Base: ARObject , FMFormulaByFeaturesAndSwSystemconsts , FE , SSCDF · FMXF Table 7.4
      └─ (AttributeValueVariationPoint subtree — see subtree 2)
```

**FMFormulaByFeaturesAndAttributes branch (direct FormulaExpression children):**

```
FormulaExpression
│
├─ FMFormulaByFeaturesAndAttributes  ❑ queued
│     Base: ARObject , FormulaExpression · FMXF Table 7.1
│   │
│   └─ FMConditionByFeaturesAndAttributes  ❑ queued
│         Base: ARObject , FMFormulaByFeaturesAndAttributes , FormulaExpression · FMXF Table 7.2
```

### 2. AttributeValueVariationPoint subtree (10)

```
AttributeValueVariationPoint(SwSystemconstDependentFormula, ABC)  ✔ STAMPED
│
├─ AbstractEnumerationValueVariationPoint(., ABC)  ❑ queued Group8
│     Base: ARObject , AVP , FE , SSCDF
├─ AbstractNumericalVariationPoint(AVP, ABC)  ✔
│   │
│   ├─ NumericalValueVariationPoint  ✔   Base: ARObject , AbstractNumericalVariationPoint , AVP , FE , SSCDF
│   └─ LimitValueVariationPoint  ✔       Base: ARObject , AbstractNumericalVariationPoint , AVP , FE , SSCDF
│
├─ BooleanValueVariationPoint  ✔            Base: ARObject , AVP , FE , SSCDF
├─ FloatValueVariationPoint  ✔              Base: ARObject , AVP , FE , SSCDF
├─ IntegerValueVariationPoint  ✔            Base: ARObject , AVP , FE , SSCDF
├─ PositiveIntegerValueVariationPoint  ✔    Base: ARObject , AVP , FE , SSCDF
├─ UnlimitedIntegerValueVariationPoint  ✔   Base: ARObject , AVP , FE , SSCDF
└─ TimeValueValueVariationPoint  ✔          Base: ARObject , AVP , FE , SSCDF
```

### 3. Direct-mixin classes (Base = plain ARObject, no stereotyped ancestor) (3 + 6)

```
AtpMixedString(ABC)
│
├─ EcucQueryExpression(ARObject, AtpMixedString)  ⚙ mixin pending
│     Base: ARObject · CP ECUC Table 2.40 (XSD: group only, no own complexType)
├─ EmphasisText(ARObject, AtpMixedString)  ⚙ mixin pending
│     Base: ARObject · MSR DataDictionary (InlineTextElements)
├─ IndexEntry(ARObject, AtpMixedString)  ⚙ mixin pending
│     Base: ARObject · MSR DataDictionary (InlineTextElements)
│
├─ MixedContentForLongName(ARObject, AtpMixedString, ABC)  ✔ IN SRC — mixin pending
   │   │   GST Table 4.9, p.63 — STAMPED
   │   │   GST Table 4.9, p.63 — STAMPED
   │   ├─ LLongName(+ LanguageSpecific)  ✔ chain correct
   │   └─ SingleLanguageLongName  ✔     GST Table 4.7, p.62 — STAMPED
   ├─ MixedContentForParagraph(ARObject, AtpMixedString, ABC)  ✔ IN SRC — mixin pending
   │   │   Subclasses: LParagraph, SlParagraph
   │   ├─ LParagraph(+ LanguageSpecific)  ✔
   │   └─ SlParagraph  ✔
   ├─ MixedContentForOverviewParagraph(ARObject, AtpMixedString, ABC)  ❑ queued Group8
   │   │   Base: ARObject · InlineTextModel
   │   ├─ LOverviewParagraph(+ LanguageSpecific)  ⚠ src misses this base
   │   └─ SlOverviewParagraph  ❑ queued Group8
   │         Base: ARObject , MixedContentForOverviewParagraph · SingleLanguageData
   ├─ MixedContentForPlainText(ARObject, AtpMixedString, ABC + WhitespaceControlled)  ❑ queued Group8
   │   │   Base: ARObject , WhitespaceControlled · InlineTextModel
   │   └─ LPlainText(+ LanguageSpecific + WhitespaceControlled)  ⚠ src misses 2 bases
   ├─ MixedContentForVerbatim(ARObject, AtpMixedString, ABC + WhitespaceControlled)  ❑ queued Group8
   │   │   Base: ARObject , WhitespaceControlled · InlineTextModel
   │   └─ LVerbatim(+ LanguageSpecific + WhitespaceControlled)  ⚠ src misses 2 bases
   └─ MixedContentForUnitNames(ARObject, AtpMixedString, ABC)  ✱ CREATED 2026-09-25 — stamp pending 9b
       │   Base: ARObject · GST Table E.55, p.456 · attrs: sub/sup (Superscript)
       └─ SingleLanguageUnitNames  ✱ FIXED 2026-09-25 (was ARLiteral; a brief
             FormulaExpression re-parent was reverted — caption-shift misread)
             Base: ARObject , MixedContentForUnitNames · CP SWCT Table 5.80, p.400
```

Secondary doc-model bases (NOT stereotyped): `LanguageSpecific(ARObject)` (abstract),
`WhitespaceControlled(ARObject)` (abstract).

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
| `SingleLanguageUnitNames` | ARObject, MixedContentForUnitNames | `(ARLiteral)` → FIXED: `(MixedContentForUnitNames)` | ✔ re-parented 2026-09-25 (was ARLiteral; a brief FormulaExpression re-parent was reverted — it came from a caption-shift misread) |

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

1. ✅ **APPLIED 2026-09-25** — re-parented to `FormulaExpression`: `CompuGenericMath`,
   `EcucConditionFormula`, `EcucParameterDerivationFormula`, `TimingConditionFormula`
   (Referrable dropped incl. parser/writer SHORT-NAME handling), `TDEventOccurrenceExpressionFormula`.
2. ✅ **APPLIED 2026-09-25** — `SingleLanguageUnitNames` re-parented to the NEW
   `MixedContentForUnitNames(ARObject, ABC)` (markdown-verified Base row; the earlier
   FormulaExpression claim was a caption-shift misread and was reverted). Serialization
   of UNIT-DISPLAY-NAME / DISPLAY-NAME switched from the ARLiteral helpers to the
   doc-family pattern (text + SUB/SUP attributes), mirroring SingleLanguageLongName.
3. **Add the mixin** (Base = plain ARObject, stereotyped): `EcucQueryExpression`,
   `EmphasisText`, `IndexEntry`, `MixedContentForLongName`, `MixedContentForParagraph`.
4. **Missing doc-model bases** (queued in Group8.md): `MixedContentForOverviewParagraph`,
   `MixedContentForPlainText`, `MixedContentForVerbatim`, `SlOverviewParagraph`;
   re-parent `LOverviewParagraph`/`LPlainText`/`LVerbatim` once their bases land.
5. **Queued (unsynced)**: `BlueprintFormula`, `FMConditionByFeaturesAndAttributes`,
   `FMConditionByFeaturesAndSwSystemconsts`, `FMFormulaByFeaturesAndAttributes`,
   `FMFormulaByFeaturesAndSwSystemconsts`, `AbstractEnumerationValueVariationPoint` —
   their Group8 rows carry the dependency order (parents before dependents).

Every re-parent above follows Rule 0001.2; each touched class needs its checklist/test
revisit (Rule 0012.3 drift pass) and 9b confirmation before its row is stamped.
