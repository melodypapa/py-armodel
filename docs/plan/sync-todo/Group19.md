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

## Queue (dependency-first)

- [ ] `ConfigReferenceValue` (input · R3.2.3 markdown · Table 3.40)
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-30 (14951 passed / 0
    failed, lint clean, black clean on touched files); 9b deferred to batch confirmation
    (user instruction)
    - note (Step 9): set-based check passed (checklist == methods, all covered, no
      marker in batch mode); repo-wide black-check reports 8 files would-reformat that
      ALREADY fail at HEAD in other rows' modules (AdaptivePlatform + subpackage
      __init__s, StandardizationTemplate/AbstractBlueprintStructure, CommonStructure/
      Timing, SWComponentTemplate/ApplicationAttributes, ARPackage.py, SystemTemplate/
      __init__.py — outside this class's scope, left for their owning rows); this
      row's files are black-clean and the full suite + npm run lint pass.

- [ ] `EcucValueCollection` (input · R23-11 markdown · Table 2.45)
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-30 (14956 passed / 0
    failed, lint + black clean); 9b deferred to batch confirmation
    (user instruction)
    - note (Step 9): set-based check passed (checklist == methods — __init__,
      addEcucValueRef, getEcucValueRefs, getEcuExtractRef, setEcuExtractRef —
      all test-covered, no `# type:` comments, member order = displayed row
      order, mutator-first for the `*` attr); Rule 0013 chained-mutator
      greps show only pre-existing construction chains (XxxEnum().setValue
      (...) inside one mutator call — untouched regions); full suite green
      (integration round-trip incl.); black reformat applied to the
      mirrored test file, all 5 touched code files re-checked clean; no
      marker in batch mode.

- [ ] `ModuleConfiguration` — ARElement — source TBC (locate table at Step 1)
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-30 (14964 passed / 0
    failed, lint + black clean); 9b deferred to batch confirmation
    (user instruction)
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

- [ ] `EcucConfigurationClassEnum` (input · R23-11 markdown/PDF · Table 2.12)
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-30 (14967 passed / 0
    failed, lint + black clean); 9b deferred to batch confirmation
    (user instruction)
    - note (Step 9): set-based enum check passed (`# (no methods)` form,
      class body defines only `__init__`, no stale method rows, no `# type:`
      comments); the subdirectory legacy tests
      (ECUCParameterDefTemplate/test_ECUCParameterDefTemplate.py) that pinned
      the old XSD-uppercase values were updated to the Table 2.12 Literal
      values in this pass; full suite 14967 passed / 0 failed (integration
      round-trips incl.); npm run lint clean; black clean on all touched
      files; no marker in batch mode.

- [ ] `EcucScopeEnum` (input · R23-11 markdown · Table 2.7)
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-30 (14970 passed / 0
    failed, lint + black clean); 9b deferred to batch confirmation
    (user instruction)
    - note (Step 9): set-based enum check passed (`# (no methods)` form,
      class body defines only `__init__`, no stale method rows, no `# type:`
      comments); the subdirectory legacy tests
      (ECUCParameterDefTemplate/test_ECUCParameterDefTemplate.py) that
      pinned the old XSD-uppercase "LOCAL" value were updated to the
      Table 2.7 Literal values in this pass; full suite 14970 passed /
      0 failed (integration round-trips incl.); npm run lint clean; black
      clean on all touched files; no marker in batch mode.

- [ ] `EcucDestinationUriDefRefType` — RefType — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - note: deviation-tracked in method_deviation_by_class_v2.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `EcucBooleanParamDef` — EcucParameterDef — R23-11 markdown · Table 2.15
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
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-30 (14973 passed /
    0 failed, lint + black clean); 9b deferred to batch confirmation
    (user instruction)
    - note (Step 9): set-based check passed; `# type:` grep clean on the
      class body; blank line between attribute blocks verified by eye
      (single attr); full suite 14973 passed / 0 failed (integration
      round-trips incl.); npm run lint clean; black clean on all touched
      files; no marker in batch mode.

- [ ] `EcucFloatParamDef` — EcucParameterDef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `EcucForeignReferenceDef` — EcucAbstractExternalReferenceDef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `EcucLinkerSymbolDef` — EcucAbstractStringParamDef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
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

- [ ] `EcucReferenceDef` — EcucAbstractInternalReferenceDef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `EcucSymbolicNameReferenceDef` — EcucAbstractInternalReferenceDef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - note: deviation-tracked in method_deviation_by_class_v2.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `EcucUriReferenceDef` — EcucAbstractInternalReferenceDef — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/ECUCParameterDefTemplate.py
  - after `EcucDestinationUriDefRefType`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `EcucConditionFormula` — pure-text formula class — locate spec table at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `EcucParameterDerivationFormula` — pure-text formula class — locate spec table at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `EcucQueryExpression` — pure-text formula class — locate spec table at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
