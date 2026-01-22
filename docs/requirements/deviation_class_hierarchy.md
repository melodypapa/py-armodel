# Class Hierarchy Deviation Report

This report shows deviations between the documented AUTOSAR M2 class hierarchy
and the actual Python implementation class hierarchy.

## Summary

- ✓ **Match**: 402 classes with correct hierarchy
- ✗ **Missing**: 892 classes documented but not found
- ⚠ **Hierarchy Mismatch**: 228 classes with wrong parent/abstract
- + **Extra**: 89 undocumented classes
- **Total Documented Classes**: 1522
- **Total Deviations**: 1209

## Hierarchy Deviations Table

| Status | Class | Documented (Parent, Abstract) | Actual (Parent, Abstract) | Notes |
|--------|-------|-------------------------------|---------------------------|-------|
| ✗ MISSING | <<atpPrototype>> PduToFrameMapping | Identifiable, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ARElement | PackageableElement, True | PackageableElement, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | ARObject | None, True | None, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | ARPackage | CollectableElement, False | Identifiable, False | parent mismatch (expected CollectableElement, got Identifiable) |
| ⚠ MISMATCH | AUTOSAR | ARObject, False | AbstractAUTOSAR, False | parent mismatch (expected ARObject, got AbstractAUTOSAR) |
| ⚠ MISMATCH | AbstractAccessPoint | AtpStructureElement, True | Identifiable, False | parent mismatch (expected AtpStructureElement, got Identifiable), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AbstractCanCluster | CommunicationCluster, True | CommunicationCluster, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AbstractCanCommunicationConnector | CommunicationConnector, True | CommunicationConnector, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AbstractCanCommunicationController | CommunicationController, True | CommunicationController, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AbstractCanCommunicationControllerAttributes | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AbstractCanPhysicalChannel | PhysicalChannel, True | PhysicalChannel, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AbstractDoIpLogicAddressProps | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | AbstractEnumerationValueVariationPoint | AttributeValueVariationPoint, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | AbstractEthernetFrame | Frame, True | Frame, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AbstractEvent | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | AbstractGlobalTimeDomainProps | ARObject, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | AbstractImplementationDataType | AutosarDataType, True | AutosarDataType, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AbstractImplementationDataTypeElement | AtpStructureElement, True | Identifiable, False | parent mismatch (expected AtpStructureElement, got Identifiable), abstract mismatch (expected True, got False) |
| ✗ MISSING | AbstractMultiplicityRestriction | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AbstractNumericalVariationPoint | AttributeValueVariationPoint, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | AbstractProvidedPortPrototype | AtpPrototype, True | PortPrototype, False | parent mismatch (expected AtpPrototype, got PortPrototype), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AbstractRequiredPortPrototype | AtpPrototype, True | PortPrototype, False | parent mismatch (expected AtpPrototype, got PortPrototype), abstract mismatch (expected True, got False) |
| ✗ MISSING | AbstractRuleBasedValueSpecification | ValueSpecification, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | AbstractServiceInstance | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | AbstractValueRestriction | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AbstractVariationRestriction | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AccessCount | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AccessCountSet | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AclObjectSet | AtpBlueprintable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AclOperation | AtpBlueprintable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AclPermission | AtpBlueprintable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AclRole | AtpBlueprintable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AgeConstraint | TimingConstraint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AliasNameAssignment | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AliasNameSet | AtpBlueprintable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AnalyzedExecutionTime | ExecutionTime, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | AnyInstanceRef | AtpInstanceRef, False | ARObject, False | parent mismatch (expected AtpInstanceRef, got ARObject) |
| ⚠ MISMATCH | ApplicationCompositeDataType | ApplicationDataType, True | ApplicationDataType, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | ApplicationCompositeDataTypeSubElementRef | SubElementRef, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ApplicationCompositeElementDataPrototype | DataPrototype, True | DataPrototype, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | ApplicationDataType | AutosarDataType, True | AutosarDataType, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | ApplicationPartition | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ApplicationRuleBasedValueSpecification | CompositeRuleBasedValueArgument, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ApplicationValueSpecification | ValueSpecification, False | CompositeRuleBasedValueArgument, False | parent mismatch (expected ValueSpecification, got CompositeRuleBasedValueArgument) |
| ✗ MISSING | ArParameterInImplementationDataInstanceRef | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ArVariableInImplementationDataInstanceRef | ARObject, False | AtpInstanceRef, False | parent mismatch (expected ARObject, got AtpInstanceRef) |
| ✗ MISSING | ArbitraryEventTriggering | EventTriggeringConstraint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Area | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ArrayValueSpecification | CompositeValueSpecification, False | ValueSpecification, False | parent mismatch (expected CompositeValueSpecification, got ValueSpecification) |
| ⚠ MISMATCH | AssemblySwConnector | AtpStructureElement, False | SwConnector, False | parent mismatch (expected AtpStructureElement, got SwConnector) |
| ✗ MISSING | AssignFrameId | LinConfigurationEntry, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AssignFrameIdRange | LinConfigurationEntry, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AssignNad | LinConfigurationEntry, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | AsynchronousServerCallPoint | AbstractAccessPoint, False | ServerCallPoint, False | parent mismatch (expected AbstractAccessPoint, got ServerCallPoint) |
| ⚠ MISMATCH | AsynchronousServerCallReturnsEvent | AtpStructureElement, False | RTEEvent, False | parent mismatch (expected AtpStructureElement, got RTEEvent) |
| ⚠ MISMATCH | AtomicSwComponentType | AtpType, True | SwComponentType, False | parent mismatch (expected AtpType, got SwComponentType), abstract mismatch (expected True, got False) |
| ✗ MISSING | AtpBlueprint | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AtpBlueprintable | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AtpClassifier | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AtpDefinition | Referrable, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | AtpFeature | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AtpInstanceRef | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AtpPrototype | AtpFeature, True | AtpFeature, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AtpStructureElement | AtpFeature, True | AtpFeature, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AtpType | AtpClassifier, True | ARElement, False | parent mismatch (expected AtpClassifier, got ARElement), abstract mismatch (expected True, got False) |
| ✗ MISSING | AttributeValueVariationPoint | SwSystemconstDependentFormula, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | AutosarDataPrototype | DataPrototype, True | DataPrototype, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AutosarDataType | AtpType, True | AtpType, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | AutosarOperationArgumentInstance | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AutosarVariableInstance | Identifiable, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | BackgroundEvent | AtpStructureElement, False | RTEEvent, False | parent mismatch (expected AtpStructureElement, got RTEEvent) |
| ⚠ MISMATCH | BaseType | ARElement, True | ARElement, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | BaseTypeDefinition | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | BinaryManifestAddressableObject | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BinaryManifestItem | BinaryManifestAddressableObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BinaryManifestItemDefinition | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BinaryManifestItemNumericalValue | BinaryManifestItemValue, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BinaryManifestItemPointerValue | BinaryManifestItemValue, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BinaryManifestItemValue | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BinaryManifestMetaDataField | BinaryManifestAddressableObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BinaryManifestProvideResource | BinaryManifestResource, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BinaryManifestRequireResource | BinaryManifestResource, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BinaryManifestResource | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BinaryManifestResourceDefinition | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BlueprintGenerator | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BlueprintMappingSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BooleanValueVariationPoint | AttributeValueVariationPoint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Br | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BswAsynchronousServerCallReturnsEvent | BswScheduleEvent, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BswCompositionTiming | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BswEntryRelationship | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BswEntryRelationshipSet | AtpBlueprintable, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | BswEvent | AbstractEvent, True | AbstractEvent, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | BswInterruptEvent | BswEvent, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BswMgrNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BswModeManagerErrorEvent | BswScheduleEvent, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BswModeReceiverPolicy | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | BswModuleCallPoint | Referrable, True | Referrable, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | BswModuleDescription | AtpStructureElement, False | ARElement, False | parent mismatch (expected AtpStructureElement, got ARElement) |
| ⚠ MISMATCH | BswModuleEntity | ExecutableEntity, True | ExecutableEntity, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | BswModuleEntry | AtpBlueprintable, False | ARElement, False | parent mismatch (expected AtpBlueprintable, got ARElement) |
| ✗ MISSING | BswModuleTiming | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | BswScheduleEvent | BswEvent, True | BswEvent, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | BswSchedulerNamePrefix | ImplementationProps, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BswServiceDependency | ServiceDependency, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BswServiceDependencyIdent | IdentCaption, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BswTriggerDirectImplementation | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BuildAction | BuildActionEntity, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BuildActionEntity | AtpBlueprintable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BuildActionEnvironment | AtpBlueprintable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BuildActionInvocator | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BuildActionIoElement | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BuildActionManifest | AtpBlueprintable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BuildEngineeringObject | EngineeringObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BulkNvDataDescriptor | AtpStructureElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BurstPatternEventTriggering | EventTriggeringConstraint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BusMirrorCanIdRangeMapping | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BusMirrorCanIdToCanIdMapping | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BusMirrorChannel | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BusMirrorChannelMapping | FibexElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BusMirrorChannelMappingCan | BusMirrorChannelMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BusMirrorChannelMappingFlexray | BusMirrorChannelMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BusMirrorChannelMappingIp | BusMirrorChannelMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BusMirrorChannelMappingUserDefined | BusMirrorChannelMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BusMirrorLinPidToCanIdMapping | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | BusspecificNmEcu | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | CalibrationParameterValue | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CalibrationParameterValueSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CanControllerConfiguration | AbstractCanCommunicationControllerAttributes, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CanGlobalTimeDomainProps | AbstractGlobalTimeDomainProps, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | CanTpConfig | FibexElement, False | TpConfig, False | parent mismatch (expected FibexElement, got TpConfig) |
| ✗ MISSING | CanXlFrameTriggeringProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Caption | MultilanguageReferrable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Chapter | Paginateable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ChapterContent | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ChapterModel | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ChapterOrMsrQuery | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ClientIdDefinition | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ClientIdDefinitionSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ClientIdRange | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ClientServerAnnotation | GeneralAnnotation, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ClientServerInterface | AtpType, False | PortInterface, False | parent mismatch (expected AtpType, got PortInterface) |
| ⚠ MISMATCH | ClientServerOperation | AtpStructureElement, False | AtpFeature, False | parent mismatch (expected AtpStructureElement, got AtpFeature) |
| ✗ MISSING | ClientServerOperationComProps | CpSoftwareClusterCommunicationResourceProps, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ClientServerToSignalMapping | DataMapping, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | CollectableElement | Identifiable, True | ARObject, False | parent mismatch (expected Identifiable, got ARObject), abstract mismatch (expected True, got False) |
| ✗ MISSING | Colspec | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ComMgrUserNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | CommConnectorPort | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | CommonSignalPath | SignalPathConstraint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CommunicationBufferLocking | SwcSupportedFeature, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | CommunicationCluster | FibexElement, True | FibexElement, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | CommunicationConnector | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | CommunicationController | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | CommunicationControllerMapping | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | CommunicationCycle | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | ComponentClustering | MappingConstraint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ComponentInCompositionInstanceRef | AtpInstanceRef, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ComponentSeparation | MappingConstraint, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | CompositeRuleBasedValueArgument | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | CompositeRuleBasedValueSpecification | AbstractRuleBasedValueSpecification, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | CompositeValueSpecification | ValueSpecification, True | ValueSpecification, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | CompositionSwComponentType | AtpType, False | SwComponentType, False | parent mismatch (expected AtpType, got SwComponentType) |
| ⚠ MISMATCH | CompuConstContent | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | CompuContent | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | CompuGenericMath | FormulaExpression, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | CompuMethod | AtpBlueprintable, False | ARElement, False | parent mismatch (expected AtpBlueprintable, got ARElement) |
| ⚠ MISMATCH | CompuScale | ARObject, False | Compu, False | parent mismatch (expected ARObject, got Compu) |
| ⚠ MISMATCH | CompuScaleContents | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | ConcretePatternEventTriggering | EventTriggeringConstraint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ConditionByFormula | SwSystemconstDependentFormula, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ConditionalChangeNad | LinConfigurationEntry, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ConfidenceInterval | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ConsistencyNeeds | AtpBlueprintable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ConstantSpecificationMapping | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ConstantSpecificationMappingSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ConsumedProvidedServiceInstanceGroup | FibexElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ContainerIPdu | IPdu, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CouplingElement | FibexElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CouplingElementAbstractDetails | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CouplingElementSwitchDetails | CouplingElementAbstractDetails, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CouplingPortAsynchronousTrafficShaper | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CouplingPortConnection | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CouplingPortCreditBasedShaper | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CouplingPortRatePolicy | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CouplingPortShaper | CouplingPortStructuralElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | CouplingPortStructuralElement | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | CouplingPortTrafficClassAssignment | Referrable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSoftwareCluster | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterBinaryManifestDescriptor | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterCommunicationResource | CpSoftwareClusterResource, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterCommunicationResourceProps | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterMappingSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterResource | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterResourcePool | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterResourceToApplicationPartitionMapping | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterServiceResource | CpSoftwareClusterResource, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterToApplicationPartitionMapping | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterToEcuInstanceMapping | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterToResourceMapping | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSwClusterResourceToDiagDataElemMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSwClusterResourceToDiagFunctionIdMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSwClusterToDiagEventMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSwClusterToDiagRoutineSubfunctionMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CryptoEllipticCurveProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CryptoKeyManagementNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CryptoServiceCertificate | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CryptoServiceJobNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CryptoServiceKey | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | CryptoServiceMapping | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | CryptoServicePrimitive | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CryptoServiceQueue | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CryptoSignatureScheme | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DataComProps | CpSoftwareClusterCommunicationResourceProps, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | DataConstr | AtpBlueprintable, False | Identifiable, False | parent mismatch (expected AtpBlueprintable, got Identifiable) |
| ✗ MISSING | DataDumpEntry | LinConfigurationEntry, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | DataInterface | AtpType, True | PortInterface, False | parent mismatch (expected AtpType, got PortInterface), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | DataMapping | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | DataPrototype | AtpPrototype, True | AtpPrototype, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | DataPrototypeGroup | AtpStructureElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DataPrototypeInClientServerInterfaceInstanceRef | DataPrototypeInPortInterfaceInstanceRef, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DataPrototypeInPortInterfaceInstanceRef | AtpInstanceRef, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DataPrototypeInPortInterfaceRef | DataPrototypeReference, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DataPrototypeInSenderReceiverInterfaceInstanceRef | DataPrototypeInPortInterfaceInstanceRef, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DataPrototypeInSystemInstanceRef | AtpInstanceRef, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DataPrototypeReference | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DataPrototypeTransformationProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | DataReceiveErrorEvent | AtpStructureElement, False | RTEEvent, False | parent mismatch (expected AtpStructureElement, got RTEEvent) |
| ⚠ MISMATCH | DataReceivedEvent | AtpStructureElement, False | RTEEvent, False | parent mismatch (expected AtpStructureElement, got RTEEvent) |
| ⚠ MISMATCH | DataSendCompletedEvent | AtpStructureElement, False | RTEEvent, False | parent mismatch (expected AtpStructureElement, got RTEEvent) |
| ⚠ MISMATCH | DataTypeMappingSet | AtpBlueprintable, False | ARElement, False | parent mismatch (expected AtpBlueprintable, got ARElement) |
| ⚠ MISMATCH | DataWriteCompletedEvent | AtpStructureElement, False | RTEEvent, False | parent mismatch (expected AtpStructureElement, got RTEEvent) |
| ✗ MISSING | DdsCpConfig | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsCpConsumedServiceInstance | DdsCpServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsCpDomain | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsCpISignalToDdsTopicMapping | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsCpPartition | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsCpProvidedServiceInstance | DdsCpServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsCpQosProfile | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsCpServiceInstance | AbstractServiceInstance, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsCpServiceInstanceEvent | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsCpServiceInstanceOperation | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsCpTopic | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsDeadline | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsDestinationOrder | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsDurability | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsDurabilityService | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsHistory | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsLatencyBudget | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsLifespan | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsLiveliness | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsOwnership | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsOwnershipStrength | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsReliability | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsResourceLimits | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsTopicData | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DdsTransportPriority | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DefItem | Paginateable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DefList | Paginateable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DelegatedPortAnnotation | GeneralAnnotation, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | DelegationSwConnector | AtpStructureElement, False | SwConnector, False | parent mismatch (expected AtpStructureElement, got SwConnector) |
| ⚠ MISMATCH | Describable | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | DevelopmentError | TracedFailure, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DhcpServerConfiguration | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Dhcpv6Props | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | DiagEventDebounceAlgorithm | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | DiagnosticAbstractAliasEvent | DiagnosticCommonElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAbstractDataIdentifier | DiagnosticCommonElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAbstractParameter | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAccessPermission | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAging | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAuthRole | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAuthRoleProxy | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAuthTransmitCertificate | DiagnosticAuthentication, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAuthTransmitCertificateEvaluation | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAuthTransmitCertificateMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAuthentication | DiagnosticServiceInstance, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAuthenticationClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAuthenticationConfiguration | DiagnosticAuthentication, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | DiagnosticCapabilityElement | ServiceNeeds, True | ServiceNeeds, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | DiagnosticClearDiagnosticInformation | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticClearDiagnosticInformationClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticClearResetEmissionRelatedInfo | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticClearResetEmissionRelatedInfoClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticComControl | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticComControlClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticComControlSpecificChannel | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticComControlSubNodeChannel | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticCommonElement | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticCommonProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticComponentNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticCondition | DiagnosticCommonElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticConditionGroup | DiagnosticCommonElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticConnectedIndicator | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticContributionSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticControlDTCSetting | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticControlDTCSettingClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticControlEnableMaskBit | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticControlNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticCustomServiceClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticCustomServiceInstance | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDataByIdentifier | DiagnosticServiceInstance, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDataElement | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDataIdentifier | DiagnosticAbstractDataIdentifier, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDataIdentifierSet | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDataTransfer | DiagnosticMemoryByAddress, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDataTransferClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDeAuthentication | DiagnosticAuthentication, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDebounceAlgorithmProps | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDemProvidedDataMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDynamicDataIdentifier | DiagnosticAbstractDataIdentifier, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDynamicallyDefineDataIdentifier | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDynamicallyDefineDataIdentifierClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEcuInstanceProps | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEcuReset | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEcuResetClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnableCondition | DiagnosticCondition, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnableConditionGroup | DiagnosticConditionGroup, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnableConditionNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnableConditionPortMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnvBswModeElement | DiagnosticEnvModeElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnvCompareCondition | DiagnosticEnvConditionFormulaPart, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnvConditionFormula | DiagnosticEnvConditionFormulaPart, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnvConditionFormulaPart | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnvDataCondition | DiagnosticEnvCompareCondition, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnvDataElementCondition | DiagnosticEnvCompareCondition, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnvModeCondition | DiagnosticEnvCompareCondition, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnvModeElement | Referrable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnvSwcModeElement | DiagnosticEnvModeElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnvironmentalCondition | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEvent | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventManagerNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventPortMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventToDebounceAlgorithmMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventToEnableConditionGroupMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventToOperationCycleMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventToSecurityEventMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventToStorageConditionGroupMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventToTroubleCodeJ1939Mapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventToTroubleCodeUdsMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventWindow | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticExtendedDataRecord | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFimAliasEvent | DiagnosticAbstractAliasEvent, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFimAliasEventGroup | DiagnosticAbstractAliasEvent, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFimAliasEventGroupMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFimAliasEventMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFimEventGroup | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFimFunctionMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFreezeFrame | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFunctionIdentifier | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFunctionIdentifierInhibit | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFunctionInhibitSource | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIOControl | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIndicator | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticInfoType | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticInhibitSourceEventMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIoControlClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIoControlNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIumpr | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIumprDenominatorGroup | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIumprGroup | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIumprGroupIdentifier | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIumprToFunctionIdentifierMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939ExpandedFreezeFrame | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939FreezeFrame | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939Node | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939Spn | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939SpnMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939SwMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMapping | DiagnosticCommonElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMasterToSlaveEventMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMeasurementIdentifier | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryAddressableRangeAccess | DiagnosticMemoryByAddress, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryByAddress | DiagnosticServiceInstance, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryDestination | DiagnosticCommonElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryDestinationPrimary | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryDestinationUserDefined | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryIdentifier | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticOperationCycle | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticOperationCycleNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticOperationCyclePortMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticParameter | DiagnosticAbstractParameter, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticParameterElement | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticParameterElementAccess | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticParameterIdent | DiagnosticServiceMappingDiagTarget, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticParameterIdentifier | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticParameterSupportInfo | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticPeriodicRate | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticPowertrainFreezeFrame | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticProofOfOwnership | DiagnosticAuthentication, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticProtocol | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadDTCInformation | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadDTCInformationClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadDataByIdentifier | DiagnosticDataByIdentifier, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadDataByIdentifierClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadDataByPeriodicID | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadDataByPeriodicIDClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadMemoryByAddress | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadMemoryByAddressClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadScalingDataByIdentifier | DiagnosticDataByIdentifier, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadScalingDataByIdentifierClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestControlOfOnBoardDevice | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestControlOfOnBoardDeviceClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestCurrentPowertrainData | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestCurrentPowertrainDataClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestDownload | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestDownloadClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestEmissionRelatedDTC | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestEmissionRelatedDTCClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestEmissionRelatedDTCPermanentStatus | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestEmissionRelatedDTCPermanentStatusClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestFileTransfer | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestFileTransferClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestFileTransferNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestOnBoardMonitoringTestResults | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestOnBoardMonitoringTestResultsClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestPowertrainFreezeFrameData | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestPowertrainFreezeFrameDataClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestRoutineResults | DiagnosticRoutineSubfunction, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestUpload | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestUploadClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestVehicleInfo | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestVehicleInfoClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticResponseOnEvent | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticResponseOnEventClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRoutine | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRoutineControl | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRoutineControlClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRoutineSubfunction | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSecureCodingMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSecurityAccess | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSecurityAccessClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSecurityEventReportingModeMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSecurityLevel | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticServiceClass | DiagnosticCommonElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticServiceDataMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticServiceInstance | DiagnosticCommonElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticServiceMappingDiagTarget | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticServiceSwMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | DiagnosticServiceTable | DiagnosticCommonElement, False | ARElement, False | parent mismatch (expected DiagnosticCommonElement, got ARElement) |
| ✗ MISSING | DiagnosticSession | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSessionControl | DiagnosticServiceInstance, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSessionControlClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticStartRoutine | DiagnosticRoutineSubfunction, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticStopRoutine | DiagnosticRoutineSubfunction, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticStorageCondition | DiagnosticCondition, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticStorageConditionGroup | DiagnosticConditionGroup, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticStorageConditionNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticStorageConditionPortMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSupportInfoByte | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSwMapping | DiagnosticMapping, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTestIdentifier | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTestResult | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTestRoutineIdentifier | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTransferExit | DiagnosticMemoryByAddress, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTransferExitClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCode | DiagnosticCommonElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeGroup | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeJ1939 | DiagnosticTroubleCode, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeObd | DiagnosticTroubleCode, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeProps | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeUds | DiagnosticTroubleCode, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeUdsToTroubleCodeObdMapping | DiagnosticMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticUploadDownloadNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticVerifyCertificateBidirectional | DiagnosticAuthentication, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticVerifyCertificateUnidirectional | DiagnosticAuthentication, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticWriteDataByIdentifier | DiagnosticDataByIdentifier, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticWriteDataByIdentifierClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticWriteMemoryByAddress | DiagnosticCommonElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticWriteMemoryByAddressClass | DiagnosticServiceClass, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticsCommunicationSecurityNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DltApplication | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DltArgument | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DltConfig | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DltContext | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DltEcu | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DltLogChannel | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DltMessage | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DoIpActivationLineNeeds | DoIpServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DoIpConfig | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DoIpGidNeeds | DoIpServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DoIpGidSynchronizationNeeds | DoIpServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DoIpInterface | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DoIpPowerModeStatusNeeds | DoIpServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DoIpRoutingActivation | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DoIpRoutingActivationAuthenticationNeeds | DoIpServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DoIpRoutingActivationConfirmationNeeds | DoIpServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DoIpServiceNeeds | ServiceNeeds, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | DoIpTpConfig | FibexElement, False | TpConfig, False | parent mismatch (expected FibexElement, got TpConfig) |
| ⚠ MISMATCH | DocumentViewSelectable | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | Documentation | ARElement, False | ARObject, False | parent mismatch (expected ARElement, got ARObject) |
| ✗ MISSING | DocumentationContext | MultilanguageReferrable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | E2EProfileCompatibilityProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EOCEventRef | EOCExecutableEntityRefAbstract, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | EOCExecutableEntityRefAbstract | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | EOCExecutableEntityRefGroup | EOCExecutableEntityRefAbstract, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EcuPartition | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EcuResourceEstimation | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EcuTiming | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | EcucAbstractConfigurationClass | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | EcucAbstractExternalReferenceDef | EcucAbstractReferenceDef, True | EcucAbstractReferenceDef, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | EcucAbstractInternalReferenceDef | EcucAbstractReferenceDef, True | EcucAbstractReferenceDef, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | EcucAbstractReferenceDef | EcucCommonAttributes, True | EcucCommonAttributes, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | EcucAbstractReferenceValue | EcucIndexableValue, True | EcucIndexableValue, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | EcucAbstractStringParamDef | EcucParameterDef, True | EcucParameterDef, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | EcucCommonAttributes | EcucDefinitionElement, True | EcucDefinitionElement, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | EcucConditionFormula | FormulaExpression, False | ARObject, False | parent mismatch (expected FormulaExpression, got ARObject) |
| ⚠ MISMATCH | EcucContainerDef | EcucDefinitionElement, True | EcucDefinitionElement, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | EcucContainerValue | Identifiable, False | ARElement, False | parent mismatch (expected Identifiable, got ARElement) |
| ⚠ MISMATCH | EcucDefinitionCollection | AtpBlueprintable, False | ARObject, False | parent mismatch (expected AtpBlueprintable, got ARObject) |
| ⚠ MISMATCH | EcucDefinitionElement | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | EcucDestinationUriDefSet | AtpBlueprintable, False | Identifiable, False | parent mismatch (expected AtpBlueprintable, got Identifiable) |
| ⚠ MISMATCH | EcucIndexableValue | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | EcucLinkerSymbolDef | EcucAbstractStringParamDef, False | Identifiable, False | parent mismatch (expected EcucAbstractStringParamDef, got Identifiable) |
| ⚠ MISMATCH | EcucModuleDef | AtpDefinition, False | EcucDefinitionElement, False | parent mismatch (expected AtpDefinition, got EcucDefinitionElement) |
| ⚠ MISMATCH | EcucParamConfContainerDef | EcucContainerDef, False | None, False | parent mismatch (expected EcucContainerDef, got None) |
| ⚠ MISMATCH | EcucParameterDef | EcucCommonAttributes, True | EcucCommonAttributes, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | EcucParameterDerivationFormula | FormulaExpression, False | ARObject, False | parent mismatch (expected FormulaExpression, got ARObject) |
| ⚠ MISMATCH | EcucParameterValue | EcucIndexableValue, True | EcucIndexableValue, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | EcucQuery | Identifiable, False | ARObject, False | parent mismatch (expected Identifiable, got ARObject) |
| ✗ MISSING | EmphasisText | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | EndToEndProtectionSet | ARElement, False | Identifiable, False | parent mismatch (expected ARElement, got Identifiable) |
| ⚠ MISMATCH | EngineeringObject | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | Entry | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EnumerationMappingEntry | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EnumerationMappingTable | PackageableElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ErrorTracerNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EthGlobalTimeDomainProps | AbstractGlobalTimeDomainProps, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EthGlobalTimeManagedCouplingPort | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EthIpProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EthTSynCrcFlags | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EthTSynSubTlvConfig | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EthTcpIpIcmpProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EthTcpIpProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EthTpConfig | FibexElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EthTpConnection | TpConnection, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EthernetFrameTriggering | FrameTriggering, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EthernetWakeupSleepOnDatalineConfig | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EthernetWakeupSleepOnDatalineConfigSet | FibexElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EvaluatedVariantSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EventObdReadinessGroup | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EventTriggeringConstraint | TimingConstraint, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ExclusiveAreaNestingOrder | Referrable, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ExecutableEntity | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | ExecutableEntityActivationReason | ImplementationProps, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ExecutionTime | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ExecutionTimeConstraint | TimingConstraint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ExternalTriggerOccurredEvent | AtpStructureElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ExternalTriggeringPointIdent | IdentCaption, False | AbstractAccessPoint, False | parent mismatch (expected IdentCaption, got AbstractAccessPoint) |
| ✗ MISSING | FMFeature | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FMFeatureModel | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | FibexElement | PackageableElement, True | Identifiable, False | parent mismatch (expected PackageableElement, got Identifiable), abstract mismatch (expected True, got False) |
| ✗ MISSING | FirewallRule | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FirewallRuleProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | FlatMap | AtpBlueprintable, False | ARElement, False | parent mismatch (expected AtpBlueprintable, got ARElement) |
| ✗ MISSING | FlexrayArTpChannel | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FlexrayArTpConfig | FibexElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FlexrayArTpConnection | TpConnection, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FlexrayArTpNode | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FlexrayFifoConfiguration | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FlexrayFifoRange | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FlexrayTpConfig | FibexElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FlexrayTpConnection | TpConnection, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FlexrayTpConnectionControl | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FlexrayTpEcu | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FlexrayTpNode | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FlexrayTpPduPool | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FloatValueVariationPoint | AttributeValueVariationPoint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ForbiddenSignalPath | SignalPathConstraint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FormulaExpression | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FrGlobalTimeDomainProps | AbstractGlobalTimeDomainProps, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | Frame | FibexElement, True | Identifiable, False | parent mismatch (expected FibexElement, got Identifiable), abstract mismatch (expected True, got False) |
| ✗ MISSING | FramePid | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | FrameTriggering | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | FreeFormat | FreeFormatEntry, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | FreeFormatEntry | ScheduleTableEntry, True | ScheduleTableEntry, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | FunctionInhibitionAvailabilityNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FunctionInhibitionNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FurtherActionByteNeeds | DoIpServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | GeneralAnnotation | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | GeneralPurposeConnection | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | GeneralPurposePdu | FibexElement, False | Pdu, False | parent mismatch (expected FibexElement, got Pdu) |
| ✗ MISSING | GenericModelReference | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | GlobalSupervisionNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | GlobalTimeCanMaster | GlobalTimeMaster, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | GlobalTimeCanSlave | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | GlobalTimeCorrectionProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | GlobalTimeCouplingPortProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | GlobalTimeDomain | FibexElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | GlobalTimeEthMaster | GlobalTimeMaster, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | GlobalTimeEthSlave | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | GlobalTimeFrMaster | GlobalTimeMaster, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | GlobalTimeFrSlave | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | GlobalTimeGateway | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | GlobalTimeMaster | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | HardwareTestNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | HeapUsage | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | HttpTp | TransportProtocolConfiguration, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | HwAttributeLiteralDef | Identifiable, False | ARElement, False | parent mismatch (expected Identifiable, got ARElement) |
| ⚠ MISMATCH | HwAttributeValue | ARObject, False | ARElement, False | parent mismatch (expected ARObject, got ARElement) |
| ⚠ MISMATCH | HwCategory | AtpDefinition, False | ARElement, False | parent mismatch (expected AtpDefinition, got ARElement) |
| ⚠ MISMATCH | HwDescriptionEntity | Referrable, True | ARElement, False | parent mismatch (expected Referrable, got ARElement), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | HwElementConnector | Describable, False | ARElement, False | parent mismatch (expected Describable, got ARElement) |
| ⚠ MISMATCH | HwPin | Identifiable, False | HwDescriptionEntity, False | parent mismatch (expected Identifiable, got HwDescriptionEntity) |
| ✗ MISSING | HwPinConnector | Describable, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | HwPinGroup | Identifiable, False | HwDescriptionEntity, False | parent mismatch (expected Identifiable, got HwDescriptionEntity) |
| ✗ MISSING | HwPinGroupConnector | Describable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | HwPortMapping | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | HwType | HwDescriptionEntity, False | ARElement, False | parent mismatch (expected HwDescriptionEntity, got ARElement) |
| ✗ MISSING | IEEE1722TpAafConnection | IEEE1722TpAvConnection, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpAcfBus | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpAcfBusPart | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpAcfCan | IEEE1722TpAcfBus, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpAcfCanPart | IEEE1722TpAcfBusPart, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpAcfConnection | IEEE1722TpConnection, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpAcfLin | IEEE1722TpAcfBus, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpAcfLinPart | IEEE1722TpAcfBusPart, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpAvConnection | IEEE1722TpConnection, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpConfig | FibexElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpConnection | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpCrfConnection | IEEE1722TpAvConnection, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpIidcConnection | IEEE1722TpAvConnection, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpRvfConnection | IEEE1722TpAvConnection, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IPSecConfig | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IPSecConfigProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IPSecRule | Identifiable, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | IPdu | FibexElement, True | Pdu, False | parent mismatch (expected FibexElement, got Pdu), abstract mismatch (expected True, got False) |
| ✗ MISSING | IPv6ExtHeaderFilterList | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IPv6ExtHeaderFilterSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ISignalProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | IdentCaption | AtpStructureElement, True | Identifiable, False | parent mismatch (expected AtpStructureElement, got Identifiable), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | Identifiable | MultilanguageReferrable, True | MultilanguageReferrable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | IdsMgrCustomTimestampNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IdsMgrNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Ieee1722Tp | TransportProtocolConfiguration, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Ieee1722TpEthernetFrame | AbstractEthernetFrame, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | Implementation | ARElement, True | PackageableElement, False | parent mismatch (expected ARElement, got PackageableElement), abstract mismatch (expected True, got False) |
| ✗ MISSING | ImplementationDataTypeElementInPortInterfaceRef | DataPrototypeReference, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ImplementationDataTypeSubElementRef | SubElementRef, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ImplementationElementInParameterInstanceRef | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ImplementationProps | Referrable, True | Referrable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | IndentSample | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IndexEntry | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IndicatorStatusNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | InitEvent | AtpStructureElement, False | RTEEvent, False | parent mismatch (expected AtpStructureElement, got RTEEvent) |
| ✗ MISSING | InnerDataPrototypeGroupInCompositionInstanceRef | AtpInstanceRef, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | InnerRunnableEntityGroupInCompositionInstanceRef | AtpInstanceRef, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | InstanceEventInCompositionInstanceRef | AtpInstanceRef, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | InstantiationDataDefProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | InstantiationRTEEventProps | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | InstantiationTimingEventProps | InstantiationRTEEventProps, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IntegerValueVariationPoint | AttributeValueVariationPoint, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | InternalBehavior | AtpStructureElement, True | Identifiable, False | parent mismatch (expected AtpStructureElement, got Identifiable), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | InternalTriggerOccurredEvent | AtpStructureElement, False | RTEEvent, False | parent mismatch (expected AtpStructureElement, got RTEEvent) |
| ✗ MISSING | InterpolationRoutine | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | InterpolationRoutineMapping | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | InterpolationRoutineMappingSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IoHwAbstractionServerAnnotation | GeneralAnnotation, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Ipv4ArpProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Ipv4AutoIpProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Ipv4DhcpServerConfiguration | Describable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Ipv4FragmentationProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Ipv4Props | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Ipv6DhcpServerConfiguration | Describable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Ipv6FragmentationProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Ipv6NdpProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Ipv6Props | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | J1939Cluster | AbstractCanCluster, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | J1939ControllerApplication | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | J1939ControllerApplicationToJ1939NmNodeMapping | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | J1939DcmDm19Support | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | J1939DcmIPdu | IPdu, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | J1939NodeName | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | J1939RmIncomingRequestServiceNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | J1939RmOutgoingRequestServiceNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | J1939TpConfig | FibexElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | J1939TpConnection | TpConnection, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | J1939TpNode | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | J1939TpPg | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | LLongName | MixedContentForLongName, False | LanguageSpecific, False | parent mismatch (expected MixedContentForLongName, got LanguageSpecific) |
| ⚠ MISMATCH | LOverviewParagraph | MixedContentForOverviewParagraph, False | LanguageSpecific, False | parent mismatch (expected MixedContentForOverviewParagraph, got LanguageSpecific) |
| ⚠ MISMATCH | LParagraph | MixedContentForParagraph, False | LanguageSpecific, False | parent mismatch (expected MixedContentForParagraph, got LanguageSpecific) |
| ⚠ MISMATCH | LPlainText | MixedContentForPlainText, False | LanguageSpecific, False | parent mismatch (expected MixedContentForPlainText, got LanguageSpecific) |
| ✗ MISSING | LVerbatim | MixedContentForVerbatim, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | LabeledItem | Paginateable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | LabeledList | Paginateable, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | LanguageSpecific | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | LatencyTimingConstraint | TimingConstraint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | LifeCycleState | AtpBlueprintable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | LifeCycleStateDefinitionGroup | AtpBlueprintable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | LimitValueVariationPoint | AbstractNumericalVariationPoint, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | LinCommunicationController | CommunicationController, True | CommunicationController, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | LinConfigurableFrame | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | LinConfigurationEntry | ScheduleTableEntry, True | ScheduleTableEntry, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | LinErrorResponse | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | LinEventTriggeredFrame | LinFrame, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | LinFrame | Frame, True | Frame, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | LinOrderedConfigurableFrame | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | LinSlave | LinCommunicationController, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | LinSlaveConfig | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | LinSlaveConfigIdent | Referrable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | LinSporadicFrame | LinFrame, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | LinTpConfig | FibexElement, False | TpConfig, False | parent mismatch (expected FibexElement, got TpConfig) |
| ✗ MISSING | Linker | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | List | Paginateable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MacMulticastConfiguration | NetworkEndpointAddress, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MacSecCipherSuiteConfig | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MacSecCryptoAlgoConfig | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MacSecGlobalKayProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MacSecKayParticipant | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MacSecLocalKayProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MacSecParticipantSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MacSecProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MappingConstraint | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | McDataAccessDetails | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | McDataInstance | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | McFunction | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | McFunctionDataRefSet | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | McGroup | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | McGroupDataRefSet | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | McParameterElementGroup | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | McSupportData | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | McSwEmulationMethodSupport | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MeasuredExecutionTime | ExecutionTime, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MeasuredHeapUsage | HeapUsage, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MemorySectionLocation | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MixedContentForLongName | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MixedContentForOverviewParagraph | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MixedContentForParagraph | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MixedContentForPlainText | WhitespaceControlled, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MixedContentForUnitNames | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MixedContentForVerbatim | WhitespaceControlled, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | MlFormula | Paginateable, False | ARObject, False | parent mismatch (expected Paginateable, got ARObject) |
| ⚠ MISMATCH | ModeDeclaration | AtpStructureElement, False | Identifiable, False | parent mismatch (expected AtpStructureElement, got Identifiable) |
| ⚠ MISMATCH | ModeDeclarationGroup | AtpType, False | Identifiable, False | parent mismatch (expected AtpType, got Identifiable) |
| ⚠ MISMATCH | ModeDeclarationGroupPrototype | AtpPrototype, False | Identifiable, False | parent mismatch (expected AtpPrototype, got Identifiable) |
| ⚠ MISMATCH | ModeDeclarationMapping | AtpStructureElement, False | Identifiable, False | parent mismatch (expected AtpStructureElement, got Identifiable) |
| ⚠ MISMATCH | ModeDeclarationMappingSet | AtpType, False | ARElement, False | parent mismatch (expected AtpType, got ARElement) |
| ✗ MISSING | ModeErrorBehavior | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ModeGroupInAtomicSwcInstanceRef | AtpInstanceRef, True | AtpInstanceRef, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | ModeInBswModuleDescriptionInstanceRef | AtpInstanceRef, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ModeInSwcInstanceRef | AtpInstanceRef, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ModePortAnnotation | GeneralAnnotation, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ModeSwitchEventTriggeredActivity | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ModeSwitchInterface | AtpType, False | PortInterface, False | parent mismatch (expected AtpType, got PortInterface) |
| ⚠ MISMATCH | ModeSwitchSenderComSpec | PPortComSpec, False | RPortComSpec, False | parent mismatch (expected PPortComSpec, got RPortComSpec) |
| ⚠ MISMATCH | ModeSwitchedAckEvent | AtpStructureElement, False | RTEEvent, False | parent mismatch (expected AtpStructureElement, got RTEEvent) |
| ✗ MISSING | ModeTransition | AtpStructureElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MsrQueryArg | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MsrQueryChapter | Paginateable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MsrQueryP1 | Paginateable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MsrQueryP2 | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MsrQueryProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MsrQueryResultChapter | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MsrQueryResultTopic1 | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MsrQueryTopic1 | Paginateable, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | MultiLanguageParagraph | Paginateable, False | ARObject, False | parent mismatch (expected Paginateable, got ARObject) |
| ✗ MISSING | MultiLanguageVerbatim | Paginateable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MultidimensionalTime | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | MultilanguageReferrable | Referrable, True | Referrable, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | MultiplexedPart | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | NetworkEndpointAddress | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | NetworkSegmentIdentification | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | NmCluster | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | NmClusterCoupling | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | NmCoordinator | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | NmNode | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | NmPdu | FibexElement, False | Pdu, False | parent mismatch (expected FibexElement, got Pdu) |
| ✗ MISSING | NotAvailableValueSpecification | ValueSpecification, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Note | Paginateable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | NumericalOrText | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | NumericalRuleBasedValueSpecification | AbstractRuleBasedValueSpecification, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | NumericalValueVariationPoint | AbstractNumericalVariationPoint, False | ARObject, False | parent mismatch (expected AbstractNumericalVariationPoint, got ARObject) |
| ✗ MISSING | NvBlockDataMapping | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | NvBlockDescriptor | AtpStructureElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | NvDataInterface | AtpType, False | DataInterface, False | parent mismatch (expected AtpType, got DataInterface) |
| ✗ MISSING | NvDataPortAnnotation | GeneralAnnotation, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ObdControlServiceNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ObdInfoServiceNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ObdMonitorServiceNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ObdPidServiceNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ObdRatioDenominatorNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ObdRatioServiceNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | OffsetTimingConstraint | TimingConstraint, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | OperationInAtomicSwcInstanceRef | AtpInstanceRef, True | AtpInstanceRef, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | OperationInSystemInstanceRef | AtpInstanceRef, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | OperationInvokedEvent | AtpStructureElement, False | RTEEvent, False | parent mismatch (expected AtpStructureElement, got RTEEvent) |
| ✗ MISSING | OrderedMaster | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | OsTaskExecutionEvent | AtpStructureElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | OsTaskProxy | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | PModeInSystemInstanceRef | AtpInstanceRef, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | PPortComSpec | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | PRPortPrototype | AbstractRequiredPortPrototype, False | PortPrototype, False | parent mismatch (expected AbstractRequiredPortPrototype, got PortPrototype) |
| ✗ MISSING | PTriggerInAtomicSwcTypeInstanceRef | TriggerInAtomicSwcInstanceRef, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | PackageableElement | CollectableElement, True | Identifiable, False | parent mismatch (expected CollectableElement, got Identifiable), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | Paginateable | DocumentViewSelectable, True | DocumentViewSelectable, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | ParameterInterface | AtpType, False | DataInterface, False | parent mismatch (expected AtpType, got DataInterface) |
| ✗ MISSING | ParameterPortAnnotation | GeneralAnnotation, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ParameterProvideComSpec | PPortComSpec, False | RPortComSpec, False | parent mismatch (expected PPortComSpec, got RPortComSpec) |
| ✗ MISSING | ParameterSwComponentType | AtpType, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | PassThroughSwConnector | AtpStructureElement, False | SwConnector, False | parent mismatch (expected AtpStructureElement, got SwConnector) |
| ⚠ MISMATCH | Pdu | FibexElement, True | FibexElement, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | PduActivationRoutingGroup | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | PdurIPduGroup | FibexElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | PerInstanceMemory | AtpStructureElement, False | Identifiable, False | parent mismatch (expected AtpStructureElement, got Identifiable) |
| ✗ MISSING | PerInstanceMemorySize | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | PeriodicEventTriggering | EventTriggeringConstraint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | PermissibleSignalPath | SignalPathConstraint, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | PhysicalChannel | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | PhysicalDimensionMapping | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | PhysicalDimensionMappingSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | PlcaProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | PncMapping | Describable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | PncMappingIdent | Referrable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | PortElementToCommunicationResourceMapping | Identifiable, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | PortGroup | AtpStructureElement, False | Identifiable, False | parent mismatch (expected AtpStructureElement, got Identifiable) |
| ✗ MISSING | PortGroupInSystemInstanceRef | AtpInstanceRef, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | PortInCompositionTypeInstanceRef | AtpInstanceRef, True | AtpInstanceRef, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | PortInterface | AtpType, True | AtpType, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | PortInterfaceMapping | AtpBlueprintable, True | Identifiable, False | parent mismatch (expected AtpBlueprintable, got Identifiable), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | PortInterfaceMappingSet | AtpBlueprintable, False | ARElement, False | parent mismatch (expected AtpBlueprintable, got ARElement) |
| ⚠ MISMATCH | PortPrototype | AtpPrototype, True | Identifiable, False | parent mismatch (expected AtpPrototype, got Identifiable), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | PortPrototypeBlueprint | AtpStructureElement, False | ARElement, False | parent mismatch (expected AtpStructureElement, got ARElement) |
| ✗ MISSING | PositiveIntegerValueVariationPoint | AttributeValueVariationPoint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | PostBuildVariantCondition | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | PostBuildVariantCriterion | AtpDefinition, False | ARObject, False | parent mismatch (expected AtpDefinition, got ARObject) |
| ✗ MISSING | PostBuildVariantCriterionValueSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | PredefinedChapter | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | PredefinedVariant | ARElement, False | ARObject, False | parent mismatch (expected ARElement, got ARObject) |
| ✗ MISSING | Prms | Paginateable, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | RPortComSpec | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | RTEEvent | AtpStructureElement, True | AbstractEvent, False | parent mismatch (expected AtpStructureElement, got AbstractEvent), abstract mismatch (expected True, got False) |
| ✗ MISSING | RTriggerInAtomicSwcInstanceRef | TriggerInAtomicSwcInstanceRef, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RapidPrototypingScenario | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ReceiverAnnotation | SenderReceiverAnnotation, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ReceiverComSpec | RPortComSpec, True | RPortComSpec, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | ReceptionComSpecProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ReferenceValueSpecification | ValueSpecification, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | Referrable | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | RoleBasedBswModuleEntryAssignment | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RoleBasedMcDataAssignment | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RoleBasedResourceDependency | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | RootSwCompositionPrototype | AtpPrototype, False | Identifiable, False | parent mismatch (expected AtpPrototype, got Identifiable) |
| ✗ MISSING | RoughEstimateHeapUsage | HeapUsage, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RoughEstimateOfExecutionTime | ExecutionTime, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Row | Paginateable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RptComponent | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RptContainer | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RptExecutableEntity | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RptExecutableEntityEvent | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RptExecutableEntityProperties | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RptExecutionContext | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RptHook | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RptImplPolicy | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RptProfile | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RptServicePoint | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RptSupportData | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RptSwPrototypingAccess | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RteEventInCompositionSeparation | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RteEventInCompositionToOsTaskProxyMapping | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RteEventInSystemSeparation | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RteEventInSystemToOsTaskProxyMapping | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RtePluginProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RtpTp | TransportProtocolConfiguration, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RuleArguments | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RuleBasedAxisCont | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RuleBasedValueCont | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RuleBasedValueSpecification | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RunnableEntityGroup | AtpStructureElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RunnableEntityInCompositionInstanceRef | AtpInstanceRef, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | RuntimeError | TracedFailure, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SOMEIPTransformationDescription | TransformationDescription, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SOMEIPTransformationISignalProps | TransformationISignalProps, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SOMEIPTransformationProps | TransformationProps, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SaveConfigurationEntry | LinConfigurationEntry, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ScaleConstr | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ScheduleTableEntry | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | Sdf | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgAbstractForeignReference | SdgAttribute, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgAbstractPrimitiveAttribute | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgAggregationWithVariation | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgAttribute | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgClass | SdgElementWithGid, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgContents | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgDef | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgElementWithGid | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgForeignReference | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgForeignReferenceWithVariation | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgPrimitiveAttribute | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgPrimitiveAttributeWithVariation | AbstractVariationRestriction, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgReference | SdgAttribute, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SectionNamePrefix | ImplementationProps, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SecureCommunicationPropsSet | FibexElement, False | Identifiable, False | parent mismatch (expected FibexElement, got Identifiable) |
| ✗ MISSING | SecureOnBoardCommunicationNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SecurityEventContextProps | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SecurityEventDefinition | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SenderAnnotation | SenderReceiverAnnotation, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SenderComSpec | PPortComSpec, True | PPortComSpec, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | SenderRecCompositeTypeMapping | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | SenderReceiverAnnotation | GeneralAnnotation, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SenderReceiverCompositeElementToSignalMapping | DataMapping, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SenderReceiverInterface | AtpType, False | DataInterface, False | parent mismatch (expected AtpType, got DataInterface) |
| ✗ MISSING | SeparateSignalPath | SignalPathConstraint, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ServerCallPoint | AbstractAccessPoint, True | AbstractAccessPoint, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | ServiceDependency | ARObject, True | Identifiable, False | parent mismatch (expected ARObject, got Identifiable), abstract mismatch (expected True, got False) |
| ✗ MISSING | ServiceInstanceCollectionSet | FibexElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ServiceNeeds | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | ShortNameFragment | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SignalPathConstraint | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SignalServiceTranslationElementProps | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SignalServiceTranslationEventProps | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SignalServiceTranslationProps | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SignalServiceTranslationPropsSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SimulatedExecutionTime | ExecutionTime, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SingleLanguageLongName | MixedContentForLongName, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SingleLanguageReferrable | Referrable, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SingleLanguageUnitNames | MixedContentForUnitNames, False | ARLiteral, False | parent mismatch (expected MixedContentForUnitNames, got ARLiteral) |
| ✗ MISSING | SlOverviewParagraph | MixedContentForOverviewParagraph, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SlParagraph | MixedContentForParagraph, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SoAdRoutingGroup | FibexElement, False | Identifiable, False | parent mismatch (expected FibexElement, got Identifiable) |
| ✗ MISSING | SoConIPduIdentifier | Referrable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SocketConnectionIpduIdentifierSet | FibexElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SomeipSdClientEventGroupTimingConfig | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SomeipSdClientServiceInstanceConfig | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SomeipSdServerEventGroupTimingConfig | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SomeipSdServerServiceInstanceConfig | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SomeipServiceVersion | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SomeipTpChannel | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SomeipTpConfig | FibexElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SomeipTpConnection | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SporadicEventTriggering | EventTriggeringConstraint, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | StackUsage | Identifiable, True | Identifiable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | StateDependentFirewall | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | StaticSocketConnection | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Std | SingleLanguageReferrable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | StreamFilterIEEE1722Tp | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | StreamFilterIpv4Address | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | StreamFilterIpv6Address | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | StreamFilterMACAddress | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | StreamFilterPortRange | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | StreamFilterRuleDataLinkLayer | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | StreamFilterRuleIpTp | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | StructuredReq | Paginateable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SubElementMapping | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SubElementRef | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SupervisedEntityCheckpointNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SupervisedEntityNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SwAddrMethod | AtpBlueprintable, False | Identifiable, False | parent mismatch (expected AtpBlueprintable, got Identifiable) |
| ✗ MISSING | SwAxisCont | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwAxisType | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwBitRepresentation | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SwCalprmAxisTypeProps | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | SwCalprmRefProxy | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SwComponentPrototype | AtpPrototype, False | Identifiable, False | parent mismatch (expected AtpPrototype, got Identifiable) |
| ✗ MISSING | SwComponentPrototypeAssignment | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SwComponentType | AtpType, True | ARElement, False | parent mismatch (expected AtpType, got ARElement), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | SwConnector | AtpStructureElement, True | Identifiable, False | parent mismatch (expected AtpStructureElement, got Identifiable), abstract mismatch (expected True, got False) |
| ✗ MISSING | SwDataDependency | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwDataDependencyArgs | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwGenericAxisParamType | Identifiable, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SwSystemconst | AtpDefinition, False | ARObject, False | parent mismatch (expected AtpDefinition, got ARObject) |
| ✗ MISSING | SwSystemconstDependentFormula | FormulaExpression, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwSystemconstValue | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SwSystemconstantValueSet | ARElement, False | ARObject, False | parent mismatch (expected ARElement, got ARObject) |
| ✗ MISSING | SwVariableRefProxy | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SwcBswMapping | AtpStructureElement, False | Identifiable, False | parent mismatch (expected AtpStructureElement, got Identifiable) |
| ✗ MISSING | SwcBswSynchronizedModeGroupPrototype | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwcBswSynchronizedTrigger | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwcExclusiveAreaPolicy | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwcModeManagerErrorEvent | AtpStructureElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SwcModeSwitchEvent | AtpStructureElement, False | RTEEvent, False | parent mismatch (expected AtpStructureElement, got RTEEvent) |
| ⚠ MISMATCH | SwcServiceDependency | AtpStructureElement, False | ServiceDependency, False | parent mismatch (expected AtpStructureElement, got ServiceDependency) |
| ✗ MISSING | SwcServiceDependencyInSystemInstanceRef | AtpInstanceRef, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwcSupportedFeature | ARObject, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SwcTiming | ARElement, False | TimingExtension, False | parent mismatch (expected ARElement, got TimingExtension) |
| ✗ MISSING | SwcToApplicationPartitionMapping | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwcToSwcOperationArguments | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwcToSwcSignal | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwitchAsynchronousTrafficShaperGroupEntry | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwitchFlowMeteringEntry | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwitchStreamFilterActionDestPortModification | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwitchStreamFilterEntry | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwitchStreamFilterRule | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwitchStreamGateEntry | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwitchStreamIdentification | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SymbolicNameProps | ImplementationProps, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SyncTimeBaseMgrUserNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SynchronizationPointConstraint | TimingConstraint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SynchronizationTimingConstraint | TimingConstraint, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SynchronousServerCallPoint | AbstractAccessPoint, False | ServerCallPoint, False | parent mismatch (expected AbstractAccessPoint, got ServerCallPoint) |
| ⚠ MISMATCH | System | AtpStructureElement, False | ARElement, False | parent mismatch (expected AtpStructureElement, got ARElement) |
| ✗ MISSING | SystemSignalGroupToCommunicationResourceMapping | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SystemSignalToCommunicationResourceMapping | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SystemTiming | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDCpSoftwareClusterMapping | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDCpSoftwareClusterMappingSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDCpSoftwareClusterResourceMapping | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventBsw | TimingDescriptionEvent, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventBswInternalBehavior | TimingDescriptionEvent, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventBswModeDeclaration | TDEventBsw, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventBswModule | TDEventBsw, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventCom | TimingDescriptionEvent, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventComplex | TimingDescriptionEvent, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventCycleStart | TDEventCom, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventFrClusterCycleStart | TDEventCycleStart, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventFrame | TDEventCom, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventFrameEthernet | TDEventCom, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventIPdu | TDEventCom, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventISignal | TDEventCom, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventModeDeclaration | TDEventVfbPort, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventOccurrenceExpression | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventOccurrenceExpressionFormula | FormulaExpression, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventOperation | TDEventVfbPort, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventSLLET | TimingDescriptionEvent, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventSLLETPort | TDEventSLLET, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventSwc | TimingDescriptionEvent, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventSwcInternalBehavior | TDEventSwc, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventSwcInternalBehaviorReference | TDEventSwc, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventTTCanCycleStart | TDEventCycleStart, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventTrigger | TDEventVfbPort, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventVariableDataPrototype | TDEventVfbPort, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventVfb | TimingDescriptionEvent, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventVfbPort | TDEventVfb, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDEventVfbReference | TDEventVfb, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TDHeaderIdRange | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Table | Paginateable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TagWithOptionalValue | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Tbody | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TcpIpIcmpv4Props | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TcpIpIcmpv6Props | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TcpOptionFilterList | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TcpOptionFilterSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TcpProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | TcpUdpConfig | TransportProtocolConfiguration, True | TransportProtocolConfiguration, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | TextTableValuePair | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Tgroup | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | TimeSyncServerConfiguration | Referrable, False | ARObject, False | parent mismatch (expected Referrable, got ARObject) |
| ✗ MISSING | TimeValueValueVariationPoint | AttributeValueVariationPoint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TimingClockSyncAccuracy | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TimingCondition | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TimingConditionFormula | FormulaExpression, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | TimingConstraint | Traceable, True | Identifiable, False | parent mismatch (expected Traceable, got Identifiable), abstract mismatch (expected True, got False) |
| ✗ MISSING | TimingDescription | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TimingDescriptionEvent | TimingDescription, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TimingDescriptionEventChain | TimingDescription, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | TimingEvent | AtpStructureElement, False | RTEEvent, False | parent mismatch (expected AtpStructureElement, got RTEEvent) |
| ⚠ MISMATCH | TimingExtension | ARElement, True | Identifiable, False | parent mismatch (expected ARElement, got Identifiable), abstract mismatch (expected True, got False) |
| ✗ MISSING | TimingExtensionResource | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TimingModeInstance | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TlsCryptoCipherSuite | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TlsCryptoCipherSuiteProps | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TlsPskIdentity | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TlvDataIdDefinition | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TlvDataIdDefinitionSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Topic1 | Paginateable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TopicContent | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TopicContentOrMsrQuery | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TopicOrMsrQuery | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | TpConfig | FibexElement, True | FibexElement, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | TpConnection | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | Traceable | MultilanguageReferrable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TraceableText | Paginateable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TracedFailure | Identifiable, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | TransformationComSpecProps | Describable, True | Describable, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | TransformationDescription | Describable, True | Describable, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | TransformationISignalProps | Describable, True | Describable, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | TransformationProps | Identifiable, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TransformationPropsSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TransformerHardErrorEvent | AtpStructureElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TransientFault | TracedFailure, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TransmissionComSpecProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | TransportProtocolConfiguration | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | Trigger | AtpStructureElement, False | Identifiable, False | parent mismatch (expected AtpStructureElement, got Identifiable) |
| ✗ MISSING | TriggerIPduSendCondition | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TriggerInAtomicSwcInstanceRef | AtpInstanceRef, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TriggerInSystemInstanceRef | AtpInstanceRef, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | TriggerInterface | AtpType, False | PortInterface, False | parent mismatch (expected AtpType, got PortInterface) |
| ✗ MISSING | TriggerPortAnnotation | GeneralAnnotation, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TriggerToSignalMapping | DataMapping, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Tt | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TtcanAbsolutelyScheduledTiming | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TtcanCluster | AbstractCanCluster, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TtcanCommunicationConnector | AbstractCanCommunicationConnector, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TtcanCommunicationController | AbstractCanCommunicationController, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TtcanPhysicalChannel | AbstractCanPhysicalChannel, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | UdpProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | UnassignFrameId | LinConfigurationEntry, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | UnlimitedIntegerValueVariationPoint | AttributeValueVariationPoint, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | UserDefinedCluster | CommunicationCluster, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | UserDefinedCommunicationConnector | CommunicationConnector, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | UserDefinedCommunicationController | CommunicationController, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | UserDefinedEthernetFrame | AbstractEthernetFrame, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | UserDefinedGlobalTimeMaster | GlobalTimeMaster, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | UserDefinedGlobalTimeSlave | Identifiable, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | UserDefinedPdu | FibexElement, False | Pdu, False | parent mismatch (expected FibexElement, got Pdu) |
| ✗ MISSING | UserDefinedPhysicalChannel | PhysicalChannel, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | UserDefinedTransformationDescription | TransformationDescription, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | UserDefinedTransformationISignalProps | TransformationISignalProps, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | UserDefinedTransformationProps | TransformationProps, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | V2xDataManagerNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | V2xFacUserNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | V2xMUserNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ValueGroup | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ValueSpecification | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | VariableAccess | AbstractAccessPoint, False | Identifiable, False | parent mismatch (expected AbstractAccessPoint, got Identifiable) |
| ✗ MISSING | VariableDataPrototypeInCompositionInstanceRef | AtpInstanceRef, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | VariableInAtomicSwcInstanceRef | AtpInstanceRef, True | AtpInstanceRef, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | VariationPointProxy | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | VendorSpecificServiceNeeds | ServiceNeeds, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | VfbTiming | AtpBlueprintable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ViewMap | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ViewMapSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | WaitPoint | Identifiable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | WarningIndicatorRequestedBitNeeds | DiagnosticCapabilityElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | WhitespaceControlled | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | WorstCaseHeapUsage | HeapUsage, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Xdoc | SingleLanguageReferrable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Xfile | SingleLanguageReferrable, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Xref | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | XrefTarget | SingleLanguageReferrable, False | Not Found, N/A | Class not found in source code |

## Extra Classes (Not Documented)

| Status | Class | Documented (Parent, Abstract) | Actual (Parent, Abstract) | Notes |
|--------|-------|-------------------------------|---------------------------|-------|
| + EXTRA | ARBoolean | N/A, N/A | ARType, False | Class exists but not documented |
| + EXTRA | AREnum | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | ARFloat | N/A, N/A | ARNumerical, False | Class exists but not documented |
| + EXTRA | ARList | N/A, N/A | Paginateable, False | Class exists but not documented |
| + EXTRA | ARLiteral | N/A, N/A | ARType, False | Class exists but not documented |
| + EXTRA | ARNumerical | N/A, N/A | ARType, False | Class exists but not documented |
| + EXTRA | ARPositiveInteger | N/A, N/A | ARNumerical, False | Class exists but not documented |
| + EXTRA | ARType | N/A, N/A | None, False | Class exists but not documented |
| + EXTRA | AUTOSARDoc | N/A, N/A | AbstractAUTOSAR, False | Class exists but not documented |
| + EXTRA | AbstractAUTOSAR | N/A, N/A | CollectableElement, False | Class exists but not documented |
| + EXTRA | ArgumentDirectionEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | AutoCollectEnum | N/A, N/A | Enum, False | Class exists but not documented |
| + EXTRA | Boolean | N/A, N/A | ARBoolean, False | Class exists but not documented |
| + EXTRA | BswApiOptions | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | BswCallType | N/A, N/A | str, False | Class exists but not documented |
| + EXTRA | BswDataReceptionPolicy | N/A, N/A | BswApiOptions, False | Class exists but not documented |
| + EXTRA | BswEntryKindEnum | N/A, N/A | str, False | Class exists but not documented |
| + EXTRA | BswExecutionContext | N/A, N/A | str, False | Class exists but not documented |
| + EXTRA | BswInterruptCategory | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | BswQueuedDataReceptionPolicy | N/A, N/A | BswDataReceptionPolicy, False | Class exists but not documented |
| + EXTRA | ByteOrderEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | CIdentifier | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | CategoryString | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | CommunicationDirectionType | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | CycleRepetitionType | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DataFilterTypeEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DataIdModeEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DataTransformationKindEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DateTime | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | DiagRequirementIdString | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | DiagnosticAudienceEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DiagnosticClearDtcNotificationEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DiagnosticProcessingStyleEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DiagnosticRoutineTypeEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DiagnosticServiceRequestCallbackTypeEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DiagnosticValueAccessEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DtcFormatTypeEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DtcKindEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | EcucConfigurationClassEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | EcucConfigurationVariantEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | EcucDestinationUriDefRefType | N/A, N/A | RefType, False | Class exists but not documented |
| + EXTRA | EcucScopeEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | EcucSymbolicNameReferenceDef | N/A, N/A | EcucAbstractInternalReferenceDef, False | Class exists but not documented |
| + EXTRA | EndToEndProfileBehaviorEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | FlexrayChannelName | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | Float | N/A, N/A | ARFloat, False | Class exists but not documented |
| + EXTRA | GraphicFitEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | HandleInvalidEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | IPduSignalProcessingEnum | N/A, N/A | Enum, False | Class exists but not documented |
| + EXTRA | ISignalPort | N/A, N/A | CommConnectorPort, False | Class exists but not documented |
| + EXTRA | Identifier | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | Integer | N/A, N/A | ARNumerical, False | Class exists but not documented |
| + EXTRA | Ip4AddressString | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | Ip6AddressString | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | KeywordSet | N/A, N/A | ARElement, False | Class exists but not documented |
| + EXTRA | LEnum | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | Limit | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ListEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | MacAddressString | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | ModeActivationKind | N/A, N/A | str, False | Class exists but not documented |
| + EXTRA | NameToken | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | NvBlockNeedsReliabilityEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | NvBlockNeedsWritingPriorityEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | PduToFrameMapping | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | PncGatewayTypeEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | PortPrototypeBlueprintInitValue | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | PositiveInteger | N/A, N/A | ARPositiveInteger, False | Class exists but not documented |
| + EXTRA | PositiveUnlimitedInteger | N/A, N/A | ARPositiveInteger, False | Class exists but not documented |
| + EXTRA | RamBlockStatusControlEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | ReentrancyLevelEnum | N/A, N/A | Enum, False | Class exists but not documented |
| + EXTRA | RefType | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ReferrableSubtypesEnum | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | RegularExpression | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | ResumePosition | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | RevisionLabelString | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | SdClientConfig | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SdServerConfig | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ServiceDiagnosticRelevanceEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | SocketConnectionBundle | N/A, N/A | Referrable, False | Class exists but not documented |
| + EXTRA | SocketConnectionIpduIdentifier | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | String | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | SwDataDefPropsConditional | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SwImplPolicyEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | SwServiceImplPolicyEnum | N/A, N/A | str, False | Class exists but not documented |
| + EXTRA | TRefType | N/A, N/A | RefType, False | Class exists but not documented |
| + EXTRA | TimeValue | N/A, N/A | ARFloat, False | Class exists but not documented |
| + EXTRA | TransformerClassEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | UnlimitedInteger | N/A, N/A | Integer, False | Class exists but not documented |
| + EXTRA | VerbatimString | N/A, N/A | ARLiteral, False | Class exists but not documented |

## Legend

- ✓ MATCH: Class has correct parent and abstract status
- ✗ MISSING: Class documented but not found in source
- ⚠ MISMATCH: Class has wrong parent or abstract status
- + EXTRA: Class exists but not documented
