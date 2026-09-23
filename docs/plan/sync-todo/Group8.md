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
  - [x] Step 1 — Sync members & description from spec — Table 4.74 (AUTOSAR_FO_TPS_GenericStructureTemplate home doc, p.165 via pdf_page.py); table identity check across the 3 reproductions: CP_TPS_SoftwareComponentTemplate Table 4.14 (p.110) + CP_TPS_BSWModuleDescriptionTemplate Table 8.22 (p.165) — Package/Base/attributes (names, types, mults, kind, Note text, displayed order cseCode→cseCodeFactor) identical everywhere; only the Note's bibliography ref number differs ([17] FO home / [15] CP SWCT / [20] CP BSWMDT — cross-doc numbering); Class-vs-Enumeration header = Class ✓; Base ARObject ✓ (XSD 00052 complexType MULTIDIMENSIONAL-TIME L83781 abstract="false" = AR-OBJECT group + MULTIDIMENSIONAL-TIME group — authoritative base confirmation); XSD group L83759: CSE-CODE (CSE-CODE-TYPE-STRING, 0..1) then CSE-CODE-FACTOR (INTEGER, 0..1) — element order CSE-CODE→CSE-CODE-FACTOR, no explicit sequenceOffset; existing class fields match spec exactly both directions (cseCode Optional[CseCodeType], cseCodeFactor Optional[Integer]); leaf file location ✓ (spec package ...GeneralTemplateClasses::MultidimensionalTime); four findings to fix: (1) stale stamp+checklist — old 4-column format, `# Spec verified: R23-11` citing CP BSWMDT Table 8.22 with WRONG page p.164 (actual p.165) and citing a reproduction instead of the home doc — stamp removed this pass (batch instruction: no marker until batch confirmation), checklist rebuilt 6-column; (2) class docstring = [20] reproduction Note + FABRICATED extra paragraphs (ASAM CSE explanation + 100/360 example) — Rule 0012 wipe+rewrite in Step 4; (3) method docstrings are "Gets/Sets the…" paraphrases with fabricated [constr_10338]/[constr_10339] tags — Step 4; (4) reader type gap — getChildElementOptionalLiteral returns ARLiteral but the field/accessor contract is CseCodeType (no matched getChildElementOptionalCseCodeType/setChildElementOptionalCseCodeType pair; precedent: VerbatimString L129 / RevisionLabelString helpers) — fix in Step 6; reader/writer coverage pre-exists (parser readMultidimensionalTime L4510, writer setMultidimensionalTime L5847, element order matches XSD) — Steps 5/6 extend, NOT N/A
  - [x] Step 2 — Write model class unit test (Red) — extended existing TestMultidimensionalTime in test_MultidimensionalTime.py (extend, no duplication): added verbatim class-Note assertion (home-doc [17] form), no-`__init__`-docstring assertion, PDF-typed accessor annotations via typing.get_type_hints (repo style per TestShortNameFragment) for cseCode→Optional[CseCodeType] + cseCodeFactor→Optional[Integer]; 2 Red / 8 passed — Red is real: class docstring still carried the [20] BSW-reproduction Note + fabricated paragraphs, `__init__` had a docstring; both annotation tests passed immediately (accessors already spec-typed — honestly noted); defaults/round-trip/chaining/None-no-op coverage pre-existed (6 tests) and was kept
  - [x] Step 3 — Implement model class (Green) — whole class body replaced (old fabricated docstrings wiped in the same pass); Base stays ARObject (XSD complexType L83781 = AR-OBJECT group, authoritative); concrete class (XSD abstract="false"); field-to-spec both directions: exactly cseCode (Optional[CseCodeType]) + cseCodeFactor (Optional[Integer]) — no fabricated/extra fields; member/accessor order cseCode→cseCodeFactor matches markdown displayed order (Rule 0001.11); PEP 526 annotated members with blank line between the two attribute blocks; setter shape kept (None no-op, returns self); imports NOT re-sorted (models rule); 10/10 Green in test_MultidimensionalTime.py
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — wipe+rewrite landed in the Step 3 body replacement (no stale wording survives: old [20]-citing Note, fabricated ASAM-CSE paragraphs + 100/360 example, "Gets/Sets the…" Google-style paraphrases and fabricated [constr_10338]/[constr_10339] tags all removed); class docstring = Table 4.74 Note verbatim ([17] home doc); inline `__init__` comments = attribute Notes verbatim, no Tags suffix (XSD elements carry no sequenceOffset); getter docstrings = Note verbatim; setter docstrings = Note + "A None value is a no-op…" sentence (form matches stamped ShortNameFragment in sibling Identifiable.py); no `__init__` docstring
  - [x] Step 5 — Write reader/writer round-trip test (Red) — created dedicated tests/test_armodel/parser/test_multidimensional_time.py (3 tests: CSE-CODE read with isinstance-CseCodeType + value assertions, CSE-CODE-FACTOR read with isinstance-Integer + value, absent-elements → both None) and tests/test_armodel/writer/test_multidimensional_time.py (3 tests: written children == [CSE-CODE, CSE-CODE-FACTOR] per XSD group order with text assertions, empty-wrapper case, parse→write→re-parse round-trip with `_round_trip` xmlns-injection helper per test_writer_timing_constraints.py precedent); 2 Red / 4 passed — Red is real: reader `getChildElementOptionalLiteral` stores a plain ARLiteral for cseCode where the field contract is CseCodeType (both failing tests assert isinstance); honest passes: written element order + empty wrapper + value round-trip were already correct, factor read already Integer-typed; one test-side fix during Red triage: re-parsing the raw un-namespaced writer element found nothing (parser find() is namespace-qualified) — fixed with the `_round_trip` helper, writer output was already correct
  - [x] Step 6 — Update parser & writer (Green) — added the matched typed leaf pair (Rule 0013.2): parser `getChildElementOptionalCseCodeType` (abstract_arxml_parser.py, after getChildElementOptionalLiteral, VerbatimString/Identifier body form, returns Optional[CseCodeType]) + writer `setChildElementOptionalCseCodeType` (abstract_arxml_writer.py, after setChildElementOptionalRevisionLabelString, delegates to setChildElementOptionalLiteral); CseCodeType added to both files' PrimitiveTypes import blocks (alphabetical insert, no re-sort); readMultidimensionalTime (arxml_parser.py) now reads CSE-CODE via the typed helper; setMultidimensionalTime (arxml_writer.py) now writes CSE-CODE via the typed helper (writer emission behavior unchanged — CseCodeType IS-A ARLiteral); Green: 16/16 across the 3 target test files + 142/142 across consumer suites (parser timing_constraints/timing_clocks/timing_condition/trigger + writer timing_constraints/timing_clocks/timing_condition/trigger/sw_data_def_props/arxml_writer)
  - [x] Step 7 — Update checklist comment — 6-column format written in the Step 3 body replacement, verified at this step: `# Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.74, p.165` (home doc; supersedes the old CP BSWMDT Table 8.22/p.164 citation), rows in markdown displayed order (`__init__`, getCseCode, setCseCode, getCseCodeFactor, setCseCodeFactor), all `[x]` with release R23-11; reader [x] on setCseCode/setCseCodeFactor (parser sets), writer [x] on getCseCode/getCseCodeFactor (writer gets), `__init__` [—]/[—]; marker NOT written (deferred to batch confirmation)
  - [x] Step 8 — Deviations  [none open: all four Step 1 findings were fixed in-band and leave no deviation rows — (1) stale 4-column checklist + pre-existing `# Spec verified: R23-11` stamp (citing reproduction CP BSWMDT Table 8.22 with off-by-one page p.164) replaced with the 6-column home-doc citation, marker withheld per batch instruction; (2) fabricated class-docstring paragraphs + (3) paraphrase method docstrings with fabricated [constr_10338]/[constr_10339] tags wiped and rewritten verbatim in Steps 3/4; (4) reader type gap (ARLiteral vs CseCodeType) fixed in Step 6 with the matched CseCodeType leaf pair — Rule 0014: fixed ⇒ no row; v1 tracker (docs/examples/method_deviation_by_class.md) `## MultidimensionalTime` section reconciled 2026-09-24 with a Resolution Note (supersedes the old BSWMDT/p.164 citation, records the sync + fixes, no-deviation); v2 tracker has no MultidimensionalTime entries (its consumer-side "missing" rows naming MultidimensionalTime as a field type belong to those consumer classes' own syncs); referenced classes: base ARObject (stamped, same package), member types CseCodeType (Table 4.75, exists in PrimitiveTypes) + Integer (Table 4.63, stamped) — no missing classes]
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-24: target files 16/16 (test_MultidimensionalTime.py 10 + test_multidimensional_time.py parser 3 + writer 3, re-run green after black reformat of the 2 new test files), full suite 11049 passed/0 failed (baseline 11039 + 10 net-new: +4 model tests, +6 round-trip tests), npm run lint (flake8+ruff) clean, npm run black reformatted the 2 new test files (canonical formatting only) + black-check clean (1148 files unchanged); integration round-trip (29 ARXML) included in the suite green; 9b blind-spot checks walked: fields↔spec both directions exact, most-derived base ARObject (XSD L83781), no fabrication/flattening, PDF-typed fields, member order = markdown displayed order, XML element order = XSD group order, docstrings verbatim (class Note [17] home doc + attribute Notes in comments/getters/setters + None-no-op sentences), blank line between __init__ attribute blocks, PEP 526 annotated members, reader+writer coverage for both attrs via matched CseCodeType/Integer leaf pairs, no open deviations, leaf-file location per spec package; 9b deferred to batch confirmation (user instruction 2026-09-24)

- [ ] `LifeCyclePeriod` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/GenericStructure/LifeCycles.py
  - [x] Step 1 — Sync members & description from spec — Table 12.4 (AUTOSAR_FO_TPS_GenericStructureTemplate, p.392 via pdf_page.py); R4.3.1 reproduction Table 11.4 (p.364) byte-identical incl. attribute rows/Notes/sequenceOffsets; Class-vs-Enumeration header = Class ✓; Package M2::AUTOSARTemplates::GenericStructure::LifeCycles matches current leaf file; Note verbatim in place (2-line wrapped); Base ARObject ✓ (XSD 00052 complexType LIFE-CYCLE-PERIOD L76738 abstract="false" = AR-OBJECT group + LIFE-CYCLE-PERIOD group — authoritative base confirmation); XSD group L76708: DATE (sequenceOffset=10) → AR-RELEASE-VERSION (=20) → PRODUCT-RELEASE (=30) — XML element order DATE, AR-RELEASE-VERSION, PRODUCT-RELEASE; attributes displayed order arReleaseVersion (RevisionLabelString 0..1 attr) → date (DateTime 0..1 attr) → productRelease (RevisionLabelString 0..1 attr) matches existing member/accessor order (Rule 0001.11 OK); Aggregated by LifeCycleInfo.periodBegin/periodEnd + LifeCycleInfoSet.defaultPeriodBegin/defaultPeriodEnd (XSD L76563/76569/76645/76651, all type LIFE-CYCLE-PERIOD); existing class fields match spec except ONE deviation: date typed Optional[datetime] vs spec DateTime (DateTime(ARLiteral) exists in PrimitiveTypes L1344; matched leaf pair getChildElementOptionalDateTime/setChildElementOptionalDateTime exists with RevisionLabel DATE precedent) — fix Steps 3/6; old 4-column checklist without `# Spec:` line — rebuild 6-column Step 7; method docstrings are "Gets/Sets the…" paraphrases — wipe+rewrite Step 4; reader/writer disposition: keyed helper-only (getLifeCyclePeriod/setLifeCyclePeriod take the wrapper key — PERIOD-BEGIN/PERIOD-END/DEFAULT-PERIOD-BEGIN/DEFAULT-PERIOD-END), no dispatcher entry (atpObject aggregated inside consumers, never standalone) — but both helpers cover ONLY AR-RELEASE-VERSION; DATE + PRODUCT-RELEASE missing on both sides — fix Step 6; consumer-side gaps (readLifeCycleInfo/writeLifeCycleInfo handle PERIOD-BEGIN only, LifeCycleInfoSet readers/writers touch no DEFAULT-PERIOD-*) belong to the later LifeCycleInfo/LifeCycleInfoSet rows — NOT this row's scope
  - [x] Step 2 — Write model class unit test (Red) — extended existing TestLifeCyclePeriod in test_LifeCycles.py (no duplication): added verbatim class-Note assertion (Table 12.4 single-line form), no-`__init__`-docstring assertion, PDF-typed accessor annotations via typing.get_type_hints (repo style per TestMultidimensionalTime) for arReleaseVersion/date/productRelease → Optional[RevisionLabelString]/Optional[DateTime]/Optional[RevisionLabelString] (setter value annotations checked as Optional too, per the stamped setUuid/ShortNameFragment convention); rewrote test_set_date + test_set_date_none to the DateTime contract (DateTime().setValue("2023-06-15T12:00:00+01:00")), removed the now-unused `from datetime import datetime`; 4 Red / 46 passed — Red is real: class docstring is 2-line wrapped vs the verbatim single-line Note (Step 4), `date` field is Optional[datetime] vs spec DateTime and both RevisionLabelString setters + setDate take non-Optional value (Step 3); test_init_has_no_docstring passed immediately (`__init__` already docstring-less — honestly noted); pre-existing defaults/round-trip/chaining/None-no-op coverage (8 tests) kept and green
  - [x] Step 3 — Implement model class (Green) — whole LifeCyclePeriod class body replaced in one pass; field-to-spec both directions: exactly arReleaseVersion (Optional[RevisionLabelString]) + date (Optional[DateTime] — retyped from Optional[datetime], spec DateTime; DateTime(ARLiteral) exists in PrimitiveTypes L1344 — Rule 0001.3) + productRelease (Optional[RevisionLabelString]); Base stays ARObject (XSD complexType L76738 = AR-OBJECT group, authoritative); concrete class (XSD abstract="false"); member/accessor order arReleaseVersion→date→productRelease matches markdown displayed order (Rule 0001.11); setters retyped `value: Optional[T]` + `-> "LifeCyclePeriod"` return annotation and inline None-no-op sentence per the stamped setFragment/setRole convention in Identifiable.py (test-checked); PEP 526 annotated members with blank line between the three attribute blocks; `from datetime import datetime` import removed, DateTime added to the existing PrimitiveTypes import line (extended in place — imports NOT re-sorted per models rule); verified no other consumer used the old datetime contract (grep); 50/50 Green in test_LifeCycles.py (3 typing tests were still Red after the first pass because setters lacked the `-> "LifeCyclePeriod"` annotation the test asserts — added, stamped-convention alignment)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — landed in the Step 3 body replacement (no stale wording survives: old "Gets/Sets the…" Google-style paraphrases + Args/Returns blocks wiped); class docstring = Table 12.4 Note verbatim (single line, was 2-line wrapped); inline `__init__` comments = attribute Notes verbatim incl. Tags (xml.sequenceOffset=20/10/30); getter docstrings = Note verbatim (no Tags suffix, per stamped ShortNameFragment form); setter docstrings = Note verbatim + "A None value is a no-op and does not overwrite an existing …" sentence; no `__init__` docstring
  - [x] Step 5 — Write reader/writer round-trip test (Red) — created dedicated tests/test_armodel/parser/test_life_cycle_period.py (3 tests: all-fields read with isinstance-DateTime/RevisionLabelString + value assertions, partial read (AR-RELEASE-VERSION only) → date/productRelease None, absent wrapper element → None) and tests/test_armodel/writer/test_life_cycle_period.py (4 tests: written children == [DATE, AR-RELEASE-VERSION, PRODUCT-RELEASE] per XSD sequenceOffset 10/20/30 with text assertions, None period → no element, empty period → empty wrapper, parse→write→re-parse round-trip with `_round_trip` xmlns helper per test_multidimensional_time.py precedent); 3 Red / 4 passed — Red is real: reader reads only AR-RELEASE-VERSION (DATE + PRODUCT-RELEASE → None), writer emits only AR-RELEASE-VERSION; honest passes: partial/absent read + None/empty write were already correct; two test-side fixes during Red triage (implementation untouched): getLifeCyclePeriod expects the PARENT element (keyed find) so parser input wrapped in PARENT, and AR-RELEASE-VERSION wire values changed "R23-11"→"4.3.1" (getChildElementOptionalRevisionLabelString regex requires major.minor.revision — model-side setValue accepts anything, parser-side validates)
  - [x] Step 6 — Update parser & writer (Green) — reader `getChildElementOptionalDateTime` (abstract_arxml_parser.py): ARLiteral-delegating body replaced with the CseCodeType-form typed body (instantiates DateTime — fixes the pre-existing reader type gap where DocRevision.setDate received a plain ARLiteral; DateTime IS-A ARLiteral so the ARLiteral-typed consumers are unaffected; DocRevision.setDate signature is Optional[DateTime] so this is strictly type-correct); getLifeCyclePeriod (arxml_parser.py) now reads DATE via getChildElementOptionalDateTime + AR-RELEASE-VERSION + PRODUCT-RELEASE via the matched RevisionLabelString leaf pair; setLifeCyclePeriod (arxml_writer.py) now writes DATE via setChildElementOptionalDateTime + AR-RELEASE-VERSION + PRODUCT-RELEASE in XSD sequenceOffset order (10/20/30); Green: 57/57 across the 3 target test files, 37/37 test_writer_signals_diagnostic.py (TestWriterSetLifeCyclePeriod/LifeCycleInfo consumers unaffected by the added DATE-first emission), 903/903 admin/doc/revision/documentation consumer tests
  - [x] Step 7 — Update checklist comment — 6-column format written in the Step 3 body replacement, verified at this step: `# Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 12.4, p.392` (home doc; R4.3.1 Table 11.4 p.364 is a byte-identical reproduction), rows in markdown displayed order (`__init__`, getArReleaseVersion, setArReleaseVersion, getDate, setDate, getProductRelease, setProductRelease), all `[x]` with release R23-11; reader [x] on the three setters (parser sets), writer [x] on the three getters (writer gets), `__init__` [—]/[—]; marker NOT written (deferred to batch confirmation)
  - [x] Step 8 — Deviations  [none open: both Step 1 findings were fixed in-band and leave no deviation rows — (1) type deviation date datetime→DateTime fixed in Step 3 with the matched typed helper repaired in Step 6 (getChildElementOptionalDateTime body instantiated a plain ARLiteral despite its DateTime signature; now CseCodeType-form — Rule 0014: fixed ⇒ no row), (2) reader/writer AR-RELEASE-VERSION-only gaps fixed in Step 6 (all three attrs, XSD order); v1 tracker (docs/examples/method_deviation_by_class.md) reconciled 2026-09-24: new `## LifeCyclePeriod` section added (sync record, no-deviation row, stamp-deferred note, consumer-wiring scope note); v2 tracker has no LifeCyclePeriod entries (verified by grep); consumer-side gaps NOT fixed unilaterally (belong to the later rows in this file): readLifeCycleInfo/writeLifeCycleInfo handle PERIOD-BEGIN only (no PERIOD-END), LifeCycleInfoSet readers/writers touch no DEFAULT-PERIOD-BEGIN/DEFAULT-PERIOD-END; referenced classes: base ARObject stamped, member types RevisionLabelString (PrimitiveTypes, unstamped, queued elsewhere) + DateTime (PrimitiveTypes, unstamped 4-column checklist, queued elsewhere), consumers LifeCycleInfo/LifeCycleInfoSet queued after this row — no missing classes]
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-24: target files 94/94 (test_LifeCycles.py 50 + test_life_cycle_period.py parser 3 + writer 4 + test_writer_signals_diagnostic.py 37, re-run green after black reformat of 2 test files), full suite 11061 passed/0 failed (baseline 11049 + 12 net-new: +5 model tests, +7 round-trip tests), npm run lint (flake8+ruff) clean, npm run black reformatted the 2 new/extended test files (canonical formatting only) + black-check clean (1150 files unchanged); integration round-trip (29 ARXML) included in the suite green; 9b blind-spot checks walked: fields↔spec both directions exact (3 attrs), most-derived base ARObject (XSD L76738), no fabrication/flattening, PDF-typed fields (RevisionLabelString/DateTime), member order = markdown displayed order, XML element order = XSD sequenceOffset 10/20/30, docstrings verbatim (class Note + attribute Notes in inline comments/getters/setters + None-no-op sentences), blank line between __init__ attribute blocks, PEP 526 annotated members, reader+writer coverage for all 3 attrs via matched leaf pairs, no open deviations, leaf-file location per spec package; 9b deferred to batch confirmation (user instruction 2026-09-24)

- [ ] `BuildActionIoElement` — ARObject — R23-11 FO_TPS_GenericStructureTemplate Table 10.3 (p.369)
  - module: M2/AUTOSARTemplates/GenericStructure/BuildActionManifest.py
  - note: Step 1 finding — orphan intake already models 5/6 attrs (category/ecucDefinitionRef/engineeringObject/role/sdgs, verbatim docstrings, ARObject base confirmed vs XSD complexType); `foreignModelReference` (aggr, ForeignModelReference) unmodeled — member class absent from src and table-less in both corpora (XSD-only, AUTOSAR_00052.xsd l.62888), not in confirmed closure → deviation row (Step 8). Reader type gap: CATEGORY read as plain ARLiteral, fix via getChildElementOptionalNameToken/setChildElementOptionalNameToken matched pair. Consume path stays helper-dispatch (readBuildActionIoElement/writeBuildActionIoElement from CREATED/INPUT/MODIFIED-DATAS wrappers).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-24: BuildActionManifest test files 72 passed (parser+writer Red first: 2 failed on CATEGORY ARLiteral-vs-NameToken, then Green after matched getChildElementOptionalNameToken/setChildElementOptionalNameToken pair); full suite `uv run python scripts/run_tests.py --no-coverage` 11067 passed / 0 failed (baseline 11061 + 6 new); `npm run lint` clean (flake8 E9,F63,F7,F82 + ruff E/F/W/I); `npm run black` + `black-check` clean (1150 files unchanged); 9b by-eye checks done (member order = Table 10.3 displayed order, XML order = XSD group sequence, docstrings verbatim by diff, blank lines between __init__ blocks, PEP 526, no `# type:`); 9b deferred to batch confirmation (user instruction 2026-09-24)

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
