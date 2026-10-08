# All Sync Todo Classes (Consolidated)

Generated from all Group files in `docs/plan/sync-todo/` — Classes ordered by name with status and commit ID.

**Status legend:** `[x] Done` = 9-step sync complete AND `# Spec verified:`/`# XSD verified:` stamped in src · `[x]`/`[ ] Deferred` = sync complete (Steps 1–8 green) but the stamp is **deferred to a batch 9b user confirmation** · `[ ] Created` = the class exists in src as an empty stub (dependency placeholder) but implementation has not started · `[ ] Implemented` = the class exists in src with members but the queued 9-step sync is not complete · `[ ] Pending` = the class is not available (not defined in src at all). (Deferred set audited 2026-09-27 against the src stamps.)

## Summary

**1902 classes total**

| Status | Classes | Percent |
| --- | --- | --- |
| [x] Done | 852 | 44.8% |
| [x] Deferred | 42 | 2.2% |
| [x] Retired | 0 | 0.0% |
| [ ] Deferred | 836 | 44.0% |
| [ ] Implemented | 29 | 1.5% |
| [ ] Created | 143 | 7.5% |
| [ ] Pending | 0 | 0.0% |

| Class Name                                              | Status      | Commit ID                                | Groups           |
| ------------------------------------------------------- | ------------| ---------------------------------------- | ---------------- |
| `ARElement`                                             | [x] Done    | 61c85fa794                               | Group1           |
| `ARList`                                                | [x] Done    | 2151ca0302                               | Group9           |
| `ARObject`                                              | [x] Done    | 78ae363c75                               | Group1           |
| `ARPackage`                                             | [x] Done    | 360648178f                               | Group1           |
| `AUTOSAR`                                               | [x] Done    | 74f4d3c80a                               | Group1           |
| `AbsoluteTolerance`                                     | [ ] Implemented| N/A                                      | Group31          |
| `AbstractAccessPoint`                                   | [x] Done    | e3d1262da1                               | Group22          |
| `AbstractCanCluster`                                    | [ ] Deferred| b9599507f4                               | Group29          |
| `AbstractCanCommunicationConnector`                     | [ ] Deferred| b6aaf97f5d                               | Group29          |
| `AbstractCanCommunicationController`                    | [ ] Deferred| b115cca55e                               | Group29          |
| `AbstractCanCommunicationControllerAttributes`          | [ ] Deferred| a7b009e6e7                               | Group29          |
| `AbstractCanPhysicalChannel`                            | [ ] Deferred| d5b7c507aa                               | Group29          |
| `AbstractClassTailoring`                                | [ ] Created | N/A                                      | Group36          |
| `AbstractCondition`                                     | [ ] Created | N/A                                      | Group36          |
| `AbstractDoIpLogicAddressProps`                         | [x] Done    | 64d125ffae                               | Group7           |
| `AbstractEnumerationValueVariationPoint`                | [x] Done    | 0518a7bca2                               | Group8           |
| `AbstractEthernetFrame`                                 | [x] Done    | cba67817b3                               | Group6           |
| `AbstractEvent`                                         | [ ] Deferred| 7d8fb2e207                               | Group28          |
| `AbstractGlobalTimeDomainProps`                         | [ ] Deferred| N/A                                      | Group34          |
| `AbstractImplementationDataType`                        | [x] Done    | 9b5379d3e3                               | Group1           |
| `AbstractImplementationDataTypeElement`                 | [x] Done    | cabd5469e9                               | Group1           |
| `AbstractMultiplicityRestriction`                       | [ ] Created | N/A                                      | Group36          |
| `AbstractNumericalVariationPoint`                       | [x] Done    | d5c96fd954                               | Group8           |
| `AbstractProvidedPortPrototype`                         | [x] Done    | 510d31dd57                               | Group11          |
| `AbstractRequiredPortPrototype`                         | [x] Done    | bbacb3368c                               | Group11          |
| `AbstractRuleBasedValueSpecification`                   | [ ] Deferred| a9f7a78876                               | Group28          |
| `AbstractSecurityEventFilter`                           | [ ] Created | N/A                                      | Group36          |
| `AbstractServiceInstance`                               | [ ] Deferred| N/A                                      | Group32          |
| `AbstractValueRestriction`                              | [ ] Deferred| N/A                                      | Group21          |
| `AbstractVariationRestriction`                          | [ ] Deferred| N/A                                      | Group21          |
| `AccessCount`                                           | [x] Done    | e3d1262da1                               | Group22          |
| `AccessCountSet`                                        | [x] Done    | e3d1262da1                               | Group22          |
| `AclObjectSet`                                          | [ ] Deferred| 11ad22dfad                               | Group22          |
| `AclOperation`                                          | [ ] Deferred| 0eb0409c12                               | Group22          |
| `AclPermission`                                         | [ ] Deferred| 29d7cfc19d                               | Group22          |
| `AclRole`                                               | [ ] Deferred| 8d5c387889                               | Group22          |
| `AclScopeEnum`                                          | [ ] Deferred| dfa53c4352                               | Group22          |
| `AdditionalBindingTimeEnum`                             | [ ] Deferred| b72807df62                               | Group29          |
| `AgeConstraint`                                         | [ ] Deferred| N/A                                      | Group35          |
| `AggregationCondition`                                  | [ ] Created | N/A                                      | Group36          |
| `AggregationTailoring`                                  | [ ] Created | N/A                                      | Group36          |
| `AliasNameAssignment`                                   | [x] Done    | N/A                                      | Group23          |
| `AliasNameSet`                                          | [x] Done    | N/A                                      | Group23          |
| `AlignEnum`                                             | [x] Done    | fa74a474a5                               | Group3           |
| `AlignmentType`                                         | [ ] Deferred| 6133a30b31                               | Group22          |
| `AnalyzedExecutionTime`                                 | [x] Done    | N/A                                      | Group23          |
| `AnyInstanceRef`                                        | [x] Done    | b64a3c317a                               | Group22          |
| `ApiPrincipleEnum`                                      | [x] Done    | c6d2e83f74                               | Group10          |
| `AppOsTaskProxyToEcuTaskProxyMapping`                   | [x] Done    | 860f23a95c                               | Group18          |
| `ApplicationArrayDataType`                              | [ ] Deferred| N/A                                      | Group28          |
| `ApplicationArrayElement`                               | [ ] Deferred| N/A                                      | Group28          |
| `ApplicationCompositeDataType`                          | [x] Done    | de9d3fe0a4                               | Group2           |
| `ApplicationCompositeDataTypeSubElementRef`             | [ ] Deferred| 46a5c6be3e                               | Group27          |
| `ApplicationCompositeElementDataPrototype`              | [x] Done    | 031d5c7848                               | Group2           |
| `ApplicationCompositeElementInPortInterfaceInstanceRef` | [x] Done    | 399b647757                               | Group2           |
| `ApplicationDataType`                                   | [x] Done    | b8d0878d98                               | Group2           |
| `ApplicationDeferredDataType`                           | [x] Done    | abdfbf1d96                               | Group1           |
| `ApplicationEndpoint`                                   | [ ] Deferred| N/A                                      | Group32          |
| `ApplicationEntry`                                      | [x] Done    | 8a6c27cb1c                               | Group17          |
| `ApplicationError`                                      | [ ] Deferred| 10a69b5248                               | Group27          |
| `ApplicationInterface`                                  | [ ] Implemented| N/A                                      | Group36          |
| `ApplicationPartition`                                  | [ ] Deferred| 9241a3d9f5                               | Group30          |
| `ApplicationPartitionToEcuPartitionMapping`             | [x] Done    | baccb40d25                               | Group18          |
| `ApplicationPrimitiveDataType`                          | [x] Done    | 4a9ccae9b8                               | Group2           |
| `ApplicationRecordDataType`                             | [x] Deferred| 0a06e0fae3                               | Group2           |
| `ApplicationRecordElement`                              | [x] Done    | ae4ed75065                               | Group2           |
| `ApplicationRuleBasedValueSpecification`                | [ ] Deferred| 1e72f8e31d                               | Group28          |
| `ApplicationSwComponentType`                            | [ ] Deferred| 31ce617eb9                               | Group27          |
| `ApplicationValueSpecification`                         | [ ] Deferred| a53eb77d97                               | Group28          |
| `ArParameterInImplementationDataInstanceRef`            | [ ] Deferred| N/A                                      | Group28          |
| `ArVariableInImplementationDataInstanceRef`             | [x] Done    | 910009eecc                               | Group2           |
| `ArbitraryEventTriggering`                              | [ ] Deferred| N/A                                      | Group35          |
| `Area`                                                  | [x] Done    | c9f2464902                               | Group3           |
| `AreaEnumNohref`                                        | [x] Done    | 1d6f8c0aa9                               | Group3           |
| `AreaEnumShape`                                         | [x] Done    | 966320f6a7                               | Group3           |
| `ArgumentDataPrototype`                                 | [ ] Deferred| 6f30a16016                               | Group27          |
| `ArgumentDirectionEnum`                                 | [x] Done    | 8b7ab62280                               | Group22          |
| `ArrayImplPolicyEnum`                                   | [x] Done    | 700b032789                               | Group10          |
| `ArraySizeHandlingEnum`                                 | [ ] Deferred| N/A                                      | Group28          |
| `ArraySizeSemanticsEnum`                                | [ ] Deferred| N/A                                      | Group28          |
| `ArrayValueSpecification`                               | [x] Done    | 043de7436d                               | Group3           |
| `AsamRecordLayoutSemantics`                             | [x] Done    | 2acaf7a45f                               | Group3           |
| `AssemblySwConnector`                                   | [x] Done    | 2a104a061c                               | Group2           |
| `AssignFrameId`                                         | [ ] Implemented| N/A                                      | Group31          |
| `AssignFrameIdRange`                                    | [ ] Implemented| N/A                                      | Group31          |
| `AssignNad`                                             | [ ] Implemented| N/A                                      | Group31          |
| `AsynchronousServerCallPoint`                           | [x] Done    | 3223dde420                               | Group2           |
| `AsynchronousServerCallResultPoint`                     | [x] Done    | 724f490c7a                               | Group2           |
| `AsynchronousServerCallReturnsEvent`                    | [x] Done    | a706fd368b                               | Group12          |
| `AtomicSwComponentType`                                 | [ ] Deferred| 184f2d7e82                               | Group27          |
| `AtpBlueprint`                                          | [x] Done    | 043de7436d                               | Group1           |
| `AtpBlueprintMapping`                                   | [x] Done    | 493e272da6                               | Group1           |
| `AtpBlueprintable`                                      | [x] Done    | b7cf03094f                               | Group1           |
| `AtpDefinition`                                         | [x] Done    | 38eb1e817c                               | Group1           |
| `AtpPrototype`                                          | [x] Done    | eb4c4bf308                               | Group1           |
| `AtpStructureElement`                                   | [x] Done    | 5eff088fa5                               | Group1           |
| `AtpType`                                               | [x] Done    | 451ad38330                               | Group1           |
| `AttributeCondition`                                    | [ ] Created | N/A                                      | Group36          |
| `AttributeTailoring`                                    | [ ] Created | N/A                                      | Group36          |
| `AttributeValueVariationPoint`                          | [x] Done    | d5c96fd954                               | Group8           |
| `AutoCollectEnum`                                       | [x] Done    | 75f4005552                               | Group1           |
| `AutosarDataPrototype`                                  | [ ] Deferred| N/A                                      | Group28          |
| `AutosarDataType`                                       | [x] Done    | a5f99df464                               | Group1           |
| `AutosarEngineeringObject`                              | [x] Done    | e485a5bcb2                               | Group22          |
| `AutosarOperationArgumentInstance`                      | [x] Done    | b8cce0057f                               | Group8           |
| `AutosarParameterRef`                                   | [x] Done    | b530f7e446                               | Group10          |
| `AutosarVariableInstance`                               | [ ] Deferred| N/A                                      | Group35          |
| `AutosarVariableRef`                                    | [x] Done    | d1b9384acc                               | Group10          |
| `BackgroundEvent`                                       | [x] Done    | 27b88a942c                               | Group2           |
| `BaseType`                                              | [ ] Deferred| N/A                                      | Group28          |
| `BaseTypeDefinition`                                    | [ ] Deferred| N/A                                      | Group28          |
| `BaseTypeDirectDefinition`                              | [ ] Deferred| N/A                                      | Group28          |
| `Baseline`                                              | [ ] Created | N/A                                      | Group36          |
| `BinaryManifestAddressableObject`                       | [ ] Created | N/A                                      | Group34          |
| `BinaryManifestItem`                                    | [ ] Created | N/A                                      | Group34          |
| `BinaryManifestItemDefinition`                          | [ ] Created | N/A                                      | Group34          |
| `BinaryManifestItemNumericalValue`                      | [ ] Created | N/A                                      | Group34          |
| `BinaryManifestItemPointerValue`                        | [ ] Created | N/A                                      | Group34          |
| `BinaryManifestItemValue`                               | [ ] Created | N/A                                      | Group34          |
| `BinaryManifestMetaDataField`                           | [ ] Deferred| N/A                                      | Group35          |
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
| `BswApiOptions`                                         | [x] Done    | 816c64f3d0                               | Group13          |
| `BswAsynchronousServerCallPoint`                        | [x] Done    | 80c7276bff                               | Group22          |
| `BswAsynchronousServerCallResultPoint`                  | [x] Done    | e1150436c3                               | Group22          |
| `BswAsynchronousServerCallReturnsEvent`                 | [x] Done    | f2df52d4b5                               | Group13          |
| `BswBackgroundEvent`                                    | [x] Done    | 584344d2e4                               | Group22          |
| `BswCallType`                                           | [x] Done    | 1a5b05b196                               | Group22          |
| `BswCalledEntity`                                       | [x] Done    | bd96645681                               | Group22          |
| `BswClientPolicy`                                       | [x] Done    | 3141824107                               | Group4           |
| `BswCompositionTiming`                                  | [ ] Deferred| N/A                                      | Group35          |
| `BswDataReceivedEvent`                                  | [x] Done    | e316f1e6ea                               | Group13          |
| `BswDataReceptionPolicy`                                | [x] Done    | 893f5df32e                               | Group13          |
| `BswDataSendPolicy`                                     | [x] Done    | ccacff4a64                               | Group4           |
| `BswDirectCallPoint`                                    | [x] Done    | 518ebf6a09                               | Group13          |
| `BswDistinguishedPartition`                             | [x] Done    | 80d341994f                               | Group22          |
| `BswEntryKindEnum`                                      | [x] Done    | 1a5b05b196                               | Group22          |
| `BswEntryRelationship`                                  | [x] Done    | 1872edcae1                               | Group13          |
| `BswEntryRelationshipEnum`                              | [x] Done    | ff1903b513                               | Group13          |
| `BswEntryRelationshipSet`                               | [x] Done    | cdbfc4ebf0                               | Group13          |
| `BswEvent`                                              | [x] Done    | af5498712f                               | Group22          |
| `BswExclusiveAreaPolicy`                                | [ ] Deferred| eb307c9898                               | Group22          |
| `BswExecutionContext`                                   | [x] Done    | 1a5b05b196                               | Group22          |
| `BswExternalTriggerOccurredEvent`                       | [ ] Deferred| a52b41da2c                               | Group22          |
| `BswImplementation`                                     | [x] Done    | 46ce237162                               | Group22          |
| `BswInternalBehavior`                                   | [x] Done    | 89a7231799                               | Group4           |
| `BswInternalTriggerOccurredEvent`                       | [x] Done    | caffd21921                               | Group13          |
| `BswInternalTriggeringPoint`                            | [x] Done    | f67e3865ef                               | Group13          |
| `BswInternalTriggeringPointPolicy`                      | [x] Done    | 2bb8413910                               | Group4           |
| `BswInterruptCategory`                                  | [ ] Deferred| 87a572d24b                               | Group22          |
| `BswInterruptEntity`                                    | [x] Done    | f19be09d07                               | Group13          |
| `BswInterruptEvent`                                     | [x] Done    | acf1e772ac                               | Group22          |
| `BswMgrNeeds`                                           | [x] Done    | 628464ed64                               | Group4           |
| `BswModeManagerErrorEvent`                              | [x] Done    | 91083c1916                               | Group13          |
| `BswModeReceiverPolicy`                                 | [ ] Deferred| 2b15f92b16                               | Group22          |
| `BswModeSenderPolicy`                                   | [ ] Deferred| af6d69bbfa                               | Group22          |
| `BswModeSwitchAckRequest`                               | [x] Done    | 8d9cad6b3c                               | Group13          |
| `BswModeSwitchEvent`                                    | [x] Done    | af5498712f                               | Group22          |
| `BswModeSwitchedAckEvent`                               | [x] Done    | a250dbe4b5                               | Group13          |
| `BswModuleCallPoint`                                    | [x] Done    | 879aacf8c4                               | Group13          |
| `BswModuleClientServerEntry`                            | [x] Done    | f57417a6a2                               | Group13          |
| `BswModuleDependency`                                   | [x] Done    | 7686874a67                               | Group13          |
| `BswModuleDescription`                                  | [x] Done    | 1a5b05b196                               | Group22          |
| `BswModuleEntity`                                       | [x] Done    | 88b336bfe9                               | Group22          |
| `BswModuleEntry`                                        | [x] Done    | 1a5b05b196                               | Group22          |
| `BswModuleTiming`                                       | [ ] Deferred| N/A                                      | Group35          |
| `BswOperationInvokedEvent`                              | [ ] Deferred| dc465f6b33                               | Group22          |
| `BswOsTaskExecutionEvent`                               | [x] Done    | 2b4b89810a                               | Group22          |
| `BswParameterPolicy`                                    | [x] Done    | eceaef9296                               | Group4           |
| `BswPerInstanceMemoryPolicy`                            | [x] Done    | b89ad783a3                               | Group4           |
| `BswQueuedDataReceptionPolicy`                          | [x] Done    | 254de705ea                               | Group13          |
| `BswReleasedTriggerPolicy`                              | [x] Done    | 04498e5b27                               | Group4           |
| `BswSchedulableEntity`                                  | [x] Done    | d2e2d7903d                               | Group22          |
| `BswScheduleEvent`                                      | [x] Done    | 46ce237162                               | Group22          |
| `BswSchedulerNamePrefix`                                | [x] Done    | 2a4f60c8c4                               | Group22          |
| `BswServiceDependency`                                  | [x] Done    | N/A                                      | Group23          |
| `BswServiceDependencyIdent`                             | [x] Done    | d488a5e4a8                               | Group26          |
| `BswSynchronousServerCallPoint`                         | [x] Done    | f23ec00417                               | Group13          |
| `BswTimingEvent`                                        | [x] Done    | 361ab10d5e                               | Group13          |
| `BswTriggerDirectImplementation`                        | [ ] Deferred| 0626aec9ca                               | Group22          |
| `BswVariableAccess`                                     | [ ] Deferred| d4d386b5c4                               | Group22          |
| `BufferProperties`                                      | [ ] Deferred| N/A                                      | Group28          |
| `BuildAction`                                           | [x] Done    | 6c9ef66b40                               | Group1           |
| `BuildActionEntity`                                     | [x] Done    | d7717e736a                               | Group1           |
| `BuildActionEnvironment`                                | [x] Done    | 2311c8754f                               | Group1           |
| `BuildActionInvocator`                                  | [x] Done    | 7008d5e857                               | Group1           |
| `BuildActionIoElement`                                  | [x] Done    | b572582c11                               | Group1           |
| `BuildActionManifest`                                   | [x] Done    | e6dcc8e79f                               | Group1           |
| `BuildEngineeringObject`                                | [x] Done    | 96d176ed20                               | Group1           |
| `BulkNvDataDescriptor`                                  | [x] Done    | 14a0a9cc5b                               | Group10          |
| `BurstPatternEventTriggering`                           | [ ] Deferred| N/A                                      | Group35          |
| `BusMirrorCanIdRangeMapping`                            | [ ] Deferred| N/A                                      | Group34          |
| `BusMirrorCanIdToCanIdMapping`                          | [ ] Deferred| N/A                                      | Group34          |
| `BusMirrorChannel`                                      | [ ] Created | N/A                                      | Group33          |
| `BusMirrorChannelMapping`                               | [ ] Implemented| N/A                                      | Group33          |
| `BusMirrorChannelMappingCan`                            | [ ] Deferred| N/A                                      | Group34          |
| `BusMirrorChannelMappingFlexray`                        | [ ] Deferred| N/A                                      | Group34          |
| `BusMirrorChannelMappingIp`                             | [ ] Deferred| N/A                                      | Group34          |
| `BusMirrorChannelMappingUserDefined`                    | [ ] Deferred| N/A                                      | Group34          |
| `BusMirrorLinPidToCanIdMapping`                         | [ ] Deferred| N/A                                      | Group34          |
| `BusspecificNmEcu`                                      | [ ] Implemented| N/A                                      | Group33          |
| `ByteOrderEnum`                                         | [ ] Deferred| N/A                                      | Group28          |
| `CIdentifier`                                           | [ ] Deferred| N/A                                      | Group21          |
| `CSTransformerErrorReactionEnum`                        | [ ] Deferred| N/A                                      | Group34          |
| `CalibrationParameterValue`                             | [ ] Deferred| 253d938ab0                               | Group28          |
| `CalibrationParameterValueSet`                          | [ ] Deferred| 92d3b31318                               | Group28          |
| `CalprmAxisCategoryEnum`                                | [ ] Deferred| N/A                                      | Group28          |
| `CanAddressingModeType`                                 | [ ] Deferred| N/A                                      | Group32          |
| `CanCluster`                                            | [ ] Deferred| ec69750f14                               | Group29          |
| `CanClusterBusOffRecovery`                              | [x] Done    | 9c4a146ff0                               | Group17          |
| `CanCommunicationConnector`                             | [x] Done    | 6e9794500d                               | Group17          |
| `CanCommunicationController`                            | [ ] Deferred| 250fded7cd                               | Group29          |
| `CanControllerConfiguration`                            | [x] Done    | 5de9869ed6                               | Group17          |
| `CanControllerConfigurationRequirements`                | [x] Done    | cd843bee26                               | Group17          |
| `CanControllerFdConfiguration`                          | [ ] Deferred| 3cd3adcdc4                               | Group29          |
| `CanControllerFdConfigurationRequirements`              | [x] Done    | a115435650                               | Group17          |
| `CanControllerXlConfiguration`                          | [ ] Deferred| 55877d3a96                               | Group29          |
| `CanControllerXlConfigurationRequirements`              | [ ] Deferred| 4e35a9d3b4                               | Group29          |
| `CanFrame`                                              | [ ] Deferred| N/A                                      | Group32          |
| `CanFrameRxBehaviorEnum`                                | [ ] Deferred| N/A                                      | Group32          |
| `CanFrameTriggering`                                    | [ ] Deferred| N/A                                      | Group32          |
| `CanFrameTxBehaviorEnum`                                | [ ] Deferred| N/A                                      | Group32          |
| `CanGlobalTimeDomainProps`                              | [ ] Created | N/A                                      | Group34          |
| `CanNmCluster`                                          | [x] Done    | 97b3ffb12e                               | Group18          |
| `CanNmClusterCoupling`                                  | [x] Done    | 8561fbb806                               | Group18          |
| `CanNmEcu`                                              | [ ] Implemented| N/A                                      | Group33          |
| `CanNmNode`                                             | [x] Done    | 3d406b5e98                               | Group18          |
| `CanPhysicalChannel`                                    | [ ] Deferred| 10e6b6aab3                               | Group29          |
| `CanTpAddress`                                          | [ ] Deferred| N/A                                      | Group33          |
| `CanTpAddressingFormatType`                             | [ ] Deferred| N/A                                      | Group33          |
| `CanTpChannel`                                          | [ ] Deferred| N/A                                      | Group33          |
| `CanTpConfig`                                           | [ ] Deferred| N/A                                      | Group33          |
| `CanTpConnection`                                       | [ ] Deferred| N/A                                      | Group33          |
| `CanTpEcu`                                              | [ ] Deferred| N/A                                      | Group33          |
| `CanTpNode`                                             | [ ] Deferred| N/A                                      | Group33          |
| `CategoryString`                                        | [ ] Deferred| N/A                                      | Group21          |
| `Chapter`                                               | [x] Done    | 0d13ccd1bc                               | Group22          |
| `ChapterContent`                                        | [x] Done    | dee07d0a3a                               | Group9           |
| `ChapterEnumBreak`                                      | [x] Done    | 20e6ee88d0                               | Group3           |
| `ChapterModel`                                          | [x] Done    | d3d61c9b2e                               | Group9           |
| `ChapterOrMsrQuery`                                     | [x] Done    | 0d13ccd1bc                               | Group22          |
| `ClassContentConditional`                               | [ ] Created | N/A                                      | Group36          |
| `ClassTailoring`                                        | [ ] Created | N/A                                      | Group36          |
| `ClientComSpec`                                         | [ ] Deferred| 1a86c955e2                               | Group27          |
| `ClientIdDefinition`                                    | [x] Done    | 8618ec8872                               | Group5           |
| `ClientIdDefinitionSet`                                 | [x] Done    | 01759771dd                               | Group5           |
| `ClientIdRange`                                         | [x] Done    | fce66955f5                               | Group5           |
| `ClientServerAnnotation`                                | [ ] Deferred| a5e2f7c628                               | Group27          |
| `ClientServerApplicationErrorMapping`                   | [x] Done    | bc933575fd                               | Group11          |
| `ClientServerInterface`                                 | [ ] Deferred| d1b24784a9                               | Group27          |
| `ClientServerInterfaceMapping`                          | [x] Done    | cae5a51c92                               | Group11          |
| `ClientServerOperation`                                 | [ ] Deferred| 15345a61f7                               | Group27          |
| `ClientServerOperationBlueprintMapping`                 | [ ] Created | N/A                                      | Group36          |
| `ClientServerOperationComProps`                         | [ ] Created | N/A                                      | Group34          |
| `ClientServerOperationMapping`                          | [x] Done    | e301de1df9                               | Group11          |
| `ClientServerToSignalMapping`                           | [ ] Deferred| N/A                                      | Group31          |
| `Code`                                                  | [x] Done    | 9f470606b5                               | Group1           |
| `CollectableElement`                                    | [x] Done    | 3b31b7c402                               | Group1           |
| `Collection`                                            | [x] Done    | 75f4005552                               | Group1           |
| `Colspec`                                               | [x] Done    | 2bd0d07503                               | Group3           |
| `ComManagementMapping`                                  | [x] Done    | 19c327cca6                               | Group5           |
| `ComMgrUserNeeds`                                       | [x] Done    | N/A                                      | Group23          |
| `CommConnectorPort`                                     | [ ] Deferred| ca22bc0a86                               | Group31          |
| `CommonSignalPath`                                      | [ ] Deferred| N/A                                      | Group31          |
| `CommunicationBufferLocking`                            | [x] Done    | 7c67628122                               | Group2           |
| `CommunicationCluster`                                  | [x] Done    | N/A                                      | Group24          |
| `CommunicationConnector`                                | [ ] Deferred| 7b29ffc2ba                               | Group29          |
| `CommunicationController`                               | [ ] Deferred| f3e797c458                               | Group27          |
| `CommunicationControllerMapping`                        | [x] Done    | 2613747d22                               | Group7           |
| `CommunicationCycle`                                    | [x] Done    | 75683a2ede                               | Group5           |
| `CommunicationDirectionType`                            | [x] Done    | 7aa197e046                               | Group15          |
| `Compiler`                                              | [x] Done    | 3fce597322                               | Group1           |
| `ComplexDeviceDriverSwComponentType`                    | [ ] Deferred| fa1d819e9d                               | Group29          |
| `ComponentClustering`                                   | [ ] Deferred| 6ddfdbb3f5                               | Group30          |
| `ComponentInCompositionInstanceRef`                     | [x] Done    | 02e863a567                               | Group7           |
| `ComponentInSystemInstanceRef`                          | [x] Done    | b511fb85b0                               | Group7           |
| `ComponentSeparation`                                   | [ ] Deferred| 525ff2c22c                               | Group30          |
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
| `ConcretePatternEventTriggering`                        | [ ] Deferred| N/A                                      | Group35          |
| `ConditionByFormula`                                    | [x] Done    | 18b494eba5                               | Group8           |
| `ConditionalChangeNad`                                  | [ ] Deferred| N/A                                      | Group32          |
| `ConfidenceInterval`                                    | [ ] Deferred| N/A                                      | Group35          |
| `ConfigReferenceValue`                                  | [x] Done    | 7ed4c9a4a4                               | Group19          |
| `ConsistencyNeeds`                                      | [ ] Deferred| N/A                                      | Group28          |
| `ConstantReference`                                     | [x] Done    | 4853348ea0                               | Group9           |
| `ConstantSpecification`                                 | [x] Done    | 265721a764                               | Group9           |
| `ConstantSpecificationMapping`                          | [ ] Deferred| 3c11d90872                               | Group28          |
| `ConstantSpecificationMappingSet`                       | [x] Done    | 8e5acbb2b1                               | Group1           |
| `ConstraintTailoring`                                   | [ ] Created | N/A                                      | Group36          |
| `ConsumedEventGroup`                                    | [ ] Deferred| N/A                                      | Group32          |
| `ConsumedProvidedServiceInstanceGroup`                  | [x] Done    | fce66955f5                               | Group5           |
| `ConsumedServiceInstance`                               | [ ] Deferred| N/A                                      | Group32          |
| `ContainedIPduCollectionSemanticsEnum`                  | [x] Done    | 64d125ffae                               | Group5           |
| `ContainedIPduProps`                                    | [x] Done    | 206cf29517                               | Group5           |
| `ContainerIPdu`                                         | [ ] Deferred| N/A                                      | Group31          |
| `ContainerIPduHeaderTypeEnum`                           | [ ] Deferred| N/A                                      | Group31          |
| `ContainerIPduTriggerEnum`                              | [ ] Deferred| N/A                                      | Group31          |
| `CouplingElement`                                       | [ ] Deferred| dccd25955a                               | Group30          |
| `CouplingElementAbstractDetails`                        | [ ] Deferred| 9c78940aa9                               | Group30          |
| `CouplingElementEnum`                                   | [ ] Deferred| cc75a503b1                               | Group30          |
| `CouplingElementSwitchDetails`                          | [ ] Deferred| d20dc66668                               | Group30          |
| `CouplingPort`                                          | [ ] Deferred| 51836c9a37                               | Group30          |
| `CouplingPortAbstractShaper`                            | [x] Done    | f02e111f65                               | Group16          |
| `CouplingPortAsynchronousTrafficShaper`                 | [x] Done    | 929cee7081                               | Group16          |
| `CouplingPortConnection`                                | [ ] Deferred| 7543596588                               | Group30          |
| `CouplingPortCreditBasedShaper`                         | [x] Done    | 929cee7081                               | Group16          |
| `CouplingPortDetails`                                   | [ ] Deferred| 7a56601b37                               | Group30          |
| `CouplingPortFifo`                                      | [ ] Deferred| 365e7aec38                               | Group30          |
| `CouplingPortRatePolicy`                                | [ ] Deferred| 9fafd3ebc2                               | Group30          |
| `CouplingPortRatePolicyActionEnum`                      | [ ] Deferred| 3f2c27ef2d                               | Group30          |
| `CouplingPortScheduler`                                 | [x] Done    | 0f61040c0c                               | Group6           |
| `CouplingPortShaper`                                    | [ ] Deferred| 5d3549490d                               | Group30          |
| `CouplingPortStructuralElement`                         | [x] Done    | 8404bbb94a                               | Group6           |
| `CouplingPortTrafficClassAssignment`                    | [ ] Deferred| aacc9860e9                               | Group30          |
| `CpSoftwareCluster`                                     | [x] Done    | 1194e00ca2                               | Group5           |
| `CpSoftwareClusterBinaryManifestDescriptor`             | [ ] Created | N/A                                      | Group34          |
| `CpSoftwareClusterCommunicationResource`                | [ ] Created | N/A                                      | Group34          |
| `CpSoftwareClusterCommunicationResourceProps`           | [ ] Created | N/A                                      | Group34          |
| `CpSoftwareClusterMappingSet`                           | [ ] Deferred| N/A                                      | Group31          |
| `CpSoftwareClusterResource`                             | [ ] Deferred| 9c0046237b                               | Group26          |
| `CpSoftwareClusterResourcePool`                         | [ ] Created | N/A                                      | Group34          |
| `CpSoftwareClusterResourceToApplicationPartitionMapping` | [ ] Deferred| N/A                                      | Group31          |
| `CpSoftwareClusterServiceResource`                      | [ ] Created | N/A                                      | Group34          |
| `CpSoftwareClusterToApplicationPartitionMapping`        | [ ] Deferred| N/A                                      | Group31          |
| `CpSoftwareClusterToEcuInstanceMapping`                 | [ ] Deferred| N/A                                      | Group31          |
| `CpSoftwareClusterToResourceMapping`                    | [ ] Created | N/A                                      | Group34          |
| `CpSwClusterResourceToDiagDataElemMapping`              | [ ] Deferred| 9c0046237b                               | Group26          |
| `CpSwClusterResourceToDiagFunctionIdMapping`            | [ ] Deferred| 9c0046237b                               | Group26          |
| `CpSwClusterToDiagEventMapping`                         | [ ] Deferred| 9c0046237b                               | Group26          |
| `CpSwClusterToDiagRoutineSubfunctionMapping`            | [ ] Deferred| 9c0046237b                               | Group26          |
| `CryptoCertificateAlgorithmFamilyEnum`                  | [x] Done    | 4c65329125                               | Group6           |
| `CryptoCertificateFormatEnum`                           | [x] Done    | 7fc9ab7674                               | Group6           |
| `CryptoEllipticCurveProps`                              | [x] Done    | d31256a6bc                               | Group6           |
| `CryptoKeyManagementNeeds`                              | [x] Done    | dc49a71665                               | Group4           |
| `CryptoKeySlot`                                         | [x] Done    | a02f617547                               | Group7           |
| `CryptoKeySlotAllowedModification`                      | [x] Done    | 1b9c5d5f92                               | Group20          |
| `CryptoKeySlotContentAllowedUsage`                      | [x] Done    | 0b871a8e8c                               | Group20          |
| `CryptoKeySlotTypeEnum`                                 | [x] Done    | cda30aac65                               | Group20          |
| `CryptoObjectTypeEnum`                                  | [x] Done    | 4ee3d9b33c                               | Group20          |
| `CryptoServiceCertificate`                              | [x] Done    | 757aea1d17                               | Group6           |
| `CryptoServiceJobNeeds`                                 | [x] Done    | 2ec474677a                               | Group4           |
| `CryptoServiceKey`                                      | [ ] Deferred| 7f0ee10676                               | Group31          |
| `CryptoServiceKeyGenerationEnum`                        | [ ] Deferred| 0ad977989f                               | Group31          |
| `CryptoServiceMapping`                                  | [x] Done    | 757aea1d17                               | Group6           |
| `CryptoServiceNeeds`                                    | [x] Done    | bea3457ed5                               | Group14          |
| `CryptoServicePrimitive`                                | [x] Done    | b609d72d59                               | Group6           |
| `CryptoServiceQueue`                                    | [ ] Deferred| eeb832d638                               | Group31          |
| `CryptoSignatureScheme`                                 | [x] Done    | 1eaeb5800b                               | Group6           |
| `CseCodeType`                                           | [ ] Deferred| N/A                                      | Group21          |
| `CycleCounter`                                          | [x] Done    | 75683a2ede                               | Group5           |
| `CycleRepetition`                                       | [x] Done    | 75683a2ede                               | Group5           |
| `CycleRepetitionType`                                   | [x] Done    | bf6cb0f022                               | Group5           |
| `CyclicTiming`                                          | [x] Done    | 7aa197e046                               | Group15          |
| `DataComProps`                                          | [ ] Created | N/A                                      | Group34          |
| `DataConsistencyPolicyEnum`                             | [ ] Deferred| N/A                                      | Group34          |
| `DataConstr`                                            | [x] Done    | 9927cc9e89                               | Group3           |
| `DataConstrRule`                                        | [x] Done    | fa640a0d86                               | Group3           |
| `DataDumpEntry`                                         | [ ] Deferred| N/A                                      | Group32          |
| `DataExchangePoint`                                     | [ ] Created | N/A                                      | Group36          |
| `DataExchangePointKind`                                 | [ ] Created | N/A                                      | Group36          |
| `DataFilter`                                            | [x] Done    | ed2a073e76                               | Group9           |
| `DataFilterTypeEnum`                                    | [x] Done    | b59bd6ebbe                               | Group9           |
| `DataFormatElementReference`                            | [ ] Created | N/A                                      | Group36          |
| `DataFormatElementScope`                                | [ ] Created | N/A                                      | Group36          |
| `DataIdModeEnum`                                        | [ ] Deferred| N/A                                      | Group34          |
| `DataInterface`                                         | [x] Done    | d838fd43f4                               | Group1           |
| `DataLimitKindEnum`                                     | [ ] Deferred| 87507e7bed                               | Group27          |
| `DataLinkLayerRule`                                     | [x] Done    | e65b8c621c                               | Group20          |
| `DataMapping`                                           | [x] Done    | dc0553786f                               | Group17          |
| `DataPrototype`                                         | [x] Done    | 9175595d88                               | Group1           |
| `DataPrototypeGroup`                                    | [ ] Deferred| N/A                                      | Group28          |
| `DataPrototypeInClientServerInterfaceInstanceRef`       | [ ] Deferred| N/A                                      | Group34          |
| `DataPrototypeInPortInterfaceRef`                       | [ ] Deferred| N/A                                      | Group34          |
| `DataPrototypeInSenderReceiverInterfaceInstanceRef`     | [ ] Deferred| N/A                                      | Group34          |
| `DataPrototypeMapping`                                  | [ ] Deferred| 2b08d90f5a                               | Group27          |
| `DataPrototypeReference`                                | [ ] Deferred| N/A                                      | Group34          |
| `DataPrototypeTransformationProps`                      | [x] Done    | ba255a82cc                               | Group6           |
| `DataReceiveErrorEvent`                                 | [x] Done    | b5ead83e20                               | Group12          |
| `DataReceivedEvent`                                     | [x] Done    | 5d23170856                               | Group12          |
| `DataSendCompletedEvent`                                | [x] Done    | 57e1abeea2                               | Group12          |
| `DataTransformation`                                    | [ ] Deferred| e34755cfd8                               | Group27          |
| `DataTransformationErrorHandlingEnum`                   | [x] Done    | 7fc79e4b73                               | Group2           |
| `DataTransformationKindEnum`                            | [ ] Deferred| 19d7d01e4d                               | Group27          |
| `DataTransformationSet`                                 | [x] Done    | 757aea1d17                               | Group6           |
| `DataTransformationStatusForwardingEnum`                | [x] Done    | 7c67628122                               | Group2           |
| `DataTypeMap`                                           | [x] Done    | 0731ff4f68                               | Group10          |
| `DataTypeMappingSet`                                    | [x] Done    | 21ab486b53                               | Group2           |
| `DataTypePolicyEnum`                                    | [ ] Implemented| N/A                                      | Group31          |
| `DataWriteCompletedEvent`                               | [x] Done    | df2a6b3a70                               | Group12          |
| `DateTime`                                              | [ ] Deferred| N/A                                      | Group21          |
| `DcmIPdu`                                               | [x] Deferred| edf35e5e2a                               | Group31          |
| `DdsCpConfig`                                           | [ ] Deferred| N/A                                      | Group32          |
| `DdsCpConsumedServiceInstance`                          | [ ] Deferred| N/A                                      | Group32          |
| `DdsCpISignalToDdsTopicMapping`                         | [ ] Deferred| N/A                                      | Group31          |
| `DdsCpPartition`                                        | [ ] Deferred| N/A                                      | Group32          |
| `DdsCpProvidedServiceInstance`                          | [ ] Deferred| N/A                                      | Group32          |
| `DdsCpQosProfile`                                       | [ ] Deferred| N/A                                      | Group32          |
| `DdsCpServiceInstance`                                  | [ ] Deferred| N/A                                      | Group32          |
| `DdsCpServiceInstanceEvent`                             | [ ] Deferred| N/A                                      | Group32          |
| `DdsCpServiceInstanceOperation`                         | [ ] Deferred| N/A                                      | Group32          |
| `DdsCpTopic`                                            | [ ] Deferred| N/A                                      | Group32          |
| `DdsDeadline`                                           | [ ] Deferred| N/A                                      | Group32          |
| `DdsDestinationOrder`                                   | [ ] Deferred| N/A                                      | Group32          |
| `DdsDestinationOrderKindEnum`                           | [ ] Deferred| N/A                                      | Group32          |
| `DdsDurability`                                         | [ ] Deferred| N/A                                      | Group32          |
| `DdsDurabilityKindEnum`                                 | [ ] Deferred| N/A                                      | Group32          |
| `DdsDurabilityService`                                  | [ ] Deferred| N/A                                      | Group32          |
| `DdsDurabilityServiceHistoryKindEnum`                   | [ ] Deferred| N/A                                      | Group32          |
| `DdsHistory`                                            | [ ] Deferred| N/A                                      | Group32          |
| `DdsHistoryKindEnum`                                    | [ ] Deferred| N/A                                      | Group32          |
| `DdsLatencyBudget`                                      | [ ] Deferred| N/A                                      | Group32          |
| `DdsLifespan`                                           | [ ] Deferred| N/A                                      | Group32          |
| `DdsLiveliness`                                         | [ ] Deferred| N/A                                      | Group32          |
| `DdsLivenessKindEnum`                                   | [ ] Deferred| N/A                                      | Group32          |
| `DdsOwnership`                                          | [ ] Deferred| N/A                                      | Group32          |
| `DdsOwnershipKindEnum`                                  | [ ] Deferred| N/A                                      | Group32          |
| `DdsOwnershipStrength`                                  | [ ] Deferred| N/A                                      | Group32          |
| `DdsReliability`                                        | [ ] Deferred| N/A                                      | Group32          |
| `DdsReliabilityKindEnum`                                | [ ] Deferred| N/A                                      | Group32          |
| `DdsResourceLimits`                                     | [ ] Deferred| N/A                                      | Group32          |
| `DdsTopicData`                                          | [ ] Deferred| N/A                                      | Group32          |
| `DdsTransportPriority`                                  | [ ] Deferred| N/A                                      | Group32          |
| `DefItem`                                               | [x] Deferred| N/A                                      | Group21          |
| `DefList`                                               | [x] Deferred| N/A                                      | Group21          |
| `DefaultValueApplicationStrategyEnum`                   | [ ] Created | N/A                                      | Group36          |
| `DefaultValueElement`                                   | [x] Done    | 721cca6400                               | Group17          |
| `DelegatedPortAnnotation`                               | [ ] Deferred| 1461e45c24                               | Group27          |
| `DelegationSwConnector`                                 | [x] Done    | 503344170e                               | Group2           |
| `DependencyOnArtifact`                                  | [x] Done    | 25211e56ca                               | Group1           |
| `DependencyUsageEnum`                                   | [x] Done    | 9a8c86ae9a                               | Group10          |
| `DevelopmentError`                                      | [x] Done    | N/A                                      | Group23          |
| `DhcpServerConfiguration`                               | [ ] Deferred| 64d337c40c                               | Group30          |
| `Dhcpv6Props`                                           | [ ] Deferred| 58cbdb9815                               | Group30          |
| `DiagEventDebounceAlgorithm`                            | [x] Done    | 4f246ae62d                               | Group4           |
| `DiagEventDebounceCounterBased`                         | [x] Done    | f41b486233                               | Group14          |
| `DiagEventDebounceMonitorInternal`                      | [x] Done    | 103cfd4316                               | Group4           |
| `DiagEventDebounceTimeBased`                            | [ ] Deferred| eb9e198676                               | Group23          |
| `DiagPduType`                                           | [x] Deferred| de6338d747                               | Group31          |
| `DiagRequirementIdString`                               | [ ] Deferred| N/A                                      | Group21          |
| `DiagnosticAbstractAliasEvent`                          | [ ] Deferred| 5ff78dec55                               | Group25          |
| `DiagnosticAbstractDataIdentifier`                      | [ ] Deferred| d32c585340                               | Group23          |
| `DiagnosticAbstractParameter`                           | [ ] Deferred| 6665fb7d71                               | Group23          |
| `DiagnosticAccessPermission`                            | [x] Done    | 9cbb4e26e7                               | Group7           |
| `DiagnosticAging`                                       | [ ] Deferred| c4704e8f01                               | Group25          |
| `DiagnosticAudienceEnum`                                | [x] Done    | 80d64e8f15                               | Group14          |
| `DiagnosticAuthRole`                                    | [ ] Deferred| 16e3c0c30d                               | Group23          |
| `DiagnosticAuthRoleProxy`                               | [x] Done    | 4579b43f0d                               | Group7           |
| `DiagnosticAuthTransmitCertificate`                     | [ ] Deferred| 94a9c9715c                               | Group24          |
| `DiagnosticAuthTransmitCertificateEvaluation`           | [ ] Deferred| 4a21071b3d                               | Group24          |
| `DiagnosticAuthTransmitCertificateMapping`              | [ ] Deferred| 531da6dd58                               | Group26          |
| `DiagnosticAuthentication`                              | [ ] Deferred| 13ac1a6b3d                               | Group24          |
| `DiagnosticAuthenticationClass`                         | [ ] Deferred| 50e51bce63                               | Group24          |
| `DiagnosticAuthenticationConfiguration`                 | [ ] Deferred| 3d83a383d7                               | Group24          |
| `DiagnosticCapabilityElement`                           | [x] Done    | caf7dc3419                               | Group14          |
| `DiagnosticClearDiagnosticInformation`                  | [ ] Deferred| 3165f87844                               | Group24          |
| `DiagnosticClearDiagnosticInformationClass`             | [ ] Deferred| b797bc6514                               | Group24          |
| `DiagnosticClearDtcLimitationEnum`                      | [ ] Deferred| 6b187ebfae                               | Group25          |
| `DiagnosticClearDtcNotificationEnum`                    | [x] Done    | 2415d2157a                               | Group14          |
| `DiagnosticClearEventAllowedBehaviorEnum`               | [ ] Deferred| 3ad75e1261                               | Group25          |
| `DiagnosticClearResetEmissionRelatedInfo`               | [ ] Deferred| 1d583075c7                               | Group25          |
| `DiagnosticClearResetEmissionRelatedInfoClass`          | [ ] Deferred| 95c27f01ee                               | Group25          |
| `DiagnosticComControl`                                  | [ ] Deferred| ed6ddee3af                               | Group24          |
| `DiagnosticComControlClass`                             | [ ] Deferred| cd8cd8c462                               | Group24          |
| `DiagnosticComControlSpecificChannel`                   | [ ] Deferred| c4bee1d353                               | Group24          |
| `DiagnosticComControlSubNodeChannel`                    | [ ] Deferred| f0a80d0b50                               | Group24          |
| `DiagnosticCommonElement`                               | [x] Done    | e0d022b1aa                               | Group7           |
| `DiagnosticCommonProps`                                 | [ ] Deferred| 0b2c7c2fa7                               | Group23          |
| `DiagnosticCommunicationManagerNeeds`                   | [x] Done    | 8c487102b9                               | Group14          |
| `DiagnosticCompareTypeEnum`                             | [ ] Deferred| cc55d1d351                               | Group23          |
| `DiagnosticComponentNeeds`                              | [x] Done    | 5c4c0963af                               | Group4           |
| `DiagnosticCondition`                                   | [ ] Deferred| 48dbae418f                               | Group25          |
| `DiagnosticConditionGroup`                              | [ ] Deferred| c04fdb8f07                               | Group25          |
| `DiagnosticConnectedIndicator`                          | [ ] Deferred| b2e6b63410                               | Group25          |
| `DiagnosticConnectedIndicatorBehaviorEnum`              | [ ] Deferred| faf9703711                               | Group25          |
| `DiagnosticConnection`                                  | [x] Done    | e96086c12f                               | Group5           |
| `DiagnosticContributionSet`                             | [ ] Deferred| 4c70e34d09                               | Group23          |
| `DiagnosticControlDTCSetting`                           | [ ] Deferred| a4ebfc734f                               | Group24          |
| `DiagnosticControlDTCSettingClass`                      | [ ] Deferred| 88c545f303                               | Group24          |
| `DiagnosticControlEnableMaskBit`                        | [ ] Deferred| e7a05b899d                               | Group24          |
| `DiagnosticControlNeeds`                                | [x] Done    | d0a1134e3b                               | Group4           |
| `DiagnosticCustomServiceClass`                          | [ ] Deferred| 259d8d82a3                               | Group23          |
| `DiagnosticCustomServiceInstance`                       | [ ] Deferred| 6beeb07b01                               | Group23          |
| `DiagnosticDataByIdentifier`                            | [ ] Deferred| 06afa0fffc                               | Group24          |
| `DiagnosticDataElement`                                 | [ ] Deferred| 04e40cda05                               | Group23          |
| `DiagnosticDataIdentifier`                              | [ ] Deferred| 18cb600978                               | Group23          |
| `DiagnosticDataIdentifierSet`                           | [ ] Deferred| 303f7cf31d                               | Group25          |
| `DiagnosticDataTransfer`                                | [ ] Deferred| 8d1719c7a9                               | Group24          |
| `DiagnosticDataTransferClass`                           | [ ] Deferred| 8d1719c7a9                               | Group24          |
| `DiagnosticDeAuthentication`                            | [ ] Deferred| 66e8ab9738                               | Group24          |
| `DiagnosticDebounceAlgorithmProps`                      | [ ] Deferred| 4a6604c7b5                               | Group25          |
| `DiagnosticDebounceBehaviorEnum`                        | [ ] Deferred| 165e554f17                               | Group25          |
| `DiagnosticDemProvidedDataMapping`                      | [ ] Deferred| 531da6dd58                               | Group26          |
| `DiagnosticDenominatorConditionEnum`                    | [x] Done    | N/A                                      | Group29          |
| `DiagnosticDynamicDataIdentifier`                       | [ ] Deferred| 6127bd9f00                               | Group23          |
| `DiagnosticDynamicallyDefineDataIdentifier`             | [ ] Deferred| 4988b642d4                               | Group24          |
| `DiagnosticDynamicallyDefineDataIdentifierClass`        | [ ] Deferred| 32e309baac                               | Group24          |
| `DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum` | [ ] Deferred| aa69f0bd9f                               | Group24          |
| `DiagnosticEcuInstanceProps`                            | [ ] Deferred| 84408cb8c9                               | Group25          |
| `DiagnosticEcuReset`                                    | [ ] Deferred| 4a568086da                               | Group24          |
| `DiagnosticEcuResetClass`                               | [ ] Deferred| 092a0c7cf2                               | Group24          |
| `DiagnosticEnableCondition`                             | [ ] Deferred| 3acb287717                               | Group25          |
| `DiagnosticEnableConditionGroup`                        | [ ] Deferred| ceea3ebd37                               | Group25          |
| `DiagnosticEnableConditionNeeds`                        | [x] Done    | N/A                                      | Group29          |
| `DiagnosticEnableConditionPortMapping`                  | [ ] Deferred| 266d4f7aa4                               | Group26          |
| `DiagnosticEnvBswModeElement`                           | [ ] Deferred| 9b90205857                               | Group23          |
| `DiagnosticEnvCompareCondition`                         | [x] Done    | e2c6fe29bb                               | Group14          |
| `DiagnosticEnvConditionFormula`                         | [x] Done    | 9f4e1849ac                               | Group14          |
| `DiagnosticEnvConditionFormulaPart`                     | [x] Done    | 66e22b5a41                               | Group14          |
| `DiagnosticEnvDataCondition`                            | [ ] Deferred| 19d7cb9cd6                               | Group23          |
| `DiagnosticEnvDataElementCondition`                     | [ ] Deferred| 519aca8534                               | Group23          |
| `DiagnosticEnvModeCondition`                            | [ ] Deferred| 4e6f0e3039                               | Group23          |
| `DiagnosticEnvModeElement`                              | [x] Done    | 513c78a4a8                               | Group14          |
| `DiagnosticEnvSwcModeElement`                           | [ ] Deferred| 4e64e33afe                               | Group23          |
| `DiagnosticEnvironmentalCondition`                      | [x] Done    | 5bbca5f217                               | Group7           |
| `DiagnosticEvent`                                       | [ ] Deferred| b1378989c8                               | Group25          |
| `DiagnosticEventClearAllowedEnum`                       | [ ] Deferred| 2bae144488                               | Group25          |
| `DiagnosticEventCombinationBehaviorEnum`                | [ ] Deferred| c5c9c65c4b                               | Group23          |
| `DiagnosticEventCombinationReportingBehaviorEnum`       | [ ] Deferred| d36baa82d6                               | Group23          |
| `DiagnosticEventDisplacementStrategyEnum`               | [ ] Deferred| 4a5813b099                               | Group25          |
| `DiagnosticEventInfoNeeds`                              | [x] Done    | 99f3db39c4                               | Group14          |
| `DiagnosticEventKindEnum`                               | [ ] Deferred| aa744716cf                               | Group25          |
| `DiagnosticEventManagerNeeds`                           | [x] Done    | dc34774429                               | Group4           |
| `DiagnosticEventNeeds`                                  | [x] Done    | N/A                                      | Group23          |
| `DiagnosticEventPortMapping`                            | [ ] Deferred| 266d4f7aa4                               | Group26          |
| `DiagnosticEventToDebounceAlgorithmMapping`             | [ ] Deferred| 664519e02e                               | Group26          |
| `DiagnosticEventToEnableConditionGroupMapping`          | [ ] Deferred| 664519e02e                               | Group26          |
| `DiagnosticEventToOperationCycleMapping`                | [ ] Deferred| 664519e02e                               | Group26          |
| `DiagnosticEventToSecurityEventMapping`                 | [ ] Deferred| 531da6dd58                               | Group26          |
| `DiagnosticEventToStorageConditionGroupMapping`         | [ ] Deferred| 664519e02e                               | Group26          |
| `DiagnosticEventToTroubleCodeJ1939Mapping`              | [ ] Deferred| 86bff0a4f2                               | Group26          |
| `DiagnosticEventToTroubleCodeUdsMapping`                | [ ] Deferred| 664519e02e                               | Group26          |
| `DiagnosticEventWindow`                                 | [ ] Deferred| e449ef97af                               | Group24          |
| `DiagnosticEventWindowTimeEnum`                         | [ ] Deferred| 2de5f4a019                               | Group24          |
| `DiagnosticExtendedDataRecord`                          | [ ] Deferred| a200a96695                               | Group25          |
| `DiagnosticFimAliasEvent`                               | [ ] Deferred| ea393b05d8                               | Group25          |
| `DiagnosticFimAliasEventGroup`                          | [ ] Deferred| d488a5e4a8                               | Group26          |
| `DiagnosticFimAliasEventGroupMapping`                   | [ ] Deferred| d488a5e4a8                               | Group26          |
| `DiagnosticFimAliasEventMapping`                        | [ ] Deferred| d488a5e4a8                               | Group26          |
| `DiagnosticFimEventGroup`                               | [ ] Deferred| N/A                                      | Group26          |
| `DiagnosticFimFunctionMapping`                          | [ ] Deferred| 86bff0a4f2                               | Group26          |
| `DiagnosticFreezeFrame`                                 | [ ] Deferred| 6c6c31d224                               | Group25          |
| `DiagnosticFunctionIdentifier`                          | [ ] Deferred| dc026145a3                               | Group25          |
| `DiagnosticFunctionIdentifierInhibit`                   | [ ] Deferred| 27e01b0795                               | Group25          |
| `DiagnosticFunctionInhibitSource`                       | [ ] Deferred| fd3444a79c                               | Group25          |
| `DiagnosticHandleDDDIConfigurationEnum`                 | [ ] Deferred| 3cde2dacdd                               | Group24          |
| `DiagnosticIOControl`                                   | [ ] Deferred| 3e204165ec                               | Group24          |
| `DiagnosticIndicator`                                   | [ ] Deferred| e603f3f050                               | Group25          |
| `DiagnosticIndicatorTypeEnum`                           | [x] Done    | N/A                                      | Group29          |
| `DiagnosticInfoType`                                    | [ ] Deferred| 87a45b092d                               | Group25          |
| `DiagnosticInhibitSourceEventMapping`                   | [ ] Deferred| d488a5e4a8                               | Group26          |
| `DiagnosticInhibitionMaskEnum`                          | [ ] Deferred| N/A                                      | Group26          |
| `DiagnosticIoControlClass`                              | [ ] Deferred| a6a5ff87e4                               | Group24          |
| `DiagnosticIoControlNeeds`                              | [x] Done    | N/A                                      | Group23          |
| `DiagnosticIumpr`                                       | [ ] Deferred| 3dce1b74b0                               | Group25          |
| `DiagnosticIumprDenominatorGroup`                       | [ ] Deferred| e1a516d394                               | Group25          |
| `DiagnosticIumprGroup`                                  | [ ] Deferred| 02133e7e76                               | Group25          |
| `DiagnosticIumprGroupIdentifier`                        | [ ] Deferred| 0b26bf6ac0                               | Group25          |
| `DiagnosticIumprKindEnum`                               | [ ] Deferred| 015af36ca8                               | Group25          |
| `DiagnosticIumprToFunctionIdentifierMapping`            | [ ] Deferred| 86bff0a4f2                               | Group26          |
| `DiagnosticJ1939ExpandedFreezeFrame`                    | [ ] Deferred| 0314338bf5                               | Group26          |
| `DiagnosticJ1939FreezeFrame`                            | [ ] Deferred| 0314338bf5                               | Group26          |
| `DiagnosticJ1939Node`                                   | [ ] Deferred| 86bff0a4f2                               | Group26          |
| `DiagnosticJ1939Spn`                                    | [ ] Deferred| ad6e53e6fe                               | Group26          |
| `DiagnosticJ1939SpnMapping`                             | [ ] Deferred| 86bff0a4f2                               | Group26          |
| `DiagnosticJ1939SwMapping`                              | [ ] Deferred| 86bff0a4f2                               | Group26          |
| `DiagnosticJumpToBootLoaderEnum`                        | [x] Done    | d901d9ee70                               | Group14          |
| `DiagnosticLogicalOperatorEnum`                         | [x] Done    | a70421898e                               | Group14          |
| `DiagnosticMapping`                                     | [ ] Deferred| fd3e548259                               | Group26          |
| `DiagnosticMasterToSlaveEventMapping`                   | [ ] Deferred| 531da6dd58                               | Group26          |
| `DiagnosticMeasurementIdentifier`                       | [ ] Deferred| 5d908b94d8                               | Group25          |
| `DiagnosticMemoryAddressableRangeAccess`                | [ ] Deferred| e6d1099722                               | Group24          |
| `DiagnosticMemoryByAddress`                             | [ ] Deferred| 97eb7a99d9                               | Group24          |
| `DiagnosticMemoryDestination`                           | [ ] Deferred| be5b392c44                               | Group25          |
| `DiagnosticMemoryDestinationPrimary`                    | [ ] Deferred| 9d32504d97                               | Group25          |
| `DiagnosticMemoryDestinationUserDefined`                | [ ] Deferred| 570c9983ad                               | Group25          |
| `DiagnosticMemoryEntryStorageTriggerEnum`               | [ ] Deferred| e550cdfbd3                               | Group25          |
| `DiagnosticMemoryIdentifier`                            | [ ] Deferred| 39631ea784                               | Group24          |
| `DiagnosticMonitorUpdateKindEnum`                       | [x] Done    | N/A                                      | Group29          |
| `DiagnosticObdSupportEnum`                              | [ ] Deferred| bfaab4368c                               | Group25          |
| `DiagnosticOccurrenceCounterProcessingEnum`             | [ ] Deferred| 5d402fe9da                               | Group23          |
| `DiagnosticOperationCycle`                              | [ ] Deferred| b5e7e1ec12                               | Group25          |
| `DiagnosticOperationCycleNeeds`                         | [x] Done    | N/A                                      | Group29          |
| `DiagnosticOperationCyclePortMapping`                   | [ ] Deferred| 266d4f7aa4                               | Group26          |
| `DiagnosticOperationCycleTypeEnum`                      | [ ] Deferred| 03a924f74f                               | Group25          |
| `DiagnosticParameter`                                   | [ ] Deferred| d1dafe3f06                               | Group23          |
| `DiagnosticParameterElement`                            | [ ] Deferred| e626d82fd2                               | Group23          |
| `DiagnosticParameterElementAccess`                      | [ ] Deferred| 80105a7831                               | Group26          |
| `DiagnosticParameterIdent`                              | [ ] Deferred| d666ff9ed7                               | Group23          |
| `DiagnosticParameterIdentifier`                         | [ ] Deferred| 69777441f4                               | Group24          |
| `DiagnosticParameterSupportInfo`                        | [ ] Deferred| 86cc1e2205                               | Group24          |
| `DiagnosticPeriodicRate`                                | [ ] Deferred| c3a080fdc4                               | Group24          |
| `DiagnosticPeriodicRateCategoryEnum`                    | [ ] Deferred| 051ec169f1                               | Group24          |
| `DiagnosticPowertrainFreezeFrame`                       | [ ] Deferred| b742a3633b                               | Group25          |
| `DiagnosticProcessingStyleEnum`                         | [x] Done    | d07b0d0144                               | Group14          |
| `DiagnosticProofOfOwnership`                            | [ ] Deferred| 3ef2fb8c98                               | Group24          |
| `DiagnosticProtocol`                                    | [ ] Deferred| 7324a51f2a                               | Group23          |
| `DiagnosticReadDTCInformation`                          | [ ] Deferred| 9ac51b650d                               | Group24          |
| `DiagnosticReadDTCInformationClass`                     | [ ] Deferred| 4b113a2dec                               | Group24          |
| `DiagnosticReadDataByIdentifier`                        | [ ] Deferred| e21b844ed0                               | Group24          |
| `DiagnosticReadDataByIdentifierClass`                   | [ ] Deferred| 01e18bd76d                               | Group24          |
| `DiagnosticReadDataByPeriodicID`                        | [ ] Deferred| 825e744a07                               | Group24          |
| `DiagnosticReadDataByPeriodicIDClass`                   | [ ] Deferred| d9cdc58eb4                               | Group24          |
| `DiagnosticReadMemoryByAddress`                         | [ ] Deferred| e0b6796763                               | Group24          |
| `DiagnosticReadMemoryByAddressClass`                    | [ ] Deferred| 314e86ace0                               | Group24          |
| `DiagnosticReadScalingDataByIdentifier`                 | [ ] Deferred| d8d4379d16                               | Group24          |
| `DiagnosticReadScalingDataByIdentifierClass`            | [ ] Deferred| 6c6eadab3d                               | Group24          |
| `DiagnosticRecordTriggerEnum`                           | [ ] Deferred| 38bfd94d4b                               | Group25          |
| `DiagnosticRequestControlOfOnBoardDevice`               | [ ] Deferred| a14b698533                               | Group25          |
| `DiagnosticRequestControlOfOnBoardDeviceClass`          | [ ] Deferred| a919e664e8                               | Group25          |
| `DiagnosticRequestCurrentPowertrainData`                | [ ] Deferred| 37165c5751                               | Group25          |
| `DiagnosticRequestCurrentPowertrainDataClass`           | [ ] Deferred| b278ba1550                               | Group25          |
| `DiagnosticRequestDownload`                             | [ ] Deferred| b24aedab49                               | Group24          |
| `DiagnosticRequestDownloadClass`                        | [ ] Deferred| 16a6c77acf                               | Group24          |
| `DiagnosticRequestEmissionRelatedDTC`                   | [ ] Deferred| 6e6de52f5d                               | Group25          |
| `DiagnosticRequestEmissionRelatedDTCClass`              | [ ] Deferred| 6112add0b4                               | Group25          |
| `DiagnosticRequestEmissionRelatedDTCPermanentStatus`    | [ ] Deferred| c50712427c                               | Group25          |
| `DiagnosticRequestEmissionRelatedDTCPermanentStatusClass` | [ ] Deferred| bc59ec221e                               | Group25          |
| `DiagnosticRequestFileTransfer`                         | [ ] Deferred| d34685d2ab                               | Group24          |
| `DiagnosticRequestFileTransferClass`                    | [ ] Deferred| 46f42c1284                               | Group24          |
| `DiagnosticRequestFileTransferNeeds`                    | [x] Done    | f084c4328c                               | Group4           |
| `DiagnosticRequestOnBoardMonitoringTestResults`         | [ ] Deferred| 5d8bb0b9aa                               | Group25          |
| `DiagnosticRequestOnBoardMonitoringTestResultsClass`    | [ ] Deferred| 445d4e053f                               | Group25          |
| `DiagnosticRequestPowertrainFreezeFrameData`            | [ ] Deferred| 1d44c26c8d                               | Group25          |
| `DiagnosticRequestPowertrainFreezeFrameDataClass`       | [ ] Deferred| 0f9475a2f5                               | Group25          |
| `DiagnosticRequestRoutineResults`                       | [ ] Deferred| c5c5cddd74                               | Group24          |
| `DiagnosticRequestUpload`                               | [ ] Deferred| 4c29de936a                               | Group24          |
| `DiagnosticRequestUploadClass`                          | [ ] Deferred| a5bf545f08                               | Group24          |
| `DiagnosticRequestVehicleInfo`                          | [ ] Deferred| a1dca9869b                               | Group25          |
| `DiagnosticRequestVehicleInfoClass`                     | [ ] Deferred| 4a2725a98e                               | Group25          |
| `DiagnosticResponseOnEvent`                             | [ ] Deferred| cd643b2b96                               | Group24          |
| `DiagnosticResponseOnEventActionEnum`                   | [ ] Deferred| 96ca415327                               | Group24          |
| `DiagnosticResponseOnEventClass`                        | [ ] Deferred| e39a10b0d8                               | Group24          |
| `DiagnosticResponseToEcuResetEnum`                      | [ ] Deferred| 4c37389432                               | Group24          |
| `DiagnosticRoutine`                                     | [ ] Deferred| 5f356c335d                               | Group24          |
| `DiagnosticRoutineControl`                              | [ ] Deferred| b7485f7941                               | Group24          |
| `DiagnosticRoutineControlClass`                         | [ ] Deferred| 4605fa8439                               | Group24          |
| `DiagnosticRoutineNeeds`                                | [x] Done    | 9f1a4310b7                               | Group14          |
| `DiagnosticRoutineSubfunction`                          | [ ] Deferred| 1b16d614ce                               | Group24          |
| `DiagnosticRoutineTypeEnum`                             | [x] Done    | f9dc536d57                               | Group14          |
| `DiagnosticSecurityAccess`                              | [ ] Deferred| 4b106b2461                               | Group24          |
| `DiagnosticSecurityAccessClass`                         | [ ] Deferred| 17ef969f39                               | Group24          |
| `DiagnosticSecurityEventReportingModeMapping`           | [ ] Deferred| 531da6dd58                               | Group26          |
| `DiagnosticSecurityLevel`                               | [x] Done    | f2da1338fc                               | Group7           |
| `DiagnosticServiceClass`                                | [x] Done    | d19685ff4f                               | Group14          |
| `DiagnosticServiceDataMapping`                          | [ ] Deferred| 80105a7831                               | Group26          |
| `DiagnosticServiceInstance`                             | [x] Done    | 6b514727f9                               | Group7           |
| `DiagnosticServiceMappingDiagTarget`                    | [ ] Deferred| 80105a7831                               | Group26          |
| `DiagnosticServiceRequestCallbackTypeEnum`              | [x] Done    | 77c7312cc8                               | Group14          |
| `DiagnosticServiceSwMapping`                            | [ ] Deferred| 0f2a3876e3                               | Group26          |
| `DiagnosticServiceTable`                                | [x] Done    | 9bd6fadae5                               | Group7           |
| `DiagnosticSession`                                     | [x] Done    | 06d4e49a26                               | Group7           |
| `DiagnosticSessionControl`                              | [ ] Deferred| a68f0804fd                               | Group23          |
| `DiagnosticSessionControlClass`                         | [ ] Deferred| 8145a0178a                               | Group24          |
| `DiagnosticSignificanceEnum`                            | [ ] Deferred| 9d20f1f7ce                               | Group25          |
| `DiagnosticStartRoutine`                                | [ ] Deferred| 30d5576f71                               | Group24          |
| `DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum` | [ ] Deferred| c97cedd4d1                               | Group25          |
| `DiagnosticStopRoutine`                                 | [ ] Deferred| 35e0590e6f                               | Group24          |
| `DiagnosticStorageCondition`                            | [ ] Deferred| bd5949a41b                               | Group25          |
| `DiagnosticStorageConditionGroup`                       | [ ] Deferred| 7b05bc91b8                               | Group25          |
| `DiagnosticStorageConditionNeeds`                       | [x] Done    | N/A                                      | Group29          |
| `DiagnosticStorageConditionPortMapping`                 | [ ] Deferred| 266d4f7aa4                               | Group26          |
| `DiagnosticSupportInfoByte`                             | [ ] Deferred| 80af808a62                               | Group25          |
| `DiagnosticSwMapping`                                   | [ ] Deferred| 80105a7831                               | Group26          |
| `DiagnosticTestIdentifier`                              | [ ] Deferred| f7cd643add                               | Group25          |
| `DiagnosticTestResult`                                  | [ ] Deferred| 30d1bea627                               | Group29          |
| `DiagnosticTestResultUpdateEnum`                        | [ ] Deferred| af61dd3966                               | Group25          |
| `DiagnosticTestRoutineIdentifier`                       | [ ] Deferred| 95790f92b8                               | Group25          |
| `DiagnosticTransferExit`                                | [ ] Deferred| 1461a0d679                               | Group24          |
| `DiagnosticTransferExitClass`                           | [ ] Deferred| 4c14a1b1d3                               | Group24          |
| `DiagnosticTroubleCode`                                 | [ ] Deferred| 086b29c68d                               | Group25          |
| `DiagnosticTroubleCodeGroup`                            | [ ] Deferred| 6e16251e8a                               | Group25          |
| `DiagnosticTroubleCodeJ1939`                            | [ ] Deferred| e51e632f04                               | Group26          |
| `DiagnosticTroubleCodeJ1939DtcKindEnum`                 | [ ] Deferred| e51e632f04                               | Group26          |
| `DiagnosticTroubleCodeObd`                              | [ ] Deferred| 5c4cbcc4b5                               | Group25          |
| `DiagnosticTroubleCodeProps`                            | [ ] Deferred| 39f801ec7e                               | Group25          |
| `DiagnosticTroubleCodeUds`                              | [ ] Deferred| fbead45f73                               | Group25          |
| `DiagnosticTroubleCodeUdsToTroubleCodeObdMapping`       | [ ] Deferred| 1f194826e7                               | Group25          |
| `DiagnosticTypeOfDtcSupportedEnum`                      | [ ] Deferred| 210840b945                               | Group23          |
| `DiagnosticTypeOfFreezeFrameRecordNumerationEnum`       | [ ] Deferred| 4e24dc1bed                               | Group25          |
| `DiagnosticUdsSeverityEnum`                             | [ ] Deferred| 056b7c5e0c                               | Group25          |
| `DiagnosticUploadDownloadNeeds`                         | [x] Done    | fe8a0a1a6d                               | Group4           |
| `DiagnosticValueAccessEnum`                             | [x] Done    | 85e9c3f3be                               | Group14          |
| `DiagnosticValueNeeds`                                  | [x] Done    | 475d150577                               | Group14          |
| `DiagnosticVerifyCertificateBidirectional`              | [ ] Deferred| 5f62e6dbb3                               | Group24          |
| `DiagnosticVerifyCertificateUnidirectional`             | [ ] Deferred| 682e50a2dd                               | Group24          |
| `DiagnosticWriteDataByIdentifier`                       | [ ] Deferred| 699b751820                               | Group24          |
| `DiagnosticWriteDataByIdentifierClass`                  | [ ] Deferred| 6f777e6bd6                               | Group24          |
| `DiagnosticWriteMemoryByAddress`                        | [ ] Deferred| 3400bec9c3                               | Group24          |
| `DiagnosticWriteMemoryByAddressClass`                   | [ ] Deferred| 223a5cbba7                               | Group24          |
| `DiagnosticWwhObdDtcClassEnum`                          | [ ] Deferred| 5663344175                               | Group25          |
| `DiagnosticsCommunicationSecurityNeeds`                 | [x] Done    | d24a66632e                               | Group4           |
| `DisplayPresentationEnum`                               | [ ] Deferred| c6c6c85d80                               | Group28          |
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
| `DoIpEntity`                                            | [x] Done    | a20bd931eb                               | Group16          |
| `DoIpEntityRoleEnum`                                    | [ ] Deferred| N/A                                      | Group32          |
| `DoIpGidNeeds`                                          | [x] Done    | 6c31e0057f                               | Group4           |
| `DoIpGidSynchronizationNeeds`                           | [x] Done    | c64cb6318c                               | Group4           |
| `DoIpInterface`                                         | [x] Done    | c53a7febdc                               | Group5           |
| `DoIpLogicAddress`                                      | [x] Done    | 20e0dbf1db                               | Group20          |
| `DoIpLogicTargetAddressProps`                           | [x] Done    | 64d125ffae                               | Group7           |
| `DoIpLogicTesterAddressProps`                           | [x] Done    | 64d125ffae                               | Group7           |
| `DoIpPowerModeStatusNeeds`                              | [x] Done    | 4350642e77                               | Group5           |
| `DoIpRoutingActivation`                                 | [x] Done    | c53a7febdc                               | Group5           |
| `DoIpRoutingActivationAuthenticationNeeds`              | [ ] Deferred| ee01eb9e60                               | Group29          |
| `DoIpRoutingActivationConfirmationNeeds`                | [ ] Deferred| ca6b7d152b                               | Group29          |
| `DoIpRule`                                              | [x] Done    | e1ebf1c4c5                               | Group20          |
| `DoIpServiceNeeds`                                      | [x] Done    | N/A                                      | Group23          |
| `DoIpTpConfig`                                          | [x] Done    | ac63e581b9                               | Group7           |
| `DoIpTpConnection`                                      | [x] Done    | b71da200f5                               | Group20          |
| `DocumentElementScope`                                  | [ ] Created | N/A                                      | Group36          |
| `DocumentViewSelectable`                                | [x] Done    | ba2c324b39                               | Group3           |
| `DocumentationBlock`                                    | [x] Deferred| N/A                                      | Group21          |
| `DocumentationContext`                                  | [x] Deferred| N/A                                      | Group21          |
| `DtcFormatTypeEnum`                                     | [x] Done    | f376d8339f                               | Group14          |
| `DtcKindEnum`                                           | [x] Done    | 8b62eec625                               | Group14          |
| `DtcStatusChangeNotificationNeeds`                      | [x] Done    | 89407b6f0f                               | Group14          |
| `DynamicPart`                                           | [x] Done    | 82138518f9                               | Group15          |
| `DynamicPartAlternative`                                | [x] Done    | 206cf29517                               | Group5           |
| `E2EProfileCompatibilityProps`                          | [ ] Deferred| N/A                                      | Group28          |
| `ECUMapping`                                            | [x] Done    | 34bb50d75e                               | Group7           |
| `EEnum`                                                 | [ ] Deferred| N/A                                      | Group21          |
| `EEnumFont`                                             | [ ] Deferred| N/A                                      | Group21          |
| `EOCEventRef`                                           | [ ] Deferred| N/A                                      | Group35          |
| `EOCExecutableEntityRef`                                | [ ] Deferred| N/A                                      | Group35          |
| `EOCExecutableEntityRefAbstract`                        | [ ] Deferred| N/A                                      | Group35          |
| `EOCExecutableEntityRefGroup`                           | [ ] Deferred| N/A                                      | Group35          |
| `EcuAbstractionSwComponentType`                         | [ ] Deferred| 7d89ea80c0                               | Group29          |
| `EcuInstance`                                           | [x] Done    | 206e89be41                               | Group5           |
| `EcuPartition`                                          | [x] Done    | c53a7febdc                               | Group5           |
| `EcuResourceEstimation`                                 | [ ] Deferred| N/A                                      | Group31          |
| `EcuStateMgrUserNeeds`                                  | [x] Done    | 6b31696dff                               | Group4           |
| `EcuTiming`                                             | [ ] Deferred| N/A                                      | Group35          |
| `EcucAbstractConfigurationClass`                        | [ ] Deferred| 6549a18aee                               | Group26          |
| `EcucAbstractExternalReferenceDef`                      | [ ] Deferred| af8e9109c7                               | Group26          |
| `EcucAbstractInternalReferenceDef`                      | [ ] Deferred| 0035a3d952                               | Group26          |
| `EcucAbstractReferenceDef`                              | [ ] Deferred| 1475d37c0d                               | Group26          |
| `EcucAbstractReferenceValue`                            | [ ] Deferred| b5f9232413                               | Group27          |
| `EcucAbstractStringParamDef`                            | [ ] Deferred| 024153f73a                               | Group26          |
| `EcucAddInfoParamDef`                                   | [ ] Deferred| cf5c0e3618                               | Group26          |
| `EcucAddInfoParamValue`                                 | [ ] Deferred| 0c30fe6b6b                               | Group27          |
| `EcucBooleanParamDef`                                   | [x] Done    | b40b99238a                               | Group19          |
| `EcucChoiceContainerDef`                                | [ ] Deferred| 416e583ff2                               | Group26          |
| `EcucChoiceReferenceDef`                                | [ ] Deferred| b85e3d5202                               | Group26          |
| `EcucCommonAttributes`                                  | [ ] Deferred| b5ba9d4e2f                               | Group26          |
| `EcucConditionFormula`                                  | [x] Done    | 86096857ad                               | Group19          |
| `EcucConditionSpecification`                            | [ ] Deferred| 901e5bb4c3                               | Group27          |
| `EcucConfigurationClassEnum`                            | [x] Done    | eb890b899c                               | Group19          |
| `EcucConfigurationVariantEnum`                          | [ ] Deferred| 5ce1bb021e                               | Group26          |
| `EcucContainerDef`                                      | [ ] Deferred| d497b88ae7                               | Group26          |
| `EcucContainerValue`                                    | [ ] Deferred| 319fcf7080                               | Group27          |
| `EcucDefinitionCollection`                              | [ ] Deferred| 4c76344b21                               | Group26          |
| `EcucDefinitionElement`                                 | [ ] Deferred| ac47ae89f3                               | Group26          |
| `EcucDerivationSpecification`                           | [ ] Deferred| 91a9e3ee35                               | Group26          |
| `EcucDestinationUriDef`                                 | [ ] Deferred| 2f69e3cc20                               | Group26          |
| `EcucDestinationUriDefRefType`                          | [x] Done    | 7047c575f7                               | Group19          |
| `EcucDestinationUriDefSet`                              | [ ] Deferred| f580ebdeec                               | Group26          |
| `EcucDestinationUriNestingContractEnum`                 | [ ] Deferred| 9a8cb02be7                               | Group26          |
| `EcucDestinationUriPolicy`                              | [ ] Deferred| 37330e12c0                               | Group26          |
| `EcucEnumerationLiteralDef`                             | [ ] Deferred| 48d98b4b49                               | Group26          |
| `EcucEnumerationParamDef`                               | [ ] Deferred| 5085d038de                               | Group26          |
| `EcucFloatParamDef`                                     | [x] Done    | 454e47206b                               | Group19          |
| `EcucForeignReferenceDef`                               | [x] Done    | 958007001d                               | Group19          |
| `EcucFunctionNameDef`                                   | [ ] Deferred| e44edd9d6d                               | Group26          |
| `EcucIndexableValue`                                    | [ ] Deferred| 7fa66d34f9                               | Group27          |
| `EcucInstanceReferenceDef`                              | [ ] Deferred| c27549b512                               | Group26          |
| `EcucInstanceReferenceValue`                            | [ ] Deferred| 9d34a15176                               | Group27          |
| `EcucIntegerParamDef`                                   | [ ] Deferred| 62c89e7a96                               | Group26          |
| `EcucLinkerSymbolDef`                                   | [x] Done    | 776f61b1df                               | Group19          |
| `EcucModuleConfigurationValues`                         | [ ] Deferred| 963ae8fcfc                               | Group27          |
| `EcucModuleDef`                                         | [ ] Deferred| 3dd8367d26                               | Group26          |
| `EcucMultilineStringParamDef`                           | [ ] Deferred| fdee6f9a41                               | Group26          |
| `EcucMultiplicityConfigurationClass`                    | [ ] Deferred| 6549a18aee                               | Group26          |
| `EcucNumericalParamValue`                               | [ ] Deferred| c2eb1c04d2                               | Group27          |
| `EcucParamConfContainerDef`                             | [ ] Deferred| 571d1bb8d7                               | Group26          |
| `EcucParameterDef`                                      | [ ] Deferred| bf479d9bf8                               | Group26          |
| `EcucParameterDerivationFormula`                        | [x] Done    | 16bd8cd3d0                               | Group19          |
| `EcucParameterValue`                                    | [ ] Deferred| de8db969b1                               | Group27          |
| `EcucQuery`                                             | [ ] Deferred| 8bb9dbd181                               | Group26          |
| `EcucQueryExpression`                                   | [x] Done    | a6ca958629                               | Group19          |
| `EcucReferenceDef`                                      | [x] Done    | 0d45067479                               | Group19          |
| `EcucReferenceValue`                                    | [ ] Deferred| 5986011aa6                               | Group27          |
| `EcucScopeEnum`                                         | [x] Done    | 096c9544fc                               | Group19          |
| `EcucStringParamDef`                                    | [ ] Deferred| 0e1c4660e5                               | Group26          |
| `EcucSymbolicNameReferenceDef`                          | [x] Done    | 0d45067479                               | Group19          |
| `EcucTextualParamValue`                                 | [ ] Deferred| b4a24a5d87                               | Group27          |
| `EcucUriReferenceDef`                                   | [x] Done    | 0d45067479                               | Group19          |
| `EcucValidationCondition`                               | [ ] Deferred| 401e19fd2d                               | Group27          |
| `EcucValueCollection`                                   | [x] Done    | b65b2313a2                               | Group19          |
| `EcucValueConfigurationClass`                           | [ ] Deferred| 6549a18aee                               | Group26          |
| `EmphasisText`                                          | [x] Deferred| N/A                                      | Group21          |
| `EndToEndDescription`                                   | [x] Done    | d3db89bb98                               | Group10          |
| `EndToEndProfileBehaviorEnum`                           | [ ] Deferred| N/A                                      | Group34          |
| `EndToEndProtection`                                    | [ ] Deferred| N/A                                      | Group28          |
| `EndToEndProtectionISignalIPdu`                         | [x] Done    | 7426eaaa52                               | Group18          |
| `EndToEndProtectionSet`                                 | [x] Done    | 4a7d82ffc7                               | Group5           |
| `EndToEndProtectionVariablePrototype`                   | [x] Done    | 4a7d82ffc7                               | Group5           |
| `EndToEndTransformationComSpecProps`                    | [ ] Deferred| N/A                                      | Group28          |
| `EndToEndTransformationDescription`                     | [ ] Deferred| N/A                                      | Group34          |
| `EndToEndTransformationISignalProps`                    | [x] Done    | 4c91e36810                               | Group18          |
| `Entry`                                                 | [x] Done    | 9005f6228e                               | Group3           |
| `ErrorTracerNeeds`                                      | [x] Done    | N/A                                      | Group23          |
| `EthGlobalTimeDomainProps`                              | [ ] Created | N/A                                      | Group34          |
| `EthGlobalTimeManagedCouplingPort`                      | [ ] Created | N/A                                      | Group34          |
| `EthGlobalTimeMessageFormatEnum`                        | [ ] Deferred| N/A                                      | Group34          |
| `EthIpProps`                                            | [ ] Deferred| 324da359ae                               | Group30          |
| `EthTSynCrcFlags`                                       | [ ] Created | N/A                                      | Group34          |
| `EthTSynSubTlvConfig`                                   | [ ] Created | N/A                                      | Group34          |
| `EthTcpIpIcmpProps`                                     | [x] Done    | c53a7febdc                               | Group5           |
| `EthTcpIpProps`                                         | [x] Done    | db98d8ff29                               | Group5           |
| `EthTpConfig`                                           | [ ] Deferred| N/A                                      | Group33          |
| `EthTpConnection`                                       | [ ] Deferred| N/A                                      | Group33          |
| `EthernetCluster`                                       | [ ] Deferred| 4b9d113878                               | Group29          |
| `EthernetCommunicationConnector`                        | [ ] Deferred| d22193a7d7                               | Group30          |
| `EthernetCommunicationController`                       | [ ] Deferred| 01e4db429e                               | Group30          |
| `EthernetConnectionNegotiationEnum`                     | [ ] Deferred| bc3d3386a2                               | Group30          |
| `EthernetCouplingPortSchedulerEnum`                     | [ ] Deferred| 909eb0ddcc                               | Group30          |
| `EthernetFrameTriggering`                               | [ ] Created | N/A                                      | Group33          |
| `EthernetMacLayerTypeEnum`                              | [ ] Deferred| d526c8ebcf                               | Group30          |
| `EthernetPhysicalChannel`                               | [x] Done    | 206cf29517                               | Group5           |
| `EthernetPhysicalLayerTypeEnum`                         | [ ] Deferred| 5eba7c6ad9                               | Group30          |
| `EthernetPriorityRegeneration`                          | [x] Done    | a513bd3ec3                               | Group16          |
| `EthernetSwitchVlanEgressTaggingEnum`                   | [ ] Deferred| 41795ad4b3                               | Group30          |
| `EthernetSwitchVlanIngressTagEnum`                      | [ ] Deferred| 0d682b9798                               | Group30          |
| `EthernetWakeupSleepOnDatalineConfig`                   | [ ] Deferred| e795dd3dc6                               | Group30          |
| `EthernetWakeupSleepOnDatalineConfigSet`                | [ ] Deferred| 2065193be7                               | Group30          |
| `EvaluatedVariantSet`                                   | [ ] Deferred| N/A                                      | Group21          |
| `EventAcceptanceStatusEnum`                             | [x] Done    | N/A                                      | Group29          |
| `EventControlledTiming`                                 | [x] Done    | 1649678501                               | Group15          |
| `EventGroupControlTypeEnum`                             | [ ] Deferred| N/A                                      | Group32          |
| `EventHandler`                                          | [ ] Deferred| N/A                                      | Group32          |
| `EventObdReadinessGroup`                                | [ ] Deferred| 51dbeac91d                               | Group25          |
| `EventOccurrenceKindEnum`                               | [ ] Deferred| N/A                                      | Group35          |
| `EventTriggeringConstraint`                             | [ ] Deferred| N/A                                      | Group35          |
| `ExclusiveArea`                                         | [x] Done    | aae3890b67                               | Group22          |
| `ExclusiveAreaNestingOrder`                             | [x] Done    | af5498712f                               | Group22          |
| `ExecutableEntity`                                      | [x] Done    | 88b336bfe9                               | Group22          |
| `ExecutableEntityActivationReason`                      | [ ] Deferred| 12b2493a29                               | Group28          |
| `ExecutionOrderConstraint`                              | [ ] Deferred| N/A                                      | Group35          |
| `ExecutionOrderConstraintTypeEnum`                      | [ ] Deferred| N/A                                      | Group35          |
| `ExecutionTime`                                         | [x] Done    | N/A                                      | Group23          |
| `ExecutionTimeConstraint`                               | [ ] Deferred| N/A                                      | Group35          |
| `ExecutionTimeTypeEnum`                                 | [ ] Deferred| N/A                                      | Group35          |
| `ExternalTriggerOccurredEvent`                          | [ ] Deferred| 84453723ad                               | Group28          |
| `ExternalTriggeringPoint`                               | [ ] Deferred| 49038a9617                               | Group29          |
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
| `FilterDebouncingEnum`                                  | [ ] Deferred| c23b544607                               | Group27          |
| `FirewallActionEnum`                                    | [x] Done    | ab2daa7785                               | Group3           |
| `FirewallRule`                                          | [x] Deferred| 00d011d4ad                               | Group1           |
| `FirewallRuleProps`                                     | [x] Done    | 89039bf2bb                               | Group7           |
| `FlatInstanceDescriptor`                                | [x] Done    | 9db34796eb                               | Group1           |
| `FlatMap`                                               | [x] Done    | 5eadca7853                               | Group1           |
| `FlexrayAbsolutelyScheduledTiming`                      | [x] Done    | 3ab64d2b03                               | Group17          |
| `FlexrayArTpChannel`                                    | [ ] Deferred| N/A                                      | Group33          |
| `FlexrayArTpConfig`                                     | [ ] Deferred| N/A                                      | Group33          |
| `FlexrayArTpConnection`                                 | [ ] Deferred| N/A                                      | Group33          |
| `FlexrayArTpNode`                                       | [ ] Deferred| N/A                                      | Group33          |
| `FlexrayChannelName`                                    | [x] Done    | f4ffa771cf                               | Group15          |
| `FlexrayCluster`                                        | [ ] Deferred| 00edf04e32                               | Group29          |
| `FlexrayCommunicationConnector`                         | [x] Done    | 73bba1d58a                               | Group17          |
| `FlexrayCommunicationController`                        | [x] Done    | 0c1ff9a927                               | Group17          |
| `FlexrayFifoConfiguration`                              | [ ] Deferred| d4975bcfb7                               | Group29          |
| `FlexrayFifoRange`                                      | [ ] Deferred| a2965515fb                               | Group29          |
| `FlexrayFrame`                                          | [x] Done    | 757aea1d17                               | Group6           |
| `FlexrayFrameTriggering`                                | [x] Done    | 3ab64d2b03                               | Group17          |
| `FlexrayNmCluster`                                      | [x] Done    | 9c8e10b37f                               | Group6           |
| `FlexrayNmClusterCoupling`                              | [x] Done    | 50b09ee73b                               | Group18          |
| `FlexrayNmEcu`                                          | [x] Done    | 9c8e10b37f                               | Group6           |
| `FlexrayNmNode`                                         | [x] Done    | 9c8e10b37f                               | Group6           |
| `FlexrayNmScheduleVariant`                              | [ ] Implemented| N/A                                      | Group33          |
| `FlexrayPhysicalChannel`                                | [x] Done    | 7774a8ec9b                               | Group17          |
| `FlexrayTpConfig`                                       | [ ] Deferred| N/A                                      | Group33          |
| `FlexrayTpConnection`                                   | [ ] Deferred| N/A                                      | Group33          |
| `FlexrayTpConnectionControl`                            | [ ] Deferred| N/A                                      | Group33          |
| `FlexrayTpEcu`                                          | [ ] Deferred| N/A                                      | Group33          |
| `FlexrayTpNode`                                         | [ ] Deferred| N/A                                      | Group33          |
| `FlexrayTpPduPool`                                      | [ ] Deferred| N/A                                      | Group33          |
| `FloatEnum`                                             | [x] Done    | 1649678501                               | Group22          |
| `FloatValueVariationPoint`                              | [x] Done    | d5c96fd954                               | Group8           |
| `FlowMeteringColorModeEnum`                             | [ ] Deferred| c140322c44                               | Group30          |
| `ForbiddenSignalPath`                                   | [ ] Deferred| N/A                                      | Group31          |
| `FormulaExpression`                                     | [x] Done    | 88ed82bed3                               | Group8           |
| `FrArTpAckType`                                         | [ ] Deferred| N/A                                      | Group33          |
| `FrGlobalTimeDomainProps`                               | [ ] Created | N/A                                      | Group34          |
| `Frame`                                                 | [ ] Implemented| N/A                                      | Group31          |
| `FrameEnum`                                             | [x] Done    | 531991e029                               | Group3           |
| `FrameMapping`                                          | [x] Done    | a5f62ee06d                               | Group17          |
| `FramePid`                                              | [ ] Implemented| N/A                                      | Group31          |
| `FramePort`                                             | [x] Done    | 75683a2ede                               | Group5           |
| `FrameTriggering`                                       | [x] Done    | 206cf29517                               | Group5           |
| `FreeFormat`                                            | [ ] Deferred| N/A                                      | Group32          |
| `FreeFormatEntry`                                       | [ ] Implemented| N/A                                      | Group31          |
| `FullBindingTimeEnum`                                   | [ ] Deferred| N/A                                      | Group21          |
| `FunctionInhibitionAvailabilityNeeds`                   | [x] Done    | N/A                                      | Group29          |
| `FunctionInhibitionNeeds`                               | [x] Done    | 5c4c0963af                               | Group4           |
| `FurtherActionByteNeeds`                                | [x] Done    | 30e266fd91                               | Group5           |
| `Gateway`                                               | [x] Done    | a00d99f993                               | Group17          |
| `GeneralAnnotation`                                     | [x] Done    | ab2daa7785                               | Group3           |
| `GeneralParameter`                                      | [x] Done    | b622d5b424                               | Group9           |
| `GeneralPurposeConnection`                              | [ ] Created | N/A                                      | Group31          |
| `GeneralPurposeIPdu`                                    | [x] Done    | 75683a2ede                               | Group5           |
| `GeneralPurposePdu`                                     | [x] Done    | 75683a2ede                               | Group5           |
| `GenericEthernetFrame`                                  | [x] Done    | 675a97e967                               | Group6           |
| `GenericTp`                                             | [x] Done    | 627b5c3a94                               | Group16          |
| `GlobalSupervisionNeeds`                                | [x] Done    | 5c4c0963af                               | Group4           |
| `GlobalTimeCanMaster`                                   | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeCanSlave`                                    | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeCorrectionProps`                             | [ ] Deferred| N/A                                      | Group34          |
| `GlobalTimeCouplingPortProps`                           | [ ] Deferred| N/A                                      | Group34          |
| `GlobalTimeCrcSupportEnum`                              | [ ] Deferred| N/A                                      | Group34          |
| `GlobalTimeCrcValidationEnum`                           | [ ] Deferred| N/A                                      | Group34          |
| `GlobalTimeDomain`                                      | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeEthMaster`                                   | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeEthSlave`                                    | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeFrMaster`                                    | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeFrSlave`                                     | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeGateway`                                     | [ ] Created | N/A                                      | Group34          |
| `GlobalTimeIcvSupportEnum`                              | [ ] Deferred| N/A                                      | Group34          |
| `GlobalTimeIcvVerificationEnum`                         | [ ] Deferred| N/A                                      | Group34          |
| `GlobalTimeMaster`                                      | [ ] Created | N/A                                      | Group34          |
| `GlobalTimePortRoleEnum`                                | [ ] Deferred| N/A                                      | Group34          |
| `GlobalTimeSlave`                                       | [ ] Created | N/A                                      | Group34          |
| `Graphic`                                               | [x] Done    | 06b46f32ba                               | Group3           |
| `GraphicFitEnum`                                        | [x] Done    | 5b543a21d4                               | Group3           |
| `GraphicNotationEnum`                                   | [x] Done    | f25e765d8b                               | Group3           |
| `HandleInvalidEnum`                                     | [x] Done    | 18271ddd84                               | Group1           |
| `HandleOutOfRangeEnum`                                  | [ ] Deferred| fd8d9ec9f7                               | Group27          |
| `HandleOutOfRangeStatusEnum`                            | [ ] Deferred| N/A                                      | Group27          |
| `HandleTimeoutEnum`                                     | [ ] Deferred| cd413d6680                               | Group27          |
| `HardwareConfiguration`                                 | [x] Done    | 3f0dca5050                               | Group20          |
| `HardwareTestNeeds`                                     | [x] Done    | 5c4c0963af                               | Group4           |
| `HeapUsage`                                             | [x] Done    | a55d2092d0                               | Group22          |
| `HttpTp`                                                | [ ] Deferred| N/A                                      | Group32          |
| `HwAttributeDef`                                        | [x] Done    | 3912963bfd                               | Group7           |
| `HwAttributeLiteralDef`                                 | [x] Done    | 5d767ace9e                               | Group7           |
| `HwAttributeValue`                                      | [x] Done    | 269d34d90f                               | Group7           |
| `HwCategory`                                            | [x] Done    | b7e2199ac8                               | Group7           |
| `HwDescriptionEntity`                                   | [ ] Deferred| 8a55380861                               | Group27          |
| `HwElement`                                             | [x] Done    | 8c7f05d40a                               | Group1           |
| `HwElementConnector`                                    | [ ] Deferred| f48bef4731                               | Group27          |
| `HwPin`                                                 | [x] Done    | ff5b0e0865                               | Group1           |
| `HwPinConnector`                                        | [ ] Deferred| 2bf0929ad2                               | Group27          |
| `HwPinGroup`                                            | [x] Done    | 69afffcc48                               | Group1           |
| `HwPinGroupConnector`                                   | [ ] Deferred| acdd47866a                               | Group27          |
| `HwPinGroupContent`                                     | [ ] Deferred| cb322b20cb                               | Group27          |
| `HwPortMapping`                                         | [x] Done    | 7d94510497                               | Group7           |
| `HwType`                                                | [x] Done    | 29f338b3c0                               | Group1           |
| `IEEE1722TpAafAes3DataTypeEnum`                         | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAafConnection`                               | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAafFormatEnum`                               | [ ] Deferred| N/A                                      | Group33          |
| `IEEE1722TpAafNominalRateEnum`                          | [ ] Deferred| N/A                                      | Group33          |
| `IEEE1722TpAcfBus`                                      | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAcfBusPart`                                  | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAcfCan`                                      | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAcfCanMessageTypeEnum`                       | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAcfCanPart`                                  | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAcfConnection`                               | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAcfLin`                                      | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAcfLinPart`                                  | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpAvConnection`                                | [ ] Deferred| N/A                                      | Group33          |
| `IEEE1722TpConfig`                                      | [ ] Deferred| N/A                                      | Group33          |
| `IEEE1722TpConnection`                                  | [ ] Deferred| N/A                                      | Group33          |
| `IEEE1722TpCrfConnection`                               | [ ] Deferred| N/A                                      | Group33          |
| `IEEE1722TpCrfPullEnum`                                 | [ ] Deferred| N/A                                      | Group33          |
| `IEEE1722TpCrfTypeEnum`                                 | [ ] Deferred| N/A                                      | Group33          |
| `IEEE1722TpIidcConnection`                              | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpRvfColorSpaceEnum`                           | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpRvfConnection`                               | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpRvfFrameRateEnum`                            | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpRvfPixelDepthEnum`                           | [ ] Created | N/A                                      | Group33          |
| `IEEE1722TpRvfPixelFormatEnum`                          | [ ] Created | N/A                                      | Group33          |
| `IPSecConfig`                                           | [x] Done    | d75eb10bff                               | Group16          |
| `IPSecConfigProps`                                      | [ ] Deferred| N/A                                      | Group32          |
| `IPSecRule`                                             | [ ] Deferred| N/A                                      | Group32          |
| `IPdu`                                                  | [x] Deferred| 6d2c23610d                               | Group31          |
| `IPduMapping`                                           | [x] Done    | 9c8e10b37f                               | Group6           |
| `IPduPort`                                              | [ ] Deferred| 5809b8408f                               | Group31          |
| `IPduSignalProcessingEnum`                              | [ ] Deferred| e34ab3e1ad                               | Group31          |
| `IPduTiming`                                            | [x] Deferred| 028e487683                               | Group31          |
| `IPsecDpdActionEnum`                                    | [ ] Deferred| N/A                                      | Group33          |
| `IPsecHeaderTypeEnum`                                   | [ ] Deferred| N/A                                      | Group33          |
| `IPsecIpProtocolEnum`                                   | [ ] Deferred| N/A                                      | Group32          |
| `IPsecModeEnum`                                         | [ ] Deferred| N/A                                      | Group32          |
| `IPsecPolicyEnum`                                       | [ ] Deferred| N/A                                      | Group32          |
| `IPv6ExtHeaderFilterList`                               | [x] Done    | d8127416ac                               | Group16          |
| `IPv6ExtHeaderFilterSet`                                | [ ] Deferred| N/A                                      | Group32          |
| `ISignal`                                               | [x] Deferred| e260b39286                               | Group31          |
| `ISignalGroup`                                          | [x] Deferred| 9e6350c7c6                               | Group31          |
| `ISignalIPdu`                                           | [x] Deferred| e9cdc05065                               | Group31          |
| `ISignalIPduGroup`                                      | [x] Done    | 4658ff431a                               | Group15          |
| `ISignalMapping`                                        | [x] Done    | ba0f1a12a8                               | Group17          |
| `ISignalPort`                                           | [x] Done    | 7a508bea29                               | Group15          |
| `ISignalProps`                                          | [ ] Deferred| 724ee746c9                               | Group31          |
| `ISignalToIPduMapping`                                  | [x] Deferred| 036440b90e                               | Group31          |
| `ISignalTriggering`                                     | [x] Deferred| 96695d8a34                               | Group31          |
| `ISignalTypeEnum`                                       | [x] Deferred| 3bf0b50440                               | Group31          |
| `IcmpRule`                                              | [x] Done    | c839e30e0e                               | Group20          |
| `IdentCaption`                                          | [x] Done    | 2dd2f91845                               | Group1           |
| `Identifiable`                                          | [x] Done    | c17bfbf60f                               | Group1           |
| `Identifier`                                            | [x] Deferred| N/A                                      | Group21          |
| `IdsDesign`                                             | [ ] Created | N/A                                      | Group36          |
| `IdsMgrCustomTimestampNeeds`                            | [x] Done    | b65fe94222                               | Group5           |
| `IdsMgrNeeds`                                           | [ ] Deferred| 4c1801ebf6                               | Group29          |
| `IdsPlatformInstantiation`                              | [x] Done    | 5d4cc1c454                               | Group7           |
| `IdsmInstance`                                          | [ ] Created | N/A                                      | Group36          |
| `IdsmModuleInstantiation`                               | [x] Done    | 5d4cc1c454                               | Group7           |
| `IdsmRateLimitation`                                    | [ ] Created | N/A                                      | Group36          |
| `IdsmTrafficLimitation`                                 | [ ] Created | N/A                                      | Group36          |
| `Ieee1722Tp`                                            | [ ] Deferred| N/A                                      | Group32          |
| `Ieee1722TpEthernetFrame`                               | [ ] Created | N/A                                      | Group33          |
| `Implementation`                                        | [x] Done    | e7dfb875d9                               | Group1           |
| `ImplementationDataType`                                | [ ] Deferred| N/A                                      | Group28          |
| `ImplementationDataTypeElement`                         | [x] Done    | 8e9b2db86b                               | Group10          |
| `ImplementationDataTypeElementInPortInterfaceRef`       | [ ] Deferred| N/A                                      | Group34          |
| `ImplementationDataTypeSubElementRef`                   | [ ] Deferred| 048dfdbb1f                               | Group27          |
| `ImplementationElementInParameterInstanceRef`           | [x] Done    | N/A                                      | Group23          |
| `ImplementationProps`                                   | [x] Done    | 3166f6e5d0                               | Group10          |
| `IncludedDataTypeSet`                                   | [ ] Deferred| 7ddafb5f11                               | Group29          |
| `IncludedModeDeclarationGroupSet`                       | [x] Done    | b9ac782d1e                               | Group2           |
| `IndentSample`                                          | [x] Deferred| N/A                                      | Group21          |
| `IndexEntry`                                            | [x] Deferred| N/A                                      | Group21          |
| `IndexedArrayElement`                                   | [x] Done    | 9eb93f743f                               | Group17          |
| `IndicatorStatusNeeds`                                  | [x] Done    | N/A                                      | Group29          |
| `InfrastructureServices`                                | [ ] Deferred| N/A                                      | Group32          |
| `InitEvent`                                             | [x] Done    | 64ab725d50                               | Group2           |
| `InitialSdDelayConfig`                                  | [x] Done    | 84dc59b646                               | Group16          |
| `InnerPortGroupInCompositionInstanceRef`                | [x] Done    | 919fbc0d11                               | Group2           |
| `InstantiationDataDefProps`                             | [x] Done    | e2aa88eb41                               | Group10          |
| `InstantiationRTEEventProps`                            | [ ] Deferred| aaffe85cbf                               | Group27          |
| `InstantiationTimingEventProps`                         | [ ] Deferred| 38df536d98                               | Group27          |
| `IntegerValueVariationPoint`                            | [x] Done    | d5c96fd954                               | Group8           |
| `InternalBehavior`                                      | [x] Done    | 68e390b39e                               | Group22          |
| `InternalConstrs`                                       | [ ] Deferred| 1469822986                               | Group28          |
| `InternalTriggerOccurredEvent`                          | [x] Done    | ac0bbe5799                               | Group12          |
| `InternalTriggeringPoint`                               | [x] Done    | 96033eb3fe                               | Group12          |
| `InterpolationRoutine`                                  | [x] Done    | 992a894be3                               | Group5           |
| `InterpolationRoutineMapping`                           | [x] Done    | d00d57b42d                               | Group5           |
| `InterpolationRoutineMappingSet`                        | [x] Done    | f3152abb23                               | Group5           |
| `IntervalTypeEnum`                                      | [ ] Deferred| 016c698ca5                               | Group28          |
| `InvalidationPolicy`                                    | [x] Done    | 1000053d88                               | Group1           |
| `InvertCondition`                                       | [ ] Created | N/A                                      | Group36          |
| `IoHwAbstractionServerAnnotation`                       | [ ] Deferred| 315b01de98                               | Group27          |
| `Ip4AddressString`                                      | [ ] Deferred| N/A                                      | Group21          |
| `Ip6AddressString`                                      | [ ] Deferred| N/A                                      | Group21          |
| `IpAddressKeepEnum`                                     | [x] Done    | 161a1b8215                               | Group16          |
| `Ipv4AddressSourceEnum`                                 | [x] Done    | 8c0771cafd                               | Group16          |
| `Ipv4ArpProps`                                          | [ ] Deferred| fbb86c3fcf                               | Group30          |
| `Ipv4AutoIpProps`                                       | [ ] Deferred| 926b146bca                               | Group30          |
| `Ipv4Configuration`                                     | [x] Done    | dcebacccb1                               | Group16          |
| `Ipv4DhcpServerConfiguration`                           | [ ] Deferred| 920dc732db                               | Group30          |
| `Ipv4FragmentationProps`                                | [ ] Deferred| e16eb379e5                               | Group30          |
| `Ipv4Props`                                             | [ ] Deferred| 614927b0c4                               | Group30          |
| `Ipv4Rule`                                              | [x] Done    | 817cf1a5de                               | Group20          |
| `Ipv6AddressSourceEnum`                                 | [x] Done    | a8fad12113                               | Group16          |
| `Ipv6Configuration`                                     | [ ] Deferred| N/A                                      | Group32          |
| `Ipv6DhcpServerConfiguration`                           | [ ] Deferred| 49ad95dd43                               | Group30          |
| `Ipv6FragmentationProps`                                | [ ] Deferred| 772f5b9b2b                               | Group30          |
| `Ipv6NdpProps`                                          | [ ] Deferred| f3c622bd64                               | Group30          |
| `Ipv6Props`                                             | [ ] Deferred| 05891c9038                               | Group30          |
| `Ipv6Rule`                                              | [x] Done    | 38bc83357c                               | Group20          |
| `Item`                                                  | [x] Done    | cf8b43c369                               | Group9           |
| `ItemLabelPosEnum`                                      | [x] Deferred| N/A                                      | Group21          |
| `J1939Cluster`                                          | [x] Done    | 44a70c3256                               | Group5           |
| `J1939ControllerApplication`                            | [ ] Deferred| bf314fe2fe                               | Group30          |
| `J1939ControllerApplicationToJ1939NmNodeMapping`        | [ ] Deferred| 7ffd517014                               | Group30          |
| `J1939DcmDm19Support`                                   | [x] Done    | 839c29d67e                               | Group5           |
| `J1939DcmIPdu`                                          | [x] Deferred| 75a272e532                               | Group31          |
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
| `LLongName`                                             | [x] Deferred| N/A                                      | Group21          |
| `LOverviewParagraph`                                    | [x] Done    | 764ef1c589                               | Group9           |
| `LParagraph`                                            | [x] Done    | 7fa4a01f74                               | Group3           |
| `LPlainText`                                            | [x] Done    | 1de91de480                               | Group9           |
| `LVerbatim`                                             | [x] Done    | d616f3d1ef                               | Group9           |
| `LabeledItem`                                           | [x] Deferred| N/A                                      | Group21          |
| `LabeledList`                                           | [x] Deferred| N/A                                      | Group21          |
| `LanguageSpecific`                                      | [x] Done    | 4566d4d4f7                               | Group22          |
| `LatencyConstraintTypeEnum`                             | [ ] Deferred| N/A                                      | Group35          |
| `LatencyTimingConstraint`                               | [ ] Deferred| N/A                                      | Group35          |
| `LetDataExchangeParadigmEnum`                           | [ ] Deferred| N/A                                      | Group35          |
| `LifeCycleInfo`                                         | [x] Done    | 5836e6eb08                               | Group8           |
| `LifeCycleInfoSet`                                      | [x] Done    | 11bd9cd848                               | Group8           |
| `LifeCyclePeriod`                                       | [x] Done    | b572582c11                               | Group8           |
| `LifeCycleState`                                        | [ ] Deferred| 8f363946f9                               | Group22          |
| `LifeCycleStateDefinitionGroup`                         | [ ] Deferred| 0c87fdbee4                               | Group22          |
| `Limit`                                                 | [ ] Deferred| 953b4ee68c                               | Group28          |
| `LimitValueVariationPoint`                              | [x] Done    | d5c96fd954                               | Group8           |
| `LinChecksumType`                                       | [ ] Created | N/A                                      | Group31          |
| `LinCluster`                                            | [ ] Deferred| d8a563e1f0                               | Group29          |
| `LinCommunicationConnector`                             | [x] Done    | da0534323b                               | Group17          |
| `LinCommunicationController`                            | [ ] Deferred| f19185283e                               | Group29          |
| `LinConfigurableFrame`                                  | [ ] Deferred| eb075693c2                               | Group29          |
| `LinConfigurationEntry`                                 | [ ] Implemented| N/A                                      | Group31          |
| `LinErrorResponse`                                      | [ ] Deferred| 6439b6cbd5                               | Group29          |
| `LinEventTriggeredFrame`                                | [ ] Created | N/A                                      | Group31          |
| `LinFrame`                                              | [ ] Implemented| N/A                                      | Group31          |
| `LinFrameTriggering`                                    | [ ] Implemented| N/A                                      | Group31          |
| `LinMaster`                                             | [ ] Deferred| 35db48e9b0                               | Group29          |
| `LinOrderedConfigurableFrame`                           | [ ] Deferred| 15a63a22ae                               | Group29          |
| `LinPhysicalChannel`                                    | [ ] Deferred| a60d5418a2                               | Group29          |
| `LinScheduleTable`                                      | [x] Done    | 0215ceb16a                               | Group17          |
| `LinSlave`                                              | [ ] Deferred| c8f1e00c47                               | Group29          |
| `LinSlaveConfig`                                        | [ ] Deferred| 81ac1ac2a0                               | Group29          |
| `LinSlaveConfigIdent`                                   | [ ] Deferred| 5e4ae9f277                               | Group29          |
| `LinSporadicFrame`                                      | [ ] Created | N/A                                      | Group31          |
| `LinTpConfig`                                           | [ ] Deferred| N/A                                      | Group33          |
| `LinTpConnection`                                       | [x] Done    | fa26bba13a                               | Group18          |
| `LinTpNode`                                             | [ ] Deferred| N/A                                      | Group33          |
| `LinUnconditionalFrame`                                 | [ ] Implemented| N/A                                      | Group31          |
| `Linker`                                                | [x] Done    | 20003dc3cc                               | Group1           |
| `List`                                                  | [x] Deferred| N/A                                      | Group21          |
| `ListEnum`                                              | [x] Done    | 0623068af8                               | Group9           |
| `LogAndTraceMessageCollectionSet`                       | [ ] Created | N/A                                      | Group36          |
| `LogTraceDefaultLogLevelEnum`                           | [x] Done    | f1eb819e47                               | Group5           |
| `MacAddressString`                                      | [x] Done    | 8b633b6dd3                               | Group20          |
| `MacMulticastConfiguration`                             | [ ] Deferred| N/A                                      | Group32          |
| `MacMulticastGroup`                                     | [x] Done    | 9ee3f1b66a                               | Group16          |
| `MacSecCapabilityEnum`                                  | [ ] Deferred| bc28f5ecb0                               | Group30          |
| `MacSecCipherSuiteConfig`                               | [ ] Deferred| 21ec4784ed                               | Group30          |
| `MacSecConfidentialityOffsetEnum`                       | [ ] Deferred| e609bd9264                               | Group30          |
| `MacSecCryptoAlgoConfig`                                | [ ] Deferred| 6ce66d34dc                               | Group30          |
| `MacSecFailPermissiveModeEnum`                          | [ ] Deferred| e4ec644192                               | Group30          |
| `MacSecGlobalKayProps`                                  | [ ] Deferred| edc1d0ae3c                               | Group30          |
| `MacSecKayParticipant`                                  | [ ] Deferred| 006a38a1cd                               | Group30          |
| `MacSecLocalKayProps`                                   | [ ] Implemented| 506d255bd5                               | Group30          |
| `MacSecParticipantSet`                                  | [ ] Deferred| 66ee2a8948                               | Group30          |
| `MacSecProps`                                           | [ ] Deferred| N/A                                      | Group30          |
| `MacSecRoleEnum`                                        | [ ] Deferred| 38c1935eff                               | Group30          |
| `Map`                                                   | [x] Done    | 43ec8ade8c                               | Group3           |
| `MappingConstraint`                                     | [ ] Deferred| a678eca673                               | Group30          |
| `MappingDirectionEnum`                                  | [ ] Deferred| 9ed89eb9e6                               | Group27          |
| `MappingScopeEnum`                                      | [ ] Deferred| b42864d264                               | Group30          |
| `MaxCommModeEnum`                                       | [x] Done    | N/A                                      | Group23          |
| `MaximumMessageLengthType`                              | [ ] Deferred| N/A                                      | Group33          |
| `McDataAccessDetails`                                   | [x] Done    | N/A                                      | Group23          |
| `McDataInstance`                                        | [x] Done    | N/A                                      | Group23          |
| `McFunction`                                            | [x] Done    | N/A                                      | Group23          |
| `McFunctionDataRefSet`                                  | [x] Done    | N/A                                      | Group23          |
| `McGroup`                                               | [x] Done    | N/A                                      | Group23          |
| `McGroupDataRefSet`                                     | [x] Done    | N/A                                      | Group23          |
| `McParameterElementGroup`                               | [x] Done    | N/A                                      | Group23          |
| `McSupportData`                                         | [x] Done    | N/A                                      | Group23          |
| `McSwEmulationMethodSupport`                            | [x] Done    | N/A                                      | Group23          |
| `McdIdentifier`                                         | [ ] Deferred| N/A                                      | Group21          |
| `MeasuredExecutionTime`                                 | [x] Done    | N/A                                      | Group23          |
| `MeasuredHeapUsage`                                     | [x] Done    | N/A                                      | Group23          |
| `MeasuredStackUsage`                                    | [x] Done    | 05f494e759                               | Group20          |
| `MemoryAllocationKeywordPolicyType`                     | [x] Done    | 70ce06f500                               | Group22          |
| `MemorySection`                                         | [x] Done    | 6d92ecd979                               | Group20          |
| `MemorySectionLocation`                                 | [x] Done    | N/A                                      | Group23          |
| `MemorySectionType`                                     | [x] Done    | 70ce06f500                               | Group22          |
| `MetaDataItem`                                          | [x] Done    | e69a025254                               | Group2           |
| `MetaDataItemSet`                                       | [x] Done    | e69a025254                               | Group2           |
| `MimeTypeString`                                        | [x] Done    | 01cc23df4e                               | Group3           |
| `MirroringProtocolEnum`                                 | [ ] Created | N/A                                      | Group33          |
| `MixedContentForLongName`                               | [x] Deferred| N/A                                      | Group21          |
| `MixedContentForOverviewParagraph`                      | [x] Done    | 18b494eba5                               | Group8           |
| `MixedContentForParagraph`                              | [x] Done    | bf9114cb01                               | Group3           |
| `MixedContentForPlainText`                              | [x] Done    | 4a95d1d305                               | Group8           |
| `MixedContentForUnitNames`                              | [x] Done    | 3d47eb65c8                               | Group8           |
| `MixedContentForVerbatim`                               | [x] Done    | 74549e6a51                               | Group8           |
| `MlFigure`                                              | [x] Done    | 9225ed1572                               | Group3           |
| `MlFormula`                                             | [x] Deferred| N/A                                      | Group21          |
| `ModeAccessPoint`                                       | [x] Done    | 543d9df4e7                               | Group12          |
| `ModeAccessPointIdent`                                  | [x] Done    | 918013a6ce                               | Group1           |
| `ModeActivationKind`                                    | [x] Done    | 1625966930                               | Group11          |
| `ModeDeclaration`                                       | [x] Done    | e3d79f89ca                               | Group22          |
| `ModeDeclarationGroup`                                  | [x] Done    | e3d79f89ca                               | Group22          |
| `ModeDeclarationGroupPrototype`                         | [x] Done    | 51f2e1155f                               | Group1           |
| `ModeDeclarationGroupPrototypeMapping`                  | [x] Done    | 96e9f073a2                               | Group11          |
| `ModeDeclarationMapping`                                | [ ] Deferred| 9df12a627d                               | Group27          |
| `ModeDeclarationMappingSet`                             | [x] Done    | eeec29b637                               | Group1           |
| `ModeDrivenTransmissionModeCondition`                   | [x] Done    | 206cf29517                               | Group5           |
| `ModeErrorBehavior`                                     | [x] Done    | e3d79f89ca                               | Group22          |
| `ModeErrorReactionPolicyEnum`                           | [x] Done    | e3d79f89ca                               | Group22          |
| `ModeGroupInAtomicSwcInstanceRef`                       | [x] Done    | cdb0951050                               | Group11          |
| `ModeInBswInstanceRef`                                  | [ ] Deferred| N/A                                      | Group35          |
| `ModeInSwcBswInstanceRef`                               | [x] Done    | 71ca6a5415                               | Group8           |
| `ModeInSwcInstanceRef`                                  | [x] Done    | 70dcc26975                               | Group8           |
| `ModeInterfaceMapping`                                  | [x] Done    | a598489544                               | Group11          |
| `ModePortAnnotation`                                    | [ ] Deferred| 2849ecb9cd                               | Group27          |
| `ModeRequestTypeMap`                                    | [x] Done    | 2b824ca5f8                               | Group11          |
| `ModeSwitchEventTriggeredActivity`                      | [x] Done    | 8fa7710539                               | Group10          |
| `ModeSwitchInterface`                                   | [ ] Deferred| a16d0c351f                               | Group27          |
| `ModeSwitchPoint`                                       | [x] Done    | 1037222ee7                               | Group12          |
| `ModeSwitchReceiverComSpec`                             | [x] Done    | 67324d240c                               | Group10          |
| `ModeSwitchSenderComSpec`                               | [x] Done    | 3fbf07cc78                               | Group10          |
| `ModeSwitchedAckEvent`                                  | [ ] Deferred| d3d54a566d                               | Group28          |
| `ModeSwitchedAckRequest`                                | [x] Done    | f587d873eb                               | Group10          |
| `ModeTransition`                                        | [x] Done    | e3d79f89ca                               | Group22          |
| `Modification`                                          | [x] Done    | 008307967e                               | Group9           |
| `ModuleConfiguration`                                   | [x] Done    | 5cedb145b9                               | Group19          |
| `MonotonyEnum`                                          | [ ] Deferred| 2386d18780                               | Group28          |
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
| `MultiLanguageVerbatim`                                 | [x] Deferred| N/A                                      | Group21          |
| `MultidimensionalTime`                                  | [x] Done    | b572582c11                               | Group8           |
| `MultilanguageLongName`                                 | [x] Done    | 87855dea47                               | Group3           |
| `MultilanguageReferrable`                               | [x] Done    | 7c7157a02b                               | Group1           |
| `MultiplexedIPdu`                                       | [x] Done    | 2c2e102933                               | Group15          |
| `MultiplexedPart`                                       | [x] Done    | 9ed9d78782                               | Group15          |
| `MultiplicityRestrictionWithSeverity`                   | [ ] Created | N/A                                      | Group36          |
| `NPdu`                                                  | [x] Deferred| 5cff010b1a                               | Group31          |
| `NameTokens`                                            | [x] Done    | c8a3ff507d                               | Group3           |
| `NetworkEndpoint`                                       | [x] Done    | 84587c11f6                               | Group16          |
| `NetworkEndpointAddress`                                | [x] Done    | c052de0226                               | Group6           |
| `NetworkLayerRule`                                      | [x] Done    | 68f8744c75                               | Group20          |
| `NetworkSegmentIdentification`                          | [ ] Deferred| N/A                                      | Group34          |
| `NetworkTargetAddressType`                              | [ ] Deferred| N/A                                      | Group33          |
| `NmCluster`                                             | [x] Done    | ae48471063                               | Group6           |
| `NmClusterCoupling`                                     | [x] Done    | 9c8e10b37f                               | Group6           |
| `NmConfig`                                              | [x] Done    | 757aea1d17                               | Group6           |
| `NmCoordinator`                                         | [ ] Implemented| N/A                                      | Group33          |
| `NmCoordinatorRoleEnum`                                 | [ ] Implemented| N/A                                      | Group33          |
| `NmEcu`                                                 | [x] Done    | c5eafef533                               | Group18          |
| `NmNode`                                                | [ ] Implemented| N/A                                      | Group33          |
| `NmPdu`                                                 | [x] Deferred| 462941c124                               | Group31          |
| `NonqueuedReceiverComSpec`                              | [ ] Deferred| 4179558606                               | Group27          |
| `NonqueuedSenderComSpec`                                | [ ] Deferred| f6f67d00a4                               | Group27          |
| `NotAvailableValueSpecification`                        | [ ] Deferred| 83ab0d13f3                               | Group28          |
| `Note`                                                  | [x] Deferred| N/A                                      | Group21          |
| `NoteTypeEnum`                                          | [x] Deferred| N/A                                      | Group21          |
| `NumericalOrText`                                       | [ ] Deferred| 0388290c04                               | Group28          |
| `NumericalRuleBasedValueSpecification`                  | [ ] Deferred| 0448eee2d6                               | Group28          |
| `NumericalValueSpecification`                           | [x] Done    | b16a369151                               | Group9           |
| `NumericalValueVariationPoint`                          | [x] Done    | d5c96fd954                               | Group8           |
| `NvBlockDataMapping`                                    | [x] Done    | cf9621f708                               | Group10          |
| `NvBlockDescriptor`                                     | [x] Done    | e5d43e9b06                               | Group10          |
| `NvBlockNeeds`                                          | [x] Done    | 72d998faaa                               | Group10          |
| `NvBlockNeedsReliabilityEnum`                           | [x] Done    | 90b381db32                               | Group10          |
| `NvBlockNeedsWritingPriorityEnum`                       | [x] Done    | 5a36c87687                               | Group10          |
| `NvBlockSwComponentType`                                | [ ] Deferred| d70be3bb2d                               | Group29          |
| `NvDataInterface`                                       | [x] Done    | 1d666bc11b                               | Group1           |
| `NvDataPortAnnotation`                                  | [ ] Deferred| b0ec28fdd3                               | Group27          |
| `NvProvideComSpec`                                      | [x] Done    | a5c437cc82                               | Group10          |
| `NvRequireComSpec`                                      | [x] Done    | cbdf05b372                               | Group10          |
| `ObdControlServiceNeeds`                                | [x] Done    | N/A                                      | Group29          |
| `ObdInfoServiceNeeds`                                   | [x] Done    | N/A                                      | Group29          |
| `ObdMonitorServiceNeeds`                                | [x] Done    | N/A                                      | Group29          |
| `ObdPidServiceNeeds`                                    | [x] Done    | N/A                                      | Group29          |
| `ObdRatioConnectionKindEnum`                            | [x] Done    | N/A                                      | Group29          |
| `ObdRatioDenominatorNeeds`                              | [ ] Deferred| c4b99a4cf3                               | Group29          |
| `ObdRatioServiceNeeds`                                  | [ ] Deferred| 86d72d7d2c                               | Group29          |
| `OffsetTimingConstraint`                                | [x] Done    | e305e80e2a                               | Group8           |
| `OperationCycleTypeEnum`                                | [x] Done    | N/A                                      | Group29          |
| `OperationInAtomicSwcInstanceRef`                       | [x] Done    | 5d9a9f9600                               | Group11          |
| `OperationInSystemInstanceRef`                          | [x] Done    | 4e0c3cbe68                               | Group5           |
| `OperationInvokedEvent`                                 | [x] Done    | e607622c82                               | Group12          |
| `OrderedMaster`                                         | [x] Done    | 5d62450236                               | Group6           |
| `OrientEnum`                                            | [x] Done    | 9223f504b5                               | Group3           |
| `OsTaskExecutionEvent`                                  | [ ] Deferred| 5958e809f2                               | Group28          |
| `OsTaskPreemptabilityEnum`                              | [x] Done    | c53a7febdc                               | Group5           |
| `OsTaskProxy`                                           | [x] Done    | 61ccaa68eb                               | Group5           |
| `PModeGroupInAtomicSwcInstanceRef`                      | [x] Done    | f517d795f6                               | Group11          |
| `POperationInAtomicSwcInstanceRef`                      | [x] Done    | b6b0ea8cf7                               | Group11          |
| `PPortComSpec`                                          | [ ] Deferred| N/A                                      | Group27          |
| `PPortInCompositionInstanceRef`                         | [x] Done    | b36a560be9                               | Group11          |
| `PPortPrototype`                                        | [x] Done    | 0927333086                               | Group2           |
| `PRPortPrototype`                                       | [x] Done    | 043de7436d                               | Group2           |
| `PTriggerInAtomicSwcTypeInstanceRef`                    | [x] Done    | dc2297cba8                               | Group11          |
| `PackageableElement`                                    | [x] Done    | bb032ddd55                               | Group1           |
| `Paginateable`                                          | [x] Done    | 20e6ee88d0                               | Group3           |
| `ParameterAccess`                                       | [x] Done    | 3b9f111270                               | Group12          |
| `ParameterDataPrototype`                                | [x] Done    | 70ce06f500                               | Group22          |
| `ParameterInAtomicSWCTypeInstanceRef`                   | [ ] Deferred| N/A                                      | Group28          |
| `ParameterInterface`                                    | [x] Done    | 6bf99879eb                               | Group1           |
| `ParameterPortAnnotation`                               | [ ] Deferred| 9d56752e39                               | Group27          |
| `ParameterProvideComSpec`                               | [ ] Deferred| e41ac253ae                               | Group27          |
| `ParameterRequireComSpec`                               | [x] Done    | 6cf8476adb                               | Group10          |
| `ParameterSwComponentType`                              | [ ] Deferred| e82f0ed83e                               | Group27          |
| `PassThroughSwConnector`                                | [ ] Deferred| 1c0ee7d639                               | Group27          |
| `PayloadBytePatternRule`                                | [x] Done    | d77a6727fc                               | Group20          |
| `PayloadBytePatternRulePart`                            | [x] Done    | 0cc195ce8e                               | Group20          |
| `Pdu`                                                   | [x] Deferred| b51f649ba4                               | Group31          |
| `PduActivationRoutingGroup`                             | [ ] Deferred| 5cb5ddacc2                               | Group32          |
| `PduCollectionSemanticsEnum`                            | [x] Done    | 5d4adec228                               | Group16          |
| `PduCollectionTriggerEnum`                              | [x] Done    | 64d125ffae                               | Group5           |
| `PduMappingDefaultValue`                                | [x] Done    | 9c8e10b37f                               | Group6           |
| `PduToFrameMapping`                                     | [x] Deferred| a8e5ac35ee                               | Group31          |
| `PduTriggering`                                         | [x] Deferred| cb8a7e121b                               | Group31          |
| `PdurIPduGroup`                                         | [x] Done    | c53a7febdc                               | Group5           |
| `PerInstanceMemory`                                     | [x] Done    | f35aa0cd0a                               | Group2           |
| `PerInstanceMemorySize`                                 | [x] Done    | df36bbb1fa                               | Group10          |
| `PeriodicEventTriggering`                               | [ ] Deferred| N/A                                      | Group35          |
| `PermissibleSignalPath`                                 | [ ] Deferred| N/A                                      | Group31          |
| `PgwideEnum`                                            | [x] Done    | 1649678501                               | Group22          |
| `PhysConstrs`                                           | [ ] Deferred| cad9e2a340                               | Group28          |
| `PhysicalChannel`                                       | [ ] Deferred| 13ae27c195                               | Group29          |
| `PhysicalDimension`                                     | [ ] Deferred| 995b22a850                               | Group28          |
| `PhysicalDimensionMapping`                              | [ ] Deferred| e8c89613ff                               | Group28          |
| `PhysicalDimensionMappingSet`                           | [ ] Deferred| 262eb0db3d                               | Group28          |
| `PlatformModuleEthernetEndpointConfiguration`           | [x] Done    | 5d4cc1c454                               | Group7           |
| `PlcaProps`                                             | [ ] Deferred| 227f0810e3                               | Group30          |
| `PncGatewayTypeEnum`                                    | [x] Done    | f4ffa771cf                               | Group15          |
| `PncMapping`                                            | [ ] Deferred| N/A                                      | Group31          |
| `PortAPIOption`                                         | [x] Done    | 7c67628122                               | Group2           |
| `PortDefinedArgumentValue`                              | [x] Done    | 7fc79e4b73                               | Group2           |
| `PortElementToCommunicationResourceMapping`             | [ ] Created | N/A                                      | Group34          |
| `PortGroup`                                             | [x] Done    | d6512dbbec                               | Group2           |
| `PortGroupInSystemInstanceRef`                          | [x] Done    | 19c327cca6                               | Group5           |
| `PortInCompositionTypeInstanceRef`                      | [x] Done    | a6d84b2601                               | Group2           |
| `PortInterface`                                         | [ ] Deferred| ea81891ead                               | Group27          |
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
| `PredefinedVariant`                                     | [x] Deferred| N/A                                      | Group21          |
| `PrimitiveAttributeCondition`                           | [ ] Created | N/A                                      | Group36          |
| `PrimitiveAttributeTailoring`                           | [ ] Created | N/A                                      | Group36          |
| `PrivacyLevel`                                          | [x] Done    | fb222ae5b2                               | Group5           |
| `PrmChar`                                               | [x] Done    | 8be54a00d1                               | Group9           |
| `PrmCharAbsTol`                                         | [x] Done    | e6c467d5f8                               | Group9           |
| `PrmCharContents`                                       | [x] Done    | 9494a593a2                               | Group9           |
| `PrmCharMinTypMax`                                      | [x] Done    | 376f43f648                               | Group9           |
| `PrmCharNumericalContents`                              | [x] Done    | 51ded41bf8                               | Group9           |
| `PrmCharNumericalValue`                                 | [x] Done    | 2f1c852dbb                               | Group9           |
| `PrmCharTextualContents`                                | [x] Done    | 83a56461a1                               | Group9           |
| `Prms`                                                  | [x] Done    | f05d3afdfa                               | Group9           |
| `ProcessingKindEnum`                                    | [ ] Deferred| 97030aba64                               | Group27          |
| `ProgramminglanguageEnum`                               | [x] Done    | be79d7993b                               | Group1           |
| `ProvidedServiceInstance`                               | [ ] Deferred| N/A                                      | Group32          |
| `PulseTestEnum`                                         | [ ] Deferred| b532d9a217                               | Group27          |
| `QueuedReceiverComSpec`                                 | [x] Done    | bb5804989f                               | Group10          |
| `QueuedSenderComSpec`                                   | [x] Done    | 4a7d82ffc7                               | Group5           |
| `RModeGroupInAtomicSWCInstanceRef`                      | [x] Done    | 7dd87307dd                               | Group11          |
| `RModeInAtomicSwcInstanceRef`                           | [x] Done    | 5a3a7d14c0                               | Group11          |
| `ROperationInAtomicSwcInstanceRef`                      | [x] Done    | d7c9455251                               | Group11          |
| `RPortComSpec`                                          | [ ] Deferred| N/A                                      | Group27          |
| `RPortInCompositionInstanceRef`                         | [x] Done    | 6056133191                               | Group11          |
| `RPortPrototype`                                        | [x] Done    | 2cd6f3c46e                               | Group2           |
| `RTEEvent`                                              | [x] Done    | f0483d5732                               | Group2           |
| `RVariableInAtomicSwcInstanceRef`                       | [x] Done    | 2014bb1a51                               | Group11          |
| `RamBlockStatusControlEnum`                             | [x] Done    | 343d2af672                               | Group10          |
| `RapidPrototypingScenario`                              | [ ] Deferred| dcf4255cac                               | Group29          |
| `ReceiverAnnotation`                                    | [ ] Deferred| f2020f54b4                               | Group27          |
| `ReceiverComSpec`                                       | [ ] Deferred| N/A                                      | Group27          |
| `ReceptionComSpecProps`                                 | [x] Done    | 0ba890ba88                               | Group10          |
| `RecordLayoutIteratorPoint`                             | [x] Done    | 2acaf7a45f                               | Group3           |
| `RecordValueSpecification`                              | [x] Done    | b1c7030b10                               | Group3           |
| `ReentrancyLevelEnum`                                   | [x] Done    | 286c7c5870                               | Group10          |
| `Ref`                                                   | [x] Done    | 0518a7bca2                               | Group3           |
| `ReferenceBase`                                         | [x] Done    | 192dfd9467                               | Group1           |
| `ReferenceCondition`                                    | [ ] Created | N/A                                      | Group36          |
| `ReferenceTailoring`                                    | [ ] Created | N/A                                      | Group36          |
| `ReferenceValueSpecification`                           | [ ] Deferred| 8186029562                               | Group28          |
| `Referrable`                                            | [x] Deferred| N/A                                      | Group21          |
| `ReferrableSubtypesEnum`                                | [ ] Deferred| N/A                                      | Group21          |
| `RegularExpression`                                     | [ ] Deferred| N/A                                      | Group21          |
| `RelativeTolerance`                                     | [ ] Implemented| N/A                                      | Group31          |
| `RequestResponseDelay`                                  | [x] Done    | 1c556f35b4                               | Group16          |
| `ResolutionPolicyEnum`                                  | [x] Done    | f0a7460898                               | Group3           |
| `ResourceConsumption`                                   | [x] Done    | 0404020952                               | Group1           |
| `RestrictionWithSeverity`                               | [ ] Created | N/A                                      | Group36          |
| `ResumePosition`                                        | [x] Done    | 40c0abb9b1                               | Group17          |
| `RevisionLabelString`                                   | [ ] Deferred| N/A                                      | Group21          |
| `RoleBasedBswModuleEntryAssignment`                     | [x] Done    | N/A                                      | Group23          |
| `RoleBasedDataAssignment`                               | [x] Done    | 5989355419                               | Group10          |
| `RoleBasedDataTypeAssignment`                           | [x] Done    | N/A                                      | Group23          |
| `RoleBasedPortAssignment`                               | [x] Done    | f94da3dd92                               | Group10          |
| `RoleBasedResourceDependency`                           | [ ] Deferred| 9c0046237b                               | Group26          |
| `RootSwCompositionPrototype`                            | [x] Done    | 671dfc3835                               | Group1           |
| `RoughEstimateHeapUsage`                                | [x] Done    | N/A                                      | Group23          |
| `RoughEstimateOfExecutionTime`                          | [x] Done    | N/A                                      | Group23          |
| `RoughEstimateStackUsage`                               | [x] Done    | 575bb536fe                               | Group20          |
| `Row`                                                   | [x] Done    | b43b860105                               | Group3           |
| `RptAccessEnum`                                         | [x] Done    | N/A                                      | Group23          |
| `RptComponent`                                          | [x] Done    | N/A                                      | Group23          |
| `RptContainer`                                          | [ ] Deferred| 8c7d753249                               | Group29          |
| `RptEnablerImplTypeEnum`                                | [x] Done    | N/A                                      | Group23          |
| `RptExecutableEntity`                                   | [x] Done    | N/A                                      | Group23          |
| `RptExecutableEntityEvent`                              | [x] Done    | N/A                                      | Group23          |
| `RptExecutableEntityProperties`                         | [x] Done    | N/A                                      | Group23          |
| `RptExecutionContext`                                   | [x] Done    | N/A                                      | Group23          |
| `RptExecutionControlEnum`                               | [x] Done    | N/A                                      | Group23          |
| `RptHook`                                               | [ ] Deferred| 81bd63ac93                               | Group29          |
| `RptImplPolicy`                                         | [x] Done    | N/A                                      | Group23          |
| `RptPreparationEnum`                                    | [x] Done    | N/A                                      | Group23          |
| `RptProfile`                                            | [ ] Deferred| 917a9b7dfa                               | Group29          |
| `RptServicePoint`                                       | [x] Done    | N/A                                      | Group23          |
| `RptServicePointEnum`                                   | [x] Done    | N/A                                      | Group23          |
| `RptSupportData`                                        | [x] Done    | N/A                                      | Group23          |
| `RptSwPrototypingAccess`                                | [x] Done    | N/A                                      | Group23          |
| `RteApiReturnValueProvisionEnum`                        | [x] Done    | N/A                                      | Group29          |
| `RteEventInCompositionSeparation`                       | [ ] Deferred| N/A                                      | Group31          |
| `RteEventInCompositionToOsTaskProxyMapping`             | [ ] Deferred| N/A                                      | Group31          |
| `RteEventInEcuInstanceRef`                              | [x] Done    | dd76ebd8bf                               | Group12          |
| `RteEventInSystemSeparation`                            | [ ] Deferred| N/A                                      | Group31          |
| `RteEventInSystemToOsTaskProxyMapping`                  | [ ] Deferred| N/A                                      | Group31          |
| `RtePluginProps`                                        | [x] Done    | ec7fa0b5df                               | Group6           |
| `RtpTp`                                                 | [ ] Deferred| N/A                                      | Group32          |
| `RuleArguments`                                         | [ ] Deferred| 571398195f                               | Group28          |
| `RuleBasedAxisCont`                                     | [ ] Deferred| ebe56c922e                               | Group28          |
| `RuleBasedValueCont`                                    | [ ] Deferred| 1c8cba3d46                               | Group28          |
| `RuleBasedValueSpecification`                           | [ ] Deferred| 01d5ffb425                               | Group28          |
| `RunMode`                                               | [x] Done    | 0215ceb16a                               | Group17          |
| `RunnableEntity`                                        | [ ] Deferred| ba3d6ff8b5                               | Group28          |
| `RunnableEntityArgument`                                | [x] Done    | 3857c2a435                               | Group2           |
| `RunnableEntityGroup`                                   | [ ] Deferred| N/A                                      | Group28          |
| `RuntimeAddressConfigurationEnum`                       | [x] Done    | f24d8b53ba                               | Group16          |
| `RuntimeError`                                          | [x] Done    | N/A                                      | Group23          |
| `RxAcceptContainedIPduEnum`                             | [ ] Deferred| N/A                                      | Group31          |
| `RxIdentifierRange`                                     | [ ] Deferred| N/A                                      | Group32          |
| `SOMEIPMessageTypeEnum`                                 | [x] Done    | b163080753                               | Group6           |
| `SOMEIPTransformationDescription`                       | [ ] Deferred| N/A                                      | Group34          |
| `SOMEIPTransformationISignalProps`                      | [x] Done    | 55ff2098b4                               | Group6           |
| `SOMEIPTransformationProps`                             | [ ] Created | N/A                                      | Group34          |
| `SaveConfigurationEntry`                                | [ ] Deferred| N/A                                      | Group32          |
| `ScaleConstrValidityEnum`                               | [x] Done    | 1bc8904eee                               | Group9           |
| `ScheduleTableEntry`                                    | [ ] Implemented| N/A                                      | Group31          |
| `SdClientConfig`                                        | [x] Done    | 8e0c8857ad                               | Group7           |
| `SdServerConfig`                                        | [x] Done    | f509df9d94                               | Group16          |
| `SdgAbstractForeignReference`                           | [ ] Deferred| N/A                                      | Group21          |
| `SdgAbstractPrimitiveAttribute`                         | [ ] Deferred| N/A                                      | Group21          |
| `SdgAggregationWithVariation`                           | [ ] Deferred| N/A                                      | Group21          |
| `SdgAttribute`                                          | [ ] Deferred| N/A                                      | Group21          |
| `SdgClass`                                              | [ ] Deferred| N/A                                      | Group21          |
| `SdgDef`                                                | [ ] Deferred| N/A                                      | Group21          |
| `SdgElementWithGid`                                     | [ ] Deferred| N/A                                      | Group21          |
| `SdgForeignReference`                                   | [ ] Deferred| N/A                                      | Group21          |
| `SdgForeignReferenceWithVariation`                      | [ ] Deferred| N/A                                      | Group21          |
| `SdgPrimitiveAttribute`                                 | [ ] Deferred| N/A                                      | Group21          |
| `SdgPrimitiveAttributeWithVariation`                    | [ ] Deferred| N/A                                      | Group21          |
| `SdgReference`                                          | [ ] Deferred| N/A                                      | Group21          |
| `SdgTailoring`                                          | [ ] Created | N/A                                      | Group36          |
| `SecOcCryptoServiceMapping`                             | [x] Done    | eec98574a9                               | Group18          |
| `SectionInitializationPolicyType`                       | [x] Done    | 70ce06f500                               | Group22          |
| `SectionNamePrefix`                                     | [x] Done    | bc26545b98                               | Group20          |
| `SecureCommunicationAuthenticationProps`                | [ ] Deferred| 56bcc7567c                               | Group31          |
| `SecureCommunicationFreshnessProps`                     | [ ] Deferred| 748ee0ad2c                               | Group31          |
| `SecureCommunicationProps`                              | [ ] Deferred| e744b793f0                               | Group31          |
| `SecureCommunicationPropsSet`                           | [ ] Deferred| ac09333846                               | Group31          |
| `SecureOnBoardCommunicationNeeds`                       | [ ] Deferred| 294106f57d                               | Group29          |
| `SecuredIPdu`                                           | [x] Done    | 2c2e102933                               | Group15          |
| `SecuredPduHeaderEnum`                                  | [x] Done    | 2c2e102933                               | Group15          |
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
| `SegmentPosition`                                       | [x] Done    | 6c2d8befb2                               | Group15          |
| `SendIndicationEnum`                                    | [ ] Deferred| N/A                                      | Group34          |
| `SenderAnnotation`                                      | [ ] Deferred| f0a69daa65                               | Group27          |
| `SenderComSpec`                                         | [ ] Deferred| a598c3519b                               | Group27          |
| `SenderRecArrayElementMapping`                          | [ ] Deferred| N/A                                      | Group31          |
| `SenderRecArrayTypeMapping`                             | [x] Done    | 757aea1d17                               | Group6           |
| `SenderRecCompositeTypeMapping`                         | [x] Done    | 757aea1d17                               | Group6           |
| `SenderRecRecordElementMapping`                         | [x] Done    | dc019f9575                               | Group17          |
| `SenderRecRecordTypeMapping`                            | [x] Done    | abbfc40109                               | Group17          |
| `SenderReceiverAnnotation`                              | [ ] Deferred| 21808a1f74                               | Group27          |
| `SenderReceiverCompositeElementToSignalMapping`         | [ ] Deferred| N/A                                      | Group31          |
| `SenderReceiverInterface`                               | [x] Done    | e4e4770fb7                               | Group1           |
| `SenderReceiverToSignalGroupMapping`                    | [x] Done    | f921dd6fb4                               | Group17          |
| `SenderReceiverToSignalMapping`                         | [x] Done    | 44442b8b6a                               | Group17          |
| `SensorActuatorSwComponentType`                         | [ ] Deferred| 5395714191                               | Group29          |
| `SeparateSignalPath`                                    | [ ] Deferred| N/A                                      | Group31          |
| `ServerArgumentImplPolicyEnum`                          | [ ] Deferred| f045532a3c                               | Group27          |
| `ServerCallPoint`                                       | [x] Done    | 774620a3b1                               | Group2           |
| `ServerComSpec`                                         | [ ] Deferred| c0dcb9aff0                               | Group27          |
| `ServiceDependency`                                     | [x] Done    | N/A                                      | Group23          |
| `ServiceDiagnosticRelevanceEnum`                        | [x] Done    | da3a2d3532                               | Group14          |
| `ServiceInstanceCollectionSet`                          | [ ] Deferred| N/A                                      | Group32          |
| `ServiceNeeds`                                          | [x] Done    | 5fd6271d70                               | Group4           |
| `ServiceProviderEnum`                                   | [ ] Deferred| 5935adb517                               | Group27          |
| `ServiceProxySwComponentType`                           | [x] Done    | 74e821ccb8                               | Group11          |
| `ServiceSwComponentType`                                | [ ] Deferred| f5ecdcb0a4                               | Group29          |
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
| `SignalFanEnum`                                         | [ ] Deferred| 332ce34385                               | Group27          |
| `SignalServiceTranslationControlEnum`                   | [ ] Deferred| N/A                                      | Group34          |
| `SignalServiceTranslationElementProps`                  | [x] Done    | 8b6384cb3f                               | Group14          |
| `SignalServiceTranslationEventProps`                    | [ ] Deferred| N/A                                      | Group34          |
| `SignalServiceTranslationProps`                         | [ ] Deferred| N/A                                      | Group34          |
| `SignalServiceTranslationPropsSet`                      | [ ] Deferred| N/A                                      | Group34          |
| `SimulatedExecutionTime`                                | [x] Done    | N/A                                      | Group23          |
| `SingleLanguageLongName`                                | [x] Done    | 8aaa2657f3                               | Group3           |
| `SingleLanguageReferrable`                              | [x] Done    | a5910c1bf5                               | Group3           |
| `SingleLanguageUnitNames`                               | [x] Done    | d42795c169                               | Group8           |
| `SlOverviewParagraph`                                   | [x] Done    | 951209dbab                               | Group8           |
| `SlParagraph`                                           | [x] Done    | b7748b3e50                               | Group3           |
| `SoAdConfig`                                            | [ ] Deferred| N/A                                      | Group32          |
| `SoAdRoutingGroup`                                      | [x] Done    | 24f9dd86bd                               | Group20          |
| `SoConIPduIdentifier`                                   | [ ] Deferred| N/A                                      | Group32          |
| `SocketAddress`                                         | [ ] Deferred| N/A                                      | Group32          |
| `SocketConnectionBundle`                                | [x] Done    | 01f37f105c                               | Group16          |
| `SocketConnectionIpduIdentifier`                        | [x] Done    | c02cad3bb9                               | Group16          |
| `SocketConnectionIpduIdentifierSet`                     | [ ] Deferred| N/A                                      | Group32          |
| `SoftwareContext`                                       | [x] Done    | 45cf952f36                               | Group20          |
| `SomeipProtocolRule`                                    | [x] Done    | ebb82db445                               | Group20          |
| `SomeipSdClientEventGroupTimingConfig`                  | [ ] Deferred| N/A                                      | Group32          |
| `SomeipSdRule`                                          | [x] Done    | 16c6ec4955                               | Group20          |
| `SomeipSdServerEventGroupTimingConfig`                  | [ ] Deferred| N/A                                      | Group32          |
| `SomeipSdServerServiceInstanceConfig`                   | [ ] Deferred| N/A                                      | Group32          |
| `SomeipTpChannel`                                       | [ ] Created | N/A                                      | Group33          |
| `SomeipTpConfig`                                        | [ ] Deferred| N/A                                      | Group33          |
| `SomeipTpConnection`                                    | [ ] Created | N/A                                      | Group33          |
| `SpecElementReference`                                  | [ ] Created | N/A                                      | Group36          |
| `SpecElementScope`                                      | [ ] Created | N/A                                      | Group36          |
| `SpecificationDocumentScope`                            | [ ] Created | N/A                                      | Group36          |
| `SpecificationScope`                                    | [ ] Created | N/A                                      | Group36          |
| `SporadicEventTriggering`                               | [ ] Deferred| N/A                                      | Group35          |
| `StackUsage`                                            | [x] Done    | 85a243308b                               | Group20          |
| `StandardNameEnum`                                      | [x] Done    | 9a9ffdae8d                               | Group1           |
| `StateDependentFirewall`                                | [ ] Implemented| N/A                                      | Group33          |
| `StaticPart`                                            | [x] Done    | 206cf29517                               | Group5           |
| `StaticSocketConnection`                                | [ ] Deferred| N/A                                      | Group32          |
| `Std`                                                   | [x] Done    | c53a240809                               | Group3           |
| `StorageConditionStatusEnum`                            | [x] Done    | N/A                                      | Group29          |
| `StreamFilterIEEE1722Tp`                                | [ ] Deferred| cc74587e4b                               | Group30          |
| `StreamFilterIpv4Address`                               | [ ] Deferred| da459aa3b7                               | Group30          |
| `StreamFilterIpv6Address`                               | [ ] Deferred| ac34699c4a                               | Group30          |
| `StreamFilterMACAddress`                                | [ ] Deferred| c74b8e553a                               | Group30          |
| `StreamFilterPortRange`                                 | [ ] Deferred| c97f9dd4ee                               | Group30          |
| `StreamFilterRuleDataLinkLayer`                         | [ ] Deferred| 65ab0bd89a                               | Group30          |
| `StreamFilterRuleIpTp`                                  | [ ] Deferred| 8989307d08                               | Group30          |
| `StructuredReq`                                         | [x] Done    | d311fc7ce0                               | Group1           |
| `SubElementMapping`                                     | [x] Done    | 5eadca7853                               | Group1           |
| `SubElementRef`                                         | [x] Done    | 47b3052188                               | Group1           |
| `Superscript`                                           | [x] Deferred| N/A                                      | Group21          |
| `SupervisedEntityCheckpointNeeds`                       | [x] Done    | 67640c8035                               | Group4           |
| `SupervisedEntityNeeds`                                 | [x] Done    | N/A                                      | Group23          |
| `SupportBufferLockingEnum`                              | [x] Done    | 7c67628122                               | Group2           |
| `SwAddrMethod`                                          | [x] Done    | 70ce06f500                               | Group22          |
| `SwAxisCont`                                            | [ ] Deferred| ea8b13a1bf                               | Group28          |
| `SwAxisGeneric`                                         | [ ] Deferred| N/A                                      | Group28          |
| `SwAxisGrouped`                                         | [x] Done    | 12a2e0170b                               | Group3           |
| `SwAxisIndividual`                                      | [x] Done    | 842e1e4227                               | Group3           |
| `SwAxisType`                                            | [ ] Deferred| N/A                                      | Group28          |
| `SwBaseType`                                            | [ ] Deferred| N/A                                      | Group28          |
| `SwBitRepresentation`                                   | [ ] Deferred| N/A                                      | Group28          |
| `SwCalibrationAccessEnum`                               | [ ] Deferred| N/A                                      | Group28          |
| `SwCalprmAxis`                                          | [ ] Deferred| N/A                                      | Group28          |
| `SwCalprmAxisSet`                                       | [x] Done    | 9209b83ea0                               | Group3           |
| `SwCalprmAxisTypeProps`                                 | [ ] Deferred| N/A                                      | Group28          |
| `SwCalprmRefProxy`                                      | [ ] Deferred| 3e551e7678                               | Group28          |
| `SwComponentDocumentation`                              | [ ] Deferred| 35074e8030                               | Group29          |
| `SwComponentPrototype`                                  | [x] Done    | ff993a74c8                               | Group1           |
| `SwComponentPrototypeAssignment`                        | [x] Done    | 88070878ea                               | Group5           |
| `SwComponentType`                                       | [ ] Deferred| 9e3500a78f                               | Group27          |
| `SwConnector`                                           | [ ] Deferred| 9c9cfd33ef                               | Group27          |
| `SwDataDefProps`                                        | [ ] Deferred| N/A                                      | Group28          |
| `SwDataDependency`                                      | [ ] Deferred| 31a72c8fa3                               | Group28          |
| `SwDataDependencyArgs`                                  | [ ] Deferred| 31a3396687                               | Group28          |
| `SwGenericAxisParam`                                    | [ ] Deferred| 13be19a5bd                               | Group28          |
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
| `SwTextProps`                                           | [ ] Deferred| N/A                                      | Group28          |
| `SwValueCont`                                           | [x] Done    | 6db47de6aa                               | Group3           |
| `SwValues`                                              | [ ] Deferred| 42073daa2a                               | Group28          |
| `SwVariableRefProxy`                                    | [ ] Deferred| 7664cf6255                               | Group28          |
| `SwcBswMapping`                                         | [x] Done    | 58b2c68a57                               | Group1           |
| `SwcBswRunnableMapping`                                 | [x] Done    | 4f1681d55f                               | Group13          |
| `SwcBswSynchronizedModeGroupPrototype`                  | [x] Done    | d024ea8472                               | Group13          |
| `SwcBswSynchronizedTrigger`                             | [x] Done    | c7756e2bea                               | Group13          |
| `SwcExclusiveAreaPolicy`                                | [x] Done    | N/A                                      | Group29          |
| `SwcImplementation`                                     | [x] Done    | 6eae95f556                               | Group10          |
| `SwcInternalBehavior`                                   | [x] Done    | 4043dc013a                               | Group2           |
| `SwcModeManagerErrorEvent`                              | [ ] Deferred| 545278ad92                               | Group29          |
| `SwcModeSwitchEvent`                                    | [ ] Deferred| 8ea809a12f                               | Group28          |
| `SwcServiceDependency`                                  | [ ] Deferred| 38630f7a82                               | Group29          |
| `SwcSupportedFeature`                                   | [x] Done    | 7c67628122                               | Group2           |
| `SwcTiming`                                             | [ ] Deferred| N/A                                      | Group35          |
| `SwcToApplicationPartitionMapping`                      | [ ] Deferred| 8323feb0a2                               | Group30          |
| `SwcToEcuMapping`                                       | [x] Done    | fc5c1e2c39                               | Group18          |
| `SwcToImplMapping`                                      | [x] Done    | 7fbdba572b                               | Group18          |
| `SwcToSwcOperationArguments`                            | [ ] Deferred| N/A                                      | Group31          |
| `SwcToSwcOperationArgumentsDirectionEnum`               | [ ] Deferred| N/A                                      | Group31          |
| `SwcToSwcSignal`                                        | [ ] Deferred| N/A                                      | Group31          |
| `SwitchAsynchronousTrafficShaperGroupEntry`             | [ ] Deferred| dc9e5d6ce4                               | Group30          |
| `SwitchFlowMeteringEntry`                               | [ ] Deferred| 29385d65d2                               | Group30          |
| `SwitchStreamFilterActionDestPortModification`          | [ ] Deferred| cbe98badf5                               | Group30          |
| `SwitchStreamFilterActionPortModificationEnum`          | [ ] Deferred| 8ca63a75f0                               | Group30          |
| `SwitchStreamFilterEntry`                               | [ ] Deferred| 8bc4f911fe                               | Group30          |
| `SwitchStreamFilterRule`                                | [ ] Deferred| 4f467314cf                               | Group30          |
| `SwitchStreamGateEntry`                                 | [ ] Deferred| ac22e340e2                               | Group30          |
| `SwitchStreamIdentification`                            | [ ] Deferred| aa06ec8a24                               | Group30          |
| `SymbolProps`                                           | [x] Done    | 2d21a9108b                               | Group2           |
| `SymbolString`                                          | [ ] Deferred| N/A                                      | Group21          |
| `SymbolicNameProps`                                     | [x] Done    | N/A                                      | Group29          |
| `SyncTimeBaseMgrUserNeeds`                              | [x] Done    | 609f148a93                               | Group4           |
| `SynchronizationPointConstraint`                        | [ ] Deferred| N/A                                      | Group35          |
| `SynchronizationTimingConstraint`                       | [x] Done    | e305e80e2a                               | Group8           |
| `SynchronizationTypeEnum`                               | [ ] Deferred| N/A                                      | Group35          |
| `SynchronousServerCallPoint`                            | [x] Done    | 9182987d97                               | Group2           |
| `System`                                                | [x] Done    | ccfb528daf                               | Group5           |
| `SystemMapping`                                         | [ ] Deferred| 1fa8787ea5                               | Group30          |
| `SystemSignal`                                          | [x] Done    | 7828064475                               | Group15          |
| `SystemSignalGroup`                                     | [x] Deferred| bf1e679967                               | Group31          |
| `SystemSignalGroupToCommunicationResourceMapping`       | [ ] Deferred| N/A                                      | Group31          |
| `SystemSignalToCommunicationResourceMapping`            | [ ] Deferred| N/A                                      | Group31          |
| `SystemTiming`                                          | [ ] Deferred| N/A                                      | Group35          |
| `TDCpSoftwareClusterMapping`                            | [ ] Deferred| N/A                                      | Group35          |
| `TDCpSoftwareClusterMappingSet`                         | [ ] Deferred| N/A                                      | Group35          |
| `TDCpSoftwareClusterResourceMapping`                    | [ ] Deferred| N/A                                      | Group35          |
| `TDEventBswInternalBehavior`                            | [ ] Deferred| N/A                                      | Group35          |
| `TDEventBswInternalBehaviorTypeEnum`                    | [ ] Deferred| N/A                                      | Group35          |
| `TDEventBswModeDeclaration`                             | [ ] Deferred| N/A                                      | Group35          |
| `TDEventBswModeDeclarationTypeEnum`                     | [ ] Deferred| N/A                                      | Group35          |
| `TDEventBswModule`                                      | [ ] Deferred| N/A                                      | Group35          |
| `TDEventBswModuleTypeEnum`                              | [ ] Deferred| N/A                                      | Group35          |
| `TDEventCom`                                            | [ ] Deferred| N/A                                      | Group35          |
| `TDEventComplex`                                        | [ ] Deferred| N/A                                      | Group35          |
| `TDEventCycleStart`                                     | [ ] Deferred| N/A                                      | Group35          |
| `TDEventFrClusterCycleStart`                            | [ ] Deferred| N/A                                      | Group35          |
| `TDEventFrame`                                          | [ ] Deferred| N/A                                      | Group35          |
| `TDEventFrameEthernet`                                  | [ ] Deferred| N/A                                      | Group35          |
| `TDEventFrameEthernetTypeEnum`                          | [ ] Deferred| N/A                                      | Group35          |
| `TDEventFrameTypeEnum`                                  | [ ] Deferred| N/A                                      | Group35          |
| `TDEventIPdu`                                           | [ ] Deferred| N/A                                      | Group35          |
| `TDEventIPduTypeEnum`                                   | [ ] Deferred| N/A                                      | Group35          |
| `TDEventISignal`                                        | [ ] Deferred| N/A                                      | Group35          |
| `TDEventISignalTypeEnum`                                | [ ] Deferred| N/A                                      | Group35          |
| `TDEventModeDeclaration`                                | [ ] Deferred| N/A                                      | Group35          |
| `TDEventModeDeclarationTypeEnum`                        | [ ] Deferred| N/A                                      | Group35          |
| `TDEventOccurrenceExpression`                           | [ ] Deferred| N/A                                      | Group35          |
| `TDEventOccurrenceExpressionFormula`                    | [ ] Deferred| N/A                                      | Group35          |
| `TDEventOperation`                                      | [ ] Deferred| N/A                                      | Group35          |
| `TDEventOperationTypeEnum`                              | [ ] Deferred| N/A                                      | Group35          |
| `TDEventSLLETPort`                                      | [ ] Deferred| N/A                                      | Group35          |
| `TDEventSwc`                                            | [ ] Deferred| N/A                                      | Group35          |
| `TDEventSwcInternalBehavior`                            | [ ] Deferred| N/A                                      | Group35          |
| `TDEventSwcInternalBehaviorReference`                   | [ ] Deferred| N/A                                      | Group35          |
| `TDEventSwcInternalBehaviorTypeEnum`                    | [ ] Deferred| N/A                                      | Group35          |
| `TDEventTTCanCycleStart`                                | [ ] Deferred| N/A                                      | Group35          |
| `TDEventTrigger`                                        | [ ] Deferred| N/A                                      | Group35          |
| `TDEventTriggerTypeEnum`                                | [ ] Deferred| N/A                                      | Group35          |
| `TDEventVariableDataPrototype`                          | [ ] Deferred| N/A                                      | Group35          |
| `TDEventVariableDataPrototypeTypeEnum`                  | [ ] Deferred| N/A                                      | Group35          |
| `TDEventVfb`                                            | [x] Done    | 18eb225f40                               | Group8           |
| `TDEventVfbPort`                                        | [ ] Deferred| N/A                                      | Group35          |
| `TDEventVfbReference`                                   | [ ] Deferred| N/A                                      | Group35          |
| `TDHeaderIdRange`                                       | [ ] Deferred| N/A                                      | Group35          |
| `Table`                                                 | [x] Done    | e347fbbfa2                               | Group3           |
| `TableSeparatorString`                                  | [x] Done    | 211031ea0f                               | Group3           |
| `TargetIPduRef`                                         | [x] Done    | 4d2c155383                               | Group17          |
| `Tbody`                                                 | [x] Done    | 004d3f1259                               | Group3           |
| `TcpIpIcmpv4Props`                                      | [x] Done    | 2cf38be61d                               | Group5           |
| `TcpIpIcmpv6Props`                                      | [x] Done    | c53a7febdc                               | Group5           |
| `TcpOptionFilterList`                                   | [x] Done    | fd11862858                               | Group16          |
| `TcpOptionFilterSet`                                    | [x] Done    | 4b1494b6d2                               | Group16          |
| `TcpProps`                                              | [x] Done    | d2d5c40a16                               | Group5           |
| `TcpRule`                                               | [x] Done    | 06d3147f65                               | Group20          |
| `TcpTp`                                                 | [x] Done    | c59e3404da                               | Group16          |
| `TcpUdpConfig`                                          | [x] Done    | 757aea1d17                               | Group6           |
| `TextTableMapping`                                      | [x] Done    | be79d7993b                               | Group1           |
| `TextTableValuePair`                                    | [ ] Deferred| ee2a8edc68                               | Group27          |
| `TextValueSpecification`                                | [x] Done    | 81588f449e                               | Group9           |
| `TextualCondition`                                      | [ ] Created | N/A                                      | Group36          |
| `Tgroup`                                                | [x] Done    | 278d4674f3                               | Group3           |
| `TimeRangeType`                                         | [x] Done    | 7aa197e046                               | Group15          |
| `TimeRangeTypeTolerance`                                | [x] Done    | ba8d04cbb4                               | Group15          |
| `TimeSyncClientConfiguration`                           | [x] Done    | a032fa05dc                               | Group6           |
| `TimeSyncServerConfiguration`                           | [x] Done    | 155cc2f7f9                               | Group16          |
| `TimeSyncTechnologyEnum`                                | [ ] Deferred| N/A                                      | Group32          |
| `TimeSynchronization`                                   | [x] Done    | f4a1df5bcb                               | Group16          |
| `TimeValue`                                             | [ ] Deferred| e079162eb7                               | Group27          |
| `TimeValueValueVariationPoint`                          | [x] Done    | d5c96fd954                               | Group8           |
| `TimingCondition`                                       | [ ] Deferred| N/A                                      | Group35          |
| `TimingConditionFormula`                                | [ ] Deferred| N/A                                      | Group35          |
| `TimingDescriptionEventChain`                           | [x] Done    | ea1a75e5b9                               | Group8           |
| `TimingEvent`                                           | [ ] Deferred| da8bfb1cf1                               | Group28          |
| `TimingExtensionResource`                               | [ ] Deferred| N/A                                      | Group35          |
| `TimingModeInstance`                                    | [ ] Deferred| N/A                                      | Group35          |
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
| `TpAddress`                                             | [x] Done    | cedb8f8498                               | Group18          |
| `TpConfig`                                              | [ ] Deferred| N/A                                      | Group33          |
| `TpConnection`                                          | [ ] Deferred| N/A                                      | Group33          |
| `TpConnectionIdent`                                     | [x] Done    | N/A                                      | Group23          |
| `TpPort`                                                | [x] Done    | 0f6b1c9bfd                               | Group16          |
| `Traceable`                                             | [x] Deferred| N/A                                      | Group21          |
| `TraceableTable`                                        | [x] Done    | fa79c73df5                               | Group3           |
| `TraceableText`                                         | [x] Done    | 9e80479bda                               | Group1           |
| `TracedFailure`                                         | [x] Done    | N/A                                      | Group23          |
| `TransferPropertyEnum`                                  | [x] Done    | f3a9dc08dd                               | Group15          |
| `TransformationComSpecProps`                            | [ ] Deferred| 720b97ba6d                               | Group27          |
| `TransformationDescription`                             | [ ] Deferred| N/A                                      | Group28          |
| `TransformationISignalProps`                            | [x] Done    | 757aea1d17                               | Group6           |
| `TransformationProps`                                   | [ ] Created | N/A                                      | Group34          |
| `TransformationPropsSet`                                | [ ] Created | N/A                                      | Group34          |
| `TransformationTechnology`                              | [ ] Deferred| fecff00ac5                               | Group27          |
| `TransformerClassEnum`                                  | [ ] Deferred| N/A                                      | Group28          |
| `TransformerHardErrorEvent`                             | [ ] Deferred| 8f21cc9672                               | Group28          |
| `TransmissionAcknowledgementRequest`                    | [ ] Deferred| 1dbcef9926                               | Group27          |
| `TransmissionComSpecProps`                              | [ ] Deferred| 3c8b18ca27                               | Group27          |
| `TransmissionModeCondition`                             | [x] Done    | 7a7ff3c5af                               | Group15          |
| `TransmissionModeDeclaration`                           | [x] Done    | f4ffa771cf                               | Group15          |
| `TransmissionModeDefinitionEnum`                        | [ ] Deferred| f13828d9d5                               | Group27          |
| `TransmissionModeTiming`                                | [x] Done    | f4ffa771cf                               | Group15          |
| `TransportLayerRule`                                    | [x] Done    | 39d8f23c1d                               | Group20          |
| `TransportProtocolConfiguration`                        | [x] Done    | 0014960828                               | Group6           |
| `Trigger`                                               | [x] Done    | 131473204c                               | Group1           |
| `TriggerIPduSendCondition`                              | [x] Done    | d2dbe59bf6                               | Group15          |
| `TriggerInAtomicSwcInstanceRef`                         | [x] Done    | 839264b3a6                               | Group11          |
| `TriggerInterface`                                      | [x] Done    | cf9c6ac4cc                               | Group1           |
| `TriggerInterfaceMapping`                               | [x] Done    | 49f19e8feb                               | Group1           |
| `TriggerMapping`                                        | [x] Done    | 905c48d323                               | Group1           |
| `TriggerMode`                                           | [x] Done    | 2c2e102933                               | Group15          |
| `TriggerPortAnnotation`                                 | [ ] Deferred| f2d78fca39                               | Group27          |
| `TriggerToSignalMapping`                                | [ ] Deferred| N/A                                      | Group31          |
| `Tt`                                                    | [x] Deferred| N/A                                      | Group21          |
| `TtcanAbsolutelyScheduledTiming`                        | [ ] Deferred| N/A                                      | Group32          |
| `TtcanCluster`                                          | [ ] Deferred| 4c24b5ae37                               | Group29          |
| `TtcanCommunicationConnector`                           | [ ] Deferred| 20db1869a0                               | Group29          |
| `TtcanCommunicationController`                          | [ ] Deferred| 20da1fc7f6                               | Group29          |
| `TtcanPhysicalChannel`                                  | [ ] Deferred| d6edfeef67                               | Group29          |
| `TtcanTriggerType`                                      | [ ] Deferred| N/A                                      | Group32          |
| `UdpChecksumCalculationEnum`                            | [ ] Deferred| N/A                                      | Group32          |
| `UdpNmCluster`                                          | [x] Done    | c32d27a505                               | Group18          |
| `UdpNmClusterCoupling`                                  | [x] Done    | a1ffa0b85a                               | Group18          |
| `UdpNmEcu`                                              | [x] Done    | 9c8e10b37f                               | Group6           |
| `UdpNmNode`                                             | [x] Done    | f933ce83ac                               | Group18          |
| `UdpProps`                                              | [x] Done    | ecb15e901f                               | Group5           |
| `UdpRule`                                               | [x] Done    | c871945ce1                               | Group20          |
| `UdpTp`                                                 | [x] Done    | 5336dd0eae                               | Group16          |
| `UnassignFrameId`                                       | [ ] Implemented| N/A                                      | Group31          |
| `Unit`                                                  | [ ] Deferred| f801a63d13                               | Group28          |
| `UnitGroup`                                             | [x] Done    | e7fdb07f2b                               | Group9           |
| `UnlimitedIntegerValueVariationPoint`                   | [x] Done    | d5c96fd954                               | Group8           |
| `UriString`                                             | [ ] Deferred| N/A                                      | Group21          |
| `Url`                                                   | [x] Done    | 4b96ab8d89                               | Group3           |
| `UserDefinedCluster`                                    | [ ] Deferred| 60a130c7b2                               | Group30          |
| `UserDefinedCommunicationConnector`                     | [ ] Deferred| ff537256be                               | Group30          |
| `UserDefinedCommunicationController`                    | [ ] Deferred| acba63082a                               | Group30          |
| `UserDefinedEthernetFrame`                              | [ ] Created | N/A                                      | Group33          |
| `UserDefinedGlobalTimeMaster`                           | [ ] Created | N/A                                      | Group34          |
| `UserDefinedGlobalTimeSlave`                            | [ ] Created | N/A                                      | Group34          |
| `UserDefinedIPdu`                                       | [x] Done    | 2c2e102933                               | Group15          |
| `UserDefinedPdu`                                        | [x] Done    | 2c2e102933                               | Group15          |
| `UserDefinedPhysicalChannel`                            | [ ] Deferred| 0d446c837a                               | Group30          |
| `UserDefinedTransformationComSpecProps`                 | [x] Done    | 4a7d82ffc7                               | Group5           |
| `UserDefinedTransformationDescription`                  | [ ] Deferred| N/A                                      | Group34          |
| `UserDefinedTransformationISignalProps`                 | [x] Done    | 301182769c                               | Group6           |
| `UserDefinedTransformationProps`                        | [ ] Created | N/A                                      | Group34          |
| `V2xDataManagerNeeds`                                   | [x] Done    | e02dc71234                               | Group5           |
| `V2xFacUserNeeds`                                       | [x] Done    | 029aa70113                               | Group5           |
| `V2xMUserNeeds`                                         | [x] Done    | d45912e177                               | Group5           |
| `ValignEnum`                                            | [x] Done    | 52d3272bbb                               | Group3           |
| `ValueGroup`                                            | [ ] Deferred| c247077e81                               | Group28          |
| `ValueList`                                             | [ ] Deferred| bc05b153d3                               | Group28          |
| `ValueRestrictionWithSeverity`                          | [ ] Created | N/A                                      | Group36          |
| `ValueSpecification`                                    | [ ] Deferred| ac709a6d45                               | Group28          |
| `VariableAccess`                                        | [x] Done    | 12e743cc9b                               | Group12          |
| `VariableAccessInEcuInstanceRef`                        | [x] Done    | b52183a6b4                               | Group12          |
| `VariableAccessScopeEnum`                               | [x] Done    | 12e743cc9b                               | Group12          |
| `VariableAndParameterInterfaceMapping`                  | [x] Done    | 0e87cc4bb9                               | Group11          |
| `VariableDataPrototype`                                 | [x] Done    | d3b5d680e2                               | Group2           |
| `VariableDataPrototypeInSystemInstanceRef`              | [x] Done    | 1b3d673dac                               | Group7           |
| `VariableInAtomicSWCTypeInstanceRef`                    | [x] Done    | c8ac9ef7de                               | Group2           |
| `VariableInAtomicSwcInstanceRef`                        | [x] Done    | 0369005450                               | Group2           |
| `VariationPoint`                                        | [x] Done    | d4fce975d6                               | Group8           |
| `VariationPointProxy`                                   | [ ] Deferred| 128ce8e538                               | Group29          |
| `VariationRestrictionWithSeverity`                      | [ ] Created | N/A                                      | Group36          |
| `VendorSpecificServiceNeeds`                            | [x] Done    | a25f9a7718                               | Group5           |
| `VerbatimStringPlain`                                   | [ ] Deferred| N/A                                      | Group21          |
| `VerificationStatusIndicationModeEnum`                  | [x] Done    | N/A                                      | Group29          |
| `VfbTiming`                                             | [ ] Deferred| N/A                                      | Group35          |
| `ViewMap`                                               | [ ] Deferred| b48c08bba2                               | Group22          |
| `ViewMapSet`                                            | [ ] Deferred| f6dc7bb594                               | Group22          |
| `ViewTokens`                                            | [x] Done    | 82c86af789                               | Group3           |
| `VlanConfig`                                            | [x] Done    | eb32bcdeea                               | Group16          |
| `VlanMembership`                                        | [x] Done    | ed6ed2a65f                               | Group6           |
| `WaitPoint`                                             | [ ] Deferred| ce4966a549                               | Group28          |
| `WarningIndicatorRequestedBitNeeds`                     | [x] Done    | 1cd8edd8fd                               | Group5           |
| `WhitespaceControlled`                                  | [x] Done    | a78d444afb                               | Group8           |
| `WorstCaseHeapUsage`                                    | [x] Done    | a55d2092d0                               | Group22          |
| `WorstCaseStackUsage`                                   | [x] Done    | 5692e873a3                               | Group20          |
| `Xdoc`                                                  | [x] Done    | 294c8aae2c                               | Group3           |
| `Xfile`                                                 | [x] Done    | 7038ce5574                               | Group3           |
| `XmlSpaceEnum`                                          | [x] Done    | ec544e7988                               | Group8           |
| `Xref`                                                  | [x] Done    | db2b4fe059                               | Group3           |
| `XrefTarget`                                            | [x] Done    | 8c9df6638a                               | Group3           |
