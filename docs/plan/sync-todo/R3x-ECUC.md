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
- [x] `FloatValue` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.35, p.99 (R3.2 Rev 3) — DONE 2026-09-19, commit `500cfd2b`
  - **Step 1 finding:** Base = `ParameterValue`. Members: `value` (Float, 1, attr). XML `FLOAT-VALUE` (XSD group L11254). 2× in Os_ECUC.arxml.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — `value` optional per XSD (spec says 1)
  - [x] Step 9 — Verify (9a: 9491 passed, lint/black clean) + confirm (9b user OK 2026-09-19)
- [x] `StringValue` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.36, p.99 (R3.2 Rev 3) — DONE 2026-09-19, commit `222ebe80`
  - **Step 1 finding:** Base = `ParameterValue`. Members: `value` (String, 1, attr). XML `STRING-VALUE` (XSD group L23739). 1× in Os_ECUC.arxml with **empty** `<VALUE></VALUE>` (Release param) — value must tolerate empty text.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — `value` optional per XSD (spec says 1); empty VALUE sample
  - [x] Step 9 — Verify (9a: 9501 passed, lint/black clean) + confirm (9b user OK 2026-09-19)
- [x] `LinkerSymbolValue` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.37, p.100 (R3.2 Rev 3) — DONE 2026-09-19, commit `c3e791a5` (handlers refactored to read/write-fill style in `772c3467`)
  - **Step 1 finding:** Base = `ARObject, ParameterValue, StringValue` → most-derived = `StringValue`. ZERO own members. XML `LINKER-SYMBOL-VALUE` (XSD group — verify line at Step 1). Not in Os_ECUC.arxml; completes section 3.4.4.5 family.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — **none** (no own members; inherits StringValue's optional-value deviation)
  - [x] Step 9 — Verify (9a: 9511 passed, lint/black clean) + confirm (9b user OK 2026-09-19)
- [ ] `FunctionNameValue` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.38, p.100 (R3.2 Rev 3)
  - **Step 1 finding:** Base = `ARObject, LinkerSymbolValue, ParameterValue, StringValue` → most-derived = `LinkerSymbolValue`. ZERO own members. XML `FUNCTION-NAME-VALUE` (XSD group — verify line at Step 1). Not in Os_ECUC.arxml; completes section 3.4.4.6 family.
  - **Step 1 verified 2026-09-19:** PDF p.100 Table 3.38 — Note "Representing a configuration value of definition type FunctionNameDef", attribute table EMPTY; XSD complexType AUTOSAR.xsd L11696 = `PARAMETER-VALUE group → STRING-VALUE group` (VALUE is String, minOccurs=0 via group); XSD doc = Note verbatim; choice membership PARAMETER-VALUES L6275 (between LINKER-SYMBOL-VALUE and INTEGER-VALUE). Helper-pair only (no ARPackage dispatch — not an ARElement), dispatched from future Container's PARAMETER-VALUES choice loop (LinkerSymbolValue precedent).
  - [x] Step 1 — Sync members & description from spec — verified 2026-09-19 (see finding above)
  - [x] Step 2 — Write model class unit test (Red) — 3 tests in TestFunctionNameValue (inheritance/initialization/get_set_value); Red = ImportError at collection (class missing)
  - [x] Step 3 — Implement model class (Green) — `class FunctionNameValue(LinkerSymbolValue)` appended to ECUCDescriptionTemplate.py (after LinkerSymbolValue); zero own members; 47/47 model tests green
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — class created bare in Step 3 (wipe vacuous); class docstring = Table 3.38 Note verbatim ("Representing a configuration value of definition type FunctionNameDef"); no own members → no member docstrings; __init__ docless
  - [x] Step 5 — Write reader/writer round-trip test (Red) — 4 parser tests (without/with DEST, missing VALUE, missing DEFINITION-REF) + 3 writer tests (without/with DEST, empty); Red = AttributeError ×7
  - [x] Step 6 — Update parser & writer (Green) — parser readFunctionNameValue after readLinkerSymbolValue (delegates to readStringValue: DEFINITION-REF + VALUE-as-String per XSD STRING-VALUE group); writer writeFunctionNameValue after writeLinkerSymbolValue (self-tagging FUNCTION-NAME-VALUE + writeParameterValue + setChildElementOptionalString VALUE); imports extended in both; no ARPackage dispatch (not an ARElement — helper pair only, LinkerSymbolValue precedent); 206/206 ECUC handler tests green
  - [x] Step 7 — Update checklist comment — 6-column format with release column R3.2.3, 3 rows all [x] (getValue [—]/[x] via writeFunctionNameValue, setValue [x]/[—] via readFunctionNameValue, __init__ [—]/[—]); `# Spec verified:` stamp deferred to batch confirmation (user-instructed 2026-09-19)
  - [x] Step 8 — Deviations — **none** (zero own members; inherits StringValue's optional-value deviation note, same disclosure as LinkerSymbolValue)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a green (333 touched tests, lint flake8+ruff clean, black 948 unchanged, parity OK); 9b DEFERRED to batch stamp confirmation (user-instructed 2026-09-19) — marker to be written with the other 6 classes after the batch gate
- [ ] `EnumerationValue` — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.39, p.101 (R3.2 Rev 3)
  - **Step 1 finding:** Base = `ParameterValue`. Members: `value` (String, 1, attr — "Stores the chosen literal"). XML `ENUMERATION-VALUE` (XSD group L9269). 13× in Os_ECUC.arxml (`<VALUE>EXTENDED</VALUE>`).
  - **Step 1 verified 2026-09-19:** PDF p.101 Table 3.39 — Note "Representing a configuration value of definition type EnumerationParamDef", Base row ARObject/ParameterValue → most-derived ParameterValue, 1 attr value (String, 1, "Stores the chosen literal."); XSD complexType L9281 = PARAMETER-VALUE group → ENUMERATION-VALUE group, VALUE xsd:string minOccurs="0" (deviation pre-noted); XSD doc = Note verbatim; PARAMETER-VALUES choice membership L9262 (first member, before BOOLEAN-VALUE).
  - [x] Step 1 — Sync members & description from spec — verified 2026-09-19 (see finding above)
  - [x] Step 2 — Write model class unit test (Red) — 3 tests in TestEnumerationValue (inheritance/initialization/get_set_value); Red = ImportError at collection (class missing)
  - [x] Step 3 — Implement model class (Green) — `class EnumerationValue(ParameterValue)` appended to ECUCDescriptionTemplate.py (after FunctionNameValue); member value: Optional[String]; 50/50 model tests green
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — class created bare in Step 3 (wipe vacuous); class docstring = Table 3.39 Note verbatim; member inline comment + get/set docstrings = "Stores the chosen literal." verbatim; setter None-no-op sentence; __init__ docless
  - [x] Step 5 — Write reader/writer round-trip test (Red) — 4 parser tests (without/with DEST, missing VALUE, missing DEFINITION-REF) + 3 writer tests (without/with DEST, empty); Red = AttributeError ×7
  - [x] Step 6 — Update parser & writer (Green) — parser readEnumerationValue after readFunctionNameValue (readParameterValue + getChildElementOptionalString VALUE); writer writeEnumerationValue after writeFunctionNameValue (self-tagging ENUMERATION-VALUE + writeParameterValue + setChildElementOptionalString VALUE); imports extended in both; no ARPackage dispatch (not an ARElement — helper pair for future Container choice loop); 263 touched tests green
  - [x] Step 7 — Update checklist comment — 6-column format with release column R3.2.3, 3 rows all [x] (getValue [—]/[x], setValue [x]/[—], __init__ [—]/[—]); `# Spec verified:` stamp deferred to batch confirmation (user-instructed 2026-09-19)
  - [x] Step 8 — Deviations — `value` optional per XSD group ENUMERATION-VALUE (AUTOSAR.xsd L9275) minOccurs="0" (spec Mul=1; Rule 0019.3 inverted, sample evidence wins) — deviation note in class checklist
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a green (263 touched tests incl. all ECUC handler/model suites, lint/black/parity clean); 9b DEFERRED to batch stamp confirmation (user-instructed 2026-09-19)
- [ ] `ConfigReferenceValue` (abstract) — R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.40, p.103 (R3.2 Rev 3)
  - **Step 1 finding:** Base = `ARObject` (abstract). Members: `definition` (ConfigReference, 1, ref, Tags: `xml.sequenceOffset=-10`). XML parent of `REFERENCE-VALUE`/`INSTANCE-REFERENCE-VALUE`.
  - **Step 1 verified 2026-09-19:** PDF p.103 Table 3.40 — Note "Abstract class to be used as common parent for all reference values in the ECU Configuration Description.", Base ARObject, 1 attr definition (ConfigReference, 1, ref, Note "Reference to the definition of this ConfigReferenceValue subclasses in the ECU Configuration Parameter Definition." + Tags xml.sequenceOffset=-10); post-table prose [ecuc_sws_3027]/[ecuc_sws_3028]/[ecuc_sws_3029] appended to class docstring per System/InterpolationRoutine precedent (disclosed at batch gate); XSD group CONFIG-REFERENCE-VALUE L6087: DEFINITION-REF minOccurs="0" (Rule 0019.3 inverted) + DEST use="required" CONFIG-REFERENCE--SUBTYPES-ENUM (DEST optional per sample, ParameterValue precedent).
  - [x] Step 1 — Sync members & description from spec — verified 2026-09-19 (see finding above)
  - [x] Step 2 — Write model class unit test (Red) — 3 tests in TestConfigReferenceValue (rejects_direct_instantiation/initialization via local stub/get_set_definition_ref); Red = ImportError at collection (class missing)
  - [x] Step 3 — Implement model class (Green) — `class ConfigReferenceValue(ARObject, ABC)` appended to ECUCDescriptionTemplate.py (after EnumerationValue); abstract type guard; member definitionRef: Optional[RefType] (renamed from spec `definition` per ECUC ref-suffix convention, ParameterValue precedent); 53/53 model tests green
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — class created bare in Step 3 (wipe vacuous); class docstring = Table 3.40 Note verbatim + ecuc_sws_3027/3028/3029 (PDF-text restored, wrap artifacts joined); member inline comment + get/set docstrings = definition Note verbatim; setter None-no-op sentence; __init__ docless
  - [x] Step 5 — Write reader/writer round-trip test (Red) — abstract: via test-local `_R3ConfigReferenceValueStub` in both files (ParameterValue precedent); 3 parser tests (without/with DEST, missing DEFINITION-REF) + 3 writer tests (without/with DEST, none-omitted); Red = AttributeError ×6
  - [x] Step 6 — Update parser & writer (Green) — parser readConfigReferenceValue after readEnumerationValue (DEFINITION-REF via getChildElementOptionalRefType, DEST optional); writer writeConfigReferenceValue after writeEnumerationValue (no self-tag — abstract parent helper, DEFINITION-REF via setChildElementOptionalRefType); imports extended in both; concrete subclasses call it (ReferenceValue/InstanceReferenceValue next); 272 touched tests green
  - [x] Step 7 — Update checklist comment — 6-column format with release column R3.2.3, 3 rows all [x] (getDefinitionRef [—]/[x], setDefinitionRef [x]/[—], __init__ [—]/[—]); `# Spec verified:` stamp deferred to batch confirmation (user-instructed 2026-09-19)
  - [x] Step 8 — Deviations — recorded in class checklist: ① `definition` optional — spec Mul=1 but XSD group CONFIG-REFERENCE-VALUE L6087 minOccurs="0" (Rule 0019.3 inverted); renamed `definitionRef` per ECUC ref-suffix convention. ② DEFINITION-REF DEST use="required" in XSD but sample carries no DEST → reader/writer treat DEST as optional (ParameterValue precedent)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a green (352 touched tests, lint flake8+ruff clean after test-import I001 fix, black 948 unchanged, parity OK); 9b DEFERRED to batch stamp confirmation (user-instructed 2026-09-19)
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
