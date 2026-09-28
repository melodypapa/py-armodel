# All Sync Todo Classes (Consolidated)

Generated from all Group files in `docs/plan/sync-todo/` — Classes ordered by name with status and commit ID.

**Status legend:** `[x] Done` = 9-step sync complete AND `# Spec verified:`/`# XSD verified:` stamped in src · `[x]`/`[ ] Deferred` = sync complete (Steps 1–8 green) but the stamp is **deferred to a batch 9b user confirmation** · `[ ] Pending` = sync not yet complete. (Deferred set audited 2026-09-27 against the src stamps.)

## Summary

**721 classes total**

| Status | Classes | Percent |
| --- | --- | --- |
| [x] Done | 477 | 66.2% |
| [x] Deferred | 11 | 1.5% |
| [x] Retired | 0 | 0.0% |
| [ ] Deferred | 167 | 23.2% |
| [ ] Pending | 66 | 9.2% |

| Class Name                                              | Status      | Commit ID                                | Groups           |
| ------------------------------------------------------- | ------------| ---------------------------------------- | ---------------- |
| `ARElement`                                             | [x] Done    | 61c85fa794                               | Group1           |
| `ARList`                                                | [x] Done    | 2151ca0302                               | Group9           |
| `ARObject`                                              | [x] Done    | 78ae363c75                               | Group1           |
| `ARPackage`                                             | [x] Done    | 360648178f                               | Group1           |
| `AUTOSAR`                                               | [x] Done    | 74f4d3c80a                               | Group1           |
| `AbstractDoIpLogicAddressProps`                         | [x] Done    | 64d125ffae                               | Group7           |
| `AbstractEnumerationValueVariationPoint`                | [x] Done    | 0518a7bca2                               | Group8           |
| `AbstractEthernetFrame`                                 | [x] Done    | cba67817b3                               | Group6           |
| `AbstractImplementationDataType`                        | [x] Done    | 9b5379d3e3                               | Group1           |
| `AbstractImplementationDataTypeElement`                 | [x] Done    | cabd5469e9                               | Group1           |
| `AbstractNumericalVariationPoint`                       | [x] Done    | d5c96fd954                               | Group8           |
| `AbstractProvidedPortPrototype`                         | [ ] Deferred| fb7a835f90                               | Group11          |
| `AbstractRequiredPortPrototype`                         | [ ] Deferred| fb7a835f90                               | Group11          |
| `AlignEnum`                                             | [x] Done    | fa74a474a5                               | Group3           |
| `ApiPrincipleEnum`                                      | [x] Done    | c6d2e83f74                               | Group10          |
| `AppOsTaskProxyToEcuTaskProxyMapping`                   | [ ] Pending | N/A                                      | Group18          |
| `ApplicationCompositeDataType`                          | [x] Done    | de9d3fe0a4                               | Group2           |
| `ApplicationCompositeElementDataPrototype`              | [x] Done    | 031d5c7848                               | Group2           |
| `ApplicationCompositeElementInPortInterfaceInstanceRef` | [x] Done    | 399b647757                               | Group2           |
| `ApplicationDataType`                                   | [x] Done    | b8d0878d98                               | Group2           |
| `ApplicationDeferredDataType`                           | [x] Done    | abdfbf1d96                               | Group1           |
| `ApplicationEntry`                                      | [ ] Pending | N/A                                      | Group17          |
| `ApplicationPartitionToEcuPartitionMapping`             | [ ] Pending | N/A                                      | Group18          |
| `ApplicationPrimitiveDataType`                          | [x] Done    | 4a9ccae9b8                               | Group2           |
| `ApplicationRecordDataType`                             | [x] Deferred| 0a06e0fae3                               | Group2           |
| `ApplicationRecordElement`                              | [x] Done    | ae4ed75065                               | Group2           |
| `ArVariableInImplementationDataInstanceRef`             | [x] Done    | 910009eecc                               | Group2           |
| `Area`                                                  | [x] Done    | c9f2464902                               | Group3           |
| `AreaEnumNohref`                                        | [x] Done    | 1d6f8c0aa9                               | Group3           |
| `AreaEnumShape`                                         | [x] Done    | 966320f6a7                               | Group3           |
| `ArrayImplPolicyEnum`                                   | [x] Done    | 700b032789                               | Group10          |
| `ArrayValueSpecification`                               | [x] Done    | 043de7436d                               | Group3           |
| `AsamRecordLayoutSemantics`                             | [x] Done    | 2acaf7a45f                               | Group3           |
| `AssemblySwConnector`                                   | [x] Done    | 2a104a061c                               | Group2           |
| `AsynchronousServerCallPoint`                           | [x] Done    | 3223dde420                               | Group2           |
| `AsynchronousServerCallResultPoint`                     | [x] Done    | 724f490c7a                               | Group2           |
| `AsynchronousServerCallReturnsEvent`                    | [ ] Deferred| N/A                                      | Group12          |
| `AtpBlueprint`                                          | [x] Done    | 043de7436d                               | Group1           |
| `AtpBlueprintMapping`                                   | [x] Done    | 493e272da6                               | Group1           |
| `AtpBlueprintable`                                      | [x] Done    | b7cf03094f                               | Group1           |
| `AtpDefinition`                                         | [x] Done    | 38eb1e817c                               | Group1           |
| `AtpPrototype`                                          | [x] Done    | eb4c4bf308                               | Group1           |
| `AtpStructureElement`                                   | [x] Done    | 5eff088fa5                               | Group1           |
| `AtpType`                                               | [x] Done    | 451ad38330                               | Group1           |
| `AttributeValueVariationPoint`                          | [x] Done    | d5c96fd954                               | Group8           |
| `AutoCollectEnum`                                       | [x] Done    | 75f4005552                               | Group1           |
| `AutosarDataType`                                       | [x] Done    | a5f99df464                               | Group1           |
| `AutosarOperationArgumentInstance`                      | [x] Done    | b8cce0057f                               | Group8           |
| `AutosarParameterRef`                                   | [ ] Deferred| N/A                                      | Group10          |
| `AutosarVariableRef`                                    | [ ] Deferred| N/A                                      | Group10          |
| `BackgroundEvent`                                       | [x] Done    | 27b88a942c                               | Group2           |
| `BindingTimeEnum`                                       | [x] Done    | 53bf180881                               | Group8           |
| `BlueprintFormula`                                      | [x] Done    | 6d8ace0288                               | Group8           |
| `BlueprintGenerator`                                    | [x] Done    | 246fc98452                               | Group8           |
| `BlueprintMapping`                                      | [x] Done    | a6fa7b8c18                               | Group8           |
| `BlueprintMappingSet`                                   | [x] Done    | aec046b9cc                               | Group1           |
| `BlueprintPolicy`                                       | [x] Done    | f5f5084e36                               | Group1           |
| `BooleanValueVariationPoint`                            | [x] Done    | d5c96fd954                               | Group8           |
| `Br`                                                    | [x] Done    | c2a85e6f8f                               | Group3           |
| `BswApiOptions`                                         | [ ] Deferred| N/A                                      | Group13          |
| `BswAsynchronousServerCallReturnsEvent`                 | [ ] Deferred| N/A                                      | Group13          |
| `BswClientPolicy`                                       | [x] Done    | 3141824107                               | Group4           |
| `BswDataReceivedEvent`                                  | [ ] Deferred| N/A                                      | Group13          |
| `BswDataReceptionPolicy`                                | [ ] Deferred| 7e3a2541a3                               | Group13          |
| `BswDataSendPolicy`                                     | [x] Done    | ccacff4a64                               | Group4           |
| `BswDirectCallPoint`                                    | [ ] Deferred| N/A                                      | Group13          |
| `BswEntryRelationship`                                  | [ ] Deferred| 75c6517342                               | Group13          |
| `BswEntryRelationshipEnum`                              | [ ] Deferred| 994c3903cb                               | Group13          |
| `BswEntryRelationshipSet`                               | [ ] Deferred| a4d57abd3a                               | Group13          |
| `BswInternalBehavior`                                   | [x] Done    | 89a7231799                               | Group4           |
| `BswInternalTriggerOccurredEvent`                       | [ ] Deferred| N/A                                      | Group13          |
| `BswInternalTriggeringPoint`                            | [ ] Deferred| N/A                                      | Group13          |
| `BswInternalTriggeringPointPolicy`                      | [x] Done    | 2bb8413910                               | Group4           |
| `BswInterruptEntity`                                    | [ ] Deferred| N/A                                      | Group13          |
| `BswMgrNeeds`                                           | [x] Done    | 628464ed64                               | Group4           |
| `BswModeManagerErrorEvent`                              | [ ] Deferred| N/A                                      | Group13          |
| `BswModeSwitchAckRequest`                               | [ ] Deferred| N/A                                      | Group13          |
| `BswModeSwitchedAckEvent`                               | [ ] Deferred| 160eae8f23                               | Group13          |
| `BswModuleCallPoint`                                    | [ ] Deferred| N/A                                      | Group13          |
| `BswModuleClientServerEntry`                            | [ ] Deferred| e69bc46baa                               | Group13          |
| `BswModuleDependency`                                   | [ ] Deferred| 1ca038b144                               | Group13          |
| `BswParameterPolicy`                                    | [x] Done    | eceaef9296                               | Group4           |
| `BswPerInstanceMemoryPolicy`                            | [x] Done    | b89ad783a3                               | Group4           |
| `BswQueuedDataReceptionPolicy`                          | [ ] Deferred| N/A                                      | Group13          |
| `BswReleasedTriggerPolicy`                              | [x] Done    | 04498e5b27                               | Group4           |
| `BswSynchronousServerCallPoint`                         | [ ] Deferred| N/A                                      | Group13          |
| `BswTimingEvent`                                        | [ ] Deferred| 1a0a0619b2                               | Group13          |
| `BuildAction`                                           | [x] Done    | 6c9ef66b40                               | Group1           |
| `BuildActionEntity`                                     | [x] Done    | d7717e736a                               | Group1           |
| `BuildActionEnvironment`                                | [x] Done    | 2311c8754f                               | Group1           |
| `BuildActionInvocator`                                  | [x] Done    | 7008d5e857                               | Group1           |
| `BuildActionIoElement`                                  | [x] Done    | b572582c11                               | Group1           |
| `BuildActionManifest`                                   | [x] Done    | e6dcc8e79f                               | Group1           |
| `BuildEngineeringObject`                                | [x] Done    | 96d176ed20                               | Group1           |
| `BulkNvDataDescriptor`                                  | [ ] Deferred| N/A                                      | Group10          |
| `CanClusterBusOffRecovery`                              | [ ] Pending | N/A                                      | Group17          |
| `CanCommunicationConnector`                             | [ ] Pending | N/A                                      | Group17          |
| `CanControllerConfiguration`                            | [ ] Pending | N/A                                      | Group17          |
| `CanControllerConfigurationRequirements`                | [ ] Pending | N/A                                      | Group17          |
| `CanControllerFdConfigurationRequirements`              | [ ] Pending | N/A                                      | Group17          |
| `CanNmCluster`                                          | [ ] Pending | N/A                                      | Group18          |
| `CanNmClusterCoupling`                                  | [ ] Pending | N/A                                      | Group18          |
| `CanNmNode`                                             | [ ] Pending | N/A                                      | Group18          |
| `ChapterContent`                                        | [x] Done    | dee07d0a3a                               | Group9           |
| `ChapterEnumBreak`                                      | [x] Done    | 20e6ee88d0                               | Group3           |
| `ChapterModel`                                          | [x] Done    | d3d61c9b2e                               | Group9           |
| `ClientIdDefinition`                                    | [x] Done    | 8618ec8872                               | Group5           |
| `ClientIdDefinitionSet`                                 | [x] Done    | 01759771dd                               | Group5           |
| `ClientIdRange`                                         | [x] Done    | fce66955f5                               | Group5           |
| `ClientServerApplicationErrorMapping`                   | [ ] Deferred| N/A                                      | Group11          |
| `ClientServerInterfaceMapping`                          | [ ] Deferred| N/A                                      | Group11          |
| `ClientServerOperationMapping`                          | [ ] Deferred| N/A                                      | Group11          |
| `Code`                                                  | [x] Done    | 9f470606b5                               | Group1           |
| `CollectableElement`                                    | [x] Done    | 3b31b7c402                               | Group1           |
| `Collection`                                            | [x] Done    | 75f4005552                               | Group1           |
| `Colspec`                                               | [x] Done    | 2bd0d07503                               | Group3           |
| `ComManagementMapping`                                  | [x] Done    | 19c327cca6                               | Group5           |
| `CommunicationBufferLocking`                            | [x] Done    | 7c67628122                               | Group2           |
| `CommunicationControllerMapping`                        | [x] Done    | 2613747d22                               | Group7           |
| `CommunicationCycle`                                    | [x] Done    | 75683a2ede                               | Group5           |
| `CommunicationDirectionType`                            | [ ] Pending | 3378eb6247                               | Group15          |
| `Compiler`                                              | [x] Done    | 3fce597322                               | Group1           |
| `ComponentInCompositionInstanceRef`                     | [x] Done    | 02e863a567                               | Group7           |
| `ComponentInSystemInstanceRef`                          | [x] Done    | b511fb85b0                               | Group7           |
| `CompositeNetworkRepresentation`                        | [x] Done    | b1e81e17d6                               | Group10          |
| `CompositeRuleBasedValueArgument`                       | [x] Done    | 0c916371eb                               | Group3           |
| `CompositeRuleBasedValueSpecification`                  | [x] Done    | 13a010bf81                               | Group3           |
| `CompositeValueSpecification`                           | [x] Done    | cc842d74c1                               | Group3           |
| `CompositionSwComponentType`                            | [x] Done    | 6b46fb26a9                               | Group2           |
| `Compu`                                                 | [x] Done    | dac94a9ffe                               | Group3           |
| `CompuConst`                                            | [x] Done    | eddddc9982                               | Group3           |
| `CompuConstContent`                                     | [x] Done    | b473f52422                               | Group3           |
| `CompuConstFormulaContent`                              | [x] Done    | 045d6fb522                               | Group3           |
| `CompuConstNumericContent`                              | [x] Done    | 4b82220e02                               | Group3           |
| `CompuConstTextContent`                                 | [x] Done    | 4cb828510e                               | Group3           |
| `CompuContent`                                          | [x] Done    | 9f67b3e297                               | Group3           |
| `CompuGenericMath`                                      | [x] Done    | 1de6c0ef23                               | Group3           |
| `CompuMethod`                                           | [x] Done    | 135f42e555                               | Group3           |
| `CompuNominatorDenominator`                             | [x] Done    | ff6ef18624                               | Group3           |
| `CompuRationalCoeffs`                                   | [x] Done    | 26100b4c69                               | Group3           |
| `CompuScale`                                            | [x] Done    | 057a103913                               | Group3           |
| `CompuScaleConstantContents`                            | [x] Done    | 3d859c8074                               | Group3           |
| `CompuScaleContents`                                    | [x] Done    | 88acf483f8                               | Group3           |
| `CompuScaleRationalFormula`                             | [x] Done    | 5a21470cd7                               | Group3           |
| `CompuScales`                                           | [x] Done    | 64d125ffae                               | Group3           |
| `ConditionByFormula`                                    | [x] Done    | 18b494eba5                               | Group8           |
| `ConfigReferenceValue`                                  | [ ] Pending | N/A                                      | Group19          |
| `ConstantReference`                                     | [x] Done    | 4853348ea0                               | Group9           |
| `ConstantSpecification`                                 | [x] Done    | 265721a764                               | Group9           |
| `ConstantSpecificationMappingSet`                       | [x] Done    | 8e5acbb2b1                               | Group1           |
| `ConsumedProvidedServiceInstanceGroup`                  | [x] Done    | fce66955f5                               | Group5           |
| `ContainedIPduCollectionSemanticsEnum`                  | [x] Done    | 64d125ffae                               | Group5           |
| `ContainedIPduProps`                                    | [x] Done    | 206cf29517                               | Group5           |
| `CouplingPortAbstractShaper`                            | [ ] Pending | N/A                                      | Group16          |
| `CouplingPortScheduler`                                 | [x] Done    | 0f61040c0c                               | Group6           |
| `CouplingPortStructuralElement`                         | [x] Done    | 8404bbb94a                               | Group6           |
| `CpSoftwareCluster`                                     | [x] Done    | 1194e00ca2                               | Group5           |
| `CryptoCertificateAlgorithmFamilyEnum`                  | [x] Done    | 4c65329125                               | Group6           |
| `CryptoCertificateFormatEnum`                           | [x] Done    | 7fc9ab7674                               | Group6           |
| `CryptoEllipticCurveProps`                              | [x] Done    | d31256a6bc                               | Group6           |
| `CryptoKeyManagementNeeds`                              | [x] Done    | dc49a71665                               | Group4           |
| `CryptoKeySlot`                                         | [x] Done    | a02f617547                               | Group7           |
| `CryptoKeySlotAllowedModification`                      | [ ] Deferred| c535a86fd6                               | Group20          |
| `CryptoKeySlotContentAllowedUsage`                      | [ ] Deferred| 6fe403d35e                               | Group20          |
| `CryptoKeySlotTypeEnum`                                 | [ ] Deferred| 4ea5cb5b45                               | Group20          |
| `CryptoObjectTypeEnum`                                  | [ ] Deferred| 5b42d57569                               | Group20          |
| `CryptoServiceCertificate`                              | [x] Done    | 757aea1d17                               | Group6           |
| `CryptoServiceJobNeeds`                                 | [x] Done    | 2ec474677a                               | Group4           |
| `CryptoServiceMapping`                                  | [x] Done    | 757aea1d17                               | Group6           |
| `CryptoServiceNeeds`                                    | [ ] Deferred| d064592a44                               | Group14          |
| `CryptoServicePrimitive`                                | [x] Done    | b609d72d59                               | Group6           |
| `CryptoSignatureScheme`                                 | [x] Done    | 1eaeb5800b                               | Group6           |
| `CycleCounter`                                          | [x] Done    | 75683a2ede                               | Group5           |
| `CycleRepetition`                                       | [x] Done    | 75683a2ede                               | Group5           |
| `CycleRepetitionType`                                   | [x] Done    | bf6cb0f022                               | Group5           |
| `CyclicTiming`                                          | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `DataConstr`                                            | [x] Done    | 9927cc9e89                               | Group3           |
| `DataConstrRule`                                        | [x] Done    | fa640a0d86                               | Group3           |
| `DataFilter`                                            | [x] Done    | ed2a073e76                               | Group9           |
| `DataFilterTypeEnum`                                    | [x] Done    | b59bd6ebbe                               | Group9           |
| `DataInterface`                                         | [x] Done    | d838fd43f4                               | Group1           |
| `DataLinkLayerRule`                                     | [ ] Deferred| 0d343df2a7                               | Group20          |
| `DataMapping`                                           | [ ] Pending | N/A                                      | Group17          |
| `DataPrototype`                                         | [x] Done    | 9175595d88                               | Group1           |
| `DataPrototypeTransformationProps`                      | [x] Done    | ba255a82cc                               | Group6           |
| `DataReceiveErrorEvent`                                 | [ ] Deferred| N/A                                      | Group12          |
| `DataReceivedEvent`                                     | [ ] Deferred| N/A                                      | Group12          |
| `DataSendCompletedEvent`                                | [ ] Deferred| N/A                                      | Group12          |
| `DataTransformationErrorHandlingEnum`                   | [x] Done    | 7fc79e4b73                               | Group2           |
| `DataTransformationSet`                                 | [x] Done    | 757aea1d17                               | Group6           |
| `DataTransformationStatusForwardingEnum`                | [x] Done    | 7c67628122                               | Group2           |
| `DataTypeMap`                                           | [ ] Deferred| N/A                                      | Group10          |
| `DataTypeMappingSet`                                    | [x] Done    | 21ab486b53                               | Group2           |
| `DataWriteCompletedEvent`                               | [ ] Deferred| N/A                                      | Group12          |
| `DefaultValueElement`                                   | [ ] Pending | N/A                                      | Group17          |
| `DelegationSwConnector`                                 | [x] Done    | 503344170e                               | Group2           |
| `DependencyOnArtifact`                                  | [x] Done    | 25211e56ca                               | Group1           |
| `DependencyUsageEnum`                                   | [x] Done    | 9a8c86ae9a                               | Group10          |
| `DiagEventDebounceAlgorithm`                            | [x] Done    | 4f246ae62d                               | Group4           |
| `DiagEventDebounceCounterBased`                         | [ ] Deferred| d064592a44                               | Group14          |
| `DiagEventDebounceMonitorInternal`                      | [x] Done    | 103cfd4316                               | Group4           |
| `DiagnosticAccessPermission`                            | [x] Done    | 9cbb4e26e7                               | Group7           |
| `DiagnosticAudienceEnum`                                | [ ] Deferred| 5685ad743e                               | Group14          |
| `DiagnosticAuthRoleProxy`                               | [x] Done    | 4579b43f0d                               | Group7           |
| `DiagnosticCapabilityElement`                           | [ ] Deferred| f5ffd3abf2                               | Group14          |
| `DiagnosticClearDtcNotificationEnum`                    | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DiagnosticCommonElement`                               | [x] Done    | e0d022b1aa                               | Group7           |
| `DiagnosticCommunicationManagerNeeds`                   | [ ] Deferred| 79c639e42a                               | Group14          |
| `DiagnosticComponentNeeds`                              | [x] Done    | 5c4c0963af                               | Group4           |
| `DiagnosticConnection`                                  | [x] Done    | e96086c12f                               | Group5           |
| `DiagnosticControlNeeds`                                | [x] Done    | d0a1134e3b                               | Group4           |
| `DiagnosticEnvCompareCondition`                         | [ ] Deferred| af255af373                               | Group14          |
| `DiagnosticEnvConditionFormula`                         | [ ] Deferred| af255af373                               | Group14          |
| `DiagnosticEnvConditionFormulaPart`                     | [x] Deferred| af255af373                               | Group14          |
| `DiagnosticEnvModeElement`                              | [ ] Deferred| af255af373                               | Group14          |
| `DiagnosticEnvironmentalCondition`                      | [x] Done    | 5bbca5f217                               | Group7           |
| `DiagnosticEventInfoNeeds`                              | [ ] Deferred| 79c639e42a                               | Group14          |
| `DiagnosticEventManagerNeeds`                           | [x] Done    | dc34774429                               | Group4           |
| `DiagnosticJumpToBootLoaderEnum`                        | [ ] Deferred| N/A                                      | Group14          |
| `DiagnosticLogicalOperatorEnum`                         | [ ] Deferred| N/A                                      | Group14          |
| `DiagnosticProcessingStyleEnum`                         | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DiagnosticRequestFileTransferNeeds`                    | [x] Done    | f084c4328c                               | Group4           |
| `DiagnosticRoutineNeeds`                                | [ ] Deferred| 79c639e42a                               | Group14          |
| `DiagnosticRoutineTypeEnum`                             | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DiagnosticSecurityLevel`                               | [x] Done    | f2da1338fc                               | Group7           |
| `DiagnosticServiceClass`                                | [x] Deferred| 6b514727f9                               | Group14          |
| `DiagnosticServiceInstance`                             | [x] Done    | 6b514727f9                               | Group7           |
| `DiagnosticServiceRequestCallbackTypeEnum`              | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DiagnosticServiceTable`                                | [x] Done    | 9bd6fadae5                               | Group7           |
| `DiagnosticSession`                                     | [x] Done    | 06d4e49a26                               | Group7           |
| `DiagnosticUploadDownloadNeeds`                         | [x] Done    | fe8a0a1a6d                               | Group4           |
| `DiagnosticValueAccessEnum`                             | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DiagnosticValueNeeds`                                  | [ ] Deferred| 79c639e42a                               | Group14          |
| `DiagnosticsCommunicationSecurityNeeds`                 | [x] Done    | d24a66632e                               | Group4           |
| `DltApplication`                                        | [x] Done    | c42f8ae9a2                               | Group5           |
| `DltArgument`                                           | [x] Done    | 64d125ffae                               | Group5           |
| `DltConfig`                                             | [x] Done    | f1eb819e47                               | Group5           |
| `DltContext`                                            | [x] Done    | c42f8ae9a2                               | Group5           |
| `DltDefaultTraceStateEnum`                              | [x] Done    | f1eb819e47                               | Group5           |
| `DltEcu`                                                | [x] Done    | c42f8ae9a2                               | Group5           |
| `DltLogChannel`                                         | [x] Done    | f1eb819e47                               | Group5           |
| `DltMessage`                                            | [x] Done    | c42f8ae9a2                               | Group5           |
| `DltUserNeeds`                                          | [x] Done    | cc86c1002b                               | Group4           |
| `DoIpActivationLineNeeds`                               | [x] Done    | bf846cce70                               | Group4           |
| `DoIpConfig`                                            | [x] Done    | fce66955f5                               | Group5           |
| `DoIpEntity`                                            | [ ] Deferred| b1e4750b14                               | Group16          |
| `DoIpGidNeeds`                                          | [x] Done    | 6c31e0057f                               | Group4           |
| `DoIpGidSynchronizationNeeds`                           | [x] Done    | c64cb6318c                               | Group4           |
| `DoIpInterface`                                         | [x] Done    | c53a7febdc                               | Group5           |
| `DoIpLogicAddress`                                      | [ ] Deferred| a5671c229e                               | Group20          |
| `DoIpLogicTargetAddressProps`                           | [x] Done    | 64d125ffae                               | Group7           |
| `DoIpLogicTesterAddressProps`                           | [x] Done    | 64d125ffae                               | Group7           |
| `DoIpPowerModeStatusNeeds`                              | [x] Done    | 4350642e77                               | Group5           |
| `DoIpRoutingActivation`                                 | [x] Done    | c53a7febdc                               | Group5           |
| `DoIpRule`                                              | [ ] Deferred| ebd95cd8f9                               | Group20          |
| `DoIpTpConfig`                                          | [x] Done    | ac63e581b9                               | Group7           |
| `DoIpTpConnection`                                      | [ ] Deferred| 0abdd0dba4                               | Group20          |
| `DocumentViewSelectable`                                | [x] Done    | ba2c324b39                               | Group3           |
| `DtcFormatTypeEnum`                                     | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DtcKindEnum`                                           | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DtcStatusChangeNotificationNeeds`                      | [ ] Deferred| 79c639e42a                               | Group14          |
| `DynamicPart`                                           | [ ] Deferred| 4211085bc4                               | Group15          |
| `DynamicPartAlternative`                                | [x] Done    | 206cf29517                               | Group5           |
| `ECUMapping`                                            | [x] Done    | 34bb50d75e                               | Group7           |
| `EcuInstance`                                           | [x] Done    | 206e89be41                               | Group5           |
| `EcuPartition`                                          | [x] Done    | c53a7febdc                               | Group5           |
| `EcuStateMgrUserNeeds`                                  | [x] Done    | 6b31696dff                               | Group4           |
| `EcucBooleanParamDef`                                   | [ ] Pending | N/A                                      | Group19          |
| `EcucConditionFormula`                                  | [ ] Pending | N/A                                      | Group19          |
| `EcucConfigurationClassEnum`                            | [ ] Pending | N/A                                      | Group19          |
| `EcucDestinationUriDefRefType`                          | [ ] Pending | N/A                                      | Group19          |
| `EcucFloatParamDef`                                     | [ ] Pending | N/A                                      | Group19          |
| `EcucForeignReferenceDef`                               | [ ] Pending | N/A                                      | Group19          |
| `EcucLinkerSymbolDef`                                   | [ ] Pending | N/A                                      | Group19          |
| `EcucParameterDerivationFormula`                        | [ ] Pending | N/A                                      | Group19          |
| `EcucQueryExpression`                                   | [ ] Pending | N/A                                      | Group19          |
| `EcucReferenceDef`                                      | [ ] Pending | N/A                                      | Group19          |
| `EcucScopeEnum`                                         | [ ] Pending | N/A                                      | Group19          |
| `EcucSymbolicNameReferenceDef`                          | [ ] Pending | N/A                                      | Group19          |
| `EcucUriReferenceDef`                                   | [ ] Pending | N/A                                      | Group19          |
| `EcucValueCollection`                                   | [ ] Pending | N/A                                      | Group19          |
| `EndToEndDescription`                                   | [ ] Deferred| N/A                                      | Group10          |
| `EndToEndProtectionISignalIPdu`                         | [ ] Pending | N/A                                      | Group18          |
| `EndToEndProtectionSet`                                 | [x] Done    | 4a7d82ffc7                               | Group5           |
| `EndToEndProtectionVariablePrototype`                   | [x] Done    | 4a7d82ffc7                               | Group5           |
| `EndToEndTransformationISignalProps`                    | [ ] Pending | N/A                                      | Group18          |
| `Entry`                                                 | [x] Done    | 9005f6228e                               | Group3           |
| `EthTcpIpIcmpProps`                                     | [x] Done    | c53a7febdc                               | Group5           |
| `EthTcpIpProps`                                         | [x] Done    | db98d8ff29                               | Group5           |
| `EthernetPhysicalChannel`                               | [x] Done    | 206cf29517                               | Group5           |
| `EthernetPriorityRegeneration`                          | [ ] Deferred| b1e4750b14                               | Group16          |
| `EventControlledTiming`                                 | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `ExternalTriggeringPointIdent`                          | [x] Done    | c04ca0f5b3                               | Group2           |
| `FMConditionByFeaturesAndAttributes`                    | [x] Done    | d69232bdf4                               | Group8           |
| `FMConditionByFeaturesAndSwSystemconsts`                | [x] Done    | d69232bdf4                               | Group8           |
| `FMFormulaByFeaturesAndAttributes`                      | [x] Done    | d69232bdf4                               | Group8           |
| `FMFormulaByFeaturesAndSwSystemconsts`                  | [x] Done    | d69232bdf4                               | Group8           |
| `Field`                                                 | [ ] Deferred| 413d1a4b62                               | Group11          |
| `FileInfoComment`                                       | [x] Done    | c62e1c8943                               | Group1           |
| `FirewallActionEnum`                                    | [x] Done    | ab2daa7785                               | Group3           |
| `FirewallRule`                                          | [x] Deferred| 00d011d4ad                               | Group1           |
| `FirewallRuleProps`                                     | [x] Done    | 89039bf2bb                               | Group7           |
| `FlatInstanceDescriptor`                                | [x] Done    | 9db34796eb                               | Group1           |
| `FlatMap`                                               | [x] Done    | 5eadca7853                               | Group1           |
| `FlexrayChannelName`                                    | [ ] Deferred| 7c137656f6                               | Group15          |
| `FlexrayCommunicationConnector`                         | [ ] Pending | N/A                                      | Group17          |
| `FlexrayCommunicationController`                        | [ ] Pending | N/A                                      | Group17          |
| `FlexrayFrame`                                          | [x] Done    | 757aea1d17                               | Group6           |
| `FlexrayFrameTriggering`                                | [ ] Pending | N/A                                      | Group17          |
| `FlexrayNmCluster`                                      | [x] Done    | 9c8e10b37f                               | Group6           |
| `FlexrayNmClusterCoupling`                              | [ ] Pending | N/A                                      | Group18          |
| `FlexrayNmEcu`                                          | [x] Done    | 9c8e10b37f                               | Group6           |
| `FlexrayNmNode`                                         | [x] Done    | 9c8e10b37f                               | Group6           |
| `FlexrayPhysicalChannel`                                | [ ] Pending | N/A                                      | Group17          |
| `FloatValueVariationPoint`                              | [x] Done    | d5c96fd954                               | Group8           |
| `FormulaExpression`                                     | [x] Done    | 88ed82bed3                               | Group8           |
| `FrameEnum`                                             | [x] Done    | 531991e029                               | Group3           |
| `FrameMapping`                                          | [ ] Pending | N/A                                      | Group17          |
| `FramePort`                                             | [x] Done    | 75683a2ede                               | Group5           |
| `FrameTriggering`                                       | [x] Done    | 206cf29517                               | Group5           |
| `FunctionInhibitionNeeds`                               | [x] Done    | 5c4c0963af                               | Group4           |
| `FurtherActionByteNeeds`                                | [x] Done    | 30e266fd91                               | Group5           |
| `Gateway`                                               | [ ] Pending | N/A                                      | Group17          |
| `GeneralAnnotation`                                     | [x] Done    | ab2daa7785                               | Group3           |
| `GeneralParameter`                                      | [x] Done    | b622d5b424                               | Group9           |
| `GeneralPurposeIPdu`                                    | [x] Done    | 75683a2ede                               | Group5           |
| `GeneralPurposePdu`                                     | [x] Done    | 75683a2ede                               | Group5           |
| `GenericEthernetFrame`                                  | [x] Done    | 675a97e967                               | Group6           |
| `GenericTp`                                             | [ ] Deferred| N/A                                      | Group16          |
| `GlobalSupervisionNeeds`                                | [x] Done    | 5c4c0963af                               | Group4           |
| `Graphic`                                               | [x] Done    | 06b46f32ba                               | Group3           |
| `GraphicFitEnum`                                        | [x] Done    | 5b543a21d4                               | Group3           |
| `GraphicNotationEnum`                                   | [x] Done    | f25e765d8b                               | Group3           |
| `HandleInvalidEnum`                                     | [x] Done    | 18271ddd84                               | Group1           |
| `HardwareConfiguration`                                 | [ ] Deferred| 35bfb17b7a                               | Group20          |
| `HardwareTestNeeds`                                     | [x] Done    | 5c4c0963af                               | Group4           |
| `HwAttributeDef`                                        | [x] Done    | 3912963bfd                               | Group7           |
| `HwAttributeLiteralDef`                                 | [x] Done    | 5d767ace9e                               | Group7           |
| `HwAttributeValue`                                      | [x] Done    | 269d34d90f                               | Group7           |
| `HwCategory`                                            | [x] Done    | b7e2199ac8                               | Group7           |
| `HwElement`                                             | [x] Done    | 8c7f05d40a                               | Group1           |
| `HwPin`                                                 | [x] Done    | ff5b0e0865                               | Group1           |
| `HwPinGroup`                                            | [x] Done    | 69afffcc48                               | Group1           |
| `HwPortMapping`                                         | [x] Done    | 7d94510497                               | Group7           |
| `HwType`                                                | [x] Done    | 29f338b3c0                               | Group1           |
| `IPSecConfig`                                           | [ ] Pending | 6c97ddc108                               | Group16          |
| `IPduMapping`                                           | [x] Done    | 9c8e10b37f                               | Group6           |
| `IPv6ExtHeaderFilterList`                               | [ ] Deferred| 2d5b3256b4                               | Group16          |
| `ISignalIPduGroup`                                      | [ ] Deferred| 1e758bd44e                               | Group15          |
| `ISignalMapping`                                        | [ ] Pending | N/A                                      | Group17          |
| `ISignalPort`                                           | [ ] Deferred| b5f92f4b28                               | Group15          |
| `IcmpRule`                                              | [x] Deferred| 5ddaf1cf94                               | Group20          |
| `IdentCaption`                                          | [x] Done    | 2dd2f91845                               | Group1           |
| `Identifiable`                                          | [x] Done    | c17bfbf60f                               | Group1           |
| `IdsMgrCustomTimestampNeeds`                            | [x] Done    | b65fe94222                               | Group5           |
| `IdsPlatformInstantiation`                              | [x] Done    | 5d4cc1c454                               | Group7           |
| `IdsmModuleInstantiation`                               | [x] Done    | 5d4cc1c454                               | Group7           |
| `Implementation`                                        | [x] Done    | e7dfb875d9                               | Group1           |
| `ImplementationDataTypeElement`                         | [x] Done    | 8e9b2db86b                               | Group10          |
| `ImplementationProps`                                   | [x] Done    | 3166f6e5d0                               | Group10          |
| `IncludedModeDeclarationGroupSet`                       | [x] Done    | b9ac782d1e                               | Group2           |
| `IndexedArrayElement`                                   | [ ] Pending | N/A                                      | Group17          |
| `InitEvent`                                             | [x] Done    | 64ab725d50                               | Group2           |
| `InitialSdDelayConfig`                                  | [ ] Deferred| d7240be740                               | Group16          |
| `InnerPortGroupInCompositionInstanceRef`                | [x] Done    | 919fbc0d11                               | Group2           |
| `InstantiationDataDefProps`                             | [ ] Deferred| N/A                                      | Group10          |
| `IntegerValueVariationPoint`                            | [x] Done    | d5c96fd954                               | Group8           |
| `InternalTriggerOccurredEvent`                          | [ ] Deferred| N/A                                      | Group12          |
| `InternalTriggeringPoint`                               | [ ] Deferred| N/A                                      | Group12          |
| `InterpolationRoutine`                                  | [x] Done    | 992a894be3                               | Group5           |
| `InterpolationRoutineMapping`                           | [x] Done    | d00d57b42d                               | Group5           |
| `InterpolationRoutineMappingSet`                        | [x] Done    | f3152abb23                               | Group5           |
| `InvalidationPolicy`                                    | [x] Done    | 1000053d88                               | Group1           |
| `IpAddressKeepEnum`                                     | [ ] Deferred| c5bb322323                               | Group16          |
| `Ipv4AddressSourceEnum`                                 | [ ] Deferred| 6c97ddc108                               | Group16          |
| `Ipv4Configuration`                                     | [ ] Deferred| 6c97ddc108                               | Group16          |
| `Ipv4Rule`                                              | [x] Deferred| b4096068d6                               | Group20          |
| `Ipv6AddressSourceEnum`                                 | [ ] Deferred| c5bb322323                               | Group16          |
| `Ipv6Rule`                                              | [x] Deferred| 18ee06b97c                               | Group20          |
| `Item`                                                  | [x] Done    | cf8b43c369                               | Group9           |
| `J1939Cluster`                                          | [x] Done    | 44a70c3256                               | Group5           |
| `J1939DcmDm19Support`                                   | [x] Done    | 839c29d67e                               | Group5           |
| `J1939NmCluster`                                        | [x] Done    | 9c8e10b37f                               | Group6           |
| `J1939NmEcu`                                            | [x] Done    | 9c8e10b37f                               | Group6           |
| `J1939RmIncomingRequestServiceNeeds`                    | [x] Done    | 9784766a6d                               | Group5           |
| `J1939RmOutgoingRequestServiceNeeds`                    | [x] Done    | 2b39e92976                               | Group5           |
| `J1939SharedAddressCluster`                             | [x] Done    | d3dc82098e                               | Group5           |
| `KeepWithPreviousEnum`                                  | [x] Done    | d447cf2a51                               | Group3           |
| `Keyword`                                               | [x] Done    | 4ed5a2fe2d                               | Group7           |
| `KeywordSet`                                            | [x] Done    | a6a1d31ccc                               | Group7           |
| `LGraphic`                                              | [x] Done    | e4b1acf6c9                               | Group3           |
| `LOverviewParagraph`                                    | [x] Done    | 764ef1c589                               | Group9           |
| `LParagraph`                                            | [x] Done    | 7fa4a01f74                               | Group3           |
| `LPlainText`                                            | [x] Done    | 1de91de480                               | Group9           |
| `LVerbatim`                                             | [x] Done    | d616f3d1ef                               | Group9           |
| `LifeCycleInfo`                                         | [x] Done    | 5836e6eb08                               | Group8           |
| `LifeCycleInfoSet`                                      | [x] Done    | 11bd9cd848                               | Group8           |
| `LifeCyclePeriod`                                       | [x] Done    | b572582c11                               | Group8           |
| `LimitValueVariationPoint`                              | [x] Done    | d5c96fd954                               | Group8           |
| `LinCommunicationConnector`                             | [ ] Pending | N/A                                      | Group17          |
| `LinScheduleTable`                                      | [ ] Pending | N/A                                      | Group17          |
| `LinTpConnection`                                       | [ ] Pending | N/A                                      | Group18          |
| `Linker`                                                | [x] Done    | 20003dc3cc                               | Group1           |
| `ListEnum`                                              | [x] Done    | 0623068af8                               | Group9           |
| `LogTraceDefaultLogLevelEnum`                           | [x] Done    | f1eb819e47                               | Group5           |
| `MacAddressString`                                      | [x] Deferred| 1fd0b00607                               | Group20          |
| `MacMulticastGroup`                                     | [ ] Deferred| b1e4750b14                               | Group16          |
| `Map`                                                   | [x] Done    | 43ec8ade8c                               | Group3           |
| `MeasuredStackUsage`                                    | [ ] Deferred| adc2e5eeb7                               | Group20          |
| `MemorySection`                                         | [ ] Deferred| a579a3592e                               | Group20          |
| `MetaDataItem`                                          | [x] Done    | e69a025254                               | Group2           |
| `MetaDataItemSet`                                       | [x] Done    | e69a025254                               | Group2           |
| `MimeTypeString`                                        | [x] Done    | 01cc23df4e                               | Group3           |
| `MixedContentForOverviewParagraph`                      | [x] Done    | 18b494eba5                               | Group8           |
| `MixedContentForParagraph`                              | [x] Done    | bf9114cb01                               | Group3           |
| `MixedContentForPlainText`                              | [x] Done    | 4a95d1d305                               | Group8           |
| `MixedContentForUnitNames`                              | [x] Done    | 3d47eb65c8                               | Group8           |
| `MixedContentForVerbatim`                               | [x] Done    | 74549e6a51                               | Group8           |
| `MlFigure`                                              | [x] Done    | 9225ed1572                               | Group3           |
| `ModeAccessPoint`                                       | [ ] Deferred| N/A                                      | Group12          |
| `ModeAccessPointIdent`                                  | [x] Done    | 918013a6ce                               | Group1           |
| `ModeActivationKind`                                    | [ ] Deferred| N/A                                      | Group11          |
| `ModeDeclarationGroupPrototype`                         | [x] Done    | 51f2e1155f                               | Group1           |
| `ModeDeclarationGroupPrototypeMapping`                  | [ ] Deferred| N/A                                      | Group11          |
| `ModeDeclarationMappingSet`                             | [x] Done    | eeec29b637                               | Group1           |
| `ModeDrivenTransmissionModeCondition`                   | [x] Done    | 206cf29517                               | Group5           |
| `ModeGroupInAtomicSwcInstanceRef`                       | [ ] Deferred| 74e821ccb8                               | Group11          |
| `ModeInSwcBswInstanceRef`                               | [x] Done    | 71ca6a5415                               | Group8           |
| `ModeInSwcInstanceRef`                                  | [x] Done    | 70dcc26975                               | Group8           |
| `ModeInterfaceMapping`                                  | [ ] Deferred| 8832375592                               | Group11          |
| `ModeRequestTypeMap`                                    | [ ] Deferred| N/A                                      | Group11          |
| `ModeSwitchEventTriggeredActivity`                      | [ ] Deferred| N/A                                      | Group10          |
| `ModeSwitchPoint`                                       | [ ] Deferred| N/A                                      | Group12          |
| `ModeSwitchReceiverComSpec`                             | [x] Done    | 67324d240c                               | Group10          |
| `ModeSwitchSenderComSpec`                               | [ ] Deferred| N/A                                      | Group10          |
| `ModeSwitchedAckRequest`                                | [x] Done    | f587d873eb                               | Group10          |
| `Modification`                                          | [x] Done    | 008307967e                               | Group9           |
| `ModuleConfiguration`                                   | [ ] Pending | N/A                                      | Group19          |
| `MsrQueryChapter`                                       | [x] Done    | 50103018c3                               | Group3           |
| `MsrQueryP1`                                            | [x] Done    | 8da723c461                               | Group3           |
| `MsrQueryResultChapter`                                 | [x] Done    | fb505d3551                               | Group3           |
| `MsrQueryResultTopic1`                                  | [x] Done    | 09314bd3ad                               | Group3           |
| `MsrQueryTopic1`                                        | [x] Done    | a09f0cdfbf                               | Group3           |
| `MultiLanguageParagraph`                                | [x] Done    | 77074563dc                               | Group3           |
| `MultidimensionalTime`                                  | [x] Done    | b572582c11                               | Group8           |
| `MultilanguageLongName`                                 | [x] Done    | 87855dea47                               | Group3           |
| `MultilanguageReferrable`                               | [x] Done    | 7c7157a02b                               | Group1           |
| `MultiplexedIPdu`                                       | [ ] Deferred| eba346cb51                               | Group15          |
| `MultiplexedPart`                                       | [ ] Deferred| 66512d0602                               | Group15          |
| `NameTokens`                                            | [x] Done    | c8a3ff507d                               | Group3           |
| `NetworkEndpoint`                                       | [ ] Deferred| 6c97ddc108                               | Group16          |
| `NetworkEndpointAddress`                                | [x] Done    | c052de0226                               | Group6           |
| `NetworkLayerRule`                                      | [ ] Deferred| 529858d9c9                               | Group20          |
| `NmCluster`                                             | [x] Done    | ae48471063                               | Group6           |
| `NmClusterCoupling`                                     | [x] Done    | 9c8e10b37f                               | Group6           |
| `NmConfig`                                              | [x] Done    | 757aea1d17                               | Group6           |
| `NmEcu`                                                 | [ ] Pending | N/A                                      | Group18          |
| `NumericalValueSpecification`                           | [x] Done    | b16a369151                               | Group9           |
| `NumericalValueVariationPoint`                          | [x] Done    | d5c96fd954                               | Group8           |
| `NvBlockDataMapping`                                    | [ ] Deferred| N/A                                      | Group10          |
| `NvBlockDescriptor`                                     | [ ] Deferred| N/A                                      | Group10          |
| `NvBlockNeeds`                                          | [ ] Deferred| N/A                                      | Group10          |
| `NvBlockNeedsReliabilityEnum`                           | [ ] Deferred| N/A                                      | Group10          |
| `NvBlockNeedsWritingPriorityEnum`                       | [ ] Deferred| N/A                                      | Group10          |
| `NvDataInterface`                                       | [x] Done    | 1d666bc11b                               | Group1           |
| `NvProvideComSpec`                                      | [ ] Deferred| N/A                                      | Group10          |
| `NvRequireComSpec`                                      | [ ] Deferred| N/A                                      | Group10          |
| `OffsetTimingConstraint`                                | [x] Done    | e305e80e2a                               | Group8           |
| `OperationInAtomicSwcInstanceRef`                       | [ ] Deferred| 74e821ccb8                               | Group11          |
| `OperationInSystemInstanceRef`                          | [x] Done    | 4e0c3cbe68                               | Group5           |
| `OperationInvokedEvent`                                 | [ ] Deferred| N/A                                      | Group12          |
| `OrderedMaster`                                         | [x] Done    | 5d62450236                               | Group6           |
| `OrientEnum`                                            | [x] Done    | 9223f504b5                               | Group3           |
| `OsTaskPreemptabilityEnum`                              | [x] Done    | c53a7febdc                               | Group5           |
| `OsTaskProxy`                                           | [x] Done    | 61ccaa68eb                               | Group5           |
| `PModeGroupInAtomicSwcInstanceRef`                      | [ ] Deferred| 74e821ccb8                               | Group11          |
| `POperationInAtomicSwcInstanceRef`                      | [ ] Deferred| 74e821ccb8                               | Group11          |
| `PPortInCompositionInstanceRef`                         | [ ] Deferred| 74e821ccb8                               | Group11          |
| `PPortPrototype`                                        | [x] Done    | 0927333086                               | Group2           |
| `PRPortPrototype`                                       | [x] Done    | 043de7436d                               | Group2           |
| `PTriggerInAtomicSwcTypeInstanceRef`                    | [ ] Deferred| 74e821ccb8                               | Group11          |
| `PackageableElement`                                    | [x] Done    | bb032ddd55                               | Group1           |
| `Paginateable`                                          | [x] Done    | 20e6ee88d0                               | Group3           |
| `ParameterAccess`                                       | [ ] Deferred| N/A                                      | Group12          |
| `ParameterInterface`                                    | [x] Done    | 6bf99879eb                               | Group1           |
| `ParameterRequireComSpec`                               | [ ] Deferred| N/A                                      | Group10          |
| `PayloadBytePatternRule`                                | [ ] Deferred| 8f863fe9dd                               | Group20          |
| `PayloadBytePatternRulePart`                            | [x] Deferred| 8c72c71709                               | Group20          |
| `PduCollectionSemanticsEnum`                            | [ ] Deferred| 4b7c8dc79c                               | Group16          |
| `PduCollectionTriggerEnum`                              | [x] Done    | 64d125ffae                               | Group5           |
| `PduMappingDefaultValue`                                | [x] Done    | 9c8e10b37f                               | Group6           |
| `PdurIPduGroup`                                         | [x] Done    | c53a7febdc                               | Group5           |
| `PerInstanceMemory`                                     | [x] Done    | f35aa0cd0a                               | Group2           |
| `PerInstanceMemorySize`                                 | [x] Done    | df36bbb1fa                               | Group10          |
| `PlatformModuleEthernetEndpointConfiguration`           | [x] Done    | 5d4cc1c454                               | Group7           |
| `PncGatewayTypeEnum`                                    | [ ] Deferred| 7c137656f6                               | Group15          |
| `PortAPIOption`                                         | [x] Done    | 7c67628122                               | Group2           |
| `PortDefinedArgumentValue`                              | [x] Done    | 7fc79e4b73                               | Group2           |
| `PortGroup`                                             | [x] Done    | d6512dbbec                               | Group2           |
| `PortGroupInSystemInstanceRef`                          | [x] Done    | 19c327cca6                               | Group5           |
| `PortInCompositionTypeInstanceRef`                      | [x] Done    | a6d84b2601                               | Group2           |
| `PortInterfaceBlueprintMapping`                         | [x] Done    | aec046b9cc                               | Group1           |
| `PortInterfaceMapping`                                  | [x] Done    | ca6a372382                               | Group1           |
| `PortInterfaceMappingSet`                               | [x] Done    | 5aa1b7460c                               | Group2           |
| `PortPrototype`                                         | [x] Done    | 74e4c8242f                               | Group1           |
| `PortPrototypeBlueprint`                                | [x] Done    | 8782a8ffe8                               | Group7           |
| `PortPrototypeBlueprintInitValue`                       | [x] Done    | 57509a2e7d                               | Group7           |
| `PortPrototypeBlueprintMapping`                         | [x] Done    | f87babf31b                               | Group1           |
| `PositiveIntegerValueVariationPoint`                    | [x] Done    | d5c96fd954                               | Group8           |
| `PostBuildVariantCondition`                             | [x] Done    | 5333bec027                               | Group8           |
| `PostBuildVariantCriterion`                             | [x] Done    | 5333bec027                               | Group8           |
| `PostBuildVariantCriterionValue`                        | [x] Done    | 8af1088fd2                               | Group8           |
| `PrivacyLevel`                                          | [x] Done    | fb222ae5b2                               | Group5           |
| `PrmChar`                                               | [x] Done    | 8be54a00d1                               | Group9           |
| `PrmCharAbsTol`                                         | [x] Done    | e6c467d5f8                               | Group9           |
| `PrmCharContents`                                       | [x] Done    | 9494a593a2                               | Group9           |
| `PrmCharMinTypMax`                                      | [x] Done    | 376f43f648                               | Group9           |
| `PrmCharNumericalContents`                              | [x] Done    | 51ded41bf8                               | Group9           |
| `PrmCharNumericalValue`                                 | [x] Done    | 2f1c852dbb                               | Group9           |
| `PrmCharTextualContents`                                | [x] Done    | 83a56461a1                               | Group9           |
| `Prms`                                                  | [x] Done    | f05d3afdfa                               | Group9           |
| `ProgramminglanguageEnum`                               | [x] Done    | be79d7993b                               | Group1           |
| `QueuedReceiverComSpec`                                 | [ ] Deferred| N/A                                      | Group10          |
| `QueuedSenderComSpec`                                   | [x] Done    | 4a7d82ffc7                               | Group5           |
| `RModeGroupInAtomicSWCInstanceRef`                      | [ ] Deferred| 74e821ccb8                               | Group11          |
| `RModeInAtomicSwcInstanceRef`                           | [ ] Deferred| 74e821ccb8                               | Group11          |
| `ROperationInAtomicSwcInstanceRef`                      | [ ] Deferred| 74e821ccb8                               | Group11          |
| `RPortInCompositionInstanceRef`                         | [ ] Deferred| 74e821ccb8                               | Group11          |
| `RPortPrototype`                                        | [x] Done    | 2cd6f3c46e                               | Group2           |
| `RTEEvent`                                              | [x] Done    | f0483d5732                               | Group2           |
| `RVariableInAtomicSwcInstanceRef`                       | [ ] Deferred| 74e821ccb8                               | Group11          |
| `RamBlockStatusControlEnum`                             | [ ] Deferred| N/A                                      | Group10          |
| `ReceptionComSpecProps`                                 | [x] Done    | 0ba890ba88                               | Group10          |
| `RecordLayoutIteratorPoint`                             | [x] Done    | 2acaf7a45f                               | Group3           |
| `RecordValueSpecification`                              | [x] Done    | b1c7030b10                               | Group3           |
| `ReentrancyLevelEnum`                                   | [x] Done    | 286c7c5870                               | Group10          |
| `Ref`                                                   | [x] Done    | 0518a7bca2                               | Group3           |
| `ReferenceBase`                                         | [x] Done    | 192dfd9467                               | Group1           |
| `RequestResponseDelay`                                  | [ ] Deferred| d7240be740                               | Group16          |
| `ResolutionPolicyEnum`                                  | [x] Done    | f0a7460898                               | Group3           |
| `ResourceConsumption`                                   | [x] Done    | 0404020952                               | Group1           |
| `ResumePosition`                                        | [ ] Pending | N/A                                      | Group17          |
| `RoleBasedDataAssignment`                               | [ ] Deferred| N/A                                      | Group10          |
| `RoleBasedPortAssignment`                               | [ ] Deferred| N/A                                      | Group10          |
| `RootSwCompositionPrototype`                            | [x] Done    | 671dfc3835                               | Group1           |
| `RoughEstimateStackUsage`                               | [ ] Deferred| 3db474b11a                               | Group20          |
| `Row`                                                   | [x] Done    | b43b860105                               | Group3           |
| `RteEventInEcuInstanceRef`                              | [ ] Deferred| N/A                                      | Group12          |
| `RtePluginProps`                                        | [x] Done    | ec7fa0b5df                               | Group6           |
| `RunnableEntityArgument`                                | [x] Done    | 3857c2a435                               | Group2           |
| `RuntimeAddressConfigurationEnum`                       | [ ] Deferred| c5bb322323                               | Group16          |
| `SOMEIPMessageTypeEnum`                                 | [x] Done    | b163080753                               | Group6           |
| `SOMEIPTransformationISignalProps`                      | [x] Done    | 55ff2098b4                               | Group6           |
| `ScaleConstrValidityEnum`                               | [x] Done    | 1bc8904eee                               | Group9           |
| `SdClientConfig`                                        | [x] Done    | 8e0c8857ad                               | Group7           |
| `SdServerConfig`                                        | [ ] Deferred| d7240be740                               | Group16          |
| `SecOcCryptoServiceMapping`                             | [ ] Pending | N/A                                      | Group18          |
| `SectionNamePrefix`                                     | [ ] Deferred| 0e26482636                               | Group20          |
| `SecuredIPdu`                                           | [ ] Deferred| 0a98655a06                               | Group15          |
| `SecuredPduHeaderEnum`                                  | [ ] Pending | 3d5cb55dbe                               | Group15          |
| `SegmentPosition`                                       | [ ] Deferred| 9546cf291b                               | Group15          |
| `SenderRecArrayTypeMapping`                             | [x] Done    | 757aea1d17                               | Group6           |
| `SenderRecCompositeTypeMapping`                         | [x] Done    | 757aea1d17                               | Group6           |
| `SenderRecRecordElementMapping`                         | [ ] Pending | N/A                                      | Group17          |
| `SenderRecRecordTypeMapping`                            | [ ] Pending | N/A                                      | Group17          |
| `SenderReceiverInterface`                               | [x] Done    | e4e4770fb7                               | Group1           |
| `SenderReceiverToSignalGroupMapping`                    | [ ] Pending | N/A                                      | Group17          |
| `SenderReceiverToSignalMapping`                         | [ ] Pending | N/A                                      | Group17          |
| `ServerCallPoint`                                       | [x] Done    | 774620a3b1                               | Group2           |
| `ServiceDiagnosticRelevanceEnum`                        | [ ] Deferred| 28746ce3cc                               | Group14          |
| `ServiceNeeds`                                          | [x] Done    | 5fd6271d70                               | Group4           |
| `ServiceProxySwComponentType`                           | [x] Done    | 74e821ccb8                               | Group11          |
| `ShortNameFragment`                                     | [x] Done    | 519d505393                               | Group8           |
| `ShowContentEnum`                                       | [x] Done    | e89003bb5b                               | Group3           |
| `ShowResourceAliasNameEnum`                             | [x] Done    | 3a68e97234                               | Group3           |
| `ShowResourceCategoryEnum`                              | [x] Done    | d7cd8c5881                               | Group3           |
| `ShowResourceLongNameEnum`                              | [x] Done    | 835b8aa103                               | Group3           |
| `ShowResourceNumberEnum`                                | [x] Done    | 6f56251392                               | Group3           |
| `ShowResourcePageEnum`                                  | [x] Done    | 54f4f3e5d6                               | Group3           |
| `ShowResourceShortNameEnum`                             | [x] Done    | e2e2c300e5                               | Group3           |
| `ShowResourceTypeEnum`                                  | [x] Done    | 447709b7f1                               | Group3           |
| `ShowSeeEnum`                                           | [x] Done    | 5d48c2a6f3                               | Group3           |
| `SignalServiceTranslationElementProps`                  | [ ] Deferred| 29d09fc625                               | Group14          |
| `SingleLanguageLongName`                                | [x] Done    | 8aaa2657f3                               | Group3           |
| `SingleLanguageReferrable`                              | [x] Done    | a5910c1bf5                               | Group3           |
| `SingleLanguageUnitNames`                               | [x] Done    | d42795c169                               | Group8           |
| `SlOverviewParagraph`                                   | [x] Done    | 951209dbab                               | Group8           |
| `SlParagraph`                                           | [x] Done    | b7748b3e50                               | Group3           |
| `SoAdRoutingGroup`                                      | [ ] Deferred| 89363ebe2b                               | Group20          |
| `SocketConnectionBundle`                                | [ ] Deferred| 4b7c8dc79c                               | Group16          |
| `SocketConnectionIpduIdentifier`                        | [ ] Deferred| 4b7c8dc79c                               | Group16          |
| `SoftwareContext`                                       | [ ] Deferred| 23884479e9                               | Group20          |
| `SomeipProtocolRule`                                    | [ ] Deferred| c18aa8d400                               | Group20          |
| `SomeipSdRule`                                          | [ ] Deferred| 17b563a730                               | Group20          |
| `StackUsage`                                            | [ ] Deferred| 9ce364e249                               | Group20          |
| `StandardNameEnum`                                      | [x] Done    | 9a9ffdae8d                               | Group1           |
| `StaticPart`                                            | [x] Done    | 206cf29517                               | Group5           |
| `Std`                                                   | [x] Done    | c53a240809                               | Group3           |
| `StructuredReq`                                         | [x] Done    | d311fc7ce0                               | Group1           |
| `SubElementMapping`                                     | [x] Done    | 5eadca7853                               | Group1           |
| `SubElementRef`                                         | [x] Done    | 47b3052188                               | Group1           |
| `SupervisedEntityCheckpointNeeds`                       | [x] Done    | 67640c8035                               | Group4           |
| `SupportBufferLockingEnum`                              | [x] Done    | 7c67628122                               | Group2           |
| `SwAxisGrouped`                                         | [x] Done    | 12a2e0170b                               | Group3           |
| `SwAxisIndividual`                                      | [x] Done    | 842e1e4227                               | Group3           |
| `SwCalprmAxisSet`                                       | [x] Done    | 9209b83ea0                               | Group3           |
| `SwComponentPrototype`                                  | [x] Done    | ff993a74c8                               | Group1           |
| `SwComponentPrototypeAssignment`                        | [x] Done    | 88070878ea                               | Group5           |
| `SwGenericAxisParamType`                                | [x] Done    | 1eacd1a7a7                               | Group3           |
| `SwImplPolicyEnum`                                      | [x] Done    | d6945a4c8a                               | Group9           |
| `SwRecordLayout`                                        | [x] Done    | f8149880de                               | Group3           |
| `SwRecordLayoutGroup`                                   | [x] Done    | 2acaf7a45f                               | Group3           |
| `SwRecordLayoutGroupContent`                            | [x] Done    | 0f19d490d3                               | Group3           |
| `SwRecordLayoutV`                                       | [x] Done    | 9c0c3f85f8                               | Group3           |
| `SwSystemconst`                                         | [x] Done    | 984387dd0c                               | Group9           |
| `SwSystemconstDependentFormula`                         | [x] Done    | f05e21d49e                               | Group8           |
| `SwSystemconstValue`                                    | [x] Done    | 5333bec027                               | Group8           |
| `SwValueCont`                                           | [x] Done    | 6db47de6aa                               | Group3           |
| `SwcBswMapping`                                         | [x] Done    | 58b2c68a57                               | Group1           |
| `SwcBswRunnableMapping`                                 | [ ] Deferred| c52cece662                               | Group13          |
| `SwcBswSynchronizedModeGroupPrototype`                  | [ ] Deferred| 659c2bf174                               | Group13          |
| `SwcBswSynchronizedTrigger`                             | [ ] Deferred| 6b4b9d6d10                               | Group13          |
| `SwcImplementation`                                     | [x] Done    | 6eae95f556                               | Group10          |
| `SwcInternalBehavior`                                   | [x] Done    | 4043dc013a                               | Group2           |
| `SwcSupportedFeature`                                   | [x] Done    | 7c67628122                               | Group2           |
| `SwcToEcuMapping`                                       | [ ] Pending | N/A                                      | Group18          |
| `SwcToImplMapping`                                      | [ ] Pending | N/A                                      | Group18          |
| `SymbolProps`                                           | [x] Done    | 2d21a9108b                               | Group2           |
| `SyncTimeBaseMgrUserNeeds`                              | [x] Done    | 609f148a93                               | Group4           |
| `SynchronizationTimingConstraint`                       | [x] Done    | e305e80e2a                               | Group8           |
| `SynchronousServerCallPoint`                            | [x] Done    | 9182987d97                               | Group2           |
| `System`                                                | [x] Done    | ccfb528daf                               | Group5           |
| `SystemSignal`                                          | [ ] Deferred| 7c5d9e9d81                               | Group15          |
| `TDEventVfb`                                            | [x] Done    | 18eb225f40                               | Group8           |
| `Table`                                                 | [x] Done    | e347fbbfa2                               | Group3           |
| `TableSeparatorString`                                  | [x] Done    | 211031ea0f                               | Group3           |
| `TargetIPduRef`                                         | [ ] Pending | N/A                                      | Group17          |
| `Tbody`                                                 | [x] Done    | 004d3f1259                               | Group3           |
| `TcpIpIcmpv4Props`                                      | [x] Done    | 2cf38be61d                               | Group5           |
| `TcpIpIcmpv6Props`                                      | [x] Done    | c53a7febdc                               | Group5           |
| `TcpOptionFilterList`                                   | [ ] Deferred| 2d5b3256b4                               | Group16          |
| `TcpOptionFilterSet`                                    | [ ] Deferred| 2d5b3256b4                               | Group16          |
| `TcpProps`                                              | [x] Done    | d2d5c40a16                               | Group5           |
| `TcpRule`                                               | [x] Deferred| d3902d0e67                               | Group20          |
| `TcpTp`                                                 | [ ] Deferred| N/A                                      | Group16          |
| `TcpUdpConfig`                                          | [x] Done    | 757aea1d17                               | Group6           |
| `TextTableMapping`                                      | [x] Done    | be79d7993b                               | Group1           |
| `TextValueSpecification`                                | [x] Done    | 81588f449e                               | Group9           |
| `Tgroup`                                                | [x] Done    | 278d4674f3                               | Group3           |
| `TimeRangeType`                                         | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `TimeRangeTypeTolerance`                                | [ ] Pending | dcbc6abdb3                               | Group15          |
| `TimeSyncClientConfiguration`                           | [x] Done    | a032fa05dc                               | Group6           |
| `TimeSyncServerConfiguration`                           | [ ] Deferred| b1e4750b14                               | Group16          |
| `TimeSynchronization`                                   | [ ] Deferred| b1e4750b14                               | Group16          |
| `TimeValueValueVariationPoint`                          | [x] Done    | d5c96fd954                               | Group8           |
| `TimingDescriptionEventChain`                           | [x] Done    | ea1a75e5b9                               | Group8           |
| `TlsCryptoCipherSuite`                                  | [x] Done    | 67315ec0a9                               | Group6           |
| `TlsCryptoCipherSuiteProps`                             | [x] Done    | 648b40acaf                               | Group6           |
| `TlsCryptoServiceMapping`                               | [x] Done    | 67315ec0a9                               | Group6           |
| `TlsPskIdentity`                                        | [x] Done    | 16c2791a2b                               | Group6           |
| `TlsVersionEnum`                                        | [x] Done    | d969a0ddc1                               | Group6           |
| `TlvDataIdDefinition`                                   | [x] Done    | 27ea0743dc                               | Group6           |
| `TlvDataIdDefinitionSet`                                | [x] Done    | f0c9473162                               | Group6           |
| `TopicContent`                                          | [x] Done    | 6d7e325736                               | Group3           |
| `TopicContentOrMsrQuery`                                | [x] Done    | 460218682e                               | Group9           |
| `TpAddress`                                             | [ ] Pending | N/A                                      | Group18          |
| `TpPort`                                                | [ ] Deferred| b1e4750b14                               | Group16          |
| `TraceableTable`                                        | [x] Done    | fa79c73df5                               | Group3           |
| `TraceableText`                                         | [x] Done    | 9e80479bda                               | Group1           |
| `TransferPropertyEnum`                                  | [ ] Pending | e6baac031c                               | Group15          |
| `TransformationISignalProps`                            | [x] Done    | 757aea1d17                               | Group6           |
| `TransmissionModeCondition`                             | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `TransmissionModeDeclaration`                           | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `TransmissionModeTiming`                                | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `TransportLayerRule`                                    | [ ] Deferred| cb197c6b8b                               | Group20          |
| `TransportProtocolConfiguration`                        | [x] Done    | 0014960828                               | Group6           |
| `Trigger`                                               | [x] Done    | 131473204c                               | Group1           |
| `TriggerIPduSendCondition`                              | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `TriggerInAtomicSwcInstanceRef`                         | [ ] Deferred| 74e821ccb8                               | Group11          |
| `TriggerInterface`                                      | [x] Done    | cf9c6ac4cc                               | Group1           |
| `TriggerInterfaceMapping`                               | [x] Done    | 49f19e8feb                               | Group1           |
| `TriggerMapping`                                        | [x] Done    | 905c48d323                               | Group1           |
| `TriggerMode`                                           | [ ] Pending | cc609f42a3                               | Group15          |
| `UdpNmCluster`                                          | [ ] Pending | N/A                                      | Group18          |
| `UdpNmClusterCoupling`                                  | [ ] Pending | N/A                                      | Group18          |
| `UdpNmEcu`                                              | [x] Done    | 9c8e10b37f                               | Group6           |
| `UdpNmNode`                                             | [ ] Pending | N/A                                      | Group18          |
| `UdpProps`                                              | [x] Done    | ecb15e901f                               | Group5           |
| `UdpRule`                                               | [x] Deferred| 29cbfb7bbd                               | Group20          |
| `UdpTp`                                                 | [ ] Deferred| N/A                                      | Group16          |
| `UnitGroup`                                             | [x] Done    | e7fdb07f2b                               | Group9           |
| `UnlimitedIntegerValueVariationPoint`                   | [x] Done    | d5c96fd954                               | Group8           |
| `Url`                                                   | [x] Done    | 4b96ab8d89                               | Group3           |
| `UserDefinedIPdu`                                       | [ ] Pending | N/A                                      | Group15          |
| `UserDefinedPdu`                                        | [ ] Pending | N/A                                      | Group15          |
| `UserDefinedTransformationComSpecProps`                 | [x] Done    | 4a7d82ffc7                               | Group5           |
| `UserDefinedTransformationISignalProps`                 | [x] Done    | 301182769c                               | Group6           |
| `V2xDataManagerNeeds`                                   | [x] Done    | e02dc71234                               | Group5           |
| `V2xFacUserNeeds`                                       | [x] Done    | 029aa70113                               | Group5           |
| `V2xMUserNeeds`                                         | [x] Done    | d45912e177                               | Group5           |
| `ValignEnum`                                            | [x] Done    | 52d3272bbb                               | Group3           |
| `VariableAccess`                                        | [ ] Deferred| N/A                                      | Group12          |
| `VariableAccessInEcuInstanceRef`                        | [ ] Deferred| N/A                                      | Group12          |
| `VariableAndParameterInterfaceMapping`                  | [ ] Deferred| de2d5fe918                               | Group11          |
| `VariableDataPrototype`                                 | [x] Done    | d3b5d680e2                               | Group2           |
| `VariableDataPrototypeInSystemInstanceRef`              | [x] Done    | 1b3d673dac                               | Group7           |
| `VariableInAtomicSWCTypeInstanceRef`                    | [x] Done    | c8ac9ef7de                               | Group2           |
| `VariableInAtomicSwcInstanceRef`                        | [x] Done    | 0369005450                               | Group2           |
| `VariationPoint`                                        | [x] Done    | d4fce975d6                               | Group8           |
| `VendorSpecificServiceNeeds`                            | [x] Done    | a25f9a7718                               | Group5           |
| `ViewTokens`                                            | [x] Done    | 82c86af789                               | Group3           |
| `VlanConfig`                                            | [ ] Deferred| b1e4750b14                               | Group16          |
| `VlanMembership`                                        | [x] Done    | ed6ed2a65f                               | Group6           |
| `WarningIndicatorRequestedBitNeeds`                     | [x] Done    | 1cd8edd8fd                               | Group5           |
| `WhitespaceControlled`                                  | [x] Done    | a78d444afb                               | Group8           |
| `WorstCaseStackUsage`                                   | [ ] Deferred| a0cbd41d08                               | Group20          |
| `Xdoc`                                                  | [x] Done    | 294c8aae2c                               | Group3           |
| `Xfile`                                                 | [x] Done    | 7038ce5574                               | Group3           |
| `XmlSpaceEnum`                                          | [x] Done    | ec544e7988                               | Group8           |
| `Xref`                                                  | [x] Done    | db2b4fe059                               | Group3           |
| `XrefTarget`                                            | [x] Done    | 8c9df6638a                               | Group3           |
