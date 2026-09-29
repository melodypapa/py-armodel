# All Sync Todo Classes (Consolidated)

Generated from all Group files in `docs/plan/sync-todo/` — Classes ordered by name with status and commit ID.

**Status legend:** `[x] Done` = 9-step sync complete AND `# Spec verified:`/`# XSD verified:` stamped in src · `[x]`/`[ ] Deferred` = sync complete (Steps 1–8 green) but the stamp is **deferred to a batch 9b user confirmation** · `[ ] Pending` = sync not yet complete. (Deferred set audited 2026-09-27 against the src stamps.)

## Summary

**1921 classes total**

| Status | Classes | Percent |
| --- | --- | --- |
| [x] Done | 501 | 26.1% |
| [x] Deferred | 11 | 0.6% |
| [x] Retired | 0 | 0.0% |
| [ ] Deferred | 171 | 8.9% |
| [ ] Pending | 1238 | 64.4% |

| Class Name                                              | Status      | Commit ID                                | Groups           |
| ------------------------------------------------------- | ------------| ---------------------------------------- | ---------------- |
| `ARElement`                                             | [x] Done    | 61c85fa794                               | Group1           |
| `ARList`                                                | [x] Done    | 2151ca0302                               | Group9           |
| `ARObject`                                              | [x] Done    | 78ae363c75                               | Group1           |
| `ARPackage`                                             | [x] Done    | 360648178f                               | Group1           |
| `AUTOSAR`                                               | [x] Done    | 74f4d3c80a                               | Group1           |
| `AbsoluteTolerance`                                     | [ ] Pending | N/A                                      | Group31          |
| `AbstractAccessPoint`                                   | [ ] Pending | N/A                                      | Group22          |
| `AbstractCanCluster`                                    | [ ] Pending | N/A                                      | Group29          |
| `AbstractCanCommunicationConnector`                     | [ ] Pending | N/A                                      | Group29          |
| `AbstractCanCommunicationController`                    | [ ] Pending | N/A                                      | Group29          |
| `AbstractCanCommunicationControllerAttributes`          | [ ] Pending | N/A                                      | Group29          |
| `AbstractCanPhysicalChannel`                            | [ ] Pending | N/A                                      | Group29          |
| `AbstractClassTailoring`                                | [ ] Pending | N/A                                      | Group36          |
| `AbstractCondition`                                     | [ ] Pending | N/A                                      | Group36          |
| `AbstractDoIpLogicAddressProps`                         | [x] Done    | 64d125ffae                               | Group7           |
| `AbstractEnumerationValueVariationPoint`                | [x] Done    | 0518a7bca2                               | Group8           |
| `AbstractEthernetFrame`                                 | [x] Done    | cba67817b3                               | Group6           |
| `AbstractEvent`                                         | [ ] Pending | N/A                                      | Group28          |
| `AbstractGlobalTimeDomainProps`                         | [ ] Pending | N/A                                      | Group34          |
| `AbstractImplementationDataType`                        | [x] Done    | 9b5379d3e3                               | Group1           |
| `AbstractImplementationDataTypeElement`                 | [x] Done    | cabd5469e9                               | Group1           |
| `AbstractMultiplicityRestriction`                       | [ ] Pending | N/A                                      | Group36          |
| `AbstractNumericalVariationPoint`                       | [x] Done    | d5c96fd954                               | Group8           |
| `AbstractProvidedPortPrototype`                         | [ ] Deferred| fb7a835f90                               | Group11          |
| `AbstractRequiredPortPrototype`                         | [ ] Deferred| fb7a835f90                               | Group11          |
| `AbstractRuleBasedValueSpecification`                   | [ ] Pending | N/A                                      | Group28          |
| `AbstractSecurityEventFilter`                           | [ ] Pending | N/A                                      | Group36          |
| `AbstractServiceInstance`                               | [ ] Pending | N/A                                      | Group32          |
| `AbstractValueRestriction`                              | [ ] Pending | N/A                                      | Group21          |
| `AbstractVariationRestriction`                          | [ ] Pending | N/A                                      | Group21          |
| `AccessCount`                                           | [ ] Pending | N/A                                      | Group22          |
| `AccessCountSet`                                        | [ ] Pending | N/A                                      | Group22          |
| `AclObjectSet`                                          | [ ] Pending | N/A                                      | Group22          |
| `AclOperation`                                          | [ ] Pending | N/A                                      | Group22          |
| `AclPermission`                                         | [ ] Pending | N/A                                      | Group22          |
| `AclRole`                                               | [ ] Pending | N/A                                      | Group22          |
| `AclScopeEnum`                                          | [ ] Pending | N/A                                      | Group22          |
| `AdditionalBindingTimeEnum`                             | [ ] Pending | N/A                                      | Group29          |
| `AdminData`                                             | [ ] Pending | N/A                                      | Group21          |
| `AgeConstraint`                                         | [ ] Pending | N/A                                      | Group35          |
| `AggregationCondition`                                  | [ ] Pending | N/A                                      | Group36          |
| `AggregationTailoring`                                  | [ ] Pending | N/A                                      | Group36          |
| `AliasNameAssignment`                                   | [ ] Pending | N/A                                      | Group23          |
| `AliasNameSet`                                          | [ ] Pending | N/A                                      | Group23          |
| `AlignEnum`                                             | [x] Done    | fa74a474a5                               | Group3           |
| `AlignmentType`                                         | [ ] Pending | N/A                                      | Group22          |
| `AnalyzedExecutionTime`                                 | [ ] Pending | N/A                                      | Group23          |
| `Annotation`                                            | [ ] Pending | N/A                                      | Group21          |
| `AnyInstanceRef`                                        | [ ] Pending | N/A                                      | Group22          |
| `ApiPrincipleEnum`                                      | [x] Done    | c6d2e83f74                               | Group10          |
| `AppOsTaskProxyToEcuTaskProxyMapping`                   | [ ] Pending | N/A                                      | Group18          |
| `ApplicationArrayDataType`                              | [ ] Pending | N/A                                      | Group28          |
| `ApplicationArrayElement`                               | [ ] Pending | N/A                                      | Group28          |
| `ApplicationCompositeDataType`                          | [x] Done    | de9d3fe0a4                               | Group2           |
| `ApplicationCompositeDataTypeSubElementRef`             | [ ] Pending | N/A                                      | Group27          |
| `ApplicationCompositeElementDataPrototype`              | [x] Done    | 031d5c7848                               | Group2           |
| `ApplicationCompositeElementInPortInterfaceInstanceRef` | [x] Done    | 399b647757                               | Group2           |
| `ApplicationDataType`                                   | [x] Done    | b8d0878d98                               | Group2           |
| `ApplicationDeferredDataType`                           | [x] Done    | abdfbf1d96                               | Group1           |
| `ApplicationEndpoint`                                   | [ ] Pending | N/A                                      | Group32          |
| `ApplicationEntry`                                      | [ ] Deferred| N/A                                      | Group17          |
| `ApplicationError`                                      | [ ] Pending | N/A                                      | Group27          |
| `ApplicationInterface`                                  | [ ] Pending | N/A                                      | Group36          |
| `ApplicationPartition`                                  | [ ] Pending | N/A                                      | Group30          |
| `ApplicationPartitionToEcuPartitionMapping`             | [ ] Pending | N/A                                      | Group18          |
| `ApplicationPrimitiveDataType`                          | [x] Done    | 4a9ccae9b8                               | Group2           |
| `ApplicationRecordDataType`                             | [x] Deferred| 0a06e0fae3                               | Group2           |
| `ApplicationRecordElement`                              | [x] Done    | ae4ed75065                               | Group2           |
| `ApplicationRuleBasedValueSpecification`                | [ ] Pending | N/A                                      | Group28          |
| `ApplicationSwComponentType`                            | [ ] Pending | N/A                                      | Group27          |
| `ApplicationValueSpecification`                         | [ ] Pending | N/A                                      | Group28          |
| `ArParameterInImplementationDataInstanceRef`            | [ ] Pending | N/A                                      | Group28          |
| `ArVariableInImplementationDataInstanceRef`             | [x] Done    | 910009eecc                               | Group2           |
| `ArbitraryEventTriggering`                              | [ ] Pending | N/A                                      | Group35          |
| `Area`                                                  | [x] Done    | c9f2464902                               | Group3           |
| `AreaEnumNohref`                                        | [x] Done    | 1d6f8c0aa9                               | Group3           |
| `AreaEnumShape`                                         | [x] Done    | 966320f6a7                               | Group3           |
| `ArgumentDataPrototype`                                 | [ ] Pending | N/A                                      | Group27          |
| `ArgumentDirectionEnum`                                 | [ ] Pending | N/A                                      | Group22          |
| `ArrayImplPolicyEnum`                                   | [x] Done    | 700b032789                               | Group10          |
| `ArraySizeHandlingEnum`                                 | [ ] Pending | N/A                                      | Group28          |
| `ArraySizeSemanticsEnum`                                | [ ] Pending | N/A                                      | Group28          |
| `ArrayValueSpecification`                               | [x] Done    | 043de7436d                               | Group3           |
| `AsamRecordLayoutSemantics`                             | [x] Done    | 2acaf7a45f                               | Group3           |
| `AssemblySwConnector`                                   | [x] Done    | 2a104a061c                               | Group2           |
| `AssignFrameId`                                         | [ ] Pending | N/A                                      | Group31          |
| `AssignFrameIdRange`                                    | [ ] Pending | N/A                                      | Group31          |
| `AssignNad`                                             | [ ] Pending | N/A                                      | Group31          |
| `AsynchronousServerCallPoint`                           | [x] Done    | 3223dde420                               | Group2           |
| `AsynchronousServerCallResultPoint`                     | [x] Done    | 724f490c7a                               | Group2           |
| `AsynchronousServerCallReturnsEvent`                    | [ ] Deferred| N/A                                      | Group12          |
| `AtomicSwComponentType`                                 | [ ] Pending | N/A                                      | Group27          |
| `AtpBlueprint`                                          | [x] Done    | 043de7436d                               | Group1           |
| `AtpBlueprintMapping`                                   | [x] Done    | 493e272da6                               | Group1           |
| `AtpBlueprintable`                                      | [x] Done    | b7cf03094f                               | Group1           |
| `AtpClassifier`                                         | [ ] Pending | N/A                                      | Group21          |
| `AtpDefinition`                                         | [x] Done    | 38eb1e817c                               | Group1           |
| `AtpFeature`                                            | [ ] Pending | N/A                                      | Group21          |
| `AtpInstanceRef`                                        | [ ] Pending | N/A                                      | Group21          |
| `AtpPrototype`                                          | [x] Done    | eb4c4bf308                               | Group1           |
| `AtpStructureElement`                                   | [x] Done    | 5eff088fa5                               | Group1           |
| `AtpType`                                               | [x] Done    | 451ad38330                               | Group1           |
| `AttributeCondition`                                    | [ ] Pending | N/A                                      | Group36          |
| `AttributeTailoring`                                    | [ ] Pending | N/A                                      | Group36          |
| `AttributeValueVariationPoint`                          | [x] Done    | d5c96fd954                               | Group8           |
| `AutoCollectEnum`                                       | [x] Done    | 75f4005552                               | Group1           |
| `AutosarDataPrototype`                                  | [ ] Pending | N/A                                      | Group28          |
| `AutosarDataType`                                       | [x] Done    | a5f99df464                               | Group1           |
| `AutosarEngineeringObject`                              | [ ] Pending | N/A                                      | Group22          |
| `AutosarOperationArgumentInstance`                      | [x] Done    | b8cce0057f                               | Group8           |
| `AutosarParameterRef`                                   | [x] Done    | b530f7e446                               | Group10          |
| `AutosarVariableInstance`                               | [ ] Pending | N/A                                      | Group35          |
| `AutosarVariableRef`                                    | [x] Done    | d1b9384acc                               | Group10          |
| `AxisIndexType`                                         | [ ] Pending | N/A                                      | Group21          |
| `BackgroundEvent`                                       | [x] Done    | 27b88a942c                               | Group2           |
| `BaseType`                                              | [ ] Pending | N/A                                      | Group28          |
| `BaseTypeDefinition`                                    | [ ] Pending | N/A                                      | Group28          |
| `BaseTypeDirectDefinition`                              | [ ] Pending | N/A                                      | Group28          |
| `BaseTypeEncodingString`                                | [ ] Pending | N/A                                      | Group21          |
| `Baseline`                                              | [ ] Pending | N/A                                      | Group36          |
| `BinaryManifestAddressableObject`                       | [ ] Pending | N/A                                      | Group34          |
| `BinaryManifestItem`                                    | [ ] Pending | N/A                                      | Group34          |
| `BinaryManifestItemDefinition`                          | [ ] Pending | N/A                                      | Group34          |
| `BinaryManifestItemNumericalValue`                      | [ ] Pending | N/A                                      | Group34          |
| `BinaryManifestItemPointerValue`                        | [ ] Pending | N/A                                      | Group34          |
| `BinaryManifestItemValue`                               | [ ] Pending | N/A                                      | Group34          |
| `BinaryManifestMetaDataField`                           | [ ] Pending | N/A                                      | Group35          |
| `BinaryManifestProvideResource`                         | [ ] Pending | N/A                                      | Group34          |
| `BinaryManifestRequireResource`                         | [ ] Pending | N/A                                      | Group34          |
| `BinaryManifestResource`                                | [ ] Pending | N/A                                      | Group34          |
| `BinaryManifestResourceDefinition`                      | [ ] Pending | N/A                                      | Group34          |
| `BindingTimeEnum`                                       | [x] Done    | 53bf180881                               | Group8           |
| `BlockState`                                            | [ ] Pending | N/A                                      | Group36          |
| `BlueprintFormula`                                      | [x] Done    | 6d8ace0288                               | Group8           |
| `BlueprintGenerator`                                    | [x] Done    | 246fc98452                               | Group8           |
| `BlueprintMapping`                                      | [x] Done    | a6fa7b8c18                               | Group8           |
| `BlueprintMappingSet`                                   | [x] Done    | aec046b9cc                               | Group1           |
| `BlueprintPolicy`                                       | [x] Done    | f5f5084e36                               | Group1           |
| `BooleanValueVariationPoint`                            | [x] Done    | d5c96fd954                               | Group8           |
| `Br`                                                    | [x] Done    | c2a85e6f8f                               | Group3           |
| `BswApiOptions`                                         | [ ] Deferred| N/A                                      | Group13          |
| `BswAsynchronousServerCallPoint`                        | [ ] Pending | N/A                                      | Group22          |
| `BswAsynchronousServerCallResultPoint`                  | [ ] Pending | N/A                                      | Group22          |
| `BswAsynchronousServerCallReturnsEvent`                 | [ ] Deferred| N/A                                      | Group13          |
| `BswBackgroundEvent`                                    | [ ] Pending | N/A                                      | Group22          |
| `BswCallType`                                           | [ ] Pending | N/A                                      | Group22          |
| `BswCalledEntity`                                       | [ ] Pending | N/A                                      | Group22          |
| `BswClientPolicy`                                       | [x] Done    | 3141824107                               | Group4           |
| `BswCompositionTiming`                                  | [ ] Pending | N/A                                      | Group35          |
| `BswDataReceivedEvent`                                  | [ ] Deferred| N/A                                      | Group13          |
| `BswDataReceptionPolicy`                                | [ ] Deferred| 7e3a2541a3                               | Group13          |
| `BswDataSendPolicy`                                     | [x] Done    | ccacff4a64                               | Group4           |
| `BswDirectCallPoint`                                    | [ ] Deferred| N/A                                      | Group13          |
| `BswDistinguishedPartition`                             | [ ] Pending | N/A                                      | Group22          |
| `BswEntryKindEnum`                                      | [ ] Pending | N/A                                      | Group22          |
| `BswEntryRelationship`                                  | [ ] Deferred| 75c6517342                               | Group13          |
| `BswEntryRelationshipEnum`                              | [ ] Deferred| 994c3903cb                               | Group13          |
| `BswEntryRelationshipSet`                               | [ ] Deferred| a4d57abd3a                               | Group13          |
| `BswEvent`                                              | [ ] Pending | N/A                                      | Group22          |
| `BswExclusiveAreaPolicy`                                | [ ] Pending | N/A                                      | Group22          |
| `BswExecutionContext`                                   | [ ] Pending | N/A                                      | Group22          |
| `BswExternalTriggerOccurredEvent`                       | [ ] Pending | N/A                                      | Group22          |
| `BswImplementation`                                     | [ ] Pending | N/A                                      | Group22          |
| `BswInternalBehavior`                                   | [x] Done    | 89a7231799                               | Group4           |
| `BswInternalTriggerOccurredEvent`                       | [ ] Deferred| N/A                                      | Group13          |
| `BswInternalTriggeringPoint`                            | [ ] Deferred| N/A                                      | Group13          |
| `BswInternalTriggeringPointPolicy`                      | [x] Done    | 2bb8413910                               | Group4           |
| `BswInterruptCategory`                                  | [ ] Pending | N/A                                      | Group22          |
| `BswInterruptEntity`                                    | [ ] Deferred| N/A                                      | Group13          |
| `BswInterruptEvent`                                     | [ ] Pending | N/A                                      | Group22          |
| `BswMgrNeeds`                                           | [x] Done    | 628464ed64                               | Group4           |
| `BswModeManagerErrorEvent`                              | [ ] Deferred| N/A                                      | Group13          |
| `BswModeReceiverPolicy`                                 | [ ] Pending | N/A                                      | Group22          |
| `BswModeSenderPolicy`                                   | [ ] Pending | N/A                                      | Group22          |
| `BswModeSwitchAckRequest`                               | [ ] Deferred| N/A                                      | Group13          |
| `BswModeSwitchEvent`                                    | [ ] Pending | N/A                                      | Group22          |
| `BswModeSwitchedAckEvent`                               | [ ] Deferred| 160eae8f23                               | Group13          |
| `BswModuleCallPoint`                                    | [ ] Deferred| N/A                                      | Group13          |
| `BswModuleClientServerEntry`                            | [ ] Deferred| e69bc46baa                               | Group13          |
| `BswModuleDependency`                                   | [ ] Deferred| 1ca038b144                               | Group13          |
| `BswModuleDescription`                                  | [ ] Pending | N/A                                      | Group22          |
| `BswModuleEntity`                                       | [ ] Pending | N/A                                      | Group22          |
| `BswModuleEntry`                                        | [ ] Pending | N/A                                      | Group22          |
| `BswModuleTiming`                                       | [ ] Pending | N/A                                      | Group35          |
| `BswOperationInvokedEvent`                              | [ ] Pending | N/A                                      | Group22          |
| `BswOsTaskExecutionEvent`                               | [ ] Pending | N/A                                      | Group22          |
| `BswParameterPolicy`                                    | [x] Done    | eceaef9296                               | Group4           |
| `BswPerInstanceMemoryPolicy`                            | [x] Done    | b89ad783a3                               | Group4           |
| `BswQueuedDataReceptionPolicy`                          | [ ] Deferred| N/A                                      | Group13          |
| `BswReleasedTriggerPolicy`                              | [x] Done    | 04498e5b27                               | Group4           |
| `BswSchedulableEntity`                                  | [ ] Pending | N/A                                      | Group22          |
| `BswScheduleEvent`                                      | [ ] Pending | N/A                                      | Group22          |
| `BswSchedulerNamePrefix`                                | [ ] Pending | N/A                                      | Group22          |
| `BswServiceDependency`                                  | [ ] Pending | N/A                                      | Group23          |
| `BswServiceDependencyIdent`                             | [ ] Pending | N/A                                      | Group26          |
| `BswSynchronousServerCallPoint`                         | [ ] Deferred| N/A                                      | Group13          |
| `BswTimingEvent`                                        | [ ] Deferred| 1a0a0619b2                               | Group13          |
| `BswTriggerDirectImplementation`                        | [ ] Pending | N/A                                      | Group22          |
| `BswVariableAccess`                                     | [ ] Pending | N/A                                      | Group22          |
| `BufferProperties`                                      | [ ] Pending | N/A                                      | Group28          |
| `BuildAction`                                           | [x] Done    | 6c9ef66b40                               | Group1           |
| `BuildActionEntity`                                     | [x] Done    | d7717e736a                               | Group1           |
| `BuildActionEnvironment`                                | [x] Done    | 2311c8754f                               | Group1           |
| `BuildActionInvocator`                                  | [x] Done    | 7008d5e857                               | Group1           |
| `BuildActionIoElement`                                  | [x] Done    | b572582c11                               | Group1           |
| `BuildActionManifest`                                   | [x] Done    | e6dcc8e79f                               | Group1           |
| `BuildEngineeringObject`                                | [x] Done    | 96d176ed20                               | Group1           |
| `BulkNvDataDescriptor`                                  | [x] Done    | 14a0a9cc5b                               | Group10          |
| `BurstPatternEventTriggering`                           | [ ] Pending | N/A                                      | Group35          |
| `BusMirrorCanIdRangeMapping`                            | [ ] Pending | N/A                                      | Group34          |
| `BusMirrorCanIdToCanIdMapping`                          | [ ] Pending | N/A                                      | Group34          |
| `BusMirrorChannel`                                      | [ ] Pending | N/A                                      | Group33          |
| `BusMirrorChannelMapping`                               | [ ] Pending | N/A                                      | Group33          |
| `BusMirrorChannelMappingCan`                            | [ ] Pending | N/A                                      | Group34          |
| `BusMirrorChannelMappingFlexray`                        | [ ] Pending | N/A                                      | Group34          |
| `BusMirrorChannelMappingIp`                             | [ ] Pending | N/A                                      | Group34          |
| `BusMirrorChannelMappingUserDefined`                    | [ ] Pending | N/A                                      | Group34          |
| `BusMirrorLinPidToCanIdMapping`                         | [ ] Pending | N/A                                      | Group34          |
| `BusspecificNmEcu`                                      | [ ] Pending | N/A                                      | Group33          |
| `ByteOrderEnum`                                         | [ ] Pending | N/A                                      | Group28          |
| `CIdentifier`                                           | [ ] Pending | N/A                                      | Group21          |
| `CSTransformerErrorReactionEnum`                        | [ ] Pending | N/A                                      | Group34          |
| `CalibrationParameterValue`                             | [ ] Pending | N/A                                      | Group28          |
| `CalibrationParameterValueSet`                          | [ ] Pending | N/A                                      | Group28          |
| `CalprmAxisCategoryEnum`                                | [ ] Pending | N/A                                      | Group28          |
| `CanAddressingModeType`                                 | [ ] Pending | N/A                                      | Group32          |
| `CanCluster`                                            | [ ] Pending | N/A                                      | Group29          |
| `CanClusterBusOffRecovery`                              | [ ] Deferred| N/A                                      | Group17          |
| `CanCommunicationConnector`                             | [ ] Deferred| N/A                                      | Group17          |
| `CanCommunicationController`                            | [ ] Pending | N/A                                      | Group29          |
| `CanControllerConfiguration`                            | [ ] Deferred| N/A                                      | Group17          |
| `CanControllerConfigurationRequirements`                | [ ] Deferred| N/A                                      | Group17          |
| `CanControllerFdConfiguration`                          | [ ] Pending | N/A                                      | Group29          |
| `CanControllerFdConfigurationRequirements`              | [ ] Deferred| N/A                                      | Group17          |
| `CanControllerXlConfiguration`                          | [ ] Pending | N/A                                      | Group29          |
| `CanControllerXlConfigurationRequirements`              | [ ] Pending | N/A                                      | Group29          |
| `CanFrame`                                              | [ ] Pending | N/A                                      | Group32          |
| `CanFrameRxBehaviorEnum`                                | [ ] Pending | N/A                                      | Group32          |
| `CanFrameTriggering`                                    | [ ] Pending | N/A                                      | Group32          |
| `CanFrameTxBehaviorEnum`                                | [ ] Pending | N/A                                      | Group32          |
| `CanGlobalTimeDomainProps`                              | [ ] Pending | N/A                                      | Group34          |
| `CanNmCluster`                                          | [ ] Pending | N/A                                      | Group18          |
| `CanNmClusterCoupling`                                  | [ ] Pending | N/A                                      | Group18          |
| `CanNmEcu`                                              | [ ] Pending | N/A                                      | Group33          |
| `CanNmNode`                                             | [ ] Pending | N/A                                      | Group18          |
| `CanPhysicalChannel`                                    | [ ] Pending | N/A                                      | Group29          |
| `CanTpAddress`                                          | [ ] Pending | N/A                                      | Group33          |
| `CanTpAddressingFormatType`                             | [ ] Pending | N/A                                      | Group33          |
| `CanTpChannel`                                          | [ ] Pending | N/A                                      | Group33          |
| `CanTpConfig`                                           | [ ] Pending | N/A                                      | Group33          |
| `CanTpConnection`                                       | [ ] Pending | N/A                                      | Group33          |
| `CanTpEcu`                                              | [ ] Pending | N/A                                      | Group33          |
| `CanTpNode`                                             | [ ] Pending | N/A                                      | Group33          |
| `CategoryString`                                        | [ ] Pending | N/A                                      | Group21          |
| `Chapter`                                               | [ ] Pending | N/A                                      | Group22          |
| `ChapterContent`                                        | [x] Done    | dee07d0a3a                               | Group9           |
| `ChapterEnumBreak`                                      | [x] Done    | 20e6ee88d0                               | Group3           |
| `ChapterModel`                                          | [x] Done    | d3d61c9b2e                               | Group9           |
| `ChapterOrMsrQuery`                                     | [ ] Pending | N/A                                      | Group22          |
| `ClassContentConditional`                               | [ ] Pending | N/A                                      | Group36          |
| `ClassTailoring`                                        | [ ] Pending | N/A                                      | Group36          |
| `ClientComSpec`                                         | [ ] Pending | N/A                                      | Group27          |
| `ClientIdDefinition`                                    | [x] Done    | 8618ec8872                               | Group5           |
| `ClientIdDefinitionSet`                                 | [x] Done    | 01759771dd                               | Group5           |
| `ClientIdRange`                                         | [x] Done    | fce66955f5                               | Group5           |
| `ClientServerAnnotation`                                | [ ] Pending | N/A                                      | Group27          |
| `ClientServerApplicationErrorMapping`                   | [x] Done    | bc933575fd                               | Group11          |
| `ClientServerInterface`                                 | [ ] Pending | N/A                                      | Group27          |
| `ClientServerInterfaceMapping`                          | [ ] Deferred| N/A                                      | Group11          |
| `ClientServerOperation`                                 | [ ] Pending | N/A                                      | Group27          |
| `ClientServerOperationBlueprintMapping`                 | [ ] Pending | N/A                                      | Group36          |
| `ClientServerOperationComProps`                         | [ ] Pending | N/A                                      | Group34          |
| `ClientServerOperationMapping`                          | [ ] Deferred| N/A                                      | Group11          |
| `ClientServerToSignalMapping`                           | [ ] Pending | N/A                                      | Group31          |
| `Code`                                                  | [x] Done    | 9f470606b5                               | Group1           |
| `CollectableElement`                                    | [x] Done    | 3b31b7c402                               | Group1           |
| `Collection`                                            | [x] Done    | 75f4005552                               | Group1           |
| `Colspec`                                               | [x] Done    | 2bd0d07503                               | Group3           |
| `ComManagementMapping`                                  | [x] Done    | 19c327cca6                               | Group5           |
| `ComMgrUserNeeds`                                       | [ ] Pending | N/A                                      | Group23          |
| `CommConnectorPort`                                     | [ ] Pending | N/A                                      | Group31          |
| `CommonSignalPath`                                      | [ ] Pending | N/A                                      | Group31          |
| `CommunicationBufferLocking`                            | [x] Done    | 7c67628122                               | Group2           |
| `CommunicationCluster`                                  | [ ] Pending | N/A                                      | Group24          |
| `CommunicationConnector`                                | [ ] Pending | N/A                                      | Group29          |
| `CommunicationController`                               | [ ] Pending | N/A                                      | Group27          |
| `CommunicationControllerMapping`                        | [x] Done    | 2613747d22                               | Group7           |
| `CommunicationCycle`                                    | [x] Done    | 75683a2ede                               | Group5           |
| `CommunicationDirectionType`                            | [ ] Pending | 3378eb6247                               | Group15          |
| `Compiler`                                              | [x] Done    | 3fce597322                               | Group1           |
| `ComplexDeviceDriverSwComponentType`                    | [ ] Pending | N/A                                      | Group29          |
| `ComponentClustering`                                   | [ ] Pending | N/A                                      | Group30          |
| `ComponentInCompositionInstanceRef`                     | [x] Done    | 02e863a567                               | Group7           |
| `ComponentInSystemInstanceRef`                          | [x] Done    | b511fb85b0                               | Group7           |
| `ComponentSeparation`                                   | [ ] Pending | N/A                                      | Group30          |
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
| `ConcreteClassTailoring`                                | [ ] Pending | N/A                                      | Group36          |
| `ConcretePatternEventTriggering`                        | [ ] Pending | N/A                                      | Group35          |
| `ConditionByFormula`                                    | [x] Done    | 18b494eba5                               | Group8           |
| `ConditionalChangeNad`                                  | [ ] Pending | N/A                                      | Group32          |
| `ConfidenceInterval`                                    | [ ] Pending | N/A                                      | Group35          |
| `ConfigReferenceValue`                                  | [ ] Pending | N/A                                      | Group19          |
| `ConsistencyNeeds`                                      | [ ] Pending | N/A                                      | Group28          |
| `ConstantReference`                                     | [x] Done    | 4853348ea0                               | Group9           |
| `ConstantSpecification`                                 | [x] Done    | 265721a764                               | Group9           |
| `ConstantSpecificationMapping`                          | [ ] Pending | N/A                                      | Group28          |
| `ConstantSpecificationMappingSet`                       | [x] Done    | 8e5acbb2b1                               | Group1           |
| `ConstraintTailoring`                                   | [ ] Pending | N/A                                      | Group36          |
| `ConsumedEventGroup`                                    | [ ] Pending | N/A                                      | Group32          |
| `ConsumedProvidedServiceInstanceGroup`                  | [x] Done    | fce66955f5                               | Group5           |
| `ConsumedServiceInstance`                               | [ ] Pending | N/A                                      | Group32          |
| `ContainedIPduCollectionSemanticsEnum`                  | [x] Done    | 64d125ffae                               | Group5           |
| `ContainedIPduProps`                                    | [x] Done    | 206cf29517                               | Group5           |
| `ContainerIPdu`                                         | [ ] Pending | N/A                                      | Group31          |
| `ContainerIPduHeaderTypeEnum`                           | [ ] Pending | N/A                                      | Group31          |
| `ContainerIPduTriggerEnum`                              | [ ] Pending | N/A                                      | Group31          |
| `CouplingElement`                                       | [ ] Pending | N/A                                      | Group30          |
| `CouplingElementAbstractDetails`                        | [ ] Pending | N/A                                      | Group30          |
| `CouplingElementEnum`                                   | [ ] Pending | N/A                                      | Group30          |
| `CouplingElementSwitchDetails`                          | [ ] Pending | N/A                                      | Group30          |
| `CouplingPort`                                          | [ ] Pending | N/A                                      | Group30          |
| `CouplingPortAbstractShaper`                            | [ ] Pending | N/A                                      | Group16          |
| `CouplingPortConnection`                                | [ ] Pending | N/A                                      | Group30          |
| `CouplingPortDetails`                                   | [ ] Pending | N/A                                      | Group30          |
| `CouplingPortFifo`                                      | [ ] Pending | N/A                                      | Group30          |
| `CouplingPortRatePolicy`                                | [ ] Pending | N/A                                      | Group30          |
| `CouplingPortRatePolicyActionEnum`                      | [ ] Pending | N/A                                      | Group30          |
| `CouplingPortScheduler`                                 | [x] Done    | 0f61040c0c                               | Group6           |
| `CouplingPortShaper`                                    | [ ] Pending | N/A                                      | Group30          |
| `CouplingPortStructuralElement`                         | [x] Done    | 8404bbb94a                               | Group6           |
| `CouplingPortTrafficClassAssignment`                    | [ ] Pending | N/A                                      | Group30          |
| `CpSoftwareCluster`                                     | [x] Done    | 1194e00ca2                               | Group5           |
| `CpSoftwareClusterBinaryManifestDescriptor`             | [ ] Pending | N/A                                      | Group34          |
| `CpSoftwareClusterCommunicationResource`                | [ ] Pending | N/A                                      | Group34          |
| `CpSoftwareClusterCommunicationResourceProps`           | [ ] Pending | N/A                                      | Group34          |
| `CpSoftwareClusterMappingSet`                           | [ ] Pending | N/A                                      | Group31          |
| `CpSoftwareClusterResource`                             | [ ] Pending | N/A                                      | Group26          |
| `CpSoftwareClusterResourcePool`                         | [ ] Pending | N/A                                      | Group34          |
| `CpSoftwareClusterResourceToApplicationPartitionMapping` | [ ] Pending | N/A                                      | Group31          |
| `CpSoftwareClusterServiceResource`                      | [ ] Pending | N/A                                      | Group34          |
| `CpSoftwareClusterToApplicationPartitionMapping`        | [ ] Pending | N/A                                      | Group31          |
| `CpSoftwareClusterToEcuInstanceMapping`                 | [ ] Pending | N/A                                      | Group31          |
| `CpSoftwareClusterToResourceMapping`                    | [ ] Pending | N/A                                      | Group34          |
| `CpSwClusterResourceToDiagDataElemMapping`              | [ ] Pending | N/A                                      | Group26          |
| `CpSwClusterResourceToDiagFunctionIdMapping`            | [ ] Pending | N/A                                      | Group26          |
| `CpSwClusterToDiagEventMapping`                         | [ ] Pending | N/A                                      | Group26          |
| `CpSwClusterToDiagRoutineSubfunctionMapping`            | [ ] Pending | N/A                                      | Group26          |
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
| `CryptoServiceKey`                                      | [ ] Pending | N/A                                      | Group31          |
| `CryptoServiceKeyGenerationEnum`                        | [ ] Pending | N/A                                      | Group31          |
| `CryptoServiceMapping`                                  | [x] Done    | 757aea1d17                               | Group6           |
| `CryptoServiceNeeds`                                    | [ ] Deferred| d064592a44                               | Group14          |
| `CryptoServicePrimitive`                                | [x] Done    | b609d72d59                               | Group6           |
| `CryptoServiceQueue`                                    | [ ] Pending | N/A                                      | Group31          |
| `CryptoSignatureScheme`                                 | [x] Done    | 1eaeb5800b                               | Group6           |
| `CseCodeType`                                           | [ ] Pending | N/A                                      | Group21          |
| `CycleCounter`                                          | [x] Done    | 75683a2ede                               | Group5           |
| `CycleRepetition`                                       | [x] Done    | 75683a2ede                               | Group5           |
| `CycleRepetitionType`                                   | [x] Done    | bf6cb0f022                               | Group5           |
| `CyclicTiming`                                          | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `DataComProps`                                          | [ ] Pending | N/A                                      | Group34          |
| `DataConsistencyPolicyEnum`                             | [ ] Pending | N/A                                      | Group34          |
| `DataConstr`                                            | [x] Done    | 9927cc9e89                               | Group3           |
| `DataConstrRule`                                        | [x] Done    | fa640a0d86                               | Group3           |
| `DataDumpEntry`                                         | [ ] Pending | N/A                                      | Group32          |
| `DataExchangePoint`                                     | [ ] Pending | N/A                                      | Group36          |
| `DataExchangePointKind`                                 | [ ] Pending | N/A                                      | Group36          |
| `DataFilter`                                            | [x] Done    | ed2a073e76                               | Group9           |
| `DataFilterTypeEnum`                                    | [x] Done    | b59bd6ebbe                               | Group9           |
| `DataFormatElementReference`                            | [ ] Pending | N/A                                      | Group36          |
| `DataFormatElementScope`                                | [ ] Pending | N/A                                      | Group36          |
| `DataIdModeEnum`                                        | [ ] Pending | N/A                                      | Group34          |
| `DataInterface`                                         | [x] Done    | d838fd43f4                               | Group1           |
| `DataLimitKindEnum`                                     | [ ] Pending | N/A                                      | Group27          |
| `DataLinkLayerRule`                                     | [ ] Deferred| 0d343df2a7                               | Group20          |
| `DataMapping`                                           | [ ] Deferred| N/A                                      | Group17          |
| `DataPrototype`                                         | [x] Done    | 9175595d88                               | Group1           |
| `DataPrototypeGroup`                                    | [ ] Pending | N/A                                      | Group28          |
| `DataPrototypeInClientServerInterfaceInstanceRef`       | [ ] Pending | N/A                                      | Group34          |
| `DataPrototypeInPortInterfaceRef`                       | [ ] Pending | N/A                                      | Group34          |
| `DataPrototypeInSenderReceiverInterfaceInstanceRef`     | [ ] Pending | N/A                                      | Group34          |
| `DataPrototypeMapping`                                  | [ ] Pending | N/A                                      | Group27          |
| `DataPrototypeReference`                                | [ ] Pending | N/A                                      | Group34          |
| `DataPrototypeTransformationProps`                      | [x] Done    | ba255a82cc                               | Group6           |
| `DataReceiveErrorEvent`                                 | [ ] Deferred| N/A                                      | Group12          |
| `DataReceivedEvent`                                     | [ ] Deferred| N/A                                      | Group12          |
| `DataSendCompletedEvent`                                | [ ] Deferred| N/A                                      | Group12          |
| `DataTransformation`                                    | [ ] Pending | N/A                                      | Group27          |
| `DataTransformationErrorHandlingEnum`                   | [x] Done    | 7fc79e4b73                               | Group2           |
| `DataTransformationKindEnum`                            | [ ] Pending | N/A                                      | Group27          |
| `DataTransformationSet`                                 | [x] Done    | 757aea1d17                               | Group6           |
| `DataTransformationStatusForwardingEnum`                | [x] Done    | 7c67628122                               | Group2           |
| `DataTypeMap`                                           | [x] Done    | 0731ff4f68                               | Group10          |
| `DataTypeMappingSet`                                    | [x] Done    | 21ab486b53                               | Group2           |
| `DataTypePolicyEnum`                                    | [ ] Pending | N/A                                      | Group31          |
| `DataWriteCompletedEvent`                               | [ ] Deferred| N/A                                      | Group12          |
| `DateTime`                                              | [ ] Pending | N/A                                      | Group21          |
| `DcmIPdu`                                               | [ ] Pending | N/A                                      | Group31          |
| `DdsCpConfig`                                           | [ ] Pending | N/A                                      | Group32          |
| `DdsCpConsumedServiceInstance`                          | [ ] Pending | N/A                                      | Group32          |
| `DdsCpDomain`                                           | [ ] Pending | N/A                                      | Group32          |
| `DdsCpISignalToDdsTopicMapping`                         | [ ] Pending | N/A                                      | Group31          |
| `DdsCpPartition`                                        | [ ] Pending | N/A                                      | Group32          |
| `DdsCpProvidedServiceInstance`                          | [ ] Pending | N/A                                      | Group32          |
| `DdsCpQosProfile`                                       | [ ] Pending | N/A                                      | Group32          |
| `DdsCpServiceInstance`                                  | [ ] Pending | N/A                                      | Group32          |
| `DdsCpServiceInstanceEvent`                             | [ ] Pending | N/A                                      | Group32          |
| `DdsCpServiceInstanceOperation`                         | [ ] Pending | N/A                                      | Group32          |
| `DdsCpTopic`                                            | [ ] Pending | N/A                                      | Group32          |
| `DdsDeadline`                                           | [ ] Pending | N/A                                      | Group32          |
| `DdsDestinationOrder`                                   | [ ] Pending | N/A                                      | Group32          |
| `DdsDestinationOrderKindEnum`                           | [ ] Pending | N/A                                      | Group32          |
| `DdsDurability`                                         | [ ] Pending | N/A                                      | Group32          |
| `DdsDurabilityKindEnum`                                 | [ ] Pending | N/A                                      | Group32          |
| `DdsDurabilityService`                                  | [ ] Pending | N/A                                      | Group32          |
| `DdsDurabilityServiceHistoryKindEnum`                   | [ ] Pending | N/A                                      | Group32          |
| `DdsHistory`                                            | [ ] Pending | N/A                                      | Group32          |
| `DdsHistoryKindEnum`                                    | [ ] Pending | N/A                                      | Group32          |
| `DdsLatencyBudget`                                      | [ ] Pending | N/A                                      | Group32          |
| `DdsLifespan`                                           | [ ] Pending | N/A                                      | Group32          |
| `DdsLiveliness`                                         | [ ] Pending | N/A                                      | Group32          |
| `DdsLivenessKindEnum`                                   | [ ] Pending | N/A                                      | Group32          |
| `DdsOwnership`                                          | [ ] Pending | N/A                                      | Group32          |
| `DdsOwnershipKindEnum`                                  | [ ] Pending | N/A                                      | Group32          |
| `DdsOwnershipStrength`                                  | [ ] Pending | N/A                                      | Group32          |
| `DdsReliability`                                        | [ ] Pending | N/A                                      | Group32          |
| `DdsReliabilityKindEnum`                                | [ ] Pending | N/A                                      | Group32          |
| `DdsResourceLimits`                                     | [ ] Pending | N/A                                      | Group32          |
| `DdsTopicData`                                          | [ ] Pending | N/A                                      | Group32          |
| `DdsTransportPriority`                                  | [ ] Pending | N/A                                      | Group32          |
| `DefItem`                                               | [ ] Pending | N/A                                      | Group21          |
| `DefList`                                               | [ ] Pending | N/A                                      | Group21          |
| `DefaultValueApplicationStrategyEnum`                   | [ ] Pending | N/A                                      | Group36          |
| `DefaultValueElement`                                   | [ ] Pending | N/A                                      | Group17          |
| `DelegatedPortAnnotation`                               | [ ] Pending | N/A                                      | Group27          |
| `DelegationSwConnector`                                 | [x] Done    | 503344170e                               | Group2           |
| `DependencyOnArtifact`                                  | [x] Done    | 25211e56ca                               | Group1           |
| `DependencyUsageEnum`                                   | [x] Done    | 9a8c86ae9a                               | Group10          |
| `DevelopmentError`                                      | [ ] Pending | N/A                                      | Group23          |
| `DhcpServerConfiguration`                               | [ ] Pending | N/A                                      | Group30          |
| `Dhcpv6Props`                                           | [ ] Pending | N/A                                      | Group30          |
| `DiagEventDebounceAlgorithm`                            | [x] Done    | 4f246ae62d                               | Group4           |
| `DiagEventDebounceCounterBased`                         | [ ] Deferred| d064592a44                               | Group14          |
| `DiagEventDebounceMonitorInternal`                      | [x] Done    | 103cfd4316                               | Group4           |
| `DiagEventDebounceTimeBased`                            | [ ] Pending | N/A                                      | Group23          |
| `DiagPduType`                                           | [ ] Pending | N/A                                      | Group31          |
| `DiagRequirementIdString`                               | [ ] Pending | N/A                                      | Group21          |
| `DiagnosticAbstractAliasEvent`                          | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticAbstractDataIdentifier`                      | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticAbstractParameter`                           | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticAccessPermission`                            | [x] Done    | 9cbb4e26e7                               | Group7           |
| `DiagnosticAging`                                       | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticAudienceEnum`                                | [ ] Deferred| 5685ad743e                               | Group14          |
| `DiagnosticAuthRole`                                    | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticAuthRoleProxy`                               | [x] Done    | 4579b43f0d                               | Group7           |
| `DiagnosticAuthTransmitCertificate`                     | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticAuthTransmitCertificateEvaluation`           | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticAuthTransmitCertificateMapping`              | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticAuthentication`                              | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticAuthenticationClass`                         | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticAuthenticationConfiguration`                 | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticCapabilityElement`                           | [ ] Deferred| f5ffd3abf2                               | Group14          |
| `DiagnosticClearDiagnosticInformation`                  | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticClearDiagnosticInformationClass`             | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticClearDtcLimitationEnum`                      | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticClearDtcNotificationEnum`                    | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DiagnosticClearEventAllowedBehaviorEnum`               | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticClearResetEmissionRelatedInfo`               | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticClearResetEmissionRelatedInfoClass`          | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticComControl`                                  | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticComControlClass`                             | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticComControlSpecificChannel`                   | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticComControlSubNodeChannel`                    | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticCommonElement`                               | [x] Done    | e0d022b1aa                               | Group7           |
| `DiagnosticCommonProps`                                 | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticCommunicationManagerNeeds`                   | [ ] Deferred| 79c639e42a                               | Group14          |
| `DiagnosticCompareTypeEnum`                             | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticComponentNeeds`                              | [x] Done    | 5c4c0963af                               | Group4           |
| `DiagnosticCondition`                                   | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticConditionGroup`                              | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticConnectedIndicator`                          | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticConnectedIndicatorBehaviorEnum`              | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticConnection`                                  | [x] Done    | e96086c12f                               | Group5           |
| `DiagnosticContributionSet`                             | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticControlDTCSetting`                           | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticControlDTCSettingClass`                      | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticControlEnableMaskBit`                        | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticControlNeeds`                                | [x] Done    | d0a1134e3b                               | Group4           |
| `DiagnosticCustomServiceClass`                          | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticCustomServiceInstance`                       | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticDataByIdentifier`                            | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticDataElement`                                 | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticDataIdentifier`                              | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticDataIdentifierSet`                           | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticDataTransfer`                                | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticDataTransferClass`                           | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticDeAuthentication`                            | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticDebounceAlgorithmProps`                      | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticDebounceBehaviorEnum`                        | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticDemProvidedDataMapping`                      | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticDenominatorConditionEnum`                    | [ ] Pending | N/A                                      | Group29          |
| `DiagnosticDynamicDataIdentifier`                       | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticDynamicallyDefineDataIdentifier`             | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticDynamicallyDefineDataIdentifierClass`        | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum` | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticEcuInstanceProps`                            | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticEcuReset`                                    | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticEcuResetClass`                               | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticEnableCondition`                             | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticEnableConditionGroup`                        | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticEnableConditionNeeds`                        | [ ] Pending | N/A                                      | Group29          |
| `DiagnosticEnableConditionPortMapping`                  | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticEnvBswModeElement`                           | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticEnvCompareCondition`                         | [ ] Deferred| af255af373                               | Group14          |
| `DiagnosticEnvConditionFormula`                         | [ ] Deferred| af255af373                               | Group14          |
| `DiagnosticEnvConditionFormulaPart`                     | [x] Deferred| af255af373                               | Group14          |
| `DiagnosticEnvDataCondition`                            | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticEnvDataElementCondition`                     | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticEnvModeCondition`                            | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticEnvModeElement`                              | [ ] Deferred| af255af373                               | Group14          |
| `DiagnosticEnvSwcModeElement`                           | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticEnvironmentalCondition`                      | [x] Done    | 5bbca5f217                               | Group7           |
| `DiagnosticEvent`                                       | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticEventClearAllowedEnum`                       | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticEventCombinationBehaviorEnum`                | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticEventCombinationReportingBehaviorEnum`       | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticEventDisplacementStrategyEnum`               | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticEventInfoNeeds`                              | [ ] Deferred| 79c639e42a                               | Group14          |
| `DiagnosticEventKindEnum`                               | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticEventManagerNeeds`                           | [x] Done    | dc34774429                               | Group4           |
| `DiagnosticEventNeeds`                                  | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticEventPortMapping`                            | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticEventToDebounceAlgorithmMapping`             | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticEventToEnableConditionGroupMapping`          | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticEventToOperationCycleMapping`                | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticEventToSecurityEventMapping`                 | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticEventToStorageConditionGroupMapping`         | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticEventToTroubleCodeJ1939Mapping`              | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticEventToTroubleCodeUdsMapping`                | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticEventWindow`                                 | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticEventWindowTimeEnum`                         | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticExtendedDataRecord`                          | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticFimAliasEvent`                               | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticFimAliasEventGroup`                          | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticFimAliasEventGroupMapping`                   | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticFimAliasEventMapping`                        | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticFimEventGroup`                               | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticFimFunctionMapping`                          | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticFreezeFrame`                                 | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticFunctionIdentifier`                          | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticFunctionIdentifierInhibit`                   | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticFunctionInhibitSource`                       | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticHandleDDDIConfigurationEnum`                 | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticIOControl`                                   | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticIndicator`                                   | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticIndicatorTypeEnum`                           | [ ] Pending | N/A                                      | Group29          |
| `DiagnosticInfoType`                                    | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticInhibitSourceEventMapping`                   | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticInhibitionMaskEnum`                          | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticIoControlClass`                              | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticIoControlNeeds`                              | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticIumpr`                                       | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticIumprDenominatorGroup`                       | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticIumprGroup`                                  | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticIumprGroupIdentifier`                        | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticIumprKindEnum`                               | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticIumprToFunctionIdentifierMapping`            | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticJ1939ExpandedFreezeFrame`                    | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticJ1939FreezeFrame`                            | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticJ1939Node`                                   | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticJ1939Spn`                                    | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticJ1939SpnMapping`                             | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticJ1939SwMapping`                              | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticJumpToBootLoaderEnum`                        | [ ] Deferred| N/A                                      | Group14          |
| `DiagnosticLogicalOperatorEnum`                         | [ ] Deferred| N/A                                      | Group14          |
| `DiagnosticMapping`                                     | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticMasterToSlaveEventMapping`                   | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticMeasurementIdentifier`                       | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticMemoryAddressableRangeAccess`                | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticMemoryByAddress`                             | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticMemoryDestination`                           | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticMemoryDestinationPrimary`                    | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticMemoryDestinationUserDefined`                | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticMemoryEntryStorageTriggerEnum`               | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticMemoryIdentifier`                            | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticMonitorUpdateKindEnum`                       | [ ] Pending | N/A                                      | Group29          |
| `DiagnosticObdSupportEnum`                              | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticOccurrenceCounterProcessingEnum`             | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticOperationCycle`                              | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticOperationCycleNeeds`                         | [ ] Pending | N/A                                      | Group29          |
| `DiagnosticOperationCyclePortMapping`                   | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticOperationCycleTypeEnum`                      | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticParameter`                                   | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticParameterElement`                            | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticParameterElementAccess`                      | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticParameterIdent`                              | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticParameterIdentifier`                         | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticParameterSupportInfo`                        | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticPeriodicRate`                                | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticPeriodicRateCategoryEnum`                    | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticPowertrainFreezeFrame`                       | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticProcessingStyleEnum`                         | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DiagnosticProofOfOwnership`                            | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticProtocol`                                    | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticReadDTCInformation`                          | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticReadDTCInformationClass`                     | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticReadDataByIdentifier`                        | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticReadDataByIdentifierClass`                   | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticReadDataByPeriodicID`                        | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticReadDataByPeriodicIDClass`                   | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticReadMemoryByAddress`                         | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticReadMemoryByAddressClass`                    | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticReadScalingDataByIdentifier`                 | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticReadScalingDataByIdentifierClass`            | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticRecordTriggerEnum`                           | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticRequestControlOfOnBoardDevice`               | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticRequestControlOfOnBoardDeviceClass`          | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticRequestCurrentPowertrainData`                | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticRequestCurrentPowertrainDataClass`           | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticRequestDownload`                             | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticRequestDownloadClass`                        | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticRequestEmissionRelatedDTC`                   | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticRequestEmissionRelatedDTCClass`              | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticRequestEmissionRelatedDTCPermanentStatus`    | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticRequestEmissionRelatedDTCPermanentStatusClass` | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticRequestFileTransfer`                         | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticRequestFileTransferClass`                    | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticRequestFileTransferNeeds`                    | [x] Done    | f084c4328c                               | Group4           |
| `DiagnosticRequestOnBoardMonitoringTestResults`         | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticRequestOnBoardMonitoringTestResultsClass`    | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticRequestPowertrainFreezeFrameData`            | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticRequestPowertrainFreezeFrameDataClass`       | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticRequestRoutineResults`                       | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticRequestUpload`                               | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticRequestUploadClass`                          | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticRequestVehicleInfo`                          | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticRequestVehicleInfoClass`                     | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticResponseOnEvent`                             | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticResponseOnEventActionEnum`                   | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticResponseOnEventClass`                        | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticResponseToEcuResetEnum`                      | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticRoutine`                                     | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticRoutineControl`                              | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticRoutineControlClass`                         | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticRoutineNeeds`                                | [ ] Deferred| 79c639e42a                               | Group14          |
| `DiagnosticRoutineSubfunction`                          | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticRoutineTypeEnum`                             | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DiagnosticSecurityAccess`                              | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticSecurityAccessClass`                         | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticSecurityEventReportingModeMapping`           | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticSecurityLevel`                               | [x] Done    | f2da1338fc                               | Group7           |
| `DiagnosticServiceClass`                                | [x] Deferred| 6b514727f9                               | Group14          |
| `DiagnosticServiceDataMapping`                          | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticServiceInstance`                             | [x] Done    | 6b514727f9                               | Group7           |
| `DiagnosticServiceMappingDiagTarget`                    | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticServiceRequestCallbackTypeEnum`              | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DiagnosticServiceSwMapping`                            | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticServiceTable`                                | [x] Done    | 9bd6fadae5                               | Group7           |
| `DiagnosticSession`                                     | [x] Done    | 06d4e49a26                               | Group7           |
| `DiagnosticSessionControl`                              | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticSessionControlClass`                         | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticSignificanceEnum`                            | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticStartRoutine`                                | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum` | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticStopRoutine`                                 | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticStorageCondition`                            | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticStorageConditionGroup`                       | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticStorageConditionNeeds`                       | [ ] Pending | N/A                                      | Group29          |
| `DiagnosticStorageConditionPortMapping`                 | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticSupportInfoByte`                             | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticSwMapping`                                   | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticTestIdentifier`                              | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticTestResult`                                  | [ ] Pending | N/A                                      | Group29          |
| `DiagnosticTestResultUpdateEnum`                        | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticTestRoutineIdentifier`                       | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticTransferExit`                                | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticTransferExitClass`                           | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticTroubleCode`                                 | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticTroubleCodeGroup`                            | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticTroubleCodeJ1939`                            | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticTroubleCodeJ1939DtcKindEnum`                 | [ ] Pending | N/A                                      | Group26          |
| `DiagnosticTroubleCodeObd`                              | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticTroubleCodeProps`                            | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticTroubleCodeUds`                              | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticTroubleCodeUdsToTroubleCodeObdMapping`       | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticTypeOfDtcSupportedEnum`                      | [ ] Pending | N/A                                      | Group23          |
| `DiagnosticTypeOfFreezeFrameRecordNumerationEnum`       | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticUdsSeverityEnum`                             | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticUploadDownloadNeeds`                         | [x] Done    | fe8a0a1a6d                               | Group4           |
| `DiagnosticValueAccessEnum`                             | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DiagnosticValueNeeds`                                  | [ ] Deferred| 79c639e42a                               | Group14          |
| `DiagnosticVerifyCertificateBidirectional`              | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticVerifyCertificateUnidirectional`             | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticWriteDataByIdentifier`                       | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticWriteDataByIdentifierClass`                  | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticWriteMemoryByAddress`                        | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticWriteMemoryByAddressClass`                   | [ ] Pending | N/A                                      | Group24          |
| `DiagnosticWwhObdDtcClassEnum`                          | [ ] Pending | N/A                                      | Group25          |
| `DiagnosticsCommunicationSecurityNeeds`                 | [x] Done    | d24a66632e                               | Group4           |
| `DisplayFormatString`                                   | [ ] Pending | N/A                                      | Group21          |
| `DisplayPresentationEnum`                               | [ ] Pending | N/A                                      | Group28          |
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
| `DoIpEntityRoleEnum`                                    | [ ] Pending | N/A                                      | Group32          |
| `DoIpGidNeeds`                                          | [x] Done    | 6c31e0057f                               | Group4           |
| `DoIpGidSynchronizationNeeds`                           | [x] Done    | c64cb6318c                               | Group4           |
| `DoIpInterface`                                         | [x] Done    | c53a7febdc                               | Group5           |
| `DoIpLogicAddress`                                      | [ ] Deferred| a5671c229e                               | Group20          |
| `DoIpLogicTargetAddressProps`                           | [x] Done    | 64d125ffae                               | Group7           |
| `DoIpLogicTesterAddressProps`                           | [x] Done    | 64d125ffae                               | Group7           |
| `DoIpPowerModeStatusNeeds`                              | [x] Done    | 4350642e77                               | Group5           |
| `DoIpRoutingActivation`                                 | [x] Done    | c53a7febdc                               | Group5           |
| `DoIpRoutingActivationAuthenticationNeeds`              | [ ] Pending | N/A                                      | Group29          |
| `DoIpRoutingActivationConfirmationNeeds`                | [ ] Pending | N/A                                      | Group29          |
| `DoIpRule`                                              | [ ] Deferred| ebd95cd8f9                               | Group20          |
| `DoIpServiceNeeds`                                      | [ ] Pending | N/A                                      | Group23          |
| `DoIpTpConfig`                                          | [x] Done    | ac63e581b9                               | Group7           |
| `DoIpTpConnection`                                      | [ ] Deferred| 0abdd0dba4                               | Group20          |
| `DocRevision`                                           | [ ] Pending | N/A                                      | Group21          |
| `DocumentElementScope`                                  | [ ] Pending | N/A                                      | Group36          |
| `DocumentViewSelectable`                                | [x] Done    | ba2c324b39                               | Group3           |
| `DocumentationBlock`                                    | [ ] Pending | N/A                                      | Group21          |
| `DocumentationContext`                                  | [ ] Pending | N/A                                      | Group21          |
| `DtcFormatTypeEnum`                                     | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DtcKindEnum`                                           | [ ] Deferred| 28746ce3cc                               | Group14          |
| `DtcStatusChangeNotificationNeeds`                      | [ ] Deferred| 79c639e42a                               | Group14          |
| `DynamicPart`                                           | [ ] Deferred| 4211085bc4                               | Group15          |
| `DynamicPartAlternative`                                | [x] Done    | 206cf29517                               | Group5           |
| `E2EProfileCompatibilityProps`                          | [ ] Pending | N/A                                      | Group28          |
| `ECUMapping`                                            | [x] Done    | 34bb50d75e                               | Group7           |
| `EEnum`                                                 | [ ] Pending | N/A                                      | Group21          |
| `EEnumFont`                                             | [ ] Pending | N/A                                      | Group21          |
| `EOCEventRef`                                           | [ ] Pending | N/A                                      | Group35          |
| `EOCExecutableEntityRef`                                | [ ] Pending | N/A                                      | Group35          |
| `EOCExecutableEntityRefAbstract`                        | [ ] Pending | N/A                                      | Group35          |
| `EOCExecutableEntityRefGroup`                           | [ ] Pending | N/A                                      | Group35          |
| `EcuAbstractionSwComponentType`                         | [ ] Pending | N/A                                      | Group29          |
| `EcuInstance`                                           | [x] Done    | 206e89be41                               | Group5           |
| `EcuPartition`                                          | [x] Done    | c53a7febdc                               | Group5           |
| `EcuResourceEstimation`                                 | [ ] Pending | N/A                                      | Group31          |
| `EcuStateMgrUserNeeds`                                  | [x] Done    | 6b31696dff                               | Group4           |
| `EcuTiming`                                             | [ ] Pending | N/A                                      | Group35          |
| `EcucAbstractConfigurationClass`                        | [ ] Pending | N/A                                      | Group26          |
| `EcucAbstractExternalReferenceDef`                      | [ ] Pending | N/A                                      | Group26          |
| `EcucAbstractInternalReferenceDef`                      | [ ] Pending | N/A                                      | Group26          |
| `EcucAbstractReferenceDef`                              | [ ] Pending | N/A                                      | Group26          |
| `EcucAbstractReferenceValue`                            | [ ] Pending | N/A                                      | Group27          |
| `EcucAbstractStringParamDef`                            | [ ] Pending | N/A                                      | Group26          |
| `EcucAddInfoParamDef`                                   | [ ] Pending | N/A                                      | Group26          |
| `EcucAddInfoParamValue`                                 | [ ] Pending | N/A                                      | Group27          |
| `EcucBooleanParamDef`                                   | [ ] Pending | N/A                                      | Group19          |
| `EcucChoiceContainerDef`                                | [ ] Pending | N/A                                      | Group26          |
| `EcucChoiceReferenceDef`                                | [ ] Pending | N/A                                      | Group26          |
| `EcucCommonAttributes`                                  | [ ] Pending | N/A                                      | Group26          |
| `EcucConditionFormula`                                  | [ ] Pending | N/A                                      | Group19          |
| `EcucConditionSpecification`                            | [ ] Pending | N/A                                      | Group27          |
| `EcucConfigurationClassEnum`                            | [ ] Pending | N/A                                      | Group19          |
| `EcucConfigurationVariantEnum`                          | [ ] Pending | N/A                                      | Group26          |
| `EcucContainerDef`                                      | [ ] Pending | N/A                                      | Group26          |
| `EcucContainerValue`                                    | [ ] Pending | N/A                                      | Group27          |
| `EcucDefinitionCollection`                              | [ ] Pending | N/A                                      | Group26          |
| `EcucDefinitionElement`                                 | [ ] Pending | N/A                                      | Group26          |
| `EcucDerivationSpecification`                           | [ ] Pending | N/A                                      | Group26          |
| `EcucDestinationUriDef`                                 | [ ] Pending | N/A                                      | Group26          |
| `EcucDestinationUriDefRefType`                          | [ ] Pending | N/A                                      | Group19          |
| `EcucDestinationUriDefSet`                              | [ ] Pending | N/A                                      | Group26          |
| `EcucDestinationUriNestingContractEnum`                 | [ ] Pending | N/A                                      | Group26          |
| `EcucDestinationUriPolicy`                              | [ ] Pending | N/A                                      | Group26          |
| `EcucEnumerationLiteralDef`                             | [ ] Pending | N/A                                      | Group26          |
| `EcucEnumerationParamDef`                               | [ ] Pending | N/A                                      | Group26          |
| `EcucFloatParamDef`                                     | [ ] Pending | N/A                                      | Group19          |
| `EcucForeignReferenceDef`                               | [ ] Pending | N/A                                      | Group19          |
| `EcucFunctionNameDef`                                   | [ ] Pending | N/A                                      | Group26          |
| `EcucIndexableValue`                                    | [ ] Pending | N/A                                      | Group27          |
| `EcucInstanceReferenceDef`                              | [ ] Pending | N/A                                      | Group26          |
| `EcucInstanceReferenceValue`                            | [ ] Pending | N/A                                      | Group27          |
| `EcucIntegerParamDef`                                   | [ ] Pending | N/A                                      | Group26          |
| `EcucLinkerSymbolDef`                                   | [ ] Pending | N/A                                      | Group19          |
| `EcucModuleConfigurationValues`                         | [ ] Pending | N/A                                      | Group27          |
| `EcucModuleDef`                                         | [ ] Pending | N/A                                      | Group26          |
| `EcucMultilineStringParamDef`                           | [ ] Pending | N/A                                      | Group26          |
| `EcucMultiplicityConfigurationClass`                    | [ ] Pending | N/A                                      | Group26          |
| `EcucNumericalParamValue`                               | [ ] Pending | N/A                                      | Group27          |
| `EcucParamConfContainerDef`                             | [ ] Pending | N/A                                      | Group26          |
| `EcucParameterDef`                                      | [ ] Pending | N/A                                      | Group26          |
| `EcucParameterDerivationFormula`                        | [ ] Pending | N/A                                      | Group19          |
| `EcucParameterValue`                                    | [ ] Pending | N/A                                      | Group27          |
| `EcucQuery`                                             | [ ] Pending | N/A                                      | Group26          |
| `EcucQueryExpression`                                   | [ ] Pending | N/A                                      | Group19          |
| `EcucReferenceDef`                                      | [ ] Pending | N/A                                      | Group19          |
| `EcucReferenceValue`                                    | [ ] Pending | N/A                                      | Group27          |
| `EcucScopeEnum`                                         | [ ] Pending | N/A                                      | Group19          |
| `EcucStringParamDef`                                    | [ ] Pending | N/A                                      | Group26          |
| `EcucSymbolicNameReferenceDef`                          | [ ] Pending | N/A                                      | Group19          |
| `EcucTextualParamValue`                                 | [ ] Pending | N/A                                      | Group27          |
| `EcucUriReferenceDef`                                   | [ ] Pending | N/A                                      | Group19          |
| `EcucValidationCondition`                               | [ ] Pending | N/A                                      | Group27          |
| `EcucValueCollection`                                   | [ ] Pending | N/A                                      | Group19          |
| `EcucValueConfigurationClass`                           | [ ] Pending | N/A                                      | Group26          |
| `EmphasisText`                                          | [ ] Pending | N/A                                      | Group21          |
| `EndToEndDescription`                                   | [x] Done    | d3db89bb98                               | Group10          |
| `EndToEndProfileBehaviorEnum`                           | [ ] Pending | N/A                                      | Group34          |
| `EndToEndProtection`                                    | [ ] Pending | N/A                                      | Group28          |
| `EndToEndProtectionISignalIPdu`                         | [ ] Pending | N/A                                      | Group18          |
| `EndToEndProtectionSet`                                 | [x] Done    | 4a7d82ffc7                               | Group5           |
| `EndToEndProtectionVariablePrototype`                   | [x] Done    | 4a7d82ffc7                               | Group5           |
| `EndToEndTransformationComSpecProps`                    | [ ] Pending | N/A                                      | Group28          |
| `EndToEndTransformationDescription`                     | [ ] Pending | N/A                                      | Group34          |
| `EndToEndTransformationISignalProps`                    | [ ] Pending | N/A                                      | Group18          |
| `EngineeringObject`                                     | [ ] Pending | N/A                                      | Group21          |
| `Entry`                                                 | [x] Done    | 9005f6228e                               | Group3           |
| `ErrorTracerNeeds`                                      | [ ] Pending | N/A                                      | Group23          |
| `EthGlobalTimeDomainProps`                              | [ ] Pending | N/A                                      | Group34          |
| `EthGlobalTimeManagedCouplingPort`                      | [ ] Pending | N/A                                      | Group34          |
| `EthGlobalTimeMessageFormatEnum`                        | [ ] Pending | N/A                                      | Group34          |
| `EthIpProps`                                            | [ ] Pending | N/A                                      | Group30          |
| `EthTSynCrcFlags`                                       | [ ] Pending | N/A                                      | Group34          |
| `EthTSynSubTlvConfig`                                   | [ ] Pending | N/A                                      | Group34          |
| `EthTcpIpIcmpProps`                                     | [x] Done    | c53a7febdc                               | Group5           |
| `EthTcpIpProps`                                         | [x] Done    | db98d8ff29                               | Group5           |
| `EthTpConfig`                                           | [ ] Pending | N/A                                      | Group33          |
| `EthTpConnection`                                       | [ ] Pending | N/A                                      | Group33          |
| `EthernetCluster`                                       | [ ] Pending | N/A                                      | Group29          |
| `EthernetCommunicationConnector`                        | [ ] Pending | N/A                                      | Group30          |
| `EthernetCommunicationController`                       | [ ] Pending | N/A                                      | Group30          |
| `EthernetConnectionNegotiationEnum`                     | [ ] Pending | N/A                                      | Group30          |
| `EthernetCouplingPortSchedulerEnum`                     | [ ] Pending | N/A                                      | Group30          |
| `EthernetFrameTriggering`                               | [ ] Pending | N/A                                      | Group33          |
| `EthernetMacLayerTypeEnum`                              | [ ] Pending | N/A                                      | Group30          |
| `EthernetPhysicalChannel`                               | [x] Done    | 206cf29517                               | Group5           |
| `EthernetPhysicalLayerTypeEnum`                         | [ ] Pending | N/A                                      | Group30          |
| `EthernetPriorityRegeneration`                          | [ ] Deferred| b1e4750b14                               | Group16          |
| `EthernetSwitchVlanEgressTaggingEnum`                   | [ ] Pending | N/A                                      | Group30          |
| `EthernetSwitchVlanIngressTagEnum`                      | [ ] Pending | N/A                                      | Group30          |
| `EthernetWakeupSleepOnDatalineConfig`                   | [ ] Pending | N/A                                      | Group30          |
| `EthernetWakeupSleepOnDatalineConfigSet`                | [ ] Pending | N/A                                      | Group30          |
| `EvaluatedVariantSet`                                   | [ ] Pending | N/A                                      | Group21          |
| `EventAcceptanceStatusEnum`                             | [ ] Pending | N/A                                      | Group29          |
| `EventControlledTiming`                                 | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `EventGroupControlTypeEnum`                             | [ ] Pending | N/A                                      | Group32          |
| `EventHandler`                                          | [ ] Pending | N/A                                      | Group32          |
| `EventObdReadinessGroup`                                | [ ] Pending | N/A                                      | Group25          |
| `EventOccurrenceKindEnum`                               | [ ] Pending | N/A                                      | Group35          |
| `EventTriggeringConstraint`                             | [ ] Pending | N/A                                      | Group35          |
| `ExclusiveArea`                                         | [ ] Pending | N/A                                      | Group22          |
| `ExclusiveAreaNestingOrder`                             | [ ] Pending | N/A                                      | Group22          |
| `ExecutableEntity`                                      | [ ] Pending | N/A                                      | Group22          |
| `ExecutableEntityActivationReason`                      | [ ] Pending | N/A                                      | Group28          |
| `ExecutionOrderConstraint`                              | [ ] Pending | N/A                                      | Group35          |
| `ExecutionOrderConstraintTypeEnum`                      | [ ] Pending | N/A                                      | Group35          |
| `ExecutionTime`                                         | [ ] Pending | N/A                                      | Group23          |
| `ExecutionTimeConstraint`                               | [ ] Pending | N/A                                      | Group35          |
| `ExecutionTimeTypeEnum`                                 | [ ] Pending | N/A                                      | Group35          |
| `ExternalTriggerOccurredEvent`                          | [ ] Pending | N/A                                      | Group28          |
| `ExternalTriggeringPoint`                               | [ ] Pending | N/A                                      | Group29          |
| `ExternalTriggeringPointIdent`                          | [x] Done    | c04ca0f5b3                               | Group2           |
| `FMAttributeDef`                                        | [ ] Pending | N/A                                      | Group36          |
| `FMAttributeValue`                                      | [ ] Pending | N/A                                      | Group36          |
| `FMConditionByFeaturesAndAttributes`                    | [x] Done    | d69232bdf4                               | Group8           |
| `FMConditionByFeaturesAndSwSystemconsts`                | [x] Done    | d69232bdf4                               | Group8           |
| `FMFeature`                                             | [ ] Pending | N/A                                      | Group36          |
| `FMFeatureDecomposition`                                | [ ] Pending | N/A                                      | Group36          |
| `FMFeatureMap`                                          | [ ] Pending | N/A                                      | Group36          |
| `FMFeatureMapAssertion`                                 | [ ] Pending | N/A                                      | Group36          |
| `FMFeatureMapCondition`                                 | [ ] Pending | N/A                                      | Group36          |
| `FMFeatureMapElement`                                   | [ ] Pending | N/A                                      | Group36          |
| `FMFeatureModel`                                        | [ ] Pending | N/A                                      | Group36          |
| `FMFeatureRelation`                                     | [ ] Pending | N/A                                      | Group36          |
| `FMFeatureRestriction`                                  | [ ] Pending | N/A                                      | Group36          |
| `FMFeatureSelection`                                    | [ ] Pending | N/A                                      | Group36          |
| `FMFeatureSelectionSet`                                 | [ ] Pending | N/A                                      | Group36          |
| `FMFeatureSelectionState`                               | [ ] Pending | N/A                                      | Group36          |
| `FMFormulaByFeaturesAndAttributes`                      | [x] Done    | d69232bdf4                               | Group8           |
| `FMFormulaByFeaturesAndSwSystemconsts`                  | [x] Done    | d69232bdf4                               | Group8           |
| `Field`                                                 | [ ] Deferred| 413d1a4b62                               | Group11          |
| `FileInfoComment`                                       | [x] Done    | c62e1c8943                               | Group1           |
| `FilterDebouncingEnum`                                  | [ ] Pending | N/A                                      | Group27          |
| `FirewallActionEnum`                                    | [x] Done    | ab2daa7785                               | Group3           |
| `FirewallRule`                                          | [x] Deferred| 00d011d4ad                               | Group1           |
| `FirewallRuleProps`                                     | [x] Done    | 89039bf2bb                               | Group7           |
| `FlatInstanceDescriptor`                                | [x] Done    | 9db34796eb                               | Group1           |
| `FlatMap`                                               | [x] Done    | 5eadca7853                               | Group1           |
| `FlexrayAbsolutelyScheduledTiming`                      | [ ] Deferred| N/A                                      | Group17          |
| `FlexrayArTpChannel`                                    | [ ] Pending | N/A                                      | Group33          |
| `FlexrayArTpConfig`                                     | [ ] Pending | N/A                                      | Group33          |
| `FlexrayArTpConnection`                                 | [ ] Pending | N/A                                      | Group33          |
| `FlexrayArTpNode`                                       | [ ] Pending | N/A                                      | Group33          |
| `FlexrayChannelName`                                    | [ ] Deferred| 7c137656f6                               | Group15          |
| `FlexrayCluster`                                        | [ ] Pending | N/A                                      | Group29          |
| `FlexrayCommunicationConnector`                         | [ ] Deferred| N/A                                      | Group17          |
| `FlexrayCommunicationController`                        | [ ] Deferred| N/A                                      | Group17          |
| `FlexrayFifoConfiguration`                              | [ ] Pending | N/A                                      | Group29          |
| `FlexrayFifoRange`                                      | [ ] Pending | N/A                                      | Group29          |
| `FlexrayFrame`                                          | [x] Done    | 757aea1d17                               | Group6           |
| `FlexrayFrameTriggering`                                | [ ] Deferred| N/A                                      | Group17          |
| `FlexrayNmCluster`                                      | [x] Done    | 9c8e10b37f                               | Group6           |
| `FlexrayNmClusterCoupling`                              | [ ] Pending | N/A                                      | Group18          |
| `FlexrayNmEcu`                                          | [x] Done    | 9c8e10b37f                               | Group6           |
| `FlexrayNmNode`                                         | [x] Done    | 9c8e10b37f                               | Group6           |
| `FlexrayNmScheduleVariant`                              | [ ] Pending | N/A                                      | Group33          |
| `FlexrayPhysicalChannel`                                | [ ] Deferred| N/A                                      | Group17          |
| `FlexrayTpConfig`                                       | [ ] Pending | N/A                                      | Group33          |
| `FlexrayTpConnection`                                   | [ ] Pending | N/A                                      | Group33          |
| `FlexrayTpConnectionControl`                            | [ ] Pending | N/A                                      | Group33          |
| `FlexrayTpEcu`                                          | [ ] Pending | N/A                                      | Group33          |
| `FlexrayTpNode`                                         | [ ] Pending | N/A                                      | Group33          |
| `FlexrayTpPduPool`                                      | [ ] Pending | N/A                                      | Group33          |
| `FloatEnum`                                             | [ ] Pending | N/A                                      | Group22          |
| `FloatValueVariationPoint`                              | [x] Done    | d5c96fd954                               | Group8           |
| `FlowMeteringColorModeEnum`                             | [ ] Pending | N/A                                      | Group30          |
| `ForbiddenSignalPath`                                   | [ ] Pending | N/A                                      | Group31          |
| `FormulaExpression`                                     | [x] Done    | 88ed82bed3                               | Group8           |
| `FrArTpAckType`                                         | [ ] Pending | N/A                                      | Group33          |
| `FrGlobalTimeDomainProps`                               | [ ] Pending | N/A                                      | Group34          |
| `Frame`                                                 | [ ] Pending | N/A                                      | Group31          |
| `FrameEnum`                                             | [x] Done    | 531991e029                               | Group3           |
| `FrameMapping`                                          | [ ] Deferred| N/A                                      | Group17          |
| `FramePid`                                              | [ ] Pending | N/A                                      | Group31          |
| `FramePort`                                             | [x] Done    | 75683a2ede                               | Group5           |
| `FrameTriggering`                                       | [x] Done    | 206cf29517                               | Group5           |
| `FreeFormat`                                            | [ ] Pending | N/A                                      | Group32          |
| `FreeFormatEntry`                                       | [ ] Pending | N/A                                      | Group31          |
| `FullBindingTimeEnum`                                   | [ ] Pending | N/A                                      | Group21          |
| `FunctionInhibitionAvailabilityNeeds`                   | [ ] Pending | N/A                                      | Group29          |
| `FunctionInhibitionNeeds`                               | [x] Done    | 5c4c0963af                               | Group4           |
| `FurtherActionByteNeeds`                                | [x] Done    | 30e266fd91                               | Group5           |
| `Gateway`                                               | [ ] Deferred| N/A                                      | Group17          |
| `GeneralAnnotation`                                     | [x] Done    | ab2daa7785                               | Group3           |
| `GeneralParameter`                                      | [x] Done    | b622d5b424                               | Group9           |
| `GeneralPurposeConnection`                              | [ ] Pending | N/A                                      | Group31          |
| `GeneralPurposeIPdu`                                    | [x] Done    | 75683a2ede                               | Group5           |
| `GeneralPurposePdu`                                     | [x] Done    | 75683a2ede                               | Group5           |
| `GenericEthernetFrame`                                  | [x] Done    | 675a97e967                               | Group6           |
| `GenericTp`                                             | [ ] Deferred| N/A                                      | Group16          |
| `GlobalSupervisionNeeds`                                | [x] Done    | 5c4c0963af                               | Group4           |
| `GlobalTimeCanMaster`                                   | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimeCanSlave`                                    | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimeCorrectionProps`                             | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimeCouplingPortProps`                           | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimeCrcSupportEnum`                              | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimeCrcValidationEnum`                           | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimeDomain`                                      | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimeEthMaster`                                   | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimeEthSlave`                                    | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimeFrMaster`                                    | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimeFrSlave`                                     | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimeGateway`                                     | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimeIcvSupportEnum`                              | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimeIcvVerificationEnum`                         | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimeMaster`                                      | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimePortRoleEnum`                                | [ ] Pending | N/A                                      | Group34          |
| `GlobalTimeSlave`                                       | [ ] Pending | N/A                                      | Group34          |
| `Graphic`                                               | [x] Done    | 06b46f32ba                               | Group3           |
| `GraphicFitEnum`                                        | [x] Done    | 5b543a21d4                               | Group3           |
| `GraphicNotationEnum`                                   | [x] Done    | f25e765d8b                               | Group3           |
| `HandleInvalidEnum`                                     | [x] Done    | 18271ddd84                               | Group1           |
| `HandleOutOfRangeEnum`                                  | [ ] Pending | N/A                                      | Group27          |
| `HandleOutOfRangeStatusEnum`                            | [ ] Pending | N/A                                      | Group27          |
| `HandleTimeoutEnum`                                     | [ ] Pending | N/A                                      | Group27          |
| `HardwareConfiguration`                                 | [ ] Deferred| 35bfb17b7a                               | Group20          |
| `HardwareTestNeeds`                                     | [x] Done    | 5c4c0963af                               | Group4           |
| `HeapUsage`                                             | [ ] Pending | N/A                                      | Group22          |
| `HttpTp`                                                | [ ] Pending | N/A                                      | Group32          |
| `HwAttributeDef`                                        | [x] Done    | 3912963bfd                               | Group7           |
| `HwAttributeLiteralDef`                                 | [x] Done    | 5d767ace9e                               | Group7           |
| `HwAttributeValue`                                      | [x] Done    | 269d34d90f                               | Group7           |
| `HwCategory`                                            | [x] Done    | b7e2199ac8                               | Group7           |
| `HwDescriptionEntity`                                   | [ ] Pending | N/A                                      | Group27          |
| `HwElement`                                             | [x] Done    | 8c7f05d40a                               | Group1           |
| `HwElementConnector`                                    | [ ] Pending | N/A                                      | Group27          |
| `HwPin`                                                 | [x] Done    | ff5b0e0865                               | Group1           |
| `HwPinConnector`                                        | [ ] Pending | N/A                                      | Group27          |
| `HwPinGroup`                                            | [x] Done    | 69afffcc48                               | Group1           |
| `HwPinGroupConnector`                                   | [ ] Pending | N/A                                      | Group27          |
| `HwPinGroupContent`                                     | [ ] Pending | N/A                                      | Group27          |
| `HwPortMapping`                                         | [x] Done    | 7d94510497                               | Group7           |
| `HwType`                                                | [x] Done    | 29f338b3c0                               | Group1           |
| `IEEE1722TpAafAes3DataTypeEnum`                         | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpAafConnection`                               | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpAafFormatEnum`                               | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpAafNominalRateEnum`                          | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpAcfBus`                                      | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpAcfBusPart`                                  | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpAcfCan`                                      | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpAcfCanMessageTypeEnum`                       | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpAcfCanPart`                                  | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpAcfConnection`                               | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpAcfLin`                                      | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpAcfLinPart`                                  | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpAvConnection`                                | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpConfig`                                      | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpConnection`                                  | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpCrfConnection`                               | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpCrfPullEnum`                                 | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpCrfTypeEnum`                                 | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpIidcConnection`                              | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpRvfColorSpaceEnum`                           | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpRvfConnection`                               | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpRvfFrameRateEnum`                            | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpRvfPixelDepthEnum`                           | [ ] Pending | N/A                                      | Group33          |
| `IEEE1722TpRvfPixelFormatEnum`                          | [ ] Pending | N/A                                      | Group33          |
| `IPSecConfig`                                           | [ ] Pending | 6c97ddc108                               | Group16          |
| `IPSecConfigProps`                                      | [ ] Pending | N/A                                      | Group32          |
| `IPSecRule`                                             | [ ] Pending | N/A                                      | Group32          |
| `IPdu`                                                  | [ ] Pending | N/A                                      | Group31          |
| `IPduMapping`                                           | [x] Done    | 9c8e10b37f                               | Group6           |
| `IPduPort`                                              | [ ] Pending | N/A                                      | Group31          |
| `IPduSignalProcessingEnum`                              | [ ] Pending | N/A                                      | Group31          |
| `IPduTiming`                                            | [ ] Pending | N/A                                      | Group31          |
| `IPsecDpdActionEnum`                                    | [ ] Pending | N/A                                      | Group33          |
| `IPsecHeaderTypeEnum`                                   | [ ] Pending | N/A                                      | Group33          |
| `IPsecIpProtocolEnum`                                   | [ ] Pending | N/A                                      | Group32          |
| `IPsecModeEnum`                                         | [ ] Pending | N/A                                      | Group32          |
| `IPsecPolicyEnum`                                       | [ ] Pending | N/A                                      | Group32          |
| `IPv6ExtHeaderFilterList`                               | [ ] Deferred| 2d5b3256b4                               | Group16          |
| `IPv6ExtHeaderFilterSet`                                | [ ] Pending | N/A                                      | Group32          |
| `ISignal`                                               | [ ] Pending | N/A                                      | Group31          |
| `ISignalGroup`                                          | [ ] Pending | N/A                                      | Group31          |
| `ISignalIPdu`                                           | [ ] Pending | N/A                                      | Group31          |
| `ISignalIPduGroup`                                      | [ ] Deferred| 1e758bd44e                               | Group15          |
| `ISignalMapping`                                        | [ ] Deferred| N/A                                      | Group17          |
| `ISignalPort`                                           | [ ] Deferred| b5f92f4b28                               | Group15          |
| `ISignalProps`                                          | [ ] Pending | N/A                                      | Group31          |
| `ISignalToIPduMapping`                                  | [ ] Pending | N/A                                      | Group31          |
| `ISignalTriggering`                                     | [ ] Pending | N/A                                      | Group31          |
| `ISignalTypeEnum`                                       | [ ] Pending | N/A                                      | Group31          |
| `IcmpRule`                                              | [x] Deferred| 5ddaf1cf94                               | Group20          |
| `IdentCaption`                                          | [x] Done    | 2dd2f91845                               | Group1           |
| `Identifiable`                                          | [x] Done    | c17bfbf60f                               | Group1           |
| `Identifier`                                            | [ ] Pending | N/A                                      | Group21          |
| `IdsDesign`                                             | [ ] Pending | N/A                                      | Group36          |
| `IdsMgrCustomTimestampNeeds`                            | [x] Done    | b65fe94222                               | Group5           |
| `IdsMgrNeeds`                                           | [ ] Pending | N/A                                      | Group29          |
| `IdsPlatformInstantiation`                              | [x] Done    | 5d4cc1c454                               | Group7           |
| `IdsmInstance`                                          | [ ] Pending | N/A                                      | Group36          |
| `IdsmModuleInstantiation`                               | [x] Done    | 5d4cc1c454                               | Group7           |
| `IdsmRateLimitation`                                    | [ ] Pending | N/A                                      | Group36          |
| `IdsmTrafficLimitation`                                 | [ ] Pending | N/A                                      | Group36          |
| `Ieee1722Tp`                                            | [ ] Pending | N/A                                      | Group32          |
| `Ieee1722TpEthernetFrame`                               | [ ] Pending | N/A                                      | Group33          |
| `Implementation`                                        | [x] Done    | e7dfb875d9                               | Group1           |
| `ImplementationDataType`                                | [ ] Pending | N/A                                      | Group28          |
| `ImplementationDataTypeElement`                         | [x] Done    | 8e9b2db86b                               | Group10          |
| `ImplementationDataTypeElementInPortInterfaceRef`       | [ ] Pending | N/A                                      | Group34          |
| `ImplementationDataTypeSubElementRef`                   | [ ] Pending | N/A                                      | Group27          |
| `ImplementationElementInParameterInstanceRef`           | [ ] Pending | N/A                                      | Group23          |
| `ImplementationProps`                                   | [x] Done    | 3166f6e5d0                               | Group10          |
| `IncludedDataTypeSet`                                   | [ ] Pending | N/A                                      | Group29          |
| `IncludedModeDeclarationGroupSet`                       | [x] Done    | b9ac782d1e                               | Group2           |
| `IndentSample`                                          | [ ] Pending | N/A                                      | Group21          |
| `IndexEntry`                                            | [ ] Pending | N/A                                      | Group21          |
| `IndexedArrayElement`                                   | [ ] Deferred| N/A                                      | Group17          |
| `IndicatorStatusNeeds`                                  | [ ] Pending | N/A                                      | Group29          |
| `InfrastructureServices`                                | [ ] Pending | N/A                                      | Group32          |
| `InitEvent`                                             | [x] Done    | 64ab725d50                               | Group2           |
| `InitialSdDelayConfig`                                  | [ ] Deferred| d7240be740                               | Group16          |
| `InnerPortGroupInCompositionInstanceRef`                | [x] Done    | 919fbc0d11                               | Group2           |
| `InstantiationDataDefProps`                             | [x] Done    | e2aa88eb41                               | Group10          |
| `InstantiationRTEEventProps`                            | [ ] Pending | N/A                                      | Group27          |
| `InstantiationTimingEventProps`                         | [ ] Pending | N/A                                      | Group27          |
| `IntegerValueVariationPoint`                            | [x] Done    | d5c96fd954                               | Group8           |
| `InternalBehavior`                                      | [ ] Pending | N/A                                      | Group22          |
| `InternalConstrs`                                       | [ ] Pending | N/A                                      | Group28          |
| `InternalTriggerOccurredEvent`                          | [ ] Deferred| N/A                                      | Group12          |
| `InternalTriggeringPoint`                               | [ ] Deferred| N/A                                      | Group12          |
| `InterpolationRoutine`                                  | [x] Done    | 992a894be3                               | Group5           |
| `InterpolationRoutineMapping`                           | [x] Done    | d00d57b42d                               | Group5           |
| `InterpolationRoutineMappingSet`                        | [x] Done    | f3152abb23                               | Group5           |
| `IntervalTypeEnum`                                      | [ ] Pending | N/A                                      | Group28          |
| `InvalidationPolicy`                                    | [x] Done    | 1000053d88                               | Group1           |
| `InvertCondition`                                       | [ ] Pending | N/A                                      | Group36          |
| `IoHwAbstractionServerAnnotation`                       | [ ] Pending | N/A                                      | Group27          |
| `Ip4AddressString`                                      | [ ] Pending | N/A                                      | Group21          |
| `Ip6AddressString`                                      | [ ] Pending | N/A                                      | Group21          |
| `IpAddressKeepEnum`                                     | [ ] Deferred| c5bb322323                               | Group16          |
| `Ipv4AddressSourceEnum`                                 | [ ] Deferred| 6c97ddc108                               | Group16          |
| `Ipv4ArpProps`                                          | [ ] Pending | N/A                                      | Group30          |
| `Ipv4AutoIpProps`                                       | [ ] Pending | N/A                                      | Group30          |
| `Ipv4Configuration`                                     | [ ] Deferred| 6c97ddc108                               | Group16          |
| `Ipv4DhcpServerConfiguration`                           | [ ] Pending | N/A                                      | Group30          |
| `Ipv4FragmentationProps`                                | [ ] Pending | N/A                                      | Group30          |
| `Ipv4Props`                                             | [ ] Pending | N/A                                      | Group30          |
| `Ipv4Rule`                                              | [x] Deferred| b4096068d6                               | Group20          |
| `Ipv6AddressSourceEnum`                                 | [ ] Deferred| c5bb322323                               | Group16          |
| `Ipv6Configuration`                                     | [ ] Pending | N/A                                      | Group32          |
| `Ipv6DhcpServerConfiguration`                           | [ ] Pending | N/A                                      | Group30          |
| `Ipv6FragmentationProps`                                | [ ] Pending | N/A                                      | Group30          |
| `Ipv6NdpProps`                                          | [ ] Pending | N/A                                      | Group30          |
| `Ipv6Props`                                             | [ ] Pending | N/A                                      | Group30          |
| `Ipv6Rule`                                              | [x] Deferred| 18ee06b97c                               | Group20          |
| `Item`                                                  | [x] Done    | cf8b43c369                               | Group9           |
| `ItemLabelPosEnum`                                      | [ ] Pending | N/A                                      | Group21          |
| `J1939Cluster`                                          | [x] Done    | 44a70c3256                               | Group5           |
| `J1939ControllerApplication`                            | [ ] Pending | N/A                                      | Group30          |
| `J1939ControllerApplicationToJ1939NmNodeMapping`        | [ ] Pending | N/A                                      | Group30          |
| `J1939DcmDm19Support`                                   | [x] Done    | 839c29d67e                               | Group5           |
| `J1939DcmIPdu`                                          | [ ] Pending | N/A                                      | Group31          |
| `J1939NmAddressConfigurationCapabilityEnum`             | [ ] Pending | N/A                                      | Group33          |
| `J1939NmCluster`                                        | [x] Done    | 9c8e10b37f                               | Group6           |
| `J1939NmEcu`                                            | [x] Done    | 9c8e10b37f                               | Group6           |
| `J1939NmNode`                                           | [ ] Pending | N/A                                      | Group33          |
| `J1939NodeName`                                         | [ ] Pending | N/A                                      | Group33          |
| `J1939RmIncomingRequestServiceNeeds`                    | [x] Done    | 9784766a6d                               | Group5           |
| `J1939RmOutgoingRequestServiceNeeds`                    | [x] Done    | 2b39e92976                               | Group5           |
| `J1939SharedAddressCluster`                             | [x] Done    | d3dc82098e                               | Group5           |
| `J1939TpConfig`                                         | [ ] Pending | N/A                                      | Group33          |
| `J1939TpConnection`                                     | [ ] Pending | N/A                                      | Group33          |
| `J1939TpNode`                                           | [ ] Pending | N/A                                      | Group33          |
| `J1939TpPg`                                             | [ ] Pending | N/A                                      | Group33          |
| `KeepWithPreviousEnum`                                  | [x] Done    | d447cf2a51                               | Group3           |
| `Keyword`                                               | [x] Done    | 4ed5a2fe2d                               | Group7           |
| `KeywordSet`                                            | [x] Done    | a6a1d31ccc                               | Group7           |
| `LEnum`                                                 | [ ] Pending | N/A                                      | Group22          |
| `LGraphic`                                              | [x] Done    | e4b1acf6c9                               | Group3           |
| `LLongName`                                             | [ ] Pending | N/A                                      | Group21          |
| `LOverviewParagraph`                                    | [x] Done    | 764ef1c589                               | Group9           |
| `LParagraph`                                            | [x] Done    | 7fa4a01f74                               | Group3           |
| `LPlainText`                                            | [x] Done    | 1de91de480                               | Group9           |
| `LVerbatim`                                             | [x] Done    | d616f3d1ef                               | Group9           |
| `LabeledItem`                                           | [ ] Pending | N/A                                      | Group21          |
| `LabeledList`                                           | [ ] Pending | N/A                                      | Group21          |
| `LanguageSpecific`                                      | [ ] Pending | N/A                                      | Group22          |
| `LatencyConstraintTypeEnum`                             | [ ] Pending | N/A                                      | Group35          |
| `LatencyTimingConstraint`                               | [ ] Pending | N/A                                      | Group35          |
| `LetDataExchangeParadigmEnum`                           | [ ] Pending | N/A                                      | Group35          |
| `LifeCycleInfo`                                         | [x] Done    | 5836e6eb08                               | Group8           |
| `LifeCycleInfoSet`                                      | [x] Done    | 11bd9cd848                               | Group8           |
| `LifeCyclePeriod`                                       | [x] Done    | b572582c11                               | Group8           |
| `LifeCycleState`                                        | [ ] Pending | N/A                                      | Group22          |
| `LifeCycleStateDefinitionGroup`                         | [ ] Pending | N/A                                      | Group22          |
| `Limit`                                                 | [ ] Pending | N/A                                      | Group28          |
| `LimitValueVariationPoint`                              | [x] Done    | d5c96fd954                               | Group8           |
| `LinChecksumType`                                       | [ ] Pending | N/A                                      | Group31          |
| `LinCluster`                                            | [ ] Pending | N/A                                      | Group29          |
| `LinCommunicationConnector`                             | [ ] Deferred| N/A                                      | Group17          |
| `LinCommunicationController`                            | [ ] Pending | N/A                                      | Group29          |
| `LinConfigurableFrame`                                  | [ ] Pending | N/A                                      | Group29          |
| `LinConfigurationEntry`                                 | [ ] Pending | N/A                                      | Group31          |
| `LinErrorResponse`                                      | [ ] Pending | N/A                                      | Group29          |
| `LinEventTriggeredFrame`                                | [ ] Pending | N/A                                      | Group31          |
| `LinFrame`                                              | [ ] Pending | N/A                                      | Group31          |
| `LinFrameTriggering`                                    | [ ] Pending | N/A                                      | Group31          |
| `LinMaster`                                             | [ ] Pending | N/A                                      | Group29          |
| `LinOrderedConfigurableFrame`                           | [ ] Pending | N/A                                      | Group29          |
| `LinPhysicalChannel`                                    | [ ] Pending | N/A                                      | Group29          |
| `LinScheduleTable`                                      | [ ] Deferred| N/A                                      | Group17          |
| `LinSlave`                                              | [ ] Pending | N/A                                      | Group29          |
| `LinSlaveConfig`                                        | [ ] Pending | N/A                                      | Group29          |
| `LinSlaveConfigIdent`                                   | [ ] Pending | N/A                                      | Group29          |
| `LinSporadicFrame`                                      | [ ] Pending | N/A                                      | Group31          |
| `LinTpConfig`                                           | [ ] Pending | N/A                                      | Group33          |
| `LinTpConnection`                                       | [ ] Pending | N/A                                      | Group18          |
| `LinTpNode`                                             | [ ] Pending | N/A                                      | Group33          |
| `LinUnconditionalFrame`                                 | [ ] Pending | N/A                                      | Group31          |
| `Linker`                                                | [x] Done    | 20003dc3cc                               | Group1           |
| `List`                                                  | [ ] Pending | N/A                                      | Group21          |
| `ListEnum`                                              | [x] Done    | 0623068af8                               | Group9           |
| `LogAndTraceMessageCollectionSet`                       | [ ] Pending | N/A                                      | Group36          |
| `LogTraceDefaultLogLevelEnum`                           | [x] Done    | f1eb819e47                               | Group5           |
| `MacAddressString`                                      | [x] Deferred| 1fd0b00607                               | Group20          |
| `MacMulticastConfiguration`                             | [ ] Pending | N/A                                      | Group32          |
| `MacMulticastGroup`                                     | [ ] Deferred| b1e4750b14                               | Group16          |
| `MacSecCapabilityEnum`                                  | [ ] Pending | N/A                                      | Group30          |
| `MacSecCipherSuiteConfig`                               | [ ] Pending | N/A                                      | Group30          |
| `MacSecConfidentialityOffsetEnum`                       | [ ] Pending | N/A                                      | Group30          |
| `MacSecCryptoAlgoConfig`                                | [ ] Pending | N/A                                      | Group30          |
| `MacSecFailPermissiveModeEnum`                          | [ ] Pending | N/A                                      | Group30          |
| `MacSecGlobalKayProps`                                  | [ ] Pending | N/A                                      | Group30          |
| `MacSecKayParticipant`                                  | [ ] Pending | N/A                                      | Group30          |
| `MacSecLocalKayProps`                                   | [ ] Pending | N/A                                      | Group30          |
| `MacSecParticipantSet`                                  | [ ] Pending | N/A                                      | Group30          |
| `MacSecProps`                                           | [ ] Pending | N/A                                      | Group30          |
| `MacSecRoleEnum`                                        | [ ] Pending | N/A                                      | Group30          |
| `Map`                                                   | [x] Done    | 43ec8ade8c                               | Group3           |
| `MappingConstraint`                                     | [ ] Pending | N/A                                      | Group30          |
| `MappingDirectionEnum`                                  | [ ] Pending | N/A                                      | Group27          |
| `MappingScopeEnum`                                      | [ ] Pending | N/A                                      | Group30          |
| `MaxCommModeEnum`                                       | [ ] Pending | N/A                                      | Group23          |
| `MaximumMessageLengthType`                              | [ ] Pending | N/A                                      | Group33          |
| `McDataAccessDetails`                                   | [ ] Pending | N/A                                      | Group23          |
| `McDataInstance`                                        | [ ] Pending | N/A                                      | Group23          |
| `McFunction`                                            | [ ] Pending | N/A                                      | Group23          |
| `McFunctionDataRefSet`                                  | [ ] Pending | N/A                                      | Group23          |
| `McGroup`                                               | [ ] Pending | N/A                                      | Group23          |
| `McGroupDataRefSet`                                     | [ ] Pending | N/A                                      | Group23          |
| `McParameterElementGroup`                               | [ ] Pending | N/A                                      | Group23          |
| `McSupportData`                                         | [ ] Pending | N/A                                      | Group23          |
| `McSwEmulationMethodSupport`                            | [ ] Pending | N/A                                      | Group23          |
| `McdIdentifier`                                         | [ ] Pending | N/A                                      | Group21          |
| `MeasuredExecutionTime`                                 | [ ] Pending | N/A                                      | Group23          |
| `MeasuredHeapUsage`                                     | [ ] Pending | N/A                                      | Group23          |
| `MeasuredStackUsage`                                    | [ ] Deferred| adc2e5eeb7                               | Group20          |
| `MemoryAllocationKeywordPolicyType`                     | [ ] Pending | N/A                                      | Group22          |
| `MemorySection`                                         | [ ] Deferred| a579a3592e                               | Group20          |
| `MemorySectionLocation`                                 | [ ] Pending | N/A                                      | Group23          |
| `MemorySectionType`                                     | [ ] Pending | N/A                                      | Group22          |
| `MetaDataItem`                                          | [x] Done    | e69a025254                               | Group2           |
| `MetaDataItemSet`                                       | [x] Done    | e69a025254                               | Group2           |
| `MimeTypeString`                                        | [x] Done    | 01cc23df4e                               | Group3           |
| `MirroringProtocolEnum`                                 | [ ] Pending | N/A                                      | Group33          |
| `MixedContentForLongName`                               | [ ] Pending | N/A                                      | Group21          |
| `MixedContentForOverviewParagraph`                      | [x] Done    | 18b494eba5                               | Group8           |
| `MixedContentForParagraph`                              | [x] Done    | bf9114cb01                               | Group3           |
| `MixedContentForPlainText`                              | [x] Done    | 4a95d1d305                               | Group8           |
| `MixedContentForUnitNames`                              | [x] Done    | 3d47eb65c8                               | Group8           |
| `MixedContentForVerbatim`                               | [x] Done    | 74549e6a51                               | Group8           |
| `MlFigure`                                              | [x] Done    | 9225ed1572                               | Group3           |
| `MlFormula`                                             | [ ] Pending | N/A                                      | Group21          |
| `ModeAccessPoint`                                       | [ ] Deferred| N/A                                      | Group12          |
| `ModeAccessPointIdent`                                  | [x] Done    | 918013a6ce                               | Group1           |
| `ModeActivationKind`                                    | [x] Done    | 1625966930                               | Group11          |
| `ModeDeclaration`                                       | [ ] Pending | N/A                                      | Group22          |
| `ModeDeclarationGroup`                                  | [ ] Pending | N/A                                      | Group22          |
| `ModeDeclarationGroupPrototype`                         | [x] Done    | 51f2e1155f                               | Group1           |
| `ModeDeclarationGroupPrototypeMapping`                  | [x] Done    | 96e9f073a2                               | Group11          |
| `ModeDeclarationMapping`                                | [ ] Pending | N/A                                      | Group27          |
| `ModeDeclarationMappingSet`                             | [x] Done    | eeec29b637                               | Group1           |
| `ModeDrivenTransmissionModeCondition`                   | [x] Done    | 206cf29517                               | Group5           |
| `ModeErrorBehavior`                                     | [ ] Pending | N/A                                      | Group22          |
| `ModeErrorReactionPolicyEnum`                           | [ ] Pending | N/A                                      | Group22          |
| `ModeGroupInAtomicSwcInstanceRef`                       | [ ] Deferred| 74e821ccb8                               | Group11          |
| `ModeInBswInstanceRef`                                  | [ ] Pending | N/A                                      | Group35          |
| `ModeInSwcBswInstanceRef`                               | [x] Done    | 71ca6a5415                               | Group8           |
| `ModeInSwcInstanceRef`                                  | [x] Done    | 70dcc26975                               | Group8           |
| `ModeInterfaceMapping`                                  | [ ] Deferred| 8832375592                               | Group11          |
| `ModePortAnnotation`                                    | [ ] Pending | N/A                                      | Group27          |
| `ModeRequestTypeMap`                                    | [x] Done    | 2b824ca5f8                               | Group11          |
| `ModeSwitchEventTriggeredActivity`                      | [x] Done    | 8fa7710539                               | Group10          |
| `ModeSwitchInterface`                                   | [ ] Pending | N/A                                      | Group27          |
| `ModeSwitchPoint`                                       | [ ] Deferred| N/A                                      | Group12          |
| `ModeSwitchReceiverComSpec`                             | [x] Done    | 67324d240c                               | Group10          |
| `ModeSwitchSenderComSpec`                               | [x] Done    | 3fbf07cc78                               | Group10          |
| `ModeSwitchedAckEvent`                                  | [ ] Pending | N/A                                      | Group28          |
| `ModeSwitchedAckRequest`                                | [x] Done    | f587d873eb                               | Group10          |
| `ModeTransition`                                        | [ ] Pending | N/A                                      | Group22          |
| `Modification`                                          | [x] Done    | 008307967e                               | Group9           |
| `ModuleConfiguration`                                   | [ ] Pending | N/A                                      | Group19          |
| `MonotonyEnum`                                          | [ ] Pending | N/A                                      | Group28          |
| `MsrQueryArg`                                           | [ ] Pending | N/A                                      | Group22          |
| `MsrQueryChapter`                                       | [x] Done    | 50103018c3                               | Group3           |
| `MsrQueryP1`                                            | [x] Done    | 8da723c461                               | Group3           |
| `MsrQueryProps`                                         | [ ] Pending | N/A                                      | Group22          |
| `MsrQueryResultChapter`                                 | [x] Done    | fb505d3551                               | Group3           |
| `MsrQueryResultTopic1`                                  | [x] Done    | 09314bd3ad                               | Group3           |
| `MsrQueryTopic1`                                        | [x] Done    | a09f0cdfbf                               | Group3           |
| `MultiLanguageOverviewParagraph`                        | [ ] Pending | N/A                                      | Group22          |
| `MultiLanguageParagraph`                                | [x] Done    | 77074563dc                               | Group3           |
| `MultiLanguagePlainText`                                | [ ] Pending | N/A                                      | Group22          |
| `MultiLanguageVerbatim`                                 | [ ] Pending | N/A                                      | Group21          |
| `MultidimensionalTime`                                  | [x] Done    | b572582c11                               | Group8           |
| `MultilanguageLongName`                                 | [x] Done    | 87855dea47                               | Group3           |
| `MultilanguageReferrable`                               | [x] Done    | 7c7157a02b                               | Group1           |
| `MultiplexedIPdu`                                       | [ ] Deferred| eba346cb51                               | Group15          |
| `MultiplexedPart`                                       | [ ] Deferred| 66512d0602                               | Group15          |
| `MultiplicityRestrictionWithSeverity`                   | [ ] Pending | N/A                                      | Group36          |
| `NPdu`                                                  | [ ] Pending | N/A                                      | Group31          |
| `NameTokens`                                            | [x] Done    | c8a3ff507d                               | Group3           |
| `NativeDeclarationString`                               | [ ] Pending | N/A                                      | Group21          |
| `NetworkEndpoint`                                       | [ ] Deferred| 6c97ddc108                               | Group16          |
| `NetworkEndpointAddress`                                | [x] Done    | c052de0226                               | Group6           |
| `NetworkLayerRule`                                      | [ ] Deferred| 529858d9c9                               | Group20          |
| `NetworkSegmentIdentification`                          | [ ] Pending | N/A                                      | Group34          |
| `NetworkTargetAddressType`                              | [ ] Pending | N/A                                      | Group33          |
| `NmCluster`                                             | [x] Done    | ae48471063                               | Group6           |
| `NmClusterCoupling`                                     | [x] Done    | 9c8e10b37f                               | Group6           |
| `NmConfig`                                              | [x] Done    | 757aea1d17                               | Group6           |
| `NmCoordinator`                                         | [ ] Pending | N/A                                      | Group33          |
| `NmCoordinatorRoleEnum`                                 | [ ] Pending | N/A                                      | Group33          |
| `NmEcu`                                                 | [ ] Pending | N/A                                      | Group18          |
| `NmNode`                                                | [ ] Pending | N/A                                      | Group33          |
| `NmPdu`                                                 | [ ] Pending | N/A                                      | Group31          |
| `NonqueuedReceiverComSpec`                              | [ ] Pending | N/A                                      | Group27          |
| `NonqueuedSenderComSpec`                                | [ ] Pending | N/A                                      | Group27          |
| `NotAvailableValueSpecification`                        | [ ] Pending | N/A                                      | Group28          |
| `Note`                                                  | [ ] Pending | N/A                                      | Group21          |
| `NoteTypeEnum`                                          | [ ] Pending | N/A                                      | Group21          |
| `NumericalOrText`                                       | [ ] Pending | N/A                                      | Group28          |
| `NumericalRuleBasedValueSpecification`                  | [ ] Pending | N/A                                      | Group28          |
| `NumericalValueSpecification`                           | [x] Done    | b16a369151                               | Group9           |
| `NumericalValueVariationPoint`                          | [x] Done    | d5c96fd954                               | Group8           |
| `NvBlockDataMapping`                                    | [x] Done    | cf9621f708                               | Group10          |
| `NvBlockDescriptor`                                     | [x] Done    | e5d43e9b06                               | Group10          |
| `NvBlockNeeds`                                          | [x] Done    | 72d998faaa                               | Group10          |
| `NvBlockNeedsReliabilityEnum`                           | [x] Done    | 90b381db32                               | Group10          |
| `NvBlockNeedsWritingPriorityEnum`                       | [x] Done    | 5a36c87687                               | Group10          |
| `NvBlockSwComponentType`                                | [ ] Pending | N/A                                      | Group29          |
| `NvDataInterface`                                       | [x] Done    | 1d666bc11b                               | Group1           |
| `NvDataPortAnnotation`                                  | [ ] Pending | N/A                                      | Group27          |
| `NvProvideComSpec`                                      | [x] Done    | a5c437cc82                               | Group10          |
| `NvRequireComSpec`                                      | [x] Done    | cbdf05b372                               | Group10          |
| `ObdControlServiceNeeds`                                | [ ] Pending | N/A                                      | Group29          |
| `ObdInfoServiceNeeds`                                   | [ ] Pending | N/A                                      | Group29          |
| `ObdMonitorServiceNeeds`                                | [ ] Pending | N/A                                      | Group29          |
| `ObdPidServiceNeeds`                                    | [ ] Pending | N/A                                      | Group29          |
| `ObdRatioConnectionKindEnum`                            | [ ] Pending | N/A                                      | Group29          |
| `ObdRatioDenominatorNeeds`                              | [ ] Pending | N/A                                      | Group29          |
| `ObdRatioServiceNeeds`                                  | [ ] Pending | N/A                                      | Group29          |
| `OffsetTimingConstraint`                                | [x] Done    | e305e80e2a                               | Group8           |
| `OperationCycleTypeEnum`                                | [ ] Pending | N/A                                      | Group29          |
| `OperationInAtomicSwcInstanceRef`                       | [ ] Deferred| 74e821ccb8                               | Group11          |
| `OperationInSystemInstanceRef`                          | [x] Done    | 4e0c3cbe68                               | Group5           |
| `OperationInvokedEvent`                                 | [ ] Deferred| N/A                                      | Group12          |
| `OrderedMaster`                                         | [x] Done    | 5d62450236                               | Group6           |
| `OrientEnum`                                            | [x] Done    | 9223f504b5                               | Group3           |
| `OsTaskExecutionEvent`                                  | [ ] Pending | N/A                                      | Group28          |
| `OsTaskPreemptabilityEnum`                              | [x] Done    | c53a7febdc                               | Group5           |
| `OsTaskProxy`                                           | [x] Done    | 61ccaa68eb                               | Group5           |
| `PModeGroupInAtomicSwcInstanceRef`                      | [ ] Deferred| 74e821ccb8                               | Group11          |
| `POperationInAtomicSwcInstanceRef`                      | [ ] Deferred| 74e821ccb8                               | Group11          |
| `PPortComSpec`                                          | [ ] Pending | N/A                                      | Group27          |
| `PPortInCompositionInstanceRef`                         | [ ] Deferred| 74e821ccb8                               | Group11          |
| `PPortPrototype`                                        | [x] Done    | 0927333086                               | Group2           |
| `PRPortPrototype`                                       | [x] Done    | 043de7436d                               | Group2           |
| `PTriggerInAtomicSwcTypeInstanceRef`                    | [ ] Deferred| 74e821ccb8                               | Group11          |
| `PackageableElement`                                    | [x] Done    | bb032ddd55                               | Group1           |
| `Paginateable`                                          | [x] Done    | 20e6ee88d0                               | Group3           |
| `ParameterAccess`                                       | [ ] Deferred| N/A                                      | Group12          |
| `ParameterDataPrototype`                                | [ ] Pending | N/A                                      | Group22          |
| `ParameterInAtomicSWCTypeInstanceRef`                   | [ ] Pending | N/A                                      | Group28          |
| `ParameterInterface`                                    | [x] Done    | 6bf99879eb                               | Group1           |
| `ParameterPortAnnotation`                               | [ ] Pending | N/A                                      | Group27          |
| `ParameterProvideComSpec`                               | [ ] Pending | N/A                                      | Group27          |
| `ParameterRequireComSpec`                               | [x] Done    | 6cf8476adb                               | Group10          |
| `ParameterSwComponentType`                              | [ ] Pending | N/A                                      | Group27          |
| `PassThroughSwConnector`                                | [ ] Pending | N/A                                      | Group27          |
| `PayloadBytePatternRule`                                | [ ] Deferred| 8f863fe9dd                               | Group20          |
| `PayloadBytePatternRulePart`                            | [x] Deferred| 8c72c71709                               | Group20          |
| `Pdu`                                                   | [ ] Pending | N/A                                      | Group31          |
| `PduActivationRoutingGroup`                             | [ ] Pending | N/A                                      | Group32          |
| `PduCollectionSemanticsEnum`                            | [ ] Deferred| 4b7c8dc79c                               | Group16          |
| `PduCollectionTriggerEnum`                              | [x] Done    | 64d125ffae                               | Group5           |
| `PduMappingDefaultValue`                                | [x] Done    | 9c8e10b37f                               | Group6           |
| `PduToFrameMapping`                                     | [ ] Pending | N/A                                      | Group31          |
| `PduTriggering`                                         | [ ] Pending | N/A                                      | Group31          |
| `PdurIPduGroup`                                         | [x] Done    | c53a7febdc                               | Group5           |
| `PerInstanceMemory`                                     | [x] Done    | f35aa0cd0a                               | Group2           |
| `PerInstanceMemorySize`                                 | [x] Done    | df36bbb1fa                               | Group10          |
| `PeriodicEventTriggering`                               | [ ] Pending | N/A                                      | Group35          |
| `PermissibleSignalPath`                                 | [ ] Pending | N/A                                      | Group31          |
| `PgwideEnum`                                            | [ ] Pending | N/A                                      | Group22          |
| `PhysConstrs`                                           | [ ] Pending | N/A                                      | Group28          |
| `PhysicalChannel`                                       | [ ] Pending | N/A                                      | Group29          |
| `PhysicalDimension`                                     | [ ] Pending | N/A                                      | Group28          |
| `PhysicalDimensionMapping`                              | [ ] Pending | N/A                                      | Group28          |
| `PhysicalDimensionMappingSet`                           | [ ] Pending | N/A                                      | Group28          |
| `PlatformModuleEthernetEndpointConfiguration`           | [x] Done    | 5d4cc1c454                               | Group7           |
| `PlcaProps`                                             | [ ] Pending | N/A                                      | Group30          |
| `PncGatewayTypeEnum`                                    | [ ] Deferred| 7c137656f6                               | Group15          |
| `PncMapping`                                            | [ ] Pending | N/A                                      | Group31          |
| `PortAPIOption`                                         | [x] Done    | 7c67628122                               | Group2           |
| `PortDefinedArgumentValue`                              | [x] Done    | 7fc79e4b73                               | Group2           |
| `PortElementToCommunicationResourceMapping`             | [ ] Pending | N/A                                      | Group34          |
| `PortGroup`                                             | [x] Done    | d6512dbbec                               | Group2           |
| `PortGroupInSystemInstanceRef`                          | [x] Done    | 19c327cca6                               | Group5           |
| `PortInCompositionTypeInstanceRef`                      | [x] Done    | a6d84b2601                               | Group2           |
| `PortInterface`                                         | [ ] Pending | N/A                                      | Group27          |
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
| `PostBuildVariantCriterionValueSet`                     | [ ] Pending | N/A                                      | Group36          |
| `PredefinedChapter`                                     | [ ] Pending | N/A                                      | Group22          |
| `PredefinedVariant`                                     | [ ] Pending | N/A                                      | Group21          |
| `PrimitiveAttributeCondition`                           | [ ] Pending | N/A                                      | Group36          |
| `PrimitiveAttributeTailoring`                           | [ ] Pending | N/A                                      | Group36          |
| `PrimitiveIdentifier`                                   | [ ] Pending | N/A                                      | Group21          |
| `PrivacyLevel`                                          | [x] Done    | fb222ae5b2                               | Group5           |
| `PrmChar`                                               | [x] Done    | 8be54a00d1                               | Group9           |
| `PrmCharAbsTol`                                         | [x] Done    | e6c467d5f8                               | Group9           |
| `PrmCharContents`                                       | [x] Done    | 9494a593a2                               | Group9           |
| `PrmCharMinTypMax`                                      | [x] Done    | 376f43f648                               | Group9           |
| `PrmCharNumericalContents`                              | [x] Done    | 51ded41bf8                               | Group9           |
| `PrmCharNumericalValue`                                 | [x] Done    | 2f1c852dbb                               | Group9           |
| `PrmCharTextualContents`                                | [x] Done    | 83a56461a1                               | Group9           |
| `Prms`                                                  | [x] Done    | f05d3afdfa                               | Group9           |
| `ProcessingKindEnum`                                    | [ ] Pending | N/A                                      | Group27          |
| `ProgramminglanguageEnum`                               | [x] Done    | be79d7993b                               | Group1           |
| `ProvidedServiceInstance`                               | [ ] Pending | N/A                                      | Group32          |
| `PulseTestEnum`                                         | [ ] Pending | N/A                                      | Group27          |
| `QueuedReceiverComSpec`                                 | [x] Done    | bb5804989f                               | Group10          |
| `QueuedSenderComSpec`                                   | [x] Done    | 4a7d82ffc7                               | Group5           |
| `RModeGroupInAtomicSWCInstanceRef`                      | [ ] Deferred| 74e821ccb8                               | Group11          |
| `RModeInAtomicSwcInstanceRef`                           | [ ] Deferred| 74e821ccb8                               | Group11          |
| `ROperationInAtomicSwcInstanceRef`                      | [ ] Deferred| 74e821ccb8                               | Group11          |
| `RPortComSpec`                                          | [ ] Pending | N/A                                      | Group27          |
| `RPortInCompositionInstanceRef`                         | [ ] Deferred| 74e821ccb8                               | Group11          |
| `RPortPrototype`                                        | [x] Done    | 2cd6f3c46e                               | Group2           |
| `RTEEvent`                                              | [x] Done    | f0483d5732                               | Group2           |
| `RVariableInAtomicSwcInstanceRef`                       | [ ] Deferred| 74e821ccb8                               | Group11          |
| `RamBlockStatusControlEnum`                             | [x] Done    | 343d2af672                               | Group10          |
| `RapidPrototypingScenario`                              | [ ] Pending | N/A                                      | Group29          |
| `ReceiverAnnotation`                                    | [ ] Pending | N/A                                      | Group27          |
| `ReceiverComSpec`                                       | [ ] Pending | N/A                                      | Group27          |
| `ReceptionComSpecProps`                                 | [x] Done    | 0ba890ba88                               | Group10          |
| `RecordLayoutIteratorPoint`                             | [x] Done    | 2acaf7a45f                               | Group3           |
| `RecordValueSpecification`                              | [x] Done    | b1c7030b10                               | Group3           |
| `ReentrancyLevelEnum`                                   | [x] Done    | 286c7c5870                               | Group10          |
| `Ref`                                                   | [x] Done    | 0518a7bca2                               | Group3           |
| `ReferenceBase`                                         | [x] Done    | 192dfd9467                               | Group1           |
| `ReferenceCondition`                                    | [ ] Pending | N/A                                      | Group36          |
| `ReferenceTailoring`                                    | [ ] Pending | N/A                                      | Group36          |
| `ReferenceValueSpecification`                           | [ ] Pending | N/A                                      | Group28          |
| `Referrable`                                            | [ ] Pending | N/A                                      | Group21          |
| `ReferrableSubtypesEnum`                                | [ ] Pending | N/A                                      | Group21          |
| `RegularExpression`                                     | [ ] Pending | N/A                                      | Group21          |
| `RelativeTolerance`                                     | [ ] Pending | N/A                                      | Group31          |
| `RequestResponseDelay`                                  | [ ] Deferred| d7240be740                               | Group16          |
| `ResolutionPolicyEnum`                                  | [x] Done    | f0a7460898                               | Group3           |
| `ResourceConsumption`                                   | [x] Done    | 0404020952                               | Group1           |
| `RestrictionWithSeverity`                               | [ ] Pending | N/A                                      | Group36          |
| `ResumePosition`                                        | [ ] Deferred| N/A                                      | Group17          |
| `RevisionLabelString`                                   | [ ] Pending | N/A                                      | Group21          |
| `RoleBasedBswModuleEntryAssignment`                     | [ ] Pending | N/A                                      | Group23          |
| `RoleBasedDataAssignment`                               | [x] Done    | 5989355419                               | Group10          |
| `RoleBasedDataTypeAssignment`                           | [ ] Pending | N/A                                      | Group23          |
| `RoleBasedPortAssignment`                               | [x] Done    | f94da3dd92                               | Group10          |
| `RoleBasedResourceDependency`                           | [ ] Pending | N/A                                      | Group26          |
| `RootSwCompositionPrototype`                            | [x] Done    | 671dfc3835                               | Group1           |
| `RoughEstimateHeapUsage`                                | [ ] Pending | N/A                                      | Group23          |
| `RoughEstimateOfExecutionTime`                          | [ ] Pending | N/A                                      | Group23          |
| `RoughEstimateStackUsage`                               | [ ] Deferred| 3db474b11a                               | Group20          |
| `Row`                                                   | [x] Done    | b43b860105                               | Group3           |
| `RptAccessEnum`                                         | [ ] Pending | N/A                                      | Group23          |
| `RptComponent`                                          | [ ] Pending | N/A                                      | Group23          |
| `RptContainer`                                          | [ ] Pending | N/A                                      | Group29          |
| `RptEnablerImplTypeEnum`                                | [ ] Pending | N/A                                      | Group23          |
| `RptExecutableEntity`                                   | [ ] Pending | N/A                                      | Group23          |
| `RptExecutableEntityEvent`                              | [ ] Pending | N/A                                      | Group23          |
| `RptExecutableEntityProperties`                         | [ ] Pending | N/A                                      | Group23          |
| `RptExecutionContext`                                   | [ ] Pending | N/A                                      | Group23          |
| `RptExecutionControlEnum`                               | [ ] Pending | N/A                                      | Group23          |
| `RptHook`                                               | [ ] Pending | N/A                                      | Group29          |
| `RptImplPolicy`                                         | [ ] Pending | N/A                                      | Group23          |
| `RptPreparationEnum`                                    | [ ] Pending | N/A                                      | Group23          |
| `RptProfile`                                            | [ ] Pending | N/A                                      | Group29          |
| `RptServicePoint`                                       | [ ] Pending | N/A                                      | Group23          |
| `RptServicePointEnum`                                   | [ ] Pending | N/A                                      | Group23          |
| `RptSupportData`                                        | [ ] Pending | N/A                                      | Group23          |
| `RptSwPrototypingAccess`                                | [ ] Pending | N/A                                      | Group23          |
| `RteApiReturnValueProvisionEnum`                        | [ ] Pending | N/A                                      | Group29          |
| `RteEventInCompositionSeparation`                       | [ ] Pending | N/A                                      | Group31          |
| `RteEventInCompositionToOsTaskProxyMapping`             | [ ] Pending | N/A                                      | Group31          |
| `RteEventInEcuInstanceRef`                              | [ ] Deferred| N/A                                      | Group12          |
| `RteEventInSystemSeparation`                            | [ ] Pending | N/A                                      | Group31          |
| `RteEventInSystemToOsTaskProxyMapping`                  | [ ] Pending | N/A                                      | Group31          |
| `RtePluginProps`                                        | [x] Done    | ec7fa0b5df                               | Group6           |
| `RtpTp`                                                 | [ ] Pending | N/A                                      | Group32          |
| `RuleArguments`                                         | [ ] Pending | N/A                                      | Group28          |
| `RuleBasedAxisCont`                                     | [ ] Pending | N/A                                      | Group28          |
| `RuleBasedValueCont`                                    | [ ] Pending | N/A                                      | Group28          |
| `RuleBasedValueSpecification`                           | [ ] Pending | N/A                                      | Group28          |
| `RunMode`                                               | [ ] Deferred| N/A                                      | Group17          |
| `RunnableEntity`                                        | [ ] Pending | N/A                                      | Group28          |
| `RunnableEntityArgument`                                | [x] Done    | 3857c2a435                               | Group2           |
| `RunnableEntityGroup`                                   | [ ] Pending | N/A                                      | Group28          |
| `RuntimeAddressConfigurationEnum`                       | [ ] Deferred| c5bb322323                               | Group16          |
| `RuntimeError`                                          | [ ] Pending | N/A                                      | Group23          |
| `RxAcceptContainedIPduEnum`                             | [ ] Pending | N/A                                      | Group31          |
| `RxIdentifierRange`                                     | [ ] Pending | N/A                                      | Group32          |
| `SOMEIPMessageTypeEnum`                                 | [x] Done    | b163080753                               | Group6           |
| `SOMEIPTransformationDescription`                       | [ ] Pending | N/A                                      | Group34          |
| `SOMEIPTransformationISignalProps`                      | [x] Done    | 55ff2098b4                               | Group6           |
| `SOMEIPTransformationProps`                             | [ ] Pending | N/A                                      | Group34          |
| `SaveConfigurationEntry`                                | [ ] Pending | N/A                                      | Group32          |
| `ScaleConstrValidityEnum`                               | [x] Done    | 1bc8904eee                               | Group9           |
| `ScheduleTableEntry`                                    | [ ] Pending | N/A                                      | Group31          |
| `Sd`                                                    | [ ] Pending | N/A                                      | Group21          |
| `SdClientConfig`                                        | [x] Done    | 8e0c8857ad                               | Group7           |
| `SdServerConfig`                                        | [ ] Deferred| d7240be740                               | Group16          |
| `Sdf`                                                   | [ ] Pending | N/A                                      | Group21          |
| `Sdg`                                                   | [ ] Pending | N/A                                      | Group21          |
| `SdgAbstractForeignReference`                           | [ ] Pending | N/A                                      | Group21          |
| `SdgAbstractPrimitiveAttribute`                         | [ ] Pending | N/A                                      | Group21          |
| `SdgAggregationWithVariation`                           | [ ] Pending | N/A                                      | Group21          |
| `SdgAttribute`                                          | [ ] Pending | N/A                                      | Group21          |
| `SdgCaption`                                            | [ ] Pending | N/A                                      | Group21          |
| `SdgClass`                                              | [ ] Pending | N/A                                      | Group21          |
| `SdgContents`                                           | [ ] Pending | N/A                                      | Group21          |
| `SdgDef`                                                | [ ] Pending | N/A                                      | Group21          |
| `SdgElementWithGid`                                     | [ ] Pending | N/A                                      | Group21          |
| `SdgForeignReference`                                   | [ ] Pending | N/A                                      | Group21          |
| `SdgForeignReferenceWithVariation`                      | [ ] Pending | N/A                                      | Group21          |
| `SdgPrimitiveAttribute`                                 | [ ] Pending | N/A                                      | Group21          |
| `SdgPrimitiveAttributeWithVariation`                    | [ ] Pending | N/A                                      | Group21          |
| `SdgReference`                                          | [ ] Pending | N/A                                      | Group21          |
| `SdgTailoring`                                          | [ ] Pending | N/A                                      | Group36          |
| `SecOcCryptoServiceMapping`                             | [ ] Pending | N/A                                      | Group18          |
| `SectionInitializationPolicyType`                       | [ ] Pending | N/A                                      | Group22          |
| `SectionNamePrefix`                                     | [ ] Deferred| 0e26482636                               | Group20          |
| `SecureCommunicationAuthenticationProps`                | [ ] Pending | N/A                                      | Group31          |
| `SecureCommunicationFreshnessProps`                     | [ ] Pending | N/A                                      | Group31          |
| `SecureCommunicationProps`                              | [ ] Pending | N/A                                      | Group31          |
| `SecureCommunicationPropsSet`                           | [ ] Pending | N/A                                      | Group31          |
| `SecureOnBoardCommunicationNeeds`                       | [ ] Pending | N/A                                      | Group29          |
| `SecuredIPdu`                                           | [ ] Deferred| 0a98655a06                               | Group15          |
| `SecuredPduHeaderEnum`                                  | [ ] Pending | 3d5cb55dbe                               | Group15          |
| `SecurityEventAggregationFilter`                        | [ ] Pending | N/A                                      | Group36          |
| `SecurityEventContextDataSourceEnum`                    | [ ] Pending | N/A                                      | Group36          |
| `SecurityEventContextMapping`                           | [ ] Pending | N/A                                      | Group36          |
| `SecurityEventContextMappingApplication`                | [ ] Pending | N/A                                      | Group36          |
| `SecurityEventContextMappingBswModule`                  | [ ] Pending | N/A                                      | Group36          |
| `SecurityEventContextMappingCommConnector`              | [ ] Pending | N/A                                      | Group36          |
| `SecurityEventContextMappingFunctionalCluster`          | [ ] Pending | N/A                                      | Group36          |
| `SecurityEventContextProps`                             | [ ] Pending | N/A                                      | Group36          |
| `SecurityEventDefinition`                               | [ ] Pending | N/A                                      | Group36          |
| `SecurityEventFilterChain`                              | [ ] Pending | N/A                                      | Group36          |
| `SecurityEventOneEveryNFilter`                          | [ ] Pending | N/A                                      | Group36          |
| `SecurityEventReportingModeEnum`                        | [ ] Pending | N/A                                      | Group36          |
| `SecurityEventStateFilter`                              | [ ] Pending | N/A                                      | Group36          |
| `SecurityEventThresholdFilter`                          | [ ] Pending | N/A                                      | Group36          |
| `SegmentPosition`                                       | [ ] Deferred| 9546cf291b                               | Group15          |
| `SendIndicationEnum`                                    | [ ] Pending | N/A                                      | Group34          |
| `SenderAnnotation`                                      | [ ] Pending | N/A                                      | Group27          |
| `SenderComSpec`                                         | [ ] Pending | N/A                                      | Group27          |
| `SenderRecArrayElementMapping`                          | [ ] Pending | N/A                                      | Group31          |
| `SenderRecArrayTypeMapping`                             | [x] Done    | 757aea1d17                               | Group6           |
| `SenderRecCompositeTypeMapping`                         | [x] Done    | 757aea1d17                               | Group6           |
| `SenderRecRecordElementMapping`                         | [ ] Deferred| N/A                                      | Group17          |
| `SenderRecRecordTypeMapping`                            | [ ] Deferred| N/A                                      | Group17          |
| `SenderReceiverAnnotation`                              | [ ] Pending | N/A                                      | Group27          |
| `SenderReceiverCompositeElementToSignalMapping`         | [ ] Pending | N/A                                      | Group31          |
| `SenderReceiverInterface`                               | [x] Done    | e4e4770fb7                               | Group1           |
| `SenderReceiverToSignalGroupMapping`                    | [ ] Deferred| N/A                                      | Group17          |
| `SenderReceiverToSignalMapping`                         | [ ] Deferred| N/A                                      | Group17          |
| `SensorActuatorSwComponentType`                         | [ ] Pending | N/A                                      | Group29          |
| `SeparateSignalPath`                                    | [ ] Pending | N/A                                      | Group31          |
| `ServerArgumentImplPolicyEnum`                          | [ ] Pending | N/A                                      | Group27          |
| `ServerCallPoint`                                       | [x] Done    | 774620a3b1                               | Group2           |
| `ServerComSpec`                                         | [ ] Pending | N/A                                      | Group27          |
| `ServiceDependency`                                     | [ ] Pending | N/A                                      | Group23          |
| `ServiceDiagnosticRelevanceEnum`                        | [ ] Deferred| 28746ce3cc                               | Group14          |
| `ServiceInstanceCollectionSet`                          | [ ] Pending | N/A                                      | Group32          |
| `ServiceNeeds`                                          | [x] Done    | 5fd6271d70                               | Group4           |
| `ServiceProviderEnum`                                   | [ ] Pending | N/A                                      | Group27          |
| `ServiceProxySwComponentType`                           | [x] Done    | 74e821ccb8                               | Group11          |
| `ServiceSwComponentType`                                | [ ] Pending | N/A                                      | Group29          |
| `SeverityEnum`                                          | [ ] Pending | N/A                                      | Group36          |
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
| `SignalFanEnum`                                         | [ ] Pending | N/A                                      | Group27          |
| `SignalServiceTranslationControlEnum`                   | [ ] Pending | N/A                                      | Group34          |
| `SignalServiceTranslationElementProps`                  | [ ] Deferred| 29d09fc625                               | Group14          |
| `SignalServiceTranslationEventProps`                    | [ ] Pending | N/A                                      | Group34          |
| `SignalServiceTranslationProps`                         | [ ] Pending | N/A                                      | Group34          |
| `SignalServiceTranslationPropsSet`                      | [ ] Pending | N/A                                      | Group34          |
| `SimulatedExecutionTime`                                | [ ] Pending | N/A                                      | Group23          |
| `SingleLanguageLongName`                                | [x] Done    | 8aaa2657f3                               | Group3           |
| `SingleLanguageReferrable`                              | [x] Done    | a5910c1bf5                               | Group3           |
| `SingleLanguageUnitNames`                               | [x] Done    | d42795c169                               | Group8           |
| `SlOverviewParagraph`                                   | [x] Done    | 951209dbab                               | Group8           |
| `SlParagraph`                                           | [x] Done    | b7748b3e50                               | Group3           |
| `SoAdConfig`                                            | [ ] Pending | N/A                                      | Group32          |
| `SoAdRoutingGroup`                                      | [ ] Deferred| 89363ebe2b                               | Group20          |
| `SoConIPduIdentifier`                                   | [ ] Pending | N/A                                      | Group32          |
| `SocketAddress`                                         | [ ] Pending | N/A                                      | Group32          |
| `SocketConnectionBundle`                                | [ ] Deferred| 4b7c8dc79c                               | Group16          |
| `SocketConnectionIpduIdentifier`                        | [ ] Deferred| 4b7c8dc79c                               | Group16          |
| `SocketConnectionIpduIdentifierSet`                     | [ ] Pending | N/A                                      | Group32          |
| `SoftwareContext`                                       | [ ] Deferred| 23884479e9                               | Group20          |
| `SomeipProtocolRule`                                    | [ ] Deferred| c18aa8d400                               | Group20          |
| `SomeipSdClientEventGroupTimingConfig`                  | [ ] Pending | N/A                                      | Group32          |
| `SomeipSdRule`                                          | [ ] Deferred| 17b563a730                               | Group20          |
| `SomeipSdServerEventGroupTimingConfig`                  | [ ] Pending | N/A                                      | Group32          |
| `SomeipSdServerServiceInstanceConfig`                   | [ ] Pending | N/A                                      | Group32          |
| `SomeipTpChannel`                                       | [ ] Pending | N/A                                      | Group33          |
| `SomeipTpConfig`                                        | [ ] Pending | N/A                                      | Group33          |
| `SomeipTpConnection`                                    | [ ] Pending | N/A                                      | Group33          |
| `SpecElementReference`                                  | [ ] Pending | N/A                                      | Group36          |
| `SpecElementScope`                                      | [ ] Pending | N/A                                      | Group36          |
| `SpecificationDocumentScope`                            | [ ] Pending | N/A                                      | Group36          |
| `SpecificationScope`                                    | [ ] Pending | N/A                                      | Group36          |
| `SporadicEventTriggering`                               | [ ] Pending | N/A                                      | Group35          |
| `StackUsage`                                            | [ ] Deferred| 9ce364e249                               | Group20          |
| `StandardNameEnum`                                      | [x] Done    | 9a9ffdae8d                               | Group1           |
| `StateDependentFirewall`                                | [ ] Pending | N/A                                      | Group33          |
| `StaticPart`                                            | [x] Done    | 206cf29517                               | Group5           |
| `StaticSocketConnection`                                | [ ] Pending | N/A                                      | Group32          |
| `Std`                                                   | [x] Done    | c53a240809                               | Group3           |
| `StorageConditionStatusEnum`                            | [ ] Pending | N/A                                      | Group29          |
| `StreamFilterIEEE1722Tp`                                | [ ] Pending | N/A                                      | Group30          |
| `StreamFilterIpv4Address`                               | [ ] Pending | N/A                                      | Group30          |
| `StreamFilterIpv6Address`                               | [ ] Pending | N/A                                      | Group30          |
| `StreamFilterMACAddress`                                | [ ] Pending | N/A                                      | Group30          |
| `StreamFilterPortRange`                                 | [ ] Pending | N/A                                      | Group30          |
| `StreamFilterRuleDataLinkLayer`                         | [ ] Pending | N/A                                      | Group30          |
| `StreamFilterRuleIpTp`                                  | [ ] Pending | N/A                                      | Group30          |
| `String`                                                | [ ] Pending | N/A                                      | Group21          |
| `StructuredReq`                                         | [x] Done    | d311fc7ce0                               | Group1           |
| `SubElementMapping`                                     | [x] Done    | 5eadca7853                               | Group1           |
| `SubElementRef`                                         | [x] Done    | 47b3052188                               | Group1           |
| `Superscript`                                           | [ ] Pending | N/A                                      | Group21          |
| `SupervisedEntityCheckpointNeeds`                       | [x] Done    | 67640c8035                               | Group4           |
| `SupervisedEntityNeeds`                                 | [ ] Pending | N/A                                      | Group23          |
| `SupportBufferLockingEnum`                              | [x] Done    | 7c67628122                               | Group2           |
| `SwAddrMethod`                                          | [ ] Pending | N/A                                      | Group22          |
| `SwAxisCont`                                            | [ ] Pending | N/A                                      | Group28          |
| `SwAxisGeneric`                                         | [ ] Pending | N/A                                      | Group28          |
| `SwAxisGrouped`                                         | [x] Done    | 12a2e0170b                               | Group3           |
| `SwAxisIndividual`                                      | [x] Done    | 842e1e4227                               | Group3           |
| `SwAxisType`                                            | [ ] Pending | N/A                                      | Group28          |
| `SwBaseType`                                            | [ ] Pending | N/A                                      | Group28          |
| `SwBitRepresentation`                                   | [ ] Pending | N/A                                      | Group28          |
| `SwCalibrationAccessEnum`                               | [ ] Pending | N/A                                      | Group28          |
| `SwCalprmAxis`                                          | [ ] Pending | N/A                                      | Group28          |
| `SwCalprmAxisSet`                                       | [x] Done    | 9209b83ea0                               | Group3           |
| `SwCalprmAxisTypeProps`                                 | [ ] Pending | N/A                                      | Group28          |
| `SwCalprmRefProxy`                                      | [ ] Pending | N/A                                      | Group28          |
| `SwComponentDocumentation`                              | [ ] Pending | N/A                                      | Group29          |
| `SwComponentPrototype`                                  | [x] Done    | ff993a74c8                               | Group1           |
| `SwComponentPrototypeAssignment`                        | [x] Done    | 88070878ea                               | Group5           |
| `SwComponentType`                                       | [ ] Pending | N/A                                      | Group27          |
| `SwConnector`                                           | [ ] Pending | N/A                                      | Group27          |
| `SwDataDefProps`                                        | [ ] Pending | N/A                                      | Group28          |
| `SwDataDependency`                                      | [ ] Pending | N/A                                      | Group28          |
| `SwDataDependencyArgs`                                  | [ ] Pending | N/A                                      | Group28          |
| `SwGenericAxisParam`                                    | [ ] Pending | N/A                                      | Group28          |
| `SwGenericAxisParamType`                                | [x] Done    | 1eacd1a7a7                               | Group3           |
| `SwImplPolicyEnum`                                      | [x] Done    | d6945a4c8a                               | Group9           |
| `SwPointerTargetProps`                                  | [ ] Pending | N/A                                      | Group22          |
| `SwRecordLayout`                                        | [x] Done    | f8149880de                               | Group3           |
| `SwRecordLayoutGroup`                                   | [x] Done    | 2acaf7a45f                               | Group3           |
| `SwRecordLayoutGroupContent`                            | [x] Done    | 0f19d490d3                               | Group3           |
| `SwRecordLayoutV`                                       | [x] Done    | 9c0c3f85f8                               | Group3           |
| `SwServiceArg`                                          | [ ] Pending | N/A                                      | Group22          |
| `SwServiceImplPolicyEnum`                               | [ ] Pending | N/A                                      | Group22          |
| `SwSystemconst`                                         | [x] Done    | 984387dd0c                               | Group9           |
| `SwSystemconstDependentFormula`                         | [x] Done    | f05e21d49e                               | Group8           |
| `SwSystemconstValue`                                    | [x] Done    | 5333bec027                               | Group8           |
| `SwSystemconstantValueSet`                              | [ ] Pending | N/A                                      | Group36          |
| `SwTextProps`                                           | [ ] Pending | N/A                                      | Group28          |
| `SwValueCont`                                           | [x] Done    | 6db47de6aa                               | Group3           |
| `SwValues`                                              | [ ] Pending | N/A                                      | Group28          |
| `SwVariableRefProxy`                                    | [ ] Pending | N/A                                      | Group28          |
| `SwcBswMapping`                                         | [x] Done    | 58b2c68a57                               | Group1           |
| `SwcBswRunnableMapping`                                 | [ ] Deferred| c52cece662                               | Group13          |
| `SwcBswSynchronizedModeGroupPrototype`                  | [ ] Deferred| 659c2bf174                               | Group13          |
| `SwcBswSynchronizedTrigger`                             | [ ] Deferred| 6b4b9d6d10                               | Group13          |
| `SwcExclusiveAreaPolicy`                                | [ ] Pending | N/A                                      | Group29          |
| `SwcImplementation`                                     | [x] Done    | 6eae95f556                               | Group10          |
| `SwcInternalBehavior`                                   | [x] Done    | 4043dc013a                               | Group2           |
| `SwcModeManagerErrorEvent`                              | [ ] Pending | N/A                                      | Group29          |
| `SwcModeSwitchEvent`                                    | [ ] Pending | N/A                                      | Group28          |
| `SwcServiceDependency`                                  | [ ] Pending | N/A                                      | Group29          |
| `SwcSupportedFeature`                                   | [x] Done    | 7c67628122                               | Group2           |
| `SwcTiming`                                             | [ ] Pending | N/A                                      | Group35          |
| `SwcToApplicationPartitionMapping`                      | [ ] Pending | N/A                                      | Group30          |
| `SwcToEcuMapping`                                       | [ ] Pending | N/A                                      | Group18          |
| `SwcToImplMapping`                                      | [ ] Pending | N/A                                      | Group18          |
| `SwcToSwcOperationArguments`                            | [ ] Pending | N/A                                      | Group31          |
| `SwcToSwcOperationArgumentsDirectionEnum`               | [ ] Pending | N/A                                      | Group31          |
| `SwcToSwcSignal`                                        | [ ] Pending | N/A                                      | Group31          |
| `SwitchAsynchronousTrafficShaperGroupEntry`             | [ ] Pending | N/A                                      | Group30          |
| `SwitchFlowMeteringEntry`                               | [ ] Pending | N/A                                      | Group30          |
| `SwitchStreamFilterActionDestPortModification`          | [ ] Pending | N/A                                      | Group30          |
| `SwitchStreamFilterActionPortModificationEnum`          | [ ] Pending | N/A                                      | Group30          |
| `SwitchStreamFilterEntry`                               | [ ] Pending | N/A                                      | Group30          |
| `SwitchStreamFilterRule`                                | [ ] Pending | N/A                                      | Group30          |
| `SwitchStreamGateEntry`                                 | [ ] Pending | N/A                                      | Group30          |
| `SwitchStreamIdentification`                            | [ ] Pending | N/A                                      | Group30          |
| `SymbolProps`                                           | [x] Done    | 2d21a9108b                               | Group2           |
| `SymbolString`                                          | [ ] Pending | N/A                                      | Group21          |
| `SymbolicNameProps`                                     | [ ] Pending | N/A                                      | Group29          |
| `SyncTimeBaseMgrUserNeeds`                              | [x] Done    | 609f148a93                               | Group4           |
| `SynchronizationPointConstraint`                        | [ ] Pending | N/A                                      | Group35          |
| `SynchronizationTimingConstraint`                       | [x] Done    | e305e80e2a                               | Group8           |
| `SynchronizationTypeEnum`                               | [ ] Pending | N/A                                      | Group35          |
| `SynchronousServerCallPoint`                            | [x] Done    | 9182987d97                               | Group2           |
| `System`                                                | [x] Done    | ccfb528daf                               | Group5           |
| `SystemMapping`                                         | [ ] Pending | N/A                                      | Group30          |
| `SystemSignal`                                          | [ ] Deferred| 7c5d9e9d81                               | Group15          |
| `SystemSignalGroup`                                     | [ ] Pending | N/A                                      | Group31          |
| `SystemSignalGroupToCommunicationResourceMapping`       | [ ] Pending | N/A                                      | Group31          |
| `SystemSignalToCommunicationResourceMapping`            | [ ] Pending | N/A                                      | Group31          |
| `SystemTiming`                                          | [ ] Pending | N/A                                      | Group35          |
| `TDCpSoftwareClusterMapping`                            | [ ] Pending | N/A                                      | Group35          |
| `TDCpSoftwareClusterMappingSet`                         | [ ] Pending | N/A                                      | Group35          |
| `TDCpSoftwareClusterResourceMapping`                    | [ ] Pending | N/A                                      | Group35          |
| `TDEventBswInternalBehavior`                            | [ ] Pending | N/A                                      | Group35          |
| `TDEventBswInternalBehaviorTypeEnum`                    | [ ] Pending | N/A                                      | Group35          |
| `TDEventBswModeDeclaration`                             | [ ] Pending | N/A                                      | Group35          |
| `TDEventBswModeDeclarationTypeEnum`                     | [ ] Pending | N/A                                      | Group35          |
| `TDEventBswModule`                                      | [ ] Pending | N/A                                      | Group35          |
| `TDEventBswModuleTypeEnum`                              | [ ] Pending | N/A                                      | Group35          |
| `TDEventCom`                                            | [ ] Pending | N/A                                      | Group35          |
| `TDEventComplex`                                        | [ ] Pending | N/A                                      | Group35          |
| `TDEventCycleStart`                                     | [ ] Pending | N/A                                      | Group35          |
| `TDEventFrClusterCycleStart`                            | [ ] Pending | N/A                                      | Group35          |
| `TDEventFrame`                                          | [ ] Pending | N/A                                      | Group35          |
| `TDEventFrameEthernet`                                  | [ ] Pending | N/A                                      | Group35          |
| `TDEventFrameEthernetTypeEnum`                          | [ ] Pending | N/A                                      | Group35          |
| `TDEventFrameTypeEnum`                                  | [ ] Pending | N/A                                      | Group35          |
| `TDEventIPdu`                                           | [ ] Pending | N/A                                      | Group35          |
| `TDEventIPduTypeEnum`                                   | [ ] Pending | N/A                                      | Group35          |
| `TDEventISignal`                                        | [ ] Pending | N/A                                      | Group35          |
| `TDEventISignalTypeEnum`                                | [ ] Pending | N/A                                      | Group35          |
| `TDEventModeDeclaration`                                | [ ] Pending | N/A                                      | Group35          |
| `TDEventModeDeclarationTypeEnum`                        | [ ] Pending | N/A                                      | Group35          |
| `TDEventOccurrenceExpression`                           | [ ] Pending | N/A                                      | Group35          |
| `TDEventOccurrenceExpressionFormula`                    | [ ] Pending | N/A                                      | Group35          |
| `TDEventOperation`                                      | [ ] Pending | N/A                                      | Group35          |
| `TDEventOperationTypeEnum`                              | [ ] Pending | N/A                                      | Group35          |
| `TDEventSLLETPort`                                      | [ ] Pending | N/A                                      | Group35          |
| `TDEventSwc`                                            | [ ] Pending | N/A                                      | Group35          |
| `TDEventSwcInternalBehavior`                            | [ ] Pending | N/A                                      | Group35          |
| `TDEventSwcInternalBehaviorReference`                   | [ ] Pending | N/A                                      | Group35          |
| `TDEventSwcInternalBehaviorTypeEnum`                    | [ ] Pending | N/A                                      | Group35          |
| `TDEventTTCanCycleStart`                                | [ ] Pending | N/A                                      | Group35          |
| `TDEventTrigger`                                        | [ ] Pending | N/A                                      | Group35          |
| `TDEventTriggerTypeEnum`                                | [ ] Pending | N/A                                      | Group35          |
| `TDEventVariableDataPrototype`                          | [ ] Pending | N/A                                      | Group35          |
| `TDEventVariableDataPrototypeTypeEnum`                  | [ ] Pending | N/A                                      | Group35          |
| `TDEventVfb`                                            | [x] Done    | 18eb225f40                               | Group8           |
| `TDEventVfbPort`                                        | [ ] Pending | N/A                                      | Group35          |
| `TDEventVfbReference`                                   | [ ] Pending | N/A                                      | Group35          |
| `TDHeaderIdRange`                                       | [ ] Pending | N/A                                      | Group35          |
| `Table`                                                 | [x] Done    | e347fbbfa2                               | Group3           |
| `TableSeparatorString`                                  | [x] Done    | 211031ea0f                               | Group3           |
| `TagWithOptionalValue`                                  | [ ] Pending | N/A                                      | Group21          |
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
| `TextTableValuePair`                                    | [ ] Pending | N/A                                      | Group27          |
| `TextValueSpecification`                                | [x] Done    | 81588f449e                               | Group9           |
| `TextualCondition`                                      | [ ] Pending | N/A                                      | Group36          |
| `Tgroup`                                                | [x] Done    | 278d4674f3                               | Group3           |
| `TimeRangeType`                                         | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `TimeRangeTypeTolerance`                                | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `TimeSyncClientConfiguration`                           | [x] Done    | a032fa05dc                               | Group6           |
| `TimeSyncServerConfiguration`                           | [ ] Deferred| b1e4750b14                               | Group16          |
| `TimeSyncTechnologyEnum`                                | [ ] Pending | N/A                                      | Group32          |
| `TimeSynchronization`                                   | [ ] Deferred| b1e4750b14                               | Group16          |
| `TimeValue`                                             | [ ] Pending | N/A                                      | Group27          |
| `TimeValueValueVariationPoint`                          | [x] Done    | d5c96fd954                               | Group8           |
| `TimingCondition`                                       | [ ] Pending | N/A                                      | Group35          |
| `TimingConditionFormula`                                | [ ] Pending | N/A                                      | Group35          |
| `TimingDescriptionEventChain`                           | [x] Done    | ea1a75e5b9                               | Group8           |
| `TimingEvent`                                           | [ ] Pending | N/A                                      | Group28          |
| `TimingExtensionResource`                               | [ ] Pending | N/A                                      | Group35          |
| `TimingModeInstance`                                    | [ ] Pending | N/A                                      | Group35          |
| `TlsCryptoCipherSuite`                                  | [x] Done    | 67315ec0a9                               | Group6           |
| `TlsCryptoCipherSuiteProps`                             | [x] Done    | 648b40acaf                               | Group6           |
| `TlsCryptoServiceMapping`                               | [x] Done    | 67315ec0a9                               | Group6           |
| `TlsPskIdentity`                                        | [x] Done    | 16c2791a2b                               | Group6           |
| `TlsVersionEnum`                                        | [x] Done    | d969a0ddc1                               | Group6           |
| `TlvDataIdDefinition`                                   | [x] Done    | 27ea0743dc                               | Group6           |
| `TlvDataIdDefinitionSet`                                | [x] Done    | f0c9473162                               | Group6           |
| `Topic1`                                                | [ ] Pending | N/A                                      | Group22          |
| `TopicContent`                                          | [x] Done    | 6d7e325736                               | Group3           |
| `TopicContentOrMsrQuery`                                | [x] Done    | 460218682e                               | Group9           |
| `TopicOrMsrQuery`                                       | [ ] Pending | N/A                                      | Group22          |
| `TpAddress`                                             | [ ] Pending | N/A                                      | Group18          |
| `TpConfig`                                              | [ ] Pending | N/A                                      | Group33          |
| `TpConnection`                                          | [ ] Pending | N/A                                      | Group33          |
| `TpConnectionIdent`                                     | [ ] Pending | N/A                                      | Group23          |
| `TpPort`                                                | [ ] Deferred| b1e4750b14                               | Group16          |
| `Traceable`                                             | [ ] Pending | N/A                                      | Group21          |
| `TraceableTable`                                        | [x] Done    | fa79c73df5                               | Group3           |
| `TraceableText`                                         | [x] Done    | 9e80479bda                               | Group1           |
| `TracedFailure`                                         | [ ] Pending | N/A                                      | Group23          |
| `TransferPropertyEnum`                                  | [ ] Pending | e6baac031c                               | Group15          |
| `TransformationComSpecProps`                            | [ ] Pending | N/A                                      | Group27          |
| `TransformationDescription`                             | [ ] Pending | N/A                                      | Group28          |
| `TransformationISignalProps`                            | [x] Done    | 757aea1d17                               | Group6           |
| `TransformationProps`                                   | [ ] Pending | N/A                                      | Group34          |
| `TransformationPropsSet`                                | [ ] Pending | N/A                                      | Group34          |
| `TransformationTechnology`                              | [ ] Pending | N/A                                      | Group27          |
| `TransformerClassEnum`                                  | [ ] Pending | N/A                                      | Group28          |
| `TransformerHardErrorEvent`                             | [ ] Pending | N/A                                      | Group28          |
| `TransmissionAcknowledgementRequest`                    | [ ] Pending | N/A                                      | Group27          |
| `TransmissionComSpecProps`                              | [ ] Pending | N/A                                      | Group27          |
| `TransmissionModeCondition`                             | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `TransmissionModeDeclaration`                           | [ ] Deferred| dcbc6abdb3                               | Group15          |
| `TransmissionModeDefinitionEnum`                        | [ ] Pending | N/A                                      | Group27          |
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
| `TriggerPortAnnotation`                                 | [ ] Pending | N/A                                      | Group27          |
| `TriggerToSignalMapping`                                | [ ] Pending | N/A                                      | Group31          |
| `Tt`                                                    | [ ] Pending | N/A                                      | Group21          |
| `TtcanAbsolutelyScheduledTiming`                        | [ ] Pending | N/A                                      | Group32          |
| `TtcanCluster`                                          | [ ] Pending | N/A                                      | Group29          |
| `TtcanCommunicationConnector`                           | [ ] Pending | N/A                                      | Group29          |
| `TtcanCommunicationController`                          | [ ] Pending | N/A                                      | Group29          |
| `TtcanPhysicalChannel`                                  | [ ] Pending | N/A                                      | Group29          |
| `TtcanTriggerType`                                      | [ ] Pending | N/A                                      | Group32          |
| `UdpChecksumCalculationEnum`                            | [ ] Pending | N/A                                      | Group32          |
| `UdpNmCluster`                                          | [ ] Pending | N/A                                      | Group18          |
| `UdpNmClusterCoupling`                                  | [ ] Pending | N/A                                      | Group18          |
| `UdpNmEcu`                                              | [x] Done    | 9c8e10b37f                               | Group6           |
| `UdpNmNode`                                             | [ ] Pending | N/A                                      | Group18          |
| `UdpProps`                                              | [x] Done    | ecb15e901f                               | Group5           |
| `UdpRule`                                               | [x] Deferred| 29cbfb7bbd                               | Group20          |
| `UdpTp`                                                 | [ ] Deferred| N/A                                      | Group16          |
| `UnassignFrameId`                                       | [ ] Pending | N/A                                      | Group31          |
| `Unit`                                                  | [ ] Pending | N/A                                      | Group28          |
| `UnitGroup`                                             | [x] Done    | e7fdb07f2b                               | Group9           |
| `UnlimitedIntegerValueVariationPoint`                   | [x] Done    | d5c96fd954                               | Group8           |
| `UriString`                                             | [ ] Pending | N/A                                      | Group21          |
| `Url`                                                   | [x] Done    | 4b96ab8d89                               | Group3           |
| `UserDefinedCluster`                                    | [ ] Pending | N/A                                      | Group30          |
| `UserDefinedCommunicationConnector`                     | [ ] Pending | N/A                                      | Group30          |
| `UserDefinedCommunicationController`                    | [ ] Pending | N/A                                      | Group30          |
| `UserDefinedEthernetFrame`                              | [ ] Pending | N/A                                      | Group33          |
| `UserDefinedGlobalTimeMaster`                           | [ ] Pending | N/A                                      | Group34          |
| `UserDefinedGlobalTimeSlave`                            | [ ] Pending | N/A                                      | Group34          |
| `UserDefinedIPdu`                                       | [ ] Deferred| N/A                                      | Group15          |
| `UserDefinedPdu`                                        | [ ] Deferred| N/A                                      | Group15          |
| `UserDefinedPhysicalChannel`                            | [ ] Pending | N/A                                      | Group30          |
| `UserDefinedTransformationComSpecProps`                 | [x] Done    | 4a7d82ffc7                               | Group5           |
| `UserDefinedTransformationDescription`                  | [ ] Pending | N/A                                      | Group34          |
| `UserDefinedTransformationISignalProps`                 | [x] Done    | 301182769c                               | Group6           |
| `UserDefinedTransformationProps`                        | [ ] Pending | N/A                                      | Group34          |
| `V2xDataManagerNeeds`                                   | [x] Done    | e02dc71234                               | Group5           |
| `V2xFacUserNeeds`                                       | [x] Done    | 029aa70113                               | Group5           |
| `V2xMUserNeeds`                                         | [x] Done    | d45912e177                               | Group5           |
| `ValignEnum`                                            | [x] Done    | 52d3272bbb                               | Group3           |
| `ValueGroup`                                            | [ ] Pending | N/A                                      | Group28          |
| `ValueList`                                             | [ ] Pending | N/A                                      | Group28          |
| `ValueRestrictionWithSeverity`                          | [ ] Pending | N/A                                      | Group36          |
| `ValueSpecification`                                    | [ ] Pending | N/A                                      | Group28          |
| `VariableAccess`                                        | [ ] Deferred| N/A                                      | Group12          |
| `VariableAccessInEcuInstanceRef`                        | [ ] Deferred| N/A                                      | Group12          |
| `VariableAccessScopeEnum`                               | [ ] Pending | N/A                                      | Group29          |
| `VariableAndParameterInterfaceMapping`                  | [ ] Deferred| de2d5fe918                               | Group11          |
| `VariableDataPrototype`                                 | [x] Done    | d3b5d680e2                               | Group2           |
| `VariableDataPrototypeInSystemInstanceRef`              | [x] Done    | 1b3d673dac                               | Group7           |
| `VariableInAtomicSWCTypeInstanceRef`                    | [x] Done    | c8ac9ef7de                               | Group2           |
| `VariableInAtomicSwcInstanceRef`                        | [x] Done    | 0369005450                               | Group2           |
| `VariationPoint`                                        | [x] Done    | d4fce975d6                               | Group8           |
| `VariationPointProxy`                                   | [ ] Pending | N/A                                      | Group29          |
| `VariationRestrictionWithSeverity`                      | [ ] Pending | N/A                                      | Group36          |
| `VendorSpecificServiceNeeds`                            | [x] Done    | a25f9a7718                               | Group5           |
| `VerbatimString`                                        | [ ] Pending | N/A                                      | Group21          |
| `VerbatimStringPlain`                                   | [ ] Pending | N/A                                      | Group21          |
| `VerificationStatusIndicationModeEnum`                  | [ ] Pending | N/A                                      | Group29          |
| `VfbTiming`                                             | [ ] Pending | N/A                                      | Group35          |
| `ViewMap`                                               | [ ] Pending | N/A                                      | Group22          |
| `ViewMapSet`                                            | [ ] Pending | N/A                                      | Group22          |
| `ViewTokens`                                            | [x] Done    | 82c86af789                               | Group3           |
| `VlanConfig`                                            | [ ] Deferred| b1e4750b14                               | Group16          |
| `VlanMembership`                                        | [x] Done    | ed6ed2a65f                               | Group6           |
| `WaitPoint`                                             | [ ] Pending | N/A                                      | Group28          |
| `WarningIndicatorRequestedBitNeeds`                     | [x] Done    | 1cd8edd8fd                               | Group5           |
| `WhitespaceControlled`                                  | [x] Done    | a78d444afb                               | Group8           |
| `WorstCaseHeapUsage`                                    | [ ] Pending | N/A                                      | Group22          |
| `WorstCaseStackUsage`                                   | [ ] Deferred| a0cbd41d08                               | Group20          |
| `Xdoc`                                                  | [x] Done    | 294c8aae2c                               | Group3           |
| `Xfile`                                                 | [x] Done    | 7038ce5574                               | Group3           |
| `XmlSpaceEnum`                                          | [x] Done    | ec544e7988                               | Group8           |
| `Xref`                                                  | [x] Done    | db2b4fe059                               | Group3           |
| `XrefTarget`                                            | [x] Done    | 8c9df6638a                               | Group3           |
