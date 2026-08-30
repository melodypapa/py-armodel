# Sync Class Groups (dependency-ordered)

Batched class list for running `sync-autosar-class`, derived from
`docs/examples/method_deviation_by_class_v2.md` (outstanding deviations, 2026-08-30).
**185 tracker classes + 13 member classes missing from `src` (NEW) + 8 existing-but-unstamped
member classes = 206 entries in 7 groups of 20–30.**

## Usage

- One class per `sync-autosar-class` invocation; Phase 1 is one class per fresh session
  (Rule 0017.1). A "group" is one batch of sessions — work through it top to bottom.
- **Order matters**: member-type classes are listed before the classes that reference them.
  Missing member classes (`NEW`) must be created (skill Rule 0016.4: Derive-from-XSD) before
  their parent is synced.
- Existing-but-unstamped member classes not listed here are auto-queued dependency-first by
  the skill's Phase 0 closure — no action needed.
- After a class is synced and stamped, tick its box here; the tracker section
  (`method_deviation_by_class_v2.md`) is then dropped (deviation-tracker convention).
- `CollectableElement` is intentionally NOT listed (internal helper, no AUTOSAR meta-class,
  no stamp — 2026-08-20 decision). Appendices of the tracker (no-spec-table classes, Rule 0007
  location audit) are informational only, not sync targets.

## Group 1 — Framework & core, PortInterface basics (29)

- [ ] `ARObject`
- [ ] `ARElement`
- [ ] `ARPackage`
- [ ] `AUTOSAR`
- [ ] `FileInfoComment`
- [ ] `Collection`
- [ ] `AtpType`
- [ ] `AtpPrototype`
- [ ] `AtpStructureElement`
- [ ] `AtpDefinition`
- [ ] `AtpBlueprintable`
- [ ] `AtpBlueprintMapping`
- [ ] `BlueprintMappingSet` — after `AtpBlueprintMapping` (aggr `blueprintMap`)
- [ ] `ApplicationDeferredDataType`
- [ ] `AbstractImplementationDataType`
- [ ] `AbstractImplementationDataTypeElement`
- [ ] `Implementation`
- [ ] `FlatMap`
- [ ] `ModeAccessPointIdent`
- [ ] `IdentCaption`
- [ ] `DataInterface`
- [ ] `NvDataInterface`
- [ ] `SenderReceiverInterface`
- [ ] `ParameterInterface`
- [ ] `TriggerInterface`
- [ ] `PortInterfaceMapping`
- [ ] `SubElementMapping`
- [ ] `TriggerInterfaceMapping`
- [ ] `ModeDeclarationMappingSet` — after `ModeDeclarationMapping` (auto-queued, exists)

## Group 2 — PortInterface sets, components, SWC behavior, datatypes (30)

- [ ] `PortInterfaceMappingSet` — after `PortInterfaceMapping` (Group 1)
- [ ] `MetaDataItemSet` — after `MetaDataItem` (auto-queued, exists)
- [ ] `ApplicationCompositeElementInPortInterfaceInstanceRef`
- [ ] `SymbolProps`
- [ ] `PPortPrototype`
- [ ] `RPortPrototype`
- [ ] `PRPortPrototype`
- [ ] `PortGroup`
- [ ] `InnerPortGroupInCompositionInstanceRef` — member type of `PortGroup.innerGroup`
- [ ] `VariableInAtomicSwcInstanceRef`
- [ ] `CompositionSwComponentType`
- [ ] `DelegationSwConnector`
- [ ] `SwcInternalBehavior`
- [ ] `ArVariableInImplementationDataInstanceRef`
- [ ] `VariableInAtomicSWCTypeInstanceRef`
- [ ] `IncludedModeDeclarationGroupSet`
- [ ] `RunnableEntityArgument`
- [ ] `AsynchronousServerCallPoint`
- [ ] `AsynchronousServerCallResultPoint` — ref target of the point class above
- [ ] `SynchronousServerCallPoint`
- [ ] `InitEvent`
- [ ] `BackgroundEvent`
- [ ] `ExternalTriggeringPointIdent`
- [ ] `PortDefinedArgumentValue` *(existing member)*
- [ ] `PortAPIOption` — after `PortDefinedArgumentValue` (aggr `portArgValue`)
- [ ] `ApplicationPrimitiveDataType`
- [ ] `ApplicationDataType`
- [ ] `ApplicationCompositeDataType`
- [ ] `ApplicationRecordElement` *(existing member)*
- [ ] `ApplicationRecordDataType` — after `ApplicationRecordElement` (aggr `element`)

## Group 3 — Constants, CompuMethod, DataDictionary, Documentation (29)

- [ ] `RecordValueSpecification`
- [ ] `ArrayValueSpecification`
- [ ] `CompositeValueSpecification`
- [ ] `CompositeRuleBasedValueArgument`
- [ ] `CompositeRuleBasedValueSpecification` — after `CompositeRuleBasedValueArgument` (aggr)
- [ ] `DataConstrRule`
- [ ] `CompuContent`
- [ ] `CompuConstContent`
- [ ] `CompuScaleContents`
- [ ] `CompuNominatorDenominator`
- [ ] `CompuScales` — after `CompuScale` (auto-queued, exists)
- [ ] `SwValueCont`
- [ ] `SwCalprmAxisSet`
- [ ] `SwAxisIndividual`
- [ ] `SwAxisGrouped`
- [ ] `SwRecordLayoutGroup`
- [ ] `SwRecordLayoutV`
- [ ] `GeneralAnnotation`
- [ ] `MultiLanguageParagraph`
- [ ] `Area` **(NEW)**
- [ ] `Map` — after `Area` (aggr `area`)
- [ ] `LGraphic` *(existing member)*
- [ ] `MlFigure` — after `LGraphic` (aggr `lGraphic`)
- [ ] `DocumentViewSelectable`
- [ ] `MsrQueryResultChapter` **(NEW)**
- [ ] `MsrQueryResultTopic1` **(NEW)**
- [ ] `MsrQueryChapter` — after `MsrQueryResultChapter` (aggr)
- [ ] `MsrQueryTopic1` — after `MsrQueryResultTopic1` (aggr)
- [ ] `MsrQueryP1`

## Group 4 — BSW behavior policies & ServiceNeeds A (29)

- [ ] `BswPerInstanceMemoryPolicy` **(NEW)**
- [ ] `BswClientPolicy` **(NEW)**
- [ ] `BswInternalTriggeringPointPolicy` **(NEW)**
- [ ] `BswParameterPolicy` **(NEW)**
- [ ] `BswReleasedTriggerPolicy` **(NEW)**
- [ ] `BswDataSendPolicy` **(NEW)**
- [ ] `BswInternalBehavior` — after all 6 NEW policy classes above (deferred full sync;
      sibling policy classes `BswModeSenderPolicy`/`BswModeReceiverPolicy`/
      `BswExclusiveAreaPolicy`/`BswDataReceptionPolicy`/`BswSchedulerNamePrefix`/
      `BswTriggerDirectImplementation` exist and are auto-queued first)
- [ ] `ServiceNeeds`
- [ ] `DiagEventDebounceAlgorithm`
- [ ] `DiagEventDebounceMonitorInternal`
- [ ] `EcuStateMgrUserNeeds`
- [ ] `DltUserNeeds`
- [ ] `DiagnosticComponentNeeds`
- [ ] `DiagnosticUploadDownloadNeeds`
- [ ] `DiagnosticsCommunicationSecurityNeeds`
- [ ] `FunctionInhibitionNeeds`
- [ ] `GlobalSupervisionNeeds`
- [ ] `HardwareTestNeeds`
- [ ] `SupervisedEntityCheckpointNeeds`
- [ ] `SyncTimeBaseMgrUserNeeds`
- [ ] `BswMgrNeeds`
- [ ] `CryptoKeyManagementNeeds`
- [ ] `CryptoServiceJobNeeds`
- [ ] `DiagnosticControlNeeds`
- [ ] `DiagnosticEventManagerNeeds`
- [ ] `DiagnosticRequestFileTransferNeeds`
- [ ] `DoIpActivationLineNeeds`
- [ ] `DoIpGidNeeds`
- [ ] `DoIpGidSynchronizationNeeds`

## Group 5 — ServiceNeeds B, SystemTemplate, Fibex core, SWC Communication & E2E (30)

- [ ] `DoIpPowerModeStatusNeeds`
- [ ] `FurtherActionByteNeeds`
- [ ] `IdsMgrCustomTimestampNeeds`
- [ ] `J1939DcmDm19Support`
- [ ] `J1939RmIncomingRequestServiceNeeds`
- [ ] `J1939RmOutgoingRequestServiceNeeds`
- [ ] `V2xDataManagerNeeds`
- [ ] `V2xFacUserNeeds`
- [ ] `V2xMUserNeeds`
- [ ] `VendorSpecificServiceNeeds`
- [ ] `WarningIndicatorRequestedBitNeeds`
- [ ] `System`
- [ ] `J1939SharedAddressCluster`
- [ ] `ComManagementMapping`
- [ ] `EcuInstance`
- [ ] `DiagnosticConnection`
- [ ] `EthernetPhysicalChannel`
- [ ] `FrameTriggering`
- [ ] `ContainedIPduProps`
- [ ] `ModeDrivenTransmissionModeCondition`
- [ ] `StaticPart`
- [ ] `DynamicPartAlternative`
- [ ] `GeneralPurposePdu`
- [ ] `GeneralPurposeIPdu`
- [ ] `CommunicationCycle`
- [ ] `FramePort`
- [ ] `QueuedSenderComSpec`
- [ ] `UserDefinedTransformationComSpecProps`
- [ ] `EndToEndProtectionVariablePrototype`
- [ ] `EndToEndProtectionSet` — after `EndToEndProtection` (auto-queued, exists)

## Group 6 — Ethernet/Flexray Fibex, SecureCommunication, Transformer, DataMapping, NM (30)

- [ ] `AbstractEthernetFrame`
- [ ] `GenericEthernetFrame`
- [ ] `CouplingPortStructuralElement`
- [ ] `CouplingPortScheduler`
- [ ] `VlanMembership`
- [ ] `NetworkEndpointAddress`
- [ ] `OrderedMaster` *(existing member)*
- [ ] `TimeSyncClientConfiguration` — after `OrderedMaster` (aggr `orderedMaster`)
- [ ] `TransportProtocolConfiguration`
- [ ] `TcpUdpConfig`
- [ ] `FlexrayFrame`
- [ ] `CryptoServiceMapping`
- [ ] `TlsCryptoServiceMapping`
- [ ] `DataTransformationSet` — after `DataTransformation`/`TransformationTechnology`
      (auto-queued, exist)
- [ ] `DataPrototypeTransformationProps` *(existing member)*
- [ ] `TransformationISignalProps` — after `DataPrototypeTransformationProps` (aggr)
- [ ] `SenderRecCompositeTypeMapping`
- [ ] `SenderRecArrayTypeMapping` — after `SenderRecArrayElementMapping`/`TextTableMapping`
      (auto-queued, exist)
- [ ] `NmClusterCoupling`
- [ ] `NmCluster`
- [ ] `FlexrayNmCluster`
- [ ] `FlexrayNmEcu`
- [ ] `FlexrayNmNode`
- [ ] `UdpNmEcu`
- [ ] `J1939NmCluster`
- [ ] `J1939NmEcu`
- [ ] `NmConfig` — after all NM classes above (aggrs `nmCluster`, `nmClusterCoupling`, `nmIfEcu`)
- [ ] `IPduMapping`
- [ ] `PduMappingDefaultValue`
- [ ] `RtePluginProps`

## Group 7 — ECU resource, Crypto/IDS, DoIP, Firewall, remaining (29)

- [ ] `HwAttributeDef` *(existing member)*
- [ ] `HwCategory` — after `HwAttributeDef` (aggr `hwAttributeDef`)
- [ ] `HwAttributeValue`
- [ ] `HwAttributeLiteralDef`
- [ ] `HwType`
- [ ] `CryptoKeySlot`
- [ ] `AbstractDoIpLogicAddressProps`
- [ ] `DoIpLogicTargetAddressProps`
- [ ] `DoIpLogicTesterAddressProps`
- [ ] `DoIpTpConfig` — after the DoIp props classes
- [ ] `FirewallActionEnum` **(NEW)**
- [ ] `FirewallRule` — after `FirewallActionEnum`
- [ ] `FirewallRuleProps` — after `FirewallRule` (refs `matchingEgressRule`/`matchingIngressRule`)
- [ ] `StateDependentFirewall` — after `FirewallRuleProps` (aggr `firewallRuleProps`)
- [ ] `IdsPlatformInstantiation`
- [ ] `IdsmModuleInstantiation`
- [ ] `PlatformModuleEthernetEndpointConfiguration`
- [ ] `CommunicationControllerMapping` **(NEW)**
- [ ] `HwPortMapping` **(NEW)**
- [ ] `ECUMapping` — after both NEW classes above (aggrs)
- [ ] `VariableDataPrototypeInSystemInstanceRef`
- [ ] `ComponentInSystemInstanceRef`
- [ ] `PortPrototypeBlueprintInitValue` *(existing member)*
- [ ] `PortPrototypeBlueprint` — after `PortPrototypeBlueprintInitValue` (aggr `initValue`)
- [ ] `Keyword` *(existing member)*
- [ ] `KeywordSet` — after `Keyword` (aggr `keyword`)
- [ ] `DiagnosticServiceInstance` **(NEW)**
- [ ] `DiagnosticServiceTable` — after `DiagnosticServiceInstance` (ref `serviceInstance`)
- [ ] `DiagnosticCommonElement`

## Progress

| Group | Entries | Tracker | NEW | Existing member | Done |
|---|---|---|---|---|---|
| 1 | 29 | 29 | 0 | 0 | 0/29 |
| 2 | 30 | 28 | 0 | 2 | 0/30 |
| 3 | 29 | 25 | 3 | 1 | 0/29 |
| 4 | 29 | 23 | 6 | 0 | 0/29 |
| 5 | 30 | 30 | 0 | 0 | 0/30 |
| 6 | 30 | 28 | 0 | 2 | 0/30 |
| 7 | 29 | 22 | 4 | 3 | 0/29 |
| **Total** | **206** | **185** | **13** | **8** | **0/206** |
