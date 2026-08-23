# Sync todo: ReferenceValueSpecification

Input classes: ReferenceValueSpecification, NotAvailableValueSpecification, ConstantSpecificationMapping, SwValues, RuleBasedAxisCont, NumericalRuleBasedValueSpecification · Generated: 2026-08-23 · Queue order = row order
(resume = first class row still `[ ]`; all class rows `[x]` = sync finished)

Spec source for all rows unless noted: `autosar/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md`
(PositiveInteger: `autosar/markdown/AUTOSAR_FO_TPS_GenericStructureTemplate.md`).

## Queue (dependency-first)

- [x] AbstractRuleBasedValueSpecification (base of NumericalRuleBasedValueSpecification · markdown · Table 5.128 · exists, no `# Spec:` line — stub sync; abstract, empty Attribute section) · commit a9112840
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: abstract class has no own XML tag
  - [x] Step 6 — Update parser & writer (Green) — N/A: no own XML tag; serialized via concrete subclasses
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [x] PositiveInteger (member · markdown Table E.64, FO_TPS_GST · pulled by NotAvailableValueSpecification.defaultPattern · exists unstamped in `PrimitiveTypes.py`; Steps 5/6 likely N/A — primitive has no own XML element, round-trips as attribute value on the consuming class) · commit 51136e44
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: primitive has no own XML element
  - [x] Step 6 — Update parser & writer (Green) — N/A: serialized as value on consuming classes; covered by their round-trips
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [x] ValueGroup (member · markdown · Table 5.126 · pulled by SwValues.vg · absent from codebase — create in `MSR/CalibrationData/CalibrationValue.py`) · commit fc3d99da
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [x] ValueList (member · markdown · Table 5.127 · pulled by RuleBasedAxisCont.swArraysize · exists unstamped in `MSR/DataDictionary/DataDefProperties.py` — current `getVfs()` sorts but spec marks `vf (ordered)`; verify against spec) · commit c49ebbc2
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [x] ReferenceValueSpecification (input · markdown · Table 5.115 · `CommonStructure/Constants/__init__.py`) · commit e97c1b37
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] NotAvailableValueSpecification (input · markdown · Table 5.116 · `CommonStructure/Constants/__init__.py`) · commit dcc5fb59
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] ConstantSpecificationMapping (input · markdown · Table 5.118 · `CommonStructure/Constants/__init__.py`)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] SwValues (input · markdown · Table 5.125 · `MSR/CalibrationData/CalibrationValue.py`)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] RuleBasedAxisCont (input · markdown · Table 5.130 · `CommonStructure/Constants/__init__.py`)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] NumericalRuleBasedValueSpecification (input · markdown · Table 5.132 · `CommonStructure/Constants/__init__.py`)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

## Not queued

- ValueSpecification — already stamped `# Spec verified: R23-11` (Table 5.109); base of ReferenceValueSpecification / NotAvailableValueSpecification / AbstractRuleBasedValueSpecification.
- DataPrototype — already stamped R23-11; member type of ReferenceValueSpecification.referenceValue.
- ConstantSpecification — already stamped R23-11; member type of ConstantSpecificationMapping.applConstant/implConstant.
- Numerical — already stamped R23-11 (Table E.58 FO_TPS_GST); member type of SwValues.v/vf.
- VerbatimString — already stamped R23-11; member type of SwValues.vt.
- NumericalOrText — already stamped R23-11; member type of SwValues.vtf.
- CalprmAxisCategoryEnum — already stamped R23-11; member type of RuleBasedAxisCont.category.
- RuleBasedValueSpecification — already stamped R23-11; member type of RuleBasedAxisCont.ruleBasedValues and NumericalRuleBasedValueSpecification.ruleBasedValues.
- AxisIndexType — already stamped R23-11; member type of RuleBasedAxisCont.swAxisIndex.
- Unit — already stamped R23-11; member type of RuleBasedAxisCont.unit.

## Decisions (16.4)

None — every closure class was found in the spec markdown; no Skip/XSD-derived resolutions needed.
