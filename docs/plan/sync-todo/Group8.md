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
  - [x] Step 1 — Sync members & description from spec — Table 4.13 (AUTOSAR_FO_TPS_GenericStructureTemplate, p.64 via pdf_page.py); R4.3.1 reproduction Table 4.18 (p.64) byte-identical incl. displayed order; Package M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable matches current file; class Note verbatim in place; Base ARObject ✓; Aggregated by Referrable.shortNameFragment → XSD wrapper SHORT-NAME-FRAGMENTS (REFERRABLE group, seqOffset=-90, unbounded choice of SHORT-NAME-FRAGMENT); attributes displayed order fragment (Identifier, 1, attr, seqOffset=20) then role (String, 1, attr, seqOffset=10); XSD 00052 group SHORT-NAME-FRAGMENT L106612 (ROLE=10, FRAGMENT=20 → XML element order ROLE,FRAGMENT — writer already emits in that order), complexType L106634; two deviations found (fix in Steps 3/6): role typed Optional[str] vs spec String (Rule 0001.3 — sibling fragment already typed Identifier; strict Optional[String] is the stamped convention per setUuid/setAnnotationOrigin/setHelpEntry) and member/accessor order role→fragment vs markdown displayed fragment→role (Rule 0001.11); reader/writer coverage pre-exists (parser getShortNameFragments L1385 consumed by readReferrable L1401, writer setShortNameFragment(s) L1224/L1233 consumed by writeReferrable L1210) — Steps 5/6 extend, NOT N/A; tracker v1 "## Referrable" section (CP BSWModuleDescriptionTemplate audit) lists shortName+shortNameFragment as missing — stale vs current code, reconcile Step 8; v2 tracker has no ShortNameFragment entries
  - [x] Step 2 — Write model class unit test (Red) — extended existing TestShortNameFragment in test_Identifiable.py (no duplication): added verbatim class-Note assertion, no-`__init__`-docstring assertion, PDF-typed accessor annotations via typing.get_type_hints (repo style per test_SwComponentPrototypeAssignment) for role→Optional[String] + fragment→Optional[Identifier]; rewrote role setter/getter + None-no-op tests to the String contract (String().setValue, isinstance + getValue); 1 Red (test_role_typed_string — role is Optional[str] vs spec String) / 8 passed — verbatim docstring, Identifier typing, defaults, round-trip, None no-ops already spec-correct, honestly noted
  - [x] Step 3 — Implement model class (Green) — role retyped Optional[str]→Optional[String] (spec String; sibling fragment already typed Identifier — Rule 0001.3), member/accessor order reordered to markdown displayed order fragment→role (was role→fragment — Rule 0001.11); Base stays ARObject; concrete class (XSD complexType abstract="false"); setter shape kept (None no-op, returns self); no fabricated/extra fields (field-to-spec both directions: exactly fragment+role); 44/44 Green in test_Identifiable.py
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — whole class body replaced in the Step 3 pass (old "Gets the…/Sets the…" Google-style paraphrases wiped, no stale wording survives); class docstring = Table 4.13 Note verbatim; inline `__init__` comments = attribute Notes verbatim incl. Tags (xml.sequenceOffset=20/10); getter docstrings = Note verbatim, setter docstrings = Note + "A None value is a no-op…" sentence (form matches stamped MultilanguageReferrable/Identifiable in the same file); no `__init__` docstring; PEP 526 annotated members with blank line between the two attribute blocks
  - [x] Step 5 — Write reader/writer round-trip test (Red) — extended existing tests/test_armodel/parser/test_short_name_fragments.py (extend, no duplication): strengthened test_round_trip with isinstance(getRole(), String) + getValue (role built via String().setValue), added test_round_trip_multiple_fragments (2 fragments, per-index role/fragment value + type assertions, field values not just len), added test_written_element_order_role_before_fragment (written XML SHORT-NAME-FRAGMENT children == [ROLE, FRAGMENT] per XSD sequenceOffset 10/20; writeARObject emits only S/T attrs so child list is exact); empty-wrapper case pre-existed; 3 Red / 1 passed — Red is real: writer assigns the String object raw to element.text → ET "cannot serialize String" TypeError; order+empty passed immediately (writer already emitted ROLE first — honestly noted)
  - [x] Step 6 — Update parser & writer (Green) — parser getShortNameFragments (arxml_parser.py L1385): raw `ROLE` text read (manual find + setRole(str)) replaced with the matched typed leaf helper getChildElementOptionalString (Rule 0013.2 pair); writer setShortNameFragment (arxml_writer.py L1224): manual ROLE SubElement + raw text assignment replaced with setChildElementOptionalString → getText() (fixes the ET "cannot serialize String" Red), ROLE→FRAGMENT emission order preserved (XSD 10/20); test-side adjustments (not writer bugs): pre-existing direct writer test test_write_referrable_with_short_name_fragments updated to the String contract (setRole(String().setValue("prefix")) — raw str had no getText), element-order test made namespace-agnostic (saved doc carries xmlns; first assertion form was a test bug, writer output was already correct); 114/114 Green across test_short_name_fragments.py + test_arxml_writer.py + test_Identifiable.py
  - [x] Step 7 — Update checklist comment — 6-column format, rows in markdown displayed order (`__init__`, getFragment, setFragment, getRole, setRole), Spec line `AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.13, p.64`, all rows `[x]` with release R23-11; reader [x] on setFragment/setRole (parser sets), writer [x] on getFragment/getRole (writer gets); marker NOT written (deferred to batch confirmation)
  - [x] Step 8 — Deviations  [none open: the two Step 1 findings were fixed in-band and leave no deviation rows — (1) type deviation role str→String fixed in Step 3 with matched parser/writer helpers in Step 6 (Rule 0014: fixed ⇒ no row), (2) member-order deviation fixed in Step 3 (fragment→role per markdown displayed order); v1 tracker (method_deviation_by_class.md) reconciled 2026-09-24: `## Referrable` section's two stale "missing" rows (shortName, shortNameFragment — from the CP BSWModuleDescriptionTemplate audit; both exist in current code) superseded by a resolution Note per XmlSpaceEnum precedent, and a new `## ShortNameFragment` section added (sync record, no-deviation row, stamp-deferred note); v2 tracker has no ShortNameFragment entries; referenced classes: base ARObject stamped, member types Identifier (Table 4.5, stamped) + String (Table 4.63, stamped), consumer Referrable (stamped, same file) — no missing classes]
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-24: target files 114/114 (test_Identifiable.py 44 + test_short_name_fragments.py 4 + test_arxml_writer.py 66), full suite 11039 passed/0 failed (baseline 11033 + 6 net-new: +4 model tests, +2 round-trip tests), npm run lint (flake8+ruff) clean, npm run black no-op (1146 files unchanged) + black-check clean; integration round-trip (29 ARXML) included in the suite green; 9b deferred to batch confirmation (user instruction 2026-09-24)

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
