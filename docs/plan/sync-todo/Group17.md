# Sync todo: Group 17 — CAN/LIN/Flexray Fibex, DataMapping & Multiplatform

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

> **Parent-dependency audit 2026-09-26 (all Group1-20 pending rows, spec-table Base chains):** every pending row's Base row extracted from the R23-11/R4.3.1 markdown (260/293 found; 33 = enums/XSD-only/user-arbitrated) and every parent classified against src stamps + the queue. Findings: DiagnosticEnvCompareCondition (Group14) and MixedContentForUnitNames (Group8) queued NEW above their children; DiagnosticEnvModeElement row-header Base corrected. ESTABLISHED SKIPS (no rows, per precedent): UploadableDesignElement / UploadablePackageElement (attribute-less abstract bases, empty XSD groups — most-derived-base collapse, Group5-audit precedent; appear in Base cells of CanClusterBusOffRecovery row below); AREnum leaf classes (no Base row by construction); the Firewall member-rule family (user arbitration 2026-08-31: no Class table in either corpus → skipped, see Group1 FirewallRule Done row); ARList (resolved under "List", FO GST Table 9.8, Group9 row).

## Queue (dependency-first)

- [ ] `CanClusterBusOffRecovery` (input · R23-11 markdown · Table 3.10)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py
  - Note: own table = AUTOSAR_CP_TPS_SystemTemplate Table 3.10, p.63 (page-split; R4.3.1 Table 3.10 p.59 agrees on row order); concrete Class; Base most-derived = `ARObject` → `__init__(self)`; 5 attrs, all 0..1 attr — borCounterL1ToL2 (PositiveInteger), borTimeL1, borTimeL2, borTimeTxEnsured, mainFunctionPeriod (TimeValue); XSD group order = displayed order; orphan intake drift found: bare annotations, untyped accessors, fabricated docstring, old 4-column checklist; reader/writer helpers missing BOR-TIME-TX-ENSURED + MAIN-FUNCTION-PERIOD.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — 11 failed / 3 passed (fabricated docstring, no type pins, no member docstrings; defaults + member order already correct)
  - [x] Step 3 — Implement model class (Green) — Optional[T] fields/accessors, self-returning guarded setters, `from __future__ import annotations` added (bare self-return per Rule 0003); 24 passed in test_CanTopology.py, SystemTemplate suite 1281 passed
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — fabricated class docstring replaced with Table 3.10 Note verbatim; per-attr inline comments + getter/setter docstrings verbatim (setters + None-no-op line); `mainFunctionPeriod` Note kept verbatim incl. the R23-11 markdown rendering quirk "Can SM_MainFunction" (XSD reads "CanSM_MainFunction")
  - [x] Step 5 — Write reader/writer round-trip test (Red) — new tests/test_armodel/parser/test_can_cluster_bus_off_recovery.py + tests/test_armodel/writer/test_can_cluster_bus_off_recovery.py; 4 failed / 4 passed (reader+writer miss BOR-TIME-TX-ENSURED + MAIN-FUNCTION-PERIOD; absent/empty-wrapper paths already correct)
  - [x] Step 6 — Update parser & writer (Green) — getCanClusterBusOffRecovery + setCanClusterBusOffRecovery extended with BOR-TIME-TX-ENSURED + MAIN-FUNCTION-PERIOD (spec-typed leaf helpers, XSD order); 852 passed across new + adjacent Fibex suites
  - [x] Step 7 — Update checklist comment — 6-column format with release column, rows in source order (getter-first per scalar attribute, spec row order); `# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.10, p.63`; reader [x] on setter rows / writer [x] on getter rows verified against the getCanClusterBusOffRecovery/setCanClusterBusOffRecovery call sites; NO `# Spec verified:` — deferred to batch confirmation
  - [x] Step 8 — Deviations (fixed+recorded in step notes: bare-T 0..1 fields → PEP 526 `Optional[PositiveInteger]`/`Optional[TimeValue]`; untyped accessors → typed with bare self-return via module-level `from __future__ import annotations` (Rule 0003 — quoted `-> "Cls"` avoided); fabricated class docstring → Table 3.10 Note verbatim; reader/writer coverage missing for borTimeTxEnsured + mainFunctionPeriod → added at Step 6; old 4-column checklist → 6-column with `# Spec:` line + release column; no pre-existing `# Spec verified:`/`# XSD verified:` marker to invalidate; deviation trackers method_deviation_by_class.md + v2 have NO entries for this class — nothing stale; no open deviations, no placeholders — Base `ARObject` exists, member types PositiveInteger/TimeValue exist, aggregator AbstractCanCluster.busOffRecovery typed `Optional[CanClusterBusOffRecovery]` in CoreTopology.py)
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28: 12789 passed / 0 failed, lint + black clean; 9b deferred to batch confirmation (user instruction)

- [ ] `CanCommunicationConnector` (input · R23-11 markdown · Table 3.23)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py
  - Note: own table = AUTOSAR_CP_TPS_SystemTemplate Table 3.23, p.74 (R4.3.1 Table 3.21 p.65 agrees); concrete Class; Base most-derived = `AbstractCanCommunicationConnector` — parent verified (stamped R23-11 Table 3.22, inherits `CommunicationConnector`, abstract guard, no own attrs); 5 attrs, all 0..1 attr — pncWakeupCanId, pncWakeupCanIdExtended (Boolean), pncWakeupCanIdMask, pncWakeupDlc (PositiveInteger), pncWakeupDataMask (PositiveUnlimitedInteger); XSD group CAN-COMMUNICATION-CONNECTOR order = displayed order; orphan intake drift found: bare annotations, untyped accessors, fabricated docstring, old 4-column checklist; reader/writer read/writeCanCommunicationConnector call readCommunicationConnector only — all five PNC-WAKEUP elements dropped.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — 11 failed / 3 passed (fabricated docstring, no type pins, no member docstrings; defaults + member order already correct)
  - [x] Step 3 — Implement model class (Green) — bare-T 0..1 fields → PEP 526 `Optional[PositiveInteger]`/`Optional[Boolean]`/`Optional[PositiveUnlimitedInteger]`; untyped accessors → typed, self-returning guarded setters (module `from __future__ import annotations` already present); 8 passed / 6 docstring tests still Red
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — fabricated class docstring replaced with Table 3.23 Note verbatim; per-attr inline comments + getter/setter docstrings verbatim (setters + None-no-op line); pncWakeupCanIdExtended Note copied with the PDF line-wrap artifact normalized ("pncWakeupCanIdMask", per XSD documentation + module precedent)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — new tests/test_armodel/parser/test_can_communication_connector.py + tests/test_armodel/writer/test_can_communication_connector.py; 4 failed / 4 passed (reader+writer drop all five PNC-WAKEUP elements; base dispatch, absent-element read→None and write→omitted paths already correct)
  - [x] Step 6 — Update parser & writer (Green) — readCanCommunicationConnector/writeCanCommunicationConnector extended with the five PNC-WAKEUP elements (mutators/getters, XSD group order); new spec-typed leaf helper pair getChildElementOptionalPositiveUnlimitedInteger (abstract_arxml_parser.py) / setChildElementOptionalPositiveUnlimitedInteger (abstract_arxml_writer.py, one-line delegation per Rule 0013.2); 46 passed across model+parser+writer class suites, 5922 across parser+writer suites
  - [x] Step 7 — Update checklist comment — 6-column format with release column, rows in source order (getter-first per scalar attribute, spec row order); `# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.23, p.74`; reader [x] on setter rows / writer [x] on getter rows verified against readCanCommunicationConnector/writeCanCommunicationConnector call sites; NO `# Spec verified:` — deferred to batch confirmation
  - [x] Step 8 — Deviations (fixed in step notes: bare-T 0..1 fields → PEP 526 Optional[T]; untyped accessors → typed; fabricated docstring → Table 3.23 Note verbatim; reader/writer coverage added for all five PNC-WAKEUP elements; old 4-column checklist → 6-column; pncWakeupCanIdExtended Note line-wrap artifact "pncWakeupCanId Mask" normalized to "pncWakeupCanIdMask" per XSD documentation + module precedent (J1939Cluster "re- quest2Support"); no open deviations, no placeholders — Base AbstractCanCommunicationConnector exists + stamped, member types PositiveInteger/Boolean/PositiveUnlimitedInteger exist; deviation trackers method_deviation_by_class.md + v2 have NO entries for this class — nothing stale; report note: spec "Aggregated by" also lists MachineDesign.communicationConnector but no MachineDesign model/reader/writer exists in the codebase — coverage provided via the EcuInstance CONNECTORS dispatch, MachineDesign belongs to its own future sync)
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28: 12811 passed / 0 failed, lint + black clean; 9b deferred to batch confirmation (user instruction)

- [ ] `CanControllerConfiguration` (input · R23-11 markdown · Table 3.14)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py
  - Note: own table = AUTOSAR_CP_TPS_SystemTemplate Table 3.14, p.64 (R4.3.1 Table 3.14 p.60 agrees); concrete Class; Base row = `ARObject , AbstractCanCommunicationControllerAttributes` → most-derived = `AbstractCanCommunicationControllerAttributes` — FIXED from the row's `ARObject` (Rule 0001.2); 4 attrs, all 0..1 attr Integer — propSeg, syncJumpWidth, timeSeg1, timeSeg2; aggregators = AbstractCanCommunicationController.canControllerAttributes + CanXlProps.canConfig (XSD group line 14537, complexType line 14584; leaf order PROP-SEG, SYNC-JUMP-WIDTH, TIME-SEG-1, TIME-SEG-2 = displayed order); orphan intake drift found: placeholder class with ARObject base, no fields, fabricated docstring; identity-only reader `getCanControllerConfiguration`/writer `setCanControllerConfiguration` (empty element) + missing CAN-CONTROLLER-CONFIGURATION dispatch branch.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — 11 failed / 1 passed (placeholder class: ARObject base drift, no fields/accessors, fabricated docstring; init-has-no-docstring already held)
  - [x] Step 3 — Implement model class (Green) — base corrected to `AbstractCanCommunicationControllerAttributes` (most-derived per spec Base row; placeholder had bare `ARObject`); 4 PEP 526 `Optional[Integer]` fields in spec row order, typed getter/guarded-setter pairs returning self, blank line between every block; test_CanTopology.py 50 passed
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — placeholder docstring removed with the block rewrite; class docstring = Table 3.14 Note verbatim; per-attr inline comments + getter/setter docstrings verbatim (setters + None-no-op line); AST audit vs /tmp markdown extraction: 0 diffs
  - [x] Step 5 — Write reader/writer round-trip test (Red) — new tests/test_armodel/parser/test_can_controller_configuration.py + tests/test_armodel/writer/test_can_controller_configuration.py; parser 3 failed / 2 passed, writer 5 failed / 3 passed (identity-only reader/writer drop the four leaf values; CAN-CONTROLLER-CONFIGURATION dispatch branch missing on both sides; absent/empty paths already correct)
  - [x] Step 6 — Update parser & writer (Green) — reader: getCanControllerConfiguration upgraded from identity-only to readCanControllerConfiguration (base helper readAbstractCanCommunicationControllerAttributes + 4 spec-typed leaves via getChildElementOptionalIntegerValue, XSD order); new CAN-CONTROLLER-CONFIGURATION elif in readAbstractCanCommunicationControllerCanControllerAttributes dispatch; writer: setCanControllerConfiguration upgraded (writeAbstractCanCommunicationControllerAttributes + 4 setChildElementOptionalIntegerValue), new one-line-delegation writeCanControllerConfiguration + isinstance elif in writeAbstractCanCommunicationControllerCanControllerAttributes; matched name pairs kept (get/set leaf pair, read/write element pair); parser+writer suites 5935 passed
  - [x] Step 7 — Update checklist comment — 6-column format with release column, rows in source order (getter-first per scalar attribute, spec row order); `# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.14, p.64`; reader [x] on setter rows / writer [x] on getter rows verified by AST against readCanControllerConfiguration + setCanControllerConfiguration call sites and both aggregator dispatches; NO `# Spec verified:` — deferred to batch confirmation
  - [x] Step 8 — Deviations (fixed in step notes: ARObject base → most-derived AbstractCanCommunicationControllerAttributes per spec Base row; whole-class placeholder (no fields, fabricated docstring) → full Table 3.14 sync; identity-only reader/writer + missing CAN-CONTROLLER-CONFIGURATION dispatch → real read/write added both sides; referenced classes all exist (AbstractCanCommunicationControllerAttributes stamped R23-11, Integer, CanXlProps XSD-verified, AbstractCanCommunicationController); deviation trackers method_deviation_by_class.md + v2 have NO entries for this class — nothing stale; no open deviations, no placeholders)
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28: 12836 passed / 0 failed, lint + black clean; 9b deferred to batch confirmation (user instruction)

- [ ] `CanControllerConfigurationRequirements` (input · R23-11 markdown · Table 3.15)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py
  - Note: own table = AUTOSAR_CP_TPS_SystemTemplate Table 3.15, p.65 (R4.3.1 Table 3.15 p.61); concrete Class; Base row = `ARObject , AbstractCanCommunicationControllerAttributes` → most-derived = `AbstractCanCommunicationControllerAttributes` — row header Base claim confirmed correct, no correction; 6 attrs, all 0..1 attr, displayed order maxNumberOfTimeQuantaPerBit, minNumberOfTimeQuantaPerBit (Integer) / maxSamplePoint, maxSyncJumpWidth, minSamplePoint, minSyncJumpWidth (Float); aggregator = AbstractCanCommunicationController.canControllerAttributes (XSD group line 14589, complexType line 14635; leaf order = displayed order); orphan intake drift found: bare-T `= None` annotations, untyped accessors, setters without None guard, fabricated docstring, old 3-column checklist, glued field blocks; reader/writer coverage already present (readCanControllerConfigurationRequirements/writeCanControllerConfigurationRequirements + CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS dispatch, spec-typed leaf helpers).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — new tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology/test_CanControllerConfigurationRequirements.py; 13 failed / 3 passed (fabricated docstring, no type pins, no None guard, no member docstrings; defaults, member order, init-no-docstring already correct)
  - [x] Step 3 — Implement model class (Green) — bare-T `= None` fields → PEP 526 `Optional[Integer]`/`Optional[Float]` in spec row order with blank line between blocks; untyped accessors → typed getter/guarded-setter pairs returning self (module `from __future__ import annotations` already present); 9 passed / 7 docstring tests still Red
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — fabricated class docstring + stale 3-column checklist removed in the Step 3 block rewrite (wipe-then-rewrite, Rule 0012.2.3); class docstring = Table 3.15 Note verbatim; per-attr inline comments + getter/setter docstrings verbatim from the markdown (setters + None-no-op line); Fibex4Can model suite 103 passed
  - [x] Step 5 — Write reader/writer round-trip test (Red) — new tests/test_armodel/parser/test_can_controller_configuration_requirements.py + tests/test_armodel/writer/test_can_controller_configuration_requirements.py (field VALUES + types, XSD leaf order, absent-element → None, empty-wrapper → no children, write→read round-trip through the CAN-CONTROLLER-ATTRIBUTES dispatch; no ref/DEST attrs in this element set); coverage found already Green — 8 passed + 1 test-bug fixed (dispatch raises notImplemented on unknown child tags by design; absence test rewritten to the true no-child case per sibling precedent)
  - [x] Step 6 — Update parser & writer (Green) — N/A: reader/writer coverage already present and spec-correct, no edits needed; evidence — parser readCanControllerConfigurationRequirements (arxml_parser.py L12100: base helper readAbstractCanCommunicationControllerAttributes + 6 spec-typed leaves getChildElementOptionalIntegerValue/getChildElementOptionalFloatValue via the model mutators, XSD order) + CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS dispatch branch (L12112); writer writeCanControllerConfigurationRequirements (arxml_writer.py L11012: None-guard, base helper + 6 setChildElementOptionalIntegerValue/FloatValue via the model getters, XSD order) + isinstance dispatch (L11027); matched name pairs read/write + set/get + leaf helper pairs; no chained mutators; adjacent suites 822 passed
  - [x] Step 7 — Update checklist comment — 6-column format with release column, rows in source order (getter-first per scalar attribute, spec row order); `# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.15, p.65`; reader [x] on setter rows / writer [x] on getter rows verified against readCanControllerConfigurationRequirements (arxml_parser.py L12100) and writeCanControllerConfigurationRequirements (arxml_writer.py L11012) call sites; NO `# Spec verified:` — deferred to batch confirmation
  - [x] Step 8 — Deviations (fixed in step notes: bare-T 0..1 fields → PEP 526 Optional[T]; untyped accessors → typed; None-unguarded setters → guarded self-returning; fabricated docstring → Table 3.15 Note verbatim; old 3-column checklist → 6-column with `# Spec:` line + release column; referenced classes all exist (AbstractCanCommunicationControllerAttributes stamped R23-11 Table 3.13, Integer, Float, aggregator AbstractCanCommunicationController); deviation trackers method_deviation_by_class.md + v2 have NO entries for this class — nothing stale; no open deviations, no placeholders)
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28: 12861 passed / 0 failed, lint + black clean; 9b deferred to batch confirmation (user instruction)

- [ ] `CanControllerFdConfigurationRequirements` (input · R23-11 markdown · Table 3.17 · Base row = ARObject confirmed, no correction)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py
  - Note: own table = AUTOSAR_CP_TPS_SystemTemplate Table 3.17, pp.66-67 page-split (header + max* rows p.66, min*/paddingValue/txBitRateSwitch rows p.67; R4.3.1 Table 3.17 p.63 agrees); concrete Class (atpObject); Base row = `ARObject` only — aggregator AbstractCanCommunicationControllerAttributes.canControllerFdRequirements (XSD group line 14724, complexType line 14798; leaf order = displayed order, 10 leaves); not VP-capable (no VARIATION-POINT), not atpMixedString; orphan intake drift found: bare-T `= None` annotations, untyped accessors, fabricated docstring, old 3-column checklist, glued field blocks; reader/writer get/setCanControllerFdConfigurationRequirements drop the PADDING-VALUE leaf on both sides.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — new tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology/test_CanControllerFdConfigurationRequirements.py; 21 failed / 3 passed (fabricated docstring, no type pins, no member docstrings; defaults, member order, init-no-docstring already correct)
  - [x] Step 3 — Implement model class (Green) — bare-T `= None` fields → PEP 526 `Optional[Integer]`/`Optional[Float]`/`Optional[TimeValue]`/`Optional[PositiveInteger]`/`Optional[Boolean]` in spec row order with blank line between every block; untyped accessors → typed getter/guarded-setter pairs returning self (module `from __future__ import annotations` already present); 13 passed / 11 docstring tests still Red
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — fabricated class docstring + stale 3-column checklist removed in the Step 3 block rewrite (wipe-then-rewrite, Rule 0012.2.3); class docstring = Table 3.17 Note verbatim; per-attr inline comments + getter/setter docstrings verbatim from the markdown (setters + None-no-op line); Fibex4Can model suite 58 passed
  - [x] Step 5 — Write reader/writer round-trip test (Red) — new tests/test_armodel/parser/test_can_controller_fd_configuration_requirements.py + tests/test_armodel/writer/test_can_controller_fd_configuration_requirements.py (field VALUES + types, XSD leaf order, absent-element → None, empty-wrapper → no children, write→read round-trip through the CAN-CONTROLLER-FD-REQUIREMENTS element; no ref/DEST attrs in this element set); 4 failed / 4 passed (reader and writer both drop PADDING-VALUE; absent/empty paths already correct); 1 test-bug fixed pre-run (ARObject-based holder constructed without parent/short_name)
  - [x] Step 6 — Update parser & writer (Green) — reader getCanControllerFdConfigurationRequirements (arxml_parser.py L12013) + writer setCanControllerFdConfigurationRequirements (arxml_writer.py L10959) extended with the missing PADDING-VALUE leaf in XSD order (between MIN-TRCV-DELAY-COMPENSATION-OFFSET and TX-BIT-RATE-SWITCH) via the spec-typed leaf pair getChildElementOptionalPositiveInteger / setChildElementOptionalPositiveInteger (PositiveInteger per PDF; Rule 0001.3) through the model mutators/getters; matched name pairs kept (set/get model, get/set element helper, get/set leaf pair); no chained mutators; class + adjacent parser/writer suites 135 passed
  - [x] Step 7 — Update checklist comment — 6-column format with release column, rows in source order (getter-first per scalar attribute, spec row order); `# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.17, pp.66-67`; reader [x] on setter rows / writer [x] on getter rows verified against getCanControllerFdConfigurationRequirements (arxml_parser.py L12013) and setCanControllerFdConfigurationRequirements (arxml_writer.py L10959) call sites; set-based checklist-vs-methods check + test-coverage assert pass; NO `# Spec verified:` — deferred to batch confirmation
  - [x] Step 8 — Deviations (fixed in step notes: bare-T 0..1 fields → PEP 526 Optional[T]; untyped accessors → typed; fabricated docstring → Table 3.17 Note verbatim; old 3-column checklist → 6-column with `# Spec:` line + release column; glued field blocks → blank line per Rule 0008; reader/writer PADDING-VALUE silent drop → full coverage added both sides at Step 6; referenced classes all exist (ARObject per spec Base row, Integer, Float, TimeValue, PositiveInteger, Boolean, aggregator AbstractCanCommunicationControllerAttributes stamped R23-11 Table 3.13); deviation trackers method_deviation_by_class.md + v2 have NO entries for this class — nothing stale; no open deviations, no placeholders)
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28: 12893 passed / 0 failed, lint + black clean; 9b deferred to batch confirmation (user instruction)

- [ ] `ResumePosition` (input · R23-11 markdown · Table 6.95)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py
  - Note: own table = AUTOSAR_CP_TPS_SystemTemplate Table 6.95, p.432 (R4.3.1 Table 6.95 p.299 agrees); Enumeration header, Package = M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication — existing module correct; 2 literals in displayed order — continueAtItPosition ("Continue at IT Point.", atp.EnumerationLiteralIndex=0), startFromBeginning ("Start from the beginning", idx=1); aggregated by LinScheduleTable.resumePosition; orphan-intake drift found: fabricated docstring, old 4-column checklist ([ ] impl-only rows, no reader/writer/release columns, no `# Spec:` line), tuple-init enum (exemplar uses list); member names/values already spec-correct; v2 deviation tracker listed ResumePosition under "Appendix: classes without a spec attribute table" — STALE (Table 6.95 exists; reviewed at Step 1, recorded at Step 8).
  - [x] Step 1 — Sync members & description from spec — Table 6.95 located (markdown AUTOSAR_CP_TPS_SystemTemplate.md L11417; PDF p.432 via pdf_page.py); Enumeration header confirmed (not a Class table); Note + literal list extracted verbatim; class already EXISTS at the spec package → orphan intake, no new file, exports intact (`armodel.ResumePosition` resolves)
  - [x] Step 2 — Write model class unit test (Red) — class TestResumePosition added to existing mirrored test_LinCommunication.py (member presence/values + instantiability `setValue(MEMBER)`/`getValue()` + class-docstring-note); 1 failed / 2 passed (fabricated docstring; member names/values/instantiability already correct)
  - [x] Step 3 — Implement model class (Green) — AREnum kept; literals verbatim in displayed order with description+Tags inline comments; `__init__` passes a list (FlexrayChannelName exemplar form; was tuple); setValue/getValue inherited per AREnum/ARLiteral convention; set-based checklist-vs-methods check OK ({`__init__`}); mirrored file 40 passed
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — fabricated class docstring replaced with Table 6.95 Note verbatim ("Defines, where a schedule table shall be proceeded in case if it has been interrupted by a run-once table or MRF/SRF."); enum has no methods → no `__init__`/accessor docstrings; literal inline comments = spec description + Tags verbatim
  - [x] Step 5 — N/A — standalone AREnum: no own XML element; serialized as an attribute value on the consuming class LinScheduleTable.resumePosition and round-tripped there (Rules 0010–0011)
  - [x] Step 6 — N/A — same reason (Rules 0010–0011); `# (no methods)` checklist treatment
  - [x] Step 7 — Update checklist comment — 6-column format with release column; `# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.95, p.432`; `# (no methods) — enum value form serialized on LinScheduleTable.resumePosition` + single `[x] __init__` row (reader/writer `[—]`), per the FlexrayChannelName exemplar; NO `# Spec verified:` — deferred to batch confirmation
  - [x] Step 8 — Deviations (fixed in step notes: fabricated docstring → Table 6.95 Note verbatim; old 4-column checklist → 6-column with `# Spec:` line + release column; tuple enum init → list per exemplar; STALE tracker entry: method_deviation_by_class_v2.md L1902 lists ResumePosition under "Appendix: classes without a spec attribute table" but Table 6.95 exists — left in place (informational appendix bullet), flagged for batch owner; method_deviation_by_class.md has NO entries; no open deviations, no placeholders — referenced classes exist: AREnum base stamped corpus, consuming aggregator LinScheduleTable queued later in this file (still unsynced with bare-T `# type:` fields — its own row will fix))
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28: 13106 passed / 0 failed, lint + black clean; 9b deferred to batch confirmation (user instruction)

- [ ] `ApplicationEntry` — ScheduleTableEntry — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py
  - Note: own table = AUTOSAR_CP_TPS_SystemTemplate Table 6.97, p.433 (R4.3.1 Table 6.97 p.300 agrees); concrete Class; Base row = `ARObject , ScheduleTableEntry` → most-derived = `ScheduleTableEntry` (already stamped R23-11, fields match Table 6.96) — confirmed, no correction; 1 own attr `frameTriggering` (LinFrameTriggering, 0..1, ref, constr_9136). Orphan-intake drift: fabricated docstring, old 4-column checklist, bare-T `RefType = None` field (0..1 → `Optional[RefType]`), untyped accessors. Reader `getApplicationEntry` + writer `setApplicationEntry` already cover FRAME-TRIGGERING-REF in XSD order (AR-OBJECT → SCHEDULE-TABLE-ENTRY → APPLICATION-ENTRY group); no integration fixture carries APPLICATION-ENTRY.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — class TestApplicationEntry added to existing mirrored test_LinCommunication.py; 2 failed / 42 passed (fabricated docstring, bare-T field + untyped accessors; defaults + None-no-op guard already correct)
  - [x] Step 3 — Implement model class (Green) — bare-T `RefType = None` field → PEP 526 `Optional[RefType]`; untyped accessors → typed (`Optional[RefType]`, self-return); `from __future__ import annotations` added at module top and 20 quoted self-returns de-quoted to bare names (CanTopology precedent, Rule 0003); 43 passed / 1 failed (docstring pending Step 4)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — fabricated class docstring wiped, replaced with Table 6.97 Note verbatim ("Schedule table entry for application messages."); per-attr inline comment + getter docstring + setter docstring verbatim (setter + None-no-op sentence); 44 passed
  - [x] Step 5 — Write reader/writer round-trip test (Red) — extended tests/test_armodel/parser/test_arxml_parser_network_handlers.py (frameTriggeringRef value + DEST asserted, absent-ref → None, None element → None; DEST fixture corrected to LIN-FRAME-TRIGGERING per XSD) + new TestApplicationEntryRoundTrip in tests/test_armodel/writer/test_writer_lin_schedule_entries.py (field-value round-trip, omit-absent-ref, omit-None-entry); all pass on first run — reader/writer already value-correct (existing full-table round-trip asserted values); no Red observed
  - [x] Step 6 — Update parser & writer (Green) — N/A: coverage already present and spec-correct, no edits needed; evidence — parser getApplicationEntry (arxml_parser.py L9229: readScheduleTableEntry + setFrameTriggeringRef via getChildElementOptionalRefType, dispatch L9327) and writer setApplicationEntry (arxml_writer.py L9325: writeScheduleTableEntry + setChildElementOptionalRefType, dispatch L9411); XSD order AR-OBJECT → SCHEDULE-TABLE-ENTRY (INTRODUCTION, DELAY, POSITION-IN-TABLE) → APPLICATION-ENTRY (FRAME-TRIGGERING-REF) matched; matched pairs setFrameTriggeringRef↔getChildElementOptionalRefType / getFrameTriggeringRef↔setChildElementOptionalRefType; 276 passed
  - [x] Step 7 — Update checklist comment — 6-column format with release column, rows in source order (getter-first scalar pair); `# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.97, p.433`; reader [x] on setFrameTriggeringRef, writer [x] on getFrameTriggeringRef; no `# Spec verified:` stamp (9b deferred to batch confirmation)
  - [x] Step 8 — Deviations (fixed in step notes: bare-T `RefType = None` 0..1 field → PEP 526 `Optional[RefType]`; untyped accessors → typed self-returning; fabricated docstring → Table 6.97 Note verbatim; old 4-column checklist → 6-column with `# Spec:` + release column. Consumer note: `from __future__ import annotations` added to LinCommunication.py and 20 pre-existing quoted self-returns de-quoted to bare names — 3.8-safe for get_type_hints pins. No unresolved deviations; no stale entries in docs/examples/method_deviation_by_class*.md; no placeholders — Base ScheduleTableEntry already stamped R23-11)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28: 13115 passed / 0 failed, lint clean + black clean on touched files (full-repo black check: 35 pre-existing baseline files untouched by this class, verified via stash); 9b deferred to batch confirmation (user instruction)

- [ ] `LinScheduleTable` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `LinCommunicationConnector` — CommunicationConnector — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinTopology.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `FlexrayFrameTriggering` — FrameTriggering — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayCommunication.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `FlexrayCommunicationConnector` — CommunicationConnector — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayTopology.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `FlexrayCommunicationController` — CommunicationController — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayTopology.py
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

- [ ] `FlexrayPhysicalChannel` — PhysicalChannel — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayTopology.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `DataMapping` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/DataMapping.py
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

- [ ] `IndexedArrayElement` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/DataMapping.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SenderRecRecordElementMapping` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/DataMapping.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SenderRecRecordTypeMapping` — SenderRecCompositeTypeMapping — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/DataMapping.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SenderReceiverToSignalMapping` — DataMapping — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/DataMapping.py
  - after `DataMapping`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SenderReceiverToSignalGroupMapping` — DataMapping — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/DataMapping.py
  - after `DataMapping`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `DefaultValueElement` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py
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

- [ ] `FrameMapping` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `ISignalMapping` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `TargetIPduRef` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `Gateway` — FibexElement — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py
  - after `FrameMapping`
  - after `ISignalMapping`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
