# All Sync Todo Classes by Group

Generated from all Group files in `docs/plan/sync-todo/` — Classes ordered by group, then by appearance order within each group.

Status `*` (or an explicit `Deferred` status) = sync complete (Steps 1–8) but the `# Spec verified:`/`# XSD verified:` stamp is **deferred to a batch 9b user confirmation** (audited 2026-09-27 against the src stamps).
Class-availability lifecycle: `Created` = the class exists in src as an empty stub (dependency placeholder — e.g. the Group21–36 stub pass) but implementation has not started · `Implemented` = the class exists in src with members but the queued 9-step sync is not complete · `Pending` = the class is not available (not defined in src at all).


## Group1

Status: **75/75** completed

| Class Name                              | Status    | Commit ID  |
| --------------------------------------- | --------- | ---------- |
| `ARObject`                              | [x] Done  | 78ae363c75 |
| `ARElement`                             | [x] Done  | 61c85fa794 |
| `ReferenceBase`                         | [x] Done  | 192dfd9467 |
| `MultilanguageReferrable`               | [x] Done  | 7c7157a02b |
| `HwPin`                                 | [x] Done  | ff5b0e0865 |
| `HwPinGroup`                            | [x] Done  | 69afffcc48 |
| `HwType`                                | [x] Done  | 29f338b3c0 |
| `HwElement`                             | [x] Done  | 8c7f05d40a |
| `FirewallRule`                          | [x] Done* | 00d011d4ad |
| `PortInterfaceBlueprintMapping`         | [x] Done  | aec046b9cc |
| `PortPrototypeBlueprintMapping`         | [x] Done  | f87babf31b |
| `BlueprintMappingSet`                   | [x] Done  | aec046b9cc |
| `ConstantSpecificationMappingSet`       | [x] Done  | 8e5acbb2b1 |
| `StandardNameEnum`                      | [x] Done  | 9a9ffdae8d |
| `StructuredReq`                         | [x] Done  | d311fc7ce0 |
| `TraceableText`                         | [x] Done  | 9e80479bda |
| `Identifiable`                          | [x] Done  | c17bfbf60f |
| `CollectableElement`                    | [x] Done  | 3b31b7c402 |
| `PackageableElement`                    | [x] Done  | bb032ddd55 |
| `ARPackage`                             | [x] Done  | 360648178f |
| `AUTOSAR`                               | [x] Done  | 74f4d3c80a |
| `FileInfoComment`                       | [x] Done  | c62e1c8943 |
| `AutoCollectEnum`                       | [x] Done  | 75f4005552 |
| `Collection`                            | [x] Done  | 75f4005552 |
| `AtpType`                               | [x] Done  | 451ad38330 |
| `AtpPrototype`                          | [x] Done  | eb4c4bf308 |
| `PortPrototype`                         | [x] Done  | 74e4c8242f |
| `DataPrototype`                         | [x] Done  | 9175595d88 |
| `ModeDeclarationGroupPrototype`         | [x] Done  | 51f2e1155f |
| `RootSwCompositionPrototype`            | [x] Done  | 671dfc3835 |
| `SwComponentPrototype`                  | [x] Done  | ff993a74c8 |
| `AtpStructureElement`                   | [x] Done  | 5eff088fa5 |
| `AtpDefinition`                         | [x] Done  | 38eb1e817c |
| `BlueprintPolicy`                       | [x] Done  | f5f5084e36 |
| `AtpBlueprint`                          | [x] Done  | 043de7436d |
| `AtpBlueprintable`                      | [x] Done  | b7cf03094f |
| `AtpBlueprintMapping`                   | [x] Done  | 493e272da6 |
| `ApplicationDeferredDataType`           | [x] Done  | abdfbf1d96 |
| `PortInterfaceMapping`                  | [x] Done  | ca6a372382 |
| `AutosarDataType`                       | [x] Done  | a5f99df464 |
| `AbstractImplementationDataType`        | [x] Done  | 9b5379d3e3 |
| `AbstractImplementationDataTypeElement` | [x] Done  | cabd5469e9 |
| `DataInterface`                         | [x] Done  | d838fd43f4 |
| `ParameterInterface`                    | [x] Done  | 6bf99879eb |
| `NvDataInterface`                       | [x] Done  | 1d666bc11b |
| `HandleInvalidEnum`                     | [x] Done  | 18271ddd84 |
| `InvalidationPolicy`                    | [x] Done  | 1000053d88 |
| `SenderReceiverInterface`               | [x] Done  | e4e4770fb7 |
| `Trigger`                               | [x] Done  | 131473204c |
| `TriggerInterface`                      | [x] Done  | cf9c6ac4cc |
| `TriggerMapping`                        | [x] Done  | 905c48d323 |
| `TriggerInterfaceMapping`               | [x] Done  | 49f19e8feb |
| `IdentCaption`                          | [x] Done  | 2dd2f91845 |
| `ModeAccessPointIdent`                  | [x] Done  | 918013a6ce |
| `ModeDeclarationMappingSet`             | [x] Done  | eeec29b637 |
| `SubElementRef`                         | [x] Done  | 47b3052188 |
| `TextTableMapping`                      | [x] Done  | be79d7993b |
| `SubElementMapping`                     | [x] Done  | 5eadca7853 |
| `FlatInstanceDescriptor`                | [x] Done  | 9db34796eb |
| `FlatMap`                               | [x] Done  | 5eadca7853 |
| `ProgramminglanguageEnum`               | [x] Done  | be79d7993b |
| `Compiler`                              | [x] Done  | 3fce597322 |
| `Linker`                                | [x] Done  | 20003dc3cc |
| `Code`                                  | [x] Done  | 9f470606b5 |
| `DependencyOnArtifact`                  | [x] Done  | 25211e56ca |
| `ResourceConsumption`                   | [x] Done  | 0404020952 |
| `SwcBswMapping`                         | [x] Done  | 58b2c68a57 |
| `BuildActionInvocator`                  | [x] Done  | 7008d5e857 |
| `BuildActionEntity`                     | [x] Done  | d7717e736a |
| `BuildEngineeringObject`                | [x] Done  | 96d176ed20 |
| `BuildActionIoElement`                  | [x] Done  | b572582c11 |
| `BuildActionEnvironment`                | [x] Done  | 2311c8754f |
| `BuildAction`                           | [x] Done  | 6c9ef66b40 |
| `BuildActionManifest`                   | [x] Done  | e6dcc8e79f |
| `Implementation`                        | [x] Done  | e7dfb875d9 |

## Group2

Status: **44/44** completed

| Class Name                                              | Status    | Commit ID  |
| ------------------------------------------------------- | --------- | ---------- |
| `PortInterfaceMappingSet`                               | [x] Done  | 5aa1b7460c |
| `MetaDataItem`                                          | [x] Done  | e69a025254 |
| `MetaDataItemSet`                                       | [x] Done  | e69a025254 |
| `ApplicationCompositeElementInPortInterfaceInstanceRef` | [x] Done  | 399b647757 |
| `SymbolProps`                                           | [x] Done  | 2d21a9108b |
| `PPortPrototype`                                        | [x] Done  | 0927333086 |
| `RPortPrototype`                                        | [x] Done  | 2cd6f3c46e |
| `PRPortPrototype`                                       | [x] Done  | 043de7436d |
| `PortGroup`                                             | [x] Done  | d6512dbbec |
| `InnerPortGroupInCompositionInstanceRef`                | [x] Done  | 919fbc0d11 |
| `RTEEvent`                                              | [x] Done  | f0483d5732 |
| `ServerCallPoint`                                       | [x] Done  | 774620a3b1 |
| `VariableDataPrototype`                                 | [x] Done  | d3b5d680e2 |
| `PerInstanceMemory`                                     | [x] Done  | f35aa0cd0a |
| `PortInCompositionTypeInstanceRef`                      | [x] Done  | a6d84b2601 |
| `AssemblySwConnector`                                   | [x] Done  | 2a104a061c |
| `DataTypeMappingSet`                                    | [x] Done  | 21ab486b53 |
| `ApplicationDataType`                                   | [x] Done  | b8d0878d98 |
| `ApplicationCompositeElementDataPrototype`              | [x] Done  | 031d5c7848 |
| `InitEvent`                                             | [x] Done  | 64ab725d50 |
| `BackgroundEvent`                                       | [x] Done  | 27b88a942c |
| `SynchronousServerCallPoint`                            | [x] Done  | 9182987d97 |
| `AsynchronousServerCallPoint`                           | [x] Done  | 3223dde420 |
| `AsynchronousServerCallResultPoint`                     | [x] Done  | 724f490c7a |
| `VariableInAtomicSwcInstanceRef`                        | [x] Done  | 0369005450 |
| `VariableInAtomicSWCTypeInstanceRef`                    | [x] Done  | c8ac9ef7de |
| `ArVariableInImplementationDataInstanceRef`             | [x] Done  | 910009eecc |
| `DelegationSwConnector`                                 | [x] Done  | 503344170e |
| `ApplicationPrimitiveDataType`                          | [x] Done  | 4a9ccae9b8 |
| `ApplicationCompositeDataType`                          | [x] Done  | de9d3fe0a4 |
| `ApplicationRecordElement`                              | [x] Done  | ae4ed75065 |
| `RunnableEntityArgument`                                | [x] Done  | 3857c2a435 |
| `ExternalTriggeringPointIdent`                          | [x] Done  | c04ca0f5b3 |
| `PortDefinedArgumentValue`                              | [x] Done  | 7fc79e4b73 |
| `CompositionSwComponentType`                            | [x] Done  | 6b46fb26a9 |
| `ApplicationRecordDataType`                             | [x] Done* | 0a06e0fae3 |
| `DataTransformationErrorHandlingEnum`                   | [x] Done  | 7fc79e4b73 |
| `DataTransformationStatusForwardingEnum`                | [x] Done  | 7c67628122 |
| `SwcSupportedFeature`                                   | [x] Done  | 7c67628122 |
| `CommunicationBufferLocking`                            | [x] Done  | 7c67628122 |
| `SupportBufferLockingEnum`                              | [x] Done  | 7c67628122 |
| `PortAPIOption`                                         | [x] Done  | 7c67628122 |
| `IncludedModeDeclarationGroupSet`                       | [x] Done  | b9ac782d1e |
| `SwcInternalBehavior`                                   | [x] Done  | 4043dc013a |

## Group3

Status: **95/95** completed

| Class Name                             | Status   | Commit ID  |
| -------------------------------------- | -------- | ---------- |
| `ChapterEnumBreak`                     | [x] Done | 20e6ee88d0 |
| `KeepWithPreviousEnum`                 | [x] Done | d447cf2a51 |
| `Paginateable`                         | [x] Done | 20e6ee88d0 |
| `MultilanguageLongName`                | [x] Done | 87855dea47 |
| `GraphicFitEnum`                       | [x] Done | 5b543a21d4 |
| `GraphicNotationEnum`                  | [x] Done | f25e765d8b |
| `Graphic`                              | [x] Done | 06b46f32ba |
| `SingleLanguageLongName`               | [x] Done | 8aaa2657f3 |
| `SingleLanguageReferrable`             | [x] Done | a5910c1bf5 |
| `MimeTypeString`                       | [x] Done | 01cc23df4e |
| `Url`                                  | [x] Done | 4b96ab8d89 |
| `Br`                                   | [x] Done | c2a85e6f8f |
| `Std`                                  | [x] Done | c53a240809 |
| `Xdoc`                                 | [x] Done | 294c8aae2c |
| `Xfile`                                | [x] Done | 7038ce5574 |
| `XrefTarget`                           | [x] Done | 8c9df6638a |
| `ResolutionPolicyEnum`                 | [x] Done | f0a7460898 |
| `ShowContentEnum`                      | [x] Done | e89003bb5b |
| `ShowResourceAliasNameEnum`            | [x] Done | 3a68e97234 |
| `ShowResourceCategoryEnum`             | [x] Done | d7cd8c5881 |
| `ShowResourceLongNameEnum`             | [x] Done | 835b8aa103 |
| `ShowResourceNumberEnum`               | [x] Done | 6f56251392 |
| `ShowResourcePageEnum`                 | [x] Done | 54f4f3e5d6 |
| `ShowResourceShortNameEnum`            | [x] Done | e2e2c300e5 |
| `ShowResourceTypeEnum`                 | [x] Done | 447709b7f1 |
| `ShowSeeEnum`                          | [x] Done | 5d48c2a6f3 |
| `Xref`                                 | [x] Done | db2b4fe059 |
| `MixedContentForParagraph`             | [x] Done | bf9114cb01 |
| `SlParagraph`                          | [x] Done | b7748b3e50 |
| `LParagraph`                           | [x] Done | 7fa4a01f74 |
| `FrameEnum`                            | [x] Done | 531991e029 |
| `AlignEnum`                            | [x] Done | fa74a474a5 |
| `ValignEnum`                           | [x] Done | 52d3272bbb |
| `OrientEnum`                           | [x] Done | 9223f504b5 |
| `TableSeparatorString`                 | [x] Done | 211031ea0f |
| `NameTokens`                           | [x] Done | c8a3ff507d |
| `ViewTokens`                           | [x] Done | 82c86af789 |
| `DocumentViewSelectable`               | [x] Done | ba2c324b39 |
| `Colspec`                              | [x] Done | 2bd0d07503 |
| `Entry`                                | [x] Done | 9005f6228e |
| `Row`                                  | [x] Done | b43b860105 |
| `Tbody`                                | [x] Done | 004d3f1259 |
| `Tgroup`                               | [x] Done | 278d4674f3 |
| `Table`                                | [x] Done | e347fbbfa2 |
| `TraceableTable`                       | [x] Done | fa79c73df5 |
| `TopicContent`                         | [x] Done | 6d7e325736 |
| `MultiLanguageParagraph`               | [x] Done | 77074563dc |
| `AreaEnumNohref`                       | [x] Done | 1d6f8c0aa9 |
| `AreaEnumShape`                        | [x] Done | 966320f6a7 |
| `Area`                                 | [x] Done | c9f2464902 |
| `Map`                                  | [x] Done | 43ec8ade8c |
| `LGraphic`                             | [x] Done | e4b1acf6c9 |
| `MlFigure`                             | [x] Done | 9225ed1572 |
| `MsrQueryResultChapter`                | [x] Done | fb505d3551 |
| `MsrQueryChapter`                      | [x] Done | 50103018c3 |
| `MsrQueryResultTopic1`                 | [x] Done | 09314bd3ad |
| `MsrQueryTopic1`                       | [x] Done | a09f0cdfbf |
| `MsrQueryP1`                           | [x] Done | 8da723c461 |
| `CompuContent`                         | [x] Done | 9f67b3e297 |
| `CompuConstContent`                    | [x] Done | b473f52422 |
| `CompuConstTextContent`                | [x] Done | 4cb828510e |
| `CompuConstNumericContent`             | [x] Done | 4b82220e02 |
| `CompuConstFormulaContent`             | [x] Done | 045d6fb522 |
| `CompuConst`                           | [x] Done | eddddc9982 |
| `CompuScaleContents`                   | [x] Done | 88acf483f8 |
| `CompuNominatorDenominator`            | [x] Done | ff6ef18624 |
| `CompuRationalCoeffs`                  | [x] Done | 26100b4c69 |
| `CompuScaleRationalFormula`            | [x] Done | 5a21470cd7 |
| `CompuScaleConstantContents`           | [x] Done | 3d859c8074 |
| `Compu`                                | [x] Done | dac94a9ffe |
| `CompuMethod`                          | [x] Done | 135f42e555 |
| `CompuScale`                           | [x] Done | 057a103913 |
| `CompuScales`                          | [x] Done | 64d125ffae |
| `DataConstrRule`                       | [x] Done | fa640a0d86 |
| `DataConstr`                           | [x] Done | 9927cc9e89 |
| `CompositeValueSpecification`          | [x] Done | cc842d74c1 |
| `ArrayValueSpecification`              | [x] Done | 043de7436d |
| `RecordValueSpecification`             | [x] Done | b1c7030b10 |
| `CompositeRuleBasedValueArgument`      | [x] Done | 0c916371eb |
| `CompositeRuleBasedValueSpecification` | [x] Done | 13a010bf81 |
| `SwValueCont`                          | [x] Done | 6db47de6aa |
| `SwCalprmAxisSet`                      | [x] Done | 9209b83ea0 |
| `SwAxisIndividual`                     | [x] Done | 842e1e4227 |
| `SwAxisGrouped`                        | [x] Done | 12a2e0170b |
| `SwRecordLayoutGroupContent`           | [x] Done | 0f19d490d3 |
| `SwGenericAxisParamType`               | [x] Done | 1eacd1a7a7 |
| `SwRecordLayoutV`                      | [x] Done | 9c0c3f85f8 |
| `SwRecordLayout`                       | [x] Done | f8149880de |
| `AsamRecordLayoutSemantics`            | [x] Done | 2acaf7a45f |
| `RecordLayoutIteratorPoint`            | [x] Done | 2acaf7a45f |
| `SwRecordLayoutGroup`                  | [x] Done | 2acaf7a45f |
| `GeneralAnnotation`                    | [x] Done | ab2daa7785 |
| `FirewallActionEnum`                   | [x] Done | ab2daa7785 |
| `CompuGenericMath`                     | [x] Done | 1de6c0ef23 |
| `Ref`                                  | [x] Done | 0518a7bca2 |

## Group4

Status: **29/29** completed

| Class Name                              | Status   | Commit ID  |
| --------------------------------------- | -------- | ---------- |
| `BswPerInstanceMemoryPolicy`            | [x] Done | b89ad783a3 |
| `BswClientPolicy`                       | [x] Done | 3141824107 |
| `BswInternalTriggeringPointPolicy`      | [x] Done | 2bb8413910 |
| `BswParameterPolicy`                    | [x] Done | eceaef9296 |
| `BswReleasedTriggerPolicy`              | [x] Done | 04498e5b27 |
| `BswDataSendPolicy`                     | [x] Done | ccacff4a64 |
| `BswInternalBehavior`                   | [x] Done | 89a7231799 |
| `ServiceNeeds`                          | [x] Done | 5fd6271d70 |
| `DiagEventDebounceAlgorithm`            | [x] Done | 4f246ae62d |
| `DiagEventDebounceMonitorInternal`      | [x] Done | 103cfd4316 |
| `EcuStateMgrUserNeeds`                  | [x] Done | 6b31696dff |
| `DltUserNeeds`                          | [x] Done | cc86c1002b |
| `DiagnosticComponentNeeds`              | [x] Done | 5c4c0963af |
| `DiagnosticUploadDownloadNeeds`         | [x] Done | fe8a0a1a6d |
| `DiagnosticsCommunicationSecurityNeeds` | [x] Done | d24a66632e |
| `FunctionInhibitionNeeds`               | [x] Done | 5c4c0963af |
| `GlobalSupervisionNeeds`                | [x] Done | 5c4c0963af |
| `HardwareTestNeeds`                     | [x] Done | 5c4c0963af |
| `SupervisedEntityCheckpointNeeds`       | [x] Done | 67640c8035 |
| `SyncTimeBaseMgrUserNeeds`              | [x] Done | 609f148a93 |
| `BswMgrNeeds`                           | [x] Done | 628464ed64 |
| `CryptoKeyManagementNeeds`              | [x] Done | dc49a71665 |
| `CryptoServiceJobNeeds`                 | [x] Done | 2ec474677a |
| `DiagnosticControlNeeds`                | [x] Done | d0a1134e3b |
| `DiagnosticEventManagerNeeds`           | [x] Done | dc34774429 |
| `DiagnosticRequestFileTransferNeeds`    | [x] Done | f084c4328c |
| `DoIpActivationLineNeeds`               | [x] Done | bf846cce70 |
| `DoIpGidNeeds`                          | [x] Done | 6c31e0057f |
| `DoIpGidSynchronizationNeeds`           | [x] Done | c64cb6318c |

## Group5

Status: **70/70** completed

| Class Name                              | Status   | Commit ID  |
| --------------------------------------- | -------- | ---------- |
| `DoIpPowerModeStatusNeeds`              | [x] Done | 4350642e77 |
| `FurtherActionByteNeeds`                | [x] Done | 30e266fd91 |
| `IdsMgrCustomTimestampNeeds`            | [x] Done | b65fe94222 |
| `J1939DcmDm19Support`                   | [x] Done | 839c29d67e |
| `J1939RmIncomingRequestServiceNeeds`    | [x] Done | 9784766a6d |
| `J1939RmOutgoingRequestServiceNeeds`    | [x] Done | 2b39e92976 |
| `V2xDataManagerNeeds`                   | [x] Done | e02dc71234 |
| `V2xFacUserNeeds`                       | [x] Done | 029aa70113 |
| `V2xMUserNeeds`                         | [x] Done | d45912e177 |
| `VendorSpecificServiceNeeds`            | [x] Done | a25f9a7718 |
| `WarningIndicatorRequestedBitNeeds`     | [x] Done | 1cd8edd8fd |
| `OperationInSystemInstanceRef`          | [x] Done | 4e0c3cbe68 |
| `ClientIdDefinition`                    | [x] Done | 8618ec8872 |
| `ClientIdDefinitionSet`                 | [x] Done | 01759771dd |
| `InterpolationRoutine`                  | [x] Done | 992a894be3 |
| `InterpolationRoutineMapping`           | [x] Done | d00d57b42d |
| `InterpolationRoutineMappingSet`        | [x] Done | f3152abb23 |
| `SwComponentPrototypeAssignment`        | [x] Done | 88070878ea |
| `CpSoftwareCluster`                     | [x] Done | 1194e00ca2 |
| `System`                                | [x] Done | ccfb528daf |
| `J1939Cluster`                          | [x] Done | 44a70c3256 |
| `J1939SharedAddressCluster`             | [x] Done | d3dc82098e |
| `PortGroupInSystemInstanceRef`          | [x] Done | 19c327cca6 |
| `ComManagementMapping`                  | [x] Done | 19c327cca6 |
| `TcpProps`                              | [x] Done | d2d5c40a16 |
| `UdpProps`                              | [x] Done | ecb15e901f |
| `EthTcpIpProps`                         | [x] Done | db98d8ff29 |
| `TcpIpIcmpv4Props`                      | [x] Done | 2cf38be61d |
| `TcpIpIcmpv6Props`                      | [x] Done | c53a7febdc |
| `EthTcpIpIcmpProps`                     | [x] Done | c53a7febdc |
| `EcuPartition`                          | [x] Done | c53a7febdc |
| `OsTaskPreemptabilityEnum`              | [x] Done | c53a7febdc |
| `OsTaskProxy`                           | [x] Done | 61ccaa68eb |
| `PdurIPduGroup`                         | [x] Done | c53a7febdc |
| `DoIpRoutingActivation`                 | [x] Done | c53a7febdc |
| `DoIpInterface`                         | [x] Done | c53a7febdc |
| `DoIpConfig`                            | [x] Done | fce66955f5 |
| `ConsumedProvidedServiceInstanceGroup`  | [x] Done | fce66955f5 |
| `ClientIdRange`                         | [x] Done | fce66955f5 |
| `PrivacyLevel`                          | [x] Done | fb222ae5b2 |
| `DltArgument`                           | [x] Done | 64d125ffae |
| `DltMessage`                            | [x] Done | c42f8ae9a2 |
| `DltContext`                            | [x] Done | c42f8ae9a2 |
| `DltApplication`                        | [x] Done | c42f8ae9a2 |
| `DltEcu`                                | [x] Done | c42f8ae9a2 |
| `DltDefaultTraceStateEnum`              | [x] Done | f1eb819e47 |
| `LogTraceDefaultLogLevelEnum`           | [x] Done | f1eb819e47 |
| `DltLogChannel`                         | [x] Done | f1eb819e47 |
| `DltConfig`                             | [x] Done | f1eb819e47 |
| `EcuInstance`                           | [x] Done | 206e89be41 |
| `DiagnosticConnection`                  | [x] Done | e96086c12f |
| `EthernetPhysicalChannel`               | [x] Done | 206cf29517 |
| `FrameTriggering`                       | [x] Done | 206cf29517 |
| `ContainedIPduCollectionSemanticsEnum`  | [x] Done | 64d125ffae |
| `PduCollectionTriggerEnum`              | [x] Done | 64d125ffae |
| `ContainedIPduProps`                    | [x] Done | 206cf29517 |
| `ModeDrivenTransmissionModeCondition`   | [x] Done | 206cf29517 |
| `StaticPart`                            | [x] Done | 206cf29517 |
| `DynamicPartAlternative`                | [x] Done | 206cf29517 |
| `GeneralPurposePdu`                     | [x] Done | 75683a2ede |
| `GeneralPurposeIPdu`                    | [x] Done | 75683a2ede |
| `CycleCounter`                          | [x] Done | 75683a2ede |
| `CycleRepetitionType`                   | [x] Done | bf6cb0f022 |
| `CycleRepetition`                       | [x] Done | 75683a2ede |
| `CommunicationCycle`                    | [x] Done | 75683a2ede |
| `FramePort`                             | [x] Done | 75683a2ede |
| `QueuedSenderComSpec`                   | [x] Done | 4a7d82ffc7 |
| `UserDefinedTransformationComSpecProps` | [x] Done | 4a7d82ffc7 |
| `EndToEndProtectionVariablePrototype`   | [x] Done | 4a7d82ffc7 |
| `EndToEndProtectionSet`                 | [x] Done | 4a7d82ffc7 |

## Group6

Status: **45/45** completed

| Class Name                              | Status   | Commit ID  |
| --------------------------------------- | -------- | ---------- |
| `AbstractEthernetFrame`                 | [x] Done | cba67817b3 |
| `GenericEthernetFrame`                  | [x] Done | 675a97e967 |
| `CouplingPortStructuralElement`         | [x] Done | 8404bbb94a |
| `CouplingPortScheduler`                 | [x] Done | 0f61040c0c |
| `VlanMembership`                        | [x] Done | ed6ed2a65f |
| `NetworkEndpointAddress`                | [x] Done | c052de0226 |
| `OrderedMaster`                         | [x] Done | 5d62450236 |
| `TimeSyncClientConfiguration`           | [x] Done | a032fa05dc |
| `TransportProtocolConfiguration`        | [x] Done | 0014960828 |
| `TcpUdpConfig`                          | [x] Done | 757aea1d17 |
| `FlexrayFrame`                          | [x] Done | 757aea1d17 |
| `CryptoServiceMapping`                  | [x] Done | 757aea1d17 |
| `TlsVersionEnum`                        | [x] Done | d969a0ddc1 |
| `TlsPskIdentity`                        | [x] Done | 16c2791a2b |
| `CryptoServicePrimitive`                | [x] Done | b609d72d59 |
| `TlsCryptoCipherSuiteProps`             | [x] Done | 648b40acaf |
| `CryptoEllipticCurveProps`              | [x] Done | d31256a6bc |
| `CryptoSignatureScheme`                 | [x] Done | 1eaeb5800b |
| `CryptoCertificateAlgorithmFamilyEnum`  | [x] Done | 4c65329125 |
| `CryptoCertificateFormatEnum`           | [x] Done | 7fc9ab7674 |
| `CryptoServiceCertificate`              | [x] Done | 757aea1d17 |
| `TlsCryptoCipherSuite`                  | [x] Done | 67315ec0a9 |
| `TlsCryptoServiceMapping`               | [x] Done | 67315ec0a9 |
| `DataTransformationSet`                 | [x] Done | 757aea1d17 |
| `DataPrototypeTransformationProps`      | [x] Done | ba255a82cc |
| `TransformationISignalProps`            | [x] Done | 757aea1d17 |
| `SOMEIPMessageTypeEnum`                 | [x] Done | b163080753 |
| `TlvDataIdDefinition`                   | [x] Done | 27ea0743dc |
| `TlvDataIdDefinitionSet`                | [x] Done | f0c9473162 |
| `SOMEIPTransformationISignalProps`      | [x] Done | 55ff2098b4 |
| `UserDefinedTransformationISignalProps` | [x] Done | 301182769c |
| `SenderRecCompositeTypeMapping`         | [x] Done | 757aea1d17 |
| `SenderRecArrayTypeMapping`             | [x] Done | 757aea1d17 |
| `NmClusterCoupling`                     | [x] Done | 9c8e10b37f |
| `NmCluster`                             | [x] Done | ae48471063 |
| `FlexrayNmCluster`                      | [x] Done | 9c8e10b37f |
| `FlexrayNmEcu`                          | [x] Done | 9c8e10b37f |
| `FlexrayNmNode`                         | [x] Done | 9c8e10b37f |
| `UdpNmEcu`                              | [x] Done | 9c8e10b37f |
| `J1939NmCluster`                        | [x] Done | 9c8e10b37f |
| `J1939NmEcu`                            | [x] Done | 9c8e10b37f |
| `NmConfig`                              | [x] Done | 757aea1d17 |
| `IPduMapping`                           | [x] Done | 9c8e10b37f |
| `PduMappingDefaultValue`                | [x] Done | 9c8e10b37f |
| `RtePluginProps`                        | [x] Done | ec7fa0b5df |

## Group7

Status: **32/32** completed

| Class Name                                    | Status   | Commit ID  |
| --------------------------------------------- | -------- | ---------- |
| `ComponentInCompositionInstanceRef`           | [x] Done | 02e863a567 |
| `SdClientConfig`                              | [x] Done | 8e0c8857ad |
| `HwAttributeDef`                              | [x] Done | 3912963bfd |
| `HwCategory`                                  | [x] Done | b7e2199ac8 |
| `HwAttributeValue`                            | [x] Done | 269d34d90f |
| `HwAttributeLiteralDef`                       | [x] Done | 5d767ace9e |
| `CryptoKeySlot`                               | [x] Done | a02f617547 |
| `AbstractDoIpLogicAddressProps`               | [x] Done | 64d125ffae |
| `DoIpLogicTargetAddressProps`                 | [x] Done | 64d125ffae |
| `DoIpLogicTesterAddressProps`                 | [x] Done | 64d125ffae |
| `DoIpTpConfig`                                | [x] Done | ac63e581b9 |
| `FirewallRuleProps`                           | [x] Done | 89039bf2bb |
| `IdsPlatformInstantiation`                    | [x] Done | 5d4cc1c454 |
| `IdsmModuleInstantiation`                     | [x] Done | 5d4cc1c454 |
| `PlatformModuleEthernetEndpointConfiguration` | [x] Done | 5d4cc1c454 |
| `CommunicationControllerMapping`              | [x] Done | 2613747d22 |
| `HwPortMapping`                               | [x] Done | 7d94510497 |
| `ECUMapping`                                  | [x] Done | 34bb50d75e |
| `VariableDataPrototypeInSystemInstanceRef`    | [x] Done | 1b3d673dac |
| `ComponentInSystemInstanceRef`                | [x] Done | b511fb85b0 |
| `PortPrototypeBlueprintInitValue`             | [x] Done | 57509a2e7d |
| `PortPrototypeBlueprint`                      | [x] Done | 8782a8ffe8 |
| `Keyword`                                     | [x] Done | 4ed5a2fe2d |
| `KeywordSet`                                  | [x] Done | a6a1d31ccc |
| `DiagnosticServiceInstance`                   | [x] Done | 6b514727f9 |
| `DiagnosticServiceTable`                      | [x] Done | 9bd6fadae5 |
| `DiagnosticCommonElement`                     | [x] Done | e0d022b1aa |
| `DiagnosticAuthRoleProxy`                     | [x] Done | 4579b43f0d |
| `DiagnosticSession`                           | [x] Done | 06d4e49a26 |
| `DiagnosticSecurityLevel`                     | [x] Done | f2da1338fc |
| `DiagnosticEnvironmentalCondition`            | [x] Done | 5bbca5f217 |
| `DiagnosticAccessPermission`                  | [x] Done | 9cbb4e26e7 |

## Group8

Status: **47/47** completed

| Class Name                               | Status   | Commit ID  |
| ---------------------------------------- | -------- | ---------- |
| `BindingTimeEnum`                        | [x] Done | 53bf180881 |
| `XmlSpaceEnum`                           | [x] Done | ec544e7988 |
| `ShortNameFragment`                      | [x] Done | 519d505393 |
| `MultidimensionalTime`                   | [x] Done | b572582c11 |
| `LifeCyclePeriod`                        | [x] Done | b572582c11 |
| `AttributeValueVariationPoint`           | [x] Done | d5c96fd954 |
| `FormulaExpression`                      | [x] Done | 88ed82bed3 |
| `SwSystemconstDependentFormula`          | [x] Done | f05e21d49e |
| `ConditionByFormula`                     | [x] Done | 18b494eba5 |
| `MixedContentForOverviewParagraph`       | [x] Done | 18b494eba5 |
| `WhitespaceControlled`                   | [x] Done | a78d444afb |
| `MixedContentForPlainText`               | [x] Done | 4a95d1d305 |
| `MixedContentForVerbatim`                | [x] Done | 74549e6a51 |
| `SlOverviewParagraph`                    | [x] Done | 951209dbab |
| `MixedContentForUnitNames`               | [x] Done | 3d47eb65c8 |
| `SingleLanguageUnitNames`                | [x] Done | d42795c169 |
| `SwSystemconstValue`                     | [x] Done | 5333bec027 |
| `PostBuildVariantCondition`              | [x] Done | 5333bec027 |
| `PostBuildVariantCriterion`              | [x] Done | 5333bec027 |
| `PostBuildVariantCriterionValue`         | [x] Done | 8af1088fd2 |
| `OffsetTimingConstraint`                 | [x] Done | e305e80e2a |
| `SynchronizationTimingConstraint`        | [x] Done | e305e80e2a |
| `TimingDescriptionEventChain`            | [x] Done | ea1a75e5b9 |
| `AutosarOperationArgumentInstance`       | [x] Done | b8cce0057f |
| `TDEventVfb`                             | [x] Done | 18eb225f40 |
| `BlueprintGenerator`                     | [x] Done | 246fc98452 |
| `BlueprintMapping`                       | [x] Done | a6fa7b8c18 |
| `LifeCycleInfo`                          | [x] Done | 5836e6eb08 |
| `LifeCycleInfoSet`                       | [x] Done | 11bd9cd848 |
| `VariationPoint`                         | [x] Done | d4fce975d6 |
| `ModeInSwcBswInstanceRef`                | [x] Done | 71ca6a5415 |
| `ModeInSwcInstanceRef`                   | [x] Done | 70dcc26975 |
| `AbstractEnumerationValueVariationPoint` | [x] Done | 0518a7bca2 |
| `AbstractNumericalVariationPoint`        | [x] Done | d5c96fd954 |
| `BooleanValueVariationPoint`             | [x] Done | d5c96fd954 |
| `FloatValueVariationPoint`               | [x] Done | d5c96fd954 |
| `IntegerValueVariationPoint`             | [x] Done | d5c96fd954 |
| `LimitValueVariationPoint`               | [x] Done | d5c96fd954 |
| `NumericalValueVariationPoint`           | [x] Done | d5c96fd954 |
| `PositiveIntegerValueVariationPoint`     | [x] Done | d5c96fd954 |
| `TimeValueValueVariationPoint`           | [x] Done | d5c96fd954 |
| `UnlimitedIntegerValueVariationPoint`    | [x] Done | d5c96fd954 |
| `BlueprintFormula`                       | [x] Done | 6d8ace0288 |
| `FMConditionByFeaturesAndAttributes`     | [x] Done | d69232bdf4 |
| `FMConditionByFeaturesAndSwSystemconsts` | [x] Done | d69232bdf4 |
| `FMFormulaByFeaturesAndAttributes`       | [x] Done | d69232bdf4 |
| `FMFormulaByFeaturesAndSwSystemconsts`   | [x] Done | d69232bdf4 |

## Group9

Status: **29/29** completed

| Class Name                    | Status   | Commit ID  |
| ----------------------------- | -------- | ---------- |
| `NumericalValueSpecification` | [x] Done | b16a369151 |
| `TextValueSpecification`      | [x] Done | 81588f449e |
| `ConstantReference`           | [x] Done | 4853348ea0 |
| `ConstantSpecification`       | [x] Done | 265721a764 |
| `DataFilterTypeEnum`          | [x] Done | b59bd6ebbe |
| `DataFilter`                  | [x] Done | ed2a073e76 |
| `Modification`                | [x] Done | 008307967e |
| `ScaleConstrValidityEnum`     | [x] Done | 1bc8904eee |
| `UnitGroup`                   | [x] Done | e7fdb07f2b |
| `SwImplPolicyEnum`            | [x] Done | d6945a4c8a |
| `SwSystemconst`               | [x] Done | 984387dd0c |
| `ListEnum`                    | [x] Done | 0623068af8 |
| `Item`                        | [x] Done | cf8b43c369 |
| `TopicContentOrMsrQuery`      | [x] Done | 460218682e |
| `LOverviewParagraph`          | [x] Done | 764ef1c589 |
| `LPlainText`                  | [x] Done | 1de91de480 |
| `LVerbatim`                   | [x] Done | d616f3d1ef |
| `ARList`                      | [x] Done | 2151ca0302 |
| `ChapterContent`              | [x] Done | dee07d0a3a |
| `ChapterModel`                | [x] Done | d3d61c9b2e |
| `PrmCharContents`             | [x] Done | 9494a593a2 |
| `PrmCharNumericalValue`       | [x] Done | 2f1c852dbb |
| `PrmCharAbsTol`               | [x] Done | e6c467d5f8 |
| `PrmCharMinTypMax`            | [x] Done | 376f43f648 |
| `PrmCharNumericalContents`    | [x] Done | 51ded41bf8 |
| `PrmCharTextualContents`      | [x] Done | 83a56461a1 |
| `PrmChar`                     | [x] Done | 8be54a00d1 |
| `GeneralParameter`            | [x] Done | b622d5b424 |
| `Prms`                        | [x] Done | f05d3afdfa |

## Group10

Status: **32/32** completed

| Class Name                         | Status   | Commit ID  |
| ---------------------------------- | -------- | ---------- |
| `DependencyUsageEnum`              | [x] Done | 9a8c86ae9a |
| `ArrayImplPolicyEnum`              | [x] Done | 700b032789 |
| `ApiPrincipleEnum`                 | [x] Done | c6d2e83f74 |
| `ReentrancyLevelEnum`              | [x] Done | 286c7c5870 |
| `ImplementationProps`              | [x] Done | 3166f6e5d0 |
| `PerInstanceMemorySize`            | [x] Done | df36bbb1fa |
| `SwcImplementation`                | [x] Done | 6eae95f556 |
| `ImplementationDataTypeElement`    | [x] Done | 8e9b2db86b |
| `ReceptionComSpecProps`            | [x] Done | 0ba890ba88 |
| `CompositeNetworkRepresentation`   | [x] Done | b1e81e17d6 |
| `ModeSwitchedAckRequest`           | [x] Done | f587d873eb |
| `ModeSwitchReceiverComSpec`        | [x] Done | 67324d240c |
| `ModeSwitchSenderComSpec`          | [x] Done | 3fbf07cc78 |
| `NvProvideComSpec`                 | [x] Done | a5c437cc82 |
| `NvRequireComSpec`                 | [x] Done | cbdf05b372 |
| `ParameterRequireComSpec`          | [x] Done | 6cf8476adb |
| `QueuedReceiverComSpec`            | [x] Done | bb5804989f |
| `DataTypeMap`                      | [x] Done | 0731ff4f68 |
| `EndToEndDescription`              | [x] Done | d3db89bb98 |
| `ModeSwitchEventTriggeredActivity` | [x] Done | 8fa7710539 |
| `AutosarVariableRef`               | [x] Done | d1b9384acc |
| `RoleBasedPortAssignment`          | [x] Done | f94da3dd92 |
| `AutosarParameterRef`              | [x] Done | b530f7e446 |
| `NvBlockNeedsReliabilityEnum`      | [x] Done | 90b381db32 |
| `NvBlockNeedsWritingPriorityEnum`  | [x] Done | 5a36c87687 |
| `RamBlockStatusControlEnum`        | [x] Done | 343d2af672 |
| `NvBlockDataMapping`               | [x] Done | cf9621f708 |
| `BulkNvDataDescriptor`             | [x] Done | 14a0a9cc5b |
| `RoleBasedDataAssignment`          | [x] Done | 5989355419 |
| `InstantiationDataDefProps`        | [x] Done | e2aa88eb41 |
| `NvBlockNeeds`                     | [x] Done | 72d998faaa |
| `NvBlockDescriptor`                | [x] Done | e5d43e9b06 |

## Group11

Status: **24/24** completed

| Class Name                             | Status   | Commit ID  |
| -------------------------------------- | -------- | ---------- |
| `ModeActivationKind`                   | [x] Done | 1625966930 |
| `ModeDeclarationGroupPrototypeMapping` | [x] Done | 96e9f073a2 |
| `ModeRequestTypeMap`                   | [x] Done | 2b824ca5f8 |
| `ClientServerApplicationErrorMapping`  | [x] Done | bc933575fd |
| `ClientServerOperationMapping`         | [x] Done | e301de1df9 |
| `ClientServerInterfaceMapping`         | [x] Done | cae5a51c92 |
| `ModeInterfaceMapping`                 | [x] Done | a598489544 |
| `VariableAndParameterInterfaceMapping` | [x] Done | 0e87cc4bb9 |
| `Field`                                | [x] Done | d31cad4d7e |
| `AbstractProvidedPortPrototype`        | [x] Done | 510d31dd57 |
| `AbstractRequiredPortPrototype`        | [x] Done | bbacb3368c |
| `ServiceProxySwComponentType`          | [x] Done | 74e821ccb8 |
| `ModeGroupInAtomicSwcInstanceRef`      | [x] Done | cdb0951050 |
| `OperationInAtomicSwcInstanceRef`      | [x] Done | 5d9a9f9600 |
| `RModeInAtomicSwcInstanceRef`          | [x] Done | 5a3a7d14c0 |
| `TriggerInAtomicSwcInstanceRef`        | [x] Done | 839264b3a6 |
| `PModeGroupInAtomicSwcInstanceRef`     | [x] Done | f517d795f6 |
| `RModeGroupInAtomicSWCInstanceRef`     | [x] Done | 7dd87307dd |
| `POperationInAtomicSwcInstanceRef`     | [x] Done | b6b0ea8cf7 |
| `ROperationInAtomicSwcInstanceRef`     | [x] Done | d7c9455251 |
| `RVariableInAtomicSwcInstanceRef`      | [x] Done | 2014bb1a51 |
| `PTriggerInAtomicSwcTypeInstanceRef`   | [x] Done | dc2297cba8 |
| `PPortInCompositionInstanceRef`        | [x] Done | b36a560be9 |
| `RPortInCompositionInstanceRef`        | [x] Done | 6056133191 |

## Group12

Status: **15/15** completed

| Class Name                           | Status   | Commit ID  |
| ------------------------------------ | -------- | ---------- |
| `ParameterAccess`                    | [x] Done | 3b9f111270 |
| `VariableAccessScopeEnum`            | [x] Done | 12e743cc9b |
| `VariableAccess`                     | [x] Done | 12e743cc9b |
| `InternalTriggeringPoint`            | [x] Done | 96033eb3fe |
| `ModeAccessPoint`                    | [x] Done | 543d9df4e7 |
| `ModeSwitchPoint`                    | [x] Done | 1037222ee7 |
| `AsynchronousServerCallReturnsEvent` | [x] Done | a706fd368b |
| `DataReceiveErrorEvent`              | [x] Done | b5ead83e20 |
| `DataReceivedEvent`                  | [x] Done | 5d23170856 |
| `DataSendCompletedEvent`             | [x] Done | 57e1abeea2 |
| `DataWriteCompletedEvent`            | [x] Done | df2a6b3a70 |
| `InternalTriggerOccurredEvent`       | [x] Done | ac0bbe5799 |
| `OperationInvokedEvent`              | [x] Done | e607622c82 |
| `RteEventInEcuInstanceRef`           | [x] Done | dd76ebd8bf |
| `VariableAccessInEcuInstanceRef`     | [x] Done | b52183a6b4 |

## Group13

Status: **23/23** completed

| Class Name                              | Status   | Commit ID  |
| --------------------------------------- | -------- | ---------- |
| `BswApiOptions`                         | [x] Done | 816c64f3d0 |
| `BswModuleCallPoint`                    | [x] Done | 879aacf8c4 |
| `BswDirectCallPoint`                    | [x] Done | 518ebf6a09 |
| `BswSynchronousServerCallPoint`         | [x] Done | f23ec00417 |
| `BswInternalTriggeringPoint`            | [x] Done | f67e3865ef |
| `BswInterruptEntity`                    | [x] Done | f19be09d07 |
| `BswModeSwitchAckRequest`               | [x] Done | 8d9cad6b3c |
| `BswDataReceptionPolicy`                | [x] Done | 893f5df32e |
| `BswQueuedDataReceptionPolicy`          | [x] Done | 254de705ea |
| `BswAsynchronousServerCallReturnsEvent` | [x] Done | f2df52d4b5 |
| `BswDataReceivedEvent`                  | [x] Done | e316f1e6ea |
| `BswInternalTriggerOccurredEvent`       | [x] Done | caffd21921 |
| `BswModeManagerErrorEvent`              | [x] Done | 91083c1916 |
| `BswModeSwitchedAckEvent`               | [x] Done | a250dbe4b5 |
| `BswTimingEvent`                        | [x] Done | 361ab10d5e |
| `BswEntryRelationshipEnum`              | [x] Done | ff1903b513 |
| `BswEntryRelationship`                  | [x] Done | 1872edcae1 |
| `BswEntryRelationshipSet`               | [x] Done | cdbfc4ebf0 |
| `BswModuleClientServerEntry`            | [x] Done | f57417a6a2 |
| `BswModuleDependency`                   | [x] Done | 7686874a67 |
| `SwcBswRunnableMapping`                 | [x] Done | 4f1681d55f |
| `SwcBswSynchronizedModeGroupPrototype`  | [x] Done | d024ea8472 |
| `SwcBswSynchronizedTrigger`             | [x] Done | c7756e2bea |

## Group14

Status: **25/25** completed

| Class Name                                 | Status   | Commit ID  |
| ------------------------------------------ | -------- | ---------- |
| `DiagnosticAudienceEnum`                   | [x] Done | 80d64e8f15 |
| `DiagnosticClearDtcNotificationEnum`       | [x] Done | 2415d2157a |
| `DiagnosticProcessingStyleEnum`            | [x] Done | d07b0d0144 |
| `DiagnosticRoutineTypeEnum`                | [x] Done | f9dc536d57 |
| `DiagnosticServiceRequestCallbackTypeEnum` | [x] Done | 77c7312cc8 |
| `DiagnosticValueAccessEnum`                | [x] Done | 85e9c3f3be |
| `DtcFormatTypeEnum`                        | [x] Done | f376d8339f |
| `DtcKindEnum`                              | [x] Done | 8b62eec625 |
| `ServiceDiagnosticRelevanceEnum`           | [x] Done | da3a2d3532 |
| `DiagnosticCapabilityElement`              | [x] Done | caf7dc3419 |
| `DiagnosticCommunicationManagerNeeds`      | [x] Done | 8c487102b9 |
| `DiagnosticEventInfoNeeds`                 | [x] Done | 99f3db39c4 |
| `DiagnosticRoutineNeeds`                   | [x] Done | 9f1a4310b7 |
| `DiagnosticValueNeeds`                     | [x] Done | 475d150577 |
| `DtcStatusChangeNotificationNeeds`         | [x] Done | 89407b6f0f |
| `CryptoServiceNeeds`                       | [x] Done | bea3457ed5 |
| `DiagEventDebounceCounterBased`            | [x] Done | f41b486233 |
| `SignalServiceTranslationElementProps`     | [x] Done | 8b6384cb3f |
| `DiagnosticServiceClass`                   | [x] Done | d19685ff4f |
| `DiagnosticJumpToBootLoaderEnum`           | [x] Done | d901d9ee70 |
| `DiagnosticLogicalOperatorEnum`            | [x] Done | a70421898e |
| `DiagnosticEnvConditionFormulaPart`        | [x] Done | 66e22b5a41 |
| `DiagnosticEnvConditionFormula`            | [x] Done | 9f4e1849ac |
| `DiagnosticEnvCompareCondition`            | [x] Done | e2c6fe29bb |
| `DiagnosticEnvModeElement`                 | [x] Done | 513c78a4a8 |

## Group15

Status: **24/24** completed

| Class Name                    | Status   | Commit ID  |
| ----------------------------- | -------- | ---------- |
| `CommunicationDirectionType`  | [x] Done | 7aa197e046 |
| `TransferPropertyEnum`        | [x] Done | f3a9dc08dd |
| `MultiplexedPart`             | [x] Done | 9ed9d78782 |
| `DynamicPart`                 | [x] Done | 82138518f9 |
| `SegmentPosition`             | [x] Done | 6c2d8befb2 |
| `ISignalPort`                 | [x] Done | 7a508bea29 |
| `ISignalIPduGroup`            | [x] Done | 4658ff431a |
| `MultiplexedIPdu`             | [x] Done | 2c2e102933 |
| `TriggerMode`                 | [x] Done | 2c2e102933 |
| `SecuredIPdu`                 | [x] Done | 2c2e102933 |
| `SecuredPduHeaderEnum`        | [x] Done | 2c2e102933 |
| `UserDefinedIPdu`             | [x] Done | 2c2e102933 |
| `UserDefinedPdu`              | [x] Done | 2c2e102933 |
| `SystemSignal`                | [x] Done | 7828064475 |
| `TimeRangeType`               | [x] Done | 7aa197e046 |
| `TimeRangeTypeTolerance`      | [x] Done | ba8d04cbb4 |
| `TransmissionModeCondition`   | [x] Done | 7a7ff3c5af |
| `TriggerIPduSendCondition`    | [x] Done | d2dbe59bf6 |
| `CyclicTiming`                | [x] Done | 7aa197e046 |
| `EventControlledTiming`       | [x] Done | 1649678501 |
| `FlexrayChannelName`          | [x] Done | f4ffa771cf |
| `PncGatewayTypeEnum`          | [x] Done | f4ffa771cf |
| `TransmissionModeTiming`      | [x] Done | f4ffa771cf |
| `TransmissionModeDeclaration` | [x] Done | f4ffa771cf |

## Group16

Status: **29/29** completed

| Class Name                              | Status   | Commit ID  |
| --------------------------------------- | -------- | ---------- |
| `RuntimeAddressConfigurationEnum`       | [x] Done | f24d8b53ba |
| `IpAddressKeepEnum`                     | [x] Done | 161a1b8215 |
| `Ipv6AddressSourceEnum`                 | [x] Done | a8fad12113 |
| `Ipv4AddressSourceEnum`                 | [x] Done | 8c0771cafd |
| `DoIpEntity`                            | [x] Done | a20bd931eb |
| `TpPort`                                | [x] Done | 0f6b1c9bfd |
| `InitialSdDelayConfig`                  | [x] Done | 84dc59b646 |
| `EthernetPriorityRegeneration`          | [x] Done | a513bd3ec3 |
| `TimeSyncServerConfiguration`           | [x] Done | 155cc2f7f9 |
| `CouplingPortAbstractShaper`            | [x] Done | f02e111f65 |
| `CouplingPortAsynchronousTrafficShaper` | [x] Done | 929cee7081 |
| `CouplingPortCreditBasedShaper`         | [x] Done | 929cee7081 |
| `MacMulticastGroup`                     | [x] Done | 9ee3f1b66a |
| `IPSecConfig`                           | [x] Done | d75eb10bff |
| `NetworkEndpoint`                       | [x] Done | 84587c11f6 |
| `VlanConfig`                            | [x] Done | eb32bcdeea |
| `Ipv4Configuration`                     | [x] Done | dcebacccb1 |
| `GenericTp`                             | [x] Done | 627b5c3a94 |
| `TcpTp`                                 | [x] Done | c59e3404da |
| `UdpTp`                                 | [x] Done | 5336dd0eae |
| `PduCollectionSemanticsEnum`            | [x] Done | 5d4adec228 |
| `SocketConnectionIpduIdentifier`        | [x] Done | c02cad3bb9 |
| `SocketConnectionBundle`                | [x] Done | 01f37f105c |
| `RequestResponseDelay`                  | [x] Done | 1c556f35b4 |
| `SdServerConfig`                        | [x] Done | f509df9d94 |
| `TcpOptionFilterList`                   | [x] Done | fd11862858 |
| `TcpOptionFilterSet`                    | [x] Done | 4b1494b6d2 |
| `IPv6ExtHeaderFilterList`               | [x] Done | d8127416ac |
| `TimeSynchronization`                   | [x] Done | f4a1df5bcb |

## Group17

Status: **26/26** completed

| Class Name                                 | Status   | Commit ID  |
| ------------------------------------------ | -------- | ---------- |
| `CanClusterBusOffRecovery`                 | [x] Done | 9c4a146ff0 |
| `CanCommunicationConnector`                | [x] Done | 6e9794500d |
| `CanControllerConfiguration`               | [x] Done | 5de9869ed6 |
| `CanControllerConfigurationRequirements`   | [x] Done | cd843bee26 |
| `CanControllerFdConfigurationRequirements` | [x] Done | a115435650 |
| `ResumePosition`                           | [x] Done | 40c0abb9b1 |
| `ApplicationEntry`                         | [x] Done | 8a6c27cb1c |
| `LinScheduleTable`                         | [x] Done | 0215ceb16a |
| `RunMode`                                  | [x] Done | 0215ceb16a |
| `LinCommunicationConnector`                | [x] Done | da0534323b |
| `FlexrayFrameTriggering`                   | [x] Done | 3ab64d2b03 |
| `FlexrayAbsolutelyScheduledTiming`         | [x] Done | 3ab64d2b03 |
| `FlexrayCommunicationConnector`            | [x] Done | 73bba1d58a |
| `FlexrayCommunicationController`           | [x] Done | 0c1ff9a927 |
| `FlexrayPhysicalChannel`                   | [x] Done | 7774a8ec9b |
| `DataMapping`                              | [x] Done | dc0553786f |
| `IndexedArrayElement`                      | [x] Done | 9eb93f743f |
| `SenderRecRecordElementMapping`            | [x] Done | dc019f9575 |
| `SenderRecRecordTypeMapping`               | [x] Done | abbfc40109 |
| `SenderReceiverToSignalMapping`            | [x] Done | 44442b8b6a |
| `SenderReceiverToSignalGroupMapping`       | [x] Done | f921dd6fb4 |
| `DefaultValueElement`                      | [x] Done | 721cca6400 |
| `FrameMapping`                             | [x] Done | a5f62ee06d |
| `ISignalMapping`                           | [x] Done | ba0f1a12a8 |
| `TargetIPduRef`                            | [x] Done | 4d2c155383 |
| `Gateway`                                  | [x] Done | a00d99f993 |

## Group18

Status: **17/17** completed

| Class Name                                  | Status   | Commit ID  |
| ------------------------------------------- | -------- | ---------- |
| `NmEcu`                                     | [x] Done | c5eafef533 |
| `CanNmCluster`                              | [x] Done | 97b3ffb12e |
| `UdpNmCluster`                              | [x] Done | c32d27a505 |
| `CanNmNode`                                 | [x] Done | 3d406b5e98 |
| `UdpNmNode`                                 | [x] Done | f933ce83ac |
| `CanNmClusterCoupling`                      | [x] Done | 8561fbb806 |
| `UdpNmClusterCoupling`                      | [x] Done | a1ffa0b85a |
| `FlexrayNmClusterCoupling`                  | [x] Done | 50b09ee73b |
| `SecOcCryptoServiceMapping`                 | [x] Done | eec98574a9 |
| `EndToEndTransformationISignalProps`        | [x] Done | 4c91e36810 |
| `TpAddress`                                 | [x] Done | cedb8f8498 |
| `LinTpConnection`                           | [x] Done | fa26bba13a |
| `EndToEndProtectionISignalIPdu`             | [x] Done | 7426eaaa52 |
| `SwcToEcuMapping`                           | [x] Done | fc5c1e2c39 |
| `ApplicationPartitionToEcuPartitionMapping` | [x] Done | baccb40d25 |
| `SwcToImplMapping`                          | [x] Done | 7fbdba572b |
| `AppOsTaskProxyToEcuTaskProxyMapping`       | [x] Done | 860f23a95c |

## Group19

Status: **16/16** completed

| Class Name                       | Status   | Commit ID  |
| -------------------------------- | -------- | ---------- |
| `ConfigReferenceValue`           | [x] Done | 7ed4c9a4a4 |
| `EcucValueCollection`            | [x] Done | b65b2313a2 |
| `ModuleConfiguration`            | [x] Done | 5cedb145b9 |
| `EcucConfigurationClassEnum`     | [x] Done | eb890b899c |
| `EcucScopeEnum`                  | [x] Done | 096c9544fc |
| `EcucDestinationUriDefRefType`   | [x] Done | 7047c575f7 |
| `EcucBooleanParamDef`            | [x] Done | b40b99238a |
| `EcucFloatParamDef`              | [x] Done | 454e47206b |
| `EcucForeignReferenceDef`        | [x] Done | 958007001d |
| `EcucLinkerSymbolDef`            | [x] Done | 776f61b1df |
| `EcucReferenceDef`               | [x] Done | 0d45067479 |
| `EcucSymbolicNameReferenceDef`   | [x] Done | 0d45067479 |
| `EcucUriReferenceDef`            | [x] Done | 0d45067479 |
| `EcucConditionFormula`           | [x] Done | 86096857ad |
| `EcucParameterDerivationFormula` | [x] Done | 16bd8cd3d0 |
| `EcucQueryExpression`            | [x] Done | a6ca958629 |

## Group20

Status: **29/29** completed

| Class Name                         | Status   | Commit ID  |
| ---------------------------------- | -------- | ---------- |
| `DoIpLogicAddress`                 | [x] Done | 20e0dbf1db |
| `DoIpTpConnection`                 | [x] Done | b71da200f5 |
| `CryptoKeySlotTypeEnum`            | [x] Done | cda30aac65 |
| `CryptoObjectTypeEnum`             | [x] Done | 4ee3d9b33c |
| `CryptoKeySlotAllowedModification` | [x] Done | 1b9c5d5f92 |
| `CryptoKeySlotContentAllowedUsage` | [x] Done | 0b871a8e8c |
| `DataLinkLayerRule`                | [x] Done | e65b8c621c |
| `NetworkLayerRule`                 | [x] Done | 68f8744c75 |
| `TransportLayerRule`               | [x] Done | 39d8f23c1d |
| `PayloadBytePatternRule`           | [x] Done | d77a6727fc |
| `SomeipProtocolRule`               | [x] Done | ebb82db445 |
| `SomeipSdRule`                     | [x] Done | 16c6ec4955 |
| `DoIpRule`                         | [x] Done | e1ebf1c4c5 |
| `MemorySection`                    | [x] Done | 6d92ecd979 |
| `SectionNamePrefix`                | [x] Done | bc26545b98 |
| `HardwareConfiguration`            | [x] Done | 3f0dca5050 |
| `SoftwareContext`                  | [x] Done | 45cf952f36 |
| `SoAdRoutingGroup`                 | [x] Done | 24f9dd86bd |
| `StackUsage`                       | [x] Done | 85a243308b |
| `MeasuredStackUsage`               | [x] Done | 05f494e759 |
| `RoughEstimateStackUsage`          | [x] Done | 575bb536fe |
| `WorstCaseStackUsage`              | [x] Done | 5692e873a3 |
| `MacAddressString`                 | [x] Done | 8b633b6dd3 |
| `PayloadBytePatternRulePart`       | [x] Done | 0cc195ce8e |
| `TcpRule`                          | [x] Done | 06d3147f65 |
| `IcmpRule`                         | [x] Done | c839e30e0e |
| `Ipv4Rule`                         | [x] Done | 817cf1a5de |
| `Ipv6Rule`                         | [x] Done | 38bc83357c |
| `UdpRule`                          | [x] Done | c871945ce1 |

## Group21

Status: **25/55** completed

| Class Name                           | Status       | Commit ID  |
| ------------------------------------ | ------------ | ---------- |
| `Identifier`                         | [x] Done*    | N/A        |
| `LLongName`                          | [x] Done*    | N/A        |
| `MixedContentForLongName`            | [x] Done*    | N/A        |
| `Referrable`                         | [x] Done*    | N/A        |
| `ReferrableSubtypesEnum`             | [x] Done     | a097cb3d4f |
| `SdgDef`                             | [x] Done     | c7d3958065 |
| `SdgElementWithGid`                  | [ ] Pending* | N/A        |
| `SdgClass`                           | [ ] Pending* | N/A        |
| `SdgAttribute`                       | [ ] Pending* | N/A        |
| `SdgAbstractPrimitiveAttribute`      | [ ] Pending* | N/A        |
| `SdgPrimitiveAttribute`              | [ ] Pending* | N/A        |
| `SdgPrimitiveAttributeWithVariation` | [ ] Pending* | N/A        |
| `SdgAggregationWithVariation`        | [ ] Pending* | N/A        |
| `SdgReference`                       | [ ] Pending* | N/A        |
| `SdgAbstractForeignReference`        | [ ] Pending* | N/A        |
| `SdgForeignReference`                | [ ] Pending* | N/A        |
| `SdgForeignReferenceWithVariation`   | [ ] Pending* | N/A        |
| `AbstractValueRestriction`           | [ ] Pending* | N/A        |
| `AbstractVariationRestriction`       | [ ] Pending* | N/A        |
| `FullBindingTimeEnum`                | [ ] Pending* | N/A        |
| `CIdentifier`                        | [ ] Pending* | N/A        |
| `CategoryString`                     | [ ] Pending* | N/A        |
| `DateTime`                           | [ ] Pending* | N/A        |
| `DiagRequirementIdString`            | [ ] Pending* | N/A        |
| `Ip4AddressString`                   | [ ] Pending* | N/A        |
| `Ip6AddressString`                   | [ ] Pending* | N/A        |
| `McdIdentifier`                      | [ ] Pending* | N/A        |
| `RegularExpression`                  | [ ] Pending* | N/A        |
| `RevisionLabelString`                | [ ] Pending* | N/A        |
| `SymbolString`                       | [ ] Pending* | N/A        |
| `UriString`                          | [ ] Pending* | N/A        |
| `VerbatimStringPlain`                | [ ] Pending* | N/A        |
| `CseCodeType`                        | [ ] Pending* | N/A        |
| `EvaluatedVariantSet`                | [ ] Pending* | N/A        |
| `PredefinedVariant`                  | [x] Done*    | N/A        |
| `DocumentationBlock`                 | [x] Done*    | N/A        |
| `MultiLanguageVerbatim`              | [x] Done*    | N/A        |
| `List`                               | [x] Done*    | N/A        |
| `LabeledList`                        | [x] Done*    | N/A        |
| `LabeledItem`                        | [x] Done*    | N/A        |
| `IndentSample`                       | [x] Done*    | N/A        |
| `ItemLabelPosEnum`                   | [x] Done*    | N/A        |
| `DefList`                            | [x] Done*    | N/A        |
| `DefItem`                            | [x] Done*    | N/A        |
| `MlFormula`                          | [x] Done*    | N/A        |
| `Note`                               | [x] Done*    | N/A        |
| `NoteTypeEnum`                       | [x] Done*    | N/A        |
| `Traceable`                          | [x] Done*    | N/A        |
| `EmphasisText`                       | [x] Done*    | N/A        |
| `IndexEntry`                         | [x] Done*    | N/A        |
| `Superscript`                        | [x] Done*    | N/A        |
| `Tt`                                 | [x] Done*    | N/A        |
| `EEnumFont`                          | [ ] Pending* | N/A        |
| `EEnum`                              | [ ] Pending* | N/A        |
| `DocumentationContext`               | [x] Done*    | N/A        |

## Group22

Status: **57/75** completed

| Class Name                             | Status       | Commit ID  |
| -------------------------------------- | ------------ | ---------- |
| `AnyInstanceRef`                       | [x] Done     | b64a3c317a |
| `Chapter`                              | [x] Done     | 0d13ccd1bc |
| `PredefinedChapter`                    | [x] Done     | 0af25ab2e5 |
| `FloatEnum`                            | [x] Done     | 1649678501 |
| `Topic1`                               | [x] Done     | 0d13ccd1bc |
| `TopicOrMsrQuery`                      | [x] Done     | 0d13ccd1bc |
| `ChapterOrMsrQuery`                    | [x] Done     | 0d13ccd1bc |
| `MsrQueryProps`                        | [x] Done     | 4566d4d4f7 |
| `MsrQueryArg`                          | [x] Done     | 4566d4d4f7 |
| `MultiLanguageOverviewParagraph`       | [x] Done     | 8294e5eeab |
| `PgwideEnum`                           | [x] Done     | 1649678501 |
| `MultiLanguagePlainText`               | [x] Done     | 53af1b9a63 |
| `LanguageSpecific`                     | [x] Done     | 4566d4d4f7 |
| `LEnum`                                | [x] Done     | 4566d4d4f7 |
| `AclPermission`                        | [ ] Pending* | 29d7cfc19d |
| `AclObjectSet`                         | [ ] Pending* | 11ad22dfad |
| `AclOperation`                         | [ ] Pending* | 0eb0409c12 |
| `AclRole`                              | [ ] Pending* | 8d5c387889 |
| `AclScopeEnum`                         | [ ] Pending* | dfa53c4352 |
| `LifeCycleStateDefinitionGroup`        | [ ] Pending* | 0c87fdbee4 |
| `LifeCycleState`                       | [ ] Pending* | 8f363946f9 |
| `ViewMapSet`                           | [ ] Pending* | f6dc7bb594 |
| `ViewMap`                              | [ ] Pending* | b48c08bba2 |
| `BswModuleDescription`                 | [x] Done     | 1a5b05b196 |
| `BswModuleEntry`                       | [x] Done     | 1a5b05b196 |
| `BswEntryKindEnum`                     | [x] Done     | 1a5b05b196 |
| `BswExecutionContext`                  | [x] Done     | 1a5b05b196 |
| `BswCallType`                          | [x] Done     | 1a5b05b196 |
| `SwServiceImplPolicyEnum`              | [x] Done     | 1a5b05b196 |
| `SwServiceArg`                         | [x] Done     | 596ec6e31e |
| `SwPointerTargetProps`                 | [x] Done     | c6247eb0db |
| `ArgumentDirectionEnum`                | [x] Done     | 8b7ab62280 |
| `ModeDeclarationGroup`                 | [x] Done     | e3d79f89ca |
| `ModeDeclaration`                      | [x] Done     | e3d79f89ca |
| `ModeTransition`                       | [x] Done     | e3d79f89ca |
| `ModeErrorBehavior`                    | [x] Done     | e3d79f89ca |
| `ModeErrorReactionPolicyEnum`          | [x] Done     | e3d79f89ca |
| `AccessCountSet`                       | [x] Done     | e3d1262da1 |
| `AccessCount`                          | [x] Done     | e3d1262da1 |
| `AbstractAccessPoint`                  | [x] Done     | e3d1262da1 |
| `InternalBehavior`                     | [x] Done     | 68e390b39e |
| `ExecutableEntity`                     | [x] Done     | 88b336bfe9 |
| `BswModuleEntity`                      | [x] Done     | 88b336bfe9 |
| `BswCalledEntity`                      | [x] Done     | bd96645681 |
| `BswSchedulableEntity`                 | [x] Done     | d2e2d7903d |
| `BswInterruptCategory`                 | [ ] Pending* | 87a572d24b |
| `BswAsynchronousServerCallPoint`       | [x] Done     | 80c7276bff |
| `BswAsynchronousServerCallResultPoint` | [x] Done     | e1150436c3 |
| `BswVariableAccess`                    | [ ] Pending* | d4d386b5c4 |
| `ExclusiveArea`                        | [x] Done     | aae3890b67 |
| `BswExclusiveAreaPolicy`               | [ ] Pending* | eb307c9898 |
| `ExclusiveAreaNestingOrder`            | [x] Done     | af5498712f |
| `BswSchedulerNamePrefix`               | [x] Done     | 2a4f60c8c4 |
| `BswEvent`                             | [x] Done     | af5498712f |
| `BswScheduleEvent`                     | [x] Done     | 46ce237162 |
| `BswInterruptEvent`                    | [x] Done     | acf1e772ac |
| `BswBackgroundEvent`                   | [x] Done     | 584344d2e4 |
| `BswOsTaskExecutionEvent`              | [x] Done     | 2b4b89810a |
| `BswExternalTriggerOccurredEvent`      | [ ] Pending* | a52b41da2c |
| `BswModeSwitchEvent`                   | [x] Done     | af5498712f |
| `BswOperationInvokedEvent`             | [ ] Pending* | dc465f6b33 |
| `BswTriggerDirectImplementation`       | [ ] Pending* | 0626aec9ca |
| `BswModeSenderPolicy`                  | [ ] Pending* | af6d69bbfa |
| `BswModeReceiverPolicy`                | [ ] Pending* | 2b15f92b16 |
| `ParameterDataPrototype`               | [x] Done     | 70ce06f500 |
| `BswDistinguishedPartition`            | [x] Done     | 80d341994f |
| `BswImplementation`                    | [x] Done     | 46ce237162 |
| `AutosarEngineeringObject`             | [x] Done     | e485a5bcb2 |
| `AlignmentType`                        | [ ] Pending* | 6133a30b31 |
| `SwAddrMethod`                         | [x] Done     | 70ce06f500 |
| `MemoryAllocationKeywordPolicyType`    | [x] Done     | 70ce06f500 |
| `SectionInitializationPolicyType`      | [x] Done     | 70ce06f500 |
| `MemorySectionType`                    | [x] Done     | 70ce06f500 |
| `HeapUsage`                            | [x] Done     | a55d2092d0 |
| `WorstCaseHeapUsage`                   | [x] Done     | a55d2092d0 |

## Group23

Status: **49/75** completed

| Class Name                                        | Status       | Commit ID  |
| ------------------------------------------------- | ------------ | ---------- |
| `MeasuredHeapUsage`                               | [x] Done     | N/A        |
| `RoughEstimateHeapUsage`                          | [x] Done     | N/A        |
| `ExecutionTime`                                   | [x] Done     | N/A        |
| `MemorySectionLocation`                           | [x] Done     | N/A        |
| `AnalyzedExecutionTime`                           | [x] Done     | N/A        |
| `MeasuredExecutionTime`                           | [x] Done     | N/A        |
| `SimulatedExecutionTime`                          | [x] Done     | N/A        |
| `RoughEstimateOfExecutionTime`                    | [x] Done     | N/A        |
| `McSupportData`                                   | [x] Done     | N/A        |
| `AliasNameSet`                                    | [x] Done     | N/A        |
| `AliasNameAssignment`                             | [x] Done     | N/A        |
| `McDataInstance`                                  | [x] Done     | N/A        |
| `McSwEmulationMethodSupport`                      | [x] Done     | N/A        |
| `McParameterElementGroup`                         | [x] Done     | N/A        |
| `ImplementationElementInParameterInstanceRef`     | [x] Done     | N/A        |
| `McFunction`                                      | [x] Done     | N/A        |
| `McFunctionDataRefSet`                            | [x] Done     | N/A        |
| `McGroup`                                         | [x] Done     | N/A        |
| `McGroupDataRefSet`                               | [x] Done     | N/A        |
| `McDataAccessDetails`                             | [x] Done     | N/A        |
| `RptSupportData`                                  | [x] Done     | N/A        |
| `RptSwPrototypingAccess`                          | [x] Done     | N/A        |
| `RptComponent`                                    | [x] Done     | N/A        |
| `RptExecutableEntity`                             | [x] Done     | N/A        |
| `RptExecutableEntityEvent`                        | [x] Done     | N/A        |
| `RptImplPolicy`                                   | [x] Done     | N/A        |
| `RptEnablerImplTypeEnum`                          | [x] Done     | N/A        |
| `RptPreparationEnum`                              | [x] Done     | N/A        |
| `RptExecutableEntityProperties`                   | [x] Done     | N/A        |
| `RptExecutionControlEnum`                         | [x] Done     | N/A        |
| `RptServicePointEnum`                             | [x] Done     | N/A        |
| `RptExecutionContext`                             | [x] Done     | N/A        |
| `RptAccessEnum`                                   | [x] Done     | N/A        |
| `RptServicePoint`                                 | [x] Done     | N/A        |
| `ServiceDependency`                               | [x] Done     | N/A        |
| `BswServiceDependency`                            | [x] Done     | N/A        |
| `RoleBasedBswModuleEntryAssignment`               | [x] Done     | N/A        |
| `RoleBasedDataTypeAssignment`                     | [x] Done     | N/A        |
| `MaxCommModeEnum`                                 | [x] Done     | N/A        |
| `SupervisedEntityNeeds`                           | [x] Done     | N/A        |
| `ComMgrUserNeeds`                                 | [x] Done     | N/A        |
| `DoIpServiceNeeds`                                | [x] Done     | N/A        |
| `DiagnosticIoControlNeeds`                        | [x] Done     | N/A        |
| `DiagnosticEventNeeds`                            | [x] Done     | N/A        |
| `DiagEventDebounceTimeBased`                      | [ ] Pending* | eb9e198676 |
| `ErrorTracerNeeds`                                | [x] Done     | N/A        |
| `TracedFailure`                                   | [x] Done     | N/A        |
| `DevelopmentError`                                | [x] Done     | N/A        |
| `RuntimeError`                                    | [x] Done     | N/A        |
| `DiagnosticDataIdentifier`                        | [ ] Pending* | 18cb600978 |
| `DiagnosticDynamicDataIdentifier`                 | [ ] Pending* | 6127bd9f00 |
| `DiagnosticAbstractDataIdentifier`                | [ ] Pending* | d32c585340 |
| `DiagnosticParameter`                             | [ ] Pending* | d1dafe3f06 |
| `DiagnosticParameterElement`                      | [ ] Pending* | e626d82fd2 |
| `DiagnosticParameterIdent`                        | [ ] Pending* | d666ff9ed7 |
| `DiagnosticAbstractParameter`                     | [ ] Pending* | 6665fb7d71 |
| `DiagnosticDataElement`                           | [ ] Pending* | 04e40cda05 |
| `DiagnosticContributionSet`                       | [ ] Pending* | 4c70e34d09 |
| `DiagnosticProtocol`                              | [ ] Pending* | 7324a51f2a |
| `TpConnectionIdent`                               | [x] Done     | N/A        |
| `DiagnosticCommonProps`                           | [ ] Pending* | 0b2c7c2fa7 |
| `DiagnosticOccurrenceCounterProcessingEnum`       | [ ] Pending* | 5d402fe9da |
| `DiagnosticTypeOfDtcSupportedEnum`                | [ ] Pending* | 210840b945 |
| `DiagnosticEventCombinationBehaviorEnum`          | [ ] Pending* | c5c9c65c4b |
| `DiagnosticEventCombinationReportingBehaviorEnum` | [ ] Pending* | d36baa82d6 |
| `DiagnosticCustomServiceInstance`                 | [ ] Pending* | 6beeb07b01 |
| `DiagnosticCustomServiceClass`                    | [ ] Pending* | 259d8d82a3 |
| `DiagnosticAuthRole`                              | [ ] Pending* | 16e3c0c30d |
| `DiagnosticCompareTypeEnum`                       | [ ] Pending* | cc55d1d351 |
| `DiagnosticEnvDataCondition`                      | [ ] Pending* | 19d7cb9cd6 |
| `DiagnosticEnvDataElementCondition`               | [ ] Pending* | 519aca8534 |
| `DiagnosticEnvModeCondition`                      | [ ] Pending* | 4e6f0e3039 |
| `DiagnosticEnvSwcModeElement`                     | [ ] Pending* | 4e64e33afe |
| `DiagnosticEnvBswModeElement`                     | [ ] Pending* | 9b90205857 |
| `DiagnosticSessionControl`                        | [ ] Pending* | a68f0804fd |

## Group24

Status: **1/75** completed

| Class Name                                                 | Status       | Commit ID  |
| ---------------------------------------------------------- | ------------ | ---------- |
| `DiagnosticSessionControlClass`                            | [ ] Pending* | 8145a0178a |
| `DiagnosticSecurityAccess`                                 | [ ] Pending* | 4b106b2461 |
| `DiagnosticSecurityAccessClass`                            | [ ] Pending* | 17ef969f39 |
| `DiagnosticAuthentication`                                 | [ ] Pending* | 13ac1a6b3d |
| `DiagnosticAuthenticationClass`                            | [ ] Pending* | 50e51bce63 |
| `DiagnosticAuthenticationConfiguration`                    | [ ] Pending* | 3d83a383d7 |
| `DiagnosticVerifyCertificateBidirectional`                 | [ ] Pending* | 5f62e6dbb3 |
| `DiagnosticVerifyCertificateUnidirectional`                | [ ] Pending* | 682e50a2dd |
| `DiagnosticDeAuthentication`                               | [ ] Pending* | 66e8ab9738 |
| `DiagnosticProofOfOwnership`                               | [ ] Pending* | 3ef2fb8c98 |
| `DiagnosticAuthTransmitCertificate`                        | [ ] Pending* | 94a9c9715c |
| `DiagnosticAuthTransmitCertificateEvaluation`              | [ ] Pending* | 4a21071b3d |
| `DiagnosticEcuReset`                                       | [ ] Pending* | 4a568086da |
| `DiagnosticEcuResetClass`                                  | [ ] Pending* | 092a0c7cf2 |
| `DiagnosticResponseToEcuResetEnum`                         | [ ] Pending* | 4c37389432 |
| `CommunicationCluster`                                     | [x] Done     | N/A        |
| `DiagnosticComControl`                                     | [ ] Pending* | ed6ddee3af |
| `DiagnosticComControlSpecificChannel`                      | [ ] Pending* | c4bee1d353 |
| `DiagnosticComControlClass`                                | [ ] Pending* | cd8cd8c462 |
| `DiagnosticComControlSubNodeChannel`                       | [ ] Pending* | f0a80d0b50 |
| `DiagnosticControlDTCSetting`                              | [ ] Pending* | a4ebfc734f |
| `DiagnosticControlDTCSettingClass`                         | [ ] Pending* | 88c545f303 |
| `DiagnosticReadDataByIdentifier`                           | [ ] Pending* | e21b844ed0 |
| `DiagnosticWriteDataByIdentifier`                          | [ ] Pending* | 699b751820 |
| `DiagnosticWriteDataByIdentifierClass`                     | [ ] Pending* | 6f777e6bd6 |
| `DiagnosticDataByIdentifier`                               | [ ] Pending* | 06afa0fffc |
| `DiagnosticReadDataByIdentifierClass`                      | [ ] Pending* | 01e18bd76d |
| `DiagnosticReadScalingDataByIdentifier`                    | [ ] Pending* | d8d4379d16 |
| `DiagnosticReadScalingDataByIdentifierClass`               | [ ] Pending* | 6c6eadab3d |
| `DiagnosticIOControl`                                      | [ ] Pending* | 3e204165ec |
| `DiagnosticIoControlClass`                                 | [ ] Pending* | a6a5ff87e4 |
| `DiagnosticControlEnableMaskBit`                           | [ ] Pending* | e7a05b899d |
| `DiagnosticRoutineSubfunction`                             | [ ] Pending* | 1b16d614ce |
| `DiagnosticRoutine`                                        | [ ] Pending* | 5f356c335d |
| `DiagnosticStartRoutine`                                   | [ ] Pending* | 30d5576f71 |
| `DiagnosticStopRoutine`                                    | [ ] Pending* | 35e0590e6f |
| `DiagnosticRequestRoutineResults`                          | [ ] Pending* | c5c5cddd74 |
| `DiagnosticRoutineControl`                                 | [ ] Pending* | b7485f7941 |
| `DiagnosticRoutineControlClass`                            | [ ] Pending* | 4605fa8439 |
| `DiagnosticDynamicallyDefineDataIdentifier`                | [ ] Pending* | 4988b642d4 |
| `DiagnosticDynamicallyDefineDataIdentifierClass`           | [ ] Pending* | 32e309baac |
| `DiagnosticHandleDDDIConfigurationEnum`                    | [ ] Pending* | 3cde2dacdd |
| `DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum` | [ ] Pending* | aa69f0bd9f |
| `DiagnosticReadDataByPeriodicID`                           | [ ] Pending* | 825e744a07 |
| `DiagnosticReadDataByPeriodicIDClass`                      | [ ] Pending* | d9cdc58eb4 |
| `DiagnosticPeriodicRate`                                   | [ ] Pending* | c3a080fdc4 |
| `DiagnosticPeriodicRateCategoryEnum`                       | [ ] Pending* | 051ec169f1 |
| `DiagnosticResponseOnEvent`                                | [ ] Pending* | cd643b2b96 |
| `DiagnosticResponseOnEventClass`                           | [ ] Pending* | e39a10b0d8 |
| `DiagnosticEventWindow`                                    | [ ] Pending* | e449ef97af |
| `DiagnosticEventWindowTimeEnum`                            | [ ] Pending* | 2de5f4a019 |
| `DiagnosticResponseOnEventActionEnum`                      | [ ] Pending* | 96ca415327 |
| `DiagnosticReadDTCInformation`                             | [ ] Pending* | 9ac51b650d |
| `DiagnosticReadDTCInformationClass`                        | [ ] Pending* | 4b113a2dec |
| `DiagnosticClearDiagnosticInformation`                     | [ ] Pending* | 3165f87844 |
| `DiagnosticClearDiagnosticInformationClass`                | [ ] Pending* | b797bc6514 |
| `DiagnosticMemoryByAddress`                                | [ ] Pending* | 97eb7a99d9 |
| `DiagnosticMemoryAddressableRangeAccess`                   | [ ] Pending* | e6d1099722 |
| `DiagnosticMemoryIdentifier`                               | [ ] Pending* | 39631ea784 |
| `DiagnosticWriteMemoryByAddress`                           | [ ] Pending* | 3400bec9c3 |
| `DiagnosticWriteMemoryByAddressClass`                      | [ ] Pending* | 223a5cbba7 |
| `DiagnosticReadMemoryByAddress`                            | [ ] Pending* | e0b6796763 |
| `DiagnosticReadMemoryByAddressClass`                       | [ ] Pending* | 314e86ace0 |
| `DiagnosticTransferExit`                                   | [ ] Pending* | 1461a0d679 |
| `DiagnosticTransferExitClass`                              | [ ] Pending* | 4c14a1b1d3 |
| `DiagnosticDataTransfer`                                   | [ ] Pending* | 8d1719c7a9 |
| `DiagnosticDataTransferClass`                              | [ ] Pending* | 8d1719c7a9 |
| `DiagnosticRequestDownload`                                | [ ] Pending* | b24aedab49 |
| `DiagnosticRequestDownloadClass`                           | [ ] Pending* | 16a6c77acf |
| `DiagnosticRequestUpload`                                  | [ ] Pending* | 4c29de936a |
| `DiagnosticRequestUploadClass`                             | [ ] Pending* | a5bf545f08 |
| `DiagnosticRequestFileTransfer`                            | [ ] Pending* | d34685d2ab |
| `DiagnosticRequestFileTransferClass`                       | [ ] Pending* | 46f42c1284 |
| `DiagnosticParameterIdentifier`                            | [ ] Pending* | 69777441f4 |
| `DiagnosticParameterSupportInfo`                           | [ ] Pending* | 86cc1e2205 |

## Group25

Status: **0/75** completed

| Class Name                                                | Status       | Commit ID  |
| --------------------------------------------------------- | ------------ | ---------- |
| `DiagnosticSupportInfoByte`                               | [ ] Pending* | 80af808a62 |
| `DiagnosticRequestCurrentPowertrainData`                  | [ ] Pending* | 37165c5751 |
| `DiagnosticRequestCurrentPowertrainDataClass`             | [ ] Pending* | b278ba1550 |
| `DiagnosticRequestPowertrainFreezeFrameData`              | [ ] Pending* | 1d44c26c8d |
| `DiagnosticRequestPowertrainFreezeFrameDataClass`         | [ ] Pending* | 0f9475a2f5 |
| `DiagnosticPowertrainFreezeFrame`                         | [ ] Pending* | b742a3633b |
| `DiagnosticRequestEmissionRelatedDTC`                     | [ ] Pending* | 6e6de52f5d |
| `DiagnosticRequestEmissionRelatedDTCClass`                | [ ] Pending* | 6112add0b4 |
| `DiagnosticClearResetEmissionRelatedInfo`                 | [ ] Pending* | 1d583075c7 |
| `DiagnosticClearResetEmissionRelatedInfoClass`            | [ ] Pending* | 95c27f01ee |
| `DiagnosticRequestOnBoardMonitoringTestResults`           | [ ] Pending* | 5d8bb0b9aa |
| `DiagnosticRequestOnBoardMonitoringTestResultsClass`      | [ ] Pending* | 445d4e053f |
| `DiagnosticRequestControlOfOnBoardDevice`                 | [ ] Pending* | a14b698533 |
| `DiagnosticRequestControlOfOnBoardDeviceClass`            | [ ] Pending* | a919e664e8 |
| `DiagnosticTestRoutineIdentifier`                         | [ ] Pending* | 95790f92b8 |
| `DiagnosticRequestVehicleInfo`                            | [ ] Pending* | a1dca9869b |
| `DiagnosticRequestVehicleInfoClass`                       | [ ] Pending* | 4a2725a98e |
| `DiagnosticInfoType`                                      | [ ] Pending* | 87a45b092d |
| `DiagnosticRequestEmissionRelatedDTCPermanentStatus`      | [ ] Pending* | c50712427c |
| `DiagnosticRequestEmissionRelatedDTCPermanentStatusClass` | [ ] Pending* | bc59ec221e |
| `DiagnosticEvent`                                         | [ ] Pending* | b1378989c8 |
| `DiagnosticClearEventAllowedBehaviorEnum`                 | [ ] Pending* | 3ad75e1261 |
| `DiagnosticConnectedIndicator`                            | [ ] Pending* | b2e6b63410 |
| `DiagnosticEventClearAllowedEnum`                         | [ ] Pending* | 2bae144488 |
| `DiagnosticEventKindEnum`                                 | [ ] Pending* | aa744716cf |
| `DiagnosticConnectedIndicatorBehaviorEnum`                | [ ] Pending* | faf9703711 |
| `DiagnosticTroubleCodeUds`                                | [ ] Pending* | fbead45f73 |
| `DiagnosticTroubleCodeObd`                                | [ ] Pending* | 5c4cbcc4b5 |
| `EventObdReadinessGroup`                                  | [ ] Pending* | 51dbeac91d |
| `DiagnosticTroubleCode`                                   | [ ] Pending* | 086b29c68d |
| `DiagnosticTroubleCodeGroup`                              | [ ] Pending* | 6e16251e8a |
| `DiagnosticMemoryDestination`                             | [ ] Pending* | be5b392c44 |
| `DiagnosticMemoryEntryStorageTriggerEnum`                 | [ ] Pending* | e550cdfbd3 |
| `DiagnosticClearDtcLimitationEnum`                        | [ ] Pending* | 6b187ebfae |
| `DiagnosticEventDisplacementStrategyEnum`                 | [ ] Pending* | 4a5813b099 |
| `DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum` | [ ] Pending* | c97cedd4d1 |
| `DiagnosticTypeOfFreezeFrameRecordNumerationEnum`         | [ ] Pending* | 4e24dc1bed |
| `DiagnosticMemoryDestinationPrimary`                      | [ ] Pending* | 9d32504d97 |
| `DiagnosticMemoryDestinationUserDefined`                  | [ ] Pending* | 570c9983ad |
| `DiagnosticTroubleCodeProps`                              | [ ] Pending* | 39f801ec7e |
| `DiagnosticSignificanceEnum`                              | [ ] Pending* | 9d20f1f7ce |
| `DiagnosticUdsSeverityEnum`                               | [ ] Pending* | 056b7c5e0c |
| `DiagnosticDataIdentifierSet`                             | [ ] Pending* | 303f7cf31d |
| `DiagnosticWwhObdDtcClassEnum`                            | [ ] Pending* | 5663344175 |
| `DiagnosticTroubleCodeUdsToTroubleCodeObdMapping`         | [ ] Pending* | 1f194826e7 |
| `DiagnosticExtendedDataRecord`                            | [ ] Pending* | a200a96695 |
| `DiagnosticRecordTriggerEnum`                             | [ ] Pending* | 38bfd94d4b |
| `DiagnosticFreezeFrame`                                   | [ ] Pending* | 6c6c31d224 |
| `DiagnosticCondition`                                     | [ ] Pending* | 48dbae418f |
| `DiagnosticEnableCondition`                               | [ ] Pending* | 3acb287717 |
| `DiagnosticStorageCondition`                              | [ ] Pending* | bd5949a41b |
| `DiagnosticDebounceAlgorithmProps`                        | [ ] Pending* | 4a6604c7b5 |
| `DiagnosticDebounceBehaviorEnum`                          | [ ] Pending* | 165e554f17 |
| `DiagnosticConditionGroup`                                | [ ] Pending* | c04fdb8f07 |
| `DiagnosticEnableConditionGroup`                          | [ ] Pending* | ceea3ebd37 |
| `DiagnosticStorageConditionGroup`                         | [ ] Pending* | 7b05bc91b8 |
| `DiagnosticOperationCycle`                                | [ ] Pending* | b5e7e1ec12 |
| `DiagnosticOperationCycleTypeEnum`                        | [ ] Pending* | 03a924f74f |
| `DiagnosticAging`                                         | [ ] Pending* | c4704e8f01 |
| `DiagnosticIndicator`                                     | [ ] Pending* | e603f3f050 |
| `DiagnosticTestResultUpdateEnum`                          | [ ] Pending* | af61dd3966 |
| `DiagnosticTestIdentifier`                                | [ ] Pending* | f7cd643add |
| `DiagnosticMeasurementIdentifier`                         | [ ] Pending* | 5d908b94d8 |
| `DiagnosticEcuInstanceProps`                              | [ ] Pending* | 84408cb8c9 |
| `DiagnosticObdSupportEnum`                                | [ ] Pending* | bfaab4368c |
| `DiagnosticIumpr`                                         | [ ] Pending* | 3dce1b74b0 |
| `DiagnosticIumprKindEnum`                                 | [ ] Pending* | 015af36ca8 |
| `DiagnosticIumprGroup`                                    | [ ] Pending* | 02133e7e76 |
| `DiagnosticIumprGroupIdentifier`                          | [ ] Pending* | 0b26bf6ac0 |
| `DiagnosticIumprDenominatorGroup`                         | [ ] Pending* | e1a516d394 |
| `DiagnosticFimAliasEvent`                                 | [ ] Pending* | ea393b05d8 |
| `DiagnosticAbstractAliasEvent`                            | [ ] Pending* | 5ff78dec55 |
| `DiagnosticFunctionIdentifier`                            | [ ] Pending* | dc026145a3 |
| `DiagnosticFunctionIdentifierInhibit`                     | [ ] Pending* | 27e01b0795 |
| `DiagnosticFunctionInhibitSource`                         | [ ] Pending* | fd3444a79c |

## Group26

Status: **1/75** completed

| Class Name                                      | Status       | Commit ID  |
| ----------------------------------------------- | ------------ | ---------- |
| `DiagnosticInhibitionMaskEnum`                  | [ ] Pending* | N/A        |
| `DiagnosticFimEventGroup`                       | [ ] Pending* | N/A        |
| `DiagnosticJ1939Spn`                            | [ ] Pending* | ad6e53e6fe |
| `DiagnosticJ1939FreezeFrame`                    | [ ] Pending* | 0314338bf5 |
| `DiagnosticJ1939ExpandedFreezeFrame`            | [ ] Pending* | 0314338bf5 |
| `DiagnosticTroubleCodeJ1939DtcKindEnum`         | [ ] Pending* | e51e632f04 |
| `DiagnosticTroubleCodeJ1939`                    | [ ] Pending* | e51e632f04 |
| `DiagnosticMapping`                             | [ ] Pending* | fd3e548259 |
| `DiagnosticServiceDataMapping`                  | [ ] Pending* | 80105a7831 |
| `DiagnosticParameterElementAccess`              | [ ] Pending* | 80105a7831 |
| `DiagnosticServiceMappingDiagTarget`            | [ ] Pending* | 80105a7831 |
| `DiagnosticSwMapping`                           | [ ] Pending* | 80105a7831 |
| `DiagnosticServiceSwMapping`                    | [ ] Pending* | 0f2a3876e3 |
| `BswServiceDependencyIdent`                     | [x] Done     | d488a5e4a8 |
| `DiagnosticAuthTransmitCertificateMapping`      | [ ] Pending* | 531da6dd58 |
| `DiagnosticSecurityEventReportingModeMapping`   | [ ] Pending* | 531da6dd58 |
| `DiagnosticEventToTroubleCodeUdsMapping`        | [ ] Pending* | 664519e02e |
| `DiagnosticEventToOperationCycleMapping`        | [ ] Pending* | 664519e02e |
| `DiagnosticEventToDebounceAlgorithmMapping`     | [ ] Pending* | 664519e02e |
| `DiagnosticEventToEnableConditionGroupMapping`  | [ ] Pending* | 664519e02e |
| `DiagnosticEventToStorageConditionGroupMapping` | [ ] Pending* | 664519e02e |
| `DiagnosticEventPortMapping`                    | [ ] Pending* | 266d4f7aa4 |
| `DiagnosticOperationCyclePortMapping`           | [ ] Pending* | 266d4f7aa4 |
| `DiagnosticEnableConditionPortMapping`          | [ ] Pending* | 266d4f7aa4 |
| `DiagnosticStorageConditionPortMapping`         | [ ] Pending* | 266d4f7aa4 |
| `DiagnosticDemProvidedDataMapping`              | [ ] Pending* | 531da6dd58 |
| `DiagnosticMasterToSlaveEventMapping`           | [ ] Pending* | 531da6dd58 |
| `DiagnosticEventToSecurityEventMapping`         | [ ] Pending* | 531da6dd58 |
| `DiagnosticInhibitSourceEventMapping`           | [ ] Pending* | d488a5e4a8 |
| `DiagnosticFimAliasEventMapping`                | [ ] Pending* | d488a5e4a8 |
| `DiagnosticFimAliasEventGroup`                  | [ ] Pending* | d488a5e4a8 |
| `DiagnosticFimAliasEventGroupMapping`           | [ ] Pending* | d488a5e4a8 |
| `DiagnosticFimFunctionMapping`                  | [ ] Pending* | 86bff0a4f2 |
| `DiagnosticIumprToFunctionIdentifierMapping`    | [ ] Pending* | 86bff0a4f2 |
| `DiagnosticJ1939SpnMapping`                     | [ ] Pending* | 86bff0a4f2 |
| `DiagnosticJ1939Node`                           | [ ] Pending* | 86bff0a4f2 |
| `DiagnosticJ1939SwMapping`                      | [ ] Pending* | 86bff0a4f2 |
| `DiagnosticEventToTroubleCodeJ1939Mapping`      | [ ] Pending* | 86bff0a4f2 |
| `CpSoftwareClusterResource`                     | [ ] Pending* | 9c0046237b |
| `RoleBasedResourceDependency`                   | [ ] Pending* | 9c0046237b |
| `CpSwClusterToDiagEventMapping`                 | [ ] Pending* | 9c0046237b |
| `CpSwClusterResourceToDiagDataElemMapping`      | [ ] Pending* | 9c0046237b |
| `CpSwClusterToDiagRoutineSubfunctionMapping`    | [ ] Pending* | 9c0046237b |
| `CpSwClusterResourceToDiagFunctionIdMapping`    | [ ] Pending* | 9c0046237b |
| `EcucDefinitionCollection`                      | [ ] Pending* | 4c76344b21 |
| `EcucModuleDef`                                 | [ ] Pending* | 3dd8367d26 |
| `EcucContainerDef`                              | [ ] Pending* | d497b88ae7 |
| `EcucParamConfContainerDef`                     | [ ] Pending* | 571d1bb8d7 |
| `EcucChoiceContainerDef`                        | [ ] Pending* | 416e583ff2 |
| `EcucDefinitionElement`                         | [ ] Pending* | ac47ae89f3 |
| `EcucCommonAttributes`                          | [ ] Pending* | b5ba9d4e2f |
| `EcucAbstractConfigurationClass`                | [ ] Pending* | 6549a18aee |
| `EcucValueConfigurationClass`                   | [ ] Pending* | 6549a18aee |
| `EcucMultiplicityConfigurationClass`            | [ ] Pending* | 6549a18aee |
| `EcucConfigurationVariantEnum`                  | [ ] Pending* | 5ce1bb021e |
| `EcucParameterDef`                              | [ ] Pending* | bf479d9bf8 |
| `EcucIntegerParamDef`                           | [ ] Pending* | 62c89e7a96 |
| `EcucAbstractStringParamDef`                    | [ ] Pending* | 024153f73a |
| `EcucStringParamDef`                            | [ ] Pending* | 0e1c4660e5 |
| `EcucMultilineStringParamDef`                   | [ ] Pending* | fdee6f9a41 |
| `EcucFunctionNameDef`                           | [ ] Pending* | e44edd9d6d |
| `EcucEnumerationParamDef`                       | [ ] Pending* | 5085d038de |
| `EcucEnumerationLiteralDef`                     | [ ] Pending* | 48d98b4b49 |
| `EcucAddInfoParamDef`                           | [ ] Pending* | cf5c0e3618 |
| `EcucAbstractReferenceDef`                      | [ ] Pending* | 1475d37c0d |
| `EcucAbstractInternalReferenceDef`              | [ ] Pending* | 0035a3d952 |
| `EcucAbstractExternalReferenceDef`              | [ ] Pending* | af8e9109c7 |
| `EcucChoiceReferenceDef`                        | [ ] Pending* | b85e3d5202 |
| `EcucInstanceReferenceDef`                      | [ ] Pending* | c27549b512 |
| `EcucDestinationUriDefSet`                      | [ ] Pending* | f580ebdeec |
| `EcucDestinationUriDef`                         | [ ] Pending* | 2f69e3cc20 |
| `EcucDestinationUriPolicy`                      | [ ] Pending* | 37330e12c0 |
| `EcucDestinationUriNestingContractEnum`         | [ ] Pending* | 9a8cb02be7 |
| `EcucDerivationSpecification`                   | [ ] Pending* | 91a9e3ee35 |
| `EcucQuery`                                     | [ ] Pending* | 8bb9dbd181 |

## Group27

Status: **0/75** completed

| Class Name                                  | Status       | Commit ID  |
| ------------------------------------------- | ------------ | ---------- |
| `EcucConditionSpecification`                | [ ] Pending* | 901e5bb4c3 |
| `EcucValidationCondition`                   | [ ] Pending* | 401e19fd2d |
| `EcucIndexableValue`                        | [ ] Pending* | 7fa66d34f9 |
| `EcucModuleConfigurationValues`             | [ ] Pending* | 963ae8fcfc |
| `EcucContainerValue`                        | [ ] Pending* | 319fcf7080 |
| `EcucParameterValue`                        | [ ] Pending* | de8db969b1 |
| `EcucTextualParamValue`                     | [ ] Pending* | b4a24a5d87 |
| `EcucNumericalParamValue`                   | [ ] Pending* | c2eb1c04d2 |
| `EcucAddInfoParamValue`                     | [ ] Pending* | 0c30fe6b6b |
| `EcucAbstractReferenceValue`                | [ ] Pending* | b5f9232413 |
| `EcucReferenceValue`                        | [ ] Pending* | 5986011aa6 |
| `EcucInstanceReferenceValue`                | [ ] Pending* | 9d34a15176 |
| `HwDescriptionEntity`                       | [ ] Pending* | 8a55380861 |
| `HwPinGroupContent`                         | [ ] Pending* | cb322b20cb |
| `HwElementConnector`                        | [ ] Pending* | f48bef4731 |
| `HwPinGroupConnector`                       | [ ] Pending* | acdd47866a |
| `HwPinConnector`                            | [ ] Pending* | 2bf0929ad2 |
| `CommunicationController`                   | [ ] Pending* | f3e797c458 |
| `ParameterSwComponentType`                  | [ ] Pending* | e82f0ed83e |
| `SwComponentType`                           | [ ] Pending* | 9e3500a78f |
| `AtomicSwComponentType`                     | [ ] Pending* | 184f2d7e82 |
| `ApplicationSwComponentType`                | [ ] Pending* | 31ce617eb9 |
| `SwConnector`                               | [ ] Pending* | 9c9cfd33ef |
| `PassThroughSwConnector`                    | [ ] Pending* | 1c0ee7d639 |
| `InstantiationTimingEventProps`             | [ ] Pending* | 38df536d98 |
| `InstantiationRTEEventProps`                | [ ] Pending* | aaffe85cbf |
| `PortInterface`                             | [ ] Pending* | ea81891ead |
| `ServiceProviderEnum`                       | [ ] Pending* | 5935adb517 |
| `ClientServerInterface`                     | [ ] Pending* | d1b24784a9 |
| `ClientServerOperation`                     | [ ] Pending* | 15345a61f7 |
| `ArgumentDataPrototype`                     | [ ] Pending* | 6f30a16016 |
| `ServerArgumentImplPolicyEnum`              | [ ] Pending* | f045532a3c |
| `ApplicationError`                          | [ ] Pending* | 10a69b5248 |
| `ModeSwitchInterface`                       | [ ] Pending* | a16d0c351f |
| `DataPrototypeMapping`                      | [ ] Pending* | 2b08d90f5a |
| `ModeDeclarationMapping`                    | [ ] Pending* | 9df12a627d |
| `ImplementationDataTypeSubElementRef`       | [ ] Pending* | 048dfdbb1f |
| `ApplicationCompositeDataTypeSubElementRef` | [ ] Pending* | 46a5c6be3e |
| `MappingDirectionEnum`                      | [ ] Pending* | 9ed89eb9e6 |
| `TextTableValuePair`                        | [ ] Pending* | ee2a8edc68 |
| `DataTransformation`                        | [ ] Pending* | e34755cfd8 |
| `DataTransformationKindEnum`                | [ ] Pending* | 19d7d01e4d |
| `SenderReceiverAnnotation`                  | [ ] Pending* | 21808a1f74 |
| `SenderAnnotation`                          | [ ] Pending* | f0a69daa65 |
| `ReceiverAnnotation`                        | [ ] Pending* | f2020f54b4 |
| `ProcessingKindEnum`                        | [ ] Pending* | 97030aba64 |
| `DataLimitKindEnum`                         | [ ] Pending* | 87507e7bed |
| `ClientServerAnnotation`                    | [ ] Pending* | a5e2f7c628 |
| `IoHwAbstractionServerAnnotation`           | [ ] Pending* | 315b01de98 |
| `FilterDebouncingEnum`                      | [ ] Pending* | c23b544607 |
| `PulseTestEnum`                             | [ ] Pending* | b532d9a217 |
| `ParameterPortAnnotation`                   | [ ] Pending* | 9d56752e39 |
| `ModePortAnnotation`                        | [ ] Pending* | 2849ecb9cd |
| `TriggerPortAnnotation`                     | [ ] Pending* | f2d78fca39 |
| `NvDataPortAnnotation`                      | [ ] Pending* | b0ec28fdd3 |
| `DelegatedPortAnnotation`                   | [ ] Pending* | 1461e45c24 |
| `SignalFanEnum`                             | [ ] Pending* | 332ce34385 |
| `PPortComSpec`                              | [ ] Pending* | N/A        |
| `RPortComSpec`                              | [ ] Pending* | N/A        |
| `ReceiverComSpec`                           | [ ] Pending* | N/A        |
| `HandleOutOfRangeStatusEnum`                | [ ] Pending* | N/A        |
| `NonqueuedReceiverComSpec`                  | [ ] Pending* | 4179558606 |
| `HandleTimeoutEnum`                         | [ ] Pending* | cd413d6680 |
| `TimeValue`                                 | [ ] Pending* | e079162eb7 |
| `SenderComSpec`                             | [ ] Pending* | a598c3519b |
| `NonqueuedSenderComSpec`                    | [ ] Pending* | f6f67d00a4 |
| `TransmissionComSpecProps`                  | [ ] Pending* | 3c8b18ca27 |
| `TransmissionAcknowledgementRequest`        | [ ] Pending* | 1dbcef9926 |
| `HandleOutOfRangeEnum`                      | [ ] Pending* | fd8d9ec9f7 |
| `TransmissionModeDefinitionEnum`            | [ ] Pending* | f13828d9d5 |
| `ClientComSpec`                             | [ ] Pending* | 1a86c955e2 |
| `ServerComSpec`                             | [ ] Pending* | c0dcb9aff0 |
| `ParameterProvideComSpec`                   | [ ] Pending* | e41ac253ae |
| `TransformationComSpecProps`                | [ ] Pending* | 720b97ba6d |
| `TransformationTechnology`                  | [ ] Pending* | fecff00ac5 |

## Group28

Status: **0/75** completed

| Class Name                                   | Status       | Commit ID  |
| -------------------------------------------- | ------------ | ---------- |
| `BufferProperties`                           | [ ] Pending* | N/A        |
| `TransformationDescription`                  | [ ] Pending* | N/A        |
| `TransformerClassEnum`                       | [ ] Pending* | N/A        |
| `EndToEndTransformationComSpecProps`         | [ ] Pending* | N/A        |
| `E2EProfileCompatibilityProps`               | [ ] Pending* | N/A        |
| `EndToEndProtection`                         | [ ] Pending* | N/A        |
| `ConsistencyNeeds`                           | [ ] Pending* | N/A        |
| `RunnableEntityGroup`                        | [ ] Pending* | N/A        |
| `DataPrototypeGroup`                         | [ ] Pending* | N/A        |
| `SwTextProps`                                | [ ] Pending* | N/A        |
| `ApplicationArrayDataType`                   | [ ] Pending* | N/A        |
| `ApplicationArrayElement`                    | [ ] Pending* | N/A        |
| `ArraySizeSemanticsEnum`                     | [ ] Pending* | N/A        |
| `ArraySizeHandlingEnum`                      | [ ] Pending* | N/A        |
| `ImplementationDataType`                     | [ ] Pending* | N/A        |
| `SwBaseType`                                 | [ ] Pending* | N/A        |
| `BaseTypeDefinition`                         | [ ] Pending* | N/A        |
| `BaseTypeDirectDefinition`                   | [ ] Pending* | N/A        |
| `BaseType`                                   | [ ] Pending* | N/A        |
| `ByteOrderEnum`                              | [ ] Pending* | N/A        |
| `AutosarDataPrototype`                       | [ ] Pending* | N/A        |
| `ParameterInAtomicSWCTypeInstanceRef`        | [ ] Pending* | N/A        |
| `ArParameterInImplementationDataInstanceRef` | [ ] Pending* | N/A        |
| `SwDataDefProps`                             | [ ] Pending* | N/A        |
| `SwBitRepresentation`                        | [ ] Pending* | N/A        |
| `SwCalibrationAccessEnum`                    | [ ] Pending* | N/A        |
| `SwCalprmAxis`                               | [ ] Pending* | N/A        |
| `CalprmAxisCategoryEnum`                     | [ ] Pending* | N/A        |
| `SwCalprmAxisTypeProps`                      | [ ] Pending* | N/A        |
| `SwAxisGeneric`                              | [ ] Pending* | N/A        |
| `SwAxisType`                                 | [ ] Pending* | N/A        |
| `SwGenericAxisParam`                         | [ ] Pending* | 13be19a5bd |
| `SwCalprmRefProxy`                           | [ ] Pending* | 3e551e7678 |
| `SwVariableRefProxy`                         | [ ] Pending* | 7664cf6255 |
| `SwDataDependency`                           | [ ] Pending* | 31a72c8fa3 |
| `SwDataDependencyArgs`                       | [ ] Pending* | 31a3396687 |
| `PhysicalDimension`                          | [ ] Pending* | 995b22a850 |
| `PhysicalDimensionMapping`                   | [ ] Pending* | e8c89613ff |
| `PhysicalDimensionMappingSet`                | [ ] Pending* | 262eb0db3d |
| `Unit`                                       | [ ] Pending* | f801a63d13 |
| `PhysConstrs`                                | [ ] Pending* | cad9e2a340 |
| `InternalConstrs`                            | [ ] Pending* | 1469822986 |
| `Limit`                                      | [ ] Pending* | 953b4ee68c |
| `MonotonyEnum`                               | [ ] Pending* | 2386d18780 |
| `IntervalTypeEnum`                           | [ ] Pending* | 016c698ca5 |
| `DisplayPresentationEnum`                    | [ ] Pending* | c6c6c85d80 |
| `ValueSpecification`                         | [ ] Pending* | ac709a6d45 |
| `ReferenceValueSpecification`                | [ ] Pending* | 8186029562 |
| `NotAvailableValueSpecification`             | [ ] Pending* | 83ab0d13f3 |
| `ConstantSpecificationMapping`               | [ ] Pending* | 3c11d90872 |
| `ApplicationValueSpecification`              | [ ] Pending* | a53eb77d97 |
| `NumericalOrText`                            | [ ] Pending* | 0388290c04 |
| `SwAxisCont`                                 | [ ] Pending* | ea8b13a1bf |
| `SwValues`                                   | [ ] Pending* | 42073daa2a |
| `ValueGroup`                                 | [ ] Pending* | c247077e81 |
| `ValueList`                                  | [ ] Pending* | bc05b153d3 |
| `AbstractRuleBasedValueSpecification`        | [ ] Pending* | a9f7a78876 |
| `ApplicationRuleBasedValueSpecification`     | [ ] Pending* | 1e72f8e31d |
| `RuleBasedAxisCont`                          | [ ] Pending* | ebe56c922e |
| `RuleBasedValueCont`                         | [ ] Pending* | 1c8cba3d46 |
| `NumericalRuleBasedValueSpecification`       | [ ] Pending* | 0448eee2d6 |
| `RuleBasedValueSpecification`                | [ ] Pending* | 01d5ffb425 |
| `RuleArguments`                              | [ ] Pending* | 571398195f |
| `CalibrationParameterValueSet`               | [ ] Pending* | 92d3b31318 |
| `CalibrationParameterValue`                  | [ ] Pending* | 253d938ab0 |
| `RunnableEntity`                             | [ ] Pending* | ba3d6ff8b5 |
| `TimingEvent`                                | [ ] Pending* | da8bfb1cf1 |
| `ExecutableEntityActivationReason`           | [ ] Pending* | 12b2493a29 |
| `AbstractEvent`                              | [ ] Pending* | 7d8fb2e207 |
| `SwcModeSwitchEvent`                         | [ ] Pending* | 8ea809a12f |
| `ModeSwitchedAckEvent`                       | [ ] Pending* | d3d54a566d |
| `ExternalTriggerOccurredEvent`               | [ ] Pending* | 84453723ad |
| `TransformerHardErrorEvent`                  | [ ] Pending* | 8f21cc9672 |
| `OsTaskExecutionEvent`                       | [ ] Pending* | 5958e809f2 |
| `WaitPoint`                                  | [ ] Pending* | ce4966a549 |

## Group29

Status: **20/74** completed

| Class Name                                     | Status       | Commit ID  |
| ---------------------------------------------- | ------------ | ---------- |
| `SwcExclusiveAreaPolicy`                       | [x] Done     | N/A        |
| `RteApiReturnValueProvisionEnum`               | [x] Done     | N/A        |
| `ExternalTriggeringPoint`                      | [ ] Pending* | 49038a9617 |
| `IncludedDataTypeSet`                          | [ ] Pending* | 7ddafb5f11 |
| `SwcServiceDependency`                         | [ ] Pending* | 38630f7a82 |
| `SymbolicNameProps`                            | [x] Done     | N/A        |
| `VariationPointProxy`                          | [ ] Pending* | 128ce8e538 |
| `SwcModeManagerErrorEvent`                     | [ ] Pending* | 545278ad92 |
| `SensorActuatorSwComponentType`                | [ ] Pending* | 5395714191 |
| `EcuAbstractionSwComponentType`                | [ ] Pending* | 7d89ea80c0 |
| `ComplexDeviceDriverSwComponentType`           | [ ] Pending* | fa1d819e9d |
| `ServiceSwComponentType`                       | [ ] Pending* | f5ecdcb0a4 |
| `NvBlockSwComponentType`                       | [ ] Pending* | d70be3bb2d |
| `SwComponentDocumentation`                     | [ ] Pending* | 35074e8030 |
| `AdditionalBindingTimeEnum`                    | [ ] Pending* | b72807df62 |
| `FunctionInhibitionAvailabilityNeeds`          | [x] Done     | N/A        |
| `DiagnosticOperationCycleNeeds`                | [x] Done     | N/A        |
| `OperationCycleTypeEnum`                       | [x] Done     | N/A        |
| `DiagnosticEnableConditionNeeds`               | [x] Done     | N/A        |
| `EventAcceptanceStatusEnum`                    | [x] Done     | N/A        |
| `DiagnosticStorageConditionNeeds`              | [x] Done     | N/A        |
| `StorageConditionStatusEnum`                   | [x] Done     | N/A        |
| `IndicatorStatusNeeds`                         | [x] Done     | N/A        |
| `DiagnosticIndicatorTypeEnum`                  | [x] Done     | N/A        |
| `ObdRatioServiceNeeds`                         | [ ] Pending* | 86d72d7d2c |
| `ObdControlServiceNeeds`                       | [x] Done     | N/A        |
| `ObdRatioConnectionKindEnum`                   | [x] Done     | N/A        |
| `ObdPidServiceNeeds`                           | [x] Done     | N/A        |
| `ObdInfoServiceNeeds`                          | [x] Done     | N/A        |
| `ObdMonitorServiceNeeds`                       | [x] Done     | N/A        |
| `DiagnosticMonitorUpdateKindEnum`              | [x] Done     | N/A        |
| `ObdRatioDenominatorNeeds`                     | [ ] Pending* | c4b99a4cf3 |
| `DiagnosticDenominatorConditionEnum`           | [x] Done     | N/A        |
| `DiagnosticTestResult`                         | [ ] Pending* | 30d1bea627 |
| `DoIpRoutingActivationAuthenticationNeeds`     | [ ] Pending* | ee01eb9e60 |
| `DoIpRoutingActivationConfirmationNeeds`       | [ ] Pending* | ca6b7d152b |
| `SecureOnBoardCommunicationNeeds`              | [ ] Pending* | 294106f57d |
| `VerificationStatusIndicationModeEnum`         | [x] Done     | N/A        |
| `IdsMgrNeeds`                                  | [ ] Pending* | 4c1801ebf6 |
| `RapidPrototypingScenario`                     | [ ] Pending* | dcf4255cac |
| `RptContainer`                                 | [ ] Pending* | 8c7d753249 |
| `RptHook`                                      | [ ] Pending* | 81bd63ac93 |
| `RptProfile`                                   | [ ] Pending* | 917a9b7dfa |
| `CommunicationConnector`                       | [ ] Pending* | 7b29ffc2ba |
| `PhysicalChannel`                              | [ ] Pending* | 13ae27c195 |
| `AbstractCanCluster`                           | [ ] Pending* | b9599507f4 |
| `CanCluster`                                   | [ ] Pending* | ec69750f14 |
| `CanCommunicationController`                   | [ ] Pending* | 250fded7cd |
| `AbstractCanCommunicationController`           | [ ] Pending* | b115cca55e |
| `AbstractCanCommunicationControllerAttributes` | [ ] Pending* | a7b009e6e7 |
| `CanControllerFdConfiguration`                 | [ ] Pending* | 3cd3adcdc4 |
| `CanControllerXlConfiguration`                 | [ ] Pending* | 55877d3a96 |
| `CanControllerXlConfigurationRequirements`     | [ ] Pending* | 4e35a9d3b4 |
| `AbstractCanPhysicalChannel`                   | [ ] Pending* | d5b7c507aa |
| `CanPhysicalChannel`                           | [ ] Pending* | 10e6b6aab3 |
| `AbstractCanCommunicationConnector`            | [ ] Pending* | b6aaf97f5d |
| `TtcanCluster`                                 | [ ] Pending* | 4c24b5ae37 |
| `TtcanCommunicationController`                 | [ ] Pending* | 20da1fc7f6 |
| `TtcanPhysicalChannel`                         | [ ] Pending* | d6edfeef67 |
| `TtcanCommunicationConnector`                  | [ ] Pending* | 20db1869a0 |
| `FlexrayCluster`                               | [ ] Pending* | 00edf04e32 |
| `FlexrayFifoConfiguration`                     | [ ] Pending* | d4975bcfb7 |
| `FlexrayFifoRange`                             | [ ] Pending* | a2965515fb |
| `LinCluster`                                   | [ ] Pending* | d8a563e1f0 |
| `LinCommunicationController`                   | [ ] Pending* | f19185283e |
| `LinMaster`                                    | [ ] Pending* | 35db48e9b0 |
| `LinSlaveConfig`                               | [ ] Pending* | 81ac1ac2a0 |
| `LinSlaveConfigIdent`                          | [ ] Pending* | 5e4ae9f277 |
| `LinSlave`                                     | [ ] Pending* | c8f1e00c47 |
| `LinErrorResponse`                             | [ ] Pending* | 6439b6cbd5 |
| `LinConfigurableFrame`                         | [ ] Pending* | eb075693c2 |
| `LinOrderedConfigurableFrame`                  | [ ] Pending* | 15a63a22ae |
| `LinPhysicalChannel`                           | [ ] Pending* | a60d5418a2 |
| `EthernetCluster`                              | [ ] Pending* | 4b9d113878 |

## Group30

Status: **0/75** completed

| Class Name                                       | Status          | Commit ID  |
| ------------------------------------------------ | --------------- | ---------- |
| `CouplingElement`                                | [ ] Pending*    | dccd25955a |
| `CouplingElementEnum`                            | [ ] Pending*    | cc75a503b1 |
| `CouplingPort`                                   | [ ] Pending*    | 51836c9a37 |
| `EthernetConnectionNegotiationEnum`              | [ ] Pending*    | bc3d3386a2 |
| `EthernetMacLayerTypeEnum`                       | [ ] Pending*    | d526c8ebcf |
| `EthernetPhysicalLayerTypeEnum`                  | [ ] Pending*    | 5eba7c6ad9 |
| `EthernetSwitchVlanIngressTagEnum`               | [ ] Pending*    | 0d682b9798 |
| `CouplingPortConnection`                         | [ ] Pending*    | 7543596588 |
| `EthernetCommunicationController`                | [ ] Pending*    | 01e4db429e |
| `EthernetCommunicationConnector`                 | [ ] Pending*    | d22193a7d7 |
| `CouplingPortDetails`                            | [ ] Pending*    | 7a56601b37 |
| `EthernetCouplingPortSchedulerEnum`              | [ ] Pending*    | 909eb0ddcc |
| `CouplingPortShaper`                             | [ ] Pending*    | 5d3549490d |
| `CouplingPortFifo`                               | [ ] Pending*    | 365e7aec38 |
| `CouplingPortRatePolicy`                         | [ ] Pending*    | 9fafd3ebc2 |
| `CouplingPortRatePolicyActionEnum`               | [ ] Pending*    | 3f2c27ef2d |
| `CouplingPortTrafficClassAssignment`             | [ ] Pending*    | aacc9860e9 |
| `EthernetSwitchVlanEgressTaggingEnum`            | [ ] Pending*    | 41795ad4b3 |
| `DhcpServerConfiguration`                        | [ ] Pending*    | 64d337c40c |
| `Ipv4DhcpServerConfiguration`                    | [ ] Pending*    | 920dc732db |
| `Ipv6DhcpServerConfiguration`                    | [ ] Pending*    | 49ad95dd43 |
| `CouplingElementAbstractDetails`                 | [ ] Pending*    | 9c78940aa9 |
| `CouplingElementSwitchDetails`                   | [ ] Pending*    | d20dc66668 |
| `SwitchStreamIdentification`                     | [ ] Pending*    | aa06ec8a24 |
| `SwitchStreamFilterRule`                         | [ ] Pending*    | 4f467314cf |
| `StreamFilterRuleDataLinkLayer`                  | [ ] Pending*    | 65ab0bd89a |
| `StreamFilterMACAddress`                         | [ ] Pending*    | c74b8e553a |
| `StreamFilterRuleIpTp`                           | [ ] Pending*    | 8989307d08 |
| `StreamFilterIpv4Address`                        | [ ] Pending*    | da459aa3b7 |
| `StreamFilterIpv6Address`                        | [ ] Pending*    | ac34699c4a |
| `StreamFilterPortRange`                          | [ ] Pending*    | c97f9dd4ee |
| `StreamFilterIEEE1722Tp`                         | [ ] Pending*    | cc74587e4b |
| `SwitchStreamFilterActionDestPortModification`   | [ ] Pending*    | cbe98badf5 |
| `SwitchStreamFilterActionPortModificationEnum`   | [ ] Pending*    | 8ca63a75f0 |
| `SwitchStreamFilterEntry`                        | [ ] Pending*    | 8bc4f911fe |
| `SwitchAsynchronousTrafficShaperGroupEntry`      | [ ] Pending*    | dc9e5d6ce4 |
| `SwitchStreamGateEntry`                          | [ ] Pending*    | ac22e340e2 |
| `SwitchFlowMeteringEntry`                        | [ ] Pending*    | 29385d65d2 |
| `FlowMeteringColorModeEnum`                      | [ ] Pending*    | c140322c44 |
| `EthIpProps`                                     | [ ] Pending*    | 324da359ae |
| `Ipv4Props`                                      | [ ] Pending*    | 614927b0c4 |
| `Ipv4ArpProps`                                   | [ ] Pending*    | fbb86c3fcf |
| `Ipv4AutoIpProps`                                | [ ] Pending*    | 926b146bca |
| `Ipv4FragmentationProps`                         | [ ] Pending*    | e16eb379e5 |
| `Ipv6Props`                                      | [ ] Pending*    | 05891c9038 |
| `Ipv6FragmentationProps`                         | [ ] Pending*    | 772f5b9b2b |
| `Dhcpv6Props`                                    | [ ] Pending*    | 58cbdb9815 |
| `Ipv6NdpProps`                                   | [ ] Pending*    | f3c622bd64 |
| `EthernetWakeupSleepOnDatalineConfig`            | [ ] Pending*    | e795dd3dc6 |
| `EthernetWakeupSleepOnDatalineConfigSet`         | [ ] Pending*    | 2065193be7 |
| `PlcaProps`                                      | [ ] Pending*    | 227f0810e3 |
| `MacSecProps`                                    | [ ] Pending*    | N/A        |
| `MacSecLocalKayProps`                            | [ ] Implemented | 506d255bd5 |
| `MacSecGlobalKayProps`                           | [ ] Pending*    | edc1d0ae3c |
| `MacSecParticipantSet`                           | [ ] Pending*    | 66ee2a8948 |
| `MacSecKayParticipant`                           | [ ] Pending*    | 006a38a1cd |
| `MacSecCryptoAlgoConfig`                         | [ ] Pending*    | 6ce66d34dc |
| `MacSecCipherSuiteConfig`                        | [ ] Pending*    | 21ec4784ed |
| `MacSecConfidentialityOffsetEnum`                | [ ] Pending*    | e609bd9264 |
| `MacSecCapabilityEnum`                           | [ ] Pending*    | bc28f5ecb0 |
| `MacSecRoleEnum`                                 | [ ] Pending*    | 38c1935eff |
| `MacSecFailPermissiveModeEnum`                   | [ ] Pending*    | e4ec644192 |
| `UserDefinedCluster`                             | [ ] Pending*    | 60a130c7b2 |
| `UserDefinedPhysicalChannel`                     | [ ] Pending*    | 0d446c837a |
| `UserDefinedCommunicationConnector`              | [ ] Pending*    | ff537256be |
| `UserDefinedCommunicationController`             | [ ] Pending*    | acba63082a |
| `SystemMapping`                                  | [ ] Pending*    | 1fa8787ea5 |
| `SwcToApplicationPartitionMapping`               | [ ] Pending*    | 8323feb0a2 |
| `ApplicationPartition`                           | [ ] Pending*    | 9241a3d9f5 |
| `MappingConstraint`                              | [ ] Pending*    | a678eca673 |
| `ComponentClustering`                            | [ ] Pending*    | 6ddfdbb3f5 |
| `MappingScopeEnum`                               | [ ] Pending*    | b42864d264 |
| `ComponentSeparation`                            | [ ] Pending*    | 525ff2c22c |
| `J1939ControllerApplicationToJ1939NmNodeMapping` | [ ] Pending*    | 7ffd517014 |
| `J1939ControllerApplication`                     | [ ] Pending*    | bf314fe2fe |

## Group31

Status: **0/75** completed

| Class Name                                               | Status          | Commit ID  |
| -------------------------------------------------------- | --------------- | ---------- |
| `RteEventInCompositionToOsTaskProxyMapping`              | [ ] Pending*    | N/A        |
| `RteEventInCompositionSeparation`                        | [ ] Pending*    | N/A        |
| `RteEventInSystemToOsTaskProxyMapping`                   | [ ] Pending*    | N/A        |
| `RteEventInSystemSeparation`                             | [ ] Pending*    | N/A        |
| `SenderRecArrayElementMapping`                           | [ ] Pending*    | N/A        |
| `ClientServerToSignalMapping`                            | [ ] Pending*    | N/A        |
| `SenderReceiverCompositeElementToSignalMapping`          | [ ] Pending*    | N/A        |
| `TriggerToSignalMapping`                                 | [ ] Pending*    | N/A        |
| `CommonSignalPath`                                       | [ ] Pending*    | N/A        |
| `SwcToSwcSignal`                                         | [ ] Pending*    | N/A        |
| `SwcToSwcOperationArguments`                             | [ ] Pending*    | N/A        |
| `SwcToSwcOperationArgumentsDirectionEnum`                | [ ] Pending*    | N/A        |
| `ForbiddenSignalPath`                                    | [ ] Pending*    | N/A        |
| `PermissibleSignalPath`                                  | [ ] Pending*    | N/A        |
| `SeparateSignalPath`                                     | [ ] Pending*    | N/A        |
| `EcuResourceEstimation`                                  | [ ] Pending*    | N/A        |
| `PncMapping`                                             | [ ] Pending*    | N/A        |
| `CpSoftwareClusterToEcuInstanceMapping`                  | [ ] Pending*    | N/A        |
| `CpSoftwareClusterResourceToApplicationPartitionMapping` | [ ] Pending*    | N/A        |
| `CpSoftwareClusterMappingSet`                            | [ ] Pending*    | N/A        |
| `CpSoftwareClusterToApplicationPartitionMapping`         | [ ] Pending*    | N/A        |
| `SystemSignalToCommunicationResourceMapping`             | [ ] Pending*    | N/A        |
| `SystemSignalGroupToCommunicationResourceMapping`        | [ ] Pending*    | N/A        |
| `DdsCpISignalToDdsTopicMapping`                          | [ ] Pending*    | N/A        |
| `CommConnectorPort`                                      | [ ] Pending*    | ca22bc0a86 |
| `IPduPort`                                               | [ ] Pending*    | 5809b8408f |
| `IPduSignalProcessingEnum`                               | [ ] Pending*    | e34ab3e1ad |
| `ISignal`                                                | [ ] Implemented | N/A        |
| `DataTypePolicyEnum`                                     | [ ] Implemented | N/A        |
| `ISignalTypeEnum`                                        | [ ] Implemented | N/A        |
| `ISignalProps`                                           | [ ] Implemented | N/A        |
| `ISignalGroup`                                           | [ ] Implemented | N/A        |
| `SystemSignalGroup`                                      | [ ] Implemented | N/A        |
| `ISignalToIPduMapping`                                   | [ ] Implemented | N/A        |
| `ISignalTriggering`                                      | [ ] Implemented | N/A        |
| `Pdu`                                                    | [ ] Implemented | N/A        |
| `IPdu`                                                   | [ ] Implemented | N/A        |
| `ISignalIPdu`                                            | [ ] Implemented | N/A        |
| `NmPdu`                                                  | [ ] Implemented | N/A        |
| `NPdu`                                                   | [ ] Implemented | N/A        |
| `DcmIPdu`                                                | [ ] Implemented | N/A        |
| `DiagPduType`                                            | [ ] Created     | N/A        |
| `J1939DcmIPdu`                                           | [ ] Created     | N/A        |
| `PduToFrameMapping`                                      | [ ] Implemented | N/A        |
| `IPduTiming`                                             | [ ] Implemented | N/A        |
| `PduTriggering`                                          | [ ] Implemented | N/A        |
| `ContainerIPdu`                                          | [ ] Pending*    | N/A        |
| `ContainerIPduTriggerEnum`                               | [ ] Pending*    | N/A        |
| `ContainerIPduHeaderTypeEnum`                            | [ ] Pending*    | N/A        |
| `RxAcceptContainedIPduEnum`                              | [ ] Pending*    | N/A        |
| `SecureCommunicationProps`                               | [ ] Implemented | N/A        |
| `SecureCommunicationPropsSet`                            | [ ] Implemented | N/A        |
| `SecureCommunicationFreshnessProps`                      | [ ] Implemented | N/A        |
| `SecureCommunicationAuthenticationProps`                 | [ ] Implemented | N/A        |
| `CryptoServiceKey`                                       | [ ] Created     | N/A        |
| `CryptoServiceKeyGenerationEnum`                         | [ ] Created     | N/A        |
| `CryptoServiceQueue`                                     | [ ] Created     | N/A        |
| `GeneralPurposeConnection`                               | [ ] Created     | N/A        |
| `RelativeTolerance`                                      | [ ] Implemented | N/A        |
| `AbsoluteTolerance`                                      | [ ] Implemented | N/A        |
| `Frame`                                                  | [ ] Implemented | N/A        |
| `LinFrame`                                               | [ ] Implemented | N/A        |
| `LinFrameTriggering`                                     | [ ] Implemented | N/A        |
| `LinChecksumType`                                        | [ ] Created     | N/A        |
| `LinUnconditionalFrame`                                  | [ ] Implemented | N/A        |
| `LinSporadicFrame`                                       | [ ] Created     | N/A        |
| `LinEventTriggeredFrame`                                 | [ ] Created     | N/A        |
| `ScheduleTableEntry`                                     | [ ] Implemented | N/A        |
| `FreeFormatEntry`                                        | [ ] Implemented | N/A        |
| `LinConfigurationEntry`                                  | [ ] Implemented | N/A        |
| `AssignFrameId`                                          | [ ] Implemented | N/A        |
| `UnassignFrameId`                                        | [ ] Implemented | N/A        |
| `AssignFrameIdRange`                                     | [ ] Implemented | N/A        |
| `FramePid`                                               | [ ] Implemented | N/A        |
| `AssignNad`                                              | [ ] Implemented | N/A        |

## Group32

Status: **0/74** completed

| Class Name                             | Status       | Commit ID  |
| -------------------------------------- | ------------ | ---------- |
| `ConditionalChangeNad`                 | [ ] Pending* | N/A        |
| `SaveConfigurationEntry`               | [ ] Pending* | N/A        |
| `DataDumpEntry`                        | [ ] Pending* | N/A        |
| `FreeFormat`                           | [ ] Pending* | N/A        |
| `CanFrame`                             | [ ] Pending* | N/A        |
| `CanFrameTriggering`                   | [ ] Pending* | N/A        |
| `CanAddressingModeType`                | [ ] Pending* | N/A        |
| `RxIdentifierRange`                    | [ ] Pending* | N/A        |
| `CanFrameRxBehaviorEnum`               | [ ] Pending* | N/A        |
| `CanFrameTxBehaviorEnum`               | [ ] Pending* | N/A        |
| `TtcanAbsolutelyScheduledTiming`       | [ ] Pending* | N/A        |
| `TtcanTriggerType`                     | [ ] Pending* | N/A        |
| `SoAdConfig`                           | [ ] Pending* | N/A        |
| `SocketAddress`                        | [ ] Pending* | N/A        |
| `UdpChecksumCalculationEnum`           | [ ] Pending* | N/A        |
| `IPv6ExtHeaderFilterSet`               | [ ] Pending* | N/A        |
| `ApplicationEndpoint`                  | [ ] Pending* | N/A        |
| `RtpTp`                                | [ ] Pending* | N/A        |
| `Ieee1722Tp`                           | [ ] Pending* | N/A        |
| `HttpTp`                               | [ ] Pending* | N/A        |
| `Ipv6Configuration`                    | [ ] Pending* | N/A        |
| `MacMulticastConfiguration`            | [ ] Pending* | N/A        |
| `InfrastructureServices`               | [ ] Pending* | N/A        |
| `TimeSyncTechnologyEnum`               | [ ] Pending* | N/A        |
| `DoIpEntityRoleEnum`                   | [ ] Pending* | N/A        |
| `DdsCpServiceInstance`                 | [ ] Pending* | N/A        |
| `DdsCpProvidedServiceInstance`         | [ ] Pending* | N/A        |
| `DdsCpConsumedServiceInstance`         | [ ] Pending* | N/A        |
| `DdsCpServiceInstanceEvent`            | [ ] Pending* | N/A        |
| `DdsCpServiceInstanceOperation`        | [ ] Pending* | N/A        |
| `ServiceInstanceCollectionSet`         | [ ] Pending* | N/A        |
| `AbstractServiceInstance`              | [ ] Pending* | N/A        |
| `ProvidedServiceInstance`              | [ ] Pending* | N/A        |
| `PduActivationRoutingGroup`            | [ ] Pending* | 5cb5ddacc2 |
| `EventGroupControlTypeEnum`            | [ ] Pending* | N/A        |
| `SoConIPduIdentifier`                  | [ ] Pending* | N/A        |
| `SocketConnectionIpduIdentifierSet`    | [ ] Pending* | N/A        |
| `EventHandler`                         | [ ] Pending* | N/A        |
| `ConsumedServiceInstance`              | [ ] Pending* | N/A        |
| `ConsumedEventGroup`                   | [ ] Pending* | N/A        |
| `SomeipSdServerServiceInstanceConfig`  | [ ] Pending* | N/A        |
| `SomeipSdServerEventGroupTimingConfig` | [ ] Pending* | N/A        |
| `SomeipSdClientEventGroupTimingConfig` | [ ] Pending* | N/A        |
| `DdsCpConfig`                          | [ ] Pending* | N/A        |
| `DdsCpTopic`                           | [ ] Pending* | N/A        |
| `DdsCpPartition`                       | [ ] Pending* | N/A        |
| `DdsCpQosProfile`                      | [ ] Pending* | N/A        |
| `DdsTopicData`                         | [ ] Pending* | N/A        |
| `DdsDurability`                        | [ ] Pending* | N/A        |
| `DdsDurabilityKindEnum`                | [ ] Pending* | N/A        |
| `DdsDurabilityService`                 | [ ] Pending* | N/A        |
| `DdsDurabilityServiceHistoryKindEnum`  | [ ] Pending* | N/A        |
| `DdsDeadline`                          | [ ] Pending* | N/A        |
| `DdsLatencyBudget`                     | [ ] Pending* | N/A        |
| `DdsOwnership`                         | [ ] Pending* | N/A        |
| `DdsOwnershipKindEnum`                 | [ ] Pending* | N/A        |
| `DdsOwnershipStrength`                 | [ ] Pending* | N/A        |
| `DdsLiveliness`                        | [ ] Pending* | N/A        |
| `DdsLivenessKindEnum`                  | [ ] Pending* | N/A        |
| `DdsReliability`                       | [ ] Pending* | N/A        |
| `DdsReliabilityKindEnum`               | [ ] Pending* | N/A        |
| `DdsTransportPriority`                 | [ ] Pending* | N/A        |
| `DdsLifespan`                          | [ ] Pending* | N/A        |
| `DdsDestinationOrder`                  | [ ] Pending* | N/A        |
| `DdsDestinationOrderKindEnum`          | [ ] Pending* | N/A        |
| `DdsHistory`                           | [ ] Pending* | N/A        |
| `DdsHistoryKindEnum`                   | [ ] Pending* | N/A        |
| `DdsResourceLimits`                    | [ ] Pending* | N/A        |
| `StaticSocketConnection`               | [ ] Pending* | N/A        |
| `IPSecRule`                            | [ ] Pending* | N/A        |
| `IPSecConfigProps`                     | [ ] Pending* | N/A        |
| `IPsecIpProtocolEnum`                  | [ ] Pending* | N/A        |
| `IPsecPolicyEnum`                      | [ ] Pending* | N/A        |
| `IPsecModeEnum`                        | [ ] Pending* | N/A        |

## Group33

Status: **0/75** completed

| Class Name                                  | Status       | Commit ID |
| ------------------------------------------- | ------------ | --------- |
| `IPsecHeaderTypeEnum`                       | [ ] Pending* | N/A       |
| `IPsecDpdActionEnum`                        | [ ] Pending* | N/A       |
| `EthernetFrameTriggering`                   | [ ] Pending* | N/A       |
| `UserDefinedEthernetFrame`                  | [ ] Pending* | N/A       |
| `Ieee1722TpEthernetFrame`                   | [ ] Pending* | N/A       |
| `StateDependentFirewall`                    | [ ] Pending* | N/A       |
| `TpConfig`                                  | [ ] Pending* | N/A       |
| `FlexrayTpConfig`                           | [ ] Pending* | N/A       |
| `FlexrayTpConnectionControl`                | [ ] Pending* | N/A       |
| `FlexrayTpConnection`                       | [ ] Pending* | N/A       |
| `FlexrayTpPduPool`                          | [ ] Pending* | N/A       |
| `FlexrayTpNode`                             | [ ] Pending* | N/A       |
| `FlexrayTpEcu`                              | [ ] Pending* | N/A       |
| `FlexrayArTpConfig`                         | [ ] Pending* | N/A       |
| `FlexrayArTpChannel`                        | [ ] Pending* | N/A       |
| `FlexrayArTpNode`                           | [ ] Pending* | N/A       |
| `FlexrayArTpConnection`                     | [ ] Pending* | N/A       |
| `FrArTpAckType`                             | [ ] Pending* | N/A       |
| `MaximumMessageLengthType`                  | [ ] Pending* | N/A       |
| `CanTpConfig`                               | [ ] Pending* | N/A       |
| `CanTpChannel`                              | [ ] Pending* | N/A       |
| `CanTpConnection`                           | [ ] Pending* | N/A       |
| `CanTpAddressingFormatType`                 | [ ] Pending* | N/A       |
| `CanTpAddress`                              | [ ] Pending* | N/A       |
| `CanTpEcu`                                  | [ ] Pending* | N/A       |
| `CanTpNode`                                 | [ ] Pending* | N/A       |
| `NetworkTargetAddressType`                  | [ ] Pending* | N/A       |
| `LinTpConfig`                               | [ ] Pending* | N/A       |
| `LinTpNode`                                 | [ ] Pending* | N/A       |
| `EthTpConfig`                               | [ ] Pending* | N/A       |
| `EthTpConnection`                           | [ ] Pending* | N/A       |
| `SomeipTpConfig`                            | [ ] Pending* | N/A       |
| `SomeipTpConnection`                        | [ ] Pending* | N/A       |
| `SomeipTpChannel`                           | [ ] Pending* | N/A       |
| `J1939TpConfig`                             | [ ] Pending* | N/A       |
| `J1939TpConnection`                         | [ ] Pending* | N/A       |
| `J1939TpPg`                                 | [ ] Pending* | N/A       |
| `J1939TpNode`                               | [ ] Pending* | N/A       |
| `TpConnection`                              | [ ] Pending* | N/A       |
| `IEEE1722TpConfig`                          | [ ] Pending* | N/A       |
| `IEEE1722TpConnection`                      | [ ] Pending* | N/A       |
| `IEEE1722TpAvConnection`                    | [ ] Pending* | N/A       |
| `IEEE1722TpCrfConnection`                   | [ ] Pending* | N/A       |
| `IEEE1722TpCrfTypeEnum`                     | [ ] Pending* | N/A       |
| `IEEE1722TpCrfPullEnum`                     | [ ] Pending* | N/A       |
| `IEEE1722TpAafConnection`                   | [ ] Pending* | N/A       |
| `IEEE1722TpAafNominalRateEnum`              | [ ] Pending* | N/A       |
| `IEEE1722TpAafFormatEnum`                   | [ ] Pending* | N/A       |
| `IEEE1722TpAafAes3DataTypeEnum`             | [ ] Pending* | N/A       |
| `IEEE1722TpIidcConnection`                  | [ ] Pending* | N/A       |
| `IEEE1722TpRvfConnection`                   | [ ] Pending* | N/A       |
| `IEEE1722TpRvfPixelDepthEnum`               | [ ] Pending* | N/A       |
| `IEEE1722TpRvfPixelFormatEnum`              | [ ] Pending* | N/A       |
| `IEEE1722TpRvfColorSpaceEnum`               | [ ] Pending* | N/A       |
| `IEEE1722TpRvfFrameRateEnum`                | [ ] Pending* | N/A       |
| `IEEE1722TpAcfConnection`                   | [ ] Pending* | N/A       |
| `IEEE1722TpAcfBus`                          | [ ] Pending* | N/A       |
| `IEEE1722TpAcfBusPart`                      | [ ] Pending* | N/A       |
| `IEEE1722TpAcfCan`                          | [ ] Pending* | N/A       |
| `IEEE1722TpAcfCanPart`                      | [ ] Pending* | N/A       |
| `IEEE1722TpAcfCanMessageTypeEnum`           | [ ] Pending* | N/A       |
| `IEEE1722TpAcfLin`                          | [ ] Pending* | N/A       |
| `IEEE1722TpAcfLinPart`                      | [ ] Pending* | N/A       |
| `BusspecificNmEcu`                          | [ ] Pending* | N/A       |
| `NmCoordinator`                             | [ ] Pending* | N/A       |
| `NmNode`                                    | [ ] Pending* | N/A       |
| `NmCoordinatorRoleEnum`                     | [ ] Pending* | N/A       |
| `FlexrayNmScheduleVariant`                  | [ ] Pending* | N/A       |
| `CanNmEcu`                                  | [ ] Pending* | N/A       |
| `J1939NmNode`                               | [ ] Pending* | N/A       |
| `J1939NodeName`                             | [ ] Pending* | N/A       |
| `J1939NmAddressConfigurationCapabilityEnum` | [ ] Pending* | N/A       |
| `BusMirrorChannelMapping`                   | [ ] Pending* | N/A       |
| `MirroringProtocolEnum`                     | [ ] Pending* | N/A       |
| `BusMirrorChannel`                          | [ ] Pending* | N/A       |

## Group34

Status: **0/75** completed

| Class Name                                          | Status       | Commit ID |
| --------------------------------------------------- | ------------ | --------- |
| `BusMirrorChannelMappingCan`                        | [ ] Pending* | N/A       |
| `BusMirrorCanIdRangeMapping`                        | [ ] Pending* | N/A       |
| `BusMirrorCanIdToCanIdMapping`                      | [ ] Pending* | N/A       |
| `BusMirrorLinPidToCanIdMapping`                     | [ ] Pending* | N/A       |
| `BusMirrorChannelMappingFlexray`                    | [ ] Pending* | N/A       |
| `BusMirrorChannelMappingIp`                         | [ ] Pending* | N/A       |
| `BusMirrorChannelMappingUserDefined`                | [ ] Pending* | N/A       |
| `SignalServiceTranslationPropsSet`                  | [ ] Pending* | N/A       |
| `SignalServiceTranslationProps`                     | [ ] Pending* | N/A       |
| `SignalServiceTranslationEventProps`                | [ ] Pending* | N/A       |
| `SignalServiceTranslationControlEnum`               | [ ] Pending* | N/A       |
| `UserDefinedTransformationDescription`              | [ ] Pending* | N/A       |
| `CSTransformerErrorReactionEnum`                    | [ ] Pending* | N/A       |
| `SOMEIPTransformationDescription`                   | [ ] Pending* | N/A       |
| `TransformationPropsSet`                            | [ ] Created  | N/A       |
| `TransformationProps`                               | [ ] Pending* | N/A       |
| `SOMEIPTransformationProps`                         | [ ] Pending* | N/A       |
| `DataPrototypeReference`                            | [ ] Pending* | N/A       |
| `DataPrototypeInPortInterfaceRef`                   | [ ] Pending* | N/A       |
| `DataPrototypeInSenderReceiverInterfaceInstanceRef` | [ ] Pending* | N/A       |
| `DataPrototypeInClientServerInterfaceInstanceRef`   | [ ] Pending* | N/A       |
| `ImplementationDataTypeElementInPortInterfaceRef`   | [ ] Pending* | N/A       |
| `EndToEndTransformationDescription`                 | [ ] Pending* | N/A       |
| `DataIdModeEnum`                                    | [ ] Pending* | N/A       |
| `EndToEndProfileBehaviorEnum`                       | [ ] Pending* | N/A       |
| `UserDefinedTransformationProps`                    | [ ] Pending* | N/A       |
| `GlobalTimeDomain`                                  | [ ] Created  | N/A       |
| `AbstractGlobalTimeDomainProps`                     | [ ] Pending* | N/A       |
| `NetworkSegmentIdentification`                      | [ ] Pending* | N/A       |
| `GlobalTimeMaster`                                  | [ ] Pending* | N/A       |
| `GlobalTimeSlave`                                   | [ ] Pending* | N/A       |
| `GlobalTimeGateway`                                 | [ ] Pending* | N/A       |
| `GlobalTimeCorrectionProps`                         | [ ] Pending* | N/A       |
| `GlobalTimeCanMaster`                               | [ ] Pending* | N/A       |
| `GlobalTimeCanSlave`                                | [ ] Pending* | N/A       |
| `CanGlobalTimeDomainProps`                          | [ ] Pending* | N/A       |
| `GlobalTimeEthMaster`                               | [ ] Pending* | N/A       |
| `EthTSynSubTlvConfig`                               | [ ] Pending* | N/A       |
| `GlobalTimeEthSlave`                                | [ ] Pending* | N/A       |
| `EthGlobalTimeDomainProps`                          | [ ] Pending* | N/A       |
| `EthTSynCrcFlags`                                   | [ ] Pending* | N/A       |
| `EthGlobalTimeMessageFormatEnum`                    | [ ] Pending* | N/A       |
| `EthGlobalTimeManagedCouplingPort`                  | [ ] Pending* | N/A       |
| `GlobalTimeCouplingPortProps`                       | [ ] Pending* | N/A       |
| `GlobalTimePortRoleEnum`                            | [ ] Pending* | N/A       |
| `GlobalTimeFrMaster`                                | [ ] Pending* | N/A       |
| `GlobalTimeFrSlave`                                 | [ ] Pending* | N/A       |
| `FrGlobalTimeDomainProps`                           | [ ] Pending* | N/A       |
| `UserDefinedGlobalTimeMaster`                       | [ ] Pending* | N/A       |
| `UserDefinedGlobalTimeSlave`                        | [ ] Pending* | N/A       |
| `GlobalTimeCrcSupportEnum`                          | [ ] Pending* | N/A       |
| `GlobalTimeCrcValidationEnum`                       | [ ] Pending* | N/A       |
| `GlobalTimeIcvSupportEnum`                          | [ ] Pending* | N/A       |
| `GlobalTimeIcvVerificationEnum`                     | [ ] Pending* | N/A       |
| `CpSoftwareClusterResourcePool`                     | [ ] Created  | N/A       |
| `CpSoftwareClusterCommunicationResource`            | [ ] Pending* | N/A       |
| `CpSoftwareClusterCommunicationResourceProps`       | [ ] Pending* | N/A       |
| `DataComProps`                                      | [ ] Pending* | N/A       |
| `DataConsistencyPolicyEnum`                         | [ ] Pending* | N/A       |
| `ClientServerOperationComProps`                     | [ ] Pending* | N/A       |
| `SendIndicationEnum`                                | [ ] Pending* | N/A       |
| `CpSoftwareClusterServiceResource`                  | [ ] Created  | N/A       |
| `PortElementToCommunicationResourceMapping`         | [ ] Created  | N/A       |
| `CpSoftwareClusterToResourceMapping`                | [ ] Created  | N/A       |
| `CpSoftwareClusterBinaryManifestDescriptor`         | [ ] Created  | N/A       |
| `BinaryManifestProvideResource`                     | [ ] Created  | N/A       |
| `BinaryManifestResource`                            | [ ] Pending* | N/A       |
| `BinaryManifestRequireResource`                     | [ ] Created  | N/A       |
| `BinaryManifestResourceDefinition`                  | [ ] Created  | N/A       |
| `BinaryManifestItem`                                | [ ] Created  | N/A       |
| `BinaryManifestItemDefinition`                      | [ ] Created  | N/A       |
| `BinaryManifestAddressableObject`                   | [ ] Pending* | N/A       |
| `BinaryManifestItemValue`                           | [ ] Pending* | N/A       |
| `BinaryManifestItemNumericalValue`                  | [ ] Pending* | N/A       |
| `BinaryManifestItemPointerValue`                    | [ ] Pending* | N/A       |

## Group35

Status: **0/75** completed

| Class Name                             | Status       | Commit ID |
| -------------------------------------- | ------------ | --------- |
| `BinaryManifestMetaDataField`          | [ ] Pending* | N/A       |
| `VfbTiming`                            | [ ] Pending* | N/A       |
| `SwcTiming`                            | [ ] Pending* | N/A       |
| `SystemTiming`                         | [ ] Pending* | N/A       |
| `BswModuleTiming`                      | [ ] Pending* | N/A       |
| `BswCompositionTiming`                 | [ ] Pending* | N/A       |
| `EcuTiming`                            | [ ] Pending* | N/A       |
| `TimingCondition`                      | [ ] Pending* | N/A       |
| `TimingConditionFormula`               | [ ] Pending* | N/A       |
| `TimingExtensionResource`              | [ ] Pending* | N/A       |
| `TimingModeInstance`                   | [ ] Pending* | N/A       |
| `ModeInBswInstanceRef`                 | [ ] Pending* | N/A       |
| `TDEventVfbReference`                  | [ ] Pending* | N/A       |
| `TDEventVfbPort`                       | [ ] Pending* | N/A       |
| `TDEventVariableDataPrototype`         | [ ] Pending* | N/A       |
| `TDEventVariableDataPrototypeTypeEnum` | [ ] Pending* | N/A       |
| `TDEventOperation`                     | [ ] Pending* | N/A       |
| `TDEventOperationTypeEnum`             | [ ] Pending* | N/A       |
| `TDEventModeDeclaration`               | [ ] Pending* | N/A       |
| `TDEventModeDeclarationTypeEnum`       | [ ] Pending* | N/A       |
| `TDEventTrigger`                       | [ ] Pending* | N/A       |
| `TDEventTriggerTypeEnum`               | [ ] Pending* | N/A       |
| `TDEventSwc`                           | [ ] Pending* | N/A       |
| `TDEventSwcInternalBehavior`           | [ ] Pending* | N/A       |
| `TDEventSwcInternalBehaviorTypeEnum`   | [ ] Pending* | N/A       |
| `TDEventSwcInternalBehaviorReference`  | [ ] Pending* | N/A       |
| `TDEventCom`                           | [ ] Pending* | N/A       |
| `TDEventISignal`                       | [ ] Pending* | N/A       |
| `TDEventISignalTypeEnum`               | [ ] Pending* | N/A       |
| `TDEventIPdu`                          | [ ] Pending* | N/A       |
| `TDEventIPduTypeEnum`                  | [ ] Pending* | N/A       |
| `TDEventFrame`                         | [ ] Pending* | N/A       |
| `TDEventFrameTypeEnum`                 | [ ] Pending* | N/A       |
| `TDEventFrameEthernet`                 | [ ] Pending* | N/A       |
| `TDEventFrameEthernetTypeEnum`         | [ ] Pending* | N/A       |
| `TDHeaderIdRange`                      | [ ] Pending* | N/A       |
| `TDEventCycleStart`                    | [ ] Pending* | N/A       |
| `TDEventFrClusterCycleStart`           | [ ] Pending* | N/A       |
| `TDEventTTCanCycleStart`               | [ ] Pending* | N/A       |
| `TDEventBswInternalBehavior`           | [ ] Pending* | N/A       |
| `TDEventBswInternalBehaviorTypeEnum`   | [ ] Pending* | N/A       |
| `TDEventBswModule`                     | [ ] Pending* | N/A       |
| `TDEventBswModuleTypeEnum`             | [ ] Pending* | N/A       |
| `TDEventBswModeDeclaration`            | [ ] Pending* | N/A       |
| `TDEventBswModeDeclarationTypeEnum`    | [ ] Pending* | N/A       |
| `TDEventComplex`                       | [ ] Pending* | N/A       |
| `TDEventSLLETPort`                     | [ ] Pending* | N/A       |
| `TDEventOccurrenceExpression`          | [ ] Pending* | N/A       |
| `TDEventOccurrenceExpressionFormula`   | [ ] Pending* | N/A       |
| `AutosarVariableInstance`              | [ ] Pending* | N/A       |
| `SynchronizationTypeEnum`              | [ ] Pending* | N/A       |
| `EventOccurrenceKindEnum`              | [ ] Pending* | N/A       |
| `LatencyTimingConstraint`              | [ ] Pending* | N/A       |
| `LatencyConstraintTypeEnum`            | [ ] Pending* | N/A       |
| `EventTriggeringConstraint`            | [ ] Pending* | N/A       |
| `PeriodicEventTriggering`              | [ ] Pending* | N/A       |
| `SporadicEventTriggering`              | [ ] Pending* | N/A       |
| `ConcretePatternEventTriggering`       | [ ] Pending* | N/A       |
| `BurstPatternEventTriggering`          | [ ] Pending* | N/A       |
| `ArbitraryEventTriggering`             | [ ] Pending* | N/A       |
| `ConfidenceInterval`                   | [ ] Pending* | N/A       |
| `AgeConstraint`                        | [ ] Pending* | N/A       |
| `ExecutionOrderConstraint`             | [ ] Pending* | N/A       |
| `ExecutionOrderConstraintTypeEnum`     | [ ] Pending* | N/A       |
| `EOCExecutableEntityRefAbstract`       | [ ] Pending* | N/A       |
| `EOCExecutableEntityRefGroup`          | [ ] Pending* | N/A       |
| `EOCExecutableEntityRef`               | [ ] Pending* | N/A       |
| `EOCEventRef`                          | [ ] Pending* | N/A       |
| `ExecutionTimeConstraint`              | [ ] Pending* | N/A       |
| `ExecutionTimeTypeEnum`                | [ ] Pending* | N/A       |
| `SynchronizationPointConstraint`       | [ ] Pending* | N/A       |
| `LetDataExchangeParadigmEnum`          | [ ] Pending* | N/A       |
| `TDCpSoftwareClusterMappingSet`        | [ ] Pending* | N/A       |
| `TDCpSoftwareClusterMapping`           | [ ] Pending* | N/A       |
| `TDCpSoftwareClusterResourceMapping`   | [ ] Pending* | N/A       |

## Group36

Status: **0/81** completed

| Class Name                                        | Status          | Commit ID  |
| ------------------------------------------------- | --------------- | ---------- |
| `ApplicationInterface`                            | [ ] Pending*    | N/A        |
| `FMFeatureModel`                                  | [ ] Pending*    | N/A        |
| `FMFeature`                                       | [ ] Pending*    | N/A        |
| `FMAttributeDef`                                  | [ ] Pending*    | N/A        |
| `FMFeatureDecomposition`                          | [ ] Pending*    | N/A        |
| `FMFeatureRestriction`                            | [ ] Pending*    | N/A        |
| `FMFeatureRelation`                               | [ ] Pending*    | N/A        |
| `FMFeatureSelection`                              | [ ] Pending*    | N/A        |
| `FMFeatureSelectionState`                         | [ ] Pending*    | N/A        |
| `FMAttributeValue`                                | [ ] Pending*    | N/A        |
| `FMFeatureSelectionSet`                           | [ ] Pending*    | N/A        |
| `FMFeatureMap`                                    | [ ] Pending*    | N/A        |
| `FMFeatureMapElement`                             | [ ] Pending*    | N/A        |
| `FMFeatureMapCondition`                           | [ ] Pending*    | N/A        |
| `FMFeatureMapAssertion`                           | [ ] Pending*    | N/A        |
| `SwSystemconstantValueSet`                        | [ ] Pending*    | N/A        |
| `PostBuildVariantCriterionValueSet`               | [ ] Pending*    | N/A        |
| `LogAndTraceMessageCollectionSet`                 | [ ] Pending*    | N/A        |
| `IdsDesign`                                       | [ ] Pending*    | N/A        |
| `SecurityEventDefinition`                         | [ ] Pending*    | N/A        |
| `SecurityEventFilterChain`                        | [ ] Pending*    | N/A        |
| `AbstractSecurityEventFilter`                     | [ ] Pending*    | N/A        |
| `SecurityEventStateFilter`                        | [ ] Pending*    | N/A        |
| `SecurityEventOneEveryNFilter`                    | [ ] Pending*    | N/A        |
| `SecurityEventAggregationFilter`                  | [ ] Pending*    | N/A        |
| `SecurityEventContextDataSourceEnum`              | [ ] Pending*    | N/A        |
| `SecurityEventThresholdFilter`                    | [ ] Pending*    | N/A        |
| `IdsmRateLimitation`                              | [ ] Pending*    | N/A        |
| `IdsmTrafficLimitation`                           | [ ] Pending*    | N/A        |
| `SecurityEventContextMapping`                     | [ ] Pending*    | N/A        |
| `SecurityEventContextProps`                       | [ ] Pending*    | N/A        |
| `SecurityEventReportingModeEnum`                  | [ ] Pending*    | N/A        |
| `SecurityEventContextMappingBswModule`            | [ ] Pending*    | N/A        |
| `SecurityEventContextMappingFunctionalCluster`    | [ ] Pending*    | N/A        |
| `SecurityEventContextMappingCommConnector`        | [ ] Pending*    | N/A        |
| `SecurityEventContextMappingApplication`          | [ ] Pending*    | N/A        |
| `IdsmInstance`                                    | [ ] Pending*    | N/A        |
| `BlockState`                                      | [ ] Pending*    | N/A        |
| `ClientServerOperationBlueprintMapping`           | [ ] Pending*    | N/A        |
| `DataExchangePoint`                               | [ ] Pending*    | N/A        |
| `Baseline`                                        | [ ] Pending*    | N/A        |
| `DataExchangePointKind`                           | [ ] Pending*    | N/A        |
| `SpecElementReference`                            | [ ] Pending*    | N/A        |
| `SpecElementScope`                                | [ ] Pending*    | N/A        |
| `RestrictionWithSeverity`                         | [ ] Pending*    | N/A        |
| `SeverityEnum`                                    | [ ] Pending*    | N/A        |
| `ValueRestrictionWithSeverity`                    | [ ] Pending*    | N/A        |
| `MultiplicityRestrictionWithSeverity`             | [ ] Pending*    | N/A        |
| `AbstractMultiplicityRestriction`                 | [ ] Pending*    | N/A        |
| `VariationRestrictionWithSeverity`                | [ ] Pending*    | N/A        |
| `DataFormatElementReference`                      | [ ] Pending*    | N/A        |
| `DataFormatElementScope`                          | [ ] Pending*    | N/A        |
| `SpecificationScope`                              | [ ] Pending*    | N/A        |
| `SpecificationDocumentScope`                      | [ ] Pending*    | N/A        |
| `DocumentElementScope`                            | [ ] Pending*    | N/A        |
| `AbstractClassTailoring`                          | [ ] Pending*    | N/A        |
| `AbstractCondition`                               | [ ] Pending*    | N/A        |
| `AggregationCondition`                            | [ ] Pending*    | N/A        |
| `AttributeCondition`                              | [ ] Pending*    | N/A        |
| `ClassTailoring`                                  | [ ] Pending*    | N/A        |
| `ClassContentConditional`                         | [ ] Pending*    | N/A        |
| `ConcreteClassTailoring`                          | [ ] Pending*    | N/A        |
| `InvertCondition`                                 | [ ] Pending*    | N/A        |
| `PrimitiveAttributeCondition`                     | [ ] Pending*    | N/A        |
| `ReferenceCondition`                              | [ ] Pending*    | N/A        |
| `TextualCondition`                                | [ ] Pending*    | N/A        |
| `AttributeTailoring`                              | [ ] Pending*    | N/A        |
| `PrimitiveAttributeTailoring`                     | [ ] Pending*    | N/A        |
| `DefaultValueApplicationStrategyEnum`             | [ ] Pending*    | N/A        |
| `AggregationTailoring`                            | [ ] Pending*    | N/A        |
| `ReferenceTailoring`                              | [ ] Pending*    | N/A        |
| `ConstraintTailoring`                             | [ ] Pending*    | N/A        |
| `SdgTailoring`                                    | [ ] Pending*    | N/A        |
| `IdsCommonElement`                                | [ ] Implemented | ecb37c71eb |
| `IdsMapping`                                      | [ ] Implemented | ecb37c71eb |
| `IdsmProperties`                                  | [ ] Implemented | 023395a0a6 |
| `IdsmSignatureSupportAp`                          | [ ] Implemented | 023395a0a6 |
| `IdsmSignatureSupportCp`                          | [ ] Implemented | 023395a0a6 |
| `SecurityEventContextData`                        | [ ] Implemented | 023395a0a6 |
| `FunctionGroupStateInFunctionGroupSetInstanceRef` | [ ] Implemented | 48a3dcb2fa |
| `DataFormatTailoring`                             | [ ] Implemented | b4ee0768b9 |
