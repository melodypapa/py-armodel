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

Status: **7/29** completed

| Class Name                              | Status       | Commit ID  |
| --------------------------------------- | ------------ | ---------- |
| `RuntimeAddressConfigurationEnum`       | [ ] Pending* | c5bb322323 |
| `IpAddressKeepEnum`                     | [ ] Pending* | c5bb322323 |
| `Ipv6AddressSourceEnum`                 | [ ] Pending* | c5bb322323 |
| `Ipv4AddressSourceEnum`                 | [ ] Pending* | 6c97ddc108 |
| `DoIpEntity`                            | [ ] Pending* | b1e4750b14 |
| `TpPort`                                | [ ] Pending* | b1e4750b14 |
| `InitialSdDelayConfig`                  | [x] Done     | 84dc59b646 |
| `EthernetPriorityRegeneration`          | [ ] Pending* | b1e4750b14 |
| `TimeSyncServerConfiguration`           | [x] Done     | 155cc2f7f9 |
| `CouplingPortAbstractShaper`            | [ ] Pending* | N/A        |
| `CouplingPortAsynchronousTrafficShaper` | [x] Done     | d419973456 |
| `CouplingPortCreditBasedShaper`         | [x] Done     | c5cfd1dc4e |
| `MacMulticastGroup`                     | [ ] Pending* | b1e4750b14 |
| `IPSecConfig`                           | [x] Done     | d75eb10bff |
| `NetworkEndpoint`                       | [x] Done     | 84587c11f6 |
| `VlanConfig`                            | [ ] Pending* | b1e4750b14 |
| `Ipv4Configuration`                     | [ ] Pending* | 6c97ddc108 |
| `GenericTp`                             | [ ] Pending* | N/A        |
| `TcpTp`                                 | [ ] Pending* | N/A        |
| `UdpTp`                                 | [ ] Pending* | N/A        |
| `PduCollectionSemanticsEnum`            | [ ] Pending* | 4b7c8dc79c |
| `SocketConnectionIpduIdentifier`        | [ ] Pending* | 4b7c8dc79c |
| `SocketConnectionBundle`                | [ ] Pending* | 4b7c8dc79c |
| `RequestResponseDelay`                  | [ ] Pending* | d7240be740 |
| `SdServerConfig`                        | [x] Done     | f509df9d94 |
| `TcpOptionFilterList`                   | [ ] Pending* | 2d5b3256b4 |
| `TcpOptionFilterSet`                    | [ ] Pending* | 2d5b3256b4 |
| `IPv6ExtHeaderFilterList`               | [ ] Pending* | 2d5b3256b4 |
| `TimeSynchronization`                   | [ ] Pending* | b1e4750b14 |

## Group17

Status: **0/26** completed

| Class Name                                 | Status       | Commit ID |
| ------------------------------------------ | ------------ | --------- |
| `CanClusterBusOffRecovery`                 | [ ] Pending* | N/A       |
| `CanCommunicationConnector`                | [ ] Pending* | N/A       |
| `CanControllerConfiguration`               | [ ] Pending* | N/A       |
| `CanControllerConfigurationRequirements`   | [ ] Pending* | N/A       |
| `CanControllerFdConfigurationRequirements` | [ ] Pending* | N/A       |
| `ResumePosition`                           | [ ] Pending* | N/A       |
| `ApplicationEntry`                         | [ ] Pending* | N/A       |
| `LinScheduleTable`                         | [ ] Pending* | N/A       |
| `RunMode`                                  | [ ] Pending* | N/A       |
| `LinCommunicationConnector`                | [ ] Pending* | N/A       |
| `FlexrayFrameTriggering`                   | [ ] Pending* | N/A       |
| `FlexrayAbsolutelyScheduledTiming`         | [ ] Pending* | N/A       |
| `FlexrayCommunicationConnector`            | [ ] Pending* | N/A       |
| `FlexrayCommunicationController`           | [ ] Pending* | N/A       |
| `FlexrayPhysicalChannel`                   | [ ] Pending* | N/A       |
| `DataMapping`                              | [ ] Pending* | N/A       |
| `IndexedArrayElement`                      | [ ] Pending* | N/A       |
| `SenderRecRecordElementMapping`            | [ ] Pending* | N/A       |
| `SenderRecRecordTypeMapping`               | [ ] Pending* | N/A       |
| `SenderReceiverToSignalMapping`            | [ ] Pending* | N/A       |
| `SenderReceiverToSignalGroupMapping`       | [ ] Pending* | N/A       |
| `DefaultValueElement`                      | [ ] Pending* | N/A       |
| `FrameMapping`                             | [ ] Pending* | N/A       |
| `ISignalMapping`                           | [ ] Pending* | N/A       |
| `TargetIPduRef`                            | [ ] Pending* | N/A       |
| `Gateway`                                  | [ ] Pending* | N/A       |

## Group18

Status: **0/17** completed

| Class Name                                  | Status       | Commit ID |
| ------------------------------------------- | ------------ | --------- |
| `NmEcu`                                     | [ ] Pending* | N/A       |
| `CanNmCluster`                              | [ ] Pending* | N/A       |
| `UdpNmCluster`                              | [ ] Pending* | N/A       |
| `CanNmNode`                                 | [ ] Pending* | N/A       |
| `UdpNmNode`                                 | [ ] Pending* | N/A       |
| `CanNmClusterCoupling`                      | [ ] Pending* | N/A       |
| `UdpNmClusterCoupling`                      | [ ] Pending* | N/A       |
| `FlexrayNmClusterCoupling`                  | [ ] Pending* | N/A       |
| `SecOcCryptoServiceMapping`                 | [ ] Pending* | N/A       |
| `EndToEndTransformationISignalProps`        | [ ] Pending* | N/A       |
| `TpAddress`                                 | [ ] Pending* | N/A       |
| `LinTpConnection`                           | [ ] Pending* | N/A       |
| `EndToEndProtectionISignalIPdu`             | [ ] Pending* | N/A       |
| `SwcToEcuMapping`                           | [ ] Pending* | N/A       |
| `ApplicationPartitionToEcuPartitionMapping` | [ ] Pending* | N/A       |
| `SwcToImplMapping`                          | [ ] Pending* | N/A       |
| `AppOsTaskProxyToEcuTaskProxyMapping`       | [ ] Pending* | N/A       |

## Group19

Status: **6/16** completed

| Class Name                       | Status          | Commit ID  |
| -------------------------------- | --------------- | ---------- |
| `ConfigReferenceValue`           | [ ] Pending*    | N/A        |
| `EcucValueCollection`            | [ ] Pending*    | N/A        |
| `ModuleConfiguration`            | [ ] Pending*    | N/A        |
| `EcucConfigurationClassEnum`     | [ ] Pending*    | N/A        |
| `EcucScopeEnum`                  | [ ] Pending*    | N/A        |
| `EcucDestinationUriDefRefType`   | [ ] Implemented | N/A        |
| `EcucBooleanParamDef`            | [ ] Pending*    | N/A        |
| `EcucFloatParamDef`              | [ ] Pending*    | N/A        |
| `EcucForeignReferenceDef`        | [ ] Pending*    | N/A        |
| `EcucLinkerSymbolDef`            | [ ] Pending*    | N/A        |
| `EcucReferenceDef`               | [x] Done        | 0d45067479 |
| `EcucSymbolicNameReferenceDef`   | [x] Done        | 0d45067479 |
| `EcucUriReferenceDef`            | [x] Done        | 0d45067479 |
| `EcucConditionFormula`           | [x] Done        | N/A        |
| `EcucParameterDerivationFormula` | [x] Done        | N/A        |
| `EcucQueryExpression`            | [x] Done        | N/A        |

## Group20

Status: **7/29** completed

| Class Name                         | Status       | Commit ID  |
| ---------------------------------- | ------------ | ---------- |
| `DoIpLogicAddress`                 | [ ] Pending* | a5671c229e |
| `DoIpTpConnection`                 | [ ] Pending* | 0abdd0dba4 |
| `CryptoKeySlotTypeEnum`            | [ ] Pending* | 4ea5cb5b45 |
| `CryptoObjectTypeEnum`             | [ ] Pending* | 5b42d57569 |
| `CryptoKeySlotAllowedModification` | [ ] Pending* | c535a86fd6 |
| `CryptoKeySlotContentAllowedUsage` | [ ] Pending* | 6fe403d35e |
| `DataLinkLayerRule`                | [ ] Pending* | 0d343df2a7 |
| `NetworkLayerRule`                 | [ ] Pending* | 529858d9c9 |
| `TransportLayerRule`               | [ ] Pending* | cb197c6b8b |
| `PayloadBytePatternRule`           | [ ] Pending* | 8f863fe9dd |
| `SomeipProtocolRule`               | [ ] Pending* | c18aa8d400 |
| `SomeipSdRule`                     | [ ] Pending* | 17b563a730 |
| `DoIpRule`                         | [ ] Pending* | ebd95cd8f9 |
| `MemorySection`                    | [ ] Pending* | a579a3592e |
| `SectionNamePrefix`                | [ ] Pending* | 0e26482636 |
| `HardwareConfiguration`            | [ ] Pending* | 35bfb17b7a |
| `SoftwareContext`                  | [ ] Pending* | 23884479e9 |
| `SoAdRoutingGroup`                 | [ ] Pending* | 89363ebe2b |
| `StackUsage`                       | [ ] Pending* | 9ce364e249 |
| `MeasuredStackUsage`               | [ ] Pending* | adc2e5eeb7 |
| `RoughEstimateStackUsage`          | [ ] Pending* | 3db474b11a |
| `WorstCaseStackUsage`              | [ ] Pending* | a0cbd41d08 |
| `MacAddressString`                 | [x] Done*    | 1fd0b00607 |
| `PayloadBytePatternRulePart`       | [x] Done*    | 8c72c71709 |
| `TcpRule`                          | [x] Done*    | d3902d0e67 |
| `IcmpRule`                         | [x] Done*    | 5ddaf1cf94 |
| `Ipv4Rule`                         | [x] Done*    | b4096068d6 |
| `Ipv6Rule`                         | [x] Done*    | 18ee06b97c |
| `UdpRule`                          | [x] Done*    | 29cbfb7bbd |

## Group21

Status: **23/55** completed

| Class Name                           | Status       | Commit ID |
| ------------------------------------ | ------------ | --------- |
| `Identifier`                         | [x] Done     | N/A       |
| `LLongName`                          | [x] Done     | N/A       |
| `MixedContentForLongName`            | [x] Done     | N/A       |
| `Referrable`                         | [x] Done     | N/A       |
| `ReferrableSubtypesEnum`             | [ ] Pending* | N/A       |
| `SdgDef`                             | [ ] Pending* | N/A       |
| `SdgElementWithGid`                  | [ ] Pending* | N/A       |
| `SdgClass`                           | [ ] Pending* | N/A       |
| `SdgAttribute`                       | [ ] Pending* | N/A       |
| `SdgAbstractPrimitiveAttribute`      | [ ] Pending* | N/A       |
| `SdgPrimitiveAttribute`              | [ ] Pending* | N/A       |
| `SdgPrimitiveAttributeWithVariation` | [ ] Pending* | N/A       |
| `SdgAggregationWithVariation`        | [ ] Pending* | N/A       |
| `SdgReference`                       | [ ] Pending* | N/A       |
| `SdgAbstractForeignReference`        | [ ] Pending* | N/A       |
| `SdgForeignReference`                | [ ] Pending* | N/A       |
| `SdgForeignReferenceWithVariation`   | [ ] Pending* | N/A       |
| `AbstractValueRestriction`           | [ ] Pending* | N/A       |
| `AbstractVariationRestriction`       | [ ] Pending* | N/A       |
| `FullBindingTimeEnum`                | [ ] Pending* | N/A       |
| `CIdentifier`                        | [ ] Pending* | N/A       |
| `CategoryString`                     | [ ] Pending* | N/A       |
| `DateTime`                           | [ ] Pending* | N/A       |
| `DiagRequirementIdString`            | [ ] Pending* | N/A       |
| `Ip4AddressString`                   | [ ] Pending* | N/A       |
| `Ip6AddressString`                   | [ ] Pending* | N/A       |
| `McdIdentifier`                      | [ ] Pending* | N/A       |
| `RegularExpression`                  | [ ] Pending* | N/A       |
| `RevisionLabelString`                | [ ] Pending* | N/A       |
| `SymbolString`                       | [ ] Pending* | N/A       |
| `UriString`                          | [ ] Pending* | N/A       |
| `VerbatimStringPlain`                | [ ] Pending* | N/A       |
| `CseCodeType`                        | [ ] Pending* | N/A       |
| `EvaluatedVariantSet`                | [ ] Pending* | N/A       |
| `PredefinedVariant`                  | [x] Done     | N/A       |
| `DocumentationBlock`                 | [x] Done     | N/A       |
| `MultiLanguageVerbatim`              | [x] Done     | N/A       |
| `List`                               | [x] Done*    | N/A       |
| `LabeledList`                        | [x] Done     | N/A       |
| `LabeledItem`                        | [x] Done     | N/A       |
| `IndentSample`                       | [x] Done     | N/A       |
| `ItemLabelPosEnum`                   | [x] Done     | N/A       |
| `DefList`                            | [x] Done     | N/A       |
| `DefItem`                            | [x] Done     | N/A       |
| `MlFormula`                          | [x] Done     | N/A       |
| `Note`                               | [x] Done     | N/A       |
| `NoteTypeEnum`                       | [x] Done     | N/A       |
| `Traceable`                          | [x] Done     | N/A       |
| `EmphasisText`                       | [x] Done     | N/A       |
| `IndexEntry`                         | [x] Done     | N/A       |
| `Superscript`                        | [x] Done     | N/A       |
| `Tt`                                 | [x] Done     | N/A       |
| `EEnumFont`                          | [ ] Pending* | N/A       |
| `EEnum`                              | [ ] Pending* | N/A       |
| `DocumentationContext`               | [x] Done     | N/A       |

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
| `DiagnosticRequestEmissionRelatedDTCPermanentStatus`      | [ ] Created  | N/A        |
| `DiagnosticRequestEmissionRelatedDTCPermanentStatusClass` | [ ] Created  | N/A        |
| `DiagnosticEvent`                                         | [ ] Created  | N/A        |
| `DiagnosticClearEventAllowedBehaviorEnum`                 | [ ] Created  | N/A        |
| `DiagnosticConnectedIndicator`                            | [ ] Created  | N/A        |
| `DiagnosticEventClearAllowedEnum`                         | [ ] Created  | N/A        |
| `DiagnosticEventKindEnum`                                 | [ ] Created  | N/A        |
| `DiagnosticConnectedIndicatorBehaviorEnum`                | [ ] Created  | N/A        |
| `DiagnosticTroubleCodeUds`                                | [ ] Created  | N/A        |
| `DiagnosticTroubleCodeObd`                                | [ ] Created  | N/A        |
| `EventObdReadinessGroup`                                  | [ ] Created  | N/A        |
| `DiagnosticTroubleCode`                                   | [ ] Created  | N/A        |
| `DiagnosticTroubleCodeGroup`                              | [ ] Created  | N/A        |
| `DiagnosticMemoryDestination`                             | [ ] Created  | N/A        |
| `DiagnosticMemoryEntryStorageTriggerEnum`                 | [ ] Created  | N/A        |
| `DiagnosticClearDtcLimitationEnum`                        | [ ] Created  | N/A        |
| `DiagnosticEventDisplacementStrategyEnum`                 | [ ] Created  | N/A        |
| `DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum` | [ ] Created  | N/A        |
| `DiagnosticTypeOfFreezeFrameRecordNumerationEnum`         | [ ] Created  | N/A        |
| `DiagnosticMemoryDestinationPrimary`                      | [ ] Created  | N/A        |
| `DiagnosticMemoryDestinationUserDefined`                  | [ ] Created  | N/A        |
| `DiagnosticTroubleCodeProps`                              | [ ] Created  | N/A        |
| `DiagnosticSignificanceEnum`                              | [ ] Created  | N/A        |
| `DiagnosticUdsSeverityEnum`                               | [ ] Created  | N/A        |
| `DiagnosticDataIdentifierSet`                             | [ ] Created  | N/A        |
| `DiagnosticWwhObdDtcClassEnum`                            | [ ] Created  | N/A        |
| `DiagnosticTroubleCodeUdsToTroubleCodeObdMapping`         | [ ] Created  | N/A        |
| `DiagnosticExtendedDataRecord`                            | [ ] Created  | N/A        |
| `DiagnosticRecordTriggerEnum`                             | [ ] Created  | N/A        |
| `DiagnosticFreezeFrame`                                   | [ ] Created  | N/A        |
| `DiagnosticCondition`                                     | [ ] Created  | N/A        |
| `DiagnosticEnableCondition`                               | [ ] Created  | N/A        |
| `DiagnosticStorageCondition`                              | [ ] Created  | N/A        |
| `DiagnosticDebounceAlgorithmProps`                        | [ ] Created  | N/A        |
| `DiagnosticDebounceBehaviorEnum`                          | [ ] Created  | N/A        |
| `DiagnosticConditionGroup`                                | [ ] Created  | N/A        |
| `DiagnosticEnableConditionGroup`                          | [ ] Created  | N/A        |
| `DiagnosticStorageConditionGroup`                         | [ ] Created  | N/A        |
| `DiagnosticOperationCycle`                                | [ ] Created  | N/A        |
| `DiagnosticOperationCycleTypeEnum`                        | [ ] Created  | N/A        |
| `DiagnosticAging`                                         | [ ] Created  | N/A        |
| `DiagnosticIndicator`                                     | [ ] Created  | N/A        |
| `DiagnosticTestResultUpdateEnum`                          | [ ] Created  | N/A        |
| `DiagnosticTestIdentifier`                                | [ ] Created  | N/A        |
| `DiagnosticMeasurementIdentifier`                         | [ ] Created  | N/A        |
| `DiagnosticEcuInstanceProps`                              | [ ] Created  | N/A        |
| `DiagnosticObdSupportEnum`                                | [ ] Created  | N/A        |
| `DiagnosticIumpr`                                         | [ ] Created  | N/A        |
| `DiagnosticIumprKindEnum`                                 | [ ] Created  | N/A        |
| `DiagnosticIumprGroup`                                    | [ ] Created  | N/A        |
| `DiagnosticIumprGroupIdentifier`                          | [ ] Created  | N/A        |
| `DiagnosticIumprDenominatorGroup`                         | [ ] Created  | N/A        |
| `DiagnosticFimAliasEvent`                                 | [ ] Created  | N/A        |
| `DiagnosticAbstractAliasEvent`                            | [ ] Created  | N/A        |
| `DiagnosticFunctionIdentifier`                            | [ ] Created  | N/A        |
| `DiagnosticFunctionIdentifierInhibit`                     | [ ] Created  | N/A        |
| `DiagnosticFunctionInhibitSource`                         | [ ] Created  | N/A        |

## Group26

Status: **1/75** completed

| Class Name                                      | Status          | Commit ID  |
| ----------------------------------------------- | --------------- | ---------- |
| `DiagnosticInhibitionMaskEnum`                  | [ ] Pending*    | N/A        |
| `DiagnosticFimEventGroup`                       | [ ] Pending*    | N/A        |
| `DiagnosticJ1939Spn`                            | [ ] Pending*    | ad6e53e6fe |
| `DiagnosticJ1939FreezeFrame`                    | [ ] Pending*    | 0314338bf5 |
| `DiagnosticJ1939ExpandedFreezeFrame`            | [ ] Pending*    | 0314338bf5 |
| `DiagnosticTroubleCodeJ1939DtcKindEnum`         | [ ] Pending*    | e51e632f04 |
| `DiagnosticTroubleCodeJ1939`                    | [ ] Pending*    | e51e632f04 |
| `DiagnosticMapping`                             | [ ] Pending*    | fd3e548259 |
| `DiagnosticServiceDataMapping`                  | [ ] Pending*    | 80105a7831 |
| `DiagnosticParameterElementAccess`              | [ ] Pending*    | 80105a7831 |
| `DiagnosticServiceMappingDiagTarget`            | [ ] Pending*    | 80105a7831 |
| `DiagnosticSwMapping`                           | [ ] Pending*    | 80105a7831 |
| `DiagnosticServiceSwMapping`                    | [ ] Pending*    | 0f2a3876e3 |
| `BswServiceDependencyIdent`                     | [x] Done        | d488a5e4a8 |
| `DiagnosticAuthTransmitCertificateMapping`      | [ ] Pending*    | 531da6dd58 |
| `DiagnosticSecurityEventReportingModeMapping`   | [ ] Pending*    | 531da6dd58 |
| `DiagnosticEventToTroubleCodeUdsMapping`        | [ ] Pending*    | 664519e02e |
| `DiagnosticEventToOperationCycleMapping`        | [ ] Pending*    | 664519e02e |
| `DiagnosticEventToDebounceAlgorithmMapping`     | [ ] Pending*    | 664519e02e |
| `DiagnosticEventToEnableConditionGroupMapping`  | [ ] Pending*    | 664519e02e |
| `DiagnosticEventToStorageConditionGroupMapping` | [ ] Pending*    | 664519e02e |
| `DiagnosticEventPortMapping`                    | [ ] Pending*    | 266d4f7aa4 |
| `DiagnosticOperationCyclePortMapping`           | [ ] Pending*    | 266d4f7aa4 |
| `DiagnosticEnableConditionPortMapping`          | [ ] Pending*    | 266d4f7aa4 |
| `DiagnosticStorageConditionPortMapping`         | [ ] Pending*    | 266d4f7aa4 |
| `DiagnosticDemProvidedDataMapping`              | [ ] Pending*    | 531da6dd58 |
| `DiagnosticMasterToSlaveEventMapping`           | [ ] Pending*    | 531da6dd58 |
| `DiagnosticEventToSecurityEventMapping`         | [ ] Pending*    | 531da6dd58 |
| `DiagnosticInhibitSourceEventMapping`           | [ ] Pending*    | d488a5e4a8 |
| `DiagnosticFimAliasEventMapping`                | [ ] Pending*    | d488a5e4a8 |
| `DiagnosticFimAliasEventGroup`                  | [ ] Pending*    | d488a5e4a8 |
| `DiagnosticFimAliasEventGroupMapping`           | [ ] Pending*    | d488a5e4a8 |
| `DiagnosticFimFunctionMapping`                  | [ ] Pending*    | 86bff0a4f2 |
| `DiagnosticIumprToFunctionIdentifierMapping`    | [ ] Pending*    | 86bff0a4f2 |
| `DiagnosticJ1939SpnMapping`                     | [ ] Pending*    | 86bff0a4f2 |
| `DiagnosticJ1939Node`                           | [ ] Pending*    | 86bff0a4f2 |
| `DiagnosticJ1939SwMapping`                      | [ ] Pending*    | 86bff0a4f2 |
| `DiagnosticEventToTroubleCodeJ1939Mapping`      | [ ] Pending*    | 86bff0a4f2 |
| `CpSoftwareClusterResource`                     | [ ] Pending*    | 9c0046237b |
| `RoleBasedResourceDependency`                   | [ ] Pending*    | 9c0046237b |
| `CpSwClusterToDiagEventMapping`                 | [ ] Pending*    | 9c0046237b |
| `CpSwClusterResourceToDiagDataElemMapping`      | [ ] Pending*    | 9c0046237b |
| `CpSwClusterToDiagRoutineSubfunctionMapping`    | [ ] Pending*    | 9c0046237b |
| `CpSwClusterResourceToDiagFunctionIdMapping`    | [ ] Pending*    | 9c0046237b |
| `EcucDefinitionCollection`                      | [ ] Implemented | N/A        |
| `EcucModuleDef`                                 | [ ] Implemented | N/A        |
| `EcucContainerDef`                              | [ ] Implemented | N/A        |
| `EcucParamConfContainerDef`                     | [ ] Implemented | N/A        |
| `EcucChoiceContainerDef`                        | [ ] Implemented | N/A        |
| `EcucDefinitionElement`                         | [ ] Pending*    | ac47ae89f3 |
| `EcucCommonAttributes`                          | [ ] Implemented | N/A        |
| `EcucAbstractConfigurationClass`                | [ ] Implemented | N/A        |
| `EcucValueConfigurationClass`                   | [ ] Implemented | N/A        |
| `EcucMultiplicityConfigurationClass`            | [ ] Implemented | N/A        |
| `EcucConfigurationVariantEnum`                  | [ ] Implemented | N/A        |
| `EcucParameterDef`                              | [ ] Implemented | N/A        |
| `EcucIntegerParamDef`                           | [ ] Implemented | N/A        |
| `EcucAbstractStringParamDef`                    | [ ] Implemented | N/A        |
| `EcucStringParamDef`                            | [ ] Implemented | N/A        |
| `EcucMultilineStringParamDef`                   | [ ] Implemented | N/A        |
| `EcucFunctionNameDef`                           | [ ] Implemented | N/A        |
| `EcucEnumerationParamDef`                       | [ ] Implemented | N/A        |
| `EcucEnumerationLiteralDef`                     | [ ] Implemented | N/A        |
| `EcucAddInfoParamDef`                           | [ ] Implemented | N/A        |
| `EcucAbstractReferenceDef`                      | [ ] Implemented | N/A        |
| `EcucAbstractInternalReferenceDef`              | [ ] Implemented | N/A        |
| `EcucAbstractExternalReferenceDef`              | [ ] Implemented | N/A        |
| `EcucChoiceReferenceDef`                        | [ ] Implemented | N/A        |
| `EcucInstanceReferenceDef`                      | [ ] Implemented | N/A        |
| `EcucDestinationUriDefSet`                      | [ ] Implemented | N/A        |
| `EcucDestinationUriDef`                         | [ ] Implemented | N/A        |
| `EcucDestinationUriPolicy`                      | [ ] Implemented | N/A        |
| `EcucDestinationUriNestingContractEnum`         | [ ] Implemented | N/A        |
| `EcucDerivationSpecification`                   | [ ] Implemented | N/A        |
| `EcucQuery`                                     | [ ] Implemented | N/A        |

## Group27

Status: **0/75** completed

| Class Name                                  | Status          | Commit ID |
| ------------------------------------------- | --------------- | --------- |
| `EcucConditionSpecification`                | [ ] Implemented | N/A       |
| `EcucValidationCondition`                   | [ ] Implemented | N/A       |
| `EcucIndexableValue`                        | [ ] Implemented | N/A       |
| `EcucModuleConfigurationValues`             | [ ] Implemented | N/A       |
| `EcucContainerValue`                        | [ ] Implemented | N/A       |
| `EcucParameterValue`                        | [ ] Implemented | N/A       |
| `EcucTextualParamValue`                     | [ ] Implemented | N/A       |
| `EcucNumericalParamValue`                   | [ ] Implemented | N/A       |
| `EcucAddInfoParamValue`                     | [ ] Implemented | N/A       |
| `EcucAbstractReferenceValue`                | [ ] Implemented | N/A       |
| `EcucReferenceValue`                        | [ ] Implemented | N/A       |
| `EcucInstanceReferenceValue`                | [ ] Implemented | N/A       |
| `HwDescriptionEntity`                       | [ ] Implemented | N/A       |
| `HwPinGroupContent`                         | [ ] Implemented | N/A       |
| `HwElementConnector`                        | [ ] Implemented | N/A       |
| `HwPinGroupConnector`                       | [ ] Implemented | N/A       |
| `HwPinConnector`                            | [ ] Implemented | N/A       |
| `CommunicationController`                   | [ ] Implemented | N/A       |
| `ParameterSwComponentType`                  | [ ] Created     | N/A       |
| `SwComponentType`                           | [ ] Implemented | N/A       |
| `AtomicSwComponentType`                     | [ ] Implemented | N/A       |
| `ApplicationSwComponentType`                | [ ] Implemented | N/A       |
| `SwConnector`                               | [ ] Implemented | N/A       |
| `PassThroughSwConnector`                    | [ ] Implemented | N/A       |
| `InstantiationTimingEventProps`             | [ ] Implemented | N/A       |
| `InstantiationRTEEventProps`                | [ ] Implemented | N/A       |
| `PortInterface`                             | [ ] Implemented | N/A       |
| `ServiceProviderEnum`                       | [ ] Implemented | N/A       |
| `ClientServerInterface`                     | [ ] Implemented | N/A       |
| `ClientServerOperation`                     | [ ] Implemented | N/A       |
| `ArgumentDataPrototype`                     | [ ] Implemented | N/A       |
| `ServerArgumentImplPolicyEnum`              | [ ] Implemented | N/A       |
| `ApplicationError`                          | [ ] Implemented | N/A       |
| `ModeSwitchInterface`                       | [ ] Implemented | N/A       |
| `DataPrototypeMapping`                      | [ ] Implemented | N/A       |
| `ModeDeclarationMapping`                    | [ ] Implemented | N/A       |
| `ImplementationDataTypeSubElementRef`       | [ ] Created     | N/A       |
| `ApplicationCompositeDataTypeSubElementRef` | [ ] Implemented | N/A       |
| `MappingDirectionEnum`                      | [ ] Implemented | N/A       |
| `TextTableValuePair`                        | [ ] Implemented | N/A       |
| `DataTransformation`                        | [ ] Implemented | N/A       |
| `DataTransformationKindEnum`                | [ ] Implemented | N/A       |
| `SenderReceiverAnnotation`                  | [ ] Implemented | N/A       |
| `SenderAnnotation`                          | [ ] Created     | N/A       |
| `ReceiverAnnotation`                        | [ ] Created     | N/A       |
| `ProcessingKindEnum`                        | [ ] Implemented | N/A       |
| `DataLimitKindEnum`                         | [ ] Implemented | N/A       |
| `ClientServerAnnotation`                    | [ ] Implemented | N/A       |
| `IoHwAbstractionServerAnnotation`           | [ ] Implemented | N/A       |
| `FilterDebouncingEnum`                      | [ ] Implemented | N/A       |
| `PulseTestEnum`                             | [ ] Implemented | N/A       |
| `ParameterPortAnnotation`                   | [ ] Implemented | N/A       |
| `ModePortAnnotation`                        | [ ] Implemented | N/A       |
| `TriggerPortAnnotation`                     | [ ] Implemented | N/A       |
| `NvDataPortAnnotation`                      | [ ] Implemented | N/A       |
| `DelegatedPortAnnotation`                   | [ ] Implemented | N/A       |
| `SignalFanEnum`                             | [ ] Implemented | N/A       |
| `PPortComSpec`                              | [ ] Implemented | N/A       |
| `RPortComSpec`                              | [ ] Implemented | N/A       |
| `ReceiverComSpec`                           | [ ] Implemented | N/A       |
| `HandleOutOfRangeStatusEnum`                | [ ] Implemented | N/A       |
| `NonqueuedReceiverComSpec`                  | [ ] Implemented | N/A       |
| `HandleTimeoutEnum`                         | [ ] Implemented | N/A       |
| `TimeValue`                                 | [ ] Implemented | N/A       |
| `SenderComSpec`                             | [ ] Implemented | N/A       |
| `NonqueuedSenderComSpec`                    | [ ] Implemented | N/A       |
| `TransmissionComSpecProps`                  | [ ] Implemented | N/A       |
| `TransmissionAcknowledgementRequest`        | [ ] Implemented | N/A       |
| `HandleOutOfRangeEnum`                      | [ ] Implemented | N/A       |
| `TransmissionModeDefinitionEnum`            | [ ] Implemented | N/A       |
| `ClientComSpec`                             | [ ] Implemented | N/A       |
| `ServerComSpec`                             | [ ] Implemented | N/A       |
| `ParameterProvideComSpec`                   | [ ] Implemented | N/A       |
| `TransformationComSpecProps`                | [ ] Implemented | N/A       |
| `TransformationTechnology`                  | [ ] Implemented | N/A       |

## Group28

Status: **0/75** completed

| Class Name                                   | Status          | Commit ID |
| -------------------------------------------- | --------------- | --------- |
| `BufferProperties`                           | [ ] Implemented | N/A       |
| `TransformationDescription`                  | [ ] Implemented | N/A       |
| `TransformerClassEnum`                       | [ ] Implemented | N/A       |
| `EndToEndTransformationComSpecProps`         | [ ] Implemented | N/A       |
| `E2EProfileCompatibilityProps`               | [ ] Implemented | N/A       |
| `EndToEndProtection`                         | [ ] Implemented | N/A       |
| `ConsistencyNeeds`                           | [ ] Implemented | N/A       |
| `RunnableEntityGroup`                        | [ ] Implemented | N/A       |
| `DataPrototypeGroup`                         | [ ] Implemented | N/A       |
| `SwTextProps`                                | [ ] Implemented | N/A       |
| `ApplicationArrayDataType`                   | [ ] Implemented | N/A       |
| `ApplicationArrayElement`                    | [ ] Implemented | N/A       |
| `ArraySizeSemanticsEnum`                     | [ ] Implemented | N/A       |
| `ArraySizeHandlingEnum`                      | [ ] Implemented | N/A       |
| `ImplementationDataType`                     | [ ] Implemented | N/A       |
| `SwBaseType`                                 | [ ] Implemented | N/A       |
| `BaseTypeDefinition`                         | [ ] Implemented | N/A       |
| `BaseTypeDirectDefinition`                   | [ ] Implemented | N/A       |
| `BaseType`                                   | [ ] Implemented | N/A       |
| `ByteOrderEnum`                              | [ ] Implemented | N/A       |
| `AutosarDataPrototype`                       | [ ] Implemented | N/A       |
| `ParameterInAtomicSWCTypeInstanceRef`        | [ ] Implemented | N/A       |
| `ArParameterInImplementationDataInstanceRef` | [ ] Created     | N/A       |
| `SwDataDefProps`                             | [ ] Implemented | N/A       |
| `SwBitRepresentation`                        | [ ] Implemented | N/A       |
| `SwCalibrationAccessEnum`                    | [ ] Implemented | N/A       |
| `SwCalprmAxis`                               | [ ] Implemented | N/A       |
| `CalprmAxisCategoryEnum`                     | [ ] Implemented | N/A       |
| `SwCalprmAxisTypeProps`                      | [ ] Implemented | N/A       |
| `SwAxisGeneric`                              | [ ] Implemented | N/A       |
| `SwAxisType`                                 | [ ] Created     | N/A       |
| `SwGenericAxisParam`                         | [ ] Implemented | N/A       |
| `SwCalprmRefProxy`                           | [ ] Implemented | N/A       |
| `SwVariableRefProxy`                         | [ ] Implemented | N/A       |
| `SwDataDependency`                           | [ ] Implemented | N/A       |
| `SwDataDependencyArgs`                       | [ ] Implemented | N/A       |
| `PhysicalDimension`                          | [ ] Implemented | N/A       |
| `PhysicalDimensionMapping`                   | [ ] Created     | N/A       |
| `PhysicalDimensionMappingSet`                | [ ] Created     | N/A       |
| `Unit`                                       | [ ] Implemented | N/A       |
| `PhysConstrs`                                | [ ] Implemented | N/A       |
| `InternalConstrs`                            | [ ] Implemented | N/A       |
| `Limit`                                      | [ ] Implemented | N/A       |
| `MonotonyEnum`                               | [ ] Implemented | N/A       |
| `IntervalTypeEnum`                           | [ ] Implemented | N/A       |
| `DisplayPresentationEnum`                    | [ ] Implemented | N/A       |
| `ValueSpecification`                         | [ ] Implemented | N/A       |
| `ReferenceValueSpecification`                | [ ] Implemented | N/A       |
| `NotAvailableValueSpecification`             | [ ] Implemented | N/A       |
| `ConstantSpecificationMapping`               | [ ] Implemented | N/A       |
| `ApplicationValueSpecification`              | [ ] Implemented | N/A       |
| `NumericalOrText`                            | [ ] Implemented | N/A       |
| `SwAxisCont`                                 | [ ] Created     | N/A       |
| `SwValues`                                   | [ ] Implemented | N/A       |
| `ValueGroup`                                 | [ ] Implemented | N/A       |
| `ValueList`                                  | [ ] Implemented | N/A       |
| `AbstractRuleBasedValueSpecification`        | [ ] Implemented | N/A       |
| `ApplicationRuleBasedValueSpecification`     | [ ] Implemented | N/A       |
| `RuleBasedAxisCont`                          | [ ] Implemented | N/A       |
| `RuleBasedValueCont`                         | [ ] Implemented | N/A       |
| `NumericalRuleBasedValueSpecification`       | [ ] Implemented | N/A       |
| `RuleBasedValueSpecification`                | [ ] Implemented | N/A       |
| `RuleArguments`                              | [ ] Implemented | N/A       |
| `CalibrationParameterValueSet`               | [ ] Created     | N/A       |
| `CalibrationParameterValue`                  | [ ] Created     | N/A       |
| `RunnableEntity`                             | [ ] Implemented | N/A       |
| `TimingEvent`                                | [ ] Implemented | N/A       |
| `ExecutableEntityActivationReason`           | [ ] Implemented | N/A       |
| `AbstractEvent`                              | [ ] Implemented | N/A       |
| `SwcModeSwitchEvent`                         | [ ] Implemented | N/A       |
| `ModeSwitchedAckEvent`                       | [ ] Implemented | N/A       |
| `ExternalTriggerOccurredEvent`               | [ ] Created     | N/A       |
| `TransformerHardErrorEvent`                  | [ ] Created     | N/A       |
| `OsTaskExecutionEvent`                       | [ ] Created     | N/A       |
| `WaitPoint`                                  | [ ] Implemented | N/A       |

## Group29

Status: **0/74** completed

| Class Name                                     | Status          | Commit ID |
| ---------------------------------------------- | --------------- | --------- |
| `SwcExclusiveAreaPolicy`                       | [ ] Implemented | N/A       |
| `RteApiReturnValueProvisionEnum`               | [ ] Implemented | N/A       |
| `ExternalTriggeringPoint`                      | [ ] Implemented | N/A       |
| `IncludedDataTypeSet`                          | [ ] Implemented | N/A       |
| `SwcServiceDependency`                         | [ ] Implemented | N/A       |
| `SymbolicNameProps`                            | [ ] Implemented | N/A       |
| `VariationPointProxy`                          | [ ] Implemented | N/A       |
| `SwcModeManagerErrorEvent`                     | [ ] Created     | N/A       |
| `SensorActuatorSwComponentType`                | [ ] Implemented | N/A       |
| `EcuAbstractionSwComponentType`                | [ ] Implemented | N/A       |
| `ComplexDeviceDriverSwComponentType`           | [ ] Implemented | N/A       |
| `ServiceSwComponentType`                       | [ ] Implemented | N/A       |
| `NvBlockSwComponentType`                       | [ ] Implemented | N/A       |
| `SwComponentDocumentation`                     | [ ] Implemented | N/A       |
| `AdditionalBindingTimeEnum`                    | [ ] Created     | N/A       |
| `FunctionInhibitionAvailabilityNeeds`          | [ ] Implemented | N/A       |
| `DiagnosticOperationCycleNeeds`                | [ ] Implemented | N/A       |
| `OperationCycleTypeEnum`                       | [ ] Implemented | N/A       |
| `DiagnosticEnableConditionNeeds`               | [ ] Implemented | N/A       |
| `EventAcceptanceStatusEnum`                    | [ ] Implemented | N/A       |
| `DiagnosticStorageConditionNeeds`              | [ ] Implemented | N/A       |
| `StorageConditionStatusEnum`                   | [ ] Implemented | N/A       |
| `IndicatorStatusNeeds`                         | [ ] Implemented | N/A       |
| `DiagnosticIndicatorTypeEnum`                  | [ ] Implemented | N/A       |
| `ObdRatioServiceNeeds`                         | [ ] Implemented | N/A       |
| `ObdControlServiceNeeds`                       | [ ] Implemented | N/A       |
| `ObdRatioConnectionKindEnum`                   | [ ] Implemented | N/A       |
| `ObdPidServiceNeeds`                           | [ ] Implemented | N/A       |
| `ObdInfoServiceNeeds`                          | [ ] Implemented | N/A       |
| `ObdMonitorServiceNeeds`                       | [ ] Implemented | N/A       |
| `DiagnosticMonitorUpdateKindEnum`              | [ ] Implemented | N/A       |
| `ObdRatioDenominatorNeeds`                     | [ ] Implemented | N/A       |
| `DiagnosticDenominatorConditionEnum`           | [ ] Implemented | N/A       |
| `DiagnosticTestResult`                         | [ ] Created     | N/A       |
| `DoIpRoutingActivationAuthenticationNeeds`     | [ ] Implemented | N/A       |
| `DoIpRoutingActivationConfirmationNeeds`       | [ ] Implemented | N/A       |
| `SecureOnBoardCommunicationNeeds`              | [ ] Implemented | N/A       |
| `VerificationStatusIndicationModeEnum`         | [ ] Implemented | N/A       |
| `IdsMgrNeeds`                                  | [ ] Implemented | N/A       |
| `RapidPrototypingScenario`                     | [ ] Created     | N/A       |
| `RptContainer`                                 | [ ] Created     | N/A       |
| `RptHook`                                      | [ ] Created     | N/A       |
| `RptProfile`                                   | [ ] Created     | N/A       |
| `CommunicationConnector`                       | [ ] Implemented | N/A       |
| `PhysicalChannel`                              | [ ] Implemented | N/A       |
| `AbstractCanCluster`                           | [ ] Implemented | N/A       |
| `CanCluster`                                   | [ ] Implemented | N/A       |
| `CanCommunicationController`                   | [ ] Implemented | N/A       |
| `AbstractCanCommunicationController`           | [ ] Implemented | N/A       |
| `AbstractCanCommunicationControllerAttributes` | [ ] Implemented | N/A       |
| `CanControllerFdConfiguration`                 | [ ] Implemented | N/A       |
| `CanControllerXlConfiguration`                 | [ ] Implemented | N/A       |
| `CanControllerXlConfigurationRequirements`     | [ ] Implemented | N/A       |
| `AbstractCanPhysicalChannel`                   | [ ] Implemented | N/A       |
| `CanPhysicalChannel`                           | [ ] Implemented | N/A       |
| `AbstractCanCommunicationConnector`            | [ ] Implemented | N/A       |
| `TtcanCluster`                                 | [ ] Created     | N/A       |
| `TtcanCommunicationController`                 | [ ] Created     | N/A       |
| `TtcanPhysicalChannel`                         | [ ] Created     | N/A       |
| `TtcanCommunicationConnector`                  | [ ] Created     | N/A       |
| `FlexrayCluster`                               | [ ] Implemented | N/A       |
| `FlexrayFifoConfiguration`                     | [ ] Implemented | N/A       |
| `FlexrayFifoRange`                             | [ ] Implemented | N/A       |
| `LinCluster`                                   | [ ] Implemented | N/A       |
| `LinCommunicationController`                   | [ ] Implemented | N/A       |
| `LinMaster`                                    | [ ] Implemented | N/A       |
| `LinSlaveConfig`                               | [ ] Implemented | N/A       |
| `LinSlaveConfigIdent`                          | [ ] Implemented | N/A       |
| `LinSlave`                                     | [ ] Created     | N/A       |
| `LinErrorResponse`                             | [ ] Implemented | N/A       |
| `LinConfigurableFrame`                         | [ ] Implemented | N/A       |
| `LinOrderedConfigurableFrame`                  | [ ] Implemented | N/A       |
| `LinPhysicalChannel`                           | [ ] Implemented | N/A       |
| `EthernetCluster`                              | [ ] Implemented | N/A       |

## Group30

Status: **0/75** completed

| Class Name                                       | Status          | Commit ID |
| ------------------------------------------------ | --------------- | --------- |
| `CouplingElement`                                | [ ] Created     | N/A       |
| `CouplingElementEnum`                            | [ ] Created     | N/A       |
| `CouplingPort`                                   | [ ] Implemented | N/A       |
| `EthernetConnectionNegotiationEnum`              | [ ] Implemented | N/A       |
| `EthernetMacLayerTypeEnum`                       | [ ] Implemented | N/A       |
| `EthernetPhysicalLayerTypeEnum`                  | [ ] Implemented | N/A       |
| `EthernetSwitchVlanIngressTagEnum`               | [ ] Implemented | N/A       |
| `CouplingPortConnection`                         | [ ] Implemented | N/A       |
| `EthernetCommunicationController`                | [ ] Implemented | N/A       |
| `EthernetCommunicationConnector`                 | [ ] Implemented | N/A       |
| `CouplingPortDetails`                            | [ ] Implemented | N/A       |
| `EthernetCouplingPortSchedulerEnum`              | [ ] Implemented | N/A       |
| `CouplingPortShaper`                             | [ ] Created     | N/A       |
| `CouplingPortFifo`                               | [ ] Implemented | N/A       |
| `CouplingPortRatePolicy`                         | [ ] Implemented | N/A       |
| `CouplingPortRatePolicyActionEnum`               | [ ] Implemented | N/A       |
| `CouplingPortTrafficClassAssignment`             | [ ] Implemented | N/A       |
| `EthernetSwitchVlanEgressTaggingEnum`            | [ ] Implemented | N/A       |
| `DhcpServerConfiguration`                        | [ ] Implemented | N/A       |
| `Ipv4DhcpServerConfiguration`                    | [ ] Implemented | N/A       |
| `Ipv6DhcpServerConfiguration`                    | [ ] Implemented | N/A       |
| `CouplingElementAbstractDetails`                 | [ ] Created     | N/A       |
| `CouplingElementSwitchDetails`                   | [ ] Created     | N/A       |
| `SwitchStreamIdentification`                     | [ ] Created     | N/A       |
| `SwitchStreamFilterRule`                         | [ ] Created     | N/A       |
| `StreamFilterRuleDataLinkLayer`                  | [ ] Created     | N/A       |
| `StreamFilterMACAddress`                         | [ ] Created     | N/A       |
| `StreamFilterRuleIpTp`                           | [ ] Created     | N/A       |
| `StreamFilterIpv4Address`                        | [ ] Created     | N/A       |
| `StreamFilterIpv6Address`                        | [ ] Created     | N/A       |
| `StreamFilterPortRange`                          | [ ] Created     | N/A       |
| `StreamFilterIEEE1722Tp`                         | [ ] Created     | N/A       |
| `SwitchStreamFilterActionDestPortModification`   | [ ] Created     | N/A       |
| `SwitchStreamFilterActionPortModificationEnum`   | [ ] Created     | N/A       |
| `SwitchStreamFilterEntry`                        | [ ] Created     | N/A       |
| `SwitchAsynchronousTrafficShaperGroupEntry`      | [ ] Created     | N/A       |
| `SwitchStreamGateEntry`                          | [ ] Created     | N/A       |
| `SwitchFlowMeteringEntry`                        | [ ] Created     | N/A       |
| `FlowMeteringColorModeEnum`                      | [ ] Created     | N/A       |
| `EthIpProps`                                     | [ ] Created     | N/A       |
| `Ipv4Props`                                      | [ ] Created     | N/A       |
| `Ipv4ArpProps`                                   | [ ] Created     | N/A       |
| `Ipv4AutoIpProps`                                | [ ] Created     | N/A       |
| `Ipv4FragmentationProps`                         | [ ] Created     | N/A       |
| `Ipv6Props`                                      | [ ] Created     | N/A       |
| `Ipv6FragmentationProps`                         | [ ] Created     | N/A       |
| `Dhcpv6Props`                                    | [ ] Created     | N/A       |
| `Ipv6NdpProps`                                   | [ ] Created     | N/A       |
| `EthernetWakeupSleepOnDatalineConfig`            | [ ] Created     | N/A       |
| `EthernetWakeupSleepOnDatalineConfigSet`         | [ ] Created     | N/A       |
| `PlcaProps`                                      | [ ] Implemented | N/A       |
| `MacSecProps`                                    | [ ] Implemented | N/A       |
| `MacSecLocalKayProps`                            | [ ] Implemented | N/A       |
| `MacSecGlobalKayProps`                           | [ ] Implemented | N/A       |
| `MacSecParticipantSet`                           | [ ] Created     | N/A       |
| `MacSecKayParticipant`                           | [ ] Implemented | N/A       |
| `MacSecCryptoAlgoConfig`                         | [ ] Implemented | N/A       |
| `MacSecCipherSuiteConfig`                        | [ ] Implemented | N/A       |
| `MacSecConfidentialityOffsetEnum`                | [ ] Implemented | N/A       |
| `MacSecCapabilityEnum`                           | [ ] Implemented | N/A       |
| `MacSecRoleEnum`                                 | [ ] Implemented | N/A       |
| `MacSecFailPermissiveModeEnum`                   | [ ] Implemented | N/A       |
| `UserDefinedCluster`                             | [ ] Created     | N/A       |
| `UserDefinedPhysicalChannel`                     | [ ] Created     | N/A       |
| `UserDefinedCommunicationConnector`              | [ ] Created     | N/A       |
| `UserDefinedCommunicationController`             | [ ] Created     | N/A       |
| `SystemMapping`                                  | [ ] Implemented | N/A       |
| `SwcToApplicationPartitionMapping`               | [ ] Created     | N/A       |
| `ApplicationPartition`                           | [ ] Created     | N/A       |
| `MappingConstraint`                              | [ ] Created     | N/A       |
| `ComponentClustering`                            | [ ] Created     | N/A       |
| `MappingScopeEnum`                               | [ ] Created     | N/A       |
| `ComponentSeparation`                            | [ ] Created     | N/A       |
| `J1939ControllerApplicationToJ1939NmNodeMapping` | [ ] Created     | N/A       |
| `J1939ControllerApplication`                     | [ ] Created     | N/A       |

## Group31

Status: **0/75** completed

| Class Name                                               | Status          | Commit ID |
| -------------------------------------------------------- | --------------- | --------- |
| `RteEventInCompositionToOsTaskProxyMapping`              | [ ] Created     | N/A       |
| `RteEventInCompositionSeparation`                        | [ ] Created     | N/A       |
| `RteEventInSystemToOsTaskProxyMapping`                   | [ ] Created     | N/A       |
| `RteEventInSystemSeparation`                             | [ ] Created     | N/A       |
| `SenderRecArrayElementMapping`                           | [ ] Implemented | N/A       |
| `ClientServerToSignalMapping`                            | [ ] Created     | N/A       |
| `SenderReceiverCompositeElementToSignalMapping`          | [ ] Created     | N/A       |
| `TriggerToSignalMapping`                                 | [ ] Created     | N/A       |
| `CommonSignalPath`                                       | [ ] Created     | N/A       |
| `SwcToSwcSignal`                                         | [ ] Created     | N/A       |
| `SwcToSwcOperationArguments`                             | [ ] Created     | N/A       |
| `SwcToSwcOperationArgumentsDirectionEnum`                | [ ] Created     | N/A       |
| `ForbiddenSignalPath`                                    | [ ] Created     | N/A       |
| `PermissibleSignalPath`                                  | [ ] Created     | N/A       |
| `SeparateSignalPath`                                     | [ ] Created     | N/A       |
| `EcuResourceEstimation`                                  | [ ] Created     | N/A       |
| `PncMapping`                                             | [ ] Created     | N/A       |
| `CpSoftwareClusterToEcuInstanceMapping`                  | [ ] Created     | N/A       |
| `CpSoftwareClusterResourceToApplicationPartitionMapping` | [ ] Created     | N/A       |
| `CpSoftwareClusterMappingSet`                            | [ ] Created     | N/A       |
| `CpSoftwareClusterToApplicationPartitionMapping`         | [ ] Created     | N/A       |
| `SystemSignalToCommunicationResourceMapping`             | [ ] Created     | N/A       |
| `SystemSignalGroupToCommunicationResourceMapping`        | [ ] Created     | N/A       |
| `DdsCpISignalToDdsTopicMapping`                          | [ ] Created     | N/A       |
| `CommConnectorPort`                                      | [ ] Implemented | N/A       |
| `IPduPort`                                               | [ ] Implemented | N/A       |
| `IPduSignalProcessingEnum`                               | [ ] Implemented | N/A       |
| `ISignal`                                                | [ ] Implemented | N/A       |
| `DataTypePolicyEnum`                                     | [ ] Implemented | N/A       |
| `ISignalTypeEnum`                                        | [ ] Implemented | N/A       |
| `ISignalProps`                                           | [ ] Implemented | N/A       |
| `ISignalGroup`                                           | [ ] Implemented | N/A       |
| `SystemSignalGroup`                                      | [ ] Implemented | N/A       |
| `ISignalToIPduMapping`                                   | [ ] Implemented | N/A       |
| `ISignalTriggering`                                      | [ ] Implemented | N/A       |
| `Pdu`                                                    | [ ] Implemented | N/A       |
| `IPdu`                                                   | [ ] Implemented | N/A       |
| `ISignalIPdu`                                            | [ ] Implemented | N/A       |
| `NmPdu`                                                  | [ ] Implemented | N/A       |
| `NPdu`                                                   | [ ] Implemented | N/A       |
| `DcmIPdu`                                                | [ ] Implemented | N/A       |
| `DiagPduType`                                            | [ ] Created     | N/A       |
| `J1939DcmIPdu`                                           | [ ] Created     | N/A       |
| `PduToFrameMapping`                                      | [ ] Implemented | N/A       |
| `IPduTiming`                                             | [ ] Implemented | N/A       |
| `PduTriggering`                                          | [ ] Implemented | N/A       |
| `ContainerIPdu`                                          | [ ] Created     | N/A       |
| `ContainerIPduTriggerEnum`                               | [ ] Created     | N/A       |
| `ContainerIPduHeaderTypeEnum`                            | [ ] Created     | N/A       |
| `RxAcceptContainedIPduEnum`                              | [ ] Created     | N/A       |
| `SecureCommunicationProps`                               | [ ] Implemented | N/A       |
| `SecureCommunicationPropsSet`                            | [ ] Implemented | N/A       |
| `SecureCommunicationFreshnessProps`                      | [ ] Implemented | N/A       |
| `SecureCommunicationAuthenticationProps`                 | [ ] Implemented | N/A       |
| `CryptoServiceKey`                                       | [ ] Created     | N/A       |
| `CryptoServiceKeyGenerationEnum`                         | [ ] Created     | N/A       |
| `CryptoServiceQueue`                                     | [ ] Created     | N/A       |
| `GeneralPurposeConnection`                               | [ ] Created     | N/A       |
| `RelativeTolerance`                                      | [ ] Implemented | N/A       |
| `AbsoluteTolerance`                                      | [ ] Implemented | N/A       |
| `Frame`                                                  | [ ] Implemented | N/A       |
| `LinFrame`                                               | [ ] Implemented | N/A       |
| `LinFrameTriggering`                                     | [ ] Implemented | N/A       |
| `LinChecksumType`                                        | [ ] Created     | N/A       |
| `LinUnconditionalFrame`                                  | [ ] Implemented | N/A       |
| `LinSporadicFrame`                                       | [ ] Created     | N/A       |
| `LinEventTriggeredFrame`                                 | [ ] Created     | N/A       |
| `ScheduleTableEntry`                                     | [ ] Implemented | N/A       |
| `FreeFormatEntry`                                        | [ ] Implemented | N/A       |
| `LinConfigurationEntry`                                  | [ ] Implemented | N/A       |
| `AssignFrameId`                                          | [ ] Implemented | N/A       |
| `UnassignFrameId`                                        | [ ] Implemented | N/A       |
| `AssignFrameIdRange`                                     | [ ] Implemented | N/A       |
| `FramePid`                                               | [ ] Implemented | N/A       |
| `AssignNad`                                              | [ ] Implemented | N/A       |

## Group32

Status: **0/75** completed

| Class Name                             | Status          | Commit ID |
| -------------------------------------- | --------------- | --------- |
| `ConditionalChangeNad`                 | [ ] Implemented | N/A       |
| `SaveConfigurationEntry`               | [ ] Implemented | N/A       |
| `DataDumpEntry`                        | [ ] Implemented | N/A       |
| `FreeFormat`                           | [ ] Implemented | N/A       |
| `CanFrame`                             | [ ] Implemented | N/A       |
| `CanFrameTriggering`                   | [ ] Implemented | N/A       |
| `CanAddressingModeType`                | [ ] Implemented | N/A       |
| `RxIdentifierRange`                    | [ ] Implemented | N/A       |
| `CanFrameRxBehaviorEnum`               | [ ] Implemented | N/A       |
| `CanFrameTxBehaviorEnum`               | [ ] Implemented | N/A       |
| `TtcanAbsolutelyScheduledTiming`       | [ ] Implemented | N/A       |
| `TtcanTriggerType`                     | [ ] Implemented | N/A       |
| `SoAdConfig`                           | [ ] Implemented | N/A       |
| `SocketAddress`                        | [ ] Implemented | N/A       |
| `UdpChecksumCalculationEnum`           | [ ] Implemented | N/A       |
| `IPv6ExtHeaderFilterSet`               | [ ] Created     | N/A       |
| `ApplicationEndpoint`                  | [ ] Implemented | N/A       |
| `RtpTp`                                | [ ] Created     | N/A       |
| `Ieee1722Tp`                           | [ ] Created     | N/A       |
| `HttpTp`                               | [ ] Created     | N/A       |
| `Ipv6Configuration`                    | [ ] Implemented | N/A       |
| `MacMulticastConfiguration`            | [ ] Created     | N/A       |
| `InfrastructureServices`               | [ ] Implemented | N/A       |
| `TimeSyncTechnologyEnum`               | [ ] Implemented | N/A       |
| `DoIpEntityRoleEnum`                   | [ ] Implemented | N/A       |
| `DdsCpServiceInstance`                 | [ ] Created     | N/A       |
| `DdsCpProvidedServiceInstance`         | [ ] Created     | N/A       |
| `DdsCpConsumedServiceInstance`         | [ ] Created     | N/A       |
| `DdsCpServiceInstanceEvent`            | [ ] Created     | N/A       |
| `DdsCpServiceInstanceOperation`        | [ ] Created     | N/A       |
| `ServiceInstanceCollectionSet`         | [ ] Created     | N/A       |
| `AbstractServiceInstance`              | [ ] Implemented | N/A       |
| `ProvidedServiceInstance`              | [ ] Implemented | N/A       |
| `PduActivationRoutingGroup`            | [ ] Implemented | N/A       |
| `EventGroupControlTypeEnum`            | [ ] Implemented | N/A       |
| `SoConIPduIdentifier`                  | [ ] Created     | N/A       |
| `SocketConnectionIpduIdentifierSet`    | [ ] Created     | N/A       |
| `EventHandler`                         | [ ] Implemented | N/A       |
| `ConsumedServiceInstance`              | [ ] Implemented | N/A       |
| `ConsumedEventGroup`                   | [ ] Implemented | N/A       |
| `SomeipSdServerServiceInstanceConfig`  | [ ] Created     | N/A       |
| `SomeipSdServerEventGroupTimingConfig` | [ ] Implemented | N/A       |
| `SomeipSdClientEventGroupTimingConfig` | [ ] Implemented | N/A       |
| `DdsCpConfig`                          | [ ] Created     | N/A       |
| `DdsCpDomain`                          | [ ] Created     | N/A       |
| `DdsCpTopic`                           | [ ] Created     | N/A       |
| `DdsCpPartition`                       | [ ] Created     | N/A       |
| `DdsCpQosProfile`                      | [ ] Created     | N/A       |
| `DdsTopicData`                         | [ ] Created     | N/A       |
| `DdsDurability`                        | [ ] Created     | N/A       |
| `DdsDurabilityKindEnum`                | [ ] Created     | N/A       |
| `DdsDurabilityService`                 | [ ] Created     | N/A       |
| `DdsDurabilityServiceHistoryKindEnum`  | [ ] Created     | N/A       |
| `DdsDeadline`                          | [ ] Created     | N/A       |
| `DdsLatencyBudget`                     | [ ] Created     | N/A       |
| `DdsOwnership`                         | [ ] Created     | N/A       |
| `DdsOwnershipKindEnum`                 | [ ] Created     | N/A       |
| `DdsOwnershipStrength`                 | [ ] Created     | N/A       |
| `DdsLiveliness`                        | [ ] Created     | N/A       |
| `DdsLivenessKindEnum`                  | [ ] Created     | N/A       |
| `DdsReliability`                       | [ ] Created     | N/A       |
| `DdsReliabilityKindEnum`               | [ ] Created     | N/A       |
| `DdsTransportPriority`                 | [ ] Created     | N/A       |
| `DdsLifespan`                          | [ ] Created     | N/A       |
| `DdsDestinationOrder`                  | [ ] Created     | N/A       |
| `DdsDestinationOrderKindEnum`          | [ ] Created     | N/A       |
| `DdsHistory`                           | [ ] Created     | N/A       |
| `DdsHistoryKindEnum`                   | [ ] Created     | N/A       |
| `DdsResourceLimits`                    | [ ] Created     | N/A       |
| `StaticSocketConnection`               | [ ] Implemented | N/A       |
| `IPSecRule`                            | [ ] Pending*    | N/A       |
| `IPSecConfigProps`                     | [ ] Pending*    | N/A       |
| `IPsecIpProtocolEnum`                  | [ ] Pending*    | N/A       |
| `IPsecPolicyEnum`                      | [ ] Pending*    | N/A       |
| `IPsecModeEnum`                        | [ ] Pending*    | N/A       |

## Group33

Status: **0/75** completed

| Class Name                                  | Status          | Commit ID |
| ------------------------------------------- | --------------- | --------- |
| `IPsecHeaderTypeEnum`                       | [ ] Pending*    | N/A       |
| `IPsecDpdActionEnum`                        | [ ] Pending*    | N/A       |
| `EthernetFrameTriggering`                   | [ ] Created     | N/A       |
| `UserDefinedEthernetFrame`                  | [ ] Created     | N/A       |
| `Ieee1722TpEthernetFrame`                   | [ ] Created     | N/A       |
| `StateDependentFirewall`                    | [ ] Implemented | N/A       |
| `TpConfig`                                  | [ ] Implemented | N/A       |
| `FlexrayTpConfig`                           | [ ] Created     | N/A       |
| `FlexrayTpConnectionControl`                | [ ] Created     | N/A       |
| `FlexrayTpConnection`                       | [ ] Created     | N/A       |
| `FlexrayTpPduPool`                          | [ ] Created     | N/A       |
| `FlexrayTpNode`                             | [ ] Created     | N/A       |
| `FlexrayTpEcu`                              | [ ] Created     | N/A       |
| `FlexrayArTpConfig`                         | [ ] Created     | N/A       |
| `FlexrayArTpChannel`                        | [ ] Created     | N/A       |
| `FlexrayArTpNode`                           | [ ] Created     | N/A       |
| `FlexrayArTpConnection`                     | [ ] Created     | N/A       |
| `FrArTpAckType`                             | [ ] Created     | N/A       |
| `MaximumMessageLengthType`                  | [ ] Created     | N/A       |
| `CanTpConfig`                               | [ ] Implemented | N/A       |
| `CanTpChannel`                              | [ ] Implemented | N/A       |
| `CanTpConnection`                           | [ ] Implemented | N/A       |
| `CanTpAddressingFormatType`                 | [ ] Implemented | N/A       |
| `CanTpAddress`                              | [ ] Implemented | N/A       |
| `CanTpEcu`                                  | [ ] Implemented | N/A       |
| `CanTpNode`                                 | [ ] Implemented | N/A       |
| `NetworkTargetAddressType`                  | [ ] Implemented | N/A       |
| `LinTpConfig`                               | [ ] Implemented | N/A       |
| `LinTpNode`                                 | [ ] Implemented | N/A       |
| `EthTpConfig`                               | [ ] Created     | N/A       |
| `EthTpConnection`                           | [ ] Created     | N/A       |
| `SomeipTpConfig`                            | [ ] Created     | N/A       |
| `SomeipTpConnection`                        | [ ] Created     | N/A       |
| `SomeipTpChannel`                           | [ ] Created     | N/A       |
| `J1939TpConfig`                             | [ ] Created     | N/A       |
| `J1939TpConnection`                         | [ ] Created     | N/A       |
| `J1939TpPg`                                 | [ ] Created     | N/A       |
| `J1939TpNode`                               | [ ] Created     | N/A       |
| `TpConnection`                              | [ ] Implemented | N/A       |
| `IEEE1722TpConfig`                          | [ ] Created     | N/A       |
| `IEEE1722TpConnection`                      | [ ] Created     | N/A       |
| `IEEE1722TpAvConnection`                    | [ ] Created     | N/A       |
| `IEEE1722TpCrfConnection`                   | [ ] Created     | N/A       |
| `IEEE1722TpCrfTypeEnum`                     | [ ] Created     | N/A       |
| `IEEE1722TpCrfPullEnum`                     | [ ] Created     | N/A       |
| `IEEE1722TpAafConnection`                   | [ ] Created     | N/A       |
| `IEEE1722TpAafNominalRateEnum`              | [ ] Created     | N/A       |
| `IEEE1722TpAafFormatEnum`                   | [ ] Created     | N/A       |
| `IEEE1722TpAafAes3DataTypeEnum`             | [ ] Created     | N/A       |
| `IEEE1722TpIidcConnection`                  | [ ] Created     | N/A       |
| `IEEE1722TpRvfConnection`                   | [ ] Created     | N/A       |
| `IEEE1722TpRvfPixelDepthEnum`               | [ ] Created     | N/A       |
| `IEEE1722TpRvfPixelFormatEnum`              | [ ] Created     | N/A       |
| `IEEE1722TpRvfColorSpaceEnum`               | [ ] Created     | N/A       |
| `IEEE1722TpRvfFrameRateEnum`                | [ ] Created     | N/A       |
| `IEEE1722TpAcfConnection`                   | [ ] Created     | N/A       |
| `IEEE1722TpAcfBus`                          | [ ] Created     | N/A       |
| `IEEE1722TpAcfBusPart`                      | [ ] Created     | N/A       |
| `IEEE1722TpAcfCan`                          | [ ] Created     | N/A       |
| `IEEE1722TpAcfCanPart`                      | [ ] Created     | N/A       |
| `IEEE1722TpAcfCanMessageTypeEnum`           | [ ] Created     | N/A       |
| `IEEE1722TpAcfLin`                          | [ ] Created     | N/A       |
| `IEEE1722TpAcfLinPart`                      | [ ] Created     | N/A       |
| `BusspecificNmEcu`                          | [ ] Implemented | N/A       |
| `NmCoordinator`                             | [ ] Created     | N/A       |
| `NmNode`                                    | [ ] Implemented | N/A       |
| `NmCoordinatorRoleEnum`                     | [ ] Implemented | N/A       |
| `FlexrayNmScheduleVariant`                  | [ ] Implemented | N/A       |
| `CanNmEcu`                                  | [ ] Implemented | N/A       |
| `J1939NmNode`                               | [ ] Implemented | N/A       |
| `J1939NodeName`                             | [ ] Implemented | N/A       |
| `J1939NmAddressConfigurationCapabilityEnum` | [ ] Implemented | N/A       |
| `BusMirrorChannelMapping`                   | [ ] Created     | N/A       |
| `MirroringProtocolEnum`                     | [ ] Created     | N/A       |
| `BusMirrorChannel`                          | [ ] Created     | N/A       |

## Group34

Status: **0/75** completed

| Class Name                                          | Status          | Commit ID |
| --------------------------------------------------- | --------------- | --------- |
| `BusMirrorChannelMappingCan`                        | [ ] Created     | N/A       |
| `BusMirrorCanIdRangeMapping`                        | [ ] Created     | N/A       |
| `BusMirrorCanIdToCanIdMapping`                      | [ ] Created     | N/A       |
| `BusMirrorLinPidToCanIdMapping`                     | [ ] Created     | N/A       |
| `BusMirrorChannelMappingFlexray`                    | [ ] Created     | N/A       |
| `BusMirrorChannelMappingIp`                         | [ ] Created     | N/A       |
| `BusMirrorChannelMappingUserDefined`                | [ ] Created     | N/A       |
| `SignalServiceTranslationPropsSet`                  | [ ] Implemented | N/A       |
| `SignalServiceTranslationProps`                     | [ ] Implemented | N/A       |
| `SignalServiceTranslationEventProps`                | [ ] Implemented | N/A       |
| `SignalServiceTranslationControlEnum`               | [ ] Implemented | N/A       |
| `UserDefinedTransformationDescription`              | [ ] Created     | N/A       |
| `CSTransformerErrorReactionEnum`                    | [ ] Implemented | N/A       |
| `SOMEIPTransformationDescription`                   | [ ] Created     | N/A       |
| `TransformationPropsSet`                            | [ ] Created     | N/A       |
| `TransformationProps`                               | [ ] Created     | N/A       |
| `SOMEIPTransformationProps`                         | [ ] Created     | N/A       |
| `DataPrototypeReference`                            | [ ] Implemented | N/A       |
| `DataPrototypeInPortInterfaceRef`                   | [ ] Implemented | N/A       |
| `DataPrototypeInSenderReceiverInterfaceInstanceRef` | [ ] Implemented | N/A       |
| `DataPrototypeInClientServerInterfaceInstanceRef`   | [ ] Implemented | N/A       |
| `ImplementationDataTypeElementInPortInterfaceRef`   | [ ] Implemented | N/A       |
| `EndToEndTransformationDescription`                 | [ ] Implemented | N/A       |
| `DataIdModeEnum`                                    | [ ] Implemented | N/A       |
| `EndToEndProfileBehaviorEnum`                       | [ ] Implemented | N/A       |
| `UserDefinedTransformationProps`                    | [ ] Created     | N/A       |
| `GlobalTimeDomain`                                  | [ ] Created     | N/A       |
| `AbstractGlobalTimeDomainProps`                     | [ ] Created     | N/A       |
| `NetworkSegmentIdentification`                      | [ ] Created     | N/A       |
| `GlobalTimeMaster`                                  | [ ] Created     | N/A       |
| `GlobalTimeSlave`                                   | [ ] Created     | N/A       |
| `GlobalTimeGateway`                                 | [ ] Created     | N/A       |
| `GlobalTimeCorrectionProps`                         | [ ] Created     | N/A       |
| `GlobalTimeCanMaster`                               | [ ] Created     | N/A       |
| `GlobalTimeCanSlave`                                | [ ] Created     | N/A       |
| `CanGlobalTimeDomainProps`                          | [ ] Created     | N/A       |
| `GlobalTimeEthMaster`                               | [ ] Created     | N/A       |
| `EthTSynSubTlvConfig`                               | [ ] Created     | N/A       |
| `GlobalTimeEthSlave`                                | [ ] Created     | N/A       |
| `EthGlobalTimeDomainProps`                          | [ ] Created     | N/A       |
| `EthTSynCrcFlags`                                   | [ ] Created     | N/A       |
| `EthGlobalTimeMessageFormatEnum`                    | [ ] Created     | N/A       |
| `EthGlobalTimeManagedCouplingPort`                  | [ ] Created     | N/A       |
| `GlobalTimeCouplingPortProps`                       | [ ] Implemented | N/A       |
| `GlobalTimePortRoleEnum`                            | [ ] Created     | N/A       |
| `GlobalTimeFrMaster`                                | [ ] Created     | N/A       |
| `GlobalTimeFrSlave`                                 | [ ] Created     | N/A       |
| `FrGlobalTimeDomainProps`                           | [ ] Created     | N/A       |
| `UserDefinedGlobalTimeMaster`                       | [ ] Created     | N/A       |
| `UserDefinedGlobalTimeSlave`                        | [ ] Created     | N/A       |
| `GlobalTimeCrcSupportEnum`                          | [ ] Created     | N/A       |
| `GlobalTimeCrcValidationEnum`                       | [ ] Created     | N/A       |
| `GlobalTimeIcvSupportEnum`                          | [ ] Created     | N/A       |
| `GlobalTimeIcvVerificationEnum`                     | [ ] Created     | N/A       |
| `CpSoftwareClusterResourcePool`                     | [ ] Created     | N/A       |
| `CpSoftwareClusterCommunicationResource`            | [ ] Created     | N/A       |
| `CpSoftwareClusterCommunicationResourceProps`       | [ ] Created     | N/A       |
| `DataComProps`                                      | [ ] Created     | N/A       |
| `DataConsistencyPolicyEnum`                         | [ ] Created     | N/A       |
| `ClientServerOperationComProps`                     | [ ] Created     | N/A       |
| `SendIndicationEnum`                                | [ ] Created     | N/A       |
| `CpSoftwareClusterServiceResource`                  | [ ] Created     | N/A       |
| `PortElementToCommunicationResourceMapping`         | [ ] Created     | N/A       |
| `CpSoftwareClusterToResourceMapping`                | [ ] Created     | N/A       |
| `CpSoftwareClusterBinaryManifestDescriptor`         | [ ] Created     | N/A       |
| `BinaryManifestProvideResource`                     | [ ] Created     | N/A       |
| `BinaryManifestResource`                            | [ ] Created     | N/A       |
| `BinaryManifestRequireResource`                     | [ ] Created     | N/A       |
| `BinaryManifestResourceDefinition`                  | [ ] Created     | N/A       |
| `BinaryManifestItem`                                | [ ] Created     | N/A       |
| `BinaryManifestItemDefinition`                      | [ ] Created     | N/A       |
| `BinaryManifestAddressableObject`                   | [ ] Created     | N/A       |
| `BinaryManifestItemValue`                           | [ ] Created     | N/A       |
| `BinaryManifestItemNumericalValue`                  | [ ] Created     | N/A       |
| `BinaryManifestItemPointerValue`                    | [ ] Created     | N/A       |

## Group35

Status: **0/75** completed

| Class Name                             | Status          | Commit ID |
| -------------------------------------- | --------------- | --------- |
| `BinaryManifestMetaDataField`          | [ ] Created     | N/A       |
| `VfbTiming`                            | [ ] Created     | N/A       |
| `SwcTiming`                            | [ ] Implemented | N/A       |
| `SystemTiming`                         | [ ] Created     | N/A       |
| `BswModuleTiming`                      | [ ] Created     | N/A       |
| `BswCompositionTiming`                 | [ ] Created     | N/A       |
| `EcuTiming`                            | [ ] Created     | N/A       |
| `TimingCondition`                      | [ ] Implemented | N/A       |
| `TimingConditionFormula`               | [ ] Implemented | N/A       |
| `TimingExtensionResource`              | [ ] Implemented | N/A       |
| `TimingModeInstance`                   | [ ] Implemented | N/A       |
| `ModeInBswInstanceRef`                 | [ ] Implemented | N/A       |
| `TDEventVfbReference`                  | [ ] Implemented | N/A       |
| `TDEventVfbPort`                       | [ ] Implemented | N/A       |
| `TDEventVariableDataPrototype`         | [ ] Implemented | N/A       |
| `TDEventVariableDataPrototypeTypeEnum` | [ ] Implemented | N/A       |
| `TDEventOperation`                     | [ ] Implemented | N/A       |
| `TDEventOperationTypeEnum`             | [ ] Implemented | N/A       |
| `TDEventModeDeclaration`               | [ ] Implemented | N/A       |
| `TDEventModeDeclarationTypeEnum`       | [ ] Implemented | N/A       |
| `TDEventTrigger`                       | [ ] Implemented | N/A       |
| `TDEventTriggerTypeEnum`               | [ ] Implemented | N/A       |
| `TDEventSwc`                           | [ ] Implemented | N/A       |
| `TDEventSwcInternalBehavior`           | [ ] Implemented | N/A       |
| `TDEventSwcInternalBehaviorTypeEnum`   | [ ] Implemented | N/A       |
| `TDEventSwcInternalBehaviorReference`  | [ ] Implemented | N/A       |
| `TDEventCom`                           | [ ] Implemented | N/A       |
| `TDEventISignal`                       | [ ] Implemented | N/A       |
| `TDEventISignalTypeEnum`               | [ ] Implemented | N/A       |
| `TDEventIPdu`                          | [ ] Implemented | N/A       |
| `TDEventIPduTypeEnum`                  | [ ] Implemented | N/A       |
| `TDEventFrame`                         | [ ] Implemented | N/A       |
| `TDEventFrameTypeEnum`                 | [ ] Implemented | N/A       |
| `TDEventFrameEthernet`                 | [ ] Implemented | N/A       |
| `TDEventFrameEthernetTypeEnum`         | [ ] Implemented | N/A       |
| `TDHeaderIdRange`                      | [ ] Implemented | N/A       |
| `TDEventCycleStart`                    | [ ] Implemented | N/A       |
| `TDEventFrClusterCycleStart`           | [ ] Implemented | N/A       |
| `TDEventTTCanCycleStart`               | [ ] Implemented | N/A       |
| `TDEventBswInternalBehavior`           | [ ] Implemented | N/A       |
| `TDEventBswInternalBehaviorTypeEnum`   | [ ] Implemented | N/A       |
| `TDEventBswModule`                     | [ ] Implemented | N/A       |
| `TDEventBswModuleTypeEnum`             | [ ] Implemented | N/A       |
| `TDEventBswModeDeclaration`            | [ ] Implemented | N/A       |
| `TDEventBswModeDeclarationTypeEnum`    | [ ] Implemented | N/A       |
| `TDEventComplex`                       | [ ] Implemented | N/A       |
| `TDEventSLLETPort`                     | [ ] Implemented | N/A       |
| `TDEventOccurrenceExpression`          | [ ] Implemented | N/A       |
| `TDEventOccurrenceExpressionFormula`   | [ ] Implemented | N/A       |
| `AutosarVariableInstance`              | [ ] Implemented | N/A       |
| `SynchronizationTypeEnum`              | [ ] Implemented | N/A       |
| `EventOccurrenceKindEnum`              | [ ] Implemented | N/A       |
| `LatencyTimingConstraint`              | [ ] Implemented | N/A       |
| `LatencyConstraintTypeEnum`            | [ ] Implemented | N/A       |
| `EventTriggeringConstraint`            | [ ] Implemented | N/A       |
| `PeriodicEventTriggering`              | [ ] Implemented | N/A       |
| `SporadicEventTriggering`              | [ ] Implemented | N/A       |
| `ConcretePatternEventTriggering`       | [ ] Implemented | N/A       |
| `BurstPatternEventTriggering`          | [ ] Implemented | N/A       |
| `ArbitraryEventTriggering`             | [ ] Implemented | N/A       |
| `ConfidenceInterval`                   | [ ] Implemented | N/A       |
| `AgeConstraint`                        | [ ] Implemented | N/A       |
| `ExecutionOrderConstraint`             | [ ] Implemented | N/A       |
| `ExecutionOrderConstraintTypeEnum`     | [ ] Implemented | N/A       |
| `EOCExecutableEntityRefAbstract`       | [ ] Implemented | N/A       |
| `EOCExecutableEntityRefGroup`          | [ ] Implemented | N/A       |
| `EOCExecutableEntityRef`               | [ ] Implemented | N/A       |
| `EOCEventRef`                          | [ ] Implemented | N/A       |
| `ExecutionTimeConstraint`              | [ ] Implemented | N/A       |
| `ExecutionTimeTypeEnum`                | [ ] Implemented | N/A       |
| `SynchronizationPointConstraint`       | [ ] Implemented | N/A       |
| `LetDataExchangeParadigmEnum`          | [ ] Implemented | N/A       |
| `TDCpSoftwareClusterMappingSet`        | [ ] Created     | N/A       |
| `TDCpSoftwareClusterMapping`           | [ ] Created     | N/A       |
| `TDCpSoftwareClusterResourceMapping`   | [ ] Created     | N/A       |

## Group36

Status: **0/73** completed

| Class Name                                     | Status          | Commit ID |
| ---------------------------------------------- | --------------- | --------- |
| `ApplicationInterface`                         | [ ] Implemented | N/A       |
| `FMFeatureModel`                               | [ ] Created     | N/A       |
| `FMFeature`                                    | [ ] Created     | N/A       |
| `FMAttributeDef`                               | [ ] Created     | N/A       |
| `FMFeatureDecomposition`                       | [ ] Created     | N/A       |
| `FMFeatureRestriction`                         | [ ] Created     | N/A       |
| `FMFeatureRelation`                            | [ ] Created     | N/A       |
| `FMFeatureSelection`                           | [ ] Created     | N/A       |
| `FMFeatureSelectionState`                      | [ ] Created     | N/A       |
| `FMAttributeValue`                             | [ ] Created     | N/A       |
| `FMFeatureSelectionSet`                        | [ ] Created     | N/A       |
| `FMFeatureMap`                                 | [ ] Created     | N/A       |
| `FMFeatureMapElement`                          | [ ] Created     | N/A       |
| `FMFeatureMapCondition`                        | [ ] Created     | N/A       |
| `FMFeatureMapAssertion`                        | [ ] Created     | N/A       |
| `SwSystemconstantValueSet`                     | [ ] Implemented | N/A       |
| `PostBuildVariantCriterionValueSet`            | [ ] Created     | N/A       |
| `LogAndTraceMessageCollectionSet`              | [ ] Created     | N/A       |
| `IdsDesign`                                    | [ ] Created     | N/A       |
| `SecurityEventDefinition`                      | [ ] Created     | N/A       |
| `SecurityEventFilterChain`                     | [ ] Created     | N/A       |
| `AbstractSecurityEventFilter`                  | [ ] Created     | N/A       |
| `SecurityEventStateFilter`                     | [ ] Created     | N/A       |
| `SecurityEventOneEveryNFilter`                 | [ ] Created     | N/A       |
| `SecurityEventAggregationFilter`               | [ ] Created     | N/A       |
| `SecurityEventContextDataSourceEnum`           | [ ] Created     | N/A       |
| `SecurityEventThresholdFilter`                 | [ ] Created     | N/A       |
| `IdsmRateLimitation`                           | [ ] Created     | N/A       |
| `IdsmTrafficLimitation`                        | [ ] Created     | N/A       |
| `SecurityEventContextMapping`                  | [ ] Created     | N/A       |
| `SecurityEventContextProps`                    | [ ] Created     | N/A       |
| `SecurityEventReportingModeEnum`               | [ ] Created     | N/A       |
| `SecurityEventContextMappingBswModule`         | [ ] Created     | N/A       |
| `SecurityEventContextMappingFunctionalCluster` | [ ] Created     | N/A       |
| `SecurityEventContextMappingCommConnector`     | [ ] Created     | N/A       |
| `SecurityEventContextMappingApplication`       | [ ] Created     | N/A       |
| `IdsmInstance`                                 | [ ] Created     | N/A       |
| `BlockState`                                   | [ ] Created     | N/A       |
| `ClientServerOperationBlueprintMapping`        | [ ] Created     | N/A       |
| `DataExchangePoint`                            | [ ] Created     | N/A       |
| `Baseline`                                     | [ ] Created     | N/A       |
| `DataExchangePointKind`                        | [ ] Created     | N/A       |
| `SpecElementReference`                         | [ ] Created     | N/A       |
| `SpecElementScope`                             | [ ] Created     | N/A       |
| `RestrictionWithSeverity`                      | [ ] Created     | N/A       |
| `SeverityEnum`                                 | [ ] Created     | N/A       |
| `ValueRestrictionWithSeverity`                 | [ ] Created     | N/A       |
| `MultiplicityRestrictionWithSeverity`          | [ ] Created     | N/A       |
| `AbstractMultiplicityRestriction`              | [ ] Created     | N/A       |
| `VariationRestrictionWithSeverity`             | [ ] Created     | N/A       |
| `DataFormatElementReference`                   | [ ] Created     | N/A       |
| `DataFormatElementScope`                       | [ ] Created     | N/A       |
| `SpecificationScope`                           | [ ] Created     | N/A       |
| `SpecificationDocumentScope`                   | [ ] Created     | N/A       |
| `DocumentElementScope`                         | [ ] Created     | N/A       |
| `AbstractClassTailoring`                       | [ ] Created     | N/A       |
| `AbstractCondition`                            | [ ] Created     | N/A       |
| `AggregationCondition`                         | [ ] Created     | N/A       |
| `AttributeCondition`                           | [ ] Created     | N/A       |
| `ClassTailoring`                               | [ ] Created     | N/A       |
| `ClassContentConditional`                      | [ ] Created     | N/A       |
| `ConcreteClassTailoring`                       | [ ] Created     | N/A       |
| `InvertCondition`                              | [ ] Created     | N/A       |
| `PrimitiveAttributeCondition`                  | [ ] Created     | N/A       |
| `ReferenceCondition`                           | [ ] Created     | N/A       |
| `TextualCondition`                             | [ ] Created     | N/A       |
| `AttributeTailoring`                           | [ ] Created     | N/A       |
| `PrimitiveAttributeTailoring`                  | [ ] Created     | N/A       |
| `DefaultValueApplicationStrategyEnum`          | [ ] Created     | N/A       |
| `AggregationTailoring`                         | [ ] Created     | N/A       |
| `ReferenceTailoring`                           | [ ] Created     | N/A       |
| `ConstraintTailoring`                          | [ ] Created     | N/A       |
| `SdgTailoring`                                 | [ ] Created     | N/A       |
