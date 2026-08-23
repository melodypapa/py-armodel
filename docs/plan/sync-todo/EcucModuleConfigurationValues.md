# Sync Queue: EcucModuleConfigurationValues

Input class: `EcucModuleConfigurationValues`
Spec source (all classes): `autosar/markdown/AUTOSAR_CP_TPS_ECUConfiguration.md` (`AUTOSAR_CP_TPS_ECUConfiguration.pdf`)
Release target: R23-11
Created: 2026-08-23
Source file for all queued classes: `src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py`

## Closure (confirmed by user 2026-08-23)

| Class | Role | Base | Spec | Notes |
|-------|------|------|------|-------|
| EcucConfigurationVariantEnum | member (attr `implementationConfigVariant`) | AREnum | Table 2.13 | STUB — `super().__init__([])` with no literals. Spec literals: Recommended Configuration, VariantLinkTime, VariantPostBuild, VariantPreCompile |
| EcucParameterValue | member (aggr `parameterValue` of ContainerValue) | ARObject, EcucIndexableValue (abstract) | Table 2.49 | attrs: definition (ref), isAutoValue (Boolean). NOTE: markdown table lacks Note/Base/Package rows (conversion artifact) — handle in Step 1 |
| EcucTextualParamValue | member subclass | …, EcucParameterValue | Table 2.50 | value: VerbatimString. Existing impl uses `# type:` comments; paraphrased docstrings |
| EcucNumericalParamValue | member subclass | …, EcucParameterValue | Table 2.51 | value: Numerical (atpVariation) |
| EcucAddInfoParamValue | member subclass | …, EcucParameterValue | Table 2.52 | value: DocumentationBlock (aggr) |
| EcucAbstractReferenceValue | member (aggr `referenceValue` of ContainerValue) | ARObject, EcucIndexableValue (abstract) | Table 2.53 | attrs: annotation (Annotation *), definition (ref), isAutoValue (Boolean) |
| EcucReferenceValue | member subclass | …, EcucAbstractReferenceValue | Table 2.54 | value: Referrable (ref) → RefType in model |
| EcucInstanceReferenceValue | member subclass | …, EcucAbstractReferenceValue | Table 2.55 | value: AtpFeature (iref, impl by AnyInstanceRef). BUG: `getValueIRef()` returns `self.valueRef` |
| EcucContainerValue | member (aggr `container` * of input) | ARObject, EcucIndexableValue, Identifiable, MultilanguageReferrable, Referrable | Table 2.48 | attrs: definition (ref EcucContainerDef), parameterValue (*), referenceValue (*), subContainer (* recursive). `getReferenceValues()` return type wrong (`EcucAbstractReferenceValue` instead of List) |
| EcucModuleConfigurationValues | **input** | ARElement chain (most-derived: ARElement) | Table 2.47, p.111 | attrs: container (aggr *), definition (ref EcucModuleDef), ecucDefEdition (RevisionLabelString), implementationConfigVariant (EcucConfigurationVariantEnum), moduleDescription (ref BswImplementation), postBuildVariantUsed (Boolean). Deprecated aliases (getDefinitionRef/setDefinitionRef/getModuleDescriptionRef/setModuleDescriptionRef + properties) not in spec; `implementationConfigVariant` typed ARLiteral not enum; docstrings paraphrased |

### Referenced-only (NOT queued)
- Already stamped `R23-11`: EcucIndexableValue (Table 2.46), BswImplementation (BSW TPS Table 6.1)
- Shared base infra: ARObject, Referrable, MultilanguageReferrable, CollectableElement, Identifiable, PackageableElement, ARElement
- Ref targets (exist, referenced as RefType): EcucModuleDef (Table 2.2 — has unstamped checklist; own pass later), EcucContainerDef / EcucParamConfContainerDef / EcucChoiceContainerDef, EcucAbstractReferenceDef, EcucParameterDef
- Primitives (PrimitiveTypes.py): RevisionLabelString, Boolean/ARBoolean, VerbatimString, Numerical/ARNumerical, PositiveInteger
- Infra: Annotation (MSR Documentation), AnyInstanceRef, DocumentationBlock

## Queue (dependency-first — one class per fresh session, Rule 0017)

- [x] EcucConfigurationVariantEnum (7913144 — resolved as duplicate stub removal; canonical stays ECUCParameterDefTemplate.py R23-11)
  - [x] Step 1 — Sync members & description from spec (RESOLVED: duplicate stub — canonical class in ECUCParameterDefTemplate.py:397 already stamped R23-11 w/ verbatim literals; user chose removal)
  - [x] Step 2 — Write model class unit test (N/A — no new code; canonical tests cover literals; regression verified)
  - [x] Step 3 — Implement model class (Green — stub deleted from ECUCDescriptionTemplate.py; AREnum import removed; test imports redirected; 130 tests pass)
  - [x] Step 4 — Sync docstrings (N/A — canonical docstrings untouched; stub removed)
  - [x] Step 5 — N/A (standalone AREnum — serialized as attribute value on consuming class, Rules 0010–0011)
  - [x] Step 6 — N/A (standalone AREnum)
  - [x] Step 7 — Update checklist comment (pointer comment left at removal site; canonical checklist+stamp unchanged)
  - [x] Step 8 — Deviations (duplicate-resolution recorded here instead of new sync)
  - [x] Step 9 — Verify (9a) + confirm (9b) ⇒ write # Spec verified: R23-11 (resolved by duplicate removal — canonical already stamped R23-11; no new code to stamp)
- [x] EcucParameterValue (221669a)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite verbatim)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment (# Spec: line + rows; marker deferred to 9b)
  - [x] Step 8 — Deviations (none expected)
  - [x] Step 9 — Verify (9a) + confirm (9b) ⇒ write # Spec verified: R23-11 (confirmed 2026-08-23 — marker at ECUCDescriptionTemplate.py; commit 221669a)
- [x] EcucTextualParamValue (cbfd622)
  - [x] Step 1 — Sync members & description from spec (Table 2.50 p.127; Base ARObject/EcucIndexableValue/EcucParameterValue; single attr value: VerbatimString 0..1)
  - [x] Step 2 — Write model class unit test (Red — chaining/None no-op/VerbatimString + verbatim docstring assertions failed first)
  - [x] Step 3 — Implement model class (Green — value retyped ARLiteral→VerbatimString per spec, PEP 526 annotation, chaining + None guard)
  - [x] Step 4 — Sync docstrings (wipe + rewrite verbatim: class Note, inline __init__ comment, getter/setter docstrings)
  - [x] Step 5 — Write reader/writer round-trip test (Red — parser materialized plain ARLiteral; VerbatimString isinstance failed)
  - [x] Step 6 — Update parser & writer (Green — reader switched to getChildElementOptionalVerbatimString; writer unchanged)
  - [x] Step 7 — Update checklist comment (# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.50, p.127; marker deferred to 9b)
  - [x] Step 8 — Deviations (none — value modeled verbatim per Table 2.50; no flattening; no placeholders)
  - [x] Step 9 — Verify (9a done: pytest 6922/flake8/ruff/black clean; parity gap pre-existing unrelated) + confirm (9b) (confirmed 2026-08-23 — marker at ECUCDescriptionTemplate.py; commit cbfd622)
- [x] EcucNumericalParamValue (7064a79)
  - [x] Step 1 — Sync members & description from spec (Table 2.51 p.128; Base ARObject/EcucIndexableValue/EcucParameterValue; single attr value: Numerical 0..1)
  - [x] Step 2 — Write model class unit test (Red — chaining/None no-op/Numerical isinstance/verbatim docstrings failed first)
  - [x] Step 3 — Implement model class (Green — value retyped ARNumerical→Numerical per spec Table 2.51, PEP 526 annotation, chaining + None guard)
  - [x] Step 4 — Sync docstrings (wipe + rewrite verbatim: class Note, inline __init__ comment incl. atpVariation tail, getter/setter docstrings)
  - [x] Step 5 — Write reader/writer round-trip test (Red — parser materialized ARNumerical; writer hit missing getShortLabel on Numerical)
  - [x] Step 6 — Update parser & writer (Green — new getChildElementOptionalNumerical helper; writer switched to setChildElementOptionalLiteral)
  - [x] Step 7 — Update checklist comment (# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.51, p.128; marker deferred to 9b)
  - [x] Step 8 — Deviations (none)
  - [x] Step 9 — Verify (9a done: pytest 6928/flake8/ruff/black clean) + confirm (9b) (confirmed 2026-08-23 — marker at ECUCDescriptionTemplate.py; commit 7064a79)
- [x] EcucAddInfoParamValue (e21f504)
  - [x] Step 1 — Sync members & description from spec (Table 2.52 p.129; single attr value: DocumentationBlock 0..1 aggr)
  - [x] Step 2 — Write model class unit test (Red — chaining/None no-op/verbatim docstring tests failed first)
  - [x] Step 3 — Implement model class (Green — value typed Optional[DocumentationBlock] per Table 2.52, PEP 526 annotation, chaining + None guard)
  - [x] Step 4 — Sync docstrings (wipe + rewrite verbatim: class Note, inline __init__ comment, getter/setter docstrings)
  - [x] Step 5 — Write reader/writer round-trip test (Red — parser AttributeError, writer NotImplementedError seen first)
  - [x] Step 6 — Update parser & writer (Green — getEcucAddInfoParamValue via getDocumentationBlock; setEcucAddInfoParamValue via writeDocumentationBlock; dispatch branches added)
  - [x] Step 7 — Update checklist comment (# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.52, p.129; marker deferred to 9b)
  - [x] Step 8 — Deviations (none; tracker entry added, stale Textual/Numerical type rows cleared)
  - [x] Step 9 — Verify (9a done: pytest 6936/flake8/ruff/black clean; parity script pass) + confirm (9b) (confirmed 2026-08-23 — marker at ECUCDescriptionTemplate.py; commit e21f504)
- [x] EcucAbstractReferenceValue (0c65ebd)
  - [x] Step 1 — Sync members & description from spec (Table 2.53 p.131; markdown line-break artifact repaired in `definition` Note; annotation Note differs from Table 2.49 wording — "a model element (e.g.")
  - [x] Step 2 — Write model class unit test (Red — setDefinition AttributeError, None no-op + verbatim docstring tests failed first)
  - [x] Step 3 — Implement model class (Green shape — `definitionRef`/`getDefinitionRef`/`setDefinitionRef` kept with Kind-`ref` Ref suffix per Rule 0001.5, Optional[Boolean] per Table 2.53, PEP 526 annotations, chaining + None guard; none_no_op passes)
  - [x] Step 4 — Sync docstrings (wipe + rewrite verbatim: class Note, inline __init__ comments incl. Tags tail, getter/setter docstrings; 27 model tests green)
  - [x] Step 5 — Write reader/writer round-trip test (Red — IS-AUTO-VALUE dropped by reader/writer; renamed accessors AttributeError)
  - [x] Step 6 — Update parser & writer (Green — readEcucAbstractReferenceValue/writeEcucAbstractReferenceValue: Ref-suffix accessors + IS-AUTO-VALUE read/write added; order aligned DEFINITION-REF, INDEX, ANNOTATIONS, IS-AUTO-VALUE; stale test call sites updated; full suite 6942 green)
  - [x] Step 7 — Update checklist comment (# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.53, p.131; 5-column rows; marker deferred to 9b)
  - [x] Step 8 — Deviations recorded (none — tracker type/naming rows fixed & removed; see decisions below)
  - [x] Step 9 — Verify (9a done: pytest 6942/flake8/ruff/black clean; parity no new gaps) + confirm (9b) (confirmed 2026-08-23 — Ref-suffix correction applied in review; marker at ECUCDescriptionTemplate.py:253; commit 0c65ebd)
- [x] EcucReferenceValue (f35eb73)
  - [x] Step 1 — Sync members & description from spec (Table 2.54 p.132; single attr value: Referrable 0..1 ref → valueRef/getValueRef/setValueRef Optional[RefType]; markdown line-break artifact repaired via XSD doc; XSD order confirms VALUE-REF after abstract group)
  - [x] Step 2 — Write model class unit test (Red — none_no_op + class/member verbatim docstring tests failed first)
  - [x] Step 3 — Implement model class (Green shape — PEP 526 annotation, Optional[RefType] getter/setter, None guard + chaining; none_no_op passes)
  - [x] Step 4 — Sync docstrings (wipe + rewrite verbatim: class Note, inline __init__ comment, getter/setter docstrings; 29 model tests green)
  - [x] Step 5 — Write reader/writer round-trip test (Red — empty ECUC-REFERENCE-VALUE wrapper emitted by writer; parser DEST assertion added; 5 tests Red→Green)
  - [x] Step 6 — Update parser & writer (Green — setEcucReferenceValue omits empty wrapper to match writeEcucAbstractReferenceValue empty-omit semantics; 5 tests pass)
  - [x] Step 7 — Update checklist comment (# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.54, p.132; 5-column rows; marker deferred to 9b)
  - [x] Step 8 — Deviations (none — no placeholders; stamp granted)
  - [x] Step 9 — Verify (9a done: pytest 3199+185/flake8/ruff/black clean; integration round-trip pass) + confirm (9b) ⇒ # Spec verified: R23-11 (confirmed — marker at ECUCDescriptionTemplate.py; commit f35eb73)
- [x] EcucInstanceReferenceValue (93b6df3)
  - [x] Step 1 — Sync members & description from spec (Table 2.55 p.134; Base ARObject/EcucAbstractReferenceValue/EcucIndexableValue; single attr value: AtpFeature 0..1 iref → valueIRef/AnyInstanceRef)
  - [x] Step 2 — Write model class unit test (Red — valueIRef field/docstring/None-no-op/verbatim tests failed first)
  - [x] Step 3 — Implement model class (Green — valueIRef retyped; PEP 526 annotation Optional[AnyInstanceRef]; chaining + None guard; bug fixed: getValueIRef/setValueIRef now use valueIRef not valueRef)
  - [x] Step 4 — Sync docstrings (wipe + rewrite verbatim: class Note, inline __init__ comment, getter/setter docstrings)
  - [x] Step 5 — Write reader/writer round-trip test (Red → Green — parser tests value.valueRef updated to getValueIRef; new write→read round-trip asserts base/target/definition refs)
  - [x] Step 6 — Update parser & writer (Green — reader/writer already call getValueIRef/setValueIRef; no source change needed; stale test call sites fixed)
  - [x] Step 7 — Update checklist comment (# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.55, p.134; 5-column rows; marker deferred to 9b)
  - [x] Step 8 — Deviations (none — bug fixed, no placeholders; no deviation rows)
  - [x] Step 9 — Verify (9a done: pytest 6950/flake8/ruff/black clean) + confirm (9b) ⇒ # Spec verified: R23-11 (confirmed — marker at ECUCDescriptionTemplate.py; commit 93b6df3)
- [x] EcucContainerValue (724ee43)
  - [x] Step 1 — Sync members & description from spec (Table 2.48 p.119; Base ARObject/EcucIndexableValue/Identifiable; attrs definition ref, parameterValue aggr *, referenceValue aggr *, subContainer aggr *)
  - [x] Step 2 — Write model class unit test (Red — none_no_op + verbatim docstring tests failed first)
  - [x] Step 3 — Implement model class (Green — PEP 526 annotations, Optional[RefType] definitionRef, List typed fields, None no-op guard on setDefinitionRef, fixed getReferenceValues return type)
  - [x] Step 4 — Sync docstrings (wipe + rewrite verbatim: class Note, inline __init__ comments, getter/setter docstrings)
  - [x] Step 5 — Write reader/writer round-trip test (Red→Green — write→re-parse asserts all four attributes)
  - [x] Step 6 — Update parser & writer (Green — no source change needed; reader/writer already cover all four attrs, verified by round-trip)
  - [x] Step 7 — Update checklist comment (# Spec: AUTOSAR_CP_TPS_ECUConfiguration.pdf, Table 2.48, p.119; 5-column rows; marker deferred to 9b)
  - [x] Step 8 — Deviations (none — fully modeled per Table 2.48; Ref-suffix naming per Rule 0001.5)
  - [x] Step 9 — Verify (9a done: pytest 6956/flake8/ruff/black clean) + confirm (9b) ⇒ # Spec verified: R23-11 (marker at ECUCDescriptionTemplate.py)
- [x] EcucModuleConfigurationValues (a7994a6)
  - [x] Step 1 — Sync members & description from spec (Table 2.47 p.111; markdown line-break artifacts repaired in Notes)
  - [x] Step 2 — Write model class unit test (Red — none_no_op + verbatim docstring tests failed first)
  - [x] Step 3 — Implement model class (Green — spec types RevisionLabelString/EcucConfigurationVariantEnum/Boolean; None no-op guards)
  - [x] Step 4 — Sync docstrings (wipe + rewrite verbatim: class Note+Tags, inline __init__ comments, getter/setter docstrings)
  - [x] Step 5 — Write reader/writer round-trip test (Red — RevisionLabelString isinstance failed against ARLiteral reader)
  - [x] Step 6 — Update parser & writer (Green — spec-name setters/getters + getChildElementOptionalRevisionLabelString)
  - [x] Step 7 — Update checklist comment (# Spec: line + rows; marker deferred to 9b)
  - [x] Step 8 — Deviations recorded (see below)
  - [x] Step 9 — Verify (9a done: pytest 6850/flake8/ruff/black clean) + confirm (9b) (confirmed — marker written ECUCDescriptionTemplate.py:366; commit a7994a6)

### Deviations / decisions (EcucParameterValue)
1. No deviations. `definition` ref target modeled as `RefType` per project convention (spec type EcucParameterDef); spec-named accessors `getDefinition`/`setDefinition` replace `*DefinitionRef` (no deprecated aliases kept — no external consumers found outside parser/writer/tests).
2. Reader/writer coverage completed: `IS-AUTO-VALUE` read (`getChildElementOptionalBooleanValue`) / written (`setChildElementOptionalBooleanValue`) newly added; `ANNOTATIONS` wrapper coverage pre-existed. Emission/read order aligned to XSD sequenceOffset: DEFINITION-REF (-10), INDEX (-5), ANNOTATIONS (+10), IS-AUTO-VALUE (+20).
3. `isAutoValue` typed `Optional[Boolean]` (XSD AR:BOOLEAN) replacing bare `ARBoolean`; all setters/add guard None (Rule 0004).

### Deviations / decisions (EcucModuleConfigurationValues)
1. Deprecated backward-compat conveniences kept (NOT in Table 2.47): get/setDefinitionRef, get/setModuleDescriptionRef methods + definitionRef/moduleDescriptionRef properties. Spec-named members are canonical; aliases delegate to them; marked [—] (no XML element).
2. implementationConfigVariant is read via getChildElementOptionalLiteral (value stored as ARLiteral value-form per project convention for enums on this side); field typed Optional[EcucConfigurationVariantEnum].
3. getContainers sorts the dedicated typed list by short_name per TPS_ECUC_06067 secondary criterion (primary index criterion lives on EcucIndexableValue rows).

### Deviations / decisions (EcucAbstractReferenceValue)
1. No deviations. Kind-`ref` Ref suffix applied per Rule 0001.5: field `definitionRef`, accessors `getDefinitionRef`/`setDefinitionRef` (an intermediate rename to spec-named `getDefinition`/`setDefinition` was reverted in 9b review — the stamped siblings `EcucParameterValue` and `EcucModuleConfigurationValues` carry that opposite naming convention and are flagged as Rule 0001.5 drift candidates for a future re-sync pass; NOT touched in this session).
2. `isAutoValue` retyped `ARBoolean` → `Optional[Boolean]` per Table 2.53; None no-op guards on all setters/add.
3. Reader/writer: `IS-AUTO-VALUE` read/write newly added (present in R23-11 XSD `AUTOSAR_00052.xsd` group ECUC-ABSTRACT-REFERENCE-VALUE; absent from older CP 4.4 XSD); emission/read order aligned DEFINITION-REF (-10), INDEX (-5), ANNOTATIONS (+10), IS-AUTO-VALUE (+20).

### Deviations / decisions (EcucAddInfoParamValue)
1. No deviations. Single attr `value` modeled as `Optional[DocumentationBlock]` (Table 2.52: DocumentationBlock 0..1 aggr); setter guards None and chains. Reader/writer reuse the matched `getDocumentationBlock`/`writeDocumentationBlock` pair (Rule 0013.2); `ECUC-ADD-INFO-PARAM-VALUE` dispatch branch added on both sides of `EcucContainerValue.parameterValue`. Tracker: entry added with "No deviations"; stale fixed rows for EcucTextualParamValue/EcucNumericalParamValue removed.
