# All Sync Todo Classes (Consolidated)

Generated from all Group files in `docs/plan/sync-todo/` — Classes ordered by name with status and commit ID.

**Status legend:** `[x] Done` = 9-step sync complete AND `# Spec verified:`/`# XSD verified:` stamped in src · `[x]`/`[ ] Deferred` = sync complete (Steps 1–8 green) but the stamp is **deferred to a batch 9b user confirmation** · `[ ] Created` = the class exists in src as an empty stub (dependency placeholder) but implementation has not started · `[ ] Implemented` = the class exists in src with members but the queued 9-step sync is not complete · `[ ] Pending` = the class is not available (not defined in src at all). (Deferred set audited 2026-09-27 against the src stamps.)

## Summary

**1923 classes total**

| Status | Classes | Percent |
| --- | --- | --- |
| [x] Done | 576 | 30.0% |
| [x] Deferred | 11 | 0.6% |
| [x] Retired | 0 | 0.0% |
| [ ] Deferred | 212 | 11.0% |
| [ ] Implemented | 543 | 28.2% |
| [ ] Created | 579 | 30.1% |
| [ ] Pending | 2 | 0.1% |

| Class Name                                              | Status      | Commit ID                                | Groups           |
| ------------------------------------------------------- | ------------| ---------------------------------------- | ---------------- |
| `ARElement`                                             | [x] Done    | 61c85fa794                               | Group1           |
| `ARList`                                                | [x] Done    | 2151ca0302                               | Group9           |
| `ARObject`                                              | [x] Done    | 78ae363c75                               | Group1           |
| `ARPackage`                                             | [x] Done    | 360648178f                               | Group1           |
| `AUTOSAR`                                               | [x] Done    | 74f4d3c80a                               | Group1           |
| `AbsoluteTolerance`                                     | [ ] Created | N/A                                      | Group31          |
| `AbstractAccessPoint`                                   | [x] Done    | e3d1262da1                               | Group22          |
| `AbstractCanCluster`                                    | [ ] Implemented| N/A                                      | Group29          |
| `AbstractCanCommunicationConnector`                     | [ ] Implemented| N/A                                      | Group29          |
| `AbstractCanCommunicationController`                    | [ ] Implemented| N/A                                      | Group29          |
| `AbstractCanCommunicationControllerAttributes`          | [ ] Implemented| N/A                                      | Group29          |
| `AbstractCanPhysicalChannel`                            | [ ] Implemented| N/A                                      | Group29          |
| `AbstractClassTailoring`                                | [ ] Created | N/A                                      | Group36          |
| `AbstractCondition`                                     | [ ] Created | N/A                                      | Group36          |
| `AbstractDoIpLogicAddressProps`                         | [x] Done    | 64d125ffae                               | Group7           |
| `AbstractEnumerationValueVariationPoint`                | [x] Done    | 0518a7bca2                               | Group8           |
| `AbstractEthernetFrame`                                 | [x] Done    | cba67817b3                               | Group6           |
| `AbstractEvent`                                         | [ ] Implemented| N/A                                      | Group28          |
| `AbstractGlobalTimeDomainProps`                         | [ ] Created | N/A                                      | Group34          |
| `AbstractImplementationDataType`                        | [x] Done    | 9b5379d3e3                               | Group1           |
| `AbstractImplementationDataTypeElement`                 | [x] Done    | cabd5469e9                               | Group1           |
| `AbstractMultiplicityRestriction`                       | [ ] Created | N/A                                      | Group36          |
| `AbstractNumericalVariationPoint`                       | [x] Done    | d5c96fd954                               | Group8           |
| `AbstractProvidedPortPrototype`                         | [x] Done    | 510d31dd57                               | Group11          |
| `AbstractRequiredPortPrototype`                         | [x] Done    | bbacb3368c                               | Group11          |
| `AbstractRuleBasedValueSpecification`                   | [ ] Implemented| N/A                                      | Group28          |
| `AbstractSecurityEventFilter`                           | [ ] Created | N/A                                      | Group36          |
| `AbstractServiceInstance`                               | [ ] Implemented| N/A                                      | Group32          |
| `AbstractValueRestriction`                              | [ ] Created | N/A                                      | Group21          |
| `AbstractVariationRestriction`                          | [ ] Created | N/A                                      | Group21          |
| `AccessCount`                                           | [x] Done    | e3d1262da1                               | Group22          |
| `AccessCountSet`                                        | [x] Done    | e3d1262da1                               | Group22          |
| `AclObjectSet`                                          | [ ] Deferred| 11ad22dfad                               | Group22          |
| `AclOperation`                                          | [ ] Deferred| 0eb0409c12                               | Group22          |
| `AclPermission`                                         | [ ] Deferred| 29d7cfc19d                               | Group22          |
| `AclRole`                                               | [ ] Deferred| 8d5c387889                               | Group22          |
| `AclScopeEnum`                                          | [ ] Deferred| dfa53c4352                               | Group22          |
| `AdditionalBindingTimeEnum`                             | [ ] Created | N/A                                      | Group29          |
| `AdminData`                                             | [ ] Implemented| N/A                                      | Group21          |
| `AgeConstraint`                                         | [ ] Implemented| N/A                                      | Group35          |
| `AggregationCondition`                                  | [ ] Created | N/A                                      | Group36          |
| `AggregationTailoring`                                  | [ ] Created | N/A                                      | Group36          |
| `AliasNameAssignment`                                   | [ ] Implemented| N/A                                      | Group23          |
| `AliasNameSet`                                          | [ ] Implemented| N/A                                      | Group23          |
| `AlignEnum`                                             | [x] Done    | fa74a474a5                               | Group3           |
| `AlignmentType`                                         | [ ] Deferred| 6133a30b31                               | Group22          |
| `AnalyzedExecutionTime`                                 | [ ] Implemented| N/A                                      | Group23          |
| `Annotation`                                            | [ ] Implemented| N/A                                      | Group21          |
| `AnyInstanceRef`                                        | [x] Done    | b64a3c317a                               | Group22          |
| `ApiPrincipleEnum`                                      | [x] Done    | c6d2e83f74                               | Group10          |
| `AppOsTaskProxyToEcuTaskProxyMapping`                   | [ ] Deferred| N/A                                      | Group18          |
| `ApplicationArrayDataType`                              | [ ] Implemented| N/A                                      | Group28          |
| `ApplicationArrayElement`                               | [ ] Implemented| N/A                                      | Group28          |
| `ApplicationCompositeDataType`                          | [x] Done    | de9d3fe0a4                               | Group2           |
| `ApplicationCompositeDataTypeSubElementRef`             | [ ] Implemented| N/A                                      | Group27          |
| `ApplicationCompositeElementDataPrototype`              | [x] Done    | 031d5c7848                               | Group2           |
| `ApplicationCompositeElementInPortInterfaceInstanceRef` | [x] Done    | 399b647757                               | Group2           |
| `ApplicationDataType`                                   | [x] Done    | b8d0878d98                               | Group2           |
| `ApplicationDeferredDataType`                           | [x] Done    | abdfbf1d96                               | Group1           |
| `ApplicationEndpoint`                                   | [ ] Implemented| N/A                                      | Group32          |
| `ApplicationEntry`                                      | [ ] Deferred| N/A                                      | Group17          |
| `ApplicationError`                                      | [ ] Implemented| N/A                                      | Group27          |
| `ApplicationInterface`                                  | [ ] Implemented| N/A                                      | Group36          |
| `ApplicationPartition`                                  | [ ] Created | N/A                                      | Group30          |
| `ApplicationPartitionToEcuPartitionMapping`             | [ ] Deferred| N/A                                      | Group18          |
| `ApplicationPrimitiveDataType`                          | [x] Done    | 4a9ccae9b8                               | Group2           |
| `ApplicationRecordDataType`                             | [x] Deferred| 0a06e0fae3                               | Group2           |
| `ApplicationRecordElement`                              | [x] Done    | ae4ed75065                               | Group2           |
| `ApplicationRuleBasedValueSpecification`                | [ ] Implemented| N/A                                      | Group28          |
| `ApplicationSwComponentType`                            | [ ] Implemented| N/A                                      | Group27          |
| `ApplicationValueSpecification`                         | [ ] Implemented| N/A                                      | Group28          |
| `ArParameterInImplementationDataInstanceRef`            | [ ] Created | N/A                                      | Group28          |
| `ArVariableInImplementationDataInstanceRef`             | [x] Done    | 910009eecc                               | Group2           |
| `ArbitraryEventTriggering`                              | [ ] Implemented| N/A                                      | Group35          |
| `Area`                                                  | [x] Done    | c9f2464902                               | Group3           |
| `AreaEnumNohref`                                        | [x] Done    | 1d6f8c0aa9                               | Group3           |
| `AreaEnumShape`                                         | [x] Done    | 966320f6a7                               | Group3           |
| `ArgumentDataPrototype`                                 | [ ] Implemented| N/A                                      | Group27          |
| `ArgumentDirectionEnum`                                 | [x] Done    | 8b7ab62280                               | Group22          |
| `ArrayImplPolicyEnum`                                   | [x] Done    | 700b032789                               | Group10          |
| `ArraySizeHandlingEnum`                                 | [ ] Implemented| N/A                                      | Group28          |
| `ArraySizeSemanticsEnum`                                | [ ] Implemented| N/A                                      | Group28          |
| `ArrayValueSpecification`                               | [x] Done    | 043de7436d                               | Group3           |
| `AsamRecordLayoutSemantics`                             | [x] Done    | 2acaf7a45f                               | Group3           |
| `AssemblySwConnector`                                   | [x] Done    | 2a104a061c                               | Group2           |
| `AssignFrameId`                                         | [ ] Implemented| N/A                                      | Group31          |
| `AssignFrameIdRange`                                    | [ ] Implemented| N/A                                      | Group31          |
| `AssignNad`                                             | [ ] Implemented| N/A                                      | Group31          |
| `AsynchronousServerCallPoint`                           | [x] Done    | 3223dde420                               | Group2           |
| `AsynchronousServerCallResultPoint`                     | [x] Done    | 724f490c7a                               | Group2           |
| `AsynchronousServerCallReturnsEvent`                    | [ ] Deferred| N/A                                      | Group12          |
| `AtomicSwComponentType`                                 | [ ] Implemented| N/A                                      | Group27          |
| `AtpBlueprint`                                          | [x] Done    | 043de7436d                               | Group1           |
| `AtpBlueprintMapping`                                   | [x] Done    | 493e272da6                               | Group1           |
| `AtpBlueprintable`                                      | [x] Done    | b7cf03094f                               | Group1           |
| `AtpClassifier`                                         | [ ] Implemented| N/A                                      | Group21          |
| `AtpDefinition`                                         | [x] Done    | 38eb1e817c                               | Group1           |
| `AtpFeature`                                            | [ ] Implemented| N/A                                      | Group21          |
| `AtpInstanceRef`                                        | [ ] Implemented| N/A                                      | Group21          |
| `AtpPrototype`                                          | [x] Done    | eb4c4bf308                               | Group1           |
| `AtpStructureElement`                                   | [x] Done    | 5eff088fa5                               | Group1           |
| `AtpType`                                               | [x] Done    | 451ad38330                               | Group1           |
| `AttributeCondition`                                    | [ ] Created | N/A                                      | Group36          |
| `AttributeTailoring`                                    | [ ] Created | N/A                                      | Group36          |
| `AttributeValueVariationPoint`                          | [x] Done    | d5c96fd954                               | Group8           |
| `AutoCollectEnum`                                       | [x] Done    | 75f4005552                               | Group1           |
| `AutosarDataPrototype`                                  | [ ] Implemented| N/A                                      | Group28          |
| `AutosarDataType`                                       | [x] Done    | a5f99df464                               | Group1           |
| `AutosarEngineeringObject`                              | [x] Done    | e485a5bcb2                               | Group22          |
| `AutosarOperationArgumentInstance`                      | [x] Done    | b8cce0057f                               | Group8           |
| `AutosarParameterRef`                                   | [x] Done    | b530f7e446                               | Group10          |
| `AutosarVariableInstance`                               | [ ] Implemented| N/A                                      | Group35          |
| `AutosarVariableRef`                                    | [x] Done    | d1b9384acc                               | Group10          |
| `AxisIndexType`                                         | [ ] Created | N/A                                      | Group21          |
| `BackgroundEvent`                                       | [x] Done    | 27b88a942c                               | Group2           |
| `BaseType`                                              | [ ] Implemented| N/A                                      | Group28          |
| `BaseTypeDefinition`                                    | [ ] Implemented| N/A                                      | Group28          |
| `BaseTypeDirectDefinition`                              | [ ] Implemented| N/A                                      | Group28          |
| `BaseTypeEncodingString`                                | [ ] Implemented| N/A                                      | Group21          |
| `Baseline`                                              | [ ] Created | N/A                                      | Group36          |
| `BinaryManifestAddressableObject`                       | [ ] Created | N/A                                      | Group34          |
| `BinaryManifestItem`                                    | [ ] Created | N/A                                      | Group34          |
| `BinaryManifestItemDefinition`                          | [ ] Created | N/A                                      | Group34          |
| `BinaryManifestItemNumericalValue`                      | [ ] Created | N/A                                      | Group34          |
| `BinaryManifestItemPointerValue`                        | [ ] Created | N/A                                      | Group34          |
| `BinaryManifestItemValue`                               | [ ] Created | N/A                                      | Group34          |
| `BinaryManifestMetaDataField`                           | [ ] Created | N/A                                      | Group35          |
| `BinaryManifestProvideResource`                         | [ ] Created | N/A                                      | Group34          |
| `BinaryManifestRequireResource`                         | [ ] Created | N/A                                      | Group34          |
| `BinaryManifestResource`                                | [ ] Created | N/A                                      | Group34          |
| `BinaryManifestResourceDefinition`                      | [ ] Created | N/A                                      | Group34          |
| `BindingTimeEnum`                                       | [x] Done    | 53bf180881                               | Group8           |
| `BlockState`                                            | [ ] Created | N/A                                      | Group36          |
| `BlueprintFormula`                                      | [x] Done    | 6d8ace0288                               | Group8           |
| `BlueprintGenerator`                                    | [x] Done    | 246fc98452                               | Group8           |
| `BlueprintMapping`                                      | [x] Done    | a6fa7b8c18                               | Group8           |
| `BlueprintMappingSet`                                   | [x] Done    | aec046b9cc                               | Group1           |
| `BlueprintPolicy`                                       | [x] Done    | f5f5084e36                               | Group1           |
| `BooleanValueVariationPoint`                            | [x] Done    | d5c96fd954                               | Group8           |
| `Br`                                                    | [x] Done    | c2a85e6f8f                               | Group3           |
| `BswApiOptions`                                         | [ ] Deferred| N/A                                      | Group13          |
| `BswAsynchronousServerCallPoint`                        | [x] Done    | 80c7276bff                               | Group22          |
| `BswAsynchronousServerCallResultPoint`                  | [x] Done    | e1150436c3                               | Group22          |
| `BswAsynchronousServerCallReturnsEvent`                 | [ ] Deferred| N/A                                      | Group13          |
| `BswBackgroundEvent`                                    | [x] Done    | 584344d2e4                               | Group22          |
| `BswCallType`                                           | [x] Done    | 1a5b05b196                               | Group22          |
| `BswCalledEntity`                                       | [x] Done    | bd96645681                               | Group22          |
| `BswClientPolicy`                                       | [x] Done    | 3141824107                               | Group4           |
| `BswCompositionTiming`                                  | [ ] Created | N/A                                      | Group35          |
| `BswDataReceivedEvent`                                  | [ ] Deferred| N/A                                      | Group13          |
| `BswDataReceptionPolicy`                                | [ ] Deferred| 7e3a2541a3                               | Group13          |
| `BswDataSendPolicy`                                     | [x] Done    | ccacff4a64                               | Group4           |
| `BswDirectCallPoint`                                    | [ ] Deferred| N/A                                      | Group13          |
| `BswDistinguishedPartition`                             | [x] Done    | 80d341994f                               | Group22          |
| `BswEntryKindEnum`                                      | [x] Done    | 1a5b05b196                               | Group22          |
| `BswEntryRelationship`                                  | [ ] Deferred| 75c6517342                               | Group13          |
| `BswEntryRelationshipEnum`                              | [ ] Deferred| 994c3903cb                               | Group13          |
| `BswEntryRelationshipSet`                               | [ ] Deferred| a4d57abd3a                               | Group13          |
| `BswEvent`                                              | [x] Done    | af5498712f                               | Group22          |
| `BswExclusiveAreaPolicy`                                | [ ] Deferred| eb307c9898                               | Group22          |
| `BswExecutionContext`                                   | [x] Done    | 1a5b05b196                               | Group22          |
| `BswExternalTriggerOccurredEvent`                       | [ ] Deferred| a52b41da2c                               | Group22          |
| `BswImplementation`                                     | [x] Done    | 46ce237162                               | Group22          |
| `BswInternalBehavior`                                   | [x] Done    | 89a7231799                               | Group4           |
| `BswInternalTriggerOccurredEvent`                       | [ ] Deferred| N/A                                      | Group13          |
| `BswInternalTriggeringPoint`                            | [ ] Deferred| N/A                                      | Group13          |
| `BswInternalTriggeringPointPolicy`                      | [x] Done    | 2bb8413910                               | Group4           |
| `BswInterruptCategory`                                  | [ ] Deferred| 87a572d24b                               | Group22          |
| `BswInterruptEntity`                                    | [ ] Deferred| N/A                                      | Group13          |
| `BswInterruptEvent`                                     | [x] Done    | acf1e772ac                               | Group22          |
| `BswMgrNeeds`                                           | [x] Done    | 628464ed64                               | Group4           |
| `BswModeManagerErrorEvent`                              | [ ] Deferred| N/A                                      | Group13          |
| `BswModeReceiverPolicy`                                 | [ ] Deferred| 2b15f92b16                               | Group22          |
| `BswModeSenderPolicy`                                   | [ ] Deferred| af6d69bbfa                               | Group22          |
| `BswModeSwitchAckRequest`                               | [ ] Deferred| N/A                                      | Group13          |
| `BswModeSwitchEvent`                                    | [x] Done    | af5498712f                               | Group22          |
| `BswModeSwitchedAckEvent`                               | [ ] Deferred| 160eae8f23                               | Group13          |
| `BswModuleCallPoint`                                    | [ ] Deferred| N/A                                      | Group13          |
| `BswModuleClientServerEntry`                            | [ ] Deferred| e69bc46baa                               | Group13          |
| `BswModuleDependency`                                   | [ ] Deferred| 1ca038b144                               | Group13          |
| `BswModuleDescription`                                  | [x] Done    | 1a5b05b196                               | Group22          |
| `BswModuleEntity`                                       | [x] Done    | 88b336bfe9                               | Group22          |
| `BswModuleEntry`                                        | [x] Done    | 1a5b05b196                               | Group22          |
| `BswModuleTiming`                                       | [ ] Created | N/A                                      | Group35          |
| `BswOperationInvokedEvent`                              | [ ] Deferred| dc465f6b33                               | Group22          |
| `BswOsTaskExecutionEvent`                               | [x] Done    | 2b4b89810a                               | Group22          |
| `BswParameterPolicy`                                    | [x] Done    | eceaef9296                               | Group4           |
| `BswPerInstanceMemoryPolicy`                            | [x] Done    | b89ad783a3                               | Group4           |
| `BswQueuedDataReceptionPolicy`                          | [ ] Deferred| N/A                                      | Group13          |
| `BswReleasedTriggerPolicy`                              | [x] Done    | 04498e5b27                               | Group4           |
| `BswSchedulableEntity`                                  | [x] Done    | d2e2d7903d                               | Group22          |
| `BswScheduleEvent`                                      | [x] Done    | 46ce237162                               | Group22          |
| `BswSchedulerNamePrefix`                                | [x] Done    | 2a4f60c8c4                               | Group22          |
| `BswServiceDependency`                                  | [ ] Implemented| N/A                                      | Group23          |
| `BswServiceDependencyIdent`                             | [ ] Implemented| N/A                                      | Group26          |
| `BswSynchronousServerCallPoint`                         | [ ] Deferred| N/A                                      | Group13          |
| `BswTimingEvent`                                        | [ ] Deferred| 1a0a0619b2                               | Group13          |
| `BswTriggerDirectImplementation`                        | [ ] Deferred| 0626aec9ca                               | Group22          |
| `BswVariableAccess`                                     | [ ] Deferred| d4d386b5c4                               | Group22          |
| `BufferProperties`                                      | [ ] Implemented| N/A                                      | Group28          |
| `BuildAction`                                           | [x] Done    | 6c9ef66b40                               | Group1           |
| `BuildActionEntity`                                     | [x] Done    | d7717e736a                               | Group1           |
| `BuildActionEnvironment`                                | [x] Done    | 2311c8754f                               | Group1           |
| `BuildActionInvocator`                                  | [x] Done    | 7008d5e857                               | Group1           |
| `BuildActionIoElement`                                  | [x] Done    | b572582c11                               | Group1           |
| `BuildActionManifest`                                   | [x] Done    | e6dcc8e79f                               | Group1           |
| `BuildEngineeringObject`                                | [x] Done    | 96d176ed20                               | Group1           |
| `BulkNvDataDescriptor`                                  | [x] Done    | 14a0a9cc5b                               | Group10          |
| `BurstPatternEventTriggering`                           | [ ] Implemented| N/A                                      | Group35          |
| `BusMirrorCanIdRangeMapping`                            | [ ] Created | N/A                                      | Group34          |
| `BusMirrorCanIdToCanIdMapping`                          | [ ] Created | N/A                                      | Group34          |
| `BusMirrorChannel`                                      | [ ] Created | N/A                                      | Group33          |
| `BusMirrorChannelMapping`                               | [ ] Created | N/A                                      | Group33          |
| `BusMirrorChannelMappingCan`                            | [ ] Created | N/A                                      | Group34          |
| `BusMirrorChannelMappingFlexray`                        | [ ] Created | N/A                                      | Group34          |
| `BusMirrorChannelMappingIp`                             | [ ] Created | N/A                                      | Group34          |
| `BusMirrorChannelMappingUserDefined`                    | [ ] Created | N/A                                      | Group34          |
| `BusMirrorLinPidToCanIdMapping`                         | [ ] Created | N/A                                      | Group34          |
| `BusspecificNmEcu`                                      | [ ] Implemented| N/A                                      | Group33          |
| `ByteOrderEnum`                                         | [ ] Implemented| N/A                                      | Group28          |
| `CIdentifier`                                           | [ ] Implemented| N/A                                      | Group21          |
| `CSTransformerErrorReactionEnum`                        | [ ] Implemented| N/A                                      | Group34          |
| `CalibrationParameterValue`                             | [ ] Created | N/A                                      | Group28          |
| `CalibrationParameterValueSet`                          | [ ] Created | N/A                                      | Group28          |
| `CalprmAxisCategoryEnum`                                | [ ] Implemented| N/A                                      | Group28          |
| `CanAddressingModeType`                                 | [ ] Implemented| N/A                                      | Group32          |
| `CanCluster`                                            | [ ] Implemented| N/A                                      | Group29          |
| `CanClusterBusOffRecovery`                              | [ ] Deferred| N/A                                      | Group17          |
| `CanCommunicationConnector`                             | [ ] Deferred| N/A                                      | Group17          |
| `CanCommunicationController`                            | [ ] Implemented| N/A                                      | Group29          |
| `CanControllerConfiguration`                            | [ ] Deferred| N/A                                      | Group17          |
| `CanControllerConfigurationRequirements`                | [ ] Deferred| N/A                                      | Group17          |
| `CanControllerFdConfiguration`                          | [ ] Implemented| N/A                                      | Group29          |
| `CanControllerFdConfigurationRequirements`              | [ ] Deferred| N/A                                      | Group17          |
| `CanControllerXlConfiguration`                          | [ ] Implemented| N/A                                      | Group29          |
| `CanControllerXlConfigurationRequirements`              | [ ] Implemented| N/A                                      | Group29          |
| `CanFrame`                                              | [ ] Implemented| N/A                                      | Group32          |
| `CanFrameRxBehaviorEnum`                                | [ ] Implemented| N/A                                      | Group32          |
| `CanFrameTriggering`                                    | [ ] Implemented| N/A                                      | Group32          |
| `CanFrameTxBehaviorEnum`                                | [ ] Implemented| N/A                                      | Group32          |
| `CanGlobalTimeDomainProps`                              | [ ] Created | N/A                                      | Group34          |
| `CanNmCluster`                                          | [ ] Deferred| N/A                                      | Group18          |
| `CanNmClusterCoupling`                                  | [ ] Deferred| N/A                                      | Group18          |
| `CanNmEcu`                                              | [ ] Implemented| N/A                                      | Group33          |
| `CanNmNode`                                             | [ ] Deferred| N/A                                      | Group18          |
| `CanPhysicalChannel`                                    | [ ] Implemented| N/A                                      | Group29          |
| `CanTpAddress`                                          | [ ] Implemented| N/A                                      | Group33          |
| `CanTpAddressingFormatType`                             | [ ] Implemented| N/A                                      | Group33          |
| `CanTpChannel`                                          | [ ] Implemented| N/A                                      | Group33          |
| `CanTpConfig`                                           | [ ] Implemented| N/A                                      | Group33          |
| `CanTpConnection`                                       | [ ] Implemented| N/A                                      | Group33          |
| `CanTpEcu`                                              | [ ] Implemented| N/A                                      | Group33          |
| `CanTpNode`                                             | [ ] Implemented| N/A                                      | Group33          |
| `CategoryString`                                        | [ ] Implemented| N/A                                      | Group21          |
| `Chapter`                                               | [x] Done    | 0d13ccd1bc                               | Group22          |
| `ChapterContent`                                        | [x] Done    | dee07d0a3a                               | Group9           |
| `ChapterEnumBreak`                                      | [x] Done    | 20e6ee88d0                               | Group3           |
| `ChapterModel`                                          | [x] Done    | d3d61c9b2e                               | Group9           |
| `ChapterOrMsrQuery`                                     | [x] Done    | 0d13ccd1bc                               | Group22          |
| `ClassContentConditional`                               | [ ] Created | N/A                                      | Group36          |
| `ClassTailoring`                                        | [ ] Created | N/A                                      | Group36          |
| `ClientComSpec`                                         | [ ] Implemented| N/A                                      | Group27          |
| `ClientIdDefinition`                                    | [x] Done    | 8618ec8872                               | Group5           |
| `ClientIdDefinitionSet`                                 | [x] Done    | 01759771dd                               | Group5           |
| `ClientIdRange`                                         | [x] Done    | fce66955f5                               | Group5           |
| `ClientServerAnnotation`                                | [ ] Implemented| N/A                                      | Group27          |
| `ClientServerApplicationErrorMapping`                   | [x] Done    | bc933575fd                               | Group11          |
| `ClientServerInterface`                                 | [ ] Implemented| N/A                                      | Group27          |
| `ClientServerInterfaceMapping`                          | [x] Done    | cae5a51c92                               | Group11          |
| `ClientServerOperation`                                 | [ ] Implemented| N/A                                      | Group27          |
| `ClientServerOperationBlueprintMapping`                 | [ ] Created | N/A                                      | Group36          |
| `ClientServerOperationComProps`                         | [ ] Created | N/A                                      | Group34          |
| `ClientServerOperationMapping`                          | [x] Done    | e301de1df9                               | Group11          |
| `ClientServerToSignalMapping`                           | [ ] Created | N/A                                      | Group31          |
| `Code`                                                  | [x] Done    | 9f470606b5                               | Group1           |
| `CollectableElement`                                    | [x] Done    | 3b31b7c402                               | Group1           |
| `Collection`                                            | [x] Done    | 75f4005552                               | Group1           |
| `Colspec`                                               | [x] Done    | 2bd0d07503                               | Group3           |
| `ComManagementMapping`                                  | [x] Done    | 19c327cca6                               | Group5           |
| `ComMgrUserNeeds`                                       | [ ] Implemented| N/A                                      | Group23          |
| `CommConnectorPort`                                     | [ ] Implemented| N/A                                      | Group31          |
| `CommonSignalPath`                                      | [ ] Created | N/A                                      | Group31          |
| `CommunicationBufferLocking`                            | [x] Done    | 7c67628122                               | Group2           |
| `CommunicationCluster`                                  | [ ] Implemented| N/A                                      | Group24          |
| `CommunicationConnector`                                | [ ] Implemented| N/A                                      | Group29          |
| `CommunicationController`                               | [ ] Implemented| N/A                                      | Group27          |
| `CommunicationControllerMapping`                        | [x] Done    | 2613747d22                               | Group7           |
| `CommunicationCycle`                                    | [x] Done    | 75683a2ede                               | Group5           |
| `CommunicationDirectionType`                            | [ ] Deferred| 3378eb6247                               | Group15          |
| `Compiler`                                              | [x] Done    | 3fce597322                               | Group1           |
| `ComplexDeviceDriverSwComponentType`                    | [ ] Implemented| N/A                                      | Group29          |
| `ComponentClustering`                                   | [ ] Created | N/A                                      | Group30          |
| `ComponentInCompositionInstanceRef`                     | [x] Done    | 02e863a567                               | Group7           |
| `ComponentInSystemInstanceRef`                          | [x] Done    | b511fb85b0                               | Group7           |
| `ComponentSeparation`                                   | [ ] Created | N/A                                      | Group30          |
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
| `ConcreteClassTailoring`                                | [ ] Created | N/A                                      | Group36          |
| `ConcretePatternEventTriggering`                        | [ ] Implemented| N/A                                      | Group35          |
| `ConditionByFormula`                                    | [x] Done    | 18b494eba5                               | Group8           |
| `ConditionalChangeNad`                                  | [ ] Implemented| N/A                                      | Group32          |
| `ConfidenceInterval`                                    | [ ] Implemented| N/A                                      | Group35          |
| `ConfigReferenceValue`                                  | [ ] Deferred| N/A                                      | Group19          |
| `ConsistencyNeeds`                                      | [ ] Implemented| N/A                                      | Group28          |
| `ConstantReference`                                     | [x] Done    | 4853348ea0                               | Group9           |
| `ConstantSpecification`                                 | [x] Done    | 265721a764                               | Group9           |
| `ConstantSpecificationMapping`                          | [ ] Implemented| N/A                                      | Group28          |
| `ConstantSpecificationMappingSet`                       | [x] Done    | 8e5acbb2b1                               | Group1           |
| `ConstraintTailoring`                                   | [ ] Created | N/A                                      | Group36          |
| `ConsumedEventGroup`                                    | [ ] Implemented| N/A                                      | Group32          |
| `ConsumedProvidedServiceInstanceGroup`                  | [x] Done    | fce66955f5                               | Group5           |
| `ConsumedServiceInstance`                               | [ ] Implemented| N/A                                      | Group32          |
| `ContainedIPduCollectionSemanticsEnum`                  | [x] Done    | 64d125ffae                               | Group5           |
| `ContainedIPduProps`                                    | [x] Done    | 206cf29517                               | Group5           |
| `ContainerIPdu`                                         | [ ] Created | N/A                                      | Group31          |
| `ContainerIPduHeaderTypeEnum`                           | [ ] Created | N/A                                      | Group31          |
| `ContainerIPduTriggerEnum`                              | [ ] Created | N/A                                      | Group31          |
| `CouplingElement`                                       | [ ] Created | N/A                                      | Group30          |
| `CouplingElementAbstractDetails`                        | [ ] Created | N/A                                      | Group30          |
| `CouplingElementEnum`                                   | [ ] Created | N/A                                      | Group30          |
| `CouplingElementSwitchDetails`                          | [ ] Created | N/A                                      | Group30          |
| `CouplingPort`                                          | [ ] Implemented| N/A                                      | Group30          |
| `CouplingPortAbstractShaper`                            | [ ] Deferred| N/A                                      | Group16          |
| `CouplingPortAsynchronousTrafficShaper`                 | [ ] Pending | N/A                                      | Group16          |
| `CouplingPortConnection`                                | [ ] Implemented| N/A                                      | Group30          |
| `CouplingPortCreditBasedShaper`                         | [ ] Pending | N/A                                      | Group16          |
| `CouplingPortDetails`                                   | [ ] Implemented| N/A                                      | Group30          |
| `CouplingPortFifo`                                      | [ ] Implemented| N/A                                      | Group30          |
| `CouplingPortRatePolicy`                                | [ ] Implemented| N/A                                      | Group30          |
| `CouplingPortRatePolicyActionEnum`                      | [ ] Implemented| N/A                                      | Group30          |
| `CouplingPortScheduler`                                 | [x] Done    | 0f61040c0c                               | Group6           |
| `CouplingPortShaper`                                    | [ ] Created | N/A                                      | Group30          |
| `CouplingPortStructuralElement`                         | [x] Done    | 8404bbb94a                               | Group6           |
| `CouplingPortTrafficClassAssignment`                    | [ ] Implemented| N/A                                      | Group30          |
| `CpSoftwareCluster`                                     | [x] Done    | 1194e00ca2                               | Group5           |
| `CpSoftwareClusterBinaryManifestDescriptor`             | [ ] Created | N/A                                      | Group34          |
| `CpSoftwareClusterCommunicationResource`                | [ ] Created | N/A                                      | Group34          |
| `CpSoftwareClusterCommunicationResourceProps`           | [ ] Created | N/A                                      | Group34          |
| `CpSoftwareClusterMappingSet`                           | [ ] Created | N/A                                      | Group31          |
| `CpSoftwareClusterResource`                             | [ ] Created | N/A                                      | Group26          |
| `CpSoftwareClusterResourcePool`                         | [ ] Created | N/A                                      | Group34          |
| `CpSoftwareClusterResourceToApplicationPartitionMapping` | [ ] Created | N/A                                      | Group31          |
| `CpSoftwareClusterServiceResource`                      | [ ] Created | N/A                                      | Group34          |
| `CpSoftwareClusterToApplicationPartitionMapping`        | [ ] Created | N/A                                      | Group31          |
| `CpSoftwareClusterToEcuInstanceMapping`                 | [ ] Created | N/A                                      | Group31          |
| `CpSoftwareClusterToResourceMapping`                    | [ ] Created | N/A                                      | Group34          |
| `CpSwClusterResourceToDiagDataElemMapping`              | [ ] Created | N/A                                      | Group26          |
| `CpSwClusterResourceToDiagFunctionIdMapping`            | [ ] Created | N/A                                      | Group26          |
| `CpSwClusterToDiagEventMapping`                         | [ ] Created | N/A                                      | Group26          |
| `CpSwClusterToDiagRoutineSubfunctionMapping`            | [ ] Created | N/A                                      | Group26          |
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
| `CryptoServiceKey`                                      | [ ] Created | N/A                                      | Group31          |
| `CryptoServiceKeyGenerationEnum`                        | [ ] Created | N/A                                      | Group31          |
| `CryptoServiceMapping`                                  | [x] Done    | 757aea1d17                               | Group6           |
| `CryptoServiceNeeds`                                    | [ ] Deferred| d064592a44                               | Group14          |
| `CryptoServicePrimitive`                                | [x] Done    | b609d72d59                               | Group6           |
| `CryptoServiceQueue`                                    | [ ] Created | N/A                                      | Group31          |
| `CryptoSignatureScheme`                                 | [x] Done    | 1eaeb5800b                               | Group6           |
| `CseCodeType`                                           | [ ] Implemented| N/A                                      | Group21          |
| `CycleCounter`                                          | [x] Done    | 75683a2ede                               | Group5           |
| `CycleRepetition`                                       | [x] Done    | 75683a2ede                               | Group5           |
| `CycleRepetitionType`                                   | [x] Done    | bf6cb0f022                               | Group5           |
| `CyclicTiming`                                          | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `DataComProps`                                          | [ ] Created | N/A                                      | Group34          |
| `DataConsistencyPolicyEnum`                             | [ ] Created | N/A                                      | Group34          |
| `DataConstr`                                            | [x] Done    | 9927cc9e89                               | Group3           |
| `DataConstrRule`                                        | [x] Done    | fa640a0d86                               | Group3           |
| `DataDumpEntry`                                         | [ ] Implemented| N/A                                      | Group32          |
| `DataExchangePoint`                                     | [ ] Created | N/A                                      | Group36          |
| `DataExchangePointKind`                                 | [ ] Created | N/A                                      | Group36          |
| `DataFilter`                                            | [x] Done    | ed2a073e76                               | Group9           |
| `DataFilterTypeEnum`                                    | [x] Done    | b59bd6ebbe                               | Group9           |
| `DataFormatElementReference`                            | [ ] Created | N/A                                      | Group36          |
| `DataFormatElementScope`                                | [ ] Created | N/A                                      | Group36          |
| `DataIdModeEnum`                                        | [ ] Implemented| N/A                                      | Group34          |
| `DataInterface`                                         | [x] Done    | d838fd43f4                               | Group1           |
| `DataLimitKindEnum`                                     | [ ] Implemented| N/A                                      | Group27          |
| `DataLinkLayerRule`                                     | [ ] Deferred| 0d343df2a7                               | Group20          |
| `DataMapping`                                           | [ ] Deferred| N/A                                      | Group17          |
| `DataPrototype`                                         | [x] Done    | 9175595d88                               | Group1           |
| `DataPrototypeGroup`                                    | [ ] Implemented| N/A                                      | Group28          |
| `DataPrototypeInClientServerInterfaceInstanceRef`       | [ ] Implemented| N/A                                      | Group34          |
| `DataPrototypeInPortInterfaceRef`                       | [ ] Implemented| N/A                                      | Group34          |
| `DataPrototypeInSenderReceiverInterfaceInstanceRef`     | [ ] Implemented| N/A                                      | Group34          |
| `DataPrototypeMapping`                                  | [ ] Implemented| N/A                                      | Group27          |
| `DataPrototypeReference`                                | [ ] Implemented| N/A                                      | Group34          |
| `DataPrototypeTransformationProps`                      | [x] Done    | ba255a82cc                               | Group6           |
| `DataReceiveErrorEvent`                                 | [ ] Deferred| N/A                                      | Group12          |
| `DataReceivedEvent`                                     | [ ] Deferred| N/A                                      | Group12          |
| `DataSendCompletedEvent`                                | [ ] Deferred| N/A                                      | Group12          |
| `DataTransformation`                                    | [ ] Implemented| N/A                                      | Group27          |
| `DataTransformationErrorHandlingEnum`                   | [x] Done    | 7fc79e4b73                               | Group2           |
| `DataTransformationKindEnum`                            | [ ] Implemented| N/A                                      | Group27          |
| `DataTransformationSet`                                 | [x] Done    | 757aea1d17                               | Group6           |
| `DataTransformationStatusForwardingEnum`                | [x] Done    | 7c67628122                               | Group2           |
| `DataTypeMap`                                           | [x] Done    | 0731ff4f68                               | Group10          |
| `DataTypeMappingSet`                                    | [x] Done    | 21ab486b53                               | Group2           |
| `DataTypePolicyEnum`                                    | [ ] Implemented| N/A                                      | Group31          |
| `DataWriteCompletedEvent`                               | [ ] Deferred| N/A                                      | Group12          |
| `DateTime`                                              | [ ] Implemented| N/A                                      | Group21          |
| `DcmIPdu`                                               | [ ] Implemented| N/A                                      | Group31          |
| `DdsCpConfig`                                           | [ ] Created | N/A                                      | Group32          |
| `DdsCpConsumedServiceInstance`                          | [ ] Created | N/A                                      | Group32          |
| `DdsCpDomain`                                           | [ ] Created | N/A                                      | Group32          |
| `DdsCpISignalToDdsTopicMapping`                         | [ ] Created | N/A                                      | Group31          |
| `DdsCpPartition`                                        | [ ] Created | N/A                                      | Group32          |
| `DdsCpProvidedServiceInstance`                          | [ ] Created | N/A                                      | Group32          |
| `DdsCpQosProfile`                                       | [ ] Created | N/A                                      | Group32          |
| `DdsCpServiceInstance`                                  | [ ] Created | N/A                                      | Group32          |
| `DdsCpServiceInstanceEvent`                             | [ ] Created | N/A                                      | Group32          |
| `DdsCpServiceInstanceOperation`                         | [ ] Created | N/A                                      | Group32          |
| `DdsCpTopic`                                            | [ ] Created | N/A                                      | Group32          |
| `DdsDeadline`                                           | [ ] Created | N/A                                      | Group32          |
| `DdsDestinationOrder`                                   | [ ] Created | N/A                                      | Group32          |
| `DdsDestinationOrderKindEnum`                           | [ ] Created | N/A                                      | Group32          |
| `DdsDurability`                                         | [ ] Created | N/A                                      | Group32          |
| `DdsDurabilityKindEnum`                                 | [ ] Created | N/A                                      | Group32          |
| `DdsDurabilityService`                                  | [ ] Created | N/A                                      | Group32          |
| `DdsDurabilityServiceHistoryKindEnum`                   | [ ] Created | N/A                                      | Group32          |
| `DdsHistory`                                            | [ ] Created | N/A                                      | Group32          |
| `DdsHistoryKindEnum`                                    | [ ] Created | N/A                                      | Group32          |
| `DdsLatencyBudget`                                      | [ ] Created | N/A                                      | Group32          |
| `DdsLifespan`                                           | [ ] Created | N/A                                      | Group32          |
| `DdsLiveliness`                                         | [ ] Created | N/A                                      | Group32          |
| `DdsLivenessKindEnum`                                   | [ ] Created | N/A                                      | Group32          |
| `DdsOwnership`                                          | [ ] Created | N/A                                      | Group32          |
| `DdsOwnershipKindEnum`                                  | [ ] Created | N/A                                      | Group32          |
| `DdsOwnershipStrength`                                  | [ ] Created | N/A                                      | Group32          |
| `DdsReliability`                                        | [ ] Created | N/A                                      | Group32          |
| `DdsReliabilityKindEnum`                                | [ ] Created | N/A                                      | Group32          |
| `DdsResourceLimits`                                     | [ ] Created | N/A                                      | Group32          |
| `DdsTopicData`                                          | [ ] Created | N/A                                      | Group32          |
| `DdsTransportPriority`                                  | [ ] Created | N/A                                      | Group32          |
| `DefItem`                                               | [ ] Implemented| N/A                                      | Group21          |
| `DefList`                                               | [ ] Implemented| N/A                                      | Group21          |
| `DefaultValueApplicationStrategyEnum`                   | [ ] Created | N/A                                      | Group36          |
| `DefaultValueElement`                                   | [ ] Deferred| N/A                                      | Group17          |
| `DelegatedPortAnnotation`                               | [ ] Implemented| N/A                                      | Group27          |
| `DelegationSwConnector`                                 | [x] Done    | 503344170e                               | Group2           |
| `DependencyOnArtifact`                                  | [x] Done    | 25211e56ca                               | Group1           |
| `DependencyUsageEnum`                                   | [x] Done    | 9a8c86ae9a                               | Group10          |
| `DevelopmentError`                                      | [ ] Implemented| N/A                                      | Group23          |
| `DhcpServerConfiguration`                               | [ ] Implemented| N/A                                      | Group30          |
| `Dhcpv6Props`                                           | [ ] Created | N/A                                      | Group30          |
| `DiagEventDebounceAlgorithm`                            | [x] Done    | 4f246ae62d                               | Group4           |
| `DiagEventDebounceCounterBased`                         | [ ] Deferred| d064592a44                               | Group14          |
| `DiagEventDebounceMonitorInternal`                      | [x] Done    | 103cfd4316                               | Group4           |
| `DiagEventDebounceTimeBased`                            | [ ] Implemented| N/A                                      | Group23          |
| `DiagPduType`                                           | [ ] Created | N/A                                      | Group31          |
| `DiagRequirementIdString`                               | [ ] Implemented| N/A                                      | Group21          |
| `DiagnosticAbstractAliasEvent`                          | [ ] Created | N/A                                      | Group25          |
| `DiagnosticAbstractDataIdentifier`                      | [ ] Created | N/A                                      | Group23          |
| `DiagnosticAbstractParameter`                           | [ ] Created | N/A                                      | Group23          |
| `DiagnosticAccessPermission`                            | [x] Done    | 9cbb4e26e7                               | Group7           |
| `DiagnosticAging`                                       | [ ] Created | N/A                                      | Group25          |
| `DiagnosticAudienceEnum`                                | [ ] Deferred| 5685ad743e                               | Group14          |
| `DiagnosticAuthRole`                                    | [ ] Created | N/A                                      | Group23          |
| `DiagnosticAuthRoleProxy`                               | [x] Done    | 4579b43f0d                               | Group7           |
| `DiagnosticAuthTransmitCertificate`                     | [ ] Created | N/A                                      | Group24          |
| `DiagnosticAuthTransmitCertificateEvaluation`           | [ ] Created | N/A                                      | Group24          |
| `DiagnosticAuthTransmitCertificateMapping`              | [ ] Created | N/A                                      | Group26          |
| `DiagnosticAuthentication`                              | [ ] Created | N/A                                      | Group24          |
| `DiagnosticAuthenticationClass`                         | [ ] Created | N/A                                      | Group24          |
| `DiagnosticAuthenticationConfiguration`                 | [ ] Created | N/A                                      | Group24          |
| `DiagnosticCapabilityElement`                           | [ ] Deferred| f5ffd3abf2                               | Group14          |
| `DiagnosticClearDiagnosticInformation`                  | [ ] Created | N/A                                      | Group24          |
| `DiagnosticClearDiagnosticInformationClass`             | [ ] Created | N/A                                      | Group24          |
| `DiagnosticClearDtcLimitationEnum`                      | [ ] Created | N/A                                      | Group25          |
| `DiagnosticClearDtcNotificationEnum`                    | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DiagnosticClearEventAllowedBehaviorEnum`               | [ ] Created | N/A                                      | Group25          |
| `DiagnosticClearResetEmissionRelatedInfo`               | [ ] Created | N/A                                      | Group25          |
| `DiagnosticClearResetEmissionRelatedInfoClass`          | [ ] Created | N/A                                      | Group25          |
| `DiagnosticComControl`                                  | [ ] Created | N/A                                      | Group24          |
| `DiagnosticComControlClass`                             | [ ] Created | N/A                                      | Group24          |
| `DiagnosticComControlSpecificChannel`                   | [ ] Created | N/A                                      | Group24          |
| `DiagnosticComControlSubNodeChannel`                    | [ ] Created | N/A                                      | Group24          |
| `DiagnosticCommonElement`                               | [x] Done    | e0d022b1aa                               | Group7           |
| `DiagnosticCommonProps`                                 | [ ] Created | N/A                                      | Group23          |
| `DiagnosticCommunicationManagerNeeds`                   | [ ] Deferred| 79c639e42a                               | Group14          |
| `DiagnosticCompareTypeEnum`                             | [ ] Implemented| N/A                                      | Group23          |
| `DiagnosticComponentNeeds`                              | [x] Done    | 5c4c0963af                               | Group4           |
| `DiagnosticCondition`                                   | [ ] Created | N/A                                      | Group25          |
| `DiagnosticConditionGroup`                              | [ ] Created | N/A                                      | Group25          |
| `DiagnosticConnectedIndicator`                          | [ ] Created | N/A                                      | Group25          |
| `DiagnosticConnectedIndicatorBehaviorEnum`              | [ ] Created | N/A                                      | Group25          |
| `DiagnosticConnection`                                  | [x] Done    | e96086c12f                               | Group5           |
| `DiagnosticContributionSet`                             | [ ] Created | N/A                                      | Group23          |
| `DiagnosticControlDTCSetting`                           | [ ] Created | N/A                                      | Group24          |
| `DiagnosticControlDTCSettingClass`                      | [ ] Created | N/A                                      | Group24          |
| `DiagnosticControlEnableMaskBit`                        | [ ] Created | N/A                                      | Group24          |
| `DiagnosticControlNeeds`                                | [x] Done    | d0a1134e3b                               | Group4           |
| `DiagnosticCustomServiceClass`                          | [ ] Created | N/A                                      | Group23          |
| `DiagnosticCustomServiceInstance`                       | [ ] Created | N/A                                      | Group23          |
| `DiagnosticDataByIdentifier`                            | [ ] Created | N/A                                      | Group24          |
| `DiagnosticDataElement`                                 | [ ] Created | N/A                                      | Group23          |
| `DiagnosticDataIdentifier`                              | [ ] Created | N/A                                      | Group23          |
| `DiagnosticDataIdentifierSet`                           | [ ] Created | N/A                                      | Group25          |
| `DiagnosticDataTransfer`                                | [ ] Created | N/A                                      | Group24          |
| `DiagnosticDataTransferClass`                           | [ ] Created | N/A                                      | Group24          |
| `DiagnosticDeAuthentication`                            | [ ] Created | N/A                                      | Group24          |
| `DiagnosticDebounceAlgorithmProps`                      | [ ] Created | N/A                                      | Group25          |
| `DiagnosticDebounceBehaviorEnum`                        | [ ] Created | N/A                                      | Group25          |
| `DiagnosticDemProvidedDataMapping`                      | [ ] Created | N/A                                      | Group26          |
| `DiagnosticDenominatorConditionEnum`                    | [ ] Implemented| N/A                                      | Group29          |
| `DiagnosticDynamicDataIdentifier`                       | [ ] Created | N/A                                      | Group23          |
| `DiagnosticDynamicallyDefineDataIdentifier`             | [ ] Created | N/A                                      | Group24          |
| `DiagnosticDynamicallyDefineDataIdentifierClass`        | [ ] Created | N/A                                      | Group24          |
| `DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum` | [ ] Created | N/A                                      | Group24          |
| `DiagnosticEcuInstanceProps`                            | [ ] Created | N/A                                      | Group25          |
| `DiagnosticEcuReset`                                    | [ ] Created | N/A                                      | Group24          |
| `DiagnosticEcuResetClass`                               | [ ] Created | N/A                                      | Group24          |
| `DiagnosticEnableCondition`                             | [ ] Created | N/A                                      | Group25          |
| `DiagnosticEnableConditionGroup`                        | [ ] Created | N/A                                      | Group25          |
| `DiagnosticEnableConditionNeeds`                        | [ ] Implemented| N/A                                      | Group29          |
| `DiagnosticEnableConditionPortMapping`                  | [ ] Created | N/A                                      | Group26          |
| `DiagnosticEnvBswModeElement`                           | [ ] Created | N/A                                      | Group23          |
| `DiagnosticEnvCompareCondition`                         | [ ] Deferred| af255af373                               | Group14          |
| `DiagnosticEnvConditionFormula`                         | [ ] Deferred| af255af373                               | Group14          |
| `DiagnosticEnvConditionFormulaPart`                     | [x] Deferred| af255af373                               | Group14          |
| `DiagnosticEnvDataCondition`                            | [ ] Created | N/A                                      | Group23          |
| `DiagnosticEnvDataElementCondition`                     | [ ] Created | N/A                                      | Group23          |
| `DiagnosticEnvModeCondition`                            | [ ] Created | N/A                                      | Group23          |
| `DiagnosticEnvModeElement`                              | [ ] Deferred| af255af373                               | Group14          |
| `DiagnosticEnvSwcModeElement`                           | [ ] Created | N/A                                      | Group23          |
| `DiagnosticEnvironmentalCondition`                      | [x] Done    | 5bbca5f217                               | Group7           |
| `DiagnosticEvent`                                       | [ ] Created | N/A                                      | Group25          |
| `DiagnosticEventClearAllowedEnum`                       | [ ] Created | N/A                                      | Group25          |
| `DiagnosticEventCombinationBehaviorEnum`                | [ ] Created | N/A                                      | Group23          |
| `DiagnosticEventCombinationReportingBehaviorEnum`       | [ ] Created | N/A                                      | Group23          |
| `DiagnosticEventDisplacementStrategyEnum`               | [ ] Created | N/A                                      | Group25          |
| `DiagnosticEventInfoNeeds`                              | [ ] Deferred| 79c639e42a                               | Group14          |
| `DiagnosticEventKindEnum`                               | [ ] Created | N/A                                      | Group25          |
| `DiagnosticEventManagerNeeds`                           | [x] Done    | dc34774429                               | Group4           |
| `DiagnosticEventNeeds`                                  | [ ] Implemented| N/A                                      | Group23          |
| `DiagnosticEventPortMapping`                            | [ ] Created | N/A                                      | Group26          |
| `DiagnosticEventToDebounceAlgorithmMapping`             | [ ] Created | N/A                                      | Group26          |
| `DiagnosticEventToEnableConditionGroupMapping`          | [ ] Created | N/A                                      | Group26          |
| `DiagnosticEventToOperationCycleMapping`                | [ ] Created | N/A                                      | Group26          |
| `DiagnosticEventToSecurityEventMapping`                 | [ ] Created | N/A                                      | Group26          |
| `DiagnosticEventToStorageConditionGroupMapping`         | [ ] Created | N/A                                      | Group26          |
| `DiagnosticEventToTroubleCodeJ1939Mapping`              | [ ] Created | N/A                                      | Group26          |
| `DiagnosticEventToTroubleCodeUdsMapping`                | [ ] Created | N/A                                      | Group26          |
| `DiagnosticEventWindow`                                 | [ ] Created | N/A                                      | Group24          |
| `DiagnosticEventWindowTimeEnum`                         | [ ] Created | N/A                                      | Group24          |
| `DiagnosticExtendedDataRecord`                          | [ ] Created | N/A                                      | Group25          |
| `DiagnosticFimAliasEvent`                               | [ ] Created | N/A                                      | Group25          |
| `DiagnosticFimAliasEventGroup`                          | [ ] Created | N/A                                      | Group26          |
| `DiagnosticFimAliasEventGroupMapping`                   | [ ] Created | N/A                                      | Group26          |
| `DiagnosticFimAliasEventMapping`                        | [ ] Created | N/A                                      | Group26          |
| `DiagnosticFimEventGroup`                               | [ ] Created | N/A                                      | Group26          |
| `DiagnosticFimFunctionMapping`                          | [ ] Created | N/A                                      | Group26          |
| `DiagnosticFreezeFrame`                                 | [ ] Created | N/A                                      | Group25          |
| `DiagnosticFunctionIdentifier`                          | [ ] Created | N/A                                      | Group25          |
| `DiagnosticFunctionIdentifierInhibit`                   | [ ] Created | N/A                                      | Group25          |
| `DiagnosticFunctionInhibitSource`                       | [ ] Created | N/A                                      | Group25          |
| `DiagnosticHandleDDDIConfigurationEnum`                 | [ ] Created | N/A                                      | Group24          |
| `DiagnosticIOControl`                                   | [ ] Created | N/A                                      | Group24          |
| `DiagnosticIndicator`                                   | [ ] Created | N/A                                      | Group25          |
| `DiagnosticIndicatorTypeEnum`                           | [ ] Implemented| N/A                                      | Group29          |
| `DiagnosticInfoType`                                    | [ ] Created | N/A                                      | Group25          |
| `DiagnosticInhibitSourceEventMapping`                   | [ ] Created | N/A                                      | Group26          |
| `DiagnosticInhibitionMaskEnum`                          | [ ] Created | N/A                                      | Group26          |
| `DiagnosticIoControlClass`                              | [ ] Created | N/A                                      | Group24          |
| `DiagnosticIoControlNeeds`                              | [ ] Implemented| N/A                                      | Group23          |
| `DiagnosticIumpr`                                       | [ ] Created | N/A                                      | Group25          |
| `DiagnosticIumprDenominatorGroup`                       | [ ] Created | N/A                                      | Group25          |
| `DiagnosticIumprGroup`                                  | [ ] Created | N/A                                      | Group25          |
| `DiagnosticIumprGroupIdentifier`                        | [ ] Created | N/A                                      | Group25          |
| `DiagnosticIumprKindEnum`                               | [ ] Created | N/A                                      | Group25          |
| `DiagnosticIumprToFunctionIdentifierMapping`            | [ ] Created | N/A                                      | Group26          |
| `DiagnosticJ1939ExpandedFreezeFrame`                    | [ ] Created | N/A                                      | Group26          |
| `DiagnosticJ1939FreezeFrame`                            | [ ] Created | N/A                                      | Group26          |
| `DiagnosticJ1939Node`                                   | [ ] Created | N/A                                      | Group26          |
| `DiagnosticJ1939Spn`                                    | [ ] Created | N/A                                      | Group26          |
| `DiagnosticJ1939SpnMapping`                             | [ ] Created | N/A                                      | Group26          |
| `DiagnosticJ1939SwMapping`                              | [ ] Created | N/A                                      | Group26          |
| `DiagnosticJumpToBootLoaderEnum`                        | [ ] Deferred| N/A                                      | Group14          |
| `DiagnosticLogicalOperatorEnum`                         | [ ] Deferred| N/A                                      | Group14          |
| `DiagnosticMapping`                                     | [ ] Created | N/A                                      | Group26          |
| `DiagnosticMasterToSlaveEventMapping`                   | [ ] Created | N/A                                      | Group26          |
| `DiagnosticMeasurementIdentifier`                       | [ ] Created | N/A                                      | Group25          |
| `DiagnosticMemoryAddressableRangeAccess`                | [ ] Created | N/A                                      | Group24          |
| `DiagnosticMemoryByAddress`                             | [ ] Created | N/A                                      | Group24          |
| `DiagnosticMemoryDestination`                           | [ ] Created | N/A                                      | Group25          |
| `DiagnosticMemoryDestinationPrimary`                    | [ ] Created | N/A                                      | Group25          |
| `DiagnosticMemoryDestinationUserDefined`                | [ ] Created | N/A                                      | Group25          |
| `DiagnosticMemoryEntryStorageTriggerEnum`               | [ ] Created | N/A                                      | Group25          |
| `DiagnosticMemoryIdentifier`                            | [ ] Created | N/A                                      | Group24          |
| `DiagnosticMonitorUpdateKindEnum`                       | [ ] Implemented| N/A                                      | Group29          |
| `DiagnosticObdSupportEnum`                              | [ ] Created | N/A                                      | Group25          |
| `DiagnosticOccurrenceCounterProcessingEnum`             | [ ] Created | N/A                                      | Group23          |
| `DiagnosticOperationCycle`                              | [ ] Created | N/A                                      | Group25          |
| `DiagnosticOperationCycleNeeds`                         | [ ] Implemented| N/A                                      | Group29          |
| `DiagnosticOperationCyclePortMapping`                   | [ ] Created | N/A                                      | Group26          |
| `DiagnosticOperationCycleTypeEnum`                      | [ ] Created | N/A                                      | Group25          |
| `DiagnosticParameter`                                   | [ ] Created | N/A                                      | Group23          |
| `DiagnosticParameterElement`                            | [ ] Created | N/A                                      | Group23          |
| `DiagnosticParameterElementAccess`                      | [ ] Created | N/A                                      | Group26          |
| `DiagnosticParameterIdent`                              | [ ] Created | N/A                                      | Group23          |
| `DiagnosticParameterIdentifier`                         | [ ] Created | N/A                                      | Group24          |
| `DiagnosticParameterSupportInfo`                        | [ ] Created | N/A                                      | Group24          |
| `DiagnosticPeriodicRate`                                | [ ] Created | N/A                                      | Group24          |
| `DiagnosticPeriodicRateCategoryEnum`                    | [ ] Created | N/A                                      | Group24          |
| `DiagnosticPowertrainFreezeFrame`                       | [ ] Created | N/A                                      | Group25          |
| `DiagnosticProcessingStyleEnum`                         | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DiagnosticProofOfOwnership`                            | [ ] Created | N/A                                      | Group24          |
| `DiagnosticProtocol`                                    | [ ] Created | N/A                                      | Group23          |
| `DiagnosticReadDTCInformation`                          | [ ] Created | N/A                                      | Group24          |
| `DiagnosticReadDTCInformationClass`                     | [ ] Created | N/A                                      | Group24          |
| `DiagnosticReadDataByIdentifier`                        | [ ] Created | N/A                                      | Group24          |
| `DiagnosticReadDataByIdentifierClass`                   | [ ] Created | N/A                                      | Group24          |
| `DiagnosticReadDataByPeriodicID`                        | [ ] Created | N/A                                      | Group24          |
| `DiagnosticReadDataByPeriodicIDClass`                   | [ ] Created | N/A                                      | Group24          |
| `DiagnosticReadMemoryByAddress`                         | [ ] Created | N/A                                      | Group24          |
| `DiagnosticReadMemoryByAddressClass`                    | [ ] Created | N/A                                      | Group24          |
| `DiagnosticReadScalingDataByIdentifier`                 | [ ] Created | N/A                                      | Group24          |
| `DiagnosticReadScalingDataByIdentifierClass`            | [ ] Created | N/A                                      | Group24          |
| `DiagnosticRecordTriggerEnum`                           | [ ] Created | N/A                                      | Group25          |
| `DiagnosticRequestControlOfOnBoardDevice`               | [ ] Created | N/A                                      | Group25          |
| `DiagnosticRequestControlOfOnBoardDeviceClass`          | [ ] Created | N/A                                      | Group25          |
| `DiagnosticRequestCurrentPowertrainData`                | [ ] Created | N/A                                      | Group25          |
| `DiagnosticRequestCurrentPowertrainDataClass`           | [ ] Created | N/A                                      | Group25          |
| `DiagnosticRequestDownload`                             | [ ] Created | N/A                                      | Group24          |
| `DiagnosticRequestDownloadClass`                        | [ ] Created | N/A                                      | Group24          |
| `DiagnosticRequestEmissionRelatedDTC`                   | [ ] Created | N/A                                      | Group25          |
| `DiagnosticRequestEmissionRelatedDTCClass`              | [ ] Created | N/A                                      | Group25          |
| `DiagnosticRequestEmissionRelatedDTCPermanentStatus`    | [ ] Created | N/A                                      | Group25          |
| `DiagnosticRequestEmissionRelatedDTCPermanentStatusClass` | [ ] Created | N/A                                      | Group25          |
| `DiagnosticRequestFileTransfer`                         | [ ] Created | N/A                                      | Group24          |
| `DiagnosticRequestFileTransferClass`                    | [ ] Created | N/A                                      | Group24          |
| `DiagnosticRequestFileTransferNeeds`                    | [x] Done    | f084c4328c                               | Group4           |
| `DiagnosticRequestOnBoardMonitoringTestResults`         | [ ] Created | N/A                                      | Group25          |
| `DiagnosticRequestOnBoardMonitoringTestResultsClass`    | [ ] Created | N/A                                      | Group25          |
| `DiagnosticRequestPowertrainFreezeFrameData`            | [ ] Created | N/A                                      | Group25          |
| `DiagnosticRequestPowertrainFreezeFrameDataClass`       | [ ] Created | N/A                                      | Group25          |
| `DiagnosticRequestRoutineResults`                       | [ ] Created | N/A                                      | Group24          |
| `DiagnosticRequestUpload`                               | [ ] Created | N/A                                      | Group24          |
| `DiagnosticRequestUploadClass`                          | [ ] Created | N/A                                      | Group24          |
| `DiagnosticRequestVehicleInfo`                          | [ ] Created | N/A                                      | Group25          |
| `DiagnosticRequestVehicleInfoClass`                     | [ ] Created | N/A                                      | Group25          |
| `DiagnosticResponseOnEvent`                             | [ ] Created | N/A                                      | Group24          |
| `DiagnosticResponseOnEventActionEnum`                   | [ ] Created | N/A                                      | Group24          |
| `DiagnosticResponseOnEventClass`                        | [ ] Created | N/A                                      | Group24          |
| `DiagnosticResponseToEcuResetEnum`                      | [ ] Created | N/A                                      | Group24          |
| `DiagnosticRoutine`                                     | [ ] Created | N/A                                      | Group24          |
| `DiagnosticRoutineControl`                              | [ ] Created | N/A                                      | Group24          |
| `DiagnosticRoutineControlClass`                         | [ ] Created | N/A                                      | Group24          |
| `DiagnosticRoutineNeeds`                                | [ ] Deferred| 79c639e42a                               | Group14          |
| `DiagnosticRoutineSubfunction`                          | [ ] Created | N/A                                      | Group24          |
| `DiagnosticRoutineTypeEnum`                             | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DiagnosticSecurityAccess`                              | [ ] Created | N/A                                      | Group24          |
| `DiagnosticSecurityAccessClass`                         | [ ] Created | N/A                                      | Group24          |
| `DiagnosticSecurityEventReportingModeMapping`           | [ ] Created | N/A                                      | Group26          |
| `DiagnosticSecurityLevel`                               | [x] Done    | f2da1338fc                               | Group7           |
| `DiagnosticServiceClass`                                | [x] Deferred| 6b514727f9                               | Group14          |
| `DiagnosticServiceDataMapping`                          | [ ] Created | N/A                                      | Group26          |
| `DiagnosticServiceInstance`                             | [x] Done    | 6b514727f9                               | Group7           |
| `DiagnosticServiceMappingDiagTarget`                    | [ ] Created | N/A                                      | Group26          |
| `DiagnosticServiceRequestCallbackTypeEnum`              | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DiagnosticServiceSwMapping`                            | [ ] Created | N/A                                      | Group26          |
| `DiagnosticServiceTable`                                | [x] Done    | 9bd6fadae5                               | Group7           |
| `DiagnosticSession`                                     | [x] Done    | 06d4e49a26                               | Group7           |
| `DiagnosticSessionControl`                              | [ ] Created | N/A                                      | Group23          |
| `DiagnosticSessionControlClass`                         | [ ] Created | N/A                                      | Group24          |
| `DiagnosticSignificanceEnum`                            | [ ] Created | N/A                                      | Group25          |
| `DiagnosticStartRoutine`                                | [ ] Created | N/A                                      | Group24          |
| `DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum` | [ ] Created | N/A                                      | Group25          |
| `DiagnosticStopRoutine`                                 | [ ] Created | N/A                                      | Group24          |
| `DiagnosticStorageCondition`                            | [ ] Created | N/A                                      | Group25          |
| `DiagnosticStorageConditionGroup`                       | [ ] Created | N/A                                      | Group25          |
| `DiagnosticStorageConditionNeeds`                       | [ ] Implemented| N/A                                      | Group29          |
| `DiagnosticStorageConditionPortMapping`                 | [ ] Created | N/A                                      | Group26          |
| `DiagnosticSupportInfoByte`                             | [ ] Created | N/A                                      | Group25          |
| `DiagnosticSwMapping`                                   | [ ] Created | N/A                                      | Group26          |
| `DiagnosticTestIdentifier`                              | [ ] Created | N/A                                      | Group25          |
| `DiagnosticTestResult`                                  | [ ] Created | N/A                                      | Group29          |
| `DiagnosticTestResultUpdateEnum`                        | [ ] Created | N/A                                      | Group25          |
| `DiagnosticTestRoutineIdentifier`                       | [ ] Created | N/A                                      | Group25          |
| `DiagnosticTransferExit`                                | [ ] Created | N/A                                      | Group24          |
| `DiagnosticTransferExitClass`                           | [ ] Created | N/A                                      | Group24          |
| `DiagnosticTroubleCode`                                 | [ ] Created | N/A                                      | Group25          |
| `DiagnosticTroubleCodeGroup`                            | [ ] Created | N/A                                      | Group25          |
| `DiagnosticTroubleCodeJ1939`                            | [ ] Created | N/A                                      | Group26          |
| `DiagnosticTroubleCodeJ1939DtcKindEnum`                 | [ ] Created | N/A                                      | Group26          |
| `DiagnosticTroubleCodeObd`                              | [ ] Created | N/A                                      | Group25          |
| `DiagnosticTroubleCodeProps`                            | [ ] Created | N/A                                      | Group25          |
| `DiagnosticTroubleCodeUds`                              | [ ] Created | N/A                                      | Group25          |
| `DiagnosticTroubleCodeUdsToTroubleCodeObdMapping`       | [ ] Created | N/A                                      | Group25          |
| `DiagnosticTypeOfDtcSupportedEnum`                      | [ ] Created | N/A                                      | Group23          |
| `DiagnosticTypeOfFreezeFrameRecordNumerationEnum`       | [ ] Created | N/A                                      | Group25          |
| `DiagnosticUdsSeverityEnum`                             | [ ] Created | N/A                                      | Group25          |
| `DiagnosticUploadDownloadNeeds`                         | [x] Done    | fe8a0a1a6d                               | Group4           |
| `DiagnosticValueAccessEnum`                             | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DiagnosticValueNeeds`                                  | [ ] Deferred| 79c639e42a                               | Group14          |
| `DiagnosticVerifyCertificateBidirectional`              | [ ] Created | N/A                                      | Group24          |
| `DiagnosticVerifyCertificateUnidirectional`             | [ ] Created | N/A                                      | Group24          |
| `DiagnosticWriteDataByIdentifier`                       | [ ] Created | N/A                                      | Group24          |
| `DiagnosticWriteDataByIdentifierClass`                  | [ ] Created | N/A                                      | Group24          |
| `DiagnosticWriteMemoryByAddress`                        | [ ] Created | N/A                                      | Group24          |
| `DiagnosticWriteMemoryByAddressClass`                   | [ ] Created | N/A                                      | Group24          |
| `DiagnosticWwhObdDtcClassEnum`                          | [ ] Created | N/A                                      | Group25          |
| `DiagnosticsCommunicationSecurityNeeds`                 | [x] Done    | d24a66632e                               | Group4           |
| `DisplayFormatString`                                   | [ ] Implemented| N/A                                      | Group21          |
| `DisplayPresentationEnum`                               | [ ] Implemented| N/A                                      | Group28          |
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
| `DoIpEntityRoleEnum`                                    | [ ] Implemented| N/A                                      | Group32          |
| `DoIpGidNeeds`                                          | [x] Done    | 6c31e0057f                               | Group4           |
| `DoIpGidSynchronizationNeeds`                           | [x] Done    | c64cb6318c                               | Group4           |
| `DoIpInterface`                                         | [x] Done    | c53a7febdc                               | Group5           |
| `DoIpLogicAddress`                                      | [ ] Deferred| a5671c229e                               | Group20          |
| `DoIpLogicTargetAddressProps`                           | [x] Done    | 64d125ffae                               | Group7           |
| `DoIpLogicTesterAddressProps`                           | [x] Done    | 64d125ffae                               | Group7           |
| `DoIpPowerModeStatusNeeds`                              | [x] Done    | 4350642e77                               | Group5           |
| `DoIpRoutingActivation`                                 | [x] Done    | c53a7febdc                               | Group5           |
| `DoIpRoutingActivationAuthenticationNeeds`              | [ ] Implemented| N/A                                      | Group29          |
| `DoIpRoutingActivationConfirmationNeeds`                | [ ] Implemented| N/A                                      | Group29          |
| `DoIpRule`                                              | [ ] Deferred| ebd95cd8f9                               | Group20          |
| `DoIpServiceNeeds`                                      | [ ] Implemented| N/A                                      | Group23          |
| `DoIpTpConfig`                                          | [x] Done    | ac63e581b9                               | Group7           |
| `DoIpTpConnection`                                      | [ ] Deferred| 0abdd0dba4                               | Group20          |
| `DocRevision`                                           | [ ] Implemented| N/A                                      | Group21          |
| `DocumentElementScope`                                  | [ ] Created | N/A                                      | Group36          |
| `DocumentViewSelectable`                                | [x] Done    | ba2c324b39                               | Group3           |
| `DocumentationBlock`                                    | [ ] Implemented| N/A                                      | Group21          |
| `DocumentationContext`                                  | [ ] Implemented| N/A                                      | Group21          |
| `DtcFormatTypeEnum`                                     | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DtcKindEnum`                                           | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DtcStatusChangeNotificationNeeds`                      | [ ] Deferred| 79c639e42a                               | Group14          |
| `DynamicPart`                                           | [ ] Deferred| 4211085bc4                               | Group15          |
| `DynamicPartAlternative`                                | [x] Done    | 206cf29517                               | Group5           |
| `E2EProfileCompatibilityProps`                          | [ ] Implemented| N/A                                      | Group28          |
| `ECUMapping`                                            | [x] Done    | 34bb50d75e                               | Group7           |
| `EEnum`                                                 | [ ] Created | N/A                                      | Group21          |
| `EEnumFont`                                             | [ ] Created | N/A                                      | Group21          |
| `EOCEventRef`                                           | [ ] Implemented| N/A                                      | Group35          |
| `EOCExecutableEntityRef`                                | [ ] Implemented| N/A                                      | Group35          |
| `EOCExecutableEntityRefAbstract`                        | [ ] Implemented| N/A                                      | Group35          |
| `EOCExecutableEntityRefGroup`                           | [ ] Implemented| N/A                                      | Group35          |
| `EcuAbstractionSwComponentType`                         | [ ] Implemented| N/A                                      | Group29          |
| `EcuInstance`                                           | [x] Done    | 206e89be41                               | Group5           |
| `EcuPartition`                                          | [x] Done    | c53a7febdc                               | Group5           |
| `EcuResourceEstimation`                                 | [ ] Created | N/A                                      | Group31          |
| `EcuStateMgrUserNeeds`                                  | [x] Done    | 6b31696dff                               | Group4           |
| `EcuTiming`                                             | [ ] Created | N/A                                      | Group35          |
| `EcucAbstractConfigurationClass`                        | [ ] Implemented| N/A                                      | Group26          |
| `EcucAbstractExternalReferenceDef`                      | [ ] Implemented| N/A                                      | Group26          |
| `EcucAbstractInternalReferenceDef`                      | [ ] Implemented| N/A                                      | Group26          |
| `EcucAbstractReferenceDef`                              | [ ] Implemented| N/A                                      | Group26          |
| `EcucAbstractReferenceValue`                            | [ ] Implemented| N/A                                      | Group27          |
| `EcucAbstractStringParamDef`                            | [ ] Implemented| N/A                                      | Group26          |
| `EcucAddInfoParamDef`                                   | [ ] Implemented| N/A                                      | Group26          |
| `EcucAddInfoParamValue`                                 | [ ] Implemented| N/A                                      | Group27          |
| `EcucBooleanParamDef`                                   | [ ] Deferred| N/A                                      | Group19          |
| `EcucChoiceContainerDef`                                | [ ] Implemented| N/A                                      | Group26          |
| `EcucChoiceReferenceDef`                                | [ ] Implemented| N/A                                      | Group26          |
| `EcucCommonAttributes`                                  | [ ] Implemented| N/A                                      | Group26          |
| `EcucConditionFormula`                                  | [ ] Implemented| N/A                                      | Group19          |
| `EcucConditionSpecification`                            | [ ] Implemented| N/A                                      | Group27          |
| `EcucConfigurationClassEnum`                            | [ ] Deferred| N/A                                      | Group19          |
| `EcucConfigurationVariantEnum`                          | [ ] Implemented| N/A                                      | Group26          |
| `EcucContainerDef`                                      | [ ] Implemented| N/A                                      | Group26          |
| `EcucContainerValue`                                    | [ ] Implemented| N/A                                      | Group27          |
| `EcucDefinitionCollection`                              | [ ] Implemented| N/A                                      | Group26          |
| `EcucDefinitionElement`                                 | [ ] Implemented| N/A                                      | Group26          |
| `EcucDerivationSpecification`                           | [ ] Implemented| N/A                                      | Group26          |
| `EcucDestinationUriDef`                                 | [ ] Implemented| N/A                                      | Group26          |
| `EcucDestinationUriDefRefType`                          | [ ] Implemented| N/A                                      | Group19          |
| `EcucDestinationUriDefSet`                              | [ ] Implemented| N/A                                      | Group26          |
| `EcucDestinationUriNestingContractEnum`                 | [ ] Implemented| N/A                                      | Group26          |
| `EcucDestinationUriPolicy`                              | [ ] Implemented| N/A                                      | Group26          |
| `EcucEnumerationLiteralDef`                             | [ ] Implemented| N/A                                      | Group26          |
| `EcucEnumerationParamDef`                               | [ ] Implemented| N/A                                      | Group26          |
| `EcucFloatParamDef`                                     | [ ] Deferred| N/A                                      | Group19          |
| `EcucForeignReferenceDef`                               | [ ] Deferred| N/A                                      | Group19          |
| `EcucFunctionNameDef`                                   | [ ] Implemented| N/A                                      | Group26          |
| `EcucIndexableValue`                                    | [ ] Implemented| N/A                                      | Group27          |
| `EcucInstanceReferenceDef`                              | [ ] Implemented| N/A                                      | Group26          |
| `EcucInstanceReferenceValue`                            | [ ] Implemented| N/A                                      | Group27          |
| `EcucIntegerParamDef`                                   | [ ] Implemented| N/A                                      | Group26          |
| `EcucLinkerSymbolDef`                                   | [ ] Deferred| N/A                                      | Group19          |
| `EcucModuleConfigurationValues`                         | [ ] Implemented| N/A                                      | Group27          |
| `EcucModuleDef`                                         | [ ] Implemented| N/A                                      | Group26          |
| `EcucMultilineStringParamDef`                           | [ ] Implemented| N/A                                      | Group26          |
| `EcucMultiplicityConfigurationClass`                    | [ ] Implemented| N/A                                      | Group26          |
| `EcucNumericalParamValue`                               | [ ] Implemented| N/A                                      | Group27          |
| `EcucParamConfContainerDef`                             | [ ] Implemented| N/A                                      | Group26          |
| `EcucParameterDef`                                      | [ ] Implemented| N/A                                      | Group26          |
| `EcucParameterDerivationFormula`                        | [ ] Implemented| N/A                                      | Group19          |
| `EcucParameterValue`                                    | [ ] Implemented| N/A                                      | Group27          |
| `EcucQuery`                                             | [ ] Implemented| N/A                                      | Group26          |
| `EcucQueryExpression`                                   | [ ] Implemented| N/A                                      | Group19          |
| `EcucReferenceDef`                                      | [ ] Implemented| N/A                                      | Group19          |
| `EcucReferenceValue`                                    | [ ] Implemented| N/A                                      | Group27          |
| `EcucScopeEnum`                                         | [ ] Deferred| N/A                                      | Group19          |
| `EcucStringParamDef`                                    | [ ] Implemented| N/A                                      | Group26          |
| `EcucSymbolicNameReferenceDef`                          | [ ] Implemented| N/A                                      | Group19          |
| `EcucTextualParamValue`                                 | [ ] Implemented| N/A                                      | Group27          |
| `EcucUriReferenceDef`                                   | [ ] Implemented| N/A                                      | Group19          |
| `EcucValidationCondition`                               | [ ] Implemented| N/A                                      | Group27          |
| `EcucValueCollection`                                   | [ ] Deferred| N/A                                      | Group19          |
| `EcucValueConfigurationClass`                           | [ ] Implemented| N/A                                      | Group26          |
| `EmphasisText`                                          | [ ] Implemented| N/A                                      | Group21          |
| `EndToEndDescription`                                   | [x] Done    | d3db89bb98                               | Group10          |
| `EndToEndProfileBehaviorEnum`                           | [ ] Implemented| N/A                                      | Group34          |
| `EndToEndProtection`                                    | [ ] Implemented| N/A                                      | Group28          |
| `EndToEndProtectionISignalIPdu`                         | [ ] Deferred| N/A                                      | Group18          |
| `EndToEndProtectionSet`                                 | [x] Done    | 4a7d82ffc7                               | Group5           |
| `EndToEndProtectionVariablePrototype`                   | [x] Done    | 4a7d82ffc7                               | Group5           |
| `EndToEndTransformationComSpecProps`                    | [ ] Implemented| N/A                                      | Group28          |
| `EndToEndTransformationDescription`                     | [ ] Implemented| N/A                                      | Group34          |
| `EndToEndTransformationISignalProps`                    | [ ] Deferred| N/A                                      | Group18          |
| `EngineeringObject`                                     | [ ] Implemented| N/A                                      | Group21          |
| `Entry`                                                 | [x] Done    | 9005f6228e                               | Group3           |
| `ErrorTracerNeeds`                                      | [ ] Implemented| N/A                                      | Group23          |
| `EthGlobalTimeDomainProps`                              | [ ] Created | N/A                                      | Group34          |
| `EthGlobalTimeManagedCouplingPort`                      | [ ] Created | N/A                                      | Group34          |
| `EthGlobalTimeMessageFormatEnum`                        | [ ] Created | N/A                                      | Group34          |
| `EthIpProps`                                            | [ ] Created | N/A                                      | Group30          |
| `EthTSynCrcFlags`                                       | [ ] Created | N/A                                      | Group34          |
| `EthTSynSubTlvConfig`                                   | [ ] Created | N/A                                      | Group34          |
| `EthTcpIpIcmpProps`                                     | [x] Done    | c53a7febdc                               | Group5           |
| `EthTcpIpProps`                                         | [x] Done    | db98d8ff29                               | Group5           |
| `EthTpConfig`                                           | [ ] Created | N/A                                      | Group33          |
| `EthTpConnection`                                       | [ ] Created | N/A                                      | Group33          |
| `EthernetCluster`                                       | [ ] Implemented| N/A                                      | Group29          |
| `EthernetCommunicationConnector`                        | [ ] Implemented| N/A                                      | Group30          |
| `EthernetCommunicationController`                       | [ ] Implemented| N/A                                      | Group30          |
| `EthernetConnectionNegotiationEnum`                     | [ ] Implemented| N/A                                      | Group30          |
| `EthernetCouplingPortSchedulerEnum`                     | [ ] Implemented| N/A                                      | Group30          |
| `EthernetFrameTriggering`                               | [ ] Created | N/A                                      | Group33          |
| `EthernetMacLayerTypeEnum`                              | [ ] Implemented| N/A                                      | Group30          |
| `EthernetPhysicalChannel`                               | [x] Done    | 206cf29517                               | Group5           |
| `EthernetPhysicalLayerTypeEnum`                         | [ ] Implemented| N/A                                      | Group30          |
| `EthernetPriorityRegeneration`                          | [ ] Deferred| b1e4750b14                               | Group16          |
| `EthernetSwitchVlanEgressTaggingEnum`                   | [ ] Implemented| N/A                                      | Group30          |
| `EthernetSwitchVlanIngressTagEnum`                      | [ ] Implemented| N/A                                      | Group30          |
| `EthernetWakeupSleepOnDatalineConfig`                   | [ ] Created | N/A                                      | Group30          |
| `EthernetWakeupSleepOnDatalineConfigSet`                | [ ] Created | N/A                                      | Group30          |
| `EvaluatedVariantSet`                                   | [ ] Created | N/A                                      | Group21          |
| `EventAcceptanceStatusEnum`                             | [ ] Implemented| N/A                                      | Group29          |
| `EventControlledTiming`                                 | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `EventGroupControlTypeEnum`                             | [ ] Implemented| N/A                                      | Group32          |
| `EventHandler`                                          | [ ] Implemented| N/A                                      | Group32          |
| `EventObdReadinessGroup`                                | [ ] Created | N/A                                      | Group25          |
| `EventOccurrenceKindEnum`                               | [ ] Implemented| N/A                                      | Group35          |
| `EventTriggeringConstraint`                             | [ ] Implemented| N/A                                      | Group35          |
| `ExclusiveArea`                                         | [x] Done    | aae3890b67                               | Group22          |
| `ExclusiveAreaNestingOrder`                             | [x] Done    | af5498712f                               | Group22          |
| `ExecutableEntity`                                      | [x] Done    | 88b336bfe9                               | Group22          |
| `ExecutableEntityActivationReason`                      | [ ] Implemented| N/A                                      | Group28          |
| `ExecutionOrderConstraint`                              | [ ] Implemented| N/A                                      | Group35          |
| `ExecutionOrderConstraintTypeEnum`                      | [ ] Implemented| N/A                                      | Group35          |
| `ExecutionTime`                                         | [ ] Implemented| N/A                                      | Group23          |
| `ExecutionTimeConstraint`                               | [ ] Implemented| N/A                                      | Group35          |
| `ExecutionTimeTypeEnum`                                 | [ ] Implemented| N/A                                      | Group35          |
| `ExternalTriggerOccurredEvent`                          | [ ] Created | N/A                                      | Group28          |
| `ExternalTriggeringPoint`                               | [ ] Implemented| N/A                                      | Group29          |
| `ExternalTriggeringPointIdent`                          | [x] Done    | c04ca0f5b3                               | Group2           |
| `FMAttributeDef`                                        | [ ] Created | N/A                                      | Group36          |
| `FMAttributeValue`                                      | [ ] Created | N/A                                      | Group36          |
| `FMConditionByFeaturesAndAttributes`                    | [x] Done    | d69232bdf4                               | Group8           |
| `FMConditionByFeaturesAndSwSystemconsts`                | [x] Done    | d69232bdf4                               | Group8           |
| `FMFeature`                                             | [ ] Created | N/A                                      | Group36          |
| `FMFeatureDecomposition`                                | [ ] Created | N/A                                      | Group36          |
| `FMFeatureMap`                                          | [ ] Created | N/A                                      | Group36          |
| `FMFeatureMapAssertion`                                 | [ ] Created | N/A                                      | Group36          |
| `FMFeatureMapCondition`                                 | [ ] Created | N/A                                      | Group36          |
| `FMFeatureMapElement`                                   | [ ] Created | N/A                                      | Group36          |
| `FMFeatureModel`                                        | [ ] Created | N/A                                      | Group36          |
| `FMFeatureRelation`                                     | [ ] Created | N/A                                      | Group36          |
| `FMFeatureRestriction`                                  | [ ] Created | N/A                                      | Group36          |
| `FMFeatureSelection`                                    | [ ] Created | N/A                                      | Group36          |
| `FMFeatureSelectionSet`                                 | [ ] Created | N/A                                      | Group36          |
| `FMFeatureSelectionState`                               | [ ] Created | N/A                                      | Group36          |
| `FMFormulaByFeaturesAndAttributes`                      | [x] Done    | d69232bdf4                               | Group8           |
| `FMFormulaByFeaturesAndSwSystemconsts`                  | [x] Done    | d69232bdf4                               | Group8           |
| `Field`                                                 | [x] Done    | d31cad4d7e                               | Group11          |
| `FileInfoComment`                                       | [x] Done    | c62e1c8943                               | Group1           |
| `FilterDebouncingEnum`                                  | [ ] Implemented| N/A                                      | Group27          |
| `FirewallActionEnum`                                    | [x] Done    | ab2daa7785                               | Group3           |
| `FirewallRule`                                          | [x] Deferred| 00d011d4ad                               | Group1           |
| `FirewallRuleProps`                                     | [x] Done    | 89039bf2bb                               | Group7           |
| `FlatInstanceDescriptor`                                | [x] Done    | 9db34796eb                               | Group1           |
| `FlatMap`                                               | [x] Done    | 5eadca7853                               | Group1           |
| `FlexrayAbsolutelyScheduledTiming`                      | [ ] Deferred| N/A                                      | Group17          |
| `FlexrayArTpChannel`                                    | [ ] Created | N/A                                      | Group33          |
| `FlexrayArTpConfig`                                     | [ ] Created | N/A                                      | Group33          |
| `FlexrayArTpConnection`                                 | [ ] Created | N/A                                      | Group33          |
| `FlexrayArTpNode`                                       | [ ] Created | N/A                                      | Group33          |
| `FlexrayChannelName`                                    | [ ] Deferred| 7c137656f6                               | Group15          |
| `FlexrayCluster`                                        | [ ] Implemented| N/A                                      | Group29          |
| `FlexrayCommunicationConnector`                         | [ ] Deferred| N/A                                      | Group17          |
| `FlexrayCommunicationController`                        | [ ] Deferred| N/A                                      | Group17          |
| `FlexrayFifoConfiguration`                              | [ ] Implemented| N/A                                      | Group29          |
| `FlexrayFifoRange`                                      | [ ] Implemented| N/A                                      | Group29          |
| `FlexrayFrame`                                          | [x] Done    | 757aea1d17                               | Group6           |
| `FlexrayFrameTriggering`                                | [ ] Deferred| N/A                                      | Group17          |
| `FlexrayNmCluster`                                      | [x] Done    | 9c8e10b37f                               | Group6           |
| `FlexrayNmClusterCoupling`                              | [ ] Deferred| N/A                                      | Group18          |
| `FlexrayNmEcu`                                          | [x] Done    | 9c8e10b37f                               | Group6           |
| `FlexrayNmNode`                                         | [x] Done    | 9c8e10b37f                               | Group6           |
| `FlexrayNmScheduleVariant`                              | [ ] Implemented| N/A                                      | Group33          |
| `FlexrayPhysicalChannel`                                | [ ] Deferred| N/A                                      | Group17          |
| `FlexrayTpConfig`                                       | [ ] Created | N/A                                      | Group33          |
| `FlexrayTpConnection`                                   | [ ] Created | N/A                                      | Group33          |
| `FlexrayTpConnectionControl`                            | [ ] Created | N/A                                      | Group33          |
| `FlexrayTpEcu`                                          | [ ] Created | N/A                                      | Group33          |
| `FlexrayTpNode`                                         | [ ] Created | N/A                                      | Group33          |
| `FlexrayTpPduPool`                                      | [ ] Created | N/A                                      | Group33          |
| `FloatEnum`                                             | [x] Done    | 1649678501                               | Group22          |
| `FloatValueVariationPoint`                              | [x] Done    | d5c96fd954                               | Group8           |
| `FlowMeteringColorModeEnum`                             | [ ] Created | N/A                                      | Group30          |
| `ForbiddenSignalPath`                                   | [ ] Created | N/A                                      | Group31          |
| `FormulaExpression`                                     | [x] Done    | 88ed82bed3                               | Group8           |
| `FrArTpAckType`                                         | [ ] Created | N/A                                      | Group33          |
| `FrGlobalTimeDomainProps`                               | [ ] Created | N/A                                      | Group34          |
| `Frame`                                                 | [ ] Implemented| N/A                                      | Group31          |
| `FrameEnum`                                             | [x] Done    | 531991e029                               | Group3           |
| `FrameMapping`                                          | [ ] Deferred| N/A                                      | Group17          |
| `FramePid`                                              | [ ] Implemented| N/A                                      | Group31          |
| `FramePort`                                             | [x] Done    | 75683a2ede                               | Group5           |
| `FrameTriggering`                                       | [x] Done    | 206cf29517                               | Group5           |
| `FreeFormat`                                            | [ ] Implemented| N/A                                      | Group32          |
| `FreeFormatEntry`                                       | [ ] Implemented| N/A                                      | Group31          |
| `FullBindingTimeEnum`                                   | [ ] Created | N/A                                      | Group21          |
| `FunctionInhibitionAvailabilityNeeds`                   | [ ] Implemented| N/A                                      | Group29          |
| `FunctionInhibitionNeeds`                               | [x] Done    | 5c4c0963af                               | Group4           |
| `FurtherActionByteNeeds`                                | [x] Done    | 30e266fd91                               | Group5           |
| `Gateway`                                               | [ ] Deferred| N/A                                      | Group17          |
| `GeneralAnnotation`                                     | [x] Done    | ab2daa7785                               | Group3           |
| `GeneralParameter`                                      | [x] Done    | b622d5b424                               | Group9           |
| `GeneralPurposeConnection`                              | [ ] Created | N/A                                      | Group31          |
| `GeneralPurposeIPdu`                                    | [x] Done    | 75683a2ede                               | Group5           |
| `GeneralPurposePdu`                                     | [x] Done    | 75683a2ede                               | Group5           |
| `GenericEthernetFrame`                                  | [x] Done    | 675a97e967                               | Group6           |
| `GenericTp`                                             | [ ] Deferred| N/A                                      | Group16          |
| `GlobalSupervisionNeeds`                                | [x] Done    | 5c4c0963af                               | Group4           |
| `GlobalTimeCanMaster`                                   | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeCanSlave`                                    | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeCorrectionProps`                             | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeCouplingPortProps`                           | [ ] Implemented| N/A                                      | Group34          |
| `GlobalTimeCrcSupportEnum`                              | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeCrcValidationEnum`                           | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeDomain`                                      | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeEthMaster`                                   | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeEthSlave`                                    | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeFrMaster`                                    | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeFrSlave`                                     | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeGateway`                                     | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeIcvSupportEnum`                              | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeIcvVerificationEnum`                         | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeMaster`                                      | [ ] Created | N/A                                      | Group34          |
| `GlobalTimePortRoleEnum`                                | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeSlave`                                       | [ ] Created | N/A                                      | Group34          |
| `Graphic`                                               | [x] Done    | 06b46f32ba                               | Group3           |
| `GraphicFitEnum`                                        | [x] Done    | 5b543a21d4                               | Group3           |
| `GraphicNotationEnum`                                   | [x] Done    | f25e765d8b                               | Group3           |
| `HandleInvalidEnum`                                     | [x] Done    | 18271ddd84                               | Group1           |
| `HandleOutOfRangeEnum`                                  | [ ] Implemented| N/A                                      | Group27          |
| `HandleOutOfRangeStatusEnum`                            | [ ] Implemented| N/A                                      | Group27          |
| `HandleTimeoutEnum`                                     | [ ] Implemented| N/A                                      | Group27          |
| `HardwareConfiguration`                                 | [ ] Deferred| 35bfb17b7a                               | Group20          |
| `HardwareTestNeeds`                                     | [x] Done    | 5c4c0963af                               | Group4           |
| `HeapUsage`                                             | [x] Done    | a55d2092d0                               | Group22          |
| `HttpTp`                                                | [ ] Created | N/A                                      | Group32          |
| `HwAttributeDef`                                        | [x] Done    | 3912963bfd                               | Group7           |
| `HwAttributeLiteralDef`                                 | [x] Done    | 5d767ace9e                               | Group7           |
| `HwAttributeValue`                                      | [x] Done    | 269d34d90f                               | Group7           |
| `HwCategory`                                            | [x] Done    | b7e2199ac8                               | Group7           |
| `HwDescriptionEntity`                                   | [ ] Implemented| N/A                                      | Group27          |
| `HwElement`                                             | [x] Done    | 8c7f05d40a                               | Group1           |
| `HwElementConnector`                                    | [ ] Implemented| N/A                                      | Group27          |
| `HwPin`                                                 | [x] Done    | ff5b0e0865                               | Group1           |
| `HwPinConnector`                                        | [ ] Implemented| N/A                                      | Group27          |
| `HwPinGroup`                                            | [x] Done    | 69afffcc48                               | Group1           |
| `HwPinGroupConnector`                                   | [ ] Implemented| N/A                                      | Group27          |
| `HwPinGroupContent`                                     | [ ] Implemented| N/A                                      | Group27          |
| `HwPortMapping`                                         | [x] Done    | 7d94510497                               | Group7           |
| `HwType`                                                | [x] Done    | 29f338b3c0                               | Group1           |
| `IEEE1722TpAafAes3DataTypeEnum`                         | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAafConnection`                               | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAafFormatEnum`                               | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAafNominalRateEnum`                          | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAcfBus`                                      | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAcfBusPart`                                  | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAcfCan`                                      | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAcfCanMessageTypeEnum`                       | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAcfCanPart`                                  | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAcfConnection`                               | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAcfLin`                                      | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAcfLinPart`                                  | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAvConnection`                                | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpConfig`                                      | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpConnection`                                  | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpCrfConnection`                               | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpCrfPullEnum`                                 | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpCrfTypeEnum`                                 | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpIidcConnection`                              | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpRvfColorSpaceEnum`                           | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpRvfConnection`                               | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpRvfFrameRateEnum`                            | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpRvfPixelDepthEnum`                           | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpRvfPixelFormatEnum`                          | [ ] Created | N/A                                      | Group33          |
| `IPSecConfig`                                           | [ ] Deferred| 6c97ddc108                               | Group16          |
| `IPSecConfigProps`                                      | [ ] Deferred| N/A                                      | Group32          |
| `IPSecRule`                                             | [ ] Deferred| N/A                                      | Group32          |
| `IPdu`                                                  | [ ] Implemented| N/A                                      | Group31          |
| `IPduMapping`                                           | [x] Done    | 9c8e10b37f                               | Group6           |
| `IPduPort`                                              | [ ] Implemented| N/A                                      | Group31          |
| `IPduSignalProcessingEnum`                              | [ ] Implemented| N/A                                      | Group31          |
| `IPduTiming`                                            | [ ] Implemented| N/A                                      | Group31          |
| `IPsecDpdActionEnum`                                    | [ ] Deferred| N/A                                      | Group33          |
| `IPsecHeaderTypeEnum`                                   | [ ] Deferred| N/A                                      | Group33          |
| `IPsecIpProtocolEnum`                                   | [ ] Deferred| N/A                                      | Group32          |
| `IPsecModeEnum`                                         | [ ] Deferred| N/A                                      | Group32          |
| `IPsecPolicyEnum`                                       | [ ] Deferred| N/A                                      | Group32          |
| `IPv6ExtHeaderFilterList`                               | [ ] Deferred| 2d5b3256b4                               | Group16          |
| `IPv6ExtHeaderFilterSet`                                | [ ] Created | N/A                                      | Group32          |
| `ISignal`                                               | [ ] Implemented| N/A                                      | Group31          |
| `ISignalGroup`                                          | [ ] Implemented| N/A                                      | Group31          |
| `ISignalIPdu`                                           | [ ] Implemented| N/A                                      | Group31          |
| `ISignalIPduGroup`                                      | [ ] Deferred| 1e758bd44e                               | Group15          |
| `ISignalMapping`                                        | [ ] Deferred| N/A                                      | Group17          |
| `ISignalPort`                                           | [ ] Deferred| b5f92f4b28                               | Group15          |
| `ISignalProps`                                          | [ ] Implemented| N/A                                      | Group31          |
| `ISignalToIPduMapping`                                  | [ ] Implemented| N/A                                      | Group31          |
| `ISignalTriggering`                                     | [ ] Implemented| N/A                                      | Group31          |
| `ISignalTypeEnum`                                       | [ ] Implemented| N/A                                      | Group31          |
| `IcmpRule`                                              | [x] Deferred| 5ddaf1cf94                               | Group20          |
| `IdentCaption`                                          | [x] Done    | 2dd2f91845                               | Group1           |
| `Identifiable`                                          | [x] Done    | c17bfbf60f                               | Group1           |
| `Identifier`                                            | [ ] Implemented| N/A                                      | Group21          |
| `IdsDesign`                                             | [ ] Created | N/A                                      | Group36          |
| `IdsMgrCustomTimestampNeeds`                            | [x] Done    | b65fe94222                               | Group5           |
| `IdsMgrNeeds`                                           | [ ] Implemented| N/A                                      | Group29          |
| `IdsPlatformInstantiation`                              | [x] Done    | 5d4cc1c454                               | Group7           |
| `IdsmInstance`                                          | [ ] Created | N/A                                      | Group36          |
| `IdsmModuleInstantiation`                               | [x] Done    | 5d4cc1c454                               | Group7           |
| `IdsmRateLimitation`                                    | [ ] Created | N/A                                      | Group36          |
| `IdsmTrafficLimitation`                                 | [ ] Created | N/A                                      | Group36          |
| `Ieee1722Tp`                                            | [ ] Created | N/A                                      | Group32          |
| `Ieee1722TpEthernetFrame`                               | [ ] Created | N/A                                      | Group33          |
| `Implementation`                                        | [x] Done    | e7dfb875d9                               | Group1           |
| `ImplementationDataType`                                | [ ] Implemented| N/A                                      | Group28          |
| `ImplementationDataTypeElement`                         | [x] Done    | 8e9b2db86b                               | Group10          |
| `ImplementationDataTypeElementInPortInterfaceRef`       | [ ] Implemented| N/A                                      | Group34          |
| `ImplementationDataTypeSubElementRef`                   | [ ] Created | N/A                                      | Group27          |
| `ImplementationElementInParameterInstanceRef`           | [ ] Implemented| N/A                                      | Group23          |
| `ImplementationProps`                                   | [x] Done    | 3166f6e5d0                               | Group10          |
| `IncludedDataTypeSet`                                   | [ ] Implemented| N/A                                      | Group29          |
| `IncludedModeDeclarationGroupSet`                       | [x] Done    | b9ac782d1e                               | Group2           |
| `IndentSample`                                          | [ ] Implemented| N/A                                      | Group21          |
| `IndexEntry`                                            | [ ] Implemented| N/A                                      | Group21          |
| `IndexedArrayElement`                                   | [ ] Deferred| N/A                                      | Group17          |
| `IndicatorStatusNeeds`                                  | [ ] Implemented| N/A                                      | Group29          |
| `InfrastructureServices`                                | [ ] Implemented| N/A                                      | Group32          |
| `InitEvent`                                             | [x] Done    | 64ab725d50                               | Group2           |
| `InitialSdDelayConfig`                                  | [ ] Deferred| d7240be740                               | Group16          |
| `InnerPortGroupInCompositionInstanceRef`                | [x] Done    | 919fbc0d11                               | Group2           |
| `InstantiationDataDefProps`                             | [x] Done    | e2aa88eb41                               | Group10          |
| `InstantiationRTEEventProps`                            | [ ] Implemented| N/A                                      | Group27          |
| `InstantiationTimingEventProps`                         | [ ] Implemented| N/A                                      | Group27          |
| `IntegerValueVariationPoint`                            | [x] Done    | d5c96fd954                               | Group8           |
| `InternalBehavior`                                      | [x] Done    | 68e390b39e                               | Group22          |
| `InternalConstrs`                                       | [ ] Implemented| N/A                                      | Group28          |
| `InternalTriggerOccurredEvent`                          | [ ] Deferred| N/A                                      | Group12          |
| `InternalTriggeringPoint`                               | [ ] Deferred| N/A                                      | Group12          |
| `InterpolationRoutine`                                  | [x] Done    | 992a894be3                               | Group5           |
| `InterpolationRoutineMapping`                           | [x] Done    | d00d57b42d                               | Group5           |
| `InterpolationRoutineMappingSet`                        | [x] Done    | f3152abb23                               | Group5           |
| `IntervalTypeEnum`                                      | [ ] Implemented| N/A                                      | Group28          |
| `InvalidationPolicy`                                    | [x] Done    | 1000053d88                               | Group1           |
| `InvertCondition`                                       | [ ] Created | N/A                                      | Group36          |
| `IoHwAbstractionServerAnnotation`                       | [ ] Implemented| N/A                                      | Group27          |
| `Ip4AddressString`                                      | [ ] Implemented| N/A                                      | Group21          |
| `Ip6AddressString`                                      | [ ] Implemented| N/A                                      | Group21          |
| `IpAddressKeepEnum`                                     | [ ] Deferred| c5bb322323                               | Group16          |
| `Ipv4AddressSourceEnum`                                 | [ ] Deferred| 6c97ddc108                               | Group16          |
| `Ipv4ArpProps`                                          | [ ] Created | N/A                                      | Group30          |
| `Ipv4AutoIpProps`                                       | [ ] Created | N/A                                      | Group30          |
| `Ipv4Configuration`                                     | [ ] Deferred| 6c97ddc108                               | Group16          |
| `Ipv4DhcpServerConfiguration`                           | [ ] Implemented| N/A                                      | Group30          |
| `Ipv4FragmentationProps`                                | [ ] Created | N/A                                      | Group30          |
| `Ipv4Props`                                             | [ ] Created | N/A                                      | Group30          |
| `Ipv4Rule`                                              | [x] Deferred| b4096068d6                               | Group20          |
| `Ipv6AddressSourceEnum`                                 | [ ] Deferred| c5bb322323                               | Group16          |
| `Ipv6Configuration`                                     | [ ] Implemented| N/A                                      | Group32          |
| `Ipv6DhcpServerConfiguration`                           | [ ] Implemented| N/A                                      | Group30          |
| `Ipv6FragmentationProps`                                | [ ] Created | N/A                                      | Group30          |
| `Ipv6NdpProps`                                          | [ ] Created | N/A                                      | Group30          |
| `Ipv6Props`                                             | [ ] Created | N/A                                      | Group30          |
| `Ipv6Rule`                                              | [x] Deferred| 18ee06b97c                               | Group20          |
| `Item`                                                  | [x] Done    | cf8b43c369                               | Group9           |
| `ItemLabelPosEnum`                                      | [ ] Implemented| N/A                                      | Group21          |
| `J1939Cluster`                                          | [x] Done    | 44a70c3256                               | Group5           |
| `J1939ControllerApplication`                            | [ ] Created | N/A                                      | Group30          |
| `J1939ControllerApplicationToJ1939NmNodeMapping`        | [ ] Created | N/A                                      | Group30          |
| `J1939DcmDm19Support`                                   | [x] Done    | 839c29d67e                               | Group5           |
| `J1939DcmIPdu`                                          | [ ] Created | N/A                                      | Group31          |
| `J1939NmAddressConfigurationCapabilityEnum`             | [ ] Implemented| N/A                                      | Group33          |
| `J1939NmCluster`                                        | [x] Done    | 9c8e10b37f                               | Group6           |
| `J1939NmEcu`                                            | [x] Done    | 9c8e10b37f                               | Group6           |
| `J1939NmNode`                                           | [ ] Implemented| N/A                                      | Group33          |
| `J1939NodeName`                                         | [ ] Implemented| N/A                                      | Group33          |
| `J1939RmIncomingRequestServiceNeeds`                    | [x] Done    | 9784766a6d                               | Group5           |
| `J1939RmOutgoingRequestServiceNeeds`                    | [x] Done    | 2b39e92976                               | Group5           |
| `J1939SharedAddressCluster`                             | [x] Done    | d3dc82098e                               | Group5           |
| `J1939TpConfig`                                         | [ ] Created | N/A                                      | Group33          |
| `J1939TpConnection`                                     | [ ] Created | N/A                                      | Group33          |
| `J1939TpNode`                                           | [ ] Created | N/A                                      | Group33          |
| `J1939TpPg`                                             | [ ] Created | N/A                                      | Group33          |
| `KeepWithPreviousEnum`                                  | [x] Done    | d447cf2a51                               | Group3           |
| `Keyword`                                               | [x] Done    | 4ed5a2fe2d                               | Group7           |
| `KeywordSet`                                            | [x] Done    | a6a1d31ccc                               | Group7           |
| `LEnum`                                                 | [x] Done    | 4566d4d4f7                               | Group22          |
| `LGraphic`                                              | [x] Done    | e4b1acf6c9                               | Group3           |
| `LLongName`                                             | [ ] Implemented| N/A                                      | Group21          |
| `LOverviewParagraph`                                    | [x] Done    | 764ef1c589                               | Group9           |
| `LParagraph`                                            | [x] Done    | 7fa4a01f74                               | Group3           |
| `LPlainText`                                            | [x] Done    | 1de91de480                               | Group9           |
| `LVerbatim`                                             | [x] Done    | d616f3d1ef                               | Group9           |
| `LabeledItem`                                           | [ ] Implemented| N/A                                      | Group21          |
| `LabeledList`                                           | [ ] Implemented| N/A                                      | Group21          |
| `LanguageSpecific`                                      | [x] Done    | 4566d4d4f7                               | Group22          |
| `LatencyConstraintTypeEnum`                             | [ ] Implemented| N/A                                      | Group35          |
| `LatencyTimingConstraint`                               | [ ] Implemented| N/A                                      | Group35          |
| `LetDataExchangeParadigmEnum`                           | [ ] Implemented| N/A                                      | Group35          |
| `LifeCycleInfo`                                         | [x] Done    | 5836e6eb08                               | Group8           |
| `LifeCycleInfoSet`                                      | [x] Done    | 11bd9cd848                               | Group8           |
| `LifeCyclePeriod`                                       | [x] Done    | b572582c11                               | Group8           |
| `LifeCycleState`                                        | [ ] Deferred| 8f363946f9                               | Group22          |
| `LifeCycleStateDefinitionGroup`                         | [ ] Deferred| 0c87fdbee4                               | Group22          |
| `Limit`                                                 | [ ] Implemented| N/A                                      | Group28          |
| `LimitValueVariationPoint`                              | [x] Done    | d5c96fd954                               | Group8           |
| `LinChecksumType`                                       | [ ] Created | N/A                                      | Group31          |
| `LinCluster`                                            | [ ] Implemented| N/A                                      | Group29          |
| `LinCommunicationConnector`                             | [ ] Deferred| N/A                                      | Group17          |
| `LinCommunicationController`                            | [ ] Implemented| N/A                                      | Group29          |
| `LinConfigurableFrame`                                  | [ ] Implemented| N/A                                      | Group29          |
| `LinConfigurationEntry`                                 | [ ] Implemented| N/A                                      | Group31          |
| `LinErrorResponse`                                      | [ ] Implemented| N/A                                      | Group29          |
| `LinEventTriggeredFrame`                                | [ ] Created | N/A                                      | Group31          |
| `LinFrame`                                              | [ ] Implemented| N/A                                      | Group31          |
| `LinFrameTriggering`                                    | [ ] Implemented| N/A                                      | Group31          |
| `LinMaster`                                             | [ ] Implemented| N/A                                      | Group29          |
| `LinOrderedConfigurableFrame`                           | [ ] Implemented| N/A                                      | Group29          |
| `LinPhysicalChannel`                                    | [ ] Implemented| N/A                                      | Group29          |
| `LinScheduleTable`                                      | [ ] Deferred| N/A                                      | Group17          |
| `LinSlave`                                              | [ ] Created | N/A                                      | Group29          |
| `LinSlaveConfig`                                        | [ ] Implemented| N/A                                      | Group29          |
| `LinSlaveConfigIdent`                                   | [ ] Implemented| N/A                                      | Group29          |
| `LinSporadicFrame`                                      | [ ] Created | N/A                                      | Group31          |
| `LinTpConfig`                                           | [ ] Implemented| N/A                                      | Group33          |
| `LinTpConnection`                                       | [ ] Deferred| N/A                                      | Group18          |
| `LinTpNode`                                             | [ ] Implemented| N/A                                      | Group33          |
| `LinUnconditionalFrame`                                 | [ ] Implemented| N/A                                      | Group31          |
| `Linker`                                                | [x] Done    | 20003dc3cc                               | Group1           |
| `List`                                                  | [ ] Created | N/A                                      | Group21          |
| `ListEnum`                                              | [x] Done    | 0623068af8                               | Group9           |
| `LogAndTraceMessageCollectionSet`                       | [ ] Created | N/A                                      | Group36          |
| `LogTraceDefaultLogLevelEnum`                           | [x] Done    | f1eb819e47                               | Group5           |
| `MacAddressString`                                      | [x] Deferred| 1fd0b00607                               | Group20          |
| `MacMulticastConfiguration`                             | [ ] Created | N/A                                      | Group32          |
| `MacMulticastGroup`                                     | [ ] Deferred| b1e4750b14                               | Group16          |
| `MacSecCapabilityEnum`                                  | [ ] Implemented| N/A                                      | Group30          |
| `MacSecCipherSuiteConfig`                               | [ ] Implemented| N/A                                      | Group30          |
| `MacSecConfidentialityOffsetEnum`                       | [ ] Implemented| N/A                                      | Group30          |
| `MacSecCryptoAlgoConfig`                                | [ ] Implemented| N/A                                      | Group30          |
| `MacSecFailPermissiveModeEnum`                          | [ ] Implemented| N/A                                      | Group30          |
| `MacSecGlobalKayProps`                                  | [ ] Implemented| N/A                                      | Group30          |
| `MacSecKayParticipant`                                  | [ ] Implemented| N/A                                      | Group30          |
| `MacSecLocalKayProps`                                   | [ ] Implemented| N/A                                      | Group30          |
| `MacSecParticipantSet`                                  | [ ] Created | N/A                                      | Group30          |
| `MacSecProps`                                           | [ ] Implemented| N/A                                      | Group30          |
| `MacSecRoleEnum`                                        | [ ] Implemented| N/A                                      | Group30          |
| `Map`                                                   | [x] Done    | 43ec8ade8c                               | Group3           |
| `MappingConstraint`                                     | [ ] Created | N/A                                      | Group30          |
| `MappingDirectionEnum`                                  | [ ] Implemented| N/A                                      | Group27          |
| `MappingScopeEnum`                                      | [ ] Created | N/A                                      | Group30          |
| `MaxCommModeEnum`                                       | [ ] Implemented| N/A                                      | Group23          |
| `MaximumMessageLengthType`                              | [ ] Created | N/A                                      | Group33          |
| `McDataAccessDetails`                                   | [ ] Implemented| N/A                                      | Group23          |
| `McDataInstance`                                        | [ ] Implemented| N/A                                      | Group23          |
| `McFunction`                                            | [ ] Implemented| N/A                                      | Group23          |
| `McFunctionDataRefSet`                                  | [ ] Implemented| N/A                                      | Group23          |
| `McGroup`                                               | [ ] Implemented| N/A                                      | Group23          |
| `McGroupDataRefSet`                                     | [ ] Implemented| N/A                                      | Group23          |
| `McParameterElementGroup`                               | [ ] Implemented| N/A                                      | Group23          |
| `McSupportData`                                         | [ ] Implemented| N/A                                      | Group23          |
| `McSwEmulationMethodSupport`                            | [ ] Implemented| N/A                                      | Group23          |
| `McdIdentifier`                                         | [ ] Implemented| N/A                                      | Group21          |
| `MeasuredExecutionTime`                                 | [ ] Implemented| N/A                                      | Group23          |
| `MeasuredHeapUsage`                                     | [ ] Implemented| N/A                                      | Group23          |
| `MeasuredStackUsage`                                    | [ ] Deferred| adc2e5eeb7                               | Group20          |
| `MemoryAllocationKeywordPolicyType`                     | [x] Done    | 70ce06f500                               | Group22          |
| `MemorySection`                                         | [ ] Deferred| a579a3592e                               | Group20          |
| `MemorySectionLocation`                                 | [ ] Implemented| N/A                                      | Group23          |
| `MemorySectionType`                                     | [x] Done    | 70ce06f500                               | Group22          |
| `MetaDataItem`                                          | [x] Done    | e69a025254                               | Group2           |
| `MetaDataItemSet`                                       | [x] Done    | e69a025254                               | Group2           |
| `MimeTypeString`                                        | [x] Done    | 01cc23df4e                               | Group3           |
| `MirroringProtocolEnum`                                 | [ ] Created | N/A                                      | Group33          |
| `MixedContentForLongName`                               | [ ] Implemented| N/A                                      | Group21          |
| `MixedContentForOverviewParagraph`                      | [x] Done    | 18b494eba5                               | Group8           |
| `MixedContentForParagraph`                              | [x] Done    | bf9114cb01                               | Group3           |
| `MixedContentForPlainText`                              | [x] Done    | 4a95d1d305                               | Group8           |
| `MixedContentForUnitNames`                              | [x] Done    | 3d47eb65c8                               | Group8           |
| `MixedContentForVerbatim`                               | [x] Done    | 74549e6a51                               | Group8           |
| `MlFigure`                                              | [x] Done    | 9225ed1572                               | Group3           |
| `MlFormula`                                             | [ ] Implemented| N/A                                      | Group21          |
| `ModeAccessPoint`                                       | [ ] Deferred| N/A                                      | Group12          |
| `ModeAccessPointIdent`                                  | [x] Done    | 918013a6ce                               | Group1           |
| `ModeActivationKind`                                    | [x] Done    | 1625966930                               | Group11          |
| `ModeDeclaration`                                       | [x] Done    | e3d79f89ca                               | Group22          |
| `ModeDeclarationGroup`                                  | [x] Done    | e3d79f89ca                               | Group22          |
| `ModeDeclarationGroupPrototype`                         | [x] Done    | 51f2e1155f                               | Group1           |
| `ModeDeclarationGroupPrototypeMapping`                  | [x] Done    | 96e9f073a2                               | Group11          |
| `ModeDeclarationMapping`                                | [ ] Implemented| N/A                                      | Group27          |
| `ModeDeclarationMappingSet`                             | [x] Done    | eeec29b637                               | Group1           |
| `ModeDrivenTransmissionModeCondition`                   | [x] Done    | 206cf29517                               | Group5           |
| `ModeErrorBehavior`                                     | [x] Done    | e3d79f89ca                               | Group22          |
| `ModeErrorReactionPolicyEnum`                           | [x] Done    | e3d79f89ca                               | Group22          |
| `ModeGroupInAtomicSwcInstanceRef`                       | [x] Done    | cdb0951050                               | Group11          |
| `ModeInBswInstanceRef`                                  | [ ] Implemented| N/A                                      | Group35          |
| `ModeInSwcBswInstanceRef`                               | [x] Done    | 71ca6a5415                               | Group8           |
| `ModeInSwcInstanceRef`                                  | [x] Done    | 70dcc26975                               | Group8           |
| `ModeInterfaceMapping`                                  | [x] Done    | a598489544                               | Group11          |
| `ModePortAnnotation`                                    | [ ] Implemented| N/A                                      | Group27          |
| `ModeRequestTypeMap`                                    | [x] Done    | 2b824ca5f8                               | Group11          |
| `ModeSwitchEventTriggeredActivity`                      | [x] Done    | 8fa7710539                               | Group10          |
| `ModeSwitchInterface`                                   | [ ] Implemented| N/A                                      | Group27          |
| `ModeSwitchPoint`                                       | [ ] Deferred| N/A                                      | Group12          |
| `ModeSwitchReceiverComSpec`                             | [x] Done    | 67324d240c                               | Group10          |
| `ModeSwitchSenderComSpec`                               | [x] Done    | 3fbf07cc78                               | Group10          |
| `ModeSwitchedAckEvent`                                  | [ ] Implemented| N/A                                      | Group28          |
| `ModeSwitchedAckRequest`                                | [x] Done    | f587d873eb                               | Group10          |
| `ModeTransition`                                        | [x] Done    | e3d79f89ca                               | Group22          |
| `Modification`                                          | [x] Done    | 008307967e                               | Group9           |
| `ModuleConfiguration`                                   | [ ] Deferred| N/A                                      | Group19          |
| `MonotonyEnum`                                          | [ ] Implemented| N/A                                      | Group28          |
| `MsrQueryArg`                                           | [x] Done    | 4566d4d4f7                               | Group22          |
| `MsrQueryChapter`                                       | [x] Done    | 50103018c3                               | Group3           |
| `MsrQueryP1`                                            | [x] Done    | 8da723c461                               | Group3           |
| `MsrQueryProps`                                         | [x] Done    | 4566d4d4f7                               | Group22          |
| `MsrQueryResultChapter`                                 | [x] Done    | fb505d3551                               | Group3           |
| `MsrQueryResultTopic1`                                  | [x] Done    | 09314bd3ad                               | Group3           |
| `MsrQueryTopic1`                                        | [x] Done    | a09f0cdfbf                               | Group3           |
| `MultiLanguageOverviewParagraph`                        | [x] Done    | 8294e5eeab                               | Group22          |
| `MultiLanguageParagraph`                                | [x] Done    | 77074563dc                               | Group3           |
| `MultiLanguagePlainText`                                | [x] Done    | 53af1b9a63                               | Group22          |
| `MultiLanguageVerbatim`                                 | [ ] Implemented| N/A                                      | Group21          |
| `MultidimensionalTime`                                  | [x] Done    | b572582c11                               | Group8           |
| `MultilanguageLongName`                                 | [x] Done    | 87855dea47                               | Group3           |
| `MultilanguageReferrable`                               | [x] Done    | 7c7157a02b                               | Group1           |
| `MultiplexedIPdu`                                       | [ ] Deferred| eba346cb51                               | Group15          |
| `MultiplexedPart`                                       | [ ] Deferred| 66512d0602                               | Group15          |
| `MultiplicityRestrictionWithSeverity`                   | [ ] Created | N/A                                      | Group36          |
| `NPdu`                                                  | [ ] Implemented| N/A                                      | Group31          |
| `NameTokens`                                            | [x] Done    | c8a3ff507d                               | Group3           |
| `NativeDeclarationString`                               | [ ] Implemented| N/A                                      | Group21          |
| `NetworkEndpoint`                                       | [ ] Deferred| 6c97ddc108                               | Group16          |
| `NetworkEndpointAddress`                                | [x] Done    | c052de0226                               | Group6           |
| `NetworkLayerRule`                                      | [ ] Deferred| 529858d9c9                               | Group20          |
| `NetworkSegmentIdentification`                          | [ ] Created | N/A                                      | Group34          |
| `NetworkTargetAddressType`                              | [ ] Implemented| N/A                                      | Group33          |
| `NmCluster`                                             | [x] Done    | ae48471063                               | Group6           |
| `NmClusterCoupling`                                     | [x] Done    | 9c8e10b37f                               | Group6           |
| `NmConfig`                                              | [x] Done    | 757aea1d17                               | Group6           |
| `NmCoordinator`                                         | [ ] Created | N/A                                      | Group33          |
| `NmCoordinatorRoleEnum`                                 | [ ] Implemented| N/A                                      | Group33          |
| `NmEcu`                                                 | [ ] Deferred| N/A                                      | Group18          |
| `NmNode`                                                | [ ] Implemented| N/A                                      | Group33          |
| `NmPdu`                                                 | [ ] Implemented| N/A                                      | Group31          |
| `NonqueuedReceiverComSpec`                              | [ ] Implemented| N/A                                      | Group27          |
| `NonqueuedSenderComSpec`                                | [ ] Implemented| N/A                                      | Group27          |
| `NotAvailableValueSpecification`                        | [ ] Implemented| N/A                                      | Group28          |
| `Note`                                                  | [ ] Implemented| N/A                                      | Group21          |
| `NoteTypeEnum`                                          | [ ] Implemented| N/A                                      | Group21          |
| `NumericalOrText`                                       | [ ] Implemented| N/A                                      | Group28          |
| `NumericalRuleBasedValueSpecification`                  | [ ] Implemented| N/A                                      | Group28          |
| `NumericalValueSpecification`                           | [x] Done    | b16a369151                               | Group9           |
| `NumericalValueVariationPoint`                          | [x] Done    | d5c96fd954                               | Group8           |
| `NvBlockDataMapping`                                    | [x] Done    | cf9621f708                               | Group10          |
| `NvBlockDescriptor`                                     | [x] Done    | e5d43e9b06                               | Group10          |
| `NvBlockNeeds`                                          | [x] Done    | 72d998faaa                               | Group10          |
| `NvBlockNeedsReliabilityEnum`                           | [x] Done    | 90b381db32                               | Group10          |
| `NvBlockNeedsWritingPriorityEnum`                       | [x] Done    | 5a36c87687                               | Group10          |
| `NvBlockSwComponentType`                                | [ ] Implemented| N/A                                      | Group29          |
| `NvDataInterface`                                       | [x] Done    | 1d666bc11b                               | Group1           |
| `NvDataPortAnnotation`                                  | [ ] Implemented| N/A                                      | Group27          |
| `NvProvideComSpec`                                      | [x] Done    | a5c437cc82                               | Group10          |
| `NvRequireComSpec`                                      | [x] Done    | cbdf05b372                               | Group10          |
| `ObdControlServiceNeeds`                                | [ ] Implemented| N/A                                      | Group29          |
| `ObdInfoServiceNeeds`                                   | [ ] Implemented| N/A                                      | Group29          |
| `ObdMonitorServiceNeeds`                                | [ ] Implemented| N/A                                      | Group29          |
| `ObdPidServiceNeeds`                                    | [ ] Implemented| N/A                                      | Group29          |
| `ObdRatioConnectionKindEnum`                            | [ ] Implemented| N/A                                      | Group29          |
| `ObdRatioDenominatorNeeds`                              | [ ] Implemented| N/A                                      | Group29          |
| `ObdRatioServiceNeeds`                                  | [ ] Implemented| N/A                                      | Group29          |
| `OffsetTimingConstraint`                                | [x] Done    | e305e80e2a                               | Group8           |
| `OperationCycleTypeEnum`                                | [ ] Implemented| N/A                                      | Group29          |
| `OperationInAtomicSwcInstanceRef`                       | [x] Done    | 5d9a9f9600                               | Group11          |
| `OperationInSystemInstanceRef`                          | [x] Done    | 4e0c3cbe68                               | Group5           |
| `OperationInvokedEvent`                                 | [ ] Deferred| N/A                                      | Group12          |
| `OrderedMaster`                                         | [x] Done    | 5d62450236                               | Group6           |
| `OrientEnum`                                            | [x] Done    | 9223f504b5                               | Group3           |
| `OsTaskExecutionEvent`                                  | [ ] Created | N/A                                      | Group28          |
| `OsTaskPreemptabilityEnum`                              | [x] Done    | c53a7febdc                               | Group5           |
| `OsTaskProxy`                                           | [x] Done    | 61ccaa68eb                               | Group5           |
| `PModeGroupInAtomicSwcInstanceRef`                      | [x] Done    | f517d795f6                               | Group11          |
| `POperationInAtomicSwcInstanceRef`                      | [x] Done    | b6b0ea8cf7                               | Group11          |
| `PPortComSpec`                                          | [ ] Implemented| N/A                                      | Group27          |
| `PPortInCompositionInstanceRef`                         | [ ] Deferred| 74e821ccb8                               | Group11          |
| `PPortPrototype`                                        | [x] Done    | 0927333086                               | Group2           |
| `PRPortPrototype`                                       | [x] Done    | 043de7436d                               | Group2           |
| `PTriggerInAtomicSwcTypeInstanceRef`                    | [ ] Deferred| 74e821ccb8                               | Group11          |
| `PackageableElement`                                    | [x] Done    | bb032ddd55                               | Group1           |
| `Paginateable`                                          | [x] Done    | 20e6ee88d0                               | Group3           |
| `ParameterAccess`                                       | [x] Done    | 3b9f111270                               | Group12          |
| `ParameterDataPrototype`                                | [x] Done    | 70ce06f500                               | Group22          |
| `ParameterInAtomicSWCTypeInstanceRef`                   | [ ] Implemented| N/A                                      | Group28          |
| `ParameterInterface`                                    | [x] Done    | 6bf99879eb                               | Group1           |
| `ParameterPortAnnotation`                               | [ ] Implemented| N/A                                      | Group27          |
| `ParameterProvideComSpec`                               | [ ] Implemented| N/A                                      | Group27          |
| `ParameterRequireComSpec`                               | [x] Done    | 6cf8476adb                               | Group10          |
| `ParameterSwComponentType`                              | [ ] Created | N/A                                      | Group27          |
| `PassThroughSwConnector`                                | [ ] Implemented| N/A                                      | Group27          |
| `PayloadBytePatternRule`                                | [ ] Deferred| 8f863fe9dd                               | Group20          |
| `PayloadBytePatternRulePart`                            | [x] Deferred| 8c72c71709                               | Group20          |
| `Pdu`                                                   | [ ] Implemented| N/A                                      | Group31          |
| `PduActivationRoutingGroup`                             | [ ] Implemented| N/A                                      | Group32          |
| `PduCollectionSemanticsEnum`                            | [ ] Deferred| 4b7c8dc79c                               | Group16          |
| `PduCollectionTriggerEnum`                              | [x] Done    | 64d125ffae                               | Group5           |
| `PduMappingDefaultValue`                                | [x] Done    | 9c8e10b37f                               | Group6           |
| `PduToFrameMapping`                                     | [ ] Implemented| N/A                                      | Group31          |
| `PduTriggering`                                         | [ ] Implemented| N/A                                      | Group31          |
| `PdurIPduGroup`                                         | [x] Done    | c53a7febdc                               | Group5           |
| `PerInstanceMemory`                                     | [x] Done    | f35aa0cd0a                               | Group2           |
| `PerInstanceMemorySize`                                 | [x] Done    | df36bbb1fa                               | Group10          |
| `PeriodicEventTriggering`                               | [ ] Implemented| N/A                                      | Group35          |
| `PermissibleSignalPath`                                 | [ ] Created | N/A                                      | Group31          |
| `PgwideEnum`                                            | [x] Done    | 1649678501                               | Group22          |
| `PhysConstrs`                                           | [ ] Implemented| N/A                                      | Group28          |
| `PhysicalChannel`                                       | [ ] Implemented| N/A                                      | Group29          |
| `PhysicalDimension`                                     | [ ] Implemented| N/A                                      | Group28          |
| `PhysicalDimensionMapping`                              | [ ] Created | N/A                                      | Group28          |
| `PhysicalDimensionMappingSet`                           | [ ] Created | N/A                                      | Group28          |
| `PlatformModuleEthernetEndpointConfiguration`           | [x] Done    | 5d4cc1c454                               | Group7           |
| `PlcaProps`                                             | [ ] Implemented| N/A                                      | Group30          |
| `PncGatewayTypeEnum`                                    | [ ] Deferred| 7c137656f6                               | Group15          |
| `PncMapping`                                            | [ ] Created | N/A                                      | Group31          |
| `PortAPIOption`                                         | [x] Done    | 7c67628122                               | Group2           |
| `PortDefinedArgumentValue`                              | [x] Done    | 7fc79e4b73                               | Group2           |
| `PortElementToCommunicationResourceMapping`             | [ ] Created | N/A                                      | Group34          |
| `PortGroup`                                             | [x] Done    | d6512dbbec                               | Group2           |
| `PortGroupInSystemInstanceRef`                          | [x] Done    | 19c327cca6                               | Group5           |
| `PortInCompositionTypeInstanceRef`                      | [x] Done    | a6d84b2601                               | Group2           |
| `PortInterface`                                         | [ ] Implemented| N/A                                      | Group27          |
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
| `PostBuildVariantCriterionValueSet`                     | [ ] Created | N/A                                      | Group36          |
| `PredefinedChapter`                                     | [x] Done    | 0af25ab2e5                               | Group22          |
| `PredefinedVariant`                                     | [ ] Implemented| N/A                                      | Group21          |
| `PrimitiveAttributeCondition`                           | [ ] Created | N/A                                      | Group36          |
| `PrimitiveAttributeTailoring`                           | [ ] Created | N/A                                      | Group36          |
| `PrimitiveIdentifier`                                   | [ ] Implemented| N/A                                      | Group21          |
| `PrivacyLevel`                                          | [x] Done    | fb222ae5b2                               | Group5           |
| `PrmChar`                                               | [x] Done    | 8be54a00d1                               | Group9           |
| `PrmCharAbsTol`                                         | [x] Done    | e6c467d5f8                               | Group9           |
| `PrmCharContents`                                       | [x] Done    | 9494a593a2                               | Group9           |
| `PrmCharMinTypMax`                                      | [x] Done    | 376f43f648                               | Group9           |
| `PrmCharNumericalContents`                              | [x] Done    | 51ded41bf8                               | Group9           |
| `PrmCharNumericalValue`                                 | [x] Done    | 2f1c852dbb                               | Group9           |
| `PrmCharTextualContents`                                | [x] Done    | 83a56461a1                               | Group9           |
| `Prms`                                                  | [x] Done    | f05d3afdfa                               | Group9           |
| `ProcessingKindEnum`                                    | [ ] Implemented| N/A                                      | Group27          |
| `ProgramminglanguageEnum`                               | [x] Done    | be79d7993b                               | Group1           |
| `ProvidedServiceInstance`                               | [ ] Implemented| N/A                                      | Group32          |
| `PulseTestEnum`                                         | [ ] Implemented| N/A                                      | Group27          |
| `QueuedReceiverComSpec`                                 | [x] Done    | bb5804989f                               | Group10          |
| `QueuedSenderComSpec`                                   | [x] Done    | 4a7d82ffc7                               | Group5           |
| `RModeGroupInAtomicSWCInstanceRef`                      | [x] Done    | 7dd87307dd                               | Group11          |
| `RModeInAtomicSwcInstanceRef`                           | [x] Done    | 5a3a7d14c0                               | Group11          |
| `ROperationInAtomicSwcInstanceRef`                      | [x] Done    | 74e821ccb8                               | Group11          |
| `RPortComSpec`                                          | [ ] Implemented| N/A                                      | Group27          |
| `RPortInCompositionInstanceRef`                         | [ ] Deferred| 74e821ccb8                               | Group11          |
| `RPortPrototype`                                        | [x] Done    | 2cd6f3c46e                               | Group2           |
| `RTEEvent`                                              | [x] Done    | f0483d5732                               | Group2           |
| `RVariableInAtomicSwcInstanceRef`                       | [ ] Deferred| 74e821ccb8                               | Group11          |
| `RamBlockStatusControlEnum`                             | [x] Done    | 343d2af672                               | Group10          |
| `RapidPrototypingScenario`                              | [ ] Created | N/A                                      | Group29          |
| `ReceiverAnnotation`                                    | [ ] Created | N/A                                      | Group27          |
| `ReceiverComSpec`                                       | [ ] Implemented| N/A                                      | Group27          |
| `ReceptionComSpecProps`                                 | [x] Done    | 0ba890ba88                               | Group10          |
| `RecordLayoutIteratorPoint`                             | [x] Done    | 2acaf7a45f                               | Group3           |
| `RecordValueSpecification`                              | [x] Done    | b1c7030b10                               | Group3           |
| `ReentrancyLevelEnum`                                   | [x] Done    | 286c7c5870                               | Group10          |
| `Ref`                                                   | [x] Done    | 0518a7bca2                               | Group3           |
| `ReferenceBase`                                         | [x] Done    | 192dfd9467                               | Group1           |
| `ReferenceCondition`                                    | [ ] Created | N/A                                      | Group36          |
| `ReferenceTailoring`                                    | [ ] Created | N/A                                      | Group36          |
| `ReferenceValueSpecification`                           | [ ] Implemented| N/A                                      | Group28          |
| `Referrable`                                            | [ ] Implemented| N/A                                      | Group21          |
| `ReferrableSubtypesEnum`                                | [ ] Implemented| N/A                                      | Group21          |
| `RegularExpression`                                     | [ ] Implemented| N/A                                      | Group21          |
| `RelativeTolerance`                                     | [ ] Created | N/A                                      | Group31          |
| `RequestResponseDelay`                                  | [ ] Deferred| d7240be740                               | Group16          |
| `ResolutionPolicyEnum`                                  | [x] Done    | f0a7460898                               | Group3           |
| `ResourceConsumption`                                   | [x] Done    | 0404020952                               | Group1           |
| `RestrictionWithSeverity`                               | [ ] Created | N/A                                      | Group36          |
| `ResumePosition`                                        | [ ] Deferred| N/A                                      | Group17          |
| `RevisionLabelString`                                   | [ ] Created | N/A                                      | Group21          |
| `RoleBasedBswModuleEntryAssignment`                     | [ ] Implemented| N/A                                      | Group23          |
| `RoleBasedDataAssignment`                               | [x] Done    | 5989355419                               | Group10          |
| `RoleBasedDataTypeAssignment`                           | [ ] Implemented| N/A                                      | Group23          |
| `RoleBasedPortAssignment`                               | [x] Done    | f94da3dd92                               | Group10          |
| `RoleBasedResourceDependency`                           | [ ] Created | N/A                                      | Group26          |
| `RootSwCompositionPrototype`                            | [x] Done    | 671dfc3835                               | Group1           |
| `RoughEstimateHeapUsage`                                | [ ] Implemented| N/A                                      | Group23          |
| `RoughEstimateOfExecutionTime`                          | [ ] Implemented| N/A                                      | Group23          |
| `RoughEstimateStackUsage`                               | [ ] Deferred| 3db474b11a                               | Group20          |
| `Row`                                                   | [x] Done    | b43b860105                               | Group3           |
| `RptAccessEnum`                                         | [ ] Implemented| N/A                                      | Group23          |
| `RptComponent`                                          | [ ] Implemented| N/A                                      | Group23          |
| `RptContainer`                                          | [ ] Created | N/A                                      | Group29          |
| `RptEnablerImplTypeEnum`                                | [ ] Implemented| N/A                                      | Group23          |
| `RptExecutableEntity`                                   | [ ] Implemented| N/A                                      | Group23          |
| `RptExecutableEntityEvent`                              | [ ] Implemented| N/A                                      | Group23          |
| `RptExecutableEntityProperties`                         | [ ] Implemented| N/A                                      | Group23          |
| `RptExecutionContext`                                   | [ ] Implemented| N/A                                      | Group23          |
| `RptExecutionControlEnum`                               | [ ] Implemented| N/A                                      | Group23          |
| `RptHook`                                               | [ ] Created | N/A                                      | Group29          |
| `RptImplPolicy`                                         | [ ] Implemented| N/A                                      | Group23          |
| `RptPreparationEnum`                                    | [ ] Implemented| N/A                                      | Group23          |
| `RptProfile`                                            | [ ] Created | N/A                                      | Group29          |
| `RptServicePoint`                                       | [ ] Implemented| N/A                                      | Group23          |
| `RptServicePointEnum`                                   | [ ] Implemented| N/A                                      | Group23          |
| `RptSupportData`                                        | [ ] Implemented| N/A                                      | Group23          |
| `RptSwPrototypingAccess`                                | [ ] Implemented| N/A                                      | Group23          |
| `RteApiReturnValueProvisionEnum`                        | [ ] Implemented| N/A                                      | Group29          |
| `RteEventInCompositionSeparation`                       | [ ] Created | N/A                                      | Group31          |
| `RteEventInCompositionToOsTaskProxyMapping`             | [ ] Created | N/A                                      | Group31          |
| `RteEventInEcuInstanceRef`                              | [ ] Deferred| N/A                                      | Group12          |
| `RteEventInSystemSeparation`                            | [ ] Created | N/A                                      | Group31          |
| `RteEventInSystemToOsTaskProxyMapping`                  | [ ] Created | N/A                                      | Group31          |
| `RtePluginProps`                                        | [x] Done    | ec7fa0b5df                               | Group6           |
| `RtpTp`                                                 | [ ] Created | N/A                                      | Group32          |
| `RuleArguments`                                         | [ ] Implemented| N/A                                      | Group28          |
| `RuleBasedAxisCont`                                     | [ ] Implemented| N/A                                      | Group28          |
| `RuleBasedValueCont`                                    | [ ] Implemented| N/A                                      | Group28          |
| `RuleBasedValueSpecification`                           | [ ] Implemented| N/A                                      | Group28          |
| `RunMode`                                               | [ ] Deferred| N/A                                      | Group17          |
| `RunnableEntity`                                        | [ ] Implemented| N/A                                      | Group28          |
| `RunnableEntityArgument`                                | [x] Done    | 3857c2a435                               | Group2           |
| `RunnableEntityGroup`                                   | [ ] Implemented| N/A                                      | Group28          |
| `RuntimeAddressConfigurationEnum`                       | [ ] Deferred| c5bb322323                               | Group16          |
| `RuntimeError`                                          | [ ] Implemented| N/A                                      | Group23          |
| `RxAcceptContainedIPduEnum`                             | [ ] Created | N/A                                      | Group31          |
| `RxIdentifierRange`                                     | [ ] Implemented| N/A                                      | Group32          |
| `SOMEIPMessageTypeEnum`                                 | [x] Done    | b163080753                               | Group6           |
| `SOMEIPTransformationDescription`                       | [ ] Created | N/A                                      | Group34          |
| `SOMEIPTransformationISignalProps`                      | [x] Done    | 55ff2098b4                               | Group6           |
| `SOMEIPTransformationProps`                             | [ ] Created | N/A                                      | Group34          |
| `SaveConfigurationEntry`                                | [ ] Implemented| N/A                                      | Group32          |
| `ScaleConstrValidityEnum`                               | [x] Done    | 1bc8904eee                               | Group9           |
| `ScheduleTableEntry`                                    | [ ] Implemented| N/A                                      | Group31          |
| `Sd`                                                    | [ ] Implemented| N/A                                      | Group21          |
| `SdClientConfig`                                        | [x] Done    | 8e0c8857ad                               | Group7           |
| `SdServerConfig`                                        | [ ] Deferred| d7240be740                               | Group16          |
| `Sdf`                                                   | [ ] Implemented| N/A                                      | Group21          |
| `Sdg`                                                   | [ ] Implemented| N/A                                      | Group21          |
| `SdgAbstractForeignReference`                           | [ ] Created | N/A                                      | Group21          |
| `SdgAbstractPrimitiveAttribute`                         | [ ] Created | N/A                                      | Group21          |
| `SdgAggregationWithVariation`                           | [ ] Created | N/A                                      | Group21          |
| `SdgAttribute`                                          | [ ] Created | N/A                                      | Group21          |
| `SdgCaption`                                            | [ ] Implemented| N/A                                      | Group21          |
| `SdgClass`                                              | [ ] Created | N/A                                      | Group21          |
| `SdgContents`                                           | [ ] Implemented| N/A                                      | Group21          |
| `SdgDef`                                                | [ ] Created | N/A                                      | Group21          |
| `SdgElementWithGid`                                     | [ ] Created | N/A                                      | Group21          |
| `SdgForeignReference`                                   | [ ] Created | N/A                                      | Group21          |
| `SdgForeignReferenceWithVariation`                      | [ ] Created | N/A                                      | Group21          |
| `SdgPrimitiveAttribute`                                 | [ ] Created | N/A                                      | Group21          |
| `SdgPrimitiveAttributeWithVariation`                    | [ ] Created | N/A                                      | Group21          |
| `SdgReference`                                          | [ ] Created | N/A                                      | Group21          |
| `SdgTailoring`                                          | [ ] Created | N/A                                      | Group36          |
| `SecOcCryptoServiceMapping`                             | [ ] Deferred| N/A                                      | Group18          |
| `SectionInitializationPolicyType`                       | [x] Done    | 70ce06f500                               | Group22          |
| `SectionNamePrefix`                                     | [ ] Deferred| 0e26482636                               | Group20          |
| `SecureCommunicationAuthenticationProps`                | [ ] Implemented| N/A                                      | Group31          |
| `SecureCommunicationFreshnessProps`                     | [ ] Implemented| N/A                                      | Group31          |
| `SecureCommunicationProps`                              | [ ] Implemented| N/A                                      | Group31          |
| `SecureCommunicationPropsSet`                           | [ ] Implemented| N/A                                      | Group31          |
| `SecureOnBoardCommunicationNeeds`                       | [ ] Implemented| N/A                                      | Group29          |
| `SecuredIPdu`                                           | [ ] Deferred| 0a98655a06                               | Group15          |
| `SecuredPduHeaderEnum`                                  | [ ] Deferred| 3d5cb55dbe                               | Group15          |
| `SecurityEventAggregationFilter`                        | [ ] Created | N/A                                      | Group36          |
| `SecurityEventContextDataSourceEnum`                    | [ ] Created | N/A                                      | Group36          |
| `SecurityEventContextMapping`                           | [ ] Created | N/A                                      | Group36          |
| `SecurityEventContextMappingApplication`                | [ ] Created | N/A                                      | Group36          |
| `SecurityEventContextMappingBswModule`                  | [ ] Created | N/A                                      | Group36          |
| `SecurityEventContextMappingCommConnector`              | [ ] Created | N/A                                      | Group36          |
| `SecurityEventContextMappingFunctionalCluster`          | [ ] Created | N/A                                      | Group36          |
| `SecurityEventContextProps`                             | [ ] Created | N/A                                      | Group36          |
| `SecurityEventDefinition`                               | [ ] Created | N/A                                      | Group36          |
| `SecurityEventFilterChain`                              | [ ] Created | N/A                                      | Group36          |
| `SecurityEventOneEveryNFilter`                          | [ ] Created | N/A                                      | Group36          |
| `SecurityEventReportingModeEnum`                        | [ ] Created | N/A                                      | Group36          |
| `SecurityEventStateFilter`                              | [ ] Created | N/A                                      | Group36          |
| `SecurityEventThresholdFilter`                          | [ ] Created | N/A                                      | Group36          |
| `SegmentPosition`                                       | [ ] Deferred| 9546cf291b                               | Group15          |
| `SendIndicationEnum`                                    | [ ] Created | N/A                                      | Group34          |
| `SenderAnnotation`                                      | [ ] Created | N/A                                      | Group27          |
| `SenderComSpec`                                         | [ ] Implemented| N/A                                      | Group27          |
| `SenderRecArrayElementMapping`                          | [ ] Implemented| N/A                                      | Group31          |
| `SenderRecArrayTypeMapping`                             | [x] Done    | 757aea1d17                               | Group6           |
| `SenderRecCompositeTypeMapping`                         | [x] Done    | 757aea1d17                               | Group6           |
| `SenderRecRecordElementMapping`                         | [ ] Deferred| N/A                                      | Group17          |
| `SenderRecRecordTypeMapping`                            | [ ] Deferred| N/A                                      | Group17          |
| `SenderReceiverAnnotation`                              | [ ] Implemented| N/A                                      | Group27          |
| `SenderReceiverCompositeElementToSignalMapping`         | [ ] Created | N/A                                      | Group31          |
| `SenderReceiverInterface`                               | [x] Done    | e4e4770fb7                               | Group1           |
| `SenderReceiverToSignalGroupMapping`                    | [ ] Deferred| N/A                                      | Group17          |
| `SenderReceiverToSignalMapping`                         | [ ] Deferred| N/A                                      | Group17          |
| `SensorActuatorSwComponentType`                         | [ ] Implemented| N/A                                      | Group29          |
| `SeparateSignalPath`                                    | [ ] Created | N/A                                      | Group31          |
| `ServerArgumentImplPolicyEnum`                          | [ ] Implemented| N/A                                      | Group27          |
| `ServerCallPoint`                                       | [x] Done    | 774620a3b1                               | Group2           |
| `ServerComSpec`                                         | [ ] Implemented| N/A                                      | Group27          |
| `ServiceDependency`                                     | [ ] Implemented| N/A                                      | Group23          |
| `ServiceDiagnosticRelevanceEnum`                        | [ ] Deferred| 28746ce3cc                               | Group14          |
| `ServiceInstanceCollectionSet`                          | [ ] Created | N/A                                      | Group32          |
| `ServiceNeeds`                                          | [x] Done    | 5fd6271d70                               | Group4           |
| `ServiceProviderEnum`                                   | [ ] Implemented| N/A                                      | Group27          |
| `ServiceProxySwComponentType`                           | [x] Done    | 74e821ccb8                               | Group11          |
| `ServiceSwComponentType`                                | [ ] Implemented| N/A                                      | Group29          |
| `SeverityEnum`                                          | [ ] Created | N/A                                      | Group36          |
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
| `SignalFanEnum`                                         | [ ] Implemented| N/A                                      | Group27          |
| `SignalServiceTranslationControlEnum`                   | [ ] Implemented| N/A                                      | Group34          |
| `SignalServiceTranslationElementProps`                  | [ ] Deferred| 29d09fc625                               | Group14          |
| `SignalServiceTranslationEventProps`                    | [ ] Implemented| N/A                                      | Group34          |
| `SignalServiceTranslationProps`                         | [ ] Implemented| N/A                                      | Group34          |
| `SignalServiceTranslationPropsSet`                      | [ ] Implemented| N/A                                      | Group34          |
| `SimulatedExecutionTime`                                | [ ] Implemented| N/A                                      | Group23          |
| `SingleLanguageLongName`                                | [x] Done    | 8aaa2657f3                               | Group3           |
| `SingleLanguageReferrable`                              | [x] Done    | a5910c1bf5                               | Group3           |
| `SingleLanguageUnitNames`                               | [x] Done    | d42795c169                               | Group8           |
| `SlOverviewParagraph`                                   | [x] Done    | 951209dbab                               | Group8           |
| `SlParagraph`                                           | [x] Done    | b7748b3e50                               | Group3           |
| `SoAdConfig`                                            | [ ] Implemented| N/A                                      | Group32          |
| `SoAdRoutingGroup`                                      | [ ] Deferred| 89363ebe2b                               | Group20          |
| `SoConIPduIdentifier`                                   | [ ] Created | N/A                                      | Group32          |
| `SocketAddress`                                         | [ ] Implemented| N/A                                      | Group32          |
| `SocketConnectionBundle`                                | [ ] Deferred| 4b7c8dc79c                               | Group16          |
| `SocketConnectionIpduIdentifier`                        | [ ] Deferred| 4b7c8dc79c                               | Group16          |
| `SocketConnectionIpduIdentifierSet`                     | [ ] Created | N/A                                      | Group32          |
| `SoftwareContext`                                       | [ ] Deferred| 23884479e9                               | Group20          |
| `SomeipProtocolRule`                                    | [ ] Deferred| c18aa8d400                               | Group20          |
| `SomeipSdClientEventGroupTimingConfig`                  | [ ] Implemented| N/A                                      | Group32          |
| `SomeipSdRule`                                          | [ ] Deferred| 17b563a730                               | Group20          |
| `SomeipSdServerEventGroupTimingConfig`                  | [ ] Implemented| N/A                                      | Group32          |
| `SomeipSdServerServiceInstanceConfig`                   | [ ] Created | N/A                                      | Group32          |
| `SomeipTpChannel`                                       | [ ] Created | N/A                                      | Group33          |
| `SomeipTpConfig`                                        | [ ] Created | N/A                                      | Group33          |
| `SomeipTpConnection`                                    | [ ] Created | N/A                                      | Group33          |
| `SpecElementReference`                                  | [ ] Created | N/A                                      | Group36          |
| `SpecElementScope`                                      | [ ] Created | N/A                                      | Group36          |
| `SpecificationDocumentScope`                            | [ ] Created | N/A                                      | Group36          |
| `SpecificationScope`                                    | [ ] Created | N/A                                      | Group36          |
| `SporadicEventTriggering`                               | [ ] Implemented| N/A                                      | Group35          |
| `StackUsage`                                            | [ ] Deferred| 9ce364e249                               | Group20          |
| `StandardNameEnum`                                      | [x] Done    | 9a9ffdae8d                               | Group1           |
| `StateDependentFirewall`                                | [ ] Implemented| N/A                                      | Group33          |
| `StaticPart`                                            | [x] Done    | 206cf29517                               | Group5           |
| `StaticSocketConnection`                                | [ ] Implemented| N/A                                      | Group32          |
| `Std`                                                   | [x] Done    | c53a240809                               | Group3           |
| `StorageConditionStatusEnum`                            | [ ] Implemented| N/A                                      | Group29          |
| `StreamFilterIEEE1722Tp`                                | [ ] Created | N/A                                      | Group30          |
| `StreamFilterIpv4Address`                               | [ ] Created | N/A                                      | Group30          |
| `StreamFilterIpv6Address`                               | [ ] Created | N/A                                      | Group30          |
| `StreamFilterMACAddress`                                | [ ] Created | N/A                                      | Group30          |
| `StreamFilterPortRange`                                 | [ ] Created | N/A                                      | Group30          |
| `StreamFilterRuleDataLinkLayer`                         | [ ] Created | N/A                                      | Group30          |
| `StreamFilterRuleIpTp`                                  | [ ] Created | N/A                                      | Group30          |
| `String`                                                | [ ] Implemented| N/A                                      | Group21          |
| `StructuredReq`                                         | [x] Done    | d311fc7ce0                               | Group1           |
| `SubElementMapping`                                     | [x] Done    | 5eadca7853                               | Group1           |
| `SubElementRef`                                         | [x] Done    | 47b3052188                               | Group1           |
| `Superscript`                                           | [ ] Implemented| N/A                                      | Group21          |
| `SupervisedEntityCheckpointNeeds`                       | [x] Done    | 67640c8035                               | Group4           |
| `SupervisedEntityNeeds`                                 | [ ] Implemented| N/A                                      | Group23          |
| `SupportBufferLockingEnum`                              | [x] Done    | 7c67628122                               | Group2           |
| `SwAddrMethod`                                          | [x] Done    | 70ce06f500                               | Group22          |
| `SwAxisCont`                                            | [ ] Created | N/A                                      | Group28          |
| `SwAxisGeneric`                                         | [ ] Implemented| N/A                                      | Group28          |
| `SwAxisGrouped`                                         | [x] Done    | 12a2e0170b                               | Group3           |
| `SwAxisIndividual`                                      | [x] Done    | 842e1e4227                               | Group3           |
| `SwAxisType`                                            | [ ] Created | N/A                                      | Group28          |
| `SwBaseType`                                            | [ ] Implemented| N/A                                      | Group28          |
| `SwBitRepresentation`                                   | [ ] Implemented| N/A                                      | Group28          |
| `SwCalibrationAccessEnum`                               | [ ] Implemented| N/A                                      | Group28          |
| `SwCalprmAxis`                                          | [ ] Implemented| N/A                                      | Group28          |
| `SwCalprmAxisSet`                                       | [x] Done    | 9209b83ea0                               | Group3           |
| `SwCalprmAxisTypeProps`                                 | [ ] Implemented| N/A                                      | Group28          |
| `SwCalprmRefProxy`                                      | [ ] Implemented| N/A                                      | Group28          |
| `SwComponentDocumentation`                              | [ ] Implemented| N/A                                      | Group29          |
| `SwComponentPrototype`                                  | [x] Done    | ff993a74c8                               | Group1           |
| `SwComponentPrototypeAssignment`                        | [x] Done    | 88070878ea                               | Group5           |
| `SwComponentType`                                       | [ ] Implemented| N/A                                      | Group27          |
| `SwConnector`                                           | [ ] Implemented| N/A                                      | Group27          |
| `SwDataDefProps`                                        | [ ] Implemented| N/A                                      | Group28          |
| `SwDataDependency`                                      | [ ] Implemented| N/A                                      | Group28          |
| `SwDataDependencyArgs`                                  | [ ] Implemented| N/A                                      | Group28          |
| `SwGenericAxisParam`                                    | [ ] Implemented| N/A                                      | Group28          |
| `SwGenericAxisParamType`                                | [x] Done    | 1eacd1a7a7                               | Group3           |
| `SwImplPolicyEnum`                                      | [x] Done    | d6945a4c8a                               | Group9           |
| `SwPointerTargetProps`                                  | [x] Done    | c6247eb0db                               | Group22          |
| `SwRecordLayout`                                        | [x] Done    | f8149880de                               | Group3           |
| `SwRecordLayoutGroup`                                   | [x] Done    | 2acaf7a45f                               | Group3           |
| `SwRecordLayoutGroupContent`                            | [x] Done    | 0f19d490d3                               | Group3           |
| `SwRecordLayoutV`                                       | [x] Done    | 9c0c3f85f8                               | Group3           |
| `SwServiceArg`                                          | [x] Done    | 596ec6e31e                               | Group22          |
| `SwServiceImplPolicyEnum`                               | [x] Done    | 1a5b05b196                               | Group22          |
| `SwSystemconst`                                         | [x] Done    | 984387dd0c                               | Group9           |
| `SwSystemconstDependentFormula`                         | [x] Done    | f05e21d49e                               | Group8           |
| `SwSystemconstValue`                                    | [x] Done    | 5333bec027                               | Group8           |
| `SwSystemconstantValueSet`                              | [ ] Implemented| N/A                                      | Group36          |
| `SwTextProps`                                           | [ ] Implemented| N/A                                      | Group28          |
| `SwValueCont`                                           | [x] Done    | 6db47de6aa                               | Group3           |
| `SwValues`                                              | [ ] Implemented| N/A                                      | Group28          |
| `SwVariableRefProxy`                                    | [ ] Implemented| N/A                                      | Group28          |
| `SwcBswMapping`                                         | [x] Done    | 58b2c68a57                               | Group1           |
| `SwcBswRunnableMapping`                                 | [ ] Deferred| c52cece662                               | Group13          |
| `SwcBswSynchronizedModeGroupPrototype`                  | [ ] Deferred| 659c2bf174                               | Group13          |
| `SwcBswSynchronizedTrigger`                             | [ ] Deferred| 6b4b9d6d10                               | Group13          |
| `SwcExclusiveAreaPolicy`                                | [ ] Implemented| N/A                                      | Group29          |
| `SwcImplementation`                                     | [x] Done    | 6eae95f556                               | Group10          |
| `SwcInternalBehavior`                                   | [x] Done    | 4043dc013a                               | Group2           |
| `SwcModeManagerErrorEvent`                              | [ ] Created | N/A                                      | Group29          |
| `SwcModeSwitchEvent`                                    | [ ] Implemented| N/A                                      | Group28          |
| `SwcServiceDependency`                                  | [ ] Implemented| N/A                                      | Group29          |
| `SwcSupportedFeature`                                   | [x] Done    | 7c67628122                               | Group2           |
| `SwcTiming`                                             | [ ] Implemented| N/A                                      | Group35          |
| `SwcToApplicationPartitionMapping`                      | [ ] Created | N/A                                      | Group30          |
| `SwcToEcuMapping`                                       | [ ] Deferred| N/A                                      | Group18          |
| `SwcToImplMapping`                                      | [ ] Deferred| N/A                                      | Group18          |
| `SwcToSwcOperationArguments`                            | [ ] Created | N/A                                      | Group31          |
| `SwcToSwcOperationArgumentsDirectionEnum`               | [ ] Created | N/A                                      | Group31          |
| `SwcToSwcSignal`                                        | [ ] Created | N/A                                      | Group31          |
| `SwitchAsynchronousTrafficShaperGroupEntry`             | [ ] Created | N/A                                      | Group30          |
| `SwitchFlowMeteringEntry`                               | [ ] Created | N/A                                      | Group30          |
| `SwitchStreamFilterActionDestPortModification`          | [ ] Created | N/A                                      | Group30          |
| `SwitchStreamFilterActionPortModificationEnum`          | [ ] Created | N/A                                      | Group30          |
| `SwitchStreamFilterEntry`                               | [ ] Created | N/A                                      | Group30          |
| `SwitchStreamFilterRule`                                | [ ] Created | N/A                                      | Group30          |
| `SwitchStreamGateEntry`                                 | [ ] Created | N/A                                      | Group30          |
| `SwitchStreamIdentification`                            | [ ] Created | N/A                                      | Group30          |
| `SymbolProps`                                           | [x] Done    | 2d21a9108b                               | Group2           |
| `SymbolString`                                          | [ ] Implemented| N/A                                      | Group21          |
| `SymbolicNameProps`                                     | [ ] Implemented| N/A                                      | Group29          |
| `SyncTimeBaseMgrUserNeeds`                              | [x] Done    | 609f148a93                               | Group4           |
| `SynchronizationPointConstraint`                        | [ ] Implemented| N/A                                      | Group35          |
| `SynchronizationTimingConstraint`                       | [x] Done    | e305e80e2a                               | Group8           |
| `SynchronizationTypeEnum`                               | [ ] Implemented| N/A                                      | Group35          |
| `SynchronousServerCallPoint`                            | [x] Done    | 9182987d97                               | Group2           |
| `System`                                                | [x] Done    | ccfb528daf                               | Group5           |
| `SystemMapping`                                         | [ ] Implemented| N/A                                      | Group30          |
| `SystemSignal`                                          | [ ] Deferred| 7c5d9e9d81                               | Group15          |
| `SystemSignalGroup`                                     | [ ] Implemented| N/A                                      | Group31          |
| `SystemSignalGroupToCommunicationResourceMapping`       | [ ] Created | N/A                                      | Group31          |
| `SystemSignalToCommunicationResourceMapping`            | [ ] Created | N/A                                      | Group31          |
| `SystemTiming`                                          | [ ] Created | N/A                                      | Group35          |
| `TDCpSoftwareClusterMapping`                            | [ ] Created | N/A                                      | Group35          |
| `TDCpSoftwareClusterMappingSet`                         | [ ] Created | N/A                                      | Group35          |
| `TDCpSoftwareClusterResourceMapping`                    | [ ] Created | N/A                                      | Group35          |
| `TDEventBswInternalBehavior`                            | [ ] Implemented| N/A                                      | Group35          |
| `TDEventBswInternalBehaviorTypeEnum`                    | [ ] Implemented| N/A                                      | Group35          |
| `TDEventBswModeDeclaration`                             | [ ] Implemented| N/A                                      | Group35          |
| `TDEventBswModeDeclarationTypeEnum`                     | [ ] Implemented| N/A                                      | Group35          |
| `TDEventBswModule`                                      | [ ] Implemented| N/A                                      | Group35          |
| `TDEventBswModuleTypeEnum`                              | [ ] Implemented| N/A                                      | Group35          |
| `TDEventCom`                                            | [ ] Implemented| N/A                                      | Group35          |
| `TDEventComplex`                                        | [ ] Implemented| N/A                                      | Group35          |
| `TDEventCycleStart`                                     | [ ] Implemented| N/A                                      | Group35          |
| `TDEventFrClusterCycleStart`                            | [ ] Implemented| N/A                                      | Group35          |
| `TDEventFrame`                                          | [ ] Implemented| N/A                                      | Group35          |
| `TDEventFrameEthernet`                                  | [ ] Implemented| N/A                                      | Group35          |
| `TDEventFrameEthernetTypeEnum`                          | [ ] Implemented| N/A                                      | Group35          |
| `TDEventFrameTypeEnum`                                  | [ ] Implemented| N/A                                      | Group35          |
| `TDEventIPdu`                                           | [ ] Implemented| N/A                                      | Group35          |
| `TDEventIPduTypeEnum`                                   | [ ] Implemented| N/A                                      | Group35          |
| `TDEventISignal`                                        | [ ] Implemented| N/A                                      | Group35          |
| `TDEventISignalTypeEnum`                                | [ ] Implemented| N/A                                      | Group35          |
| `TDEventModeDeclaration`                                | [ ] Implemented| N/A                                      | Group35          |
| `TDEventModeDeclarationTypeEnum`                        | [ ] Implemented| N/A                                      | Group35          |
| `TDEventOccurrenceExpression`                           | [ ] Implemented| N/A                                      | Group35          |
| `TDEventOccurrenceExpressionFormula`                    | [ ] Implemented| N/A                                      | Group35          |
| `TDEventOperation`                                      | [ ] Implemented| N/A                                      | Group35          |
| `TDEventOperationTypeEnum`                              | [ ] Implemented| N/A                                      | Group35          |
| `TDEventSLLETPort`                                      | [ ] Implemented| N/A                                      | Group35          |
| `TDEventSwc`                                            | [ ] Implemented| N/A                                      | Group35          |
| `TDEventSwcInternalBehavior`                            | [ ] Implemented| N/A                                      | Group35          |
| `TDEventSwcInternalBehaviorReference`                   | [ ] Implemented| N/A                                      | Group35          |
| `TDEventSwcInternalBehaviorTypeEnum`                    | [ ] Implemented| N/A                                      | Group35          |
| `TDEventTTCanCycleStart`                                | [ ] Implemented| N/A                                      | Group35          |
| `TDEventTrigger`                                        | [ ] Implemented| N/A                                      | Group35          |
| `TDEventTriggerTypeEnum`                                | [ ] Implemented| N/A                                      | Group35          |
| `TDEventVariableDataPrototype`                          | [ ] Implemented| N/A                                      | Group35          |
| `TDEventVariableDataPrototypeTypeEnum`                  | [ ] Implemented| N/A                                      | Group35          |
| `TDEventVfb`                                            | [x] Done    | 18eb225f40                               | Group8           |
| `TDEventVfbPort`                                        | [ ] Implemented| N/A                                      | Group35          |
| `TDEventVfbReference`                                   | [ ] Implemented| N/A                                      | Group35          |
| `TDHeaderIdRange`                                       | [ ] Implemented| N/A                                      | Group35          |
| `Table`                                                 | [x] Done    | e347fbbfa2                               | Group3           |
| `TableSeparatorString`                                  | [x] Done    | 211031ea0f                               | Group3           |
| `TagWithOptionalValue`                                  | [ ] Implemented| N/A                                      | Group21          |
| `TargetIPduRef`                                         | [ ] Deferred| N/A                                      | Group17          |
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
| `TextTableValuePair`                                    | [ ] Implemented| N/A                                      | Group27          |
| `TextValueSpecification`                                | [x] Done    | 81588f449e                               | Group9           |
| `TextualCondition`                                      | [ ] Created | N/A                                      | Group36          |
| `Tgroup`                                                | [x] Done    | 278d4674f3                               | Group3           |
| `TimeRangeType`                                         | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `TimeRangeTypeTolerance`                                | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `TimeSyncClientConfiguration`                           | [x] Done    | a032fa05dc                               | Group6           |
| `TimeSyncServerConfiguration`                           | [ ] Deferred| b1e4750b14                               | Group16          |
| `TimeSyncTechnologyEnum`                                | [ ] Implemented| N/A                                      | Group32          |
| `TimeSynchronization`                                   | [ ] Deferred| b1e4750b14                               | Group16          |
| `TimeValue`                                             | [ ] Implemented| N/A                                      | Group27          |
| `TimeValueValueVariationPoint`                          | [x] Done    | d5c96fd954                               | Group8           |
| `TimingCondition`                                       | [ ] Implemented| N/A                                      | Group35          |
| `TimingConditionFormula`                                | [ ] Implemented| N/A                                      | Group35          |
| `TimingDescriptionEventChain`                           | [x] Done    | ea1a75e5b9                               | Group8           |
| `TimingEvent`                                           | [ ] Implemented| N/A                                      | Group28          |
| `TimingExtensionResource`                               | [ ] Implemented| N/A                                      | Group35          |
| `TimingModeInstance`                                    | [ ] Implemented| N/A                                      | Group35          |
| `TlsCryptoCipherSuite`                                  | [x] Done    | 67315ec0a9                               | Group6           |
| `TlsCryptoCipherSuiteProps`                             | [x] Done    | 648b40acaf                               | Group6           |
| `TlsCryptoServiceMapping`                               | [x] Done    | 67315ec0a9                               | Group6           |
| `TlsPskIdentity`                                        | [x] Done    | 16c2791a2b                               | Group6           |
| `TlsVersionEnum`                                        | [x] Done    | d969a0ddc1                               | Group6           |
| `TlvDataIdDefinition`                                   | [x] Done    | 27ea0743dc                               | Group6           |
| `TlvDataIdDefinitionSet`                                | [x] Done    | f0c9473162                               | Group6           |
| `Topic1`                                                | [x] Done    | 0d13ccd1bc                               | Group22          |
| `TopicContent`                                          | [x] Done    | 6d7e325736                               | Group3           |
| `TopicContentOrMsrQuery`                                | [x] Done    | 460218682e                               | Group9           |
| `TopicOrMsrQuery`                                       | [x] Done    | 0d13ccd1bc                               | Group22          |
| `TpAddress`                                             | [ ] Deferred| N/A                                      | Group18          |
| `TpConfig`                                              | [ ] Implemented| N/A                                      | Group33          |
| `TpConnection`                                          | [ ] Implemented| N/A                                      | Group33          |
| `TpConnectionIdent`                                     | [ ] Implemented| N/A                                      | Group23          |
| `TpPort`                                                | [ ] Deferred| b1e4750b14                               | Group16          |
| `Traceable`                                             | [ ] Implemented| N/A                                      | Group21          |
| `TraceableTable`                                        | [x] Done    | fa79c73df5                               | Group3           |
| `TraceableText`                                         | [x] Done    | 9e80479bda                               | Group1           |
| `TracedFailure`                                         | [ ] Implemented| N/A                                      | Group23          |
| `TransferPropertyEnum`                                  | [ ] Deferred| e6baac031c                               | Group15          |
| `TransformationComSpecProps`                            | [ ] Implemented| N/A                                      | Group27          |
| `TransformationDescription`                             | [ ] Implemented| N/A                                      | Group28          |
| `TransformationISignalProps`                            | [x] Done    | 757aea1d17                               | Group6           |
| `TransformationProps`                                   | [ ] Created | N/A                                      | Group34          |
| `TransformationPropsSet`                                | [ ] Created | N/A                                      | Group34          |
| `TransformationTechnology`                              | [ ] Implemented| N/A                                      | Group27          |
| `TransformerClassEnum`                                  | [ ] Implemented| N/A                                      | Group28          |
| `TransformerHardErrorEvent`                             | [ ] Created | N/A                                      | Group28          |
| `TransmissionAcknowledgementRequest`                    | [ ] Implemented| N/A                                      | Group27          |
| `TransmissionComSpecProps`                              | [ ] Implemented| N/A                                      | Group27          |
| `TransmissionModeCondition`                             | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `TransmissionModeDeclaration`                           | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `TransmissionModeDefinitionEnum`                        | [ ] Implemented| N/A                                      | Group27          |
| `TransmissionModeTiming`                                | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `TransportLayerRule`                                    | [ ] Deferred| cb197c6b8b                               | Group20          |
| `TransportProtocolConfiguration`                        | [x] Done    | 0014960828                               | Group6           |
| `Trigger`                                               | [x] Done    | 131473204c                               | Group1           |
| `TriggerIPduSendCondition`                              | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `TriggerInAtomicSwcInstanceRef`                         | [x] Done    | 839264b3a6                               | Group11          |
| `TriggerInterface`                                      | [x] Done    | cf9c6ac4cc                               | Group1           |
| `TriggerInterfaceMapping`                               | [x] Done    | 49f19e8feb                               | Group1           |
| `TriggerMapping`                                        | [x] Done    | 905c48d323                               | Group1           |
| `TriggerMode`                                           | [ ] Deferred| cc609f42a3                               | Group15          |
| `TriggerPortAnnotation`                                 | [ ] Implemented| N/A                                      | Group27          |
| `TriggerToSignalMapping`                                | [ ] Created | N/A                                      | Group31          |
| `Tt`                                                    | [ ] Implemented| N/A                                      | Group21          |
| `TtcanAbsolutelyScheduledTiming`                        | [ ] Implemented| N/A                                      | Group32          |
| `TtcanCluster`                                          | [ ] Created | N/A                                      | Group29          |
| `TtcanCommunicationConnector`                           | [ ] Created | N/A                                      | Group29          |
| `TtcanCommunicationController`                          | [ ] Created | N/A                                      | Group29          |
| `TtcanPhysicalChannel`                                  | [ ] Created | N/A                                      | Group29          |
| `TtcanTriggerType`                                      | [ ] Implemented| N/A                                      | Group32          |
| `UdpChecksumCalculationEnum`                            | [ ] Implemented| N/A                                      | Group32          |
| `UdpNmCluster`                                          | [ ] Deferred| N/A                                      | Group18          |
| `UdpNmClusterCoupling`                                  | [ ] Deferred| N/A                                      | Group18          |
| `UdpNmEcu`                                              | [x] Done    | 9c8e10b37f                               | Group6           |
| `UdpNmNode`                                             | [ ] Deferred| N/A                                      | Group18          |
| `UdpProps`                                              | [x] Done    | ecb15e901f                               | Group5           |
| `UdpRule`                                               | [x] Deferred| 29cbfb7bbd                               | Group20          |
| `UdpTp`                                                 | [ ] Deferred| N/A                                      | Group16          |
| `UnassignFrameId`                                       | [ ] Implemented| N/A                                      | Group31          |
| `Unit`                                                  | [ ] Implemented| N/A                                      | Group28          |
| `UnitGroup`                                             | [x] Done    | e7fdb07f2b                               | Group9           |
| `UnlimitedIntegerValueVariationPoint`                   | [x] Done    | d5c96fd954                               | Group8           |
| `UriString`                                             | [ ] Implemented| N/A                                      | Group21          |
| `Url`                                                   | [x] Done    | 4b96ab8d89                               | Group3           |
| `UserDefinedCluster`                                    | [ ] Created | N/A                                      | Group30          |
| `UserDefinedCommunicationConnector`                     | [ ] Created | N/A                                      | Group30          |
| `UserDefinedCommunicationController`                    | [ ] Created | N/A                                      | Group30          |
| `UserDefinedEthernetFrame`                              | [ ] Created | N/A                                      | Group33          |
| `UserDefinedGlobalTimeMaster`                           | [ ] Created | N/A                                      | Group34          |
| `UserDefinedGlobalTimeSlave`                            | [ ] Created | N/A                                      | Group34          |
| `UserDefinedIPdu`                                       | [ ] Deferred| N/A                                      | Group15          |
| `UserDefinedPdu`                                        | [ ] Deferred| N/A                                      | Group15          |
| `UserDefinedPhysicalChannel`                            | [ ] Created | N/A                                      | Group30          |
| `UserDefinedTransformationComSpecProps`                 | [x] Done    | 4a7d82ffc7                               | Group5           |
| `UserDefinedTransformationDescription`                  | [ ] Created | N/A                                      | Group34          |
| `UserDefinedTransformationISignalProps`                 | [x] Done    | 301182769c                               | Group6           |
| `UserDefinedTransformationProps`                        | [ ] Created | N/A                                      | Group34          |
| `V2xDataManagerNeeds`                                   | [x] Done    | e02dc71234                               | Group5           |
| `V2xFacUserNeeds`                                       | [x] Done    | 029aa70113                               | Group5           |
| `V2xMUserNeeds`                                         | [x] Done    | d45912e177                               | Group5           |
| `ValignEnum`                                            | [x] Done    | 52d3272bbb                               | Group3           |
| `ValueGroup`                                            | [ ] Implemented| N/A                                      | Group28          |
| `ValueList`                                             | [ ] Implemented| N/A                                      | Group28          |
| `ValueRestrictionWithSeverity`                          | [ ] Created | N/A                                      | Group36          |
| `ValueSpecification`                                    | [ ] Implemented| N/A                                      | Group28          |
| `VariableAccess`                                        | [x] Done    | 12e743cc9b                               | Group12          |
| `VariableAccessInEcuInstanceRef`                        | [ ] Deferred| N/A                                      | Group12          |
| `VariableAccessScopeEnum`                               | [x] Done    | 12e743cc9b                               | Group12          |
| `VariableAndParameterInterfaceMapping`                  | [x] Done    | 0e87cc4bb9                               | Group11          |
| `VariableDataPrototype`                                 | [x] Done    | d3b5d680e2                               | Group2           |
| `VariableDataPrototypeInSystemInstanceRef`              | [x] Done    | 1b3d673dac                               | Group7           |
| `VariableInAtomicSWCTypeInstanceRef`                    | [x] Done    | c8ac9ef7de                               | Group2           |
| `VariableInAtomicSwcInstanceRef`                        | [x] Done    | 0369005450                               | Group2           |
| `VariationPoint`                                        | [x] Done    | d4fce975d6                               | Group8           |
| `VariationPointProxy`                                   | [ ] Implemented| N/A                                      | Group29          |
| `VariationRestrictionWithSeverity`                      | [ ] Created | N/A                                      | Group36          |
| `VendorSpecificServiceNeeds`                            | [x] Done    | a25f9a7718                               | Group5           |
| `VerbatimString`                                        | [ ] Implemented| N/A                                      | Group21          |
| `VerbatimStringPlain`                                   | [ ] Implemented| N/A                                      | Group21          |
| `VerificationStatusIndicationModeEnum`                  | [ ] Implemented| N/A                                      | Group29          |
| `VfbTiming`                                             | [ ] Created | N/A                                      | Group35          |
| `ViewMap`                                               | [ ] Deferred| b48c08bba2                               | Group22          |
| `ViewMapSet`                                            | [ ] Deferred| f6dc7bb594                               | Group22          |
| `ViewTokens`                                            | [x] Done    | 82c86af789                               | Group3           |
| `VlanConfig`                                            | [ ] Deferred| b1e4750b14                               | Group16          |
| `VlanMembership`                                        | [x] Done    | ed6ed2a65f                               | Group6           |
| `WaitPoint`                                             | [ ] Implemented| N/A                                      | Group28          |
| `WarningIndicatorRequestedBitNeeds`                     | [x] Done    | 1cd8edd8fd                               | Group5           |
| `WhitespaceControlled`                                  | [x] Done    | a78d444afb                               | Group8           |
| `WorstCaseHeapUsage`                                    | [x] Done    | a55d2092d0                               | Group22          |
| `WorstCaseStackUsage`                                   | [ ] Deferred| a0cbd41d08                               | Group20          |
| `Xdoc`                                                  | [x] Done    | 294c8aae2c                               | Group3           |
| `Xfile`                                                 | [x] Done    | 7038ce5574                               | Group3           |
| `XmlSpaceEnum`                                          | [x] Done    | ec544e7988                               | Group8           |
| `Xref`                                                  | [x] Done    | db2b4fe059                               | Group3           |
| `XrefTarget`                                            | [x] Done    | 8c9df6638a                               | Group3           |
