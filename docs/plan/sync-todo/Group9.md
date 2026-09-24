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
  - [x] Step 1 — Sync members & description from spec — Table 5.113 (AUTOSAR_CP_TPS_SoftwareComponentTemplate.md, body split across page break: header rows L12551-12557, title + attribute row L12565-12569, p.436 via pdf_page.py); reproductions verified identical: Table F.136 (AUTOSAR_CP_TPS_SystemTemplate.md L76158 title, body before title L76142-76156 — appendix title-after-content rendering) + R4.3.1 Table 5.121 (AUTOSAR_TPS_SoftwareComponentTemplate.md L10394 — same Note/Base/attr text but mult 1 vs R23-11 0..1; R23-11 + XSD minOccurs=0 authoritative, Rule 0015); Class table: Package M2::AUTOSARTemplates::CommonStructure::Constants matches current file; class Note "The purpose of TextValueSpecification is to define the labels that correspond to enumeration values."; Base ARObject, ValueSpecification → most-derived base ValueSpecification — already stamped `# Spec verified: R23-11` in this module (L29); single attribute row: value (VerbatimString, 0..1, attr, Note "This is the value itself. Note that vt uses the | operator to separate the values for the different bitfield masks in case that the semantics of the related DataPrototype is described by means of a BITFIELD_TEXTTABLE in the associated CompuMethod." — markdown `&#124;` = literal pipe; XSD documentation confirms the two-sentence text); constr_1919 existence constraint is doc-level, not a model member; Aggregated-by list is consumer-side, not modeled. XSD 00052 ground truth: group TEXT-VALUE-SPECIFICATION L122617 (single VALUE minOccurs 0 type VERBATIM-STRING) + complexType L122635 (AR-OBJECT + VALUE-SPECIFICATION + TEXT-VALUE-SPECIFICATION groups → XML element order SHORT-LABEL then VALUE); reader pre-exists (parser getTextValueSpecification arxml_parser.py L7936 via readValueSpecification base helper + setShortLabel duplicate + setValue(getChildElementOptionalLiteral "VALUE") — TYPE GAP: reads plain ARLiteral, spec type is VerbatimString; established sibling pattern reads VerbatimString fields via getChildElementOptionalVerbatimString e.g. SwValues.vt L6678, RuleArguments.vt L7871; tag dispatch getValueSpecification L7999; also consumed L7608 MetaDataItem.metaDataItemType) and writer pre-exists (writeTextValueSpecification arxml_writer.py L1769 via writeValueSpecification + setChildElementOptionalLiteral("VALUE", getValue()) — this IS the established writer convention for VerbatimString fields, no setChildElementOptionalVerbatimString exists, all VT fields write via setChildElementOptionalLiteral; consumers L1798 ArrayValueSpecification.elements / L1853 setChildValueSpecification / L3391 RecordValueSpecification.fields); model layer is old-style: 4-col checklist without `# Spec:` line, fabricated class docstring ("Represents a text value specification…", not the spec Note), paraphrased docstrings, `self.value: ARLiteral = None` non-Optional + wrong type (spec: Optional[VerbatimString]), setValue no None-guard, no chaining return type → Steps 2–7 align
  - [x] Step 2 — Write model class unit test (Red) — new mirror file tests/test_armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/test_TextValueSpecification.py (7 tests, style of prior-agent test_NumericalValueSpecification.py): inheritance isinstance ValueSpecification, initialization (value/shortLabel None), get/set round-trip with VerbatimString("ON") asserting identity + string value, setValue(None) no-op, shortLabel base round-trip + None no-op, and typing.get_type_hints assert Optional[VerbatimString] on getValue return + setValue param; Red confirmed 2 failed/5 passed (test_value_annotation_is_optional — accessors carry no annotations, get_type_hints misses; test_set_value_none — setValue(None) overwrites, no None-guard); honest note: the 5 behavioral tests pass immediately — the class pre-exists with value/getValue/setValue (orphan intake, alignment pass); the genuine Reds are the unannotated accessors (Rule 0003) and the missing None-guard (stamped-sibling convention)
  - [x] Step 3 — Implement model class (Green) — member set per Table 5.113 already complete (single attr value; no fabrication, no missing member, dedicated field not a registry filter); base ValueSpecification (most-derived, stamped) already provides shortLabel; Green edits: `self.value: ARLiteral = None` → `self.value: Optional[VerbatimString] = None` (spec type VerbatimString, already imported in the module — used by sibling RuleArguments.vt), getValue return `Optional[VerbatimString]`, setValue param `Optional[VerbatimString]` + explicit chaining return `-> TextValueSpecification` (stamped-sibling convention) + None-guard; mirror test 7/7 passed (0.19s); Step-3 referenced classes: none missing — VerbatimString (PrimitiveTypes, imported), ValueSpecification (same module, stamped)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — wiped ALL stale docstrings in the class (old class docstring "Represents a text value specification…", `__init__` docstring "Initializes…", paraphrased getter "Gets the text value…"/setter "Sets the text value…" + Args/Returns blocks) then rewrote verbatim from Table 5.113 markdown: class docstring = class Note "The purpose of TextValueSpecification is to define the labels that correspond to enumeration values."; `__init__` no docstring (Rule 0012.2.5.2) with inline member comment = attribute Note verbatim "This is the value itself. Note that vt uses the | operator to separate the values for the different bitfield masks in case that the semantics of the related DataPrototype is described by means of a BITFIELD_TEXTTABLE in the associated CompuMethod."; getter docstring = attribute Note verbatim (with closing period, markdown cell carries it); guarded setter docstring = attribute Note verbatim + "A None value is a no-op and does not overwrite an existing value."; shape mirrors prior-agent NumericalValueSpecification (multi-line triple-quoted); PEP 526 annotated member directly under its note comment, blank line between `__init__` attribute block and methods; Constants 156 + CommonStructure_init 163 total passed after rewrite
  - [x] Step 5 — Write reader/writer round-trip test (Red) — new tests/test_armodel/writer/test_writer_text_value_specification.py (3 tests, style of prior-agent test_writer_numerical_value_specification.py, AUTOSAR.getInstance().new() fixture): (1) write with SHORT-LABEL "tvs" + VALUE "ON" asserting the full child tag sequence == ["SHORT-LABEL", "VALUE"] (XSD 00052 complexType L122635 group order: AR-OBJECT + VALUE-SPECIFICATION + TEXT-VALUE-SPECIFICATION) and both field values; (2) empty-wrapper case — bare spec writes the tag with NO VALUE child; (3) write → ET serialize → namespace-inject → parser.getValueSpecification re-parse asserting isinstance TextValueSpecification + isinstance VerbatimString on getValue() + shortLabel "tvs" + value "ON" (field values + spec type fidelity, not len()); Red confirmed 1 failed/2 passed (test_text_value_specification_round_trip — reader getChildElementOptionalLiteral returns plain ARLiteral, isinstance VerbatimString False — genuine Red on spec-type fidelity; the 2 writer tests pass immediately — writer coverage pre-exists and is correct, no dropped field)
  - [x] Step 6 — Update parser & writer (Green) — reader arxml_parser.py getTextValueSpecification (L7936): single-line change `setValue(getChildElementOptionalLiteral(element, "VALUE"))` → `setValue(getChildElementOptionalVerbatimString(element, "VALUE"))` — spec-type fidelity fix matching the model's Optional[VerbatimString], same pattern as sibling VerbatimString readers (SwValues.vt L6678, RuleArguments.vt L7871); setValue/setShortLabel mutator form, no chaining, dispatched from the getValueSpecification tag dispatch (L7999-8000) and consumed at L7608 MetaDataItem.metaDataItemType; writer arxml_writer.py writeTextValueSpecification (L1769) NO CHANGE needed — already writes tag → writeValueSpecification base → setChildElementOptionalLiteral("VALUE", getValue()) in XSD order; setChildElementOptionalLiteral IS the established writer convention for VerbatimString fields (no setChildElementOptionalVerbatimString exists; SwValues.vt L1724, RuleArguments.vt L3293 all write via Literal helper — VerbatimString is an ARLiteral subclass), consumed from ArrayValueSpecification.elements (L1798), setChildValueSpecification polymorphic dispatch (L1853), RecordValueSpecification.fields (L3391); Rule 0013 matched-name pairs verified (readValueSpecification↔writeValueSpecification, setValue↔getValue, setShortLabel↔getShortLabel); observation: reader re-calls setShortLabel after readValueSpecification already set it — idempotent duplicate (setShortLabel None-guards), present on all value-spec siblings, left as-is; round-trip 3/3 + model 7/7 re-run green (10 passed)
  - [x] Step 7 — Update checklist comment — class-body checklist rewritten to 6-column Rule 0002 format: `# Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.113, p.436` + Columns legend + 3 rows source order (__init__ [—]/[—], getValue writer [x] — writer calls getValue/shortLabel getter, setValue reader [x] — reader calls setValue/setShortLabel), every row release R23-11; shortLabel accessor rows stay on the stamped base ValueSpecification checklist (base owns them); `# Spec verified:` marker NOT written (deferred to 9b/batch confirmation)
  - [x] Step 8 — Deviations — NO deviations: no placeholders, no missing members (table = single attr value, all modeled), no naming (ref/tref/aggr rules n/a), no type deviations remaining — reader's VALUE read upgraded ARLiteral → VerbatimString in Step 6 to match the spec Type column (pre-existing intake gap fixed, not an open deviation), reader+writer coverage complete, member order = displayed row order (single attribute); nothing to add to method_deviation_by_class*.md; observations recorded at Steps 1/6 (stamped base; idempotent setShortLabel re-read) are not spec deviations; `# Spec verified:` stamp WITHHELD pending 9b batch confirmation (Rule 0012.1)
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-24: target tests 10/10 (new test_TextValueSpecification.py 7 + new test_writer_text_value_specification.py 3), full suite 11356 passed/0 failed (prior-row baseline 11346 + 10 net-new: 7 model + 3 round-trip), npm run lint (flake8+ruff) clean, npm run black no-op (1163 files unchanged) + black-check clean, integration round-trip (29 ARXML) included in suite green; 9b deferred to batch confirmation (user instruction 2026-09-24)

- [ ] `ConstantReference` — ValueSpecification — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py
  - [x] Step 1 — Sync members & description from spec — Table 5.117 (AUTOSAR_CP_TPS_SoftwareComponentTemplate.md; page-split table: Class/Package/Note/Base header rows L12692-12696, title + attribute rows L12714-12720, p.441 via pdf_page.py); reproduction verified: R4.3.1 Table 5.132 (AUTOSAR_TPS_SoftwareComponentTemplate.md L10804) — identical Class/Package/Note/Base/attr Note text, only mult differs (R4.3.1 1 vs R23-11 0..1; R23-11 + XSD minOccurs=0 authoritative, Rule 0015); Class table: Package M2::AUTOSARTemplates::CommonStructure::Constants matches current file; class Note "Instead of defining this value inline, a constant is referenced." (verbatim confirmed by XSD 00052 group/complexType CONSTANT-REFERENCE documentation L22134/L22157); Base ARObject, ValueSpecification → most-derived base ValueSpecification — stamped `# Spec verified: R23-11` in this module; single attribute row: constant (ConstantSpecification, 0..1, ref, Note "The referenced constant.") → field name constantRef = spec base name + Kind ref→Ref (Rule 0001.5, existing name already correct); typed Optional[RefType] per stamped ref-sibling ReferenceValueSpecification (Table 5.115, same module); constr_1930 existence constraint is doc-level, not a model member; Aggregated-by list is consumer-side, not modeled. XSD 00052 ground truth: group CONSTANT-REFERENCE L22132 (single CONSTANT-REF minOccurs 0, AR:REF extension + DEST CONSTANT-SPECIFICATION--SUBTYPES-ENUM required) + complexType L22155 (AR-OBJECT + VALUE-SPECIFICATION + CONSTANT-REFERENCE groups → XML element order SHORT-LABEL, VARIATION-POINT then CONSTANT-REF); reader pre-exists (getConstantReference arxml_parser.py L7954 via readValueSpecification base helper + setConstantRef(getChildElementOptionalRefType "CONSTANT-REF"), tag dispatch getValueSpecification L8001) and writer pre-exists (setConstantReference arxml_writer.py L1812 via writeValueSpecification + setChildElementOptionalRefType("CONSTANT-REF", getConstantRef()); consumers L1855 setChildValueSpecification polymorphic dispatch + L3353/L3369 CompositeRuleBasedValueSpecification arguments/compound) — GAP FOUND: ConstantReference is missing from the writeArrayValueSpecification elements dispatch (arxml_writer.py L1788-1811) although Table 5.117 Aggregated-by includes ArrayValueSpecification.element and the reader handles CONSTANT-REFERENCE inside ELEMENTS via the generic tag dispatch → asymmetric round-trip (write hits notImplemented: raises, or logs-and-drops the element in warning mode); genuine Red candidate for Step 5; model layer is old-style: 4-col checklist without `# Spec:` line, fabricated class docstring, `__init__` docstring, `self.constantRef: RefType = None` non-Optional (Rule 0003), untyped setter param, no None-guard, no explicit chaining return → Steps 2–7 align
  - [x] Step 2 — Write model class unit test (Red) — new mirror file tests/test_armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/test_ConstantReference.py (7 tests, style of prior-agent test_NumericalValueSpecification.py / stamped ref-sibling ReferenceValueSpecification): inheritance isinstance ValueSpecification, initialization (constantRef/shortLabel None), typing.get_type_hints assert Optional[RefType] on getConstantRef return + setConstantRef param, getConstantRef initial None, setConstantRef round-trip with RefType asserting identity + chaining + ref value, setConstantRef(None) no-op, shortLabel base round-trip + None no-op; Red confirmed 2 failed/5 passed (test_constant_ref_annotation_is_optional — accessors carry no annotations, get_type_hints misses; test_set_constant_ref_none — setConstantRef(None) overwrites, no None-guard); honest note: the 5 behavioral tests pass immediately — the class pre-exists with constantRef/getConstantRef/setConstantRef (orphan intake, alignment pass); the genuine Reds are the unannotated accessors (Rule 0003) and the missing None-guard (stamped-sibling convention)
  - [x] Step 3 — Implement model class (Green) — member set per Table 5.117 already complete (single attr constant modeled as constantRef; no fabrication, no missing member, dedicated field not a registry filter); base ValueSpecification (most-derived, stamped) already provides shortLabel; Green edits: `self.constantRef: RefType = None` → `self.constantRef: Optional[RefType] = None`, getConstantRef return `Optional[RefType]`, setConstantRef param `Optional[RefType]` + explicit chaining return `-> ConstantReference` (stamped-sibling convention) + None-guard; mirror test 7/7 passed (0.13s); Step-3 referenced classes: none missing — RefType (PrimitiveTypes, imported), ConstantSpecification (referenced type, exists in same module, queued separately as the next row), ValueSpecification (same module, stamped)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — wiped ALL stale docstrings in the class (old fabricated class docstring "Represents a constant reference in AUTOSAR models. This class contains a reference to a constant…", `__init__` docstring "Initializes the ConstantReference with default values.", paraphrased getter "Gets the reference to the constant…"/setter "Sets the reference to the constant…" + Args/Returns blocks, stale inline member comment "Reference to the constant for this specification") then rewrote verbatim from Table 5.117 markdown: class docstring = class Note "Instead of defining this value inline, a constant is referenced."; `__init__` no docstring (Rule 0012.2.5.2) with inline member comment = attribute Note verbatim "The referenced constant."; getter docstring = attribute Note verbatim (markdown cell carries the closing period); guarded setter docstring = attribute Note verbatim + "A None value is a no-op and does not overwrite an existing constantRef."; shape mirrors stamped ref-sibling ReferenceValueSpecification (multi-line triple-quoted); PEP 526 annotated member directly under its note comment, blank line between `__init__` attribute block and methods; Constants model dir 72/72 after rewrite
  - [x] Step 5 — Write reader/writer round-trip test (Red) — new tests/test_armodel/writer/test_writer_constant_reference.py (4 tests, style of prior-agent test_writer_numerical_value_specification.py, AUTOSAR.getInstance().new() fixture): (1) write with SHORT-LABEL "crs" + CONSTANT-REF asserting the full child tag sequence == ["SHORT-LABEL", "CONSTANT-REF"] (XSD 00052 complexType L22155 group order: AR-OBJECT + VALUE-SPECIFICATION + CONSTANT-REFERENCE) + DEST attribute + both field values; (2) empty-wrapper case — bare spec writes the tag with NO CONSTANT-REF child; (3) write → ET serialize → namespace-inject → parser.getValueSpecification re-parse asserting isinstance ConstantReference + isinstance RefType on getConstantRef() + shortLabel "crs" + ref value + DEST (field values, not len()); (4) array case — ArrayValueSpecification.addElement(ConstantReference) → writeArrayValueSpecification → re-parse asserting the element round-trips as ConstantReference with its constantRef; Red confirmed 1 failed/3 passed — test_constant_reference_round_trip_in_array raises NotImplementedError "Unsupported element type of <ConstantReference> of ArrayValueSpecification" (writer elements dispatch L1788-1811 lacks the ConstantReference branch although Table 5.117 Aggregated-by includes ArrayValueSpecification.element and the reader reads it via the generic tag dispatch → asymmetric round-trip, genuine dropped field on write); honest note: the 3 direct tests pass immediately — reader/writer coverage pre-exists and is correct on the direct path (init-value consumers), no dropped field there
  - [x] Step 6 — Update parser & writer (Green) — READER arxml_parser.py NO CHANGE needed: getConstantReference (L7954) already reads via readValueSpecification base helper → setConstantRef(getChildElementOptionalRefType(element, "CONSTANT-REF")) (mutator form, no chaining — and unlike the Numerical/Text siblings it does not re-call setShortLabel after readValueSpecification, so no idempotent-duplicate observation here), dispatched from the getValueSpecification tag dispatch (L8001-8002) and reaches ArrayValueSpecification.elements through the generic per-child dispatch in getArrayValueSpecification; WRITER arxml_writer.py ONE CHANGE: added the missing `elif isinstance(sub_element, ConstantReference): self.setConstantReference(elements_tag, sub_element)` branch to the writeArrayValueSpecification elements dispatch (between TextValueSpecification and ArrayValueSpecification branches, mirroring the setChildValueSpecification dispatch order) — closes the Step 5 Red (NotImplementedError drop); setConstantReference (L1812) otherwise unchanged — tag → writeValueSpecification base → setChildElementOptionalRefType("CONSTANT-REF", getConstantRef()) in XSD order, other consumers L1855 setChildValueSpecification + L3353/L3369 CompositeRuleBasedValueSpecification arguments/compound untouched; Rule 0013 matched-name pairs verified (readValueSpecification↔writeValueSpecification, getConstantReference↔setConstantReference element pair, setConstantRef↔getConstantRef, setShortLabel↔getShortLabel); round-trip 4/4 + model 7/7 re-run green (11 passed)
  - [x] Step 7 — Update checklist comment — class-body checklist rewritten to 6-column Rule 0002 format: `# Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.117, p.441` + Columns legend + 3 rows source order (__init__ [—]/[—], getConstantRef writer [x] — writer calls getConstantRef, setConstantRef reader [x] — reader calls setConstantRef), every row release R23-11; shortLabel accessor rows stay on the stamped base ValueSpecification checklist (base owns them); `# Spec verified:` marker NOT written (deferred to 9b/batch confirmation)
  - [x] Step 8 — Deviations — NO deviations: no placeholders, no missing members (table = single attr constant, modeled as constantRef per Rule 0001.5), no naming (constant + Kind ref → Ref suffix correct), no type deviations (ref → RefType with DEST CONSTANT-SPECIFICATION--SUBTYPES-ENUM is the established mapped ref type, same as stamped siblings ReferenceValueSpecification.referenceValueRef and ConstantSpecificationMapping.appl/implConstantRef), reader+writer coverage complete (direct path pre-existing; ArrayValueSpecification.elements writer dispatch gap closed in Step 6), member order = displayed row order (single attribute); no ConstantReference entries in docs/examples/method_deviation_by_class*.md and nothing to add; observations recorded at Steps 1/5 (stamped base; array-dispatch gap — fixed, not open) are not open deviations; `# Spec verified:` stamp WITHHELD pending 9b batch confirmation (Rule 0012.1)
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-24: target tests 11/11 (new test_ConstantReference.py 7 + new test_writer_constant_reference.py 4), full suite 11367 passed/0 failed (prior-row baseline 11356 + 11 net-new: 7 model + 4 round-trip), npm run lint (flake8+ruff) clean, npm run black no-op (1165 files unchanged) + black-check clean, integration round-trip (29 ARXML) included in suite green; 9b deferred to batch confirmation (user instruction 2026-09-24)

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
