# XSD-only classes (source: AUTOSAR_00052.xsd)

Every class whose node in `hierarchy_tree.md` is tagged `(XSD)` — no Class/Enumeration
table in either the R23-11 or R4.3.1 markdown corpus; spec source is the R23-11 XSD
(`autosar/R23-11/xsd/AUTOSAR_00052.xsd`).

Excluded from the table: the atpVariation-generated variation-point containers
(`*Content` / `*Conditional` classes whose XSD documentation reads "This element was
generated/modified due to an atpVariation stereotype") — see the appendix at the bottom.

Columns:

- **Class** — spec class name (hierarchy_tree.md node).
- **XML element** — matching `xsd:complexType` name in `AUTOSAR_00052.xsd`; that name is
  the element name used in instance arxml documents (enumerations are complexTypes
  wrapping a `--SIMPLE` simpleType, so they carry an element name too). `(X group only)`
  = the class exists in the XSD only as an `xsd:element group` named X with no own
  complexType (abstract base composition — no own instance element).
- **Group** — Group*.md sync-queue file(s) holding the class's `- [ ]`/`- [x]` row
  (`G<n>` = Group<n>.md); `—` = no queue row anywhere in Group1–36 (not queued, not
  modeled in src).

**Total: 648 XSD-only classes** — 553 with an own `xsd:complexType` (incl. enumerations, which are complexTypes wrapping a `--SIMPLE` simpleType), 95 element-group-only, 0 unmatched against the XSD, 597 without a Group*.md queue row; plus 57 atpVariation-generated containers excluded (see appendix).

| Class | XML element | Group |
|---|---|---|
| `AbstractExecutionContext` | (ABSTRACT-EXECUTION-CONTEXT group only) | — |
| `AbstractIamRemoteSubject` | (ABSTRACT-IAM-REMOTE-SUBJECT group only) | — |
| `AbstractMethodInExecutableInstanceRef` | (ABSTRACT-METHOD-IN-EXECUTABLE-INSTANCE-REF group only) | — |
| `AbstractPortPrototypeInExecutableInstanceRef` | (ABSTRACT-PORT-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF group only) | — |
| `AbstractPortPrototypeInSoftwareClusterDesignInstanceRef` | (ABSTRACT-PORT-PROTOTYPE-IN-SOFTWARE-CLUSTER-DESIGN-INSTANCE-REF group only) | — |
| `AbstractRawDataStreamEthernetCredentials` | (ABSTRACT-RAW-DATA-STREAM-ETHERNET-CREDENTIALS group only) | — |
| `AbstractRawDataStreamInterface` | (ABSTRACT-RAW-DATA-STREAM-INTERFACE group only) | — |
| `AbstractSecurityIdsmInstanceFilter` | (ABSTRACT-SECURITY-IDSM-INSTANCE-FILTER group only) | — |
| `AbstractSignalBasedToISignalTriggeringMapping` | (ABSTRACT-SIGNAL-BASED-TO-I-SIGNAL-TRIGGERING-MAPPING group only) | — |
| `AbstractSynchronizedTimeBaseInterface` | (ABSTRACT-SYNCHRONIZED-TIME-BASE-INTERFACE group only) | — |
| `AccessControlEnum` | ACCESS-CONTROL-ENUM | — |
| `AdaptiveApplicationSwComponentType` | ADAPTIVE-APPLICATION-SW-COMPONENT-TYPE | — |
| `AdaptiveFirewallModuleInstantiation` | ADAPTIVE-FIREWALL-MODULE-INSTANTIATION | — |
| `AdaptiveFirewallToPortPrototypeMapping` | ADAPTIVE-FIREWALL-TO-PORT-PROTOTYPE-MAPPING | — |
| `AdaptiveModuleInstantiation` | (ADAPTIVE-MODULE-INSTANTIATION group only) | — |
| `AdaptivePlatformServiceInstance` | (ADAPTIVE-PLATFORM-SERVICE-INSTANCE group only) | — |
| `AdaptiveSwcInternalBehavior` | ADAPTIVE-SWC-INTERNAL-BEHAVIOR | — |
| `AliveSupervision` | ALIVE-SUPERVISION | — |
| `Allocator` | ALLOCATOR | — |
| `ApApplicationEndpoint` | AP-APPLICATION-ENDPOINT | — |
| `ApApplicationError` | AP-APPLICATION-ERROR | — |
| `ApApplicationErrorDomain` | AP-APPLICATION-ERROR-DOMAIN | — |
| `ApApplicationErrorSet` | AP-APPLICATION-ERROR-SET | — |
| `ApSomeipTransformationProps` | AP-SOMEIP-TRANSFORMATION-PROPS | — |
| `ApplicabilityInfo` | APPLICABILITY-INFO | — |
| `ApplicabilityInfoSet` | APPLICABILITY-INFO-SET | — |
| `ApplicationAssocMapDataType` | APPLICATION-ASSOC-MAP-DATA-TYPE | — |
| `ApplicationAssocMapElement` | APPLICATION-ASSOC-MAP-ELEMENT | — |
| `ApplicationAssocMapElementValueSpecification` | APPLICATION-ASSOC-MAP-ELEMENT-VALUE-SPECIFICATION | — |
| `ApplicationAssocMapValueSpecification` | APPLICATION-ASSOC-MAP-VALUE-SPECIFICATION | — |
| `ApplicationDataPrototypeInSystemInstanceRef` | APPLICATION-DATA-PROTOTYPE-IN-SYSTEM-INSTANCE-REF | — |
| `ApplicationErrorMapping` | APPLICATION-ERROR-MAPPING | — |
| `AppliedStandard` | APPLIED-STANDARD | — |
| `ArtifactChecksum` | ARTIFACT-CHECKSUM | — |
| `ArtifactChecksumToCryptoProviderMapping` | ARTIFACT-CHECKSUM-TO-CRYPTO-PROVIDER-MAPPING | — |
| `ArtifactLocator` | ARTIFACT-LOCATOR | — |
| `AutosarDataPrototypeInExecutableInstanceRef` | (AUTOSAR-DATA-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF group only) | — |
| `BswApiOptions` | (BSW-API-OPTIONS group only) | G13 |
| `BswClientPolicy` | BSW-CLIENT-POLICY | G4 |
| `BswDataSendPolicy` | BSW-DATA-SEND-POLICY | G4 |
| `BswDebugInfo` | BSW-DEBUG-INFO | — |
| `BswInternalTriggeringPointPolicy` | BSW-INTERNAL-TRIGGERING-POINT-POLICY | G4 |
| `BswParameterPolicy` | BSW-PARAMETER-POLICY | G4 |
| `BswPerInstanceMemoryPolicy` | BSW-PER-INSTANCE-MEMORY-POLICY | G4 |
| `BswReleasedTriggerPolicy` | BSW-RELEASED-TRIGGER-POLICY | G4 |
| `BuildTypeEnum` | BUILD-TYPE-ENUM | — |
| `CanNmRangeConfig` | CAN-NM-RANGE-CONFIG | — |
| `CanTpChannelModeType` | CAN-TP-CHANNEL-MODE-TYPE | — |
| `CanXlNmNodeProps` | CAN-XL-NM-NODE-PROPS | — |
| `CanXlProps` | CAN-XL-PROPS | — |
| `CheckpointTransition` | CHECKPOINT-TRANSITION | — |
| `ClientIdMapping` | CLIENT-ID-MAPPING | — |
| `ClientIntentEnum` | CLIENT-INTENT-ENUM | — |
| `ClientServerArrayElementMapping` | CLIENT-SERVER-ARRAY-ELEMENT-MAPPING | — |
| `ClientServerArrayTypeMapping` | CLIENT-SERVER-ARRAY-TYPE-MAPPING | — |
| `ClientServerCompositeTypeMapping` | (CLIENT-SERVER-COMPOSITE-TYPE-MAPPING group only) | — |
| `ClientServerPrimitiveTypeMapping` | CLIENT-SERVER-PRIMITIVE-TYPE-MAPPING | — |
| `ClientServerRecordElementMapping` | CLIENT-SERVER-RECORD-ELEMENT-MAPPING | — |
| `ClientServerRecordTypeMapping` | CLIENT-SERVER-RECORD-TYPE-MAPPING | — |
| `ClientServerToSignalGroupMapping` | CLIENT-SERVER-TO-SIGNAL-GROUP-MAPPING | — |
| `ComCertificateToCryptoCertificateMapping` | COM-CERTIFICATE-TO-CRYPTO-CERTIFICATE-MAPPING | — |
| `ComEventGrant` | COM-EVENT-GRANT | — |
| `ComEventGrantDesign` | COM-EVENT-GRANT-DESIGN | — |
| `ComFieldGrant` | COM-FIELD-GRANT | — |
| `ComFieldGrantDesign` | COM-FIELD-GRANT-DESIGN | — |
| `ComFindServiceGrant` | COM-FIND-SERVICE-GRANT | — |
| `ComFindServiceGrantDesign` | COM-FIND-SERVICE-GRANT-DESIGN | — |
| `ComGrant` | (COM-GRANT group only) | — |
| `ComGrantDesign` | (COM-GRANT-DESIGN group only) | — |
| `ComKeyToCryptoKeySlotMapping` | COM-KEY-TO-CRYPTO-KEY-SLOT-MAPPING | — |
| `ComMethodGrant` | COM-METHOD-GRANT | — |
| `ComMethodGrantDesign` | COM-METHOD-GRANT-DESIGN | — |
| `ComOfferServiceGrant` | COM-OFFER-SERVICE-GRANT | — |
| `ComOfferServiceGrantDesign` | COM-OFFER-SERVICE-GRANT-DESIGN | — |
| `ComSecOcToCryptoKeySlotMapping` | COM-SEC-OC-TO-CRYPTO-KEY-SLOT-MAPPING | — |
| `ComTriggerGrant` | COM-TRIGGER-GRANT | — |
| `ComTriggerGrantDesign` | COM-TRIGGER-GRANT-DESIGN | — |
| `CompositionPPortToExecutablePPortMapping` | COMPOSITION-P-PORT-TO-EXECUTABLE-P-PORT-MAPPING | — |
| `CompositionPortToExecutablePortMapping` | (COMPOSITION-PORT-TO-EXECUTABLE-PORT-MAPPING group only) | — |
| `CompositionRPortToExecutableRPortMapping` | COMPOSITION-R-PORT-TO-EXECUTABLE-R-PORT-MAPPING | — |
| `CouplingPortAbstractShaper` | (COUPLING-PORT-ABSTRACT-SHAPER group only) | G16 |
| `CppImplementationDataType` | (CPP-IMPLEMENTATION-DATA-TYPE group only) | — |
| `CppImplementationDataTypeContextTarget` | (CPP-IMPLEMENTATION-DATA-TYPE-CONTEXT-TARGET group only) | — |
| `CppImplementationDataTypeElement` | CPP-IMPLEMENTATION-DATA-TYPE-ELEMENT | — |
| `CppImplementationDataTypeElementQualifier` | CPP-IMPLEMENTATION-DATA-TYPE-ELEMENT-QUALIFIER | — |
| `CppTemplateArgument` | CPP-TEMPLATE-ARGUMENT | — |
| `CryptoCertificate` | CRYPTO-CERTIFICATE | — |
| `CryptoCertificateInterface` | CRYPTO-CERTIFICATE-INTERFACE | — |
| `CryptoCertificateKeySlotNeeds` | CRYPTO-CERTIFICATE-KEY-SLOT-NEEDS | — |
| `CryptoCertificateToCryptoKeySlotMapping` | CRYPTO-CERTIFICATE-TO-CRYPTO-KEY-SLOT-MAPPING | — |
| `CryptoCertificateToPortPrototypeMapping` | CRYPTO-CERTIFICATE-TO-PORT-PROTOTYPE-MAPPING | — |
| `CryptoInterface` | (CRYPTO-INTERFACE group only) | — |
| `CryptoKeySlotAllowedModification` | CRYPTO-KEY-SLOT-ALLOWED-MODIFICATION | G20 |
| `CryptoKeySlotContentAllowedUsage` | CRYPTO-KEY-SLOT-CONTENT-ALLOWED-USAGE | G20 |
| `CryptoKeySlotInterface` | CRYPTO-KEY-SLOT-INTERFACE | — |
| `CryptoKeySlotToPortPrototypeMapping` | CRYPTO-KEY-SLOT-TO-PORT-PROTOTYPE-MAPPING | — |
| `CryptoKeySlotTypeEnum` | CRYPTO-KEY-SLOT-TYPE-ENUM | G20 |
| `CryptoKeySlotUsageEnum` | CRYPTO-KEY-SLOT-USAGE-ENUM | — |
| `CryptoModuleInstantiation` | CRYPTO-MODULE-INSTANTIATION | — |
| `CryptoNeeds` | (CRYPTO-NEEDS group only) | — |
| `CryptoObjectTypeEnum` | CRYPTO-OBJECT-TYPE-ENUM | G20 |
| `CryptoProvider` | CRYPTO-PROVIDER | — |
| `CryptoProviderInterface` | CRYPTO-PROVIDER-INTERFACE | — |
| `CryptoProviderToPortPrototypeMapping` | CRYPTO-PROVIDER-TO-PORT-PROTOTYPE-MAPPING | — |
| `CryptoTrustMasterInterface` | CRYPTO-TRUST-MASTER-INTERFACE | — |
| `CustomCppImplementationDataType` | CUSTOM-CPP-IMPLEMENTATION-DATA-TYPE | — |
| `DataLinkLayerRule` | DATA-LINK-LAYER-RULE | G20 |
| `DataPrototypeInServiceInterfaceInstanceRef` | DATA-PROTOTYPE-IN-SERVICE-INTERFACE-INSTANCE-REF | — |
| `DataPrototypeInServiceInterfaceRef` | DATA-PROTOTYPE-IN-SERVICE-INTERFACE-REF | — |
| `DataPrototypeInSystemRef` | (DATA-PROTOTYPE-IN-SYSTEM-REF group only) | — |
| `DataPrototypeWithApplicationDataTypeInSystemRef` | DATA-PROTOTYPE-WITH-APPLICATION-DATA-TYPE-IN-SYSTEM-REF | — |
| `DdsDomainRange` | DDS-DOMAIN-RANGE | — |
| `DdsEventDeployment` | DDS-EVENT-DEPLOYMENT | — |
| `DdsEventQosProps` | DDS-EVENT-QOS-PROPS | — |
| `DdsFieldDeployment` | DDS-FIELD-DEPLOYMENT | — |
| `DdsFieldQosProps` | DDS-FIELD-QOS-PROPS | — |
| `DdsProtectionKindEnum` | DDS-PROTECTION-KIND-ENUM | — |
| `DdsProvidedServiceInstance` | DDS-PROVIDED-SERVICE-INSTANCE | — |
| `DdsQosProps` | (DDS-QOS-PROPS group only) | — |
| `DdsRequiredServiceInstance` | DDS-REQUIRED-SERVICE-INSTANCE | — |
| `DdsRule` | DDS-RULE | — |
| `DdsSecureComProps` | DDS-SECURE-COM-PROPS | — |
| `DdsSecureGovernance` | DDS-SECURE-GOVERNANCE | — |
| `DdsServiceInstanceDiscoveryTypeEnum` | DDS-SERVICE-INSTANCE-DISCOVERY-TYPE-ENUM | — |
| `DdsServiceInstanceProps` | (DDS-SERVICE-INSTANCE-PROPS group only) | — |
| `DdsServiceInstanceResourceIdentifierTypeEnum` | DDS-SERVICE-INSTANCE-RESOURCE-IDENTIFIER-TYPE-ENUM | — |
| `DdsServiceInstanceToMachineMapping` | DDS-SERVICE-INSTANCE-TO-MACHINE-MAPPING | — |
| `DdsServiceInterfaceDeployment` | DDS-SERVICE-INTERFACE-DEPLOYMENT | — |
| `DdsServiceVersion` | DDS-SERVICE-VERSION | — |
| `DdsTopicAccessRule` | DDS-TOPIC-ACCESS-RULE | — |
| `DeadlineSupervision` | DEADLINE-SUPERVISION | — |
| `DiagnosticAbstractDataIdentifierInterface` | (DIAGNOSTIC-ABSTRACT-DATA-IDENTIFIER-INTERFACE group only) | — |
| `DiagnosticAbstractRoutineInterface` | (DIAGNOSTIC-ABSTRACT-ROUTINE-INTERFACE group only) | — |
| `DiagnosticAccessPermissionValidityEnum` | DIAGNOSTIC-ACCESS-PERMISSION-VALIDITY-ENUM | — |
| `DiagnosticAuthenticationInterface` | DIAGNOSTIC-AUTHENTICATION-INTERFACE | — |
| `DiagnosticAuthenticationPortMapping` | DIAGNOSTIC-AUTHENTICATION-PORT-MAPPING | — |
| `DiagnosticClearCondition` | DIAGNOSTIC-CLEAR-CONDITION | — |
| `DiagnosticClearConditionGroup` | DIAGNOSTIC-CLEAR-CONDITION-GROUP | — |
| `DiagnosticClearConditionNeeds` | DIAGNOSTIC-CLEAR-CONDITION-NEEDS | — |
| `DiagnosticClearConditionPortMapping` | DIAGNOSTIC-CLEAR-CONDITION-PORT-MAPPING | — |
| `DiagnosticClearEventBehaviorEnum` | DIAGNOSTIC-CLEAR-EVENT-BEHAVIOR-ENUM | — |
| `DiagnosticComControlInterface` | DIAGNOSTIC-COM-CONTROL-INTERFACE | — |
| `DiagnosticConditionInterface` | DIAGNOSTIC-CONDITION-INTERFACE | — |
| `DiagnosticDTCInformationInterface` | DIAGNOSTIC-DTC-INFORMATION-INTERFACE | — |
| `DiagnosticDataCaptureEnum` | DIAGNOSTIC-DATA-CAPTURE-ENUM | — |
| `DiagnosticDataChangeTrigger` | DIAGNOSTIC-DATA-CHANGE-TRIGGER | — |
| `DiagnosticDataElementInterface` | DIAGNOSTIC-DATA-ELEMENT-INTERFACE | — |
| `DiagnosticDataIdentifierGenericInterface` | DIAGNOSTIC-DATA-IDENTIFIER-GENERIC-INTERFACE | — |
| `DiagnosticDataIdentifierInterface` | DIAGNOSTIC-DATA-IDENTIFIER-INTERFACE | — |
| `DiagnosticDataPortMapping` | DIAGNOSTIC-DATA-PORT-MAPPING | — |
| `DiagnosticDoIPActivationLineInterface` | DIAGNOSTIC-DO-IP-ACTIVATION-LINE-INTERFACE | — |
| `DiagnosticDoIPEntityIdentificationInterface` | DIAGNOSTIC-DO-IP-ENTITY-IDENTIFICATION-INTERFACE | — |
| `DiagnosticDoIPGroupIdentificationInterface` | DIAGNOSTIC-DO-IP-GROUP-IDENTIFICATION-INTERFACE | — |
| `DiagnosticDoIPPowerModeInterface` | DIAGNOSTIC-DO-IP-POWER-MODE-INTERFACE | — |
| `DiagnosticDoIPTriggerVehicleAnnouncementInterface` | DIAGNOSTIC-DO-IP-TRIGGER-VEHICLE-ANNOUNCEMENT-INTERFACE | — |
| `DiagnosticDownloadInterface` | DIAGNOSTIC-DOWNLOAD-INTERFACE | — |
| `DiagnosticDtcChangeTrigger` | DIAGNOSTIC-DTC-CHANGE-TRIGGER | — |
| `DiagnosticEcuProps` | DIAGNOSTIC-ECU-PROPS | — |
| `DiagnosticEcuResetInterface` | DIAGNOSTIC-ECU-RESET-INTERFACE | — |
| `DiagnosticEventInterface` | DIAGNOSTIC-EVENT-INTERFACE | — |
| `DiagnosticExternalAuthenticationIdentification` | DIAGNOSTIC-EXTERNAL-AUTHENTICATION-IDENTIFICATION | — |
| `DiagnosticExternalAuthenticationInterface` | DIAGNOSTIC-EXTERNAL-AUTHENTICATION-INTERFACE | — |
| `DiagnosticExternalAuthenticationPortMapping` | DIAGNOSTIC-EXTERNAL-AUTHENTICATION-PORT-MAPPING | — |
| `DiagnosticGenericUdsInterface` | DIAGNOSTIC-GENERIC-UDS-INTERFACE | — |
| `DiagnosticGenericUdsNeeds` | DIAGNOSTIC-GENERIC-UDS-NEEDS | — |
| `DiagnosticIndicatorInterface` | DIAGNOSTIC-INDICATOR-INTERFACE | — |
| `DiagnosticIndicatorNeeds` | DIAGNOSTIC-INDICATOR-NEEDS | — |
| `DiagnosticIndicatorPortMapping` | DIAGNOSTIC-INDICATOR-PORT-MAPPING | — |
| `DiagnosticInitialEventStatusEnum` | DIAGNOSTIC-INITIAL-EVENT-STATUS-ENUM | — |
| `DiagnosticMasterToSlaveEventMappingSet` | DIAGNOSTIC-MASTER-TO-SLAVE-EVENT-MAPPING-SET | — |
| `DiagnosticMemoryDestinationMirror` | DIAGNOSTIC-MEMORY-DESTINATION-MIRROR | — |
| `DiagnosticMemoryDestinationPortMapping` | DIAGNOSTIC-MEMORY-DESTINATION-PORT-MAPPING | — |
| `DiagnosticMonitorInterface` | DIAGNOSTIC-MONITOR-INTERFACE | — |
| `DiagnosticMonitorPortMapping` | DIAGNOSTIC-MONITOR-PORT-MAPPING | — |
| `DiagnosticMultipleConditionInterface` | DIAGNOSTIC-MULTIPLE-CONDITION-INTERFACE | — |
| `DiagnosticMultipleConditionPortMapping` | DIAGNOSTIC-MULTIPLE-CONDITION-PORT-MAPPING | — |
| `DiagnosticMultipleEventInterface` | DIAGNOSTIC-MULTIPLE-EVENT-INTERFACE | — |
| `DiagnosticMultipleEventPortMapping` | DIAGNOSTIC-MULTIPLE-EVENT-PORT-MAPPING | — |
| `DiagnosticMultipleMonitorInterface` | DIAGNOSTIC-MULTIPLE-MONITOR-INTERFACE | — |
| `DiagnosticMultipleMonitorPortMapping` | DIAGNOSTIC-MULTIPLE-MONITOR-PORT-MAPPING | — |
| `DiagnosticMultipleResourceInterface` | (DIAGNOSTIC-MULTIPLE-RESOURCE-INTERFACE group only) | — |
| `DiagnosticMultipleResourcePortMapping` | (DIAGNOSTIC-MULTIPLE-RESOURCE-PORT-MAPPING group only) | — |
| `DiagnosticOperationCycleInterface` | DIAGNOSTIC-OPERATION-CYCLE-INTERFACE | — |
| `DiagnosticPortInterface` | (DIAGNOSTIC-PORT-INTERFACE group only) | — |
| `DiagnosticProvidedDataMapping` | DIAGNOSTIC-PROVIDED-DATA-MAPPING | — |
| `DiagnosticRequestFileTransferInterface` | DIAGNOSTIC-REQUEST-FILE-TRANSFER-INTERFACE | — |
| `DiagnosticResponseOnEventNeeds` | DIAGNOSTIC-RESPONSE-ON-EVENT-NEEDS | — |
| `DiagnosticResponseOnEventTrigger` | (DIAGNOSTIC-RESPONSE-ON-EVENT-TRIGGER group only) | — |
| `DiagnosticRoutineGenericInterface` | DIAGNOSTIC-ROUTINE-GENERIC-INTERFACE | — |
| `DiagnosticRoutineInterface` | DIAGNOSTIC-ROUTINE-INTERFACE | — |
| `DiagnosticSecurityLevelInterface` | DIAGNOSTIC-SECURITY-LEVEL-INTERFACE | — |
| `DiagnosticSecurityLevelPortMapping` | DIAGNOSTIC-SECURITY-LEVEL-PORT-MAPPING | — |
| `DiagnosticServiceGenericMapping` | DIAGNOSTIC-SERVICE-GENERIC-MAPPING | — |
| `DiagnosticServiceValidationConfiguration` | DIAGNOSTIC-SERVICE-VALIDATION-CONFIGURATION | — |
| `DiagnosticServiceValidationInterface` | DIAGNOSTIC-SERVICE-VALIDATION-INTERFACE | — |
| `DiagnosticServiceValidationMapping` | DIAGNOSTIC-SERVICE-VALIDATION-MAPPING | — |
| `DiagnosticSovdAuthorizationInterface` | DIAGNOSTIC-SOVD-AUTHORIZATION-INTERFACE | — |
| `DiagnosticSovdAuthorizationPortMapping` | DIAGNOSTIC-SOVD-AUTHORIZATION-PORT-MAPPING | — |
| `DiagnosticSovdBulkData` | DIAGNOSTIC-SOVD-BULK-DATA | — |
| `DiagnosticSovdBulkDataInterface` | DIAGNOSTIC-SOVD-BULK-DATA-INTERFACE | — |
| `DiagnosticSovdBulkDataPortMapping` | DIAGNOSTIC-SOVD-BULK-DATA-PORT-MAPPING | — |
| `DiagnosticSovdConfiguration` | (DIAGNOSTIC-SOVD-CONFIGURATION group only) | — |
| `DiagnosticSovdConfigurationBulkData` | DIAGNOSTIC-SOVD-CONFIGURATION-BULK-DATA | — |
| `DiagnosticSovdConfigurationDataIdentifierMapping` | DIAGNOSTIC-SOVD-CONFIGURATION-DATA-IDENTIFIER-MAPPING | — |
| `DiagnosticSovdConfigurationInterface` | DIAGNOSTIC-SOVD-CONFIGURATION-INTERFACE | — |
| `DiagnosticSovdConfigurationParameter` | DIAGNOSTIC-SOVD-CONFIGURATION-PARAMETER | — |
| `DiagnosticSovdConfigurationPortMapping` | DIAGNOSTIC-SOVD-CONFIGURATION-PORT-MAPPING | — |
| `DiagnosticSovdLock` | DIAGNOSTIC-SOVD-LOCK | — |
| `DiagnosticSovdLog` | DIAGNOSTIC-SOVD-LOG | — |
| `DiagnosticSovdMethod` | DIAGNOSTIC-SOVD-METHOD | — |
| `DiagnosticSovdMethodPrimitive` | DIAGNOSTIC-SOVD-METHOD-PRIMITIVE | — |
| `DiagnosticSovdPortInterface` | (DIAGNOSTIC-SOVD-PORT-INTERFACE group only) | — |
| `DiagnosticSovdProximityChallengeInterface` | DIAGNOSTIC-SOVD-PROXIMITY-CHALLENGE-INTERFACE | — |
| `DiagnosticSovdProximityChallengePortMapping` | DIAGNOSTIC-SOVD-PROXIMITY-CHALLENGE-PORT-MAPPING | — |
| `DiagnosticSovdServiceInstance` | (DIAGNOSTIC-SOVD-SERVICE-INSTANCE group only) | — |
| `DiagnosticSovdServiceValidationInterface` | DIAGNOSTIC-SOVD-SERVICE-VALIDATION-INTERFACE | — |
| `DiagnosticSovdServiceValidationPortMapping` | DIAGNOSTIC-SOVD-SERVICE-VALIDATION-PORT-MAPPING | — |
| `DiagnosticSovdUpdate` | DIAGNOSTIC-SOVD-UPDATE | — |
| `DiagnosticSovdUpdateInterface` | DIAGNOSTIC-SOVD-UPDATE-INTERFACE | — |
| `DiagnosticSovdUpdatePortMapping` | DIAGNOSTIC-SOVD-UPDATE-PORT-MAPPING | — |
| `DiagnosticStoreEventSupportEnum` | DIAGNOSTIC-STORE-EVENT-SUPPORT-ENUM | — |
| `DiagnosticTroubleCodeUdsToClearConditionGroupMapping` | DIAGNOSTIC-TROUBLE-CODE-UDS-TO-CLEAR-CONDITION-GROUP-MAPPING | — |
| `DiagnosticUploadInterface` | DIAGNOSTIC-UPLOAD-INTERFACE | — |
| `DiscoveryTechnology` | DISCOVERY-TECHNOLOGY | — |
| `DiscoveryTechnologyEnum` | DISCOVERY-TECHNOLOGY-ENUM | — |
| `DltApplicationToProcessMapping` | DLT-APPLICATION-TO-PROCESS-MAPPING | — |
| `DltLogSink` | DLT-LOG-SINK | — |
| `DltLogSinkToPortPrototypeMapping` | DLT-LOG-SINK-TO-PORT-PROTOTYPE-MAPPING | — |
| `DltMessageCollectionSet` | DLT-MESSAGE-COLLECTION-SET | — |
| `DoIpEidRetrievalEnum` | DO-IP-EID-RETRIEVAL-ENUM | — |
| `DoIpInstantiation` | DO-IP-INSTANTIATION | — |
| `DoIpNetworkConfiguration` | DO-IP-NETWORK-CONFIGURATION | — |
| `DoIpRequestConfiguration` | DO-IP-REQUEST-CONFIGURATION | — |
| `DoIpRule` | DO-IP-RULE | G20 |
| `E2EProfileConfiguration` | E-2-E-PROFILE-CONFIGURATION | — |
| `E2EProfileConfigurationSet` | E-2-E-PROFILE-CONFIGURATION-SET | — |
| `EcuInstanceProps` | ECU-INSTANCE-PROPS | — |
| `EcucAffectionEnum` | ECUC-AFFECTION-ENUM | — |
| `EcucConfigurationClassAffection` | ECUC-CONFIGURATION-CLASS-AFFECTION | — |
| `EcucImplementationConfigurationClass` | ECUC-IMPLEMENTATION-CONFIGURATION-CLASS | — |
| `EmptySignalMapping` | EMPTY-SIGNAL-MAPPING | — |
| `End2EndEventProtectionProps` | END-2-END-EVENT-PROTECTION-PROPS | — |
| `End2EndMethodProtectionProps` | END-2-END-METHOD-PROTECTION-PROPS | — |
| `EnterExitTimeout` | ENTER-EXIT-TIMEOUT | — |
| `EnvironmentCaptureToReportingEnum` | ENVIRONMENT-CAPTURE-TO-REPORTING-ENUM | — |
| `EthernetFrame` | ETHERNET-FRAME | — |
| `EthernetRawDataStreamClientMapping` | ETHERNET-RAW-DATA-STREAM-CLIENT-MAPPING | — |
| `EthernetRawDataStreamGrant` | ETHERNET-RAW-DATA-STREAM-GRANT | — |
| `EthernetRawDataStreamLocalEndpointConfig` | ETHERNET-RAW-DATA-STREAM-LOCAL-ENDPOINT-CONFIG | — |
| `EthernetRawDataStreamMapping` | (ETHERNET-RAW-DATA-STREAM-MAPPING group only) | — |
| `EthernetRawDataStreamRemoteClientConfig` | ETHERNET-RAW-DATA-STREAM-REMOTE-CLIENT-CONFIG | — |
| `EthernetRawDataStreamRemoteServerConfig` | ETHERNET-RAW-DATA-STREAM-REMOTE-SERVER-CONFIG | — |
| `EthernetRawDataStreamServerMapping` | ETHERNET-RAW-DATA-STREAM-SERVER-MAPPING | — |
| `EventInExecutableInstanceRef` | EVENT-IN-EXECUTABLE-INSTANCE-REF | — |
| `EventMapping` | EVENT-MAPPING | — |
| `Executable` | EXECUTABLE | — |
| `ExecutableImplementationProps` | (EXECUTABLE-IMPLEMENTATION-PROPS group only) | — |
| `ExecutableLoggingImplementationProps` | EXECUTABLE-LOGGING-IMPLEMENTATION-PROPS | — |
| `ExecutableTiming` | EXECUTABLE-TIMING | — |
| `ExecutionDependency` | EXECUTION-DEPENDENCY | — |
| `ExecutionStateReportingBehaviorEnum` | EXECUTION-STATE-REPORTING-BEHAVIOR-ENUM | — |
| `FieldAccessEnum` | FIELD-ACCESS-ENUM | — |
| `FieldInExecutableInstanceRef` | FIELD-IN-EXECUTABLE-INSTANCE-REF | — |
| `FieldMapping` | FIELD-MAPPING | — |
| `FieldSenderComSpec` | FIELD-SENDER-COM-SPEC | — |
| `FireAndForgetMethodMapping` | FIRE-AND-FORGET-METHOD-MAPPING | — |
| `FirewallActionEnum` | FIREWALL-ACTION-ENUM | G3 |
| `FirewallStateInFirwallStateSwitchInterfaceInstanceRef` | FIREWALL-STATE-IN-FIRWALL-STATE-SWITCH-INTERFACE-INSTANCE-REF | — |
| `FirewallStateSwitchInterface` | FIREWALL-STATE-SWITCH-INTERFACE | — |
| `ForeignModelReference` | FOREIGN-MODEL-REFERENCE | — |
| `FunctionGroupPhmStateReference` | FUNCTION-GROUP-PHM-STATE-REFERENCE | — |
| `FunctionGroupSet` | FUNCTION-GROUP-SET | — |
| `FunctionGroupStateInFunctionGroupSetInstanceRef` | FUNCTION-GROUP-STATE-IN-FUNCTION-GROUP-SET-INSTANCE-REF | — |
| `FunctionalClusterInteractsWithFunctionalClusterMapping` | (FUNCTIONAL-CLUSTER-INTERACTS-WITH-FUNCTIONAL-CLUSTER-MAPPING group only) | — |
| `FunctionalClusterInteractsWithPersistencyDeploymentMapping` | FUNCTIONAL-CLUSTER-INTERACTS-WITH-PERSISTENCY-DEPLOYMENT-MAPPING | — |
| `FunctionalClusterPersistencyAccessEnum` | FUNCTIONAL-CLUSTER-PERSISTENCY-ACCESS-ENUM | — |
| `FunctionalClusterToSecurityEventDefinitionMapping` | FUNCTIONAL-CLUSTER-TO-SECURITY-EVENT-DEFINITION-MAPPING | — |
| `GeneralParameter` | GENERAL-PARAMETER | G9 |
| `GenericModuleInstantiation` | GENERIC-MODULE-INSTANTIATION | — |
| `GlobalSupervision` | GLOBAL-SUPERVISION | — |
| `Grant` | (GRANT group only) | — |
| `GrantDesign` | (GRANT-DESIGN group only) | — |
| `HandleTerminationAndRestartEnum` | HANDLE-TERMINATION-AND-RESTART-ENUM | — |
| `HealthChannel` | (HEALTH-CHANNEL group only) | — |
| `HealthChannelExternalReportedStatus` | HEALTH-CHANNEL-EXTERNAL-REPORTED-STATUS | — |
| `HealthChannelExternalStatus` | HEALTH-CHANNEL-EXTERNAL-STATUS | — |
| `HealthChannelSupervision` | HEALTH-CHANNEL-SUPERVISION | — |
| `IEEE1722TpAafConnection` | IEEE-1722-TP-AAF-CONNECTION | G33 |
| `IEEE1722TpAcfConnection` | IEEE-1722-TP-ACF-CONNECTION | G33 |
| `IEEE1722TpCrfConnection` | IEEE-1722-TP-CRF-CONNECTION | G33 |
| `IEEE1722TpCrfTypeEnum` | IEEE-1722-TP-CRF-TYPE-ENUM | G33 |
| `IPSecIamRemoteSubject` | IP-SEC-IAM-REMOTE-SUBJECT | — |
| `IPTransportProtocolEnum` | IP-TRANSPORT-PROTOCOL-ENUM | — |
| `IamModuleInstantiation` | IAM-MODULE-INSTANTIATION | — |
| `IcmpRule` | ICMP-RULE | G20 |
| `IdsmAbstractPortInterface` | (IDSM-ABSTRACT-PORT-INTERFACE group only) | — |
| `IdsmContextProviderInterface` | IDSM-CONTEXT-PROVIDER-INTERFACE | — |
| `IdsmContextProviderMapping` | IDSM-CONTEXT-PROVIDER-MAPPING | — |
| `IdsmTimestampProviderInterface` | IDSM-TIMESTAMP-PROVIDER-INTERFACE | — |
| `IdsmTimestampProviderMapping` | IDSM-TIMESTAMP-PROVIDER-MAPPING | — |
| `IkeAuthenticationMethodEnum` | IKE-AUTHENTICATION-METHOD-ENUM | — |
| `ImplementationDataTypeElementInSystemRef` | IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-SYSTEM-REF | — |
| `ImpositionTimeDefinitionGroup` | IMPOSITION-TIME-DEFINITION-GROUP | — |
| `InterfaceMapping` | INTERFACE-MAPPING | — |
| `IpIamAuthenticConnectionProps` | IP-IAM-AUTHENTIC-CONNECTION-PROPS | — |
| `IpIamRemoteSubject` | IP-IAM-REMOTE-SUBJECT | — |
| `Ipv4Rule` | IPV-4-RULE | G20 |
| `Ipv6Rule` | IPV-6-RULE | G20 |
| `J1939TpPg` | J-1939-TP-PG | G33 |
| `KeyUsageRestrictionEnum` | KEY-USAGE-RESTRICTION-ENUM | — |
| `LTMessageCollectionToPortPrototypeMapping` | LT-MESSAGE-COLLECTION-TO-PORT-PROTOTYPE-MAPPING | — |
| `LogAndTraceInstantiation` | LOG-AND-TRACE-INSTANTIATION | — |
| `LogAndTraceInterface` | LOG-AND-TRACE-INTERFACE | — |
| `LogicAddress` | LOGIC-ADDRESS | — |
| `LogicalSupervision` | LOGICAL-SUPERVISION | — |
| `MacSecCryptoAlgoConfig` | MAC-SEC-CRYPTO-ALGO-CONFIG | G30 |
| `MacSecKayParticipant` | MAC-SEC-KAY-PARTICIPANT | G30 |
| `Machine` | MACHINE | — |
| `MachineDesign` | MACHINE-DESIGN | — |
| `MachineTiming` | MACHINE-TIMING | — |
| `MemoryUsage` | MEMORY-USAGE | — |
| `MethodMapping` | METHOD-MAPPING | — |
| `ModeDeclarationGroupPrototypeInExecutableInstanceRef` | MODE-DECLARATION-GROUP-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF | — |
| `ModeDeclarationGroupPrototypeInSystemInstanceRef` | MODE-DECLARATION-GROUP-PROTOTYPE-IN-SYSTEM-INSTANCE-REF | — |
| `ModeDeclarationInStateManagementStateNotificationInstanceRef` | MODE-DECLARATION-IN-STATE-MANAGEMENT-STATE-NOTIFICATION-INSTANCE-REF | — |
| `ModeInProcessInstanceRef` | MODE-IN-PROCESS-INSTANCE-REF | — |
| `ModeInSwcBswInstanceRef` | (MODE-IN-SWC-BSW-INSTANCE-REF group only) | G8 |
| `ModificationTypeEnum` | MODIFICATION-TYPE-ENUM | — |
| `NameTokenValueVariationPoint` | NAME-TOKEN-VALUE-VARIATION-POINT | — |
| `NetworkHandlePortMapping` | NETWORK-HANDLE-PORT-MAPPING | — |
| `NetworkLayerRule` | (NETWORK-LAYER-RULE group only) | G20 |
| `NetworkManagementPortInterface` | NETWORK-MANAGEMENT-PORT-INTERFACE | — |
| `NmHandleMappingDirectionEnum` | NM-HANDLE-MAPPING-DIRECTION-ENUM | — |
| `NmHandleToFunctionGroupStateMapping` | NM-HANDLE-TO-FUNCTION-GROUP-STATE-MAPPING | — |
| `NmInstantiation` | NM-INSTANTIATION | — |
| `NmInteractsWithSmMapping` | NM-INTERACTS-WITH-SM-MAPPING | — |
| `NmNetworkHandle` | NM-NETWORK-HANDLE | — |
| `NmStateRequestEnum` | NM-STATE-REQUEST-ENUM | — |
| `NoCheckpointSupervision` | NO-CHECKPOINT-SUPERVISION | — |
| `NoSupervision` | NO-SUPERVISION | — |
| `NonOsModuleInstantiation` | (NON-OS-MODULE-INSTANTIATION group only) | — |
| `NormalizedInstruction` | NORMALIZED-INSTRUCTION | — |
| `OperationArgumentInComponentInstanceRef` | OPERATION-ARGUMENT-IN-COMPONENT-INSTANCE-REF | — |
| `OrientEnum` | ORIENT-ENUM | G3 |
| `OsArtiAdapterLaunchBehaviorEnum` | OS-ARTI-ADAPTER-LAUNCH-BEHAVIOR-ENUM | — |
| `OsModuleInstantiation` | OS-MODULE-INSTANTIATION | — |
| `PPortPrototypeInExecutableInstanceRef` | P-PORT-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF | — |
| `PPortPrototypeInSoftwareClusterDesignInstanceRef` | P-PORT-PROTOTYPE-IN-SOFTWARE-CLUSTER-DESIGN-INSTANCE-REF | — |
| `ParameterDataPrototypeInSystemInstanceRef` | PARAMETER-DATA-PROTOTYPE-IN-SYSTEM-INSTANCE-REF | — |
| `PayloadBytePatternRule` | PAYLOAD-BYTE-PATTERN-RULE | G20 |
| `PayloadBytePatternRulePart` | PAYLOAD-BYTE-PATTERN-RULE-PART | G20 |
| `PersistencyCollectionLevelUpdateStrategyEnum` | PERSISTENCY-COLLECTION-LEVEL-UPDATE-STRATEGY-ENUM | — |
| `PersistencyDataElement` | PERSISTENCY-DATA-ELEMENT | — |
| `PersistencyDataRequiredComSpec` | PERSISTENCY-DATA-REQUIRED-COM-SPEC | — |
| `PersistencyDeployment` | (PERSISTENCY-DEPLOYMENT group only) | — |
| `PersistencyDeploymentElement` | (PERSISTENCY-DEPLOYMENT-ELEMENT group only) | — |
| `PersistencyDeploymentElementToCryptoKeySlotMapping` | PERSISTENCY-DEPLOYMENT-ELEMENT-TO-CRYPTO-KEY-SLOT-MAPPING | — |
| `PersistencyDeploymentToCryptoKeySlotMapping` | PERSISTENCY-DEPLOYMENT-TO-CRYPTO-KEY-SLOT-MAPPING | — |
| `PersistencyDeploymentToDltLogSinkMapping` | PERSISTENCY-DEPLOYMENT-TO-DLT-LOG-SINK-MAPPING | — |
| `PersistencyDeploymentUri` | PERSISTENCY-DEPLOYMENT-URI | — |
| `PersistencyElementLevelUpdateStrategyEnum` | PERSISTENCY-ELEMENT-LEVEL-UPDATE-STRATEGY-ENUM | — |
| `PersistencyFile` | PERSISTENCY-FILE | — |
| `PersistencyFileElement` | PERSISTENCY-FILE-ELEMENT | — |
| `PersistencyFileStorage` | PERSISTENCY-FILE-STORAGE | — |
| `PersistencyFileStorageInterface` | PERSISTENCY-FILE-STORAGE-INTERFACE | — |
| `PersistencyInterface` | (PERSISTENCY-INTERFACE group only) | — |
| `PersistencyInterfaceElement` | (PERSISTENCY-INTERFACE-ELEMENT group only) | — |
| `PersistencyKeyValueDataTypeMapping` | PERSISTENCY-KEY-VALUE-DATA-TYPE-MAPPING | — |
| `PersistencyKeyValuePair` | PERSISTENCY-KEY-VALUE-PAIR | — |
| `PersistencyKeyValueStorage` | PERSISTENCY-KEY-VALUE-STORAGE | — |
| `PersistencyKeyValueStorageInterface` | PERSISTENCY-KEY-VALUE-STORAGE-INTERFACE | — |
| `PersistencyPortPrototypeToDeploymentMapping` | (PERSISTENCY-PORT-PROTOTYPE-TO-DEPLOYMENT-MAPPING group only) | — |
| `PersistencyPortPrototypeToFileStorageMapping` | PERSISTENCY-PORT-PROTOTYPE-TO-FILE-STORAGE-MAPPING | — |
| `PersistencyPortPrototypeToKeyValueStorageMapping` | PERSISTENCY-PORT-PROTOTYPE-TO-KEY-VALUE-STORAGE-MAPPING | — |
| `PersistencyRedundancyChecksum` | (PERSISTENCY-REDUNDANCY-CHECKSUM group only) | — |
| `PersistencyRedundancyCrc` | PERSISTENCY-REDUNDANCY-CRC | — |
| `PersistencyRedundancyEnum` | PERSISTENCY-REDUNDANCY-ENUM | — |
| `PersistencyRedundancyHandling` | (PERSISTENCY-REDUNDANCY-HANDLING group only) | — |
| `PersistencyRedundancyHandlingScopeEnum` | PERSISTENCY-REDUNDANCY-HANDLING-SCOPE-ENUM | — |
| `PersistencyRedundancyHash` | PERSISTENCY-REDUNDANCY-HASH | — |
| `PersistencyRedundancyMOutOfN` | PERSISTENCY-REDUNDANCY-M-OUT-OF-N | — |
| `PhmAbstractRecoveryNotificationInterface` | (PHM-ABSTRACT-RECOVERY-NOTIFICATION-INTERFACE group only) | — |
| `PhmCheckpoint` | PHM-CHECKPOINT | — |
| `PhmCheckpointInExecutableInstanceRef` | PHM-CHECKPOINT-IN-EXECUTABLE-INSTANCE-REF | — |
| `PhmContributionToMachineMapping` | PHM-CONTRIBUTION-TO-MACHINE-MAPPING | — |
| `PhmHealthChannelInterface` | PHM-HEALTH-CHANNEL-INTERFACE | — |
| `PhmHealthChannelRecoveryNotificationInterface` | PHM-HEALTH-CHANNEL-RECOVERY-NOTIFICATION-INTERFACE | — |
| `PhmHealthChannelStatus` | PHM-HEALTH-CHANNEL-STATUS | — |
| `PhmRecoveryActionInterface` | PHM-RECOVERY-ACTION-INTERFACE | — |
| `PhmStateReference` | (PHM-STATE-REFERENCE group only) | — |
| `PhmSupervisedEntityInterface` | PHM-SUPERVISED-ENTITY-INTERFACE | — |
| `PhmSupervision` | (PHM-SUPERVISION group only) | — |
| `PhmSupervisionRecoveryNotificationInterface` | PHM-SUPERVISION-RECOVERY-NOTIFICATION-INTERFACE | — |
| `PlatformHealthManagementContribution` | PLATFORM-HEALTH-MANAGEMENT-CONTRIBUTION | — |
| `PlatformHealthManagementInterface` | (PLATFORM-HEALTH-MANAGEMENT-INTERFACE group only) | — |
| `PlatformModuleEndpointConfiguration` | (PLATFORM-MODULE-ENDPOINT-CONFIGURATION group only) | — |
| `PortDefinedArgumentBlueprint` | PORT-DEFINED-ARGUMENT-BLUEPRINT | — |
| `PortInterfaceBlueprintMapping` | PORT-INTERFACE-BLUEPRINT-MAPPING | G1 |
| `PortInterfaceElementInImplementationDatatypeRef` | PORT-INTERFACE-ELEMENT-IN-IMPLEMENTATION-DATATYPE-REF | — |
| `PortInterfaceToDataTypeMapping` | PORT-INTERFACE-TO-DATA-TYPE-MAPPING | — |
| `PortPrototypeBlueprintMapping` | PORT-PROTOTYPE-BLUEPRINT-MAPPING | G1 |
| `PortPrototypeInExecutableInstanceRef` | PORT-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF | — |
| `PortPrototypeProps` | (PORT-PROTOTYPE-PROPS group only) | — |
| `PossibleErrorReaction` | POSSIBLE-ERROR-REACTION | — |
| `PrmChar` | PRM-CHAR | G9 |
| `PrmCharAbsTol` | PRM-CHAR-ABS-TOL | G9 |
| `PrmCharContents` | (PRM-CHAR-CONTENTS group only) | G9 |
| `PrmCharMinTypMax` | PRM-CHAR-MIN-TYP-MAX | G9 |
| `PrmCharNumericalContents` | PRM-CHAR-NUMERICAL-CONTENTS | G9 |
| `PrmCharNumericalValue` | (PRM-CHAR-NUMERICAL-VALUE group only) | G9 |
| `PrmCharTextualContents` | PRM-CHAR-TEXTUAL-CONTENTS | G9 |
| `Process` | PROCESS | — |
| `ProcessArgument` | PROCESS-ARGUMENT | — |
| `ProcessDesign` | PROCESS-DESIGN | — |
| `ProcessDesignToMachineDesignMapping` | PROCESS-DESIGN-TO-MACHINE-DESIGN-MAPPING | — |
| `ProcessExecutionError` | PROCESS-EXECUTION-ERROR | — |
| `ProcessToMachineMapping` | PROCESS-TO-MACHINE-MAPPING | — |
| `ProcessToMachineMappingSet` | PROCESS-TO-MACHINE-MAPPING-SET | — |
| `Processor` | PROCESSOR | — |
| `ProcessorCore` | PROCESSOR-CORE | — |
| `ProvidedApServiceInstance` | (PROVIDED-AP-SERVICE-INSTANCE group only) | — |
| `ProvidedServiceInstanceToSwClusterDesignPPortPrototypeMapping` | PROVIDED-SERVICE-INSTANCE-TO-SW-CLUSTER-DESIGN-P-PORT-PROTOTYPE-MAPPING | — |
| `ProvidedSomeipServiceInstance` | PROVIDED-SOMEIP-SERVICE-INSTANCE | — |
| `ProvidedUserDefinedServiceInstance` | PROVIDED-USER-DEFINED-SERVICE-INSTANCE | — |
| `PskIdentityToKeySlotMapping` | PSK-IDENTITY-TO-KEY-SLOT-MAPPING | — |
| `RPortPrototypeInExecutableInstanceRef` | R-PORT-PROTOTYPE-IN-EXECUTABLE-INSTANCE-REF | — |
| `RPortPrototypeInSoftwareClusterDesignInstanceRef` | R-PORT-PROTOTYPE-IN-SOFTWARE-CLUSTER-DESIGN-INSTANCE-REF | — |
| `RPortPrototypeProps` | R-PORT-PROTOTYPE-PROPS | — |
| `RawDataStreamClientInterface` | RAW-DATA-STREAM-CLIENT-INTERFACE | — |
| `RawDataStreamDeployment` | RAW-DATA-STREAM-DEPLOYMENT | — |
| `RawDataStreamEthernetTcpUdpCredentials` | RAW-DATA-STREAM-ETHERNET-TCP-UDP-CREDENTIALS | — |
| `RawDataStreamEthernetUdpCredentials` | RAW-DATA-STREAM-ETHERNET-UDP-CREDENTIALS | — |
| `RawDataStreamGrant` | (RAW-DATA-STREAM-GRANT group only) | — |
| `RawDataStreamGrantDesign` | RAW-DATA-STREAM-GRANT-DESIGN | — |
| `RawDataStreamMapping` | (RAW-DATA-STREAM-MAPPING group only) | — |
| `RawDataStreamServerInterface` | RAW-DATA-STREAM-SERVER-INTERFACE | — |
| `ReceiverIntentEnum` | RECEIVER-INTENT-ENUM | — |
| `RecoveryNotification` | RECOVERY-NOTIFICATION | — |
| `RecoveryNotificationToPPortPrototypeMapping` | RECOVERY-NOTIFICATION-TO-P-PORT-PROTOTYPE-MAPPING | — |
| `RemotingTechnology` | REMOTING-TECHNOLOGY | — |
| `RemotingTechnologyEnum` | REMOTING-TECHNOLOGY-ENUM | — |
| `ReportBehaviorEnum` | REPORT-BEHAVIOR-ENUM | — |
| `RequestMethodEnum` | REQUEST-METHOD-ENUM | — |
| `RequestTypeEnum` | REQUEST-TYPE-ENUM | — |
| `RequiredApServiceInstance` | (REQUIRED-AP-SERVICE-INSTANCE group only) | — |
| `RequiredMethodInExecutableInstanceRef` | REQUIRED-METHOD-IN-EXECUTABLE-INSTANCE-REF | — |
| `RequiredServiceInstanceToSwClusterDesignRPortPrototypeMapping` | REQUIRED-SERVICE-INSTANCE-TO-SW-CLUSTER-DESIGN-R-PORT-PROTOTYPE-MAPPING | — |
| `RequiredSomeipServiceInstance` | REQUIRED-SOMEIP-SERVICE-INSTANCE | — |
| `RequiredUserDefinedServiceInstance` | REQUIRED-USER-DEFINED-SERVICE-INSTANCE | — |
| `ResourceGroup` | RESOURCE-GROUP | — |
| `RootSwClusterDesignComponentPrototype` | ROOT-SW-CLUSTER-DESIGN-COMPONENT-PROTOTYPE | — |
| `RootSwComponentPrototype` | ROOT-SW-COMPONENT-PROTOTYPE | — |
| `RteEventInCompositionInstanceRef` | RTE-EVENT-IN-COMPOSITION-INSTANCE-REF | — |
| `RteEventInEcuInstanceRef` | RTE-EVENT-IN-ECU-INSTANCE-REF | G12 |
| `RteEventInSystemInstanceRef` | RTE-EVENT-IN-SYSTEM-INSTANCE-REF | — |
| `SOMEIPTransformerSessionHandlingEnum` | SOMEIP-TRANSFORMER-SESSION-HANDLING-ENUM | — |
| `SearchIntentionEnum` | SEARCH-INTENTION-ENUM | — |
| `SecOcDeployment` | SEC-OC-DEPLOYMENT | — |
| `SecOcJobMapping` | SEC-OC-JOB-MAPPING | — |
| `SecOcJobRequirement` | SEC-OC-JOB-REQUIREMENT | — |
| `SecOcJobSemanticEnum` | SEC-OC-JOB-SEMANTIC-ENUM | — |
| `SecOcSecureComProps` | SEC-OC-SECURE-COM-PROPS | — |
| `SecureComProps` | (SECURE-COM-PROPS group only) | — |
| `SecureCommunicationDeployment` | (SECURE-COMMUNICATION-DEPLOYMENT group only) | — |
| `SecurityEventMapping` | SECURITY-EVENT-MAPPING | — |
| `SecurityEventReportInterface` | SECURITY-EVENT-REPORT-INTERFACE | — |
| `SecurityEventReportToSecurityEventDefinitionMapping` | SECURITY-EVENT-REPORT-TO-SECURITY-EVENT-DEFINITION-MAPPING | — |
| `SenderIntentEnum` | SENDER-INTENT-ENUM | — |
| `SequenceCounterMapping` | SEQUENCE-COUNTER-MAPPING | — |
| `SerializationTechnology` | SERIALIZATION-TECHNOLOGY | — |
| `SerializationTechnologyEnum` | SERIALIZATION-TECHNOLOGY-ENUM | — |
| `ServiceDiscoveryConfiguration` | (SERVICE-DISCOVERY-CONFIGURATION group only) | — |
| `ServiceEventDeployment` | (SERVICE-EVENT-DEPLOYMENT group only) | — |
| `ServiceFieldDeployment` | (SERVICE-FIELD-DEPLOYMENT group only) | — |
| `ServiceInstanceToMachineMapping` | (SERVICE-INSTANCE-TO-MACHINE-MAPPING group only) | — |
| `ServiceInstanceToPortPrototypeMapping` | SERVICE-INSTANCE-TO-PORT-PROTOTYPE-MAPPING | — |
| `ServiceInstanceToSignalMapping` | SERVICE-INSTANCE-TO-SIGNAL-MAPPING | — |
| `ServiceInstanceToSwClusterDesignPortPrototypeMapping` | (SERVICE-INSTANCE-TO-SW-CLUSTER-DESIGN-PORT-PROTOTYPE-MAPPING group only) | — |
| `ServiceInterface` | SERVICE-INTERFACE | — |
| `ServiceInterfaceDeployment` | (SERVICE-INTERFACE-DEPLOYMENT group only) | — |
| `ServiceInterfaceElementMapping` | (SERVICE-INTERFACE-ELEMENT-MAPPING group only) | — |
| `ServiceInterfaceElementSecureComConfig` | SERVICE-INTERFACE-ELEMENT-SECURE-COM-CONFIG | — |
| `ServiceInterfaceEventMapping` | SERVICE-INTERFACE-EVENT-MAPPING | — |
| `ServiceInterfaceFieldMapping` | SERVICE-INTERFACE-FIELD-MAPPING | — |
| `ServiceInterfaceMapping` | SERVICE-INTERFACE-MAPPING | — |
| `ServiceInterfaceMethodMapping` | SERVICE-INTERFACE-METHOD-MAPPING | — |
| `ServiceInterfacePedigree` | SERVICE-INTERFACE-PEDIGREE | — |
| `ServiceInterfaceTriggerMapping` | SERVICE-INTERFACE-TRIGGER-MAPPING | — |
| `ServiceMethodDeployment` | (SERVICE-METHOD-DEPLOYMENT group only) | — |
| `ServiceTiming` | SERVICE-TIMING | — |
| `SignalBasedEventElementToISignalTriggeringMapping` | SIGNAL-BASED-EVENT-ELEMENT-TO-I-SIGNAL-TRIGGERING-MAPPING | — |
| `SignalBasedFieldToISignalTriggeringMapping` | SIGNAL-BASED-FIELD-TO-I-SIGNAL-TRIGGERING-MAPPING | — |
| `SignalBasedFireAndForgetMethodToISignalTriggeringMapping` | SIGNAL-BASED-FIRE-AND-FORGET-METHOD-TO-I-SIGNAL-TRIGGERING-MAPPING | — |
| `SignalBasedMethodToISignalTriggeringMapping` | SIGNAL-BASED-METHOD-TO-I-SIGNAL-TRIGGERING-MAPPING | — |
| `SignalBasedTriggerToISignalTriggeringMapping` | SIGNAL-BASED-TRIGGER-TO-I-SIGNAL-TRIGGERING-MAPPING | — |
| `SignalIPduCounter` | SIGNAL-I-PDU-COUNTER | — |
| `SignalIPduReplication` | SIGNAL-I-PDU-REPLICATION | — |
| `SmInteractsWithNmMapping` | SM-INTERACTS-WITH-NM-MAPPING | — |
| `SoAdConnectorType` | SO-AD-CONNECTOR-TYPE | — |
| `SoAdProtocolType` | SO-AD-PROTOCOL-TYPE | — |
| `SoftwareCluster` | SOFTWARE-CLUSTER | — |
| `SoftwareClusterDependencyCompareCondition` | SOFTWARE-CLUSTER-DEPENDENCY-COMPARE-CONDITION | — |
| `SoftwareClusterDependencyFormula` | SOFTWARE-CLUSTER-DEPENDENCY-FORMULA | — |
| `SoftwareClusterDependencyFormulaPart` | (SOFTWARE-CLUSTER-DEPENDENCY-FORMULA-PART group only) | — |
| `SoftwareClusterDependencyLogicalOperatorEnum` | SOFTWARE-CLUSTER-DEPENDENCY-LOGICAL-OPERATOR-ENUM | — |
| `SoftwareClusterDependencyOperatorEnum` | SOFTWARE-CLUSTER-DEPENDENCY-OPERATOR-ENUM | — |
| `SoftwareClusterDesign` | SOFTWARE-CLUSTER-DESIGN | — |
| `SoftwareClusterDiagnosticAddress` | (SOFTWARE-CLUSTER-DIAGNOSTIC-ADDRESS group only) | — |
| `SoftwareClusterDiagnosticAddressSemanticsEnum` | SOFTWARE-CLUSTER-DIAGNOSTIC-ADDRESS-SEMANTICS-ENUM | — |
| `SoftwareClusterDiagnosticDeploymentProps` | SOFTWARE-CLUSTER-DIAGNOSTIC-DEPLOYMENT-PROPS | — |
| `SoftwareClusterDoipDiagnosticAddress` | SOFTWARE-CLUSTER-DOIP-DIAGNOSTIC-ADDRESS | — |
| `SoftwareClusterInstallationBehaviorEnum` | SOFTWARE-CLUSTER-INSTALLATION-BEHAVIOR-ENUM | — |
| `SoftwareClusterSovdAddress` | SOFTWARE-CLUSTER-SOVD-ADDRESS | — |
| `SoftwareClusterUdsDiagnosticAddress` | SOFTWARE-CLUSTER-UDS-DIAGNOSTIC-ADDRESS | — |
| `SoftwarePackage` | SOFTWARE-PACKAGE | — |
| `SoftwarePackageActionTypeEnum` | SOFTWARE-PACKAGE-ACTION-TYPE-ENUM | — |
| `SoftwarePackageActivationActionEnum` | SOFTWARE-PACKAGE-ACTIVATION-ACTION-ENUM | — |
| `SoftwarePackageStep` | SOFTWARE-PACKAGE-STEP | — |
| `SoftwarePackageStoring` | SOFTWARE-PACKAGE-STORING | — |
| `SoftwarePackageStoringEnum` | SOFTWARE-PACKAGE-STORING-ENUM | — |
| `SomeipCollectionProps` | SOMEIP-COLLECTION-PROPS | — |
| `SomeipDataPrototypeTransformationProps` | SOMEIP-DATA-PROTOTYPE-TRANSFORMATION-PROPS | — |
| `SomeipEventDeployment` | SOMEIP-EVENT-DEPLOYMENT | — |
| `SomeipEventGroup` | SOMEIP-EVENT-GROUP | — |
| `SomeipEventProps` | SOMEIP-EVENT-PROPS | — |
| `SomeipFieldDeployment` | SOMEIP-FIELD-DEPLOYMENT | — |
| `SomeipMethodDeployment` | SOMEIP-METHOD-DEPLOYMENT | — |
| `SomeipMethodProps` | SOMEIP-METHOD-PROPS | — |
| `SomeipProtocolRule` | SOMEIP-PROTOCOL-RULE | G20 |
| `SomeipProvidedEventGroup` | SOMEIP-PROVIDED-EVENT-GROUP | — |
| `SomeipRemoteMulticastConfig` | SOMEIP-REMOTE-MULTICAST-CONFIG | — |
| `SomeipRemoteUnicastConfig` | SOMEIP-REMOTE-UNICAST-CONFIG | — |
| `SomeipRequiredEventGroup` | SOMEIP-REQUIRED-EVENT-GROUP | — |
| `SomeipSdRule` | SOMEIP-SD-RULE | G20 |
| `SomeipServiceDiscovery` | SOMEIP-SERVICE-DISCOVERY | — |
| `SomeipServiceInstanceToMachineMapping` | SOMEIP-SERVICE-INSTANCE-TO-MACHINE-MAPPING | — |
| `SomeipServiceInterfaceDeployment` | SOMEIP-SERVICE-INTERFACE-DEPLOYMENT | — |
| `SovdGatewayEthernetCredentials` | (SOVD-GATEWAY-ETHERNET-CREDENTIALS group only) | — |
| `SovdGatewayInstantiation` | SOVD-GATEWAY-INSTANTIATION | — |
| `SovdGatewayLocalEndpointTcpConfig` | SOVD-GATEWAY-LOCAL-ENDPOINT-TCP-CONFIG | — |
| `SovdModuleInstantiation` | (SOVD-MODULE-INSTANTIATION group only) | — |
| `SovdServerInstantiation` | SOVD-SERVER-INSTANTIATION | — |
| `StartupConfig` | STARTUP-CONFIG | — |
| `StateDependentStartupConfig` | STATE-DEPENDENT-STARTUP-CONFIG | — |
| `StateManagemenPhmErrorInterface` | STATE-MANAGEMEN-PHM-ERROR-INTERFACE | — |
| `StateManagementActionItem` | (STATE-MANAGEMENT-ACTION-ITEM group only) | — |
| `StateManagementActionList` | STATE-MANAGEMENT-ACTION-LIST | — |
| `StateManagementCompareCondition` | (STATE-MANAGEMENT-COMPARE-CONDITION group only) | — |
| `StateManagementCompareEnum` | STATE-MANAGEMENT-COMPARE-ENUM | — |
| `StateManagementCompareFormula` | STATE-MANAGEMENT-COMPARE-FORMULA | — |
| `StateManagementCompareFormulaPart` | (STATE-MANAGEMENT-COMPARE-FORMULA-PART group only) | — |
| `StateManagementDiagTriggerInterface` | STATE-MANAGEMENT-DIAG-TRIGGER-INTERFACE | — |
| `StateManagementEmErrorInterface` | STATE-MANAGEMENT-EM-ERROR-INTERFACE | — |
| `StateManagementErrorCompareRule` | STATE-MANAGEMENT-ERROR-COMPARE-RULE | — |
| `StateManagementErrorInterface` | (STATE-MANAGEMENT-ERROR-INTERFACE group only) | — |
| `StateManagementFunctionGroupSwitchNotificationInterface` | STATE-MANAGEMENT-FUNCTION-GROUP-SWITCH-NOTIFICATION-INTERFACE | — |
| `StateManagementLogicalOperatorEnum` | STATE-MANAGEMENT-LOGICAL-OPERATOR-ENUM | — |
| `StateManagementModuleInstantiation` | STATE-MANAGEMENT-MODULE-INSTANTIATION | — |
| `StateManagementNmActionItem` | STATE-MANAGEMENT-NM-ACTION-ITEM | — |
| `StateManagementNotificationInterface` | (STATE-MANAGEMENT-NOTIFICATION-INTERFACE group only) | — |
| `StateManagementPortInterface` | (STATE-MANAGEMENT-PORT-INTERFACE group only) | — |
| `StateManagementRequestError` | STATE-MANAGEMENT-REQUEST-ERROR | — |
| `StateManagementRequestInterface` | (STATE-MANAGEMENT-REQUEST-INTERFACE group only) | — |
| `StateManagementRequestRule` | STATE-MANAGEMENT-REQUEST-RULE | — |
| `StateManagementRequestTrigger` | STATE-MANAGEMENT-REQUEST-TRIGGER | — |
| `StateManagementSetFunctionGroupStateActionItem` | STATE-MANAGEMENT-SET-FUNCTION-GROUP-STATE-ACTION-ITEM | — |
| `StateManagementSleepActionItem` | STATE-MANAGEMENT-SLEEP-ACTION-ITEM | — |
| `StateManagementStateMachineActionItem` | STATE-MANAGEMENT-STATE-MACHINE-ACTION-ITEM | — |
| `StateManagementStateNotification` | STATE-MANAGEMENT-STATE-NOTIFICATION | — |
| `StateManagementStateRequest` | (STATE-MANAGEMENT-STATE-REQUEST group only) | — |
| `StateManagementSyncActionItem` | STATE-MANAGEMENT-SYNC-ACTION-ITEM | — |
| `StateManagementTriggerCompareRule` | STATE-MANAGEMENT-TRIGGER-COMPARE-RULE | — |
| `StateManagementTriggerInterface` | (STATE-MANAGEMENT-TRIGGER-INTERFACE group only) | — |
| `StdCppImplementationDataType` | STD-CPP-IMPLEMENTATION-DATA-TYPE | — |
| `SupervisionCheckpoint` | SUPERVISION-CHECKPOINT | — |
| `SupervisionMode` | SUPERVISION-MODE | — |
| `SupervisionModeCondition` | SUPERVISION-MODE-CONDITION | — |
| `SwComponentMappingConstraints` | SW-COMPONENT-MAPPING-CONSTRAINTS | — |
| `SwServiceReentranceEnum` | SW-SERVICE-REENTRANCE-ENUM | — |
| `SwVariableAccessImplPolicyEnum` | SW-VARIABLE-ACCESS-IMPL-POLICY-ENUM | — |
| `SwcServiceDependencyInCompositionInstanceRef` | SWC-SERVICE-DEPENDENCY-IN-COMPOSITION-INSTANCE-REF | — |
| `SwcToEcuMappingConstraint` | SWC-TO-ECU-MAPPING-CONSTRAINT | — |
| `SwcToEcuMappingConstraintType` | SWC-TO-ECU-MAPPING-CONSTRAINT-TYPE | — |
| `SynchronizedTimeBaseConsumer` | SYNCHRONIZED-TIME-BASE-CONSUMER | — |
| `SynchronizedTimeBaseConsumerInterface` | SYNCHRONIZED-TIME-BASE-CONSUMER-INTERFACE | — |
| `SynchronizedTimeBaseProvider` | SYNCHRONIZED-TIME-BASE-PROVIDER | — |
| `SynchronizedTimeBaseProviderInterface` | SYNCHRONIZED-TIME-BASE-PROVIDER-INTERFACE | — |
| `TDEventServiceInstance` | (TD-EVENT-SERVICE-INSTANCE group only) | — |
| `TDEventServiceInstanceDiscovery` | TD-EVENT-SERVICE-INSTANCE-DISCOVERY | — |
| `TDEventServiceInstanceDiscoveryTypeEnum` | TD-EVENT-SERVICE-INSTANCE-DISCOVERY-TYPE-ENUM | — |
| `TDEventServiceInstanceEvent` | TD-EVENT-SERVICE-INSTANCE-EVENT | — |
| `TDEventServiceInstanceEventTypeEnum` | TD-EVENT-SERVICE-INSTANCE-EVENT-TYPE-ENUM | — |
| `TDEventServiceInstanceField` | TD-EVENT-SERVICE-INSTANCE-FIELD | — |
| `TDEventServiceInstanceFieldTypeEnum` | TD-EVENT-SERVICE-INSTANCE-FIELD-TYPE-ENUM | — |
| `TDEventServiceInstanceMethod` | TD-EVENT-SERVICE-INSTANCE-METHOD | — |
| `TDEventServiceInstanceMethodTypeEnum` | TD-EVENT-SERVICE-INSTANCE-METHOD-TYPE-ENUM | — |
| `TcpRule` | TCP-RULE | G20 |
| `TerminationBehaviorEnum` | TERMINATION-BEHAVIOR-ENUM | — |
| `TimeBaseProviderToPersistencyMapping` | TIME-BASE-PROVIDER-TO-PERSISTENCY-MAPPING | — |
| `TimeBaseResource` | (TIME-BASE-RESOURCE group only) | — |
| `TimeRangeTypeTolerance` | (TIME-RANGE-TYPE-TOLERANCE group only) | G15 |
| `TimeSyncCorrection` | TIME-SYNC-CORRECTION | — |
| `TimeSyncModuleInstantiation` | TIME-SYNC-MODULE-INSTANTIATION | — |
| `TimeSyncPortPrototypeToTimeBaseMapping` | TIME-SYNC-PORT-PROTOTYPE-TO-TIME-BASE-MAPPING | — |
| `TimeSynchronizationKindEnum` | TIME-SYNCHRONIZATION-KIND-ENUM | — |
| `TlsConnectionGroup` | TLS-CONNECTION-GROUP | — |
| `TlsDeployment` | TLS-DEPLOYMENT | — |
| `TlsIamRemoteSubject` | TLS-IAM-REMOTE-SUBJECT | — |
| `TlsJobMapping` | TLS-JOB-MAPPING | — |
| `TlsSecureComProps` | TLS-SECURE-COM-PROPS | — |
| `TpAckType` | TP-ACK-TYPE | — |
| `TraceReferrable` | (TRACE-REFERRABLE group only) | — |
| `TraceSwitchConfiguration` | TRACE-SWITCH-CONFIGURATION | — |
| `TraceSwitchEnum` | TRACE-SWITCH-ENUM | — |
| `TraceableTable` | TRACEABLE-TABLE | G3 |
| `TransformationPropsToServiceInterfaceElementMapping` | TRANSFORMATION-PROPS-TO-SERVICE-INTERFACE-ELEMENT-MAPPING | — |
| `TransportLayerProtocolEnum` | TRANSPORT-LAYER-PROTOCOL-ENUM | — |
| `TransportLayerRule` | (TRANSPORT-LAYER-RULE group only) | G20 |
| `TriggerInExecutableInstanceRef` | TRIGGER-IN-EXECUTABLE-INSTANCE-REF | — |
| `TrustedPlatformExecutableLaunchBehaviorEnum` | TRUSTED-PLATFORM-EXECUTABLE-LAUNCH-BEHAVIOR-ENUM | — |
| `UcmDescription` | UCM-DESCRIPTION | — |
| `UcmMasterModuleInstantiation` | UCM-MASTER-MODULE-INSTANTIATION | — |
| `UcmModuleInstantiation` | (UCM-MODULE-INSTANTIATION group only) | — |
| `UcmRetryStrategy` | UCM-RETRY-STRATEGY | — |
| `UcmStep` | UCM-STEP | — |
| `UcmSubordinateModuleInstantiation` | UCM-SUBORDINATE-MODULE-INSTANTIATION | — |
| `UcmToTimeBaseResourceMapping` | UCM-TO-TIME-BASE-RESOURCE-MAPPING | — |
| `UdpCollectionTriggerEnum` | UDP-COLLECTION-TRIGGER-ENUM | — |
| `UdpNmNetworkConfiguration` | UDP-NM-NETWORK-CONFIGURATION | — |
| `UdpRule` | UDP-RULE | G20 |
| `UploadableDeploymentElement` | (UPLOADABLE-DEPLOYMENT-ELEMENT group only) | — |
| `UploadableExclusivePackageElement` | (UPLOADABLE-EXCLUSIVE-PACKAGE-ELEMENT group only) | — |
| `Url` | URL | G3 |
| `UserDefinedEventDeployment` | USER-DEFINED-EVENT-DEPLOYMENT | — |
| `UserDefinedFieldDeployment` | USER-DEFINED-FIELD-DEPLOYMENT | — |
| `UserDefinedMethodDeployment` | USER-DEFINED-METHOD-DEPLOYMENT | — |
| `UserDefinedServiceInstanceToMachineMapping` | USER-DEFINED-SERVICE-INSTANCE-TO-MACHINE-MAPPING | — |
| `UserDefinedServiceInterfaceDeployment` | USER-DEFINED-SERVICE-INTERFACE-DEPLOYMENT | — |
| `V2xSupportEnum` | V-2-X-SUPPORT-ENUM | — |
| `VariableAccessInEcuInstanceRef` | VARIABLE-ACCESS-IN-ECU-INSTANCE-REF | G12 |
| `VariableInComponentInstanceRef` | VARIABLE-IN-COMPONENT-INSTANCE-REF | — |
| `VehicleDriverNotification` | VEHICLE-DRIVER-NOTIFICATION | — |
| `VehicleDriverNotificationEnum` | VEHICLE-DRIVER-NOTIFICATION-ENUM | — |
| `VehiclePackage` | VEHICLE-PACKAGE | — |
| `VehicleRolloutStep` | VEHICLE-ROLLOUT-STEP | — |
| `ViolatedSafetyConditionBehaviorEnum` | VIOLATED-SAFETY-CONDITION-BEHAVIOR-ENUM | — |
| `XcpPdu` | XCP-PDU | — |
| `XmlSpaceEnum` | XML-SPACE-ENUM | G8 |

## XSD-only classes with no Group*.md queue row

`AbstractExecutionContext`, `AbstractIamRemoteSubject`, `AbstractMethodInExecutableInstanceRef`, `AbstractPortPrototypeInExecutableInstanceRef`, `AbstractPortPrototypeInSoftwareClusterDesignInstanceRef`, `AbstractRawDataStreamEthernetCredentials`, `AbstractRawDataStreamInterface`, `AbstractSecurityIdsmInstanceFilter`, `AbstractSignalBasedToISignalTriggeringMapping`, `AbstractSynchronizedTimeBaseInterface`, `AccessControlEnum`, `AdaptiveApplicationSwComponentType`, `AdaptiveFirewallModuleInstantiation`, `AdaptiveFirewallToPortPrototypeMapping`, `AdaptiveModuleInstantiation`, `AdaptivePlatformServiceInstance`, `AdaptiveSwcInternalBehavior`, `AliveSupervision`, `Allocator`, `ApApplicationEndpoint`, `ApApplicationError`, `ApApplicationErrorDomain`, `ApApplicationErrorSet`, `ApSomeipTransformationProps`, `ApplicabilityInfo`, `ApplicabilityInfoSet`, `ApplicationAssocMapDataType`, `ApplicationAssocMapElement`, `ApplicationAssocMapElementValueSpecification`, `ApplicationAssocMapValueSpecification`, `ApplicationDataPrototypeInSystemInstanceRef`, `ApplicationErrorMapping`, `AppliedStandard`, `ArtifactChecksum`, `ArtifactChecksumToCryptoProviderMapping`, `ArtifactLocator`, `AutosarDataPrototypeInExecutableInstanceRef`, `BswDebugInfo`, `BuildTypeEnum`, `CanNmRangeConfig`, `CanTpChannelModeType`, `CanXlNmNodeProps`, `CanXlProps`, `CheckpointTransition`, `ClientIdMapping`, `ClientIntentEnum`, `ClientServerArrayElementMapping`, `ClientServerArrayTypeMapping`, `ClientServerCompositeTypeMapping`, `ClientServerPrimitiveTypeMapping`, `ClientServerRecordElementMapping`, `ClientServerRecordTypeMapping`, `ClientServerToSignalGroupMapping`, `ComCertificateToCryptoCertificateMapping`, `ComEventGrant`, `ComEventGrantDesign`, `ComFieldGrant`, `ComFieldGrantDesign`, `ComFindServiceGrant`, `ComFindServiceGrantDesign`, `ComGrant`, `ComGrantDesign`, `ComKeyToCryptoKeySlotMapping`, `ComMethodGrant`, `ComMethodGrantDesign`, `ComOfferServiceGrant`, `ComOfferServiceGrantDesign`, `ComSecOcToCryptoKeySlotMapping`, `ComTriggerGrant`, `ComTriggerGrantDesign`, `CompositionPPortToExecutablePPortMapping`, `CompositionPortToExecutablePortMapping`, `CompositionRPortToExecutableRPortMapping`, `CppImplementationDataType`, `CppImplementationDataTypeContextTarget`, `CppImplementationDataTypeElement`, `CppImplementationDataTypeElementQualifier`, `CppTemplateArgument`, `CryptoCertificate`, `CryptoCertificateInterface`, `CryptoCertificateKeySlotNeeds`, `CryptoCertificateToCryptoKeySlotMapping`, `CryptoCertificateToPortPrototypeMapping`, `CryptoInterface`, `CryptoKeySlotInterface`, `CryptoKeySlotToPortPrototypeMapping`, `CryptoKeySlotUsageEnum`, `CryptoModuleInstantiation`, `CryptoNeeds`, `CryptoProvider`, `CryptoProviderInterface`, `CryptoProviderToPortPrototypeMapping`, `CryptoTrustMasterInterface`, `CustomCppImplementationDataType`, `DataPrototypeInServiceInterfaceInstanceRef`, `DataPrototypeInServiceInterfaceRef`, `DataPrototypeInSystemRef`, `DataPrototypeWithApplicationDataTypeInSystemRef`, `DdsDomainRange`, `DdsEventDeployment`, `DdsEventQosProps`, `DdsFieldDeployment`, `DdsFieldQosProps`, `DdsProtectionKindEnum`, `DdsProvidedServiceInstance`, `DdsQosProps`, `DdsRequiredServiceInstance`, `DdsRule`, `DdsSecureComProps`, `DdsSecureGovernance`, `DdsServiceInstanceDiscoveryTypeEnum`, `DdsServiceInstanceProps`, `DdsServiceInstanceResourceIdentifierTypeEnum`, `DdsServiceInstanceToMachineMapping`, `DdsServiceInterfaceDeployment`, `DdsServiceVersion`, `DdsTopicAccessRule`, `DeadlineSupervision`, `DiagnosticAbstractDataIdentifierInterface`, `DiagnosticAbstractRoutineInterface`, `DiagnosticAccessPermissionValidityEnum`, `DiagnosticAuthenticationInterface`, `DiagnosticAuthenticationPortMapping`, `DiagnosticClearCondition`, `DiagnosticClearConditionGroup`, `DiagnosticClearConditionNeeds`, `DiagnosticClearConditionPortMapping`, `DiagnosticClearEventBehaviorEnum`, `DiagnosticComControlInterface`, `DiagnosticConditionInterface`, `DiagnosticDTCInformationInterface`, `DiagnosticDataCaptureEnum`, `DiagnosticDataChangeTrigger`, `DiagnosticDataElementInterface`, `DiagnosticDataIdentifierGenericInterface`, `DiagnosticDataIdentifierInterface`, `DiagnosticDataPortMapping`, `DiagnosticDoIPActivationLineInterface`, `DiagnosticDoIPEntityIdentificationInterface`, `DiagnosticDoIPGroupIdentificationInterface`, `DiagnosticDoIPPowerModeInterface`, `DiagnosticDoIPTriggerVehicleAnnouncementInterface`, `DiagnosticDownloadInterface`, `DiagnosticDtcChangeTrigger`, `DiagnosticEcuProps`, `DiagnosticEcuResetInterface`, `DiagnosticEventInterface`, `DiagnosticExternalAuthenticationIdentification`, `DiagnosticExternalAuthenticationInterface`, `DiagnosticExternalAuthenticationPortMapping`, `DiagnosticGenericUdsInterface`, `DiagnosticGenericUdsNeeds`, `DiagnosticIndicatorInterface`, `DiagnosticIndicatorNeeds`, `DiagnosticIndicatorPortMapping`, `DiagnosticInitialEventStatusEnum`, `DiagnosticMasterToSlaveEventMappingSet`, `DiagnosticMemoryDestinationMirror`, `DiagnosticMemoryDestinationPortMapping`, `DiagnosticMonitorInterface`, `DiagnosticMonitorPortMapping`, `DiagnosticMultipleConditionInterface`, `DiagnosticMultipleConditionPortMapping`, `DiagnosticMultipleEventInterface`, `DiagnosticMultipleEventPortMapping`, `DiagnosticMultipleMonitorInterface`, `DiagnosticMultipleMonitorPortMapping`, `DiagnosticMultipleResourceInterface`, `DiagnosticMultipleResourcePortMapping`, `DiagnosticOperationCycleInterface`, `DiagnosticPortInterface`, `DiagnosticProvidedDataMapping`, `DiagnosticRequestFileTransferInterface`, `DiagnosticResponseOnEventNeeds`, `DiagnosticResponseOnEventTrigger`, `DiagnosticRoutineGenericInterface`, `DiagnosticRoutineInterface`, `DiagnosticSecurityLevelInterface`, `DiagnosticSecurityLevelPortMapping`, `DiagnosticServiceGenericMapping`, `DiagnosticServiceValidationConfiguration`, `DiagnosticServiceValidationInterface`, `DiagnosticServiceValidationMapping`, `DiagnosticSovdAuthorizationInterface`, `DiagnosticSovdAuthorizationPortMapping`, `DiagnosticSovdBulkData`, `DiagnosticSovdBulkDataInterface`, `DiagnosticSovdBulkDataPortMapping`, `DiagnosticSovdConfiguration`, `DiagnosticSovdConfigurationBulkData`, `DiagnosticSovdConfigurationDataIdentifierMapping`, `DiagnosticSovdConfigurationInterface`, `DiagnosticSovdConfigurationParameter`, `DiagnosticSovdConfigurationPortMapping`, `DiagnosticSovdLock`, `DiagnosticSovdLog`, `DiagnosticSovdMethod`, `DiagnosticSovdMethodPrimitive`, `DiagnosticSovdPortInterface`, `DiagnosticSovdProximityChallengeInterface`, `DiagnosticSovdProximityChallengePortMapping`, `DiagnosticSovdServiceInstance`, `DiagnosticSovdServiceValidationInterface`, `DiagnosticSovdServiceValidationPortMapping`, `DiagnosticSovdUpdate`, `DiagnosticSovdUpdateInterface`, `DiagnosticSovdUpdatePortMapping`, `DiagnosticStoreEventSupportEnum`, `DiagnosticTroubleCodeUdsToClearConditionGroupMapping`, `DiagnosticUploadInterface`, `DiscoveryTechnology`, `DiscoveryTechnologyEnum`, `DltApplicationToProcessMapping`, `DltLogSink`, `DltLogSinkToPortPrototypeMapping`, `DltMessageCollectionSet`, `DoIpEidRetrievalEnum`, `DoIpInstantiation`, `DoIpNetworkConfiguration`, `DoIpRequestConfiguration`, `E2EProfileConfiguration`, `E2EProfileConfigurationSet`, `EcuInstanceProps`, `EcucAffectionEnum`, `EcucConfigurationClassAffection`, `EcucImplementationConfigurationClass`, `EmptySignalMapping`, `End2EndEventProtectionProps`, `End2EndMethodProtectionProps`, `EnterExitTimeout`, `EnvironmentCaptureToReportingEnum`, `EthernetFrame`, `EthernetRawDataStreamClientMapping`, `EthernetRawDataStreamGrant`, `EthernetRawDataStreamLocalEndpointConfig`, `EthernetRawDataStreamMapping`, `EthernetRawDataStreamRemoteClientConfig`, `EthernetRawDataStreamRemoteServerConfig`, `EthernetRawDataStreamServerMapping`, `EventInExecutableInstanceRef`, `EventMapping`, `Executable`, `ExecutableImplementationProps`, `ExecutableLoggingImplementationProps`, `ExecutableTiming`, `ExecutionDependency`, `ExecutionStateReportingBehaviorEnum`, `FieldAccessEnum`, `FieldInExecutableInstanceRef`, `FieldMapping`, `FieldSenderComSpec`, `FireAndForgetMethodMapping`, `FirewallStateInFirwallStateSwitchInterfaceInstanceRef`, `FirewallStateSwitchInterface`, `ForeignModelReference`, `FunctionGroupPhmStateReference`, `FunctionGroupSet`, `FunctionGroupStateInFunctionGroupSetInstanceRef`, `FunctionalClusterInteractsWithFunctionalClusterMapping`, `FunctionalClusterInteractsWithPersistencyDeploymentMapping`, `FunctionalClusterPersistencyAccessEnum`, `FunctionalClusterToSecurityEventDefinitionMapping`, `GenericModuleInstantiation`, `GlobalSupervision`, `Grant`, `GrantDesign`, `HandleTerminationAndRestartEnum`, `HealthChannel`, `HealthChannelExternalReportedStatus`, `HealthChannelExternalStatus`, `HealthChannelSupervision`, `IPSecIamRemoteSubject`, `IPTransportProtocolEnum`, `IamModuleInstantiation`, `IdsmAbstractPortInterface`, `IdsmContextProviderInterface`, `IdsmContextProviderMapping`, `IdsmTimestampProviderInterface`, `IdsmTimestampProviderMapping`, `IkeAuthenticationMethodEnum`, `ImplementationDataTypeElementInSystemRef`, `ImpositionTimeDefinitionGroup`, `InterfaceMapping`, `IpIamAuthenticConnectionProps`, `IpIamRemoteSubject`, `KeyUsageRestrictionEnum`, `LTMessageCollectionToPortPrototypeMapping`, `LogAndTraceInstantiation`, `LogAndTraceInterface`, `LogicAddress`, `LogicalSupervision`, `Machine`, `MachineDesign`, `MachineTiming`, `MemoryUsage`, `MethodMapping`, `ModeDeclarationGroupPrototypeInExecutableInstanceRef`, `ModeDeclarationGroupPrototypeInSystemInstanceRef`, `ModeDeclarationInStateManagementStateNotificationInstanceRef`, `ModeInProcessInstanceRef`, `ModificationTypeEnum`, `NameTokenValueVariationPoint`, `NetworkHandlePortMapping`, `NetworkManagementPortInterface`, `NmHandleMappingDirectionEnum`, `NmHandleToFunctionGroupStateMapping`, `NmInstantiation`, `NmInteractsWithSmMapping`, `NmNetworkHandle`, `NmStateRequestEnum`, `NoCheckpointSupervision`, `NoSupervision`, `NonOsModuleInstantiation`, `NormalizedInstruction`, `OperationArgumentInComponentInstanceRef`, `OsArtiAdapterLaunchBehaviorEnum`, `OsModuleInstantiation`, `PPortPrototypeInExecutableInstanceRef`, `PPortPrototypeInSoftwareClusterDesignInstanceRef`, `ParameterDataPrototypeInSystemInstanceRef`, `PersistencyCollectionLevelUpdateStrategyEnum`, `PersistencyDataElement`, `PersistencyDataRequiredComSpec`, `PersistencyDeployment`, `PersistencyDeploymentElement`, `PersistencyDeploymentElementToCryptoKeySlotMapping`, `PersistencyDeploymentToCryptoKeySlotMapping`, `PersistencyDeploymentToDltLogSinkMapping`, `PersistencyDeploymentUri`, `PersistencyElementLevelUpdateStrategyEnum`, `PersistencyFile`, `PersistencyFileElement`, `PersistencyFileStorage`, `PersistencyFileStorageInterface`, `PersistencyInterface`, `PersistencyInterfaceElement`, `PersistencyKeyValueDataTypeMapping`, `PersistencyKeyValuePair`, `PersistencyKeyValueStorage`, `PersistencyKeyValueStorageInterface`, `PersistencyPortPrototypeToDeploymentMapping`, `PersistencyPortPrototypeToFileStorageMapping`, `PersistencyPortPrototypeToKeyValueStorageMapping`, `PersistencyRedundancyChecksum`, `PersistencyRedundancyCrc`, `PersistencyRedundancyEnum`, `PersistencyRedundancyHandling`, `PersistencyRedundancyHandlingScopeEnum`, `PersistencyRedundancyHash`, `PersistencyRedundancyMOutOfN`, `PhmAbstractRecoveryNotificationInterface`, `PhmCheckpoint`, `PhmCheckpointInExecutableInstanceRef`, `PhmContributionToMachineMapping`, `PhmHealthChannelInterface`, `PhmHealthChannelRecoveryNotificationInterface`, `PhmHealthChannelStatus`, `PhmRecoveryActionInterface`, `PhmStateReference`, `PhmSupervisedEntityInterface`, `PhmSupervision`, `PhmSupervisionRecoveryNotificationInterface`, `PlatformHealthManagementContribution`, `PlatformHealthManagementInterface`, `PlatformModuleEndpointConfiguration`, `PortDefinedArgumentBlueprint`, `PortInterfaceElementInImplementationDatatypeRef`, `PortInterfaceToDataTypeMapping`, `PortPrototypeInExecutableInstanceRef`, `PortPrototypeProps`, `PossibleErrorReaction`, `Process`, `ProcessArgument`, `ProcessDesign`, `ProcessDesignToMachineDesignMapping`, `ProcessExecutionError`, `ProcessToMachineMapping`, `ProcessToMachineMappingSet`, `Processor`, `ProcessorCore`, `ProvidedApServiceInstance`, `ProvidedServiceInstanceToSwClusterDesignPPortPrototypeMapping`, `ProvidedSomeipServiceInstance`, `ProvidedUserDefinedServiceInstance`, `PskIdentityToKeySlotMapping`, `RPortPrototypeInExecutableInstanceRef`, `RPortPrototypeInSoftwareClusterDesignInstanceRef`, `RPortPrototypeProps`, `RawDataStreamClientInterface`, `RawDataStreamDeployment`, `RawDataStreamEthernetTcpUdpCredentials`, `RawDataStreamEthernetUdpCredentials`, `RawDataStreamGrant`, `RawDataStreamGrantDesign`, `RawDataStreamMapping`, `RawDataStreamServerInterface`, `ReceiverIntentEnum`, `RecoveryNotification`, `RecoveryNotificationToPPortPrototypeMapping`, `RemotingTechnology`, `RemotingTechnologyEnum`, `ReportBehaviorEnum`, `RequestMethodEnum`, `RequestTypeEnum`, `RequiredApServiceInstance`, `RequiredMethodInExecutableInstanceRef`, `RequiredServiceInstanceToSwClusterDesignRPortPrototypeMapping`, `RequiredSomeipServiceInstance`, `RequiredUserDefinedServiceInstance`, `ResourceGroup`, `RootSwClusterDesignComponentPrototype`, `RootSwComponentPrototype`, `RteEventInCompositionInstanceRef`, `RteEventInSystemInstanceRef`, `SOMEIPTransformerSessionHandlingEnum`, `SearchIntentionEnum`, `SecOcDeployment`, `SecOcJobMapping`, `SecOcJobRequirement`, `SecOcJobSemanticEnum`, `SecOcSecureComProps`, `SecureComProps`, `SecureCommunicationDeployment`, `SecurityEventMapping`, `SecurityEventReportInterface`, `SecurityEventReportToSecurityEventDefinitionMapping`, `SenderIntentEnum`, `SequenceCounterMapping`, `SerializationTechnology`, `SerializationTechnologyEnum`, `ServiceDiscoveryConfiguration`, `ServiceEventDeployment`, `ServiceFieldDeployment`, `ServiceInstanceToMachineMapping`, `ServiceInstanceToPortPrototypeMapping`, `ServiceInstanceToSignalMapping`, `ServiceInstanceToSwClusterDesignPortPrototypeMapping`, `ServiceInterface`, `ServiceInterfaceDeployment`, `ServiceInterfaceElementMapping`, `ServiceInterfaceElementSecureComConfig`, `ServiceInterfaceEventMapping`, `ServiceInterfaceFieldMapping`, `ServiceInterfaceMapping`, `ServiceInterfaceMethodMapping`, `ServiceInterfacePedigree`, `ServiceInterfaceTriggerMapping`, `ServiceMethodDeployment`, `ServiceTiming`, `SignalBasedEventElementToISignalTriggeringMapping`, `SignalBasedFieldToISignalTriggeringMapping`, `SignalBasedFireAndForgetMethodToISignalTriggeringMapping`, `SignalBasedMethodToISignalTriggeringMapping`, `SignalBasedTriggerToISignalTriggeringMapping`, `SignalIPduCounter`, `SignalIPduReplication`, `SmInteractsWithNmMapping`, `SoAdConnectorType`, `SoAdProtocolType`, `SoftwareCluster`, `SoftwareClusterDependencyCompareCondition`, `SoftwareClusterDependencyFormula`, `SoftwareClusterDependencyFormulaPart`, `SoftwareClusterDependencyLogicalOperatorEnum`, `SoftwareClusterDependencyOperatorEnum`, `SoftwareClusterDesign`, `SoftwareClusterDiagnosticAddress`, `SoftwareClusterDiagnosticAddressSemanticsEnum`, `SoftwareClusterDiagnosticDeploymentProps`, `SoftwareClusterDoipDiagnosticAddress`, `SoftwareClusterInstallationBehaviorEnum`, `SoftwareClusterSovdAddress`, `SoftwareClusterUdsDiagnosticAddress`, `SoftwarePackage`, `SoftwarePackageActionTypeEnum`, `SoftwarePackageActivationActionEnum`, `SoftwarePackageStep`, `SoftwarePackageStoring`, `SoftwarePackageStoringEnum`, `SomeipCollectionProps`, `SomeipDataPrototypeTransformationProps`, `SomeipEventDeployment`, `SomeipEventGroup`, `SomeipEventProps`, `SomeipFieldDeployment`, `SomeipMethodDeployment`, `SomeipMethodProps`, `SomeipProvidedEventGroup`, `SomeipRemoteMulticastConfig`, `SomeipRemoteUnicastConfig`, `SomeipRequiredEventGroup`, `SomeipServiceDiscovery`, `SomeipServiceInstanceToMachineMapping`, `SomeipServiceInterfaceDeployment`, `SovdGatewayEthernetCredentials`, `SovdGatewayInstantiation`, `SovdGatewayLocalEndpointTcpConfig`, `SovdModuleInstantiation`, `SovdServerInstantiation`, `StartupConfig`, `StateDependentStartupConfig`, `StateManagemenPhmErrorInterface`, `StateManagementActionItem`, `StateManagementActionList`, `StateManagementCompareCondition`, `StateManagementCompareEnum`, `StateManagementCompareFormula`, `StateManagementCompareFormulaPart`, `StateManagementDiagTriggerInterface`, `StateManagementEmErrorInterface`, `StateManagementErrorCompareRule`, `StateManagementErrorInterface`, `StateManagementFunctionGroupSwitchNotificationInterface`, `StateManagementLogicalOperatorEnum`, `StateManagementModuleInstantiation`, `StateManagementNmActionItem`, `StateManagementNotificationInterface`, `StateManagementPortInterface`, `StateManagementRequestError`, `StateManagementRequestInterface`, `StateManagementRequestRule`, `StateManagementRequestTrigger`, `StateManagementSetFunctionGroupStateActionItem`, `StateManagementSleepActionItem`, `StateManagementStateMachineActionItem`, `StateManagementStateNotification`, `StateManagementStateRequest`, `StateManagementSyncActionItem`, `StateManagementTriggerCompareRule`, `StateManagementTriggerInterface`, `StdCppImplementationDataType`, `SupervisionCheckpoint`, `SupervisionMode`, `SupervisionModeCondition`, `SwComponentMappingConstraints`, `SwServiceReentranceEnum`, `SwVariableAccessImplPolicyEnum`, `SwcServiceDependencyInCompositionInstanceRef`, `SwcToEcuMappingConstraint`, `SwcToEcuMappingConstraintType`, `SynchronizedTimeBaseConsumer`, `SynchronizedTimeBaseConsumerInterface`, `SynchronizedTimeBaseProvider`, `SynchronizedTimeBaseProviderInterface`, `TDEventServiceInstance`, `TDEventServiceInstanceDiscovery`, `TDEventServiceInstanceDiscoveryTypeEnum`, `TDEventServiceInstanceEvent`, `TDEventServiceInstanceEventTypeEnum`, `TDEventServiceInstanceField`, `TDEventServiceInstanceFieldTypeEnum`, `TDEventServiceInstanceMethod`, `TDEventServiceInstanceMethodTypeEnum`, `TerminationBehaviorEnum`, `TimeBaseProviderToPersistencyMapping`, `TimeBaseResource`, `TimeSyncCorrection`, `TimeSyncModuleInstantiation`, `TimeSyncPortPrototypeToTimeBaseMapping`, `TimeSynchronizationKindEnum`, `TlsConnectionGroup`, `TlsDeployment`, `TlsIamRemoteSubject`, `TlsJobMapping`, `TlsSecureComProps`, `TpAckType`, `TraceReferrable`, `TraceSwitchConfiguration`, `TraceSwitchEnum`, `TransformationPropsToServiceInterfaceElementMapping`, `TransportLayerProtocolEnum`, `TriggerInExecutableInstanceRef`, `TrustedPlatformExecutableLaunchBehaviorEnum`, `UcmDescription`, `UcmMasterModuleInstantiation`, `UcmModuleInstantiation`, `UcmRetryStrategy`, `UcmStep`, `UcmSubordinateModuleInstantiation`, `UcmToTimeBaseResourceMapping`, `UdpCollectionTriggerEnum`, `UdpNmNetworkConfiguration`, `UploadableDeploymentElement`, `UploadableExclusivePackageElement`, `UserDefinedEventDeployment`, `UserDefinedFieldDeployment`, `UserDefinedMethodDeployment`, `UserDefinedServiceInstanceToMachineMapping`, `UserDefinedServiceInterfaceDeployment`, `V2xSupportEnum`, `VariableInComponentInstanceRef`, `VehicleDriverNotification`, `VehicleDriverNotificationEnum`, `VehiclePackage`, `VehicleRolloutStep`, `ViolatedSafetyConditionBehaviorEnum`, `XcpPdu`

## Excluded — atpVariation-generated variation-point containers

XSD documentation of each reads "This element was generated/modified due to an
atpVariation stereotype." — they are variation-point decomposition artifacts
(`*Content` attribute holders / `*Conditional` wrappers), not standalone meta-classes;
their members are owned by the parent class (`mmt.qualifiedName="Parent.attr"`).

| Class | XML element | Group |
|---|---|---|
| `AbstractCanClusterContent` | (ABSTRACT-CAN-CLUSTER-CONTENT group only) | — |
| `AbstractCanCommunicationControllerContent` | (ABSTRACT-CAN-COMMUNICATION-CONTROLLER-CONTENT group only) | — |
| `CanClusterConditional` | CAN-CLUSTER-CONDITIONAL | — |
| `CanClusterContent` | (CAN-CLUSTER-CONTENT group only) | — |
| `CanCommunicationControllerConditional` | CAN-COMMUNICATION-CONTROLLER-CONDITIONAL | — |
| `CanCommunicationControllerContent` | (CAN-COMMUNICATION-CONTROLLER-CONTENT group only) | — |
| `CommunicationClusterContent` | (COMMUNICATION-CLUSTER-CONTENT group only) | — |
| `CommunicationControllerContent` | (COMMUNICATION-CONTROLLER-CONTENT group only) | — |
| `DiagnosticCommonPropsConditional` | DIAGNOSTIC-COMMON-PROPS-CONDITIONAL | — |
| `DiagnosticCommonPropsContent` | (DIAGNOSTIC-COMMON-PROPS-CONTENT group only) | — |
| `EcucAbstractStringParamDefContent` | (ECUC-ABSTRACT-STRING-PARAM-DEF-CONTENT group only) | — |
| `EcucFunctionNameDefConditional` | ECUC-FUNCTION-NAME-DEF-CONDITIONAL | — |
| `EcucFunctionNameDefContent` | (ECUC-FUNCTION-NAME-DEF-CONTENT group only) | — |
| `EcucLinkerSymbolDefConditional` | ECUC-LINKER-SYMBOL-DEF-CONDITIONAL | — |
| `EcucLinkerSymbolDefContent` | (ECUC-LINKER-SYMBOL-DEF-CONTENT group only) | — |
| `EcucMultilineStringParamDefConditional` | ECUC-MULTILINE-STRING-PARAM-DEF-CONDITIONAL | — |
| `EcucMultilineStringParamDefContent` | (ECUC-MULTILINE-STRING-PARAM-DEF-CONTENT group only) | — |
| `EcucStringParamDefConditional` | ECUC-STRING-PARAM-DEF-CONDITIONAL | — |
| `EcucStringParamDefContent` | (ECUC-STRING-PARAM-DEF-CONTENT group only) | — |
| `EndToEndTransformationISignalPropsConditional` | END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL | — |
| `EndToEndTransformationISignalPropsContent` | (END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONTENT group only) | — |
| `EthernetClusterConditional` | ETHERNET-CLUSTER-CONDITIONAL | — |
| `EthernetClusterContent` | (ETHERNET-CLUSTER-CONTENT group only) | — |
| `EthernetCommunicationControllerConditional` | ETHERNET-COMMUNICATION-CONTROLLER-CONDITIONAL | — |
| `EthernetCommunicationControllerContent` | (ETHERNET-COMMUNICATION-CONTROLLER-CONTENT group only) | — |
| `FlexrayClusterConditional` | FLEXRAY-CLUSTER-CONDITIONAL | — |
| `FlexrayClusterContent` | (FLEXRAY-CLUSTER-CONTENT group only) | — |
| `FlexrayCommunicationControllerConditional` | FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL | — |
| `FlexrayCommunicationControllerContent` | (FLEXRAY-COMMUNICATION-CONTROLLER-CONTENT group only) | — |
| `J1939ClusterConditional` | J-1939-CLUSTER-CONDITIONAL | — |
| `J1939ClusterContent` | (J-1939-CLUSTER-CONTENT group only) | — |
| `LinClusterConditional` | LIN-CLUSTER-CONDITIONAL | — |
| `LinClusterContent` | (LIN-CLUSTER-CONTENT group only) | — |
| `LinCommunicationControllerContent` | (LIN-COMMUNICATION-CONTROLLER-CONTENT group only) | — |
| `LinMasterConditional` | LIN-MASTER-CONDITIONAL | — |
| `LinMasterContent` | (LIN-MASTER-CONTENT group only) | — |
| `LinSlaveConditional` | LIN-SLAVE-CONDITIONAL | — |
| `LinSlaveContent` | (LIN-SLAVE-CONTENT group only) | — |
| `McFunctionDataRefSetConditional` | MC-FUNCTION-DATA-REF-SET-CONDITIONAL | — |
| `McFunctionDataRefSetContent` | (MC-FUNCTION-DATA-REF-SET-CONTENT group only) | — |
| `McGroupDataRefSetConditional` | MC-GROUP-DATA-REF-SET-CONDITIONAL | — |
| `McGroupDataRefSetContent` | (MC-GROUP-DATA-REF-SET-CONTENT group only) | — |
| `SOMEIPTransformationISignalPropsConditional` | SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL | — |
| `SOMEIPTransformationISignalPropsContent` | (SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-CONTENT group only) | — |
| `SwDataDefPropsConditional` | SW-DATA-DEF-PROPS-CONDITIONAL | — |
| `SwDataDefPropsContent` | (SW-DATA-DEF-PROPS-CONTENT group only) | — |
| `TransformationISignalPropsContent` | (TRANSFORMATION-I-SIGNAL-PROPS-CONTENT group only) | — |
| `TtcanClusterConditional` | TTCAN-CLUSTER-CONDITIONAL | — |
| `TtcanClusterContent` | (TTCAN-CLUSTER-CONTENT group only) | — |
| `TtcanCommunicationControllerConditional` | TTCAN-COMMUNICATION-CONTROLLER-CONDITIONAL | — |
| `TtcanCommunicationControllerContent` | (TTCAN-COMMUNICATION-CONTROLLER-CONTENT group only) | — |
| `UserDefinedClusterConditional` | USER-DEFINED-CLUSTER-CONDITIONAL | — |
| `UserDefinedClusterContent` | (USER-DEFINED-CLUSTER-CONTENT group only) | — |
| `UserDefinedCommunicationControllerConditional` | USER-DEFINED-COMMUNICATION-CONTROLLER-CONDITIONAL | — |
| `UserDefinedCommunicationControllerContent` | (USER-DEFINED-COMMUNICATION-CONTROLLER-CONTENT group only) | — |
| `UserDefinedTransformationISignalPropsConditional` | USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL | — |
| `UserDefinedTransformationISignalPropsContent` | (USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-CONTENT group only) | — |
