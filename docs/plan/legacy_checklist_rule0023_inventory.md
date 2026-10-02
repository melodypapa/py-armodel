# Legacy-format checklist inventory (Rule 0023 re-sync survey)

Generated 2026-10-02 by `scripts/eval_skill_static_checks.py` (mechanical scan of `src/armodel/models/**`).

A checklist whose method rows end at the `test` column — no `reader`/`writer` columns, no per-row
release token — is **legacy format** (Rule 0023, added 2026-10-01). Its `# Spec verified:` stamp
certifies the old bar only: the class is **not** synced against the current rules. When a sync is
invoked for (or touches) one of these classes, remove the stale marker at session start and run the
full 9-step workflow from Step 1 (both Red→Green pairs); at Step 7 write the 6-column format.

**Total: 97 legacy blocks** — 91 carry a stale `Spec verified`/`XSD verified` marker, 6 carry none.

Drain plan: one class per session (Rule 0017), highest-traffic packages first — CommonStructure (34),
MeasurementCalibrationSupport (20), ResourceConsumption (10), ApplicationAttributes (8),
GeneralTemplateClasses (6). The inventory never fails the static checker by itself (non-blocking).

## Inventory (file → class → stale marker)

  - src/armodel/models/M2/AUTOSARTemplates/AbstractPlatform/__init__.py: ApplicationInterface — stale stamp: none
  - src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py: RoleBasedBswModuleEntryAssignment — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py: BswServiceDependency — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py: ApplicationValueSpecification — stale stamp: none
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py: ApplicationRuleBasedValueSpecification — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py: AliasNameAssignment — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py: AliasNameSet — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/McGroups.py: McGroup — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/McGroups.py: McGroupDataRefSet — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py: RptAccessEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py: RptEnablerImplTypeEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py: RptExecutionControlEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py: RptPreparationEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py: RptExecutionContext — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py: RptSwPrototypingAccess — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py: RptServicePoint — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py: McFunctionDataRefSet — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py: RptExecutableEntityEvent — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py: RptExecutableEntity — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py: RptComponent — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py: RptSupportData — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py: McDataAccessDetails — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py: McParameterElementGroup — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py: McSwEmulationMethodSupport — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py: ImplementationElementInParameterInstanceRef — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py: McFunction — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py: RoleBasedMcDataAssignment — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py: McDataInstance — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py: McSupportData — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py: ExecutionTime — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py: MemorySectionLocation — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py: AnalyzedExecutionTime — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py: MeasuredExecutionTime — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py: SimulatedExecutionTime — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py: RoughEstimateOfExecutionTime — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py: HeapUsage — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py: MeasuredHeapUsage — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py: RoughEstimateHeapUsage — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py: WorstCaseHeapUsage — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: DiagnosticEventNeeds — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: ComMgrUserNeeds — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: TracedFailure — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: DevelopmentError — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: DiagnosticDenominatorConditionEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: DiagnosticEnableConditionNeeds — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: DiagnosticIoControlNeeds — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: DiagnosticMonitorUpdateKindEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: DiagnosticOperationCycleNeeds — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: DiagnosticStorageConditionNeeds — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: DoIpServiceNeeds — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: ErrorTracerNeeds — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: EventAcceptanceStatusEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: FunctionInhibitionAvailabilityNeeds — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: DiagnosticIndicatorTypeEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: IndicatorStatusNeeds — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: MaxCommModeEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: ObdControlServiceNeeds — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: ObdInfoServiceNeeds — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: ObdMonitorServiceNeeds — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: ObdPidServiceNeeds — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: ObdRatioConnectionKindEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: OperationCycleTypeEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: RuntimeError — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: ServiceProviderEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: StorageConditionStatusEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: SupervisedEntityNeeds — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: SymbolicNameProps — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: TransientFault — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py: VerificationStatusIndicationModeEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/DiagnosticMapping/ServiceMapping.py: BswServiceDependencyIdent — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py: ARType — stale stamp: none
  - src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py: AREnum — stale stamp: none
  - src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py: Boolean — stale stamp: none
  - src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py: RefType — stale stamp: none
  - src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py: ArgumentDirectionEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py: ByteOrderEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py: SenderReceiverAnnotation — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py: ClientServerAnnotation — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py: IoHwAbstractionServerAnnotation — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py: ModePortAnnotation — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py: NvDataPortAnnotation — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py: ParameterPortAnnotation — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py: TriggerPortAnnotation — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py: DelegatedPortAnnotation — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py: AtomicSwComponentType — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py: ServerArgumentImplPolicyEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py: ArgumentDataPrototype — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py: ClientServerOperation — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py: ClientServerInterface — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/RPTScenario.py: RptServicePointEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/RPTScenario.py: RptImplPolicy — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/RPTScenario.py: RptExecutableEntityProperties — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/AccessCount.py: RteApiReturnValueProvisionEnum — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/AccessCount.py: AbstractAccessPoint — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/AccessCount.py: AccessCount — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/AccessCount.py: AccessCountSet — stale stamp: Spec verified: R23-11
  - src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/__init__.py: SwcExclusiveAreaPolicy — stale stamp: Spec verified: R23-11
All mechanical checks passed.

## Rule-based audit (skill-rule check, 2026-10-02)

Run with: `python3 scripts/audit_legacy_checklists.py` (committed alongside this doc).
It audits every legacy class against its spec table with the checks automation can perform:

- **Rule 0002 / 0001.3** — field-to-spec cross-check in both directions (spec attributes missing in the model; members not in the table → Rule 0019 legacy-combine candidates), plus the Base chain (Rule 0001.2) and enum literal sets (Rule 0002). Handles the corpus traps: trailing-caption layout, page-split table halves (unioned), wrap-mangled camelCase names, `Kind=ref/iref` → `Ref`/`IRef` suffix and `*` → plural member naming (Rule 0001.5), `(ordered)` markers, glossary-table bleed filters.
- **Rule 0022** — member annotation shape vs the table's multiplicity column (0..1 → `Optional[T]`, 0..* → `List[T]`, 1 → `T`).
- **Rule 0001.7** — reader/writer coverage: parser must call the member's mutator, writer its getter.
- **Rule 0003** — trailing `# type:` member declarations (legacy form).
- **Rule 0012** — class docstring vs the spec `Note` (whitespace-collapsed; soft flag).
- **Rule 0023** — the stale marker itself (informational; removed at re-sync session start).

**audited: 97 | DRIFT 3 | FORMAT-ONLY 70 | REVIEW 24** — every one of the 97 owes the Rule 0023 full re-sync regardless of verdict;
the verdict only sets the drain order and flags classes whose re-sync will need real repair work:

- **DRIFT (3)** — hard findings; repair work guaranteed during re-sync:
  - `ServiceProviderEnum` (ServiceNeeds.py) — spec literal `watchDogManager` missing in model (R23-11 Table, second table copy).
  - `ServerArgumentImplPolicyEnum` (PortInterface/__init__.py) — spec literal `innerPort` missing; model carries `bidirectional`/`firstToSecond`/`secondToFirst` not in the R23-11 table (cross-corpus drift, arbitration at re-sync).
  - `IoHwAbstractionServerAnnotation` (ApplicationAttributes/__init__.py) — most of the R23-11 Table 4.47 members (age, argument, bswResolution, dataElement, failureMonitoring, …) never modeled; class only has filteringDebouncing/pulseTest.
- **REVIEW (24)** — soft findings: 13 with **no Class/Enumeration table in either corpus** (existing skip-arbitration precedents apply — confirm at re-sync), 10 with a class docstring differing from the spec `Note` (Rule 0012 verbatim rewrite needed), 1 enum literal-order deviation (Rule 0001.11).
- **FORMAT-ONLY (70)** — members, multiplicity shapes, reader/writer coverage, literals and Base all match the spec; only the legacy 4-column format + stale marker re-run is owed.

Reader/writer coverage is NOT the problem in this population (0 findings) — the re-syncs are mainly
checklist-format rewrites + docstring verbatim refreshes, except the 3 DRIFT classes above.

<details><summary>Full per-class audit findings</summary>

```
=== Rule 0023 legacy-checklist audit (skill-rule based) ===
audited: 97 | DRIFT 3 | FORMAT-ONLY 70 | REVIEW 24

[DRIFT] ServiceProviderEnum (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Enumeration)
    - R0002 missing literals: ['watchDogManager']

[DRIFT] IoHwAbstractionServerAnnotation (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Class)
    - R0002 spec attr missing in model: age (mult 0..1, kind aggr)
    - R0002 spec attr missing in model: argument (mult 0..1, kind ref)
    - R0002 spec attr missing in model: bswResolution (mult 0..1, kind attr)
    - R0002 spec attr missing in model: dataElement (mult 0..1, kind ref)
    - R0002 spec attr missing in model: failureMonitoring (mult 0..1, kind ref)
    - R0012 class docstring differs from spec Note (review verbatim)

[DRIFT] ServerArgumentImplPolicyEnum (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Enumeration)
    - R0002 missing literals: ['innerPort']

[REVIEW] ApplicationInterface (src/armodel/models/M2/AUTOSARTemplates/AbstractPlatform/__init__.py)
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_FO_TPS_AbstractPlatformSpecification.md (Class)
    - R0012 class docstring differs from spec Note (review verbatim)

[REVIEW] ApplicationValueSpecification (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py)
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_DiagnosticExtractTemplate.md (Class)
    - R0012 class docstring differs from spec Note (review verbatim)

[REVIEW] AliasNameSet (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)
    - R0012 class docstring differs from spec Note (review verbatim)

[REVIEW] McGroup (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/McGroups.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)
    - R0012 class docstring differs from spec Note (review verbatim)

[REVIEW] McGroupDataRefSet (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/McGroups.py)
    - R0023 stale marker: Spec verified: R23-11
    - no Class/Enumeration table in R23-11 or R4.3.1 corpora (arbitration/skip precedent applies)

[REVIEW] McFunctionDataRefSet (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - no Class/Enumeration table in R23-11 or R4.3.1 corpora (arbitration/skip precedent applies)

[REVIEW] RptEnablerImplTypeEnum (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Enumeration)
    - R0001.11 literal order differs from spec display order

[REVIEW] RptPreparationEnum (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Enumeration)
    - R0012 class docstring differs from spec Note (review verbatim)

[REVIEW] RptSupportData (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)
    - R0012 class docstring differs from spec Note (review verbatim)

[REVIEW] ImplementationElementInParameterInstanceRef (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)
    - R0012 class docstring differs from spec Note (review verbatim)

[REVIEW] ExecutionTime (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - no Class/Enumeration table in R23-11 or R4.3.1 corpora (arbitration/skip precedent applies)

[REVIEW] HeapUsage (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py)
    - R0023 stale marker: Spec verified: R23-11
    - no Class/Enumeration table in R23-11 or R4.3.1 corpora (arbitration/skip precedent applies)

[REVIEW] DoIpServiceNeeds (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - no Class/Enumeration table in R23-11 or R4.3.1 corpora (arbitration/skip precedent applies)

[REVIEW] TracedFailure (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - no Class/Enumeration table in R23-11 or R4.3.1 corpora (arbitration/skip precedent applies)

[REVIEW] AREnum (src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py)
    - no Class/Enumeration table in R23-11 or R4.3.1 corpora (arbitration/skip precedent applies)

[REVIEW] ARType (src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py)
    - no Class/Enumeration table in R23-11 or R4.3.1 corpora (arbitration/skip precedent applies)

[REVIEW] Boolean (src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py)
    - no Class/Enumeration table in R23-11 or R4.3.1 corpora (arbitration/skip precedent applies)

[REVIEW] RefType (src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py)
    - no Class/Enumeration table in R23-11 or R4.3.1 corpora (arbitration/skip precedent applies)

[REVIEW] DelegatedPortAnnotation (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Class)
    - R0012 class docstring differs from spec Note (review verbatim)

[REVIEW] SenderReceiverAnnotation (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - no Class/Enumeration table in R23-11 or R4.3.1 corpora (arbitration/skip precedent applies)

[REVIEW] AtomicSwComponentType (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - no Class/Enumeration table in R23-11 or R4.3.1 corpora (arbitration/skip precedent applies)

[REVIEW] ClientServerInterface (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)
    - R0012 class docstring differs from spec Note (review verbatim)

[REVIEW] RptServicePointEnum (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/RPTScenario.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Enumeration)
    - R0012 class docstring differs from spec Note (review verbatim)

[REVIEW] AbstractAccessPoint (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/AccessCount.py)
    - R0023 stale marker: Spec verified: R23-11
    - no Class/Enumeration table in R23-11 or R4.3.1 corpora (arbitration/skip precedent applies)

[FORMAT-ONLY] BswServiceDependency (src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] RoleBasedBswModuleEntryAssignment (src/armodel/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] ApplicationRuleBasedValueSpecification (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Constants/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] AliasNameAssignment (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] RptAccessEnum (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Enumeration)

[FORMAT-ONLY] RptComponent (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] RptExecutableEntity (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] RptExecutableEntityEvent (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] RptExecutionContext (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] RptExecutionControlEnum (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Enumeration)

[FORMAT-ONLY] RptServicePoint (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] RptSwPrototypingAccess (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] McDataAccessDetails (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] McDataInstance (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] McFunction (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] McParameterElementGroup (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] McSupportData (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] McSwEmulationMethodSupport (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] RoleBasedMcDataAssignment (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] AnalyzedExecutionTime (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] MeasuredExecutionTime (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] MemorySectionLocation (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] RoughEstimateOfExecutionTime (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] SimulatedExecutionTime (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/ExecutionTime/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] MeasuredHeapUsage (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] RoughEstimateHeapUsage (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] WorstCaseHeapUsage (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] ComMgrUserNeeds (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] DevelopmentError (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] DiagnosticDenominatorConditionEnum (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Enumeration)

[FORMAT-ONLY] DiagnosticEnableConditionNeeds (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Class)

[FORMAT-ONLY] DiagnosticEventNeeds (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] DiagnosticIndicatorTypeEnum (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_DiagnosticExtractTemplate.md (Enumeration)

[FORMAT-ONLY] DiagnosticIoControlNeeds (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] DiagnosticMonitorUpdateKindEnum (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Enumeration)

[FORMAT-ONLY] DiagnosticOperationCycleNeeds (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Class)

[FORMAT-ONLY] DiagnosticStorageConditionNeeds (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Class)

[FORMAT-ONLY] ErrorTracerNeeds (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] EventAcceptanceStatusEnum (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Enumeration)

[FORMAT-ONLY] FunctionInhibitionAvailabilityNeeds (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] IndicatorStatusNeeds (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Class)

[FORMAT-ONLY] MaxCommModeEnum (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Enumeration)

[FORMAT-ONLY] ObdControlServiceNeeds (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_DiagnosticExtractTemplate.md (Class)

[FORMAT-ONLY] ObdInfoServiceNeeds (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] ObdMonitorServiceNeeds (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_DiagnosticExtractTemplate.md (Class)

[FORMAT-ONLY] ObdPidServiceNeeds (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] ObdRatioConnectionKindEnum (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Enumeration)

[FORMAT-ONLY] OperationCycleTypeEnum (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Enumeration)

[FORMAT-ONLY] RuntimeError (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] StorageConditionStatusEnum (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Enumeration)

[FORMAT-ONLY] SupervisedEntityNeeds (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] SymbolicNameProps (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Class)

[FORMAT-ONLY] TransientFault (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Class)

[FORMAT-ONLY] VerificationStatusIndicationModeEnum (src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Enumeration)

[FORMAT-ONLY] BswServiceDependencyIdent (src/armodel/models/M2/AUTOSARTemplates/DiagnosticExtract/DiagnosticMapping/ServiceMapping.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_DiagnosticExtractTemplate.md (Class)

[FORMAT-ONLY] ArgumentDirectionEnum (src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Enumeration)

[FORMAT-ONLY] ByteOrderEnum (src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_DiagnosticExtractTemplate.md (Enumeration)

[FORMAT-ONLY] ClientServerAnnotation (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Class)

[FORMAT-ONLY] ModePortAnnotation (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Class)

[FORMAT-ONLY] NvDataPortAnnotation (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Class)

[FORMAT-ONLY] ParameterPortAnnotation (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Class)

[FORMAT-ONLY] TriggerPortAnnotation (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/ApplicationAttributes/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Class)

[FORMAT-ONLY] ArgumentDataPrototype (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] ClientServerOperation (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] RptExecutableEntityProperties (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/RPTScenario.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] RptImplPolicy (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/RPTScenario.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] AccessCount (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/AccessCount.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] AccessCountSet (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/AccessCount.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.md (Class)

[FORMAT-ONLY] RteApiReturnValueProvisionEnum (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/AccessCount.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Enumeration)

[FORMAT-ONLY] SwcExclusiveAreaPolicy (src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/__init__.py)
    - R0023 stale marker: Spec verified: R23-11
    - spec: R23-11 autosar/R23-11/markdown/AUTOSAR_CP_TPS_SoftwareComponentTemplate.md (Class)
```

</details>

## Re-sync drain (batch 1, 2026-10-02)

Executed on `feature/legacy-checklist-resync` (batch mode, stamps deferred to batch confirmation):

- **84 classes re-synced to the 6-column bar**: stale markers removed, docstrings wiped and rewritten
  verbatim from the spec `Note`, legacy 4-column checklists converted to the current format with
  reader/writer/release columns. Tooling: `scripts/legacy_resync_apply.py` (consumes
  `audit_legacy_checklists.py --dump`).
- **Real drift repaired (8 classes)**:
  - `AliasNameAssignment` / `AliasNameSet` — full read/write chains added (were completely
    unwired) + `ARPackage.createAliasNameSet` factory + ELEMENTS dispatch + round-trip tests.
  - `ApplicationInterface` — full read/write chain (ATTRIBUTES/FIELD, COMMANDS/CLIENT-SERVER-OPERATION,
    INDICATIONS/VARIABLE-DATA-PROTOTYPE) + new `writeField` + `ARPackage.createApplicationInterface`
    factory + dispatch + round-trip tests.
  - `ApplicationValueSpecification` — SW-AXIS-CONTS reader/writer added (was silently dropped).
  - `IoHwAbstractionServerAnnotation` — 5 never-modeled members added (age, argumentRef,
    bswResolution, dataElementRef, failureMonitoringRef) with reader/writer coverage + round-trip test.
  - `ServiceProviderEnum` — `watchDogManager` literal added (R23-11 Table 13.x / XSD WATCH-DOG-MANAGER).
- **Deviation noted, arbitration pending**: `ServerArgumentImplPolicyEnum` — R23-11 defines
  `innerPort`; the model carries `bidirectional`/`firstToSecond`/`secondToFirst` not in the table.
- **Verification**: battery 15,915 passed / 0 failed; ruff + flake8 clean; black clean except the
  pre-existing main set.
- **Remaining inventory: 13 blocks** — the no-spec-table set below, pending per-class arbitration
  (table-less classes: skip / XSD-only / R4.4-corpus decision). They stay legacy until ruled on.

## Batch 9b stamp wave (2026-10-02, user confirmation)

`# Spec verified: R23-11` written on **83 of the 84 re-synced classes** (battery 15,915/0 at stamping).
Withheld, pending user decisions:
- `ServerArgumentImplPolicyEnum` — literal arbitration (R23-11 `innerPort` vs model's
  `bidirectional`/`firstToSecond`/`secondToFirst`) unresolved.
- the 13 no-spec-table blocks above — per-class skip / XSD-only / R4.4-corpus ruling unresolved.
