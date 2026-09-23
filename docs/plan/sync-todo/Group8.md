# Sync todo: Group 8 — CommonStructure/GeneralStructure generics

Input: full-repo orphan audit 2026-09-23 (unstamped ∧ untracked, M2 only) · Queue order = row order
(resume = first class row still `[ ]`; all class rows `[x]` = sync finished — Rule 0017.3)
> **Rule — already-verified short-circuit (added 2026-09-04):** before running the 9-step
> sync for a row, check whether the class already carries `# Spec verified: <RELEASE>` or
> `# XSD verified: <xsd-file>` in its own class body (verify the marker in the source — a
> row in this todo is not proof). If it does **and** a quick deviation check finds nothing
> new (base vs the spec `Base` closure, member types vs its table, verbatim docstrings,
> reader/writer coverage, checklist shape per Rules 0002/0012), **skip the 9 steps**: mark
> the row `- [x] <Class> — already verified (<marker>, <file>)` and move on. If the check
> finds a new deviation, do **not** mark it verified — keep the row queued, run the steps
> for the deviation only, and record it in Step 8 (Rule 0012.3: an existing marker is not
> proof).

## Queue (dependency-first)

- [ ] `BindingTimeEnum` — AREnum — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Enumerations.py
  - note: deviation-tracked in method_deviation_by_class_v2.md — review entries at Step 1
  - [x] Step 1 — Sync members & description from spec — Table E.8 (AUTOSAR_CP_TPS_SoftwareComponentTemplate, p.972) cited; byte-identical reproductions Table D.16 (CP BSWModuleDescriptionTemplate, p.308) + Table C.15 (FO StandardizationTemplate, p.163); Enumeration table: Package M2::AUTOSARTemplates::GenericStructure::VariantHandling; Note "This enumerator specifies the applicable binding times for the pre build variation points."; Aggregated by AttributeValueVariationPoint.bindingTime, ConditionByFormula.bindingTime, FMFeature.max/minIntendedBindingTime, FMFeatureSelection.max/minSelectedBindingTime; 4 literals displayed order idx0-3 codeGenerationTime/linkTime/preCompileTime/systemDesignTime ("codeGeneration Time" spacing in D.16 is a PDF-extraction artifact — XSD mmt.qualifiedName confirms camelCase); XSD 00052 L131754 BINDING-TIME-ENUM--SIMPLE wire tokens CODE-GENERATION-TIME/LINK-TIME/PRE-COMPILE-TIME/SYSTEM-DESIGN-TIME, no atp.Status=removed literals; pdf_page.py cannot index letter-table ids (numeric-only regex) — pages via direct pypdf scan; spec Package row → VariantHandling (non-leaf) vs file GeneralTemplateClasses/Enumerations.py — location kept per queue row, recorded as Step 8 finding
  - [x] Step 2 — Write model class unit test (Red) — extended existing TestBindingTimeEnum in test_Enumerations.py (no duplication): verbatim class-Note assertion, no-`__init__`-docstring, member constants + camelCase values, displayed-order getEnumValues, setValue/getValue/getText, validateEnumValue true/false; 3 Red (missing member constants, paraphrased docstring) / 6 passed — literal values + order already spec-correct (verified vs E.8 + XSD), honestly noted
  - [x] Step 3 — Implement model class (Green) — AREnum shape already spec-correct on values/order (verified vs E.8 + XSD); added Rule 0011 member constants CODE_GENERATION_TIME/LINK_TIME/PRE_COMPILE_TIME/SYSTEM_DESIGN_TIME = camelCase spec literals (matching parser/writer BINDING_TIME_XML_MAP keys), displayed-order tuple, per-literal verbatim description comments + Tags; 9/9 Green, 445 consumer tests pass
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — paraphrased class docstring ("Enumeration for binding time in AUTOSAR variant handling…") wiped and replaced with the verbatim Table E.8 Note; enum has no `__init__`/getter/setter docstrings to sync (AREnum base supplies accessors)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: standalone AREnum, no own XML element; serialized as attribute value on consumers (AttributeValueVariationPoint.bindingTime, ConditionByFormula.bindingTime per the table's Aggregated-by row) and round-tripped there; camelCase↔UPPER-KEBAB wire mapping via BINDING_TIME_XML_MAP (parser L1143 / writer L1014) verified by 445 existing consumer tests
  - [x] Step 6 — Update parser & writer (Green) — N/A: standalone AREnum (no readBindingTimeEnum/writeBindingTimeEnum exists or is needed); consumer readConditionByFormula/readAttributeValueVariationPoint + write counterparts pre-exist and pass
  - [x] Step 7 — Update checklist comment — 6-column format with `# (no methods) — enum value form serialized on AttributeValueVariationPoint.bindingTime + ConditionByFormula.bindingTime (Steps 5/6 N/A: standalone AREnum)`, Spec line cites Table E.8 p.972; marker NOT written (deferred to batch confirmation)
  - [x] Step 8 — Deviations  [none open: no naming/type/missing rows — literals were already camelCase-correct vs E.8/XSD; v1 tracker (method_deviation_by_class.md) has NO BindingTimeEnum entry (verified by grep); v2 tracker has only an Appendix bullet ("classes without a spec attribute table", L1861) — accurate for an enum, left in place per AutoCollectEnum precedent (stamped + still listed until next regeneration); location finding: spec Package row = GenericStructure::VariantHandling (non-leaf → Rule 0007 would put the class in VariantHandling/__init__.py) but class stays in GeneralTemplateClasses/Enumerations.py per the queue row — flagged for batch/user decision, not moved unilaterally; referenced classes: base AREnum (PrimitiveTypes) exists, unstamped, queued elsewhere — no missing classes]
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-23: target file 9/9, full suite 11030 passed/0 failed (baseline 11025 + 5 net-new), npm run lint (flake8+ruff) clean, black-check clean; 9b deferred to batch confirmation (user instruction 2026-09-24)

- [ ] `XmlSpaceEnum` — AREnum — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Enumerations.py
  - note: deviation-tracked in method_deviation_by_class.md + method_deviation_by_class_v2.md — review entries at Step 1
  - [x] Step 1 — Sync members & description from spec — XSD-only confirmed via mandatory both-corpora gate: caption grep `^Table [id]: XmlSpaceEnum` (case-insensitive tolerant pass too) + header-cell/subject-row grep = 0 hits in R23-11 (CP_TPS+FO_TPS) AND R4.3.1 markdown; only consumer attribute-type refs (Sd.xmlSpace FO ARXMLSerializationRules L925, VerbatimString CP ECUConfiguration Table F.48 + FO GenericStructureTemplate Tables 4.21/4.67, WhitespaceControlled FO GenericStructureTemplate Table 9.7); derived from XSD AUTOSAR_00052.xsd L145398 XML-SPACE-ENUM / L145410 --SIMPLE: class Note "This enumerator specifies the fact that white-space shall be preserved."; literals displayed order idx0-1 default/preserve (wire tokens ARE the lowercase xml:space values — no kebab-case mapping unlike BindingTimeEnum; XSD xml.name=default/preserve confirms), per-literal Notes verbatim from XSD docs, Tags atp.EnumerationLiteralIndex=0/1 (existing comments wrongly said atp.EnumerationValue); consumers: Sd.xmlSpace (writer writeSds arxml_writer.py:1090 emits {xml}space attr; parser readSd arxml_parser.py:1213 does NOT read it back — consumer gap → Step 8), VerbatimString.xmlSpace not implemented ("missing enum type" note now stale → Step 8); tracker entries reviewed (v1 skip-note stale → reconcile Step 8, v2 Appendix bullet accurate → keep)
  - [x] Step 2 — Write model class unit test (Red) — rewrote existing weak TestXmlSpaceEnum in test_Enumerations.py to the spec-contract form (mirrors TestBindingTimeEnum): verbatim class-Note assertion (XSD L145398 doc), no-`__init__`-docstring, member constants + wire values, displayed-order getEnumValues ["default","preserve"], setValue/getValue/getText, validateEnumValue true/false (incl. case-sensitivity); 1 Red (verbatim docstring — old class docstring carried the consumer-attribute Note, wrong provenance) / 11 passed — literal values + order + validateEnumValue already spec-correct vs XSD, honestly noted
  - [x] Step 3 — Implement model class (Green) — AREnum shape already spec-correct on values/order (verified vs XSD L145410 --SIMPLE); kept constants DEFAULT/PRESERVE (already UPPER_SNAKE), displayed-order tuple, verbatim per-literal comments; fixed comment Tags atp.EnumerationValue→atp.EnumerationLiteralIndex=0/1 (XSD appinfo) + class docstring replaced with verbatim XSD Note; 12/12 Green + 19/19 consumer (test_SpecialData)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — wiped the stale class docstring (was the Sd.xmlSpace consumer-attribute Note "This attribute is used to signal an intention…W3C.") and replaced with the enum's own XSD documentation verbatim ("This enumerator specifies the fact that white-space shall be preserved."); enum has no `__init__`/getter/setter docstrings to sync (AREnum base supplies accessors, None asserted by test); per-literal inline comments verbatim from XSD docs incl. lowercase "the value \"preserve\"…"
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: standalone AREnum, no own XML element; serialized as attribute value on the consumer Sd.xmlSpace (XSD mmt.qualifiedName="Sd.xmlSpace" L101701; other XSD consumers VerbatimString.xmlSpace / WhitespaceControlled.xmlSpace not modeled) — writer writeSds (arxml_writer.py:1090) emits {http://www.w3.org/XML/1998/namespace}space from xml_space.getValue(); round-tripped on the consumer side (19 Sd tests pass)
  - [x] Step 6 — Update parser & writer (Green) — N/A: standalone AREnum (no readXmlSpaceEnum/writeXmlSpaceEnum exists or is needed); note: parser readSd (arxml_parser.py:1213) does not read the xml:space attribute back while the writer emits it — pre-existing consumer-level gap in Sd, recorded as Step 8 finding, NOT fixed unilaterally (Sd is a stamped class outside this row's scope)
  - [x] Step 7 — Update checklist comment — 6-column format with `# Spec: XSD-only, AUTOSAR_00052.xsd line 145398 (no own table in repo corpus)` + `# (no methods) — enum value form serialized on Sd.xmlSpace (Steps 5/6 N/A: standalone AREnum)`; `__init__` row all-[x] with release R23-11; marker (`# XSD verified: AUTOSAR_00052.xsd`) NOT written (deferred to batch confirmation)
  - [x] Step 8 — Deviations  [none open: no naming/type/missing rows — values/order/docstrings all match XSD L145398/145410; v1 tracker (method_deviation_by_class.md) XmlSpaceEnum skip-note reconciled 2026-09-24 → now records the XSD-only sync and supersedes the old "left as-is" wording; v2 tracker has only an Appendix bullet ("classes without a spec attribute table", L1862) — accurate for an enum, left in place per AutoCollectEnum/BindingTimeEnum precedent; findings (consumer-level, not class deviations, not fixed unilaterally): (1) parser readSd does not read xml:space back while writer writeSds emits it — Sd reader gap, flagged for Sd/SdgContents sync (Sd is stamped; fixing would change a stamped class's round-trip); (2) VerbatimString.xmlSpace unimplemented — its docstring note "missing enum type" is now stale since the enum exists, flagged for VerbatimString sync; (3) location: XSD mmt.qualifiedName="XmlSpaceEnum" carries no package qualifier — kept in GeneralTemplateClasses/Enumerations.py per queue row; referenced classes: base AREnum (PrimitiveTypes) exists unstamped/queued elsewhere, consumer Sd exists and is stamped — no missing classes]
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-24: target file 12/12 (TestXmlSpaceEnum 6 + TestBindingTimeEnum 6), full suite 11033 passed/0 failed (baseline 11030 + 3 net-new from rewriting 3 weak tests into 6), npm run lint (flake8+ruff) clean, npm run black no-op + black-check clean; 9b deferred to batch confirmation (user instruction 2026-09-24)

- [ ] `ShortNameFragment` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `MultidimensionalTime` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/MultidimensionalTime.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `LifeCyclePeriod` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/LifeCycles.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `BuildActionIoElement` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/BuildActionManifest.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `AttributeValueVariationPoint` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/VariantHandling/AttributeValueVariationPoints/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `BindingTimeEnum`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ConditionByFormula` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `BindingTimeEnum`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SwSystemconstValue` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `PostBuildVariantCondition` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `PostBuildVariantCriterion` — ARElement — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `PostBuildVariantCriterionValue` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ModeInSwcBswInstanceRef` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `OffsetTimingConstraint` — TimingConstraint — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/OffsetConstraint.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `MultidimensionalTime`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SynchronizationTimingConstraint` — TimingConstraint — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `MultidimensionalTime`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `TimingDescriptionEventChain` — TimingDescription — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/Timing/TimingDescription/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `AutosarOperationArgumentInstance` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/Timing/TimingDescription/TimingDescriptionEvents/TDEventOccurrenceExpression.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ConcreteTDEventVfb` — TDEventVfb — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/Timing/TimingDescription/TimingDescriptionEvents/TDEventVfb.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `AtpBlueprint` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/AbstractBlueprintStructure/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md + method_deviation_by_class_v2.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `BlueprintGenerator` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintGenerator.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `BlueprintMapping` — AtpBlueprintMapping — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintMapping.py
  - note: deviation-tracked in method_deviation_by_class.md + method_deviation_by_class_v2.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `LifeCycleInfo` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/LifeCycles.py
  - after `LifeCyclePeriod`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `LifeCycleInfoSet` — ARElement — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/LifeCycles.py
  - after `LifeCyclePeriod`
  - after `LifeCycleInfo`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `VariationPoint` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/VariantHandling/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `ConditionByFormula`
  - after `PostBuildVariantCondition`
  - after `BlueprintGenerator`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ModeInSwcInstanceRef` — AtpInstanceRef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `ModeInSwcBswInstanceRef`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
