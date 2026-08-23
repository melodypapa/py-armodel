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
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write # Spec verified: R23-11
- [ ] EcucParameterValue
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite verbatim)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec: line + rows; marker deferred to 9b)
  - [ ] Step 8 — Deviations (none expected)
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write # Spec verified: R23-11
- [ ] EcucTextualParamValue
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite verbatim)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec: line + rows; marker deferred to 9b)
  - [ ] Step 8 — Deviations (none expected)
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write # Spec verified: R23-11
- [ ] EcucNumericalParamValue
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite verbatim)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec: line + rows; marker deferred to 9b)
  - [ ] Step 8 — Deviations (none expected)
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write # Spec verified: R23-11
- [ ] EcucAddInfoParamValue
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite verbatim)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec: line + rows; marker deferred to 9b)
  - [ ] Step 8 — Deviations (none expected)
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write # Spec verified: R23-11
- [ ] EcucAbstractReferenceValue
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite verbatim)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec: line + rows; marker deferred to 9b)
  - [ ] Step 8 — Deviations (none expected)
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write # Spec verified: R23-11
- [ ] EcucReferenceValue
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite verbatim)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec: line + rows; marker deferred to 9b)
  - [ ] Step 8 — Deviations (none expected)
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write # Spec verified: R23-11
- [ ] EcucInstanceReferenceValue
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite verbatim)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec: line + rows; marker deferred to 9b)
  - [ ] Step 8 — Deviations (fix getValueIRef returning self.valueRef)
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write # Spec verified: R23-11
- [ ] EcucContainerValue
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite verbatim)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment (# Spec: line + rows; marker deferred to 9b)
  - [ ] Step 8 — Deviations (none expected)
  - [ ] Step 9 — Verify (9a) + confirm (9b) ⇒ write # Spec verified: R23-11
- [x] EcucModuleConfigurationValues (a7994a6)
  - [x] Step 1 — Sync members & description from spec (Table 2.47 p.111; markdown line-break artifacts repaired in Notes)
  - [x] Step 2 — Write model class unit test (Red — none_no_op + verbatim docstring tests failed first)
  - [x] Step 3 — Implement model class (Green — spec types RevisionLabelString/EcucConfigurationVariantEnum/Boolean; None no-op guards)
  - [x] Step 4 — Sync docstrings (wipe + rewrite verbatim: class Note+Tags, inline __init__ comments, getter/setter docstrings)
  - [x] Step 5 — Write reader/writer round-trip test (Red — RevisionLabelString isinstance failed against ARLiteral reader)
  - [x] Step 6 — Update parser & writer (Green — spec-name setters/getters + getChildElementOptionalRevisionLabelString)
  - [x] Step 7 — Update checklist comment (# Spec: line + rows; marker deferred to 9b)
  - [x] Step 8 — Deviations recorded (see below)
  - [ ] Step 9 — Verify (9a done: pytest 6850/flake8/ruff/black clean) + confirm (9b)

### Deviations / decisions (EcucModuleConfigurationValues)
1. Deprecated backward-compat conveniences kept (NOT in Table 2.47): get/setDefinitionRef, get/setModuleDescriptionRef methods + definitionRef/moduleDescriptionRef properties. Spec-named members are canonical; aliases delegate to them; marked [—] (no XML element).
2. implementationConfigVariant is read via getChildElementOptionalLiteral (value stored as ARLiteral value-form per project convention for enums on this side); field typed Optional[EcucConfigurationVariantEnum].
3. getContainers sorts the dedicated typed list by short_name per TPS_ECUC_06067 secondary criterion (primary index criterion lives on EcucIndexableValue rows).
