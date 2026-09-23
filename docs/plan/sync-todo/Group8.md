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
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

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
