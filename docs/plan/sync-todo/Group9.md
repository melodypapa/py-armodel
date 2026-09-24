# Sync todo: Group 9 — Constants & MSR

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

- [ ] `NumericalValueSpecification` — ValueSpecification — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py
  - [x] Step 1 — Sync members & description from spec — Table 5.114 (AUTOSAR_CP_TPS_SoftwareComponentTemplate.md L12573, p.436 via pdf_page.py); reproductions verified identical: Table D.43 (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md L8855) + Table F.84 (AUTOSAR_CP_TPS_SystemTemplate.md L75190 table body before title — appendix title-after-content rendering); Class table: Package M2::AUTOSARTemplates::CommonStructure::Constants matches current file; class Note "A numerical ValueSpecification which is intended to be assigned to a Primitive data element. Note that the numerical value is a variant, it can be computed by a formula."; Base ARObject, ValueSpecification → most-derived base ValueSpecification — already stamped `# Spec verified: R23-11` in this module (L29; base-stamp observation, not a blocker); single attribute row: value (Numerical, 0..1, attr, Note "This is the value itself. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime" — Numerical → ARNumerical, the atpMixedString NUMERICAL-VALUE-VARIATION-POINT payload); constr_1920 existence constraint is doc-level, not a model member; Aggregated-by list is consumer-side, not modeled. XSD 00052 ground truth: group NUMERICAL-VALUE-SPECIFICATION L85701 (single VALUE minOccurs 0) + complexType L85718 (AR-OBJECT + VALUE-SPECIFICATION + NUMERICAL-VALUE-SPECIFICATION groups → XML element order SHORT-LABEL then VALUE); reader pre-exists (parser getNumericalValueSpecification arxml_parser.py L7929 via readValueSpecification base helper + getChildElementOptionalNumericalValue; tag dispatch getValueSpecification L7995) and writer pre-exists (writeNumericalValueSpecification arxml_writer.py L1775 via writeValueSpecification + setChildElementOptionalNumericalValue; consumers L1788 ArrayValueSpecification.elements / L1861 setChildValueSpecification / L3389 RecordValueSpecification.fields) — coverage complete, XSD order correct, no dropped field; model layer is old-style: 4-col checklist without `# Spec:` line, paraphrased docstrings, `ARNumerical` non-Optional hints → Steps 2–7 align
  - [x] Step 2 — Write model class unit test (Red) — new mirror file tests/test_armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/test_NumericalValueSpecification.py (7 tests, style of stamped sibling test_ReferenceValueSpecification.py): inheritance isinstance ValueSpecification, initialization (value/shortLabel None), get/set round-trip with ARNumerical("3.14") asserting identity + float value, setValue(None) no-op, shortLabel base round-trip + None no-op, and typing.get_type_hints assert Optional[ARNumerical] on getValue return + setValue param; Red confirmed 1 failed/6 passed (first run KeyError'd on __init__-body hints — PEP 526 self.attr annotations in method bodies are not runtime-visible, moved the Red assert to the accessor signatures — final Red: getValue return = ARNumerical ≠ Optional[ARNumerical]); honest note: the 6 behavioral tests pass immediately — the class pre-exists with value/getValue/setValue and a None-guard (orphan intake, alignment pass); the only genuine Red is the non-Optional typing (Rule 0003)
  - [x] Step 3 — Implement model class (Green) — member set per Table 5.114 already complete (single attr value; no fabrication, no missing member, dedicated field not a registry filter); base ValueSpecification (most-derived, stamped) already provides shortLabel; Green edits: `self.value: ARNumerical = None` → `self.value: Optional[ARNumerical] = None`, getValue return `ARNumerical` → `Optional[ARNumerical]`, setValue param `ARNumerical` → `Optional[ARNumerical]` + explicit chaining return `-> NumericalValueSpecification` (stamped-sibling convention); mirror test 7/7 passed (0.16s); Step-3 referenced classes: none missing — ARNumerical (PrimitiveTypes, imported), ValueSpecification (same module, stamped)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — wiped ALL stale docstrings in the class (old class docstring "Represents a numerical value specification…", `__init__` docstring "Initializes…", paraphrased getter "Gets the numerical value…"/setter "Sets the numerical value…" + Args/Returns blocks) then rewrote verbatim from Table 5.114 markdown: class docstring = class Note "A numerical ValueSpecification which is intended to be assigned to a Primitive data element. Note that the numerical value is a variant, it can be computed by a formula."; `__init__` no docstring (Rule 0012.2.5.2) with inline member comment = attribute Note verbatim "This is the value itself. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime"; getter docstring = attribute Note verbatim (+ closing period per stamped-sibling inline shape); guarded setter docstring = attribute Note verbatim + "A None value is a no-op and does not overwrite an existing value."; shape mirrors stamped sibling ReferenceValueSpecification (multi-line triple-quoted); PEP 526 annotated member directly under its note comment, blank line between `__init__` attribute block and methods; mirror test 7/7 after rewrite
  - [x] Step 5 — Write reader/writer round-trip test (Red) — new tests/test_armodel/writer/test_writer_numerical_value_specification.py (3 tests, style of stamped sibling test_writer_not_available_value_specification.py, AUTOSAR.getInstance().new() fixture): (1) write with SHORT-LABEL "nvs" + VALUE 3.14 asserting the full child tag sequence == ["SHORT-LABEL", "VALUE"] (XSD 00052 complexType L85718 group order: AR-OBJECT + VALUE-SPECIFICATION + NUMERICAL-VALUE-SPECIFICATION) and both field values; (2) empty-wrapper case — bare spec writes the tag with NO VALUE child; (3) write → ET serialize → namespace-inject → parser.getValueSpecification re-parse asserting isinstance + shortLabel "nvs" + value 3.14 (field values, not len()); honest note: 3/3 passed immediately (0.17s) — reader/writer coverage pre-exists and is correct for this class; no genuine Red found (no dropped field)
  - [x] Step 6 — Update parser & writer (Green) — NO CHANGE needed: reader arxml_parser.py getNumericalValueSpecification (L7929) already reads via readValueSpecification base helper → setShortLabel + setValue(getChildElementOptionalNumericalValue("VALUE")) (mutator form, no chaining), dispatched from the getValueSpecification tag dispatch (L7995-7996); writer arxml_writer.py writeNumericalValueSpecification (L1775) already writes tag → writeValueSpecification base → setChildElementOptionalNumericalValue("VALUE", getValue()) in XSD order, consumed from ArrayValueSpecification.elements (L1788), setChildValueSpecification polymorphic dispatch (L1861), RecordValueSpecification.fields (L3389); Rule 0013 matched-name pairs verified (readValueSpecification↔writeValueSpecification, setValue↔getValue, setShortLabel↔getShortLabel); observation: reader re-calls setShortLabel after readValueSpecification already set it — idempotent duplicate (setShortLabel None-guards), present on all value-spec siblings, left as-is; round-trip 3/3 + model 7/7 re-run green
  - [x] Step 7 — Update checklist comment — class-body checklist rewritten to 6-column Rule 0002 format: `# Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.114, p.436` + Columns legend + 3 rows source order (__init__ [—]/[—], getValue writer [x] — writer calls getValue/shortLabel getter, setValue reader [x] — reader calls setValue/setShortLabel), every row release R23-11; shortLabel accessor rows stay on the stamped base ValueSpecification checklist (base owns them); `# Spec verified:` marker NOT written (deferred to 9b/batch confirmation)
  - [x] Step 8 — Deviations — NO deviations: no placeholders, no missing members (table = single attr value, all modeled), no naming (ref/tref/aggr rules n/a), no type deviations (Numerical → ARNumerical is the established mapped type, same as stamped consumers), reader+writer coverage complete, member order = displayed row order (single attribute); nothing to add to method_deviation_by_class*.md; observations recorded at Steps 1/6 (stamped base; idempotent setShortLabel re-read) are not spec deviations; `# Spec verified:` stamp WITHHELD pending 9b batch confirmation (Rule 0012.1)
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-24: target tests 159/159 (Constants model dir incl. new test_NumericalValueSpecification.py 7 + CommonStructure_init.py 149 + new test_writer_numerical_value_specification.py 3), full suite 11346 passed/0 failed (parent-branch baseline 11336 per Group8 final rows + 10 net-new: 7 model + 3 round-trip; the 11326 figure in the batch brief predates the last Group8 additions), npm run lint (flake8+ruff) clean, npm run black no-op (1161 files unchanged) + black-check clean, integration round-trip (29 ARXML) included in suite green; 9b deferred to batch confirmation (user instruction 2026-09-24)

- [ ] `TextValueSpecification` — ValueSpecification — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ConstantReference` — ValueSpecification — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ConstantSpecification` — ARElement — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py
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

- [ ] `DataFilterTypeEnum` — AREnum — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/Filter.py
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

- [ ] `DataFilter` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/Filter.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `DataFilterTypeEnum`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `Modification` — ARObject — source TBC (locate table at Step 1)
  - module: M2/MSR/AsamHdo/AdminData.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ScaleConstrValidityEnum` — AREnum — source TBC (locate table at Step 1)
  - module: M2/MSR/AsamHdo/Constraints/GlobalConstraints.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `UnitGroup` — ARElement — source TBC (locate table at Step 1)
  - module: M2/MSR/AsamHdo/Units.py
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

- [ ] `SwImplPolicyEnum` — AREnum — source TBC (locate table at Step 1)
  - module: M2/MSR/DataDictionary/DataDefProperties.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SwSystemconst` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/MSR/DataDictionary/SystemConstant.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ListEnum` — AREnum — source TBC (locate table at Step 1)
  - module: M2/MSR/Documentation/BlockElements/ListElements.py
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

- [ ] `Item` — Paginateable — source TBC (locate table at Step 1)
  - module: M2/MSR/Documentation/BlockElements/ListElements.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `TopicContentOrMsrQuery` — ARObject — source TBC (locate table at Step 1)
  - module: M2/MSR/Documentation/Chapters.py
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

- [ ] `LOverviewParagraph` — LanguageSpecific — source TBC (locate table at Step 1)
  - module: M2/MSR/Documentation/TextModel/LanguageDataModel.py
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

- [ ] `LPlainText` — LanguageSpecific — source TBC (locate table at Step 1)
  - module: M2/MSR/Documentation/TextModel/LanguageDataModel.py
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

- [ ] `LVerbatim` — LanguageSpecific — source TBC (locate table at Step 1)
  - module: M2/MSR/Documentation/TextModel/LanguageDataModel.py
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

- [ ] `ARList` — Paginateable — source TBC (locate table at Step 1)
  - module: M2/MSR/Documentation/BlockElements/ListElements.py
  - note: deviation-tracked in method_deviation_by_class_v2.md — review entries at Step 1
  - after `Item`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ChapterContent` — ARObject — source TBC (locate table at Step 1)
  - module: M2/MSR/Documentation/Chapters.py
  - note: deviation-tracked in method_deviation_by_class.md + method_deviation_by_class_v2.md — review entries at Step 1
  - after `TopicContentOrMsrQuery`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ChapterModel` — ARObject — source TBC (locate table at Step 1)
  - module: M2/MSR/Documentation/Chapters.py
  - after `ChapterContent`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
