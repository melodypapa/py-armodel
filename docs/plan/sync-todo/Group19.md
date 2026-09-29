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

- [ ] `EcucValueCollection` — ARElement — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/ECUCDescriptionTemplate.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ModuleConfiguration` — ARElement — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/ECUCDescriptionTemplate.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `EcucConfigurationClassEnum` — AREnum — source TBC (locate table at Step 1)
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

- [ ] `EcucScopeEnum` — AREnum — source TBC (locate table at Step 1)
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

- [ ] `EcucBooleanParamDef` — EcucParameterDef — source TBC (locate table at Step 1)
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
