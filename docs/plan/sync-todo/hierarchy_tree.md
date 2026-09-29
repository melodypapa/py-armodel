# Sync-todo class hierarchy tree (names only, source-tagged)

Generated 2026-09-29 — V4 REGENERATION (v3 2026-09-28 plus: the Primitive/Enumeration leaves now modeled
in src by the Group21-36 stub pass, the 4 enums wrongly dropped as leaves, the R3.2.3-only Group19 trio,
and the ARList node renamed to its spec caption List — the · src: ARList alias annotation maps the
src-class name back onto the node, as both names are queued). Replaces the 2026-09-26 tree that covered only the
Base rows of Group1-20 queue rows. Source: every Class / Enumeration / Primitive spec table in
autosar/R23-11/markdown/ (15 CP_TPS / FO_TPS files), caption→table attribution by the table's own
Class header cell (handles the trailing-caption render used by appendix and reproduction tables),
same-table identity vote across reproductions, ancestor closure to ARObject. ONE occurrence per
class: each class hangs from its most-derived spec parent (deepest non-ancestor Base entry;
displayed-order first when several unrelated maxima remain). Additional Base entries are annotated
inline as `+ Parent` — real inheritance edges, not duplicate subtrees (ARObject omitted from
annotations; it is the root edge).

Source tag on every node — where the class's own spec table lives:
  (R23-11)  table found in the R23-11 corpus (CP_TPS / FO_TPS markdown)
  (R4.3.1)  no R23-11 table — synced/queued from the R4.3.1 corpus (pre-split naming); removed-in-R23-11
            classes that were never queued are NOT nodes
  (R3.2.3)  no R23-11 table — queued from the R3.2.3 corpus (ECU_Configuration); removed-in-R23-11
            classes kept because they are queued and modeled in src
  (XSD)     no table in EITHER corpus — class exists only in the XSD (AUTOSAR_00052.xsd); Base derived
            from the complexType group-composition chain (group → class via mmt.qualifiedName)

Excluded from nodes: AtpMixedString / VariationPointCapable (interface mixins), PrimitiveTypes leaf
types (src PrimitiveTypes.py + AsamHdo numeric leaves), UploadableDesignElement / UploadablePackageElement
(most-derived-base-collapse precedent), non-meta syntax-type tables (Primitive-kind tables still not modeled in
src after the Group21-36 stub pass — see prim_leaves bookkeeping), the ARObject root edge itself. Enumerations and classes
with no extractable Base row attach to the root. XSD-only classes whose class has only an abstract
group (no complexType) also attach to the root. The "List" spec table is represented by the src class name ARList in earlier trees; v4 uses the spec caption List.

```
ARObject
├─ AbstractCanClusterContent (XSD)
├─ AbstractCanCommunicationControllerAttributes (R23-11)
│  ├─ CanControllerConfiguration (R23-11)
│  └─ CanControllerConfigurationRequirements (R23-11)
├─ AbstractCanCommunicationControllerContent (XSD)
├─ AbstractCondition (R23-11)
│  ├─ AttributeCondition (R23-11)  + AbstractMultiplicityRestriction
│  │  ├─ AggregationCondition (R23-11)  + AbstractCondition, AbstractMultiplicityRestriction
│  │  ├─ PrimitiveAttributeCondition (R23-11)  + AbstractCondition, AbstractMultiplicityRestriction, AbstractValueRestriction
│  │  └─ ReferenceCondition (R23-11)  + AbstractCondition, AbstractMultiplicityRestriction
│  ├─ InvertCondition (R23-11)
│  └─ TextualCondition (R23-11)
├─ AbstractExecutionContext (XSD)
├─ AbstractGlobalTimeDomainProps (R23-11)
│  ├─ CanGlobalTimeDomainProps (R23-11)
│  ├─ EthGlobalTimeDomainProps (R23-11)
│  └─ FrGlobalTimeDomainProps (R23-11)
├─ AbstractIamRemoteSubject (XSD)
├─ AbstractMethodInExecutableInstanceRef (XSD)
├─ AbstractMultiplicityRestriction (R23-11)
│  └─ MultiplicityRestrictionWithSeverity (R23-11)  + RestrictionWithSeverity
├─ AbstractPortPrototypeInExecutableInstanceRef (XSD)
├─ AbstractPortPrototypeInSoftwareClusterDesignInstanceRef (XSD)
├─ AbstractRawDataStreamEthernetCredentials (XSD)
├─ AbstractRawDataStreamInterface (XSD)
├─ AbstractSecurityIdsmInstanceFilter (XSD)
├─ AbstractServiceInstance (R23-11)
├─ AbstractSignalBasedToISignalTriggeringMapping (XSD)
├─ AbstractSynchronizedTimeBaseInterface (XSD)
├─ AbstractValueRestriction (R23-11)
│  └─ ValueRestrictionWithSeverity (R23-11)  + RestrictionWithSeverity
├─ AbstractVariationRestriction (R23-11)
│  └─ VariationRestrictionWithSeverity (R23-11)  + RestrictionWithSeverity
├─ AccessControlEnum (XSD)
├─ AccessCount (R23-11)
├─ AccessCountSet (R23-11)
├─ AclScopeEnum (R23-11)
├─ AdaptiveModuleInstantiation (XSD)
├─ AdaptivePlatformServiceInstance (XSD)
├─ AdditionalBindingTimeEnum (R23-11)
├─ AdminData (R23-11)
├─ AliasNameAssignment (R23-11)
├─ AlignEnum (R23-11)
├─ AlignmentType (R23-11)
├─ ApiPrincipleEnum (R23-11)
├─ ApplicabilityInfo (XSD)
├─ ApplicationAssocMapElementValueSpecification (XSD)
├─ ApplicationEndpoint (R23-11)
├─ ApplicationErrorMapping (XSD)
├─ ArbitraryEventTriggering (R23-11)
├─ Area (R23-11)
├─ AreaEnumNohref (R23-11)
├─ AreaEnumShape (R23-11)
├─ ArgumentDirectionEnum (R23-11)
├─ ArParameterInImplementationDataInstanceRef (R23-11)
├─ ArrayImplPolicyEnum (R23-11)
├─ ArraySizeHandlingEnum (R23-11)
├─ ArraySizeSemanticsEnum (R23-11)
├─ ArVariableInImplementationDataInstanceRef (R23-11)
├─ AsamRecordLayoutSemantics (R23-11)
├─ AtpBlueprintMapping (R23-11)
│  ├─ BlueprintMapping (R23-11)
│  ├─ PortInterfaceBlueprintMapping (XSD)
│  └─ PortPrototypeBlueprintMapping (XSD)
├─ AtpFeature (R23-11)
├─ AtpInstanceRef (R23-11)
│  ├─ AnyInstanceRef (R23-11)
│  ├─ ApplicationCompositeElementInPortInterfaceInstanceRef (R23-11)
│  ├─ ApplicationDataPrototypeInSystemInstanceRef (XSD)
│  ├─ ComponentInCompositionInstanceRef (R23-11)
│  ├─ DataPrototypeInPortInterfaceInstanceRef (R23-11)
│  │  ├─ DataPrototypeInClientServerInterfaceInstanceRef (R23-11)  + AtpInstanceRef
│  │  ├─ DataPrototypeInSenderReceiverInterfaceInstanceRef (R23-11)  + AtpInstanceRef
│  │  └─ DataPrototypeInServiceInterfaceInstanceRef (XSD)  + AtpInstanceRef
│  ├─ DataPrototypeInSystemInstanceRef (R23-11)
│  ├─ EventInExecutableInstanceRef (XSD)  + AutosarDataPrototypeInExecutableInstanceRef
│  ├─ FieldInExecutableInstanceRef (XSD)  + AutosarDataPrototypeInExecutableInstanceRef
│  ├─ FirewallStateInFirwallStateSwitchInterfaceInstanceRef (XSD)
│  ├─ FunctionGroupStateInFunctionGroupSetInstanceRef (XSD)
│  ├─ InnerPortGroupInCompositionInstanceRef (R23-11)
│  ├─ InnerRunnableEntityGroupInCompositionInstanceRef (R23-11)
│  ├─ InstanceEventInCompositionInstanceRef (R23-11)
│  ├─ ModeDeclarationGroupPrototypeInExecutableInstanceRef (XSD)
│  ├─ ModeDeclarationGroupPrototypeInSystemInstanceRef (XSD)
│  ├─ ModeDeclarationInStateManagementStateNotificationInstanceRef (XSD)
│  ├─ ModeGroupInAtomicSwcInstanceRef (R23-11)
│  │  ├─ PModeGroupInAtomicSwcInstanceRef (R23-11)  + AtpInstanceRef
│  │  └─ RModeGroupInAtomicSWCInstanceRef (R23-11)  + AtpInstanceRef
│  ├─ ModeInBswModuleDescriptionInstanceRef (R23-11)
│  ├─ ModeInProcessInstanceRef (XSD)
│  ├─ OperationArgumentInComponentInstanceRef (XSD)
│  ├─ OperationInAtomicSwcInstanceRef (R23-11)
│  │  ├─ POperationInAtomicSwcInstanceRef (R23-11)  + AtpInstanceRef
│  │  └─ ROperationInAtomicSwcInstanceRef (R23-11)  + AtpInstanceRef
│  ├─ ParameterDataPrototypeInSystemInstanceRef (XSD)
│  ├─ ParameterInAtomicSWCTypeInstanceRef (R23-11)
│  ├─ PhmCheckpointInExecutableInstanceRef (XSD)
│  ├─ PModeInSystemInstanceRef (R23-11)
│  ├─ PortGroupInSystemInstanceRef (R23-11)
│  ├─ PortInCompositionTypeInstanceRef (R23-11)
│  │  ├─ PPortInCompositionInstanceRef (R23-11)  + AtpInstanceRef
│  │  └─ RPortInCompositionInstanceRef (R23-11)  + AtpInstanceRef
│  ├─ PortPrototypeInExecutableInstanceRef (XSD)  + AbstractPortPrototypeInExecutableInstanceRef
│  ├─ PPortPrototypeInExecutableInstanceRef (XSD)  + AbstractPortPrototypeInExecutableInstanceRef
│  ├─ PPortPrototypeInSoftwareClusterDesignInstanceRef (XSD)  + AbstractPortPrototypeInSoftwareClusterDesignInstanceRef
│  ├─ RequiredMethodInExecutableInstanceRef (XSD)  + AbstractMethodInExecutableInstanceRef
│  ├─ RModeInAtomicSwcInstanceRef (R23-11)
│  ├─ RPortPrototypeInExecutableInstanceRef (XSD)  + AbstractPortPrototypeInExecutableInstanceRef
│  ├─ RPortPrototypeInSoftwareClusterDesignInstanceRef (XSD)  + AbstractPortPrototypeInSoftwareClusterDesignInstanceRef
│  ├─ RteEventInCompositionInstanceRef (XSD)
│  ├─ RteEventInEcuInstanceRef (XSD)
│  ├─ RteEventInSystemInstanceRef (XSD)
│  ├─ RunnableEntityInCompositionInstanceRef (R23-11)
│  ├─ SwcServiceDependencyInCompositionInstanceRef (XSD)
│  ├─ SwcServiceDependencyInSystemInstanceRef (R23-11)
│  ├─ TriggerInAtomicSwcInstanceRef (R23-11)
│  │  ├─ PTriggerInAtomicSwcTypeInstanceRef (R23-11)  + AtpInstanceRef
│  │  └─ RTriggerInAtomicSwcInstanceRef (R23-11)  + AtpInstanceRef
│  ├─ TriggerInExecutableInstanceRef (XSD)
│  ├─ TriggerInSystemInstanceRef (R23-11)
│  ├─ VariableAccessInEcuInstanceRef (XSD)
│  ├─ VariableDataPrototypeInCompositionInstanceRef (R23-11)
│  ├─ VariableInAtomicSwcInstanceRef (R23-11)
│  │  └─ RVariableInAtomicSwcInstanceRef (R23-11)  + AtpInstanceRef
│  └─ VariableInComponentInstanceRef (XSD)
├─ AutoCollectEnum (R23-11)
├─ AUTOSAR (R23-11)
├─ AutosarDataPrototypeInExecutableInstanceRef (XSD)
├─ AutosarParameterRef (R23-11)
├─ AutosarVariableRef (R23-11)
├─ AxisIndexType (R23-11)
├─ Baseline (R23-11)
├─ BaseTypeDefinition (R23-11)
│  └─ BaseTypeDirectDefinition (R23-11)
├─ BaseTypeEncodingString (R23-11)
├─ BinaryManifestAddressableObject (R23-11)
├─ BinaryManifestItemValue (R23-11)
│  ├─ BinaryManifestItemNumericalValue (R23-11)
│  └─ BinaryManifestItemPointerValue (R23-11)
├─ BinaryManifestResource (R23-11)
├─ BindingTimeEnum (R23-11)
├─ BlueprintGenerator (R23-11)
├─ BlueprintPolicy (R23-11)
│  ├─ BlueprintPolicyModifiable (R4.3.1)
│  │  ├─ BlueprintPolicyList (R23-11)  + BlueprintPolicy
│  │  └─ BlueprintPolicySingle (R23-11)  + BlueprintPolicy
│  └─ BlueprintPolicyNotModifiable (R23-11)
├─ Br (R23-11)
├─ BswApiOptions (XSD)
│  ├─ BswClientPolicy (XSD)
│  ├─ BswDataSendPolicy (XSD)
│  ├─ BswInternalTriggeringPointPolicy (XSD)
│  ├─ BswParameterPolicy (XSD)
│  ├─ BswPerInstanceMemoryPolicy (XSD)
│  ├─ BswQueuedDataReceptionPolicy (R23-11)  + BswDataReceptionPolicy
│  └─ BswReleasedTriggerPolicy (XSD)
├─ BswCallType (R23-11)
├─ BswDataReceptionPolicy (R23-11)
├─ BswEntryKindEnum (R23-11)
├─ BswEntryRelationship (R23-11)
├─ BswEntryRelationshipEnum (R23-11)
├─ BswExclusiveAreaPolicy (R23-11)
├─ BswExecutionContext (R23-11)
├─ BswInternalBehavior (R23-11)
├─ BswInterruptCategory (R23-11)
├─ BswModeReceiverPolicy (R23-11)
├─ BswModeSenderPolicy (R23-11)
├─ BswModeSwitchAckRequest (R23-11)
├─ BswModeSwitchEvent (R23-11)
├─ BswModuleClientServerEntry (R23-11)
├─ BswModuleDependency (R23-11)
├─ BswModuleDescription (R23-11)
├─ BswTriggerDirectImplementation (R23-11)
├─ BufferProperties (R23-11)
├─ BuildActionEntity (R23-11)
├─ BuildActionInvocator (R23-11)
├─ BuildActionIoElement (R23-11)
├─ BuildEngineeringObject (R23-11)
├─ BuildTypeEnum (XSD)
├─ BusMirrorCanIdRangeMapping (R23-11)
├─ BusMirrorCanIdToCanIdMapping (R23-11)
├─ BusMirrorChannel (R23-11)
├─ BusMirrorChannelMappingCan (R23-11)
├─ BusMirrorChannelMappingIp (R23-11)
├─ BusMirrorLinPidToCanIdMapping (R23-11)
├─ BusspecificNmEcu (R23-11)
│  ├─ CanNmEcu (R23-11)
│  ├─ FlexrayNmEcu (R23-11)
│  ├─ J1939NmEcu (R23-11)
│  └─ UdpNmEcu (R23-11)
├─ ByteOrderEnum (R23-11)
├─ CalibrationParameterValue (R23-11)
├─ CalprmAxisCategoryEnum (R23-11)
├─ CanAddressingModeType (R23-11)
├─ CanClusterBusOffRecovery (R23-11)
├─ CanClusterContent (XSD)
├─ CanCommunicationControllerContent (XSD)
├─ CanControllerFdConfiguration (R23-11)
├─ CanControllerFdConfigurationRequirements (R23-11)
├─ CanControllerXlConfiguration (R23-11)
├─ CanControllerXlConfigurationRequirements (R23-11)
├─ CanFrameRxBehaviorEnum (R23-11)
├─ CanFrameTxBehaviorEnum (R23-11)
├─ CanNmRangeConfig (XSD)
├─ CanTpAddressingFormatType (R23-11)
├─ CanTpChannelModeType (XSD)
├─ CanTpConfig (R23-11)
├─ CanTpConnection (R23-11)
├─ CanTpEcu (R23-11)
├─ CanXlFrameTriggeringProps (R23-11)
├─ CanXlNmNodeProps (XSD)
├─ CategoryString (R23-11)
├─ ChapterContent (R23-11)
├─ ChapterEnumBreak (R23-11)
├─ ChapterModel (R23-11)
├─ ChapterOrMsrQuery (R23-11)
├─ CIdentifier (R23-11)
├─ ClassTailoring (R23-11)
├─ ClientIdMapping (XSD)
├─ ClientIdRange (R23-11)
├─ ClientIntentEnum (XSD)
├─ ClientServerApplicationErrorMapping (R23-11)
├─ ClientServerArrayElementMapping (XSD)
├─ ClientServerCompositeTypeMapping (XSD)
│  ├─ ClientServerArrayTypeMapping (XSD)
│  └─ ClientServerRecordTypeMapping (XSD)
├─ ClientServerOperationBlueprintMapping (R23-11)
├─ ClientServerOperationMapping (R23-11)
├─ ClientServerPrimitiveTypeMapping (XSD)
├─ ClientServerRecordElementMapping (XSD)
├─ Colspec (R23-11)
├─ ComGrant (XSD)
├─ ComGrantDesign (XSD)
├─ CommunicationClusterContent (XSD)
│  ├─ CanClusterConditional (XSD)  + AbstractCanClusterContent, CanClusterContent
│  ├─ EthernetClusterConditional (XSD)  + EthernetClusterContent
│  ├─ FlexrayClusterConditional (XSD)  + FlexrayClusterContent
│  ├─ J1939ClusterConditional (XSD)  + AbstractCanClusterContent, J1939ClusterContent
│  ├─ LinClusterConditional (XSD)  + LinClusterContent
│  ├─ TtcanClusterConditional (XSD)  + AbstractCanClusterContent, TtcanClusterContent
│  └─ UserDefinedClusterConditional (XSD)  + UserDefinedClusterContent
├─ CommunicationControllerContent (XSD)
│  ├─ CanCommunicationControllerConditional (XSD)  + AbstractCanCommunicationControllerContent, CanCommunicationControllerContent
│  ├─ EthernetCommunicationControllerConditional (XSD)  + EthernetCommunicationControllerContent
│  ├─ FlexrayCommunicationControllerConditional (XSD)  + FlexrayCommunicationControllerContent
│  ├─ LinMasterConditional (XSD)  + LinCommunicationControllerContent, LinMasterContent
│  ├─ LinSlaveConditional (XSD)  + LinCommunicationControllerContent, LinSlaveContent
│  ├─ TtcanCommunicationControllerConditional (XSD)  + AbstractCanCommunicationControllerContent, TtcanCommunicationControllerContent
│  └─ UserDefinedCommunicationControllerConditional (XSD)  + UserDefinedCommunicationControllerContent
├─ CommunicationControllerMapping (R23-11)
├─ CommunicationCycle (R23-11)
│  ├─ CycleCounter (R23-11)
│  └─ CycleRepetition (R23-11)
├─ CommunicationDirectionType (R23-11)
├─ ComponentInSystemInstanceRef (R23-11)
├─ CompositeNetworkRepresentation (R23-11)
├─ CompositeRuleBasedValueArgument (R23-11)
│  └─ ApplicationValueSpecification (R23-11)  + ValueSpecification
├─ CompositionPortToExecutablePortMapping (XSD)
├─ Compu (R23-11)
├─ CompuConst (R23-11)
├─ CompuConstContent (R23-11)
│  ├─ CompuConstFormulaContent (R23-11)
│  ├─ CompuConstNumericContent (R23-11)
│  └─ CompuConstTextContent (R23-11)
├─ CompuContent (R23-11)
│  └─ CompuScales (R23-11)
├─ CompuNominatorDenominator (R23-11)
├─ CompuRationalCoeffs (R23-11)
├─ CompuScale (R23-11)
├─ CompuScaleConstantContents (R23-11)
├─ CompuScaleContents (R23-11)
│  └─ CompuScaleRationalFormula (R23-11)
├─ ConcretePatternEventTriggering (R23-11)
├─ ConfidenceInterval (R23-11)
├─ ConfigReferenceValue (R3.2.3)
├─ ConstantReference (R23-11)
├─ ConstantSpecificationMapping (R23-11)
├─ ConsumedEventGroup (R23-11)
├─ ContainedIPduCollectionSemanticsEnum (R23-11)
├─ ContainedIPduProps (R23-11)
├─ ContainerIPdu (R23-11)
├─ ContainerIPduHeaderTypeEnum (R23-11)
├─ ContainerIPduTriggerEnum (R23-11)
├─ CouplingElement (R23-11)
├─ CouplingElementEnum (R23-11)
├─ CouplingPort (R23-11)
├─ CouplingPortAbstractShaper (XSD)
├─ CouplingPortConnection (R23-11)
├─ CouplingPortDetails (R23-11)
├─ CouplingPortRatePolicy (R23-11)
├─ CouplingPortRatePolicyActionEnum (R23-11)
├─ CouplingPortRoleEnum (R23-11)
├─ CppImplementationDataType (XSD)
├─ CppImplementationDataTypeContextTarget (XSD)
├─ CppImplementationDataTypeElementQualifier (XSD)
├─ CppTemplateArgument (XSD)
├─ CpSoftwareClusterCommunicationResourceProps (R23-11)
│  ├─ ClientServerOperationComProps (R23-11)
│  └─ DataComProps (R23-11)
├─ CryptoCertificateAlgorithmFamilyEnum (R23-11)
├─ CryptoCertificateFormatEnum (R23-11)
├─ CryptoCertificateToCryptoKeySlotMapping (XSD)
├─ CryptoInterface (XSD)
├─ CryptoKeySlot (R23-11)
├─ CryptoKeySlotAllowedModification (XSD)
├─ CryptoKeySlotContentAllowedUsage (XSD)
├─ CryptoKeySlotTypeEnum (XSD)
├─ CryptoKeySlotUsageEnum (XSD)
├─ CryptoNeeds (XSD)
├─ CryptoObjectTypeEnum (XSD)
├─ CryptoServiceKeyGenerationEnum (R23-11)
├─ CseCodeType (R23-11)
├─ CSTransformerErrorReactionEnum (R23-11)
├─ CycleRepetitionType (R23-11)
├─ DataConsistencyPolicyEnum (R23-11)
├─ DataConstrRule (R23-11)
├─ DataExchangePointKind (R23-11)
├─ DataFilter (R23-11)
├─ DataFilterTypeEnum (R23-11)
├─ DataFormatTailoring (R23-11)
├─ DataIdModeEnum (R23-11)
├─ DataLimitKindEnum (R23-11)
├─ DataLinkLayerRule (XSD)
├─ DataMapping (R23-11)
│  ├─ ClientServerToSignalGroupMapping (XSD)
│  ├─ ClientServerToSignalMapping (R23-11)
│  ├─ SenderReceiverCompositeElementToSignalMapping (R23-11)
│  ├─ SenderReceiverToSignalGroupMapping (R23-11)
│  └─ SenderReceiverToSignalMapping (R23-11)
├─ DataPrototypeInPortInterfaceRef (R23-11)
├─ DataPrototypeInServiceInterfaceRef (XSD)
├─ DataPrototypeInSystemRef (XSD)
│  ├─ DataPrototypeWithApplicationDataTypeInSystemRef (XSD)
│  └─ ImplementationDataTypeElementInSystemRef (XSD)
├─ DataPrototypeMapping (R23-11)
├─ DataPrototypeReference (R23-11)
│  └─ ImplementationDataTypeElementInPortInterfaceRef (R23-11)
├─ DataPrototypeTransformationProps (R23-11)
├─ DataTransformationErrorHandlingEnum (R23-11)
├─ DataTransformationKindEnum (R23-11)
├─ DataTransformationSet (R23-11)
├─ DataTransformationStatusForwardingEnum (R23-11)
├─ DataTypeMap (R23-11)
├─ DataTypePolicyEnum (R23-11)
├─ DateTime (R23-11)
├─ DdsCpISignalToDdsTopicMapping (R23-11)
├─ DdsCpProvidedServiceInstance (R23-11)
├─ DdsCpQosProfile (R23-11)
├─ DdsCpServiceInstanceEvent (R23-11)
├─ DdsCpServiceInstanceOperation (R23-11)
├─ DdsCpTopic (R23-11)
├─ DdsDeadline (R23-11)
├─ DdsDestinationOrder (R23-11)
├─ DdsDestinationOrderKindEnum (R23-11)
├─ DdsDurability (R23-11)
├─ DdsDurabilityKindEnum (R23-11)
├─ DdsDurabilityService (R23-11)
├─ DdsDurabilityServiceHistoryKindEnum (R23-11)
├─ DdsHistory (R23-11)
├─ DdsHistoryKindEnum (R23-11)
├─ DdsLatencyBudget (R23-11)
├─ DdsLifespan (R23-11)
├─ DdsLiveliness (R23-11)
├─ DdsLivenessKindEnum (R23-11)
├─ DdsOwnership (R23-11)
├─ DdsOwnershipKindEnum (R23-11)
├─ DdsOwnershipStrength (R23-11)
├─ DdsProtectionKindEnum (XSD)
├─ DdsQosProps (XSD)
│  ├─ DdsEventQosProps (XSD)
│  └─ DdsFieldQosProps (XSD)
├─ DdsReliability (R23-11)
├─ DdsReliabilityKindEnum (R23-11)
├─ DdsResourceLimits (R23-11)
├─ DdsRule (XSD)
├─ DdsServiceInstanceDiscoveryTypeEnum (XSD)
├─ DdsServiceInstanceProps (XSD)
├─ DdsServiceInstanceResourceIdentifierTypeEnum (XSD)
├─ DdsServiceVersion (XSD)
├─ DdsTopicData (R23-11)
├─ DdsTransportPriority (R23-11)
├─ DefaultValueApplicationStrategyEnum (R23-11)
├─ DefaultValueElement (R23-11)
├─ DefList (R23-11)
├─ DelegationSwConnector (R23-11)
├─ DependencyUsageEnum (R23-11)
├─ Describable (R23-11)
│  ├─ CyclicTiming (R23-11)
│  ├─ EventControlledTiming (R23-11)
│  ├─ ExecutableLoggingImplementationProps (XSD)  + ExecutableImplementationProps
│  ├─ HwElementConnector (R23-11)
│  ├─ HwPinConnector (R23-11)
│  ├─ HwPinGroupConnector (R23-11)
│  ├─ IPduTiming (R23-11)
│  ├─ Ipv6DhcpServerConfiguration (R23-11)
│  ├─ PersistencyKeyValueDataTypeMapping (XSD)
│  ├─ RawDataStreamEthernetTcpUdpCredentials (XSD)  + AbstractRawDataStreamEthernetCredentials
│  ├─ RawDataStreamEthernetUdpCredentials (XSD)  + AbstractRawDataStreamEthernetCredentials
│  ├─ SocketConnection (R23-11)
│  ├─ TransformationComSpecProps (R23-11)
│  │  ├─ EndToEndTransformationComSpecProps (R23-11)  + Describable
│  │  └─ UserDefinedTransformationComSpecProps (R23-11)  + Describable
│  ├─ TransformationDescription (R23-11)
│  │  ├─ EndToEndTransformationDescription (R23-11)  + Describable
│  │  ├─ SOMEIPTransformationDescription (R23-11)  + Describable
│  │  └─ UserDefinedTransformationDescription (R23-11)  + Describable
│  └─ TransformationISignalProps (R23-11)
│     ├─ SOMEIPTransformationISignalProps (R23-11)  + Describable
│     └─ UserDefinedTransformationISignalProps (R23-11)  + Describable
├─ DhcpServerConfiguration (R23-11)
├─ Dhcpv6Props (R23-11)
├─ DiagnosticAbstractDataIdentifierInterface (XSD)
├─ DiagnosticAbstractParameter (R23-11)
│  └─ DiagnosticParameter (R23-11)
├─ DiagnosticAbstractRoutineInterface (XSD)
├─ DiagnosticAccessPermissionValidityEnum (XSD)
├─ DiagnosticAudienceEnum (R23-11)
├─ DiagnosticAuthRoleProxy (R23-11)
├─ DiagnosticClearDtcLimitationEnum (R23-11)
├─ DiagnosticClearDtcNotificationEnum (R23-11)
├─ DiagnosticClearEventAllowedBehaviorEnum (R23-11)
├─ DiagnosticClearEventBehaviorEnum (XSD)
├─ DiagnosticClearResetEmissionRelatedInfo (R23-11)
├─ DiagnosticComControlSpecificChannel (R23-11)
├─ DiagnosticComControlSubNodeChannel (R23-11)
├─ DiagnosticCommonElement (R23-11)
├─ DiagnosticCommonProps (R23-11)
├─ DiagnosticCommonPropsContent (XSD)
│  └─ DiagnosticCommonPropsConditional (XSD)
├─ DiagnosticCompareTypeEnum (R23-11)
├─ DiagnosticConnectedIndicator (R23-11)
├─ DiagnosticConnectedIndicatorBehaviorEnum (R23-11)
├─ DiagnosticContributionSet (R23-11)
├─ DiagnosticControlDTCSetting (R23-11)
├─ DiagnosticControlEnableMaskBit (R23-11)
├─ DiagnosticDataCaptureEnum (XSD)
├─ DiagnosticDebounceBehaviorEnum (R23-11)
├─ DiagnosticDenominatorConditionEnum (R23-11)
├─ DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum (R23-11)
├─ DiagnosticEcuProps (XSD)
├─ DiagnosticEnableConditionPortMapping (R23-11)
├─ DiagnosticEnvConditionFormulaPart (R23-11)
│  ├─ DiagnosticEnvCompareCondition (R23-11)
│  │  ├─ DiagnosticEnvDataCondition (R23-11)  + DiagnosticEnvConditionFormulaPart
│  │  └─ DiagnosticEnvDataElementCondition (R23-11)  + DiagnosticEnvConditionFormulaPart
│  └─ DiagnosticEnvConditionFormula (R23-11)
├─ DiagnosticEnvModeCondition (R23-11)
├─ DiagnosticEventClearAllowedEnum (R23-11)
├─ DiagnosticEventCombinationBehaviorEnum (R23-11)
├─ DiagnosticEventCombinationReportingBehaviorEnum (R23-11)
├─ DiagnosticEventDisplacementStrategyEnum (R23-11)
├─ DiagnosticEventKindEnum (R23-11)
├─ DiagnosticEventWindow (R23-11)
├─ DiagnosticEventWindowTimeEnum (R23-11)
├─ DiagnosticExternalAuthenticationIdentification (XSD)
├─ DiagnosticFimFunctionMapping (R23-11)
├─ DiagnosticFunctionIdentifierInhibit (R23-11)
├─ DiagnosticHandleDDDIConfigurationEnum (R23-11)
├─ DiagnosticIndicatorTypeEnum (R23-11)
├─ DiagnosticInhibitionMaskEnum (R23-11)
├─ DiagnosticInhibitSourceEventMapping (R23-11)
├─ DiagnosticInitialEventStatusEnum (XSD)
├─ DiagnosticIumprGroupIdentifier (R23-11)
├─ DiagnosticIumprKindEnum (R23-11)
├─ DiagnosticJumpToBootLoaderEnum (R23-11)
├─ DiagnosticLogicalOperatorEnum (R23-11)
├─ DiagnosticMemoryDestination (R23-11)
├─ DiagnosticMemoryDestinationUserDefined (R23-11)
├─ DiagnosticMemoryEntryStorageTriggerEnum (R23-11)
├─ DiagnosticMonitorUpdateKindEnum (R23-11)
├─ DiagnosticMultipleResourceInterface (XSD)
├─ DiagnosticMultipleResourcePortMapping (XSD)
├─ DiagnosticObdSupportEnum (R23-11)
├─ DiagnosticOccurrenceCounterProcessingEnum (R23-11)
├─ DiagnosticOperationCycleTypeEnum (R23-11)
├─ DiagnosticParameterElementAccess (R23-11)
├─ DiagnosticParameterSupportInfo (R23-11)
├─ DiagnosticPeriodicRate (R23-11)
├─ DiagnosticPeriodicRateCategoryEnum (R23-11)
├─ DiagnosticPortInterface (XSD)
├─ DiagnosticProcessingStyleEnum (R23-11)
├─ DiagnosticReadMemoryByAddress (R23-11)
├─ DiagnosticRecordTriggerEnum (R23-11)
├─ DiagnosticRequestCurrentPowertrainData (R23-11)
├─ DiagnosticRequestDownloadClass (R23-11)
├─ DiagnosticRequestEmissionRelatedDTC (R23-11)
├─ DiagnosticRequestOnBoardMonitoringTestResultsClass (R23-11)
├─ DiagnosticResponseOnEventActionEnum (R23-11)
├─ DiagnosticResponseOnEventTrigger (XSD)
│  ├─ DiagnosticDataChangeTrigger (XSD)
│  └─ DiagnosticDtcChangeTrigger (XSD)
├─ DiagnosticResponseToEcuResetEnum (R23-11)
├─ DiagnosticRoutineTypeEnum (R23-11)
├─ DiagnosticServiceInstance (R23-11)
├─ DiagnosticServiceMappingDiagTarget (R23-11)
├─ DiagnosticServiceRequestCallbackTypeEnum (R23-11)
├─ DiagnosticServiceSwMapping (R23-11)
├─ DiagnosticServiceValidationConfiguration (XSD)
├─ DiagnosticSession (R23-11)
├─ DiagnosticSignificanceEnum (R23-11)
├─ DiagnosticSovdConfiguration (XSD)
├─ DiagnosticSovdPortInterface (XSD)
├─ DiagnosticSovdServiceInstance (XSD)
├─ DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum (R23-11)
├─ DiagnosticStoreEventSupportEnum (XSD)
├─ DiagnosticSupportInfoByte (R23-11)
├─ DiagnosticTestIdentifier (R23-11)
├─ DiagnosticTestResultUpdateEnum (R23-11)
├─ DiagnosticTroubleCodeJ1939 (R23-11)
├─ DiagnosticTroubleCodeJ1939DtcKindEnum (R23-11)
├─ DiagnosticTroubleCodeObd (R23-11)
├─ DiagnosticTroubleCodeProps (R23-11)
├─ DiagnosticTroubleCodeUds (R23-11)
├─ DiagnosticTypeOfDtcSupportedEnum (R23-11)
├─ DiagnosticTypeOfFreezeFrameRecordNumerationEnum (R23-11)
├─ DiagnosticUdsSeverityEnum (R23-11)
├─ DiagnosticValueAccessEnum (R23-11)
├─ DiagnosticWriteMemoryByAddress (R23-11)
├─ DiagnosticWwhObdDtcClassEnum (R23-11)
├─ DiagPduType (R23-11)
├─ DiagRequirementIdString (R23-11)
├─ DiscoveryTechnology (XSD)
├─ DiscoveryTechnologyEnum (XSD)
├─ DisplayFormatString (R23-11)
├─ DisplayPresentationEnum (R23-11)
├─ DltConfig (R23-11)
├─ DltDefaultTraceStateEnum (R23-11)
├─ DocRevision (R23-11)
├─ DocumentationBlock (R23-11)
├─ DocumentViewSelectable (R23-11)
│  └─ Paginateable (R23-11)
│     ├─ Item (R23-11)  + DocumentViewSelectable
│     ├─ LabeledItem (R23-11)  + DocumentViewSelectable
│     ├─ LabeledList (R23-11)  + DocumentViewSelectable
│     ├─ List (R23-11)  + DocumentViewSelectable  · src: ARList
│     ├─ MlFigure (R23-11)  + DocumentViewSelectable
│     ├─ MlFormula (R23-11)  + DocumentViewSelectable
│     ├─ MsrQueryChapter (R23-11)  + DocumentViewSelectable
│     ├─ MsrQueryP1 (R23-11)  + DocumentViewSelectable
│     ├─ MsrQueryTopic1 (R23-11)  + DocumentViewSelectable
│     ├─ MultiLanguageParagraph (R23-11)  + DocumentViewSelectable
│     ├─ MultiLanguageVerbatim (R23-11)  + DocumentViewSelectable
│     ├─ Note (R23-11)  + DocumentViewSelectable
│     └─ Row (R23-11)  + DocumentViewSelectable
├─ DoIpConfig (R23-11)
├─ DoIpEidRetrievalEnum (XSD)
├─ DoIpEntity (R23-11)
├─ DoIpEntityRoleEnum (R23-11)
├─ DoIpInterface (R23-11)
├─ DoIpLogicTesterAddressProps (R23-11)
├─ DoIpNetworkConfiguration (XSD)
├─ DoIpRequestConfiguration (XSD)
├─ DoIpRule (XSD)
├─ DtcFormatTypeEnum (R4.3.1)
├─ DtcKindEnum (R4.3.1)
├─ DynamicPartAlternative (R23-11)
├─ EcucAbstractConfigurationClass (R23-11)
│  ├─ EcucMultiplicityConfigurationClass (R23-11)
│  └─ EcucValueConfigurationClass (R23-11)
├─ EcucAbstractStringParamDefContent (XSD)
│  ├─ EcucFunctionNameDefConditional (XSD)  + EcucFunctionNameDefContent
│  ├─ EcucLinkerSymbolDefConditional (XSD)  + EcucLinkerSymbolDefContent
│  ├─ EcucMultilineStringParamDefConditional (XSD)  + EcucMultilineStringParamDefContent
│  └─ EcucStringParamDefConditional (XSD)  + EcucStringParamDefContent
├─ EcucAffectionEnum (XSD)
├─ EcucCommonAttributes (R23-11)
├─ EcucConditionSpecification (R23-11)
├─ EcucConfigurationClassAffection (XSD)
├─ EcucConfigurationClassEnum (R23-11)
├─ EcucConfigurationVariantEnum (R23-11)
├─ EcucDerivationSpecification (R23-11)
├─ EcucDestinationUriDefRefType (R3.2.3)
├─ EcucDestinationUriNestingContractEnum (R23-11)
├─ EcucDestinationUriPolicy (R23-11)
├─ EcucFunctionNameDefContent (XSD)
├─ EcucImplementationConfigurationClass (XSD)
├─ EcucIndexableValue (R23-11)
│  ├─ EcucAbstractReferenceValue (R23-11)
│  │  ├─ EcucInstanceReferenceValue (R23-11)  + EcucIndexableValue
│  │  └─ EcucReferenceValue (R23-11)  + EcucIndexableValue
│  └─ EcucParameterValue (R23-11)
│     ├─ EcucAddInfoParamValue (R23-11)  + EcucIndexableValue
│     ├─ EcucNumericalParamValue (R23-11)  + EcucIndexableValue
│     └─ EcucTextualParamValue (R23-11)  + EcucIndexableValue
├─ EcucLinkerSymbolDefContent (XSD)
├─ EcucMultilineStringParamDefContent (XSD)
├─ EcucQueryExpression (R23-11)
├─ EcucScopeEnum (R23-11)
├─ EcucStringParamDefContent (XSD)
├─ EcuInstanceProps (XSD)
├─ EcuResourceEstimation (R23-11)
├─ EEnum (R23-11)
├─ EEnumFont (R23-11)
├─ EmphasisText (R23-11)
├─ EmptySignalMapping (XSD)
├─ EndToEndDescription (R23-11)
├─ EndToEndProfileBehaviorEnum (R23-11)
├─ EndToEndProtectionISignalIPdu (R23-11)
├─ EndToEndProtectionVariablePrototype (R23-11)
├─ EndToEndTransformationISignalProps (R23-11)
├─ EndToEndTransformationISignalPropsContent (XSD)
├─ EngineeringObject (R23-11)
│  ├─ AutosarEngineeringObject (R23-11)
│  └─ Graphic (R23-11)
├─ EnterExitTimeout (XSD)
├─ Entry (R23-11)
├─ EnumerationMappingEntry (R23-11)
├─ EnvironmentCaptureToReportingEnum (XSD)
├─ EOCEventRef (R23-11)
├─ EthernetClusterContent (XSD)
├─ EthernetCommunicationController (R23-11)
├─ EthernetCommunicationControllerContent (XSD)
├─ EthernetConnectionNegotiationEnum (R23-11)
├─ EthernetCouplingPortSchedulerEnum (R23-11)
├─ EthernetMacLayerTypeEnum (R23-11)
├─ EthernetPhysicalLayerTypeEnum (R23-11)
├─ EthernetRawDataStreamLocalEndpointConfig (XSD)
├─ EthernetRawDataStreamMapping (XSD)
├─ EthernetRawDataStreamRemoteClientConfig (XSD)
├─ EthernetRawDataStreamRemoteServerConfig (XSD)
├─ EthernetSwitchVlanEgressTaggingEnum (R23-11)
├─ EthernetSwitchVlanIngressTagEnum (R23-11)
├─ EthernetWakeupSleepOnDatalineConfig (R23-11)
├─ EthGlobalTimeManagedCouplingPort (R23-11)
├─ EthGlobalTimeMessageFormatEnum (R23-11)
├─ EthTSynCrcFlags (R23-11)
├─ EthTSynSubTlvConfig (R23-11)
├─ EventAcceptanceStatusEnum (R23-11)
├─ EventGroupControlTypeEnum (R23-11)
├─ EventObdReadinessGroup (R23-11)
├─ EventOccurrenceKindEnum (R23-11)
├─ ExecutableImplementationProps (XSD)
├─ ExecutionDependency (XSD)
├─ ExecutionOrderConstraintTypeEnum (R23-11)
├─ ExecutionStateReportingBehaviorEnum (XSD)
├─ ExecutionTimeTypeEnum (R23-11)
├─ ExternalTriggeringPoint (R23-11)
├─ FieldAccessEnum (XSD)
├─ FileInfoComment (R23-11)
├─ FilterDebouncingEnum (R23-11)
├─ FirewallActionEnum (XSD)
├─ FirewallRule (R23-11)
├─ FirewallRuleProps (R23-11)
├─ FlexrayAbsolutelyScheduledTiming (R23-11)
├─ FlexrayArTpChannel (R23-11)
├─ FlexrayChannelName (R23-11)
├─ FlexrayCluster (R23-11)
├─ FlexrayClusterContent (XSD)
├─ FlexrayCommunicationController (R23-11)
├─ FlexrayCommunicationControllerContent (XSD)
├─ FlexrayFifoConfiguration (R23-11)
├─ FlexrayFifoRange (R23-11)
├─ FlexrayFrameTriggering (R23-11)
├─ FlexrayNmScheduleVariant (R23-11)
├─ FlexrayTpEcu (R23-11)
├─ FloatEnum (R23-11)
├─ FlowMeteringColorModeEnum (R23-11)
├─ FMAttributeValue (R23-11)
├─ FMFeatureDecomposition (R23-11)
├─ FMFeatureSelectionState (R23-11)
├─ ForeignModelReference (XSD)
├─ FormulaExpression (R23-11)
│  ├─ CompuGenericMath (R23-11)
│  ├─ EcucConditionFormula (R23-11)
│  ├─ EcucParameterDerivationFormula (R23-11)
│  ├─ FMFormulaByFeaturesAndAttributes (R23-11)
│  │  └─ FMConditionByFeaturesAndAttributes (R23-11)  + FormulaExpression
│  ├─ SwSystemconstDependentFormula (R23-11)
│  │  ├─ AttributeValueVariationPoint (R23-11)  + FormulaExpression
│  │  │  ├─ AbstractEnumerationValueVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  │  │  ├─ AbstractNumericalVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  │  │  │  ├─ LimitValueVariationPoint (R23-11)  + AttributeValueVariationPoint, FormulaExpression, SwSystemconstDependentFormula
│  │  │  │  └─ NumericalValueVariationPoint (R23-11)  + AttributeValueVariationPoint, FormulaExpression, SwSystemconstDependentFormula
│  │  │  ├─ BooleanValueVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  │  │  ├─ FloatValueVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  │  │  ├─ IntegerValueVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  │  │  ├─ NameTokenValueVariationPoint (XSD)  + FormulaExpression, SwSystemconstDependentFormula
│  │  │  ├─ PositiveIntegerValueVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  │  │  ├─ TimeValueValueVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  │  │  └─ UnlimitedIntegerValueVariationPoint (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  │  ├─ BlueprintFormula (R23-11)  + FormulaExpression
│  │  ├─ ConditionByFormula (R23-11)  + FormulaExpression
│  │  └─ FMFormulaByFeaturesAndSwSystemconsts (R23-11)  + FormulaExpression
│  │     └─ FMConditionByFeaturesAndSwSystemconsts (R23-11)  + FormulaExpression, SwSystemconstDependentFormula
│  ├─ TDEventOccurrenceExpressionFormula (R23-11)
│  └─ TimingConditionFormula (R23-11)
├─ FrameEnum (R23-11)
├─ FrameMapping (R23-11)
├─ FramePid (R23-11)
├─ FrArTpAckType (R23-11)
├─ FreeFormatEntry (R23-11)
│  └─ FreeFormat (R23-11)  + ScheduleTableEntry
├─ FullBindingTimeEnum (R23-11)
├─ FunctionalClusterInteractsWithFunctionalClusterMapping (XSD)
├─ FunctionalClusterPersistencyAccessEnum (XSD)
├─ GeneralAnnotation (R23-11)
│  ├─ Annotation (R23-11)
│  ├─ ClientServerAnnotation (R23-11)
│  ├─ DelegatedPortAnnotation (R23-11)
│  ├─ IoHwAbstractionServerAnnotation (R23-11)
│  ├─ ModePortAnnotation (R23-11)
│  ├─ NvDataPortAnnotation (R23-11)
│  ├─ SenderReceiverAnnotation (R23-11)
│  │  ├─ ReceiverAnnotation (R23-11)  + GeneralAnnotation
│  │  └─ SenderAnnotation (R23-11)  + GeneralAnnotation
│  └─ TriggerPortAnnotation (R23-11)
├─ GenericModelReference (R23-11)
├─ GlobalTimeCorrectionProps (R23-11)
├─ GlobalTimeCouplingPortProps (R23-11)
├─ GlobalTimeCrcSupportEnum (R23-11)
├─ GlobalTimeCrcValidationEnum (R23-11)
├─ GlobalTimeIcvSupportEnum (R23-11)
├─ GlobalTimeIcvVerificationEnum (R23-11)
├─ GlobalTimePortRoleEnum (R23-11)
├─ GlobalTimeSlave (R23-11)
├─ Grant (XSD)
├─ GrantDesign (XSD)
├─ GraphicFitEnum (R23-11)
├─ GraphicNotationEnum (R23-11)
├─ HandleInvalidEnum (R23-11)
├─ HandleOutOfRangeEnum (R23-11)
├─ HandleOutOfRangeStatusEnum (R23-11)
├─ HandleTerminationAndRestartEnum (XSD)
├─ HandleTimeoutEnum (R23-11)
├─ HardwareConfiguration (R23-11)
├─ HealthChannel (XSD)
├─ HealthChannelExternalReportedStatus (XSD)
├─ HwAttributeValue (R23-11)
├─ HwPinGroupContent (R23-11)
├─ HwPortMapping (R23-11)
├─ IcmpRule (XSD)
├─ Identifier (R23-11)
├─ IdsmAbstractPortInterface (XSD)
├─ IdsmInstance (R23-11)
├─ IdsmSignatureSupportAp (R23-11)
├─ IdsmSignatureSupportCp (R23-11)
├─ IdsmTrafficLimitation (R23-11)
├─ IEEE1722TpAafAes3DataTypeEnum (R23-11)
├─ IEEE1722TpAafFormatEnum (R23-11)
├─ IEEE1722TpAafNominalRateEnum (R23-11)
├─ IEEE1722TpAcfBusPart (R23-11)
├─ IEEE1722TpAcfCanMessageTypeEnum (R23-11)
├─ IEEE1722TpAcfLin (R23-11)
├─ IEEE1722TpConfig (R23-11)
├─ IEEE1722TpCrfPullEnum (R23-11)
├─ IEEE1722TpCrfTypeEnum (XSD)
├─ IEEE1722TpRvfColorSpaceEnum (R23-11)
├─ IEEE1722TpRvfFrameRateEnum (R23-11)
├─ IEEE1722TpRvfPixelDepthEnum (R23-11)
├─ IEEE1722TpRvfPixelFormatEnum (R23-11)
├─ IkeAuthenticationMethodEnum (XSD)
├─ ImplementationElementInParameterInstanceRef (R23-11)
├─ IncludedDataTypeSet (R23-11)
├─ IncludedModeDeclarationGroupSet (R23-11)
├─ IndentSample (R23-11)
├─ IndexedArrayElement (R23-11)
├─ IndexEntry (R23-11)
├─ InfrastructureServices (R23-11)
├─ InitialSdDelayConfig (R23-11)
├─ InnerDataPrototypeGroupInCompositionInstanceRef (R23-11)
├─ InstantiationDataDefProps (R23-11)
├─ InstantiationRTEEventProps (R23-11)
│  └─ InstantiationTimingEventProps (R23-11)
├─ InternalConstrs (R23-11)
├─ InterpolationRoutine (R23-11)
├─ InterpolationRoutineMapping (R23-11)
├─ IntervalTypeEnum (R23-11)
├─ InvalidationPolicy (R23-11)
├─ Ip4AddressString (R23-11)
├─ Ip6AddressString (R23-11)
├─ IpAddressKeepEnum (R23-11)
├─ IPduMapping (R23-11)
├─ IPduSignalProcessingEnum (R23-11)
├─ IpIamAuthenticConnectionProps (XSD)
├─ IPSecConfig (R23-11)
├─ IPsecDpdActionEnum (R23-11)
├─ IPsecHeaderTypeEnum (R23-11)
├─ IPsecIpProtocolEnum (R23-11)
├─ IPsecModeEnum (R23-11)
├─ IPsecPolicyEnum (R23-11)
├─ IPTransportProtocolEnum (XSD)
├─ Ipv4AddressSourceEnum (R23-11)
├─ Ipv4ArpProps (R23-11)
├─ Ipv4AutoIpProps (R23-11)
├─ Ipv4DhcpServerConfiguration (R23-11)
├─ Ipv4FragmentationProps (R23-11)
├─ Ipv4Props (R23-11)
├─ Ipv6AddressSourceEnum (R23-11)
├─ IPv6ExtHeaderFilterList (R23-11)
├─ Ipv6FragmentationProps (R23-11)
├─ Ipv6NdpProps (R23-11)
├─ Ipv6Props (R23-11)
├─ ISignalMapping (R23-11)
├─ ISignalPort (R23-11)
├─ ISignalProps (R23-11)
├─ ISignalToIPduMapping (R23-11)
├─ ISignalTypeEnum (R23-11)
├─ ItemLabelPosEnum (R23-11)
├─ J1939ClusterContent (XSD)
├─ J1939ControllerApplicationToJ1939NmNodeMapping (R23-11)
├─ J1939NmAddressConfigurationCapabilityEnum (R23-11)
├─ J1939NodeName (R23-11)
├─ J1939TpConfig (R23-11)
├─ J1939TpConnection (R23-11)
├─ J1939TpPg (XSD)
├─ KeepWithPreviousEnum (R23-11)
├─ KeyUsageRestrictionEnum (XSD)
├─ LanguageSpecific (R23-11)
│  ├─ LLongName (R23-11)  + MixedContentForLongName
│  ├─ LOverviewParagraph (R23-11)  + MixedContentForOverviewParagraph
│  └─ LParagraph (R23-11)  + MixedContentForParagraph
├─ LatencyConstraintTypeEnum (R23-11)
├─ LEnum (R23-11)
├─ LetDataExchangeParadigmEnum (R23-11)
├─ LGraphic (R23-11)
├─ LifeCycleInfo (R23-11)
├─ LifeCyclePeriod (R23-11)
├─ Limit (R23-11)
├─ LinChecksumType (R23-11)
├─ LinClusterContent (XSD)
├─ LinCommunicationControllerContent (XSD)
├─ LinConfigurableFrame (R23-11)
├─ LinErrorResponse (R23-11)
├─ LinMasterContent (XSD)
├─ LinOrderedConfigurableFrame (R23-11)
├─ LinPhysicalChannel (R23-11)
├─ LinSlaveConfig (R23-11)
├─ LinSlaveContent (XSD)
├─ ListEnum (R23-11)
├─ LogTraceDefaultLogLevelEnum (R23-11)
├─ MacAddressString (R23-11)
├─ MacMulticastGroup (R23-11)
├─ MacSecCapabilityEnum (R23-11)
├─ MacSecCipherSuiteConfig (R23-11)
├─ MacSecConfidentialityOffsetEnum (R23-11)
├─ MacSecCryptoAlgoConfig (XSD)
├─ MacSecFailPermissiveModeEnum (R23-11)
├─ MacSecLocalKayProps (R23-11)
├─ MacSecProps (R23-11)
├─ MacSecRoleEnum (R23-11)
├─ Map (R23-11)
├─ MappingConstraint (R23-11)
│  ├─ ComponentClustering (R23-11)
│  ├─ ComponentSeparation (R23-11)
│  └─ SwcToEcuMappingConstraint (XSD)
├─ MappingDirectionEnum (R23-11)
├─ MappingScopeEnum (R23-11)
├─ MaxCommModeEnum (R23-11)
├─ MaximumMessageLengthType (R23-11)
├─ McDataAccessDetails (R23-11)
├─ McdIdentifier (R23-11)
├─ McFunctionDataRefSet (R23-11)
├─ McFunctionDataRefSetContent (XSD)
│  └─ McFunctionDataRefSetConditional (XSD)
├─ McGroup (R23-11)
├─ McGroupDataRefSet (R23-11)
├─ McGroupDataRefSetContent (XSD)
│  └─ McGroupDataRefSetConditional (XSD)
├─ McParameterElementGroup (R23-11)
├─ McSupportData (R23-11)
├─ McSwEmulationMethodSupport (R23-11)
├─ MeasuredHeapUsage (R23-11)
├─ MemoryAllocationKeywordPolicyType (R23-11)
├─ MemorySectionLocation (R23-11)
├─ MemorySectionType (R23-11)
├─ MetaDataItem (R23-11)
├─ MetaDataItemSet (R23-11)
├─ MimeTypeString (R23-11)
├─ MirroringProtocolEnum (R23-11)
├─ MixedContentForLongName (R23-11)
│  └─ SingleLanguageLongName (R23-11)
├─ MixedContentForOverviewParagraph (R23-11)
│  └─ SlOverviewParagraph (R23-11)
├─ MixedContentForParagraph (R23-11)
│  └─ SlParagraph (R23-11)
├─ MixedContentForUnitNames (R23-11)
├─ ModeAccessPoint (R23-11)
├─ ModeActivationKind (R23-11)
├─ ModeDeclarationGroupPrototypeMapping (R23-11)
├─ ModeDrivenTransmissionModeCondition (R23-11)
├─ ModeErrorBehavior (R23-11)
├─ ModeErrorReactionPolicyEnum (R23-11)
├─ ModeInSwcBswInstanceRef (XSD)
│  └─ ModeInBswInstanceRef (R23-11)
├─ ModeInSwcInstanceRef (R23-11)
├─ ModeRequestTypeMap (R23-11)
├─ ModeSwitchedAckRequest (R23-11)
├─ ModeSwitchEventTriggeredActivity (R23-11)
├─ Modification (R23-11)
├─ ModificationTypeEnum (XSD)
├─ ModuleConfiguration (R3.2.3)
├─ MonotonyEnum (R23-11)
├─ MsrQueryArg (R23-11)
├─ MsrQueryP2 (R23-11)
├─ MsrQueryProps (R23-11)
├─ MsrQueryResultChapter (R23-11)
├─ MsrQueryResultTopic1 (R23-11)
├─ MultidimensionalTime (R23-11)
├─ MultilanguageLongName (R23-11)
├─ MultiLanguageOverviewParagraph (R23-11)
├─ MultiLanguagePlainText (R23-11)
├─ MultiplexedIPdu (R23-11)
├─ MultiplexedPart (R23-11)
│  ├─ DynamicPart (R23-11)
│  └─ StaticPart (R23-11)
├─ NameTokens (R23-11)
├─ NativeDeclarationString (R23-11)
├─ NetworkEndpointAddress (R23-11)
│  ├─ Ipv4Configuration (R23-11)
│  ├─ Ipv6Configuration (R23-11)
│  └─ MacMulticastConfiguration (R23-11)
├─ NetworkLayerRule (XSD)
│  ├─ Ipv4Rule (XSD)
│  └─ Ipv6Rule (XSD)
├─ NetworkSegmentIdentification (R23-11)
├─ NetworkTargetAddressType (R23-11)
├─ NmCluster (R23-11)
├─ NmClusterCoupling (R23-11)
│  ├─ CanNmClusterCoupling (R23-11)
│  ├─ FlexrayNmClusterCoupling (R23-11)
│  └─ UdpNmClusterCoupling (R23-11)
├─ NmCoordinator (R23-11)
├─ NmCoordinatorRoleEnum (R23-11)
├─ NmHandleMappingDirectionEnum (XSD)
├─ NmStateRequestEnum (XSD)
├─ NonOsModuleInstantiation (XSD)
├─ NormalizedInstruction (XSD)
├─ NoteTypeEnum (R23-11)
├─ NumericalOrText (R23-11)
├─ NvBlockDataMapping (R23-11)
├─ NvBlockDescriptor (R23-11)
├─ NvBlockNeedsReliabilityEnum (R23-11)
├─ NvBlockNeedsWritingPriorityEnum (R23-11)
├─ ObdRatioConnectionKindEnum (R23-11)
├─ ObdRatioDenominatorNeeds (R23-11)
├─ OperationCycleTypeEnum (R23-11)
├─ OperationInSystemInstanceRef (R23-11)
├─ OrderedMaster (R23-11)
├─ OrientEnum (XSD)
├─ OsArtiAdapterLaunchBehaviorEnum (XSD)
├─ OsTaskPreemptabilityEnum (R23-11)
├─ ParameterPortAnnotation (R23-11)
├─ PayloadBytePatternRule (XSD)
├─ PayloadBytePatternRulePart (XSD)
├─ PduCollectionSemanticsEnum (R23-11)
├─ PduCollectionTriggerEnum (R23-11)
├─ PduMappingDefaultValue (R23-11)
├─ PduToFrameMapping (R23-11)
├─ PerInstanceMemorySize (R23-11)
├─ PersistencyCollectionLevelUpdateStrategyEnum (XSD)
├─ PersistencyDeployment (XSD)
├─ PersistencyDeploymentElement (XSD)
├─ PersistencyDeploymentUri (XSD)
├─ PersistencyElementLevelUpdateStrategyEnum (XSD)
├─ PersistencyInterface (XSD)
├─ PersistencyInterfaceElement (XSD)
├─ PersistencyPortPrototypeToDeploymentMapping (XSD)
├─ PersistencyRedundancyChecksum (XSD)
├─ PersistencyRedundancyEnum (XSD)
├─ PersistencyRedundancyHandling (XSD)
│  ├─ PersistencyRedundancyCrc (XSD)  + PersistencyRedundancyChecksum
│  ├─ PersistencyRedundancyHash (XSD)  + PersistencyRedundancyChecksum
│  └─ PersistencyRedundancyMOutOfN (XSD)
├─ PersistencyRedundancyHandlingScopeEnum (XSD)
├─ PgwideEnum (R23-11)
├─ PhmAbstractRecoveryNotificationInterface (XSD)
├─ PhmStateReference (XSD)
│  └─ FunctionGroupPhmStateReference (XSD)
├─ PhmSupervision (XSD)
├─ PhysConstrs (R23-11)
├─ PhysicalDimensionMapping (R23-11)
├─ PlatformHealthManagementInterface (XSD)
├─ PlatformModuleEndpointConfiguration (XSD)
├─ PlcaProps (R23-11)
├─ PncGatewayTypeEnum (R23-11)
├─ PncMapping (R23-11)
├─ PortAPIOption (R23-11)
├─ PortDefinedArgumentBlueprint (XSD)
├─ PortDefinedArgumentValue (R23-11)
├─ PortInterfaceElementInImplementationDatatypeRef (XSD)
├─ PortPrototypeBlueprintInitValue (R23-11)
├─ PortPrototypeProps (XSD)
│  └─ RPortPrototypeProps (XSD)
├─ PostBuildVariantCondition (R23-11)
├─ PostBuildVariantCriterionValue (R23-11)
├─ PPortComSpec (R23-11)
│  ├─ ModeSwitchSenderComSpec (R23-11)
│  ├─ NvProvideComSpec (R23-11)
│  ├─ ParameterProvideComSpec (R23-11)
│  ├─ SenderComSpec (R23-11)
│  │  ├─ FieldSenderComSpec (XSD)  + PPortComSpec
│  │  ├─ NonqueuedSenderComSpec (R23-11)  + PPortComSpec
│  │  └─ QueuedSenderComSpec (R23-11)  + PPortComSpec
│  └─ ServerComSpec (R23-11)
├─ PredefinedChapter (R23-11)
├─ PrimitiveIdentifier (R23-11)
├─ PrivacyLevel (R23-11)
├─ PrmChar (XSD)
├─ PrmCharContents (XSD)
│  ├─ PrmCharNumericalContents (XSD)
│  └─ PrmCharTextualContents (XSD)
├─ PrmCharNumericalValue (XSD)
│  ├─ PrmCharAbsTol (XSD)
│  └─ PrmCharMinTypMax (XSD)
├─ Prms (R23-11)
├─ ProcessArgument (XSD)
├─ ProcessingKindEnum (R23-11)
├─ ProgramminglanguageEnum (R23-11)
├─ ProvidedApServiceInstance (XSD)
├─ ProvidedServiceInstance (R23-11)
├─ PulseTestEnum (R23-11)
├─ RamBlockStatusControlEnum (R23-11)
├─ RawDataStreamGrant (XSD)
├─ RawDataStreamMapping (XSD)
├─ ReceiverIntentEnum (XSD)
├─ ReceptionComSpecProps (R23-11)
├─ RecordLayoutIteratorPoint (R23-11)
├─ ReentrancyLevelEnum (R23-11)
├─ Ref (R23-11)
├─ ReferenceBase (R23-11)
├─ ReferenceValueSpecification (R23-11)
├─ Referrable (R23-11)
│  ├─ AtpDefinition (R23-11)
│  ├─ BswDistinguishedPartition (R23-11)
│  ├─ BswModuleCallPoint (R23-11)
│  │  ├─ BswAsynchronousServerCallPoint (R23-11)  + Referrable
│  │  ├─ BswAsynchronousServerCallResultPoint (R23-11)  + Referrable
│  │  ├─ BswDirectCallPoint (R23-11)  + Referrable
│  │  └─ BswSynchronousServerCallPoint (R23-11)  + Referrable
│  ├─ BswVariableAccess (R23-11)
│  ├─ CouplingPortTrafficClassAssignment (R23-11)
│  ├─ DiagnosticEnvModeElement (R23-11)
│  │  ├─ DiagnosticEnvBswModeElement (R23-11)  + Referrable
│  │  └─ DiagnosticEnvSwcModeElement (R23-11)  + Referrable
│  ├─ EthernetPriorityRegeneration (R23-11)
│  ├─ ExclusiveAreaNestingOrder (R23-11)
│  ├─ HwDescriptionEntity (R23-11)
│  ├─ ImplementationProps (R23-11)
│  │  ├─ BswSchedulerNamePrefix (R23-11)  + Referrable
│  │  ├─ ExecutableEntityActivationReason (R23-11)  + Referrable
│  │  ├─ SectionNamePrefix (R23-11)  + Referrable
│  │  ├─ SymbolicNameProps (R23-11)  + Referrable
│  │  └─ SymbolProps (R23-11)  + Referrable
│  ├─ LinSlaveConfigIdent (R23-11)
│  ├─ MultilanguageReferrable (R23-11)
│  │  ├─ Caption (R23-11)  + Referrable
│  │  ├─ DefItem (R23-11)  + DocumentViewSelectable, Paginateable, Referrable
│  │  ├─ DocumentationContext (R23-11)  + Referrable
│  │  ├─ Identifiable (R23-11)  + Referrable
│  │  │  ├─ AbstractDoIpLogicAddressProps (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  └─ DoIpLogicTargetAddressProps (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ AbstractEvent (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  └─ BswEvent (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ BswInterruptEvent (R23-11)  + AbstractEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ BswOperationInvokedEvent (R23-11)  + AbstractEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     └─ BswScheduleEvent (R23-11)  + AbstractEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │        ├─ BswAsynchronousServerCallReturnsEvent (R23-11)  + AbstractEvent, BswEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │        ├─ BswBackgroundEvent (R23-11)  + AbstractEvent, BswEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │        ├─ BswDataReceivedEvent (R23-11)  + AbstractEvent, BswEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │        ├─ BswExternalTriggerOccurredEvent (R23-11)  + AbstractEvent, BswEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │        ├─ BswInternalTriggerOccurredEvent (R23-11)  + AbstractEvent, BswEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │        ├─ BswModeManagerErrorEvent (R23-11)  + AbstractEvent, BswEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │        ├─ BswModeSwitchedAckEvent (R23-11)  + AbstractEvent, BswEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │        ├─ BswOsTaskExecutionEvent (R23-11)  + AbstractEvent, BswEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │        └─ BswTimingEvent (R23-11)  + AbstractEvent, BswEvent, Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ AbstractSecurityEventFilter (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ SecurityEventOneEveryNFilter (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ SecurityEventThresholdFilter (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ AdaptiveSwcInternalBehavior (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ AliveSupervision (XSD)  + MultilanguageReferrable, PhmSupervision, Referrable
│  │  │  ├─ ApApplicationEndpoint (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ApplicationError (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ApplicationPartitionToEcuPartitionMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ AppliedStandard (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ AppOsTaskProxyToEcuTaskProxyMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ApSomeipTransformationProps (XSD)  + MultilanguageReferrable, Referrable, TransformationProps
│  │  │  ├─ ArtifactChecksum (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ArtifactLocator (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ AtpBlueprint (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ BuildAction (R23-11)  + AtpBlueprintable, BuildActionEntity, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ BuildActionEnvironment (R23-11)  + AtpBlueprintable, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ ConsistencyNeeds (R23-11)  + AtpBlueprintable, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ ImpositionTime (R23-11)  + AtpBlueprintable, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ LifeCycleState (R23-11)  + AtpBlueprintable, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ PortInterfaceMapping (R23-11)  + AtpBlueprintable, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ ClientServerInterfaceMapping (R23-11)  + AtpBlueprint, AtpBlueprintable, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ ModeInterfaceMapping (R23-11)  + AtpBlueprint, AtpBlueprintable, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ ServiceInterfaceMapping (XSD)  + AtpBlueprint, AtpBlueprintable, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ TriggerInterfaceMapping (R23-11)  + AtpBlueprint, AtpBlueprintable, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     └─ VariableAndParameterInterfaceMapping (R23-11)  + AtpBlueprint, AtpBlueprintable, Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ AtpBlueprintable (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ AtpClassifier (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ AtpStructureElement (R23-11)  + AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ AbstractAccessPoint (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ AsynchronousServerCallResultPoint (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ ExternalTriggeringPointIdent (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, IdentCaption, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ InternalTriggeringPoint (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ ModeAccessPointIdent (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, IdentCaption, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ ModeSwitchPoint (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ ParameterAccess (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ ServerCallPoint (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  │  ├─ AsynchronousServerCallPoint (R23-11)  + AbstractAccessPoint, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  │  └─ SynchronousServerCallPoint (R23-11)  + AbstractAccessPoint, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  └─ VariableAccess (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ AbstractImplementationDataTypeElement (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ CppImplementationDataTypeElement (XSD)  + AtpClassifier, AtpFeature, AtpStructureElement, CppImplementationDataTypeContextTarget, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  └─ ImplementationDataTypeElement (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ AdaptiveFirewallModuleInstantiation (XSD)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, NonOsModuleInstantiation, Referrable
│  │  │  │  │  ├─ BulkNvDataDescriptor (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ ClientServerOperation (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ CryptoModuleInstantiation (XSD)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, NonOsModuleInstantiation, Referrable
│  │  │  │  │  ├─ DataPrototypeGroup (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ DoIpInstantiation (XSD)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, NonOsModuleInstantiation, Referrable
│  │  │  │  │  ├─ GenericModuleInstantiation (XSD)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, NonOsModuleInstantiation, Referrable
│  │  │  │  │  ├─ IamModuleInstantiation (XSD)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, NonOsModuleInstantiation, Referrable
│  │  │  │  │  ├─ IdentCaption (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ BswServiceDependencyIdent (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  └─ DiagnosticParameterIdent (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, DiagnosticServiceMappingDiagTarget, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ IdsPlatformInstantiation (R23-11)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, NonOsModuleInstantiation, Referrable
│  │  │  │  │  │  └─ IdsmModuleInstantiation (R23-11)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, NonOsModuleInstantiation, Referrable
│  │  │  │  │  ├─ InternalBehavior (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ LogAndTraceInstantiation (XSD)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, NonOsModuleInstantiation, Referrable
│  │  │  │  │  ├─ ModeDeclaration (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ ModeDeclarationMapping (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ ModeTransition (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ NmInstantiation (XSD)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, NonOsModuleInstantiation, Referrable
│  │  │  │  │  ├─ OsModuleInstantiation (XSD)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ PerInstanceMemory (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ PortGroup (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ RTEEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ AsynchronousServerCallReturnsEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ BackgroundEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ DataReceivedEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ DataReceiveErrorEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ DataSendCompletedEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ DataWriteCompletedEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ ExternalTriggerOccurredEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ InitEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ InternalTriggerOccurredEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ ModeSwitchedAckEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ OperationInvokedEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ OsTaskExecutionEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ SwcModeSwitchEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ TimingEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  └─ TransformerHardErrorEvent (R23-11)  + AbstractEvent, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ RunnableEntityGroup (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ SovdGatewayInstantiation (XSD)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, NonOsModuleInstantiation, Referrable, SovdModuleInstantiation
│  │  │  │  │  ├─ SovdServerInstantiation (XSD)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, NonOsModuleInstantiation, Referrable, SovdModuleInstantiation
│  │  │  │  │  ├─ StateManagementModuleInstantiation (XSD)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, NonOsModuleInstantiation, Referrable
│  │  │  │  │  ├─ SwConnector (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ AssemblySwConnector (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  └─ PassThroughSwConnector (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ SwcServiceDependency (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable, ServiceDependency
│  │  │  │  │  ├─ TimeSyncModuleInstantiation (XSD)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, NonOsModuleInstantiation, Referrable
│  │  │  │  │  ├─ Trigger (R23-11)  + AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ UcmMasterModuleInstantiation (XSD)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, NonOsModuleInstantiation, Referrable, UcmModuleInstantiation
│  │  │  │  │  └─ UcmSubordinateModuleInstantiation (XSD)  + AdaptiveModuleInstantiation, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, NonOsModuleInstantiation, Referrable, UcmModuleInstantiation
│  │  │  │  ├─ AtpType (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ StateManagementStateNotification (XSD)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ AtpPrototype (R23-11)  + AtpFeature, MultilanguageReferrable, Referrable
│  │  │  │  ├─ DataPrototype (R23-11)  + AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ ApplicationCompositeElementDataPrototype (R23-11)  + AtpFeature, AtpPrototype, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ ApplicationArrayElement (R23-11)  + AtpFeature, AtpPrototype, DataPrototype, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ ApplicationAssocMapElement (XSD)  + AtpFeature, AtpPrototype, DataPrototype, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  └─ ApplicationRecordElement (R23-11)  + AtpFeature, AtpPrototype, DataPrototype, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  └─ AutosarDataPrototype (R23-11)  + AtpFeature, AtpPrototype, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │     ├─ ArgumentDataPrototype (R23-11)  + AtpFeature, AtpPrototype, DataPrototype, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │     ├─ Field (R23-11)  + AtpFeature, AtpPrototype, DataPrototype, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │     ├─ ParameterDataPrototype (R23-11)  + AtpFeature, AtpPrototype, DataPrototype, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │     ├─ PersistencyDataElement (XSD)  + AtpFeature, AtpPrototype, DataPrototype, Identifiable, MultilanguageReferrable, PersistencyInterfaceElement, Referrable
│  │  │  │  │     └─ VariableDataPrototype (R23-11)  + AtpFeature, AtpPrototype, DataPrototype, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ ModeDeclarationGroupPrototype (R23-11)  + AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ PortPrototype (R23-11)  + AtpBlueprintable, AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ AbstractProvidedPortPrototype (R23-11)  + AtpBlueprintable, AtpFeature, AtpPrototype, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ PPortPrototype (R23-11)  + AtpBlueprintable, AtpFeature, AtpPrototype, Identifiable, MultilanguageReferrable, PortPrototype, Referrable
│  │  │  │  │  │  └─ PRPortPrototype (R23-11)  + AbstractRequiredPortPrototype, AtpBlueprintable, AtpFeature, AtpPrototype, Identifiable, MultilanguageReferrable, PortPrototype, Referrable
│  │  │  │  │  └─ AbstractRequiredPortPrototype (R23-11)  + AtpBlueprintable, AtpFeature, AtpPrototype, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │     └─ RPortPrototype (R23-11)  + AtpBlueprintable, AtpFeature, AtpPrototype, Identifiable, MultilanguageReferrable, PortPrototype, Referrable
│  │  │  │  ├─ RootSwClusterDesignComponentPrototype (XSD)  + AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ RootSwComponentPrototype (XSD)  + AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ RootSwCompositionPrototype (R23-11)  + AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ SwComponentPrototype (R23-11)  + AtpFeature, Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ AutosarOperationArgumentInstance (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ AutosarVariableInstance (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ BinaryManifestItem (R23-11)  + BinaryManifestAddressableObject, MultilanguageReferrable, Referrable
│  │  │  ├─ BinaryManifestItemDefinition (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ BinaryManifestMetaDataField (R23-11)  + BinaryManifestAddressableObject, MultilanguageReferrable, Referrable
│  │  │  ├─ BinaryManifestProvideResource (R23-11)  + BinaryManifestResource, MultilanguageReferrable, Referrable
│  │  │  ├─ BinaryManifestRequireResource (R23-11)  + BinaryManifestResource, MultilanguageReferrable, Referrable
│  │  │  ├─ BinaryManifestResourceDefinition (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ BlockState (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ BswDebugInfo (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ BswInternalTriggeringPoint (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ CanNmCluster (R23-11)  + MultilanguageReferrable, NmCluster, Referrable
│  │  │  ├─ CanTpAddress (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ CanTpChannel (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ CanTpNode (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ Chapter (R23-11)  + DocumentViewSelectable, MultilanguageReferrable, Paginateable, Referrable
│  │  │  ├─ CheckpointTransition (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ClassContentConditional (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ClientIdDefinition (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ Code (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ CollectableElement (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ ARPackage (R23-11)  + AtpBlueprint, AtpBlueprintable, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ PackageableElement (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ ARElement (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     │  ├─ AclObjectSet (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ AclOperation (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ AclPermission (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ AclRole (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ AdaptiveFirewallToPortPrototypeMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ AliasNameSet (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ Allocator (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ApApplicationError (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ApApplicationErrorDomain (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ApApplicationErrorSet (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ApplicabilityInfoSet (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ApplicationPartition (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ArtifactChecksumToCryptoProviderMapping (XSD)  + CollectableElement, FunctionalClusterInteractsWithFunctionalClusterMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ AutosarDataType (R23-11)  + AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ AbstractImplementationDataType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ CustomCppImplementationDataType (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, AutosarDataType, CollectableElement, CppImplementationDataType, CppImplementationDataTypeContextTarget, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ ImplementationDataType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, AutosarDataType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  └─ StdCppImplementationDataType (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, AutosarDataType, CollectableElement, CppImplementationDataType, CppImplementationDataTypeContextTarget, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  └─ ApplicationDataType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │     ├─ ApplicationCompositeDataType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, AutosarDataType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │     │  ├─ ApplicationArrayDataType (R23-11)  + ARElement, ApplicationDataType, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, AutosarDataType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │     │  ├─ ApplicationAssocMapDataType (XSD)  + ARElement, ApplicationDataType, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, AutosarDataType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │     │  └─ ApplicationRecordDataType (R23-11)  + ARElement, ApplicationDataType, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, AutosarDataType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │     ├─ ApplicationDeferredDataType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, AutosarDataType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │     └─ ApplicationPrimitiveDataType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, AutosarDataType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ BaseType (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  └─ SwBaseType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ BlueprintMappingSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ BswCompositionTiming (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TimingExtension
│  │  │  │     │  ├─ BswEntryRelationshipSet (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ BswModuleEntry (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ BswModuleTiming (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TimingExtension
│  │  │  │     │  ├─ BuildActionManifest (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ CalibrationParameterValueSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ CanXlProps (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ ClientIdDefinitionSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ClientServerInterfaceToBswModuleEntryBlueprintMapping (R23-11)  + AtpBlueprint, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ Collection (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ComCertificateToCryptoCertificateMapping (XSD)  + CollectableElement, FunctionalClusterInteractsWithFunctionalClusterMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ ComEventGrant (XSD)  + CollectableElement, ComGrant, Grant, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ ComEventGrantDesign (XSD)  + CollectableElement, ComGrantDesign, GrantDesign, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ComFieldGrant (XSD)  + CollectableElement, ComGrant, Grant, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ ComFieldGrantDesign (XSD)  + CollectableElement, ComGrantDesign, GrantDesign, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ComFindServiceGrant (XSD)  + CollectableElement, Grant, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ ComFindServiceGrantDesign (XSD)  + CollectableElement, GrantDesign, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ComKeyToCryptoKeySlotMapping (XSD)  + CollectableElement, FunctionalClusterInteractsWithFunctionalClusterMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ ComMethodGrant (XSD)  + CollectableElement, ComGrant, Grant, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ ComMethodGrantDesign (XSD)  + CollectableElement, ComGrantDesign, GrantDesign, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ CommunicationCluster (R23-11)  + CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  ├─ AbstractCanCluster (R23-11)  + ARElement, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, Uploadable PackageElement, UploadableDesignElement
│  │  │  │     │  │  │  ├─ CanCluster (R23-11)  + ARElement, CollectableElement, CommunicationCluster, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  │  ├─ J1939Cluster (R23-11)  + ARElement, CollectableElement, CommunicationCluster, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  │  └─ TtcanCluster (R23-11)  + ARElement, CollectableElement, CommunicationCluster, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  ├─ EthernetCluster (R23-11)  + ARElement, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, Uploadable PackageElement, UploadableDesignElement
│  │  │  │     │  │  ├─ LinCluster (R23-11)  + ARElement, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, Uploadable PackageElement, UploadableDesignElement
│  │  │  │     │  │  └─ UserDefinedCluster (R23-11)  + ARElement, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, Uploadable PackageElement, UploadableDesignElement
│  │  │  │     │  ├─ ComOfferServiceGrant (XSD)  + CollectableElement, Grant, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ ComOfferServiceGrantDesign (XSD)  + CollectableElement, GrantDesign, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ CompositionPPortToExecutablePPortMapping (XSD)  + CollectableElement, CompositionPortToExecutablePortMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ CompositionRPortToExecutableRPortMapping (XSD)  + CollectableElement, CompositionPortToExecutablePortMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ CompuMethod (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ComSecOcToCryptoKeySlotMapping (XSD)  + CollectableElement, FunctionalClusterInteractsWithFunctionalClusterMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ ComTriggerGrant (XSD)  + CollectableElement, ComGrant, Grant, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ ComTriggerGrantDesign (XSD)  + CollectableElement, ComGrantDesign, GrantDesign, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ConsistencyNeedsBlueprintSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ConstantSpecification (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ConstantSpecificationMappingSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ CpSoftwareCluster (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ CpSoftwareClusterBinaryManifestDescriptor (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ CpSoftwareClusterMappingSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ CpSoftwareClusterResourcePool (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ CryptoCertificateToPortPrototypeMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ CryptoEllipticCurveProps (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ CryptoKeySlotToPortPrototypeMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ CryptoProviderToPortPrototypeMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ CryptoServiceCertificate (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ CryptoServiceKey (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ CryptoServicePrimitive (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ CryptoServiceQueue (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ CryptoSignatureScheme (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DataConstr (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DataExchangePoint (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DataTypeMappingSet (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DdsCpConfig (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DdsProvidedServiceInstance (XSD)  + AdaptivePlatformServiceInstance, CollectableElement, DdsQosProps, DdsServiceInstanceProps, Identifiable, MultilanguageReferrable, PackageableElement, ProvidedApServiceInstance, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ DdsRequiredServiceInstance (XSD)  + AdaptivePlatformServiceInstance, CollectableElement, DdsQosProps, DdsServiceInstanceProps, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, RequiredApServiceInstance, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ DdsSecureComProps (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, SecureComProps, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ DdsSecureGovernance (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ DdsServiceInstanceToMachineMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, ServiceInstanceToMachineMapping, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ DdsServiceInterfaceDeployment (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, ServiceInterfaceDeployment, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ DdsTopicAccessRule (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ DiagnosticAbstractAliasEvent (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticFimAliasEvent (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  └─ DiagnosticFimAliasEventGroup (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticAbstractDataIdentifier (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDataIdentifier (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  └─ DiagnosticDynamicDataIdentifier (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticAccessPermission (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticAging (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticAuthentication (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticAuthenticationConfiguration (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticAuthTransmitCertificate (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDeAuthentication (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticProofOfOwnership (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticVerifyCertificateBidirectional (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  └─ DiagnosticVerifyCertificateUnidirectional (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticAuthRole (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticClearDiagnosticInformation (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticComControl (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticCondition (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticClearCondition (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticEnableCondition (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  └─ DiagnosticStorageCondition (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticConditionGroup (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticClearConditionGroup (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticEnableConditionGroup (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  └─ DiagnosticStorageConditionGroup (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticConnection (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticCustomServiceInstance (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticDataByIdentifier (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticReadDataByIdentifier (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticReadScalingDataByIdentifier (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  └─ DiagnosticWriteDataByIdentifier (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticDataIdentifierSet (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticDynamicallyDefineDataIdentifier (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticEcuInstanceProps (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticEcuReset (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticEnvironmentalCondition (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticEvent (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticExtendedDataRecord (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticFimEventGroup (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticFreezeFrame (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticFunctionIdentifier (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticIndicator (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticInfoType (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticIOControl (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticIumpr (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticIumprDenominatorGroup (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticIumprGroup (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticJ1939ExpandedFreezeFrame (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticJ1939FreezeFrame (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticJ1939Node (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticJ1939Spn (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticMapping (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ CpSwClusterResourceToDiagDataElemMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ CpSwClusterResourceToDiagFunctionIdMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ CpSwClusterToDiagEventMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ CpSwClusterToDiagRoutineSubfunctionMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticAuthTransmitCertificateMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDemProvidedDataMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticEventToDebounceAlgorithmMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticEventToEnableConditionGroupMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticEventToOperationCycleMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticEventToSecurityEventMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticEventToStorageConditionGroupMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticEventToTroubleCodeJ1939Mapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticEventToTroubleCodeUdsMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticFimAliasEventGroupMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticFimAliasEventMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticIumprToFunctionIdentifierMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticJ1939SpnMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticMasterToSlaveEventMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticProvidedDataMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticSecureCodingMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticSecurityEventReportingModeMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticSovdConfigurationDataIdentifierMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticSwMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticAuthenticationPortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticClearConditionPortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticDataPortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticEventPortMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticExternalAuthenticationPortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticIndicatorPortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticJ1939SwMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticMemoryDestinationPortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticMonitorPortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticMultipleConditionPortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, DiagnosticMultipleResourcePortMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticMultipleEventPortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, DiagnosticMultipleResourcePortMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticMultipleMonitorPortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, DiagnosticMultipleResourcePortMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticOperationCyclePortMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticSecurityLevelPortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticServiceDataMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticServiceGenericMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticServiceValidationMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticSovdAuthorizationPortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticSovdBulkDataPortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticSovdConfigurationPortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticSovdProximityChallengePortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticSovdServiceValidationPortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticSovdUpdatePortMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  └─ DiagnosticStorageConditionPortMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticTroubleCodeUdsToClearConditionGroupMapping (XSD)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  └─ DiagnosticTroubleCodeUdsToTroubleCodeObdMapping (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticMasterToSlaveEventMappingSet (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticMeasurementIdentifier (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticMemoryByAddress (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDataTransfer (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticMemoryAddressableRangeAccess (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ DiagnosticRequestDownload (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMemoryByAddress, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  └─ DiagnosticRequestUpload (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticMemoryByAddress, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  └─ DiagnosticTransferExit (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement
│  │  │  │     │  ├─ DiagnosticMemoryDestinationMirror (XSD)  + CollectableElement, DiagnosticCommonElement, DiagnosticMemoryDestination, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticMemoryDestinationPrimary (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticMemoryDestination, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticMemoryIdentifier (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticOperationCycle (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticParameterIdentifier (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticPowertrainFreezeFrame (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticProtocol (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticReadDataByPeriodicID (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticReadDTCInformation (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticRequestControlOfOnBoardDevice (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticRequestEmissionRelatedDTCPermanentStatus (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticRequestFileTransfer (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticRequestOnBoardMonitoringTestResults (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticRequestPowertrainFreezeFrameData (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticRequestVehicleInfo (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticResponseOnEvent (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticRoutine (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticRoutineControl (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticSecurityAccess (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticSecurityLevel (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticServiceClass (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticAuthenticationClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticClearDiagnosticInformationClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticClearResetEmissionRelatedInfoClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticComControlClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticControlDTCSettingClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticCustomServiceClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDataTransferClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDynamicallyDefineDataIdentifierClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticEcuResetClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticIoControlClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticReadDataByIdentifierClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticReadDataByPeriodicIDClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticReadDTCInformationClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticReadMemoryByAddressClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticReadScalingDataByIdentifierClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticRequestControlOfOnBoardDeviceClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticRequestCurrentPowertrainDataClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticRequestEmissionRelatedDTCClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticRequestEmissionRelatedDTCPermanentStatusClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticRequestFileTransferClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticRequestPowertrainFreezeFrameDataClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticRequestUploadClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticRequestVehicleInfoClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticResponseOnEventClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticRoutineControlClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticSecurityAccessClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticSessionControlClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticTransferExitClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticWriteDataByIdentifierClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  └─ DiagnosticWriteMemoryByAddressClass (R23-11)  + ARElement, CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticServiceTable (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticSessionControl (R23-11)  + CollectableElement, DiagnosticCommonElement, DiagnosticServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticSovdBulkData (XSD)  + CollectableElement, DiagnosticCommonElement, DiagnosticSovdServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticSovdConfigurationBulkData (XSD)  + CollectableElement, DiagnosticCommonElement, DiagnosticSovdConfiguration, DiagnosticSovdServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticSovdConfigurationParameter (XSD)  + CollectableElement, DiagnosticCommonElement, DiagnosticSovdConfiguration, DiagnosticSovdServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticSovdLock (XSD)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticSovdLog (XSD)  + CollectableElement, DiagnosticCommonElement, DiagnosticSovdServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticSovdMethod (XSD)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticSovdUpdate (XSD)  + CollectableElement, DiagnosticCommonElement, DiagnosticSovdServiceInstance, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticTestResult (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticTestRoutineIdentifier (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticTroubleCode (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DiagnosticTroubleCodeGroup (R23-11)  + CollectableElement, DiagnosticCommonElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ DltApplicationToProcessMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ DltContext (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ DltEcu (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ DltLogSink (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ DltLogSinkToPortPrototypeMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ Documentation (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ E2EProfileCompatibilityProps (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ E2EProfileConfigurationSet (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ EcucDefinitionCollection (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ EcucDestinationUriDefSet (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ EcucModuleConfigurationValues (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ EcucModuleDef (R23-11)  + AtpBlueprint, AtpBlueprintable, AtpDefinition, CollectableElement, EcucDefinitionElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ EcucValueCollection (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ EcuTiming (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TimingExtension
│  │  │  │     │  ├─ EndToEndProtectionSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ EthernetRawDataStreamClientMapping (XSD)  + CollectableElement, EthernetRawDataStreamMapping, Identifiable, MultilanguageReferrable, PackageableElement, RawDataStreamMapping, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ EthernetRawDataStreamGrant (XSD)  + CollectableElement, Grant, Identifiable, MultilanguageReferrable, PackageableElement, RawDataStreamGrant, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ EthernetRawDataStreamServerMapping (XSD)  + CollectableElement, EthernetRawDataStreamMapping, Identifiable, MultilanguageReferrable, PackageableElement, RawDataStreamMapping, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ EthIpProps (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ EthTcpIpIcmpProps (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ EthTcpIpProps (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ EvaluatedVariantSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ Executable (XSD)  + AtpClassifier, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ ExecutableTiming (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TimingExtension
│  │  │  │     │  ├─ FlatMap (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ FMFeature (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ FMFeatureMap (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ FMFeatureModel (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ FMFeatureSelectionSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ FunctionalClusterInteractsWithPersistencyDeploymentMapping (XSD)  + CollectableElement, FunctionalClusterInteractsWithFunctionalClusterMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ FunctionalClusterToSecurityEventDefinitionMapping (XSD)  + CollectableElement, FunctionalClusterInteractsWithFunctionalClusterMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ FunctionGroupSet (XSD)  + AtpClassifier, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ GeneralPurposeConnection (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ GlobalTimeDomain (R23-11)  + CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ HwCategory (R23-11)  + AtpDefinition, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ HwElement (R23-11)  + CollectableElement, HwDescriptionEntity, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ HwType (R23-11)  + CollectableElement, HwDescriptionEntity, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ IdsCommonElement (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  ├─ IdsMapping (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  │  ├─ SecurityEventContextMappingApplication (R23-11)  + ARElement, CollectableElement, Identifiable, IdsCommonElement, MultilanguageReferrable, PackageableElement, Referrable, SecurityEventContextMapping, Uploadable DesignElement, UploadablePackageElement
│  │  │  │     │  │  │  ├─ SecurityEventContextMappingBswModule (R23-11)  + ARElement, CollectableElement, Identifiable, IdsCommonElement, MultilanguageReferrable, PackageableElement, Referrable, SecurityEventContextMapping, Uploadable DesignElement, UploadablePackageElement
│  │  │  │     │  │  │  └─ SecurityEventContextMappingFunctionalCluster (R23-11)  + ARElement, CollectableElement, Identifiable, IdsCommonElement, MultilanguageReferrable, PackageableElement, Referrable, SecurityEventContextMapping, Uploadable DesignElement, UploadablePackageElement
│  │  │  │     │  │  ├─ IdsmProperties (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  └─ SecurityEventDefinition (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ IdsDesign (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ IdsmContextProviderMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ IdsmTimestampProviderMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ IEEE1722TpConnection (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ IEEE1722TpAcfConnection (XSD)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  └─ IEEE1722TpAvConnection (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │     ├─ IEEE1722TpAafConnection (XSD)  + ARElement, CollectableElement, IEEE1722TpConnection, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │     ├─ IEEE1722TpCrfConnection (XSD)  + ARElement, CollectableElement, IEEE1722TpConnection, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │     ├─ IEEE1722TpIidcConnection (R23-11)  + ARElement, CollectableElement, IEEE1722TpConnection, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │     └─ IEEE1722TpRvfConnection (R23-11)  + ARElement, CollectableElement, IEEE1722TpConnection, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ Implementation (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ BswImplementation (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  └─ SwcImplementation (R23-11)  + ARElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ImpositionTimeDefinitionGroup (XSD)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ InterfaceMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ InterpolationRoutineMappingSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ IpIamRemoteSubject (XSD)  + AbstractIamRemoteSubject, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ IPSecConfigProps (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ IPSecIamRemoteSubject (XSD)  + AbstractIamRemoteSubject, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ IPv6ExtHeaderFilterSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ISignal (R23-11)  + CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ ISignalGroup (R23-11)  + CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ J1939ControllerApplication (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ KeywordSet (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ LifeCycleInfoSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ LifeCycleStateDefinitionGroup (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ LogAndTraceMessageCollectionSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ LTMessageCollectionToPortPrototypeMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ Machine (XSD)  + AtpClassifier, AtpFeature, AtpStructureElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ MachineTiming (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TimingExtension
│  │  │  │     │  ├─ MacSecGlobalKayProps (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ MacSecParticipantSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ McFunction (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, Packageable
│  │  │  │     │  ├─ ModeDeclarationGroup (R23-11)  + AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ ModeDeclarationMappingSet (R23-11)  + AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ NetworkHandlePortMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ NmConfig (R23-11)  + CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ NmHandleToFunctionGroupStateMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ NmInteractsWithSmMapping (XSD)  + CollectableElement, FunctionalClusterInteractsWithFunctionalClusterMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ OsTaskProxy (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ Pdu (R23-11)  + CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  ├─ GeneralPurposePdu (R23-11)  + ARElement, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  ├─ IPdu (R23-11)  + ARElement, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  │  ├─ DcmIPdu (R23-11)  + ARElement, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Pdu, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  │  ├─ GeneralPurposeIPdu (R23-11)  + ARElement, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Pdu, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  │  ├─ ISignalIPdu (R23-11)  + ARElement, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Pdu, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  │  ├─ J1939DcmIPdu (R23-11)  + ARElement, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Pdu, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  │  ├─ NPdu (R23-11)  + ARElement, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Pdu, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  │  ├─ UserDefinedIPdu (R23-11)  + ARElement, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Pdu, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  │  └─ XcpPdu (XSD)  + ARElement, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Pdu, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  ├─ NmPdu (R23-11)  + ARElement, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  │  └─ UserDefinedPdu (R23-11)  + ARElement, CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ PersistencyDeploymentElementToCryptoKeySlotMapping (XSD)  + CollectableElement, FunctionalClusterInteractsWithFunctionalClusterMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ PersistencyDeploymentToCryptoKeySlotMapping (XSD)  + CollectableElement, FunctionalClusterInteractsWithFunctionalClusterMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ PersistencyDeploymentToDltLogSinkMapping (XSD)  + CollectableElement, FunctionalClusterInteractsWithFunctionalClusterMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ PersistencyFileStorage (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PersistencyDeployment, Referrable, UploadableDeploymentElement, UploadableExclusivePackageElement, UploadablePackageElement
│  │  │  │     │  ├─ PersistencyKeyValueStorage (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PersistencyDeployment, Referrable, UploadableDeploymentElement, UploadableExclusivePackageElement, UploadablePackageElement
│  │  │  │     │  ├─ PersistencyPortPrototypeToFileStorageMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PersistencyPortPrototypeToDeploymentMapping, Referrable, UploadableDeploymentElement, UploadableExclusivePackageElement, UploadablePackageElement
│  │  │  │     │  ├─ PersistencyPortPrototypeToKeyValueStorageMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PersistencyPortPrototypeToDeploymentMapping, Referrable, UploadableDeploymentElement, UploadableExclusivePackageElement, UploadablePackageElement
│  │  │  │     │  ├─ PhmContributionToMachineMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ PhysicalDimension (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ PhysicalDimensionMappingSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ PlatformHealthManagementContribution (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ PlatformModuleEthernetEndpointConfiguration (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PlatformModuleEndpointConfiguration, Referrable
│  │  │  │     │  ├─ PortInterface (R23-11)  + AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ ApplicationInterface (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ ClientServerInterface (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ CryptoCertificateInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, CryptoInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ CryptoKeySlotInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, CryptoInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ CryptoProviderInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, CryptoInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ CryptoTrustMasterInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, CryptoInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DataInterface (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ NvDataInterface (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PortInterface, Referrable
│  │  │  │     │  │  │  ├─ ParameterInterface (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PortInterface, Referrable
│  │  │  │     │  │  │  └─ SenderReceiverInterface (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PortInterface, Referrable
│  │  │  │     │  │  ├─ DiagnosticAuthenticationInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticComControlInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticConditionInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDataElementInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticAbstractDataIdentifierInterface, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDataIdentifierGenericInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticAbstractDataIdentifierInterface, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDataIdentifierInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticAbstractDataIdentifierInterface, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDoIPActivationLineInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDoIPEntityIdentificationInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDoIPGroupIdentificationInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDoIPPowerModeInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDoIPTriggerVehicleAnnouncementInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDownloadInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticDTCInformationInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticEcuResetInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticEventInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticExternalAuthenticationInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticGenericUdsInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticIndicatorInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticMonitorInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticMultipleConditionInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticMultipleResourceInterface, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticMultipleEventInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticMultipleResourceInterface, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticMultipleMonitorInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticMultipleResourceInterface, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticOperationCycleInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticRequestFileTransferInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticRoutineGenericInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticAbstractRoutineInterface, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticRoutineInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticAbstractRoutineInterface, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticSecurityLevelInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticServiceValidationInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticSovdAuthorizationInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, DiagnosticSovdPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticSovdBulkDataInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, DiagnosticSovdPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticSovdConfigurationInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, DiagnosticSovdPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticSovdProximityChallengeInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, DiagnosticSovdPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticSovdServiceValidationInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, DiagnosticSovdPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticSovdUpdateInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, DiagnosticSovdPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ DiagnosticUploadInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, DiagnosticPortInterface, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ FirewallStateSwitchInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ IdsmContextProviderInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, IdsmAbstractPortInterface, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ IdsmTimestampProviderInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, IdsmAbstractPortInterface, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ LogAndTraceInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ ModeSwitchInterface (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ NetworkManagementPortInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ PersistencyFileStorageInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PersistencyInterface, Referrable
│  │  │  │     │  │  ├─ PersistencyKeyValueStorageInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PersistencyInterface, Referrable
│  │  │  │     │  │  ├─ PhmHealthChannelInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PlatformHealthManagementInterface, Referrable
│  │  │  │     │  │  ├─ PhmHealthChannelRecoveryNotificationInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PhmAbstractRecoveryNotificationInterface, PlatformHealthManagementInterface, Referrable
│  │  │  │     │  │  ├─ PhmRecoveryActionInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PlatformHealthManagementInterface, Referrable
│  │  │  │     │  │  ├─ PhmSupervisedEntityInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PlatformHealthManagementInterface, Referrable
│  │  │  │     │  │  ├─ PhmSupervisionRecoveryNotificationInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PhmAbstractRecoveryNotificationInterface, PlatformHealthManagementInterface, Referrable
│  │  │  │     │  │  ├─ RawDataStreamClientInterface (XSD)  + ARElement, AbstractRawDataStreamInterface, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ RawDataStreamServerInterface (XSD)  + ARElement, AbstractRawDataStreamInterface, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ SecurityEventReportInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, IdsmAbstractPortInterface, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ ServiceInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ StateManagemenPhmErrorInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, StateManagementErrorInterface, StateManagementPortInterface, StateManagementRequestInterface
│  │  │  │     │  │  ├─ StateManagementDiagTriggerInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, StateManagementPortInterface, StateManagementRequestInterface, StateManagementTriggerInterface
│  │  │  │     │  │  ├─ StateManagementEmErrorInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, StateManagementErrorInterface, StateManagementPortInterface, StateManagementRequestInterface
│  │  │  │     │  │  ├─ StateManagementFunctionGroupSwitchNotificationInterface (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, StateManagementNotificationInterface, StateManagementPortInterface
│  │  │  │     │  │  ├─ SynchronizedTimeBaseConsumerInterface (XSD)  + ARElement, AbstractSynchronizedTimeBaseInterface, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ SynchronizedTimeBaseProviderInterface (XSD)  + ARElement, AbstractSynchronizedTimeBaseInterface, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  └─ TriggerInterface (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ PortInterfaceMappingSet (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ PortInterfaceToDataTypeMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ PortPrototypeBlueprint (R23-11)  + AtpBlueprint, AtpClassifier, AtpFeature, AtpStructureElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ PostBuildVariantCriterion (R23-11)  + AtpDefinition, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ PostBuildVariantCriterionValueSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ PredefinedVariant (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ Process (XSD)  + AbstractExecutionContext, AtpClassifier, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ ProcessDesign (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ProcessDesignToMachineDesignMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ProcessExecutionError (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ ProcessToMachineMappingSet (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ ProvidedServiceInstanceToSwClusterDesignPPortPrototypeMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, ServiceInstanceToSwClusterDesignPortPrototypeMapping
│  │  │  │     │  ├─ ProvidedSomeipServiceInstance (XSD)  + AdaptivePlatformServiceInstance, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, ProvidedApServiceInstance, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ ProvidedUserDefinedServiceInstance (XSD)  + AdaptivePlatformServiceInstance, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, ProvidedApServiceInstance, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ RapidPrototypingScenario (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ RawDataStreamDeployment (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ RawDataStreamGrantDesign (XSD)  + CollectableElement, GrantDesign, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ RecoveryNotification (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ RecoveryNotificationToPPortPrototypeMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ RequiredServiceInstanceToSwClusterDesignRPortPrototypeMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, ServiceInstanceToSwClusterDesignPortPrototypeMapping
│  │  │  │     │  ├─ RequiredSomeipServiceInstance (XSD)  + AdaptivePlatformServiceInstance, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, RequiredApServiceInstance, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ RequiredUserDefinedServiceInstance (XSD)  + AdaptivePlatformServiceInstance, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, RequiredApServiceInstance, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ SdgDef (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ SecOcSecureComProps (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, SecureComProps, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ SecurityEventMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ SecurityEventReportToSecurityEventDefinitionMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ SerializationTechnology (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ServiceInstanceToPortPrototypeMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ ServiceInstanceToSignalMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ ServiceInterfaceEventMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, ServiceInterfaceElementMapping
│  │  │  │     │  ├─ ServiceInterfaceFieldMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, ServiceInterfaceElementMapping
│  │  │  │     │  ├─ ServiceInterfaceMethodMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, ServiceInterfaceElementMapping
│  │  │  │     │  ├─ ServiceInterfacePedigree (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ ServiceInterfaceTriggerMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, ServiceInterfaceElementMapping
│  │  │  │     │  ├─ ServiceTiming (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TimingExtension
│  │  │  │     │  ├─ SignalServiceTranslationPropsSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ SmInteractsWithNmMapping (XSD)  + CollectableElement, FunctionalClusterInteractsWithFunctionalClusterMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ SocketConnectionIpduIdentifierSet (R23-11)  + CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ SoftwareCluster (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ SoftwareClusterDesign (XSD)  + AtpClassifier, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ SoftwareClusterDiagnosticDeploymentProps (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ SoftwarePackage (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ SomeipDataPrototypeTransformationProps (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ SomeipRemoteMulticastConfig (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ SomeipRemoteUnicastConfig (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ SomeipSdClientEventGroupTimingConfig (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ SomeipSdClientServiceInstanceConfig (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ SomeipSdServerEventGroupTimingConfig (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ SomeipServiceInstanceToMachineMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, ServiceInstanceToMachineMapping, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ SomeipServiceInterfaceDeployment (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, ServiceInterfaceDeployment, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ StartupConfig (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ StateDependentFirewall (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ SwAddrMethod (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ SwAxisType (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ SwcBswMapping (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ SwComponentMappingConstraints (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ SwComponentType (R23-11)  + AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ AdaptiveApplicationSwComponentType (XSD)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  ├─ AtomicSwComponentType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  │  ├─ ApplicationSwComponentType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, SwComponentType
│  │  │  │     │  │  │  ├─ ComplexDeviceDriverSwComponentType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, SwComponentType
│  │  │  │     │  │  │  ├─ EcuAbstractionSwComponentType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, SwComponentType
│  │  │  │     │  │  │  ├─ NvBlockSwComponentType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, SwComponentType
│  │  │  │     │  │  │  ├─ SensorActuatorSwComponentType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, SwComponentType
│  │  │  │     │  │  │  ├─ ServiceProxySwComponentType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, SwComponentType
│  │  │  │     │  │  │  └─ ServiceSwComponentType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, SwComponentType
│  │  │  │     │  │  ├─ CompositionSwComponentType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  │  └─ ParameterSwComponentType (R23-11)  + ARElement, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ SwcTiming (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TimingExtension
│  │  │  │     │  ├─ SwRecordLayout (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ SwSystemconst (R23-11)  + AtpDefinition, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ SwSystemconstantValueSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ System (R23-11)  + AtpClassifier, AtpFeature, AtpStructureElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ SystemSignal (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ SystemSignalGroup (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ TcpOptionFilterSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ TimeBaseProviderToPersistencyMapping (XSD)  + CollectableElement, FunctionalClusterInteractsWithFunctionalClusterMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ TimeSyncPortPrototypeToTimeBaseMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ TlsConnectionGroup (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ TlsIamRemoteSubject (XSD)  + AbstractIamRemoteSubject, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ TlsSecureComProps (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, SecureComProps, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ TlvDataIdDefinitionSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ TransformationPropsSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ TransformationPropsToServiceInterfaceElementMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ UcmToTimeBaseResourceMapping (XSD)  + CollectableElement, FunctionalClusterInteractsWithFunctionalClusterMapping, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ Unit (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ UnitGroup (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     │  ├─ UserDefinedServiceInstanceToMachineMapping (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, ServiceInstanceToMachineMapping, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ UserDefinedServiceInterfaceDeployment (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, ServiceInterfaceDeployment, UploadableDesignElement, UploadablePackageElement
│  │  │  │     │  ├─ VehiclePackage (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDeploymentElement, UploadablePackageElement
│  │  │  │     │  ├─ VfbTiming (R23-11)  + AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TimingExtension
│  │  │  │     │  └─ ViewMapSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │     ├─ EnumerationMappingTable (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     └─ FibexElement (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │        ├─ BusMirrorChannelMapping (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        │  ├─ BusMirrorChannelMappingFlexray (R23-11)  + CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        │  └─ BusMirrorChannelMappingUserDefined (R23-11)  + CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        ├─ ConsumedProvidedServiceInstanceGroup (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        ├─ DltMessageCollectionSet (XSD)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        ├─ DoIpTpConfig (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TpConfig
│  │  │  │        ├─ EcuInstance (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        ├─ EthernetWakeupSleepOnDatalineConfigSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        ├─ EthTpConfig (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TpConfig
│  │  │  │        ├─ FlexrayArTpConfig (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TpConfig
│  │  │  │        ├─ FlexrayTpConfig (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TpConfig
│  │  │  │        ├─ Frame (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        │  ├─ AbstractEthernetFrame (R23-11)  + CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        │  │  ├─ GenericEthernetFrame (R23-11)  + CollectableElement, FibexElement, Frame, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        │  │  ├─ Ieee1722TpEthernetFrame (R23-11)  + CollectableElement, FibexElement, Frame, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        │  │  └─ UserDefinedEthernetFrame (R23-11)  + CollectableElement, FibexElement, Frame, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        │  ├─ CanFrame (R23-11)  + CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        │  ├─ EthernetFrame (XSD)  + CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        │  ├─ FlexrayFrame (R23-11)  + CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        │  └─ LinFrame (R23-11)  + CollectableElement, FibexElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        │     ├─ LinEventTriggeredFrame (R23-11)  + CollectableElement, FibexElement, Frame, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        │     ├─ LinSporadicFrame (R23-11)  + CollectableElement, FibexElement, Frame, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        │     └─ LinUnconditionalFrame (R23-11)  + CollectableElement, FibexElement, Frame, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        ├─ Gateway (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        ├─ ISignalIPduGroup (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        ├─ LinTpConfig (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TpConfig
│  │  │  │        ├─ MachineDesign (XSD)  + ARElement, AtpClassifier, AtpFeature, AtpStructureElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, UploadableDesignElement, UploadablePackageElement
│  │  │  │        ├─ PdurIPduGroup (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        ├─ SecureCommunicationPropsSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        ├─ ServiceInstanceCollectionSet (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        ├─ SoAdRoutingGroup (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable
│  │  │  │        └─ SomeipTpConfig (R23-11)  + CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable, TpConfig
│  │  │  ├─ ComManagementMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ CommConnectorPort (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ FramePort (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ IPduPort (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ CommunicationConnector (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ AbstractCanCommunicationConnector (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ CanCommunicationConnector (R23-11)  + CommunicationConnector, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  └─ TtcanCommunicationConnector (R23-11)  + CommunicationConnector, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ EthernetCommunicationConnector (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ FlexrayCommunicationConnector (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ LinCommunicationConnector (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ CommunicationController (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ AbstractCanCommunicationController (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  └─ CanCommunicationController (R23-11)  + CommunicationController, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ LinCommunicationController (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ LinMaster (R23-11)  + CommunicationController, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  └─ LinSlave (R23-11)  + CommunicationController, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ UserDefinedCommunicationController (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ Compiler (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ConsumedServiceInstance (R23-11)  + AbstractServiceInstance, MultilanguageReferrable, Referrable
│  │  │  ├─ CouplingElementAbstractDetails (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  └─ CouplingElementSwitchDetails (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ CouplingPortAsynchronousTrafficShaper (R23-11)  + CouplingPortAbstractShaper, MultilanguageReferrable, Referrable
│  │  │  ├─ CouplingPortCreditBasedShaper (R23-11)  + CouplingPortAbstractShaper, MultilanguageReferrable, Referrable
│  │  │  ├─ CouplingPortStructuralElement (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ CouplingPortFifo (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ CouplingPortScheduler (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ CouplingPortShaper (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ CpSoftwareClusterResource (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ CpSoftwareClusterCommunicationResource (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ CpSoftwareClusterServiceResource (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ CpSoftwareClusterResourceToApplicationPartitionMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ CpSoftwareClusterToApplicationPartitionMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ CpSoftwareClusterToEcuInstanceMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ CpSoftwareClusterToResourceMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ CryptoCertificate (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ CryptoProvider (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ CryptoServiceMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  └─ SecOcCryptoServiceMapping (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ DataTransformation (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ DdsCpDomain (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ DdsCpPartition (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ DdsCpServiceInstance (R23-11)  + AbstractServiceInstance, MultilanguageReferrable, Referrable
│  │  │  │  └─ DdsCpConsumedServiceInstance (R23-11)  + AbstractServiceInstance, Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ DdsDomainRange (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ DdsEventDeployment (XSD)  + MultilanguageReferrable, Referrable, ServiceEventDeployment
│  │  │  ├─ DdsFieldDeployment (XSD)  + MultilanguageReferrable, Referrable, ServiceFieldDeployment
│  │  │  ├─ DeadlineSupervision (XSD)  + MultilanguageReferrable, PhmSupervision, Referrable
│  │  │  ├─ DependencyOnArtifact (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ DiagEventDebounceAlgorithm (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ DiagEventDebounceCounterBased (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ DiagEventDebounceMonitorInternal (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ DiagEventDebounceTimeBased (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ DiagnosticAuthTransmitCertificateEvaluation (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ DiagnosticDataElement (R23-11)  + DiagnosticServiceMappingDiagTarget, MultilanguageReferrable, Referrable
│  │  │  ├─ DiagnosticDebounceAlgorithmProps (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ DiagnosticFunctionInhibitSource (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ DiagnosticParameterElement (R23-11)  + DiagnosticAbstractParameter, DiagnosticServiceMappingDiagTarget, MultilanguageReferrable, Referrable
│  │  │  ├─ DiagnosticRoutineSubfunction (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ DiagnosticRequestRoutineResults (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ DiagnosticStartRoutine (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ DiagnosticStopRoutine (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ DiagnosticSovdMethodPrimitive (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ DltApplication (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ DltArgument (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ DltLogChannel (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ DltMessage (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ DoIpLogicAddress (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ DoIpRoutingActivation (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ E2EProfileConfiguration (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ EcucContainerValue (R23-11)  + EcucIndexableValue, MultilanguageReferrable, Referrable
│  │  │  ├─ EcucDefinitionElement (R23-11)  + AtpDefinition, MultilanguageReferrable, Referrable
│  │  │  │  ├─ EcucAbstractReferenceDef (R23-11)  + AtpDefinition, EcucCommonAttributes, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ EcucAbstractExternalReferenceDef (R23-11)  + AtpDefinition, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  ├─ EcucForeignReferenceDef (R23-11)  + AtpDefinition, EcucAbstractReferenceDef, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  │  └─ EcucInstanceReferenceDef (R23-11)  + AtpDefinition, EcucAbstractReferenceDef, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  └─ EcucAbstractInternalReferenceDef (R23-11)  + AtpDefinition, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │     ├─ EcucChoiceReferenceDef (R23-11)  + AtpDefinition, EcucAbstractReferenceDef, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │     ├─ EcucReferenceDef (R23-11)  + AtpDefinition, EcucAbstractReferenceDef, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │     ├─ EcucSymbolicNameReferenceDef (R4.3.1)  + AtpDefinition, EcucAbstractReferenceDef, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │     └─ EcucUriReferenceDef (R23-11)  + AtpDefinition, EcucAbstractReferenceDef, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ EcucContainerDef (R23-11)  + AtpDefinition, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ EcucChoiceContainerDef (R23-11)  + AtpDefinition, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  └─ EcucParamConfContainerDef (R23-11)  + AtpDefinition, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ EcucParameterDef (R23-11)  + AtpDefinition, EcucCommonAttributes, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ EcucAbstractStringParamDef (R23-11)  + AtpDefinition, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     │  ├─ EcucFunctionNameDef (R23-11)  + AtpDefinition, EcucCommonAttributes, EcucDefinitionElement, EcucParameterDef, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     │  ├─ EcucLinkerSymbolDef (R23-11)  + AtpDefinition, EcucCommonAttributes, EcucDefinitionElement, EcucParameterDef, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     │  ├─ EcucMultilineStringParamDef (R23-11)  + AtpDefinition, EcucCommonAttributes, EcucDefinitionElement, EcucParameterDef, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     │  └─ EcucStringParamDef (R23-11)  + AtpDefinition, EcucCommonAttributes, EcucDefinitionElement, EcucParameterDef, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ EcucAddInfoParamDef (R23-11)  + AtpDefinition, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ EcucBooleanParamDef (R23-11)  + AtpDefinition, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ EcucEnumerationParamDef (R23-11)  + AtpDefinition, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ EcucFloatParamDef (R23-11)  + AtpDefinition, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     └─ EcucIntegerParamDef (R23-11)  + AtpDefinition, EcucCommonAttributes, EcucDefinitionElement, Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ EcucDestinationUriDef (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ EcucEnumerationLiteralDef (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ EcucQuery (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ EcucValidationCondition (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ECUMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ EcuPartition (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ End2EndEventProtectionProps (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ End2EndMethodProtectionProps (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ EndToEndProtection (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ EOCExecutableEntityRefAbstract (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ EOCExecutableEntityRef (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ EOCExecutableEntityRefGroup (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ EventHandler (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ EventMapping (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ExclusiveArea (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ExecutableEntity (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  └─ BswModuleEntity (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ BswCalledEntity (R23-11)  + ExecutableEntity, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ BswInterruptEntity (R23-11)  + ExecutableEntity, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     └─ BswSchedulableEntity (R23-11)  + ExecutableEntity, Identifiable, MultilanguageReferrable
│  │  │  ├─ ExecutionTime (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ AnalyzedExecutionTime (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ MeasuredExecutionTime (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ SimulatedExecutionTime (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ FieldMapping (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ FireAndForgetMethodMapping (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ FlatInstanceDescriptor (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ FlexrayArTpNode (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ FlexrayNmCluster (R23-11)  + MultilanguageReferrable, NmCluster, Referrable
│  │  │  ├─ FlexrayTpConnectionControl (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ FlexrayTpNode (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ FlexrayTpPduPool (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ FMAttributeDef (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ FMFeatureMapAssertion (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ FMFeatureMapCondition (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ FMFeatureMapElement (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ FMFeatureRelation (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ FMFeatureRestriction (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ FMFeatureSelection (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ FrameTriggering (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ CanFrameTriggering (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ EthernetFrameTriggering (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ LinFrameTriggering (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ GeneralParameter (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ GlobalSupervision (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ GlobalTimeCanSlave (R23-11)  + GlobalTimeSlave, MultilanguageReferrable, Referrable
│  │  │  ├─ GlobalTimeEthSlave (R23-11)  + GlobalTimeSlave, MultilanguageReferrable, Referrable
│  │  │  ├─ GlobalTimeFrSlave (R23-11)  + GlobalTimeSlave, MultilanguageReferrable, Referrable
│  │  │  ├─ GlobalTimeGateway (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ GlobalTimeMaster (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ GlobalTimeCanMaster (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ GlobalTimeEthMaster (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ GlobalTimeFrMaster (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ UserDefinedGlobalTimeMaster (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ HealthChannelExternalStatus (XSD)  + HealthChannel, MultilanguageReferrable, Referrable
│  │  │  ├─ HealthChannelSupervision (XSD)  + HealthChannel, MultilanguageReferrable, Referrable
│  │  │  ├─ HeapUsage (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ RoughEstimateHeapUsage (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ WorstCaseHeapUsage (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ HwAttributeDef (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ HwAttributeLiteralDef (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ HwPin (R23-11)  + HwDescriptionEntity, MultilanguageReferrable, Referrable
│  │  │  ├─ HwPinGroup (R23-11)  + HwDescriptionEntity, MultilanguageReferrable, Referrable
│  │  │  ├─ IdsmRateLimitation (R23-11)  + AbstractSecurityIdsmInstanceFilter, MultilanguageReferrable, Referrable
│  │  │  ├─ IEEE1722TpAcfBus (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  └─ IEEE1722TpAcfCan (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ IEEE1722TpAcfCanPart (R23-11)  + IEEE1722TpAcfBusPart, MultilanguageReferrable, Referrable
│  │  │  ├─ IEEE1722TpAcfLinPart (R23-11)  + IEEE1722TpAcfBusPart, MultilanguageReferrable, Referrable
│  │  │  ├─ IPSecRule (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ISignalTriggering (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ J1939NmCluster (R23-11)  + MultilanguageReferrable, NmCluster, Referrable
│  │  │  ├─ J1939SharedAddressCluster (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ J1939TpNode (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ Keyword (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ Linker (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ LinNmCluster (R4.3.1)  + MultilanguageReferrable, NmCluster, Referrable
│  │  │  ├─ LinScheduleTable (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ LinTpNode (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ LogicAddress (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ LogicalSupervision (XSD)  + MultilanguageReferrable, PhmSupervision, Referrable
│  │  │  ├─ MacSecKayParticipant (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ McDataInstance (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ MemorySection (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ MemoryUsage (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ MethodMapping (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ NetworkEndpoint (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ NmEcu (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ NmNode (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ CanNmNode (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ FlexrayNmNode (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ J1939NmNode (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ NoCheckpointSupervision (XSD)  + MultilanguageReferrable, PhmSupervision, Referrable
│  │  │  ├─ NoSupervision (XSD)  + MultilanguageReferrable, PhmSupervision, Referrable
│  │  │  ├─ PduActivationRoutingGroup (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ PduTriggering (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ PersistencyFile (XSD)  + MultilanguageReferrable, PersistencyDeploymentElement, Referrable
│  │  │  ├─ PersistencyFileElement (XSD)  + MultilanguageReferrable, PersistencyInterfaceElement, Referrable
│  │  │  ├─ PersistencyKeyValuePair (XSD)  + MultilanguageReferrable, PersistencyDeploymentElement, Referrable
│  │  │  ├─ PhmCheckpoint (XSD)  + AtpFeature, MultilanguageReferrable, Referrable
│  │  │  ├─ PhmHealthChannelStatus (XSD)  + AtpFeature, MultilanguageReferrable, Referrable
│  │  │  ├─ PhysicalChannel (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ AbstractCanPhysicalChannel (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ CanPhysicalChannel (R23-11)  + Identifiable, MultilanguageReferrable, PhysicalChannel, Referrable
│  │  │  │  │  └─ TtcanPhysicalChannel (R23-11)  + Identifiable, MultilanguageReferrable, PhysicalChannel, Referrable
│  │  │  │  ├─ EthernetPhysicalChannel (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ FlexrayPhysicalChannel (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ UserDefinedPhysicalChannel (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ PortElementToCommunicationResourceMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ PossibleErrorReaction (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ Processor (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ProcessorCore (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ProcessToMachineMapping (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ PskIdentityToKeySlotMapping (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ResourceGroup (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ RptComponent (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ RptContainer (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ RptExecutableEntity (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ RptExecutableEntityEvent (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ RptExecutionContext (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ RptServicePoint (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ RteEventInCompositionSeparation (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ RteEventInSystemSeparation (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SdgAttribute (R23-11)  + AbstractMultiplicityRestriction, MultilanguageReferrable, Referrable
│  │  │  │  ├─ SdgAbstractForeignReference (R23-11)  + AbstractMultiplicityRestriction, Identifiable, MultilanguageReferrable, Referrable, SdgElementWithGid
│  │  │  │  │  ├─ SdgForeignReference (R23-11)  + AbstractMultiplicityRestriction, Identifiable, MultilanguageReferrable, Referrable, SdgAttribute, SdgElementWithGid
│  │  │  │  │  └─ SdgForeignReferenceWithVariation (R23-11)  + AbstractMultiplicityRestriction, AbstractVariationRestriction, Identifiable, MultilanguageReferrable, Referrable, SdgAttribute, SdgElementWithGid
│  │  │  │  ├─ SdgAbstractPrimitiveAttribute (R23-11)  + AbstractMultiplicityRestriction, AbstractValueRestriction, Identifiable, MultilanguageReferrable, Referrable, SdgElementWithGid
│  │  │  │  │  ├─ SdgPrimitiveAttribute (R23-11)  + AbstractMultiplicityRestriction, AbstractValueRestriction, Identifiable, MultilanguageReferrable, Referrable, SdgAttribute, SdgElementWithGid
│  │  │  │  │  └─ SdgPrimitiveAttributeWithVariation (R23-11)  + AbstractMultiplicityRestriction, AbstractValueRestriction, AbstractVariationRestriction, Identifiable, MultilanguageReferrable, Referrable, SdgAttribute, SdgElementWithGid
│  │  │  │  ├─ SdgAggregationWithVariation (R23-11)  + AbstractMultiplicityRestriction, AbstractVariationRestriction, Identifiable, MultilanguageReferrable, Referrable, SdgElementWithGid
│  │  │  │  └─ SdgReference (R23-11)  + AbstractMultiplicityRestriction, Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ SdgClass (R23-11)  + MultilanguageReferrable, Referrable, SdgElementWithGid
│  │  │  ├─ SecOcDeployment (XSD)  + MultilanguageReferrable, Referrable, SecureCommunicationDeployment
│  │  │  ├─ SecOcJobMapping (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SecOcJobRequirement (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SecureCommunicationAuthenticationProps (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ServiceInterfaceElementSecureComConfig (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ServiceNeeds (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ BswMgrNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ ComMgrUserNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ CryptoCertificateKeySlotNeeds (XSD)  + CryptoNeeds, Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ CryptoKeyManagementNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ CryptoServiceJobNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ CryptoServiceNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ DiagnosticCapabilityElement (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ DiagnosticClearConditionNeeds (XSD)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticCommunicationManagerNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticComponentNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticControlNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticEnableConditionNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticEventInfoNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticEventManagerNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticEventNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticGenericUdsNeeds (XSD)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticIndicatorNeeds (XSD)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticIoControlNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticOperationCycleNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticRequestFileTransferNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticResponseOnEventNeeds (XSD)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticRoutineNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticsCommunicationSecurityNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticStorageConditionNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticUploadDownloadNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DiagnosticValueNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DtcStatusChangeNotificationNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ ObdControlServiceNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ ObdInfoServiceNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ ObdMonitorServiceNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ ObdPidServiceNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ ObdRatioServiceNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  └─ WarningIndicatorRequestedBitNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  ├─ DltUserNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ DoIpServiceNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ DoIpActivationLineNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DoIpGidNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DoIpGidSynchronizationNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DoIpPowerModeStatusNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DoIpRoutingActivationAuthenticationNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  ├─ DoIpRoutingActivationConfirmationNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  │  └─ FurtherActionByteNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, ServiceNeeds
│  │  │  │  ├─ EcuStateMgrUserNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ ErrorTracerNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ FunctionInhibitionAvailabilityNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ FunctionInhibitionNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ GlobalSupervisionNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ HardwareTestNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ IdsMgrCustomTimestampNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ IdsMgrNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ IndicatorStatusNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ J1939DcmDm19Support (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ J1939RmIncomingRequestServiceNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ J1939RmOutgoingRequestServiceNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ NvBlockNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ SecureOnBoardCommunicationNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ SupervisedEntityCheckpointNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ SupervisedEntityNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ SyncTimeBaseMgrUserNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ V2xDataManagerNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ V2xFacUserNeeds (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ SignalBasedEventElementToISignalTriggeringMapping (XSD)  + AbstractSignalBasedToISignalTriggeringMapping, MultilanguageReferrable, Referrable
│  │  │  ├─ SignalBasedFieldToISignalTriggeringMapping (XSD)  + AbstractSignalBasedToISignalTriggeringMapping, MultilanguageReferrable, Referrable
│  │  │  ├─ SignalBasedFireAndForgetMethodToISignalTriggeringMapping (XSD)  + AbstractSignalBasedToISignalTriggeringMapping, MultilanguageReferrable, Referrable
│  │  │  ├─ SignalBasedMethodToISignalTriggeringMapping (XSD)  + AbstractSignalBasedToISignalTriggeringMapping, MultilanguageReferrable, Referrable
│  │  │  ├─ SignalBasedTriggerToISignalTriggeringMapping (XSD)  + AbstractSignalBasedToISignalTriggeringMapping, MultilanguageReferrable, Referrable
│  │  │  ├─ SignalServiceTranslationElementProps (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SignalServiceTranslationEventProps (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SignalServiceTranslationProps (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SoftwarePackageStep (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SomeipEventDeployment (XSD)  + MultilanguageReferrable, Referrable, ServiceEventDeployment
│  │  │  ├─ SomeipEventGroup (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SomeipFieldDeployment (XSD)  + MultilanguageReferrable, Referrable, ServiceFieldDeployment
│  │  │  ├─ SomeipMethodDeployment (XSD)  + MultilanguageReferrable, Referrable, ServiceMethodDeployment
│  │  │  ├─ SomeipProvidedEventGroup (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SomeipTpChannel (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SOMEIPTransformationProps (R23-11)  + MultilanguageReferrable, Referrable, TransformationProps
│  │  │  ├─ SpecElementReference (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ DataFormatElementReference (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  │  ├─ AbstractClassTailoring (R23-11)  + ClassTailoring, Identifiable, MultilanguageReferrable, Referrable, SpecElementReference
│  │  │  │  │  └─ DataFormatElementScope (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, SpecElementReference, SpecElementScope
│  │  │  │  │     ├─ AttributeTailoring (R23-11)  + DataFormatElementReference, Identifiable, MultilanguageReferrable, Referrable, SpecElementReference, SpecElementScope
│  │  │  │  │     │  ├─ AggregationTailoring (R23-11)  + DataFormatElementReference, DataFormatElementScope, Identifiable, MultilanguageReferrable, Referrable, SpecElementReference, SpecElementScope
│  │  │  │  │     │  ├─ PrimitiveAttributeTailoring (R23-11)  + DataFormatElementReference, DataFormatElementScope, Identifiable, MultilanguageReferrable, Referrable, SpecElementReference, SpecElementScope
│  │  │  │  │     │  └─ ReferenceTailoring (R23-11)  + DataFormatElementReference, DataFormatElementScope, Identifiable, MultilanguageReferrable, Referrable, SpecElementReference, SpecElementScope
│  │  │  │  │     ├─ ConcreteClassTailoring (R23-11)  + ClassTailoring, DataFormatElementReference, Identifiable, MultilanguageReferrable, Referrable, SpecElementReference, SpecElementScope
│  │  │  │  │     ├─ ConstraintTailoring (R23-11)  + DataFormatElementReference, Identifiable, MultilanguageReferrable, Referrable, RestrictionWithSeverity, SpecElementReference, SpecElementScope
│  │  │  │  │     └─ SdgTailoring (R23-11)  + DataFormatElementReference, Identifiable, MultilanguageReferrable, Referrable, RestrictionWithSeverity, SpecElementReference, SpecElementScope
│  │  │  │  └─ SpecElementScope (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ DocumentElementScope (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, SpecElementReference
│  │  │  │     └─ SpecificationDocumentScope (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, SpecElementReference
│  │  │  ├─ StackUsage (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ MeasuredStackUsage (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ RoughEstimateStackUsage (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ WorstCaseStackUsage (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ StateManagementActionList (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ StateManagementNmActionItem (XSD)  + MultilanguageReferrable, Referrable, StateManagementActionItem
│  │  │  ├─ StateManagementRequestError (XSD)  + MultilanguageReferrable, Referrable, StateManagementStateRequest
│  │  │  ├─ StateManagementRequestTrigger (XSD)  + MultilanguageReferrable, Referrable, StateManagementStateRequest
│  │  │  ├─ StateManagementSetFunctionGroupStateActionItem (XSD)  + MultilanguageReferrable, Referrable, StateManagementActionItem
│  │  │  ├─ StateManagementSleepActionItem (XSD)  + MultilanguageReferrable, Referrable, StateManagementActionItem
│  │  │  ├─ StateManagementStateMachineActionItem (XSD)  + MultilanguageReferrable, Referrable, StateManagementActionItem
│  │  │  ├─ StateManagementSyncActionItem (XSD)  + MultilanguageReferrable, Referrable, StateManagementActionItem
│  │  │  ├─ StructuredReq (R23-11)  + DocumentViewSelectable, MultilanguageReferrable, Paginateable, Referrable, Traceable
│  │  │  ├─ SupervisionCheckpoint (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SupervisionMode (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SupervisionModeCondition (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SwcToApplicationPartitionMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SwcToEcuMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SwcToImplMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SwGenericAxisParamType (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SwitchAsynchronousTrafficShaperGroupEntry (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SwitchFlowMeteringEntry (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SwitchStreamFilterActionDestPortModification (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SwitchStreamFilterEntry (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SwitchStreamFilterRule (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SwitchStreamGateEntry (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SwitchStreamIdentification (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SwServiceArg (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SynchronizedTimeBaseConsumer (XSD)  + MultilanguageReferrable, Referrable, TimeBaseResource
│  │  │  ├─ SynchronizedTimeBaseProvider (XSD)  + MultilanguageReferrable, Referrable, TimeBaseResource
│  │  │  ├─ SystemSignalGroupToCommunicationResourceMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ SystemSignalToCommunicationResourceMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ TcpOptionFilterList (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ TDCpSoftwareClusterMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ TDCpSoftwareClusterResourceMapping (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ TimingClock (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  └─ TDLETZoneClock (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ TimingClockSyncAccuracy (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ TimingCondition (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ TimingConstraint (R23-11)  + MultilanguageReferrable, Referrable, Traceable
│  │  │  │  ├─ AgeConstraint (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, Traceable
│  │  │  │  ├─ EventTriggeringConstraint (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, Traceable
│  │  │  │  │  ├─ BurstPatternEventTriggering (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingConstraint, Traceable
│  │  │  │  │  ├─ PeriodicEventTriggering (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingConstraint, Traceable
│  │  │  │  │  └─ SporadicEventTriggering (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingConstraint, Traceable
│  │  │  │  ├─ ExecutionOrderConstraint (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, Traceable
│  │  │  │  ├─ ExecutionTimeConstraint (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, Traceable
│  │  │  │  ├─ LatencyTimingConstraint (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, Traceable
│  │  │  │  ├─ OffsetTimingConstraint (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, Traceable
│  │  │  │  ├─ SynchronizationPointConstraint (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, Traceable
│  │  │  │  └─ SynchronizationTimingConstraint (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, Traceable
│  │  │  ├─ TimingDescription (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  └─ TimingDescriptionEvent (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │     ├─ TDEventBsw (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription
│  │  │  │     │  └─ TDEventBswModule (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription, TimingDescriptionEvent
│  │  │  │     ├─ TDEventBswInternalBehavior (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription
│  │  │  │     ├─ TDEventCom (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription
│  │  │  │     │  ├─ TDEventCycleStart (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription, TimingDescriptionEvent
│  │  │  │     │  │  ├─ TDEventFrClusterCycleStart (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TDEventCom, TimingDescription, TimingDescriptionEvent
│  │  │  │     │  │  └─ TDEventTTCanCycleStart (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TDEventCom, TimingDescription, TimingDescriptionEvent
│  │  │  │     │  ├─ TDEventFrameEthernet (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription, TimingDescriptionEvent
│  │  │  │     │  ├─ TDEventIPdu (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription, TimingDescriptionEvent
│  │  │  │     │  └─ TDEventISignal (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription, TimingDescriptionEvent
│  │  │  │     ├─ TDEventComplex (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription
│  │  │  │     ├─ TDEventServiceInstanceDiscovery (XSD)  + Identifiable, MultilanguageReferrable, Referrable, TDEventServiceInstance, TimingDescription
│  │  │  │     ├─ TDEventServiceInstanceEvent (XSD)  + Identifiable, MultilanguageReferrable, Referrable, TDEventServiceInstance, TimingDescription
│  │  │  │     ├─ TDEventServiceInstanceField (XSD)  + Identifiable, MultilanguageReferrable, Referrable, TDEventServiceInstance, TimingDescription
│  │  │  │     ├─ TDEventServiceInstanceMethod (XSD)  + Identifiable, MultilanguageReferrable, Referrable, TDEventServiceInstance, TimingDescription
│  │  │  │     ├─ TDEventSLLET (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription
│  │  │  │     │  └─ TDEventSLLETPort (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription, TimingDescriptionEvent
│  │  │  │     ├─ TDEventSwc (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription
│  │  │  │     │  └─ TDEventSwcInternalBehaviorReference (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription, TimingDescriptionEvent
│  │  │  │     └─ TDEventVfb (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription
│  │  │  │        ├─ TDEventVfbPort (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription, TimingDescriptionEvent
│  │  │  │        │  ├─ TDEventModeDeclaration (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TDEventVfb, TimingDescription, TimingDescriptionEvent
│  │  │  │        │  ├─ TDEventOperation (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TDEventVfb, TimingDescription, TimingDescriptionEvent
│  │  │  │        │  └─ TDEventTrigger (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TDEventVfb, TimingDescription, TimingDescriptionEvent
│  │  │  │        └─ TDEventVfbReference (R23-11)  + Identifiable, MultilanguageReferrable, Referrable, TimingDescription, TimingDescriptionEvent
│  │  │  ├─ TimingModeInstance (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ TlsCryptoCipherSuite (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ TlsCryptoCipherSuiteProps (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ TlsDeployment (XSD)  + MultilanguageReferrable, Referrable, SecureCommunicationDeployment
│  │  │  ├─ TlsJobMapping (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ Topic1 (R23-11)  + DocumentViewSelectable, MultilanguageReferrable, Paginateable, Referrable
│  │  │  ├─ TpAddress (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ TraceableTable (XSD)  + DocumentViewSelectable, MultilanguageReferrable, Paginateable, Referrable, Traceable
│  │  │  ├─ TraceableText (R23-11)  + DocumentViewSelectable, MultilanguageReferrable, Paginateable, Referrable, Traceable
│  │  │  ├─ TracedFailure (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  │  ├─ DevelopmentError (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  ├─ RuntimeError (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  │  └─ TransientFault (R23-11)  + Identifiable, MultilanguageReferrable, Referrable
│  │  │  ├─ TransformationTechnology (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ UcmDescription (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ UcmRetryStrategy (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ UcmStep (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ UdpNmCluster (R23-11)  + MultilanguageReferrable, NmCluster, Referrable
│  │  │  ├─ UserDefinedEventDeployment (XSD)  + MultilanguageReferrable, Referrable, ServiceEventDeployment
│  │  │  ├─ UserDefinedFieldDeployment (XSD)  + MultilanguageReferrable, Referrable, ServiceFieldDeployment
│  │  │  ├─ UserDefinedGlobalTimeSlave (R23-11)  + GlobalTimeSlave, MultilanguageReferrable, Referrable
│  │  │  ├─ UserDefinedMethodDeployment (XSD)  + MultilanguageReferrable, Referrable, ServiceMethodDeployment
│  │  │  ├─ UserDefinedTransformationProps (R23-11)  + MultilanguageReferrable, Referrable, TransformationProps
│  │  │  ├─ VariationPointProxy (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ VehicleRolloutStep (XSD)  + MultilanguageReferrable, Referrable
│  │  │  ├─ ViewMap (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  ├─ VlanConfig (R23-11)  + MultilanguageReferrable, Referrable
│  │  │  └─ WaitPoint (R23-11)  + MultilanguageReferrable, Referrable
│  │  ├─ SdgCaption (R23-11)  + Referrable
│  │  └─ Traceable (R23-11)  + Referrable
│  ├─ NmNetworkHandle (XSD)
│  ├─ PncMappingIdent (R23-11)
│  ├─ SingleLanguageReferrable (R23-11)
│  │  ├─ Std (R23-11)  + Referrable
│  │  ├─ Xdoc (R23-11)  + Referrable
│  │  └─ XrefTarget (R23-11)  + Referrable
│  ├─ SocketConnectionBundle (R4.3.1)
│  ├─ SoConIPduIdentifier (R23-11)
│  ├─ SomeipRequiredEventGroup (XSD)
│  ├─ TimeSyncServerConfiguration (R23-11)
│  └─ TpConnectionIdent (R23-11)
├─ ReferrableSubtypesEnum (R23-11)
├─ RegularExpression (R23-11)
├─ RemotingTechnology (XSD)
├─ RemotingTechnologyEnum (XSD)
├─ ReportBehaviorEnum (XSD)
├─ RequestMethodEnum (XSD)
├─ RequestResponseDelay (R23-11)
├─ RequestTypeEnum (XSD)
├─ RequiredApServiceInstance (XSD)
├─ ResolutionPolicyEnum (R23-11)
├─ ResourceConsumption (R23-11)
├─ RestrictionWithSeverity (R23-11)
│  └─ UnresolvedReferenceRestrictionWithSeverity (R23-11)
├─ ResumePosition (R23-11)
├─ RevisionLabelString (R23-11)
├─ RoleBasedBswModuleEntryAssignment (R23-11)
├─ RoleBasedDataAssignment (R23-11)
├─ RoleBasedDataTypeAssignment (R23-11)
├─ RoleBasedMcDataAssignment (R23-11)
├─ RoleBasedPortAssignment (R23-11)
├─ RoleBasedResourceDependency (R23-11)
├─ RoughEstimateOfExecutionTime (R23-11)
├─ RPortComSpec (R23-11)
│  ├─ ClientComSpec (R23-11)
│  ├─ ModeSwitchReceiverComSpec (R23-11)
│  ├─ NvRequireComSpec (R23-11)
│  ├─ ParameterRequireComSpec (R23-11)
│  ├─ PersistencyDataRequiredComSpec (XSD)
│  └─ ReceiverComSpec (R23-11)
│     ├─ NonqueuedReceiverComSpec (R23-11)  + RPortComSpec
│     └─ QueuedReceiverComSpec (R23-11)  + RPortComSpec
├─ RptAccessEnum (R23-11)
├─ RptEnablerImplTypeEnum (R23-11)
├─ RptExecutableEntityProperties (R23-11)
├─ RptExecutionControlEnum (R23-11)
├─ RptHook (R23-11)
├─ RptImplPolicy (R23-11)
├─ RptPreparationEnum (R23-11)
├─ RptProfile (R23-11)
├─ RptServicePointEnum (R23-11)
├─ RptSupportData (R23-11)
├─ RptSwPrototypingAccess (R23-11)
├─ RteApiReturnValueProvisionEnum (R23-11)
├─ RteEventInCompositionToOsTaskProxyMapping (R23-11)
├─ RteEventInSystemToOsTaskProxyMapping (R23-11)
├─ RtePluginProps (R23-11)
├─ RuleArguments (R23-11)
├─ RuleBasedAxisCont (R23-11)
├─ RuleBasedValueCont (R23-11)
├─ RuleBasedValueSpecification (R23-11)
├─ RunMode (R23-11)
├─ RunnableEntity (R23-11)
├─ RunnableEntityArgument (R23-11)
├─ RuntimeAddressConfigurationEnum (R4.3.1)
├─ RxAcceptContainedIPduEnum (R23-11)
├─ RxIdentifierRange (R23-11)
├─ ScaleConstr (R23-11)
├─ ScaleConstrValidityEnum (R4.3.1)
├─ ScheduleTableEntry (R23-11)
│  ├─ ApplicationEntry (R23-11)
│  └─ LinConfigurationEntry (R23-11)
│     ├─ AssignFrameId (R23-11)  + ScheduleTableEntry
│     ├─ AssignFrameIdRange (R23-11)  + ScheduleTableEntry
│     ├─ AssignNad (R23-11)  + ScheduleTableEntry
│     ├─ ConditionalChangeNad (R23-11)  + ScheduleTableEntry
│     ├─ DataDumpEntry (R23-11)  + ScheduleTableEntry
│     ├─ SaveConfigurationEntry (R23-11)  + ScheduleTableEntry
│     └─ UnassignFrameId (R23-11)  + ScheduleTableEntry
├─ Sd (R23-11)
├─ SdClientConfig (R4.3.1)
├─ Sdf (R23-11)
├─ Sdg (R23-11)
├─ SdgContents (R23-11)
├─ SdgElementWithGid (R23-11)
├─ SdServerConfig (R4.3.1)
├─ SearchIntentionEnum (XSD)
├─ SecOcJobSemanticEnum (XSD)
├─ SectionInitializationPolicyType (R23-11)
├─ SecureCommunicationDeployment (XSD)
├─ SecureCommunicationFreshnessProps (R23-11)
├─ SecureCommunicationProps (R23-11)
├─ SecureComProps (XSD)
├─ SecuredIPdu (R23-11)
├─ SecuredPduHeaderEnum (R23-11)
├─ SecurityEventAggregationFilter (R23-11)
├─ SecurityEventContextData (R23-11)
├─ SecurityEventContextDataSourceEnum (R23-11)
├─ SecurityEventContextMapping (R23-11)
├─ SecurityEventContextMappingCommConnector (R23-11)
├─ SecurityEventContextProps (R23-11)
├─ SecurityEventFilterChain (R23-11)
├─ SecurityEventReportingModeEnum (R23-11)
├─ SecurityEventStateFilter (R23-11)
├─ SegmentPosition (R23-11)
├─ SenderIntentEnum (XSD)
├─ SenderRecArrayElementMapping (R23-11)
├─ SenderRecCompositeTypeMapping (R23-11)
│  └─ SenderRecArrayTypeMapping (R23-11)
├─ SenderRecRecordElementMapping (R23-11)
├─ SenderRecRecordTypeMapping (R23-11)
├─ SendIndicationEnum (R23-11)
├─ SequenceCounterMapping (XSD)
├─ SerializationTechnologyEnum (XSD)
├─ ServerArgumentImplPolicyEnum (R23-11)
├─ ServiceDependency (R23-11)
│  └─ BswServiceDependency (R23-11)
├─ ServiceDiagnosticRelevanceEnum (R23-11)
├─ ServiceDiscoveryConfiguration (XSD)
│  └─ SomeipServiceDiscovery (XSD)
├─ ServiceEventDeployment (XSD)
├─ ServiceFieldDeployment (XSD)
├─ ServiceInstanceToMachineMapping (XSD)
├─ ServiceInstanceToSwClusterDesignPortPrototypeMapping (XSD)
├─ ServiceInterfaceDeployment (XSD)
├─ ServiceInterfaceElementMapping (XSD)
├─ ServiceMethodDeployment (XSD)
├─ ServiceProviderEnum (R23-11)
├─ ServiceVersionAcceptanceKindEnum (R23-11)
├─ SeverityEnum (R23-11)
├─ ShortNameFragment (R23-11)
├─ ShowContentEnum (R23-11)
├─ ShowResourceAliasNameEnum (R23-11)
├─ ShowResourceCategoryEnum (R23-11)
├─ ShowResourceLongNameEnum (R23-11)
├─ ShowResourceNumberEnum (R23-11)
├─ ShowResourcePageEnum (R23-11)
├─ ShowResourceShortNameEnum (R23-11)
├─ ShowResourceTypeEnum (R23-11)
├─ ShowSeeEnum (R23-11)
├─ SignalFanEnum (R23-11)
├─ SignalIPduCounter (XSD)
├─ SignalIPduReplication (XSD)
├─ SignalPathConstraint (R23-11)
│  ├─ CommonSignalPath (R23-11)
│  ├─ ForbiddenSignalPath (R23-11)
│  ├─ PermissibleSignalPath (R23-11)
│  └─ SeparateSignalPath (R23-11)
├─ SignalServiceTranslationControlEnum (R23-11)
├─ SingleLanguageUnitNames (R23-11)
├─ SoAdConfig (R23-11)
├─ SoAdConnectorType (XSD)
├─ SoAdProtocolType (XSD)
├─ SocketAddress (R23-11)
├─ SocketConnectionIpduIdentifier (R4.3.1)
├─ SoftwareClusterDependencyFormulaPart (XSD)
│  ├─ SoftwareClusterDependencyCompareCondition (XSD)
│  └─ SoftwareClusterDependencyFormula (XSD)
├─ SoftwareClusterDependencyLogicalOperatorEnum (XSD)
├─ SoftwareClusterDependencyOperatorEnum (XSD)
├─ SoftwareClusterDiagnosticAddress (XSD)
│  ├─ SoftwareClusterDoipDiagnosticAddress (XSD)
│  ├─ SoftwareClusterSovdAddress (XSD)
│  └─ SoftwareClusterUdsDiagnosticAddress (XSD)
├─ SoftwareClusterDiagnosticAddressSemanticsEnum (XSD)
├─ SoftwareClusterInstallationBehaviorEnum (XSD)
├─ SoftwareContext (R23-11)
├─ SoftwarePackageActionTypeEnum (XSD)
├─ SoftwarePackageActivationActionEnum (XSD)
├─ SoftwarePackageStoring (XSD)
├─ SoftwarePackageStoringEnum (XSD)
├─ SomeipCollectionProps (XSD)
├─ SomeipEventProps (XSD)
├─ SOMEIPMessageTypeEnum (R23-11)
├─ SomeipMethodProps (XSD)
├─ SomeipProtocolRule (XSD)
├─ SomeipSdRule (XSD)
├─ SomeipSdServerServiceInstanceConfig (R23-11)
├─ SomeipServiceVersion (R23-11)
├─ SomeipTpConnection (R23-11)
├─ SOMEIPTransformationISignalPropsContent (XSD)
├─ SOMEIPTransformerSessionHandlingEnum (XSD)
├─ SovdGatewayEthernetCredentials (XSD)
│  └─ SovdGatewayLocalEndpointTcpConfig (XSD)
├─ SovdModuleInstantiation (XSD)
├─ SpecificationScope (R23-11)
├─ StandardNameEnum (R23-11)
├─ StateDependentStartupConfig (XSD)
├─ StateManagementActionItem (XSD)
├─ StateManagementCompareCondition (XSD)
├─ StateManagementCompareEnum (XSD)
├─ StateManagementCompareFormulaPart (XSD)
│  ├─ StateManagementCompareFormula (XSD)
│  ├─ StateManagementErrorCompareRule (XSD)  + StateManagementCompareCondition
│  └─ StateManagementTriggerCompareRule (XSD)  + StateManagementCompareCondition
├─ StateManagementErrorInterface (XSD)
├─ StateManagementLogicalOperatorEnum (XSD)
├─ StateManagementNotificationInterface (XSD)
├─ StateManagementPortInterface (XSD)
├─ StateManagementRequestInterface (XSD)
├─ StateManagementRequestRule (XSD)
├─ StateManagementStateRequest (XSD)
├─ StateManagementTriggerInterface (XSD)
├─ StaticSocketConnection (R23-11)
├─ StorageConditionStatusEnum (R23-11)
├─ StreamFilterIEEE1722Tp (R23-11)
├─ StreamFilterIpv4Address (R23-11)
├─ StreamFilterIpv6Address (R23-11)
├─ StreamFilterMACAddress (R23-11)
├─ StreamFilterPortRange (R23-11)
├─ StreamFilterRuleDataLinkLayer (R23-11)
├─ StreamFilterRuleIpTp (R23-11)
├─ String (R23-11)
├─ SubElementMapping (R23-11)
├─ SubElementRef (R23-11)
│  ├─ ApplicationCompositeDataTypeSubElementRef (R23-11)
│  └─ ImplementationDataTypeSubElementRef (R23-11)
├─ Superscript (R23-11)
├─ SupportBufferLockingEnum (R23-11)
├─ SwAxisCont (R23-11)
├─ SwAxisGeneric (R23-11)
├─ SwBitRepresentation (R23-11)
├─ SwCalibrationAccessEnum (R23-11)
├─ SwCalprmAxis (R23-11)
├─ SwCalprmAxisSet (R23-11)
├─ SwCalprmAxisTypeProps (R23-11)
│  ├─ SwAxisGrouped (R23-11)
│  └─ SwAxisIndividual (R23-11)
├─ SwCalprmRefProxy (R23-11)
├─ SwcBswRunnableMapping (R23-11)
├─ SwcBswSynchronizedModeGroupPrototype (R23-11)
├─ SwcBswSynchronizedTrigger (R23-11)
├─ SwcExclusiveAreaPolicy (R23-11)
├─ SwcInternalBehavior (R23-11)
├─ SwcModeManagerErrorEvent (R23-11)
├─ SwComponentDocumentation (R23-11)
├─ SwComponentPrototypeAssignment (R23-11)
├─ SwcSupportedFeature (R23-11)
│  └─ CommunicationBufferLocking (R23-11)
├─ SwcToEcuMappingConstraintType (XSD)
├─ SwcToSwcOperationArguments (R23-11)
├─ SwcToSwcOperationArgumentsDirectionEnum (R23-11)
├─ SwcToSwcSignal (R23-11)
├─ SwDataDefProps (R23-11)
├─ SwDataDefPropsContent (XSD)
│  └─ SwDataDefPropsConditional (XSD)
├─ SwDataDependency (R23-11)
├─ SwDataDependencyArgs (R23-11)
├─ SwGenericAxisParam (R23-11)
├─ SwImplPolicyEnum (R23-11)
├─ SwitchStreamFilterActionPortModificationEnum (R23-11)
├─ SwPointerTargetProps (R23-11)
├─ SwRecordLayoutGroup (R23-11)
├─ SwRecordLayoutGroupContent (R23-11)
├─ SwRecordLayoutV (R23-11)
├─ SwServiceImplPolicyEnum (R23-11)
├─ SwServiceReentranceEnum (XSD)
├─ SwSystemconstValue (R23-11)
├─ SwTextProps (R23-11)
├─ SwValueCont (R23-11)
├─ SwValues (R23-11)
├─ SwVariableAccessImplPolicyEnum (XSD)
├─ SwVariableRefProxy (R23-11)
├─ SymbolString (R23-11)
├─ SynchronizationTypeEnum (R23-11)
├─ SystemMapping (R23-11)
├─ SystemTiming (R23-11)
├─ Table (R23-11)
├─ TableSeparatorString (R23-11)
├─ TagWithOptionalValue (R23-11)
├─ TargetIPduRef (R23-11)
├─ Tbody (R23-11)
├─ TcpIpIcmpv4Props (R23-11)
├─ TcpIpIcmpv6Props (R23-11)
├─ TcpProps (R23-11)
├─ TcpRoleEnum (R23-11)
├─ TDCpSoftwareClusterMappingSet (R23-11)
├─ TDEventBswInternalBehaviorTypeEnum (R23-11)
├─ TDEventBswModeDeclaration (R23-11)
├─ TDEventBswModeDeclarationTypeEnum (R23-11)
├─ TDEventBswModuleTypeEnum (R23-11)
├─ TDEventFrame (R23-11)
├─ TDEventFrameEthernetTypeEnum (R23-11)
├─ TDEventFrameTypeEnum (R23-11)
├─ TDEventIPduTypeEnum (R23-11)
├─ TDEventISignalTypeEnum (R23-11)
├─ TDEventModeDeclarationTypeEnum (R23-11)
├─ TDEventOccurrenceExpression (R23-11)
├─ TDEventOperationTypeEnum (R23-11)
├─ TDEventServiceInstance (XSD)
├─ TDEventServiceInstanceDiscoveryTypeEnum (XSD)
├─ TDEventServiceInstanceEventTypeEnum (XSD)
├─ TDEventServiceInstanceFieldTypeEnum (XSD)
├─ TDEventServiceInstanceMethodTypeEnum (XSD)
├─ TDEventSwcInternalBehavior (R23-11)
├─ TDEventSwcInternalBehaviorTypeEnum (R23-11)
├─ TDEventTriggerTypeEnum (R23-11)
├─ TDEventVariableDataPrototype (R23-11)
├─ TDEventVariableDataPrototypeTypeEnum (R23-11)
├─ TDHeaderIdRange (R23-11)
├─ TerminationBehaviorEnum (XSD)
├─ TextTableMapping (R23-11)
├─ TextTableValuePair (R23-11)
├─ Tgroup (R23-11)
├─ TimeBaseResource (XSD)
├─ TimeRangeType (R23-11)
├─ TimeRangeTypeTolerance (XSD)
│  ├─ AbsoluteTolerance (R23-11)
│  └─ RelativeTolerance (R23-11)
├─ TimeSyncClientConfiguration (R23-11)
├─ TimeSyncCorrection (XSD)
├─ TimeSynchronization (R23-11)
├─ TimeSynchronizationKindEnum (XSD)
├─ TimeSyncTechnologyEnum (R23-11)
├─ TimeValue (R23-11)
├─ TimingDescriptionEventChain (R23-11)
├─ TimingExtension (R23-11)
├─ TimingExtensionResource (R23-11)
├─ TlsCryptoServiceMapping (R23-11)
├─ TlsPskIdentity (R23-11)
├─ TlsVersionEnum (R23-11)
├─ TlvDataIdDefinition (R23-11)
├─ TopicContent (R23-11)
├─ TopicContentOrMsrQuery (R23-11)
├─ TopicOrMsrQuery (R23-11)
├─ TpAckType (XSD)
├─ TpConfig (R23-11)
├─ TpConnection (R23-11)
│  ├─ DoIpTpConnection (R23-11)
│  ├─ EthTpConnection (R23-11)
│  ├─ FlexrayArTpConnection (R23-11)
│  ├─ FlexrayTpConnection (R23-11)
│  └─ LinTpConnection (R23-11)
├─ TpPort (R23-11)
├─ TraceReferrable (XSD)
├─ TraceSwitchConfiguration (XSD)
├─ TraceSwitchEnum (XSD)
├─ TransferPropertyEnum (R23-11)
├─ TransformationISignalPropsContent (XSD)
│  ├─ EndToEndTransformationISignalPropsConditional (XSD)  + EndToEndTransformationISignalPropsContent
│  ├─ SOMEIPTransformationISignalPropsConditional (XSD)  + SOMEIPTransformationISignalPropsContent
│  └─ UserDefinedTransformationISignalPropsConditional (XSD)  + UserDefinedTransformationISignalPropsContent
├─ TransformationProps (R23-11)
├─ TransformerClassEnum (R23-11)
├─ TransmissionAcknowledgementRequest (R23-11)
├─ TransmissionComSpecProps (R23-11)
├─ TransmissionModeCondition (R23-11)
├─ TransmissionModeDeclaration (R23-11)
├─ TransmissionModeDefinitionEnum (R23-11)
├─ TransmissionModeTiming (R23-11)
├─ TransportLayerProtocolEnum (XSD)
├─ TransportLayerRule (XSD)
│  ├─ TcpRule (XSD)
│  └─ UdpRule (XSD)
├─ TransportProtocolConfiguration (R23-11)
│  ├─ GenericTp (R23-11)
│  ├─ HttpTp (R23-11)
│  ├─ Ieee1722Tp (R23-11)
│  ├─ RtpTp (R23-11)
│  └─ TcpUdpConfig (R23-11)
│     ├─ TcpTp (R23-11)  + TransportProtocolConfiguration
│     └─ UdpTp (R23-11)  + TransportProtocolConfiguration
├─ TriggerIPduSendCondition (R23-11)
├─ TriggerMapping (R23-11)
├─ TriggerMode (R23-11)
├─ TriggerToSignalMapping (R23-11)
├─ TrustedPlatformExecutableLaunchBehaviorEnum (XSD)
├─ Tt (R23-11)
├─ TtcanAbsolutelyScheduledTiming (R23-11)
├─ TtcanClusterContent (XSD)
├─ TtcanCommunicationController (R23-11)
├─ TtcanCommunicationControllerContent (XSD)
├─ TtcanTriggerType (R23-11)
├─ UcmModuleInstantiation (XSD)
├─ UdpChecksumCalculationEnum (R23-11)
├─ UdpCollectionTriggerEnum (XSD)
├─ UdpNmNetworkConfiguration (XSD)
├─ UdpNmNode (R23-11)
├─ UdpProps (R23-11)
├─ UploadableDeploymentElement (XSD)
├─ UploadableExclusivePackageElement (XSD)
├─ UriString (R23-11)
├─ Url (XSD)
├─ UserDefinedClusterContent (XSD)
├─ UserDefinedCommunicationConnector (R23-11)
├─ UserDefinedCommunicationControllerContent (XSD)
├─ UserDefinedTransformationISignalPropsContent (XSD)
├─ V2xMUserNeeds (R23-11)
├─ V2xSupportEnum (XSD)
├─ ValignEnum (R23-11)
├─ ValueGroup (R23-11)
├─ ValueList (R23-11)
├─ ValueSpecification (R23-11)
│  ├─ AbstractRuleBasedValueSpecification (R23-11)
│  │  ├─ ApplicationRuleBasedValueSpecification (R23-11)  + CompositeRuleBasedValueArgument, ValueSpecification
│  │  ├─ CompositeRuleBasedValueSpecification (R23-11)  + ValueSpecification
│  │  └─ NumericalRuleBasedValueSpecification (R23-11)  + ValueSpecification
│  ├─ CompositeValueSpecification (R23-11)
│  │  ├─ ApplicationAssocMapValueSpecification (XSD)  + ValueSpecification
│  │  ├─ ArrayValueSpecification (R23-11)  + ValueSpecification
│  │  └─ RecordValueSpecification (R23-11)  + ValueSpecification
│  ├─ NotAvailableValueSpecification (R23-11)
│  ├─ NumericalValueSpecification (R23-11)
│  └─ TextValueSpecification (R23-11)
├─ VariableAccessScopeEnum (R23-11)
├─ VariableDataPrototypeInSystemInstanceRef (R23-11)
├─ VariableInAtomicSWCTypeInstanceRef (R23-11)
├─ VariationPoint (R23-11)
├─ VehicleDriverNotification (XSD)
├─ VehicleDriverNotificationEnum (XSD)
├─ VendorSpecificServiceNeeds (R23-11)
├─ VerbatimString (R23-11)
├─ VerbatimStringPlain (R23-11)
├─ VerificationStatusIndicationModeEnum (R23-11)
├─ ViewTokens (R23-11)
├─ ViolatedSafetyConditionBehaviorEnum (XSD)
├─ VlanMembership (R23-11)
├─ WhitespaceControlled (R23-11)
│  ├─ MixedContentForPlainText (R23-11)
│  │  └─ LPlainText (R23-11)  + LanguageSpecific, WhitespaceControlled
│  └─ MixedContentForVerbatim (R23-11)
│     └─ LVerbatim (R23-11)  + LanguageSpecific, WhitespaceControlled
├─ Xfile (R23-11)
├─ XmlSpaceEnum (XSD)
└─ Xref (R23-11)
```
