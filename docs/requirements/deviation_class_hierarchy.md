# Class Hierarchy Deviation Report

This report shows deviations between the documented AUTOSAR M2 class hierarchy
and the actual Python implementation class hierarchy.

## Summary

- ✓ **Match**: 524 classes with correct hierarchy
- ✗ **Missing**: 1076 classes documented but not found
- ⚠ **Hierarchy Mismatch**: 17 classes with wrong parent/abstract
- + **Extra**: 82 undocumented classes
- **Total Documented Classes**: 1617
- **Total Deviations**: 1175

## Hierarchy Mismatches

| Status | Class | Hierarchy | Notes |
|--------|-------|-----------|-------|
| ⚠ MISMATCH | AUTOSARTemplates.AutosarTopLevelStructure.AUTOSAR | **Documented:**<br>Parent: ARObject<br>Type: Concrete<br><br>**Actual:**<br>Parent: AbstractAUTOSAR<br>Type: Concrete | parent mismatch (expected ARObject, got AbstractAUTOSAR) |
| ⚠ MISMATCH | AUTOSARTemplates.GenericStructure.AbstractStructure.AtpPrototype | **Documented:**<br>Parent: AtpFeature<br>Type: Abstract<br><br>**Actual:**<br>Parent: AtpBlueprintable<br>Type: Abstract | parent mismatch (expected AtpFeature, got AtpBlueprintable) |
| ⚠ MISMATCH | AUTOSARTemplates.GenericStructure.AbstractStructure.AtpStructureElement | **Documented:**<br>Parent: AtpFeature<br>Type: Abstract<br><br>**Actual:**<br>Parent: AtpBlueprintable<br>Type: Abstract | parent mismatch (expected AtpFeature, got AtpBlueprintable) |
| ⚠ MISMATCH | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.CollectableElement | **Documented:**<br>Parent: Identifiable<br>Type: Abstract<br><br>**Actual:**<br>Parent: ARObject<br>Type: Abstract | parent mismatch (expected Identifiable, got ARObject) |
| ⚠ MISMATCH | AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution.DiagnosticServiceTable | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete<br><br>**Actual:**<br>Parent: ARElement<br>Type: Concrete | parent mismatch (expected DiagnosticCommonElement, got ARElement) |
| ⚠ MISMATCH | AUTOSARTemplates.ECUCParameterDefTemplate.EcucConditionFormula | **Documented:**<br>Parent: FormulaExpression<br>Type: Concrete<br><br>**Actual:**<br>Parent: ARObject<br>Type: Concrete | parent mismatch (expected FormulaExpression, got ARObject) |
| ⚠ MISMATCH | AUTOSARTemplates.ECUCParameterDefTemplate.EcucParameterDerivationFormula | **Documented:**<br>Parent: FormulaExpression<br>Type: Concrete<br><br>**Actual:**<br>Parent: ARObject<br>Type: Concrete | parent mismatch (expected FormulaExpression, got ARObject) |
| ⚠ MISMATCH | AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.HwCategory | **Documented:**<br>Parent: AtpDefinition<br>Type: Concrete<br><br>**Actual:**<br>Parent: ARElement<br>Type: Concrete | parent mismatch (expected AtpDefinition, got ARElement) |
| ⚠ MISMATCH | MSR.Documentation.TextModel.LanguageDataModel.LLongName | **Documented:**<br>Parent: MixedContentForLongName<br>Type: Concrete<br><br>**Actual:**<br>Parent: LanguageSpecific<br>Type: Concrete | parent mismatch (expected MixedContentForLongName, got LanguageSpecific) |
| ⚠ MISMATCH | MSR.Documentation.TextModel.LanguageDataModel.LOverviewParagraph | **Documented:**<br>Parent: MixedContentForOverviewParagraph<br>Type: Concrete<br><br>**Actual:**<br>Parent: LanguageSpecific<br>Type: Concrete | parent mismatch (expected MixedContentForOverviewParagraph, got LanguageSpecific) |
| ⚠ MISMATCH | MSR.Documentation.TextModel.LanguageDataModel.LParagraph | **Documented:**<br>Parent: MixedContentForParagraph<br>Type: Concrete<br><br>**Actual:**<br>Parent: LanguageSpecific<br>Type: Concrete | parent mismatch (expected MixedContentForParagraph, got LanguageSpecific) |
| ⚠ MISMATCH | MSR.Documentation.TextModel.LanguageDataModel.LPlainText | **Documented:**<br>Parent: MixedContentForPlainText<br>Type: Concrete<br><br>**Actual:**<br>Parent: LanguageSpecific<br>Type: Concrete | parent mismatch (expected MixedContentForPlainText, got LanguageSpecific) |
| ⚠ MISMATCH | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.PackageableElement | **Documented:**<br>Parent: CollectableElement<br>Type: Abstract<br><br>**Actual:**<br>Parent: Identifiable<br>Type: Abstract | parent mismatch (expected CollectableElement, got Identifiable) |
| ⚠ MISMATCH | AUTOSARTemplates.CommonStructure.ServiceNeeds.ServiceDependency | **Documented:**<br>Parent: ARObject<br>Type: Abstract<br><br>**Actual:**<br>Parent: Identifiable<br>Type: Abstract | parent mismatch (expected ARObject, got Identifiable) |
| ⚠ MISMATCH | MSR.AsamHdo.Units.SingleLanguageUnitNames | **Documented:**<br>Parent: MixedContentForUnitNames<br>Type: Concrete<br><br>**Actual:**<br>Parent: ARLiteral<br>Type: Concrete | parent mismatch (expected MixedContentForUnitNames, got ARLiteral) |
| ⚠ MISMATCH | MSR.DataDictionary.SystemConstant.SwSystemconst | **Documented:**<br>Parent: AtpDefinition<br>Type: Concrete<br><br>**Actual:**<br>Parent: ARObject<br>Type: Concrete | parent mismatch (expected AtpDefinition, got ARObject) |
| ⚠ MISMATCH | AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint.TimingConstraint | **Documented:**<br>Parent: Traceable<br>Type: Abstract<br><br>**Actual:**<br>Parent: Identifiable<br>Type: Abstract | parent mismatch (expected Traceable, got Identifiable) |

## Missing Classes (Documented but Not Found)

| Status | Class | Hierarchy | Notes |
|--------|-------|-----------|-------|
| ✗ MISSING | <<atpPrototype>> PduToFrameMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AbstractClassTailoring | **Documented:**<br>Parent: DataFormatElementReference<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AbstractCondition | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AbstractEnumerationValueVariationPoint | **Documented:**<br>Parent: AttributeValueVariationPoint<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AbstractGlobalTimeDomainProps | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AbstractMultiplicityRestriction | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AbstractNumericalVariationPoint | **Documented:**<br>Parent: AttributeValueVariationPoint<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AbstractProvidedPortPrototype | **Documented:**<br>Parent: PortPrototype<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AbstractRequiredPortPrototype | **Documented:**<br>Parent: PortPrototype<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AbstractRuleBasedValueSpecification | **Documented:**<br>Parent: ValueSpecification<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AbstractSecurityEventFilter | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AbstractValueRestriction | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AbstractVariationRestriction | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AccessCount | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AccessCountSet | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AclObjectSet | **Documented:**<br>Parent: AtpBlueprintable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AclOperation | **Documented:**<br>Parent: AtpBlueprintable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AclPermission | **Documented:**<br>Parent: AtpBlueprintable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AclRole | **Documented:**<br>Parent: AtpBlueprintable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AgeConstraint | **Documented:**<br>Parent: TimingConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AggregationCondition | **Documented:**<br>Parent: AttributeCondition<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AggregationTailoring | **Documented:**<br>Parent: AttributeTailoring<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AliasNameAssignment | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AliasNameSet | **Documented:**<br>Parent: AtpBlueprintable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AnalyzedExecutionTime | **Documented:**<br>Parent: ExecutionTime<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ApplicationCompositeDataTypeSubElementRef | **Documented:**<br>Parent: SubElementRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ApplicationDeferredDataType | **Documented:**<br>Parent: ApplicationDataType<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ApplicationError | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ApplicationInterface | **Documented:**<br>Parent: PortInterface<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ApplicationPartition | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ApplicationRuleBasedValueSpecification | **Documented:**<br>Parent: CompositeRuleBasedValueArgument<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ApplicationSwComponentType | **Documented:**<br>Parent: AtomicSwComponentType<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ApplicationValueSpecification | **Documented:**<br>Parent: ValueSpecification<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ArParameterInImplementationDataInstanceRef | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ArbitraryEventTriggering | **Documented:**<br>Parent: EventTriggeringConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Area | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ArgumentDataPrototype | **Documented:**<br>Parent: AutosarDataPrototype<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ArrayValueSpecification | **Documented:**<br>Parent: CompositeValueSpecification<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AssemblySwConnector | **Documented:**<br>Parent: SwConnector<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AssignFrameId | **Documented:**<br>Parent: LinConfigurationEntry<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AssignFrameIdRange | **Documented:**<br>Parent: LinConfigurationEntry<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AssignNad | **Documented:**<br>Parent: LinConfigurationEntry<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AsynchronousServerCallPoint | **Documented:**<br>Parent: ServerCallPoint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AsynchronousServerCallResultPoint | **Documented:**<br>Parent: AbstractAccessPoint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AtomicSwComponentType | **Documented:**<br>Parent: SwComponentType<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AtpBlueprint | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AtpBlueprintMapping | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AtpDefinition | **Documented:**<br>Parent: Referrable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AtpFeature | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AttributeCondition | **Documented:**<br>Parent: AbstractMultiplicityRestriction<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AttributeTailoring | **Documented:**<br>Parent: DataFormatElementScope<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AttributeValueVariationPoint | **Documented:**<br>Parent: SwSystemconstDependentFormula<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | AutosarOperationArgumentInstance | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | AutosarVariableInstance | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Baseline | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BinaryManifestAddressableObject | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | BinaryManifestItem | **Documented:**<br>Parent: BinaryManifestAddressableObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BinaryManifestItemDefinition | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BinaryManifestItemNumericalValue | **Documented:**<br>Parent: BinaryManifestItemValue<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BinaryManifestItemPointerValue | **Documented:**<br>Parent: BinaryManifestItemValue<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BinaryManifestItemValue | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | BinaryManifestMetaDataField | **Documented:**<br>Parent: BinaryManifestAddressableObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BinaryManifestProvideResource | **Documented:**<br>Parent: BinaryManifestResource<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BinaryManifestRequireResource | **Documented:**<br>Parent: BinaryManifestResource<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BinaryManifestResource | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | BinaryManifestResourceDefinition | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BlockState | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BlueprintFormula | **Documented:**<br>Parent: SwSystemconstDependentFormula<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BlueprintGenerator | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BlueprintMapping | **Documented:**<br>Parent: AtpBlueprintMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BlueprintMappingSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BlueprintPolicy | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | BlueprintPolicyList | **Documented:**<br>Parent: BlueprintPolicy<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BlueprintPolicyNotModifiable | **Documented:**<br>Parent: BlueprintPolicy<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BlueprintPolicySingle | **Documented:**<br>Parent: BlueprintPolicy<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BooleanValueVariationPoint | **Documented:**<br>Parent: AttributeValueVariationPoint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Br | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BswAsynchronousServerCallReturnsEvent | **Documented:**<br>Parent: BswScheduleEvent<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BswCompositionTiming | **Documented:**<br>Parent: TimingExtension<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BswEntryRelationship | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BswEntryRelationshipSet | **Documented:**<br>Parent: AtpBlueprintable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BswInterruptEvent | **Documented:**<br>Parent: BswEvent<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BswMgrNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BswModeManagerErrorEvent | **Documented:**<br>Parent: BswScheduleEvent<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BswModeReceiverPolicy | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BswModuleTiming | **Documented:**<br>Parent: TimingExtension<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BswSchedulerNamePrefix | **Documented:**<br>Parent: ImplementationProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BswServiceDependency | **Documented:**<br>Parent: ServiceDependency<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BswServiceDependencyIdent | **Documented:**<br>Parent: IdentCaption<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BswTriggerDirectImplementation | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BufferProperties | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BuildAction | **Documented:**<br>Parent: BuildActionEntity<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BuildActionEntity | **Documented:**<br>Parent: AtpBlueprintable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | BuildActionEnvironment | **Documented:**<br>Parent: AtpBlueprintable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BuildActionInvocator | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BuildActionIoElement | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BuildActionManifest | **Documented:**<br>Parent: AtpBlueprintable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BuildEngineeringObject | **Documented:**<br>Parent: EngineeringObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BulkNvDataDescriptor | **Documented:**<br>Parent: AtpStructureElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BurstPatternEventTriggering | **Documented:**<br>Parent: EventTriggeringConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BusMirrorCanIdRangeMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BusMirrorCanIdToCanIdMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BusMirrorChannel | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BusMirrorChannelMapping | **Documented:**<br>Parent: FibexElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | BusMirrorChannelMappingCan | **Documented:**<br>Parent: BusMirrorChannelMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BusMirrorChannelMappingFlexray | **Documented:**<br>Parent: BusMirrorChannelMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BusMirrorChannelMappingIp | **Documented:**<br>Parent: BusMirrorChannelMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BusMirrorChannelMappingUserDefined | **Documented:**<br>Parent: BusMirrorChannelMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | BusMirrorLinPidToCanIdMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CalibrationParameterValue | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CalibrationParameterValueSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CanControllerConfiguration | **Documented:**<br>Parent: AbstractCanCommunicationControllerAttributes<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CanGlobalTimeDomainProps | **Documented:**<br>Parent: AbstractGlobalTimeDomainProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CanXlFrameTriggeringProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Caption | **Documented:**<br>Parent: MultilanguageReferrable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Chapter | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ChapterContent | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ChapterModel | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ChapterOrMsrQuery | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ClassContentConditional | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ClassTailoring | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | ClientIdDefinition | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ClientIdDefinitionSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ClientIdRange | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ClientServerAnnotation | **Documented:**<br>Parent: GeneralAnnotation<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ClientServerApplicationErrorMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ClientServerInterface | **Documented:**<br>Parent: PortInterface<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ClientServerInterfaceMapping | **Documented:**<br>Parent: PortInterfaceMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ClientServerInterfaceToBswModuleEntryBlueprintMapping | **Documented:**<br>Parent: AtpBlueprint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ClientServerOperation | **Documented:**<br>Parent: AtpStructureElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ClientServerOperationBlueprintMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ClientServerOperationComProps | **Documented:**<br>Parent: CpSoftwareClusterCommunicationResourceProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ClientServerOperationMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ClientServerToSignalMapping | **Documented:**<br>Parent: DataMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Colspec | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ComManagementMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ComMgrUserNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CommonSignalPath | **Documented:**<br>Parent: SignalPathConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CommunicationBufferLocking | **Documented:**<br>Parent: SwcSupportedFeature<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CommunicationControllerMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ComplexDeviceDriverSwComponentType | **Documented:**<br>Parent: AtomicSwComponentType<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ComponentClustering | **Documented:**<br>Parent: MappingConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ComponentInCompositionInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ComponentSeparation | **Documented:**<br>Parent: MappingConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CompositeRuleBasedValueArgument | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | CompositeRuleBasedValueSpecification | **Documented:**<br>Parent: AbstractRuleBasedValueSpecification<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CompositeValueSpecification | **Documented:**<br>Parent: ValueSpecification<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | CompositionSwComponentType | **Documented:**<br>Parent: SwComponentType<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CompuGenericMath | **Documented:**<br>Parent: FormulaExpression<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ConcreteClassTailoring | **Documented:**<br>Parent: DataFormatElementScope<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ConcretePatternEventTriggering | **Documented:**<br>Parent: EventTriggeringConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ConditionByFormula | **Documented:**<br>Parent: SwSystemconstDependentFormula<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ConditionalChangeNad | **Documented:**<br>Parent: LinConfigurationEntry<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ConfidenceInterval | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ConsistencyNeeds | **Documented:**<br>Parent: AtpBlueprintable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ConsistencyNeedsBlueprintSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ConstantReference | **Documented:**<br>Parent: ValueSpecification<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ConstantSpecification | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ConstantSpecificationMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ConstantSpecificationMappingSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ConstraintTailoring | **Documented:**<br>Parent: RestrictionWithSeverity<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ConsumedProvidedServiceInstanceGroup | **Documented:**<br>Parent: FibexElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ContainerIPdu | **Documented:**<br>Parent: IPdu<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CouplingElement | **Documented:**<br>Parent: FibexElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CouplingElementAbstractDetails | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | CouplingElementSwitchDetails | **Documented:**<br>Parent: CouplingElementAbstractDetails<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CouplingPortAsynchronousTrafficShaper | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CouplingPortConnection | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CouplingPortCreditBasedShaper | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CouplingPortRatePolicy | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CouplingPortShaper | **Documented:**<br>Parent: CouplingPortStructuralElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CouplingPortTrafficClassAssignment | **Documented:**<br>Parent: Referrable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CpSoftwareCluster | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterBinaryManifestDescriptor | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterCommunicationResource | **Documented:**<br>Parent: CpSoftwareClusterResource<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterCommunicationResourceProps | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterMappingSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterResource | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterResourcePool | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterResourceToApplicationPartitionMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterServiceResource | **Documented:**<br>Parent: CpSoftwareClusterResource<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterToApplicationPartitionMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterToEcuInstanceMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterToResourceMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CpSwClusterResourceToDiagDataElemMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CpSwClusterResourceToDiagFunctionIdMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CpSwClusterToDiagEventMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CpSwClusterToDiagRoutineSubfunctionMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CryptoEllipticCurveProps | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CryptoKeyManagementNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CryptoKeySlot | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CryptoServiceCertificate | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CryptoServiceJobNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CryptoServiceKey | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CryptoServicePrimitive | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CryptoServiceQueue | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | CryptoSignatureScheme | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DataComProps | **Documented:**<br>Parent: CpSoftwareClusterCommunicationResourceProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DataDumpEntry | **Documented:**<br>Parent: LinConfigurationEntry<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DataExchangePoint | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DataFormatElementReference | **Documented:**<br>Parent: SpecElementReference<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DataFormatElementScope | **Documented:**<br>Parent: SpecElementScope<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DataFormatTailoring | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DataInterface | **Documented:**<br>Parent: PortInterface<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DataPrototypeGroup | **Documented:**<br>Parent: AtpStructureElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DataPrototypeInClientServerInterfaceInstanceRef | **Documented:**<br>Parent: DataPrototypeInPortInterfaceInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DataPrototypeInPortInterfaceInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DataPrototypeInPortInterfaceRef | **Documented:**<br>Parent: DataPrototypeReference<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DataPrototypeInSenderReceiverInterfaceInstanceRef | **Documented:**<br>Parent: DataPrototypeInPortInterfaceInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DataPrototypeInSystemInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DataPrototypeMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DataPrototypeReference | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DataPrototypeTransformationProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DataTransformation | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DataTransformationSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsCpConfig | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsCpConsumedServiceInstance | **Documented:**<br>Parent: DdsCpServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsCpDomain | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsCpISignalToDdsTopicMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsCpPartition | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsCpProvidedServiceInstance | **Documented:**<br>Parent: DdsCpServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsCpQosProfile | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsCpServiceInstance | **Documented:**<br>Parent: AbstractServiceInstance<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DdsCpServiceInstanceEvent | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsCpServiceInstanceOperation | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsCpTopic | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsDeadline | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsDestinationOrder | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsDurability | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsDurabilityService | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsHistory | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsLatencyBudget | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsLifespan | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsLiveliness | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsOwnership | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsOwnershipStrength | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsReliability | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsResourceLimits | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsTopicData | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DdsTransportPriority | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DefItem | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DefList | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DelegatedPortAnnotation | **Documented:**<br>Parent: GeneralAnnotation<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DelegationSwConnector | **Documented:**<br>Parent: SwConnector<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DevelopmentError | **Documented:**<br>Parent: TracedFailure<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DhcpServerConfiguration | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Dhcpv6Props | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticAbstractAliasEvent | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticAbstractDataIdentifier | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticAbstractParameter | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticAccessPermission | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticAging | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticAuthRole | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticAuthRoleProxy | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticAuthTransmitCertificate | **Documented:**<br>Parent: DiagnosticAuthentication<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticAuthTransmitCertificateEvaluation | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticAuthTransmitCertificateMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticAuthentication | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticAuthenticationClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticAuthenticationConfiguration | **Documented:**<br>Parent: DiagnosticAuthentication<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticClearDiagnosticInformation | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticClearDiagnosticInformationClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticClearResetEmissionRelatedInfo | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticClearResetEmissionRelatedInfoClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticComControl | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticComControlClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticComControlSpecificChannel | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticComControlSubNodeChannel | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticCommonElement | **Documented:**<br>Parent: ARElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticCommonProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticComponentNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticCondition | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticConditionGroup | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticConnectedIndicator | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticContributionSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticControlDTCSetting | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticControlDTCSettingClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticControlEnableMaskBit | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticControlNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticCustomServiceClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticCustomServiceInstance | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticDataByIdentifier | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticDataElement | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticDataIdentifier | **Documented:**<br>Parent: DiagnosticAbstractDataIdentifier<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticDataIdentifierSet | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticDataTransfer | **Documented:**<br>Parent: DiagnosticMemoryByAddress<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticDataTransferClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticDeAuthentication | **Documented:**<br>Parent: DiagnosticAuthentication<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticDebounceAlgorithmProps | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticDemProvidedDataMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticDynamicDataIdentifier | **Documented:**<br>Parent: DiagnosticAbstractDataIdentifier<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticDynamicallyDefineDataIdentifier | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticDynamicallyDefineDataIdentifierClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEcuInstanceProps | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEcuReset | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEcuResetClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEnableCondition | **Documented:**<br>Parent: DiagnosticCondition<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEnableConditionGroup | **Documented:**<br>Parent: DiagnosticConditionGroup<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEnableConditionNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEnableConditionPortMapping | **Documented:**<br>Parent: DiagnosticSwMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEnvBswModeElement | **Documented:**<br>Parent: DiagnosticEnvModeElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEnvCompareCondition | **Documented:**<br>Parent: DiagnosticEnvConditionFormulaPart<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticEnvConditionFormula | **Documented:**<br>Parent: DiagnosticEnvConditionFormulaPart<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEnvConditionFormulaPart | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticEnvDataCondition | **Documented:**<br>Parent: DiagnosticEnvCompareCondition<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEnvDataElementCondition | **Documented:**<br>Parent: DiagnosticEnvCompareCondition<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEnvModeCondition | **Documented:**<br>Parent: DiagnosticEnvCompareCondition<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEnvModeElement | **Documented:**<br>Parent: Referrable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticEnvSwcModeElement | **Documented:**<br>Parent: DiagnosticEnvModeElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEnvironmentalCondition | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEvent | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEventManagerNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEventPortMapping | **Documented:**<br>Parent: DiagnosticSwMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEventToDebounceAlgorithmMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEventToEnableConditionGroupMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEventToOperationCycleMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEventToSecurityEventMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEventToStorageConditionGroupMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEventToTroubleCodeJ1939Mapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEventToTroubleCodeUdsMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticEventWindow | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticExtendedDataRecord | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticFimAliasEvent | **Documented:**<br>Parent: DiagnosticAbstractAliasEvent<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticFimAliasEventGroup | **Documented:**<br>Parent: DiagnosticAbstractAliasEvent<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticFimAliasEventGroupMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticFimAliasEventMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticFimEventGroup | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticFimFunctionMapping | **Documented:**<br>Parent: DiagnosticSwMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticFreezeFrame | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticFunctionIdentifier | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticFunctionIdentifierInhibit | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticFunctionInhibitSource | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticIOControl | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticIndicator | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticInfoType | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticInhibitSourceEventMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticIoControlClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticIoControlNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticIumpr | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticIumprDenominatorGroup | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticIumprGroup | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticIumprGroupIdentifier | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticIumprToFunctionIdentifierMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939ExpandedFreezeFrame | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939FreezeFrame | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939Node | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939Spn | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939SpnMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939SwMapping | **Documented:**<br>Parent: DiagnosticSwMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticMapping | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticMasterToSlaveEventMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticMeasurementIdentifier | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryAddressableRangeAccess | **Documented:**<br>Parent: DiagnosticMemoryByAddress<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryByAddress | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryDestination | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryDestinationPrimary | **Documented:**<br>Parent: DiagnosticMemoryDestination<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryDestinationUserDefined | **Documented:**<br>Parent: DiagnosticMemoryDestination<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryIdentifier | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticOperationCycle | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticOperationCycleNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticOperationCyclePortMapping | **Documented:**<br>Parent: DiagnosticSwMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticParameter | **Documented:**<br>Parent: DiagnosticAbstractParameter<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticParameterElement | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticParameterElementAccess | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticParameterIdent | **Documented:**<br>Parent: IdentCaption<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticParameterIdentifier | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticParameterSupportInfo | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticPeriodicRate | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticPowertrainFreezeFrame | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticProofOfOwnership | **Documented:**<br>Parent: DiagnosticAuthentication<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticProtocol | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticReadDTCInformation | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticReadDTCInformationClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticReadDataByIdentifier | **Documented:**<br>Parent: DiagnosticDataByIdentifier<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticReadDataByIdentifierClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticReadDataByPeriodicID | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticReadDataByPeriodicIDClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticReadMemoryByAddress | **Documented:**<br>Parent: DiagnosticMemoryAddressableRangeAccess<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticReadMemoryByAddressClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticReadScalingDataByIdentifier | **Documented:**<br>Parent: DiagnosticDataByIdentifier<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticReadScalingDataByIdentifierClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestControlOfOnBoardDevice | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestControlOfOnBoardDeviceClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestCurrentPowertrainData | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestCurrentPowertrainDataClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestDownload | **Documented:**<br>Parent: DiagnosticMemoryAddressableRangeAccess<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestDownloadClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestEmissionRelatedDTC | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestEmissionRelatedDTCClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestEmissionRelatedDTCPermanentStatus | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestEmissionRelatedDTCPermanentStatusClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestFileTransfer | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestFileTransferClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestFileTransferNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestOnBoardMonitoringTestResults | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestOnBoardMonitoringTestResultsClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestPowertrainFreezeFrameData | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestPowertrainFreezeFrameDataClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestRoutineResults | **Documented:**<br>Parent: DiagnosticRoutineSubfunction<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestUpload | **Documented:**<br>Parent: DiagnosticMemoryAddressableRangeAccess<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestUploadClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestVehicleInfo | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRequestVehicleInfoClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticResponseOnEvent | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticResponseOnEventClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRoutine | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRoutineControl | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRoutineControlClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticRoutineSubfunction | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticSecureCodingMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticSecurityAccess | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticSecurityAccessClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticSecurityEventReportingModeMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticSecurityLevel | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticServiceClass | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticServiceDataMapping | **Documented:**<br>Parent: DiagnosticSwMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticServiceInstance | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticServiceMappingDiagTarget | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticServiceSwMapping | **Documented:**<br>Parent: DiagnosticSwMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticSession | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticSessionControl | **Documented:**<br>Parent: DiagnosticServiceInstance<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticSessionControlClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticStartRoutine | **Documented:**<br>Parent: DiagnosticRoutineSubfunction<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticStopRoutine | **Documented:**<br>Parent: DiagnosticRoutineSubfunction<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticStorageCondition | **Documented:**<br>Parent: DiagnosticCondition<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticStorageConditionGroup | **Documented:**<br>Parent: DiagnosticConditionGroup<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticStorageConditionNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticStorageConditionPortMapping | **Documented:**<br>Parent: DiagnosticSwMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticSupportInfoByte | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticSwMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticTestIdentifier | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticTestResult | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticTestRoutineIdentifier | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticTransferExit | **Documented:**<br>Parent: DiagnosticMemoryByAddress<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticTransferExitClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCode | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeGroup | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeJ1939 | **Documented:**<br>Parent: DiagnosticTroubleCode<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeObd | **Documented:**<br>Parent: DiagnosticTroubleCode<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeProps | **Documented:**<br>Parent: DiagnosticCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeUds | **Documented:**<br>Parent: DiagnosticTroubleCode<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeUdsToTroubleCodeObdMapping | **Documented:**<br>Parent: DiagnosticMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticUploadDownloadNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticVerifyCertificateBidirectional | **Documented:**<br>Parent: DiagnosticAuthentication<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticVerifyCertificateUnidirectional | **Documented:**<br>Parent: DiagnosticAuthentication<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticWriteDataByIdentifier | **Documented:**<br>Parent: DiagnosticDataByIdentifier<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticWriteDataByIdentifierClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticWriteMemoryByAddress | **Documented:**<br>Parent: DiagnosticMemoryAddressableRangeAccess<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticWriteMemoryByAddressClass | **Documented:**<br>Parent: DiagnosticServiceClass<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DiagnosticsCommunicationSecurityNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DltApplication | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DltArgument | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DltConfig | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DltContext | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DltEcu | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DltLogChannel | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DltMessage | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DoIpActivationLineNeeds | **Documented:**<br>Parent: DoIpServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DoIpConfig | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DoIpGidNeeds | **Documented:**<br>Parent: DoIpServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DoIpGidSynchronizationNeeds | **Documented:**<br>Parent: DoIpServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DoIpInterface | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DoIpPowerModeStatusNeeds | **Documented:**<br>Parent: DoIpServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DoIpRoutingActivation | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DoIpRoutingActivationAuthenticationNeeds | **Documented:**<br>Parent: DoIpServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DoIpRoutingActivationConfirmationNeeds | **Documented:**<br>Parent: DoIpServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DoIpServiceNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | DocumentElementScope | **Documented:**<br>Parent: SpecElementReference<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Documentation | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DocumentationBlock | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | DocumentationContext | **Documented:**<br>Parent: MultilanguageReferrable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | E2EProfileCompatibilityProps | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EOCEventRef | **Documented:**<br>Parent: EOCExecutableEntityRefAbstract<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EOCExecutableEntityRefGroup | **Documented:**<br>Parent: EOCExecutableEntityRefAbstract<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EcuAbstractionSwComponentType | **Documented:**<br>Parent: AtomicSwComponentType<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EcuPartition | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EcuResourceEstimation | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EcuTiming | **Documented:**<br>Parent: TimingExtension<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EmphasisText | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EndToEndTransformationDescription | **Documented:**<br>Parent: TransformationDescription<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EndToEndTransformationISignalProps | **Documented:**<br>Parent: TransformationISignalProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Entry | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EnumerationMappingEntry | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EnumerationMappingTable | **Documented:**<br>Parent: PackageableElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ErrorTracerNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EthGlobalTimeDomainProps | **Documented:**<br>Parent: AbstractGlobalTimeDomainProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EthGlobalTimeManagedCouplingPort | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EthIpProps | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EthTSynCrcFlags | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EthTSynSubTlvConfig | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EthTcpIpIcmpProps | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EthTcpIpProps | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EthTpConfig | **Documented:**<br>Parent: TpConfig<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EthTpConnection | **Documented:**<br>Parent: TpConnection<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EthernetFrameTriggering | **Documented:**<br>Parent: FrameTriggering<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EthernetWakeupSleepOnDatalineConfig | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EthernetWakeupSleepOnDatalineConfigSet | **Documented:**<br>Parent: FibexElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EvaluatedVariantSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EventObdReadinessGroup | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | EventTriggeringConstraint | **Documented:**<br>Parent: TimingConstraint<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | ExclusiveAreaNestingOrder | **Documented:**<br>Parent: Referrable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ExecutableEntityActivationReason | **Documented:**<br>Parent: ImplementationProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ExecutionTime | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | ExecutionTimeConstraint | **Documented:**<br>Parent: TimingConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ExternalTriggerOccurredEvent | **Documented:**<br>Parent: RTEEvent<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMAttributeDef | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMAttributeValue | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMConditionByFeaturesAndAttributes | **Documented:**<br>Parent: FMFormulaByFeaturesAndAttributes<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMConditionByFeaturesAndSwSystemconsts | **Documented:**<br>Parent: FMFormulaByFeaturesAndSwSystemconsts<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMFeature | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMFeatureDecomposition | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMFeatureMap | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMFeatureMapAssertion | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMFeatureMapCondition | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMFeatureMapElement | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMFeatureModel | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMFeatureRelation | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMFeatureRestriction | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMFeatureSelection | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMFeatureSelectionSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FMFormulaByFeaturesAndAttributes | **Documented:**<br>Parent: FormulaExpression<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | FMFormulaByFeaturesAndSwSystemconsts | **Documented:**<br>Parent: SwSystemconstDependentFormula<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | Field | **Documented:**<br>Parent: AutosarDataPrototype<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FirewallRule | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FirewallRuleProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FlexrayArTpChannel | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FlexrayArTpConfig | **Documented:**<br>Parent: TpConfig<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FlexrayArTpConnection | **Documented:**<br>Parent: TpConnection<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FlexrayArTpNode | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FlexrayFifoConfiguration | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FlexrayFifoRange | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FlexrayTpConfig | **Documented:**<br>Parent: TpConfig<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FlexrayTpConnection | **Documented:**<br>Parent: TpConnection<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FlexrayTpConnectionControl | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FlexrayTpEcu | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FlexrayTpNode | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FlexrayTpPduPool | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FloatValueVariationPoint | **Documented:**<br>Parent: AttributeValueVariationPoint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ForbiddenSignalPath | **Documented:**<br>Parent: SignalPathConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FormulaExpression | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | FrGlobalTimeDomainProps | **Documented:**<br>Parent: AbstractGlobalTimeDomainProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FramePid | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FreeFormat | **Documented:**<br>Parent: FreeFormatEntry<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FunctionInhibitionAvailabilityNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FunctionInhibitionNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | FurtherActionByteNeeds | **Documented:**<br>Parent: DoIpServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | GeneralPurposeConnection | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | GenericModelReference | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | GlobalSupervisionNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | GlobalTimeCanMaster | **Documented:**<br>Parent: GlobalTimeMaster<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | GlobalTimeCanSlave | **Documented:**<br>Parent: GlobalTimeSlave<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | GlobalTimeCorrectionProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | GlobalTimeCouplingPortProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | GlobalTimeDomain | **Documented:**<br>Parent: FibexElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | GlobalTimeEthMaster | **Documented:**<br>Parent: GlobalTimeMaster<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | GlobalTimeEthSlave | **Documented:**<br>Parent: GlobalTimeSlave<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | GlobalTimeFrMaster | **Documented:**<br>Parent: GlobalTimeMaster<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | GlobalTimeFrSlave | **Documented:**<br>Parent: GlobalTimeSlave<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | GlobalTimeGateway | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | GlobalTimeMaster | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | GlobalTimeSlave | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | HardwareTestNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | HttpTp | **Documented:**<br>Parent: TransportProtocolConfiguration<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | HwDescriptionEntity | **Documented:**<br>Parent: Referrable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | HwElement | **Documented:**<br>Parent: HwDescriptionEntity<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | HwPin | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | HwPinConnector | **Documented:**<br>Parent: Describable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | HwPinGroup | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | HwPinGroupConnector | **Documented:**<br>Parent: Describable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | HwPinGroupContent | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | HwPortMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IEEE1722TpAafConnection | **Documented:**<br>Parent: IEEE1722TpAvConnection<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IEEE1722TpAcfBus | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | IEEE1722TpAcfBusPart | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | IEEE1722TpAcfCan | **Documented:**<br>Parent: IEEE1722TpAcfBus<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IEEE1722TpAcfCanPart | **Documented:**<br>Parent: IEEE1722TpAcfBusPart<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IEEE1722TpAcfConnection | **Documented:**<br>Parent: IEEE1722TpConnection<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IEEE1722TpAcfLin | **Documented:**<br>Parent: IEEE1722TpAcfBus<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IEEE1722TpAcfLinPart | **Documented:**<br>Parent: IEEE1722TpAcfBusPart<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IEEE1722TpAvConnection | **Documented:**<br>Parent: IEEE1722TpConnection<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | IEEE1722TpConfig | **Documented:**<br>Parent: TpConfig<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IEEE1722TpConnection | **Documented:**<br>Parent: ARElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | IEEE1722TpCrfConnection | **Documented:**<br>Parent: IEEE1722TpAvConnection<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IEEE1722TpIidcConnection | **Documented:**<br>Parent: IEEE1722TpAvConnection<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IEEE1722TpRvfConnection | **Documented:**<br>Parent: IEEE1722TpAvConnection<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IPSecConfig | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IPSecConfigProps | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IPSecRule | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IPv6ExtHeaderFilterList | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IPv6ExtHeaderFilterSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ISignalProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IdsCommonElement | **Documented:**<br>Parent: ARElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | IdsDesign | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IdsMapping | **Documented:**<br>Parent: IdsCommonElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | IdsMgrCustomTimestampNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IdsMgrNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IdsPlatformInstantiation | **Documented:**<br>Parent: AtpStructureElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | IdsmInstance | **Documented:**<br>Parent: IdsCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IdsmModuleInstantiation | **Documented:**<br>Parent: IdsPlatformInstantiation<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IdsmProperties | **Documented:**<br>Parent: IdsCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IdsmRateLimitation | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IdsmSignatureSupportAp | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IdsmSignatureSupportCp | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IdsmTrafficLimitation | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Ieee1722Tp | **Documented:**<br>Parent: TransportProtocolConfiguration<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Ieee1722TpEthernetFrame | **Documented:**<br>Parent: AbstractEthernetFrame<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ImplementationDataTypeElementInPortInterfaceRef | **Documented:**<br>Parent: DataPrototypeReference<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ImplementationDataTypeSubElementRef | **Documented:**<br>Parent: SubElementRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ImplementationElementInParameterInstanceRef | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ImpositionTime | **Documented:**<br>Parent: AtpBlueprintable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IndentSample | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IndexEntry | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IndicatorStatusNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | InnerDataPrototypeGroupInCompositionInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | InnerRunnableEntityGroupInCompositionInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | InstanceEventInCompositionInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | InstantiationDataDefProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | InstantiationRTEEventProps | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | InstantiationTimingEventProps | **Documented:**<br>Parent: InstantiationRTEEventProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IntegerValueVariationPoint | **Documented:**<br>Parent: AttributeValueVariationPoint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | InterpolationRoutine | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | InterpolationRoutineMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | InterpolationRoutineMappingSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | InvalidationPolicy | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | InvertCondition | **Documented:**<br>Parent: AbstractCondition<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | IoHwAbstractionServerAnnotation | **Documented:**<br>Parent: GeneralAnnotation<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Ipv4ArpProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Ipv4AutoIpProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Ipv4DhcpServerConfiguration | **Documented:**<br>Parent: Describable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Ipv4FragmentationProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Ipv4Props | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Ipv6DhcpServerConfiguration | **Documented:**<br>Parent: Describable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Ipv6FragmentationProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Ipv6NdpProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Ipv6Props | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | J1939Cluster | **Documented:**<br>Parent: AbstractCanCluster<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | J1939ControllerApplication | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | J1939ControllerApplicationToJ1939NmNodeMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | J1939DcmDm19Support | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | J1939DcmIPdu | **Documented:**<br>Parent: IPdu<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | J1939NodeName | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | J1939RmIncomingRequestServiceNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | J1939RmOutgoingRequestServiceNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | J1939SharedAddressCluster | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | J1939TpConfig | **Documented:**<br>Parent: TpConfig<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | J1939TpConnection | **Documented:**<br>Parent: TpConnection<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | J1939TpNode | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | J1939TpPg | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LVerbatim | **Documented:**<br>Parent: MixedContentForVerbatim<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LabeledItem | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LabeledList | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LatencyTimingConstraint | **Documented:**<br>Parent: TimingConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LifeCycleState | **Documented:**<br>Parent: AtpBlueprintable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LifeCycleStateDefinitionGroup | **Documented:**<br>Parent: AtpBlueprintable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LimitValueVariationPoint | **Documented:**<br>Parent: AbstractNumericalVariationPoint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LinConfigurableFrame | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LinErrorResponse | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LinEventTriggeredFrame | **Documented:**<br>Parent: LinFrame<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LinOrderedConfigurableFrame | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LinSlave | **Documented:**<br>Parent: LinCommunicationController<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LinSlaveConfig | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LinSlaveConfigIdent | **Documented:**<br>Parent: Referrable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LinSporadicFrame | **Documented:**<br>Parent: LinFrame<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Linker | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | List | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | LogAndTraceMessageCollectionSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MacMulticastConfiguration | **Documented:**<br>Parent: NetworkEndpointAddress<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MacSecCipherSuiteConfig | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MacSecCryptoAlgoConfig | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MacSecGlobalKayProps | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MacSecKayParticipant | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MacSecLocalKayProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MacSecParticipantSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MacSecProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MappingConstraint | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | McDataAccessDetails | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | McDataInstance | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | McFunction | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | McFunctionDataRefSet | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | McGroup | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | McGroupDataRefSet | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | McParameterElementGroup | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | McSupportData | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | McSwEmulationMethodSupport | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MeasuredExecutionTime | **Documented:**<br>Parent: ExecutionTime<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MeasuredHeapUsage | **Documented:**<br>Parent: HeapUsage<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MemorySectionLocation | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MetaDataItem | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MetaDataItemSet | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MixedContentForLongName | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | MixedContentForOverviewParagraph | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | MixedContentForParagraph | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | MixedContentForPlainText | **Documented:**<br>Parent: WhitespaceControlled<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | MixedContentForUnitNames | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | MixedContentForVerbatim | **Documented:**<br>Parent: WhitespaceControlled<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | MlFormula | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ModeDeclarationMapping | **Documented:**<br>Parent: AtpStructureElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ModeDeclarationMappingSet | **Documented:**<br>Parent: AtpType<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ModeErrorBehavior | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ModeInBswModuleDescriptionInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ModeInSwcInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ModeInterfaceMapping | **Documented:**<br>Parent: PortInterfaceMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ModePortAnnotation | **Documented:**<br>Parent: GeneralAnnotation<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ModeSwitchEventTriggeredActivity | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ModeSwitchInterface | **Documented:**<br>Parent: PortInterface<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ModeTransition | **Documented:**<br>Parent: AtpStructureElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MsrQueryArg | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MsrQueryChapter | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MsrQueryP1 | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MsrQueryP2 | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MsrQueryProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MsrQueryResultChapter | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MsrQueryResultTopic1 | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MsrQueryTopic1 | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MultiLanguageVerbatim | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MultidimensionalTime | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | MultiplicityRestrictionWithSeverity | **Documented:**<br>Parent: RestrictionWithSeverity<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | NetworkSegmentIdentification | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | NmCoordinator | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | NotAvailableValueSpecification | **Documented:**<br>Parent: ValueSpecification<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Note | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | NumericalOrText | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | NumericalRuleBasedValueSpecification | **Documented:**<br>Parent: AbstractRuleBasedValueSpecification<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | NumericalValueSpecification | **Documented:**<br>Parent: ValueSpecification<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | NumericalValueVariationPoint | **Documented:**<br>Parent: AbstractNumericalVariationPoint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | NvBlockDataMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | NvBlockDescriptor | **Documented:**<br>Parent: AtpStructureElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | NvBlockSwComponentType | **Documented:**<br>Parent: AtomicSwComponentType<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | NvDataInterface | **Documented:**<br>Parent: DataInterface<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | NvDataPortAnnotation | **Documented:**<br>Parent: GeneralAnnotation<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ObdControlServiceNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ObdInfoServiceNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ObdMonitorServiceNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ObdPidServiceNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ObdRatioDenominatorNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ObdRatioServiceNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | OffsetTimingConstraint | **Documented:**<br>Parent: TimingConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | OperationInSystemInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | OrderedMaster | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | OsTaskExecutionEvent | **Documented:**<br>Parent: RTEEvent<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | OsTaskProxy | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PModeInSystemInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PPortPrototype | **Documented:**<br>Parent: AbstractProvidedPortPrototype<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PRPortPrototype | **Documented:**<br>Parent: AbstractRequiredPortPrototype<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PTriggerInAtomicSwcTypeInstanceRef | **Documented:**<br>Parent: TriggerInAtomicSwcInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ParameterInterface | **Documented:**<br>Parent: DataInterface<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ParameterPortAnnotation | **Documented:**<br>Parent: GeneralAnnotation<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ParameterSwComponentType | **Documented:**<br>Parent: SwComponentType<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PassThroughSwConnector | **Documented:**<br>Parent: SwConnector<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PduActivationRoutingGroup | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PdurIPduGroup | **Documented:**<br>Parent: FibexElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PerInstanceMemorySize | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PeriodicEventTriggering | **Documented:**<br>Parent: EventTriggeringConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PermissibleSignalPath | **Documented:**<br>Parent: SignalPathConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PhysicalDimensionMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PhysicalDimensionMappingSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PlatformModuleEthernetEndpointConfiguration | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PlcaProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PncMapping | **Documented:**<br>Parent: Describable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PncMappingIdent | **Documented:**<br>Parent: Referrable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PortElementToCommunicationResourceMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PortGroup | **Documented:**<br>Parent: AtpStructureElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PortGroupInSystemInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PortInterface | **Documented:**<br>Parent: AtpType<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | PortInterfaceMapping | **Documented:**<br>Parent: AtpBlueprintable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | PortInterfaceMappingSet | **Documented:**<br>Parent: AtpBlueprintable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PortPrototype | **Documented:**<br>Parent: AtpPrototype<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | PositiveIntegerValueVariationPoint | **Documented:**<br>Parent: AttributeValueVariationPoint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PostBuildVariantCondition | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PostBuildVariantCriterion | **Documented:**<br>Parent: AtpDefinition<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PostBuildVariantCriterionValue | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PostBuildVariantCriterionValueSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PredefinedChapter | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PredefinedVariant | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PrimitiveAttributeCondition | **Documented:**<br>Parent: AttributeCondition<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PrimitiveAttributeTailoring | **Documented:**<br>Parent: AttributeTailoring<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | PrivacyLevel | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Prms | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RPortPrototype | **Documented:**<br>Parent: AbstractRequiredPortPrototype<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RTriggerInAtomicSwcInstanceRef | **Documented:**<br>Parent: TriggerInAtomicSwcInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RapidPrototypingScenario | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ReceiverAnnotation | **Documented:**<br>Parent: SenderReceiverAnnotation<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ReceptionComSpecProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RecordValueSpecification | **Documented:**<br>Parent: CompositeValueSpecification<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ReferenceCondition | **Documented:**<br>Parent: AttributeCondition<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ReferenceTailoring | **Documented:**<br>Parent: AttributeTailoring<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ReferenceValueSpecification | **Documented:**<br>Parent: ValueSpecification<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ResourceConsumption | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RestrictionWithSeverity | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | RoleBasedBswModuleEntryAssignment | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RoleBasedMcDataAssignment | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RoleBasedResourceDependency | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RootSwCompositionPrototype | **Documented:**<br>Parent: AtpPrototype<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RoughEstimateHeapUsage | **Documented:**<br>Parent: HeapUsage<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RoughEstimateOfExecutionTime | **Documented:**<br>Parent: ExecutionTime<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Row | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RptComponent | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RptContainer | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RptExecutableEntity | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RptExecutableEntityEvent | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RptExecutableEntityProperties | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RptExecutionContext | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RptHook | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RptImplPolicy | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RptProfile | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RptServicePoint | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RptSupportData | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RptSwPrototypingAccess | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RteEventInCompositionSeparation | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RteEventInCompositionToOsTaskProxyMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RteEventInSystemSeparation | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RteEventInSystemToOsTaskProxyMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RtePluginProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RtpTp | **Documented:**<br>Parent: TransportProtocolConfiguration<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RuleArguments | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RuleBasedAxisCont | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RuleBasedValueCont | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RuleBasedValueSpecification | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RunnableEntity | **Documented:**<br>Parent: ExecutableEntity<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RunnableEntityArgument | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RunnableEntityGroup | **Documented:**<br>Parent: AtpStructureElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RunnableEntityInCompositionInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | RuntimeError | **Documented:**<br>Parent: TracedFailure<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SOMEIPTransformationDescription | **Documented:**<br>Parent: TransformationDescription<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SOMEIPTransformationISignalProps | **Documented:**<br>Parent: TransformationISignalProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SOMEIPTransformationProps | **Documented:**<br>Parent: TransformationProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SaveConfigurationEntry | **Documented:**<br>Parent: LinConfigurationEntry<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ScaleConstr | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Sdf | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SdgAbstractForeignReference | **Documented:**<br>Parent: SdgElementWithGid<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | SdgAbstractPrimitiveAttribute | **Documented:**<br>Parent: SdgElementWithGid<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | SdgAggregationWithVariation | **Documented:**<br>Parent: SdgElementWithGid<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SdgAttribute | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | SdgClass | **Documented:**<br>Parent: SdgElementWithGid<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SdgContents | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SdgDef | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SdgElementWithGid | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | SdgForeignReference | **Documented:**<br>Parent: SdgAbstractForeignReference<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SdgForeignReferenceWithVariation | **Documented:**<br>Parent: SdgAbstractForeignReference<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SdgPrimitiveAttribute | **Documented:**<br>Parent: SdgAbstractPrimitiveAttribute<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SdgPrimitiveAttributeWithVariation | **Documented:**<br>Parent: SdgAbstractPrimitiveAttribute<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SdgReference | **Documented:**<br>Parent: SdgAttribute<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SdgTailoring | **Documented:**<br>Parent: RestrictionWithSeverity<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SectionNamePrefix | **Documented:**<br>Parent: ImplementationProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SecureOnBoardCommunicationNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SecurityEventAggregationFilter | **Documented:**<br>Parent: AbstractSecurityEventFilter<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SecurityEventContextData | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SecurityEventContextMapping | **Documented:**<br>Parent: IdsMapping<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | SecurityEventContextMappingApplication | **Documented:**<br>Parent: SecurityEventContextMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SecurityEventContextMappingBswModule | **Documented:**<br>Parent: SecurityEventContextMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SecurityEventContextMappingCommConnector | **Documented:**<br>Parent: SecurityEventContextMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SecurityEventContextMappingFunctionalCluster | **Documented:**<br>Parent: SecurityEventContextMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SecurityEventContextProps | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SecurityEventDefinition | **Documented:**<br>Parent: IdsCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SecurityEventFilterChain | **Documented:**<br>Parent: IdsCommonElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SecurityEventOneEveryNFilter | **Documented:**<br>Parent: AbstractSecurityEventFilter<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SecurityEventStateFilter | **Documented:**<br>Parent: AbstractSecurityEventFilter<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SecurityEventThresholdFilter | **Documented:**<br>Parent: AbstractSecurityEventFilter<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SenderAnnotation | **Documented:**<br>Parent: SenderReceiverAnnotation<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SenderReceiverAnnotation | **Documented:**<br>Parent: GeneralAnnotation<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | SenderReceiverCompositeElementToSignalMapping | **Documented:**<br>Parent: DataMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SenderReceiverInterface | **Documented:**<br>Parent: DataInterface<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SensorActuatorSwComponentType | **Documented:**<br>Parent: AtomicSwComponentType<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SeparateSignalPath | **Documented:**<br>Parent: SignalPathConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ServiceInstanceCollectionSet | **Documented:**<br>Parent: FibexElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ServiceProxySwComponentType | **Documented:**<br>Parent: AtomicSwComponentType<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ServiceSwComponentType | **Documented:**<br>Parent: AtomicSwComponentType<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ShortNameFragment | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SignalPathConstraint | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | SignalServiceTranslationElementProps | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SignalServiceTranslationEventProps | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SignalServiceTranslationProps | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SignalServiceTranslationPropsSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SimulatedExecutionTime | **Documented:**<br>Parent: ExecutionTime<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SingleLanguageLongName | **Documented:**<br>Parent: MixedContentForLongName<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SingleLanguageReferrable | **Documented:**<br>Parent: Referrable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | SlOverviewParagraph | **Documented:**<br>Parent: MixedContentForOverviewParagraph<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SlParagraph | **Documented:**<br>Parent: MixedContentForParagraph<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SoConIPduIdentifier | **Documented:**<br>Parent: Referrable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SocketConnectionIpduIdentifierSet | **Documented:**<br>Parent: FibexElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SomeipSdClientEventGroupTimingConfig | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SomeipSdClientServiceInstanceConfig | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SomeipSdServerEventGroupTimingConfig | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SomeipSdServerServiceInstanceConfig | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SomeipServiceVersion | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SomeipTpChannel | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SomeipTpConfig | **Documented:**<br>Parent: TpConfig<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SomeipTpConnection | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SpecElementReference | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | SpecElementScope | **Documented:**<br>Parent: SpecElementReference<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | SpecificationDocumentScope | **Documented:**<br>Parent: SpecElementReference<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SpecificationScope | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SporadicEventTriggering | **Documented:**<br>Parent: EventTriggeringConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | StateDependentFirewall | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | StaticSocketConnection | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Std | **Documented:**<br>Parent: SingleLanguageReferrable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | StreamFilterIEEE1722Tp | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | StreamFilterIpv4Address | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | StreamFilterIpv6Address | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | StreamFilterMACAddress | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | StreamFilterPortRange | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | StreamFilterRuleDataLinkLayer | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | StreamFilterRuleIpTp | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | StructuredReq | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SubElementMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SubElementRef | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | SupervisedEntityCheckpointNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SupervisedEntityNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwAxisCont | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwAxisType | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwBitRepresentation | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwCalprmRefProxy | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwComponentPrototype | **Documented:**<br>Parent: AtpPrototype<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwComponentPrototypeAssignment | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwConnector | **Documented:**<br>Parent: AtpStructureElement<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | SwDataDependency | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwDataDependencyArgs | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwGenericAxisParamType | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwSystemconstDependentFormula | **Documented:**<br>Parent: FormulaExpression<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | SwSystemconstValue | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwSystemconstantValueSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwVariableRefProxy | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwcBswSynchronizedModeGroupPrototype | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwcBswSynchronizedTrigger | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwcExclusiveAreaPolicy | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwcInternalBehavior | **Documented:**<br>Parent: InternalBehavior<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwcModeManagerErrorEvent | **Documented:**<br>Parent: RTEEvent<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwcServiceDependencyInSystemInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwcSupportedFeature | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | SwcToApplicationPartitionMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwcToEcuMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwcToSwcOperationArguments | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwcToSwcSignal | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwitchAsynchronousTrafficShaperGroupEntry | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwitchFlowMeteringEntry | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwitchStreamFilterActionDestPortModification | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwitchStreamFilterEntry | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwitchStreamFilterRule | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwitchStreamGateEntry | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SwitchStreamIdentification | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SymbolProps | **Documented:**<br>Parent: ImplementationProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SymbolicNameProps | **Documented:**<br>Parent: ImplementationProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SyncTimeBaseMgrUserNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SynchronizationPointConstraint | **Documented:**<br>Parent: TimingConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SynchronizationTimingConstraint | **Documented:**<br>Parent: TimingConstraint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SynchronousServerCallPoint | **Documented:**<br>Parent: ServerCallPoint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | System | **Documented:**<br>Parent: AtpStructureElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SystemMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SystemSignalGroupToCommunicationResourceMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SystemSignalToCommunicationResourceMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | SystemTiming | **Documented:**<br>Parent: TimingExtension<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDCpSoftwareClusterMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDCpSoftwareClusterMappingSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDCpSoftwareClusterResourceMapping | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventBsw | **Documented:**<br>Parent: TimingDescriptionEvent<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TDEventBswInternalBehavior | **Documented:**<br>Parent: TimingDescriptionEvent<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventBswModeDeclaration | **Documented:**<br>Parent: TDEventBsw<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventBswModule | **Documented:**<br>Parent: TDEventBsw<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventCom | **Documented:**<br>Parent: TimingDescriptionEvent<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TDEventComplex | **Documented:**<br>Parent: TimingDescriptionEvent<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventCycleStart | **Documented:**<br>Parent: TDEventCom<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TDEventFrClusterCycleStart | **Documented:**<br>Parent: TDEventCycleStart<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventFrame | **Documented:**<br>Parent: TDEventCom<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventFrameEthernet | **Documented:**<br>Parent: TDEventCom<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventIPdu | **Documented:**<br>Parent: TDEventCom<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventISignal | **Documented:**<br>Parent: TDEventCom<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventModeDeclaration | **Documented:**<br>Parent: TDEventVfbPort<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventOccurrenceExpression | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventOccurrenceExpressionFormula | **Documented:**<br>Parent: FormulaExpression<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventOperation | **Documented:**<br>Parent: TDEventVfbPort<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventSLLET | **Documented:**<br>Parent: TimingDescriptionEvent<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TDEventSLLETPort | **Documented:**<br>Parent: TDEventSLLET<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventSwc | **Documented:**<br>Parent: TimingDescriptionEvent<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TDEventSwcInternalBehavior | **Documented:**<br>Parent: TDEventSwc<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventSwcInternalBehaviorReference | **Documented:**<br>Parent: TDEventSwc<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventTTCanCycleStart | **Documented:**<br>Parent: TDEventCycleStart<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventTrigger | **Documented:**<br>Parent: TDEventVfbPort<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventVariableDataPrototype | **Documented:**<br>Parent: TDEventVfbPort<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDEventVfb | **Documented:**<br>Parent: TimingDescriptionEvent<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TDEventVfbPort | **Documented:**<br>Parent: TDEventVfb<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TDEventVfbReference | **Documented:**<br>Parent: TDEventVfb<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDHeaderIdRange | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TDLETZoneClock | **Documented:**<br>Parent: TimingClock<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Table | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TagWithOptionalValue | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Tbody | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TcpIpIcmpv4Props | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TcpIpIcmpv6Props | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TcpOptionFilterList | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TcpOptionFilterSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TcpProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TextTableMapping | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TextTableValuePair | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TextValueSpecification | **Documented:**<br>Parent: ValueSpecification<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TextualCondition | **Documented:**<br>Parent: AbstractCondition<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Tgroup | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TimeValueValueVariationPoint | **Documented:**<br>Parent: AttributeValueVariationPoint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TimingClock | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TimingClockSyncAccuracy | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TimingCondition | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TimingConditionFormula | **Documented:**<br>Parent: FormulaExpression<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TimingDescription | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TimingDescriptionEvent | **Documented:**<br>Parent: TimingDescription<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TimingDescriptionEventChain | **Documented:**<br>Parent: TimingDescription<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TimingExtensionResource | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TimingModeInstance | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TlsCryptoCipherSuite | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TlsCryptoCipherSuiteProps | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TlsPskIdentity | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TlvDataIdDefinition | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TlvDataIdDefinitionSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Topic1 | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TopicContent | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TopicContentOrMsrQuery | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TopicOrMsrQuery | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Traceable | **Documented:**<br>Parent: MultilanguageReferrable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TraceableText | **Documented:**<br>Parent: Paginateable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TracedFailure | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TransformationDescription | **Documented:**<br>Parent: Describable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TransformationISignalProps | **Documented:**<br>Parent: Describable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TransformationProps | **Documented:**<br>Parent: Identifiable<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TransformationPropsSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TransformationTechnology | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TransformerHardErrorEvent | **Documented:**<br>Parent: RTEEvent<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TransientFault | **Documented:**<br>Parent: TracedFailure<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TransmissionComSpecProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TriggerIPduSendCondition | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TriggerInAtomicSwcInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | TriggerInSystemInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TriggerInterface | **Documented:**<br>Parent: PortInterface<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TriggerInterfaceMapping | **Documented:**<br>Parent: PortInterfaceMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TriggerPortAnnotation | **Documented:**<br>Parent: GeneralAnnotation<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TriggerToSignalMapping | **Documented:**<br>Parent: DataMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Tt | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TtcanAbsolutelyScheduledTiming | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TtcanCluster | **Documented:**<br>Parent: AbstractCanCluster<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TtcanCommunicationConnector | **Documented:**<br>Parent: AbstractCanCommunicationConnector<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TtcanCommunicationController | **Documented:**<br>Parent: AbstractCanCommunicationController<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | TtcanPhysicalChannel | **Documented:**<br>Parent: AbstractCanPhysicalChannel<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | UdpProps | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | UnassignFrameId | **Documented:**<br>Parent: LinConfigurationEntry<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | UnlimitedIntegerValueVariationPoint | **Documented:**<br>Parent: AttributeValueVariationPoint<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | UnresolvedReferenceRestrictionWithSeverity | **Documented:**<br>Parent: RestrictionWithSeverity<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | UserDefinedCluster | **Documented:**<br>Parent: CommunicationCluster<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | UserDefinedCommunicationConnector | **Documented:**<br>Parent: CommunicationConnector<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | UserDefinedCommunicationController | **Documented:**<br>Parent: CommunicationController<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | UserDefinedEthernetFrame | **Documented:**<br>Parent: AbstractEthernetFrame<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | UserDefinedGlobalTimeMaster | **Documented:**<br>Parent: GlobalTimeMaster<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | UserDefinedGlobalTimeSlave | **Documented:**<br>Parent: GlobalTimeSlave<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | UserDefinedPhysicalChannel | **Documented:**<br>Parent: PhysicalChannel<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | UserDefinedTransformationDescription | **Documented:**<br>Parent: TransformationDescription<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | UserDefinedTransformationISignalProps | **Documented:**<br>Parent: TransformationISignalProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | UserDefinedTransformationProps | **Documented:**<br>Parent: TransformationProps<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | V2xDataManagerNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | V2xFacUserNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | V2xMUserNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ValueGroup | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ValueRestrictionWithSeverity | **Documented:**<br>Parent: RestrictionWithSeverity<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ValueSpecification | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | VariableAndParameterInterfaceMapping | **Documented:**<br>Parent: PortInterfaceMapping<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | VariableDataPrototypeInCompositionInstanceRef | **Documented:**<br>Parent: AtpInstanceRef<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | VariationPoint | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | VariationPointProxy | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | VariationRestrictionWithSeverity | **Documented:**<br>Parent: RestrictionWithSeverity<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | VendorSpecificServiceNeeds | **Documented:**<br>Parent: ServiceNeeds<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | VfbTiming | **Documented:**<br>Parent: TimingExtension<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ViewMap | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | ViewMapSet | **Documented:**<br>Parent: ARElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | WaitPoint | **Documented:**<br>Parent: Identifiable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | WarningIndicatorRequestedBitNeeds | **Documented:**<br>Parent: DiagnosticCapabilityElement<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | WhitespaceControlled | **Documented:**<br>Parent: ARObject<br>Type: Abstract | Class not found in source code |
| ✗ MISSING | WorstCaseHeapUsage | **Documented:**<br>Parent: HeapUsage<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Xdoc | **Documented:**<br>Parent: SingleLanguageReferrable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Xfile | **Documented:**<br>Parent: SingleLanguageReferrable<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | Xref | **Documented:**<br>Parent: ARObject<br>Type: Concrete | Class not found in source code |
| ✗ MISSING | XrefTarget | **Documented:**<br>Parent: SingleLanguageReferrable<br>Type: Concrete | Class not found in source code |

## Extra Classes (Not Documented)

| Status | Class | Hierarchy | Notes |
|--------|-------|-----------|-------|
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ARBoolean | **Actual:**<br>Parent: ARType<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.AREnum | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ARFloat | **Actual:**<br>Parent: ARNumerical<br>Type: Concrete | Class exists but not documented |
| + EXTRA | MSR.Documentation.TextModel.BlockElements.ListElements.ARList | **Actual:**<br>Parent: Paginateable<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ARLiteral | **Actual:**<br>Parent: ARType<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ARNumerical | **Actual:**<br>Parent: ARType<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ARPositiveInteger | **Actual:**<br>Parent: ARNumerical<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ARType | **Actual:**<br>Parent: None<br>Type: Abstract | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.AutosarTopLevelStructure.AUTOSARDoc | **Actual:**<br>Parent: AbstractAUTOSAR<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.AutosarTopLevelStructure.AbstractAUTOSAR | **Actual:**<br>Parent: CollectableElement<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ArgumentDirectionEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations.AutoCollectEnum | **Actual:**<br>Parent: None<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.Boolean | **Actual:**<br>Parent: ARBoolean<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.BswModuleTemplate.BswBehavior.BswApiOptions | **Actual:**<br>Parent: ARObject<br>Type: Abstract | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.BswModuleTemplate.BswInterfaces.BswCallType | **Actual:**<br>Parent: str<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.BswModuleTemplate.BswBehavior.BswDataReceptionPolicy | **Actual:**<br>Parent: BswApiOptions<br>Type: Abstract | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.BswModuleTemplate.BswInterfaces.BswEntryKindEnum | **Actual:**<br>Parent: str<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.BswModuleTemplate.BswInterfaces.BswExecutionContext | **Actual:**<br>Parent: str<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.BswModuleTemplate.BswBehavior.BswInterruptCategory | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.BswModuleTemplate.BswBehavior.BswQueuedDataReceptionPolicy | **Actual:**<br>Parent: BswDataReceptionPolicy<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ByteOrderEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.CIdentifier | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.CategoryString | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.CommunicationDirectionType | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.CycleRepetitionType | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.CommonStructure.Filter.DataFilterTypeEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.DateTime | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.DiagRequirementIdString | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.CommonStructure.ServiceNeeds.DiagnosticAudienceEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.CommonStructure.ServiceNeeds.DiagnosticClearDtcNotificationEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.CommonStructure.ServiceNeeds.DiagnosticProcessingStyleEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.CommonStructure.ServiceNeeds.DiagnosticRoutineTypeEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.CommonStructure.ServiceNeeds.DiagnosticServiceRequestCallbackTypeEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.CommonStructure.ServiceNeeds.DiagnosticValueAccessEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.CommonStructure.ServiceNeeds.DtcFormatTypeEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.CommonStructure.ServiceNeeds.DtcKindEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.ECUCParameterDefTemplate.EcucConfigurationClassEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.ECUCParameterDefTemplate.EcucConfigurationVariantEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.ECUCParameterDefTemplate.EcucDestinationUriDefRefType | **Actual:**<br>Parent: RefType<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.ECUCParameterDefTemplate.EcucScopeEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.ECUCParameterDefTemplate.EcucSymbolicNameReferenceDef | **Actual:**<br>Parent: EcucAbstractInternalReferenceDef<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.FlexrayChannelName | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.Float | **Actual:**<br>Parent: ARFloat<br>Type: Concrete | Class exists but not documented |
| + EXTRA | MSR.Documentation.BlockElements.Figure.GraphicFitEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.SWComponentTemplate.Communication.HandleInvalidEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.IPduSignalProcessingEnum | **Actual:**<br>Parent: None<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.Identifier | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.Integer | **Actual:**<br>Parent: ARNumerical<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.Ip4AddressString | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.Ip6AddressString | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |
| + EXTRA | MSR.Documentation.TextModel.LanguageDataModel.LEnum | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.Limit | **Actual:**<br>Parent: ARObject<br>Type: Concrete | Class exists but not documented |
| + EXTRA | MSR.Documentation.TextModel.BlockElements.ListElements.ListEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.MacAddressString | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.CommonStructure.ModeDeclaration.ModeActivationKind | **Actual:**<br>Parent: str<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.NameToken | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.CommonStructure.ServiceNeeds.NvBlockNeedsReliabilityEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.CommonStructure.ServiceNeeds.NvBlockNeedsWritingPriorityEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.PduToFrameMapping | **Actual:**<br>Parent: Identifiable<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.PncGatewayTypeEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.PositiveInteger | **Actual:**<br>Parent: ARPositiveInteger<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.PositiveUnlimitedInteger | **Actual:**<br>Parent: ARPositiveInteger<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.CommonStructure.ServiceNeeds.RamBlockStatusControlEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.CommonStructure.InternalBehavior.ReentrancyLevelEnum | **Actual:**<br>Parent: None<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.RefType | **Actual:**<br>Parent: ARObject<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ReferrableSubtypesEnum | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.RegularExpression | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.ResumePosition | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.RevisionLabelString | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.SdClientConfig | **Actual:**<br>Parent: ARObject<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.SdServerConfig | **Actual:**<br>Parent: ARObject<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.CommonStructure.ServiceNeeds.ServiceDiagnosticRelevanceEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication.SocketConnectionBundle | **Actual:**<br>Parent: Referrable<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication.SocketConnectionIpduIdentifier | **Actual:**<br>Parent: ARObject<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.String | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |
| + EXTRA | MSR.DataDictionary.DataDefProperties.SwDataDefPropsConditional | **Actual:**<br>Parent: ARObject<br>Type: Concrete | Class exists but not documented |
| + EXTRA | MSR.DataDictionary.DataDefProperties.SwImplPolicyEnum | **Actual:**<br>Parent: AREnum<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.BswModuleTemplate.BswInterfaces.SwServiceImplPolicyEnum | **Actual:**<br>Parent: str<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.TRefType | **Actual:**<br>Parent: RefType<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.TimeValue | **Actual:**<br>Parent: ARFloat<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.UnlimitedInteger | **Actual:**<br>Parent: Integer<br>Type: Concrete | Class exists but not documented |
| + EXTRA | AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.VerbatimString | **Actual:**<br>Parent: ARLiteral<br>Type: Concrete | Class exists but not documented |

## Legend

- ✓ MATCH: Class has correct parent and abstract status
- ✗ MISSING: Class documented but not found in source
- ⚠ MISMATCH: Class has wrong parent or abstract status
- + EXTRA: Class exists but not documented
