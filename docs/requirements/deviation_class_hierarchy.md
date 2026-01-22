# Class Hierarchy Deviation Report

This report shows deviations between the documented AUTOSAR M2 class hierarchy
and the actual Python implementation class hierarchy.

## Summary

- ✓ **Match**: 48 classes with correct hierarchy
- ✗ **Missing**: 347 classes documented but not found
- ⚠ **Hierarchy Mismatch**: 114 classes with wrong parent/abstract
- + **Extra**: 557 undocumented classes
- **Total Documented Classes**: 509
- **Total Deviations**: 1018

## Hierarchy Deviations Table

| Status | Class | Documented (Parent, Abstract) | Actual (Parent, Abstract) | Notes |
|--------|-------|-------------------------------|---------------------------|-------|
| ⚠ MISMATCH | ARElement | ARObject, True | PackageableElement, False | parent mismatch (expected ARObject, got PackageableElement), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | ARPackage | ARObject, False | Identifiable, False | parent mismatch (expected ARObject, got Identifiable) |
| ⚠ MISMATCH | AUTOSAR | ARObject, False | AbstractAUTOSAR, False | parent mismatch (expected ARObject, got AbstractAUTOSAR) |
| ⚠ MISMATCH | AbstractCanCluster | ARElement, True | CommunicationCluster, False | parent mismatch (expected ARElement, got CommunicationCluster), abstract mismatch (expected True, got False) |
| ✗ MISSING | AbstractEnumerationValueVariationPoint | ARObject, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | AbstractImplementationDataType | ARElement, True | AutosarDataType, False | parent mismatch (expected ARElement, got AutosarDataType), abstract mismatch (expected True, got False) |
| ✗ MISSING | AbstractMultiplicityRestriction | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AbstractNumericalVariationPoint | ARObject, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | AbstractRequiredPortPrototype | ARObject, True | PortPrototype, False | parent mismatch (expected ARObject, got PortPrototype), abstract mismatch (expected True, got False) |
| ✗ MISSING | AbstractValueRestriction | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AbstractVariationRestriction | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AclObjectSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AclOperation | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AclPermission | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AclRole | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AliasNameSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | Annotation | ARObject, False | GeneralAnnotation, False | parent mismatch (expected ARObject, got GeneralAnnotation) |
| ⚠ MISMATCH | ApplicationArrayDataType | ARElement, False | ApplicationCompositeDataType, False | parent mismatch (expected ARElement, got ApplicationCompositeDataType) |
| ⚠ MISMATCH | ApplicationCompositeDataType | ARElement, True | ApplicationDataType, False | parent mismatch (expected ARElement, got ApplicationDataType), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | ApplicationDataType | ARElement, True | AutosarDataType, False | parent mismatch (expected ARElement, got AutosarDataType), abstract mismatch (expected True, got False) |
| ✗ MISSING | ApplicationPartition | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ApplicationPrimitiveDataType | ARElement, False | ApplicationDataType, False | parent mismatch (expected ARElement, got ApplicationDataType) |
| ⚠ MISMATCH | ApplicationRecordDataType | ARElement, False | ApplicationCompositeDataType, False | parent mismatch (expected ARElement, got ApplicationCompositeDataType) |
| ⚠ MISMATCH | ApplicationSwComponentType | ARElement, False | AtomicSwComponentType, False | parent mismatch (expected ARElement, got AtomicSwComponentType) |
| ✗ MISSING | Area | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | AssemblySwConnector | ARObject, False | SwConnector, False | parent mismatch (expected ARObject, got SwConnector) |
| ✗ MISSING | AtpBlueprint | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AtpBlueprintable | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AtpClassifier | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | AtpDefinition | ARObject, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | AtpFeature | ARObject, True | Identifiable, False | parent mismatch (expected ARObject, got Identifiable), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AtpInstanceRef | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AtpPrototype | ARObject, True | AtpFeature, False | parent mismatch (expected ARObject, got AtpFeature), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AtpStructureElement | ARObject, True | AtpFeature, False | parent mismatch (expected ARObject, got AtpFeature), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AtpType | ARObject, True | ARElement, False | parent mismatch (expected ARObject, got ARElement), abstract mismatch (expected True, got False) |
| ✗ MISSING | AttributeValueVariationPoint | ARObject, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | AutosarDataType | ARElement, True | AtpType, False | parent mismatch (expected ARElement, got AtpType), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | AutosarEngineeringObject | ARObject, False | EngineeringObject, False | parent mismatch (expected ARObject, got EngineeringObject) |
| ⚠ MISMATCH | BaseType | ARElement, True | ARElement, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | BlueprintGenerator | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BlueprintMappingSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BooleanValueVariationPoint | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Br | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BswEntryRelationshipSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | BswImplementation | ARElement, False | Implementation, False | parent mismatch (expected ARElement, got Implementation) |
| ⚠ MISMATCH | BswModuleEntity | ARObject, True | ExecutableEntity, False | parent mismatch (expected ARObject, got ExecutableEntity), abstract mismatch (expected True, got False) |
| ✗ MISSING | BuildAction | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BuildActionEntity | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BuildActionEnvironment | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BuildActionInvocator | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BuildActionIoElement | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BuildActionManifest | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | BuildEngineeringObject | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CalibrationParameterValueSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | CanCluster | ARElement, False | AbstractCanCluster, False | parent mismatch (expected ARElement, got AbstractCanCluster) |
| ✗ MISSING | Caption | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Chapter | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ChapterContent | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ChapterModel | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ChapterOrMsrQuery | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ClientIdDefinitionSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ClientServerInterface | ARElement, False | PortInterface, False | parent mismatch (expected ARElement, got PortInterface) |
| ⚠ MISMATCH | ClientServerOperation | ARObject, False | AtpFeature, False | parent mismatch (expected ARObject, got AtpFeature) |
| ⚠ MISMATCH | CollectableElement | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | Colspec | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | CommunicationCluster | ARElement, True | FibexElement, False | parent mismatch (expected ARElement, got FibexElement), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | Compiler | ARObject, False | Identifiable, False | parent mismatch (expected ARObject, got Identifiable) |
| ⚠ MISMATCH | CompositionSwComponentType | ARElement, False | SwComponentType, False | parent mismatch (expected ARElement, got SwComponentType) |
| ✗ MISSING | ConditionByFormula | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ConstantSpecificationMappingSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ContainerIPdu | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterBinaryManifestDescriptor | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterMappingSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSoftwareClusterResourcePool | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSwClusterResourceToDiagDataElemMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSwClusterResourceToDiagFunctionIdMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSwClusterToDiagEventMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CpSwClusterToDiagRoutineSubfunctionMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CryptoEllipticCurveProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CryptoServiceCertificate | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CryptoServiceKey | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CryptoServicePrimitive | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CryptoServiceQueue | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | CryptoSignatureScheme | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | DataConstr | ARElement, False | Identifiable, False | parent mismatch (expected ARElement, got Identifiable) |
| ⚠ MISMATCH | DataInterface | ARElement, True | PortInterface, False | parent mismatch (expected ARElement, got PortInterface), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | DcmIPdu | ARElement, False | IPdu, False | parent mismatch (expected ARElement, got IPdu) |
| ✗ MISSING | DdsCpConfig | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DefItem | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DefList | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | Describable | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | DiagnosticAbstractAliasEvent | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAbstractDataIdentifier | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAccessPermission | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAging | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAuthRole | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAuthTransmitCertificate | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAuthTransmitCertificateMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAuthentication | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAuthenticationClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticAuthenticationConfiguration | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticClearDiagnosticInformation | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticClearDiagnosticInformationClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticClearResetEmissionRelatedInfo | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticClearResetEmissionRelatedInfoClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticComControl | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticComControlClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticCommonElement | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticCondition | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticConditionGroup | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticContributionSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticControlDTCSetting | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticControlDTCSettingClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticCustomServiceClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticCustomServiceInstance | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDataByIdentifier | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDataIdentifier | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDataIdentifierSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDataTransfer | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDataTransferClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDeAuthentication | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDebounceAlgorithmProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDemProvidedDataMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDynamicDataIdentifier | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDynamicallyDefineDataIdentifier | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticDynamicallyDefineDataIdentifierClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEcuInstanceProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEcuReset | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEcuResetClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnableCondition | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnableConditionGroup | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnableConditionPortMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEnvironmentalCondition | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEvent | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventPortMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventToDebounceAlgorithmMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventToEnableConditionGroupMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventToOperationCycleMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventToSecurityEventMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventToStorageConditionGroupMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventToTroubleCodeJ1939Mapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticEventToTroubleCodeUdsMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticExtendedDataRecord | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFimAliasEvent | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFimAliasEventGroup | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFimAliasEventGroupMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFimAliasEventMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFimEventGroup | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFimFunctionMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFreezeFrame | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFunctionIdentifier | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticFunctionIdentifierInhibit | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIOControl | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIndicator | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticInfoType | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticInhibitSourceEventMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIoControlClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIumpr | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIumprDenominatorGroup | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIumprGroup | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticIumprToFunctionIdentifierMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939ExpandedFreezeFrame | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939FreezeFrame | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939Node | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939Spn | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939SpnMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticJ1939SwMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMapping | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMasterToSlaveEventMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMeasurementIdentifier | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryAddressableRangeAccess | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryByAddress | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryDestination | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryDestinationPrimary | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryDestinationUserDefined | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticMemoryIdentifier | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticOperationCycle | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticOperationCyclePortMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticParameterIdentifier | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticPowertrainFreezeFrame | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticProofOfOwnership | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticProtocol | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadDTCInformation | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadDTCInformationClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadDataByIdentifier | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadDataByIdentifierClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadDataByPeriodicID | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadDataByPeriodicIDClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadMemoryByAddress | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadMemoryByAddressClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadScalingDataByIdentifier | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticReadScalingDataByIdentifierClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestControlOfOnBoardDevice | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestControlOfOnBoardDeviceClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestCurrentPowertrainData | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestCurrentPowertrainDataClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestDownload | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestDownloadClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestEmissionRelatedDTC | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestEmissionRelatedDTCClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestEmissionRelatedDTCPermanentStatus | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestEmissionRelatedDTCPermanentStatusClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestFileTransfer | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestFileTransferClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestOnBoardMonitoringTestResults | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestOnBoardMonitoringTestResultsClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestPowertrainFreezeFrameData | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestPowertrainFreezeFrameDataClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestUpload | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestUploadClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestVehicleInfo | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRequestVehicleInfoClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticResponseOnEvent | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticResponseOnEventClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRoutine | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRoutineControl | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticRoutineControlClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSecureCodingMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSecurityAccess | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSecurityAccessClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSecurityEventReportingModeMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSecurityLevel | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticServiceClass | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticServiceDataMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticServiceInstance | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticServiceSwMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSession | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSessionControl | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSessionControlClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticStorageCondition | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticStorageConditionGroup | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticStorageConditionPortMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticSwMapping | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTestResult | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTestRoutineIdentifier | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTransferExit | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTransferExitClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCode | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeGroup | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeJ1939 | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeObd | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeUds | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticTroubleCodeUdsToTroubleCodeObdMapping | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticVerifyCertificateBidirectional | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticVerifyCertificateUnidirectional | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticWriteDataByIdentifier | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticWriteDataByIdentifierClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticWriteMemoryByAddress | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DiagnosticWriteMemoryByAddressClass | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DltContext | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | DltEcu | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | DocumentViewSelectable | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | Documentation | ARElement, False | ARObject, False | parent mismatch (expected ARElement, got ARObject) |
| ✗ MISSING | DocumentationContext | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | E2EProfileCompatibilityProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | EcucContainerValue | ARObject, False | ARElement, False | parent mismatch (expected ARObject, got ARElement) |
| ⚠ MISMATCH | EcucDefinitionCollection | ARElement, False | ARObject, False | parent mismatch (expected ARElement, got ARObject) |
| ⚠ MISMATCH | EcucDefinitionElement | ARObject, True | Identifiable, False | parent mismatch (expected ARObject, got Identifiable), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | EcucDestinationUriDefSet | ARElement, False | Identifiable, False | parent mismatch (expected ARElement, got Identifiable) |
| ⚠ MISMATCH | EcucModuleDef | ARElement, False | EcucDefinitionElement, False | parent mismatch (expected ARElement, got EcucDefinitionElement) |
| ⚠ MISMATCH | EcucNumericalParamValue | ARObject, False | EcucParameterValue, False | parent mismatch (expected ARObject, got EcucParameterValue) |
| ⚠ MISMATCH | EcucParameterValue | ARObject, True | EcucIndexableValue, False | parent mismatch (expected ARObject, got EcucIndexableValue), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | EcucReferenceDef | ARObject, False | EcucAbstractInternalReferenceDef, False | parent mismatch (expected ARObject, got EcucAbstractInternalReferenceDef) |
| ⚠ MISMATCH | EcucReferenceValue | ARObject, False | EcucAbstractReferenceValue, False | parent mismatch (expected ARObject, got EcucAbstractReferenceValue) |
| ⚠ MISMATCH | EcucTextualParamValue | ARObject, False | EcucParameterValue, False | parent mismatch (expected ARObject, got EcucParameterValue) |
| ✗ MISSING | EmphasisText | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | EndToEndProtectionSet | ARElement, False | Identifiable, False | parent mismatch (expected ARElement, got Identifiable) |
| ⚠ MISMATCH | EngineeringObject | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | Entry | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EnumerationMappingEntry | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EnumerationMappingTable | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EthIpProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EthTcpIpIcmpProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | EthTcpIpProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | EthernetCluster | ARElement, False | CommunicationCluster, False | parent mismatch (expected ARElement, got CommunicationCluster) |
| ✗ MISSING | EvaluatedVariantSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FMFeature | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FMFeatureModel | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | FibexElement | ARObject, True | Identifiable, False | parent mismatch (expected ARObject, got Identifiable), abstract mismatch (expected True, got False) |
| ✗ MISSING | FirewallRule | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | FlexrayCluster | ARElement, False | CommunicationCluster, False | parent mismatch (expected ARElement, got CommunicationCluster) |
| ⚠ MISMATCH | FlexrayCommunicationController | ARObject, False | CommunicationController, False | parent mismatch (expected ARObject, got CommunicationController) |
| ✗ MISSING | FloatValueVariationPoint | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | FormulaExpression | ARObject, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | GeneralAnnotation | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | GeneralPurposeConnection | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | GeneralPurposeIPdu | ARElement, False | IPdu, False | parent mismatch (expected ARElement, got IPdu) |
| ⚠ MISMATCH | GeneralPurposePdu | ARElement, False | Pdu, False | parent mismatch (expected ARElement, got Pdu) |
| ✗ MISSING | GenericModelReference | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | Graphic | ARObject, False | EngineeringObject, False | parent mismatch (expected ARObject, got EngineeringObject) |
| ⚠ MISMATCH | HwElement | ARElement, False | HwDescriptionEntity, False | parent mismatch (expected ARElement, got HwDescriptionEntity) |
| ✗ MISSING | IEEE1722TpAafConnection | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpAcfConnection | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpAvConnection | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpConnection | ARElement, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpCrfConnection | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpIidcConnection | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IEEE1722TpRvfConnection | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IPSecConfigProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IPv6ExtHeaderFilterSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ISignalGroup | ARElement, False | FibexElement, False | parent mismatch (expected ARElement, got FibexElement) |
| ⚠ MISMATCH | ISignalIPdu | ARElement, False | IPdu, False | parent mismatch (expected ARElement, got IPdu) |
| ⚠ MISMATCH | Identifiable | ARObject, True | MultilanguageReferrable, False | parent mismatch (expected ARObject, got MultilanguageReferrable), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | Implementation | ARElement, True | PackageableElement, False | parent mismatch (expected ARElement, got PackageableElement), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | ImplementationDataType | ARElement, False | AbstractImplementationDataType, False | parent mismatch (expected ARElement, got AbstractImplementationDataType) |
| ⚠ MISMATCH | ImplementationDataTypeElement | ARObject, False | AbstractImplementationDataTypeElement, False | parent mismatch (expected ARObject, got AbstractImplementationDataTypeElement) |
| ✗ MISSING | IndentSample | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IndexEntry | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | IntegerValueVariationPoint | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | InternalBehavior | ARObject, True | Identifiable, False | parent mismatch (expected ARObject, got Identifiable), abstract mismatch (expected True, got False) |
| ✗ MISSING | InterpolationRoutineMappingSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | Item | ARObject, False | Paginateable, False | parent mismatch (expected ARObject, got Paginateable) |
| ✗ MISSING | J1939Cluster | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | J1939ControllerApplication | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | J1939DcmIPdu | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | Keyword | ARObject, False | Identifiable, False | parent mismatch (expected ARObject, got Identifiable) |
| ⚠ MISMATCH | LGraphic | ARObject, False | LanguageSpecific, False | parent mismatch (expected ARObject, got LanguageSpecific) |
| ⚠ MISMATCH | LLongName | ARObject, False | LanguageSpecific, False | parent mismatch (expected ARObject, got LanguageSpecific) |
| ⚠ MISMATCH | LOverviewParagraph | ARObject, False | LanguageSpecific, False | parent mismatch (expected ARObject, got LanguageSpecific) |
| ⚠ MISMATCH | LParagraph | ARObject, False | LanguageSpecific, False | parent mismatch (expected ARObject, got LanguageSpecific) |
| ⚠ MISMATCH | LPlainText | ARObject, False | LanguageSpecific, False | parent mismatch (expected ARObject, got LanguageSpecific) |
| ✗ MISSING | LVerbatim | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | LabeledItem | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | LabeledList | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | LanguageSpecific | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | LifeCycleState | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | LifeCycleStateDefinitionGroup | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | LimitValueVariationPoint | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | LinCluster | ARElement, False | CommunicationCluster, False | parent mismatch (expected ARElement, got CommunicationCluster) |
| ✗ MISSING | List | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MacSecGlobalKayProps | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MacSecParticipantSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | McFunction | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | McFunctionDataRefSet | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | McGroup | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MixedContentForLongName | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MixedContentForOverviewParagraph | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MixedContentForParagraph | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MixedContentForPlainText | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MixedContentForUnitNames | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MixedContentForVerbatim | ARObject, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | MlFigure | ARObject, False | Paginateable, False | parent mismatch (expected ARObject, got Paginateable) |
| ⚠ MISMATCH | ModeDeclarationGroup | ARElement, False | Identifiable, False | parent mismatch (expected ARElement, got Identifiable) |
| ⚠ MISMATCH | ModeSwitchInterface | ARElement, False | PortInterface, False | parent mismatch (expected ARElement, got PortInterface) |
| ✗ MISSING | MsrQueryArg | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MsrQueryChapter | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MsrQueryP1 | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MsrQueryP2 | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MsrQueryProps | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MsrQueryResultChapter | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MsrQueryResultTopic1 | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MsrQueryTopic1 | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MultiLanguageVerbatim | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | MultidimensionalTime | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | MultilanguageReferrable | ARObject, True | Referrable, False | parent mismatch (expected ARObject, got Referrable), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | MultiplexedIPdu | ARElement, False | IPdu, False | parent mismatch (expected ARElement, got IPdu) |
| ⚠ MISMATCH | NPdu | ARElement, False | IPdu, False | parent mismatch (expected ARElement, got IPdu) |
| ⚠ MISMATCH | NmConfig | ARElement, False | FibexElement, False | parent mismatch (expected ARElement, got FibexElement) |
| ⚠ MISMATCH | NmPdu | ARElement, False | Pdu, False | parent mismatch (expected ARElement, got Pdu) |
| ✗ MISSING | Note | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | NvBlockSwComponentType | ARElement, False | AtomicSwComponentType, False | parent mismatch (expected ARElement, got AtomicSwComponentType) |
| ⚠ MISMATCH | NvDataInterface | ARElement, False | DataInterface, False | parent mismatch (expected ARElement, got DataInterface) |
| ✗ MISSING | OsTaskProxy | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | PackageableElement | ARObject, True | Identifiable, False | parent mismatch (expected ARObject, got Identifiable), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | Paginateable | ARObject, True | DocumentViewSelectable, False | parent mismatch (expected ARObject, got DocumentViewSelectable), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | ParameterDataPrototype | ARObject, False | AutosarDataPrototype, False | parent mismatch (expected ARObject, got AutosarDataPrototype) |
| ⚠ MISMATCH | ParameterInterface | ARElement, False | DataInterface, False | parent mismatch (expected ARElement, got DataInterface) |
| ✗ MISSING | ParameterSwComponentType | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | Pdu | ARElement, True | FibexElement, False | parent mismatch (expected ARElement, got FibexElement), abstract mismatch (expected True, got False) |
| ✗ MISSING | PhysicalDimensionMappingSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | PortInterface | ARElement, True | AtpType, False | parent mismatch (expected ARElement, got AtpType), abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | PortPrototype | ARObject, True | Identifiable, False | parent mismatch (expected ARObject, got Identifiable), abstract mismatch (expected True, got False) |
| ✗ MISSING | PositiveIntegerValueVariationPoint | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | PostBuildVariantCondition | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | PostBuildVariantCriterion | ARElement, False | ARObject, False | parent mismatch (expected ARElement, got ARObject) |
| ✗ MISSING | PostBuildVariantCriterionValueSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | PredefinedChapter | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | PredefinedVariant | ARElement, False | ARObject, False | parent mismatch (expected ARElement, got ARObject) |
| ✗ MISSING | Prms | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | RPortInCompositionInstanceRef | ARObject, False | PortInCompositionTypeInstanceRef, False | parent mismatch (expected ARObject, got PortInCompositionTypeInstanceRef) |
| ⚠ MISMATCH | RPortPrototype | ARObject, False | AbstractRequiredPortPrototype, False | parent mismatch (expected ARObject, got AbstractRequiredPortPrototype) |
| ✗ MISSING | RapidPrototypingScenario | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | Referrable | ARObject, True | ARObject, False | abstract mismatch (expected True, got False) |
| ✗ MISSING | Row | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | RunnableEntity | ARObject, False | ExecutableEntity, False | parent mismatch (expected ARObject, got ExecutableEntity) |
| ✗ MISSING | Sdf | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgAbstractForeignReference | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgAbstractPrimitiveAttribute | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgAggregationWithVariation | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgAttribute | ARObject, True | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SdgCaption | ARObject, False | MultilanguageReferrable, False | parent mismatch (expected ARObject, got MultilanguageReferrable) |
| ✗ MISSING | SdgClass | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgContents | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgDef | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgElementWithGid | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgForeignReference | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgForeignReferenceWithVariation | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgPrimitiveAttribute | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgPrimitiveAttributeWithVariation | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SdgReference | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SecuredIPdu | ARElement, False | IPdu, False | parent mismatch (expected ARElement, got IPdu) |
| ✗ MISSING | SecurityEventDefinition | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | ServiceProxySwComponentType | ARElement, False | AtomicSwComponentType, False | parent mismatch (expected ARElement, got AtomicSwComponentType) |
| ⚠ MISMATCH | ServiceSwComponentType | ARElement, False | AtomicSwComponentType, False | parent mismatch (expected ARElement, got AtomicSwComponentType) |
| ✗ MISSING | ShortNameFragment | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SignalServiceTranslationPropsSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SingleLanguageLongName | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SingleLanguageReferrable | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SlOverviewParagraph | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SlParagraph | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SocketConnectionIpduIdentifierSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SomeipSdClientEventGroupTimingConfig | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SomeipSdClientServiceInstanceConfig | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SomeipSdServerEventGroupTimingConfig | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SomeipSdServerServiceInstanceConfig | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | StateDependentFirewall | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Std | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | StructuredReq | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SwAddrMethod | ARElement, False | Identifiable, False | parent mismatch (expected ARElement, got Identifiable) |
| ✗ MISSING | SwAxisType | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SwBaseType | ARElement, False | BaseType, False | parent mismatch (expected ARElement, got BaseType) |
| ⚠ MISMATCH | SwComponentPrototype | ARObject, False | Identifiable, False | parent mismatch (expected ARObject, got Identifiable) |
| ⚠ MISMATCH | SwComponentType | ARElement, True | ARElement, False | abstract mismatch (expected True, got False) |
| ⚠ MISMATCH | SwServiceArg | ARObject, False | Identifiable, False | parent mismatch (expected ARObject, got Identifiable) |
| ⚠ MISMATCH | SwSystemconst | ARElement, False | ARObject, False | parent mismatch (expected ARElement, got ARObject) |
| ✗ MISSING | SwSystemconstDependentFormula | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | SwSystemconstValue | ARObject, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | SwSystemconstantValueSet | ARElement, False | ARObject, False | parent mismatch (expected ARElement, got ARObject) |
| ⚠ MISMATCH | SwcBswMapping | ARElement, False | Identifiable, False | parent mismatch (expected ARElement, got Identifiable) |
| ⚠ MISMATCH | SwcImplementation | ARElement, False | Implementation, False | parent mismatch (expected ARElement, got Implementation) |
| ⚠ MISMATCH | SwcInternalBehavior | ARObject, False | InternalBehavior, False | parent mismatch (expected ARObject, got InternalBehavior) |
| ✗ MISSING | Table | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TagWithOptionalValue | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Tbody | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TcpOptionFilterSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Tgroup | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TimeValueValueVariationPoint | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TlvDataIdDefinitionSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Topic1 | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TopicContent | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TopicContentOrMsrQuery | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TopicOrMsrQuery | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Traceable | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TraceableText | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TransformationPropsSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | TriggerInterface | ARElement, False | PortInterface, False | parent mismatch (expected ARElement, got PortInterface) |
| ✗ MISSING | Tt | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | TtcanCluster | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | UnlimitedIntegerValueVariationPoint | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | UserDefinedCluster | ARElement, False | Not Found, N/A | Class not found in source code |
| ⚠ MISMATCH | UserDefinedIPdu | ARElement, False | IPdu, False | parent mismatch (expected ARElement, got IPdu) |
| ⚠ MISMATCH | UserDefinedPdu | ARElement, False | Pdu, False | parent mismatch (expected ARElement, got Pdu) |
| ✗ MISSING | VariationPointProxy | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ViewMap | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | ViewMapSet | ARElement, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | WhitespaceControlled | ARObject, True | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Xdoc | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Xfile | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | Xref | ARObject, False | Not Found, N/A | Class not found in source code |
| ✗ MISSING | XrefTarget | ARObject, False | Not Found, N/A | Class not found in source code |

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
| + EXTRA | AbstractAccessPoint | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | AbstractCanCommunicationConnector | N/A, N/A | CommunicationConnector, False | Class exists but not documented |
| + EXTRA | AbstractCanCommunicationController | N/A, N/A | CommunicationController, False | Class exists but not documented |
| + EXTRA | AbstractCanCommunicationControllerAttributes | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | AbstractCanPhysicalChannel | N/A, N/A | PhysicalChannel, False | Class exists but not documented |
| + EXTRA | AbstractDoIpLogicAddressProps | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | AbstractEthernetFrame | N/A, N/A | Frame, False | Class exists but not documented |
| + EXTRA | AbstractEvent | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | AbstractImplementationDataTypeElement | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | AbstractProvidedPortPrototype | N/A, N/A | PortPrototype, False | Class exists but not documented |
| + EXTRA | AbstractServiceInstance | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | AppOsTaskProxyToEcuTaskProxyMapping | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | ApplicationArrayElement | N/A, N/A | ApplicationCompositeElementDataPrototype, False | Class exists but not documented |
| + EXTRA | ApplicationCompositeElementDataPrototype | N/A, N/A | DataPrototype, False | Class exists but not documented |
| + EXTRA | ApplicationCompositeElementInPortInterfaceInstanceRef | N/A, N/A | AtpInstanceRef, False | Class exists but not documented |
| + EXTRA | ApplicationEndpoint | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | ApplicationEntry | N/A, N/A | ScheduleTableEntry, False | Class exists but not documented |
| + EXTRA | ApplicationError | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | ApplicationPartitionToEcuPartitionMapping | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | ApplicationRecordElement | N/A, N/A | ApplicationCompositeElementDataPrototype, False | Class exists but not documented |
| + EXTRA | ApplicationValueSpecification | N/A, N/A | CompositeRuleBasedValueArgument, False | Class exists but not documented |
| + EXTRA | ArVariableInImplementationDataInstanceRef | N/A, N/A | AtpInstanceRef, False | Class exists but not documented |
| + EXTRA | ArgumentDataPrototype | N/A, N/A | AutosarDataPrototype, False | Class exists but not documented |
| + EXTRA | ArgumentDirectionEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | ArrayValueSpecification | N/A, N/A | ValueSpecification, False | Class exists but not documented |
| + EXTRA | AsynchronousServerCallPoint | N/A, N/A | ServerCallPoint, False | Class exists but not documented |
| + EXTRA | AsynchronousServerCallResultPoint | N/A, N/A | AbstractAccessPoint, False | Class exists but not documented |
| + EXTRA | AsynchronousServerCallReturnsEvent | N/A, N/A | RTEEvent, False | Class exists but not documented |
| + EXTRA | AtomicSwComponentType | N/A, N/A | SwComponentType, False | Class exists but not documented |
| + EXTRA | AutoCollectEnum | N/A, N/A | Enum, False | Class exists but not documented |
| + EXTRA | AutosarDataPrototype | N/A, N/A | DataPrototype, False | Class exists but not documented |
| + EXTRA | AutosarParameterRef | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | AutosarVariableRef | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | BackgroundEvent | N/A, N/A | RTEEvent, False | Class exists but not documented |
| + EXTRA | BaseTypeDefinition | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | BaseTypeDirectDefinition | N/A, N/A | BaseTypeDefinition, False | Class exists but not documented |
| + EXTRA | Boolean | N/A, N/A | ARBoolean, False | Class exists but not documented |
| + EXTRA | BswApiOptions | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | BswAsynchronousServerCallPoint | N/A, N/A | BswModuleCallPoint, False | Class exists but not documented |
| + EXTRA | BswAsynchronousServerCallResultPoint | N/A, N/A | BswModuleCallPoint, False | Class exists but not documented |
| + EXTRA | BswBackgroundEvent | N/A, N/A | BswScheduleEvent, False | Class exists but not documented |
| + EXTRA | BswCallType | N/A, N/A | str, False | Class exists but not documented |
| + EXTRA | BswCalledEntity | N/A, N/A | BswModuleEntity, False | Class exists but not documented |
| + EXTRA | BswDataReceivedEvent | N/A, N/A | BswScheduleEvent, False | Class exists but not documented |
| + EXTRA | BswDataReceptionPolicy | N/A, N/A | BswApiOptions, False | Class exists but not documented |
| + EXTRA | BswDirectCallPoint | N/A, N/A | BswModuleCallPoint, False | Class exists but not documented |
| + EXTRA | BswDistinguishedPartition | N/A, N/A | Referrable, False | Class exists but not documented |
| + EXTRA | BswEntryKindEnum | N/A, N/A | str, False | Class exists but not documented |
| + EXTRA | BswEvent | N/A, N/A | AbstractEvent, False | Class exists but not documented |
| + EXTRA | BswExecutionContext | N/A, N/A | str, False | Class exists but not documented |
| + EXTRA | BswExternalTriggerOccurredEvent | N/A, N/A | BswScheduleEvent, False | Class exists but not documented |
| + EXTRA | BswInternalBehavior | N/A, N/A | InternalBehavior, False | Class exists but not documented |
| + EXTRA | BswInternalTriggerOccurredEvent | N/A, N/A | BswScheduleEvent, False | Class exists but not documented |
| + EXTRA | BswInternalTriggeringPoint | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | BswInterruptCategory | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | BswInterruptEntity | N/A, N/A | BswModuleEntity, False | Class exists but not documented |
| + EXTRA | BswModeSenderPolicy | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | BswModeSwitchAckRequest | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | BswModeSwitchEvent | N/A, N/A | BswScheduleEvent, False | Class exists but not documented |
| + EXTRA | BswModeSwitchedAckEvent | N/A, N/A | BswScheduleEvent, False | Class exists but not documented |
| + EXTRA | BswModuleCallPoint | N/A, N/A | Referrable, False | Class exists but not documented |
| + EXTRA | BswModuleClientServerEntry | N/A, N/A | Referrable, False | Class exists but not documented |
| + EXTRA | BswModuleDependency | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | BswOperationInvokedEvent | N/A, N/A | BswEvent, False | Class exists but not documented |
| + EXTRA | BswOsTaskExecutionEvent | N/A, N/A | BswScheduleEvent, False | Class exists but not documented |
| + EXTRA | BswQueuedDataReceptionPolicy | N/A, N/A | BswDataReceptionPolicy, False | Class exists but not documented |
| + EXTRA | BswSchedulableEntity | N/A, N/A | BswModuleEntity, False | Class exists but not documented |
| + EXTRA | BswScheduleEvent | N/A, N/A | BswEvent, False | Class exists but not documented |
| + EXTRA | BswSynchronousServerCallPoint | N/A, N/A | BswModuleCallPoint, False | Class exists but not documented |
| + EXTRA | BswTimingEvent | N/A, N/A | BswScheduleEvent, False | Class exists but not documented |
| + EXTRA | BswVariableAccess | N/A, N/A | Referrable, False | Class exists but not documented |
| + EXTRA | BufferProperties | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | BusspecificNmEcu | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ByteOrderEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | CIdentifier | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | CanClusterBusOffRecovery | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CanCommunicationConnector | N/A, N/A | AbstractCanCommunicationConnector, False | Class exists but not documented |
| + EXTRA | CanCommunicationController | N/A, N/A | AbstractCanCommunicationController, False | Class exists but not documented |
| + EXTRA | CanControllerConfigurationRequirements | N/A, N/A | AbstractCanCommunicationControllerAttributes, False | Class exists but not documented |
| + EXTRA | CanControllerFdConfiguration | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CanControllerFdConfigurationRequirements | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CanControllerXlConfiguration | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CanControllerXlConfigurationRequirements | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CanFrame | N/A, N/A | Frame, False | Class exists but not documented |
| + EXTRA | CanFrameTriggering | N/A, N/A | FrameTriggering, False | Class exists but not documented |
| + EXTRA | CanNmCluster | N/A, N/A | NmCluster, False | Class exists but not documented |
| + EXTRA | CanNmClusterCoupling | N/A, N/A | NmClusterCoupling, False | Class exists but not documented |
| + EXTRA | CanNmEcu | N/A, N/A | BusspecificNmEcu, False | Class exists but not documented |
| + EXTRA | CanNmNode | N/A, N/A | NmNode, False | Class exists but not documented |
| + EXTRA | CanPhysicalChannel | N/A, N/A | AbstractCanPhysicalChannel, False | Class exists but not documented |
| + EXTRA | CanTpAddress | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | CanTpChannel | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | CanTpConfig | N/A, N/A | TpConfig, False | Class exists but not documented |
| + EXTRA | CanTpConnection | N/A, N/A | TpConnection, False | Class exists but not documented |
| + EXTRA | CanTpEcu | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CanTpNode | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | CategoryString | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | ClientComSpec | N/A, N/A | RPortComSpec, False | Class exists but not documented |
| + EXTRA | ClientServerApplicationErrorMapping | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ClientServerInterfaceMapping | N/A, N/A | PortInterfaceMapping, False | Class exists but not documented |
| + EXTRA | ClientServerOperationMapping | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | Code | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | ComManagementMapping | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | CommConnectorPort | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | CommunicationConnector | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | CommunicationController | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | CommunicationCycle | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CommunicationDirectionType | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | ComplexDeviceDriverSwComponentType | N/A, N/A | AtomicSwComponentType, False | Class exists but not documented |
| + EXTRA | ComponentInSystemInstanceRef | N/A, N/A | AtpInstanceRef, False | Class exists but not documented |
| + EXTRA | CompositeNetworkRepresentation | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CompositeRuleBasedValueArgument | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CompositeValueSpecification | N/A, N/A | ValueSpecification, False | Class exists but not documented |
| + EXTRA | Compu | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CompuConst | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CompuConstContent | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CompuConstFormulaContent | N/A, N/A | CompuConstContent, False | Class exists but not documented |
| + EXTRA | CompuConstNumericContent | N/A, N/A | CompuConstContent, False | Class exists but not documented |
| + EXTRA | CompuConstTextContent | N/A, N/A | CompuConstContent, False | Class exists but not documented |
| + EXTRA | CompuContent | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CompuNominatorDenominator | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CompuRationalCoeffs | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CompuScale | N/A, N/A | Compu, False | Class exists but not documented |
| + EXTRA | CompuScaleConstantContents | N/A, N/A | CompuScaleContents, False | Class exists but not documented |
| + EXTRA | CompuScaleContents | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CompuScaleRationalFormula | N/A, N/A | CompuScaleContents, False | Class exists but not documented |
| + EXTRA | CompuScales | N/A, N/A | CompuContent, False | Class exists but not documented |
| + EXTRA | ConstantReference | N/A, N/A | ValueSpecification, False | Class exists but not documented |
| + EXTRA | ConsumedEventGroup | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | ConsumedServiceInstance | N/A, N/A | AbstractServiceInstance, False | Class exists but not documented |
| + EXTRA | ContainedIPduProps | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CouplingPort | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | CouplingPortDetails | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | CouplingPortFifo | N/A, N/A | CouplingPortStructuralElement, False | Class exists but not documented |
| + EXTRA | CouplingPortScheduler | N/A, N/A | CouplingPortStructuralElement, False | Class exists but not documented |
| + EXTRA | CouplingPortStructuralElement | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | CryptoServiceMapping | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | CryptoServiceNeeds | N/A, N/A | ServiceNeeds, False | Class exists but not documented |
| + EXTRA | CycleCounter | N/A, N/A | CommunicationCycle, False | Class exists but not documented |
| + EXTRA | CycleRepetition | N/A, N/A | CommunicationCycle, False | Class exists but not documented |
| + EXTRA | CycleRepetitionType | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | CyclicTiming | N/A, N/A | Describable, False | Class exists but not documented |
| + EXTRA | DataConstrRule | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | DataFilter | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | DataFilterTypeEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DataIdModeEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DataMapping | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | DataPrototype | N/A, N/A | AtpPrototype, False | Class exists but not documented |
| + EXTRA | DataPrototypeMapping | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | DataReceiveErrorEvent | N/A, N/A | RTEEvent, False | Class exists but not documented |
| + EXTRA | DataReceivedEvent | N/A, N/A | RTEEvent, False | Class exists but not documented |
| + EXTRA | DataSendCompletedEvent | N/A, N/A | RTEEvent, False | Class exists but not documented |
| + EXTRA | DataTransformation | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | DataTransformationKindEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DataTypeMap | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | DataWriteCompletedEvent | N/A, N/A | RTEEvent, False | Class exists but not documented |
| + EXTRA | DateTime | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | DefaultValueElement | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | DelegationSwConnector | N/A, N/A | SwConnector, False | Class exists but not documented |
| + EXTRA | DependencyOnArtifact | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | DiagEventDebounceAlgorithm | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | DiagEventDebounceCounterBased | N/A, N/A | DiagEventDebounceAlgorithm, False | Class exists but not documented |
| + EXTRA | DiagEventDebounceMonitorInternal | N/A, N/A | DiagEventDebounceAlgorithm, False | Class exists but not documented |
| + EXTRA | DiagEventDebounceTimeBased | N/A, N/A | DiagEventDebounceAlgorithm, False | Class exists but not documented |
| + EXTRA | DiagRequirementIdString | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | DiagnosticAudienceEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DiagnosticCapabilityElement | N/A, N/A | ServiceNeeds, False | Class exists but not documented |
| + EXTRA | DiagnosticClearDtcNotificationEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DiagnosticCommunicationManagerNeeds | N/A, N/A | DiagnosticCapabilityElement, False | Class exists but not documented |
| + EXTRA | DiagnosticEventInfoNeeds | N/A, N/A | DiagnosticCapabilityElement, False | Class exists but not documented |
| + EXTRA | DiagnosticEventNeeds | N/A, N/A | DiagnosticCapabilityElement, False | Class exists but not documented |
| + EXTRA | DiagnosticProcessingStyleEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DiagnosticRoutineNeeds | N/A, N/A | DiagnosticCapabilityElement, False | Class exists but not documented |
| + EXTRA | DiagnosticRoutineTypeEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DiagnosticServiceRequestCallbackTypeEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DiagnosticValueAccessEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DiagnosticValueNeeds | N/A, N/A | DiagnosticCapabilityElement, False | Class exists but not documented |
| + EXTRA | DltUserNeeds | N/A, N/A | ServiceNeeds, False | Class exists but not documented |
| + EXTRA | DoIpEntity | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | DoIpLogicAddress | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | DoIpLogicTargetAddressProps | N/A, N/A | AbstractDoIpLogicAddressProps, False | Class exists but not documented |
| + EXTRA | DoIpLogicTesterAddressProps | N/A, N/A | AbstractDoIpLogicAddressProps, False | Class exists but not documented |
| + EXTRA | DoIpTpConfig | N/A, N/A | TpConfig, False | Class exists but not documented |
| + EXTRA | DoIpTpConnection | N/A, N/A | TpConnection, False | Class exists but not documented |
| + EXTRA | DtcFormatTypeEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DtcKindEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | DtcStatusChangeNotificationNeeds | N/A, N/A | DiagnosticCapabilityElement, False | Class exists but not documented |
| + EXTRA | DynamicPart | N/A, N/A | MultiplexedPart, False | Class exists but not documented |
| + EXTRA | DynamicPartAlternative | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ECUMapping | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | EOCExecutableEntityRef | N/A, N/A | EOCExecutableEntityRefAbstract, False | Class exists but not documented |
| + EXTRA | EOCExecutableEntityRefAbstract | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | EcuAbstractionSwComponentType | N/A, N/A | AtomicSwComponentType, False | Class exists but not documented |
| + EXTRA | EcuInstance | N/A, N/A | FibexElement, False | Class exists but not documented |
| + EXTRA | EcuStateMgrUserNeeds | N/A, N/A | ServiceNeeds, False | Class exists but not documented |
| + EXTRA | EcucAbstractConfigurationClass | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | EcucAbstractExternalReferenceDef | N/A, N/A | EcucAbstractReferenceDef, False | Class exists but not documented |
| + EXTRA | EcucAbstractInternalReferenceDef | N/A, N/A | EcucAbstractReferenceDef, False | Class exists but not documented |
| + EXTRA | EcucAbstractReferenceDef | N/A, N/A | EcucCommonAttributes, False | Class exists but not documented |
| + EXTRA | EcucAbstractReferenceValue | N/A, N/A | EcucIndexableValue, False | Class exists but not documented |
| + EXTRA | EcucAbstractStringParamDef | N/A, N/A | EcucParameterDef, False | Class exists but not documented |
| + EXTRA | EcucAddInfoParamDef | N/A, N/A | EcucParameterDef, False | Class exists but not documented |
| + EXTRA | EcucAddInfoParamValue | N/A, N/A | EcucParameterValue, False | Class exists but not documented |
| + EXTRA | EcucBooleanParamDef | N/A, N/A | EcucParameterDef, False | Class exists but not documented |
| + EXTRA | EcucChoiceContainerDef | N/A, N/A | EcucContainerDef, False | Class exists but not documented |
| + EXTRA | EcucChoiceReferenceDef | N/A, N/A | EcucAbstractInternalReferenceDef, False | Class exists but not documented |
| + EXTRA | EcucCommonAttributes | N/A, N/A | EcucDefinitionElement, False | Class exists but not documented |
| + EXTRA | EcucConditionFormula | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | EcucConditionSpecification | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | EcucConfigurationClassEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | EcucConfigurationVariantEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | EcucContainerDef | N/A, N/A | EcucDefinitionElement, False | Class exists but not documented |
| + EXTRA | EcucDerivationSpecification | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | EcucDestinationUriDef | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | EcucDestinationUriDefRefType | N/A, N/A | RefType, False | Class exists but not documented |
| + EXTRA | EcucDestinationUriPolicy | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | EcucEnumerationLiteralDef | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | EcucEnumerationParamDef | N/A, N/A | EcucParameterDef, False | Class exists but not documented |
| + EXTRA | EcucFloatParamDef | N/A, N/A | EcucParameterDef, False | Class exists but not documented |
| + EXTRA | EcucForeignReferenceDef | N/A, N/A | EcucAbstractExternalReferenceDef, False | Class exists but not documented |
| + EXTRA | EcucFunctionNameDef | N/A, N/A | EcucAbstractStringParamDef, False | Class exists but not documented |
| + EXTRA | EcucIndexableValue | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | EcucInstanceReferenceDef | N/A, N/A | EcucAbstractExternalReferenceDef, False | Class exists but not documented |
| + EXTRA | EcucInstanceReferenceValue | N/A, N/A | EcucAbstractReferenceValue, False | Class exists but not documented |
| + EXTRA | EcucIntegerParamDef | N/A, N/A | EcucParameterDef, False | Class exists but not documented |
| + EXTRA | EcucLinkerSymbolDef | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | EcucMultilineStringParamDef | N/A, N/A | EcucAbstractStringParamDef, False | Class exists but not documented |
| + EXTRA | EcucMultiplicityConfigurationClass | N/A, N/A | EcucAbstractConfigurationClass, False | Class exists but not documented |
| + EXTRA | EcucParamConfContainerDef | N/A, N/A | None, False | Class exists but not documented |
| + EXTRA | EcucParameterDef | N/A, N/A | EcucCommonAttributes, False | Class exists but not documented |
| + EXTRA | EcucParameterDerivationFormula | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | EcucQuery | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | EcucQueryExpression | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | EcucScopeEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | EcucStringParamDef | N/A, N/A | EcucAbstractStringParamDef, False | Class exists but not documented |
| + EXTRA | EcucSymbolicNameReferenceDef | N/A, N/A | EcucAbstractInternalReferenceDef, False | Class exists but not documented |
| + EXTRA | EcucUriReferenceDef | N/A, N/A | EcucAbstractInternalReferenceDef, False | Class exists but not documented |
| + EXTRA | EcucValidationCondition | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | EcucValueCollection | N/A, N/A | ARElement, False | Class exists but not documented |
| + EXTRA | EcucValueConfigurationClass | N/A, N/A | EcucAbstractConfigurationClass, False | Class exists but not documented |
| + EXTRA | EndToEndDescription | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | EndToEndProfileBehaviorEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | EndToEndProtection | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | EndToEndProtectionISignalIPdu | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | EndToEndProtectionVariablePrototype | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | EndToEndTransformationComSpecProps | N/A, N/A | TransformationComSpecProps, False | Class exists but not documented |
| + EXTRA | EndToEndTransformationDescription | N/A, N/A | TransformationDescription, False | Class exists but not documented |
| + EXTRA | EndToEndTransformationISignalProps | N/A, N/A | TransformationISignalProps, False | Class exists but not documented |
| + EXTRA | EthernetCommunicationConnector | N/A, N/A | CommunicationConnector, False | Class exists but not documented |
| + EXTRA | EthernetCommunicationController | N/A, N/A | CommunicationController, False | Class exists but not documented |
| + EXTRA | EthernetPhysicalChannel | N/A, N/A | PhysicalChannel, False | Class exists but not documented |
| + EXTRA | EthernetPriorityRegeneration | N/A, N/A | Referrable, False | Class exists but not documented |
| + EXTRA | EventControlledTiming | N/A, N/A | Describable, False | Class exists but not documented |
| + EXTRA | EventHandler | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | ExclusiveArea | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | ExecutableEntity | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | ExecutionOrderConstraint | N/A, N/A | TimingConstraint, False | Class exists but not documented |
| + EXTRA | ExternalTriggeringPoint | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ExternalTriggeringPointIdent | N/A, N/A | AbstractAccessPoint, False | Class exists but not documented |
| + EXTRA | FlatInstanceDescriptor | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | FlexrayAbsolutelyScheduledTiming | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | FlexrayChannelName | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | FlexrayCommunicationConnector | N/A, N/A | CommunicationConnector, False | Class exists but not documented |
| + EXTRA | FlexrayFrame | N/A, N/A | Frame, False | Class exists but not documented |
| + EXTRA | FlexrayFrameTriggering | N/A, N/A | FrameTriggering, False | Class exists but not documented |
| + EXTRA | FlexrayNmCluster | N/A, N/A | NmCluster, False | Class exists but not documented |
| + EXTRA | FlexrayNmClusterCoupling | N/A, N/A | NmClusterCoupling, False | Class exists but not documented |
| + EXTRA | FlexrayNmEcu | N/A, N/A | BusspecificNmEcu, False | Class exists but not documented |
| + EXTRA | FlexrayNmNode | N/A, N/A | NmNode, False | Class exists but not documented |
| + EXTRA | FlexrayPhysicalChannel | N/A, N/A | PhysicalChannel, False | Class exists but not documented |
| + EXTRA | Float | N/A, N/A | ARFloat, False | Class exists but not documented |
| + EXTRA | Frame | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | FrameMapping | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | FramePort | N/A, N/A | CommConnectorPort, False | Class exists but not documented |
| + EXTRA | FrameTriggering | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | FreeFormatEntry | N/A, N/A | ScheduleTableEntry, False | Class exists but not documented |
| + EXTRA | Gateway | N/A, N/A | FibexElement, False | Class exists but not documented |
| + EXTRA | GenericEthernetFrame | N/A, N/A | AbstractEthernetFrame, False | Class exists but not documented |
| + EXTRA | GenericTp | N/A, N/A | TransportProtocolConfiguration, False | Class exists but not documented |
| + EXTRA | GraphicFitEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | HandleInvalidEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | HardwareConfiguration | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | HeapUsage | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | HwAttributeDef | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | HwAttributeLiteralDef | N/A, N/A | ARElement, False | Class exists but not documented |
| + EXTRA | HwAttributeValue | N/A, N/A | ARElement, False | Class exists but not documented |
| + EXTRA | HwDescriptionEntity | N/A, N/A | ARElement, False | Class exists but not documented |
| + EXTRA | HwElementConnector | N/A, N/A | ARElement, False | Class exists but not documented |
| + EXTRA | HwPin | N/A, N/A | HwDescriptionEntity, False | Class exists but not documented |
| + EXTRA | HwPinGroup | N/A, N/A | HwDescriptionEntity, False | Class exists but not documented |
| + EXTRA | HwPinGroupContent | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | IPdu | N/A, N/A | Pdu, False | Class exists but not documented |
| + EXTRA | IPduMapping | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | IPduPort | N/A, N/A | CommConnectorPort, False | Class exists but not documented |
| + EXTRA | IPduSignalProcessingEnum | N/A, N/A | Enum, False | Class exists but not documented |
| + EXTRA | IPduTiming | N/A, N/A | Describable, False | Class exists but not documented |
| + EXTRA | ISignal | N/A, N/A | FibexElement, False | Class exists but not documented |
| + EXTRA | ISignalIPduGroup | N/A, N/A | FibexElement, False | Class exists but not documented |
| + EXTRA | ISignalMapping | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ISignalPort | N/A, N/A | CommConnectorPort, False | Class exists but not documented |
| + EXTRA | ISignalToIPduMapping | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | ISignalTriggering | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | IdentCaption | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | Identifier | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | ImplementationProps | N/A, N/A | Referrable, False | Class exists but not documented |
| + EXTRA | IncludedDataTypeSet | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | IncludedModeDeclarationGroupSet | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | IndexedArrayElement | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | InfrastructureServices | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | InitEvent | N/A, N/A | RTEEvent, False | Class exists but not documented |
| + EXTRA | InitialSdDelayConfig | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | InnerPortGroupInCompositionInstanceRef | N/A, N/A | AtpInstanceRef, False | Class exists but not documented |
| + EXTRA | Integer | N/A, N/A | ARNumerical, False | Class exists but not documented |
| + EXTRA | InternalConstrs | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | InternalTriggerOccurredEvent | N/A, N/A | RTEEvent, False | Class exists but not documented |
| + EXTRA | InternalTriggeringPoint | N/A, N/A | AbstractAccessPoint, False | Class exists but not documented |
| + EXTRA | InvalidationPolicy | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | Ip4AddressString | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | Ip6AddressString | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | Ipv4Configuration | N/A, N/A | NetworkEndpointAddress, False | Class exists but not documented |
| + EXTRA | Ipv6Configuration | N/A, N/A | NetworkEndpointAddress, False | Class exists but not documented |
| + EXTRA | J1939NmCluster | N/A, N/A | NmCluster, False | Class exists but not documented |
| + EXTRA | J1939NmEcu | N/A, N/A | BusspecificNmEcu, False | Class exists but not documented |
| + EXTRA | J1939NmNode | N/A, N/A | NmNode, False | Class exists but not documented |
| + EXTRA | J1939SharedAddressCluster | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | KeywordSet | N/A, N/A | ARElement, False | Class exists but not documented |
| + EXTRA | LEnum | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | Limit | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | LinCommunicationConnector | N/A, N/A | CommunicationConnector, False | Class exists but not documented |
| + EXTRA | LinCommunicationController | N/A, N/A | CommunicationController, False | Class exists but not documented |
| + EXTRA | LinConfigurationEntry | N/A, N/A | ScheduleTableEntry, False | Class exists but not documented |
| + EXTRA | LinFrame | N/A, N/A | Frame, False | Class exists but not documented |
| + EXTRA | LinFrameTriggering | N/A, N/A | FrameTriggering, False | Class exists but not documented |
| + EXTRA | LinMaster | N/A, N/A | LinCommunicationController, False | Class exists but not documented |
| + EXTRA | LinPhysicalChannel | N/A, N/A | PhysicalChannel, False | Class exists but not documented |
| + EXTRA | LinScheduleTable | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | LinTpConfig | N/A, N/A | TpConfig, False | Class exists but not documented |
| + EXTRA | LinTpConnection | N/A, N/A | TpConnection, False | Class exists but not documented |
| + EXTRA | LinTpNode | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | LinUnconditionalFrame | N/A, N/A | LinFrame, False | Class exists but not documented |
| + EXTRA | ListEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | MacAddressString | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | MacMulticastGroup | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | MeasuredStackUsage | N/A, N/A | StackUsage, False | Class exists but not documented |
| + EXTRA | MemorySection | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | MetaDataItem | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | MetaDataItemSet | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ModeAccessPoint | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ModeAccessPointIdent | N/A, N/A | IdentCaption, False | Class exists but not documented |
| + EXTRA | ModeActivationKind | N/A, N/A | str, False | Class exists but not documented |
| + EXTRA | ModeDeclaration | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | ModeDeclarationGroupPrototype | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | ModeDeclarationGroupPrototypeMapping | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ModeDeclarationMapping | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | ModeDrivenTransmissionModeCondition | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ModeGroupInAtomicSwcInstanceRef | N/A, N/A | AtpInstanceRef, False | Class exists but not documented |
| + EXTRA | ModeInterfaceMapping | N/A, N/A | PortInterfaceMapping, False | Class exists but not documented |
| + EXTRA | ModeRequestTypeMap | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ModeSwitchPoint | N/A, N/A | AbstractAccessPoint, False | Class exists but not documented |
| + EXTRA | ModeSwitchReceiverComSpec | N/A, N/A | RPortComSpec, False | Class exists but not documented |
| + EXTRA | ModeSwitchSenderComSpec | N/A, N/A | RPortComSpec, False | Class exists but not documented |
| + EXTRA | ModeSwitchedAckEvent | N/A, N/A | RTEEvent, False | Class exists but not documented |
| + EXTRA | ModeSwitchedAckRequest | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | MultiplexedPart | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | NameToken | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | NetworkEndpoint | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | NetworkEndpointAddress | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | NmCluster | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | NmClusterCoupling | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | NmEcu | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | NmNode | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | NonqueuedReceiverComSpec | N/A, N/A | ReceiverComSpec, False | Class exists but not documented |
| + EXTRA | NonqueuedSenderComSpec | N/A, N/A | SenderComSpec, False | Class exists but not documented |
| + EXTRA | NumericalValueSpecification | N/A, N/A | ValueSpecification, False | Class exists but not documented |
| + EXTRA | NvBlockNeeds | N/A, N/A | ServiceNeeds, False | Class exists but not documented |
| + EXTRA | NvBlockNeedsReliabilityEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | NvBlockNeedsWritingPriorityEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | NvProvideComSpec | N/A, N/A | PPortComSpec, False | Class exists but not documented |
| + EXTRA | NvRequireComSpec | N/A, N/A | RPortComSpec, False | Class exists but not documented |
| + EXTRA | OperationInAtomicSwcInstanceRef | N/A, N/A | AtpInstanceRef, False | Class exists but not documented |
| + EXTRA | OperationInvokedEvent | N/A, N/A | RTEEvent, False | Class exists but not documented |
| + EXTRA | PModeGroupInAtomicSwcInstanceRef | N/A, N/A | ModeGroupInAtomicSwcInstanceRef, False | Class exists but not documented |
| + EXTRA | POperationInAtomicSwcInstanceRef | N/A, N/A | OperationInAtomicSwcInstanceRef, False | Class exists but not documented |
| + EXTRA | PPortComSpec | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | PPortInCompositionInstanceRef | N/A, N/A | PortInCompositionTypeInstanceRef, False | Class exists but not documented |
| + EXTRA | PPortPrototype | N/A, N/A | AbstractProvidedPortPrototype, False | Class exists but not documented |
| + EXTRA | PRPortPrototype | N/A, N/A | PortPrototype, False | Class exists but not documented |
| + EXTRA | ParameterAccess | N/A, N/A | AbstractAccessPoint, False | Class exists but not documented |
| + EXTRA | ParameterInAtomicSWCTypeInstanceRef | N/A, N/A | AtpInstanceRef, False | Class exists but not documented |
| + EXTRA | ParameterProvideComSpec | N/A, N/A | RPortComSpec, False | Class exists but not documented |
| + EXTRA | ParameterRequireComSpec | N/A, N/A | RPortComSpec, False | Class exists but not documented |
| + EXTRA | PassThroughSwConnector | N/A, N/A | SwConnector, False | Class exists but not documented |
| + EXTRA | PduMappingDefaultValue | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | PduToFrameMapping | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | PduTriggering | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | PerInstanceMemory | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | PhysConstrs | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | PhysicalChannel | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | PncGatewayTypeEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | PortAPIOption | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | PortDefinedArgumentValue | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | PortGroup | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | PortInCompositionTypeInstanceRef | N/A, N/A | AtpInstanceRef, False | Class exists but not documented |
| + EXTRA | PortInterfaceMapping | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | PortPrototypeBlueprintInitValue | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | PositiveInteger | N/A, N/A | ARPositiveInteger, False | Class exists but not documented |
| + EXTRA | PositiveUnlimitedInteger | N/A, N/A | ARPositiveInteger, False | Class exists but not documented |
| + EXTRA | ProvidedServiceInstance | N/A, N/A | AbstractServiceInstance, False | Class exists but not documented |
| + EXTRA | QueuedReceiverComSpec | N/A, N/A | ReceiverComSpec, False | Class exists but not documented |
| + EXTRA | QueuedSenderComSpec | N/A, N/A | SenderComSpec, False | Class exists but not documented |
| + EXTRA | RModeGroupInAtomicSWCInstanceRef | N/A, N/A | ModeGroupInAtomicSwcInstanceRef, False | Class exists but not documented |
| + EXTRA | RModeInAtomicSwcInstanceRef | N/A, N/A | AtpInstanceRef, False | Class exists but not documented |
| + EXTRA | ROperationInAtomicSwcInstanceRef | N/A, N/A | OperationInAtomicSwcInstanceRef, False | Class exists but not documented |
| + EXTRA | RPortComSpec | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | RTEEvent | N/A, N/A | AbstractEvent, False | Class exists but not documented |
| + EXTRA | RVariableInAtomicSwcInstanceRef | N/A, N/A | VariableInAtomicSwcInstanceRef, False | Class exists but not documented |
| + EXTRA | RamBlockStatusControlEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | ReceiverComSpec | N/A, N/A | RPortComSpec, False | Class exists but not documented |
| + EXTRA | RecordValueSpecification | N/A, N/A | CompositeValueSpecification, False | Class exists but not documented |
| + EXTRA | ReentrancyLevelEnum | N/A, N/A | Enum, False | Class exists but not documented |
| + EXTRA | RefType | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ReferrableSubtypesEnum | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | RegularExpression | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | RequestResponseDelay | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ResourceConsumption | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | ResumePosition | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | RevisionLabelString | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | RoleBasedDataAssignment | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | RoleBasedDataTypeAssignment | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | RoleBasedPortAssignment | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | RootSwCompositionPrototype | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | RoughEstimateStackUsage | N/A, N/A | StackUsage, False | Class exists but not documented |
| + EXTRA | RunnableEntityArgument | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | RxIdentifierRange | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ScheduleTableEntry | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SdClientConfig | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SdServerConfig | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SecOcCryptoServiceMapping | N/A, N/A | CryptoServiceMapping, False | Class exists but not documented |
| + EXTRA | SecureCommunicationAuthenticationProps | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | SecureCommunicationFreshnessProps | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | SecureCommunicationProps | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SecureCommunicationPropsSet | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | SegmentPosition | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SenderComSpec | N/A, N/A | PPortComSpec, False | Class exists but not documented |
| + EXTRA | SenderRecArrayElementMapping | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SenderRecArrayTypeMapping | N/A, N/A | SenderRecCompositeTypeMapping, False | Class exists but not documented |
| + EXTRA | SenderRecCompositeTypeMapping | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SenderRecRecordElementMapping | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SenderRecRecordTypeMapping | N/A, N/A | SenderRecCompositeTypeMapping, False | Class exists but not documented |
| + EXTRA | SenderReceiverInterface | N/A, N/A | DataInterface, False | Class exists but not documented |
| + EXTRA | SenderReceiverToSignalGroupMapping | N/A, N/A | DataMapping, False | Class exists but not documented |
| + EXTRA | SenderReceiverToSignalMapping | N/A, N/A | DataMapping, False | Class exists but not documented |
| + EXTRA | SensorActuatorSwComponentType | N/A, N/A | AtomicSwComponentType, False | Class exists but not documented |
| + EXTRA | ServerCallPoint | N/A, N/A | AbstractAccessPoint, False | Class exists but not documented |
| + EXTRA | ServerComSpec | N/A, N/A | PPortComSpec, False | Class exists but not documented |
| + EXTRA | ServiceDependency | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | ServiceDiagnosticRelevanceEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | ServiceNeeds | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | SingleLanguageUnitNames | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | SoAdConfig | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SoAdRoutingGroup | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | SocketAddress | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | SocketConnection | N/A, N/A | Describable, False | Class exists but not documented |
| + EXTRA | SocketConnectionBundle | N/A, N/A | Referrable, False | Class exists but not documented |
| + EXTRA | SocketConnectionIpduIdentifier | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SoftwareContext | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | StackUsage | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | StaticPart | N/A, N/A | MultiplexedPart, False | Class exists but not documented |
| + EXTRA | String | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | SwAxisGeneric | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SwAxisGrouped | N/A, N/A | SwCalprmAxisTypeProps, False | Class exists but not documented |
| + EXTRA | SwAxisIndividual | N/A, N/A | SwCalprmAxisTypeProps, False | Class exists but not documented |
| + EXTRA | SwCalprmAxis | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SwCalprmAxisSet | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SwCalprmAxisTypeProps | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SwConnector | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | SwDataDefPropsConditional | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SwGenericAxisParam | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SwImplPolicyEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | SwRecordLayoutGroup | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SwRecordLayoutGroupContent | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SwRecordLayoutV | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SwServiceImplPolicyEnum | N/A, N/A | str, False | Class exists but not documented |
| + EXTRA | SwTextProps | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SwValueCont | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SwValues | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SwcBswRunnableMapping | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | SwcModeSwitchEvent | N/A, N/A | RTEEvent, False | Class exists but not documented |
| + EXTRA | SwcServiceDependency | N/A, N/A | ServiceDependency, False | Class exists but not documented |
| + EXTRA | SwcTiming | N/A, N/A | TimingExtension, False | Class exists but not documented |
| + EXTRA | SwcToEcuMapping | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | SwcToImplMapping | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | SymbolProps | N/A, N/A | ImplementationProps, False | Class exists but not documented |
| + EXTRA | SynchronousServerCallPoint | N/A, N/A | ServerCallPoint, False | Class exists but not documented |
| + EXTRA | SystemMapping | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | TRefType | N/A, N/A | RefType, False | Class exists but not documented |
| + EXTRA | TargetIPduRef | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | TcpTp | N/A, N/A | TcpUdpConfig, False | Class exists but not documented |
| + EXTRA | TcpUdpConfig | N/A, N/A | TransportProtocolConfiguration, False | Class exists but not documented |
| + EXTRA | TextTableMapping | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | TextValueSpecification | N/A, N/A | ValueSpecification, False | Class exists but not documented |
| + EXTRA | TimeRangeType | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | TimeSyncClientConfiguration | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | TimeSyncServerConfiguration | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | TimeSynchronization | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | TimeValue | N/A, N/A | ARFloat, False | Class exists but not documented |
| + EXTRA | TimingConstraint | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | TimingEvent | N/A, N/A | RTEEvent, False | Class exists but not documented |
| + EXTRA | TimingExtension | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | TlsCryptoServiceMapping | N/A, N/A | CryptoServiceMapping, False | Class exists but not documented |
| + EXTRA | TpAddress | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | TpConfig | N/A, N/A | FibexElement, False | Class exists but not documented |
| + EXTRA | TpConnection | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | TpConnectionIdent | N/A, N/A | Referrable, False | Class exists but not documented |
| + EXTRA | TpPort | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | TransformationComSpecProps | N/A, N/A | Describable, False | Class exists but not documented |
| + EXTRA | TransformationDescription | N/A, N/A | Describable, False | Class exists but not documented |
| + EXTRA | TransformationISignalProps | N/A, N/A | Describable, False | Class exists but not documented |
| + EXTRA | TransformationTechnology | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | TransformerClassEnum | N/A, N/A | AREnum, False | Class exists but not documented |
| + EXTRA | TransmissionAcknowledgementRequest | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | TransmissionModeCondition | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | TransmissionModeDeclaration | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | TransmissionModeTiming | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | TransportProtocolConfiguration | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | Trigger | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | TriggerInterfaceMapping | N/A, N/A | PortInterfaceMapping, False | Class exists but not documented |
| + EXTRA | TriggerMapping | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | UdpNmCluster | N/A, N/A | NmCluster, False | Class exists but not documented |
| + EXTRA | UdpNmClusterCoupling | N/A, N/A | NmClusterCoupling, False | Class exists but not documented |
| + EXTRA | UdpNmEcu | N/A, N/A | BusspecificNmEcu, False | Class exists but not documented |
| + EXTRA | UdpNmNode | N/A, N/A | NmNode, False | Class exists but not documented |
| + EXTRA | UdpTp | N/A, N/A | TcpUdpConfig, False | Class exists but not documented |
| + EXTRA | UnlimitedInteger | N/A, N/A | Integer, False | Class exists but not documented |
| + EXTRA | UserDefinedTransformationComSpecProps | N/A, N/A | TransformationComSpecProps, False | Class exists but not documented |
| + EXTRA | ValueList | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | ValueSpecification | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | VariableAccess | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | VariableAndParameterInterfaceMapping | N/A, N/A | PortInterfaceMapping, False | Class exists but not documented |
| + EXTRA | VariableDataPrototype | N/A, N/A | AutosarDataPrototype, False | Class exists but not documented |
| + EXTRA | VariableDataPrototypeInSystemInstanceRef | N/A, N/A | AtpInstanceRef, False | Class exists but not documented |
| + EXTRA | VariableInAtomicSWCTypeInstanceRef | N/A, N/A | AtpInstanceRef, False | Class exists but not documented |
| + EXTRA | VariableInAtomicSwcInstanceRef | N/A, N/A | AtpInstanceRef, False | Class exists but not documented |
| + EXTRA | VerbatimString | N/A, N/A | ARLiteral, False | Class exists but not documented |
| + EXTRA | VlanConfig | N/A, N/A | Identifiable, False | Class exists but not documented |
| + EXTRA | VlanMembership | N/A, N/A | ARObject, False | Class exists but not documented |
| + EXTRA | WorstCaseStackUsage | N/A, N/A | StackUsage, False | Class exists but not documented |

## Legend

- ✓ MATCH: Class has correct parent and abstract status
- ✗ MISSING: Class documented but not found in source
- ⚠ MISMATCH: Class has wrong parent or abstract status
- + EXTRA: Class exists but not documented
