# Docstring Coverage Report

Generated for manual review. Flag any inaccurate docstrings for correction.
**Overall: 815/815 documented (100.0%), 0 missing**


## data_models

### data_models/sw_connector.py

- **SwConnectorData** (L1): Base data class for SW connector data with short name.
- **DelegationSwConnectorData** (L8): Data for delegation SW connectors with inner and outer port, SWC
- **AssemblySwConnectorData** (L22): Data for assembly SW connectors with provider/requester SWC and port

> Coverage: 3/3 (100.0%)

## lib

### lib/cli_args_parser.py

- **InputFileParser** (L7): Parser for CLI input arguments that resolves directories, file lists,

### lib/sw_component.py

- **SwComponentAnalyzer** (L7): Analyzer that collects and displays software component types from the

### lib/system_signal.py

- **SystemSignalAnalyzer** (L7): Analyzer that collects and displays system signals from the AUTOSAR

> Coverage: 3/3 (100.0%)

## models/M2/AUTOSARTemplates

### models/M2/AUTOSARTemplates/ECUCDescriptionTemplate.py

- **EcucValueCollection** (L13): Collection of ECUC values with references to ECU extract.
- **EcucIndexableValue** (L38): Abstract base class for indexable ECUC values.
- **EcucParameterValue** (L49): Abstract base class for ECUC parameter values with annotation,
- **EcucAddInfoParamValue** (L86): ECUC parameter value for additional info with documentation block
- **EcucTextualParamValue** (L103): ECUC parameter value for textual string values.
- **EcucNumericalParamValue** (L119): ECUC parameter value for numerical values.
- **EcucAbstractReferenceValue** (L135): Abstract base class for ECUC reference values with annotation,
- **EcucInstanceReferenceValue** (L172): ECUC reference value using an AnyInstanceRef for instance-based
- **EcucReferenceValue** (L190): ECUC reference value using a RefType for standard references.
- **EcucContainerValue** (L207): Container value holding parameter values, reference values, and
- **EcucModuleConfigurationValues** (L252): ECUC module configuration values with containers, definition
- **EcucConditionSpecification** (L313): Condition specification for ECUC definitions with condition formula
- **EcucConfigurationVariantEnum** (L326): Enumeration for ECUC configuration variant types.

### models/M2/AUTOSARTemplates/ECUCParameterDefTemplate.py

- **EcucConditionSpecification** (L14): Represents an ECUC (Electronic Control Unit Configuration) condition specification
- **EcucValidationCondition** (L38): Represents an ECUC validation condition in the AUTOSAR model.
- **EcucScopeEnum** (L53): Enumeration for ECUC definition scope types.
- **EcucDefinitionElement** (L61): Represents an ECUC (Electronic Control Unit Configuration) definition element
- **EcucDestinationUriDefRefType** (L173): EcucDestinationUriDefRefType is a class that represents a reference type 
- **EcucConfigurationClassEnum** (L189): Enumeration for ECUC configuration class types.
- **EcucConfigurationVariantEnum** (L197): Enumeration for ECUC configuration variant types.
- **EcucAbstractConfigurationClass** (L205): Represents an abstract configuration class for ECUC (Electronic Control Unit Configuration).
- **EcucMultiplicityConfigurationClass** (L249): EcucMultiplicityConfigurationClass is a subclass of EcucAbstractConfigurationClass.
- **EcucContainerDef** (L266): Represents an ECUC container definition in the AUTOSAR model.
- **EcucValueConfigurationClass** (L369): EcucValueConfigurationClass is a subclass of EcucAbstractConfigurationClass.
- **EcucCommonAttributes** (L384): EcucCommonAttributes is an abstract base class that represents common attributes 
- **EcucDerivationSpecification** (L490): Represents an ECUC Derivation Specification in the AUTOSAR model.
- **EcucParameterDef** (L501): Represents an ECUC (Electronic Control Unit Configuration) parameter definition
- **EcucBooleanParamDef** (L562): Represents a boolean parameter definition in the AUTOSAR ECUC model.
- **EcucAbstractReferenceDef** (L587): EcucAbstractReferenceDef is an abstract class that extends EcucCommonAttributes and uses ABCMeta as its metaclass.
- **EcucAbstractInternalReferenceDef** (L619): EcucAbstractInternalReferenceDef is an abstract class that extends EcucAbstractReferenceDef 
- **EcucAbstractExternalReferenceDef** (L649): Abstract base class for ECUC external reference definitions.
- **EcucSymbolicNameReferenceDef** (L660): ECUC reference definition using symbolic names with a destination
- **EcucChoiceReferenceDef** (L679): ECUC reference definition for choice containers with a destination
- **EcucReferenceDef** (L698): ECUC reference definition with a destination reference.
- **EcucUriReferenceDef** (L716): ECUC reference definition using a URI with a destination URI
- **EcucForeignReferenceDef** (L735): ECUC reference definition to a foreign context with destination
- **EcucInstanceReferenceDef** (L763): ECUC reference definition for instance-based references with
- **EcucAbstractStringParamDef** (L782): EcucAbstractStringParamDef is an abstract class that represents a string parameter definition
- **EcucStringParamDef** (L856): Represents a specific type of ECUC parameter definition for string parameters.
- **EcucFunctionNameDef** (L871): Represents a specific type of ECUC parameter definition for function names.
- **EcucIntegerParamDef** (L886): ECUC integer parameter definition with default value, min, and max
- **EcucEnumerationLiteralDef** (L923): Represents an ECUC Enumeration Literal Definition in the AUTOSAR model.
- **EcucEnumerationParamDef** (L966): Represents an ECUC (Electronic Control Unit Configuration) enumeration parameter definition.
- **EcucFloatParamDef** (L1011): ECUC float parameter definition with default value, min, and max
- **EcucChoiceContainerDef** (L1048): Represents an ECUC choice container definition in the AUTOSAR model.
- **EcucParamConfContainerDef** (L1075): Represents a configuration container definition in the AUTOSAR ECUC model.
- **EcucAddInfoParamDef** (L1291): Represents an ECUC additional info parameter definition in the AUTOSAR model.
- **EcucConditionFormula** (L1317): Represents an ECUC condition formula in the AUTOSAR model.
- **EcucDefinitionCollection** (L1341): Represents an ECUC definition collection in the AUTOSAR model.
- **EcucDestinationUriDef** (L1364): Represents an ECUC destination URI definition in the AUTOSAR model.
- **EcucDestinationUriDefSet** (L1389): Represents an ECUC destination URI definition set in the AUTOSAR model.
- **EcucDestinationUriPolicy** (L1414): Represents an ECUC destination URI policy in the AUTOSAR model.
- **EcucLinkerSymbolDef** (L1437): Represents an ECUC linker symbol definition in the AUTOSAR model.
- **EcucMultilineStringParamDef** (L1462): Represents an ECUC multiline string parameter definition in the AUTOSAR model.
- **EcucParameterDerivationFormula** (L1477): Represents an ECUC parameter derivation formula in the AUTOSAR model.
- **EcucQuery** (L1500): Represents an ECUC query in the AUTOSAR model.
- **EcucQueryExpression** (L1523): Represents an ECUC query expression in the AUTOSAR model.
- **EcucModuleDef** (L1546): ECUC module definition with API service prefix, container

> Coverage: 58/58 (100.0%)

## models/M2/AUTOSARTemplates/AbstractPlatform

### models/M2/AUTOSARTemplates/AbstractPlatform/ApplicationDeferredDataType.py

- **ApplicationDeferredDataType** (L9): A placeholder data type in which the precise application data type is

### models/M2/AUTOSARTemplates/AbstractPlatform/ApplicationInterface.py

- **ApplicationInterface** (L19): This represents the ability to define a PortInterface that consists of a

> Coverage: 2/2 (100.0%)

## models/M2/AUTOSARTemplates/AdaptivePlatform/ApplicationDesign/PortInterface

### models/M2/AUTOSARTemplates/AdaptivePlatform/ApplicationDesign/PortInterface/Field.py

- **Field** (L6): This meta-class represents the ability to define a piece of data that can be

> Coverage: 1/1 (100.0%)

## models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/AdaptiveModule

### models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/AdaptiveModule/PlatformModuleEthernetEndpointConfiguration.py

- **PlatformModuleEthernetEndpointConfiguration** (L16): This meta-class defines the attributes for the configuration of a port,

> Coverage: 1/1 (100.0%)

## models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment

### models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment/CryptoKeySlot.py

- **CryptoKeySlot** (L22): This meta-class represents the ability to define a concrete key to be used

### models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment/CryptoKeySlotContent.py

- **CryptoKeySlotContent** (L9): This meta-class represents the restriction of allowed usage of a key stored

> Coverage: 2/2 (100.0%)

## models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall

### models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/FirewallRule.py

- **FirewallRule** (L6): Represents a firewall rule in AUTOSAR Adaptive Platform PlatformModuleDeployment.

### models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/FirewallRuleProps.py

- **FirewallRuleProps** (L4): Represents firewall rule properties in AUTOSAR Adaptive Platform PlatformModuleDeployment.

### models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/StateDependentFirewall.py

- **StateDependentFirewall** (L6): Represents a state-dependent firewall in AUTOSAR Adaptive Platform PlatformModuleDeployment.

> Coverage: 3/3 (100.0%)

## models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/IntrusionDetectionSystem

### models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/IntrusionDetectionSystem/IdsPlatformInstantiation.py

- **IdsPlatformInstantiation** (L11): This meta-class acts as an abstract base class for platform modules that

### models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/IntrusionDetectionSystem/IdsmModuleInstantiation.py

- **IdsmModuleInstantiation** (L9): This meta-class defines the attributes for the IdsM configuration on a

> Coverage: 2/2 (100.0%)

## models/M2/AUTOSARTemplates/BswModuleTemplate

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior.py

- **BswModuleCallPoint** (L29): Represents a call point for a BSW module, which defines how the module can be called.
- **BswAsynchronousServerCallPoint** (L74): Represents an asynchronous server call point in a BSW module.
- **BswDirectCallPoint** (L118): Represents a direct call point in a BSW module.
- **BswSynchronousServerCallPoint** (L188): Represents a synchronous server call point in a BSW module.
- **BswAsynchronousServerCallResultPoint** (L258): Represents a result point for an asynchronous server call in a BSW module.
- **BswVariableAccess** (L278): Represents access to a variable by a BSW module entity.
- **BswDistinguishedPartition** (L344): Each instance of this meta-class represents an abstract partition in which context 
- **BswModuleEntity** (L364): Abstract base class for BSW module entities.
- **BswCalledEntity** (L638): Represents a BSW module entity that can be called by other entities.
- **BswSchedulableEntity** (L655): Represents a BSW module entity that can be scheduled for execution.
- **BswInterruptCategory** (L672): Enumeration for BSW interrupt categories.
- **BswInterruptEntity** (L692): Represents an interrupt entity in a BSW module.
- **BswEvent** (L758): Abstract base class for BSW events.
- **BswOperationInvokedEvent** (L803): Represents an event that is triggered when a BSW operation is invoked.
- **BswScheduleEvent** (L847): Abstract base class for BSW scheduled events.
- **BswModeSwitchEvent** (L867): Represents an event that is triggered when a mode switch occurs.
- **BswModeSwitchedAckEvent** (L909): Represents an event that is triggered when a mode switch acknowledgment occurs.
- **BswTimingEvent** (L927): Represents a timing event in a BSW module.
- **BswDataReceivedEvent** (L983): Represents an event that is triggered when data is received by a BSW module.
- **BswInternalTriggerOccurredEvent** (L1025): Represents an event that is triggered by an internal trigger in a BSW module.
- **BswModeSwitchAckRequest** (L1067): Represents an acknowledgment request for a mode switch operation.
- **BswModeSenderPolicy** (L1105): Represents the policy for a BSW mode sender.
- **BswBackgroundEvent** (L1177): Represents a background event in a BSW module.
- **BswOsTaskExecutionEvent** (L1194): Represents an OS task execution event in a BSW module.
- **BswExternalTriggerOccurredEvent** (L1211): Represents an event that is triggered by an external trigger in a BSW module.
- **BswApiOptions** (L1255): Abstract base class for BSW API options.
- **BswDataReceptionPolicy** (L1299): Abstract base class for BSW data reception policies.
- **BswQueuedDataReceptionPolicy** (L1343): Represents a queued data reception policy in a BSW module.
- **BswInternalTriggeringPoint** (L1383): Represents an internal triggering point in a BSW module's internal behavior.
- **BswInternalBehavior** (L1427): Represents the internal behavior of a BSW module.

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswImplementation.py

- **BswImplementation** (L12): Represents a Basic Software (BSW) implementation in AUTOSAR.

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces.py

- **BswEntryKindEnum** (L19): Enumeration for BSW Entry Kind values.
- **BswCallType** (L28): Enumeration for BSW Call Type values.
- **BswExecutionContext** (L39): Enumeration for BSW Execution Context values.
- **SwServiceImplPolicyEnum** (L56): Enumeration for SW Service Implementation Policy values.
- **BswModuleDependency** (L71): Represents a dependency relationship between BSW modules.
- **BswModuleEntry** (L167): Represents an entry point in a BSW module.
- **BswModuleClientServerEntry** (L493): Represents a client-server entry in a BSW module.

> Coverage: 38/38 (100.0%)

## models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswAsynchronousServerCallReturnsEvent.py

- **BswAsynchronousServerCallReturnsEvent** (L9): Represents a BSW asynchronous server call returns event in AUTOSAR.

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswExclusiveAreaPolicy.py

- **BswExclusiveAreaPolicy** (L8): Enumeration for BSW exclusive area policy.

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswInterruptEvent.py

- **BswInterruptEvent** (L8): Represents a BSW interrupt event in AUTOSAR.

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswModeManagerErrorEvent.py

- **BswModeManagerErrorEvent** (L8): Represents a BSW mode manager error event in AUTOSAR.

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswModeReceiverPolicy.py

- **BswModeReceiverPolicy** (L8): Enumeration for BSW mode receiver policy.

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswSchedulerNamePrefix.py

- **BswSchedulerNamePrefix** (L8): Represents a BSW scheduler name prefix in AUTOSAR.

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswServiceDependency.py

- **BswServiceDependency** (L9): Represents a BSW service dependency in AUTOSAR.

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/BswTriggerDirectImplementation.py

- **BswTriggerDirectImplementation** (L9): Enumeration for BSW trigger direct implementation.

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/RoleBasedBswModuleEntryAssignment.py

- **RoleBasedBswModuleEntryAssignment** (L9): Represents a role-based BSW module entry assignment in AUTOSAR.

> Coverage: 9/9 (100.0%)

## models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces/BswEntryRelationship.py

- **BswEntryRelationship** (L8): Represents a BSW entry relationship in AUTOSAR.

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces/BswEntryRelationshipEnum.py

- **BswEntryRelationshipEnum** (L8): Enumeration for BSW entry relationship types.

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswInterfaces/BswEntryRelationshipSet.py

- **BswEntryRelationshipSet** (L8): Represents a set of BSW entry relationships in AUTOSAR.

> Coverage: 3/3 (100.0%)

## models/M2/AUTOSARTemplates/BswModuleTemplate/BswOverview/InstanceRefs

### models/M2/AUTOSARTemplates/BswModuleTemplate/BswOverview/InstanceRefs/ModeInBswModuleDescriptionInstanceRef.py

- **ModeInBswModuleDescriptionInstanceRef** (L16): Sources:

> Coverage: 1/1 (100.0%)

## models/M2/AUTOSARTemplates/CommonStructure

### models/M2/AUTOSARTemplates/CommonStructure/Filter.py

- **DataFilterTypeEnum** (L11): Enumeration for data filter types in AUTOSAR models.
- **DataFilter** (L47): Represents a data filter configuration in AUTOSAR models.

### models/M2/AUTOSARTemplates/CommonStructure/FlatMap.py

- **FlatInstanceDescriptor** (L16): Represents a flat instance descriptor in AUTOSAR models.
- **FlatMap** (L154): Represents a flat map in AUTOSAR models.
- **AliasNameAssignment** (L199): Represents an alias name assignment in AUTOSAR.
- **AliasNameSet** (L228): Represents a set of alias name assignments.
- **RtePluginProps** (L247): Represents RTE plugin properties in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/Implementation.py

- **ImplementationProps** (L16): Abstract base class for implementation properties in AUTOSAR models.
- **Code** (L62): Represents code descriptor in AUTOSAR models.
- **Compiler** (L112): Represents a compiler in AUTOSAR models.
- **DependencyOnArtifact** (L226): Represents a dependency on an artifact in AUTOSAR models.
- **Implementation** (L292): Abstract base class for implementations in AUTOSAR models.
- **DependencyUsageEnum** (L696): Enumeration for dependency usage.
- **Linker** (L711): Represents a linker configuration in AUTOSAR.
- **ProgramminglanguageEnum** (L740): Enumeration for programming languages.

### models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py

- **AbstractImplementationDataTypeElement** (L13): Abstract base class for implementation data type elements.
- **ImplementationDataTypeElement** (L23): Element of an implementation data type defining array properties,
- **AbstractImplementationDataType** (L101): Abstract base class for implementation data types.
- **ImplementationDataType** (L112): Represents an implementation data type in AUTOSAR models.
- **ArrayImplPolicyEnum** (L319): Enumeration for array implementation policy.
- **ArraySizeSemanticsEnum** (L334): Enumeration for array size semantics.

### models/M2/AUTOSARTemplates/CommonStructure/InternalBehavior.py

- **ReentrancyLevelEnum** (L17): Enumeration for reentrancy levels in AUTOSAR executable entities.
- **ExclusiveArea** (L30): Represents an exclusive area in AUTOSAR models.
- **ExecutableEntity** (L48): Abstract base class for executable entities in AUTOSAR models.
- **InternalBehavior** (L203): Abstract base class for internal behavior in AUTOSAR models.
- **AbstractEvent** (L330): Represents an abstract event in AUTOSAR models.
- **ApiPrincipleEnum** (L377): Enumeration for API principle.
- **ExclusiveAreaNestingOrder** (L392): Represents exclusive area nesting order in AUTOSAR.
- **ExecutableEntityActivationReason** (L413): Represents the reason for executable entity activation in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/McGroups.py

- **McGroup** (L8): Represents a measurement and calibration group in AUTOSAR.
- **McGroupDataRefSet** (L37): Represents a set of MC group data references.

### models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py

- **ModeActivationKind** (L16): Enumeration for mode activation kind values.
- **ModeDeclarationGroupPrototypeMapping** (L29): Represents a mapping between mode declaration group prototypes in AUTOSAR models.
- **ModeDeclaration** (L121): Represents a mode declaration in AUTOSAR models.
- **ModeRequestTypeMap** (L164): Represents a mapping between mode requests and implementation data types in AUTOSAR models.
- **ModeDeclarationGroup** (L228): Represents a mode declaration group in AUTOSAR models.
- **ModeDeclarationGroupPrototype** (L332): Represents a mode declaration group prototype in AUTOSAR models.

### models/M2/AUTOSARTemplates/CommonStructure/ModeDeclarationExtra.py

- **ModeTransition** (L9): Represents a mode transition in AUTOSAR.
- **ModeErrorBehavior** (L38): Represents mode error behavior in AUTOSAR.
- **ModeErrorReactionPolicyEnum** (L59): Enumeration for mode error reaction policy.

### models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py

- **RoleBasedDataAssignment** (L18): Represents a role-based data assignment in AUTOSAR models.
- **ServiceNeeds** (L132): Abstract base class for service needs in AUTOSAR models.
- **RamBlockStatusControlEnum** (L153): Enumeration for RAM block status control methods in AUTOSAR NV block needs.
- **NvBlockNeedsReliabilityEnum** (L173): Enumeration for NV block needs reliability levels in AUTOSAR models.
- **NvBlockNeedsWritingPriorityEnum** (L196): Enumeration for NV block needs writing priorities in AUTOSAR models.
- **NvBlockNeeds** (L219): Represents NV (Non-Volatile) block needs in AUTOSAR models.
- **RoleBasedDataTypeAssignment** (L436): Represents a role-based data type assignment in AUTOSAR models.
- **ServiceDiagnosticRelevanceEnum** (L500): Enumeration for service diagnostic relevance in AUTOSAR models.
- **ServiceDependency** (L513): Represents a service dependency in AUTOSAR models.
- **DiagnosticAudienceEnum** (L608): Enumeration for diagnostic audiences in AUTOSAR models.
- **DiagnosticServiceRequestCallbackTypeEnum** (L637): Enumeration for diagnostic service request callback types in AUTOSAR models.
- **DiagnosticCapabilityElement** (L657): Abstract base class for diagnostic capability elements in AUTOSAR models.
- **DiagnosticRoutineTypeEnum** (L753): Enumeration for diagnostic routine types in AUTOSAR models.
- **DiagnosticCommunicationManagerNeeds** (L773): Represents diagnostic communication manager needs in AUTOSAR models.
- **DiagnosticRoutineNeeds** (L816): Represents diagnostic routine needs in AUTOSAR models.
- **DiagnosticValueAccessEnum** (L884): Enumeration for diagnostic value access types in AUTOSAR models.
- **DiagnosticProcessingStyleEnum** (L907): Enumeration for diagnostic processing styles in AUTOSAR models.
- **DiagnosticValueNeeds** (L930): Represents diagnostic value needs in AUTOSAR models.
- **DiagEventDebounceAlgorithm** (L1073): Abstract base class for diagnostic event debounce algorithms in AUTOSAR models.
- **DiagEventDebounceCounterBased** (L1094): Represents a counter-based diagnostic event debounce algorithm in AUTOSAR models.
- **DiagEventDebounceMonitorInternal** (L1193): Represents an internal monitor-based diagnostic event debounce algorithm in AUTOSAR models.
- **DiagEventDebounceTimeBased** (L1210): Represents a time-based diagnostic event debounce algorithm in AUTOSAR models.
- **DtcKindEnum** (L1255): Enumeration for DTC (Diagnostic Trouble Code) kinds in AUTOSAR models.
- **DiagnosticEventInfoNeeds** (L1268): Represents diagnostic event information needs in AUTOSAR models.
- **DiagnosticClearDtcNotificationEnum** (L1364): Enumeration for diagnostic clear DTC notification types in AUTOSAR models.
- **DtcFormatTypeEnum** (L1377): Enumeration for DTC format types in AUTOSAR models.
- **DtcStatusChangeNotificationNeeds** (L1390): Represents DTC status change notification needs in AUTOSAR models.
- **DiagnosticEventNeeds** (L1461): Represents diagnostic event needs in AUTOSAR models.
- **CryptoServiceNeeds** (L1712): Represents cryptographic service needs in AUTOSAR models.
- **EcuStateMgrUserNeeds** (L1830): Represents ECU state manager user needs in AUTOSAR models.
- **DltUserNeeds** (L1847): Represents DLT (Diagnostic Log and Trace) user needs in AUTOSAR models.
- **BswMgrNeeds** (L1864): Represents BSW Manager needs in AUTOSAR models.
- **ComMgrUserNeeds** (L1881): Represents Communication Manager user needs in AUTOSAR models.
- **CryptoKeyManagementNeeds** (L1898): Represents Cryptographic Key Management needs in AUTOSAR models.
- **CryptoServiceJobNeeds** (L1915): Represents Cryptographic Service Job needs in AUTOSAR models.
- **DevelopmentError** (L1932): Represents a development error in AUTOSAR models.
- **DiagnosticComponentNeeds** (L1961): Represents Diagnostic Component needs in AUTOSAR models.
- **DiagnosticControlNeeds** (L1978): Represents Diagnostic Control needs in AUTOSAR models.
- **DiagnosticDenominatorConditionEnum** (L1995): Enumeration for diagnostic denominator condition types.
- **DiagnosticEnableConditionNeeds** (L2010): Represents Diagnostic Enable Condition needs in AUTOSAR models.
- **DiagnosticEventManagerNeeds** (L2027): Represents Diagnostic Event Manager needs in AUTOSAR models.
- **DiagnosticIoControlNeeds** (L2044): Represents Diagnostic I/O Control needs in AUTOSAR models.
- **DiagnosticMonitorUpdateKindEnum** (L2061): Enumeration for diagnostic monitor update kinds.
- **DiagnosticOperationCycleNeeds** (L2076): Represents Diagnostic Operation Cycle needs in AUTOSAR models.
- **DiagnosticRequestFileTransferNeeds** (L2093): Represents Diagnostic Request File Transfer needs in AUTOSAR models.
- **DiagnosticStorageConditionNeeds** (L2110): Represents Diagnostic Storage Condition needs in AUTOSAR models.
- **DiagnosticUploadDownloadNeeds** (L2127): Represents Diagnostic Upload/Download needs in AUTOSAR models.
- **DiagnosticsCommunicationSecurityNeeds** (L2144): Represents Diagnostics Communication Security needs in AUTOSAR models.
- **DoIpActivationLineNeeds** (L2161): Represents DoIP Activation Line needs in AUTOSAR models.
- **DoIpGidNeeds** (L2178): Represents DoIP GID needs in AUTOSAR models.
- **DoIpGidSynchronizationNeeds** (L2195): Represents DoIP GID Synchronization needs in AUTOSAR models.
- **DoIpPowerModeStatusNeeds** (L2212): Represents DoIP Power Mode Status needs in AUTOSAR models.
- **DoIpRoutingActivationAuthenticationNeeds** (L2229): Represents DoIP Routing Activation Authentication needs in AUTOSAR models.
- **DoIpRoutingActivationConfirmationNeeds** (L2246): Represents DoIP Routing Activation Confirmation needs in AUTOSAR models.
- **DoIpServiceNeeds** (L2263): Represents DoIP Service needs in AUTOSAR models.
- **ErrorTracerNeeds** (L2280): Represents Error Tracer needs in AUTOSAR models.
- **EventAcceptanceStatusEnum** (L2297): Enumeration for event acceptance status types.
- **FunctionInhibitionAvailabilityNeeds** (L2312): Represents Function Inhibition Availability needs in AUTOSAR models.
- **FunctionInhibitionNeeds** (L2329): Represents Function Inhibition needs in AUTOSAR models.
- **FurtherActionByteNeeds** (L2346): Represents Further Action Byte needs in AUTOSAR models.
- **GlobalSupervisionNeeds** (L2363): Represents Global Supervision needs in AUTOSAR models.
- **HardwareTestNeeds** (L2380): Represents Hardware Test needs in AUTOSAR models.
- **IdsMgrCustomTimestampNeeds** (L2397): Represents IDS Manager Custom Timestamp needs in AUTOSAR models.
- **IdsMgrNeeds** (L2414): Represents IDS Manager needs in AUTOSAR models.
- **IndicatorStatusNeeds** (L2431): Represents Indicator Status needs in AUTOSAR models.
- **J1939DcmDm19Support** (L2448): Represents J1939 DCM DM19 Support needs in AUTOSAR models.
- **J1939RmIncomingRequestServiceNeeds** (L2465): Represents J1939 RM Incoming Request Service needs in AUTOSAR models.
- **J1939RmOutgoingRequestServiceNeeds** (L2482): Represents J1939 RM Outgoing Request Service needs in AUTOSAR models.
- **MaxCommModeEnum** (L2499): Enumeration for maximum communication mode types.
- **ObdControlServiceNeeds** (L2516): Represents OBD Control Service needs in AUTOSAR models.
- **ObdInfoServiceNeeds** (L2533): Represents OBD Info Service needs in AUTOSAR models.
- **ObdMonitorServiceNeeds** (L2550): Represents OBD Monitor Service needs in AUTOSAR models.
- **ObdPidServiceNeeds** (L2567): Represents OBD PID Service needs in AUTOSAR models.
- **ObdRatioConnectionKindEnum** (L2584): Enumeration for OBD ratio connection kind types.
- **ObdRatioDenominatorNeeds** (L2599): Represents OBD Ratio Denominator needs in AUTOSAR models.
- **ObdRatioServiceNeeds** (L2616): Represents OBD Ratio Service needs in AUTOSAR models.
- **OperationCycleTypeEnum** (L2633): Enumeration for operation cycle type.
- **RuntimeError** (L2650): Represents a runtime error in AUTOSAR models.
- **SecureOnBoardCommunicationNeeds** (L2679): Represents Secure On-Board Communication needs in AUTOSAR models.
- **ServiceProviderEnum** (L2696): Enumeration for service provider types.
- **StorageConditionStatusEnum** (L2713): Enumeration for storage condition status types.
- **SupervisedEntityCheckpointNeeds** (L2728): Represents Supervised Entity Checkpoint needs in AUTOSAR models.
- **SupervisedEntityNeeds** (L2745): Represents Supervised Entity needs in AUTOSAR models.
- **SymbolicNameProps** (L2762): Represents Symbolic Name properties in AUTOSAR models.
- **SyncTimeBaseMgrUserNeeds** (L2783): Represents Synchronized Time Base Manager User needs in AUTOSAR models.
- **TracedFailure** (L2800): Represents a Traced Failure in AUTOSAR models.
- **TransientFault** (L2829): Represents a Transient Fault in AUTOSAR models.
- **V2xDataManagerNeeds** (L2858): Represents V2X Data Manager needs in AUTOSAR models.
- **V2xFacUserNeeds** (L2875): Represents V2X Functional Application Cluster User needs in AUTOSAR models.
- **V2xMUserNeeds** (L2892): Represents V2X Manager User needs in AUTOSAR models.
- **VendorSpecificServiceNeeds** (L2909): Represents Vendor Specific Service needs in AUTOSAR models.
- **VerificationStatusIndicationModeEnum** (L2926): Enumeration for verification status indication mode types.
- **WarningIndicatorRequestedBitNeeds** (L2941): Represents Warning Indicator Requested Bit needs in AUTOSAR models.

### models/M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py

- **SwcBswRunnableMapping** (L13): Represents a mapping between BSW module entities and SWC runnable entities in AUTOSAR models.
- **SwcBswMapping** (L79): Represents SWC-BSW mapping in AUTOSAR models.
- **SwcBswSynchronizedModeGroupPrototype** (L221): Represents a SWC-BSW synchronized mode group prototype in AUTOSAR.
- **SwcBswSynchronizedTrigger** (L257): Represents a SWC-BSW synchronized trigger in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/TriggerDeclaration.py

- **Trigger** (L14): Represents a trigger in AUTOSAR models.
- **TriggerMapping** (L84): Represents a mapping between triggers in AUTOSAR models.

> Coverage: 139/139 (100.0%)

## models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/ImplementationElementInParameterInstanceRef.py

- **ImplementationElementInParameterInstanceRef** (L5): Represents a reference to an implementation element in a parameter instance.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/McDataAccessDetails.py

- **McDataAccessDetails** (L4): Represents MC (Measurement and Calibration) data access details in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/McDataInstance.py

- **McDataInstance** (L6): Represents an MC (Measurement and Calibration) data instance in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/McFunction.py

- **McFunction** (L6): Represents an MC (Measurement and Calibration) function in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/McParameterElementGroup.py

- **McParameterElementGroup** (L6): Represents an MC (Measurement and Calibration) parameter element group in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/McSupportData.py

- **McSupportData** (L6): Represents MC (Measurement and Calibration) support data in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/McSwEmulationMethodSupport.py

- **McSwEmulationMethodSupport** (L4): Represents MC (Measurement and Calibration) software emulation method support in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RoleBasedMcDataAssignment.py

- **RoleBasedMcDataAssignment** (L5): Represents a role-based MC (Measurement and Calibration) data assignment in AUTOSAR.

> Coverage: 8/8 (100.0%)

## models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/McFunctionDataRefSet.py

- **McFunctionDataRefSet** (L6): Represents a set of MC function data references in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptAccessEnum.py

- **RptAccessEnum** (L4): Enumeration for RPT (Read-Protect-Transform) access types in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptComponent.py

- **RptComponent** (L4): Represents an RPT (Read-Protect-Transform) component in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptEnablerImplTypeEnum.py

- **RptEnablerImplTypeEnum** (L4): Enumeration for RPT enabler implementation types in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptExecutableEntity.py

- **RptExecutableEntity** (L6): Represents an RPT executable entity in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptExecutableEntityEvent.py

- **RptExecutableEntityEvent** (L6): Represents an RPT executable entity event in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptExecutionContext.py

- **RptExecutionContext** (L5): Represents an RPT execution context in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptExecutionControlEnum.py

- **RptExecutionControlEnum** (L4): Enumeration for RPT execution control types in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptPreparationEnum.py

- **RptPreparationEnum** (L4): Enumeration for RPT preparation types in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptServicePoint.py

- **RptServicePoint** (L6): Represents an RPT service point in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptSupportData.py

- **RptSupportData** (L9): Represents RPT support data in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/MeasurementCalibrationSupport/RptSupport/RptSwPrototypingAccess.py

- **RptSwPrototypingAccess** (L6): Represents RPT software prototyping access in AUTOSAR.

> Coverage: 12/12 (100.0%)

## models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption

### models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HardwareConfiguration.py

- **HardwareConfiguration** (L9): Represents hardware configuration information in AUTOSAR models.

### models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/HeapUsage.py

- **HeapUsage** (L10): Abstract base class for representing heap usage in AUTOSAR models.
- **MeasuredHeapUsage** (L30): Represents measured heap usage in AUTOSAR.
- **RoughEstimateHeapUsage** (L47): Represents rough estimate of heap usage in AUTOSAR.
- **WorstCaseHeapUsage** (L64): Represents worst case heap usage in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/MemorySectionUsage.py

- **MemorySection** (L11): Represents a memory section in AUTOSAR models.
- **SectionNamePrefix** (L206): Represents a section name prefix in AUTOSAR memory section usage.

### models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/SoftwareContext.py

- **SoftwareContext** (L9): Represents software execution context information in AUTOSAR models.

### models/M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py

- **StackUsage** (L13): Abstract base class for representing stack usage in AUTOSAR models.
- **MeasuredStackUsage** (L130): Represents measured stack usage in AUTOSAR models.
- **RoughEstimateStackUsage** (L195): Represents rough estimate stack usage in AUTOSAR models.
- **WorstCaseStackUsage** (L236): Represents worst case stack usage in AUTOSAR models.

> Coverage: 12/12 (100.0%)

## models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation

### models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/SignalServiceTranslationControlEnum.py

- **SignalServiceTranslationControlEnum** (L4): Enumeration for signal service translation control types in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/SignalServiceTranslationElementProps.py

- **SignalServiceTranslationElementProps** (L4): Represents signal service translation element properties in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/SignalServiceTranslationEventProps.py

- **SignalServiceTranslationEventProps** (L4): Represents signal service translation event properties in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/SignalServiceTranslationProps.py

- **SignalServiceTranslationProps** (L5): Represents signal service translation properties in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/SignalServiceTranslation/SignalServiceTranslationPropsSet.py

- **SignalServiceTranslationPropsSet** (L5): Represents a set of signal service translation properties in AUTOSAR.

> Coverage: 5/5 (100.0%)

## models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate

### models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/Keyword.py

- **Keyword** (L14): Represents a keyword in AUTOSAR models for standardization and classification purposes.
- **KeywordSet** (L84): Represents a set of keywords in AUTOSAR models for standardization and classification purposes.

> Coverage: 2/2 (100.0%)

## models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/AbstractBlueprintStructure

### models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/AbstractBlueprintStructure/AtpBlueprint.py

- **AtpBlueprint** (L10): Abstract base class for AUTOSAR Template (ATP) blueprint elements.

> Coverage: 1/1 (100.0%)

## models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintDedicated

### models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintDedicated/PortPrototypeBlueprint.py

- **PortPrototypeBlueprintInitValue** (L23): Represents an initial value specification for a port prototype blueprint.
- **PortPrototypeBlueprint** (L82): Defines a blueprint for port prototypes in AUTOSAR standardization templates.

> Coverage: 2/2 (100.0%)

## models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintGenerator

### models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintGenerator/BlueprintGenerator.py

- **BlueprintGenerator** (L4): Represents a blueprint generator in AUTOSAR.

> Coverage: 1/1 (100.0%)

## models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintMapping

### models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/BlueprintMapping/BlueprintMappingSet.py

- **BlueprintMappingSet** (L5): Represents a set of blueprint mappings in AUTOSAR.

> Coverage: 1/1 (100.0%)

## models/M2/AUTOSARTemplates/CommonStructure/Timing

### models/M2/AUTOSARTemplates/CommonStructure/Timing/Traceable.py

- **Traceable** (L7): Abstract base class for traceable identifiable elements.

> Coverage: 1/1 (100.0%)

## models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingClock

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingClock/TDLETZoneClock.py

- **TDLETZoneClock** (L5): Represents a TDLET zone clock in AUTOSAR timing specifications.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingClock/TimingClock.py

- **TimingClock** (L4): Represents a timing clock in AUTOSAR timing specifications.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingClock/TimingClockSyncAccuracy.py

- **TimingClockSyncAccuracy** (L4): Represents timing clock synchronization accuracy in AUTOSAR.

> Coverage: 3/3 (100.0%)

## models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/ModeInBswInstanceRef.py

- **ModeInBswInstanceRef** (L4): Represents a reference to a mode in a BSW instance.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/ModeInSwcInstanceRef.py

- **ModeInSwcInstanceRef** (L4): Represents a reference to a mode in a SWC instance.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/TimingCondition.py

- **TimingCondition** (L5): Represents a timing condition in AUTOSAR timing specifications.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/TimingConditionFormula.py

- **TimingConditionFormula** (L4): Represents a timing condition formula in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/TimingExtensionResource.py

- **TimingExtensionResource** (L4): Represents a timing extension resource in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingCondition/TimingModeInstance.py

- **TimingModeInstance** (L5): Represents a timing mode instance in AUTOSAR.

> Coverage: 6/6 (100.0%)

## models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/AgeConstraint.py

- **AgeConstraint** (L17): Specifies the maximum allowed age of data in AUTOSAR timing specifications.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py

- **EventTriggeringConstraint** (L26): Abstract base class for event triggering constraints.
- **PeriodicEventTriggering** (L40): Specifies periodic event triggering requirements.
- **SporadicEventTriggering** (L67): Specifies sporadic event triggering requirements.
- **ArbitraryEventTriggering** (L94): Specifies arbitrary event triggering requirements.
- **BurstPatternEventTriggering** (L111): Specifies burst pattern event triggering requirements.
- **ConcretePatternEventTriggering** (L147): Specifies concrete pattern event triggering requirements.
- **ConfidenceInterval** (L164): Specifies a confidence interval for timing measurements.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionOrderConstraint.py

- **EOCExecutableEntityRefAbstract** (L22): Abstract base class for execution order constraint executable entity references.
- **EOCExecutableEntityRef** (L35): Concrete implementation of executable entity reference for execution order constraints.
- **ExecutionOrderConstraint** (L64): Execution order constraint defining the execution sequence of executable entities.
- **EOCEventRef** (L101): Represents an event reference in execution order constraints.
- **EOCExecutableEntityRefGroup** (L137): Represents a group of executable entity references in execution order constraints.
- **ExecutionOrderConstraintTypeEnum** (L173): Enumeration for execution order constraint types in AUTOSAR.
- **LetDataExchangeParadigmEnum** (L185): Enumeration for LET (Logical Execution Time) data exchange paradigms in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/ExecutionTimeConstraint.py

- **ExecutionTimeTypeEnum** (L20): Enumeration for execution time constraint types.
- **ExecutionTimeConstraint** (L37): Specifies execution time requirements for AUTOSAR entities.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/LatencyTimingConstraint.py

- **LatencyConstraintTypeEnum** (L19): Enumeration for latency constraint types.
- **LatencyTimingConstraint** (L36): Specifies latency requirements in AUTOSAR timing specifications.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/OffsetConstraint.py

- **OffsetTimingConstraint** (L16): Specifies timing offset requirements in AUTOSAR timing specifications.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationPointConstraint.py

- **SynchronizationPointConstraint** (L17): Specifies synchronization point requirements in AUTOSAR timing specifications.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py

- **SynchronizationTypeEnum** (L19): Enumeration for synchronization types.
- **EventOccurrenceKindEnum** (L36): Enumeration for event occurrence kinds.
- **SynchronizationTimingConstraint** (L53): Specifies synchronization timing requirements in AUTOSAR timing specifications.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/TimingConstraint.py

- **TimingConstraint** (L26): Abstract base class for all timing constraints in AUTOSAR.

### models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/TimingExtensions.py

- **TimingExtension** (L21): Abstract base class for timing extensions in AUTOSAR.
- **SwcTiming** (L63): Software component timing specification that defines timing constraints

> Coverage: 27/27 (100.0%)

## models/M2/AUTOSARTemplates/DiagnosticExtract

### models/M2/AUTOSARTemplates/DiagnosticExtract/DiagnosticCommonElement.py

- **DiagnosticCommonElement** (L7): Abstract base class for common diagnostic elements in the diagnostic

### models/M2/AUTOSARTemplates/DiagnosticExtract/DiagnosticContribution.py

- **DiagnosticServiceTable** (L21): Represents a diagnostic service table in AUTOSAR diagnostic extract.

> Coverage: 2/2 (100.0%)

## models/M2/AUTOSARTemplates/EcuResourceTemplate

### models/M2/AUTOSARTemplates/EcuResourceTemplate/HwAttributeValue.py

- **HwAttributeValue** (L13): Represents a hardware attribute value in AUTOSAR hardware descriptions.
- **HwAttributeLiteralDef** (L77): Represents a hardware attribute literal definition in AUTOSAR hardware descriptions.

### models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementCategory.py

- **HwType** (L25): Represents a hardware type in AUTOSAR hardware descriptions.
- **HwAttributeDef** (L42): Represents a hardware attribute definition in AUTOSAR hardware descriptions.
- **HwCategory** (L135): Represents a hardware category in AUTOSAR hardware descriptions.

### models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementConnector.py

- **HwElementConnector** (L12): Represents a connection between hardware elements in AUTOSAR hardware descriptions.

> Coverage: 6/6 (100.0%)

## models/M2/AUTOSARTemplates/GenericStructure

### models/M2/AUTOSARTemplates/GenericStructure/AbstractStructure.py

- **AtpInstanceRef** (L14): Abstract class for AUTOSAR Template Parameter (ATP) instance references.
- **AtpBlueprintable** (L97): Abstract base class for AUTOSAR Template (ATP) blueprintable elements.
- **AtpClassifier** (L120): Abstract base class for AUTOSAR Template (ATP) classifier elements.
- **AtpFeature** (L143): Abstract base class for AUTOSAR Template (ATP) feature elements.
- **AtpType** (L172): Abstract base class for AUTOSAR Template (ATP) type elements.
- **AtpPrototype** (L198): Abstract base class for AUTOSAR Template (ATP) prototype elements.
- **AtpStructureElement** (L227): Abstract base class for AUTOSAR Template (ATP) structure elements.
- **AtpBlueprintMapping** (L269): Abstract base class for AUTOSAR Template (ATP) blueprint mapping elements.

### models/M2/AUTOSARTemplates/GenericStructure/LifeCycles.py

- **LifeCyclePeriod** (L15): This meta class represents the ability to specify a point of time within a specified period, e.g. the starting
- **LifeCycleInfo** (L101): Represents life cycle information in AUTOSAR models.
- **LifeCycleInfoSet** (L262): Represents a set of life cycle information in AUTOSAR models.

> Coverage: 11/11 (100.0%)

## models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses

### models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ARPackage.py

- **ReferenceBase** (L82): Represents a reference base in AUTOSAR models. Reference bases define 
- **ARPackage** (L266): Represents an AUTOSAR package, which is a container for organizing 

### models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/AnyInstanceRef.py

- **AnyInstanceRef** (L11): Represents a generic instance reference in AUTOSAR models.

### models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ArObject.py

- **ARObject** (L10): Abstract base class for all AUTOSAR objects.

### models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ElementCollection.py

- **Collection** (L14): Represents a collection of elements in AUTOSAR models.

### models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/EngineeringObject.py

- **EngineeringObject** (L12): Abstract class for AUTOSAR engineering objects.
- **AutosarEngineeringObject** (L123): Represents an AUTOSAR engineering object.

### models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Enumerations.py

- **AutoCollectEnum** (L9): Enumeration for auto-collect settings in AUTOSAR collections.

### models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py

- **Referrable** (L17): Abstract class for elements that can be referenced by other elements in AUTOSAR models.
- **MultilanguageReferrable** (L76): Abstract class for referrable elements that support multilingual text.
- **CollectableElement** (L114): Abstract class for elements that can collect other referrable elements.
- **Identifiable** (L221): Abstract class for identifiable elements in AUTOSAR models.
- **PackageableElement** (L455): Abstract class for elements that can be packaged in AUTOSAR models.
- **ARElement** (L467): Abstract class for AUTOSAR elements.
- **Describable** (L479): Abstract class for elements that can be described in AUTOSAR models.

### models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py

- **ARType** (L12): Abstract base class for all AUTOSAR types.
- **ARNumerical** (L66): Base class for numerical AUTOSAR types.
- **ARFloat** (L165): Base class for floating-point AUTOSAR types.
- **Float** (L200): An instance of Float is an element from the set of real numbers.
- **TimeValue** (L211): This primitive type is taken for expressing time values. The numerical value is supposed to be interpreted
- **ARLiteral** (L224): Base class for literal AUTOSAR types.
- **AREnum** (L260): Base class for enumeration AUTOSAR types.
- **String** (L308): Represents a string AUTOSAR type.
- **ReferrableSubtypesEnum** (L318): Represents an enum for referrable subtypes in AUTOSAR models.
- **ARPositiveInteger** (L327): Base class for positive integer AUTOSAR types.
- **ARBoolean** (L354): Base class for boolean AUTOSAR types.
- **NameToken** (L425): This is an identifier as used in xml, e.g. xml-names. Typical usages are, for example, the names of type
- **PositiveInteger** (L442): \n
- **PositiveUnlimitedInteger** (L457): This is a positive unlimited integer which can be denoted in decimal, binary, octal and hexadecimal.
- **Integer** (L468): An instance of Integer is an element in the set of integer numbers ( ..., -2, -1, 0, 1, 2, ...).
- **UnlimitedInteger** (L484): An instance of UnlimitedInteger is an element in the set of integer numbers ( ..., -2, -1, 0, 1, 2, ...).
- **Boolean** (L500): A Boolean value denotes a logical condition that is either 'true' or 'false'. It can be one of "0", "1", "true",
- **Identifier** (L514): An Identifier is a string with a number of constraints on its appearance, satisfying the requirements typical
- **CIdentifier** (L531): This datatype represents a string, that follows the rules of C-identifiers.
- **RevisionLabelString** (L591): This primitive represents an internal AUTOSAR revision label which identifies an engineering object. It
- **Limit** (L605): Represents a limit in AUTOSAR models.
- **RefType** (L662): Represents a reference type in AUTOSAR models.
- **TRefType** (L759): Represents a typed reference type in AUTOSAR models.
- **DiagRequirementIdString** (L769): This string denotes an Identifier for a requirement.
- **ArgumentDirectionEnum** (L782): Enumeration for argument direction in AUTOSAR models.
- **Ip4AddressString** (L799): This is used to specify an IP4 address. Notation: 255.255.255.255
- **Ip6AddressString** (L812): This is used to specify an IP6 address. Notation: FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
- **MacAddressString** (L827): This primitive specifies a Mac Address. Notation: FF:FF:FF:FF:FF:FF
- **CategoryString** (L841): This represents the pattern applicable to categories.
- **ByteOrderEnum** (L856): Enumeration for byte order in AUTOSAR models.
- **DateTime** (L865): A datatype representing a timestamp. The smallest granularity is 1 second.
- **VerbatimString** (L885): Represents a verbatim string in AUTOSAR models.
- **RegularExpression** (L895): Represents a regular expression in AUTOSAR models.

> Coverage: 48/48 (100.0%)

## models/M2/AUTOSARTemplates/GenericStructure/RolesAndRights

### models/M2/AUTOSARTemplates/GenericStructure/RolesAndRights/AtpDefinition.py

- **AtpDefinition** (L10): Abstract base class for AUTOSAR Template (ATP) definition elements.

> Coverage: 1/1 (100.0%)

## models/M2/AUTOSARTemplates/SWComponentTemplate

### models/M2/AUTOSARTemplates/SWComponentTemplate/Communication.py

- **HandleInvalidEnum** (L21): Strategies of handling the reception of invalidValue.
- **PPortComSpec** (L40): Communication attributes of a provided PortPrototype. This class will contain attributes
- **RPortComSpec** (L53): Communication attributes of a required PortPrototype. This class will contain attributes
- **CompositeNetworkRepresentation** (L67): This meta-class is used to define the network representation of leaf elements
- **TransmissionAcknowledgementRequest** (L126): Requests transmission acknowledgement that data has been sent successfully.
- **SenderComSpec** (L162): Communication attributes for a sender port (PPortPrototype typed by SenderReceiverInterface).
- **QueuedSenderComSpec** (L315): Communication attributes specific to distribution of events (PPortPrototype,
- **NonqueuedSenderComSpec** (L325): Communication attributes for non-queued sender/receiver communication (sender side).
- **ClientComSpec** (L361): Client-specific communication attributes (RPortPrototype typed by ClientServerInterface).
- **ModeSwitchReceiverComSpec** (L395): Communication attributes of RPortPrototypes with respect to mode communication.
- **NvRequireComSpec** (L477): Communication attributes of RPortPrototypes with respect to Nv data communication
- **ParameterRequireComSpec** (L538): "Communication" specification that applies to parameters on the required side
- **ReceiverComSpec** (L597): Receiver-specific communication attributes (RPortPrototype typed by SenderReceiverInterface).
- **ModeSwitchedAckRequest** (L818): Requests acknowledgements that a mode switch has been proceeded successfully.
- **ModeSwitchSenderComSpec** (L853): Communication attributes of PPortPrototypes with respect to mode communication.
- **ParameterProvideComSpec** (L959): "Communication" specification that applies to parameters on the provided side
- **TransformationComSpecProps** (L969): TransformationComSpecProps holds all the attributes for transformers that are
- **EndToEndTransformationComSpecProps** (L982): The class EndToEndTransformationComSpecProps specifies port specific configuration
- **UserDefinedTransformationComSpecProps** (L1430): The UserDefinedTransformationComSpecProps is used to specify port specific
- **ServerComSpec** (L1440): Communication attributes for a server port (PPortPrototype and ClientServerInterface).
- **NvProvideComSpec** (L1526): Communication attributes of PPortPrototypes with respect to Nv data communication
- **NonqueuedReceiverComSpec** (L1612): Communication attributes specific to non-queued receiving.
- **QueuedReceiverComSpec** (L1825): Communication attributes specific to queued receiving.
- **HandleOutOfRangeEnum** (L1859): Enumeration for handle out of range behavior.
- **HandleOutOfRangeStatusEnum** (L1878): Enumeration for handle out of range status.
- **HandleTimeoutEnum** (L1893): Enumeration for handle timeout behavior.
- **TransmissionModeDefinitionEnum** (L1910): Enumeration for transmission mode definition.

### models/M2/AUTOSARTemplates/SWComponentTemplate/EndToEndProtection.py

- **EndToEndDescription** (L15): End-to-end protection profile description defining CRC, counter, and
- **EndToEndProtectionVariablePrototype** (L257): Associates a VariableDataPrototype with sender and receiver roles
- **EndToEndProtectionISignalIPdu** (L290): Defines to which ISignalIPdu-ISignalGroup pair an EndToEndProtection
- **EndToEndProtection** (L370): This meta-class represents the ability to describe a particular end to
- **EndToEndProtectionSet** (L453): This represents a container for the collection of EndToEndProtection

### models/M2/AUTOSARTemplates/SWComponentTemplate/RPTScenario.py

- **IdentCaption** (L11): Abstract base class for identification captions used in access points.
- **ModeAccessPointIdent** (L23): Identification of a mode access point used to reference a specific

### models/M2/AUTOSARTemplates/SWComponentTemplate/SoftwareComponentDocumentation.py

- **SwComponentDocumentation** (L9): Documentation for a software component including chapters, calibration

### models/M2/AUTOSARTemplates/SWComponentTemplate/SwComponentType.py

- **SwComponentType** (L15): Abstract base class for all software component types in AUTOSAR.

### models/M2/AUTOSARTemplates/SWComponentTemplate/SwcImplementation.py

- **SwcImplementation** (L10): Implementation of an atomic software component defining the behavior

> Coverage: 37/37 (100.0%)

## models/M2/AUTOSARTemplates/SWComponentTemplate/Components

### models/M2/AUTOSARTemplates/SWComponentTemplate/Components/InstanceRefs.py

- **ModeGroupInAtomicSwcInstanceRef** (L12): Abstract base class for mode group instance references within an atomic
- **PModeGroupInAtomicSwcInstanceRef** (L51): Instance reference to a mode group in an atomic software component
- **RModeGroupInAtomicSWCInstanceRef** (L77): Instance reference to a mode group in an atomic software component
- **RModeInAtomicSwcInstanceRef** (L104): Instance reference to a mode declaration in an atomic software component
- **VariableInAtomicSwcInstanceRef** (L146): Abstract base class for variable instance references within an atomic
- **RVariableInAtomicSwcInstanceRef** (L162): Instance reference to a variable in an atomic software component
- **InnerPortGroupInCompositionInstanceRef** (L188): Instance reference to a port group within a composition software

> Coverage: 7/7 (100.0%)

## models/M2/AUTOSARTemplates/SWComponentTemplate/Composition

### models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/InstanceRefs.py

- **PortInCompositionTypeInstanceRef** (L11): Abstract base class for port instance references within a composition
- **PPortInCompositionInstanceRef** (L49): Instance reference to a PPortPrototype within a composition software
- **RPortInCompositionInstanceRef** (L76): Instance reference to an RPortPrototype within a composition software
- **OperationInAtomicSwcInstanceRef** (L102): Abstract base class for operation instance references within an atomic
- **POperationInAtomicSwcInstanceRef** (L139): Instance reference to a provided operation in an atomic software
- **ROperationInAtomicSwcInstanceRef** (L166): Instance reference to a required operation in an atomic software

> Coverage: 6/6 (100.0%)

## models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype

### models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/DataPrototypes.py

- **DataPrototype** (L16): Abstract base class for all AUTOSAR data prototypes within software
- **AutosarDataPrototype** (L52): Abstract base class for AUTOSAR data prototypes that have a type
- **VariableDataPrototype** (L88): A data prototype that represents a variable data element with an
- **ApplicationCompositeElementDataPrototype** (L121): Abstract base class for data prototypes that represent elements within
- **ApplicationArrayElement** (L143): An element of an application array data type defining the array
- **ApplicationRecordElement** (L249): An element of an application record data type defining a field within
- **ParameterDataPrototype** (L284): A data prototype that represents a parameter data element with an

### models/M2/AUTOSARTemplates/SWComponentTemplate/Datatype/Datatypes.py

- **AutosarDataType** (L19): Abstract base class for all AUTOSAR data types within the SW component
- **ApplicationDataType** (L41): Abstract base class for all application data types.
- **ApplicationPrimitiveDataType** (L53): An application data type that represents a primitive (non-composite)
- **ApplicationCompositeDataType** (L63): Abstract base class for application composite data types such as
- **ApplicationArrayDataType** (L76): An application data type representing an array with elements of the
- **ApplicationRecordDataType** (L104): An application data type representing a record with fields of possibly
- **DataTypeMap** (L126): Maps an application data type to an implementation data type.
- **DataTypeMappingSet** (L151): A set of data type maps and mode request type maps that define

> Coverage: 15/15 (100.0%)

## models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface

### models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/InstanceRefs.py

- **ApplicationCompositeElementInPortInterfaceInstanceRef** (L10): Instance reference to an application composite element within the

> Coverage: 1/1 (100.0%)

## models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior

### models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/AccessCount.py

- **AbstractAccessPoint** (L11): Abstract class indicating an access point from an ExecutableEntity.

### models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/AutosarVariableRef.py

- **AutosarVariableRef** (L11): A reference to a variable used in the context of AUTOSAR software component

### models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/DataElements.py

- **ParameterAccess** (L15): A ParameterAccess represents the access to a parameter data prototype
- **VariableAccess** (L72): A VariableAccess represents the access to a variable data prototype

### models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/IncludedDataTypes.py

- **IncludedDataTypeSet** (L10): A set of data type references that are included in the context of

### models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/InstanceRefsUsage.py

- **ArVariableInImplementationDataInstanceRef** (L12): A reference to an AUTOSAR variable in the context of an implementation
- **VariableInAtomicSWCTypeInstanceRef** (L114): A reference to a variable data prototype in the context of an atomic
- **ParameterInAtomicSWCTypeInstanceRef** (L240): A reference to a parameter data prototype in the context of an atomic
- **AutosarParameterRef** (L366): A reference to an AUTOSAR parameter.

### models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ModeDeclarationGroup.py

- **ModeAccessPoint** (L14): A mode access point used by a runnable entity to read the current mode
- **ModeSwitchPoint** (L70): A mode switch point used by a runnable entity to switch the mode
- **IncludedModeDeclarationGroupSet** (L104): A set of mode declaration group references included in the scope

### models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/PerInstanceMemory.py

- **PerInstanceMemory** (L12): A per-instance memory is a memory block that is allocated separately

### models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/PortAPIOptions.py

- **PortDefinedArgumentValue** (L11): A value defined for a port argument in the context of port API options.
- **PortAPIOption** (L66): Port API options that define the API configuration for a specific port

### models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/RTEEvents.py

- **RTEEvent** (L16): Abstract base class for all RTE-related events.
- **AsynchronousServerCallReturnsEvent** (L74): This event is raised when an asynchronous server call is finished.
- **DataSendCompletedEvent** (L107): This event is raised when the referenced explicit data element has been
- **DataWriteCompletedEvent** (L141): This event is raised when an implicit write access was successful or
- **DataReceivedEvent** (L175): This event is raised when the referenced data element is received.
- **SwcModeSwitchEvent** (L208): This event is raised when the specified mode change occurs.
- **DataReceiveErrorEvent** (L264): This event is raised when the Com layer detects and notifies an error
- **OperationInvokedEvent** (L298): This event is raised when the ClientServerOperation referenced in
- **InitEvent** (L333): This RTEEvent is used for initialization purposes, i.e. for starting and
- **TimingEvent** (L345): This event is used to start RunnableEntities that shall be executed
- **InternalTriggerOccurredEvent** (L415): This event is raised when the referenced InternalTriggeringPoint has
- **BackgroundEvent** (L450): This event is used to start RunnableEntities that are supposed to be
- **ModeSwitchedAckEvent** (L460): This event is raised when the referenced ModeSwitchPoint has been

### models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServerCall.py

- **ServerCallPoint** (L11): If a RunnableEntity owns a ServerCallPoint it is entitled to invoke a

### models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServiceMapping.py

- **RoleBasedPortAssignment** (L16): A role-based port assignment that links a port prototype to a specific
- **SwcServiceDependency** (L73): A service dependency for an atomic software component that defines the

### models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/Trigger.py

- **InternalTriggeringPoint** (L13): An internal triggering point that can be referenced by an
- **ExternalTriggeringPointIdent** (L48): Identification of an external triggering point.
- **ExternalTriggeringPoint** (L57): An external triggering point that references a trigger defined in a

> Coverage: 34/34 (100.0%)

## models/M2/AUTOSARTemplates/SystemTemplate

### models/M2/AUTOSARTemplates/SystemTemplate/DataMapping.py

- **DataMapping** (L14): Abstract base class for data mapping elements that define relationships between 
- **SenderReceiverToSignalMapping** (L37): Maps data elements from sender/receiver interfaces to system signals.
- **SenderRecCompositeTypeMapping** (L89): Abstract base class for composite type mappings between sender/receiver
- **SenderRecRecordElementMapping** (L102): Defines mapping for individual elements within a record structure,
- **SenderRecRecordTypeMapping** (L168): Maps record data types between sender/receiver interfaces and system signals,
- **IndexedArrayElement** (L188): Represents an element in an array with a specific index, connecting
- **SenderRecArrayElementMapping** (L226): Maps individual elements of an array data type between sender/receiver
- **SenderRecArrayTypeMapping** (L264): Maps array data types between sender/receiver interfaces and system signals,
- **SenderReceiverToSignalGroupMapping** (L302): Maps sender/receiver interface data to system signal groups, enabling

### models/M2/AUTOSARTemplates/SystemTemplate/DiagnosticConnection.py

- **DiagnosticConnection** (L8): Represents a diagnostic connection in the AUTOSAR system, defining the relationship

### models/M2/AUTOSARTemplates/SystemTemplate/DoIp.py

- **AbstractDoIpLogicAddressProps** (L10): Abstract base class for DoIP (Diagnostics over IP) logic address properties.
- **DoIpLogicTargetAddressProps** (L22): Defines properties for DoIP (Diagnostics over IP) logic target addresses,
- **DoIpLogicTesterAddressProps** (L31): Defines properties for DoIP (Diagnostics over IP) logic tester addresses,

### models/M2/AUTOSARTemplates/SystemTemplate/ECUResourceMapping.py

- **ECUMapping** (L4): Represents an ECU mapping that defines the relationship between AUTOSAR software components

### models/M2/AUTOSARTemplates/SystemTemplate/InstanceRefs.py

- **VariableDataPrototypeInSystemInstanceRef** (L9): Instance reference to a VariableDataPrototype in the context of a
- **ComponentInSystemInstanceRef** (L60): Instance reference to a component in the context of a system model.

### models/M2/AUTOSARTemplates/SystemTemplate/NetworkManagement.py

- **NmClusterCoupling** (L12): Abstract base class for network management cluster coupling,
- **CanNmClusterCoupling** (L24): Defines coupling properties for CAN network management clusters,
- **FlexrayNmClusterCoupling** (L58): Defines coupling properties for FlexRay network management clusters,
- **NmNode** (L85): Abstract base class for network management nodes, defining
- **CanNmNode** (L162): Represents a CAN network management node in the system,
- **FlexrayNmNode** (L219): Represents a FlexRay network management node in the system,
- **J1939NmNode** (L228): Represents a J1939 network management node in the system,
- **UdpNmNode** (L237): Represents a UDP network management node in the system,
- **BusspecificNmEcu** (L265): Abstract base class for bus-specific network management ECU
- **CanNmEcu** (L276): Defines CAN-specific network management ECU properties,
- **FlexrayNmEcu** (L284): Defines FlexRay-specific network management ECU properties,
- **J1939NmEcu** (L292): Defines J1939-specific network management ECU properties,
- **UdpNmEcu** (L300): Defines UDP-specific network management ECU properties,
- **NmEcu** (L320): Represents a network management ECU in the system,
- **NmConfig** (L447): Represents network management configuration in the system,
- **NmCluster** (L497): Abstract base class for network management clusters,
- **CanNmCluster** (L598): Represents a CAN network management cluster in the system,
- **FlexrayNmCluster** (L736): Represents a FlexRay network management cluster in the system,
- **J1939NmCluster** (L745): Represents a J1939 network management cluster in the system,
- **UdpNmClusterCoupling** (L754): Defines coupling properties for UDP network management clusters,
- **UdpNmCluster** (L783): Represents a UDP network management cluster in the system,

### models/M2/AUTOSARTemplates/SystemTemplate/RteEventToOsTaskMapping.py

- **AppOsTaskProxyToEcuTaskProxyMapping** (L8): Represents a mapping between application OS task proxies and ECU task proxies

### models/M2/AUTOSARTemplates/SystemTemplate/SWmapping.py

- **SwcToImplMapping** (L10): Represents a mapping between software components and their implementations,
- **ApplicationPartitionToEcuPartitionMapping** (L39): Represents a mapping between application partitions and ECU partitions,

### models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py

- **CryptoServiceMapping** (L10): Abstract base class for crypto service mappings, defining
- **SecOcCryptoServiceMapping** (L23): Represents a Secure Onboard Communication (SecOC) crypto service mapping,
- **TlsCryptoServiceMapping** (L61): Represents a TLS (Transport Layer Security) crypto service mapping,

### models/M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py

- **TpConfig** (L13): Abstract base class for transport protocol configurations,
- **CanTpAddress** (L35): Represents a CAN transport protocol address in the system,
- **CanTpChannel** (L63): Represents a CAN transport protocol channel in the system,
- **TpConnectionIdent** (L90): Represents a transport protocol connection identifier,
- **TpConnection** (L99): Abstract base class for transport protocol connections,
- **CanTpConnection** (L121): Represents a CAN transport protocol connection in the system,
- **CanTpEcu** (L275): Represents a CAN transport protocol ECU configuration,
- **CanTpNode** (L303): Represents a CAN transport protocol node in the system,
- **CanTpConfig** (L369): Represents CAN transport protocol configuration in the system,
- **DoIpLogicAddress** (L430): Represents a DoIP (Diagnostics over IP) logic address in the system,
- **DoIpTpConnection** (L458): Represents a DoIP transport protocol connection in the system,
- **DoIpTpConfig** (L496): Represents DoIP transport protocol configuration in the system,
- **TpAddress** (L526): Represents a generic transport protocol address in the system,
- **LinTpConnection** (L544): Represents a LIN transport protocol connection in the system,
- **LinTpNode** (L635): Represents a LIN transport protocol node in the system,
- **LinTpConfig** (L700): Represents LIN transport protocol configuration in the system,

> Coverage: 59/59 (100.0%)

## models/M2/AUTOSARTemplates/SystemTemplate/Fibex

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py

- **FrameMapping** (L9): A PduToFrameMapping defines the composition of Pdus in each frame.
- **ISignalMapping** (L42): Arranges signals transferred by the gateway from one channel to another
- **DefaultValueElement** (L76): The default value consists of a number of elements. Each element is one
- **PduMappingDefaultValue** (L104): Default value which will be distributed if no I-Pdu has been received
- **TargetIPduRef** (L123): Target destination of the referencing mapping.
- **IPduMapping** (L150): An ISignalToIPduMapping describes the mapping of ISignals to ISignalIPdus
- **Gateway** (L198): A gateway is an ECU that is connected to two or more clusters and

> Coverage: 7/7 (100.0%)

## models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanCommunication.py

- **RxIdentifierRange** (L8): Defines a range of CAN identifiers used for receive filtering in CAN communication.
- **CanFrame** (L34): Represents a CAN frame in the AUTOSAR system, extending the generic Frame class
- **CanFrameTriggering** (L43): Defines the triggering mechanism for CAN frames, specifying how and when

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Can/CanTopology.py

- **CanControllerFdConfiguration** (L12): Defines CAN FD (Flexible Data Rate) configuration parameters for CAN controllers,
- **CanControllerFdConfigurationRequirements** (L86): Specifies the requirements for CAN FD configuration parameters, defining
- **CanControllerXlConfiguration** (L187): Defines CAN XL (eXtended Length) configuration parameters for CAN controllers,
- **CanControllerXlConfigurationRequirements** (L324): Specifies the requirements for CAN XL configuration parameters, defining
- **AbstractCanCommunicationControllerAttributes** (L425): Abstract base class for CAN communication controller attributes,
- **CanControllerConfigurationRequirements** (L471): Defines configuration requirements for CAN controllers, specifying
- **AbstractCanCommunicationController** (L530): Abstract base class for CAN communication controllers, defining
- **CanCommunicationController** (L552): Represents a CAN communication controller in the system, implementing
- **AbstractCanCommunicationConnector** (L562): Abstract base class for CAN communication connectors, providing
- **CanCommunicationConnector** (L575): Represents a CAN communication connector that links CAN controllers

> Coverage: 13/13 (100.0%)

## models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetCommunication.py

- **SocketConnection** (L10): Represents a socket connection in the Ethernet communication system,
- **SocketConnectionIpduIdentifier** (L117): Identifies an IPDU (Interaction Protocol Data Unit) within a socket connection,
- **SocketConnectionBundle** (L184): Groups multiple socket connections into a bundle for managing related
- **SoAdRoutingGroup** (L250): Defines a routing group for the Socket Adaptor (SoAd) module,

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetFrame.py

- **AbstractEthernetFrame** (L9): Abstract base class for Ethernet frames in the AUTOSAR system,
- **GenericEthernetFrame** (L23): Represents a generic Ethernet frame in the AUTOSAR system,

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py

- **MacMulticastGroup** (L9): Represents a MAC multicast group used in Ethernet communication,
- **EthernetCluster** (L29): Defines an Ethernet communication cluster in the system topology,
- **CouplingPortStructuralElement** (L78): Abstract base class for coupling port structural elements in Ethernet
- **CouplingPortFifo** (L91): Defines a FIFO (First In, First Out) buffer for coupling ports in
- **CouplingPortScheduler** (L138): Defines a scheduler for coupling ports in Ethernet switches,
- **EthernetPriorityRegeneration** (L167): Defines priority regeneration rules for Ethernet traffic,
- **CouplingPortDetails** (L196): Contains detailed configuration information for coupling ports
- **VlanMembership** (L298): Defines VLAN membership properties for network interfaces,
- **CouplingPort** (L345): Defines a coupling port in an Ethernet switch or bridge,
- **EthernetCommunicationController** (L482): Represents an Ethernet communication controller in the system,
- **EthernetCommunicationConnector** (L560): Defines an Ethernet communication connector that links Ethernet
- **RequestResponseDelay** (L620): Defines the delay constraints for request-response communication
- **InitialSdDelayConfig** (L649): Configures the initial delay parameters for Service Discovery (SD)
- **SdClientConfig** (L696): Configures Service Discovery (SD) client properties, including

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/NetworkEndpoint.py

- **NetworkEndpointAddress** (L10): Abstract base class for network endpoint addresses, defining the
- **Ipv4Configuration** (L22): Defines IPv4 network configuration properties for a network endpoint,
- **Ipv6Configuration** (L96): Defines IPv6 network configuration properties for a network endpoint,
- **DoIpEntity** (L178): Defines properties for a DoIP (Diagnostics over IP) entity,
- **TimeSyncClientConfiguration** (L197): Configures time synchronization client properties, defining
- **TimeSyncServerConfiguration** (L226): Configures time synchronization server properties, specifying
- **TimeSynchronization** (L273): Defines time synchronization configuration for network entities,
- **InfrastructureServices** (L302): Defines infrastructure services available at a network endpoint,
- **NetworkEndpoint** (L328): Represents a network endpoint in the AUTOSAR system, defining

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py

- **TransportProtocolConfiguration** (L13): Abstract base class for transport protocol configurations,
- **GenericTp** (L26): Defines generic transport protocol configuration properties,
- **TcpUdpConfig** (L53): Abstract base class for TCP and UDP transport protocol configurations,
- **TpPort** (L65): Defines properties for a transport protocol port, including
- **UdpTp** (L92): Defines UDP (User Datagram Protocol) transport protocol configuration,
- **TcpTp** (L111): Defines TCP (Transmission Control Protocol) transport protocol configuration,
- **AbstractServiceInstance** (L185): Abstract base class for service instances, defining common properties
- **ConsumedEventGroup** (L234): Defines a consumed event group for service-oriented communication,
- **ConsumedServiceInstance** (L326): Represents a consumed service instance in the AUTOSAR service-oriented
- **InitialSdDelayConfig** (L464): Configures initial delay parameters for Service Discovery (SD)
- **SdServerConfig** (L511): Configures Service Discovery (SD) server properties, specifying
- **EventHandler** (L585): Defines an event handler for service-oriented communication,
- **ProvidedServiceInstance** (L641): Represents a provided service instance in the AUTOSAR service-oriented
- **ApplicationEndpoint** (L699): Defines an application endpoint for service-oriented communication,
- **SocketAddress** (L771): Defines a socket address for network communication, specifying
- **SoAdConfig** (L886): Defines Socket Adaptor (SoAd) configuration, specifying socket

> Coverage: 45/45 (100.0%)

## models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayCommunication.py

- **FlexrayFrame** (L8): Represents a FlexRay frame in the AUTOSAR system, extending the generic
- **FlexrayAbsolutelyScheduledTiming** (L19): Defines absolutely scheduled timing properties for FlexRay communication,
- **FlexrayFrameTriggering** (L48): Defines the triggering mechanism for FlexRay frames, specifying how and when

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Flexray/FlexrayTopology.py

- **FlexrayCommunicationController** (L8): Represents a FlexRay communication controller in the system,
- **FlexrayCommunicationConnector** (L308): Defines a FlexRay communication connector that links FlexRay controllers
- **FlexrayCluster** (L346): Defines a FlexRay communication cluster in the system topology,

> Coverage: 6/6 (100.0%)

## models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinCommunication.py

- **LinFrame** (L10): Abstract base class for LIN frames, extending the generic Frame class
- **LinUnconditionalFrame** (L22): Represents an unconditional LIN frame in the AUTOSAR system,
- **LinFrameTriggering** (L31): Defines the triggering mechanism for LIN frames, specifying how and when
- **ResumePosition** (L59): Enumeration defining possible resume positions for LIN schedule tables,
- **ScheduleTableEntry** (L73): Abstract base class for schedule table entries, defining common
- **ApplicationEntry** (L114): Defines an application entry in a LIN schedule table,
- **FreeFormatEntry** (L133): Defines a free format entry in a LIN schedule table,
- **LinConfigurationEntry** (L145): Abstract base class for LIN configuration entries in schedule tables,
- **LinScheduleTable** (L158): Represents a LIN schedule table defining the timing and sequence

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Lin/LinTopology.py

- **LinCommunicationController** (L7): Represents a LIN communication controller in the system,
- **LinMaster** (L29): Defines a LIN master node in the network topology, specifying
- **LinCommunicationConnector** (L66): Defines a LIN communication connector that links LIN controllers

> Coverage: 12/12 (100.0%)

## models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py

- **FibexElement** (L12): Abstract base class for FIBEX (FIBer EXchange) elements in the
- **PduToFrameMapping** (L26): Defines the mapping between Protocol Data Units (PDUs) and frames,
- **Frame** (L69): Abstract base class for communication frames in the AUTOSAR system,
- **ContainedIPduProps** (L102): Defines properties for contained Interaction Protocol Data Units (IPDUs),
- **ISignalGroup** (L169): Defines a group of interaction signals in the communication system,
- **ISignalIPduGroup** (L213): Defines a group of Interaction Protocol Data Units (IPDUs) based on interaction signals,
- **Pdu** (L264): Abstract base class for Protocol Data Units (PDUs) in the communication system,
- **IPdu** (L294): Abstract base class for Interaction Protocol Data Units (IPDUs),
- **SecureCommunicationProps** (L317): Defines properties for secure communication, including authentication
- **SecuredIPdu** (L454): Represents a secured Interaction Protocol Data Unit (IPDU) with
- **ISignalToIPduMapping** (L528): Defines the mapping between interaction signals and Interaction Protocol Data Units (IPDUs),
- **NmPdu** (L587): Represents a Network Management Protocol Data Unit (PDU) used for
- **NPdu** (L636): Represents a Network Protocol Data Unit (PDU) used for network-level
- **DcmIPdu** (L645): Represents a Diagnostic Communication Management Interaction Protocol Data Unit (IPDU)
- **IPduTiming** (L663): Defines timing properties for Interaction Protocol Data Units (IPDUs),
- **ISignalIPdu** (L690): Represents an Interaction Protocol Data Unit (IPDU) based on interaction signals,
- **ISignal** (L728): Represents an interaction signal in the communication system,
- **PduTriggering** (L819): Defines the triggering mechanism for Protocol Data Units (PDUs),
- **FrameTriggering** (L871): Abstract base class for frame triggering mechanisms, defining
- **SystemSignal** (L909): Represents a system signal in the AUTOSAR system, defining
- **SystemSignalGroup** (L936): Represents a group of system signals, defining relationships
- **ISignalTriggering** (L963): Defines triggering properties for interaction signals, specifying
- **SegmentPosition** (L998): Defines the position of a segment within a communication element,
- **MultiplexedPart** (L1036): Abstract base class for multiplexed communication parts, defining
- **StaticPart** (L1059): Defines a static part of multiplexed communication, specifying
- **DynamicPartAlternative** (L1079): Defines an alternative for dynamic parts in multiplexed communication,
- **DynamicPart** (L1117): Defines a dynamic part of multiplexed communication, specifying
- **MultiplexedIPdu** (L1137): Represents a multiplexed Interaction Protocol Data Unit (IPDU)
- **GeneralPurposePdu** (L1211): Represents a general-purpose Protocol Data Unit (PDU) for flexible
- **GeneralPurposeIPdu** (L1220): Represents a general-purpose Interaction Protocol Data Unit (IPDU) for flexible
- **SecureCommunicationPropsSet** (L1229): Represents a set of secure communication properties that can be grouped
- **UserDefinedPdu** (L1240): Represents a user-defined Protocol Data Unit (PDU) that allows for custom
- **UserDefinedIPdu** (L1249): Represents a user-defined Interaction Protocol Data Unit (IPDU) that allows for custom
- **SecureCommunicationAuthenticationProps** (L1258): Defines authentication properties for secure communication,
- **SecureCommunicationFreshnessProps** (L1305): Defines freshness properties for secure communication,

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreTopology.py

- **CommunicationCycle** (L17): Abstract base class for communication cycles, defining common
- **CycleCounter** (L30): Defines a counter for communication cycles, specifying the
- **CycleRepetitionType** (L49): Enumeration defining types of cycle repetitions in communication
- **CycleRepetition** (L59): Defines repetition properties for communication cycles,
- **PhysicalChannel** (L88): Abstract base class for physical communication channels,
- **AbstractCanPhysicalChannel** (L162): Abstract base class for CAN physical channels, defining
- **CanPhysicalChannel** (L175): Represents a CAN physical channel in the communication system,
- **LinPhysicalChannel** (L185): Represents a LIN physical channel in the communication system,
- **VlanConfig** (L216): Defines Virtual LAN (VLAN) configuration properties,
- **EthernetPhysicalChannel** (L236): Represents an Ethernet physical channel in the communication system,
- **FlexrayChannelName** (L277): Enumeration defining names for FlexRay channels,
- **FlexrayPhysicalChannel** (L293): Represents a FlexRay physical channel in the communication system,
- **CommunicationCluster** (L313): Abstract base class for communication clusters, defining
- **CanClusterBusOffRecovery** (L393): Defines bus off recovery properties for CAN clusters,
- **AbstractCanCluster** (L449): Abstract base class for CAN clusters, extending communication
- **CanCluster** (L495): Represents a CAN cluster in the communication system,
- **LinCluster** (L505): Represents a LIN cluster in the communication system,
- **CommunicationController** (L515): Abstract base class for communication controllers,
- **PncGatewayTypeEnum** (L537): Enumeration defining types of PNC (Partial Network Cluster)
- **CommunicationDirectionType** (L555): Enumeration defining communication direction types,
- **CommConnectorPort** (L570): Abstract base class for communication connector ports,
- **FramePort** (L593): Represents a frame port for communication connectors,
- **IPduSignalProcessingEnum** (L602): Enumeration defining types of IPDU signal processing,
- **IPduPort** (L611): Represents an IPDU port for communication connectors,
- **ISignalPort** (L667): Represents an interaction signal port for communication connectors,
- **CommunicationConnector** (L723): Abstract base class for communication connectors,

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/EcuInstance.py

- **EcuInstance** (L10): ECUInstances are used to define the ECUs used in the topology.

### models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/Timing.py

- **ModeDrivenTransmissionModeCondition** (L7): The condition defined by this class evaluates to true if one of the
- **TransmissionModeCondition** (L25): Possibility to attach a condition to each signal within an I-PDU.
- **TimeRangeType** (L53): The timeRange can be specified with the value attribute. Optionally a
- **CyclicTiming** (L80): Specification of a cyclic sending behavior.
- **EventControlledTiming** (L106): Specification of an event-driven sending behavior. The PDU is sent
- **TransmissionModeTiming** (L133): Defines the timing behavior for a transmission mode. If the COM
- **TransmissionModeDeclaration** (L160): Defines two different TRANSMISSION MODES (True and False) for each

> Coverage: 69/69 (100.0%)

## models/M2/MSR/AsamHdo

### models/M2/MSR/AsamHdo/AdminData.py

- **Modification** (L8): Represents a modification made to a document.
- **DocRevision** (L37): Represents a single revision of a document with metadata.
- **AdminData** (L111): Container for administrative data including document revisions and language settings.

### models/M2/MSR/AsamHdo/BaseTypes.py

- **BaseTypeDefinition** (L6): Abstract base class for base type definitions.
- **BaseTypeDirectDefinition** (L18): Direct definition of a base type with encoding, size, and memory alignment specifications.
- **BaseType** (L69): Abstract base class for base types.
- **SwBaseType** (L89): Software base type representing primitive data types in software.

### models/M2/MSR/AsamHdo/ComputationMethod.py

- **CompuContent** (L12): Abstract base class for computation content.
- **CompuConst** (L24): This meta-class represents the fact that the value of a computation method scale is constant.
- **Compu** (L42): Base class for computation methods.
- **CompuConstContent** (L68): This meta-class represents the fact that the constant value of the computation method can be numerical or textual.
- **CompuConstTextContent** (L82): This meta-class represents the textual content of a scale.
- **CompuConstNumericContent** (L100): This meta-class represents the numeric content of a scale.
- **CompuConstFormulaContent** (L117): This meta-class represents the formula content of a scale.
- **CompuScaleContents** (L137): Abstract base class for computation scale contents.
- **CompuScaleConstantContents** (L149): Represents constant contents of a computation scale.
- **CompuRationalCoeffs** (L166): This meta-class represents the ability to express a rational function by specifying the coefficients of nominator and...
- **CompuScaleRationalFormula** (L192): This meta-class represents the fact that the computation in this scale is represented as rational term.
- **CompuNominatorDenominator** (L209): This class represents the ability to express a polynomial either as Nominator or as Denominator.
- **CompuScale** (L227): Represents a single scale in a computation method with limits and content.
- **CompuScales** (L309): Container for multiple computation scales.
- **CompuMethod** (L326): Represents a computation method for converting between internal and physical values.

### models/M2/MSR/AsamHdo/SpecialData.py

- **Sd** (L7): Represents special data with a global identifier and value.
- **SdgCaption** (L32): Represents a caption for special data groups with multilingual description.
- **Sdg** (L51): Represents a special data group containing special data items and references.

### models/M2/MSR/AsamHdo/Units.py

- **PhysicalDimension** (L16): Represents a physical dimension with exponents for SI base units.
- **SingleLanguageUnitNames** (L83): Represents single language unit names.
- **Unit** (L93): Represents a unit with display name, conversion factor, and physical dimension reference.
- **UnitGroup** (L136): Represents a group of units in the AUTOSAR model.

> Coverage: 29/29 (100.0%)

## models/M2/MSR/AsamHdo/Constraints

### models/M2/MSR/AsamHdo/Constraints/GlobalConstraints.py

- **InternalConstrs** (L7): Represents internal constraints for data values.
- **PhysConstrs** (L19): Represents physical constraints for data values with unit reference.
- **DataConstrRule** (L32): Represents a single data constraint rule with internal and physical constraints.
- **DataConstr** (L45): Represents data constraints with multiple rules.

> Coverage: 4/4 (100.0%)

## models/M2/MSR/CalibrationData

### models/M2/MSR/CalibrationData/CalibrationValue.py

- **SwValues** (L6): Collection of numerical values for calibration data.
- **SwValueCont** (L23): Container for calibration values with array size, physical values,

> Coverage: 2/2 (100.0%)

## models/M2/MSR/DataDictionary

### models/M2/MSR/DataDictionary/AuxillaryObjects.py

- **SwAddrMethod** (L5): Software address method defining memory allocation properties for data

### models/M2/MSR/DataDictionary/Axis.py

- **SwGenericAxisParam** (L4): Parameters for a generic axis including type reference and value list.
- **SwAxisGeneric** (L28): Generic axis definition with axis type reference and parameters.
- **SwAxisIndividual** (L52): Individual axis properties extending calibration axis type with compu
- **SwAxisGrouped** (L126): Grouped axis properties referencing a shared axis type with index and

### models/M2/MSR/DataDictionary/CalibrationParameter.py

- **SwCalprmAxisTypeProps** (L5): Abstract base class for calibration axis type properties including
- **SwCalprmAxis** (L20): Calibration axis with category, format, access mode, and axis type
- **SwCalprmAxisSet** (L34): Collection of SwCalprmAxis elements.

### models/M2/MSR/DataDictionary/DataDefProperties.py

- **SwImplPolicyEnum** (L7): Enumeration for software implementation policy.
- **SwDataDefPropsConditional** (L45): Patch for the time-stamp
- **SwDataDefProps** (L53): Software data definition properties describing data characteristics
- **SwPointerTargetProps** (L306): Properties for pointer targets including function pointer signature and
- **ValueList** (L340): List of values with single value and multi-value support.
- **SwTextProps** (L364): Represents software text properties in the AUTOSAR model.

### models/M2/MSR/DataDictionary/RecordLayout.py

- **SwRecordLayoutV** (L4): Variable definition within a record layout including base type, axis,
- **SwRecordLayoutGroupContent** (L77): Content of a record layout group referencing a sub-layout, sub-group, or
- **SwRecordLayoutGroup** (L111): Group within a record layout defining axis, category, and indexing
- **SwRecordLayout** (L208): Record layout element defining the structure of calibration data in

### models/M2/MSR/DataDictionary/ServiceProcessTask.py

- **SwServiceArg** (L4): Service argument with direction, array size, and data definition

### models/M2/MSR/DataDictionary/SystemConstant.py

- **SwSystemconst** (L10): Represents a software system constant in the AUTOSAR model.

> Coverage: 20/20 (100.0%)

## models/M2/MSR/Documentation

### models/M2/MSR/Documentation/Annotation.py

- **GeneralAnnotation** (L7): Abstract base class for annotations including origin, text, and label.
- **Annotation** (L42): Concrete annotation with origin, text, and label for documenting

> Coverage: 2/2 (100.0%)

## models/M2/MSR/Documentation/BlockElements

### models/M2/MSR/Documentation/BlockElements/Figure.py

- **GraphicFitEnum** (L9): Enumeration for graphic fitting modes.
- **Graphic** (L19): Graphic element with filename, dimensions, and fit properties.
- **Map** (L82): Image map definition for clickable regions within a graphic.
- **LGraphic** (L90): Language-specific graphic with an associated image and optional map.
- **MlFigure** (L126): Multi-language figure with caption, graphics, and optional verbatim

> Coverage: 5/5 (100.0%)

## models/M2/MSR/Documentation/TextModel

### models/M2/MSR/Documentation/TextModel/LanguageDataModel.py

- **LEnum** (L10): Enumeration literal for language-specific values.
- **LanguageSpecific** (L18): Abstract base class for language-specific content with language
- **LOverviewParagraph** (L47): Language-specific overview paragraph element.
- **LParagraph** (L55): Language-specific paragraph element.
- **LLongName** (L63): Language-specific long name element.
- **LPlainText** (L71): Language-specific plain text element.

### models/M2/MSR/Documentation/TextModel/MultilanguageData.py

- **MultiLanguageParagraph** (L7): Multi-language paragraph containing language-specific long name
- **MultiLanguageOverviewParagraph** (L25): Multi-language overview paragraph with language-specific overview
- **MultilanguageLongName** (L43): Multi-language long name containing language-specific long name
- **MultiLanguagePlainText** (L60): Multi-language plain text with language-specific text entries.

> Coverage: 10/10 (100.0%)

## models/M2/MSR/Documentation/TextModel/BlockElements

### models/M2/MSR/Documentation/TextModel/BlockElements/ListElements.py

- **ListEnum** (L6): Enumeration for list numbering types: number or unnumber.
- **Item** (L21): An item within a list with content defined by itemContents.
- **ARList** (L38): This meta-class represents the ability to express a list. The kind of list is specified in the attribute.

### models/M2/MSR/Documentation/TextModel/BlockElements/PaginationAndView.py

- **DocumentViewSelectable** (L5): Abstract base class for elements that can be selected in a document
- **Paginateable** (L16): Abstract base class for paginated document elements with chapter

> Coverage: 5/5 (100.0%)

## models/utils

### models/utils/uuid_mgr.py

- **UUIDMgr** (L5): Manager for UUID-based object tracking and duplicate detection in the

> Coverage: 1/1 (100.0%)

## parser

### parser/abstract_arxml_parser.py

- **AbstractARXMLParser** (L16): Abstract base class for ARXML parsers providing common XML parsing

### parser/arxml_parser.py

- **ARXMLParser** (L234): Main ARXML parser that loads AUTOSAR XML files into the model.

### parser/connector_xlsx_parser.py

- **ConnectorXls** (L17): Constants class defining column names for connector Excel worksheets.
- **ConnectorXlsReader** (L34): Reads connector definitions from Excel worksheets and maps them to

### parser/excel_parser.py

- **AbstractExcelParser** (L5): Abstract base class for Excel-based parsers providing column title

### parser/file_parser.py

- **FileListParser** (L9): FileListParser supports to collect the arxml files from the following rules

> Coverage: 6/6 (100.0%)

## report

### report/connector_xls_report.py

- **ConnectorXlsReport** (L7): Generates Excel reports for assembly and delegation SW connectors

### report/excel_report.py

- **ExcelReporter** (L5): Base class for Excel report generation providing workbook management,

> Coverage: 2/2 (100.0%)

## transformer

### transformer/abstract.py

- **AbstractTransformer** (L1): Abstract base class for data transformers with lifecycle methods.

### transformer/admin_data.py

- **AdminDataTransformer** (L8): Transformer that removes AdminData from all ARPackages and

> Coverage: 2/2 (100.0%)

## writer

### writer/abstract_arxml_writer.py

- **AbstractARXMLWriter** (L16): Abstract base class for ARXML writers providing common XML

### writer/arxml_writer.py

- **ARXMLWriter** (L226): Main ARXML writer that serializes the AUTOSAR model back to ARXML

> Coverage: 2/2 (100.0%)
