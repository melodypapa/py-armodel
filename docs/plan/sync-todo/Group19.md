# Sync todo: Group 19 — ECUC templates

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

## Batch 9b audit findings (2026-10-05)

Mechanical gate `audit_class.py` run over all 16 Group19 rows on branch
`feature/g19-9b-fixes`. Two groups of findings, both fixed in this batch (Rule 0026: the
row is a claim, the source is the evidence).

**A. Four defects in the 10 pending rows — all confirmed against the XSD.** Each was a
silent `AR:AR-OBJECT` `S`/`T` drop (Rule 0025) or a checklist shape defect; fixed with
base-helper calls + S/T round-trip tests.

1. `ConfigReferenceValue` — `readConfigReferenceValue` / `writeConfigReferenceValue`
   dropped `S`/`T`: the R3.2.3 `REFERENCE-VALUE` complexType carries the AR-OBJECT
   attributeGroup (AUTOSAR.xsd l.20729-20739). Fix: `readARObject` / `writeARObject`
   added on the reader/writer entry points.
2. `EcucConfigurationClassEnum` — checklist lacked the `# Columns:` line and the
   `__init__` row though the class defines `__init__`. Fix: 6-column AREnum shape
   (mirrors the passing sibling `EcucConfigurationVariantEnum`).
3. `EcucScopeEnum` — same ROWS defect as (2); same fix.
4. `EcucDestinationUriDefRefType` — `getEcucDestinationUriRefs` /
   `setEcucDestinationUriRefs` dropped `S`/`T`: `<DESTINATION-URI-REF>` is a simpleContent
   extension of `AR:REF` (AUTOSAR_00052.xsd l.51614-51621) and `AR:REF` carries the
   AR-OBJECT attributeGroup (l.96344-96363). Fix: `readARObject` / `writeARObject` +
   round-trip test.

**B. Three rows marked `[x]` by the 2026-09-30 short-circuit that FAIL the current bar.**
Each is an `<<atpMixedString>>` pure-text formula carrying a legacy 5-column checklist
(rows end at `writer`, no `# Columns:` line, no per-row release token) plus a
`# Spec verified: R23-11` marker, and its reader/writer drops `S`/`T` (both complexTypes
carry the AR-OBJECT attributeGroup, AUTOSAR_00052.xsd):

- `EcucConditionFormula` (`ECUC-CONDITION-FORMULA`, l.51486-51498)
- `EcucParameterDerivationFormula` (`ECUC-PARAMETER-DERIVATION-FORMULA`, l.53258-53270)
- `EcucQueryExpression` (`ECUC-QUERY-EXPRESSION`, l.53401-53412)

Reopened and re-synced in this batch: stale marker removed at session start (Rule 0023
staleness), checklist converted to the 6-column format (Step 7), `readARObject` /
`writeARObject` added on the reader/writer entry points + S/T round-trip tests
(Steps 5/6), re-stamped only after a fresh 9b confirmation.

## Queue (dependency-first)

- [x] `ConfigReferenceValue` (input · R3.2.3 markdown · Table 3.40) — commit 7ed4c9a4a (stamped 2026-10-06, # Spec verified: R3.2.3)
  - module: M2/AUTOSARTemplates/ECUCDescriptionTemplate.py
  - note (Step 1): R3.2.3-only class — no table in R23-11 or R4.3.1 markdown;
    Table 3.40 AUTOSAR_ECU_Configuration.md l.2284 (pdf_page.py: no caption
    hit in the R3.2.3 PDF → markdown line cited per batch brief). Abstract
    Class; Package M2::AUTOSARTemplates::ECUCDescriptionTemplate; Note
    "Abstract class to be used as common parent for all reference values in
    the ECU Configuration Description."; Base ARObject (most-derived,
    matches src, ABC for the abstract guard); 1 attr: definition
    (ConfigReference, 1, ref) → `definitionRef: Optional[RefType]` per the
    kind-ref Ref suffix (module convention, EcucContainerValue precedent);
    the attr row has no table Note → XSD group CONFIG-REFERENCE-VALUE
    (AUTOSAR.xsd l.6087) DEFINITION-REF doc used verbatim (Rule 0012.2.4).
    XSD: DEFINITION-REF minOccurs=0 maxOccurs=1, DEST use="required"
    (CONFIG-REFERENCE--SUBTYPES-ENUM); Os_ECUC.arxml fixture carries
    DEFINITION-REF with NO DEST (0 hits) → DEST optional deviation is
    fixture-required. Consumed by complexTypes REFERENCE-VALUE + INSTANCE-
    REFERENCE-VALUE; Group19 sibling classes ReferenceValue /
    InstanceReferenceValue subclass it. Pre-existing state was synced and
    9b-stamped by the R3x-ECUC passes (commits 500cfd2bd..3f0dac184) — the
    `# Spec verified: R3.2.3` marker is in the file; batch mode strips the
    marker (deferred to batch confirmation). Drift found: quoted setter
    return annotation `-> "ConfigReferenceValue"` (Rule 0003).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
    - note (Step 2): tests already existed (abstract rejection / defaults /
      get-set + None no-op — legacy-level test_ECUCDescriptionTemplate.py
      TestConfigReferenceValue) and pass; added test_member_annotations
      pinning Optional[RefType] + bare-name return — seen Red 1 failed
      (`'ConfigReferenceValue' is ConfigReferenceValue`) / 3 passed.
  - [x] Step 3 — Implement model class (Green)
    - note (Step 3): field-to-spec cross-check both directions PASSES as-is —
      Base ARObject+ABC (spec abstract) with instantiation guard, single attr
      definition → `definitionRef: Optional[RefType]` PEP 526 under its
      comment, matched get/setDefinitionRef pair (None-guard, returns self),
      no fabricated fields; the attempted bare-return fix was reverted —
      bare `ConfigReferenceValue` raises NameError at class creation (self-
      reference, module has no PEP 563 and the batch brief forbids adding
      it); quoted self-return is this module's required forward-ref form and
      resolves under get_type_hints (repo Rule 0006 canonical pin). Net code
      change: none; pin test Green 4 passed.
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    - note (Step 4): all member docstrings diffed against the corpus — class
      docstring = Table 3.40 Note verbatim + ecuc_sws_3027/3028/3029 class
      requirements (md l.2289/2294/2296/2298; `\_` unescaped, extraction-
      artifact space-before-punct normalized — same convention as the
      9b-confirmed siblings in this file); attr has no table Note → XSD group
      doc l.6101 verbatim in inline comment + getter + setter, `Tags:
      xml.sequenceOffset=-10` tail kept (EcucIndexableValue stamped
      precedent), setter None-no-op sentence appended. Wipe+rewrite would be
      byte-identical — no stale wording, `__init__` has no docstring, blank
      line between attribute blocks (single attr).
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    - note (Steps 5/6): coverage already complete from the R3x-ECUC passes —
      parser test_arxml_parser_ecuc_handlers.py TestConfigReferenceValue
      (DEFINITION-REF value asserted with DEST absent / DEST present /
      missing-element None case) + writer test_writer_ecuc_values_variant.py
      TestConfigReferenceValueWrite (no-DEST emit, DEST emit, None omits the
      element); field values asserted, not lengths; the element-optional
      "empty case" is the missing/None pair. Ran both + test_os_ecuc_parser.py:
      27 passed; Os_ECUC.arxml full round-trip runs in the 9a suite. No new
      tests needed → no Red observable; nothing to fix.
  - [x] Step 6 — Update parser & writer (Green)
    - note (Steps 5/6): none needed — readConfigReferenceValue (parser
      l.13154, setDefinitionRef via getChildElementOptionalRefType) and
      writeConfigReferenceValue (writer l.12736, getDefinitionRef via
      setChildElementOptionalRefType) are matched Rule 0013.2 pairs, single
      mutator statements (no chained set/add on one receiver), DEST written
      only when present; REFERENCE-VALUE / INSTANCE-REFERENCE-VALUE concrete
      handlers call these base helpers (Rule 0013.1 leveling: ARObject base,
      no readReferrable in the path).
  - [x] Step 7 — Update checklist comment
    - note (Step 7): 6-column block rewritten — `# Spec:
      R3.2.3/AUTOSAR_ECU_Configuration.md, Table 3.40, l.2284 (R3.2.3)`
      (unverifiable `p.103 (R3.2 Rev 3)` replaced; pdf_page.py has no R3.2.3
      caption hit → markdown line per brief); `# Spec verified: R3.2.3`
      marker STRIPPED per batch mode (stamp deferred to batch confirmation);
      naming note separated (Rule 0001.5 Ref suffix — not a deviation);
      deviation rows now cite the real XSD line + fixture evidence (stale
      "Rule 0019.3" citation removed).
  - [x] Step 8 — Deviations
    - note (Step 8): two accepted deviations, mirrored inline + tracker:
      (1) definition optional — spec Mul=1 vs XSD minOccurs=0 (group
      CONFIG-REFERENCE-VALUE l.6087); (2) DEST optional — XSD use="required"
      but Os_ECUC.arxml fixture carries no DEST (lossless round-trip).
      Recorded in method_deviation_by_class.md (new ConfigReferenceValue
      section); v2 tracker is script-generated and skips marker classes —
      left to its next regen. No missing referenced classes (RefType covers
      the kind-ref target; ConfigReference is the definition-side class, not
      a field type). No placeholder remains.
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-30 (14951 passed / 0
    failed, lint clean, black clean on touched files); 9b deferred to batch confirmation
    (user instruction)
    - note (Step 9 re-verify 2026-10-04): 9a re-passed on feature/g19-batch-9b (base 42a9a0dc9) — full suite 17607 passed / 0 failed (integration round-trips incl.), ruff + flake8 + mypy (268 files) clean, black clean on touched files, set-based checklist-vs-methods PASS, member-annotation gate PASS; 9b still deferred to batch confirmation.
    - note (Step 9): set-based check passed (checklist == methods, all covered, no
      marker in batch mode); repo-wide black-check reports 8 files would-reformat that
      ALREADY fail at HEAD in other rows' modules (AdaptivePlatform + subpackage
      __init__s, StandardizationTemplate/AbstractBlueprintStructure, CommonStructure/
      Timing, SWComponentTemplate/ApplicationAttributes, ARPackage.py, SystemTemplate/
      __init__.py — outside this class's scope, left for their owning rows); this
      row's files are black-clean and the full suite + npm run lint pass.

- [x] `EcucValueCollection` (input · R23-11 markdown · Table 2.45) — commit b65b2313a (stamped 2026-10-06, # Spec verified: R23-11)
  - module: M2/AUTOSARTemplates/ECUCDescriptionTemplate.py
  - note (Step 1): Table 2.45 AUTOSAR_CP_TPS_ECUConfiguration.md l.2949
    (pdf_page.py: no caption hit → direct pypdf caption scan → PDF p.108).
    Concrete Class; Package M2::AUTOSARTemplates::ECUCDescriptionTemplate;
    Note "This represents the anchor point of the ECU configuration
    description. Tags: atp.recommendedPackage=EcucValueCollections"; Base
    most-derived = ARElement (matches src); Aggregated by
    ARPackage.element (createEcucValueCollection factory + reader dispatch
    exist). 2 attrs, displayed order: ecucValue
    (EcucModuleConfigurationValues, *, ref) → ecucValueRefs
    List[RefType] (get/add pair); ecuExtract (System, 0..1, ref) →
    ecuExtractRef Optional[RefType] (get/set pair). Not VP-capable
    (Rule 0020): atpVariation sits on a Kind=ref row (association
    pattern) and the XSD complexType declares no VARIATION-POINT. XSD
    group ECUC-VALUE-COLLECTION (AUTOSAR_00052.xsd l.53750): XML order
    ECU-EXTRACT-REF → ECUC-VALUES (wrapper of
    ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL*) — reader/writer
    already follow it. Class requirements [TPS_ECUC_02151] (l.8351) +
    [constr_3588] (l.8395) → class docstring. Drift: src unstamped, old
    4-column checklist, fields untyped, setEcuExtractRef untyped + no
    None-guard, class docstring paraphrased; writer writeARPackageElement
    dispatch has NO EcucValueCollection branch (silent drop on write) —
    the Step 5/6 fix.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
    - note (Step 2): mirrored test_ECUCDescriptionTemplate.py — replaced the
      legacy bare-string test_ecuc_value_collection with the standard set
      (initialization defaults / add chaining + None no-op / set chaining +
      None no-op / docstring verbatim / get_type_hints member pins). Seen
      Red 4 failed / 1 passed: addEcucValueRef(None) appended None,
      setEcuExtractRef(None) overwrote, class docstring paraphrased +
      member docstrings absent, annotations untyped (KeyError 'value' —
      param named `ref`).
  - [x] Step 3 — Implement model class (Green)
    - note (Step 3): field-to-spec cross-check both directions PASSES — Base
      most-derived ARElement (concrete, no instantiation guard), 2 attrs →
      dedicated typed fields `ecucValueRefs: List[RefType]` (addEcucValueRef
      None-guarded, param renamed ref→value per Rule 0003, returns self) +
      `ecuExtractRef: Optional[RefType]` (setEcuExtractRef None-guarded,
      returns self); no fabricated fields; quoted self-return is this
      module's required forward-ref form (no PEP 563; ConfigReferenceValue
      precedent). Green: module suite 112 passed.
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    - note (Step 4): old paraphrased class docstring + stale 4-column
      checklist wiped; class docstring = Table 2.45 Note verbatim (Tags
      tail kept, EcucModuleConfigurationValues stamped precedent) +
      [TPS_ECUC_02151] (md l.8351) + [constr_3588] (md l.8395) appended
      (`\_` unescaped, glyph markers + `()` stripped, space-before-punct
      normalized — ConfigReferenceValue convention). Per-attribute: inline
      `__init__` comment + getter + setter/add docstrings = spec Note
      verbatim (ecucValue keeps the full atpVariation/Stereotypes/Tags
      tail, EcucContainerValue precedent); setter/add None-no-op sentence
      appended; `__init__` has no docstring; blank line between attribute
      blocks; members PEP 526 annotated. Diffed against the corpus —
      verbatim.
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    - note (Step 5): coverage mostly pre-existing (parser
      test_arxml_parser_orchestrators test_readEcucValueCollection_full
      asserted field values; dispatch test_ecuc_value_collection;
      writer test_writer_ecuc_values_variant TestWriterEcucValueCollectio
      n{EcucValues,} full + empty-wrapper/minimal cases) — strengthened
      the parser test with ref value + DEST asserts and ADDED
      TestWriterEcucValueCollection.test_round_trip (set → save →
      reload → assert field values; release R23-11 set). Seen Red:
      NotImplementedError "Unsupported Elements of ARPackage
      <EcucValueCollection>" — save never wrote the file (5 passed,
      1 failed).
  - [x] Step 6 — Update parser & writer (Green)
    - note (Step 6): parser needed nothing (readEcucValueCollection /
      readEcucValueCollectionEcucValues are complete, XSD-ordered,
      matched Rule 0013.2 pairs, single mutator statements). WRITER FIX:
      writeARPackageElement isinstance dispatch had NO EcucValueCollection
      branch (element silently dropped / dispatch raise on save) → added
      `elif isinstance(ar_element, EcucValueCollection):
      self.writeEcucValueCollection(...)` next to the ModuleConfiguration
      branch (line ~14450). Green: parser+writer+dispatch suites 484
      passed; round-trip now asserts /System/Extract + both ref values.
  - [x] Step 7 — Update checklist comment
    - note (Step 7): 6-column block written in source order (mutator-first
      for the `*` attr: addEcucValueRef → getEcucValueRefs; getter-first
      for the 0..1 attr: getEcuExtractRef → setEcuExtractRef) — `# Spec:
      AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.45, p.108` (pdf_page.py
      no caption hit → direct pypdf caption scan); every row release
      R23-11; reader [x] on mutator/setter rows, writer [x] on getter
      rows; `# Spec verified:` marker NOT written (batch mode — deferred
      to batch confirmation); dispatch note line added (ARPackage.element
      branches both present).
  - [x] Step 8 — Deviations
    - note (Step 8): No deviations — both attrs modeled with the Kind-ref
      Ref suffix (naming per Rule 0001.5, not a deviation), RefType is the
      kind-ref target type (EcucModuleConfigurationValues / System are the
      destinations, not field types), Base most-derived ARElement, not
      VP-capable (Rule 0020: atpVariation on a Kind=ref row + no
      VARIATION-POINT in the XSD complexType). No Rule 0001.10 missing
      classes; no fixture constraints (no integration fixture carries
      ECUC-VALUE-COLLECTION). "No deviations" entry + provenance note
      appended to docs/examples/method_deviation_by_class.md; v2 tracker
      is script-generated — left to its next regen (ConfigReferenceValue
      precedent).
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-30 (14956 passed / 0
    failed, lint + black clean); 9b deferred to batch confirmation
    (user instruction)
    - note (Step 9 re-verify 2026-10-04): 9a re-passed on feature/g19-batch-9b (base 42a9a0dc9) — full suite 17607 passed / 0 failed (integration round-trips incl.), ruff + flake8 + mypy (268 files) clean, black clean on touched files, set-based checklist-vs-methods PASS, member-annotation gate PASS; 9b still deferred to batch confirmation.
    - note (Step 9): set-based check passed (checklist == methods — __init__,
      addEcucValueRef, getEcucValueRefs, getEcuExtractRef, setEcuExtractRef —
      all test-covered, no `# type:` comments, member order = displayed row
      order, mutator-first for the `*` attr); Rule 0013 chained-mutator
      greps show only pre-existing construction chains (XxxEnum().setValue
      (...) inside one mutator call — untouched regions); full suite green
      (integration round-trip incl.); black reformat applied to the
      mirrored test file, all 5 touched code files re-checked clean; no
      marker in batch mode.

- [x] `ModuleConfiguration` — ARElement — source TBC (locate table at Step 1) — commit 5cedb145b (stamped 2026-10-06, # Spec verified: R3.2.3)
  - module: M2/AUTOSARTemplates/ECUCDescriptionTemplate.py
  - note (Step 1): R3.2.3-only class — Table 3.30 AUTOSAR_ECU_Configuration.md
    l.1916 (pdf_page.py: no caption hit in the R3.2.3 PDF → markdown line
    cited per batch brief). Concrete Class; Package
    M2::AUTOSARTemplates::ECUCDescriptionTemplate; Note "Head of the
    configuration of one Module…" verbatim (incl. the spec "tthe" typo);
    Base most-derived = ARElement (matches src). 4 attrs, displayed order:
    container (Container, 1..*, aggr) → containers List[Container] +
    create/get pair; definition (ModuleDef, 1, ref) → definitionRef
    Optional[RefType] (Rule 0001.5 Ref suffix, module convention);
    implementationConfigVariant (ConfigurationVariant, 1, attr);
    moduleDescription (BswImplementation, 0..1, ref) → moduleDescriptionRef
    Optional[RefType]. Not VP-capable (Rule 0020): atpSplitable only, no
    atpVariation row, XSD group MODULE-CONFIGURATION (AUTOSAR.xsd l.16416)
    declares no VARIATION-POINT. XSD XML order DEFINITION-REF (offset -10)
    → IMPLEMENTATION-CONFIG-VARIANT → MODULE-DESCRIPTION-REF → CONTAINERS
    (wrapper of CONTAINER*) — reader/writer already follow. XSD
    DEFINITION-REF/IMPLEMENTATION-CONFIG-VARIANT minOccurs=0 vs spec Mul=1
    → Optional modeled (accepted deviation, StringValue precedent); DEST
    use="required" in XSD but Os_ECUC.arxml carries no DEST → DEST
    optional (RefType helpers round-trip DEST/BASE when present).
    Aggregated by ARPackage.element (XSD l.222) → ARPackage
    .createModuleConfiguration factory + reader/writer dispatch exist.
    Pre-existing state was synced and 9b-stamped by the R3x-ECUC passes —
    the `# Spec verified: R3.2.3` marker is in the file; batch mode strips
    the marker (deferred to batch confirmation). Drift found: container
    Note missing "Stereotypes: atpSplitable" (inline comment +
    createContainer/getContainers docstrings); `# Spec:` cites
    unverifiable "p.86 (R3.2 Rev 3)"; stale "Rule 0019.3" deviation
    citation; mirrored model tests absent (parser/writer tests exist).
    Rule 0001.10 missing member type: spec attr type ConfigurationVariant
    (R3.2.3 Table 3.11 l.1200, ECUCParameterDefTemplate pkg) is not in the
    codebase — placeholder R23-11 EcucConfigurationVariantEnum in use
    (literal sets differ: R3.2.3 adds VARIANT-POST-BUILD-LOADABLE/SELECTABLE,
    has no RECOMMENDED-CONFIGURATION) → recorded in Step 8, switch when the
    class gets its own pass. Container member type is fully synced in the
    same file (Table 3.31) — not a stub.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
    - note (Step 2): mirrored test_ECUCDescriptionTemplate.py had NO
      ModuleConfiguration tests (only the R23-11 sibling
      EcucModuleConfigurationValues) — added the standard set
      (initialization defaults / createContainer append + duplicate-returns-
      existing / get-set + None no-op x3 / docstring verbatim /
      get_type_hints member pins). Seen Red 1 failed / 9 passed: container
      docstrings lack the spec "Stereotypes: atpSplitable" tail; the 9
      structural tests pass (R3x-ECUC implementation sound).
  - [x] Step 3 — Implement model class (Green)
    - note (Step 3): field-to-spec cross-check both directions PASSES as-is —
      Base most-derived ARElement (concrete), 4 attrs → dedicated typed
      fields (`containers: List[Container]` — Container is an Identifiable
      child so createContainer(short_name) + getElement duplicate check is
      the Rule 0001.6 shape; definitionRef/moduleDescriptionRef
      Optional[RefType] per the kind-ref Ref suffix; implementationConfigVariant
      Optional[EcucConfigurationVariantEnum] placeholder, see Step 8),
      None-guarded setters returning self, mutator-first accessor order, no
      fabricated fields. Net code change: none (R3x-ECUC implementation
      already spec-shaped); structural tests Green 8 passed (the remaining
      Red is the Step 4 docstring scope).
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    - note (Step 4): all 11 member docstrings + 4 inline `__init__` comments
      re-diffed against the corpus — only the 3 container strings were
      stale (missing "Stereotypes: atpSplitable"); fixed in the inline
      comment + createContainer/getContainers docstrings (full Note cell
      verbatim incl. Tags tail, EcucValueCollection batch precedent);
      class docstring = Table 3.30 Note verbatim (multi-paragraph form,
      "tthe" spec typo preserved); setter None-no-op sentences are
      code-behavior notes; `__init__` has no docstring; blank line between
      attribute blocks; PEP 526 annotated members. Wipe+rewrite net diff =
      the 3 container strings; module suite 10 passed.
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    - note (Step 5): coverage mostly pre-existing from the R3x-ECUC passes
      (parser test_arxml_parser_ecuc_handlers.py TestModuleConfiguration —
      full read with all 4 attrs + field-value asserts incl. enum, and the
      minimal None case; writer test_writer_ecuc_values_variant.py
      TestModuleConfigurationWrite — full write in XSD order + minimal
      no-wrapper case). ADDED TestModuleConfigurationWrite.test_round_trip
      (ARPackage factory → save → reload → assert refs + DEST attrs +
      enum value + container one level down; Rule 0006 end-to-end). No
      genuine Red observable — reader/writer were already complete; the
      first run failed on this test's own expected-string typo
      (expected VARIANT-PRE-COMPLETE vs the XSD's VARIANT-PRE-COMPILE), fixed in
      the test; parser+writer+orchestrator+os-ecuc suites 556 passed.
  - [x] Step 6 — Update parser & writer (Green)
    - note (Steps 5/6): none needed — readModuleConfiguration (parser
      l.13230: readIdentifiable + setDefinitionRef /
      setImplementationConfigVariant / setModuleDescriptionRef via optional
      helpers, CONTAINERS/* iterated into createContainer + readContainer)
      and writeModuleConfiguration (writer l.12799: writeIdentifiable +
      matched getters, CONTAINERS wrapper only when non-empty) are matched
      Rule 0013.2 pairs, single mutator statements, XSD sequence order
      (DEFINITION-REF → IMPLEMENTATION-CONFIG-VARIANT →
      MODULE-DESCRIPTION-REF → CONTAINERS). ARPackage.element dispatch
      branches present both sides (parser l.14713 MODULE-CONFIGURATION →
      createModuleConfiguration + readModuleConfiguration; writer l.14448
      isinstance ModuleConfiguration → writeModuleConfiguration).
      Rule 0013 chained-mutator greps clean (see Step 9 note).
  - [x] Step 7 — Update checklist comment
    - note (Step 7): 6-column block rewritten in source order (mutator-first
      for the `*` attr: createContainer → getContainers; getter-first for
      the scalar pairs) — `# Spec:
      R3.2.3/AUTOSAR_ECU_Configuration.md, Table 3.30, l.1916 (R3.2.3)`
      (unverifiable `p.86 (R3.2 Rev 3)` replaced; pdf_page.py has no R3.2.3
      caption hit → markdown line per brief); `# Spec verified: R3.2.3`
      marker STRIPPED per batch mode (stamp deferred to batch
      confirmation); naming note separated (Rule 0001.5 Ref suffix — not a
      deviation); deviation rows renumbered with the real XSD line +
      fixture evidence (stale "Rule 0019.3" citation removed) + the NEW
      Rule 0001.10 placeholder row for the ConfigurationVariant type; test
      column claims now genuinely [x] (model tests added in Step 2).
  - [x] Step 8 — Deviations
    - note (Step 8): three accepted deviations, mirrored inline + tracker
      (docs/examples/method_deviation_by_class.md, new ModuleConfiguration
      section): (1) definition + implementationConfigVariant optional —
      spec Mul=1 vs XSD group MODULE-CONFIGURATION l.16416 minOccurs=0
      (Os_ECUC.arxml carries neither); (2) DEFINITION-REF/
      MODULE-DESCRIPTION-REF DEST optional — XSD use="required" but
      Os_ECUC.arxml carries no DEST (lossless round-trip; BASE/DEST
      round-trip when present); (3) Rule 0001.10 placeholder —
      implementationConfigVariant spec type ConfigurationVariant (R3.2.3
      Table 3.11 l.1200, ECUCParameterDefTemplate pkg) not in the codebase;
      R23-11 EcucConfigurationVariantEnum placeholder (literal sets
      differ) — class not yet implemented, switch when it gets its own
      pass (queuing it is the orchestrator's call). Naming rows are NOT
      deviations (Rule 0001.5 Ref suffix, module convention). v2 tracker is
      script-generated — left to its next regen (ConfigReferenceValue
      precedent). Container member type fully synced (Table 3.31, same
      file) — not a stub.
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-30 (14964 passed / 0
    failed, lint + black clean); 9b deferred to batch confirmation
    (user instruction)
    - note (Step 9 re-verify 2026-10-04): 9a re-passed on feature/g19-batch-9b (base 42a9a0dc9) — full suite 17607 passed / 0 failed (integration round-trips incl.), ruff + flake8 + mypy (268 files) clean, black clean on touched files, set-based checklist-vs-methods PASS, member-annotation gate PASS; 9b still deferred to batch confirmation.
    - note (Step 9): set-based check passed (checklist == methods — __init__,
      createContainer, getContainers, get/setDefinitionRef,
      get/setImplementationConfigVariant, get/setModuleDescriptionRef —
      all test-covered, no `# type:` comments, member order = displayed
      row order, mutator-first for the `*` attr); `armodel
      .ModuleConfiguration` top-level export resolves; Rule 0013
      chained-mutator greps show only pre-existing construction chains
      (XxxEnum().setValue(...) inside one mutator call — untouched
      regions); full suite green incl. the 11 integration round-trips
      (Os_ECUC.arxml carries MODULE-CONFIGURATION); black clean on all
      touched files; no marker in batch mode.

- [x] `EcucConfigurationClassEnum` (input · R23-11 markdown/PDF · Table 2.12) — commit eb890b899 (stamped 2026-10-06, # Spec verified: R23-11)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - note: deviation-tracked in method_deviation_by_class_v2.md — review entries at Step 1
  - note (Step 1): Table 2.12 AUTOSAR_CP_TPS_ECUConfiguration.pdf p.52
    (pdf_page.py caption hit). Enumeration header → AREnum (Rule 0001.1);
    Package M2::AUTOSARTemplates::ECUCParameterDefTemplate; Note "Possible
    configuration classes for the AUTOSAR configuration parameters.";
    Aggregated by EcucAbstractConfigurationClass.configClass (consumer class
    stamped R23-11; parser l.11517 / writer l.10436 cover CONFIG-CLASS).
    The markdown block at l.1356 is page-split-garbled: its
    Enumeration/Note/Aggregated-by header rows and the "Preconfigured
    Configuration" literal belong to Table 2.13 EcucConfigurationVariantEnum
    (XSD mmt.qualifiedName EcucConfigurationVariantEnum
    .PreconfiguredConfiguration proves it) — rows taken from the PDF page
    text, cross-checked against ECUC-CONFIGURATION-CLASS-ENUM
    (AUTOSAR_00052.xsd l.135895; 4 literals, none atp.Status=removed).
    4 literals in displayed order: Link(0), PostBuild(1), PreCompile(2),
    PublishedInformation(3). Drift found (Rule 0011): member values carry
    the XSD-uppercase wire forms (LINK/POST-BUILD/PRE-COMPILE/
    PUBLISHED-INFORMATION) instead of the spec literals → fix in Step 3
    (FlexrayNmScheduleVariant batch precedent: values from the PDF Literal
    column, e.g. "scheduleVariant1"). Class docstring + all 4 literal
    comments already verbatim; no Rule 0001.10 missing types (enum has no
    member types).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
    - note (Step 2): extended TestEcucConfigurationClassEnum in the mirrored
      test_ECUCParameterDefTemplate.py with the enum set — instantiation /
      literal order via getEnumValues (displayed row order) /
      Enum().setValue(Enum.MEMBER) + getValue round-trip + validateEnumValue /
      class docstring + 4 literal comments verbatim (inspect.getsource,
      cleandoc for the 3.13 dedent trap). Seen Red 1 failed / 3 passed —
      test_configuration_class_literals asserts the Rule 0011 literal values
      ("Link"/"PostBuild"/"PreCompile"/"PublishedInformation") against the
      XSD-uppercase drift.
  - [x] Step 3 — Implement model class (Green)
    - note (Step 3): field-to-spec cross-check both directions PASSES after
      the Rule 0011 value fix — 4 literals 1:1 with the Table 2.12 rows, no
      extra/missing member, member names = literal UPPER_CASE (LINK,
      POST_BUILD, PRE_COMPILE, PUBLISHED_INFORMATION), values now exactly the
      spec literals ("Link"/"PostBuild"/"PreCompile"/"PublishedInformation";
      XSD-uppercase wire forms belong to XML fixtures only per Rule 0011),
      `__init__` passes them to AREnum in displayed order so `Enum()` is
      instantiable; Base AREnum (Enumeration header, Rule 0001.1/0010);
      no fabricated members; `armodel.EcucConfigurationClassEnum` top-level
      export resolves. Green: module suite 94 passed.
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    - note (Step 4): diffed every string against the PDF Table 2.12 Note +
      literal descriptions (markdown garbled — PDF page text is the
      authority, XSD 00052 docs agree verbatim): class docstring
      "Possible configuration classes for the AUTOSAR configuration
      parameters." already verbatim; all 4 literal comments verbatim incl.
      the Tags tails; the enum has no method docstrings and `__init__` has
      none (enum pattern). Wipe+rewrite would be byte-identical — no stale
      wording survived (the class was never docstring-synced before this
      pass; nothing pre-wipe remains).
  - [x] Step 5 — Write reader/writer round-trip test (Red) (N/A: standalone enum — no own XML element; serialized as an attribute value on consuming classes, EcucAbstractConfigurationClass.configClass round-trips there)
  - [x] Step 6 — Update parser & writer (Green) (N/A: standalone enum — parser readEcucAbstractConfigurationClass l.11517 / writer writeEcucAbstractConfigurationClass l.10436 already cover CONFIG-CLASS via getChild/setChildElementOptionalLiteral; no parser/writer change)
  - [x] Step 7 — Update checklist comment
    - note (Step 7): checklist already in the final batch-mode enum shape —
      `# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.12, p.52`
      (pdf_page.py caption hit confirms p.52) + `# (no methods)` (the
      skill's AREnum form; reader/writer coverage is the enum value form);
      `# Spec verified:` marker NOT written (batch mode — deferred to batch
      confirmation). No edit needed.
  - [x] Step 8 — Deviations
    - note (Step 8): No deviations — the Rule 0011 member-value fix is a
      to-fix completed in this pass (drift, not a deviation row). "No
      deviations" entry + provenance note appended to
      docs/examples/method_deviation_by_class.md (new
      EcucConfigurationClassEnum section): markdown garble resolved via PDF
      p.52 + XSD l.135895; no fixture carries CONFIG-CLASS (no Rule 0019
      case); reconciliation item recorded for the stamped sibling
      EcucConfigurationVariantEnum (XSD-uppercase values, out of row
      scope); the stale v2-tracker appendix classification ("classes
      without a spec attribute table") left to the script's next regen
      (batch precedent). No Rule 0001.10 missing referenced classes (enum
      references no model type).
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-30 (14967 passed / 0
    failed, lint + black clean); 9b deferred to batch confirmation
    (user instruction)
    - note (Step 9 re-verify 2026-10-04): 9a re-passed on feature/g19-batch-9b (base 42a9a0dc9) — full suite 17607 passed / 0 failed (integration round-trips incl.), ruff + flake8 + mypy (268 files) clean, black clean on touched files, set-based checklist-vs-methods PASS, member-annotation gate PASS; 9b still deferred to batch confirmation.
    - note (Step 9): set-based enum check passed (`# (no methods)` form,
      class body defines only `__init__`, no stale method rows, no `# type:`
      comments); the subdirectory legacy tests
      (ECUCParameterDefTemplate/test_ECUCParameterDefTemplate.py) that pinned
      the old XSD-uppercase values were updated to the Table 2.12 Literal
      values in this pass; full suite 14967 passed / 0 failed (integration
      round-trips incl.); npm run lint clean; black clean on all touched
      files; no marker in batch mode.

- [x] `EcucScopeEnum` (input · R23-11 markdown · Table 2.7) — commit 096c9544f (stamped 2026-10-06, # Spec verified: R23-11)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - note: deviation-tracked in method_deviation_by_class_v2.md — review entries at Step 1
  - note (Step 1): Table 2.7 AUTOSAR_CP_TPS_ECUConfiguration.md l.1163
    (complete, not page-split; pdf_page.py: PDF p.46 caption hit).
    Enumeration header → AREnum (Rule 0001.1); Package
    M2::AUTOSARTemplates::ECUCParameterDefTemplate; Note "Possible scope
    settings for a configuration element."; Aggregated by
    EcucDefinitionElement.scope (consumer class stamped R23-11; parser
    l.11509 / writer l.10425 cover SCOPE via getChild/
    setChildElementOptionalLiteral). 2 literals in displayed order: ECU(0)
    "An element may be shared with other modules.", local(1) "An element is
    only be applicable for the module it is defined in." (spec grammar
    quirk preserved). XSD ECUC-SCOPE-ENUM (AUTOSAR_00052.xsd l.136032/
    l.136044) corroborates: values ECU/LOCAL, mmt.qualifiedName tails
    EcucScopeEnum.ECU / EcucScopeEnum.local, none atp.Status=removed.
    Drift found (Rule 0011): LOCAL carries the XSD-uppercase wire form
    "LOCAL" instead of the spec literal "local" → fix in Step 3
    (FlexrayNmScheduleVariant batch precedent; ECU is unchanged — the
    literal is uppercase in the table itself). Class docstring + both
    literal comments already verbatim. constr_3509 (scope prohibited on
    EcucModuleDef/EcucContainerDef subclasses) is consumer-class content,
    not enum content. No Rule 0001.10 missing types; no integration fixture
    carries SCOPE.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
    - note (Step 2): extended TestEcucScopeEnum in the mirrored
      test_ECUCParameterDefTemplate.py with the enum set — instantiation /
      literal order via getEnumValues (displayed row order) /
      Enum().setValue(Enum.MEMBER) + getValue round-trip + validateEnumValue /
      class docstring + both literal comments verbatim (inspect.getsource,
      cleandoc for the 3.13 dedent trap). Seen Red 1 failed / 3 passed —
      test_scope_literals asserts the Rule 0011 literal values
      ("ECU"/"local") against the XSD-uppercase drift on LOCAL.
  - [x] Step 3 — Implement model class (Green)
    - note (Step 3): field-to-spec cross-check both directions PASSES after
      the Rule 0011 value fix — 2 literals 1:1 with the Table 2.7 rows, no
      extra/missing member, member names = literal UPPER_CASE (ECU, LOCAL),
      values now exactly the spec literals ("ECU"/"local"; the XSD
      uppercase wire form "LOCAL" belongs to XML fixtures only per Rule
      0011), `__init__` passes them to AREnum in displayed order so `Enum()`
      is instantiable; Base AREnum (Enumeration header, Rule 0001.1/0010);
      no fabricated members; `armodel.EcucScopeEnum` top-level export
      resolves. Green: module suite 97 passed.
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    - note (Step 4): diffed every string against the Table 2.7 markdown
      (complete, not garbled; PDF p.46 + XSD 00052 docs agree verbatim):
      class docstring "Possible scope settings for a configuration
      element." already verbatim; both literal comments verbatim incl. the
      Tags tails and the spec grammar quirk ("is only be applicable"); the
      enum has no method docstrings and `__init__` has none (enum
      pattern). Wipe+rewrite would be byte-identical — no stale wording
      survived.
  - [x] Step 5 — Write reader/writer round-trip test (Red) (N/A: standalone enum — no own XML element; serialized as an attribute value on consuming classes, EcucDefinitionElement.scope round-trips there)
  - [x] Step 6 — Update parser & writer (Green) (N/A: standalone enum — parser readEcucDefinitionElement l.11509 / writer writeEcucDefinitionElement l.10425 already cover SCOPE via getChild/setChildElementOptionalLiteral; no parser/writer change)
  - [x] Step 7 — Update checklist comment
    - note (Step 7): checklist already in the final batch-mode enum shape —
      `# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.7, p.46`
      (pdf_page.py caption hit confirms p.46) + `# (no methods)` (the
      skill's AREnum form; reader/writer coverage is the enum value form);
      `# Spec verified:` marker NOT written (batch mode — deferred to batch
      confirmation). No edit needed.
  - [x] Step 8 — Deviations
    - note (Step 8): No deviations — the Rule 0011 member-value fix is a
      to-fix completed in this pass (drift, not a deviation row). "No
      deviations" entry + provenance note appended to
      docs/examples/method_deviation_by_class.md (new EcucScopeEnum
      section); the stale v2-tracker appendix classification ("classes
      without a spec attribute table") left to the script's next regen
      (batch precedent). No Rule 0001.10 missing referenced classes (enum
      references no model type); no integration fixture carries SCOPE (no
      Rule 0019 case).
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-30 (14970 passed / 0
    failed, lint + black clean); 9b deferred to batch confirmation
    (user instruction)
    - note (Step 9 re-verify 2026-10-04): 9a re-passed on feature/g19-batch-9b (base 42a9a0dc9) — full suite 17607 passed / 0 failed (integration round-trips incl.), ruff + flake8 + mypy (268 files) clean, black clean on touched files, set-based checklist-vs-methods PASS, member-annotation gate PASS; 9b still deferred to batch confirmation.
    - note (Step 9): set-based enum check passed (`# (no methods)` form,
      class body defines only `__init__`, no stale method rows, no `# type:`
      comments); the subdirectory legacy tests
      (ECUCParameterDefTemplate/test_ECUCParameterDefTemplate.py) that
      pinned the old XSD-uppercase "LOCAL" value were updated to the
      Table 2.7 Literal values in this pass; full suite 14970 passed /
      0 failed (integration round-trips incl.); npm run lint clean; black
      clean on all touched files; no marker in batch mode.

- [x] `EcucDestinationUriDefRefType` — RefType — XSD-only (resolved at Step 1; no own table in any corpus) — commit 7047c575f (stamped 2026-10-06, # XSD verified: AUTOSAR_00052.xsd)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - note: deviation-tracked in method_deviation_by_class_v2.md — review entries at Step 1
  - note (Step 1): XSD-only class — no PDF/markdown table in R23-11 or R4.3.1 markdown;
    the model-side type of the anonymous DESTINATION-URI-REF nested complexType
    (AUTOSAR_00052.xsd l.51614: simpleContent extension of AR:REF + DEST attr
    use="required" of ECUC-DESTINATION-URI-DEF--SUBTYPES-ENUM) inside the
    DESTINATION-URI-REFS wrapper of group ECUC-CONTAINER-DEF
    (mmt.qualifiedName EcucContainerDef.destinationUri, 0..*). Concrete
    complexType → RefType subclass (same shape as the sibling TRefType);
    ZERO own attributes — element content + BASE/DEST attribs live on the
    inherited RefType value/base/dest. Retire-or-keep arbitration RESOLVED to
    keep: the class is required for the DEST-typed isinstance dispatch in
    parser getEcucDestinationUriRefs (l.12948) / writer setEcucDestinationUriRefs
    (l.11283) — retiring it would untype the EcucContainerDef.destinationUriRefs
    round-trip. Provenance form: `# XSD verified: AUTOSAR_00052.xsd`
    (written at 9b batch confirmation — batch mode). Drift found: fabricated
    pre-sync docstring + legacy 4-column checklist.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
    - note (Step 2): extended TestEcucDestinationUriDefRefType in the mirrored
      test_ECUCParameterDefTemplate.py — added test_inheritance (isinstance
      RefType pin), test_inherited_accessors_roundtrip (setValue/setBase/
      setDest round-trip + None defaults — the inherited members carry the
      nested type's content + attribs), test_class_docstring (XSD-evidence
      pin) + test_init_has_no_docstring. Seen Red 1 failed / 4 passed — the
      docstring pin failed on the fabricated pre-sync docstring.
  - [x] Step 3 — Implement model class (Green)
    - note (Step 3): field-to-spec cross-check both directions PASSES as-is —
      the nested complexType contributes no own attribute (DEST maps to the
      inherited RefType.dest; base AR:REF → RefType base, src matches), zero
      own fields declared (no fabrication, no flattening), `__init__` calls
      super() only. Net code change: none; structural tests Green 4 passed
      (the remaining Red is the Step 4 docstring scope).
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    - note (Step 4): wiped the fabricated class docstring, rewrote from the
      XSD evidence (single-line form — the pin compares raw `__doc__`):
      names the DESTINATION-URI-REF nested complexType, its AR:REF extension
      base + required DEST attribute, the DESTINATION-URI-REFS wrapper and
      the EcucContainerDef.destinationUri aggregation (PModeInSystemInstanceRef
      hand-written-XSD-evidence convention; the nested element carries no
      xsd:documentation of its own, so no spec Note exists to copy verbatim).
      `__init__` has no docstring (nothing else to wipe). Green: mirrored
      module 240 passed.
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    - note (Steps 5/6): ADDED parser test_arxml_parser_ecuc_handlers.py
      TestEcucContainerDefDestinationUriRefs (full read of 2 DESTINATION-URI-REF
      via readEcucContainerDef with value/DEST/BASE asserts + absent-wrapper
      empty case) + writer test_writer_ecuc_def.py TestWriterEcucDestinationUriRefs
      (emit with DEST/BASE attribs + text, omits-when-empty, save→reload
      round-trip through EcucParamConfContainerDef asserting
      isinstance EcucDestinationUriDefRefType + all field values). No Red
      observable — getEcucDestinationUriRefs/setEcucDestinationUriRefs
      pre-existed and pass; the tests are the lossless end-to-end proof.
      5 passed.
  - [x] Step 6 — Update parser & writer (Green) (no change needed — parser
    getEcucDestinationUriRefs l.12948 (BASE/DEST attribs + text into the
    constructed EcucDestinationUriDefRefType, notImplemented guard for foreign
    tags) and writer setEcucDestinationUriRefs l.11283 (DESTINATION-URI-REFS
    wrapper only when non-empty, isinstance dispatch, attribs written when
    present) are matched Rule 0013.2 pairs, single mutator statements, called
    from readEcucContainerDef l.12934 / writeEcucContainerDef in XSD group
    order; no receiver chains added)
  - [x] Step 7 — Update checklist comment
    - note (Step 7): checklist rebuilt to the final batch-mode 6-column
      XSD-only shape — `# Spec: R23-11/AUTOSAR_00052.xsd, DESTINATION-URI-REF
      nested type (group ECUC-CONTAINER-DEF), line 51614 (XSD-only; no own
      table in repo corpus)`; single `__init__` row [x] impl/docstring/test
      with `[—]` reader/writer (no own accessors — the element round-trips via
      the consuming class EcucContainerDef.destinationUriRefs helpers, note
      line added); `# XSD verified:` marker NOT written (batch mode — deferred
      to batch confirmation).
  - [x] Step 8 — Deviations
    - note (Step 8): ONE accepted deviation, mirrored inline + tracker
      (docs/examples/method_deviation_by_class.md, new EcucDestinationUriDefRefType
      section): DEST optional in the model (inherited `RefType.dest:
      Optional[str]`) vs XSD use="required" on the nested type — per-subclass
      attribute requiredness cannot be expressed on the shared RefType base;
      no integration fixture carries DESTINATION-URI-REF (no Rule 0019 case).
      Retire-or-keep arbitration resolution recorded (keep — see Step 1).
      No Rule 0001.10 missing referenced classes (RefType is the stamped base;
      EcucDestinationUriDef Table 2.35 p.82 is the destination-side class,
      stamped separately). v2 tracker lists the class only in its generated
      "classes without a spec attribute table" appendix — left to the script's
      next regen.
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a runs in the batch verification
    pass (2026-10-04); 9b deferred to batch confirmation (user instruction)
    - note (Step 9 re-verify 2026-10-04): 9a re-passed on feature/g19-batch-9b (base 42a9a0dc9) — full suite 17607 passed / 0 failed (integration round-trips incl.), ruff + flake8 + mypy (268 files) clean, black clean on touched files, set-based checklist-vs-methods PASS (single __init__ row), member-annotation gate PASS; 9b still deferred to batch confirmation.

- [x] `EcucBooleanParamDef` — EcucParameterDef — R23-11 markdown · Table 2.15 — commit b40b99238 (stamped 2026-10-06, # Spec verified: R23-11)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - note (Step 1): Table 2.15 AUTOSAR_CP_TPS_ECUConfiguration.md l.1495
    (complete, not page-split; pdf_page.py: PDF p.58 caption hit). Concrete
    Class; Package M2::AUTOSARTemplates::ECUCParameterDefTemplate; Note
    "Configuration parameter type for Boolean. Allowed values are true and
    false." (class docstring already verbatim); Base chain
    ARObject/AtpDefinition/EcucCommonAttributes/EcucDefinitionElement/
    EcucParameterDef/Identifiable/MultilanguageReferrable/Referrable →
    most-derived base EcucParameterDef (stamped R23-11, Table 2.14 p.57,
    same file) — src matches, no flattening. Aggregated by
    EcucDestinationUriPolicy.parameter + EcucParamConfContainerDef.parameter
    (both consumers already dispatch createEcucBooleanParamDef; parser
    readEcucBooleanParamDef l.11769 / writer writeEcucBooleanParamDef
    l.10554 cover DEFAULT-VALUE via getChild/setChildElementOptionalBoolean
    Value; XSD group ECUC-BOOLEAN-PARAM-DEF (AUTOSAR_00052.xsd l.51216):
    DEFAULT-VALUE minOccurs=0 maxOccurs=1, no VARIANTS wrapper → flat
    optional element is correct). 1 attr in displayed order: defaultValue
    (Boolean, 0..1, attr). Drift found (Rule 0001.4): field/getter/setter
    carry bare `Boolean` annotations (0..1 → Optional[Boolean]); setter
    lacks the chaining return annotation; Note comment + getter/setter
    docstrings missing (Step 4). Not VP-capable (Rule 0020 — Kind=attr
    atpVariation row; no VARIATION-POINT in the XSD complexType). No Rule
    0001.10 missing types (Boolean is a stamped PrimitiveTypes class).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
    - note (Step 2): extended TestEcucBooleanParamDef in the mirrored
      ECUCParameterDefTemplate/test_ECUCParameterDefTemplate.py — added
      test_set_default_value_none_no_op (Rule 0004 None no-op, typed
      Boolean primitive) + test_member_annotations (get_type_hints pin:
      getter return / setter value == Optional[Boolean], setter return is
      EcucBooleanParamDef — quoted self-return, this module's forward-ref
      form, no PEP 563). Seen Red 1 failed / 3 passed — the pin failed on
      the pre-sync bare `Boolean` return annotation.
  - [x] Step 3 — Implement model class (Green)
    - note (Step 3): field-to-spec cross-check both directions PASSES after
      the Rule 0001.4 annotation fix — 1 attr (defaultValue, Boolean,
      0..1) 1:1 with Table 2.15, field/getter/setter now Optional[Boolean]
      with chaining `-> "EcucBooleanParamDef"` setter, None-guard kept; no
      fabricated/ flattened members (inherited derivation/symbolicNameValue/
      withAuto live on the stamped base EcucParameterDef, Table 2.14); no
      Rule 0001.10 missing types. Green: TestEcucBooleanParamDef 4 passed.
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    - note (Step 4): pre-sync body carried NO member docstrings/comments
      (nothing stale to wipe — confirmed by diffing the class body against
      the pre-edit state); class docstring already verbatim (Table 2.15
      Note). Wrote fresh: inline `__init__` comment + getter docstring +
      setter docstring, all = "Default value of the boolean configuration
      parameter. atpVariation: [RS_ECUC_00083] Stereotypes: atpVariation
      Tags: vh.latestBindingTime=codeGenerationTime" verbatim (module
      convention keeps the Stereotypes/Tags tails — EcucEnumerationParamDef
      stamped precedent); setter appended the None-no-op sentence;
      `__init__` has no docstring; blank line between attribute blocks
      (single attr).
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    - note (Steps 5/6): reader/writer coverage pre-existed complete — parser
      test_arxml_parser_ecuc_handlers.py TestEcucContainerDefParameters
      (DEFAULT-VALUE value asserted via getValue() is True / missing-element
      None pair) + writer test_writer_ecuc_def.py TestWriterEcucBoolean
      ParamDef (DEFAULT-VALUE "true" emit, None omits the element); XSD has
      no VARIANTS wrapper for this class → the missing-element pair is the
      "empty case". Added test_round_trip_default_value (set → save →
      reload → assert getValue() is True, field values not lengths) — no Red
      observable (both sides pre-existed and pass; the test is the lossless
      end-to-end proof). Ran both files: 226 passed.
  - [x] Step 6 — Update parser & writer (Green) (no change needed — readEcucBooleanParamDef l.11769 / writeEcucBooleanParamDef l.10554 already form the matched name pair (Rule 0013.2) over the spec-typed getChild/setChildElementOptionalBooleanValue helpers; XML order DEFAULT-VALUE matches the XSD group sequence; no receiver chains added)
  - [x] Step 7 — Update checklist comment
    - note (Step 7): checklist rewritten to the final batch-mode shape —
      `# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.15, p.58`
      (pdf_page.py caption hit confirms p.58) + the `# Columns:` header +
      per-row `R23-11` release column (the pre-sync rows had no Columns
      line/release); `# Spec verified:` marker NOT written (batch mode —
      deferred to batch confirmation). Set-based check passed: checklist ==
      {__init__, getDefaultValue, setDefaultValue}, all covered in the
      mirrored test.
  - [x] Step 8 — Deviations
    - note (Step 8): No deviations — the bare-`Boolean` annotations and
      missing chaining return were Rule 0001.4/0003 to-fix drift, completed
      in this pass (not deviation rows). "No deviations" entry + provenance
      note appended to docs/examples/method_deviation_by_class.md (new
      EcucBooleanParamDef section). No Rule 0001.10 missing referenced
      classes; no integration fixture carries elements beyond DEFAULT-VALUE
      (no Rule 0019 combine case).
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-30 (14973 passed /
    0 failed, lint + black clean); 9b deferred to batch confirmation
    (user instruction)
    - note (Step 9 re-verify 2026-10-04): 9a re-passed on feature/g19-batch-9b (base 42a9a0dc9) — full suite 17607 passed / 0 failed (integration round-trips incl.), ruff + flake8 + mypy (268 files) clean, black clean on touched files, set-based checklist-vs-methods PASS, member-annotation gate PASS; 9b still deferred to batch confirmation.
    - note (Step 9): set-based check passed; `# type:` grep clean on the
      class body; blank line between attribute blocks verified by eye
      (single attr); full suite 14973 passed / 0 failed (integration
      round-trips incl.); npm run lint clean; black clean on all touched
      files; no marker in batch mode.

- [x] `EcucFloatParamDef` — EcucParameterDef — R23-11 markdown · Table 2.17 — commit 454e47206 (stamped 2026-10-06, # Spec verified: R23-11)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - note (Step 1): Table 2.17 AUTOSAR_CP_TPS_ECUConfiguration.md — PAGE-
    SPLIT render: body rows (Class/Package/Note/Base/Aggregated-by/
    Attribute header + defaultValue + max) sit at l.1589-1599 BEFORE the
    caption "Table 2.17: EcucFloatParamDef" at l.1609, min row follows the
    caption at l.1611 → displayed row order = defaultValue, max, min
    (concatenation of per-page row groups, Rule 0001.11); pdf_page.py:
    PDF p.62 caption hit (cite the header-row page). Concrete Class;
    Package M2::AUTOSARTemplates::ECUCParameterDefTemplate; Note
    "Configuration parameter type for Float." (class docstring already
    verbatim); Base chain → most-derived base EcucParameterDef (stamped
    R23-11, Table 2.14 p.57, same file) — src matches, no flattening.
    Aggregated by EcucDestinationUriPolicy.parameter +
    EcucParamConfContainerDef.parameter (both consumers already dispatch
    createEcucFloatParamDef; parser readEcucFloatParamDef l.11804 / writer
    writeEcucFloatParamDef l.10583 cover DEFAULT-VALUE/MAX/MIN via getChild/
    setChildElementOptionalFloatValue + getChild/setChildLimitElement; XSD
    group ECUC-FLOAT-PARAM-DEF (AUTOSAR_00052.xsd l.52244, complexType
    l.52278): sequence DEFAULT-VALUE, MAX (AR:LIMIT), MIN (AR:LIMIT) all
    minOccurs=0 maxOccurs=1, no VARIANTS wrapper → flat optional elements
    are correct). 3 attrs in displayed order: defaultValue (Float, 0..1),
    max (Limit, 0..1), min (Limit, 0..1) — class field order already
    matches. Drift found (Rule 0001.4): all three field/getter/setter sets
    carry bare `Float`/`Limit` annotations (0..1 → Optional[...]); setters
    lack the chaining return annotation; Note comments + getter/setter
    docstrings missing (Step 4). Not VP-capable (Rule 0020 — Kind=attr
    atpVariation rows; no VARIATION-POINT in the XSD complexType). No Rule
    0001.10 missing types (Float/Limit are stamped PrimitiveTypes classes).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
    - note (Step 2): extended TestEcucFloatParamDef in the mirrored
      ECUCParameterDefTemplate/test_ECUCParameterDefTemplate.py — added
      test_set_default_value_none_no_op (Rule 0004 None no-op, typed Float
      primitive), test_setter_returns_self (chaining on all three setters,
      typed Float/Limit primitives) + test_member_annotations (get_type_
      hints pins: get/setDefaultValue == Optional[Float], get/setMax and
      get/setMin == Optional[Limit], setter returns is EcucFloatParamDef —
      quoted self-return, this module's forward-ref form, no PEP 563).
      Seen Red 1 failed / 8 passed — the pin failed on the pre-sync bare
      `Float` return annotation.
  - [x] Step 3 — Implement model class (Green)
    - note (Step 3): field-to-spec cross-check both directions PASSES after
      the Rule 0001.4 annotation fix — 3 attrs (defaultValue Float, max
      Limit, min Limit; all 0..1) 1:1 with Table 2.17 in displayed order
      (defaultValue, max, min), field/getter/setter now Optional[...] with
      chaining `-> "EcucFloatParamDef"` setters, None-guards kept, blank
      line between every attribute block; no fabricated/flattened members
      (inherited derivation/symbolicNameValue/withAuto live on the stamped
      base EcucParameterDef, Table 2.14); no Rule 0001.10 missing types.
      Green: TestEcucFloatParamDef 9 passed.
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    - note (Step 4): pre-sync body carried NO member docstrings/comments
      (nothing stale to wipe — confirmed by diffing the class body against
      the pre-edit state); class docstring already verbatim (Table 2.17
      Note). Wrote fresh for all three attrs in displayed order (default-
      Value, max, min): inline `__init__` comments + getter docstrings +
      setter docstrings, all = the Table 2.17 row Note verbatim ("Default
      value of the float configuration parameter." / "Max value allowed for
      the parameter defined." / "Min value allowed for the parameter
      defined.", each with its `atpVariation: [RS_ECUC_0008x] Stereotypes:
      atpVariation Tags: vh.latestBindingTime=codeGenerationTime` tail kept
      verbatim per the stamped module precedent); setters appended the
      None-no-op sentences; `__init__` has no docstring; blank line between
      every attribute block.
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    - note (Steps 5/6): reader/writer coverage pre-existed complete — parser
      test_arxml_parser_ecuc_handlers.py (DEFAULT-VALUE + MAX/MIN with
      INTERVAL-TYPE read, missing-element None pair) + writer test_writer_
      ecuc_def.py TestWriterEcucFloatParamDef (DEFAULT-VALUE/MAX/MIN emit
      with INTERVAL-TYPE attrib, None omits the element); XSD has no
      VARIANTS wrapper for this class → the missing-element pair is the
      "empty case". Added test_round_trip_default_and_limits (set → save →
      reload → assert Float value 1.5 + Limit values "99.5"/"0.0" with
      CLOSED/OPEN interval types, field values not lengths) — no Red
      observable (both sides pre-existed and pass; the test is the lossless
      end-to-end proof). Ran writer+parser+model Float: 236 passed.
  - [x] Step 6 — Update parser & writer (Green) (no change needed — readEcucFloatParamDef l.11804 / writeEcucFloatParamDef l.10583 already form the matched name pair (Rule 0013.2) over the spec-typed getChild/setChildElementOptionalFloatValue + getChild/setChildLimitElement helpers; XML order DEFAULT-VALUE, MAX, MIN matches the XSD group sequence l.52244; no receiver chains added)
  - [x] Step 7 — Update checklist comment
    - note (Step 7): checklist rewritten to the final batch-mode shape —
      `# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.17, p.62`
      (pdf_page.py caption hit confirms p.62; header-row page cited for the
      page-split table) + the `# Columns:` header + per-row `R23-11`
      release column (the pre-sync rows had no Columns line/release); rows
      in source order = displayed row order (defaultValue/max/min, getter
      first per scalar attr); `# Spec verified:` marker NOT written (batch
      mode — deferred to batch confirmation). Set-based check passed:
      checklist == {__init__, get/setDefaultValue, get/setMax, get/setMin},
      all covered in the mirrored test.
  - [x] Step 8 — Deviations
    - note (Step 8): No deviations — the bare-`Float`/`Limit` annotations
      and missing chaining returns were Rule 0001.4/0003 to-fix drift,
      completed in this pass (not deviation rows). "No deviations" entry +
      provenance note appended to docs/examples/method_deviation_by_class.md
      (new EcucFloatParamDef section; records the page-split render and the
      displayed-row-order finding). No Rule 0001.10 missing referenced
      classes; no Rule 0019 combine case (no fixture carries anything
      beyond DEFAULT-VALUE/MAX/MIN).
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-30 (14977 passed /
    0 failed, lint + black clean); 9b deferred to batch confirmation
    (user instruction)
    - note (Step 9 re-verify 2026-10-04): 9a re-passed on feature/g19-batch-9b (base 42a9a0dc9) — full suite 17607 passed / 0 failed (integration round-trips incl.), ruff + flake8 + mypy (268 files) clean, black clean on touched files, set-based checklist-vs-methods PASS, member-annotation gate PASS; 9b still deferred to batch confirmation.
    - note (Step 9): set-based check passed; `# type:` grep clean on the
      class body; blank line between every attribute block verified by eye
      (three blocks, spec row order); full suite 14977 passed / 0 failed
      (integration round-trips incl.); npm run lint clean; black clean on
      all touched files; no marker in batch mode.

- [x] `EcucForeignReferenceDef` — EcucAbstractExternalReferenceDef — R23-11 markdown · Table 2.31 — commit 958007001 (stamped 2026-10-06, # Spec verified: R23-11)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - note (Step 1): Table 2.31 AUTOSAR_CP_TPS_ECUConfiguration.md l.2009-2016
    (caption l.2007; pdf_page.py: PDF p.75 caption hit). Concrete Class;
    Package M2::AUTOSARTemplates::ECUCParameterDefTemplate; Note "Specify a
    reference to an XML description of an entity described in another
    AUTOSAR template."; Base chain ARObject/AtpDefinition/
    EcucAbstractExternalReferenceDef/EcucAbstractReferenceDef/
    EcucCommonAttributes/EcucDefinitionElement/Identifiable/
    MultilanguageReferrable/Referrable → most-derived base
    EcucAbstractExternalReferenceDef (stamped R23-11, Table 2.28 p.72, same
    file) — src matches, no flattening. Aggregated by
    EcucDestinationUriPolicy.reference + EcucParamConfContainerDef.reference.
    1 attr: destinationType (String, 0..1, attr). XSD group
    ECUC-FOREIGN-REFERENCE-DEF (AUTOSAR_00052.xsd l.52299, complexType
    l.52315): DESTINATION-TYPE minOccurs=0 maxOccurs=1, NO VARIANTS wrapper,
    no VARIATION-POINT → flat optional element, last in the base-group
    sequence; not VP-capable (Rule 0020). Class requirements
    [TPS_ECUC_02041] (l.2005) + [TPS_ECUC_02042] (l.2018) + [TPS_ECUC_06088]
    (l.2024) → class docstring. Drift found (Rule 0001.4): field/getter/
    setter carry bare `String` annotations (0..1 → Optional[String]);
    getter/setter docstrings are "Gets/Sets the..." paraphrases; class
    docstring reflowed. Reader/writer: NO coverage at all — no
    readEcucForeignReferenceDef/writeEcucForeignReferenceDef helpers, no
    dispatch branch in any of the 4 aggregation sites, no
    createEcucForeignReferenceDef factory on EcucParamConfContainerDef →
    elements silently dropped on round-trip (the Steps 5/6 fix). No Rule
    0001.10 missing types (String is a stamped PrimitiveTypes class); no
    integration fixture carries ECUC-FOREIGN-REFERENCE-DEF (no Rule 0019
    case).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
    - note (Step 2): extended TestEcucForeignReferenceDef in the mirrored
      ECUCParameterDefTemplate/test_ECUCParameterDefTemplate.py — added
      test_set_destination_type_none_no_op (Rule 0004 None no-op, typed
      String primitive), test_setter_returns_self (chaining) +
      test_member_annotations (get_type_hints pins: get/setDestinationType
      == Optional[String], setter return is EcucForeignReferenceDef —
      quoted self-return, this module's forward-ref form, no PEP 563) +
      test_docstrings_verbatim (class + getter + setter, Table 2.31 Notes).
      Seen Red 2 failed / 4 passed — the pin failed on the pre-sync bare
      `String` return annotation; the verbatim test failed on the reflowed
      class docstring (and would fail the paraphrased getter/setter).
  - [x] Step 3 — Implement model class (Green)
    - note (Step 3): field-to-spec cross-check both directions PASSES after
      the Rule 0001.4 annotation fix — 1 attr (destinationType, String,
      0..1) 1:1 with Table 2.31, field/getter/setter now Optional[String]
      with chaining `-> "EcucForeignReferenceDef"` setter, None-guard kept;
      Base most-derived EcucAbstractExternalReferenceDef (stamped R23-11,
      Table 2.28) — no flattening (inherited withAuto lives there); no
      fabricated fields; no Rule 0001.10 missing types. Green: annotations
      Green 5 passed (the remaining Red is the Step 4 docstring scope).
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    - note (Step 4): wiped the class docstring + getter/setter docstrings
      and rewrote fresh — class docstring = Table 2.31 Note verbatim
      (single line, reflow removed) + [TPS_ECUC_02041] / [TPS_ECUC_02042] /
      [TPS_ECUC_06088] appended verbatim (`\_` unescaped, `glyph[...]` +
      `()` markers stripped — EcucValueCollection batch convention);
      getter + setter docstrings = the destinationType row Note verbatim
      ("The type in the AUTOSAR Metamodel to which instance this reference
      is allowed to point to.", EcucInstanceReferenceDef stamped-sibling
      wording), setter appended the None-no-op sentence; inline `__init__`
      comment already the Note verbatim (kept); `__init__` has no
      docstring; blank line between attribute blocks (single attr).
      Green: TestEcucForeignReferenceDef 6 passed.
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    - note (Step 5): ADDED — parser test_arxml_parser_ecuc_handlers.py
      TestEcucContainerDefReferences.test_readEcucForeignReferenceDef
      (REFERENCES/ECUC-FOREIGN-REFERENCE-DEF via the container dispatch,
      DESTINATION-TYPE value asserted) + writer test_writer_ecuc_def.py
      TestWriterEcucForeignReferenceDef (test_full emit + test_omits_when_none
      + test_round_trip_destination_type end-to-end set → save → reload →
      assert field values through the reloaded container). Seen Red 4 failed:
      parser NotImplementedError "Unsupported EcucReferenceDef
      <ECUC-FOREIGN-REFERENCE-DEF>"; writer AttributeError (no
      createEcucForeignReferenceDef factory / no writeEcucForeignReferenceDef
      helper) — coverage was entirely absent.
  - [x] Step 6 — Update parser & writer (Green)
    - note (Steps 5/6): MODEL: added createEcucForeignReferenceDef factory on
      the stamped aggregator EcucParamConfContainerDef (IsElementExists
      duplicate-check + addElement + references append — sibling factory
      shape). PARSER: readEcucForeignReferenceDef (readEcucAbstractExternal
      ReferenceDef + setDestinationType via getChildElementOptionalLiteral —
      the stamped readEcucInstanceReferenceDef helper choice for String-typed
      fields) + dispatch branches in readEcucContainerDefReferences AND
      readEcucDestinationUriPolicyReferences (createEcucForeignReferenceDef
      factory — policy convention). WRITER: writeEcucForeignReferenceDef
      (writeEcucAbstractExternalReferenceDef + setChildElementOptionalLiteral,
      DESTINATION-TYPE flat — XSD has no VARIANTS wrapper) + isinstance
      branches in writeEcucContainerDefReferences AND
      writeEcucDestinationUriPolicyReferences. All matched Rule 0013.2 name
      pairs, single mutator statements; imports added alphabetically (no
      re-sort). Green: parser + writer suites 231 passed.
  - [x] Step 7 — Update checklist comment
    - note (Step 7): checklist rewritten to the final batch-mode shape —
      `# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.31, p.75`
      (pdf_page.py caption hit confirms p.75) + the `# Columns:` header +
      per-row `R23-11` release column (the pre-sync rows had no Columns
      line/release); rows in source order = displayed row order (single
      attr, getter first per scalar pair); reader [x] on the setDestination
      Type row, writer [x] on the getDestinationType row; `# Spec verified:`
      marker NOT written (batch mode — deferred to batch confirmation);
      dispatch note line added (both aggregation branches + the aggregator
      factory). Set-based check passed: checklist == {__init__,
      getDestinationType, setDestinationType}, all covered in the mirrored
      test.
  - [x] Step 8 — Deviations
    - note (Step 8): No deviations — the bare-`String` annotations,
      paraphrased/reflowed docstrings were Rule 0001.4/0003 to-fix drift
      completed in this pass (not deviation rows); the absent reader/writer
      coverage was implemented in this pass (Rule 0001.7 five-place pattern:
      subtype class + aggregator factory + reader branches + writer
      branches + dispatch tests), also not a deviation row. "No deviations"
      entry + provenance note appended to docs/examples/method_deviation_by
      _class.md (new EcucForeignReferenceDef section). No Rule 0001.10
      missing referenced classes; not VP-capable (Rule 0020); no
      integration fixture carries ECUC-FOREIGN-REFERENCE-DEF (no Rule 0019
      combine case). v2 tracker has no EcucForeignReferenceDef entry
      (nothing to reconcile there).
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-30 (14985 passed /
    0 failed, lint + black clean); 9b deferred to batch confirmation
    (user instruction)
    - note (Step 9 re-verify 2026-10-04): 9a re-passed on feature/g19-batch-9b (base 42a9a0dc9) — full suite 17607 passed / 0 failed (integration round-trips incl.), ruff + flake8 + mypy (268 files) clean, black clean on touched files, set-based checklist-vs-methods PASS, member-annotation gate PASS; 9b still deferred to batch confirmation.
    - note (Step 9): set-based check passed (checklist == {__init__,
      getDestinationType, setDestinationType}, all test-covered, no
      `# type:` comments, member order = displayed row order, getter-first
      scalar pair); Rule 0013 chained-mutator greps show only pre-existing
      construction chains (NameToken()/Numerical().setValue(...) inside one
      mutator call — untouched regions); full suite 14985 passed / 0 failed
      (integration round-trips incl.); npm run lint clean; black clean on
      all 6 touched code files; no marker in batch mode.

- [ ] `EcucLinkerSymbolDef` — EcucAbstractStringParamDef — R23-11 markdown · Table 2.21
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - note (Step 1): Table 2.21 AUTOSAR_CP_TPS_ECUConfiguration.md l.1707-1714
    (caption l.1705; pdf_page.py: PDF p.65 caption hit). Concrete Class
    (class-row `<<atpVariation>>` — not a VP-aggregation indicator per
    Rule 0020); Package M2::AUTOSARTemplates::ECUCParameterDefTemplate;
    Note "Configuration parameter type for Linker Symbol Names like those
    used to specify memory locations of variables and constants."; Base
    chain ARObject/AtpDefinition/EcucAbstractStringParamDef/
    EcucCommonAttributes/EcucDefinitionElement/EcucParameterDef/
    Identifiable/MultilanguageReferrable/Referrable → most-derived base
    EcucAbstractStringParamDef (stamped R23-11, Table 2.18 p.63, same
    file) — src matches, no flattening. EMPTY attribute table — corpus
    l.1699 "The class EcucLinkerSymbolDef does not introduce any
    additional attributes" (0 own rows; all attrs inherited from the
    base — Rule 0002 empty-attribute-rendering case). XSD group
    ECUC-LINKER-SYMBOL-DEF (AUTOSAR_00052.xsd l.52608, complexType
    l.52630) = only the ECUC-LINKER-SYMBOL-DEF-VARIANTS/
    ECUC-LINKER-SYMBOL-DEF-CONDITIONAL wrapper — no own attribute
    elements; aggregators' PARAMETERS choices carry the element at
    l.52117 + l.53107. Class requirement [TPS_ECUC_02031] (l.1697,
    255-char value/defaultValue length restriction) → class docstring
    per the batch convention (`\_` unescaped, glyph markers stripped).
    Drift found: model already spec-shaped (base, verbatim Note
    docstring, __init__) but reader/writer coverage ENTIRELY ABSENT —
    no readEcucLinkerSymbolDef/writeEcucLinkerSymbolDef helpers, no
    dispatch branch in any of the 4 aggregation sites, no
    createEcucLinkerSymbolDef factory on EcucParamConfContainerDef →
    elements silently dropped on round-trip (the Steps 5/6 fix). v1
    tracker has a STALE `missing` row (ecucLinkerSymbolDefVariant /
    EcucLinkerSymbolDefConditional) — Table 2.21's attribute column is
    empty, the variant conditional is an XSD-only atpVariation artifact,
    NOT a spec attribute (Rule 0015) → row resolved at Step 8. v2
    tracker lists the class only in its generated "classes without a
    spec attribute table" appendix (nothing to reconcile). No
    integration fixture carries ECUC-LINKER-SYMBOL-DEF (no Rule 0019
    combine case).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
    - note (Step 2): extended the mirrored
      ECUCParameterDefTemplate/test_ECUCParameterDefTemplate.py —
      TestEcucLinkerSymbolDef.test_inheritance (isinstance pin on the
      most-derived base EcucAbstractStringParamDef) +
      test_docstrings_verbatim (inspect.cleandoc pin: class docstring ==
      Table 2.21 Note verbatim + [TPS_ECUC_02031] appended per batch
      convention) + TestEcucParamConfContainerDef
      .test_create_ecuc_linker_symbol_def (create appends to parameters +
      duplicate returns the existing instance). Seen Red 2 failed / 3
      passed — the docstring pin failed on the missing [TPS_ECUC_02031]
      requirement text; the factory test failed with AttributeError (no
      createEcucLinkerSymbolDef).
  - [x] Step 3 — Implement model class (Green)
    - note (Step 3): field-to-spec cross-check both directions PASSES —
      Table 2.21 has an EMPTY attribute column and the class declares
      zero own fields (no fabrication, no flattening; all attrs inherited
      from the stamped base EcucAbstractStringParamDef); Base = most-
      derived EcucAbstractStringParamDef (stamped R23-11, Table 2.18) —
      src already matched. Added createEcucLinkerSymbolDef factory on the
      stamped aggregator EcucParamConfContainerDef (IsElementExists
      duplicate-check + addElement + parameters append — sibling factory
      shape; quoted `-> "EcucLinkerSymbolDef"` forward-ref return, this
      module's no-PEP-563 convention, name defined later in the module).
      Green: factory test passes; remaining Red is the Step 4 docstring
      scope only (8 passed / 1 failed at this point).
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    - note (Step 4): wiped and rewrote the class docstring — Table 2.21
      Note verbatim ("Configuration parameter type for Linker Symbol
      Names like those used to specify memory locations of variables and
      constants.") + the class requirement [TPS_ECUC_02031] appended
      verbatim (md l.1697, `\_` unescaped, `glyph[ceilingleft]`/
      `glyph[floorright] ()` markers stripped — the ForeignReferenceDef
      batch convention; the requirement targets this class's value/
      defaultValue length). No getter/setter docstrings or __init__
      member comments exist to wipe (0 own attributes — Rule 0002
      empty-attribute case); `__init__` has no docstring; the new
      factory's docstring is the EcucParamConfContainerDef parameter
      Note verbatim (identical to the stamped sibling factories).
      Green: mirrored file 146 passed.
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    - note (Step 5): new tests/test_armodel/parser/test_arxml_parser_ecuc_handlers.py
      TestEcucLinkerSymbolDefParameters (3 tests: container-site read with
      DEFAULT-VALUE/MAX-LENGTH/MIN-LENGTH inside the CONDITIONAL, minimal read,
      EcucDestinationUriPolicy-site dispatch) + tests/test_armodel/writer/
      test_writer_ecuc_def.py TestWriterEcucLinkerSymbolDef (4 tests: direct write
      structure + VARIANTS-wrapper-last XSD order, container-params dispatch,
      policy-params dispatch, full save→reload round-trip with value asserts). Seen
      Red 7 failed (3 parser — ECUC-LINKER-SYMBOL-DEF hit notImplemented; 4 writer —
      no helpers/dispatch).
  - [x] Step 6 — Update parser & writer (Green)
    - note (Step 6): readEcucLinkerSymbolDef/writeEcucLinkerSymbolDef helpers added
      (readEcucParameterDef + CONDITIONAL-wrapper content via the inherited base
      accessors — EcucMultilineStringParamDef pattern; writer mirrors via
      writeEcucParameterDef + VARIANTS/CONDITIONAL + writeEcucAbstractStringParamDef);
      ECUC-LINKER-SYMBOL-DEF dispatch branches added after the MULTILINE branch in all
      four aggregation sites (readEcucContainerDefParameters,
      readEcucDestinationUriPolicyParameters, writeEcucContainerDefParameters,
      writeEcucDestinationUriPolicyParameters); createEcucLinkerSymbolDef factory on
      EcucParamConfContainerDef (Step 3); imports added. 7 passed (Green); touched
      suites 384 passed.
  - [x] Step 7 — Update checklist comment
    - note (Step 7): 6-column format, `# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf,
      Table 2.21, p.65`, single `__init__` row (Table 2.21 has zero attribute rows —
      Rule 0002 empty-attribute case; reader/writer coverage claimed on the stamped
      base EcucAbstractStringParamDef's rows, EcucMultilineStringParamDef precedent);
      no marker written (unstamped batch).
  - [x] Step 8 — Deviations
    - note (Step 8): v1 tracker stale `missing` row (ecucLinkerSymbolDefVariant /
      EcucLinkerSymbolDefConditional) resolved to removed (Rule 0015 — XSD-only
      atpVariation split artifact, attribute column empty); missing reader/writer
      coverage fixed in-pass, recorded as no-deviation rows + batch Note in
      method_deviation_by_class.md; v2 tracker appendix needs no reconciliation; no
      open deviation remains.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-30 (14995 passed / 0
      failed incl. integration round-trips; npm run lint clean; black clean on all
      touched files); 9b deferred to batch confirmation (user instruction)
    - note (Step 9 re-verify 2026-10-04): 9a re-passed on feature/g19-batch-9b (base 42a9a0dc9) — full suite 17607 passed / 0 failed (integration round-trips incl.), ruff + flake8 + mypy (268 files) clean, black clean on touched files, set-based checklist-vs-methods PASS, member-annotation gate PASS; 9b still deferred to batch confirmation.

- [x] `EcucReferenceDef` — EcucAbstractInternalReferenceDef — R23-11 markdown · Table 2.29 (CP_TPS_ECUConfiguration), p.73 — commit 0d4506747 (stamped 2026-10-02, # Spec verified: R23-11)

- [x] `EcucSymbolicNameReferenceDef` — EcucAbstractInternalReferenceDef — R4.3.1 markdown · Table 2.34 (AUTOSAR_TPS_ECUConfiguration), p.83 — commit 0d4506747 (stamped 2026-10-02, # Spec verified: R4.3.1)

- [x] `EcucUriReferenceDef` — EcucAbstractInternalReferenceDef — R23-11 markdown · Table 2.33 (CP_TPS_ECUConfiguration), p.81 — commits 0d4506747 + d495d9ebf (rw completion; stamped 2026-10-02, # Spec verified: R23-11)

- [ ] `EcucConditionFormula` (input · R23-11 PDF · Table 2.43) — REOPENED 2026-10-05 (batch 9b audit, Group B)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - note (Step 1): Table 2.43 AUTOSAR_CP_TPS_ECUConfiguration.pdf p.100. Class
    `<<atpMixedString>>` pure-text formula; Package
    M2::AUTOSARTemplates::ECUCParameterDefTemplate; Note "This formula shall
    yield a boolean expression depending on ecuc queries. Note that the
    EcucCondition Formula is a mixed string. Therefore, the properties have the
    upper multiplicity 1." (class docstring already verbatim); Base
    FormulaExpression (spec most-derived; re-parented 2026-09-25 per
    docs/plan/atp_mixed_string_hierarchy.md, tree unchanged — the drift-fix
    comment was retired into this row). 2 attrs in displayed order:
    ecucQueryRef (EcucQuery, 0..1, ref) → Optional[RefType]; ecucQueryStringRef
    (EcucQuery, 0..1, ref) → Optional[RefType] (Rule 0001.5 Ref suffix, module
    convention). XSD complexType ECUC-CONDITION-FORMULA (AUTOSAR_00052.xsd
    l.51486) declares `AR:AR-OBJECT` group + attributeGroup → S/T must
    round-trip. Drift found on reopen: legacy 5-column checklist (rows ended at
    `writer`, no `# Columns:` line / release token) + `readARObject` /
    `writeARObject` absent from the reader/writer entry points (Rule 0025 S/T
    drop) + stale `# Spec verified: R23-11` marker. Not VP-capable (Rule 0020 —
    no VARIATION-POINT in the XSD complexType). No Rule 0001.10 missing types.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
    - note (Step 2): mirror TestEcucConditionFormula already present in both
      test_ECUCParameterDefTemplate.py copies (init defaults / set-get chaining
      on both refs); added the S/T reader + writer coverage in Steps 5/6 (the
      Red is the missing base-helper call, observed by audit_class.py BASE).
  - [x] Step 3 — Implement model class (Green)
    - note (Step 3): field-to-spec cross-check both directions PASSES as-is —
      Base FormulaExpression (most-derived, re-parented 2026-09-25), 2 attrs
      1:1 with Table 2.43 in displayed order, members Optional[RefType] PEP 526
      under verbatim Notes, None-guarded setters returning self; no fabricated /
      flattened fields (the `<<atpMixedString>>` content markings — atpMixedString,
      Stereotypes, Tags — are the class-level stereotype, not attributes). Net
      code change: none.
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    - note (Step 4): class docstring + both member Notes + accessor docstrings
      diffed against Table 2.43 — all verbatim (member Notes "The EcucQuery
      serves as a argument for the formula." / "This indicates that the
      referenced query shall return a string.", spec grammar quirk "a argument"
      preserved); setters carry the None-no-op sentence; `__init__` has no
      docstring. Wipe+rewrite would be byte-identical.
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    - note (Step 5): ADDED parser test_arxml_parser_ecuc_handlers.py
      TestEcucConditionSpecification.test_read_condition_formula_checksum_and_timestamp
      (CONDITION-FORMULA with S/T attribs → getChecksum()/getTimestamp()) and
      writer test_writer_ecuc_def.py TestWriterEcucConditionFormula
      .test_writes_checksum_and_timestamp (model S/T → CONDITION-FORMULA S/T
      attribs). Red observable: audit_class.py BASE flagged no base helper call
      (S/T silently dropped) before the fix.
  - [x] Step 6 — Update parser & writer (Green)
    - note (Steps 5/6): added `self.readARObject(element, formula)` to
      readEcucConditionFormula (parser l.13588) and
      `self.writeARObject(formula_element, formula)` to writeEcucConditionFormula
      (writer l.11340) — Rule 0025 base-helper symmetry, single call (Rule 0013.1),
      literal accessors dropped; matched Rule 0013.2 name pair, no receiver chains.
      Green: touched suites 420 passed.
  - [x] Step 7 — Update checklist comment
    - note (Step 7): legacy 5-column block converted to the 6-column format in
      source order (getter-first scalar pairs, reader [x] on setter rows / writer
      [x] on getter rows) — `# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf,
      Table 2.43, p.100` + `# Columns:` header + per-row `R23-11` release; stale
      `# Spec verified: R23-11` marker STRIPPED (Rule 0023 staleness; batch mode
      — re-stamp deferred to batch confirmation).
  - [x] Step 8 — Deviations
    - note (Step 8): No deviations — the legacy checklist shape + missing
      base-helper call were Rule 0023/0025 to-fix drift completed in this pass
      (not deviation rows). The 2026-09-25 re-parent to FormulaExpression is a
      recorded drift fix (docs/plan/atp_mixed_string_hierarchy.md), not a
      deviation. No Rule 0001.10 missing referenced classes (RefType is the
      stamped base; EcucQuery is the destination-side class).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a reruns in the batch verification pass; 9b deferred to batch confirmation (user instruction)
    - note (2026-10-06, batch-9b review): class re-verified PASS (fields/
      docstrings/base/rw coverage all conform); stale tracker `missing` rows
      (ecucQueryRef/ecucQueryStringRef) removed from
      method_deviation_by_class.md (Rule 0014) — no source change.

- [ ] `EcucParameterDerivationFormula` (input · R23-11 PDF · Table 2.39) — REOPENED 2026-10-05 (batch 9b audit, Group B)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - note (Step 1): Table 2.39 AUTOSAR_CP_TPS_ECUConfiguration.pdf p.88. Class
    `<<atpMixedString>>` pure-text formula; Package
    M2::AUTOSARTemplates::ECUCParameterDefTemplate; Note "This formula is
    intended to specify how an ecu parameter can be derived from other
    information in the Autosar Templates." (class docstring already verbatim);
    Base FormulaExpression (spec most-derived; re-parented 2026-09-25, tree
    unchanged). 2 attrs in displayed order: ecucQueryRef (EcucQuery, 0..1, ref)
    → Optional[RefType]; ecucQueryStringRef (EcucQuery, 0..1, ref) →
    Optional[RefType]. XSD complexType ECUC-PARAMETER-DERIVATION-FORMULA
    (AUTOSAR_00052.xsd l.53258) declares `AR:AR-OBJECT` group + attributeGroup →
    S/T must round-trip. Drift found on reopen: legacy 5-column checklist +
    `readARObject` / `writeARObject` absent from the reader/writer entry points
    (Rule 0025 S/T drop) + stale marker. Not VP-capable (Rule 0020). No Rule
    0001.10 missing types.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
    - note (Step 2): mirror TestEcucParameterDerivationFormula already present
      in both test_ECUCParameterDefTemplate.py copies; added the S/T reader +
      writer coverage in Steps 5/6. Red = audit BASE failure before the fix.
  - [x] Step 3 — Implement model class (Green)
    - note (Step 3): field-to-spec cross-check both directions PASSES as-is —
      Base FormulaExpression, 2 attrs 1:1 with Table 2.39 in displayed order,
      members Optional[RefType] PEP 526 under verbatim Notes, None-guarded
      setters returning self; no fabricated/flattened fields. Net code change:
      none.
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    - note (Step 4): class docstring + both member Notes ("This is one
      particular EcucQuery used in the calculation formula." / "This indicates
      that the referenced query shall return a string.") + accessor docstrings
      verbatim; setters carry the None-no-op sentence; `__init__` has no
      docstring. Wipe+rewrite would be byte-identical.
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    - note (Step 5): ADDED parser
      TestEcucDerivationSpecification.test_read_calculation_formula_checksum_and_timestamp
      (CALCULATION-FORMULA with S/T attribs) and writer
      TestWriterEcucDerivationSpecification
      .test_writes_calculation_formula_checksum_and_timestamp (model S/T →
      CALCULATION-FORMULA S/T attribs). Red observable: audit_class.py BASE
      failure before the fix.
  - [x] Step 6 — Update parser & writer (Green)
    - note (Steps 5/6): added `self.readARObject(element, formula)` to
      readEcucParameterDerivationFormula (parser l.13581) and
      `self.writeARObject(formula_element, formula)` to
      writeEcucParameterDerivationFormula (writer l.11332) — Rule 0025 symmetry,
      single call, matched Rule 0013.2 pair. Green: touched suites 420 passed.
  - [x] Step 7 — Update checklist comment
    - note (Step 7): legacy 5-column block converted to the 6-column format in
      source order — `# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.39,
      p.88` + `# Columns:` header + per-row `R23-11` release; stale marker
      STRIPPED (Rule 0023 staleness; batch mode).
  - [x] Step 8 — Deviations
    - note (Step 8): No deviations — legacy checklist shape + missing
      base-helper call were Rule 0023/0025 to-fix drift. No Rule 0001.10
      missing referenced classes.
    - note (Steps 3/4 re-run 2026-10-06, batch-9b review): 2 defects found by
      the 2026-10-06 Rule-0026 audit and fixed — (1) Rule 0001.4: setter
      params were bare `RefType` (spec 0..1 → Optional[RefType]); field/getter
      were already Optional; sibling EcucConditionFormula was the correct
      shape; (2) Rule 0012 verbatim: class docstring hard-wrapped the Note
      mid-sentence ("derived\nfrom") — unwrapped to the spec's single
      sentence. Stale tracker `missing` rows (ecucQueryRef/ecucQueryStringRef)
      removed from method_deviation_by_class.md (Rule 0014). Both mirrored
      test classes pin behavior only — no test change needed.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a reruns in the batch verification pass; 9b deferred to batch confirmation (user instruction)

- [ ] `EcucQueryExpression` (input · R23-11 PDF · Table 2.41) — REOPENED 2026-10-05 (batch 9b audit, Group B)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - note (Step 1): Table 2.41 AUTOSAR_CP_TPS_ECUConfiguration.pdf p.90. Class
    `<<atpMixedString>>` pure-text formula; Package
    M2::AUTOSARTemplates::ECUCParameterDefTemplate; Note "Defines a query
    expression to the ECUC Description and output the result as an numerical
    value. Due to the \"mixedString\" nature of the formula there can be several
    EcuQueryExpressions used." (class docstring already verbatim); Base ARObject
    (XSD complexType ECUC-QUERY-EXPRESSION carries AR-OBJECT only). 2 attrs in
    displayed order: configElementDefGlobalRef (EcucDefinitionElement, 0..1,
    ref) → Optional[RefType]; configElementDefLocalRef (EcucDefinitionElement,
    0..1, ref) → Optional[RefType] (the markdown render shows only the local
    row — a render artifact; the XSD group carries both CONFIG-ELEMENT-DEF-GLOBAL-REF
    and -LOCAL-REF). XSD complexType ECUC-QUERY-EXPRESSION (AUTOSAR_00052.xsd
    l.53401) declares `AR:AR-OBJECT` group + attributeGroup → S/T must
    round-trip. Drift found on reopen: legacy 5-column checklist +
    `readARObject` / `writeARObject` absent from the inline
    construction sites (Rule 0025 S/T drop) + stale marker. Not VP-capable
    (Rule 0020). No Rule 0001.10 missing types.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
    - note (Step 2): mirror TestEcucQueryExpression already present in both
      test_ECUCParameterDefTemplate.py copies; added the S/T reader + writer
      coverage in Steps 5/6. Red = audit BASE failure before the fix.
  - [x] Step 3 — Implement model class (Green)
    - note (Step 3): field-to-spec cross-check both directions PASSES as-is —
      Base ARObject, 2 attrs 1:1 with Table 2.41 in displayed order, members
      Optional[RefType] PEP 526 under verbatim Notes, None-guarded setters
      returning self; no fabricated/flattened fields. Net code change: none.
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    - note (Step 4): class docstring + both member Notes (the long
      "The EcucQueryExpression points to an EcucDefinition Element …" global /
      local wording) + accessor docstrings verbatim; setters carry the None-no-op
      sentence; `__init__` has no docstring. Wipe+rewrite would be byte-identical.
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    - note (Step 5): ADDED parser
      TestEcucConditionSpecification.test_read_query_expression_checksum_and_timestamp
      (ECUC-QUERY-EXPRESSION with S/T attribs → getChecksum()/getTimestamp()) and
      writer TestWriterEcucQuery
      .test_writes_query_expression_checksum_and_timestamp (model S/T →
      ECUC-QUERY-EXPRESSION S/T attribs). Red observable: audit_class.py BASE
      failure before the fix.
  - [x] Step 6 — Update parser & writer (Green)
    - note (Steps 5/6): the class is built inline in the EcucQuery reader/writer,
      so added `self.readARObject(expr_element, expr)` in readEcucQuery (parser
      l.13630) and `self.writeARObject(expr_element, expr)` in writeEcucQuery
      (writer l.11385) — Rule 0025 symmetry, single call. Green: touched suites
      420 passed.
  - [x] Step 7 — Update checklist comment
    - note (Step 7): legacy 5-column block converted to the 6-column format in
      source order — `# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.41,
      p.90` + `# Columns:` header + per-row `R23-11` release; stale marker
      STRIPPED (Rule 0023 staleness; batch mode).
  - [x] Step 8 — Deviations
    - note (Step 8): No deviations — legacy checklist shape + missing
      base-helper call were Rule 0023/0025 to-fix drift. No Rule 0001.10
      missing referenced classes.
    - note (Step 4 re-run 2026-10-06, batch-9b review): Rule 0012.2.5.3 —
      the `Stereotypes: atpUriDef` tail was dropped from both attribute Notes
      (Table 2.41 rows end with it; the stamped atpUriDef siblings keep it).
      Appended in all 6 places (inline __init__ comments + getter/setter
      docstrings, global + local). Stale tracker `missing` rows
      (configElementDefGlobalRef/LocalRef) removed from
      method_deviation_by_class.md (Rule 0014). Mirrored test class pins
      behavior only — no test change needed.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a reruns in the batch verification pass; 9b deferred to batch confirmation (user instruction)
