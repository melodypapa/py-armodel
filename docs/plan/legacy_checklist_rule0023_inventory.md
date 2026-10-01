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
