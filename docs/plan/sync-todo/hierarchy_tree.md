# Sync-todo class hierarchy tree (names only, source-tagged)

Generated 2026-09-26 from the spec-table Base rows of every queue row in Group1-20 (parent-dependency
audit; same-table identity extraction, ancestor closure to ARObject). ONE occurrence per class: each
class hangs from its most-derived spec parent (first non-infrastructure Base entry in the table's
displayed order; heritage-chain classes nest under ARElement). Additional spec parents (multiple
inheritance) are annotated inline as `+ Parent` on the same node — they are real inheritance edges,
not rendered as duplicate subtrees.

Source tag on every node — where the class's own spec table lives:
  (R23-11)  table found in the R23-11 corpus (CP_TPS / FO_TPS markdown)
  (R4.3.1)  no R23-11 table — synced/queued from the R4.3.1 corpus (pre-split naming)
  (XSD)     no table in EITHER corpus — class exists only in the XSD (AUTOSAR_00052.xsd / 00044.xsd)
             (override: ARList's table exists under the class name "List" — tagged R23-11)

Excluded: AtpMixedString / VariationPointCapable (interface mixins), PrimitiveTypes leaf types,
UploadableDesignElement / UploadablePackageElement (most-derived-base-collapse precedent), the ARObject
edge itself. Queued classes with no extractable Base row (AREnum leaves, XSD-only classes) attach to
the root. Subclasses mentioned only in table Subclasses rows (never queued) are not nodes.

```
ARObject
├─ AbstractCanCommunicationControllerAttributes (R23-11)
│  ├─ CanControllerConfiguration (R23-11)
│  └─ CanControllerConfigurationRequirements (R23-11)
├─ ApiPrincipleEnum (R23-11)
├─ ARList (R23-11)
├─ ArrayImplPolicyEnum (R23-11)
├─ AsamRecordLayoutSemantics (R23-11)
├─ AtpBlueprintMapping (R23-11)
│  └─ BlueprintMapping (R23-11)
├─ AtpInstanceRef (R23-11)
│  ├─ ModeGroupInAtomicSwcInstanceRef (R23-11)
│  ├─ ModeInSwcInstanceRef (R23-11)  + ModeInSwcBswInstanceRef
│  ├─ OperationInAtomicSwcInstanceRef (R23-11)
│  ├─ PModeGroupInAtomicSwcInstanceRef (R23-11)  + ModeGroupInAtomicSwcInstanceRef
│  ├─ POperationInAtomicSwcInstanceRef (R23-11)  + OperationInAtomicSwcInstanceRef
│  ├─ PPortInCompositionInstanceRef (R23-11)  + PortInCompositionTypeInstanceRef
│  ├─ PTriggerInAtomicSwcTypeInstanceRef (R23-11)  + TriggerInAtomicSwcInstanceRef
│  ├─ RModeGroupInAtomicSWCInstanceRef (R23-11)  + ModeGroupInAtomicSwcInstanceRef
│  ├─ RModeInAtomicSwcInstanceRef (R23-11)
│  ├─ ROperationInAtomicSwcInstanceRef (R23-11)  + OperationInAtomicSwcInstanceRef
│  ├─ RPortInCompositionInstanceRef (R23-11)  + PortInCompositionTypeInstanceRef
│  ├─ RVariableInAtomicSwcInstanceRef (R23-11)  + VariableInAtomicSwcInstanceRef
│  └─ TriggerInAtomicSwcInstanceRef (R23-11)
├─ AutosarParameterRef (R23-11)
├─ AutosarVariableRef (R23-11)
├─ BindingTimeEnum (R23-11)
├─ BlueprintGenerator (R23-11)
├─ BswApiOptions (XSD)
│  ├─ BswDataReceptionPolicy (R23-11)
│  └─ BswQueuedDataReceptionPolicy (R23-11)  + BswDataReceptionPolicy
├─ BswEntryRelationshipEnum (R23-11)
├─ BswModeSwitchAckRequest (R23-11)
├─ BuildActionIoElement (R23-11)
├─ CanClusterBusOffRecovery (R23-11)
├─ CanControllerFdConfigurationRequirements (R23-11)
├─ ChapterContent (R23-11)
├─ ChapterModel (R23-11)
├─ ClientIdRange (R23-11)
├─ ClientServerApplicationErrorMapping (R23-11)
├─ ClientServerOperationMapping (R23-11)
├─ CommunicationDirectionType (R23-11)
├─ CompositeNetworkRepresentation (R23-11)
├─ ConcreteTDEventVfb (XSD)
├─ ConfigReferenceValue (XSD)
├─ ContainedIPduCollectionSemanticsEnum (R23-11)
├─ CouplingPortAbstractShaper (XSD)
├─ CryptoKeySlotAllowedModification (XSD)
├─ CryptoKeySlotContentAllowedUsage (XSD)
├─ CryptoKeySlotTypeEnum (XSD)
├─ CryptoObjectTypeEnum (XSD)
├─ DataFilter (R23-11)
├─ DataFilterTypeEnum (R23-11)
├─ DataLinkLayerRule (XSD)
├─ DataMapping (R23-11)
│  ├─ SenderReceiverToSignalGroupMapping (R23-11)
│  └─ SenderReceiverToSignalMapping (R23-11)
├─ DataPrototypeTransformationProps (R23-11)
├─ DataTypeMap (R23-11)
├─ DefaultValueElement (R23-11)
├─ DependencyUsageEnum (R23-11)
├─ Describable (R23-11)
│  ├─ CyclicTiming (R23-11)
│  ├─ EndToEndTransformationISignalProps (R23-11)  + TransformationISignalProps
│  └─ EventControlledTiming (R23-11)
├─ DiagnosticAudienceEnum (R23-11)
├─ DiagnosticClearDtcNotificationEnum (R23-11)
├─ DiagnosticEnvConditionFormulaPart (R23-11)
│  ├─ DiagnosticEnvCompareCondition (R23-11)
│  └─ DiagnosticEnvConditionFormula (R23-11)
├─ DiagnosticJumpToBootLoaderEnum (R23-11)
├─ DiagnosticLogicalOperatorEnum (R23-11)
├─ DiagnosticProcessingStyleEnum (R23-11)
├─ DiagnosticRoutineTypeEnum (R23-11)
├─ DiagnosticServiceRequestCallbackTypeEnum (R23-11)
├─ DiagnosticValueAccessEnum (R23-11)
├─ DocumentViewSelectable (R23-11)
│  └─ Item (R23-11)  + Paginateable
├─ DoIpEntity (R23-11)
├─ DoIpRule (XSD)
├─ DtcFormatTypeEnum (R4.3.1)
├─ DtcKindEnum (R4.3.1)
├─ EcucConfigurationClassEnum (R23-11)
├─ EcucDestinationUriDefRefType (XSD)
├─ EcucQueryExpression (R23-11)
├─ EcucScopeEnum (R23-11)
├─ EndToEndDescription (R23-11)
├─ EndToEndProtectionISignalIPdu (R23-11)
├─ FirewallActionEnum (XSD)
├─ FlexrayChannelName (R23-11)
├─ FormulaExpression (R23-11)
│  ├─ AttributeValueVariationPoint (R23-11)  + SwSystemconstDependentFormula
│  │  ├─ AbstractEnumerationValueVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  │  ├─ AbstractNumericalVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  │  │  ├─ LimitValueVariationPoint (R23-11)  + AttributeValueVariationPoint, FormulaExpression, SwSystemconstDependentFormula
│  │  │  └─ NumericalValueVariationPoint (R23-11)  + AttributeValueVariationPoint, FormulaExpression, SwSystemconstDependentFormula
│  │  ├─ BooleanValueVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  │  ├─ FloatValueVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  │  ├─ IntegerValueVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  │  ├─ PositiveIntegerValueVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  │  ├─ TimeValueValueVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  │  └─ UnlimitedIntegerValueVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  ├─ BlueprintFormula (R23-11)  + SwSystemconstDependentFormula
│  ├─ CompuGenericMath (R23-11)
│  ├─ ConditionByFormula (R23-11)  + SwSystemconstDependentFormula
│  ├─ EcucConditionFormula (R23-11)
│  ├─ EcucParameterDerivationFormula (R23-11)
│  ├─ FMFormulaByFeaturesAndAttributes (R23-11)
│  │  └─ FMConditionByFeaturesAndAttributes (R23-11)  + FormulaExpression
│  ├─ FMFormulaByFeaturesAndSwSystemconsts (R23-11)  + SwSystemconstDependentFormula
│  │  └─ FMConditionByFeaturesAndSwSystemconsts (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  └─ SwSystemconstDependentFormula (R23-11)
├─ FrameMapping (R23-11)
├─ HardwareConfiguration (R23-11)
├─ IndexedArrayElement (R23-11)
├─ InitialSdDelayConfig (R23-11)
├─ InstantiationDataDefProps (R23-11)
├─ IpAddressKeepEnum (R23-11)
├─ Ipv6AddressSourceEnum (R23-11)
├─ ISignalMapping (R23-11)
├─ LanguageSpecific (R23-11)
│  ├─ LOverviewParagraph (R23-11)  + MixedContentForOverviewParagraph
│  ├─ LPlainText (R23-11)  + MixedContentForPlainText, WhitespaceControlled
│  └─ LVerbatim (R23-11)  + MixedContentForVerbatim, WhitespaceControlled
├─ LifeCyclePeriod (R23-11)
├─ ListEnum (R23-11)
├─ MixedContentForOverviewParagraph (R23-11)
│  └─ SlOverviewParagraph (R23-11)
├─ MixedContentForUnitNames (R23-11)
│  └─ SingleLanguageUnitNames (R23-11)
├─ ModeAccessPoint (R23-11)
├─ ModeActivationKind (R23-11)
├─ ModeDeclarationGroupPrototypeMapping (R23-11)
├─ ModeInSwcBswInstanceRef (XSD)
├─ ModeRequestTypeMap (R23-11)
├─ ModeSwitchedAckRequest (R23-11)
├─ ModeSwitchEventTriggeredActivity (R23-11)
├─ Modification (R23-11)
├─ ModuleConfiguration (XSD)
├─ MultidimensionalTime (R23-11)
├─ MultiplexedPart (R23-11)
│  └─ DynamicPart (R23-11)
├─ NetworkEndpointAddress (R23-11)
│  └─ Ipv4Configuration (R23-11)
├─ NetworkLayerRule (XSD)
├─ NmClusterCoupling (R23-11)
│  ├─ CanNmClusterCoupling (R23-11)
│  ├─ FlexrayNmClusterCoupling (R23-11)
│  └─ UdpNmClusterCoupling (R23-11)
├─ NvBlockDataMapping (R23-11)
├─ NvBlockNeedsReliabilityEnum (R23-11)
├─ NvBlockNeedsWritingPriorityEnum (R23-11)
├─ OrderedMaster (R23-11)
├─ PayloadBytePatternRule (XSD)
├─ PncGatewayTypeEnum (R23-11)
├─ PostBuildVariantCondition (R23-11)
├─ PostBuildVariantCriterionValue (R23-11)
├─ PPortComSpec (R23-11)
│  ├─ ModeSwitchSenderComSpec (R23-11)
│  └─ NvProvideComSpec (R23-11)
├─ RamBlockStatusControlEnum (R23-11)
├─ ReceptionComSpecProps (R23-11)
├─ RecordLayoutIteratorPoint (R23-11)
├─ ReentrancyLevelEnum (R23-11)
├─ Referrable (R23-11)
│  ├─ AbstractEvent (R23-11)  + Identifiable, MultilanguageReferrable
│  │  ├─ AsynchronousServerCallReturnsEvent (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, RTEEvent, Referrable
│  │  ├─ BswAsynchronousServerCallReturnsEvent (R23-11)  + BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ BswDataReceivedEvent (R23-11)  + BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ BswInternalTriggerOccurredEvent (R23-11)  + BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ BswModeManagerErrorEvent (R23-11)  + BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ BswModeSwitchedAckEvent (R23-11)  + BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ BswTimingEvent (R23-11)  + BswEvent, BswScheduleEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ DataReceivedEvent (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, RTEEvent, Referrable
│  │  ├─ DataReceiveErrorEvent (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, RTEEvent, Referrable
│  │  ├─ DataSendCompletedEvent (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, RTEEvent, Referrable
│  │  ├─ DataWriteCompletedEvent (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, RTEEvent, Referrable
│  │  ├─ InternalTriggerOccurredEvent (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, RTEEvent, Referrable
│  │  └─ OperationInvokedEvent (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, RTEEvent, Referrable
│  ├─ ApplicationPartitionToEcuPartitionMapping (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ AppOsTaskProxyToEcuTaskProxyMapping (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ AtpBlueprint (R23-11)  + Identifiable, MultilanguageReferrable
│  │  ├─ AtomicSwComponentType (R23-11)  + ARElement, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, SwComponentType
│  │  │  └─ ServiceProxySwComponentType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, SwComponentType
│  │  ├─ BswEntryRelationship (R23-11)  + ARElement, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  ├─ BswEntryRelationshipSet (R23-11)  + ARElement, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  ├─ ClientServerInterfaceMapping (R23-11)  + AtpBlueprintable, Identifiable, MultilanguageReferrable, PortInterfaceMapping, Referrable
│  │  ├─ ModeInterfaceMapping (R23-11)  + AtpBlueprintable, Identifiable, MultilanguageReferrable, PortInterfaceMapping, Referrable
│  │  └─ VariableAndParameterInterfaceMapping (R23-11)  + AtpBlueprintable, Identifiable, MultilanguageReferrable, PortInterfaceMapping, Referrable
│  ├─ AtpBlueprintable (R23-11)  + Identifiable, MultilanguageReferrable
│  │  ├─ AbstractProvidedPortPrototype (R23-11)  + AtpFeature, AtpPrototype, Identifiable, MultilanguageReferrable, PortPrototype, Referrable
│  │  └─ AbstractRequiredPortPrototype (R23-11)  + AtpFeature, AtpPrototype, Identifiable, MultilanguageReferrable, PortPrototype, Referrable
│  ├─ AtpClassifier (R23-11)  + Identifiable, MultilanguageReferrable
│  │  ├─ AbstractAccessPoint (R23-11)  + AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ InternalTriggeringPoint (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ ModeSwitchPoint (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ ParameterAccess (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  └─ VariableAccess (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ AbstractImplementationDataTypeElement (R23-11)  + AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  └─ ImplementationDataTypeElement (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ BulkNvDataDescriptor (R23-11)  + AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  └─ NvBlockDescriptor (R23-11)  + AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  ├─ AtpDefinition (R23-11)
│  │  ├─ EcucBooleanParamDef (R23-11)  + EcucCommonAttributes, EcucDefinitionElement, EcucParameterDef, Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ EcucFloatParamDef (R23-11)  + EcucCommonAttributes, EcucDefinitionElement, EcucParameterDef, Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ EcucForeignReferenceDef (R23-11)  + EcucAbstractExternalReferenceDef, EcucAbstractReferenceDef, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ EcucLinkerSymbolDef (R23-11)  + EcucAbstractStringParamDef, EcucCommonAttributes, EcucDefinitionElement, EcucParameterDef, Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ EcucReferenceDef (R23-11)  + EcucAbstractInternalReferenceDef, EcucAbstractReferenceDef, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ EcucSymbolicNameReferenceDef (R4.3.1)  + EcucAbstractInternalReferenceDef, EcucAbstractReferenceDef, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ EcucUriReferenceDef (R23-11)  + EcucAbstractInternalReferenceDef, EcucAbstractReferenceDef, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ PostBuildVariantCriterion (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  └─ SwSystemconst (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  ├─ AtpFeature (R23-11)  + Identifiable, MultilanguageReferrable
│  │  └─ Field (R23-11)  + AtpPrototype, AutosarDataPrototype, DataPrototype, Identifiable, MultilanguageReferrable, Referrable
│  ├─ AutosarOperationArgumentInstance (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ BswInternalTriggeringPoint (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ BswModuleCallPoint (R23-11)
│  │  ├─ BswDirectCallPoint (R23-11)  + Referrable
│  │  └─ BswSynchronousServerCallPoint (R23-11)  + Referrable
│  ├─ BswModuleClientServerEntry (R23-11)
│  ├─ BswModuleDependency (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ CommConnectorPort (R23-11)  + Identifiable, MultilanguageReferrable
│  │  └─ ISignalPort (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  ├─ CommunicationConnector (R23-11)  + Identifiable, MultilanguageReferrable
│  │  ├─ CanCommunicationConnector (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ FlexrayCommunicationConnector (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  └─ LinCommunicationConnector (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  ├─ CommunicationController (R23-11)  + Identifiable, MultilanguageReferrable
│  │  └─ FlexrayCommunicationController (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  ├─ ConstantSpecification (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement
│  ├─ CryptoServiceMapping (R23-11)  + Identifiable, MultilanguageReferrable
│  │  └─ SecOcCryptoServiceMapping (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  ├─ DiagEventDebounceAlgorithm (R23-11)  + Identifiable, MultilanguageReferrable
│  │  └─ DiagEventDebounceCounterBased (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  ├─ DiagnosticCommonElement (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement
│  │  ├─ DiagnosticAccessPermission (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  └─ DiagnosticServiceClass (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  ├─ DiagnosticEnvModeElement (R23-11)
│  ├─ DltApplication (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ DltArgument (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ DltContext (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement
│  ├─ DltLogChannel (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ DoIpLogicAddress (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ EcucValueCollection (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement
│  ├─ EthernetPriorityRegeneration (R23-11)
│  ├─ ExecutableEntity (R23-11)  + Identifiable, MultilanguageReferrable
│  │  └─ BswModuleEntity (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │     └─ BswInterruptEntity (R23-11)  + ExecutableEntity, Identifiable, MultilanguageReferrable, Referrable
│  ├─ FibexElement (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement
│  │  ├─ Gateway (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  ├─ ISignalIPduGroup (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  ├─ MultiplexedIPdu (R23-11)  + ARElement, CollectableElement, IPdu, Identifiable, MultilanguageReferrable, PackageableElement, Pdu, Referrable
│  │  ├─ SecuredIPdu (R23-11)  + ARElement, CollectableElement, IPdu, Identifiable, MultilanguageReferrable, PackageableElement, Pdu, Referrable
│  │  ├─ SoAdRoutingGroup (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  ├─ UserDefinedIPdu (R23-11)  + ARElement, CollectableElement, IPdu, Identifiable, MultilanguageReferrable, PackageableElement, Pdu, Referrable
│  │  └─ UserDefinedPdu (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Pdu, Referrable
│  ├─ FrameTriggering (R23-11)  + Identifiable, MultilanguageReferrable
│  │  └─ FlexrayFrameTriggering (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  ├─ Implementation (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement
│  │  └─ SwcImplementation (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  ├─ ImplementationProps (R23-11)
│  │  └─ SectionNamePrefix (R23-11)  + Referrable
│  ├─ IPv6ExtHeaderFilterList (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ LifeCycleInfo (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement
│  ├─ LifeCycleInfoSet (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement
│  ├─ LinScheduleTable (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ MacMulticastGroup (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ MemorySection (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ NetworkEndpoint (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ NmCluster (R23-11)  + Identifiable, MultilanguageReferrable
│  │  ├─ CanNmCluster (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  └─ UdpNmCluster (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  ├─ NmEcu (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ NmNode (R23-11)  + Identifiable, MultilanguageReferrable
│  │  ├─ CanNmNode (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  └─ UdpNmNode (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  ├─ PhysicalChannel (R23-11)  + Identifiable, MultilanguageReferrable
│  │  └─ FlexrayPhysicalChannel (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  ├─ ServiceNeeds (R23-11)  + Identifiable, MultilanguageReferrable
│  │  ├─ CryptoServiceNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ DiagnosticCapabilityElement (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ DiagnosticCommunicationManagerNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  ├─ DiagnosticControlNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  ├─ DiagnosticEventInfoNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  ├─ DiagnosticEventManagerNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  ├─ DiagnosticRequestFileTransferNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  ├─ DiagnosticRoutineNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  ├─ DiagnosticValueNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  └─ DtcStatusChangeNotificationNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  ├─ DoIpServiceNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ DoIpActivationLineNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  ├─ DoIpGidNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  └─ DoIpGidSynchronizationNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  └─ NvBlockNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  ├─ SignalServiceTranslationElementProps (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ SocketConnectionBundle (R4.3.1)
│  ├─ StackUsage (R23-11)  + Identifiable, MultilanguageReferrable
│  │  ├─ MeasuredStackUsage (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  ├─ RoughEstimateStackUsage (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  └─ WorstCaseStackUsage (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  ├─ SwcToEcuMapping (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ SwcToImplMapping (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ SystemSignal (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement
│  ├─ TcpOptionFilterList (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ TcpOptionFilterSet (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement
│  ├─ TimeSyncServerConfiguration (R23-11)
│  ├─ TimingDescription (R23-11)  + Identifiable, MultilanguageReferrable
│  │  └─ TimingDescriptionEventChain (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  ├─ TpAddress (R23-11)  + Identifiable, MultilanguageReferrable
│  ├─ Traceable (R23-11)  + MultilanguageReferrable
│  │  └─ TimingConstraint (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │     ├─ OffsetTimingConstraint (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, Traceable
│  │     └─ SynchronizationTimingConstraint (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, Traceable
│  ├─ UnitGroup (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement
│  └─ VlanConfig (R23-11)  + Identifiable, MultilanguageReferrable
├─ RequestResponseDelay (R23-11)
├─ ResumePosition (R23-11)
├─ RoleBasedDataAssignment (R23-11)
├─ RoleBasedPortAssignment (R23-11)
├─ RPortComSpec (R23-11)
│  ├─ ModeSwitchReceiverComSpec (R23-11)
│  ├─ NvRequireComSpec (R23-11)
│  ├─ ParameterRequireComSpec (R23-11)
│  └─ QueuedReceiverComSpec (R23-11)  + ReceiverComSpec
├─ RteEventInEcuInstanceRef (XSD)
├─ RuntimeAddressConfigurationEnum (R4.3.1)
├─ ScaleConstrValidityEnum (R4.3.1)
├─ ScheduleTableEntry (R23-11)
│  └─ ApplicationEntry (R23-11)
├─ SdServerConfig (R4.3.1)
├─ SegmentPosition (R23-11)
├─ SenderRecCompositeTypeMapping (R23-11)
│  └─ SenderRecRecordTypeMapping (R23-11)
├─ SenderRecRecordElementMapping (R23-11)
├─ ServiceDiagnosticRelevanceEnum (R23-11)
├─ ShortNameFragment (R23-11)
├─ SocketConnectionIpduIdentifier (R4.3.1)
├─ SoftwareContext (R23-11)
├─ SomeipProtocolRule (XSD)
├─ SomeipSdRule (XSD)
├─ SwcBswRunnableMapping (R23-11)
├─ SwcBswSynchronizedModeGroupPrototype (R23-11)
├─ SwcBswSynchronizedTrigger (R23-11)
├─ SwImplPolicyEnum (R23-11)
├─ SwRecordLayoutGroup (R23-11)
├─ SwSystemconstValue (R23-11)
├─ TargetIPduRef (R23-11)
├─ TcpProps (R23-11)
├─ TimeRangeType (R23-11)
├─ TimeSynchronization (R23-11)
├─ TopicContentOrMsrQuery (R23-11)
├─ TpConnection (R23-11)
│  ├─ DoIpTpConnection (R23-11)
│  └─ LinTpConnection (R23-11)
├─ TpPort (R23-11)
├─ TransferPropertyEnum (R23-11)
├─ TransmissionModeCondition (R23-11)
├─ TransmissionModeDeclaration (R23-11)
├─ TransmissionModeTiming (R23-11)
├─ TransportLayerRule (XSD)
├─ TransportProtocolConfiguration (R23-11)
│  ├─ GenericTp (R23-11)
│  └─ TcpUdpConfig (R23-11)
│     ├─ TcpTp (R23-11)  + TransportProtocolConfiguration
│     └─ UdpTp (R23-11)  + TransportProtocolConfiguration
├─ TriggerIPduSendCondition (R23-11)
├─ ValueSpecification (R23-11)
│  ├─ ConstantReference (R23-11)
│  ├─ NumericalValueSpecification (R23-11)
│  └─ TextValueSpecification (R23-11)
├─ VariableAccessInEcuInstanceRef (XSD)
├─ VariationPoint (R23-11)
├─ WhitespaceControlled (R23-11)
│  ├─ MixedContentForPlainText (R23-11)
│  └─ MixedContentForVerbatim (R23-11)
└─ XmlSpaceEnum (XSD)
```
