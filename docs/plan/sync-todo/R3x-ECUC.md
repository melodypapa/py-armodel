# Sync todo: Group R3x — Legacy R3.2.3 ECUC (TOP-LEVEL-PACKAGES / MODULE-CONFIGURATION)

Input: R3.2.3 legacy spec `autosar/R3.2.3/pdf/AUTOSAR_ECU_Configuration.pdf` (V2.5.0 R3.2 Rev 3) + `autosar/R3.2.3/xsd/AUTOSAR.xsd` · Trigger: `tests/integration_tests/test_files/Os_ECUC.arxml` fails round-trip (parses 0 packages — legacy `TOP-LEVEL-PACKAGES` + `MODULE-CONFIGURATION` format unsupported) · Generated: 2026-09-19 · Queue order = row order (resume = first class row still `[ ]` — Rule 0017)

> **Release-scope rules for this group:**
> 1. Spec citations use `R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table N.M, p.P (R3.2 Rev 3)`; XSD evidence cites `autosar/R3.2.3/xsd/AUTOSAR.xsd` line numbers.
> 2. Stamp marker: `# Spec verified: R3.2.3` (these classes do NOT exist in R4+ specs — R23-11 TPS has zero occurrences of `TOP-LEVEL-PACKAGES`/`MODULE-CONFIGURATION`; verified against all 15 R23-11 PDFs 2026-09-19).
> 3. Rule 0019 applies inverted: spec Mul=1 but XSD `minOccurs="0"` → implement optional (XSD + Os_ECUC.arxml sample evidence wins for legacy format).
> 4. No class-name collisions (checked 2026-09-19: none of the 13 names below exists in `src/armodel/models`).
> 5. Goal gate: `Os_ECUC.arxml` passes full round-trip (parse → write → re-parse → compare). Do NOT exclude it via `config.yaml` — superseded by this group.

## Infrastructure prerequisites (non-class, before Step 2 of first class) — DONE 2026-09-19

- [x] `AUTOSAR.setARRelease('3.2.3')` — add `"3.2.3": "autosar.xsd"` to `release_xsd_mappings` ([AutosarTopLevelStructure/__init__.py](file:///Users/ray/Workspace/py-armodel/src/armodel/models/M2/AUTOSARTemplates/AutosarTopLevelStructure/__init__.py) L151-L168); `setARRelease` L460 must emit `http://autosar.org autosar.xsd` (R3 namespace, NOT `/schema/r4.0`) for 3.2.3
- [x] Namespace detection — `AbstractARXMLParser.nsmap` is hardcoded `http://autosar.org/schema/r4.0` ([abstract_arxml_parser.py](file:///Users/ray/Workspace/py-armodel/src/armodel/parser/abstract_arxml_parser.py) L41): detect root ns in `load()` (e.g. `{http://autosar.org}AUTOSAR` → nsmap `http://autosar.org`)
- [x] `readARPackages` fallback — accept `TOP-LEVEL-PACKAGES/*` when `AR-PACKAGES` absent ([arxml_parser.py](file:///Users/ray/Workspace/py-armodel/src/armodel/parser/arxml_parser.py) L13037-L13044); writer mirror in `writeARPackages` ([arxml_writer.py](file:///Users/ray/Workspace/py-armodel/src/armodel/writer/arxml_writer.py) L12759) — emit `TOP-LEVEL-PACKAGES` wrapper when release is 3.2.3. **Extra (XSD L270):** nested R3 packages use `SUB-PACKAGES` (parser fallback + writer `_legacy_namespace` wrapper); legacy root skips FILE-INFO-COMMENT/INTRODUCTION (R3 root = ADMIN-DATA → TOP-LEVEL-PACKAGES only)
- [x] `detect_autosar_version` in [test_roundtrip.py](file:///Users/ray/Workspace/py-armodel/tests/integration_tests/test_roundtrip.py) L179-193: map `http://autosar.org autosar.xsd` → `3.2.3` — implemented in [conftest.py](file:///Users/ray/Workspace/py-armodel/tests/integration_tests/conftest.py) `xsd_to_version_mapping` (the mapping lives there)

> Smoke result 2026-09-19: Os_ECUC.arxml parses to 1 package (`Os`) with warning=True; writer emits legacy ns + `TOP-LEVEL-PACKAGES`; R4 files unaffected. Suite: 9451 unit PASS, integration 130/131 — Os_ECUC red at parse (`Unsupported <MODULE-CONFIGURATION>`) until the class queue below is done (goal gate).

## Queue (dependency-first)

- [x] `ParameterValue` (abstract) — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.32, p.97 (R3.2 Rev 3) — DONE 2026-09-19, commit `ba944c20`
  - **Step 1 finding:** Base row = `ARObject` (NOT Identifiable — no SHORT-NAME). Members: `definition` (ConfigParameter, 1, ref, Tags: `xml.sequenceOffset=-10`). XML: abstract parent of all `*-VALUE` elements; each concrete value element = `DEFINITION-REF` + `VALUE`. Placement: leaf module [ECUCDescriptionTemplate.py](file:///Users/ray/Workspace/py-armodel/src/armodel/models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py) (spec package M2::AUTOSARTemplates::ECUCDescriptionTemplate — same leaf, Rule 0007 OK; no subpackage churn).
  - **Step 8 deviations (recorded):** ① `definition` optional — spec Mul=1 but XSD group PARAMETER-VALUE (AUTOSAR.xsd L18140) minOccurs="0" (Rule 0019.3 inverted); renamed to `definitionRef` per ECUC ref-suffix convention. ② DEFINITION-REF DEST — XSD use="required" but Os_ECUC.arxml carries no DEST; reader/writer treat DEST as optional.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — abstract: reader/writer via concrete subclasses only (test-local `_R3ParameterValueStub`)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — 2 recorded (see above; "none expected" pre-check was inaccurate)
  - [x] Step 9 — Verify (9a: 9461 passed, lint/black clean) + confirm (9b user OK 2026-09-19)
- [x] `IntegerValue` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.34, p.98 (R3.2 Rev 3) — DONE 2026-09-19, commit `7492972b`
  - **Step 1 finding:** Base = `ParameterValue`. Members: `value` (UnlimitedInteger, 1, attr). XML `INTEGER-VALUE`: `DEFINITION-REF` → `VALUE` (XSD group L13673; value minOccurs=0 — file has `<VALUE>5</VALUE>`; spec Mul=1 → deviation note Rule 0019.3). 33× in Os_ECUC.arxml. Reader/writer: `PARAMETER-VALUES` container inside `CONTAINER`.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — `value` optional per XSD minOccurs=0 (spec says 1)
  - [x] Step 9 — Verify (9a: 9471 passed, lint/black clean) + confirm (9b user OK 2026-09-19)
- [x] `BooleanValue` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.33, p.97 (R3.2 Rev 3) — DONE 2026-09-19, commit `bb87f12d`
  - **Step 1 finding:** Base = `ParameterValue`. Members: `value` (Boolean, 1, attr). XML `BOOLEAN-VALUE` (XSD group L1544, value minOccurs=0). 25× in Os_ECUC.arxml (`<VALUE>false</VALUE>`).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — `value` optional per XSD (spec says 1)
  - [x] Step 9 — Verify (9a: 9481 passed, lint/black clean) + confirm (9b user OK 2026-09-19)
- [ ] `FloatValue` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.35, p.99 (R3.2 Rev 3)
  - **Step 1 finding:** Base = `ParameterValue`. Members: `value` (Float, 1, attr). XML `FLOAT-VALUE` (XSD group L11254). 2× in Os_ECUC.arxml.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations — `value` optional per XSD (spec says 1)
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `StringValue` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.36, p.99 (R3.2 Rev 3)
  - **Step 1 finding:** Base = `ParameterValue`. Members: `value` (String, 1, attr). XML `STRING-VALUE` (XSD group L23739). 1× in Os_ECUC.arxml with **empty** `<VALUE></VALUE>` (Release param) — value must tolerate empty text.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations — `value` optional per XSD (spec says 1); empty VALUE sample
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `LinkerSymbolValue` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.37, p.100 (R3.2 Rev 3)
  - **Step 1 finding:** Base = `ARObject, ParameterValue, StringValue` → most-derived = `StringValue`. ZERO own members. XML `LINKER-SYMBOL-VALUE` (XSD group — verify line at Step 1). Not in Os_ECUC.arxml; completes section 3.4.4.5 family.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations — **none expected**
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `FunctionNameValue` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.38, p.100 (R3.2 Rev 3)
  - **Step 1 finding:** Base = `ARObject, LinkerSymbolValue, ParameterValue, StringValue` → most-derived = `LinkerSymbolValue`. ZERO own members. XML `FUNCTION-NAME-VALUE` (XSD group — verify line at Step 1). Not in Os_ECUC.arxml; completes section 3.4.4.6 family.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations — **none expected**
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `EnumerationValue` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.39, p.101 (R3.2 Rev 3)
  - **Step 1 finding:** Base = `ParameterValue`. Members: `value` (String, 1, attr — "Stores the chosen literal"). XML `ENUMERATION-VALUE` (XSD group L9269). 13× in Os_ECUC.arxml (`<VALUE>EXTENDED</VALUE>`).
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations — `value` optional per XSD (spec says 1)
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `ConfigReferenceValue` (abstract) — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.40, p.103 (R3.2 Rev 3)
  - **Step 1 finding:** Base = `ARObject` (abstract). Members: `definition` (ConfigReference, 1, ref, Tags: `xml.sequenceOffset=-10`). XML parent of `REFERENCE-VALUE`/`INSTANCE-REFERENCE-VALUE`.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red) — abstract: via concrete subclasses
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations — **none expected**
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `ReferenceValue` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.41, p.103 (R3.2 Rev 3)
  - **Step 1 finding:** Base = `ConfigReferenceValue`. Members: `value` (Identifiable, 1, ref). XML `REFERENCE-VALUE`: `DEFINITION-REF` → `VALUE-REF` (XSD group L20706; verify element order at Step 1). 18× in Os_ECUC.arxml under `REFERENCE-VALUES` (XSD group CONFIG-REFERENCE-VALUE L6087 wraps the choice).
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations — `value` optional per XSD (spec says 1)
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `InstanceReferenceValue` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.42, p.106 (R3.2 Rev 3)
  - **Step 1 finding:** Base = `ConfigReferenceValue`. Members: `value` (Identifiable, 1, **iref** — decomposed context path + target; compare R4 pattern `AbstractEcucInstanceReferenceValue` in same leaf module). XML `INSTANCE-REFERENCE-VALUE`. Not in Os_ECUC.arxml; completes section 3.4.5.1.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations — **none expected**
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `Container` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.31, p.93 (R3.2 Rev 3)
  - **Step 1 finding:** Base = `Identifiable` (has SHORT-NAME). Members: `definition` (ContainerDef, 1, ref, `xml.sequenceOffset=-10`); `parameterValue` (ParameterValue, *, aggr); `referenceValue` (ConfigReferenceValue, *, aggr); `subContainer` (Container, *, aggr). XML `CONTAINER` (XSD group L6243-L6305): `SHORT-NAME` → `DEFINITION-REF` → `PARAMETER-VALUES` (choice: BOOLEAN/ENUMERATION/FLOAT/INTEGER/STRING/LINKER-SYMBOL/FUNCTION-NAME-VALUE) → `REFERENCE-VALUES` → `SUB-CONTAINERS`. 20× in Os_ECUC.arxml. Factory: `createSubContainer` on self + `ARPackage`-level containers live under MODULE-CONFIGURATION only.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations — `definition` optional per XSD minOccurs=0 (spec says 1)
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `ModuleConfiguration` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.30, p.86 (R3.2 Rev 3)
  - **Step 1 finding:** Base = `ARElement` (via Identifiable/PackageableElement). Members: `container` (Container, 1..*, aggr, atpSplitable, `xml.sequenceOffset=10`); `definition` (ModuleDef, 1, ref, `xml.sequenceOffset=-10`); `implementationConfigVariant` (ConfigurationVariant, 1, attr); `moduleDescription` (BswImplementation, 0..1, ref). XML `MODULE-CONFIGURATION` (XSD complexType L16479, group L16416): `SHORT-NAME` → `DEFINITION-REF` (DEST=`MODULE-DEF--SUBTYPES-ENUM`) → `IMPLEMENTATION-CONFIG-VARIANT` → `MODULE-DESCRIPTION-REF` (DEST=`BSW-IMPLEMENTATION--SUBTYPES-ENUM`) → `CONTAINERS`. XSD element at AR-PACKAGE/ELEMENTS choice L222. 1× in Os_ECUC.arxml (`/TS_T19D1M6I1R0_AS403/Os`, NO IMPLEMENTATION-CONFIG-VARIANT → both `definition`/`implementationConfigVariant` optional per Rule 0019.3). Factory: `ARPackage.createModuleConfiguration` (duplicate protection `IsElementExists(short_name, ModuleConfiguration)`). `implementationConfigVariant` reuses `EcucConfigurationVariantEnum` (R4 [ECUCParameterDefTemplate.py](file:///Users/ray/Workspace/py-armodel/src/armodel/models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py)) — verify literals match R3.2.3 ConfigurationVariant (VariantPreCompile/VariantLinkTime/VariantPostBuild/VariantPostBuildLoadable/VariantPostBuildSelectable) at Step 1. 5-place dispatch: parser `readARPackageElements` L12491 + writer `writeARPackageElement`.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations — `definition` + `implementationConfigVariant` optional per XSD minOccurs=0 (spec says 1); Os_ECUC.arxml omits both
  - [ ] Step 9 — Verify (9a) + confirm (9b) — final gate: Os_ECUC.arxml full round-trip green

## Out of scope (documented, not queued)

- `EcuConfiguration` (Table 3.29, p.85) — R3.2.3 anchor class; Os_ECUC.arxml does NOT use `ECU-CONFIGURATION` element (MODULE-CONFIGURATION sits directly under AR-PACKAGE/ELEMENTS per XSD L222). Queue only if a sample file appears.
- R3.2.3 `ModuleDef`/`ContainerDef`/`EcucParameterDefinition` definition-side classes — value files reference them by `DEFINITION-REF` only; no sample file carries definitions.
- `ModuleConfiguration.recommendedConfiguration`/`preconfiguredConfiguration` roles — prose concept (spec §3.4.2), no distinct XML member.
