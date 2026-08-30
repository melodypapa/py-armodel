import xml.etree.cElementTree as ET
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswApiOptions,
    BswAsynchronousServerCallPoint,
    BswAsynchronousServerCallResultPoint,
    BswAsynchronousServerCallReturnsEvent,
    BswBackgroundEvent,
    BswCalledEntity,
    BswDataReceivedEvent,
    BswDataReceptionPolicy,
    BswDistinguishedPartition,
    BswOsTaskExecutionEvent,
    BswSchedulerNamePrefix,
    BswEvent,
    BswExternalTriggerOccurredEvent,
    BswInternalBehavior,
    BswInternalTriggeringPoint,
    BswInternalTriggerOccurredEvent,
    BswInterruptEntity,
    BswInterruptEvent,
    BswModeManagerErrorEvent,
    BswModeSenderPolicy,
    BswModeSwitchAckRequest,
    BswModeSwitchedAckEvent,
    BswModeSwitchEvent,
    BswModuleCallPoint,
    BswModuleEntity,
    BswOperationInvokedEvent,
    BswQueuedDataReceptionPolicy,
    BswSchedulableEntity,
    BswScheduleEvent,
    BswServiceDependency,
    BswServiceDependencyIdent,
    BswSynchronousServerCallPoint,
    BswTimingEvent,
    BswVariableAccess,
    RoleBasedBswModuleEntryAssignment,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation import BswImplementation
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import BswModuleClientServerEntry, BswModuleDependency, BswModuleEntry
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import BswModuleDescription
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.InstanceRefs import ModeInBswModuleDescriptionInstanceRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure import (
    ApplicationRuleBasedValueSpecification,
    ApplicationValueSpecification,
    ArrayValueSpecification,
    CompositeRuleBasedValueSpecification,
    ConstantReference,
    ConstantSpecification,
    NumericalValueSpecification,
    RecordValueSpecification,
    ReferenceValueSpecification,
    RuleArguments,
    RuleBasedAxisCont,
    RuleBasedValueCont,
    RuleBasedValueSpecification,
    TextValueSpecification,
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ConstantSpecificationMapping,
    NotAvailableValueSpecification,
    NumericalOrText,
    NumericalRuleBasedValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import FlatInstanceDescriptor, FlatMap
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import Code, Compiler, DependencyOnArtifact, Implementation, ImplementationProps, Linker
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import AbstractImplementationDataTypeElement, ImplementationDataType, ImplementationDataTypeElement
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ExecutableEntity, ExecutableEntityActivationReason, InternalBehavior
from armodel.models.M2.AUTOSARTemplates.CommonStructure.McGroups import McGroup, McGroupDataRefSet
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import (
    McDataAccessDetails,
    McDataInstance,
    McFunction,
    McParameterElementGroup,
    McSupportData,
    McSwEmulationMethodSupport,
    RoleBasedMcDataAssignment,
    RteEventInEcuInstanceRef,
    VariableAccessInEcuInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import (
    McFunctionDataRefSet,
    RptComponent,
    RptExecutableEntity,
    RptExecutableEntityEvent,
    RptServicePoint,
    RptSupportData,
    RptSwPrototypingAccess,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeDeclaration, ModeDeclarationGroup, ModeDeclarationGroupPrototype, ModeErrorBehavior
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import ResourceConsumption
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime import AnalyzedExecutionTime, MeasuredExecutionTime, RoughEstimateOfExecutionTime, SimulatedExecutionTime
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage import MeasuredHeapUsage, RoughEstimateHeapUsage, WorstCaseHeapUsage
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import MemorySection, SectionNamePrefix
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import MeasuredStackUsage, RoughEstimateStackUsage, StackUsage, WorstCaseStackUsage
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    BswMgrNeeds,
    ComMgrUserNeeds,
    CryptoServiceNeeds,
    DevelopmentError,
    DiagEventDebounceCounterBased,
    DiagEventDebounceMonitorInternal,
    DiagEventDebounceTimeBased,
    DiagnosticCapabilityElement,
    DiagnosticCommunicationManagerNeeds,
    DiagnosticEnableConditionNeeds,
    DiagnosticEventInfoNeeds,
    DiagnosticEventNeeds,
    DiagnosticIoControlNeeds,
    DiagnosticOperationCycleNeeds,
    DiagnosticRoutineNeeds,
    DiagnosticStorageConditionNeeds,
    DiagnosticValueNeeds,
    DltUserNeeds,
    DoIpRoutingActivationAuthenticationNeeds,
    DoIpRoutingActivationConfirmationNeeds,
    DtcStatusChangeNotificationNeeds,
    EcuStateMgrUserNeeds,
    ErrorTracerNeeds,
    FunctionInhibitionAvailabilityNeeds,
    IdsMgrNeeds,
    IndicatorStatusNeeds,
    NvBlockNeeds,
    ObdControlServiceNeeds,
    ObdInfoServiceNeeds,
    ObdMonitorServiceNeeds,
    ObdPidServiceNeeds,
    ObdRatioDenominatorNeeds,
    ObdRatioServiceNeeds,
    PossibleErrorReaction,
    RoleBasedDataAssignment,
    RuntimeError,
    SecureOnBoardCommunicationNeeds,
    ServiceDependency,
    ServiceNeeds,
    SupervisedEntityNeeds,
    TracedFailure,
    TransientFault,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation import (
    SignalServiceTranslationElementProps,
    SignalServiceTranslationEventProps,
    SignalServiceTranslationProps,
    SignalServiceTranslationPropsSet,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import PortPrototypeBlueprint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator import BlueprintGenerator
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import Keyword, KeywordSet
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import SwcBswMapping, SwcBswRunnableMapping, SwcBswSynchronizedModeGroupPrototype, SwcBswSynchronizedTrigger
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock import TDLETZoneClock, TimingClock, TimingClockSyncAccuracy
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescriptionEvent,
    TimingDescriptionEventChain,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventCom,
    TDEventCycleStart,
    TDEventFrClusterCycleStart,
    TDEventTTCanCycleStart,
    TDEventISignal,
    TDEventIPdu,
    TDEventFrame,
    TDEventFrameEthernet,
    TDHeaderIdRange,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.AgeConstraint import AgeConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    EOCEventRef,
    EOCExecutableEntityRefAbstract,
    EOCExecutableEntityRef,
    EOCExecutableEntityRefGroup,
    ExecutionOrderConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionTimeConstraint import (
    ExecutionTimeConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.LatencyTimingConstraint import LatencyTimingConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.OffsetConstraint import OffsetTimingConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationPointConstraint import SynchronizationPointConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming import SynchronizationTimingConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import SwcTiming, TimingExtension
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import DiagnosticServiceTable
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucAbstractReferenceValue,
    EcucAddInfoParamValue,
    EcucContainerValue,
    EcucInstanceReferenceValue,
    EcucModuleConfigurationValues,
    EcucNumericalParamValue,
    EcucParameterValue,
    EcucReferenceValue,
    EcucTextualParamValue,
    EcucValueCollection,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucAbstractConfigurationClass,
    EcucAbstractExternalReferenceDef,
    EcucAbstractInternalReferenceDef,
    EcucAbstractReferenceDef,
    EcucAbstractStringParamDef,
    EcucAddInfoParamDef,
    EcucBooleanParamDef,
    EcucChoiceContainerDef,
    EcucChoiceReferenceDef,
    EcucCommonAttributes,
    EcucConditionFormula,
    EcucConditionSpecification,
    EcucContainerDef,
    EcucDefinitionCollection,
    EcucDefinitionElement,
    EcucDerivationSpecification,
    EcucDestinationUriDef,
    EcucDestinationUriDefRefType,
    EcucDestinationUriDefSet,
    EcucDestinationUriPolicy,
    EcucEnumerationLiteralDef,
    EcucEnumerationParamDef,
    EcucFloatParamDef,
    EcucFunctionNameDef,
    EcucInstanceReferenceDef,
    EcucIntegerParamDef,
    EcucModuleDef,
    EcucMultilineStringParamDef,
    EcucMultiplicityConfigurationClass,
    EcucParamConfContainerDef,
    EcucParameterDef,
    EcucParameterDerivationFormula,
    EcucQuery,
    EcucReferenceDef,
    EcucStringParamDef,
    EcucSymbolicNameReferenceDef,
    EcucValidationCondition,
    EcucValueConfigurationClass,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwDescriptionEntity, HwElement, HwElementConnector, HwPin, HwPinConnector, HwPinGroup, HwPinGroupConnector
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwAttributeValue import HwAttributeValue
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeDef, HwCategory, HwType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1 import Documentation, DocumentationContext
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage, ReferenceBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import Collection
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject, EngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Describable, Identifiable, MultilanguageReferrable, Referrable, ShortNameFragment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue import TagWithOptionalValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    ARNumerical,
    Limit,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import LifeCycleInfo, LifeCycleInfoSet, LifeCyclePeriod
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    ConditionByFormula,
    PostBuildVariantCondition,
    PostBuildVariantCriterion,
    PredefinedVariant,
    SwSystemconstantValueSet,
    SwSystemconstValue,
    VariationPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints import (
    AttributeValueVariationPoint,
    BooleanValueVariationPoint,
    FloatValueVariationPoint,
    IntegerValueVariationPoint,
    LimitValueVariationPoint,
    NumericalValueVariationPoint,
    PositiveIntegerValueVariationPoint,
    TimeValueValueVariationPoint,
    UnlimitedIntegerValueVariationPoint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import TimingConditionFormula
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import ModeInBswInstanceRef, ModeInSwcInstanceRef, TimingCondition
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    TimingExtensionResource,
    TimingModeInstance,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import ComponentInCompositionInstanceRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression import (
    AutosarOperationArgumentInstance,
    AutosarVariableInstance,
    OperationArgumentInComponentInstanceRef,
    TDEventOccurrenceExpression,
    TDEventOccurrenceExpressionFormula,
    VariableInComponentInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventVfb import (
    TDEventModeDeclaration,
    TDEventOperation,
    TDEventTrigger,
    TDEventVariableDataPrototype,
    TDEventVfb,
    TDEventVfbPort,
    TDEventVfbReference,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSwcInternalBehavior import (
    TDEventSwc,
    TDEventSwcInternalBehavior,
    TDEventSwcInternalBehaviorReference,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBswInternalBehavior import (
    TDEventBswInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBsw import (
    TDEventBsw,
    TDEventBswModule,
    TDEventBswModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventComplex import (
    TDEventComplex,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSLLET import (
    TDEventSLLET,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSLLET import (
    TDEventSLLETPort,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import (
    ArbitraryEventTriggering,
    BurstPatternEventTriggering,
    ConcretePatternEventTriggering,
    ConfidenceInterval,
    EventTriggeringConstraint,
    PeriodicEventTriggering,
    SporadicEventTriggering,
)

VALUE_ACCESS_CLASS_TO_TAG = {
    LimitValueVariationPoint: "LIMIT",
    NumericalValueVariationPoint: "NUMERICAL-VALUE-VARIATION-POINT",
    BooleanValueVariationPoint: "BOOLEAN-VALUE-VARIATION-POINT",
    FloatValueVariationPoint: "FLOAT-VALUE-VARIATION-POINT",
    IntegerValueVariationPoint: "INTEGER-VALUE-VARIATION-POINT",
    PositiveIntegerValueVariationPoint: "POSITIVE-INTEGER-VALUE-VARIATION-POINT",
    TimeValueValueVariationPoint: "TIME-VALUE-VARIATION-POINT",
    UnlimitedIntegerValueVariationPoint: "UNLIMITED-INTEGER-VALUE-VARIATION-POINT",
}
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    ClientServerAnnotation,
    DelegatedPortAnnotation,
    IoHwAbstractionServerAnnotation,
    ModePortAnnotation,
    NvDataPortAnnotation,
    ParameterPortAnnotation,
    SenderReceiverAnnotation,
    TriggerPortAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    ClientComSpec,
    CompositeNetworkRepresentation,
    ModeSwitchedAckRequest,
    ModeSwitchReceiverComSpec,
    ModeSwitchSenderComSpec,
    NonqueuedReceiverComSpec,
    NonqueuedSenderComSpec,
    NvProvideComSpec,
    NvRequireComSpec,
    ParameterProvideComSpec,
    ParameterRequireComSpec,
    PPortComSpec,
    QueuedReceiverComSpec,
    QueuedSenderComSpec,
    ReceiverComSpec,
    ReceptionComSpecProps,
    RPortComSpec,
    SenderComSpec,
    ServerComSpec,
    TransformationComSpecProps,
    TransmissionAcknowledgementRequest,
    TransmissionComSpecProps,
    UserDefinedTransformationComSpecProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    AbstractProvidedPortPrototype,
    AbstractRequiredPortPrototype,
    ApplicationSwComponentType,
    AtomicSwComponentType,
    ComplexDeviceDriverSwComponentType,
    EcuAbstractionSwComponentType,
    NvBlockSwComponentType,
    PortGroup,
    PortPrototype,
    PPortPrototype,
    PRPortPrototype,
    RPortPrototype,
    SensorActuatorSwComponentType,
    ServiceProxySwComponentType,
    ServiceSwComponentType,
    SwComponentType,
    SymbolProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
    InnerPortGroupInCompositionInstanceRef,
    ModeGroupInAtomicSwcInstanceRef,
    PModeGroupInAtomicSwcInstanceRef,
    PTriggerInAtomicSwcTypeInstanceRef,
    RModeGroupInAtomicSWCInstanceRef,
    RModeInAtomicSwcInstanceRef,
    RVariableInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    AssemblySwConnector,
    CompositionSwComponentType,
    DelegationSwConnector,
    InstantiationTimingEventProps,
    PassThroughSwConnector,
    SwComponentPrototype,
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import (
    InstanceEventInCompositionInstanceRef,
    PPortInCompositionInstanceRef,
    RPortInCompositionInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
    POperationInAtomicSwcInstanceRef,
    ROperationInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    ApplicationArrayElement,
    ApplicationCompositeElementDataPrototype,
    ApplicationRecordElement,
    AutosarDataPrototype,
    DataPrototype,
    ParameterDataPrototype,
    VariableDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ApplicationArrayDataType,
    ApplicationCompositeDataType,
    ApplicationDataType,
    ApplicationPrimitiveDataType,
    ApplicationRecordDataType,
    AutosarDataType,
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import (
    EndToEndDescription,
    EndToEndProtection,
    EndToEndProtectionSet,
    EndToEndProtectionVariablePrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.EndToEndProtection import EndToEndProtectionISignalIPdu
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import (
    ConsistencyNeeds,
    DataPrototypeGroup,
    RunnableEntityGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import (
    InnerDataPrototypeGroupInCompositionInstanceRef,
    InnerRunnableEntityGroupInCompositionInstanceRef,
    RunnableEntityInCompositionInstanceRef,
    VariableDataPrototypeInCompositionInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor, ModeSwitchEventTriggeredActivity, NvBlockDataMapping, NvBlockDescriptor
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ApplicationError,
    ArgumentDataPrototype,
    ClientServerInterface,
    ClientServerInterfaceMapping,
    ClientServerOperation,
    ClientServerOperationMapping,
    DataInterface,
    DataPrototypeMapping,
    ModeDeclarationMapping,
    ModeDeclarationMappingSet,
    ModeInterfaceMapping,
    ModeSwitchInterface,
    NvDataInterface,
    ParameterInterface,
    PortInterface,
    PortInterfaceMappingSet,
    SenderReceiverInterface,
    SubElementMapping,
    TextTableMapping,
    TriggerInterface,
    VariableAndParameterInterfaceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import ApplicationCompositeElementInPortInterfaceInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RptExecutableEntityProperties, RptImplPolicy
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import SwcImplementation
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import (
    AsynchronousServerCallPoint,
    RunnableEntity,
    RunnableEntityArgument,
    SwcExclusiveAreaPolicy,
    SwcInternalBehavior,
    SynchronousServerCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarVariableRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import ParameterAccess, VariableAccess
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import ParameterInAtomicSWCTypeInstanceRef, VariableInAtomicSWCTypeInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import IncludedModeDeclarationGroupSet, ModeAccessPoint, ModeSwitchPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import PortDefinedArgumentValue
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import (
    AsynchronousServerCallReturnsEvent,
    BackgroundEvent,
    DataReceivedEvent,
    DataSendCompletedEvent,
    InitEvent,
    InternalTriggerOccurredEvent,
    ModeSwitchedAckEvent,
    OperationInvokedEvent,
    RTEEvent,
    SwcModeSwitchEvent,
    TimingEvent,
    WaitPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import ServerCallPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import RoleBasedDataTypeAssignment, RoleBasedPortAssignment, SwcServiceDependency
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import VariationPointProxy
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SwcToEcuMapping, System, SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    SenderRecCompositeTypeMapping,
    SenderReceiverToSignalGroupMapping,
    SenderReceiverToSignalMapping,
    SenderRecRecordElementMapping,
    SenderRecRecordTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import DiagnosticConnection, TpConnection
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import ECUMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanFrame,
    CanFrameTriggering,
    CanXlFrameTriggeringProps,
    RxIdentifierRange,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanCommunication import TtcanAbsolutelyScheduledTiming
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    AbstractCanCommunicationController,
    AbstractCanCommunicationControllerAttributes,
    CanCommunicationConnector,
    CanCommunicationController,
    CanControllerConfigurationRequirements,
    CanControllerFdConfiguration,
    CanControllerFdConfigurationRequirements,
    CanControllerXlConfiguration,
    CanControllerXlConfigurationRequirements,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    SocketConnectionBundle,
    SocketConnectionIpduIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet import (
    TcpOptionFilterList,
    TcpOptionFilterSet,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel import (
    SoAdRoutingGroup,
    SocketConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import GenericEthernetFrame
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPort,
    CouplingPortAbstractShaper,
    CouplingPortConnection,
    CouplingPortDetails,
    CouplingPortFifo,
    CouplingPortRatePolicy,
    CouplingPortScheduler,
    CouplingPortStructuralElement,
    CouplingPortTrafficClassAssignment,
    EthernetCluster,
    GlobalTimeCouplingPortProps,
    PlcaProps,
    EthernetCommunicationConnector,
    EthernetCommunicationController,
    EthernetPriorityRegeneration,
    DhcpServerConfiguration,
    InitialSdDelayConfig,
    Ipv4DhcpServerConfiguration,
    Ipv6DhcpServerConfiguration,
    MacMulticastGroup,
    SdClientConfig,
    VlanMembership,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import RequestResponseDelay
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    MacSecCipherSuiteConfig,
    MacSecCryptoAlgoConfig,
    MacSecGlobalKayProps,
    MacSecKayParticipant,
    MacSecLocalKayProps,
    MacSecProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanControllerConfiguration, CanXlProps
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    ApplicationEndpoint,
    DoIpEntity,
    InfrastructureServices,
    Ipv6Configuration,
    NetworkEndpoint,
    NetworkEndpointAddress,
    TimeSyncClientConfiguration,
    TimeSynchronization,
    GenericTp,
    TcpTp,
    TpPort,
    TransportProtocolConfiguration,
    UdpTp,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    AbstractServiceInstance,
    ConsumedEventGroup,
    ConsumedServiceInstance,
    EventHandler,
    PduActivationRoutingGroup,
    ProvidedServiceInstance,
    SdServerConfig,
    SoAdConfig,
    StaticSocketConnection,
    SocketAddress,
    SomeipSdClientEventGroupTimingConfig,
    SomeipSdClientServiceInstanceConfig,
    SomeipSdServerEventGroupTimingConfig,
    SomeipServiceVersion,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayAbsolutelyScheduledTiming, FlexrayFrame, FlexrayFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
    FlexrayCluster,
    FlexrayCommunicationConnector,
    FlexrayCommunicationController,
    FlexrayFifoConfiguration,
    FlexrayFifoRange,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    ApplicationEntry,
    AssignFrameId,
    AssignFrameIdRange,
    AssignNad,
    ConditionalChangeNad,
    DataDumpEntry,
    FreeFormat,
    LinConfigurationEntry,
    LinErrorResponse,
    LinFrameTriggering,
    LinScheduleTable,
    LinUnconditionalFrame,
    SaveConfigurationEntry,
    ScheduleTableEntry,
    UnassignFrameId,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import (
    LinCluster,
    LinCommunicationConnector,
    LinCommunicationController,
    LinConfigurableFrame,
    LinMaster,
    LinOrderedConfigurableFrame,
    LinSlaveConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import Gateway, IPduMapping, ISignalMapping, TargetIPduRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    CommConnectorPort,
    ContainedIPduProps,
    DcmIPdu,
    DynamicPart,
    DynamicPartAlternative,
    Frame,
    FramePort,
    FrameTriggering,
    GeneralPurposeIPdu,
    GeneralPurposePdu,
    IPdu,
    IPduPort,
    IPduTiming,
    ISignal,
    ISignalGroup,
    ISignalIPdu,
    ISignalIPduGroup,
    ISignalPort,
    ISignalToIPduMapping,
    ISignalTriggering,
    MultiplexedIPdu,
    MultiplexedPart,
    NmPdu,
    NPdu,
    Pdu,
    PduTriggering,
    SecureCommunicationAuthenticationProps,
    SecureCommunicationFreshnessProps,
    SecureCommunicationProps,
    SecureCommunicationPropsSet,
    SecuredIPdu,
    SegmentPosition,
    StaticPart,
    SystemSignal,
    SystemSignalGroup,
    UserDefinedIPdu,
    UserDefinedPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (  # noqa: F401
    AbstractCanPhysicalChannel,
    CanPhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanClusterBusOffRecovery
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    AbstractCanCluster,
    CanCluster,
    CommunicationCluster,
    CommunicationConnector,
    CommunicationController,
    CommunicationCycle,
    CycleRepetition,
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinPhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import EthernetPhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayPhysicalChannel
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import (
    CyclicTiming,
    EventControlledTiming,
    TimeRangeType,
    TransmissionModeCondition,
    TransmissionModeDeclaration,
    TransmissionModeTiming,
    TriggerIPduSendCondition,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef, VariableDataPrototypeInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    CanNmCluster,
    CanNmEcu,
    CanNmClusterCoupling,
    CanNmNode,
    J1939NmNode,
    J1939NodeName,
    NmCluster,
    NmConfig,
    NmEcu,
    NmNode,
    UdpNmCluster,
    UdpNmClusterCoupling,
    UdpNmEcu,
    UdpNmNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import SwcToImplMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    BufferProperties,
    DataPrototypeInPortInterfaceRef,
    DataPrototypeInClientServerInterfaceInstanceRef,
    DataPrototypeInSenderReceiverInterfaceInstanceRef,
    DataPrototypeTransformationProps,
    DataTransformation,
    DataTransformationSet,
    E2EProfileCompatibilityProps,
    EndToEndTransformationComSpecProps,
    EndToEndTransformationDescription,
    EndToEndTransformationISignalProps,
    TransformationDescription,
    TransformationISignalProps,
    TransformationTechnology,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    CanTpAddress,
    CanTpChannel,
    CanTpConfig,
    CanTpConnection,
    CanTpEcu,
    CanTpNode,
    DoIpLogicAddress,
    DoIpTpConfig,
    DoIpTpConnection,
    LinTpConfig,
    LinTpConnection,
    LinTpNode,
    TpAddress,
    TpConfig,
)
from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData, DocRevision, Modification
from armodel.models.M2.MSR.AsamHdo.BaseTypes import BaseTypeDirectDefinition, SwBaseType
from armodel.models.M2.MSR.AsamHdo.ComputationMethod import (
    Compu,
    CompuConst,
    CompuConstContent,
    CompuConstFormulaContent,
    CompuConstNumericContent,
    CompuConstTextContent,
    CompuMethod,
    CompuNominatorDenominator,
    CompuScale,
    CompuScaleConstantContents,
    CompuScaleRationalFormula,
    CompuScales,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import DataConstr, InternalConstrs, PhysConstrs, ScaleConstr
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg, SdgContents
from armodel.models.M2.MSR.AsamHdo.Units import PhysicalDimension, Unit
from armodel.models.M2.MSR.CalibrationData.CalibrationValue import SwValueCont, SwValues, ValueGroup
from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects import SwAddrMethod
from armodel.models.M2.MSR.DataDictionary.Axis import SwAxisGeneric, SwAxisGrouped, SwAxisIndividual, SwGenericAxisParam
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import SwCalprmAxis, SwCalprmAxisSet
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwBitRepresentation,
    SwCalprmRefProxy,
    SwDataDefProps,
    SwDataDependency,
    SwPointerTargetProps,
    SwTextProps,
    SwVariableRefProxy,
    ValueList,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout import SwRecordLayout, SwRecordLayoutGroup, SwRecordLayoutV
from armodel.models.M2.MSR.DataDictionary.ServiceProcessTask import SwServiceArg
from armodel.models.M2.MSR.DataDictionary.SystemConstant import SwSystemconst
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.MSR.Documentation.BlockElements import Caption
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import Graphic, MlFigure
from armodel.models.M2.MSR.Documentation.BlockElements.Formula import MlFormula
from armodel.models.M2.MSR.Documentation.Chapters import (
    Chapter,
    ChapterContent,
    ChapterModel,
    PredefinedChapter,
    Topic1,
    TopicContent,
    TopicContentOrMsrQuery,
)
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryChapter, MsrQueryTopic1
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import ARList, DefItem, DefList, IndentSample, LabeledItem, LabeledList
from armodel.models.M2.MSR.Documentation.BlockElements.Note import Note
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import DocumentViewSelectable, Paginateable
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import (
    StructuredReq,
    Traceable,
    TraceableText,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import EmphasisText, IndexEntry, Tt
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LanguageSpecific, LLongName, LPlainText, LVerbatim
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryArg, MsrQueryP1, MsrQueryP2, MsrQueryProps
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName, MultiLanguageOverviewParagraph, MultiLanguageParagraph, MultiLanguagePlainText, MultiLanguageVerbatim
from armodel.writer.abstract_arxml_writer import AbstractARXMLWriter

#: Mapping between BindingTimeEnum camelCase values and their XML attribute tokens
#: (AR:BINDING-TIME-ENUM--SIMPLE).
BINDING_TIME_XML_MAP = {
    "codeGenerationTime": "CODE-GENERATION-TIME",
    "linkTime": "LINK-TIME",
    "preCompileTime": "PRE-COMPILE-TIME",
    "systemDesignTime": "SYSTEM-DESIGN-TIME",
}

#: Mapping between IntervalTypeEnum values and their XML attribute tokens
#: (AR:INTERVAL-TYPE-ENUM--SIMPLE).
INTERVAL_TYPE_XML_MAP = {
    "closed": "CLOSED",
    "open": "OPEN",
}


class ARXMLWriter(AbstractARXMLWriter):
    """
    Main ARXML writer that serializes the AUTOSAR model back to ARXML
    format. Dispatches element writing to type-specific write methods.
    """

    def __init__(self, options=None) -> None:
        super().__init__(options)

    def setShortName(self, parent: ET.Element, name: str) -> ET.Element:
        sub_element = ET.SubElement(parent, "SHORT-NAME")
        sub_element.text = name

        return sub_element

    def setRxIdentifierRange(self, element: ET.Element, key: str, range: RxIdentifierRange):
        if range is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalNumericalValue(child_element, "LOWER-CAN-ID", range.getLowerCanId())
            self.setChildElementOptionalNumericalValue(child_element, "UPPER-CAN-ID", range.getUpperCanId())

    def setJ1939NodeName(self, element: ET.Element, key: str, node_name: J1939NodeName):
        if node_name is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalBooleanValue(child_element, "ARBITRARY-ADDRESS-CAPABLE", node_name.getArbitraryAddressCapable())
            self.setChildElementOptionalIntegerValue(child_element, "ECU-INSTANCE", node_name.getEcuInstance())
            self.setChildElementOptionalIntegerValue(child_element, "FUNCTION", node_name.getFunction())
            self.setChildElementOptionalIntegerValue(child_element, "FUNCTION-INSTANCE", node_name.getFunctionInstance())
            self.setChildElementOptionalIntegerValue(child_element, "IDENTITIY-NUMBER", node_name.getIdentitiyNumber())
            self.setChildElementOptionalIntegerValue(child_element, "INDUSTRY-GROUP", node_name.getIndustryGroup())
            self.setChildElementOptionalIntegerValue(child_element, "MANUFACTURER-CODE", node_name.getManufacturerCode())
            self.setChildElementOptionalIntegerValue(child_element, "VEHICLE-SYSTEM", node_name.getVehicleSystem())
            self.setChildElementOptionalIntegerValue(child_element, "VEHICLE-SYSTEM-INSTANCE", node_name.getVehicleSystemInstance())

    def writeSds(self, parent: ET.Element, contents: SdgContents):
        for sd in contents.getSds():
            sd_tag = ET.SubElement(parent, "SD")
            self.writeARObjectAttributes(sd_tag, sd)
            gid = sd.getGID()
            if gid is not None:
                sd_tag.attrib["GID"] = gid.getValue()
            xml_space = sd.getXmlSpace()
            if xml_space is not None:
                sd_tag.attrib["{http://www.w3.org/XML/1998/namespace}space"] = xml_space.getValue()
            value = sd.getValue()
            if value is not None:
                sd_tag.text = value.getValue()

    def writeSdfs(self, parent: ET.Element, contents: SdgContents):
        for sdf in contents.getSdfs():
            sdf_tag = ET.SubElement(parent, "SDF")
            self.writeARObjectAttributes(sdf_tag, sdf)
            gid = sdf.getGID()
            if gid is not None:
                sdf_tag.attrib["GID"] = gid.getValue()
            value = sdf.getValue()
            if value is not None:
                sdf_tag.text = value.getValue()

    def writeSdgCaption(self, element: ET.Element, sdg: Sdg):
        caption = sdg.getSdgCaption()
        if caption is not None:
            child_element = ET.SubElement(element, "SDG-CAPTION")
            self.writeMultilanguageReferrable(child_element, caption)

    def writeSdgSdxRefs(self, element: ET.Element, contents: SdgContents):
        for ref in contents.getSdxRefs():
            self.setChildElementOptionalRefType(element, "SDX-REF", ref)

    def writeSdgSdxfRefs(self, element: ET.Element, contents: SdgContents):
        for ref in contents.getSdxfRefs():
            self.setChildElementOptionalRefType(element, "SDXF", ref)

    def setSdg(self, element: ET.Element, sdg: Sdg):
        if sdg is not None:
            child_element = ET.SubElement(element, "SDG")
            self.writeARObjectAttributes(child_element, sdg)
            gid = sdg.getGID()
            if gid is not None:
                child_element.attrib["GID"] = gid.getValue()
            self.writeSdgCaption(child_element, sdg)
            contents = sdg.getSdgContentsType()
            if contents is not None:
                for sdg_item in contents.getSdgs():
                    self.setSdg(child_element, sdg_item)
                self.writeSds(child_element, contents)
                self.writeSdfs(child_element, contents)
                self.writeSdgSdxRefs(child_element, contents)
                self.writeSdgSdxfRefs(child_element, contents)

    def writeBlueprintGenerator(self, element: ET.Element, generator: BlueprintGenerator):
        if generator is not None:
            child_element = ET.SubElement(element, "FORMAL-BLUEPRINT-GENERATOR")
            self.writeARObjectAttributes(child_element, generator)
            # XSD sequence: INTRODUCTION (offset 10) before EXPRESSION (offset 20).
            self.writeDocumentationBlock(child_element, "INTRODUCTION", generator.getIntroduction())
            expression = generator.getExpression()
            if expression is not None:
                expression_element = ET.SubElement(child_element, "EXPRESSION")
                expression_element.text = expression.getValue()

    def writeConditionByFormula(self, element: ET.Element, condition: ConditionByFormula, key: str = "SW-SYSCOND"):
        if condition is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, condition)
            binding_time = condition.getBindingTime()
            if binding_time is not None:
                token = BINDING_TIME_XML_MAP.get(binding_time.getValue())
                if token is None:
                    self.notImplemented("Unsupported BINDING-TIME <%s>" % binding_time.getValue())
                else:
                    child_element.attrib["BINDING-TIME"] = token

    def writePostBuildVariantCondition(self, element: ET.Element, condition: PostBuildVariantCondition):
        child_element = ET.SubElement(element, "POST-BUILD-VARIANT-CONDITION")
        self.writeARObjectAttributes(child_element, condition)
        self.setChildElementOptionalRefType(child_element, "MATCHING-CRITERION-REF", condition.getMatchingCriterionRef())
        self.setChildElementOptionalIntegerValue(child_element, "VALUE", condition.getValue())

    def writeVariationPoint(self, element: ET.Element, variation_point: VariationPoint):
        if variation_point is not None:
            child_element = ET.SubElement(element, "VARIATION-POINT")
            self.writeARObjectAttributes(child_element, variation_point)
            # XSD sequence (AUTOSAR_00046.xsd group AR:VARIATION-POINT, line 99470):
            # SHORT-LABEL, DESC, BLUEPRINT-CONDITION, [FORMAL-BLUEPRINT-CONDITION obsolete],
            # FORMAL-BLUEPRINT-GENERATOR, SW-SYSCOND, POST-BUILD-VARIANT-CONDITIONS, SDG.
            short_label = variation_point.getShortLabel()
            if short_label is not None:
                label_element = ET.SubElement(child_element, "SHORT-LABEL")
                label_element.text = short_label.getValue()
            self.setMultiLanguageOverviewParagraph(child_element, "DESC", variation_point.getDesc())
            self.writeDocumentationBlock(child_element, "BLUEPRINT-CONDITION", variation_point.getBlueprintCondition())
            self.writeBlueprintGenerator(child_element, variation_point.getFormalBlueprintGenerator())
            self.writeConditionByFormula(child_element, variation_point.getSwSyscond())
            conditions = variation_point.getPostBuildVariantConditions()
            if len(conditions) > 0:
                conditions_element = ET.SubElement(child_element, "POST-BUILD-VARIANT-CONDITIONS")
                for condition in conditions:
                    self.writePostBuildVariantCondition(conditions_element, condition)
            self.setSdg(child_element, variation_point.getSdg())

    def writeAdminDataSdgs(self, parent: ET.Element, admin_data: AdminData):
        sdgs = admin_data.getSdgs()
        if len(sdgs) > 0:
            sdgs_tag = ET.SubElement(parent, "SDGS")
            for sdg in sdgs:
                self.setSdg(sdgs_tag, sdg)

    def setChildLimitElement(self, element: ET.Element, key: str, limit: Limit):
        if limit is not None:
            limit_tag = ET.SubElement(element, key)
            self.writeARObjectAttributes(limit_tag, limit)
            interval_type = limit.getIntervalType()
            if interval_type is not None:
                limit_tag.attrib["INTERVAL-TYPE"] = interval_type.getValue()
            limit_tag.text = limit.getValue()

    def writeReferrable(self, element: ET.Element, referrable: Referrable):
        self.writeARObjectAttributes(element, referrable)
        self.setShortName(element, referrable.getShortName())
        if isinstance(referrable, Referrable):
            self.setShortNameFragments(element, referrable.getShortNameFragments())

    def writeTraceable(self, element: ET.Element, traceable: Traceable):
        trace_refs = traceable.getTraceRefs()
        if trace_refs is not None and len(trace_refs) > 0:
            refs_tag = ET.SubElement(element, "TRACE-REFS")
            for trace_ref in trace_refs:
                ref_tag = ET.SubElement(refs_tag, "TRACE-REF")
                ref_tag.text = trace_ref.getValue()

    def setShortNameFragment(self, element: ET.Element, fragment: ShortNameFragment):
        if fragment is not None:
            child_element = ET.SubElement(element, "SHORT-NAME-FRAGMENT")
            self.writeARObjectAttributes(child_element, fragment)
            if fragment.getRole() is not None:
                role_element = ET.SubElement(child_element, "ROLE")
                role_element.text = fragment.getRole()
            self.setChildElementOptionalIdentifier(child_element, "FRAGMENT", fragment.getFragment())

    def setShortNameFragments(self, element: ET.Element, fragments: List[ShortNameFragment]):
        if fragments is not None and len(fragments) > 0:
            child_element = ET.SubElement(element, "SHORT-NAME-FRAGMENTS")
            for fragment in fragments:
                self.setShortNameFragment(child_element, fragment)

    def setLanguageSpecific(self, element: ET.Element, key: str, specific: LanguageSpecific):
        child_element = ET.SubElement(element, key)
        self.writeARObjectAttributes(child_element, specific)
        if specific.getL() is not None:
            child_element.attrib["L"] = specific.getL()
        child_element.text = specific.getValue()

    def setLLongName(self, element: ET.Element, name: LLongName):
        child_element = ET.SubElement(element, "L-4")
        self.writeARObjectAttributes(child_element, name)
        if name.getL() is not None:
            child_element.attrib["L"] = name.getL()
        if name.getSup() is not None:
            child_element.attrib["SUP"] = name.getSup().getValue()
        if name.getSub() is not None:
            child_element.attrib["SUB"] = name.getSub().getValue()
        child_element.text = name.getValue()
        if name.getE() is not None:
            self.setEmphasisText(child_element, "E", name.getE())
        if name.getIe() is not None:
            self.setIndexEntry(child_element, "IE", name.getIe())
        if name.getTt() is not None:
            self.setTt(child_element, "TT", name.getTt())

    def setEmphasisText(self, element: ET.Element, key: str, emphasis: EmphasisText):
        child_element = ET.SubElement(element, key)
        if emphasis.getColor() is not None:
            child_element.attrib["COLOR"] = emphasis.getColor().getValue()
        if emphasis.getSup() is not None:
            child_element.attrib["SUP"] = emphasis.getSup().getValue()
        if emphasis.getSub() is not None:
            child_element.attrib["SUB"] = emphasis.getSub().getValue()
        child_element.text = emphasis.getValue().getValue() if emphasis.getValue() is not None else None
        if emphasis.getTt() is not None:
            self.setTt(child_element, "TT", emphasis.getTt())

    def setIndexEntry(self, element: ET.Element, key: str, index_entry: IndexEntry):
        child_element = ET.SubElement(element, key)
        if index_entry.getSup() is not None:
            child_element.attrib["SUP"] = index_entry.getSup().getValue()
        if index_entry.getSub() is not None:
            child_element.attrib["SUB"] = index_entry.getSub().getValue()
        child_element.text = index_entry.getValue().getValue() if index_entry.getValue() is not None else None

    def setTt(self, element: ET.Element, key: str, tt: Tt):
        child_element = ET.SubElement(element, key)
        if tt.getType() is not None:
            child_element.attrib["TYPE"] = tt.getType().getValue()
        if tt.getTexRender() is not None:
            child_element.attrib["TEX-RENDER"] = tt.getTexRender().getValue()
        child_element.text = tt.getValue().getValue() if tt.getValue() is not None else None

    def setMultiLongName(self, element: ET.Element, key: str, long_name: MultilanguageLongName):
        if long_name is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, long_name)
            for l4 in long_name.getL4s():
                self.setLLongName(child_element, l4)

    def setLOverviewParagraph(self, element: ET.Element, name: LLongName):
        self.setLanguageSpecific(element, "L-2", name)

    def setMultiLanguageOverviewParagraph(self, element: ET.Element, key: str, paragraph: MultiLanguageOverviewParagraph):
        if paragraph is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, paragraph)
            for l2 in paragraph.getL2s():
                self.setLOverviewParagraph(child_element, l2)

    def writeMultilanguageReferrable(self, element: ET.Element, referrable: MultilanguageReferrable):
        self.writeReferrable(element, referrable)
        if referrable.longName is not None:
            self.setMultiLongName(element, "LONG-NAME", referrable.longName)

    def setCaption(self, element: ET.Element, key: str, caption: Caption):
        if caption is not None:
            child_element = ET.SubElement(element, key)
            self.writeMultilanguageReferrable(child_element, caption)
            self.setMultiLanguageOverviewParagraph(child_element, "DESC", caption.getDesc())

    def setLPlainText(self, element: ET.Element, text: LPlainText):
        self.setLanguageSpecific(element, "L-10", text)

    def setMultiLanguagePlainText(self, element: ET.Element, key: str, paragraph: MultiLanguagePlainText):
        if paragraph is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, paragraph)
            for l10 in paragraph.getL10s():
                self.setLPlainText(child_element, l10)

    def writeModification(self, element: ET.Element, modification: Modification):
        if modification is not None:
            child_element = ET.SubElement(element, "MODIFICATION")
            self.setMultiLanguageOverviewParagraph(child_element, "CHANGE", modification.getChange())
            self.setMultiLanguageOverviewParagraph(child_element, "REASON", modification.getReason())

    def writeDocRevisionModifications(self, element: ET.Element, revision: DocRevision):
        modifications = revision.getModifications()
        if len(modifications) > 0:
            child_element = ET.SubElement(element, "MODIFICATIONS")
            for modification in modifications:
                if isinstance(modification, Modification):
                    self.writeModification(child_element, modification)
                else:
                    self.notImplemented("Unsupported Modification <%s>" % type(modification))

    def writeDocRevision(self, element: ET.Element, revision: DocRevision):
        if revision is not None:
            child_element = ET.SubElement(element, "DOC-REVISION")
            # self.setChildElementOptionalDateTime(child_element, "DATE", revision.getDate())
            # self.setChildElementOptionalLiteral(child_element, "ISSUED-BY", revision.getIssuedBy())
            self.setChildElementOptionalRevisionLabelString(child_element, "REVISION-LABEL", revision.getRevisionLabel())
            self.setChildElementOptionalRevisionLabelString(child_element, "REVISION-LABEL-P-1", revision.getRevisionLabelP1())
            self.setChildElementOptionalRevisionLabelString(child_element, "REVISION-LABEL-P-2", revision.getRevisionLabelP2())
            self.setChildElementOptionalLiteral(child_element, "STATE", revision.getState())
            self.setChildElementOptionalLiteral(child_element, "ISSUED-BY", revision.getIssuedBy())
            self.setChildElementOptionalDateTime(child_element, "DATE", revision.getDate())
            self.writeDocRevisionModifications(child_element, revision)

    def writeAdminDataDocRevisions(self, element: ET.Element, admin_data: AdminData):
        revisions = admin_data.getDocRevisions()
        if len(revisions) > 0:
            child_element = ET.SubElement(element, "DOC-REVISIONS")
            for revision in revisions:
                if isinstance(revision, DocRevision):
                    self.writeDocRevision(child_element, revision)
                else:
                    self.notImplemented("Unsupported DocRevision <%s>" % type(revision))

    def setAdminData(self, element: ET.Element, admin_data: AdminData):
        if admin_data is not None:
            self.logger.debug("Write AdminData")
            child_element = ET.SubElement(element, "ADMIN-DATA")
            self.writeARObjectAttributes(child_element, admin_data)
            self.setChildElementOptionalLiteral(child_element, "LANGUAGE", admin_data.getLanguage())
            self.setMultiLanguagePlainText(child_element, "USED-LANGUAGES", admin_data.getUsedLanguages())
            self.writeAdminDataSdgs(child_element, admin_data)
            self.writeAdminDataDocRevisions(child_element, admin_data)

    def writeIdentifiable(self, element: ET.Element, identifiable: Identifiable):
        self.writeMultilanguageReferrable(element, identifiable)
        self.setAnnotations(element, identifiable.getAnnotations())
        self.setMultiLanguageOverviewParagraph(element, "DESC", identifiable.getDesc())
        self.setChildElementOptionalLiteral(element, "CATEGORY", identifiable.getCategory())
        self.writeDocumentationBlock(element, "INTRODUCTION", identifiable.getIntroduction())
        self.setAdminData(element, identifiable.getAdminData())
        if isinstance(identifiable, Identifiable):
            self.writeVariationPoint(element, identifiable.getVariationPoint())

    def writeARElement(self, parent: ET.Element, ar_element: ARElement):
        self.writeIdentifiable(parent, ar_element)

    def writeTransmissionAcknowledgementRequest(self, element: ET.Element, acknowledge: TransmissionAcknowledgementRequest):
        if acknowledge is not None:
            child_element = ET.SubElement(element, "TRANSMISSION-ACKNOWLEDGE")
            self.writeARObjectAttributes(child_element, acknowledge)
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT", acknowledge.getTimeout())

    def writeTransmissionComSpecProps(self, element: ET.Element, props: TransmissionComSpecProps):
        if props is not None:
            child_element = ET.SubElement(element, "TRANSMISSION-PROPS")
            self.writeARObjectAttributes(child_element, props)
            self.setChildElementOptionalTimeValue(child_element, "DATA-UPDATE-PERIOD", props.getDataUpdatePeriod())
            self.setChildElementOptionalTimeValue(child_element, "MINIMUM-SEND-INTERVAL", props.getMinimumSendInterval())
            self.setChildElementOptionalLiteral(child_element, "TRANSMISSION-MODE", props.getTransmissionMode())

    def writeSenderComSpec(self, element: ET.Element, com_spec: SenderComSpec):
        representations = com_spec.getCompositeNetworkRepresentations()
        if len(representations) > 0:
            child_element = ET.SubElement(element, "COMPOSITE-NETWORK-REPRESENTATIONS")
            for representation in representations:
                self.writeCompositeNetworkRepresentation(child_element, representation)
        self.setChildElementOptionalRefType(element, "DATA-ELEMENT-REF", com_spec.getDataElementRef())
        self.setChildElementOptionalLiteral(element, "HANDLE-OUT-OF-RANGE", com_spec.getHandleOutOfRange())
        self.setSwDataDefProps(element, "NETWORK-REPRESENTATION", com_spec.getNetworkRepresentation())
        self.writeTransmissionAcknowledgementRequest(element, com_spec.getTransmissionAcknowledge())
        self.writeTransmissionComSpecProps(element, com_spec.getTransmissionProps())
        self.setChildElementOptionalBooleanValue(element, "USES-END-TO-END-PROTECTION", com_spec.getUsesEndToEndProtection())

    def writeNonqueuedSenderComSpec(self, element: ET.Element, com_spec: NonqueuedSenderComSpec):
        child_element = ET.SubElement(element, "NONQUEUED-SENDER-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.writeSenderComSpec(child_element, com_spec)
        self.setDataFilter(child_element, "DATA-FILTER", com_spec.getDataFilter())
        self.setChildValueSpecification(child_element, "INIT-VALUE", com_spec.getInitValue())

    def writeTransformationComSpecProps(self, element: ET.Element, prop: TransformationComSpecProps):
        if prop is not None:
            self.writeARObjectAttributes(element, prop)

    def writeUserDefinedTransformationComSpecProps(self, element: ET.Element, prop: UserDefinedTransformationComSpecProps):
        if prop is not None:
            child_element = ET.SubElement(element, "USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS")
            self.writeTransformationComSpecProps(child_element, prop)

    def writeEndToEndTransformationComSpecProps(self, element: ET.Element, prop: EndToEndTransformationComSpecProps):
        if prop is not None:
            child_element = ET.SubElement(element, "END-TO-END-TRANSFORMATION-COM-SPEC-PROPS")
            self.writeTransformationComSpecProps(child_element, prop)
            self.setChildElementOptionalBooleanValue(child_element, "CLEAR-FROM-VALID-TO-INVALID", prop.getClearFromValidToInvalid())
            self.setChildElementOptionalBooleanValue(child_element, "DISABLE-END-TO-END-CHECK", prop.getDisableEndToEndCheck())
            self.setChildElementOptionalBooleanValue(child_element, "DISABLE-END-TO-END-STATE-MACHINE", prop.getDisableEndToEndStateMachine())
            self.setChildElementOptionalRefType(child_element, "E2E-PROFILE-COMPATIBILITY-PROPS-REF", prop.getE2eProfileCompatibilityPropsRef())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-DELTA-COUNTER", prop.getMaxDeltaCounter())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-ERROR-STATE-INIT", prop.getMaxErrorStateInit())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-ERROR-STATE-INVALID", prop.getMaxErrorStateInvalid())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-ERROR-STATE-VALID", prop.getMaxErrorStateValid())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-NO-NEW-OR-REPEATED-DATA", prop.getMaxNoNewOrRepeatedData())
            self.setChildElementOptionalPositiveInteger(child_element, "MIN-OK-STATE-INIT", prop.getMinOkStateInit())
            self.setChildElementOptionalPositiveInteger(child_element, "MIN-OK-STATE-INVALID", prop.getMinOkStateInvalid())
            self.setChildElementOptionalPositiveInteger(child_element, "MIN-OK-STATE-VALID", prop.getMinOkStateValid())
            self.setChildElementOptionalPositiveInteger(child_element, "SYNC-COUNTER-INIT", prop.getSyncCounterInit())
            self.setChildElementOptionalPositiveInteger(child_element, "WINDOW-SIZE-INIT", prop.getWindowSizeInit())
            self.setChildElementOptionalPositiveInteger(child_element, "WINDOW-SIZE-INVALID", prop.getWindowSizeInvalid())
            self.setChildElementOptionalPositiveInteger(child_element, "WINDOW-SIZE-VALID", prop.getWindowSizeValid())

    def writeServerComSpecTransformationComSpecProps(self, element: ET.Element, com_spec: ServerComSpec):
        self.writeTransformationComSpecPropss(element, com_spec.getTransformationComSpecProps())

    def writeServerComSpec(self, element: ET.Element, com_spec: ServerComSpec):
        child_element = ET.SubElement(element, "SERVER-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.setChildElementOptionalRefType(child_element, "OPERATION-REF", com_spec.getOperationRef())
        self.setChildElementOptionalPositiveInteger(child_element, "QUEUE-LENGTH", com_spec.getQueueLength())
        self.writeServerComSpecTransformationComSpecProps(child_element, com_spec)

    def writeQueuedSenderComSpec(self, element: ET.Element, com_spec: QueuedSenderComSpec):
        child_element = ET.SubElement(element, "QUEUED-SENDER-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.writeSenderComSpec(child_element, com_spec)

    def setModeSwitchedAckRequest(self, element: ET.Element, key: str, request: ModeSwitchedAckRequest):
        if request is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, request)
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT", request.getTimeout())

    def writeModeSwitchSenderComSpec(self, element: ET.Element, com_spec: ModeSwitchSenderComSpec):
        child_element = ET.SubElement(element, "MODE-SWITCH-SENDER-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.setChildElementOptionalRefType(child_element, "MODE-GROUP-REF", com_spec.getModeGroupRef())
        self.setModeSwitchedAckRequest(child_element, "MODE-SWITCHED-ACK", com_spec.getModeSwitchedAck())
        self.setChildElementOptionalNumericalValue(child_element, "QUEUE-LENGTH", com_spec.getQueueLength())

    def writeNvProvideComSpec(self, com_specs_tag: ET.Element, com_spec: NvProvideComSpec):
        if com_spec is not None:
            child_element = ET.SubElement(com_specs_tag, "NV-PROVIDE-COM-SPEC")
            self.writeARObjectAttributes(child_element, com_spec)
            self.setChildValueSpecification(child_element, "RAM-BLOCK-INIT-VALUE", com_spec.getRamBlockInitValue())
            self.setChildValueSpecification(child_element, "ROM-BLOCK-INIT-VALUE", com_spec.getRomBlockInitValue())
            self.setChildElementOptionalRefType(child_element, "VARIABLE-REF", com_spec.getVariableRef())

    def writePPortComSpec(self, com_specs_tag: ET.Element, com_spec: PPortComSpec):
        if isinstance(com_spec, NonqueuedSenderComSpec):
            self.writeNonqueuedSenderComSpec(com_specs_tag, com_spec)
        elif isinstance(com_spec, ServerComSpec):
            self.writeServerComSpec(com_specs_tag, com_spec)
        elif isinstance(com_spec, QueuedSenderComSpec):
            self.writeQueuedSenderComSpec(com_specs_tag, com_spec)
        elif isinstance(com_spec, ModeSwitchSenderComSpec):
            self.writeModeSwitchSenderComSpec(com_specs_tag, com_spec)
        elif isinstance(com_spec, NvProvideComSpec):
            self.writeNvProvideComSpec(com_specs_tag, com_spec)
        elif isinstance(com_spec, ParameterProvideComSpec):
            self.writeParameterProvideComSpec(com_specs_tag, com_spec)
        else:
            self.notImplemented("Unsupported PPortComSpec %s" % type(com_spec))

    def setApplicationCompositeElementInPortInterfaceInstanceRef(self, element: ET.Element, key: str, iref: ApplicationCompositeElementInPortInterfaceInstanceRef):  # noqa E501
        if iref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "ROOT-DATA-PROTOTYPE-REF", iref.getRootDataPrototypeRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF", iref.getTargetDataPrototypeRef())
        return iref

    def writeCompositeNetworkRepresentation(self, element: ET.Element, representation: CompositeNetworkRepresentation):
        if representation is not None:
            self.logger.debug("setCompositeNetworkRepresentation")
            child_element = ET.SubElement(element, "COMPOSITE-NETWORK-REPRESENTATION")
            self.setApplicationCompositeElementInPortInterfaceInstanceRef(child_element, "LEAF-ELEMENT-IREF", representation.getLeafElementIRef())
            self.setSwDataDefProps(child_element, "NETWORK-REPRESENTATION", representation.getNetworkRepresentation())

    def writeReceiverComSpec(self, element: ET.Element, com_spec: ReceiverComSpec):
        representations = com_spec.getCompositeNetworkRepresentations()
        if len(representations) > 0:
            child_element = ET.SubElement(element, "COMPOSITE-NETWORK-REPRESENTATIONS")
            for representation in representations:
                self.writeCompositeNetworkRepresentation(child_element, representation)
        self.setChildElementOptionalRefType(element, "DATA-ELEMENT-REF", com_spec.getDataElementRef())
        self.setSwDataDefProps(element, "NETWORK-REPRESENTATION", com_spec.getNetworkRepresentation())
        self.setChildElementOptionalLiteral(element, "HANDLE-OUT-OF-RANGE", com_spec.getHandleOutOfRange())
        self.setChildElementOptionalLiteral(element, "HANDLE-OUT-OF-RANGE-STATUS", com_spec.getHandleOutOfRangeStatus())
        self.setChildElementOptionalPositiveInteger(element, "MAX-DELTA-COUNTER-INIT", com_spec.getMaxDeltaCounterInit())
        self.setChildElementOptionalPositiveInteger(element, "MAX-NO-NEW-OR-REPEATED-DATA", com_spec.getMaxNoNewOrRepeatedData())
        self.setChildElementOptionalBooleanValue(element, "USES-END-TO-END-PROTECTION", com_spec.getUsesEndToEndProtection())
        self.writeReceptionComSpecProps(element, "RECEPTION-PROPS", com_spec.getReceptionProps())
        self.writeReceiverReplaceWith(element, "REPLACE-WITH", com_spec.getReplaceWith())
        self.setChildElementOptionalPositiveInteger(element, "SYNC-COUNTER-INIT", com_spec.getSyncCounterInit())
        props = com_spec.getTransformationComSpecProps()
        if len(props) > 0:
            props_tag = ET.SubElement(element, "TRANSFORMATION-COM-SPEC-PROPSS")
            for prop in props:
                if isinstance(prop, EndToEndTransformationComSpecProps):
                    child = ET.SubElement(props_tag, "END-TO-END-TRANSFORMATION-COM-SPEC-PROPS")
                    self.writeTransformationComSpecProps(child, prop)
                elif isinstance(prop, UserDefinedTransformationComSpecProps):
                    self.writeUserDefinedTransformationComSpecProps(props_tag, prop)
                else:
                    self.notImplemented("Unsupported TransformationComSpecProps %s" % type(prop))

    def writeReceptionComSpecProps(self, element: ET.Element, key: str, props: ReceptionComSpecProps):
        if props is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, props)
            self.setChildElementOptionalTimeValue(child_element, "DATA-UPDATE-PERIOD", props.getDataUpdatePeriod())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT", props.getTimeout())

    def writeReceiverReplaceWith(self, element: ET.Element, key: str, access: VariableAccess):
        if access is not None:
            child_element = ET.SubElement(element, key)
            self.writeIdentifiable(child_element, access)
            self.setAutosarVariableRef(child_element, "ACCESSED-VARIABLE", access.getAccessedVariableRef())
            self.setChildElementOptionalLiteral(child_element, "SCOPE", access.getScope())

    def setSwValues(self, element: ET.Element, key: str, sw_values: SwValues):
        if sw_values is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, sw_values)
            for vf in sw_values.getVfs():
                self.setChildElementOptionalFloatValue(child_element, "VF", vf)
            self.setChildElementOptionalLiteral(child_element, "VT", sw_values.getVt())
            for v in sw_values.getVs():
                self.setChildElementOptionalFloatValue(child_element, "V", v)
            self.setValueGroup(child_element, "VG", sw_values.getVg())
            for vtf in sw_values.getVtfs():
                self.writeNumericalOrText(child_element, "VTF", vtf)

    def setValueGroup(self, element: ET.Element, key: str, value_group: ValueGroup):
        if value_group is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, value_group)
            self.setMultiLongName(child_element, "LABEL", value_group.getLabel())
            contents = value_group.getVgContents()
            if contents is not None:
                for vf in contents.getVfs():
                    self.setChildElementOptionalFloatValue(child_element, "VF", vf)
                self.setChildElementOptionalLiteral(child_element, "VT", contents.getVt())
                for v in contents.getVs():
                    self.setChildElementOptionalFloatValue(child_element, "V", v)
                for vtf in contents.getVtfs():
                    self.writeNumericalOrText(child_element, "VTF", vtf)

    def setValueList(self, element: ET.Element, key: str, value_list: ValueList):
        if value_list is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, value_list)
            for vf in value_list.getVfs():
                vf_element = ET.SubElement(child_element, "VF")
                self.setChildElementOptionalNumerical(vf_element, "V", vf)
            self.setChildElementOptionalNumerical(child_element, "V", value_list.v)

    def writeSwValueCont(self, element: ET.Element, cont: SwValueCont):
        if cont is not None:
            child_element = ET.SubElement(element, "SW-VALUE-CONT")
            self.writeARObjectAttributes(child_element, cont)
            self.setChildElementOptionalRefType(child_element, "UNIT-REF", cont.unitRef)
            self.setValueList(child_element, "SW-ARRAYSIZE", cont.swArraysize)
            self.setSwValues(child_element, "SW-VALUES-PHYS", cont.swValuesPhys)

    def writeValueSpecification(self, element: ET.Element, value_spec: ValueSpecification):
        if value_spec is not None:
            self.writeARObjectAttributes(element, value_spec)
            self.setChildElementOptionalLiteral(element, "SHORT-LABEL", value_spec.getShortLabel())

    def writeTextValueSpecification(self, element: ET.Element, value_spec: TextValueSpecification):
        if value_spec is not None:
            value_spec_tag = ET.SubElement(element, "TEXT-VALUE-SPECIFICATION")
            self.writeValueSpecification(value_spec_tag, value_spec)
            self.setChildElementOptionalLiteral(value_spec_tag, "VALUE", value_spec.getValue())

    def writeNumericalValueSpecification(self, element: ET.Element, value_spec: NumericalValueSpecification):
        if value_spec is not None:
            value_spec_tag = ET.SubElement(element, "NUMERICAL-VALUE-SPECIFICATION")
            self.writeValueSpecification(value_spec_tag, value_spec)
            self.setChildElementOptionalNumericalValue(value_spec_tag, "VALUE", value_spec.getValue())

    def writeArrayValueSpecification(self, element: ET.Element, value_spec: ArrayValueSpecification):
        value_spec_tag = ET.SubElement(element, "ARRAY-VALUE-SPECIFICATION")
        self.writeValueSpecification(value_spec_tag, value_spec)
        sub_elements = value_spec.getElements()
        if len(sub_elements) > 0:
            elements_tag = ET.SubElement(value_spec_tag, "ELEMENTS")
            for sub_element in sub_elements:
                if isinstance(sub_element, NumericalValueSpecification):
                    self.writeNumericalValueSpecification(elements_tag, sub_element)
                elif isinstance(sub_element, ApplicationValueSpecification):
                    self.writeApplicationValueSpecification(elements_tag, sub_element)
                elif isinstance(sub_element, ApplicationRuleBasedValueSpecification):
                    self.writeApplicationRuleBasedValueSpecification(elements_tag, sub_element)
                elif isinstance(sub_element, CompositeRuleBasedValueSpecification):
                    self.writeCompositeRuleBasedValueSpecification(elements_tag, sub_element)
                elif isinstance(sub_element, NumericalRuleBasedValueSpecification):
                    self.writeNumericalRuleBasedValueSpecification(elements_tag, sub_element)
                elif isinstance(sub_element, TextValueSpecification):
                    self.writeTextValueSpecification(elements_tag, sub_element)
                elif isinstance(sub_element, ArrayValueSpecification):
                    self.writeArrayValueSpecification(elements_tag, sub_element)
                elif isinstance(sub_element, RecordValueSpecification):
                    self.writeRecordValueSpecification(elements_tag, sub_element)
                elif isinstance(sub_element, ReferenceValueSpecification):
                    self.writeReferenceValueSpecification(elements_tag, sub_element)
                elif isinstance(sub_element, NotAvailableValueSpecification):
                    self.writeNotAvailableValueSpecification(elements_tag, sub_element)
                else:
                    self.notImplemented("Unsupported element type of <%s> of ArrayValueSpecification" % type(sub_element))

    def setConstantReference(self, element: ET.Element, value_spec: ConstantReference):
        value_spec_tag = ET.SubElement(element, "CONSTANT-REFERENCE")
        self.writeValueSpecification(value_spec_tag, value_spec)
        self.setChildElementOptionalRefType(value_spec_tag, "CONSTANT-REF", value_spec.getConstantRef())

    def writeReferenceValueSpecification(self, element: ET.Element, value_spec: ReferenceValueSpecification):
        if value_spec is not None:
            value_spec_tag = ET.SubElement(element, "REFERENCE-VALUE-SPECIFICATION")
            self.writeValueSpecification(value_spec_tag, value_spec)
            self.setChildElementOptionalRefType(value_spec_tag, "REFERENCE-VALUE-REF", value_spec.getReferenceValueRef())

    def writeNotAvailableValueSpecification(self, element: ET.Element, value_spec: NotAvailableValueSpecification):
        if value_spec is not None:
            value_spec_tag = ET.SubElement(element, "NOT-AVAILABLE-VALUE-SPECIFICATION")
            self.writeValueSpecification(value_spec_tag, value_spec)
            self.setChildElementOptionalPositiveInteger(value_spec_tag, "DEFAULT-PATTERN", value_spec.getDefaultPattern())

    def writeNumericalRuleBasedValueSpecification(self, element: ET.Element, value_spec: NumericalRuleBasedValueSpecification):
        if value_spec is not None:
            value_spec_tag = ET.SubElement(element, "NUMERICAL-RULE-BASED-VALUE-SPECIFICATION")
            self.writeValueSpecification(value_spec_tag, value_spec)
            self.writeRuleBasedValueSpecification(value_spec_tag, "RULE-BASED-VALUES", value_spec.getRuleBasedValues())

    def writeConstantSpecificationMapping(self, element: ET.Element, mapping: ConstantSpecificationMapping):
        if mapping is not None:
            mapping_tag = ET.SubElement(element, "CONSTANT-SPECIFICATION-MAPPING")
            self.writeARObjectAttributes(mapping_tag, mapping)
            self.setChildElementOptionalRefType(mapping_tag, "APPL-CONSTANT-REF", mapping.getApplConstantRef())
            self.setChildElementOptionalRefType(mapping_tag, "IMPL-CONSTANT-REF", mapping.getImplConstantRef())

    def setChildValueSpecification(self, element: ET.Element, key: str, value_spec: ValueSpecification):
        if value_spec is not None:
            child_element = ET.SubElement(element, key)
            if isinstance(value_spec, ApplicationValueSpecification):
                self.writeApplicationValueSpecification(child_element, value_spec)
            elif isinstance(value_spec, ApplicationRuleBasedValueSpecification):
                self.writeApplicationRuleBasedValueSpecification(child_element, value_spec)
            elif isinstance(value_spec, CompositeRuleBasedValueSpecification):
                self.writeCompositeRuleBasedValueSpecification(child_element, value_spec)
            elif isinstance(value_spec, NumericalRuleBasedValueSpecification):
                self.writeNumericalRuleBasedValueSpecification(child_element, value_spec)
            elif isinstance(value_spec, TextValueSpecification):
                self.writeTextValueSpecification(child_element, value_spec)
            elif isinstance(value_spec, ConstantReference):
                self.setConstantReference(child_element, value_spec)
            elif isinstance(value_spec, ReferenceValueSpecification):
                self.writeReferenceValueSpecification(child_element, value_spec)
            elif isinstance(value_spec, NotAvailableValueSpecification):
                self.writeNotAvailableValueSpecification(child_element, value_spec)
            elif isinstance(value_spec, NumericalValueSpecification):
                self.writeNumericalValueSpecification(child_element, value_spec)
            elif isinstance(value_spec, ArrayValueSpecification):
                self.writeArrayValueSpecification(child_element, value_spec)
            elif isinstance(value_spec, RecordValueSpecification):
                self.writeRecordValueSpecification(child_element, value_spec)
            else:
                self.notImplemented("Unsupported ValueSpecification %s" % type(value_spec))

    def writeNonqueuedReceiverComSpec(self, element: ET.Element, com_spec: NonqueuedReceiverComSpec):
        child_element = ET.SubElement(element, "NONQUEUED-RECEIVER-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.writeReceiverComSpec(child_element, com_spec)
        self.setChildElementOptionalFloatValue(child_element, "ALIVE-TIMEOUT", com_spec.getAliveTimeout())
        self.setChildElementOptionalBooleanValue(child_element, "ENABLE-UPDATE", com_spec.getEnableUpdate())
        self.setDataFilter(child_element, "FILTER", com_spec.getFilter())
        self.setChildElementOptionalBooleanValue(child_element, "HANDLE-DATA-STATUS", com_spec.getHandleDataStatus())
        self.setChildElementOptionalBooleanValue(child_element, "HANDLE-NEVER-RECEIVED", com_spec.getHandleNeverReceived())
        self.setChildElementOptionalLiteral(child_element, "HANDLE-TIMEOUT-TYPE", com_spec.getHandleTimeoutType())

        self.setChildValueSpecification(child_element, "INIT-VALUE", com_spec.getInitValue())
        self.setChildValueSpecification(child_element, "TIMEOUT-SUBSTITUTION-VALUE", com_spec.getTimeoutSubstitutionValue())

    def writeQueuedReceiverComSpec(self, element: ET.Element, com_spec: QueuedReceiverComSpec):
        child_element = ET.SubElement(element, "QUEUED-RECEIVER-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.writeReceiverComSpec(child_element, com_spec)
        self.setChildElementOptionalNumericalValue(child_element, "QUEUE-LENGTH", com_spec.queueLength)

    def writeClientComSpec(self, element: ET.Element, com_spec: ClientComSpec):
        self.logger.debug("writeClientComSpec")
        child_element = ET.SubElement(element, "CLIENT-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.setChildElementOptionalTimeValue(child_element, "END-TO-END-CALL-RESPONSE-TIMEOUT", com_spec.getEndToEndCallResponseTimeout())
        self.setChildElementOptionalRefType(child_element, "OPERATION-REF", com_spec.getOperationRef())
        self.writeTransformationComSpecPropss(child_element, com_spec.getTransformationComSpecProps())

    def writeTransformationComSpecPropss(self, element: ET.Element, props):
        if len(props) > 0:
            child_element = ET.SubElement(element, "TRANSFORMATION-COM-SPEC-PROPSS")
            for prop in props:
                if isinstance(prop, UserDefinedTransformationComSpecProps):
                    self.writeUserDefinedTransformationComSpecProps(child_element, prop)
                elif isinstance(prop, EndToEndTransformationComSpecProps):
                    self.writeEndToEndTransformationComSpecProps(child_element, prop)
                else:
                    self.notImplemented("Unsupported TransformationComSpecProps %s" % type(prop))

    def writeParameterProvideComSpec(self, element: ET.Element, com_spec: ParameterProvideComSpec):
        self.logger.debug("writeParameterProvideComSpec")
        child_element = ET.SubElement(element, "PARAMETER-PROVIDE-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.setChildValueSpecification(child_element, "INIT-VALUE", com_spec.getInitValue())
        self.setChildElementOptionalRefType(child_element, "PARAMETER-REF", com_spec.getParameterRef())

    def writeParameterRequireComSpec(self, element: ET.Element, com_spec: ParameterRequireComSpec):
        self.logger.debug("writeParameterRequireComSpec")
        child_element = ET.SubElement(element, "PARAMETER-REQUIRE-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.setChildValueSpecification(child_element, "INIT-VALUE", com_spec.getInitValue())
        self.setChildElementOptionalRefType(child_element, "PARAMETER-REF", com_spec.getParameterRef())

    def writeNvRequireComSpec(self, element: ET.Element, com_spec: NvRequireComSpec):
        self.logger.debug("writeNvRequireComSpec")
        child_element = ET.SubElement(element, "NV-REQUIRE-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.setChildValueSpecification(child_element, "INIT-VALUE", com_spec.getInitValue())
        self.setChildElementOptionalRefType(child_element, "VARIABLE-REF", com_spec.getVariableRef())

    def setModeSwitchReceiverComSpec(self, element: ET.Element, com_spec: ModeSwitchReceiverComSpec):
        self.logger.debug("writeModeSwitchReceiverComSpec")
        child_element = ET.SubElement(element, "MODE-SWITCH-RECEIVER-COM-SPEC")
        self.writeARObjectAttributes(child_element, com_spec)
        self.setChildElementOptionalBooleanValue(child_element, "ENHANCED-MODE-API", com_spec.getEnhancedModeApi())
        self.setChildElementOptionalRefType(child_element, "MODE-GROUP-REF", com_spec.getModeGroupRef())
        self.setChildElementOptionalBooleanValue(child_element, "SUPPORTS-ASYNCHRONOUS-MODE-SWITCH", com_spec.getSupportsAsynchronousModeSwitch())

    def writeRPortComSpec(self, element: ET.Element, com_spec: RPortComSpec):
        if isinstance(com_spec, NonqueuedReceiverComSpec):
            self.writeNonqueuedReceiverComSpec(element, com_spec)
        elif isinstance(com_spec, QueuedReceiverComSpec):
            self.writeQueuedReceiverComSpec(element, com_spec)
        elif isinstance(com_spec, ClientComSpec):
            self.writeClientComSpec(element, com_spec)
        elif isinstance(com_spec, ModeSwitchReceiverComSpec):
            self.setModeSwitchReceiverComSpec(element, com_spec)
        elif isinstance(com_spec, ParameterRequireComSpec):
            self.writeParameterRequireComSpec(element, com_spec)
        elif isinstance(com_spec, NvRequireComSpec):
            self.writeNvRequireComSpec(element, com_spec)
        else:
            raise ValueError("Unsupported RPortComSpec %s" % type(com_spec))

    def setAbstractProvidedPortPrototype(self, element: ET.Element, prototype: AbstractProvidedPortPrototype):
        com_specs = prototype.getProvidedComSpecs()
        if len(com_specs):
            com_specs_tag = ET.SubElement(element, "PROVIDED-COM-SPECS")
            for com_spec in com_specs:
                self.writePPortComSpec(com_specs_tag, com_spec)

    def writePPortPrototype(self, ports_tag: ET.Element, prototype: PPortPrototype):
        prototype_tag = ET.SubElement(ports_tag, "P-PORT-PROTOTYPE")

        self.writeIdentifiable(prototype_tag, prototype)
        self.logger.debug("write PPortPrototype %s" % prototype.getShortName())
        self.setAbstractProvidedPortPrototype(prototype_tag, prototype)
        self.setChildElementOptionalRefType(prototype_tag, "PROVIDED-INTERFACE-TREF", prototype.getProvidedInterfaceTRef())
        self.setPortPrototype(prototype_tag, prototype)

    def setAbstractRequiredPortPrototype(self, element: ET.Element, prototype: AbstractRequiredPortPrototype):
        com_specs = prototype.getRequiredComSpecs()
        if len(com_specs) > 0:
            com_specs_tag = ET.SubElement(element, "REQUIRED-COM-SPECS")
            for com_spec in com_specs:
                self.writeRPortComSpec(com_specs_tag, com_spec)

    def writeRPortPrototype(self, ports_tag: ET.Element, prototype: RPortPrototype):
        self.logger.debug("write RPortPrototype %s" % prototype.getShortName())
        prototype_tag = ET.SubElement(ports_tag, "R-PORT-PROTOTYPE")
        self.writeIdentifiable(prototype_tag, prototype)
        self.setAbstractRequiredPortPrototype(prototype_tag, prototype)
        self.setChildElementOptionalRefType(prototype_tag, "REQUIRED-INTERFACE-TREF", prototype.getRequiredInterfaceTRef())
        self.setPortPrototype(prototype_tag, prototype)

    def writePRPortPrototype(self, ports_tag: ET.Element, prototype: PRPortPrototype):
        self.logger.debug("write PRPortPrototype %s" % prototype.getShortName())
        prototype_tag = ET.SubElement(ports_tag, "PR-PORT-PROTOTYPE")
        self.writeIdentifiable(prototype_tag, prototype)
        self.setAbstractProvidedPortPrototype(prototype_tag, prototype)
        self.setAbstractRequiredPortPrototype(prototype_tag, prototype)
        self.setChildElementOptionalRefType(prototype_tag, "PROVIDED-REQUIRED-INTERFACE-TREF", prototype.getProvidedRequiredInterface())
        self.setPortPrototype(prototype_tag, prototype)

    def setPortPrototype(self, element: ET.Element, prototype: PortPrototype):
        client_server_annotations = prototype.getClientServerAnnotations()
        if len(client_server_annotations) > 0:
            annotations_tag = ET.SubElement(element, "CLIENT-SERVER-ANNOTATIONS")
            for annotation in client_server_annotations:
                self.writeClientServerAnnotation(annotations_tag, annotation)
        delegated_port_annotation = prototype.getDelegatedPortAnnotation()
        if delegated_port_annotation is not None:
            self.writeDelegatedPortAnnotation(element, delegated_port_annotation)
        io_hw_annotations = prototype.getIoHwAbstractionServerAnnotations()
        if len(io_hw_annotations) > 0:
            annotations_tag = ET.SubElement(element, "IO-HW-ABSTRACTION-SERVER-ANNOTATIONS")
            for annotation in io_hw_annotations:
                self.writeIoHwAbstractionServerAnnotation(annotations_tag, annotation)
        mode_annotations = prototype.getModePortAnnotations()
        if len(mode_annotations) > 0:
            annotations_tag = ET.SubElement(element, "MODE-PORT-ANNOTATIONS")
            for annotation in mode_annotations:
                self.writeModePortAnnotation(annotations_tag, annotation)
        nv_data_annotations = prototype.getNvDataPortAnnotations()
        if len(nv_data_annotations) > 0:
            annotations_tag = ET.SubElement(element, "NV-DATA-PORT-ANNOTATIONS")
            for annotation in nv_data_annotations:
                self.writeNvDataPortAnnotation(annotations_tag, annotation)
        parameter_annotations = prototype.getParameterPortAnnotations()
        if len(parameter_annotations) > 0:
            annotations_tag = ET.SubElement(element, "PARAMETER-PORT-ANNOTATIONS")
            for annotation in parameter_annotations:
                self.writeParameterPortAnnotation(annotations_tag, annotation)
        sender_receiver_annotations = prototype.getSenderReceiverAnnotations()
        if len(sender_receiver_annotations) > 0:
            annotations_tag = ET.SubElement(element, "SENDER-RECEIVER-ANNOTATIONS")
            for annotation in sender_receiver_annotations:
                self.writeSenderReceiverAnnotation(annotations_tag, annotation)
        trigger_annotations = prototype.getTriggerPortAnnotations()
        if len(trigger_annotations) > 0:
            annotations_tag = ET.SubElement(element, "TRIGGER-PORT-ANNOTATIONS")
            for annotation in trigger_annotations:
                self.writeTriggerPortAnnotation(annotations_tag, annotation)

    def writeClientServerAnnotation(self, element: ET.Element, annotation: ClientServerAnnotation):
        child_element = ET.SubElement(element, "CLIENT-SERVER-ANNOTATION")
        self.setChildElementOptionalRefType(child_element, "OPERATION-REF", annotation.getOperationRef())

    def writeDelegatedPortAnnotation(self, element: ET.Element, annotation: DelegatedPortAnnotation):
        child_element = ET.SubElement(element, "DELEGATED-PORT-ANNOTATION")
        self.setChildElementOptionalLiteral(child_element, "SIGNAL-FAN", annotation.getSignalFan())

    def writeIoHwAbstractionServerAnnotation(self, element: ET.Element, annotation: IoHwAbstractionServerAnnotation):
        child_element = ET.SubElement(element, "IO-HW-ABSTRACTION-SERVER-ANNOTATION")
        self.setChildElementOptionalLiteral(child_element, "FILTERING-DEBOUNCING", annotation.getFilteringDebouncing())
        self.setChildElementOptionalLiteral(child_element, "PULSE-TEST", annotation.getPulseTest())
        self.setChildElementOptionalRefType(child_element, "TRIGGER-REF", annotation.getTriggerRef())

    def writeModePortAnnotation(self, element: ET.Element, annotation: ModePortAnnotation):
        child_element = ET.SubElement(element, "MODE-PORT-ANNOTATION")
        self.setChildElementOptionalRefType(child_element, "MODE-GROUP-REF", annotation.getModeGroupRef())

    def writeNvDataPortAnnotation(self, element: ET.Element, annotation: NvDataPortAnnotation):
        child_element = ET.SubElement(element, "NV-DATA-PORT-ANNOTATION")
        self.setChildElementOptionalRefType(child_element, "VARIABLE-REF", annotation.getVariableRef())

    def writeParameterPortAnnotation(self, element: ET.Element, annotation: ParameterPortAnnotation):
        child_element = ET.SubElement(element, "PARAMETER-PORT-ANNOTATION")
        self.setChildElementOptionalRefType(child_element, "PARAMETER-REF", annotation.getParameterRef())

    def writeSenderReceiverAnnotation(self, element: ET.Element, annotation: SenderReceiverAnnotation):
        child_element = ET.SubElement(element, "SENDER-RECEIVER-ANNOTATION")
        self.setChildElementOptionalBooleanValue(child_element, "COMPUTED", annotation.getComputed())
        self.setChildElementOptionalRefType(child_element, "DATA-ELEMENT-REF", annotation.getDataElementRef())
        self.setChildElementOptionalLiteral(child_element, "LIMIT-KIND", annotation.getLimitKind())
        self.setChildElementOptionalLiteral(child_element, "PROCESSING-KIND", annotation.getProcessingKind())

    def writeTriggerPortAnnotation(self, element: ET.Element, annotation: TriggerPortAnnotation):
        child_element = ET.SubElement(element, "TRIGGER-PORT-ANNOTATION")
        self.setChildElementOptionalRefType(child_element, "TRIGGER-REF", annotation.getTriggerRef())

    def writeSwComponentTypePorts(self, element: ET.Element, sw_component: SwComponentType):
        ports = sw_component.getPorts()
        if len(ports) > 0:
            child_element = ET.SubElement(element, "PORTS")
            for port in ports:
                if isinstance(port, PPortPrototype):
                    self.writePPortPrototype(child_element, port)
                elif isinstance(port, RPortPrototype):
                    self.writeRPortPrototype(child_element, port)
                elif isinstance(port, PRPortPrototype):
                    self.writePRPortPrototype(child_element, port)
                else:
                    self.notImplemented("Unsupported Port Prototype <%s>" % type(port))

    def writeInnerGroupIRef(self, element: ET.Element, inner_group_iref: InnerPortGroupInCompositionInstanceRef):
        child_element = ET.SubElement(element, "INNER-GROUP-IREF")
        # self.setChildElementOptionalRefType(child_element, "CONTEXT-REF", inner_group_iref.contextRef)
        self.setChildElementOptionalRefType(child_element, "TARGET-REF", inner_group_iref.getTargetRef())

    def writePortGroupInnerGroupIRefs(self, element: ET.Element, parent: PortGroup):
        irefs = parent.getInnerGroupIRefs()
        if len(irefs) > 0:
            child_element = ET.SubElement(element, "INNER-GROUP-IREFS")
            for iref in irefs:
                self.writeInnerGroupIRef(child_element, iref)

    def writePortGroupOuterPortRefs(self, element: ET.Element, parent: PortGroup):
        refs = parent.getOuterPortRefs()
        if len(refs) > 0:
            outer_ports_element = ET.SubElement(element, "OUTER-PORTS")
            for ref in refs:
                child_element = ET.SubElement(outer_ports_element, "PORT-PROTOTYPE-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF", ref)

    def writePortGroup(self, element: ET.Element, port_group: PortGroup):
        self.logger.debug("writePortGroup %s" % port_group.getShortName())
        child_element = ET.SubElement(element, "PORT-GROUP")
        self.writeIdentifiable(child_element, port_group)
        self.writePortGroupInnerGroupIRefs(child_element, port_group)
        self.writePortGroupOuterPortRefs(child_element, port_group)

    def writeSwComponentTypePortGroups(self, element: ET.Element, parent: SwComponentType):
        port_groups = parent.getPortGroups()
        if len(port_groups) > 0:
            child_element = ET.SubElement(element, "PORT-GROUPS")
            for port_group in port_groups:
                self.writePortGroup(child_element, port_group)

    def writeSwComponentTypeSwcMappingConstraints(self, element: ET.Element, parent: SwComponentType):
        refs = parent.getSwcMappingConstraintsRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "SWC-MAPPING-CONSTRAINT-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "SWC-MAPPING-CONSTRAINT-REF", ref)

    def writeSwComponentDocumentationElement(self, child_element: ET.Element, documentation):
        predefined_chapters = [
            (documentation.getSwFeatureDef(), "SW-FEATURE-DEF"),
            (documentation.getSwFeatureDesc(), "SW-FEATURE-DESC"),
            (documentation.getSwTestDesc(), "SW-TEST-DESC"),
            (documentation.getSwCalibrationNotes(), "SW-CALIBRATION-NOTES"),
            (documentation.getSwMaintenanceNotes(), "SW-MAINTENANCE-NOTES"),
            (documentation.getSwDiagnosticsNotes(), "SW-DIAGNOSTICS-NOTES"),
            (documentation.getSwCarbDoc(), "SW-CARB-DOC"),
        ]
        for chapter, tag_name in predefined_chapters:
            if chapter is not None:
                self.writeChapter(child_element, chapter, tag_name)
        for chapter in documentation.getChapters():
            self.writeChapter(child_element, chapter, "CHAPTER")

    def writeSwComponentTypeSwComponentDocumentation(self, element: ET.Element, parent: SwComponentType):
        documentation = parent.getSwComponentDocumentation()
        if documentation is None:
            return
        child_element = ET.SubElement(element, "SW-COMPONENT-DOCUMENTATION")
        self.writeSwComponentDocumentationElement(child_element, documentation)

    def writeChapter(self, element: ET.Element, chapter: Chapter, tag_name: str):
        child_element = ET.SubElement(element, tag_name)
        self.writeIdentifiable(child_element, chapter)
        if chapter.getHelpEntry() is not None:
            child_element.set("HELP-ENTRY", chapter.getHelpEntry().getValue())
        chapter_model = chapter.getChapterModel()
        if chapter_model is not None:
            self.writeChapterModel(child_element, chapter_model)

    def writeChapterModel(self, element: ET.Element, chapter_model: ChapterModel):
        child_element = ET.SubElement(element, "CHAPTER-MODEL")
        chapter_content = chapter_model.getChapterContent()
        if chapter_content is not None:
            self.writeChapterContent(child_element, chapter_content)
        topic1 = chapter_model.getTopic1()
        if topic1 is not None:
            for topic in topic1.getTopic1s():
                self.writeTopic1(child_element, topic)
            if topic1.getMsrQueryTopic1() is not None:
                self.writeMsrQueryTopic1(child_element, topic1.getMsrQueryTopic1())
        chapter = chapter_model.getChapter()
        if chapter is not None:
            for chapter_item in chapter.getChapters():
                self.writeChapter(child_element, chapter_item, "CHAPTER")
            if chapter.getMsrQueryChapter() is not None:
                self.writeMsrQueryChapter(child_element, chapter.getMsrQueryChapter())

    def writePredefinedChapter(self, element: ET.Element, predefined: Optional[PredefinedChapter]):
        if predefined is not None:
            chapter_model = predefined.getChapterModel()
            if chapter_model is not None:
                self.writeChapterModel(element, chapter_model)
        return predefined

    def writeDocumentationContext(self, element: ET.Element, context: DocumentationContext):
        self.writeMultilanguageReferrable(element, context)
        feature_iref = context.getFeatureIRef()
        if feature_iref is not None:
            self.setAnyInstanceRef(element, "FEATURE-IREF", feature_iref)
        self.setChildElementOptionalRefType(element, "IDENTIFIABLE-REF", context.getIdentifiableRef())

    def writeDocumentation(self, element: ET.Element, documentation: Documentation):
        child_element = ET.SubElement(element, "DOCUMENTATION")
        self.writeARElement(child_element, documentation)
        contexts = documentation.getContexts()
        if len(contexts) > 0:
            contexts_tag = ET.SubElement(child_element, "CONTEXTS")
            for context in contexts:
                context_el = ET.SubElement(contexts_tag, "DOCUMENTATION-CONTEXT")
                self.writeDocumentationContext(context_el, context)
        documentation_content = documentation.getDocumentationContent()
        if documentation_content is not None:
            content_el = ET.SubElement(child_element, "DOCUMENTATION-CONTENT")
            self.writePredefinedChapter(content_el, documentation_content)
        return documentation

    def writeChapterContent(self, element: ET.Element, chapter_content: ChapterContent):
        child_element = ET.SubElement(element, "CHAPTER-CONTENT")
        self.writeTopicContentOrMsrQuery(child_element, chapter_content.getTopicContent())

    def writeTopicContentOrMsrQuery(self, element: ET.Element, topic_content_or_msr_query: TopicContentOrMsrQuery):
        if topic_content_or_msr_query is None:
            return
        if topic_content_or_msr_query.getMsrQueryP1() is not None:
            self.writeMsrQueryP1(element, topic_content_or_msr_query.getMsrQueryP1())
        if topic_content_or_msr_query.getTopicContent() is not None:
            self.writeTopicContent(element, topic_content_or_msr_query.getTopicContent())

    def writeMsrQueryP1(self, element: ET.Element, msr_query_p1: MsrQueryP1):
        child_element = ET.SubElement(element, "MSR-QUERY-P1")
        self.writeARObjectAttributes(child_element, msr_query_p1)

    def writeTopicContent(self, element: ET.Element, topic_content: TopicContent):
        child_element = ET.SubElement(element, "TOPIC-CONTENT")
        self.writeARObjectAttributes(child_element, topic_content)
        self.writeDocumentationBlock(child_element, "DOCUMENTATION-BLOCK", topic_content.getBlockLevelContent())

    def writeTopic1(self, element: ET.Element, topic1: Topic1):
        child_element = ET.SubElement(element, "TOPIC-1")
        self.writeIdentifiable(child_element, topic1)
        if topic1.getHelpEntry() is not None:
            child_element.set("HELP-ENTRY", topic1.getHelpEntry().getValue())
        self.writeTopicContentOrMsrQuery(child_element, topic1.getTopicContent())

    def writeMsrQueryTopic1(self, element: ET.Element, msr_query_topic1: MsrQueryTopic1):
        child_element = ET.SubElement(element, "MSR-QUERY-TOPIC-1")
        self.writeARObjectAttributes(child_element, msr_query_topic1)
        if msr_query_topic1.getMsrQueryProps() is not None:
            self.setMsrQueryProps(child_element, msr_query_topic1.getMsrQueryProps())

    def writeMsrQueryChapter(self, element: ET.Element, msr_query_chapter: MsrQueryChapter):
        child_element = ET.SubElement(element, "MSR-QUERY-CHAPTER")
        self.writeARObjectAttributes(child_element, msr_query_chapter)
        if msr_query_chapter.getMsrQueryProps() is not None:
            self.setMsrQueryProps(child_element, msr_query_chapter.getMsrQueryProps())

    def writeSwComponentTypeUnitGroups(self, element: ET.Element, parent: SwComponentType):
        refs = parent.getUnitGroupRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "UNIT-GROUP-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "UNIT-GROUP-REF", ref)

    def writeSwComponentTypeConsistencyNeeds(self, element: ET.Element, parent: SwComponentType):
        consistency_needs_list = parent.getConsistencyNeeds()
        if len(consistency_needs_list) > 0:
            child_element = ET.SubElement(element, "CONSISTENCY-NEEDSS")
            for consistency_needs in consistency_needs_list:
                self.writeConsistencyNeeds(child_element, consistency_needs)

    def writeSwComponentType(self, element: ET.Element, sw_component: SwComponentType):
        self.writeIdentifiable(element, sw_component)
        self.writeSwComponentTypeSwComponentDocumentation(element, sw_component)
        self.writeSwComponentTypeConsistencyNeeds(element, sw_component)
        self.writeSwComponentTypePorts(element, sw_component)
        self.writeSwComponentTypePortGroups(element, sw_component)
        self.writeSwComponentTypeSwcMappingConstraints(element, sw_component)
        self.writeSwComponentTypeUnitGroups(element, sw_component)

    def writeSwComponentPrototype(self, element: ET.Element, prototype: SwComponentPrototype):
        prototype_tag = ET.SubElement(element, "SW-COMPONENT-PROTOTYPE")
        self.writeIdentifiable(prototype_tag, prototype)
        self.setChildElementOptionalRefType(prototype_tag, "TYPE-TREF", prototype.getTypeTRef())

    def writeCompositionSwComponentTypeComponents(self, element: ET.Element, sw_component: CompositionSwComponentType):
        components = sw_component.getComponents()
        if len(components) > 0:
            components_tag = ET.SubElement(element, "COMPONENTS")
            for component in components:
                if isinstance(component, SwComponentPrototype):
                    self.writeSwComponentPrototype(components_tag, component)
                else:
                    self.notImplemented("Unsupported Component <%s>" % type(component))

    def writeAssemblySwConnector(self, element: ET.Element, sw_connector: AssemblySwConnector):
        child_element = ET.SubElement(element, "ASSEMBLY-SW-CONNECTOR")
        self.writeSwConnector(child_element, sw_connector)

        if sw_connector.getProviderIRef() is not None:
            provider_iref_tag = ET.SubElement(child_element, "PROVIDER-IREF")
            provider_iref = sw_connector.getProviderIRef()
            self.writeARObjectAttributes(provider_iref_tag, provider_iref)
            self.setChildElementOptionalRefType(provider_iref_tag, "CONTEXT-COMPONENT-REF", provider_iref.getContextComponentRef())
            self.setChildElementOptionalRefType(provider_iref_tag, "TARGET-P-PORT-REF", provider_iref.getTargetPPortRef())

        if sw_connector.getRequesterIRef() is not None:
            requester_iref_tag = ET.SubElement(child_element, "REQUESTER-IREF")
            requester_iref = sw_connector.getRequesterIRef()
            self.writeARObjectAttributes(requester_iref_tag, requester_iref)
            self.setChildElementOptionalRefType(requester_iref_tag, "CONTEXT-COMPONENT-REF", requester_iref.getContextComponentRef())
            self.setChildElementOptionalRefType(requester_iref_tag, "TARGET-R-PORT-REF", requester_iref.getTargetRPortRef())

    def writeDelegationSwConnector(self, element: ET.Element, sw_connector: DelegationSwConnector):
        connector_tag = ET.SubElement(element, "DELEGATION-SW-CONNECTOR")
        self.writeIdentifiable(connector_tag, sw_connector)

        if sw_connector.getInnerPortIRref() is not None:
            inner_port_iref_tag = ET.SubElement(connector_tag, "INNER-PORT-IREF")
            inner_port_iref = sw_connector.getInnerPortIRref()
            if isinstance(inner_port_iref, PPortInCompositionInstanceRef):
                instance_ref_tag = ET.SubElement(inner_port_iref_tag, "P-PORT-IN-COMPOSITION-INSTANCE-REF")
                self.setChildElementOptionalRefType(instance_ref_tag, "CONTEXT-COMPONENT-REF", inner_port_iref.getContextComponentRef())
                self.setChildElementOptionalRefType(instance_ref_tag, "TARGET-P-PORT-REF", inner_port_iref.getTargetPPortRef())
            elif isinstance(inner_port_iref, RPortInCompositionInstanceRef):
                instance_ref_tag = ET.SubElement(inner_port_iref_tag, "R-PORT-IN-COMPOSITION-INSTANCE-REF")
                self.setChildElementOptionalRefType(instance_ref_tag, "CONTEXT-COMPONENT-REF", inner_port_iref.getContextComponentRef())
                self.setChildElementOptionalRefType(instance_ref_tag, "TARGET-R-PORT-REF", inner_port_iref.getTargetRPortRef())
            else:
                self._raiseError("Invalid inner port of DelegationSwConnector <%s>" % sw_connector.getShortName())

        if sw_connector.getOuterPortRef() is not None:
            self.setChildElementOptionalRefType(connector_tag, "OUTER-PORT-REF", sw_connector.getOuterPortRef())
            # self.writeChildOptionalRefElement(requester_iref_tag, "TARGET-R-PORT-REF", sw_connector.requester_iref.target_r_port_ref)

    def writePassThroughSwConnector(self, element: ET.Element, sw_connector: PassThroughSwConnector):
        connector_tag = ET.SubElement(element, "PASS-THROUGH-SW-CONNECTOR")
        self.writeSwConnector(connector_tag, sw_connector)
        self.setChildElementOptionalRefType(connector_tag, "PROVIDED-OUTER-PORT-REF", sw_connector.getProvidedOuterPortRef())
        self.setChildElementOptionalRefType(connector_tag, "REQUIRED-OUTER-PORT-REF", sw_connector.getRequiredOuterPortRef())

    def writeSwConnector(self, element: ET.Element, sw_connector: SwConnector):
        self.writeIdentifiable(element, sw_connector)
        self.setChildElementOptionalRefType(element, "MAPPING-REF", sw_connector.getMappingRef())

    def writeCompositionSwComponentTypeSwConnectors(self, element: ET.Element, sw_component: CompositionSwComponentType):
        sw_connectors = sw_component.getSwConnectors()
        if len(sw_connectors) > 0:
            child_element = ET.SubElement(element, "CONNECTORS")
            for sw_connector in sw_connectors:
                if isinstance(sw_connector, AssemblySwConnector):
                    self.writeAssemblySwConnector(child_element, sw_connector)
                elif isinstance(sw_connector, DelegationSwConnector):
                    self.writeDelegationSwConnector(child_element, sw_connector)
                elif isinstance(sw_connector, PassThroughSwConnector):
                    self.writePassThroughSwConnector(child_element, sw_connector)
                else:
                    self.notImplemented("Unsupported Sw Connector %s" % type(sw_connector))

    def writeCompositionSwComponentTypeDataTypeMappingSet(self, element: ET.Element, parent: CompositionSwComponentType):
        data_type_mappings = parent.getDataTypeMappingRefs()
        if len(data_type_mappings) > 0:
            child_element = ET.SubElement(element, "DATA-TYPE-MAPPING-REFS")
            self.logger.debug("writeDataTypeMappingSet")
            for data_type_mapping in data_type_mappings:
                self.setChildElementOptionalRefType(child_element, "DATA-TYPE-MAPPING-REF", data_type_mapping)

    def writeCompositionSwComponentTypeConstantValueMappingSet(self, element: ET.Element, parent: CompositionSwComponentType):
        constant_value_mappings = parent.getConstantValueMappingRefs()
        if len(constant_value_mappings) > 0:
            child_element = ET.SubElement(element, "CONSTANT-VALUE-MAPPING-REFS")
            for constant_value_mapping in constant_value_mappings:
                self.setChildElementOptionalRefType(child_element, "CONSTANT-VALUE-MAPPING-REF", constant_value_mapping)

    def writeInstanceEventInCompositionInstanceRef(self, element: ET.Element, instance_ref: InstanceEventInCompositionInstanceRef):
        for ref in instance_ref.getContextComponentPrototypeRefs():
            self.setChildElementOptionalRefType(element, "CONTEXT-COMPONENT-PROTOTYPE-REF", ref)
        self.setChildElementOptionalRefType(element, "TARGET-EVENT-REF", instance_ref.getTargetEventRef())

    def writeInstantiationRTEEventProps(self, element: ET.Element, props: InstantiationTimingEventProps):
        props_tag = ET.SubElement(element, "INSTANTIATION-TIMING-EVENT-PROPS")
        self.writeARObjectAttributes(props_tag, props)
        if props.getRefinedEventIRef() is not None:
            refined_event_tag = ET.SubElement(props_tag, "REFINED-EVENT-IREF")
            refined_event = props.getRefinedEventIRef()
            self.writeARObjectAttributes(refined_event_tag, refined_event)
            self.writeInstanceEventInCompositionInstanceRef(refined_event_tag, refined_event)
        self.setChildElementOptionalLiteral(props_tag, "SHORT-LABEL", props.getShortLabel())
        self.setChildElementOptionalTimeValue(props_tag, "PERIOD", props.getPeriod())

    def writeCompositionSwComponentTypeInstantiationRTEEventProps(self, element: ET.Element, parent: CompositionSwComponentType):
        props_list = parent.getInstantiationRTEEventProps()
        if len(props_list) > 0:
            child_element = ET.SubElement(element, "INSTANTIATION-RTE-EVENT-PROPSS")
            for props in props_list:
                if isinstance(props, InstantiationTimingEventProps):
                    self.writeInstantiationRTEEventProps(child_element, props)
                else:
                    self.notImplemented("Unsupported InstantiationRTEEventProps %s" % type(props))

    def writeCompositionSwComponentType(self, parent: ET.Element, sw_component: CompositionSwComponentType):
        child_element = ET.SubElement(parent, "COMPOSITION-SW-COMPONENT-TYPE")

        self.writeSwComponentType(child_element, sw_component)
        self.writeCompositionSwComponentTypeComponents(child_element, sw_component)
        self.writeCompositionSwComponentTypeSwConnectors(child_element, sw_component)
        self.writeCompositionSwComponentTypeDataTypeMappingSet(child_element, sw_component)
        self.writeCompositionSwComponentTypeConstantValueMappingSet(child_element, sw_component)
        self.writeCompositionSwComponentTypeInstantiationRTEEventProps(child_element, sw_component)

    def writeCompositionSwComponentTypes(self, element: ET.Element, ar_package: ARPackage):
        for sw_component in ar_package.getCompositionSwComponentTypes():
            self.writeCompositionSwComponentType(element, sw_component)

    def writeLParagraphs(self, element: ET.Element, paragraph: MultiLanguageParagraph):
        for l1 in paragraph.getL1s():
            l1_tag = ET.SubElement(element, "L-1")
            self.writeARObjectAttributes(l1_tag, l1)
            if l1.l is not None:
                l1_tag.attrib["L"] = l1.l
                l1_tag.text = l1.value

    def setMultiLanguageParagraphs(self, element: ET.Element, key: str, paragraphs: List[MultiLanguageParagraph]):
        for paragraph in paragraphs:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, paragraph)
            self.writeLParagraphs(child_element, paragraph)
        return paragraphs

    def setListElement(self, element: ET.Element, key: str, list: ARList):
        if list is not None:
            child_element = ET.SubElement(element, key)
            type = list.getType()
            if type is not None:
                child_element.attrib["TYPE"] = type
            for item in list.getItems():
                self.writeDocumentationBlock(child_element, "ITEM", item)

    def setGraphic(self, element: ET.Element, key: str, graphic: Graphic):
        if graphic is not None:
            child_element = ET.SubElement(element, key)
            if graphic.getFilename() is not None:
                child_element.attrib["FILENAME"] = graphic.getFilename()

    def writeMlFigureLGraphics(self, element: ET.Element, figure: MlFigure):
        graphics = figure.getLGraphics()
        for graphic in graphics:
            child_element = ET.SubElement(element, "L-GRAPHIC")
            if graphic.getL() is not None:
                child_element.attrib["L"] = graphic.getL()
            self.setGraphic(child_element, "GRAPHIC", graphic.getGraphic())

    def writeDocumentViewSelectable(self, element: ET.Element, selectable: DocumentViewSelectable):
        self.writeARObjectAttributes(element, selectable)

    def writePaginateable(self, element: ET.Element, paginateable: Paginateable):
        self.writeDocumentViewSelectable(element, paginateable)

    def writeMlFigure(self, element: ET.Element, figure: MlFigure):
        self.writePaginateable(element, figure)
        self.writeMlFigureLGraphics(element, figure)

    def setMlFigures(self, element: ET.Element, key: str, figures: List[MlFigure]):
        for figure in figures:
            child_element = ET.SubElement(element, key)
            self.writeMlFigure(child_element, figure)

    def writeDocumentationBlock(self, element: ET.Element, key: str, block: DocumentationBlock):
        if block is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, block)
            self.setMsrQueryP2(child_element, block.getMsrQueryP2())
            self.setMultiLanguageParagraphs(child_element, "P", block.getPs())
            self.setMultiLanguageVerbatim(child_element, "VERBATIM", block.getVerbatim())
            for list in block.getLists():
                self.setListElement(child_element, "LIST", list)
            self.setDefList(child_element, block.getDefList())
            self.setLabeledList(child_element, block.getLabeledList())
            self.setMlFormula(child_element, "FORMULA", block.getFormula())
            self.setMlFigures(child_element, "FIGURE", block.getFigures())
            self.setNote(child_element, block.getNote())
            self.setTraceableText(child_element, "TRACE", block.getTrace())
            self.setStructuredReq(child_element, block.getStructuredReq())

    def setDefList(self, element: ET.Element, def_list: DefList):
        if def_list is not None:
            child_element = ET.SubElement(element, "DEF-LIST")
            self.writeARObjectAttributes(child_element, def_list)
            for def_item in def_list.getDefItems():
                self.setDefItem(child_element, def_item)

    def setDefItem(self, element: ET.Element, def_item: DefItem):
        child_element = ET.SubElement(element, "DEF-ITEM")
        self.writeARObjectAttributes(child_element, def_item)
        if def_item.getHelpEntry() is not None:
            child_element.attrib["HELPENTRY"] = def_item.getHelpEntry().getValue()
        self.writeDocumentationBlock(child_element, "DEF", def_item.getDef())

    def setMlFormula(self, element: ET.Element, key: str, formula: MlFormula):
        if formula is not None:
            child_element = ET.SubElement(element, key)
            self.writePaginateable(child_element, formula)
            self.setCaption(child_element, "FORMULA-CAPTION", formula.getFormulaCaption())
            for graphic in formula.getLGraphics():
                l_graphic_element = ET.SubElement(child_element, "L-GRAPHIC")
                if graphic.getL() is not None:
                    l_graphic_element.attrib["L"] = graphic.getL()
                self.setGraphic(l_graphic_element, "GRAPHIC", graphic.getGraphic())
            self.setMultiLanguageVerbatim(child_element, "VERBATIM", formula.getVerbatim())
            self.setMultiLanguagePlainText(child_element, "TEX-MATH", formula.getTexMath())
            self.setMultiLanguagePlainText(child_element, "GENERIC-MATH", formula.getGenericMath())

    def setLabeledList(self, element: ET.Element, labeled_list: LabeledList):
        if labeled_list is not None:
            child_element = ET.SubElement(element, "LABELED-LIST")
            self.writeARObjectAttributes(child_element, labeled_list)
            if labeled_list.getIndentSample() is not None:
                self.setIndentSample(child_element, labeled_list.getIndentSample())
            for labeled_item in labeled_list.getLabeledItems():
                self.setLabeledItem(child_element, labeled_item)

    def setIndentSample(self, element: ET.Element, indent_sample: IndentSample):
        child_element = ET.SubElement(element, "INDENT-SAMPLE")
        self.writeARObjectAttributes(child_element, indent_sample)
        if indent_sample.getItemLabelPos() is not None:
            child_element.attrib["ITEMLABELPOS"] = indent_sample.getItemLabelPos().getValue()
        for l2 in indent_sample.getL2s():
            self.setLOverviewParagraph(child_element, l2)

    def setLabeledItem(self, element: ET.Element, labeled_item: LabeledItem):
        child_element = ET.SubElement(element, "LABELED-ITEM")
        self.writeARObjectAttributes(child_element, labeled_item)
        if labeled_item.getHelpEntry() is not None:
            child_element.attrib["HELPENTRY"] = labeled_item.getHelpEntry().getValue()
        self.setMultiLanguageOverviewParagraph(child_element, "ITEM-LABEL", labeled_item.getItemLabel())
        self.writeDocumentationBlock(child_element, "ITEM-CONTENTS", labeled_item.getItemContents())

    def setNote(self, element: ET.Element, note: Note):
        if note is not None:
            child_element = ET.SubElement(element, "NOTE")
            self.writeARObjectAttributes(child_element, note)
            self.setMultiLongName(child_element, "LABEL", note.getLabel())
            if note.getNoteType() is not None:
                child_element.attrib["NOTETYPE"] = note.getNoteType().getValue()
            self.writeDocumentationBlock(child_element, "NOTE-TEXT", note.getNoteText())

    def setTraceableText(self, element: ET.Element, key: str, traceable_text: TraceableText):
        if traceable_text is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, traceable_text)
            self.writeDocumentationBlock(child_element, "TEXT", traceable_text.getText())
            self.writeTraceable(child_element, traceable_text)

    def setStructuredReq(self, element: ET.Element, structured_req: StructuredReq):
        if structured_req is not None:
            child_element = ET.SubElement(element, "STRUCTURED-REQ")
            self.writeARObjectAttributes(child_element, structured_req)
            self.setChildElementOptionalLiteral(child_element, "DATE", structured_req.getDate())
            self.setChildElementOptionalLiteral(child_element, "IMPORTANCE", structured_req.getImportance())
            self.setChildElementOptionalLiteral(child_element, "ISSUED-BY", structured_req.getIssuedBy())
            self.setChildElementOptionalLiteral(child_element, "TYPE", structured_req.getType())
            self.writeDocumentationBlock(child_element, "DESCRIPTION", structured_req.getDescription())
            self.writeDocumentationBlock(child_element, "RATIONALE", structured_req.getRationale())
            self.writeDocumentationBlock(child_element, "DEPENDENCIES", structured_req.getDependencies())
            self.writeDocumentationBlock(child_element, "USE-CASE", structured_req.getUseCase())
            self.writeDocumentationBlock(child_element, "CONFLICTS", structured_req.getConflicts())
            self.writeDocumentationBlock(child_element, "SUPPORTING-MATERIAL", structured_req.getSupportingMaterial())
            self.writeDocumentationBlock(child_element, "REMARK", structured_req.getRemark())
            tested_item_refs = structured_req.getTestedItemRefs()
            if len(tested_item_refs) > 0:
                refs_tag = ET.SubElement(child_element, "TESTED-ITEM-REFS")
                for tested_item_ref in tested_item_refs:
                    ref_tag = ET.SubElement(refs_tag, "TESTED-ITEM-REF")
                    ref_tag.text = tested_item_ref.getValue()

    def setMultiLanguageVerbatim(self, element: ET.Element, key: str, verbatim: MultiLanguageVerbatim):
        if verbatim is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, verbatim)
            if verbatim.getAllowBreak() is not None:
                child_element.attrib["ALLOWBREAK"] = verbatim.getAllowBreak().getValue()
            if verbatim.getFloat() is not None:
                child_element.attrib["FLOAT"] = verbatim.getFloat().getValue()
            if verbatim.getHelpEntry() is not None:
                child_element.attrib["HELPENTRY"] = verbatim.getHelpEntry().getValue()
            if verbatim.getPgwide() is not None:
                child_element.attrib["PGWIDE"] = verbatim.getPgwide().getValue()
            for l5 in verbatim.getL5s():
                self.setLVerbatim(child_element, l5)

    def setLVerbatim(self, element: ET.Element, text: LVerbatim):
        self.setLanguageSpecific(element, "L-5", text)

    def setMsrQueryP2(self, element: ET.Element, msr_query_p2: MsrQueryP2):
        if msr_query_p2 is not None:
            child_element = ET.SubElement(element, "MSR-QUERY-P2")
            self.writeARObjectAttributes(child_element, msr_query_p2)
            if msr_query_p2.getMsrQueryProps() is not None:
                self.setMsrQueryProps(child_element, msr_query_p2.getMsrQueryProps())
            self.writeDocumentationBlock(child_element, "MSR-QUERY-RESULT-P2", msr_query_p2.getMsrQueryResultP2())

    def setMsrQueryProps(self, element: ET.Element, msr_query_props: MsrQueryProps):
        child_element = ET.SubElement(element, "MSR-QUERY-PROPS")
        self.writeARObjectAttributes(child_element, msr_query_props)
        self.setChildElementOptionalLiteral(child_element, "COMMENT", msr_query_props.getComment())
        self.setChildElementOptionalLiteral(child_element, "MSR-QUERY-NAME", msr_query_props.getMsrQueryName())
        for msr_query_arg in msr_query_props.getMsrQueryArgs():
            self.setMsrQueryArg(child_element, msr_query_arg)

    def setMsrQueryArg(self, element: ET.Element, msr_query_arg: MsrQueryArg):
        child_element = ET.SubElement(element, "MSR-QUERY-ARG")
        self.writeARObjectAttributes(child_element, msr_query_arg)
        self.setChildElementOptionalLiteral(child_element, "ARG", msr_query_arg.getArg())
        if msr_query_arg.getSi() is not None:
            child_element.attrib["SI"] = msr_query_arg.getSi().getValue()

    def writeGeneralAnnotation(self, element: ET.Element, annotation: Annotation):
        self.setMultiLongName(element, "LABEL", annotation.getLabel())
        self.setChildElementOptionalLiteral(element, "ANNOTATION-ORIGIN", annotation.getAnnotationOrigin())
        self.writeDocumentationBlock(element, "ANNOTATION-TEXT", annotation.getAnnotationText())

    def setAnnotations(self, element: ET.Element, annotations: List[Annotation]):
        if len(annotations) > 0:
            annotations_tag = ET.SubElement(element, "ANNOTATIONS")
            for annotation in annotations:
                annotation_tag = ET.SubElement(annotations_tag, "ANNOTATION")
                self.writeGeneralAnnotation(annotation_tag, annotation)

    def setSwAxisIndividual(self, element: ET.Element, props: SwAxisIndividual):
        child_element = ET.SubElement(element, "SW-AXIS-INDIVIDUAL")
        self.writeARObjectAttributes(child_element, props)
        self.setChildElementOptionalFloatValue(child_element, "MAX-GRADIENT", props.getMaxGradient())
        self.setChildElementOptionalLiteral(child_element, "MONOTONY", props.getMonotony())
        self.setChildElementOptionalRefType(child_element, "INPUT-VARIABLE-TYPE-REF", props.getInputVariableTypeRef())
        self.setChildElementOptionalRefType(child_element, "COMPU-METHOD-REF", props.getCompuMethodRef())
        self.setChildElementOptionalNumericalValue(child_element, "SW-MAX-AXIS-POINTS", props.getSwMaxAxisPoints())
        self.setChildElementOptionalNumericalValue(child_element, "SW-MIN-AXIS-POINTS", props.getSwMinAxisPoints())
        self.setChildElementOptionalRefType(child_element, "DATA-CONSTR-REF", props.getDataConstrRef())
        if props.getSwAxisGeneric() is not None:
            self.setSwAxisGeneric(child_element, props.getSwAxisGeneric())

    def setSwAxisGeneric(self, element: ET.Element, axis: SwAxisGeneric):
        child_element = ET.SubElement(element, "SW-AXIS-GENERIC")
        self.writeARObjectAttributes(child_element, axis)
        self.setChildElementOptionalRefType(child_element, "SW-AXIS-TYPE-REF", axis.getSwAxisTypeRef())
        if axis.getSwGenericAxisParams():
            params_wrapper = ET.SubElement(child_element, "SW-GENERIC-AXIS-PARAMS")
            for param in axis.getSwGenericAxisParams():
                self.setSwGenericAxisParam(params_wrapper, param)

    def setSwGenericAxisParam(self, element: ET.Element, param: SwGenericAxisParam):
        param_element = ET.SubElement(element, "SW-GENERIC-AXIS-PARAM")
        self.writeARObjectAttributes(param_element, param)
        self.setChildElementOptionalRefType(param_element, "SW-GENERIC-AXIS-PARAM-TYPE-REF", param.getSwGenericAxisParamTypeRef())
        for vf in param.getVfs():
            self.setChildElementOptionalNumericalValue(param_element, "VF", vf)

    def setSwAxisGrouped(self, element: ET.Element, props: SwAxisGrouped):
        child_element = ET.SubElement(element, "SW-AXIS-GROUPED")
        self.writeARObjectAttributes(child_element, props)
        self.setChildElementOptionalFloatValue(child_element, "MAX-GRADIENT", props.getMaxGradient())
        self.setChildElementOptionalLiteral(child_element, "MONOTONY", props.getMonotony())
        self.setChildElementOptionalRefType(child_element, "SHARED-AXIS-TYPE-REF", props.sharedAxisTypeRef)

    def setSwCalprmAxis(self, element: ET.Element, axis: SwCalprmAxis):
        if axis is not None:
            child_element = ET.SubElement(element, "SW-CALPRM-AXIS")
            self.setChildElementOptionalLiteral(child_element, "SW-AXIS-INDEX", axis.getSwAxisIndex())
            self.setChildElementOptionalLiteral(child_element, "CATEGORY", axis.getCategory())
            if axis.getSwCalprmAxisTypeProps() is not None:
                if isinstance(axis.getSwCalprmAxisTypeProps(), SwAxisIndividual):
                    self.setSwAxisIndividual(child_element, axis.getSwCalprmAxisTypeProps())
                elif isinstance(axis.getSwCalprmAxisTypeProps(), SwAxisGrouped):
                    self.setSwAxisGrouped(child_element, axis.getSwCalprmAxisTypeProps())
                else:
                    self.notImplemented("Unsupported SwCalprmAxisTypeProps %s" % type(axis.getSwCalprmAxisTypeProps()))
            self.setChildElementOptionalLiteral(child_element, "SW-CALIBRATION-ACCESS", axis.getSwCalibrationAccess())
            self.setChildElementOptionalLiteral(child_element, "DISPLAY-FORMAT", axis.getDisplayFormat())

    def setSwCalprmAxisSet(self, element: ET.Element, key: str, set: SwCalprmAxisSet):
        if set is not None:
            axises = set.getSwCalprmAxises()
            if len(axises) > 0:
                child_element = ET.SubElement(element, key)
                for axis in axises:
                    self.setSwCalprmAxis(child_element, axis)

    def setSwPointerTargetProps(self, element: ET.Element, key: str, props: SwPointerTargetProps):
        if props is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "TARGET-CATEGORY", props.getTargetCategory())
            self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", props.getSwDataDefProps())
            self.setChildElementOptionalRefType(child_element, "FUNCTION-POINTER-SIGNATURE-REF", props.getFunctionPointerSignatureRef())

    def setSwDataDefProps(self, element: ET.Element, key: str, props: SwDataDefProps):
        if props is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, props)
            sw_data_def_props_variants_tag = ET.SubElement(child_element, "SW-DATA-DEF-PROPS-VARIANTS")
            conditional_tag = ET.SubElement(sw_data_def_props_variants_tag, "SW-DATA-DEF-PROPS-CONDITIONAL")
            self.setAnnotations(conditional_tag, props.getAnnotations())
            self.setChildElementOptionalLiteral(conditional_tag, "DISPLAY-PRESENTATION", props.getDisplayPresentation())
            self.setChildElementOptionalRefType(conditional_tag, "BASE-TYPE-REF", props.getBaseTypeRef())
            self.setChildElementOptionalRefType(conditional_tag, "SW-ADDR-METHOD-REF", props.getSwAddrMethodRef())
            self.setChildElementOptionalLiteral(conditional_tag, "SW-ALIGNMENT", props.getSwAlignment())
            self.setChildElementOptionalLiteral(conditional_tag, "SW-CALIBRATION-ACCESS", props.getSwCalibrationAccess())
            self.setChildElementOptionalRefType(conditional_tag, "COMPU-METHOD-REF", props.getCompuMethodRef())
            self.setChildValueSpecification(conditional_tag, "INVALID-VALUE", props.getInvalidValue())
            self.setChildElementOptionalFloatValue(conditional_tag, "STEP-SIZE", props.getStepSize())
            self.setChildElementOptionalRefType(conditional_tag, "DATA-CONSTR-REF", props.getDataConstrRef())
            self.setChildElementOptionalRefType(conditional_tag, "IMPLEMENTATION-DATA-TYPE-REF", props.getImplementationDataTypeRef())
            self.setSwCalprmAxisSet(conditional_tag, "SW-CALPRM-AXIS-SET", props.getSwCalprmAxisSet())
            self.setSwBitRepresentation(conditional_tag, props.getSwBitRepresentation())
            self.setChildElementOptionalNumericalValue(conditional_tag, "SW-VALUE-BLOCK-SIZE", props.getSwValueBlockSize())
            self.setSwValueBlockSizeMults(conditional_tag, props.getSwValueBlockSizeMults())
            self.setChildElementOptionalLiteral(conditional_tag, "SW-IMPL-POLICY", props.getSwImplPolicy())
            self.setChildElementOptionalNumericalValue(conditional_tag, "SW-INTENDED-RESOLUTION", props.getSwIntendedResolution())
            self.setSwPointerTargetProps(conditional_tag, "SW-POINTER-TARGET-PROPS", props.getSwPointerTargetProps())
            self.setSwTextProps(conditional_tag, props.getSwTextProps())
            self.setSwComparisonVariables(conditional_tag, props.getSwComparisonVariables())
            self.setChildElementOptionalRefType(conditional_tag, "SW-RECORD-LAYOUT-REF", props.getSwRecordLayoutRef())
            self.setChildElementOptionalRefType(conditional_tag, "VALUE-AXIS-DATA-TYPE-REF", props.getValueAxisDataTypeRef())
            self.setChildElementOptionalRefType(conditional_tag, "UNIT-REF", props.getUnitRef())
            self.setSwDataDependency(conditional_tag, props.getSwDataDependency())
            self.setChildElementOptionalLiteral(conditional_tag, "DISPLAY-FORMAT", props.getDisplayFormat())
            self.setChildElementOptionalLiteral(conditional_tag, "ADDITIONAL-NATIVE-TYPE-QUALIFIER", props.getAdditionalNativeTypeQualifier())
            self.setChildElementOptionalLiteral(conditional_tag, "SW-INTERPOLATION-METHOD", props.getSwInterpolationMethod())
            self.setChildElementOptionalBooleanValue(conditional_tag, "SW-IS-VIRTUAL", props.getSwIsVirtual())
            self.setSwHostVariable(conditional_tag, props.getSwHostVariable())
            self.setMultidimensionalTime(conditional_tag, "SW-REFRESH-TIMING", props.getSwRefreshTiming())

    def setSwBitRepresentation(self, element: ET.Element, bit_representation: SwBitRepresentation):
        if bit_representation is not None:
            child_element = ET.SubElement(element, "SW-BIT-REPRESENTATION")
            self.writeARObjectAttributes(child_element, bit_representation)
            self.setChildElementOptionalIntegerValue(child_element, "BIT-POSITION", bit_representation.getBitPosition())
            self.setChildElementOptionalIntegerValue(child_element, "NUMBER-OF-BITS", bit_representation.getNumberOfBits())

    def setSwValueBlockSizeMults(self, element: ET.Element, mults: List[ARNumerical]):
        if len(mults) > 0:
            mults_element = ET.SubElement(element, "SW-VALUE-BLOCK-SIZE-MULTS")
            for mult in mults:
                value_element = ET.SubElement(mults_element, "NUMERICAL-VALUE-VARIATION-POINT")
                self.setChildElementOptionalNumericalValue(value_element, "V", mult)

    def setSwComparisonVariables(self, element: ET.Element, comparison_variables: List[SwVariableRefProxy]):
        if len(comparison_variables) > 0:
            comparison_variables_element = ET.SubElement(element, "SW-COMPARISON-VARIABLES")
            for comparison_variable in comparison_variables:
                self.setSwVariableRefProxy(comparison_variables_element, "SW-VARIABLE-REF-PROXY", comparison_variable)

    def setSwHostVariable(self, element: ET.Element, host_variable: SwVariableRefProxy):
        if host_variable is not None:
            self.setSwVariableRefProxy(element, "SW-HOST-VARIABLE", host_variable)

    def setSwVariableRefProxy(self, element: ET.Element, key: str, proxy: SwVariableRefProxy):
        if proxy is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, proxy)
            self.setAutosarVariableRef(child_element, "AUTOSAR-VARIABLE", proxy.getAutosarVariable())
            self.setChildElementOptionalRefType(child_element, "MC-DATA-INSTANCE-VAR-REF", proxy.getMcDataInstanceVarRef())

    def setSwCalprmRefProxy(self, element: ET.Element, key: str, proxy: SwCalprmRefProxy):
        if proxy is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, proxy)
            self.setAutosarParameterRef(child_element, "AR-PARAMETER", proxy.getArParameter())
            self.setChildElementOptionalRefType(child_element, "MC-DATA-INSTANCE-REF", proxy.getMcDataInstanceRef())

    def setSwDataDependency(self, element: ET.Element, dependency: SwDataDependency):
        if dependency is not None:
            dependency_element = ET.SubElement(element, "SW-DATA-DEPENDENCY")
            self.writeARObjectAttributes(dependency_element, dependency)
            formula = dependency.getSwDataDependencyFormula()
            if formula is not None:
                formula_element = ET.SubElement(dependency_element, "SW-DATA-DEPENDENCY-FORMULA")
                self.writeARObjectAttributes(formula_element, formula)
                if formula.getLevel() is not None:
                    formula_element.set("LEVEL", formula.getLevel().value)
            args = dependency.getSwDataDependencyArgs()
            if args is not None:
                args_element = ET.SubElement(dependency_element, "SW-DATA-DEPENDENCY-ARGS")
                self.writeARObjectAttributes(args_element, args)
                self.setSwCalprmRefProxy(args_element, "SW-CALPRM-REF-PROXY", args.getSwCalprmRef())
                self.setSwVariableRefProxy(args_element, "SW-VARIABLE-REF-PROXY", args.getSwVariable())

    def setSwTextProps(self, element: ET.Element, props: SwTextProps):
        if props is not None:
            child_element = ET.SubElement(element, "SW-TEXT-PROPS")
            self.writeARObjectAttributes(child_element, props)
            self.setChildElementOptionalLiteral(child_element, "ARRAY-SIZE-SEMANTICS", props.getArraySizeSemantics())
            self.setChildElementOptionalRefType(child_element, "BASE-TYPE-REF", props.getBaseTypeRef())
            self.setChildElementOptionalIntegerValue(child_element, "SW-FILL-CHARACTER", props.getSwFillCharacter())
            self.setChildElementOptionalIntegerValue(child_element, "SW-MAX-TEXT-SIZE", props.getSwMaxTextSize())

    def setApplicationDataType(self, element: ET.Element, data_type: ApplicationDataType):
        self.writeAutosarDataType(element, data_type)

    def setApplicationCompositeDataType(self, element: ET.Element, data_type: ApplicationCompositeDataType):
        self.setApplicationDataType(element, data_type)

    def writeAutosarDataType(self, element: ET.Element, data_type: AutosarDataType):
        self.writeARElement(element, data_type)
        self.setSwDataDefProps(element, "SW-DATA-DEF-PROPS", data_type.getSwDataDefProps())

    def writeApplicationPrimitiveDataType(self, element: ET.Element, data_type: ApplicationPrimitiveDataType):
        self.logger.debug("writeApplicationPrimitiveDataType %s" % data_type.getShortName())
        data_type_tag = ET.SubElement(element, "APPLICATION-PRIMITIVE-DATA-TYPE")
        self.setApplicationDataType(data_type_tag, data_type)

    def writeDataPrototype(self, element: ET.Element, prototype: DataPrototype):
        self.writeIdentifiable(element, prototype)
        self.setSwDataDefProps(element, "SW-DATA-DEF-PROPS", prototype.getSwDataDefProps())

    def writeApplicationCompositeElementDataPrototype(self, element: ET.Element, prototype: ApplicationCompositeElementDataPrototype):
        self.writeDataPrototype(element, prototype)
        self.setChildElementOptionalRefType(element, "TYPE-TREF", prototype.typeTRef)

    def writeApplicationRecordElement(self, element: ET.Element, prototype: ApplicationRecordElement):
        child_element = ET.SubElement(element, "APPLICATION-RECORD-ELEMENT")
        self.writeApplicationCompositeElementDataPrototype(child_element, prototype)

    def writeApplicationRecordDataTypeElements(self, element: ET.Element, data_type: ApplicationRecordDataType):
        record_elements = data_type.getApplicationRecordElements()
        if len(record_elements) > 0:
            child_element = ET.SubElement(element, "ELEMENTS")
            for record_element in record_elements:
                if isinstance(record_element, ApplicationRecordElement):
                    self.writeApplicationRecordElement(child_element, record_element)
                else:
                    self.notImplemented("Unsupported ApplicationRecordDataType Element <%s>" % type(record_element))

    def writeApplicationRecordDataType(self, element: ET.Element, data_type: ApplicationRecordDataType):
        data_type_tag = ET.SubElement(element, "APPLICATION-RECORD-DATA-TYPE")
        self.setApplicationDataType(data_type_tag, data_type)
        self.writeApplicationRecordDataTypeElements(data_type_tag, data_type)

    def writeApplicationDataTypes(self, parent: ET.Element, ar_package: ARPackage):
        for data_type in ar_package.getApplicationDataType():
            if isinstance(data_type, ApplicationPrimitiveDataType):
                self.writeApplicationPrimitiveDataType(parent, data_type)
            elif isinstance(data_type, ApplicationRecordDataType):
                self.writeApplicationRecordDataType(parent, data_type)
            else:
                self.notImplemented("Unsupported ApplicationDataType <%s>" % type(data_type))

    def setBaseTypeDirectDefinition(self, element: ET.Element, base_type_definition: BaseTypeDirectDefinition):
        self.setChildElementOptionalPositiveInteger(element, "BASE-TYPE-SIZE", base_type_definition.getBaseTypeSize())
        self.setChildElementOptionalLiteral(element, "BASE-TYPE-ENCODING", base_type_definition.getBaseTypeEncoding())
        self.setChildElementOptionalPositiveInteger(element, "MEM-ALIGNMENT", base_type_definition.getMemAlignment())
        self.setChildElementOptionalLiteral(element, "BYTE-ORDER", base_type_definition.getByteOrder())
        self.setChildElementOptionalLiteral(element, "NATIVE-DECLARATION", base_type_definition.getNativeDeclaration())

    def writeSwBaseType(self, element: ET.Element, base_type: SwBaseType):
        data_type_tag = ET.SubElement(element, "SW-BASE-TYPE")
        self.writeIdentifiable(data_type_tag, base_type)
        self.setBaseTypeDirectDefinition(data_type_tag, base_type.getBaseTypeDefinition())

    def writeCompuScaleConstantContents(self, element: ET.Element, contents: CompuScaleConstantContents):
        compu_const_tag = ET.SubElement(element, "COMPU-CONST")
        if isinstance(contents.compuConst.compuConstContentType, CompuConstTextContent):
            self.setChildElementOptionalLiteral(compu_const_tag, "VT", contents.compuConst.compuConstContentType.vt)

    def writeCompuNominatorDenominator(self, element: ET.Element, key: str, parent: CompuNominatorDenominator):
        child_element = ET.SubElement(element, key)
        for v in parent.get_vs():
            v_tag = ET.SubElement(child_element, "V")
            v_tag.text = v

    def writeCompuScaleRationalFormula(self, element: ET.Element, contents: CompuScaleRationalFormula):
        if contents.compuRationalCoeffs is not None:
            coeffs_tag = ET.SubElement(element, "COMPU-RATIONAL-COEFFS")
            if contents.compuRationalCoeffs.compuNumerator:
                self.writeCompuNominatorDenominator(coeffs_tag, "COMPU-NUMERATOR", contents.compuRationalCoeffs.compuNumerator)
            if contents.compuRationalCoeffs.compuDenominator:
                self.writeCompuNominatorDenominator(coeffs_tag, "COMPU-DENOMINATOR", contents.compuRationalCoeffs.compuDenominator)

    def writeCompuScaleContents(self, element: ET.Element, compu_scale: CompuScale):
        if isinstance(compu_scale.compuScaleContents, CompuScaleConstantContents):
            self.writeCompuScaleConstantContents(element, compu_scale.compuScaleContents)
        elif isinstance(compu_scale.compuScaleContents, CompuScaleRationalFormula):
            self.writeCompuScaleRationalFormula(element, compu_scale.compuScaleContents)
        else:
            self.notImplemented("Unsupported CompuScaleContents %s" % type(compu_scale.compuScaleContents))

    def setCompuConstContent(self, element: ET.Element, content: CompuConstContent):
        if content is not None:
            if isinstance(content, CompuConstFormulaContent):
                self.setChildElementOptionalLiteral(element, "VF", content.getVf())
            elif isinstance(content, CompuConstNumericContent):
                self.setChildElementOptionalNumericalValue(element, "V", content.getV())
            elif isinstance(content, CompuConstTextContent):
                self.setChildElementOptionalLiteral(element, "VT", content.getVt())
            else:
                self.notImplemented("Unsupported CompuConstContent <%s>" % type(content))

    def writeCompuScale(self, element: ET.Element, key: str, compu_scale: CompuScale):
        if compu_scale is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, compu_scale)
            self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", compu_scale.getShortLabel())
            self.setChildElementOptionalLiteral(child_element, "SYMBOL", compu_scale.getSymbol())
            self.setMultiLanguageOverviewParagraph(child_element, "DESC", compu_scale.getDesc())
            self.setChildElementOptionalPositiveInteger(child_element, "MASK", compu_scale.getMask())
            self.setChildLimitElement(child_element, "LOWER-LIMIT", compu_scale.getLowerLimit())
            self.setChildLimitElement(child_element, "UPPER-LIMIT", compu_scale.getUpperLimit())
            self.writeCompuScaleContents(child_element, compu_scale)

    def setCompuScales(self, element: ET.Element, compu_scales: CompuScales):
        if compu_scales is not None:
            child_element = ET.SubElement(element, "COMPU-SCALES")
            for compu_scale in compu_scales.getCompuScales():
                self.writeCompuScale(child_element, "COMPU-SCALE", compu_scale)

    def setCompuConst(self, element: ET.Element, key: str, compu_const: CompuConst):
        if compu_const is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, compu_const)
            self.setCompuConstContent(child_element, compu_const.getCompuConstContentType())

    def setCompu(self, element: ET.Element, key: str, compu: Compu):
        if compu is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, compu)
            self.setCompuScales(child_element, compu.getCompuContent())
            self.setCompuConst(child_element, "COMPU-DEFAULT-VALUE", compu.getCompuDefaultValue())

    def writeCompuMethod(self, element: ET.Element, compu_method: CompuMethod):
        child_element = ET.SubElement(element, "COMPU-METHOD")
        self.logger.debug("write CompuMethods %s" % compu_method.getShortName())
        self.writeIdentifiable(child_element, compu_method)
        self.setChildElementOptionalRefType(child_element, "UNIT-REF", compu_method.getUnitRef())
        self.setCompu(child_element, "COMPU-INTERNAL-TO-PHYS", compu_method.getCompuInternalToPhys())
        self.setCompu(child_element, "COMPU-PHYS-TO-INTERNAL", compu_method.getCompuPhysToInternal())

    def writeApplicationValueSpecification(self, element: ET.Element, value_spec: ApplicationValueSpecification):
        if value_spec is not None:
            child_element = ET.SubElement(element, "APPLICATION-VALUE-SPECIFICATION")
            self.writeValueSpecification(child_element, value_spec)
            self.setChildElementOptionalLiteral(child_element, "CATEGORY", value_spec.getCategory())
            self.writeSwValueCont(child_element, value_spec.getSwValueCont())

    def writeNumericalOrText(self, element: ET.Element, key: str, not_text: NumericalOrText):
        if not_text is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, not_text)
            self.setChildElementOptionalNumericalValue(child_element, "VF", not_text.getVf())
            self.setChildElementOptionalLiteral(child_element, "VT", not_text.getVt())

    def writeRuleArguments(self, element: ET.Element, arguments: RuleArguments):
        if arguments is not None:
            child_element = ET.SubElement(element, "RULE-ARGUMENTS")
            self.writeARObjectAttributes(child_element, arguments)
            self.setChildElementOptionalNumericalValue(child_element, "V", arguments.getV())
            self.setChildElementOptionalNumericalValue(child_element, "VF", arguments.getVf())
            self.setChildElementOptionalLiteral(child_element, "VT", arguments.getVt())
            self.writeNumericalOrText(child_element, "VTF", arguments.getVtf())

    def writeRuleBasedValueSpecification(self, element: ET.Element, key: str, value_spec: RuleBasedValueSpecification):
        if value_spec is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, value_spec)
            self.setChildElementOptionalIdentifier(child_element, "RULE", value_spec.getRule())
            arguments = value_spec.getArguments()
            if len(arguments) > 0:
                arguments_tag = ET.SubElement(child_element, "ARGUMENTSS")
                for argument in arguments:
                    self.writeRuleArguments(arguments_tag, argument)
            self.setChildElementOptionalIntegerValue(child_element, "MAX-SIZE-TO-FILL", value_spec.getMaxSizeToFill())

    def writeRuleBasedAxisCont(self, element: ET.Element, cont: RuleBasedAxisCont):
        if cont is not None:
            child_element = ET.SubElement(element, "RULE-BASED-AXIS-CONT")
            self.writeARObjectAttributes(child_element, cont)
            self.setChildElementOptionalLiteral(child_element, "CATEGORY", cont.getCategory())
            self.setChildElementOptionalRefType(child_element, "UNIT-REF", cont.getUnitRef())
            self.setValueList(child_element, "SW-ARRAYSIZE", cont.getSwArraysize())
            self.setChildElementOptionalLiteral(child_element, "SW-AXIS-INDEX", cont.getSwAxisIndex())
            self.writeRuleBasedValueSpecification(child_element, "RULE-BASED-VALUES", cont.getRuleBasedValues())

    def writeRuleBasedValueCont(self, element: ET.Element, cont: RuleBasedValueCont):
        if cont is not None:
            child_element = ET.SubElement(element, "SW-VALUE-CONT")
            self.writeARObjectAttributes(child_element, cont)
            self.setChildElementOptionalRefType(child_element, "UNIT-REF", cont.getUnitRef())
            self.setValueList(child_element, "SW-ARRAYSIZE", cont.getSwArraysize())
            self.writeRuleBasedValueSpecification(child_element, "RULE-BASED-VALUES", cont.getRuleBasedValues())

    def writeApplicationRuleBasedValueSpecification(self, element: ET.Element, value_spec: ApplicationRuleBasedValueSpecification):
        if value_spec is not None:
            child_element = ET.SubElement(element, "APPLICATION-RULE-BASED-VALUE-SPECIFICATION")
            self.writeValueSpecification(child_element, value_spec)
            self.setChildElementOptionalLiteral(child_element, "CATEGORY", value_spec.getCategory())
            axis_conts = value_spec.getSwAxisConts()
            if len(axis_conts) > 0:
                axis_conts_tag = ET.SubElement(child_element, "SW-AXIS-CONTS")
                for axis_cont in axis_conts:
                    self.writeRuleBasedAxisCont(axis_conts_tag, axis_cont)
            self.writeRuleBasedValueCont(child_element, value_spec.getSwValueCont())

    def writeCompositeRuleBasedValueSpecification(self, element: ET.Element, value_spec: CompositeRuleBasedValueSpecification):
        if value_spec is not None:
            child_element = ET.SubElement(element, "COMPOSITE-RULE-BASED-VALUE-SPECIFICATION")
            self.writeValueSpecification(child_element, value_spec)
            self.setChildElementOptionalIdentifier(child_element, "RULE", value_spec.getRule())
            arguments = value_spec.getArguments()
            if len(arguments) > 0:
                arguments_tag = ET.SubElement(child_element, "ARGUMENTS")
                for argument in arguments:
                    if isinstance(argument, CompositeRuleBasedValueSpecification):
                        self.writeCompositeRuleBasedValueSpecification(arguments_tag, argument)
                    elif isinstance(argument, ArrayValueSpecification):
                        self.writeArrayValueSpecification(arguments_tag, argument)
                    elif isinstance(argument, RecordValueSpecification):
                        self.writeRecordValueSpecification(arguments_tag, argument)
                    elif isinstance(argument, ConstantReference):
                        self.setConstantReference(arguments_tag, argument)
                    else:
                        self.notImplemented("Unsupported argument type of <%s> of CompositeRuleBasedValueSpecification" % type(argument))
            compound_arguments = value_spec.getCompoundPrimitiveArguments()
            if len(compound_arguments) > 0:
                compound_tag = ET.SubElement(child_element, "COMPOUND-PRIMITIVE-ARGUMENTS")
                for argument in compound_arguments:
                    if isinstance(argument, ApplicationRuleBasedValueSpecification):
                        self.writeApplicationRuleBasedValueSpecification(compound_tag, argument)
                    elif isinstance(argument, CompositeRuleBasedValueSpecification):
                        self.writeCompositeRuleBasedValueSpecification(compound_tag, argument)
                    elif isinstance(argument, ArrayValueSpecification):
                        self.writeArrayValueSpecification(compound_tag, argument)
                    elif isinstance(argument, RecordValueSpecification):
                        self.writeRecordValueSpecification(compound_tag, argument)
                    elif isinstance(argument, ConstantReference):
                        self.setConstantReference(compound_tag, argument)
                    else:
                        self.notImplemented("Unsupported compound primitive argument type of <%s> of CompositeRuleBasedValueSpecification" % type(argument))
            self.setChildElementOptionalIntegerValue(child_element, "MAX-SIZE-TO-FILL", value_spec.getMaxSizeToFill())

    def writeRecordValueSpecification(self, element: ET.Element, spec: RecordValueSpecification):
        child_element = ET.SubElement(element, "RECORD-VALUE-SPECIFICATION")
        self.writeARObjectAttributes(child_element, spec)
        self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", spec.getShortLabel())
        fields = spec.getFields()
        if len(fields) > 0:
            fields_tag = ET.SubElement(child_element, "FIELDS")
            for field in fields:
                if isinstance(field, ApplicationValueSpecification):
                    self.writeApplicationValueSpecification(fields_tag, field)
                elif isinstance(field, ApplicationRuleBasedValueSpecification):
                    self.writeApplicationRuleBasedValueSpecification(fields_tag, field)
                elif isinstance(field, CompositeRuleBasedValueSpecification):
                    self.writeCompositeRuleBasedValueSpecification(fields_tag, field)
                elif isinstance(field, NumericalValueSpecification):
                    self.writeNumericalValueSpecification(fields_tag, field)
                elif isinstance(field, TextValueSpecification):
                    self.writeTextValueSpecification(fields_tag, field)
                elif isinstance(field, ArrayValueSpecification):
                    self.writeArrayValueSpecification(fields_tag, field)
                elif isinstance(field, RecordValueSpecification):
                    self.writeRecordValueSpecification(fields_tag, field)
                elif isinstance(field, NotAvailableValueSpecification):
                    self.writeNotAvailableValueSpecification(fields_tag, field)
                else:
                    self.notImplemented("Unsupported Field <%s>" % type(field))

    def writeConstantSpecification(self, element: ET.Element, spec: ConstantSpecification):
        spec_tag = ET.SubElement(element, "CONSTANT-SPECIFICATION")
        self.writeIdentifiable(spec_tag, spec)

        if spec.getValueSpec() is not None:
            self.setChildValueSpecification(spec_tag, "VALUE-SPEC", spec.getValueSpec())

    def setInternalConstrs(self, element: ET.Element, constrs: InternalConstrs):
        if constrs is not None:
            constrs_tag = ET.SubElement(element, "INTERNAL-CONSTRS")
            self.writeARObjectAttributes(constrs_tag, constrs)
            if constrs.getLowerLimit() is not None:
                self.setChildLimitElement(constrs_tag, "LOWER-LIMIT", constrs.getLowerLimit())
            if constrs.getUpperLimit() is not None:
                self.setChildLimitElement(constrs_tag, "UPPER-LIMIT", constrs.getUpperLimit())
            scale_constrs = constrs.getScaleConstrs()
            if len(scale_constrs) > 0:
                scales_element = ET.SubElement(constrs_tag, "SCALE-CONSTRS")
                for scale_constr in scale_constrs:
                    self.setScaleConstr(scales_element, "SCALE-CONSTR", scale_constr)
            self.setChildElementOptionalNumericalValue(constrs_tag, "MAX-GRADIENT", constrs.getMaxGradient())
            self.setChildElementOptionalNumericalValue(constrs_tag, "MAX-DIFF", constrs.getMaxDiff())
            self.setChildElementOptionalLiteral(constrs_tag, "MONOTONY", constrs.getMonotony())

    def setScaleConstr(self, element: ET.Element, key: str, scale_constr: ScaleConstr):
        if scale_constr is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, scale_constr)
            self.setChildElementOptionalIdentifier(child_element, "SHORT-LABEL", scale_constr.getShortLabel())
            self.setMultiLanguageOverviewParagraph(child_element, "DESC", scale_constr.getDesc())
            if scale_constr.getLowerLimit() is not None:
                self.setChildLimitElement(child_element, "LOWER-LIMIT", scale_constr.getLowerLimit())
            if scale_constr.getUpperLimit() is not None:
                self.setChildLimitElement(child_element, "UPPER-LIMIT", scale_constr.getUpperLimit())
            if scale_constr.getValidity() is not None:
                child_element.set("VALIDITY", scale_constr.getValidity().getValue())

    def setPhysConstrs(self, element: ET.Element, constrs: PhysConstrs):
        if constrs is not None:
            child_element = ET.SubElement(element, "PHYS-CONSTRS")
            self.writeARObjectAttributes(child_element, constrs)
            if constrs.getLowerLimit() is not None:
                self.setChildLimitElement(child_element, "LOWER-LIMIT", constrs.getLowerLimit())
            if constrs.getUpperLimit() is not None:
                self.setChildLimitElement(child_element, "UPPER-LIMIT", constrs.getUpperLimit())
            scale_constrs = constrs.getScaleConstrs()
            if len(scale_constrs) > 0:
                scales_element = ET.SubElement(child_element, "SCALE-CONSTRS")
                for scale_constr in scale_constrs:
                    self.setScaleConstr(scales_element, "SCALE-CONSTR", scale_constr)
            self.setChildElementOptionalNumericalValue(child_element, "MAX-GRADIENT", constrs.getMaxGradient())
            self.setChildElementOptionalNumericalValue(child_element, "MAX-DIFF", constrs.getMaxDiff())
            monotony = constrs.getMonotony()
            if monotony is not None:
                mono_element = ET.SubElement(child_element, "MONOTONY")
                mono_element.text = monotony.getText() if hasattr(monotony, "getText") else str(monotony)
            self.setChildElementOptionalRefType(child_element, "UNIT-REF", constrs.getUnitRef())

    def writeDataConstrRules(self, element: ET.Element, parent: DataConstr):
        rules = parent.getDataConstrRules()
        if len(rules) > 0:
            rules_tag = ET.SubElement(element, "DATA-CONSTR-RULES")
            for rule in rules:
                child_element = ET.SubElement(rules_tag, "DATA-CONSTR-RULE")
                self.writeARObjectAttributes(child_element, rule)
                self.setChildElementOptionalNumericalValue(child_element, "CONSTR-LEVEL", rule.constrLevel)
                self.setPhysConstrs(child_element, rule.physConstrs)
                self.setInternalConstrs(child_element, rule.internalConstrs)

    def writeDataConstr(self, element: ET.Element, constr: DataConstr):
        child_element = ET.SubElement(element, "DATA-CONSTR")
        self.writeIdentifiable(child_element, constr)
        self.writeDataConstrRules(child_element, constr)

    def writeUnit(self, element: ET.Element, unit: Unit):
        self.logger.debug("writeUnit %s" % unit.getShortName())
        child_element = ET.SubElement(element, "UNIT")
        self.writeIdentifiable(child_element, unit)
        self.setChildElementOptionalLiteral(child_element, "DISPLAY-NAME", unit.getDisplayName())
        self.setChildElementOptionalFloatValue(child_element, "FACTOR-SI-TO-UNIT", unit.getFactorSiToUnit())
        self.setChildElementOptionalFloatValue(child_element, "OFFSET-SI-TO-UNIT", unit.getOffsetSiToUnit())
        self.setChildElementOptionalRefType(child_element, "PHYSICAL-DIMENSION-REF", unit.getPhysicalDimensionRef())

    def setRModeInAtomicSwcInstanceRef(self, element: ET.Element, key: str, iref: RModeInAtomicSwcInstanceRef):
        child_element = ET.SubElement(element, key)
        self.writeARObjectAttributes(child_element, iref)
        self.setChildElementOptionalRefType(child_element, "BASE", iref.getBaseRef())
        self.setChildElementOptionalRefType(child_element, "CONTEXT-PORT-REF", iref.getContextPortRef())
        self.setChildElementOptionalRefType(child_element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF", iref.getContextModeDeclarationGroupPrototypeRef())  # noqa E501
        self.setChildElementOptionalRefType(child_element, "TARGET-MODE-DECLARATION-REF", iref.getTargetModeDeclarationRef())

    def setModeInBswModuleDescriptionInstanceRef(self, element: ET.Element, key: str, iref: ModeInBswModuleDescriptionInstanceRef):
        child_element = ET.SubElement(element, key)
        self.writeARObjectAttributes(child_element, iref)
        self.setChildElementOptionalRefType(child_element, "CONTEXT-MODE-DECLARATION-GROUP-REF", iref.getContextModeDeclarationGroupRef())
        self.setChildElementOptionalRefType(child_element, "TARGET-MODE-REF", iref.getTargetModeRef())

    def setPOperationInAtomicSwcInstanceRef(self, element: ET.Element, key: str, iref: POperationInAtomicSwcInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, iref)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-P-PORT-REF", iref.getContextPPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-PROVIDED-OPERATION-REF", iref.getTargetProvidedOperationRef())

    def setRTEEvent(self, element: ET.Element, event: RTEEvent):
        self.writeIdentifiable(element, event)
        self.setChildElementOptionalRefType(element, "ACTIVATION-REASON-REPRESENTATION-REF", event.getActivationReasonRepresentationRef())
        irefs = event.getDisabledModeIRefs()
        if len(irefs) > 0:
            child_element = ET.SubElement(element, "DISABLED-MODE-IREFS")
            for iref in irefs:
                self.setRModeInAtomicSwcInstanceRef(child_element, "DISABLED-MODE-IREF", iref)
        self.setChildElementOptionalRefType(element, "START-ON-EVENT-REF", event.startOnEventRef)

    def writeTimingEvent(self, element: ET.Element, event: TimingEvent):
        if event is not None:
            child_element = ET.SubElement(element, "TIMING-EVENT")
            self.setRTEEvent(child_element, event)
            self.setChildElementOptionalTimeValue(child_element, "OFFSET", event.getOffset())
            self.setChildElementOptionalTimeValue(child_element, "PERIOD", event.getPeriod())

    def writeOperationInvokedEvent(self, element: ET.Element, event: OperationInvokedEvent):
        if event is not None:
            child_element = ET.SubElement(element, "OPERATION-INVOKED-EVENT")
            self.setRTEEvent(child_element, event)
            self.setPOperationInAtomicSwcInstanceRef(child_element, "OPERATION-IREF", event.operationIRef)

    def writeSwcModeSwitchEvent(self, element: ET.Element, event: SwcModeSwitchEvent):
        if event is not None:
            child_element = ET.SubElement(element, "SWC-MODE-SWITCH-EVENT")
            self.setRTEEvent(child_element, event)
            self.setChildElementOptionalLiteral(child_element, "ACTIVATION", event.getActivation())
            irefs = event.getModeIRefs()
            if len(irefs) > 0:
                mode_irefs_tag = ET.SubElement(child_element, "MODE-IREFS")
                for iref in irefs:
                    self.setRModeInAtomicSwcInstanceRef(mode_irefs_tag, "MODE-IREF", iref)

    def setRVariableInAtomicSwcInstanceRef(self, element: ET.Element, iref: RVariableInAtomicSwcInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, "DATA-IREF")
            self.setChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF", iref.getContextRPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-DATA-ELEMENT-REF", iref.getTargetDataElementRef())

    def writeDataReceivedEvent(self, element: ET.Element, event: DataReceivedEvent):
        if event is not None:
            child_element = ET.SubElement(element, "DATA-RECEIVED-EVENT")
            self.setRTEEvent(child_element, event)
            self.setRVariableInAtomicSwcInstanceRef(child_element, event.dataIRef)

    def writeInternalTriggerOccurredEvent(self, element: ET.Element, event: InternalTriggerOccurredEvent):
        if event is not None:
            child_element = ET.SubElement(element, "INTERNAL-TRIGGER-OCCURRED-EVENT")
            self.setRTEEvent(child_element, event)
            self.setChildElementOptionalRefType(child_element, "EVENT-SOURCE-REF", event.getEventSourceRef())

    def writeInitEvent(self, element: ET.Element, event: InitEvent):
        if event is not None:
            child_element = ET.SubElement(element, "INIT-EVENT")
            self.setRTEEvent(child_element, event)

    def writeAsynchronousServerCallReturnsEvent(self, element: ET.Element, event: InitEvent):
        if event is not None:
            child_element = ET.SubElement(element, "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT")
            self.setRTEEvent(child_element, event)
            self.setChildElementOptionalRefType(child_element, "EVENT-SOURCE-REF", event.getActivationReasonRepresentationRef())

    def writeModeSwitchedAckEvent(self, element: ET.Element, event: ModeSwitchedAckEvent):
        if event is not None:
            child_element = ET.SubElement(element, "MODE-SWITCHED-ACK-EVENT")
            self.setRTEEvent(child_element, event)
            self.setChildElementOptionalRefType(child_element, "EVENT-SOURCE-REF", event.getEventSourceRef())

    def writeBackgroundEvent(self, element: ET.Element, event: BackgroundEvent):
        if event is not None:
            child_element = ET.SubElement(element, "BACKGROUND-EVENT")
            self.setRTEEvent(child_element, event)

    def writeDataSendCompletedEvent(self, element: ET.Element, event: DataSendCompletedEvent):
        if event is not None:
            child_element = ET.SubElement(element, "DATA-SEND-COMPLETED-EVENT")
            self.setRTEEvent(child_element, event)
            self.setChildElementOptionalRefType(child_element, "EVENT-SOURCE-REF", event.getEventSourceRef())

    def writeSwcInternalBehaviorEvents(self, element: ET.Element, parent: SwcInternalBehavior):
        events = parent.getRteEvents()
        if len(events) > 0:
            child_element = ET.SubElement(element, "EVENTS")

            for event in events:
                if isinstance(event, TimingEvent):
                    self.writeTimingEvent(child_element, event)
                elif isinstance(event, OperationInvokedEvent):
                    self.writeOperationInvokedEvent(child_element, event)
                elif isinstance(event, SwcModeSwitchEvent):
                    self.writeSwcModeSwitchEvent(child_element, event)
                elif isinstance(event, DataReceivedEvent):
                    self.writeDataReceivedEvent(child_element, event)
                elif isinstance(event, InternalTriggerOccurredEvent):
                    self.writeInternalTriggerOccurredEvent(child_element, event)
                elif isinstance(event, InitEvent):
                    self.writeInitEvent(child_element, event)
                elif isinstance(event, AsynchronousServerCallReturnsEvent):
                    self.writeAsynchronousServerCallReturnsEvent(child_element, event)
                elif isinstance(event, ModeSwitchedAckEvent):
                    self.writeModeSwitchedAckEvent(child_element, event)
                elif isinstance(event, BackgroundEvent):
                    self.writeBackgroundEvent(child_element, event)
                elif isinstance(event, DataSendCompletedEvent):
                    self.writeDataSendCompletedEvent(child_element, event)
                else:
                    self.notImplemented("Unsupported Event <%s>" % type(event))

    def writeExclusiveAreas(self, element: ET.Element, behavior: InternalBehavior):
        areas = behavior.getExclusiveAreas()
        if len(areas) > 0:
            areas_tag = ET.SubElement(element, "EXCLUSIVE-AREAS")
            for area in areas:
                child_element = ET.SubElement(areas_tag, "EXCLUSIVE-AREA")
                self.writeIdentifiable(child_element, area)

    def writeExclusiveAreaNestingOrders(self, element: ET.Element, behavior: InternalBehavior):
        nesting_orders = behavior.getExclusiveAreaNestingOrders()
        if len(nesting_orders) > 0:
            orders_tag = ET.SubElement(element, "EXCLUSIVE-AREA-NESTING-ORDERS")
            for nesting_order in nesting_orders:
                child_element = ET.SubElement(orders_tag, "EXCLUSIVE-AREA-NESTING-ORDER")
                self.writeReferrable(child_element, nesting_order)
                refs = nesting_order.getExclusiveAreaRefs()
                if len(refs) > 0:
                    refs_tag = ET.SubElement(child_element, "EXCLUSIVE-AREA-REFS")
                    for ref in refs:
                        self.setChildElementOptionalRefType(refs_tag, "EXCLUSIVE-AREA-REF", ref)

    def writeInternalBehaviorConstantValueMappingRefs(self, element: ET.Element, behavior: InternalBehavior):
        refs = behavior.getConstantValueMappingRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "CONSTANT-VALUE-MAPPING-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "CONSTANT-VALUE-MAPPING-REF", ref)

    def writeDataTypeMappingRefs(self, element: ET.Element, behavior: InternalBehavior):
        refs = behavior.getDataTypeMappingRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "DATA-TYPE-MAPPING-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "DATA-TYPE-MAPPING-REF", ref)

    def writeInternalBehaviorStaticMemories(self, element: ET.Element, behavior: InternalBehavior):
        memories = behavior.getStaticMemories()
        if len(memories) > 0:
            child_element = ET.SubElement(element, "STATIC-MEMORYS")
            for memory in memories:
                if isinstance(memory, VariableDataPrototype):
                    self.writeVariableDataPrototype(child_element, memory)

    def writeInternalBehavior(self, element: ET.Element, behavior: InternalBehavior):
        self.writeIdentifiable(element, behavior)
        self.writeSwcInternalBehaviorParameterDataPrototypes(element, "CONSTANT-MEMORYS", behavior.getConstantMemories())
        self.writeInternalBehaviorConstantValueMappingRefs(element, behavior)
        self.writeDataTypeMappingRefs(element, behavior)
        self.writeExclusiveAreas(element, behavior)
        self.writeExclusiveAreaNestingOrders(element, behavior)
        self.writeInternalBehaviorStaticMemories(element, behavior)

    def setVariableInAtomicSWCTypeInstanceRef(self, element: ET.Element, key: str, iref: VariableInAtomicSWCTypeInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, iref)
            self.setChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF", iref.getPortPrototypeRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF", iref.getTargetDataPrototypeRef())

    def setAutosarVariableRef(self, element: ET.Element, key: str, ref: AutosarVariableRef):
        if ref is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, ref)
            self.setVariableInAtomicSWCTypeInstanceRef(child_element, "AUTOSAR-VARIABLE-IREF", ref.getAutosarVariableIRef())
            self.setChildElementOptionalRefType(child_element, "LOCAL-VARIABLE-REF", ref.getLocalVariableRef())

    def writeNvBlockDataMapping(self, element: ET.Element, mapping: NvBlockDataMapping):
        child_element = ET.SubElement(element, "NV-BLOCK-DATA-MAPPING")
        self.writeARObjectAttributes(child_element, mapping)
        self.setChildElementOptionalPositiveInteger(child_element, "BITFIELD-TEXT-TABLE-MASK-NV-BLOCK-DESCRIPTOR", mapping.getBitfieldTextTableMaskNvBlockDescriptor())
        self.setChildElementOptionalPositiveInteger(child_element, "BITFIELD-TEXT-TABLE-MASK-PORT-PROTOTYPE", mapping.getBitfieldTextTableMaskPortPrototype())
        self.setAutosarVariableRef(child_element, "NV-RAM-BLOCK-ELEMENT", mapping.getNvRamBlockElement())
        self.setAutosarVariableRef(child_element, "READ-NV-DATA", mapping.getReadNvData())
        self.setAutosarVariableRef(child_element, "WRITTEN-NV-DATA", mapping.getWrittenNvData())
        self.setAutosarVariableRef(child_element, "WRITTEN-READ-NV-DATA", mapping.getWrittenReadNvData())

    def writeBulkNvDataDescriptor(self, element: ET.Element, descriptor: BulkNvDataDescriptor):
        child_element = ET.SubElement(element, "BULK-NV-DATA-DESCRIPTOR")
        self.writeIdentifiable(child_element, descriptor)
        block = descriptor.getBulkNvBlock()
        if block is not None:
            block_element = ET.SubElement(child_element, "BULK-NV-BLOCK")
            self.writeVariableDataPrototype(block_element, block)
        mappings = descriptor.getNvBlockDataMappings()
        if len(mappings) > 0:
            mappings_element = ET.SubElement(child_element, "NV-BLOCK-DATA-MAPPINGS")
            for mapping in mappings:
                self.writeNvBlockDataMapping(mappings_element, mapping)

    def writeNvBlockDescriptor(self, element: ET.Element, descriptor: NvBlockDescriptor):
        child_element = ET.SubElement(element, "NV-BLOCK-DESCRIPTOR")
        self.writeIdentifiable(child_element, descriptor)
        client_server_ports = descriptor.getClientServerPorts()
        if len(client_server_ports) > 0:
            ports_element = ET.SubElement(child_element, "CLIENT-SERVER-PORTS")
            for assignment in client_server_ports:
                if isinstance(assignment, RoleBasedPortAssignment):
                    self.writeRoleBasedPortAssignment(ports_element, assignment)
                else:
                    self.notImplemented("Unsupported Client Server Port <%s>" % type(assignment))
        constant_mapping_refs = descriptor.getConstantValueMappingRefs()
        if len(constant_mapping_refs) > 0:
            refs_element = ET.SubElement(child_element, "CONSTANT-VALUE-MAPPING-REFS")
            for ref in constant_mapping_refs:
                self.setChildElementOptionalRefType(refs_element, "CONSTANT-VALUE-MAPPING-REF", ref)
        data_type_mapping_refs = descriptor.getDataTypeMappingRefs()
        if len(data_type_mapping_refs) > 0:
            refs_element = ET.SubElement(child_element, "DATA-TYPE-MAPPING-REFS")
            for ref in data_type_mapping_refs:
                self.setChildElementOptionalRefType(refs_element, "DATA-TYPE-MAPPING-REF", ref)
        props_list = descriptor.getInstantiationDataDefPropss()
        if len(props_list) > 0:
            props_tag = ET.SubElement(child_element, "INSTANTIATION-DATA-DEF-PROPSS")
            for props in props_list:
                if isinstance(props, InstantiationDataDefProps):
                    props_element = ET.SubElement(props_tag, "INSTANTIATION-DATA-DEF-PROPS")
                    self.setAutosarParameterRef(props_element, "PARAMETER-INSTANCE", props.getParameterInstance())
                    self.setSwDataDefProps(props_element, "SW-DATA-DEF-PROPS", props.getSwDataDefProps())
                    self.setAutosarVariableRef(props_element, "VARIABLE-INSTANCE", props.getVariableInstance())
                else:
                    self.notImplemented("Unsupported InstantiationDataDefProps <%s>" % type(props))
        activities = descriptor.getModeSwitchEventTriggeredActivitys()
        if len(activities) > 0:
            activities_element = ET.SubElement(child_element, "MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS")
            for activity in activities:
                if isinstance(activity, ModeSwitchEventTriggeredActivity):
                    self.writeModeSwitchEventTriggeredActivity(activities_element, activity)
                else:
                    self.notImplemented("Unsupported ModeSwitchEventTriggeredActivity <%s>" % type(activity))
        mappings = descriptor.getNvBlockDataMappings()
        if len(mappings) > 0:
            mappings_element = ET.SubElement(child_element, "NV-BLOCK-DATA-MAPPINGS")
            for mapping in mappings:
                self.writeNvBlockDataMapping(mappings_element, mapping)
        needs = descriptor.getNvBlockNeeds()
        if needs is not None:
            self.writeNvBlockNeeds(child_element, needs)
        ram_block = descriptor.getRamBlock()
        if ram_block is not None:
            ram_block_element = ET.SubElement(child_element, "RAM-BLOCK")
            self.writeAutosarDataPrototype(ram_block_element, ram_block)
        rom_block = descriptor.getRomBlock()
        if rom_block is not None:
            rom_block_element = ET.SubElement(child_element, "ROM-BLOCK")
            self.writeAutosarDataPrototype(rom_block_element, rom_block)
        self.setChildElementOptionalBooleanValue(child_element, "SUPPORT-DIRTY-FLAG", descriptor.getSupportDirtyFlag())
        self.setChildElementOptionalRefType(child_element, "TIMING-EVENT-REF", descriptor.getTimingEventRef())
        strategies = descriptor.getWritingStrategies()
        if len(strategies) > 0:
            strategies_element = ET.SubElement(child_element, "WRITING-STRATEGYS")
            for strategy in strategies:
                if isinstance(strategy, RoleBasedDataAssignment):
                    self.writeRoleBasedDataAssignment(strategies_element, strategy)
                else:
                    self.notImplemented("Unsupported Writing Strategy <%s>" % type(strategy))

    def writeModeSwitchEventTriggeredActivity(self, element: ET.Element, activity: ModeSwitchEventTriggeredActivity):
        child_element = ET.SubElement(element, "MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY")
        self.setChildElementOptionalLiteral(child_element, "ROLE", activity.getRole())
        self.setChildElementOptionalRefType(child_element, "SWC-MODE-SWITCH-EVENT-REF", activity.getSwcModeSwitchEventRef())

    def setComponentInSystemInstanceRef(self, element: ET.Element, tag_name: str, ref: ComponentInSystemInstanceRef):
        if ref is not None:
            child_element = ET.SubElement(element, tag_name)
            self.writeARObjectAttributes(child_element, ref)
            self.setChildElementOptionalRefType(child_element, "BASE-REF", ref.getBaseRef())
            self.setChildElementOptionalRefType(child_element, "CONTEXT-COMPOSITION-REF", ref.getContextCompositionRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-COMPONENT-REF", ref.getTargetComponentRef())

    def writeVariableAccess(self, element: ET.Element, access: VariableAccess):
        child_element = ET.SubElement(element, "VARIABLE-ACCESS")
        self.writeIdentifiable(child_element, access)
        self.setAutosarVariableRef(child_element, "ACCESSED-VARIABLE", access.getAccessedVariableRef())

    def setParameterInAtomicSWCTypeInstanceRef(self, element: ET.Element, key: str, parameter_iref: ParameterInAtomicSWCTypeInstanceRef):
        if parameter_iref is not None:
            child_element = ET.SubElement(element, key)
            for ref in parameter_iref.getContextDataPrototypeRefs():
                self.setChildElementOptionalRefType(child_element, "CONTEXT-DATA-PROTOTYPE-REF", ref)
            self.setChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF", parameter_iref.getPortPrototypeRef())
            self.setChildElementOptionalRefType(child_element, "ROOT-PARAMETER-DATA-PROTOTYPE-REF", parameter_iref.getRootParameterDataPrototypeRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF", parameter_iref.getTargetDataPrototypeRef())

    def setAutosarParameterRef(self, element: ET.Element, key: str, parameter_ref: AutosarParameterRef):
        if parameter_ref is not None:
            child_element = ET.SubElement(element, key)
            self.setParameterInAtomicSWCTypeInstanceRef(child_element, "AUTOSAR-PARAMETER-IREF", parameter_ref.getAutosarParameterIRef())
            self.setChildElementOptionalRefType(child_element, "LOCAL-PARAMETER-REF", parameter_ref.getLocalParameterRef())

    def writeParameterAccess(self, element: ET.Element, parameter_access: ParameterAccess):
        child_element = ET.SubElement(element, "PARAMETER-ACCESS")
        self.writeIdentifiable(child_element, parameter_access)
        self.setAutosarParameterRef(child_element, "ACCESSED-PARAMETER", parameter_access.getAccessedParameter())

    def writeRunnableEntityParameterAccesses(self, element: ET.Element, entity: RunnableEntity):
        parameter_accesses = entity.getParameterAccesses()
        if len(parameter_accesses) > 0:
            child_element = ET.SubElement(element, "PARAMETER-ACCESSS")
            for parameter_access in parameter_accesses:
                self.writeParameterAccess(child_element, parameter_access)

    def writeRunnableEntityDataReceivePointByArguments(self, element: ET.Element, entity: RunnableEntity):
        accesses = entity.getDataReceivePointByArguments()
        if len(accesses) > 0:
            child_element = ET.SubElement(element, "DATA-RECEIVE-POINT-BY-ARGUMENTS")
            for access in accesses:
                self.writeVariableAccess(child_element, access)

    def writeRunnableEntityDataReceivePointByValues(self, element: ET.Element, entity: RunnableEntity):
        accesses = entity.getDataReceivePointByValues()
        if len(accesses) > 0:
            child_element = ET.SubElement(element, "DATA-RECEIVE-POINT-BY-VALUES")
            for access in accesses:
                self.writeVariableAccess(child_element, access)

    def writeRunnableEntityDataSendPoints(self, element: ET.Element, entity: RunnableEntity):
        points = entity.getDataSendPoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "DATA-SEND-POINTS")
            for point in points:
                self.writeVariableAccess(child_element, point)

    def writeRunnableEntityDataReadAccesses(self, element: ET.Element, entity: RunnableEntity):
        accesses = entity.getDataReadAccesses()
        if len(accesses) > 0:
            child_element = ET.SubElement(element, "DATA-READ-ACCESSS")
            for access in accesses:
                self.writeVariableAccess(child_element, access)

    def writeRunnableEntityDataWriteAccesses(self, element: ET.Element, entity: RunnableEntity):
        accesses = entity.getDataWriteAccesses()
        if len(accesses) > 0:
            child_element = ET.SubElement(element, "DATA-WRITE-ACCESSS")
            for access in accesses:
                self.writeVariableAccess(child_element, access)

    def writeRunnableEntityReadLocalVariables(self, element: ET.Element, entity: RunnableEntity):
        variables = entity.getReadLocalVariables()
        if len(variables) > 0:
            child_element = ET.SubElement(element, "READ-LOCAL-VARIABLES")
            for access in variables:
                self.writeVariableAccess(child_element, access)

    def setROperationInAtomicSwcInstanceRef(self, element: ET.Element, key: str, iref: ROperationInAtomicSwcInstanceRef):
        if iref is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, iref)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF", iref.getContextRPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-REQUIRED-OPERATION-REF", iref.getTargetRequiredOperationRef())

    def setServerCallPoint(self, element: ET.Element, call_point: ServerCallPoint):
        self.setROperationInAtomicSwcInstanceRef(element, "OPERATION-IREF", call_point.getOperationIRef())
        self.setChildElementOptionalFloatValue(element, "TIMEOUT", call_point.timeout)

    def setSynchronousServerCallPoint(self, element: ET.Element, call_point: SynchronousServerCallPoint):
        child_element = ET.SubElement(element, "SYNCHRONOUS-SERVER-CALL-POINT")
        self.writeIdentifiable(child_element, call_point)
        self.setServerCallPoint(child_element, call_point)

    def setAsynchronousServerCallPoint(self, element: ET.Element, call_point: SynchronousServerCallPoint):
        child_element = ET.SubElement(element, "ASYNCHRONOUS-SERVER-CALL-POINT")
        self.writeIdentifiable(child_element, call_point)
        self.setServerCallPoint(child_element, call_point)

    def writeRunnableEntityServerCallPoints(self, element: ET.Element, entity: RunnableEntity):
        call_points = entity.getServerCallPoints()
        if len(call_points) > 0:
            child_element = ET.SubElement(element, "SERVER-CALL-POINTS")
            for call_point in call_points:
                if isinstance(call_point, SynchronousServerCallPoint):
                    self.setSynchronousServerCallPoint(child_element, call_point)
                elif isinstance(call_point, AsynchronousServerCallPoint):
                    self.setAsynchronousServerCallPoint(child_element, call_point)
                else:
                    self.notImplemented("Unsupported ServerCallPoint type <%s>" % type(call_point))

    def writeRunnableEntityWrittenLocalVariable(self, element: ET.Element, entity: RunnableEntity):
        variables = entity.getWrittenLocalVariables()
        if len(variables) > 0:
            child_element = ET.SubElement(element, "WRITTEN-LOCAL-VARIABLES")
            for access in variables:
                self.writeVariableAccess(child_element, access)

    def writeModeGroupInAtomicSwcInstanceRef(self, element: ET.Element, instance_ref: ModeGroupInAtomicSwcInstanceRef):
        self.setChildElementOptionalRefType(element, "BASE-REF", instance_ref.getBaseRef())
        self.setChildElementOptionalRefType(element, "CONTEXT-PORT-REF", instance_ref.getContextPortRef())

    def writeRModeGroupInAtomicSWCInstanceRef(self, element: ET.Element, instance_ref: RModeGroupInAtomicSWCInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, "R-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF")
            self.writeModeGroupInAtomicSwcInstanceRef(child_element, instance_ref)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF", instance_ref.getContextRPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-MODE-GROUP-REF", instance_ref.getTargetModeGroupRef())

    def writePModeGroupInAtomicSWCInstanceRef(self, element: ET.Element, instance_ref: PModeGroupInAtomicSwcInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, "P-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF")
            self.writeModeGroupInAtomicSwcInstanceRef(child_element, instance_ref)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-P-PORT-REF", instance_ref.getContextPPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-MODE-GROUP-REF", instance_ref.getTargetModeGroupRef())

    def writePTriggerInAtomicSwcTypeInstanceRef(self, element: ET.Element, key: str, instance_ref: PTriggerInAtomicSwcTypeInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-P-PORT-REF", instance_ref.getContextPPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-TRIGGER-REF", instance_ref.getTargetTriggerRef())

    def writeInnerDataPrototypeGroupInCompositionInstanceRef(self, element: ET.Element, key: str, instance_ref: InnerDataPrototypeGroupInCompositionInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, key)
            for ref in instance_ref.getContextSwComponentPrototypeRefs():
                self.setChildElementOptionalRefType(child_element, "CONTEXT-SW-COMPONENT-PROTOTYPE-REF", ref)
            self.setChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-GROUP-REF", instance_ref.getTargetDataPrototypeGroupRef())

    def writeInnerRunnableEntityGroupInCompositionInstanceRef(self, element: ET.Element, key: str, instance_ref: InnerRunnableEntityGroupInCompositionInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, key)
            for ref in instance_ref.getContextSwComponentPrototypeRefs():
                self.setChildElementOptionalRefType(child_element, "CONTEXT-SW-COMPONENT-PROTOTYPE-REF", ref)
            self.setChildElementOptionalRefType(child_element, "TARGET-RUNNABLE-ENTITY-GROUP-REF", instance_ref.getTargetRunnableEntityGroupRef())

    def writeRunnableEntityInCompositionInstanceRef(self, element: ET.Element, key: str, instance_ref: RunnableEntityInCompositionInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, key)
            for ref in instance_ref.getContextSwComponentPrototypeRefs():
                self.setChildElementOptionalRefType(child_element, "CONTEXT-SW-COMPONENT-PROTOTYPE-REF", ref)
            self.setChildElementOptionalRefType(child_element, "TARGET-RUNNABLE-ENTITY-REF", instance_ref.getTargetRunnableEntityRef())

    def writeVariableDataPrototypeInCompositionInstanceRef(self, element: ET.Element, key: str, instance_ref: VariableDataPrototypeInCompositionInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, key)
            for ref in instance_ref.getContextSwComponentPrototypeRefs():
                self.setChildElementOptionalRefType(child_element, "CONTEXT-SW-COMPONENT-PROTOTYPE-REF", ref)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-PORT-PROTOTYPE-REF", instance_ref.getContextPortPrototypeRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-VARIABLE-DATA-PROTOTYPE-REF", instance_ref.getTargetVariableDataPrototypeRef())

    def writeDataPrototypeGroupDataPrototypeGroupIRefs(self, element: ET.Element, data_group: DataPrototypeGroup):
        irefs = data_group.getDataPrototypeGroupIRefs()
        if len(irefs) > 0:
            child_element = ET.SubElement(element, "DATA-PROTOTYPE-GROUP-IREFS")
            for iref in irefs:
                self.writeInnerDataPrototypeGroupInCompositionInstanceRef(child_element, "DATA-PROTOTYPE-GROUP-IREF", iref)

    def writeDataPrototypeGroupImplicitDataAccessIRefs(self, element: ET.Element, data_group: DataPrototypeGroup):
        irefs = data_group.getImplicitDataAccessIRefs()
        if len(irefs) > 0:
            child_element = ET.SubElement(element, "IMPLICIT-DATA-ACCESS-IREFS")
            for iref in irefs:
                self.writeVariableDataPrototypeInCompositionInstanceRef(child_element, "IMPLICIT-DATA-ACCESS-IREF", iref)

    def writeDataPrototypeGroup(self, element: ET.Element, data_group: DataPrototypeGroup):
        self.logger.debug("writeDataPrototypeGroup %s" % data_group.getShortName())
        child_element = ET.SubElement(element, "DATA-PROTOTYPE-GROUP")
        self.writeIdentifiable(child_element, data_group)
        self.writeDataPrototypeGroupDataPrototypeGroupIRefs(child_element, data_group)
        self.writeDataPrototypeGroupImplicitDataAccessIRefs(child_element, data_group)

    def writeRunnableEntityGroupRunnableEntityGroupIRefs(self, element: ET.Element, runnable_group: RunnableEntityGroup):
        irefs = runnable_group.getRunnableEntityGroupIRefs()
        if len(irefs) > 0:
            child_element = ET.SubElement(element, "RUNNABLE-ENTITY-GROUP-IREFS")
            for iref in irefs:
                self.writeInnerRunnableEntityGroupInCompositionInstanceRef(child_element, "RUNNABLE-ENTITY-GROUP-IREF", iref)

    def writeRunnableEntityGroupRunnableEntityIRefs(self, element: ET.Element, runnable_group: RunnableEntityGroup):
        irefs = runnable_group.getRunnableEntityIRefs()
        if len(irefs) > 0:
            child_element = ET.SubElement(element, "RUNNABLE-ENTITY-IREFS")
            for iref in irefs:
                self.writeRunnableEntityInCompositionInstanceRef(child_element, "RUNNABLE-ENTITY-IREF", iref)

    def writeRunnableEntityGroup(self, element: ET.Element, runnable_group: RunnableEntityGroup):
        self.logger.debug("writeRunnableEntityGroup %s" % runnable_group.getShortName())
        child_element = ET.SubElement(element, "RUNNABLE-ENTITY-GROUP")
        self.writeIdentifiable(child_element, runnable_group)
        self.writeRunnableEntityGroupRunnableEntityGroupIRefs(child_element, runnable_group)
        self.writeRunnableEntityGroupRunnableEntityIRefs(child_element, runnable_group)

    def writeConsistencyNeedsDpgDoesNotRequireCoherencys(self, element: ET.Element, consistency_needs: ConsistencyNeeds):
        if len(consistency_needs.getDpgDoesNotRequireCoherencys()) > 0:
            child_element = ET.SubElement(element, "DPG-DOES-NOT-REQUIRE-COHERENCYS")
            for data_group in consistency_needs.getDpgDoesNotRequireCoherencys():
                self.writeDataPrototypeGroup(child_element, data_group)

    def writeConsistencyNeedsDpgRequiresCoherencys(self, element: ET.Element, consistency_needs: ConsistencyNeeds):
        if len(consistency_needs.getDpgRequiresCoherencys()) > 0:
            child_element = ET.SubElement(element, "DPG-REQUIRES-COHERENCYS")
            for data_group in consistency_needs.getDpgRequiresCoherencys():
                self.writeDataPrototypeGroup(child_element, data_group)

    def writeConsistencyNeedsRegDoesNotRequireStabilitys(self, element: ET.Element, consistency_needs: ConsistencyNeeds):
        if len(consistency_needs.getRegDoesNotRequireStabilitys()) > 0:
            child_element = ET.SubElement(element, "REG-DOES-NOT-REQUIRE-STABILITYS")
            for runnable_group in consistency_needs.getRegDoesNotRequireStabilitys():
                self.writeRunnableEntityGroup(child_element, runnable_group)

    def writeConsistencyNeedsRegRequiresStabilitys(self, element: ET.Element, consistency_needs: ConsistencyNeeds):
        if len(consistency_needs.getRegRequiresStabilitys()) > 0:
            child_element = ET.SubElement(element, "REG-REQUIRES-STABILITYS")
            for runnable_group in consistency_needs.getRegRequiresStabilitys():
                self.writeRunnableEntityGroup(child_element, runnable_group)

    def writeConsistencyNeeds(self, element: ET.Element, consistency_needs: ConsistencyNeeds):
        self.logger.debug("writeConsistencyNeeds %s" % consistency_needs.getShortName())
        child_element = ET.SubElement(element, "CONSISTENCY-NEEDS")
        self.writeIdentifiable(child_element, consistency_needs)
        self.writeConsistencyNeedsDpgDoesNotRequireCoherencys(child_element, consistency_needs)
        self.writeConsistencyNeedsDpgRequiresCoherencys(child_element, consistency_needs)
        self.writeConsistencyNeedsRegDoesNotRequireStabilitys(child_element, consistency_needs)
        self.writeConsistencyNeedsRegRequiresStabilitys(child_element, consistency_needs)

    def setPModeGroupInAtomicSwcInstanceRef(self, element: ET.Element, key: str, instance_ref: PModeGroupInAtomicSwcInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, key)
            self.writeModeGroupInAtomicSwcInstanceRef(child_element, instance_ref)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-P-PORT-REF", instance_ref.getContextPPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-MODE-GROUP-REF", instance_ref.getTargetModeGroupRef())

    def setModeGroupIRef(self, element: ET.Element, key: str, instance_ref: ModeGroupInAtomicSwcInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, key)
            if isinstance(instance_ref, PModeGroupInAtomicSwcInstanceRef):
                self.writePModeGroupInAtomicSWCInstanceRef(child_element, instance_ref)
            elif isinstance(instance_ref, RModeGroupInAtomicSWCInstanceRef):
                self.writeRModeGroupInAtomicSWCInstanceRef(child_element, instance_ref)
            else:
                self.notImplemented("Unsupported Mode Group IRef <%s>" % type(instance_ref))
        return instance_ref

    def writeModeAccessPoint(self, element: ET.Element, point: ModeAccessPoint):
        if point is not None:
            child_element = ET.SubElement(element, "MODE-ACCESS-POINT")
            self.writeARObjectAttributes(child_element, point)
            self.setModeGroupIRef(child_element, "MODE-GROUP-IREF", point.getModeGroupIRef())

    def writeRunnableEntityExternalTriggeringPoints(self, element: ET.Element, entity: RunnableEntity):
        points = entity.getExternalTriggeringPoints()
        if len(points) > 0:
            points_tag = ET.SubElement(element, "EXTERNAL-TRIGGERING-POINTS")
            for point in points:
                child_element = ET.SubElement(points_tag, "EXTERNAL-TRIGGERING-POINT")
                ident = point.getIdent()
                if ident is not None:
                    ident_element = ET.SubElement(child_element, "IDENT")
                    self.writeIdentifiable(ident_element, ident)
                trigger = point.getTrigger()
                if trigger is not None:
                    self.writePTriggerInAtomicSwcTypeInstanceRef(child_element, "TRIGGER-IREF", trigger)

    def writeRunnableEntityModeAccessPoints(self, element: ET.Element, entity: RunnableEntity):
        points = entity.getModeAccessPoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "MODE-ACCESS-POINTS")
            for point in points:
                if isinstance(point, ModeAccessPoint):
                    self.writeModeAccessPoint(child_element, point)
                else:
                    self.notImplemented("Unsupported Mode Access Points <%s>" % type(point))

    def writeModeSwitchPointModeGroupIRef(self, element: ET.Element, point: ModeSwitchPoint):
        if point is not None:
            child_element = ET.SubElement(element, "MODE-GROUP-IREF")
            instance_ref = point.getModeGroupIRef()
            self.setChildElementOptionalRefType(child_element, "CONTEXT-P-PORT-REF", instance_ref.getContextPPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-MODE-GROUP-REF", instance_ref.getTargetModeGroupRef())

    def writeModeSwitchPoint(self, element: ET.Element, point: ModeSwitchPoint):
        if point is not None:
            child_element = ET.SubElement(element, "MODE-SWITCH-POINT")
            self.writeIdentifiable(child_element, point)
            self.writeModeSwitchPointModeGroupIRef(child_element, point)

    def writeRunnableEntityModeSwitchPoints(self, element: ET.Element, entity: RunnableEntity):
        points = entity.getModeSwitchPoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "MODE-SWITCH-POINTS")
            for point in points:
                if isinstance(point, ModeSwitchPoint):
                    self.writeModeSwitchPoint(child_element, point)
                else:
                    self.notImplemented("unsupported Mode Switch Point <%s>" % type(point))

    def setRunnableEntityArgument(self, element: ET.Element, argument: RunnableEntityArgument):
        child_element = ET.SubElement(element, "RUNNABLE-ENTITY-ARGUMENT")
        self.setChildElementOptionalLiteral(child_element, "SYMBOL", argument.getSymbol())

    def writeRunnableEntityArguments(self, element: ET.Element, entity: RunnableEntity):
        arguments = entity.getArguments()
        if len(arguments) > 0:
            child_element = ET.SubElement(element, "ARGUMENTS")
            for argument in arguments:
                if isinstance(argument, RunnableEntityArgument):
                    self.setRunnableEntityArgument(child_element, argument)
                else:
                    self.notImplemented("Unsupported argument of Runnable Entity <%s>" % type(argument))

    def writeRunnableEntityWaitPoints(self, element: ET.Element, entity: RunnableEntity):
        points = entity.getWaitPoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "WAIT-POINTS")
            for point in points:
                if isinstance(point, WaitPoint):
                    wp_element = ET.SubElement(child_element, "WAIT-POINT")
                    self.writeIdentifiable(wp_element, point)
                    self.setChildElementOptionalTimeValue(wp_element, "TIMEOUT", point.getTimeout())
                    self.setChildElementOptionalRefType(wp_element, "TRIGGER", point.getTriggerRef())
                else:
                    self.notImplemented("Unsupported WaitPoint <%s>" % type(point))

    def writeRunnableEntityAsynchronousServerCallResultPoint(self, element: ET.Element, entity: RunnableEntity):
        points = entity.getAsynchronousServerCallResultPoints()
        if len(points) > 0:
            points_tag = ET.SubElement(element, "ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS")
            for point in points:
                child_element = ET.SubElement(points_tag, "ASYNCHRONOUS-SERVER-CALL-RESULT-POINT")
                self.writeIdentifiable(child_element, point)
                self.setChildElementOptionalRefType(child_element, "ASYNCHRONOUS-SERVER-CALL-POINT-REF", point.getAsynchronousServerCallPointRef())

    def writeRunnableEntity(self, element: ET.Element, entity: RunnableEntity):
        if entity is not None:
            child_element = ET.SubElement(element, "RUNNABLE-ENTITY")
            self.writeExecutableEntity(child_element, entity)
            self.writeRunnableEntityArguments(child_element, entity)
            self.writeRunnableEntityAsynchronousServerCallResultPoint(child_element, entity)
            self.setChildElementOptionalBooleanValue(child_element, "CAN-BE-INVOKED-CONCURRENTLY", entity.getCanBeInvokedConcurrently())
            self.writeRunnableEntityDataReadAccesses(child_element, entity)
            self.writeRunnableEntityDataReceivePointByArguments(child_element, entity)
            self.writeRunnableEntityDataReceivePointByValues(child_element, entity)
            self.writeRunnableEntityDataSendPoints(child_element, entity)
            self.writeRunnableEntityDataWriteAccesses(child_element, entity)
            self.writeRunnableEntityModeAccessPoints(child_element, entity)
            self.writeRunnableEntityModeSwitchPoints(child_element, entity)
            self.writeRunnableEntityExternalTriggeringPoints(child_element, entity)
            self.writeRunnableEntityParameterAccesses(child_element, entity)
            self.writeRunnableEntityReadLocalVariables(child_element, entity)
            self.writeRunnableEntityServerCallPoints(child_element, entity)
            self.setChildElementOptionalLiteral(child_element, "SYMBOL", entity.symbol)
            self.writeRunnableEntityWaitPoints(child_element, entity)
            self.writeRunnableEntityWrittenLocalVariable(child_element, entity)

    def writeSwcInternalBehaviorRunnables(self, element: ET.Element, behavior: SwcInternalBehavior):
        entities = behavior.getRunnableEntities()
        if len(entities) > 0:
            runnables_tag = ET.SubElement(element, "RUNNABLES")
            for entity in entities:
                if isinstance(entity, RunnableEntity):
                    self.writeRunnableEntity(runnables_tag, entity)
                else:
                    self.notImplemented("Unsupported RunnableEntity <%s>" % type(entity))

    def writeSwcInternalBehaviorArTypedPerInstanceMemories(self, element: ET.Element, behavior: SwcInternalBehavior):
        prototypes = behavior.getArTypedPerInstanceMemories()
        if len(prototypes) > 0:
            child_element = ET.SubElement(element, "AR-TYPED-PER-INSTANCE-MEMORYS")
            for prototype in prototypes:
                if isinstance(prototype, VariableDataPrototype):
                    self.writeVariableDataPrototype(child_element, prototype)
                else:
                    self.notImplemented("Unsupported ArTypedPerInstanceMemories <%s>" % type(prototype))

    def writeSwcInternalBehaviorExplicitInterRunnableVariables(self, element: ET.Element, behavior: SwcInternalBehavior):
        prototypes = behavior.getExplicitInterRunnableVariables()
        if len(prototypes) > 0:
            child_element = ET.SubElement(element, "EXPLICIT-INTER-RUNNABLE-VARIABLES")
            for prototype in prototypes:
                if isinstance(prototype, VariableDataPrototype):
                    self.writeVariableDataPrototype(child_element, prototype)
                else:
                    self.notImplemented("Unsupported ExplicitInterRunnableVariables <%s>" % type(prototype))

    def writeSwcInternalBehaviorPerInstanceMemories(self, element: ET.Element, behavior: SwcInternalBehavior):
        memories = behavior.getPerInstanceMemories()
        if len(memories) > 0:
            memories_tag = ET.SubElement(element, "PER-INSTANCE-MEMORYS")
            for memory in memories:
                child_element = ET.SubElement(memories_tag, "PER-INSTANCE-MEMORY")
                self.writeIdentifiable(child_element, memory)
                self.setChildElementOptionalLiteral(child_element, "INIT-VALUE", memory.getInitValue())
                self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", memory.getSwDataDefProps())
                self.setChildElementOptionalLiteral(child_element, "TYPE", memory.getType())
                self.setChildElementOptionalLiteral(child_element, "TYPE-DEFINITION", memory.getTypeDefinition())

    def writeParameterDataPrototype(self, element: ET.Element, prototype: ParameterDataPrototype):
        child_element = ET.SubElement(element, "PARAMETER-DATA-PROTOTYPE")
        self.writeAutosarDataPrototype(child_element, prototype)
        self.setChildValueSpecification(child_element, "INIT-VALUE", prototype.getInitValue())

    def writeSwcInternalBehaviorParameterDataPrototypes(self, element: ET.Element, key: str, parameters: List[ParameterDataPrototype]):
        if len(parameters) > 0:
            child_element = ET.SubElement(element, key)
            for parameter in parameters:
                self.writeParameterDataPrototype(child_element, parameter)

    def writeVariationPointProxy(self, element: ET.Element, proxy: VariationPointProxy):
        child_element = ET.SubElement(element, "VARIATION-POINT-PROXY")
        self.writeIdentifiable(child_element, proxy)
        self.writeConditionByFormula(child_element, proxy.getConditionAccess(), "CONDITION-ACCESS")
        self.setChildElementOptionalRefType(child_element, "IMPLEMENTATION-DATA-TYPE-REF", proxy.getImplementationDataTypeRef())
        self.setChildElementOptionalRefType(child_element, "POST-BUILD-VALUE-ACCESS-REF", proxy.getPostBuildValueAccessRef())
        conditions = proxy.getPostBuildVariantConditions()
        if len(conditions) > 0:
            conditions_tag = ET.SubElement(child_element, "POST-BUILD-VARIANT-CONDITIONS")
            for condition in conditions:
                self.writePostBuildVariantCondition(conditions_tag, condition)
        value_access = proxy.getValueAccess()
        if value_access is not None:
            value_access_element = ET.SubElement(child_element, "VALUE-ACCESS")
            tag = VALUE_ACCESS_CLASS_TO_TAG.get(type(value_access))
            if tag is not None:
                sub_element = ET.SubElement(value_access_element, tag)
                self.writeAttributeValueVariationPoint(sub_element, value_access)
            else:
                self.notImplemented("Unsupported VALUE-ACCESS type <%s>" % type(value_access).__name__)

    def writeAttributeValueVariationPoint(self, element: ET.Element, avp: AttributeValueVariationPoint):
        self.writeARObjectAttributes(element, avp)
        binding_time = avp.getBindingTime()
        if binding_time is not None:
            token = BINDING_TIME_XML_MAP.get(binding_time.getValue())
            if token is None:
                self.notImplemented("Unsupported BINDING-TIME <%s>" % binding_time.getValue())
            else:
                element.attrib["BINDING-TIME"] = token
        blueprint_value = avp.getBlueprintValue()
        if blueprint_value is not None:
            element.attrib["BLUEPRINT-VALUE"] = blueprint_value.getValue()
        sd = avp.getSd()
        if sd is not None:
            element.attrib["SD"] = sd.getValue()
        short_label = avp.getShortLabel()
        if short_label is not None:
            element.attrib["SHORT-LABEL"] = short_label.getValue()
        if isinstance(avp, LimitValueVariationPoint):
            interval_type = avp.getIntervalType()
            if interval_type is not None:
                token = INTERVAL_TYPE_XML_MAP.get(interval_type.getValue())
                if token is None:
                    self.notImplemented("Unsupported INTERVAL-TYPE <%s>" % interval_type.getValue())
                else:
                    element.attrib["INTERVAL-TYPE"] = token
        text = avp.getText()
        if text is not None:
            element.text = text

    def writeTimingDescriptionEventChain(self, element: ET.Element, chain: TimingDescriptionEventChain):
        self.writeIdentifiable(element, chain)
        self.setChildElementOptionalBooleanValue(element, "IS-PIPELINING-PERMITTED", chain.getIsPipeliningPermitted())
        self.setChildElementOptionalRefType(element, "STIMULUS-REF", chain.getStimulusRef())
        self.setChildElementOptionalRefType(element, "RESPONSE-REF", chain.getResponseRef())
        segments = chain.getSegmentRefs()
        if len(segments) > 0:
            segments_tag = ET.SubElement(element, "SEGMENT-REFS")
            for segment in segments:
                self.setChildElementOptionalRefType(segments_tag, "SEGMENT-REF", segment)

    def writeTimingDescriptionEvent(self, element: ET.Element, event: TimingDescriptionEvent):
        self.writeIdentifiable(element, event)
        self.setChildElementOptionalRefType(element, "CLOCK-REFERENCE-REF", event.getClockReferenceRef())
        expression = event.getOccurrenceExpression()
        if expression is not None:
            self.writeTDEventOccurrenceExpression(ET.SubElement(element, "OCCURRENCE-EXPRESSION"), expression)

    def writeTDEventCom(self, element: ET.Element, event: "TDEventCom"):
        self.writeTimingDescriptionEvent(element, event)
        self.setChildElementOptionalRefType(element, "ECU-INSTANCE-REF", event.getEcuInstanceRef())

    def writeTDEventCycleStart(self, element: ET.Element, event: "TDEventCycleStart"):
        self.writeTDEventCom(element, event)
        self.setChildElementOptionalIntegerValue(element, "CYCLE-REPETITION", event.getCycleRepetition())

    def writeTDEventFrClusterCycleStart(self, element: ET.Element, event: "TDEventFrClusterCycleStart"):
        self.writeTDEventCycleStart(element, event)
        self.setChildElementOptionalRefType(element, "FR-CLUSTER-REF", event.getFrClusterRef())

    def writeTDEventTTCanCycleStart(self, element: ET.Element, event: "TDEventTTCanCycleStart"):
        self.writeTDEventCycleStart(element, event)
        self.setChildElementOptionalRefType(element, "TT-CAN-CLUSTER-REF", event.getTtCanClusterRef())

    def writeTDEventISignal(self, element: ET.Element, event: "TDEventISignal"):
        self.writeTDEventCom(element, event)
        self.setChildElementOptionalRefType(element, "I-SIGNAL-REF", event.getISignalRef())
        self.setChildElementOptionalRefType(element, "PHYSICAL-CHANNEL-REF", event.getPhysicalChannelRef())
        enum = event.getTdEventType()
        if enum is not None:
            self.setChildElementOptionalLiteral(element, "TD-EVENT-TYPE", enum)

    def writeTDEventIPdu(self, element: ET.Element, event: "TDEventIPdu"):
        self.writeTDEventCom(element, event)
        self.setChildElementOptionalRefType(element, "I-PDU-REF", event.getIPduRef())
        self.setChildElementOptionalRefType(element, "PHYSICAL-CHANNEL-REF", event.getPhysicalChannelRef())
        enum = event.getTdEventType()
        if enum is not None:
            self.setChildElementOptionalLiteral(element, "TD-EVENT-TYPE", enum)

    def writeTDEventFrame(self, element: ET.Element, event: "TDEventFrame"):
        self.writeTDEventCom(element, event)
        self.setChildElementOptionalRefType(element, "FRAME-REF", event.getFrameRef())
        self.setChildElementOptionalRefType(element, "PHYSICAL-CHANNEL-REF", event.getPhysicalChannelRef())
        enum = event.getTdEventType()
        if enum is not None:
            self.setChildElementOptionalLiteral(element, "TD-EVENT-TYPE", enum)

    def writeTDHeaderIdRange(self, element: ET.Element, header_id_range: "TDHeaderIdRange"):
        self.setChildElementOptionalIntegerValue(element, "MAX-HEADER-ID", header_id_range.getMaxHeaderId())
        self.setChildElementOptionalIntegerValue(element, "MIN-HEADER-ID", header_id_range.getMinHeaderId())

    def writeTDEventFrameEthernet(self, element: ET.Element, event: "TDEventFrameEthernet"):
        self.writeTDEventCom(element, event)
        self.setChildElementOptionalRefType(element, "STATIC-SOCKET-CONNECTION-REF", event.getStaticSocketConnectionRef())
        enum = event.getTdEventType()
        if enum is not None:
            self.setChildElementOptionalLiteral(element, "TD-EVENT-TYPE", enum)
        ranges = event.getTdHeaderIdFilter()
        if len(ranges) > 0:
            filters_element = ET.SubElement(element, "TD-HEADER-ID-FILTERS")
            for header_id_range in ranges:
                range_tag = ET.SubElement(filters_element, "TD-HEADER-ID-RANGE")
                self.writeTDHeaderIdRange(range_tag, header_id_range)
        refs = event.getTdPduTriggeringFilterRefs()
        if len(refs) > 0:
            refs_element = ET.SubElement(element, "TD-PDU-TRIGGERING-FILTER-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_element, "TD-PDU-TRIGGERING-FILTER-REF", ref)

    def writeTDEventVfb(self, element: ET.Element, event: TDEventVfb):
        self.writeTimingDescriptionEvent(element, event)
        self.writeEOCComponentIRef(element, event.getComponentIRef())

    def writeTDEventVfbReference(self, element: ET.Element, event: TDEventVfbReference):
        self.writeTDEventVfb(element, event)
        self.setChildElementOptionalRefType(element, "REFERENCED-TD-EVENT-VFB-REF", event.getReferencedTDEventVfbRef())

    def writeTDEventVfbPort(self, element: ET.Element, event: TDEventVfbPort):
        self.writeTDEventVfb(element, event)
        self.setChildElementOptionalBooleanValue(element, "IS-EXTERNAL", event.getIsExternal())
        self.setChildElementOptionalRefType(element, "PORT-REF", event.getPortRef())
        self.setChildElementOptionalRefType(element, "PORT-PROTOTYPE-BLUEPRINT-REF", event.getPortPrototypeBlueprintRef())

    def writeTDEventVariableDataPrototype(self, element: ET.Element, event: TDEventVariableDataPrototype):
        self.writeTDEventVfbPort(element, event)
        self.setChildElementOptionalRefType(element, "DATA-ELEMENT-REF", event.getDataElementRef())
        enum = event.getTdEventVariableDataPrototypeType()
        if enum is not None:
            self.setChildElementOptionalLiteral(element, "TD-EVENT-VARIABLE-DATA-PROTOTYPE-TYPE", enum)

    def writeTDEventOperation(self, element: ET.Element, event: TDEventOperation):
        self.writeTDEventVfbPort(element, event)
        self.setChildElementOptionalRefType(element, "OPERATION-REF", event.getOperationRef())
        enum = event.getTdEventOperationType()
        if enum is not None:
            self.setChildElementOptionalLiteral(element, "TD-EVENT-OPERATION-TYPE", enum)

    def writeTDEventModeDeclaration(self, element: ET.Element, event: TDEventModeDeclaration):
        self.writeTDEventVfbPort(element, event)
        self.setChildElementOptionalRefType(element, "ENTRY-MODE-DECLARATION-REF", event.getEntryModeDeclarationRef())
        self.setChildElementOptionalRefType(element, "EXIT-MODE-DECLARATION-REF", event.getExitModeDeclarationRef())
        self.setChildElementOptionalRefType(element, "MODE-DECLARATION-REF", event.getModeDeclarationRef())
        enum = event.getTdEventModeDeclarationType()
        if enum is not None:
            self.setChildElementOptionalLiteral(element, "TD-EVENT-MODE-DECLARATION-TYPE", enum)

    def writeTDEventTrigger(self, element: ET.Element, event: TDEventTrigger):
        self.writeTDEventVfbPort(element, event)
        self.setChildElementOptionalRefType(element, "TRIGGER-REF", event.getTriggerRef())
        enum = event.getTdEventTriggerType()
        if enum is not None:
            self.setChildElementOptionalLiteral(element, "TD-EVENT-TRIGGER-TYPE", enum)

    def writeTDEventSwc(self, element: ET.Element, event: TDEventSwc):
        self.writeTimingDescriptionEvent(element, event)
        self.writeEOCComponentIRef(element, event.getComponentIRef())

    def writeTDEventSwcInternalBehavior(self, element: ET.Element, event: TDEventSwcInternalBehavior):
        self.writeTDEventSwc(element, event)
        self.setChildElementOptionalRefType(element, "RUNNABLE-REF", event.getRunnableRef())
        enum = event.getTdEventSwcInternalBehaviorType()
        if enum is not None:
            self.setChildElementOptionalLiteral(element, "TD-EVENT-SWC-INTERNAL-BEHAVIOR-TYPE", enum)
        self.setChildElementOptionalRefType(element, "VARIABLE-ACCESS-REF", event.getVariableAccessRef())

    def writeTDEventSwcInternalBehaviorReference(self, element: ET.Element, event: TDEventSwcInternalBehaviorReference):
        self.writeTDEventSwc(element, event)
        self.setChildElementOptionalRefType(element, "REFERENCED-TD-EVENT-SWC-REF", event.getReferencedTDEventSwcRef())

    def writeTDEventBswInternalBehavior(self, element: ET.Element, event: TDEventBswInternalBehavior):
        self.writeTimingDescriptionEvent(element, event)
        self.setChildElementOptionalRefType(element, "BSW-MODULE-ENTITY-REF", event.getBswModuleEntityRef())
        enum = event.getTdEventBswInternalBehaviorType()
        if enum is not None:
            self.setChildElementOptionalLiteral(element, "TD-EVENT-BSW-INTERNAL-BEHAVIOR-TYPE", enum)

    def writeTDEventBsw(self, element: ET.Element, event: TDEventBsw):
        self.writeTimingDescriptionEvent(element, event)
        self.setChildElementOptionalRefType(element, "BSW-MODULE-DESCRIPTION-REF", event.getBswModuleDescriptionRef())

    def writeTDEventBswModule(self, element: ET.Element, event: TDEventBswModule):
        self.writeTDEventBsw(element, event)
        self.setChildElementOptionalRefType(element, "BSW-MODULE-ENTRY-REF", event.getBswModuleEntryRef())
        enum = event.getTdEventBswModuleType()
        if enum is not None:
            self.setChildElementOptionalLiteral(element, "TD-EVENT-BSW-MODULE-TYPE", enum)

    def writeTDEventBswModeDeclaration(self, element: ET.Element, event: TDEventBswModeDeclaration):
        self.writeTDEventBsw(element, event)
        self.setChildElementOptionalRefType(element, "ENTRY-MODE-DECLARATION-REF", event.getEntryModeDeclarationRef())
        self.setChildElementOptionalRefType(element, "EXIT-MODE-DECLARATION-REF", event.getExitModeDeclarationRef())
        self.setChildElementOptionalRefType(element, "MODE-DECLARATION-REF", event.getModeDeclarationRef())
        enum = event.getTdEventBswModeDeclarationType()
        if enum is not None:
            self.setChildElementOptionalLiteral(element, "TD-EVENT-BSW-MODE-DECLARATION-TYPE", enum)

    def writeTDEventComplex(self, element: ET.Element, event: TDEventComplex):
        self.writeTimingDescriptionEvent(element, event)

    def writeTDEventSLLET(self, element: ET.Element, event: TDEventSLLET):
        self.writeTimingDescriptionEvent(element, event)

    def writeTDEventSLLETPort(self, element: ET.Element, event: TDEventSLLETPort):
        self.writeTDEventSLLET(element, event)
        self.setChildElementOptionalRefType(element, "PORT-REF", event.getPortRef())

    def writeTDEventOccurrenceExpression(self, element: ET.Element, expression: TDEventOccurrenceExpression):
        self.writeARObjectAttributes(element, expression)
        arguments = expression.getArguments()
        if len(arguments) > 0:
            arguments_tag = ET.SubElement(element, "ARGUMENTS")
            for argument in arguments:
                argument_tag = ET.SubElement(arguments_tag, "AUTOSAR-OPERATION-ARGUMENT-INSTANCE")
                self.writeAutosarOperationArgumentInstance(argument_tag, argument)
        formula = expression.getFormula()
        if formula is not None:
            self.writeTDEventOccurrenceExpressionFormula(ET.SubElement(element, "FORMULA"), formula)
        modes = expression.getModes()
        if len(modes) > 0:
            modes_tag = ET.SubElement(element, "MODES")
            for mode in modes:
                mode_tag = ET.SubElement(modes_tag, "TIMING-MODE-INSTANCE")
                self.writeTimingModeInstance(mode_tag, mode)
        variables = expression.getVariables()
        if len(variables) > 0:
            variables_tag = ET.SubElement(element, "VARIABLES")
            for variable in variables:
                variable_tag = ET.SubElement(variables_tag, "AUTOSAR-VARIABLE-INSTANCE")
                self.writeAutosarVariableInstance(variable_tag, variable)

    def writeTDEventOccurrenceExpressionFormula(self, element: ET.Element, formula: TDEventOccurrenceExpressionFormula):
        self.writeReferrable(element, formula)
        self.setChildElementOptionalRefType(element, "ARGUMENT-REF", formula.getArgumentRef())
        self.setChildElementOptionalRefType(element, "EVENT-REF", formula.getEventRef())
        self.setChildElementOptionalRefType(element, "MODE-REF", formula.getModeRef())
        self.setChildElementOptionalRefType(element, "VARIABLE-REF", formula.getVariableRef())
        text = formula.getText()
        if text is not None:
            element.text = text

    def writeTimingConditionFormula(self, element: ET.Element, tcf: TimingConditionFormula):
        self.writeReferrable(element, tcf)
        self.setChildElementOptionalRefType(element, "TIMING-ARGUMENT-REF", tcf.getTimingArgumentRef())
        self.setChildElementOptionalRefType(element, "TIMING-CONDITION-REF", tcf.getTimingConditionRef())
        self.setChildElementOptionalRefType(element, "TIMING-EVENT-REF", tcf.getTimingEventRef())
        self.setChildElementOptionalRefType(element, "TIMING-MODE-REF", tcf.getTimingModeRef())
        self.setChildElementOptionalRefType(element, "TIMING-VARIABLE-REF", tcf.getTimingVariableRef())
        text = tcf.getText()
        if text is not None:
            element.text = text

    def writeTimingCondition(self, element: ET.Element, condition: TimingCondition):
        self.writeIdentifiable(element, condition)
        formula = condition.getTimingConditionFormula()
        if formula is not None:
            self.writeTimingConditionFormula(ET.SubElement(element, "TIMING-CONDITION-FORMULA"), formula)

    def writeConfidenceInterval(self, element: ET.Element, interval: ConfidenceInterval):
        self.writeARObjectAttributes(element, interval)
        self.setMultidimensionalTime(element, "LOWER-BOUND", interval.getLowerBound())
        self.setChildElementOptionalFloatValue(element, "PROPABILITY", interval.getPropability())
        self.setMultidimensionalTime(element, "UPPER-BOUND", interval.getUpperBound())

    def writeModeInBswInstanceRef(self, element: ET.Element, iref: ModeInBswInstanceRef):
        self.writeARObjectAttributes(element, iref)
        self.setChildElementOptionalRefType(element, "CONTEXT-BSW-IMPLEMENTATION-REF", iref.getContextBswImplementationRef())
        self.setChildElementOptionalRefType(element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF", iref.getContextModeDeclarationGroupPrototypeRef())
        self.setChildElementOptionalRefType(element, "TARGET-MODE-DECLARATION-REF", iref.getTargetModeDeclarationRef())

    def writeModeInSwcInstanceRef(self, element: ET.Element, iref: ModeInSwcInstanceRef):
        self.writeARObjectAttributes(element, iref)
        for component_ref in iref.getContextComponentRefs():
            self.setChildElementOptionalRefType(element, "CONTEXT-COMPONENT-REF", component_ref)
        self.setChildElementOptionalRefType(element, "CONTEXT-PORT-REF", iref.getContextPortRef())
        self.setChildElementOptionalRefType(element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF", iref.getContextModeDeclarationGroupPrototypeRef())
        self.setChildElementOptionalRefType(element, "TARGET-MODE-DECLARATION-REF", iref.getTargetModeDeclarationRef())

    def writeTimingModeInstance(self, element: ET.Element, instance: TimingModeInstance):
        self.writeIdentifiable(element, instance)
        mode_instance = instance.getModeInstance()
        if mode_instance is not None:
            mode_instance_tag = ET.SubElement(element, "MODE-INSTANCE")
            if isinstance(mode_instance, ModeInBswInstanceRef):
                self.writeModeInBswInstanceRef(ET.SubElement(mode_instance_tag, "MODE-IN-BSW-INSTANCE-REF"), mode_instance)
            elif isinstance(mode_instance, ModeInSwcInstanceRef):
                self.writeModeInSwcInstanceRef(ET.SubElement(mode_instance_tag, "MODE-IN-SWC-INSTANCE-REF"), mode_instance)
            else:
                self.notImplemented("Unsupported TimingModeInstance.modeInstance <%s>" % type(mode_instance).__name__)

    def writeTimingExtensionResource(self, element: ET.Element, resource: TimingExtensionResource):
        self.writeIdentifiable(element, resource)
        arguments = resource.getTimingArguments()
        if len(arguments) > 0:
            arguments_tag = ET.SubElement(element, "TIMING-ARGUMENTS")
            for argument in arguments:
                argument_tag = ET.SubElement(arguments_tag, "AUTOSAR-OPERATION-ARGUMENT-INSTANCE")
                self.writeAutosarOperationArgumentInstance(argument_tag, argument)
        modes = resource.getTimingModes()
        if len(modes) > 0:
            modes_tag = ET.SubElement(element, "TIMING-MODES")
            for mode in modes:
                mode_tag = ET.SubElement(modes_tag, "TIMING-MODE-INSTANCE")
                self.writeTimingModeInstance(mode_tag, mode)
        variables = resource.getTimingVariables()
        if len(variables) > 0:
            variables_tag = ET.SubElement(element, "TIMING-VARIABLES")
            for variable in variables:
                variable_tag = ET.SubElement(variables_tag, "AUTOSAR-VARIABLE-INSTANCE")
                self.writeAutosarVariableInstance(variable_tag, variable)

    def writeAutosarOperationArgumentInstance(self, element: ET.Element, instance: AutosarOperationArgumentInstance):
        self.writeIdentifiable(element, instance)
        iref = instance.getOperationArgumentInstanceIRef()
        if iref is not None:
            iref_tag = ET.SubElement(element, "OPERATION-ARGUMENT-INSTANCE-IREF")
            self.writeOperationArgumentInComponentInstanceRef(iref_tag, iref)

    def writeComponentInCompositionInstanceRef(self, element: ET.Element, iref: ComponentInCompositionInstanceRef):
        for context_component_ref in iref.getContextComponentRefs():
            self.setChildElementOptionalRefType(element, "CONTEXT-COMPONENT-REF", context_component_ref)
        self.setChildElementOptionalRefType(element, "TARGET-COMPONENT-REF", iref.getTargetComponentRef())

    def writeOperationArgumentInComponentInstanceRef(self, element: ET.Element, iref: OperationArgumentInComponentInstanceRef):
        for context_component_ref in iref.getContextComponentRefs():
            self.setChildElementOptionalRefType(element, "CONTEXT-COMPONENT-REF", context_component_ref)
        self.setChildElementOptionalRefType(element, "CONTEXT-PORT-PROTOTYPE-REF", iref.getContextPortPrototypeRef())
        self.setChildElementOptionalRefType(element, "CONTEXT-OPERATION-REF", iref.getContextOperationRef())
        self.setChildElementOptionalRefType(element, "ROOT-ARGUMENT-DATA-PROTOTYPE-REF", iref.getRootArgumentDataPrototypeRef())
        for context_data_prototype_ref in iref.getContextDataPrototypeRefs():
            self.setChildElementOptionalRefType(element, "CONTEXT-DATA-PROTOTYPE-REF", context_data_prototype_ref)
        self.setChildElementOptionalRefType(element, "TARGET-DATA-PROTOTYPE-REF", iref.getTargetDataPrototypeRef())

    def writeAutosarVariableInstance(self, element: ET.Element, instance: AutosarVariableInstance):
        self.writeIdentifiable(element, instance)
        iref = instance.getVariableInstanceIRef()
        if iref is not None:
            iref_tag = ET.SubElement(element, "VARIABLE-INSTANCE-IREF")
            self.writeVariableInComponentInstanceRef(iref_tag, iref)

    def writeVariableInComponentInstanceRef(self, element: ET.Element, iref: VariableInComponentInstanceRef):
        for context_component_ref in iref.getContextComponentRefs():
            self.setChildElementOptionalRefType(element, "CONTEXT-COMPONENT-REF", context_component_ref)
        self.setChildElementOptionalRefType(element, "CONTEXT-PORT-PROTOTYPE-REF", iref.getContextPortPrototypeRef())
        self.setChildElementOptionalRefType(element, "ROOT-VARIABLE-DATA-PROTOTYPE-REF", iref.getRootVariableDataPrototypeRef())
        for context_data_prototype_ref in iref.getContextDataPrototypeRefs():
            self.setChildElementOptionalRefType(element, "CONTEXT-DATA-PROTOTYPE-REF", context_data_prototype_ref)
        self.setChildElementOptionalRefType(element, "TARGET-DATA-PROTOTYPE-REF", iref.getTargetDataPrototypeRef())

    def writeTimingConstraint(self, element: ET.Element, constraint: TimingConstraint):
        self.writeIdentifiable(element, constraint)
        self.writeTraceable(element, constraint)
        self.setChildElementOptionalRefType(element, "TIMING-CONDITION-REF", constraint.getTimingConditionRef())

    def writeSynchronizationTimingConstraint(self, element: ET.Element, constraint: SynchronizationTimingConstraint):
        self.logger.debug("writeSynchronizationTimingConstraint %s" % constraint.getShortName())
        self.writeTimingConstraint(element, constraint)
        self.setChildElementOptionalLiteral(element, "EVENT-OCCURRENCE-KIND", constraint.getEventOccurrenceKind())
        scope_events = constraint.getScopeEvents()
        if len(scope_events) > 0:
            refs_tag = ET.SubElement(element, "SCOPE-EVENT-REFS")
            for scope_event in scope_events:
                self.setChildElementOptionalRefType(refs_tag, "SCOPE-EVENT-REF", scope_event)
        scopes = constraint.getScopes()
        if len(scopes) > 0:
            refs_tag = ET.SubElement(element, "SCOPE-REFS")
            for scope in scopes:
                self.setChildElementOptionalRefType(refs_tag, "SCOPE-REF", scope)
        self.setChildElementOptionalLiteral(element, "SYNCHRONIZATION-CONSTRAINT-TYPE", constraint.getSynchronizationConstraintType())
        self.setMultidimensionalTime(element, "TOLERANCE", constraint.getTolerance())

    def writeLatencyTimingConstraint(self, element: ET.Element, constraint: LatencyTimingConstraint):
        self.logger.debug("writeLatencyTimingConstraint %s" % constraint.getShortName())
        self.writeTimingConstraint(element, constraint)
        self.setChildElementOptionalLiteral(element, "LATENCY-CONSTRAINT-TYPE", constraint.getLatencyConstraintType())
        self.setChildElementOptionalRefType(element, "SCOPE-REF", constraint.getScopeRef())
        self.setMultidimensionalTime(element, "MINIMUM", constraint.getMinimum())
        self.setMultidimensionalTime(element, "MAXIMUM", constraint.getMaximum())
        self.setMultidimensionalTime(element, "NOMINAL", constraint.getNominal())

    def writeOffsetTimingConstraint(self, element: ET.Element, constraint: OffsetTimingConstraint):
        self.logger.debug("writeOffsetTimingConstraint %s" % constraint.getShortName())
        self.writeTimingConstraint(element, constraint)
        self.setChildElementOptionalRefType(element, "SOURCE-REF", constraint.getSourceRef())
        self.setChildElementOptionalRefType(element, "TARGET-REF", constraint.getTargetRef())
        self.setMultidimensionalTime(element, "MINIMUM", constraint.getMinimum())
        self.setMultidimensionalTime(element, "MAXIMUM", constraint.getMaximum())

    def writeAgeConstraint(self, element: ET.Element, constraint: AgeConstraint):
        self.logger.debug("writeAgeConstraint %s" % constraint.getShortName())
        self.writeTimingConstraint(element, constraint)
        self.setMultidimensionalTime(element, "MAXIMUM", constraint.getMaximum())
        self.setMultidimensionalTime(element, "MINIMUM", constraint.getMinimum())
        self.setChildElementOptionalRefType(element, "SCOPE-REF", constraint.getScopeRef())

    def writeExecutionTimeConstraint(self, element: ET.Element, constraint: ExecutionTimeConstraint):
        self.logger.debug("writeExecutionTimeConstraint %s" % constraint.getShortName())
        self.writeTimingConstraint(element, constraint)
        self.writeEOCComponentIRef(element, constraint.getComponentIRef())
        self.setChildElementOptionalRefType(element, "EXECUTABLE-REF", constraint.getExecutableRef())
        self.setChildElementOptionalLiteral(element, "EXECUTION-TIME-TYPE", constraint.getExecutionTimeType())
        self.setMultidimensionalTime(element, "MAXIMUM", constraint.getMaximum())
        self.setMultidimensionalTime(element, "MINIMUM", constraint.getMinimum())

    def writeSynchronizationPointConstraint(self, element: ET.Element, constraint: SynchronizationPointConstraint):
        self.logger.debug("writeSynchronizationPointConstraint %s" % constraint.getShortName())
        self.writeTimingConstraint(element, constraint)
        source_eec_refs = constraint.getSourceEecRefs()
        if len(source_eec_refs) > 0:
            refs_tag = ET.SubElement(element, "SOURCE-EEC-REFS")
            for source_eec_ref in source_eec_refs:
                self.setChildElementOptionalRefType(refs_tag, "SOURCE-EEC-REF", source_eec_ref)
        source_event_refs = constraint.getSourceEventRefs()
        if len(source_event_refs) > 0:
            refs_tag = ET.SubElement(element, "SOURCE-EVENT-REFS")
            for source_event_ref in source_event_refs:
                self.setChildElementOptionalRefType(refs_tag, "SOURCE-EVENT-REF", source_event_ref)
        target_eec_refs = constraint.getTargetEecRefs()
        if len(target_eec_refs) > 0:
            refs_tag = ET.SubElement(element, "TARGET-EEC-REFS")
            for target_eec_ref in target_eec_refs:
                self.setChildElementOptionalRefType(refs_tag, "TARGET-EEC-REF", target_eec_ref)
        target_event_refs = constraint.getTargetEventRefs()
        if len(target_event_refs) > 0:
            refs_tag = ET.SubElement(element, "TARGET-EVENT-REFS")
            for target_event_ref in target_event_refs:
                self.setChildElementOptionalRefType(refs_tag, "TARGET-EVENT-REF", target_event_ref)

    def writeEventTriggeringConstraint(self, element: ET.Element, constraint: EventTriggeringConstraint):
        self.writeTimingConstraint(element, constraint)
        self.setChildElementOptionalRefType(element, "EVENT-REF", constraint.getEventRef())

    def writePeriodicEventTriggering(self, element: ET.Element, constraint: PeriodicEventTriggering):
        self.logger.debug("writePeriodicEventTriggering %s" % constraint.getShortName())
        self.writeEventTriggeringConstraint(element, constraint)
        self.setMultidimensionalTime(element, "MINIMUM-INTER-ARRIVAL-TIME", constraint.getMinimumInterArrivalTime())
        self.setMultidimensionalTime(element, "JITTER", constraint.getJitter())
        self.setMultidimensionalTime(element, "PERIOD", constraint.getPeriod())

    def writeSporadicEventTriggering(self, element: ET.Element, constraint: SporadicEventTriggering):
        self.logger.debug("writeSporadicEventTriggering %s" % constraint.getShortName())
        self.writeEventTriggeringConstraint(element, constraint)
        self.setMultidimensionalTime(element, "MINIMUM-INTER-ARRIVAL-TIME", constraint.getMinimumInterArrivalTime())
        self.setMultidimensionalTime(element, "MAXIMUM-INTER-ARRIVAL-TIME", constraint.getMaximumInterArrivalTime())
        self.setMultidimensionalTime(element, "JITTER", constraint.getJitter())
        self.setMultidimensionalTime(element, "PERIOD", constraint.getPeriod())

    def writeConcretePatternEventTriggering(self, element: ET.Element, constraint: ConcretePatternEventTriggering):
        self.logger.debug("writeConcretePatternEventTriggering %s" % constraint.getShortName())
        self.writeEventTriggeringConstraint(element, constraint)
        self.setMultidimensionalTime(element, "PATTERN-JITTER", constraint.getPatternJitter())
        self.setMultidimensionalTime(element, "PATTERN-PERIOD", constraint.getPatternPeriod())
        offsets = constraint.getOffsets()
        if len(offsets) > 0:
            offsets_tag = ET.SubElement(element, "OFFSETS")
            for offset in offsets:
                self.setMultidimensionalTime(offsets_tag, "TIME-VALUE", offset)
        self.setMultidimensionalTime(element, "PATTERN-LENGTH", constraint.getPatternLength())

    def writeBurstPatternEventTriggering(self, element: ET.Element, constraint: BurstPatternEventTriggering):
        self.logger.debug("writeBurstPatternEventTriggering %s" % constraint.getShortName())
        self.writeEventTriggeringConstraint(element, constraint)
        self.setChildElementOptionalPositiveInteger(element, "MAX-NUMBER-OF-OCCURRENCES", constraint.getMaxNumberOfOccurrences())
        self.setMultidimensionalTime(element, "MINIMUM-INTER-ARRIVAL-TIME", constraint.getMinimumInterArrivalTime())
        self.setMultidimensionalTime(element, "PATTERN-JITTER", constraint.getPatternJitter())
        self.setMultidimensionalTime(element, "PATTERN-LENGTH", constraint.getPatternLength())
        self.setMultidimensionalTime(element, "PATTERN-PERIOD", constraint.getPatternPeriod())
        self.setChildElementOptionalPositiveInteger(element, "MIN-NUMBER-OF-OCCURRENCES", constraint.getMinNumberOfOccurrences())

    def writeArbitraryEventTriggering(self, element: ET.Element, constraint: ArbitraryEventTriggering):
        self.logger.debug("writeArbitraryEventTriggering %s" % constraint.getShortName())
        self.writeEventTriggeringConstraint(element, constraint)
        minimum_distances = constraint.getMinimumDistances()
        if len(minimum_distances) > 0:
            minimum_distances_tag = ET.SubElement(element, "MINIMUM-DISTANCES")
            for distance in minimum_distances:
                self.setMultidimensionalTime(minimum_distances_tag, "TIME-VALUE", distance)
        maximum_distances = constraint.getMaximumDistances()
        if len(maximum_distances) > 0:
            maximum_distances_tag = ET.SubElement(element, "MAXIMUM-DISTANCES")
            for distance in maximum_distances:
                self.setMultidimensionalTime(maximum_distances_tag, "TIME-VALUE", distance)
        confidence_intervals = constraint.getConfidenceIntervals()
        if len(confidence_intervals) > 0:
            confidence_intervals_tag = ET.SubElement(element, "CONFIDENCE-INTERVALS")
            for interval in confidence_intervals:
                self.writeConfidenceInterval(ET.SubElement(confidence_intervals_tag, "CONFIDENCE-INTERVAL"), interval)

    def writeTimingClock(self, element: ET.Element, clock: TimingClock):
        self.writeIdentifiable(element, clock)
        platform_time_base_ref = clock.getPlatformTimeBaseRef()
        if platform_time_base_ref is not None:
            time_bases_tag = ET.SubElement(element, "PLATFORM-TIME-BASES")
            conditional_tag = ET.SubElement(time_bases_tag, "GLOBAL-TIME-DOMAIN-REF-CONDITIONAL")
            self.setChildElementOptionalRefType(conditional_tag, "GLOBAL-TIME-DOMAIN-REF", platform_time_base_ref)

    def writeTDLETZoneClock(self, element: ET.Element, clock: TDLETZoneClock):
        self.writeTimingClock(element, clock)
        self.setMultidimensionalTime(element, "ACCURACY-EXT", clock.getAccuracyExt())
        self.setMultidimensionalTime(element, "ACCURACY-INT", clock.getAccuracyInt())

    def writeTimingClockSyncAccuracy(self, element: ET.Element, sync_accuracy: TimingClockSyncAccuracy):
        self.writeIdentifiable(element, sync_accuracy)
        self.setMultidimensionalTime(element, "ACCURACY", sync_accuracy.getAccuracy())
        self.setChildElementOptionalRefType(element, "LOWER-REF", sync_accuracy.getLowerRef())
        self.setChildElementOptionalRefType(element, "UPPER-REF", sync_accuracy.getUpperRef())

    def setEOCExecutableEntityRefSuccessorRefs(self, element: ET.Element, successor_refs: List[RefType]):
        if len(successor_refs) > 0:
            child_element = ET.SubElement(element, "SUCCESSOR-REFS")
            for successor_ref in successor_refs:
                self.setChildElementOptionalRefType(child_element, "SUCCESSOR-REF", successor_ref)

    def writeEOCExecutableEntityRefAbstract(self, element: ET.Element, obj: EOCExecutableEntityRefAbstract):
        direct_successor_refs = obj.getDirectSuccessorRefs()
        if len(direct_successor_refs) > 0:
            refs_tag = ET.SubElement(element, "DIRECT-SUCCESSOR-REFS")
            for direct_successor_ref in direct_successor_refs:
                self.setChildElementOptionalRefType(refs_tag, "DIRECT-SUCCESSOR-REF", direct_successor_ref)

    def writeEOCComponentIRef(self, element: ET.Element, component_iref: Optional[ComponentInCompositionInstanceRef]):
        if component_iref is not None:
            iref_tag = ET.SubElement(element, "COMPONENT-IREF")
            self.writeComponentInCompositionInstanceRef(iref_tag, component_iref)

    def writeEOCExecutableEntityRef(self, element: ET.Element, entity_ref: EOCExecutableEntityRef):
        child_element = ET.SubElement(element, "EOC-EXECUTABLE-ENTITY-REF")
        self.writeIdentifiable(child_element, entity_ref)
        self.writeEOCExecutableEntityRefAbstract(child_element, entity_ref)
        self.setChildElementOptionalRefType(child_element, "BSW-MODULE-INSTANCE-REF", entity_ref.getBswModuleInstanceRef())
        self.writeEOCComponentIRef(child_element, entity_ref.getComponentIRef())
        self.setChildElementOptionalRefType(child_element, "EXECUTABLE-REF", entity_ref.getExecutableRef())
        self.setEOCExecutableEntityRefSuccessorRefs(child_element, entity_ref.getSuccessorRefs())

    def writeEOCEventRef(self, element: ET.Element, event_ref: EOCEventRef):
        child_element = ET.SubElement(element, "EOC-EVENT-REF")
        self.writeIdentifiable(child_element, event_ref)
        self.writeEOCExecutableEntityRefAbstract(child_element, event_ref)
        self.setChildElementOptionalRefType(child_element, "BSW-MODULE-INSTANCE-REF", event_ref.getBswModuleInstanceRef())
        self.writeEOCComponentIRef(child_element, event_ref.getComponentIRef())
        self.setChildElementOptionalRefType(child_element, "EVENT-REF", event_ref.getEventRef())
        self.setEOCExecutableEntityRefSuccessorRefs(child_element, event_ref.getSuccessorRefs())

    def writeEOCExecutableEntityRefGroup(self, element: ET.Element, group: EOCExecutableEntityRefGroup):
        child_element = ET.SubElement(element, "EOC-EXECUTABLE-ENTITY-REF-GROUP")
        self.writeIdentifiable(child_element, group)
        self.writeEOCExecutableEntityRefAbstract(child_element, group)
        self.setChildElementOptionalLiteral(child_element, "LET-DATA-EXCHANGE-PARADIGM", group.getLetDataExchangeParadigm())
        let_interval_refs = group.getLetIntervalRefs()
        if len(let_interval_refs) > 0:
            refs_tag = ET.SubElement(child_element, "LET-INTERVAL-REFS")
            for let_interval_ref in let_interval_refs:
                self.setChildElementOptionalRefType(refs_tag, "LET-INTERVAL-REF", let_interval_ref)
        self.setChildElementOptionalPositiveInteger(child_element, "MAX-CYCLE-REPETITIONS", group.getMaxCycleRepetitions())
        self.setChildElementOptionalIntegerValue(child_element, "MAX-CYCLES", group.getMaxCycles())
        self.setChildElementOptionalIntegerValue(child_element, "MAX-SLOTS", group.getMaxSlots())
        self.setChildElementOptionalPositiveInteger(child_element, "MAX-SLOTS-PER-CYCLE", group.getMaxSlotsPerCycle())
        nested_element_refs = group.getNestedElementRefs()
        if len(nested_element_refs) > 0:
            refs_tag = ET.SubElement(child_element, "NESTED-ELEMENT-REFS")
            for nested_element_ref in nested_element_refs:
                self.setChildElementOptionalRefType(refs_tag, "NESTED-ELEMENT-REF", nested_element_ref)
        self.setEOCExecutableEntityRefSuccessorRefs(child_element, group.getSuccessorRefs())
        self.setChildElementOptionalRefType(child_element, "TRIGGERING-EVENT-REF", group.getTriggeringEventRef())

    def writeSwcInternalBehaviorVariationPointProxies(self, element: ET.Element, behavior: SwcInternalBehavior):
        proxies = behavior.getVariationPointProxies()
        if len(proxies) > 0:
            proxies_tag = ET.SubElement(element, "VARIATION-POINT-PROXYS")
            for proxy in proxies:
                self.writeVariationPointProxy(proxies_tag, proxy)

    def writePortDefinedArgumentValues(self, element: ET.Element, argument_values: List[PortDefinedArgumentValue]):
        if len(argument_values) > 0:
            child_element = ET.SubElement(element, "PORT-ARG-VALUES")
            for argument_value in argument_values:
                child_element = ET.SubElement(child_element, "PORT-DEFINED-ARGUMENT-VALUE")
                if argument_value.getValue() is not None:
                    self.setChildValueSpecification(child_element, "VALUE", argument_value.getValue())
                self.setChildElementOptionalRefType(child_element, "VALUE-TYPE-TREF", argument_value.getValueTypeTRef())

    def writeSwcInternalBehaviorPortAPIOptions(self, element: ET.Element, behavior: SwcInternalBehavior):
        options = behavior.getPortAPIOptions()
        if len(options) > 0:
            port_api_options_tag = ET.SubElement(element, "PORT-API-OPTIONS")
            for option in options:
                child_element = ET.SubElement(port_api_options_tag, "PORT-API-OPTION")
                self.setChildElementOptionalBooleanValue(child_element, "ENABLE-TAKE-ADDRESS", option.getEnableTakeAddress())
                self.setChildElementOptionalLiteral(child_element, "ERROR-HANDLING", option.getErrorHandling())
                self.setChildElementOptionalBooleanValue(child_element, "INDIRECT-API", option.getIndirectAPI())
                self.writePortDefinedArgumentValues(child_element, option.getPortArgValues())
                self.setChildElementOptionalRefType(child_element, "PORT-REF", option.getPortRef())

    def writeRoleBasedDataTypeAssignment(self, element: ET.Element, assignment: RoleBasedDataTypeAssignment):
        child_element = ET.SubElement(element, "ROLE-BASED-DATA-TYPE-ASSIGNMENT")
        self.setChildElementOptionalLiteral(child_element, "ROLE", assignment.getRole())
        self.setChildElementOptionalRefType(child_element, "USED-IMPLEMENTATION-DATA-TYPE-REF", assignment.getUsedImplementationDataTypeRef())

    def writeServiceDependencyAssignedDataType(self, element: ET.Element, dependency: ServiceDependency):
        assigned_data = dependency.getAssignedDataType()
        if assigned_data is not None:
            child_element = ET.SubElement(element, "ASSIGNED-DATA-TYPES")
            if isinstance(assigned_data, RoleBasedDataTypeAssignment):
                self.writeRoleBasedDataTypeAssignment(child_element, assigned_data)
            else:
                self.notImplemented("Unsupported Assigned Data <%s>" % type(assigned_data))

    def writeServiceDependency(self, element: ET.Element, dependency: ServiceDependency):
        self.writeIdentifiable(element, dependency)
        self.writeServiceDependencyAssignedDataType(element, dependency)
        self.setChildElementOptionalLiteral(element, "DIAGNOSTIC-RELEVANCE", dependency.getDiagnosticRelevance())
        self.writeSymbolicNameProps(element, dependency)

    def writeSymbolicNameProps(self, element: ET.Element, dependency: ServiceDependency):
        props = dependency.getSymbolicNameProps()
        if props is None:
            return
        child_element = ET.SubElement(element, "SYMBOLIC-NAME-PROPS")
        self.writeImplementationProps(child_element, props)

    def writeBswServiceDependencyIdent(self, element: ET.Element, ident: BswServiceDependencyIdent):
        child_element = ET.SubElement(element, "IDENT")
        self.writeIdentifiable(child_element, ident)

    def writeRoleBasedBswModuleEntryAssignment(self, element: ET.Element, assignment: RoleBasedBswModuleEntryAssignment):
        child_element = ET.SubElement(element, "ROLE-BASED-BSW-MODULE-ENTRY-ASSIGNMENT")
        self.writeARObjectAttributes(child_element, assignment)
        self.setChildElementOptionalRefType(child_element, "ASSIGNED-ENTRY-REF", assignment.getAssignedEntryRef())
        self.setChildElementOptionalLiteral(child_element, "ROLE", assignment.getRole())

    def writeBswServiceDependencyAssignedData(self, element: ET.Element, dependency: BswServiceDependency):
        assigned_data = dependency.getAssignedData()
        if len(assigned_data) > 0:
            child_element = ET.SubElement(element, "ASSIGNED-DATAS")
            for data in assigned_data:
                if isinstance(data, RoleBasedDataAssignment):
                    self.writeRoleBasedDataAssignment(child_element, data)
                else:
                    self.notImplemented("Unsupported Assigned Data <%s>" % type(data))

    def writeBswServiceDependencyAssignedEntryRoles(self, element: ET.Element, dependency: BswServiceDependency):
        assigned_entry_roles = dependency.getAssignedEntryRole()
        if len(assigned_entry_roles) > 0:
            child_element = ET.SubElement(element, "ASSIGNED-ENTRY-ROLES")
            for assignment in assigned_entry_roles:
                if isinstance(assignment, RoleBasedBswModuleEntryAssignment):
                    self.writeRoleBasedBswModuleEntryAssignment(child_element, assignment)
                else:
                    self.notImplemented("Unsupported Assigned Entry Role <%s>" % type(assignment))

    def writeBswServiceDependencyServiceNeeds(self, element: ET.Element, dependency: BswServiceDependency):
        needs = dependency.getServiceNeeds()
        if needs is None:
            return
        child_element = ET.SubElement(element, "SERVICE-NEEDS")
        if isinstance(needs, BswMgrNeeds):
            self.writeBswMgrNeeds(child_element, needs)
        elif isinstance(needs, NvBlockNeeds):
            self.writeNvBlockNeeds(child_element, needs)
        elif isinstance(needs, DiagnosticCommunicationManagerNeeds):
            self.writeDiagnosticCommunicationManagerNeeds(child_element, needs)
        elif isinstance(needs, DiagnosticRoutineNeeds):
            self.writeDiagnosticRoutineNeeds(child_element, needs)
        elif isinstance(needs, DiagnosticValueNeeds):
            self.writeDiagnosticValueNeeds(child_element, needs)
        elif isinstance(needs, DiagnosticEventNeeds):
            self.writeDiagnosticEventNeeds(child_element, needs)
        elif isinstance(needs, DiagnosticEventInfoNeeds):
            self.writeDiagnosticEventInfoNeeds(child_element, needs)
        elif isinstance(needs, DiagnosticIoControlNeeds):
            self.writeDiagnosticIoControlNeeds(child_element, needs)
        elif isinstance(needs, DiagnosticEnableConditionNeeds):
            self.writeDiagnosticEnableConditionNeeds(child_element, needs)
        elif isinstance(needs, DiagnosticOperationCycleNeeds):
            self.writeDiagnosticOperationCycleNeeds(child_element, needs)
        elif isinstance(needs, DiagnosticStorageConditionNeeds):
            self.writeDiagnosticStorageConditionNeeds(child_element, needs)
        elif isinstance(needs, IndicatorStatusNeeds):
            self.writeIndicatorStatusNeeds(child_element, needs)
        elif isinstance(needs, FunctionInhibitionAvailabilityNeeds):
            self.writeFunctionInhibitionAvailabilityNeeds(child_element, needs)
        elif isinstance(needs, CryptoServiceNeeds):
            self.writeCryptoServiceNeeds(child_element, needs)
        elif isinstance(needs, EcuStateMgrUserNeeds):
            self.writeEcuStateMgrUserNeeds(child_element, needs)
        elif isinstance(needs, DtcStatusChangeNotificationNeeds):
            self.writeDtcStatusChangeNotificationNeeds(child_element, needs)
        elif isinstance(needs, DltUserNeeds):
            self.writeDltUserNeeds(child_element, needs)
        elif isinstance(needs, ComMgrUserNeeds):
            self.writeComMgrUserNeeds(child_element, needs)
        elif isinstance(needs, SupervisedEntityNeeds):
            self.writeSupervisedEntityNeeds(child_element, needs)
        elif isinstance(needs, ErrorTracerNeeds):
            self.writeErrorTracerNeeds(child_element, needs)
        elif isinstance(needs, ObdInfoServiceNeeds):
            self.writeObdInfoServiceNeeds(child_element, needs)
        elif isinstance(needs, ObdMonitorServiceNeeds):
            self.writeObdMonitorServiceNeeds(child_element, needs)
        elif isinstance(needs, ObdPidServiceNeeds):
            self.writeObdPidServiceNeeds(child_element, needs)
        elif isinstance(needs, ObdControlServiceNeeds):
            self.writeObdControlServiceNeeds(child_element, needs)
        elif isinstance(needs, ObdRatioServiceNeeds):
            self.writeObdRatioServiceNeeds(child_element, needs)
        elif isinstance(needs, ObdRatioDenominatorNeeds):
            self.writeObdRatioDenominatorNeeds(child_element, needs)
        elif isinstance(needs, DoIpRoutingActivationAuthenticationNeeds):
            self.writeDoIpRoutingActivationAuthenticationNeeds(child_element, needs)
        elif isinstance(needs, DoIpRoutingActivationConfirmationNeeds):
            self.writeDoIpRoutingActivationConfirmationNeeds(child_element, needs)
        elif isinstance(needs, SecureOnBoardCommunicationNeeds):
            self.writeSecureOnBoardCommunicationNeeds(child_element, needs)
        elif isinstance(needs, IdsMgrNeeds):
            self.writeIdsMgrNeeds(child_element, needs)
        else:
            self.notImplemented("Unsupported service needs <%s>" % type(needs))

    def writeBswServiceDependency(self, element: ET.Element, dependency: BswServiceDependency):
        child_element = ET.SubElement(element, "BSW-SERVICE-DEPENDENCY")
        self.writeARObjectAttributes(child_element, dependency)
        ident = dependency.getIdent()
        if ident is not None:
            self.writeBswServiceDependencyIdent(child_element, ident)
        self.writeServiceDependencyAssignedDataType(child_element, dependency)
        self.writeBswServiceDependencyAssignedData(child_element, dependency)
        self.writeBswServiceDependencyAssignedEntryRoles(child_element, dependency)
        self.writeBswServiceDependencyServiceNeeds(child_element, dependency)
        self.writeSymbolicNameProps(child_element, dependency)

    def writeBswInternalBehaviorServiceDependencies(self, element: ET.Element, behavior: BswInternalBehavior):
        dependencies = behavior.getServiceDependencies()
        if len(dependencies) > 0:
            child_element = ET.SubElement(element, "SERVICE-DEPENDENCYS")
            for dependency in dependencies:
                if isinstance(dependency, BswServiceDependency):
                    self.writeBswServiceDependency(child_element, dependency)
                else:
                    self.notImplemented("Unsupported ServiceDependency <%s>" % type(dependency))

    def writeRoleBasedDataAssignment(self, element: ET.Element, assignment: RoleBasedDataAssignment):
        child_element = ET.SubElement(element, "ROLE-BASED-DATA-ASSIGNMENT")
        self.setChildElementOptionalLiteral(child_element, "ROLE", assignment.role)
        self.setAutosarVariableRef(child_element, "USED-DATA-ELEMENT", assignment.getUsedDataElement())
        self.setAutosarParameterRef(child_element, "USED-PARAMETER-ELEMENT", assignment.getUsedParameterElement())
        self.setChildElementOptionalRefType(child_element, "USED-PIM-REF", assignment.getUsedPimRef())

    def writeRoleBasedPortAssignment(self, element: ET.Element, assignment: RoleBasedPortAssignment):
        child_element = ET.SubElement(element, "ROLE-BASED-PORT-ASSIGNMENT")
        self.writeARObjectAttributes(child_element, assignment)
        self.setChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF", assignment.portPrototypeRef)
        self.setChildElementOptionalLiteral(child_element, "ROLE", assignment.role)

    def writeSwcServiceDependencyAssignedData(self, element: ET.Element, dependency: SwcServiceDependency):
        assigned_data = dependency.getAssignedData()
        if len(assigned_data) > 0:
            child_element = ET.SubElement(element, "ASSIGNED-DATAS")
            for data in assigned_data:
                if isinstance(data, RoleBasedDataAssignment):
                    self.writeRoleBasedDataAssignment(child_element, data)
                else:
                    self.notImplemented("Unsupported Assigned Data <%s>" % type(data))

    def writeSwcServiceDependencyAssignedPorts(self, element: ET.Element, dependency: SwcServiceDependency):
        assigned_data = dependency.getAssignedPorts()
        if len(assigned_data) > 0:
            child_element = ET.SubElement(element, "ASSIGNED-PORTS")
            for data in assigned_data:
                if isinstance(data, RoleBasedPortAssignment):
                    self.writeRoleBasedPortAssignment(child_element, data)
                else:
                    self.notImplemented("Unsupported Assigned Data <%s>" % type(data))

    def writeServiceNeeds(self, element: ET.Element, needs: ServiceNeeds):
        self.writeIdentifiable(element, needs)

    def writeBswMgrNeeds(self, element: ET.Element, needs: BswMgrNeeds):
        child_element = ET.SubElement(element, "BSW-MGR-NEEDS")
        self.writeServiceNeeds(child_element, needs)

    def writeNvBlockNeeds(self, element: ET.Element, needs: NvBlockNeeds):
        child_element = ET.SubElement(element, "NV-BLOCK-NEEDS")
        self.logger.debug("write NvBlockNeeds %s" % needs.getShortName())
        self.writeServiceNeeds(child_element, needs)
        self.setChildElementOptionalBooleanValue(child_element, "CALC-RAM-BLOCK-CRC", needs.getCalcRamBlockCrc())
        self.setChildElementOptionalBooleanValue(child_element, "CHECK-STATIC-BLOCK-ID", needs.getCheckStaticBlockId())
        self.setChildElementOptionalNumericalValue(child_element, "N-DATA-SETS", needs.getNDataSets())
        self.setChildElementOptionalNumericalValue(child_element, "N-ROM-BLOCKS", needs.getNRomBlocks())
        self.setChildElementOptionalLiteral(child_element, "RAM-BLOCK-STATUS-CONTROL", needs.getRamBlockStatusControl())
        self.setChildElementOptionalBooleanValue(child_element, "READONLY", needs.getReadonly())
        self.setChildElementOptionalLiteral(child_element, "RELIABILITY", needs.getReliability())
        self.setChildElementOptionalBooleanValue(child_element, "RESISTANT-TO-CHANGED-SW", needs.getResistantToChangedSw())
        self.setChildElementOptionalBooleanValue(child_element, "RESTORE-AT-START", needs.getRestoreAtStart())
        self.setChildElementOptionalBooleanValue(child_element, "STORE-AT-SHUTDOWN", needs.getStoreAtShutdown())
        self.setChildElementOptionalBooleanValue(child_element, "STORE-CYCLIC", needs.getStoreCyclic())
        self.setChildElementOptionalBooleanValue(child_element, "STORE-EMERGENCY", needs.getStoreEmergency())
        self.setChildElementOptionalBooleanValue(child_element, "STORE-IMMEDIATE", needs.getStoreImmediate())
        self.setChildElementOptionalBooleanValue(child_element, "USE-AUTO-VALIDATION-AT-SHUT-DOWN", needs.getUseAutoValidationAtShutDown())
        self.setChildElementOptionalBooleanValue(child_element, "USE-CRC-COMP-MECHANISM", needs.getUseCRCCompMechanism())
        self.setChildElementOptionalBooleanValue(child_element, "WRITE-ONLY-ONCE", needs.getWriteOnlyOnce())
        self.setChildElementOptionalBooleanValue(child_element, "WRITE-VERIFICATION", needs.getWriteVerification())
        self.setChildElementOptionalPositiveInteger(child_element, "WRITING-FREQUENCY", needs.getWritingFrequency())
        self.setChildElementOptionalLiteral(child_element, "WRITING-PRIORITY", needs.getWritingPriority())

    def writeDiagnosticCapabilityElement(self, element: ET.Element, needs: DiagnosticCapabilityElement):
        self.writeServiceNeeds(element, needs)

    def writeDiagnosticCommunicationManagerNeeds(self, element: ET.Element, needs: DiagnosticCommunicationManagerNeeds):
        child_element = ET.SubElement(element, "DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS")
        self.logger.debug("write DiagnosticCommunicationManagerNeeds %s" % needs.getShortName())
        self.writeDiagnosticCapabilityElement(child_element, needs)
        self.setChildElementOptionalLiteral(child_element, "SERVICE-REQUEST-CALLBACK-TYPE", needs.getServiceRequestCallbackType())

    def writeDiagnosticRoutineNeeds(self, element: ET.Element, needs: DiagnosticRoutineNeeds):
        child_element = ET.SubElement(element, "DIAGNOSTIC-ROUTINE-NEEDS")
        self.logger.debug("write DiagnosticRoutineNeeds %s" % needs.getShortName())
        self.writeDiagnosticCapabilityElement(child_element, needs)
        self.setChildElementOptionalLiteral(child_element, "DIAG-ROUTINE-TYPE", needs.getDiagRoutineType())
        self.setChildElementOptionalIntegerValue(child_element, "RID-NUMBER", needs.getRidNumber())

    def writeDiagnosticValueNeeds(self, element: ET.Element, needs: DiagnosticValueNeeds):
        child_element = ET.SubElement(element, "DIAGNOSTIC-VALUE-NEEDS")
        self.logger.debug("write DiagnosticValueNeeds %s" % needs.getShortName())
        self.writeDiagnosticCapabilityElement(child_element, needs)
        self.setChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH", needs.getDataLength())
        self.setChildElementOptionalLiteral(child_element, "DIAGNOSTIC-VALUE-ACCESS", needs.getDiagnosticValueAccess())
        self.setChildElementOptionalIntegerValue(child_element, "DID-NUMBER", needs.getDidNumber())
        self.setChildElementOptionalBooleanValue(child_element, "FIXED-LENGTH", needs.getFixedLength())
        self.setChildElementOptionalLiteral(child_element, "PROCESSING-STYLE", needs.getProcessingStyle())

    def writeObdInfoServiceNeeds(self, element: ET.Element, needs: ObdInfoServiceNeeds):
        child_element = ET.SubElement(element, "OBD-INFO-SERVICE-NEEDS")
        self.logger.debug("write ObdInfoServiceNeeds %s" % needs.getShortName())
        self.writeDiagnosticCapabilityElement(child_element, needs)

    def writeObdMonitorServiceNeeds(self, element: ET.Element, needs: ObdMonitorServiceNeeds):
        child_element = ET.SubElement(element, "OBD-MONITOR-SERVICE-NEEDS")
        self.logger.debug("write ObdMonitorServiceNeeds %s" % needs.getShortName())
        self.writeDiagnosticCapabilityElement(child_element, needs)
        self.setChildElementOptionalRefType(child_element, "APPLICATION-DATA-TYPE-REF", needs.getApplicationDataTypeRef())
        self.setChildElementOptionalRefType(child_element, "EVENT-NEEDS-REF", needs.getEventNeedsRef())
        self.setChildElementOptionalPositiveInteger(child_element, "UNIT-AND-SCALING-ID", needs.getUnitAndScalingId())
        self.setChildElementOptionalLiteral(child_element, "UPDATE-KIND", needs.getUpdateKind())

    def writeObdPidServiceNeeds(self, element: ET.Element, needs: ObdPidServiceNeeds):
        child_element = ET.SubElement(element, "OBD-PID-SERVICE-NEEDS")
        self.logger.debug("write ObdPidServiceNeeds %s" % needs.getShortName())
        self.writeDiagnosticCapabilityElement(child_element, needs)

    def writeObdControlServiceNeeds(self, element: ET.Element, needs: ObdControlServiceNeeds):
        child_element = ET.SubElement(element, "OBD-CONTROL-SERVICE-NEEDS")
        self.logger.debug("write ObdControlServiceNeeds %s" % needs.getShortName())
        self.writeDiagnosticCapabilityElement(child_element, needs)

    def writeObdRatioServiceNeeds(self, element: ET.Element, needs: ObdRatioServiceNeeds):
        child_element = ET.SubElement(element, "OBD-RATIO-SERVICE-NEEDS")
        self.logger.debug("write ObdRatioServiceNeeds %s" % needs.getShortName())
        self.writeDiagnosticCapabilityElement(child_element, needs)
        self.setChildElementOptionalLiteral(child_element, "CONNECTION-TYPE", needs.getConnectionType())
        self.setChildElementOptionalRefType(child_element, "RATE-BASED-MONITORED-EVENT-REF", needs.getRateBasedMonitoredEventRef())
        self.setChildElementOptionalRefType(child_element, "USED-FID-REF", needs.getUsedFidRef())

    def writeObdRatioDenominatorNeeds(self, element: ET.Element, needs: ObdRatioDenominatorNeeds):
        child_element = ET.SubElement(element, "OBD-RATIO-DENOMINATOR-NEEDS")
        self.logger.debug("write ObdRatioDenominatorNeeds %s" % needs.getShortName())
        self.writeServiceNeeds(child_element, needs)
        self.setChildElementOptionalLiteral(child_element, "DENOMINATOR-CONDITION", needs.getDenominatorCondition())

    def writeDoIpRoutingActivationAuthenticationNeeds(self, element: ET.Element, needs: DoIpRoutingActivationAuthenticationNeeds):
        child_element = ET.SubElement(element, "DO-IP-ROUTING-ACTIVATION-AUTHENTICATION-NEEDS")
        self.logger.debug("write DoIpRoutingActivationAuthenticationNeeds %s" % needs.getShortName())
        self.writeServiceNeeds(child_element, needs)
        self.setChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH-REQUEST", needs.getDataLengthRequest())
        self.setChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH-RESPONSE", needs.getDataLengthResponse())
        self.setChildElementOptionalLiteral(child_element, "ROUTING-ACTIVATION-TYPE", needs.getRoutingActivationType())

    def writeDoIpRoutingActivationConfirmationNeeds(self, element: ET.Element, needs: DoIpRoutingActivationConfirmationNeeds):
        child_element = ET.SubElement(element, "DO-IP-ROUTING-ACTIVATION-CONFIRMATION-NEEDS")
        self.logger.debug("write DoIpRoutingActivationConfirmationNeeds %s" % needs.getShortName())
        self.writeServiceNeeds(child_element, needs)
        self.setChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH-REQUEST", needs.getDataLengthRequest())
        self.setChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH-RESPONSE", needs.getDataLengthResponse())
        self.setChildElementOptionalLiteral(child_element, "ROUTING-ACTIVATION-TYPE", needs.getRoutingActivationType())

    def writeSecureOnBoardCommunicationNeeds(self, element: ET.Element, needs: SecureOnBoardCommunicationNeeds):
        child_element = ET.SubElement(element, "SECURE-ON-BOARD-COMMUNICATION-NEEDS")
        self.logger.debug("write SecureOnBoardCommunicationNeeds %s" % needs.getShortName())
        self.writeServiceNeeds(child_element, needs)
        self.setChildElementOptionalLiteral(child_element, "VERIFICATION-STATUS-INDICATION-MODE", needs.getVerificationStatusIndicationMode())

    def writeIdsMgrNeeds(self, element: ET.Element, needs: IdsMgrNeeds):
        child_element = ET.SubElement(element, "IDS-MGR-NEEDS")
        self.logger.debug("write IdsMgrNeeds %s" % needs.getShortName())
        self.writeServiceNeeds(child_element, needs)
        self.setChildElementOptionalBooleanValue(child_element, "USE-SMART-SENSOR-API", needs.getUseSmartSensorApi())

    def setDiagEventDebounceCounterBased(self, element: ET.Element, algorithm: DiagEventDebounceCounterBased):
        child_element = ET.SubElement(element, "DIAG-EVENT-DEBOUNCE-COUNTER-BASED")
        self.writeDiagnosticCapabilityElement(child_element, algorithm)

    def setDiagEventDebounceMonitorInternal(self, element: ET.Element, algorithm: DiagEventDebounceMonitorInternal):
        child_element = ET.SubElement(element, "DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL")
        self.writeDiagnosticCapabilityElement(child_element, algorithm)

    def setDiagEventDebounceTimeBased(self, element: ET.Element, algorithm: DiagEventDebounceTimeBased):
        child_element = ET.SubElement(element, "DIAG-EVENT-DEBOUNCE-TIME-BASED")
        self.writeDiagnosticCapabilityElement(child_element, algorithm)

    def writeDiagEventDebounceAlgorithm(self, element: ET.Element, needs: DiagnosticEventNeeds):
        algorithm = needs.getDiagEventDebounceAlgorithm()
        if algorithm is not None:
            child_element = ET.SubElement(element, "DIAG-EVENT-DEBOUNCE-ALGORITHM")
            if isinstance(algorithm, DiagEventDebounceCounterBased):
                self.setDiagEventDebounceCounterBased(child_element, algorithm)
            elif isinstance(algorithm, DiagEventDebounceMonitorInternal):
                self.setDiagEventDebounceMonitorInternal(child_element, algorithm)
            elif isinstance(algorithm, DiagEventDebounceTimeBased):
                self.setDiagEventDebounceTimeBased(child_element, algorithm)
            else:
                self.notImplemented("Unsupported DiagEventDebounceAlgorithm <%s>" % type(algorithm))

    def writeDiagnosticEventNeeds(self, element: ET.Element, needs: DiagnosticEventNeeds):
        # self.logger.debug("Write DiagnosticEventNeeds %s" % needs.getShortName())
        child_element = ET.SubElement(element, "DIAGNOSTIC-EVENT-NEEDS")
        self.writeDiagnosticCapabilityElement(child_element, needs)
        refs = needs.getDeferringFidRefs()
        if len(refs) > 0:
            wrapper = ET.SubElement(child_element, "DEFERRING-FID-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(wrapper, "DEFERRING-FID-REF", ref)
        self.writeDiagEventDebounceAlgorithm(child_element, needs)
        self.setChildElementOptionalRefType(child_element, "INHIBITING-FID-REF", needs.getInhibitingFidRef())
        refs = needs.getInhibitingSecondaryFidRefs()
        if len(refs) > 0:
            wrapper = ET.SubElement(child_element, "INHIBITING-SECONDARY-FID-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(wrapper, "INHIBITING-SECONDARY-FID-REF", ref)
        self.setChildElementOptionalBooleanValue(child_element, "PRESTORED-FREEZEFRAME-STORED-IN-NVM", needs.getPrestoredFreezeframeStoredInNvm())
        self.setChildElementOptionalBooleanValue(child_element, "USES-MONITOR-DATA", needs.getUsesMonitorData())

    def writeDiagnosticEventInfoNeeds(self, element: ET.Element, needs: DiagnosticEventInfoNeeds):
        # self.logger.debug("Write DiagnosticEventNeeds %s" % needs.getShortName())
        child_element = ET.SubElement(element, "DIAGNOSTIC-EVENT-INFO-NEEDS")
        self.writeDiagnosticCapabilityElement(child_element, needs)
        self.setChildElementOptionalLiteral(child_element, "DTC-KIND", needs.getDtcKind())
        self.setChildElementOptionalPositiveInteger(child_element, "UDS-DTC-NUMBER", needs.getUdsDtcNumber())

    def writeDiagnosticIoControlNeeds(self, element: ET.Element, needs: DiagnosticIoControlNeeds):
        # self.logger.debug("Write DiagnosticIoControlNeeds %s" % needs.getShortName())
        child_element = ET.SubElement(element, "DIAGNOSTIC-IO-CONTROL-NEEDS")
        self.writeDiagnosticCapabilityElement(child_element, needs)
        self.setChildElementOptionalRefType(child_element, "CURRENT-VALUE-REF", needs.getCurrentValueRef())
        self.setChildElementOptionalBooleanValue(child_element, "FREEZE-CURRENT-STATE-SUPPORTED", needs.getFreezeCurrentStateSupported())
        self.setChildElementOptionalBooleanValue(child_element, "RESET-TO-DEFAULT-SUPPORTED", needs.getResetToDefaultSupported())
        self.setChildElementOptionalBooleanValue(child_element, "SHORT-TERM-ADJUSTMENT-SUPPORTED", needs.getShortTermAdjustmentSupported())

    def writeDiagnosticEnableConditionNeeds(self, element: ET.Element, needs: DiagnosticEnableConditionNeeds):
        # self.logger.debug("Write DiagnosticEnableConditionNeeds %s" % needs.getShortName())
        child_element = ET.SubElement(element, "DIAGNOSTIC-ENABLE-CONDITION-NEEDS")
        self.writeDiagnosticCapabilityElement(child_element, needs)
        self.setChildElementOptionalLiteral(child_element, "INITIAL-STATUS", needs.getInitialStatus())

    def writeDiagnosticOperationCycleNeeds(self, element: ET.Element, needs: DiagnosticOperationCycleNeeds):
        # self.logger.debug("Write DiagnosticOperationCycleNeeds %s" % needs.getShortName())
        child_element = ET.SubElement(element, "DIAGNOSTIC-OPERATION-CYCLE-NEEDS")
        self.writeDiagnosticCapabilityElement(child_element, needs)
        self.setChildElementOptionalLiteral(child_element, "OPERATION-CYCLE", needs.getOperationCycle())

    def writeDiagnosticStorageConditionNeeds(self, element: ET.Element, needs: DiagnosticStorageConditionNeeds):
        # self.logger.debug("Write DiagnosticStorageConditionNeeds %s" % needs.getShortName())
        child_element = ET.SubElement(element, "DIAGNOSTIC-STORAGE-CONDITION-NEEDS")
        self.writeDiagnosticCapabilityElement(child_element, needs)
        self.setChildElementOptionalLiteral(child_element, "INITIAL-STATUS", needs.getInitialStatus())

    def writeIndicatorStatusNeeds(self, element: ET.Element, needs: IndicatorStatusNeeds):
        # self.logger.debug("Write IndicatorStatusNeeds %s" % needs.getShortName())
        child_element = ET.SubElement(element, "INDICATOR-STATUS-NEEDS")
        self.writeServiceNeeds(child_element, needs)
        self.setChildElementOptionalLiteral(child_element, "TYPE", needs.getType())

    def writeFunctionInhibitionAvailabilityNeeds(self, element: ET.Element, needs: FunctionInhibitionAvailabilityNeeds):
        # self.logger.debug("Write FunctionInhibitionAvailabilityNeeds %s" % needs.getShortName())
        child_element = ET.SubElement(element, "FUNCTION-INHIBITION-AVAILABILITY-NEEDS")
        self.writeServiceNeeds(child_element, needs)
        self.setChildElementOptionalRefType(child_element, "CONTROLLED-FID-REF", needs.getControlledFidRef())

    def writeCryptoServiceNeeds(self, element: ET.Element, needs: CryptoServiceNeeds):
        # self.logger.debug("Write CryptoServiceNeeds %s" % needs.getShortName())
        child_element = ET.SubElement(element, "CRYPTO-SERVICE-NEEDS")
        self.writeServiceNeeds(child_element, needs)
        self.setChildElementOptionalPositiveInteger(child_element, "MAXIMUM-KEY-LENGTH", needs.getMaximumKeyLength())

    def writeEcuStateMgrUserNeeds(self, element: ET.Element, needs: EcuStateMgrUserNeeds):
        # self.logger.debug("write EcuStateMgrUserNeeds %s" % needs.getShortName())
        child_element = ET.SubElement(element, "ECU-STATE-MGR-USER-NEEDS")
        self.writeServiceNeeds(child_element, needs)

    def writeDtcStatusChangeNotificationNeeds(self, element: ET.Element, needs: DtcStatusChangeNotificationNeeds):
        # self.logger.debug("Write DtcStatusChangeNotificationNeeds %s" % needs.getShortName())
        child_element = ET.SubElement(element, "DTC-STATUS-CHANGE-NOTIFICATION-NEEDS")
        self.writeDiagnosticCapabilityElement(child_element, needs)
        self.setChildElementOptionalLiteral(child_element, "DTC-FORMAT-TYPE", needs.getDtcFormatType())

    def writeDltUserNeeds(self, element: ET.Element, needs: DtcStatusChangeNotificationNeeds):
        # self.logger.debug("Write DtcStatusChangeNotificationNeeds %s" % needs.getShortName())
        child_element = ET.SubElement(element, "DLT-USER-NEEDS")
        self.writeServiceNeeds(child_element, needs)

    def writeComMgrUserNeeds(self, element: ET.Element, needs: ComMgrUserNeeds):
        # self.logger.debug("Write ComMgrUserNeeds %s" % needs.getShortName())
        child_element = ET.SubElement(element, "COM-MGR-USER-NEEDS")
        self.writeServiceNeeds(child_element, needs)
        self.setChildElementOptionalLiteral(child_element, "MAX-COMM-MODE", needs.getMaxCommMode())

    def writeSupervisedEntityNeeds(self, element: ET.Element, needs: SupervisedEntityNeeds):
        child_element = ET.SubElement(element, "SUPERVISED-ENTITY-NEEDS")
        self.writeServiceNeeds(child_element, needs)
        self.setChildElementOptionalBooleanValue(child_element, "ACTIVATE-AT-START", needs.getActivateAtStart())
        refs = needs.getCheckpointsRefs()
        if len(refs) > 0:
            wrapper = ET.SubElement(child_element, "CHECKPOINTSS")
            for ref in refs:
                cond_tag = ET.SubElement(wrapper, "SUPERVISED-ENTITY-CHECKPOINT-NEEDS-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(cond_tag, "SUPERVISED-ENTITY-CHECKPOINT-NEEDS-REF", ref)
        self.setChildElementOptionalBooleanValue(child_element, "ENABLE-DEACTIVATION", needs.getEnableDeactivation())
        self.setChildElementOptionalTimeValue(child_element, "EXPECTED-ALIVE-CYCLE", needs.getExpectedAliveCycle())
        self.setChildElementOptionalTimeValue(child_element, "MAX-ALIVE-CYCLE", needs.getMaxAliveCycle())
        self.setChildElementOptionalTimeValue(child_element, "MIN-ALIVE-CYCLE", needs.getMinAliveCycle())
        self.setChildElementOptionalPositiveInteger(child_element, "TOLERATED-FAILED-CYCLES", needs.getToleratedFailedCycles())

    def writeTracedFailure(self, element: ET.Element, failure: TracedFailure):
        self.writeIdentifiable(element, failure)
        self.setChildElementOptionalPositiveInteger(element, "ID", failure.getId())

    def setDevelopmentError(self, element: ET.Element, failure: DevelopmentError):
        child_element = ET.SubElement(element, "DEVELOPMENT-ERROR")
        self.writeTracedFailure(child_element, failure)

    def setRuntimeError(self, element: ET.Element, failure: RuntimeError):
        child_element = ET.SubElement(element, "RUNTIME-ERROR")
        self.writeTracedFailure(child_element, failure)

    def setPossibleErrorReaction(self, element: ET.Element, reaction: PossibleErrorReaction):
        child_element = ET.SubElement(element, "POSSIBLE-ERROR-REACTION")
        self.writeIdentifiable(child_element, reaction)
        self.setChildElementOptionalPositiveInteger(child_element, "REACTION-CODE", reaction.getReactionCode())

    def setTransientFault(self, element: ET.Element, failure: TransientFault):
        child_element = ET.SubElement(element, "TRANSIENT-FAULT")
        self.writeTracedFailure(child_element, failure)
        reactions = failure.getPossibleErrorReactions()
        if len(reactions) > 0:
            wrapper = ET.SubElement(child_element, "POSSIBLE-ERROR-REACTIONS")
            for reaction in reactions:
                self.setPossibleErrorReaction(wrapper, reaction)

    def writeErrorTracerNeeds(self, element: ET.Element, needs: ErrorTracerNeeds):
        # self.logger.debug("Write ErrorTracerNeeds %s" % needs.getShortName())
        child_element = ET.SubElement(element, "ERROR-TRACER-NEEDS")
        self.writeServiceNeeds(child_element, needs)
        failures = needs.getTracedFailures()
        if len(failures) > 0:
            wrapper = ET.SubElement(child_element, "TRACED-FAILURES")
            for failure in failures:
                if isinstance(failure, DevelopmentError):
                    self.setDevelopmentError(wrapper, failure)
                elif isinstance(failure, RuntimeError):
                    self.setRuntimeError(wrapper, failure)
                elif isinstance(failure, TransientFault):
                    self.setTransientFault(wrapper, failure)
                else:
                    self.notImplemented("Unsupported traced failure <%s>" % type(failure))

    def writeSwcServiceDependencyServiceNeeds(self, element: ET.Element, parent: SwcServiceDependency):
        needs_list = parent.getServiceNeeds()
        if len(needs_list) > 0:
            child_element = ET.SubElement(element, "SERVICE-NEEDS")
            for needs in needs_list:
                if isinstance(needs, NvBlockNeeds):
                    self.writeNvBlockNeeds(child_element, needs)
                elif isinstance(needs, DiagnosticCommunicationManagerNeeds):
                    self.writeDiagnosticCommunicationManagerNeeds(child_element, needs)
                elif isinstance(needs, DiagnosticRoutineNeeds):
                    self.writeDiagnosticRoutineNeeds(child_element, needs)
                elif isinstance(needs, DiagnosticValueNeeds):
                    self.writeDiagnosticValueNeeds(child_element, needs)
                elif isinstance(needs, DiagnosticEventNeeds):
                    self.writeDiagnosticEventNeeds(child_element, needs)
                elif isinstance(needs, DiagnosticEventInfoNeeds):
                    self.writeDiagnosticEventInfoNeeds(child_element, needs)
                elif isinstance(needs, DiagnosticIoControlNeeds):
                    self.writeDiagnosticIoControlNeeds(child_element, needs)
                elif isinstance(needs, DiagnosticEnableConditionNeeds):
                    self.writeDiagnosticEnableConditionNeeds(child_element, needs)
                elif isinstance(needs, DiagnosticOperationCycleNeeds):
                    self.writeDiagnosticOperationCycleNeeds(child_element, needs)
                elif isinstance(needs, DiagnosticStorageConditionNeeds):
                    self.writeDiagnosticStorageConditionNeeds(child_element, needs)
                elif isinstance(needs, IndicatorStatusNeeds):
                    self.writeIndicatorStatusNeeds(child_element, needs)
                elif isinstance(needs, FunctionInhibitionAvailabilityNeeds):
                    self.writeFunctionInhibitionAvailabilityNeeds(child_element, needs)
                elif isinstance(needs, CryptoServiceNeeds):
                    self.writeCryptoServiceNeeds(child_element, needs)
                elif isinstance(needs, EcuStateMgrUserNeeds):
                    self.writeEcuStateMgrUserNeeds(child_element, needs)
                elif isinstance(needs, DtcStatusChangeNotificationNeeds):
                    self.writeDtcStatusChangeNotificationNeeds(child_element, needs)
                elif isinstance(needs, DltUserNeeds):
                    self.writeDltUserNeeds(child_element, needs)
                elif isinstance(needs, ComMgrUserNeeds):
                    self.writeComMgrUserNeeds(child_element, needs)
                elif isinstance(needs, ErrorTracerNeeds):
                    self.writeErrorTracerNeeds(child_element, needs)
                elif isinstance(needs, ObdInfoServiceNeeds):
                    self.writeObdInfoServiceNeeds(child_element, needs)
                elif isinstance(needs, ObdMonitorServiceNeeds):
                    self.writeObdMonitorServiceNeeds(child_element, needs)
                elif isinstance(needs, ObdPidServiceNeeds):
                    self.writeObdPidServiceNeeds(child_element, needs)
                elif isinstance(needs, ObdControlServiceNeeds):
                    self.writeObdControlServiceNeeds(child_element, needs)
                elif isinstance(needs, ObdRatioServiceNeeds):
                    self.writeObdRatioServiceNeeds(child_element, needs)
                elif isinstance(needs, ObdRatioDenominatorNeeds):
                    self.writeObdRatioDenominatorNeeds(child_element, needs)
                elif isinstance(needs, DoIpRoutingActivationAuthenticationNeeds):
                    self.writeDoIpRoutingActivationAuthenticationNeeds(child_element, needs)
                elif isinstance(needs, DoIpRoutingActivationConfirmationNeeds):
                    self.writeDoIpRoutingActivationConfirmationNeeds(child_element, needs)
                elif isinstance(needs, SecureOnBoardCommunicationNeeds):
                    self.writeSecureOnBoardCommunicationNeeds(child_element, needs)
                elif isinstance(needs, IdsMgrNeeds):
                    self.writeIdsMgrNeeds(child_element, needs)
                else:
                    self.notImplemented("Unsupported service needs <%s>" % type(needs))

    def writeSwcServiceDependencyRepresentedPortGroup(self, element: ET.Element, dependency: SwcServiceDependency):
        self.setChildElementOptionalRefType(element, "REPRESENTED-PORT-GROUP-REF", dependency.getRepresentedPortGroup())

    def writeSwcServiceDependency(self, element: ET.Element, dependency: SwcServiceDependency):
        child_element = ET.SubElement(element, "SWC-SERVICE-DEPENDENCY")
        self.writeServiceDependency(child_element, dependency)
        self.writeSwcServiceDependencyAssignedData(child_element, dependency)
        self.writeSwcServiceDependencyAssignedPorts(child_element, dependency)
        self.writeSwcServiceDependencyServiceNeeds(child_element, dependency)
        self.writeSwcServiceDependencyRepresentedPortGroup(child_element, dependency)

    def writeSwcInternalBehaviorServiceDependencies(self, element: ET.Element, behavior: SwcInternalBehavior):
        dependencies = behavior.getSwcServiceDependencies()
        if len(dependencies) > 0:
            child_element = ET.SubElement(element, "SERVICE-DEPENDENCYS")
            for dependency in dependencies:
                if isinstance(dependency, SwcServiceDependency):
                    self.writeSwcServiceDependency(child_element, dependency)
                else:
                    self.notImplemented("Unsupported ServiceDependency <%s>" % type(dependency))

    def setIncludedDataTypeSets(self, element: ET.Element, sets: List[IncludedDataTypeSet]):
        if len(sets) > 0:
            include_data_type_sets_tag = ET.SubElement(element, "INCLUDED-DATA-TYPE-SETS")
            for set in sets:
                child_element = ET.SubElement(include_data_type_sets_tag, "INCLUDED-DATA-TYPE-SET")
                self.writeARObjectAttributes(child_element, set)
                self.setChildElementOptionalLiteral(child_element, "LITERAL-PREFIX", set.getLiteralPrefix())
                type_refs = set.getDataTypeRefs()
                if len(type_refs) > 0:
                    data_type_refs_tag = ET.SubElement(child_element, "DATA-TYPE-REFS")
                    for type_ref in type_refs:
                        self.setChildElementOptionalRefType(data_type_refs_tag, "DATA-TYPE-REF", type_ref)

    def writeIncludedModeDeclarationGroupSet(self, element: ET.Element, set: IncludedModeDeclarationGroupSet):
        if set is not None:
            child_element = ET.SubElement(element, "INCLUDED-MODE-DECLARATION-GROUP-SET")
            refs = set.getModeDeclarationGroupRefs()
            if len(refs) > 0:
                refs_tag = ET.SubElement(child_element, "MODE-DECLARATION-GROUP-REFS")
                for ref in refs:
                    self.setChildElementOptionalRefType(refs_tag, "MODE-DECLARATION-GROUP-REF", ref)
            self.setChildElementOptionalLiteral(child_element, "PREFIX", set.getPrefix())

    def writeSwcInternalBehaviorIncludedModeDeclarationGroupSets(self, element: ET.Element, behavior: SwcInternalBehavior):
        group_sets = behavior.getIncludedModeDeclarationGroupSets()
        if len(group_sets) > 0:
            child_element = ET.SubElement(element, "INCLUDED-MODE-DECLARATION-GROUP-SETS")
            for group_set in group_sets:
                if isinstance(group_set, IncludedModeDeclarationGroupSet):
                    self.writeIncludedModeDeclarationGroupSet(child_element, group_set)
                else:
                    self.notImplemented("Unsupported IncludedModeDeclarationGroupSet <%s>" % type(group_set))

    def writeSwcInternalBehaviorExclusiveAreaPolicies(self, element: ET.Element, behavior: SwcInternalBehavior):
        policies = behavior.getExclusiveAreaPolicies()
        if len(policies) > 0:
            policies_tag = ET.SubElement(element, "EXCLUSIVE-AREA-POLICYS")
            for policy in policies:
                if isinstance(policy, SwcExclusiveAreaPolicy):
                    policy_element = ET.SubElement(policies_tag, "SWC-EXCLUSIVE-AREA-POLICY")
                    self.setChildElementOptionalLiteral(policy_element, "API-PRINCIPLE", policy.getApiPrinciple())
                    self.setChildElementOptionalRefType(policy_element, "EXCLUSIVE-AREA-REF", policy.getExclusiveAreaRef())

    def writeSwcInternalBehaviorInstantiationDataDefProps(self, element: ET.Element, behavior: SwcInternalBehavior):
        props_list = behavior.getInstantiationDataDefPropss()
        if len(props_list) > 0:
            props_tag = ET.SubElement(element, "INSTANTIATION-DATA-DEF-PROPSS")
            for props in props_list:
                if isinstance(props, InstantiationDataDefProps):
                    child_element = ET.SubElement(props_tag, "INSTANTIATION-DATA-DEF-PROPS")
                    self.setAutosarParameterRef(child_element, "PARAMETER-INSTANCE", props.getParameterInstance())
                    self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", props.getSwDataDefProps())
                    self.setAutosarVariableRef(child_element, "VARIABLE-INSTANCE", props.getVariableInstance())
                else:
                    self.notImplemented("Unsupported InstantiationDataDefProps <%s>" % type(props))

    def writeSwcInternalBehavior(self, element: ET.Element, behavior: SwcInternalBehavior):
        self.logger.debug("writeSwInternalBehavior %s" % behavior.getShortName())
        child_element = ET.SubElement(element, "SWC-INTERNAL-BEHAVIOR")
        self.writeInternalBehavior(child_element, behavior)

        self.writeSwcInternalBehaviorArTypedPerInstanceMemories(child_element, behavior)
        self.writeSwcInternalBehaviorExclusiveAreaPolicies(child_element, behavior)
        self.writeSwcInternalBehaviorEvents(child_element, behavior)
        self.writeSwcInternalBehaviorExplicitInterRunnableVariables(child_element, behavior)
        self.setChildElementOptionalLiteral(child_element, "HANDLE-TERMINATION-AND-RESTART", behavior.getHandleTerminationAndRestart())
        self.setIncludedDataTypeSets(child_element, behavior.getIncludedDataTypeSets())
        self.writeSwcInternalBehaviorIncludedModeDeclarationGroupSets(child_element, behavior)
        self.writeSwcInternalBehaviorInstantiationDataDefProps(child_element, behavior)
        self.writeSwcInternalBehaviorPerInstanceMemories(child_element, behavior)
        self.writeSwcInternalBehaviorParameterDataPrototypes(child_element, "PER-INSTANCE-PARAMETERS", behavior.getPerInstanceParameters())
        self.writeSwcInternalBehaviorPortAPIOptions(child_element, behavior)
        self.writeSwcInternalBehaviorRunnables(child_element, behavior)
        self.writeSwcInternalBehaviorServiceDependencies(child_element, behavior)
        self.writeSwcInternalBehaviorParameterDataPrototypes(child_element, "SHARED-PARAMETERS", behavior.getSharedParameters())
        self.writeSwcInternalBehaviorVariationPointProxies(child_element, behavior)
        self.setChildElementOptionalBooleanValue(child_element, "SUPPORTS-MULTIPLE-INSTANTIATION", behavior.getSupportsMultipleInstantiation())

    def writeAtomicSwComponentTypeInternalBehaviors(self, element: ET.Element, behavior: InternalBehavior):
        if behavior is not None:
            behaviors_tag = ET.SubElement(element, "INTERNAL-BEHAVIORS")
            if isinstance(behavior, SwcInternalBehavior):
                self.writeSwcInternalBehavior(behaviors_tag, behavior)
            else:
                self.notImplemented("Unsupported Internal Behaviors <%s>" % type(behavior))

    def writeAtomicSwComponentType(self, element: ET.Element, sw_component: AtomicSwComponentType):
        self.writeSwComponentType(element, sw_component)
        self.writeAtomicSwComponentTypeInternalBehaviors(element, sw_component.getInternalBehavior())
        self.writeSymbolProps(element, sw_component.getSymbolProps())

    def writeComplexDeviceDriverSwComponentType(self, element: ET.Element, sw_component: ComplexDeviceDriverSwComponentType):
        self.logger.debug("writeComplexDeviceDriverSwComponentType %s" % sw_component.getShortName())
        child_element = ET.SubElement(element, "COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE")
        self.writeAtomicSwComponentType(child_element, sw_component)
        self.writeHardwareElementRefs(child_element, sw_component.getHardwareElementRefs())

    def writeHardwareElementRefs(self, element: ET.Element, refs: List[RefType]):
        if len(refs) > 0:
            child_element = ET.SubElement(element, "HARDWARE-ELEMENT-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "HARDWARE-ELEMENT-REF", ref)

    def writeArtifactDescriptors(self, element: ET.Element, code_desc: Code):
        artifact_descriptors = code_desc.getArtifactDescriptors()
        if len(artifact_descriptors) > 0:
            artifact_descs_tag = ET.SubElement(element, "ARTIFACT-DESCRIPTORS")
            for artifact_desc in artifact_descriptors:
                artifact_desc_tag = ET.SubElement(artifact_descs_tag, "AUTOSAR-ENGINEERING-OBJECT")
                self.logger.debug("writeArtifactDescriptor %s", artifact_desc.getShortLabel())
                self.writeARObjectAttributes(artifact_desc_tag, artifact_desc)
                self.setChildElementOptionalLiteral(artifact_desc_tag, "SHORT-LABEL", artifact_desc.getShortLabel())
                self.setChildElementOptionalLiteral(artifact_desc_tag, "CATEGORY", artifact_desc.getCategory())

    def writeCode(self, element: ET.SubElement, code_desc: Code):
        # self.logger.debug("Write Code %s" % code_desc.getShortName())
        child_element = ET.SubElement(element, "CODE")
        self.writeIdentifiable(child_element, code_desc)
        self.writeArtifactDescriptor(child_element, code_desc)
        self.writeCodeCallbackHeaderRefs(child_element, code_desc)

    def writeCodeCallbackHeaderRefs(self, element: ET.Element, code_desc: Code):
        refs = code_desc.getCallbackHeaderRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "CALLBACK-HEADER-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "CALLBACK-HEADER-REF", ref)

    def writeCodeDescriptors(self, element: ET.Element, impl: Implementation):
        descs = impl.getCodeDescriptors()
        if len(descs) > 0:
            child_element = ET.SubElement(element, "CODE-DESCRIPTORS")
            for desc in descs:
                if isinstance(desc, Code):
                    self.writeCode(child_element, desc)
                else:
                    self.notImplemented("Unsupported Code Descriptor <%s>" % type(desc))

    def setMemorySectionOptions(self, element: ET.Element, options: List[ARLiteral]):
        if len(options) > 0:
            child_element = ET.SubElement(element, "OPTIONS")
            for option in options:
                self.setChildElementOptionalLiteral(child_element, "OPTION", option)

    def writeMemorySectionExecutableEntityRefs(self, element: ET.Element, memory_section: MemorySection):
        refs = memory_section.getExecutableEntityRefs()
        if len(refs) > 0:
            refs_element = ET.SubElement(element, "EXECUTABLE-ENTITY-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_element, "EXECUTABLE-ENTITY-REF", ref)

    def writeMemorySections(self, element: ET.Element, consumption: ResourceConsumption):
        memory_sections = consumption.getMemorySections()
        if len(memory_sections) > 0:
            sections_tag = ET.SubElement(element, "MEMORY-SECTIONS")
            for memory_section in memory_sections:
                child_element = ET.SubElement(sections_tag, "MEMORY-SECTION")
                self.writeIdentifiable(child_element, memory_section)
                self.setChildElementOptionalLiteral(child_element, "ALIGNMENT", memory_section.getAlignment())
                self.writeMemorySectionExecutableEntityRefs(child_element, memory_section)
                self.setChildElementOptionalLiteral(child_element, "MEM-CLASS-SYMBOL", memory_section.getMemClassSymbol())
                self.setMemorySectionOptions(child_element, memory_section.getOptions())
                self.setChildElementOptionalRefType(child_element, "PREFIX-REF", memory_section.getPrefixRef())
                self.setChildElementOptionalPositiveInteger(child_element, "SIZE", memory_section.getSize())
                self.setChildElementOptionalRefType(child_element, "SW-ADDRMETHOD-REF", memory_section.getSwAddrMethodRef())
                self.setChildElementOptionalLiteral(child_element, "SYMBOL", memory_section.getSymbol())
                self.logger.debug("Write MemorySection %s" % memory_section.getShortName())

    def setMultidimensionalTime(self, element: ET.Element, key: str, value: MultidimensionalTime):
        if value is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "CSE-CODE", value.getCseCode())
            self.setChildElementOptionalIntegerValue(child_element, "CSE-CODE-FACTOR", value.getCseCodeFactor())

    def setHardwareConfiguration(self, element: ET.Element, config):
        if config is not None:
            child_element = ET.SubElement(element, "HARDWARE-CONFIGURATION")
            self.setChildElementOptionalLiteral(child_element, "ADDITIONAL-INFORMATION", config.getAdditionalInformation())
            self.setChildElementOptionalLiteral(child_element, "PROCESSOR-MODE", config.getProcessorMode())
            self.setChildElementOptionalLiteral(child_element, "PROCESSOR-SPEED", config.getProcessorSpeed())

    def setSoftwareContext(self, element: ET.Element, context):
        if context is not None:
            child_element = ET.SubElement(element, "SOFTWARE-CONTEXT")
            self.setChildElementOptionalLiteral(child_element, "INPUT", context.getInput())
            self.setChildElementOptionalLiteral(child_element, "STATE", context.getState())

    def writeExecutionTime(self, element: ET.Element, execution_time):
        self.writeIdentifiable(element, execution_time)
        self.setChildElementOptionalRefType(element, "EXCLUSIVE-AREA-REF", execution_time.getExclusiveAreaRef())
        self.setChildElementOptionalRefType(element, "EXECUTABLE-ENTITY-REF", execution_time.getExecutableEntityRef())
        self.setHardwareConfiguration(element, execution_time.getHardwareConfiguration())
        self.setChildElementOptionalRefType(element, "HW-ELEMENT-REF", execution_time.getHwElementRef())
        included_library_refs = execution_time.getIncludedLibraryRefs()
        if len(included_library_refs) > 0:
            refs_element = ET.SubElement(element, "INCLUDED-LIBRARY-REFS")
            for ref in included_library_refs:
                self.setChildElementOptionalRefType(refs_element, "INCLUDED-LIBRARY-REF", ref)
        memory_section_locations = execution_time.getMemorySectionLocations()
        if len(memory_section_locations) > 0:
            locations_element = ET.SubElement(element, "MEMORY-SECTION-LOCATIONS")
            for location in memory_section_locations:
                location_element = ET.SubElement(locations_element, "MEMORY-SECTION-LOCATION")
                self.setChildElementOptionalRefType(location_element, "PROVIDED-MEMORY-REF", location.getProvidedMemoryRef())
                self.setChildElementOptionalRefType(location_element, "SOFTWARE-MEMORY-SECTION-REF", location.getSoftwareMemorySectionRef())
        self.setSoftwareContext(element, execution_time.getSoftwareContext())

    def writeAnalyzedExecutionTime(self, element: ET.Element, execution_time: AnalyzedExecutionTime):
        child_element = ET.SubElement(element, "ANALYZED-EXECUTION-TIME")
        self.writeExecutionTime(child_element, execution_time)
        self.setMultidimensionalTime(child_element, "BEST-CASE-EXECUTION-TIME", execution_time.getBestCaseExecutionTime())
        self.setMultidimensionalTime(child_element, "WORST-CASE-EXECUTION-TIME", execution_time.getWorstCaseExecutionTime())

    def writeMeasuredExecutionTime(self, element: ET.Element, execution_time: MeasuredExecutionTime):
        child_element = ET.SubElement(element, "MEASURED-EXECUTION-TIME")
        self.writeExecutionTime(child_element, execution_time)
        self.setMultidimensionalTime(child_element, "MAXIMUM-EXECUTION-TIME", execution_time.getMaximumExecutionTime())
        self.setMultidimensionalTime(child_element, "MINIMUM-EXECUTION-TIME", execution_time.getMinimumExecutionTime())
        self.setMultidimensionalTime(child_element, "NOMINAL-EXECUTION-TIME", execution_time.getNominalExecutionTime())

    def writeSimulatedExecutionTime(self, element: ET.Element, execution_time: SimulatedExecutionTime):
        child_element = ET.SubElement(element, "SIMULATED-EXECUTION-TIME")
        self.writeExecutionTime(child_element, execution_time)
        self.setMultidimensionalTime(child_element, "MAXIMUM-EXECUTION-TIME", execution_time.getMaximumExecutionTime())
        self.setMultidimensionalTime(child_element, "MINIMUM-EXECUTION-TIME", execution_time.getMinimumExecutionTime())
        self.setMultidimensionalTime(child_element, "NOMINAL-EXECUTION-TIME", execution_time.getNominalExecutionTime())

    def writeRoughEstimateOfExecutionTime(self, element: ET.Element, execution_time: RoughEstimateOfExecutionTime):
        child_element = ET.SubElement(element, "ROUGH-ESTIMATE-OF-EXECUTION-TIME")
        self.writeExecutionTime(child_element, execution_time)
        self.setChildElementOptionalLiteral(child_element, "ADDITIONAL-INFORMATION", execution_time.getAdditionalInformation())
        self.setMultidimensionalTime(child_element, "ESTIMATED-EXECUTION-TIME", execution_time.getEstimatedExecutionTime())

    def writeExecutionTimes(self, element: ET.Element, execution_times: List):
        if len(execution_times) > 0:
            child_element = ET.SubElement(element, "EXECUTION-TIMES")
            for execution_time in execution_times:
                if isinstance(execution_time, AnalyzedExecutionTime):
                    self.writeAnalyzedExecutionTime(child_element, execution_time)
                elif isinstance(execution_time, MeasuredExecutionTime):
                    self.writeMeasuredExecutionTime(child_element, execution_time)
                elif isinstance(execution_time, RoughEstimateOfExecutionTime):
                    self.writeRoughEstimateOfExecutionTime(child_element, execution_time)
                elif isinstance(execution_time, SimulatedExecutionTime):
                    self.writeSimulatedExecutionTime(child_element, execution_time)
                else:
                    self.notImplemented("Unsupported Execution Time: <%s>" % type(execution_time))

    def writeHeapUsage(self, element: ET.Element, usage):
        self.writeIdentifiable(element, usage)
        self.setHardwareConfiguration(element, usage.getHardwareConfiguration())
        self.setChildElementOptionalRefType(element, "HW-ELEMENT-REF", usage.getHwElementRef())
        self.setSoftwareContext(element, usage.getSoftwareContext())

    def writeMeasuredHeapUsage(self, element: ET.Element, usage: MeasuredHeapUsage):
        child_element = ET.SubElement(element, "MEASURED-HEAP-USAGE")
        self.writeHeapUsage(child_element, usage)
        self.setChildElementOptionalPositiveInteger(child_element, "AVERAGE-MEMORY-CONSUMPTION", usage.getAverageMemoryConsumption())
        self.setChildElementOptionalPositiveInteger(child_element, "MAXIMUM-MEMORY-CONSUMPTION", usage.getMaximumMemoryConsumption())
        self.setChildElementOptionalPositiveInteger(child_element, "MINIMUM-MEMORY-CONSUMPTION", usage.getMinimumMemoryConsumption())
        self.setChildElementOptionalLiteral(child_element, "TEST-PATTERN", usage.getTestPattern())

    def writeRoughEstimateHeapUsage(self, element: ET.Element, usage: RoughEstimateHeapUsage):
        child_element = ET.SubElement(element, "ROUGH-ESTIMATE-HEAP-USAGE")
        self.writeHeapUsage(child_element, usage)
        self.setChildElementOptionalPositiveInteger(child_element, "MEMORY-CONSUMPTION", usage.getMemoryConsumption())

    def writeWorstCaseHeapUsage(self, element: ET.Element, usage: WorstCaseHeapUsage):
        child_element = ET.SubElement(element, "WORST-CASE-HEAP-USAGE")
        self.writeHeapUsage(child_element, usage)
        self.setChildElementOptionalPositiveInteger(child_element, "MEMORY-CONSUMPTION", usage.getMemoryConsumption())

    def writeHeapUsages(self, element: ET.Element, usages: List):
        if len(usages) > 0:
            child_element = ET.SubElement(element, "HEAP-USAGES")
            for usage in usages:
                if isinstance(usage, MeasuredHeapUsage):
                    self.writeMeasuredHeapUsage(child_element, usage)
                elif isinstance(usage, RoughEstimateHeapUsage):
                    self.writeRoughEstimateHeapUsage(child_element, usage)
                elif isinstance(usage, WorstCaseHeapUsage):
                    self.writeWorstCaseHeapUsage(child_element, usage)
                else:
                    self.notImplemented("Unsupported Heap Usage: <%s>" % type(usage))

    def writeSectionNamePrefixes(self, element: ET.Element, prefixes: List[SectionNamePrefix]):
        if len(prefixes) > 0:
            child_element = ET.SubElement(element, "SECTION-NAME-PREFIXS")
            for prefix in prefixes:
                prefix_element = ET.SubElement(child_element, "SECTION-NAME-PREFIX")
                self.writeReferrable(prefix_element, prefix)
                self.setChildElementOptionalRefType(prefix_element, "IMPLEMENTED-IN-REF", prefix.getImplementedInRef())

    def writeAccessCountSets(self, element: ET.Element, access_count_sets: List):
        if len(access_count_sets) > 0:
            child_element = ET.SubElement(element, "ACCESS-COUNT-SETS")
            for access_count_set in access_count_sets:
                access_count_set_element = ET.SubElement(child_element, "ACCESS-COUNT-SET")
                self.setChildElementOptionalLiteral(access_count_set_element, "COUNT-PROFILE", access_count_set.getCountProfile())
                access_counts = access_count_set.getAccessCounts()
                if len(access_counts) > 0:
                    counts_element = ET.SubElement(access_count_set_element, "ACCESS-COUNTS")
                    for count in access_counts:
                        count_element = ET.SubElement(counts_element, "ACCESS-COUNT")
                        self.setChildElementOptionalRefType(count_element, "ACCESS-POINT-REF", count.getAccessPointRef())
                        self.setChildElementOptionalPositiveInteger(count_element, "VALUE", count.getValue())

    def setStackUsage(self, element: ET.Element, usage: StackUsage):
        self.logger.debug("Write StackUsage %s" % usage.getShortName())
        self.writeIdentifiable(element, usage)
        self.setChildElementOptionalRefType(element, "EXECUTABLE-ENTITY-REF", usage.getExecutableEntityRef())
        self.setHardwareConfiguration(element, usage.getHardwareConfiguration())
        self.setChildElementOptionalRefType(element, "HW-ELEMENT-REF", usage.getHwElementRef())
        self.setSoftwareContext(element, usage.getSoftwareContext())

    def setRoughEstimateStackUsage(self, element: ET.Element, usage: RoughEstimateStackUsage):
        if usage is not None:
            child_element = ET.SubElement(element, "ROUGH-ESTIMATE-STACK-USAGE")
            self.setStackUsage(child_element, usage)
            self.setChildElementOptionalPositiveInteger(child_element, "MEMORY-CONSUMPTION", usage.getMemoryConsumption())

    def setMeasuredStackUsage(self, element: ET.Element, usage: MeasuredStackUsage):
        if usage is not None:
            child_element = ET.SubElement(element, "MEASURED-STACK-USAGE")
            self.setStackUsage(child_element, usage)
            self.setChildElementOptionalPositiveInteger(child_element, "AVERAGE-MEMORY-CONSUMPTION", usage.getAverageMemoryConsumption())
            self.setChildElementOptionalPositiveInteger(child_element, "MAXIMUM-MEMORY-CONSUMPTION", usage.getMaximumMemoryConsumption())
            self.setChildElementOptionalPositiveInteger(child_element, "MINIMUM-MEMORY-CONSUMPTION", usage.getMinimumMemoryConsumption())
            self.setChildElementOptionalLiteral(child_element, "TEST-PATTERN", usage.getTestPattern())

    def setWorstCaseStackUsage(self, element: ET.Element, usage: WorstCaseStackUsage):
        if usage is not None:
            child_element = ET.SubElement(element, "WORST-CASE-STACK-USAGE")
            self.setStackUsage(child_element, usage)
            self.setChildElementOptionalPositiveInteger(child_element, "MEMORY-CONSUMPTION", usage.getMemoryConsumption())

    def writeStackUsages(self, element: ET.Element, usages: List[StackUsage]):
        if len(usages) > 0:
            child_element = ET.SubElement(element, "STACK-USAGES")
            for usage in usages:
                if isinstance(usage, RoughEstimateStackUsage):
                    self.setRoughEstimateStackUsage(child_element, usage)
                elif isinstance(usage, MeasuredStackUsage):
                    self.setMeasuredStackUsage(child_element, usage)
                elif isinstance(usage, WorstCaseStackUsage):
                    self.setWorstCaseStackUsage(child_element, usage)
                else:
                    self.notImplemented("Unsupported Stack Usages: <%s>" % type(usage))

    def setResourceConsumption(self, element: ET.Element, consumption: ResourceConsumption):
        if consumption is not None:
            child_element = ET.SubElement(element, "RESOURCE-CONSUMPTION")
            self.writeIdentifiable(child_element, consumption)
            self.writeAccessCountSets(child_element, consumption.getAccessCountSets())
            self.writeExecutionTimes(child_element, consumption.getExecutionTimes())
            self.writeHeapUsages(child_element, consumption.getHeapUsages())
            self.writeMemorySections(child_element, consumption)
            self.writeSectionNamePrefixes(child_element, consumption.getSectionNamePrefixes())
            self.writeStackUsages(child_element, consumption.getStackUsages())

    def writeImplementation(self, element: ET.Element, impl: Implementation):
        self.writeIdentifiable(element, impl)
        self.writeImplementationBuildActionManifests(element, impl)
        self.writeCodeDescriptors(element, impl)
        self.writeCompilers(element, impl)
        self.writeDependencyOnArtifacts(element, impl, "GENERATED-ARTIFACTS", impl.getGeneratedArtifacts())
        self.writeImplementationHwElementRefs(element, impl)
        self.writeLinkers(element, impl)
        self.setChildElementOptionalLiteral(element, "PROGRAMMING-LANGUAGE", impl.getProgrammingLanguage())
        self.writeDependencyOnArtifacts(element, impl, "REQUIRED-ARTIFACTS", impl.getRequiredArtifacts())
        self.writeDependencyOnArtifacts(element, impl, "REQUIRED-GENERATOR-TOOLS", impl.getRequiredGeneratorTools())
        self.setResourceConsumption(element, impl.getResourceConsumption())
        self.setChildElementOptionalLiteral(element, "SW-VERSION", impl.getSwVersion())
        self.setChildElementOptionalRefType(element, "SWC-BSW-MAPPING-REF", impl.getSwcBswMappingRef())
        self.setChildElementOptionalLiteral(element, "USED-CODE-GENERATOR", impl.getUsedCodeGenerator())
        self.setChildElementOptionalPositiveInteger(element, "VENDOR-ID", impl.getVendorId())
        if impl.getMcSupport() is not None:
            self.writeMcSupportData(element, impl.getMcSupport())

    def writeMcSupportData(self, element: ET.Element, support: McSupportData):
        child_element = ET.SubElement(element, "MC-SUPPORT")
        emulation_supports = support.getEmulationSupports()
        if len(emulation_supports) > 0:
            supports_element = ET.SubElement(child_element, "EMULATION-SUPPORTS")
            for emulation_support in emulation_supports:
                self.writeMcSwEmulationMethodSupport(ET.SubElement(supports_element, "MC-SW-EMULATION-METHOD-SUPPORT"), emulation_support)
        mc_parameter_instances = support.getMcParameterInstances()
        if len(mc_parameter_instances) > 0:
            instances_element = ET.SubElement(child_element, "MC-PARAMETER-INSTANCES")
            for instance in mc_parameter_instances:
                self.writeMcDataInstance(ET.SubElement(instances_element, "MC-DATA-INSTANCE"), instance)
        mc_variable_instances = support.getMcVariableInstances()
        if len(mc_variable_instances) > 0:
            instances_element = ET.SubElement(child_element, "MC-VARIABLE-INSTANCES")
            for instance in mc_variable_instances:
                self.writeMcDataInstance(ET.SubElement(instances_element, "MC-DATA-INSTANCE"), instance)
        measurable_system_constant_values_refs = support.getMeasurableSystemConstantValuesRefs()
        if len(measurable_system_constant_values_refs) > 0:
            refs_element = ET.SubElement(child_element, "MEASURABLE-SYSTEM-CONSTANT-VALUES-REFS")
            for ref in measurable_system_constant_values_refs:
                self.setChildElementOptionalRefType(refs_element, "MEASURABLE-SYSTEM-CONSTANT-VALUES-REF", ref)
        rpt_support_data = support.getRptSupportData()
        if rpt_support_data is not None:
            self.writeRptSupportData(child_element, rpt_support_data)

    def writeMcSwEmulationMethodSupport(self, element: ET.Element, support: McSwEmulationMethodSupport):
        self.setChildElementOptionalLiteral(element, "SHORT-LABEL", support.getShortLabel())
        self.setChildElementOptionalLiteral(element, "CATEGORY", support.getCategory())
        self.setChildElementOptionalRefType(element, "BASE-REFERENCE-REF", support.getBaseReferenceRef())
        element_groups = support.getElementGroups()
        if len(element_groups) > 0:
            groups_element = ET.SubElement(element, "ELEMENT-GROUPS")
            for group in element_groups:
                self.writeMcParameterElementGroup(ET.SubElement(groups_element, "MC-PARAMETER-ELEMENT-GROUP"), group)
        self.setChildElementOptionalRefType(element, "REFERENCE-TABLE-REF", support.getReferenceTableRef())

    def writeMcParameterElementGroup(self, element: ET.Element, group: McParameterElementGroup):
        self.setChildElementOptionalLiteral(element, "SHORT-LABEL", group.getShortLabel())
        self.setChildElementOptionalRefType(element, "RAM-LOCATION-REF", group.getRamLocationRef())
        self.setChildElementOptionalRefType(element, "ROM-LOCATION-REF", group.getRomLocationRef())

    def writeRteEventInEcuInstanceRef(self, element: ET.Element, iref: RteEventInEcuInstanceRef):
        self.setChildElementOptionalRefType(element, "CONTEXT-ROOT-COMPOSITION-REF", iref.getContextRootCompositionRef())
        self.setChildElementOptionalRefType(element, "CONTEXT-ATOMIC-COMPONENT-REF", iref.getContextAtomicComponentRef())
        self.setChildElementOptionalRefType(element, "TARGET-RTE-EVENT-REF", iref.getTargetRteEventRef())

    def writeVariableAccessInEcuInstanceRef(self, element: ET.Element, iref: VariableAccessInEcuInstanceRef):
        self.setChildElementOptionalRefType(element, "CONTEXT-ROOT-COMPOSITION-REF", iref.getContextRootCompositionRef())
        self.setChildElementOptionalRefType(element, "CONTEXT-ATOMIC-COMPONENT-REF", iref.getContextAtomicComponentRef())
        self.setChildElementOptionalRefType(element, "TARGET-VARIABLE-ACCESS-REF", iref.getTargetVariableAccessRef())

    def writeMcDataAccessDetails(self, element: ET.Element, details: McDataAccessDetails):
        rte_event_irefs = details.getRteEventIRefs()
        if len(rte_event_irefs) > 0:
            rte_event_irefs_element = ET.SubElement(element, "RTE-EVENT-IREFS")
            for iref in rte_event_irefs:
                self.writeRteEventInEcuInstanceRef(ET.SubElement(rte_event_irefs_element, "RTE-EVENT-IREF"), iref)
        variable_access_irefs = details.getVariableAccessIRefs()
        if len(variable_access_irefs) > 0:
            variable_access_irefs_element = ET.SubElement(element, "VARIABLE-ACCESS-IREFS")
            for iref in variable_access_irefs:
                self.writeVariableAccessInEcuInstanceRef(ET.SubElement(variable_access_irefs_element, "VARIABLE-ACCESS-IREF"), iref)

    def writeMcDataInstance(self, element: ET.Element, instance: McDataInstance):
        self.writeIdentifiable(element, instance)
        self.setChildElementOptionalPositiveInteger(element, "ARRAY-SIZE", instance.getArraySize())
        self.setChildElementOptionalLiteral(element, "DISPLAY-IDENTIFIER", instance.getDisplayIdentifier())
        self.setChildElementOptionalRefType(element, "FLAT-MAP-ENTRY-REF", instance.getFlatMapEntryRef())
        instance_in_memory = instance.getInstanceInMemory()
        if instance_in_memory is not None:
            instance_in_memory_element = ET.SubElement(element, "INSTANCE-IN-MEMORY")
            self.setChildElementOptionalRefType(instance_in_memory_element, "CONTEXT-REF", instance_in_memory.getContextRef())
            self.setChildElementOptionalRefType(instance_in_memory_element, "TARGET-REF", instance_in_memory.getTargetRef())
        if instance.getMcDataAccessDetails() is not None:
            self.writeMcDataAccessDetails(ET.SubElement(element, "MC-DATA-ACCESS-DETAILS"), instance.getMcDataAccessDetails())
        mc_data_assignments = instance.getMcDataAssignments()
        if len(mc_data_assignments) > 0:
            assignments_element = ET.SubElement(element, "MC-DATA-ASSIGNMENTS")
            for assignment in mc_data_assignments:
                self.writeRoleBasedMcDataAssignment(ET.SubElement(assignments_element, "ROLE-BASED-MC-DATA-ASSIGNMENT"), assignment)
        if instance.getResultingProperties() is not None:
            ET.SubElement(element, "RESULTING-PROPERTIES")
        if instance.getResultingRptSwPrototypingAccess() is not None:
            self.writeRptSwPrototypingAccess(ET.SubElement(element, "RESULTING-RPT-SW-PROTOTYPING-ACCESS"), instance.getResultingRptSwPrototypingAccess())
        self.setChildElementOptionalLiteral(element, "ROLE", instance.getRole())
        if instance.getRptImplPolicy() is not None:
            self.writeRptImplPolicy(ET.SubElement(element, "RPT-IMPL-POLICY"), instance.getRptImplPolicy())
        sub_elements = instance.getSubElements()
        if len(sub_elements) > 0:
            sub_elements_element = ET.SubElement(element, "SUB-ELEMENTS")
            for sub_element in sub_elements:
                self.writeMcDataInstance(ET.SubElement(sub_elements_element, "MC-DATA-INSTANCE"), sub_element)
        self.setChildElementOptionalLiteral(element, "SYMBOL", instance.getSymbol())

    def writeRoleBasedMcDataAssignment(self, element: ET.Element, assignment: RoleBasedMcDataAssignment):
        execution_context_refs = assignment.getExecutionContextRefs()
        if len(execution_context_refs) > 0:
            refs_element = ET.SubElement(element, "EXECUTION-CONTEXT-REFS")
            for ref in execution_context_refs:
                self.setChildElementOptionalRefType(refs_element, "EXECUTION-CONTEXT-REF", ref)
        mc_data_instance_refs = assignment.getMcDataInstanceRefs()
        if len(mc_data_instance_refs) > 0:
            refs_element = ET.SubElement(element, "MC-DATA-INSTANCE-REFS")
            for ref in mc_data_instance_refs:
                self.setChildElementOptionalRefType(refs_element, "MC-DATA-INSTANCE-REF", ref)
        self.setChildElementOptionalIdentifier(element, "ROLE", assignment.getRole())

    def writeRptSwPrototypingAccess(self, element: ET.Element, access: RptSwPrototypingAccess):
        self.setChildElementOptionalLiteral(element, "RPT-HOOK-ACCESS", access.getRptHookAccess())
        self.setChildElementOptionalLiteral(element, "RPT-READ-ACCESS", access.getRptReadAccess())
        self.setChildElementOptionalLiteral(element, "RPT-WRITE-ACCESS", access.getRptWriteAccess())

    def writeRptImplPolicy(self, element: ET.Element, policy: RptImplPolicy):
        self.setChildElementOptionalLiteral(element, "RPT-ENABLER-IMPL-TYPE", policy.getRptEnablerImplType())
        self.setChildElementOptionalLiteral(element, "RPT-PREPARATION-LEVEL", policy.getRptPreparationLevel())

    def writeRptExecutableEntityProperties(self, element: ET.Element, properties: RptExecutableEntityProperties):
        self.setChildElementOptionalPositiveInteger(element, "MAX-RPT-EVENT-ID", properties.getMaxRptEventId())
        self.setChildElementOptionalPositiveInteger(element, "MIN-RPT-EVENT-ID", properties.getMinRptEventId())
        self.setChildElementOptionalLiteral(element, "RPT-EXECUTION-CONTROL", properties.getRptExecutionControl())
        self.setChildElementOptionalLiteral(element, "RPT-SERVICE-POINT", properties.getRptServicePoint())

    def writeRptServicePoint(self, element: ET.Element, service_point: RptServicePoint):
        self.writeIdentifiable(element, service_point)
        self.setChildElementOptionalPositiveInteger(element, "SERVICE-ID", service_point.getServiceId())
        self.setChildElementOptionalLiteral(element, "SYMBOL", service_point.getSymbol())

    def writeRptExecutableEntityEvent(self, element: ET.Element, event: RptExecutableEntityEvent):
        self.writeIdentifiable(element, event)
        execution_context_refs = event.getExecutionContextRefs()
        if len(execution_context_refs) > 0:
            refs_element = ET.SubElement(element, "EXECUTION-CONTEXT-REFS")
            for ref in execution_context_refs:
                self.setChildElementOptionalRefType(refs_element, "EXECUTION-CONTEXT-REF", ref)
        mc_data_assignments = event.getMcDataAssignments()
        if len(mc_data_assignments) > 0:
            assignments_element = ET.SubElement(element, "MC-DATA-ASSIGNMENTS")
            for assignment in mc_data_assignments:
                self.writeRoleBasedMcDataAssignment(ET.SubElement(assignments_element, "ROLE-BASED-MC-DATA-ASSIGNMENT"), assignment)
        self.setChildElementOptionalPositiveInteger(element, "RPT-EVENT-ID", event.getRptEventId())
        if event.getRptExecutableEntityProperties() is not None:
            self.writeRptExecutableEntityProperties(ET.SubElement(element, "RPT-EXECUTABLE-ENTITY-PROPERTIES"), event.getRptExecutableEntityProperties())
        if event.getRptImplPolicy() is not None:
            self.writeRptImplPolicy(ET.SubElement(element, "RPT-IMPL-POLICY"), event.getRptImplPolicy())
        rpt_service_point_post_refs = event.getRptServicePointPostRefs()
        if len(rpt_service_point_post_refs) > 0:
            refs_element = ET.SubElement(element, "RPT-SERVICE-POINT-POST-REFS")
            for ref in rpt_service_point_post_refs:
                self.setChildElementOptionalRefType(refs_element, "RPT-SERVICE-POINT-POST-REF", ref)
        rpt_service_point_pre_refs = event.getRptServicePointPreRefs()
        if len(rpt_service_point_pre_refs) > 0:
            refs_element = ET.SubElement(element, "RPT-SERVICE-POINT-PRE-REFS")
            for ref in rpt_service_point_pre_refs:
                self.setChildElementOptionalRefType(refs_element, "RPT-SERVICE-POINT-PRE-REF", ref)

    def writeRptExecutableEntity(self, element: ET.Element, entity: RptExecutableEntity):
        self.writeIdentifiable(element, entity)
        rpt_executable_entity_events = entity.getRptExecutableEntityEvents()
        if len(rpt_executable_entity_events) > 0:
            events_element = ET.SubElement(element, "RPT-EXECUTABLE-ENTITY-EVENTS")
            for event in rpt_executable_entity_events:
                self.writeRptExecutableEntityEvent(ET.SubElement(events_element, "RPT-EXECUTABLE-ENTITY-EVENT"), event)
        rpt_reads = entity.getRptReads()
        if len(rpt_reads) > 0:
            reads_element = ET.SubElement(element, "RPT-READS")
            for assignment in rpt_reads:
                self.writeRoleBasedMcDataAssignment(ET.SubElement(reads_element, "ROLE-BASED-MC-DATA-ASSIGNMENT"), assignment)
        rpt_writes = entity.getRptWrites()
        if len(rpt_writes) > 0:
            writes_element = ET.SubElement(element, "RPT-WRITES")
            for assignment in rpt_writes:
                self.writeRoleBasedMcDataAssignment(ET.SubElement(writes_element, "ROLE-BASED-MC-DATA-ASSIGNMENT"), assignment)
        self.setChildElementOptionalLiteral(element, "SYMBOL", entity.getSymbol())

    def writeRptComponent(self, element: ET.Element, component: RptComponent):
        self.writeIdentifiable(element, component)
        mc_data_assignments = component.getMcDataAssignments()
        if len(mc_data_assignments) > 0:
            assignments_element = ET.SubElement(element, "MC-DATA-ASSIGNMENTS")
            for assignment in mc_data_assignments:
                self.writeRoleBasedMcDataAssignment(ET.SubElement(assignments_element, "ROLE-BASED-MC-DATA-ASSIGNMENT"), assignment)
        if component.getRpImplPolicy() is not None:
            self.writeRptImplPolicy(ET.SubElement(element, "RP-IMPL-POLICY"), component.getRpImplPolicy())
        rpt_executable_entities = component.getRptExecutableEntities()
        if len(rpt_executable_entities) > 0:
            entities_element = ET.SubElement(element, "RPT-EXECUTABLE-ENTITYS")
            for entity in rpt_executable_entities:
                self.writeRptExecutableEntity(ET.SubElement(entities_element, "RPT-EXECUTABLE-ENTITY"), entity)

    def writeRptSupportData(self, element: ET.Element, rpt_support_data: RptSupportData):
        child_element = ET.SubElement(element, "RPT-SUPPORT-DATA")
        execution_contexts = rpt_support_data.getExecutionContexts()
        if len(execution_contexts) > 0:
            contexts_element = ET.SubElement(child_element, "EXECUTION-CONTEXTS")
            for context in execution_contexts:
                self.writeIdentifiable(ET.SubElement(contexts_element, "RPT-EXECUTION-CONTEXT"), context)
        rpt_components = rpt_support_data.getRptComponents()
        if len(rpt_components) > 0:
            components_element = ET.SubElement(child_element, "RPT-COMPONENTS")
            for component in rpt_components:
                self.writeRptComponent(ET.SubElement(components_element, "RPT-COMPONENT"), component)
        rpt_service_points = rpt_support_data.getRptServicePoints()
        if len(rpt_service_points) > 0:
            service_points_element = ET.SubElement(child_element, "RPT-SERVICE-POINTS")
            for service_point in rpt_service_points:
                self.writeRptServicePoint(ET.SubElement(service_points_element, "RPT-SERVICE-POINT"), service_point)

    def writeImplementationBuildActionManifests(self, element: ET.Element, impl: Implementation):
        ref = impl.getBuildActionManifestRef()
        if ref is not None:
            child_element = ET.SubElement(element, "BUILD-ACTION-MANIFESTS")
            ref_cond = ET.SubElement(child_element, "BUILD-ACTION-MANIFEST-REF-CONDITIONAL")
            self.setChildElementOptionalRefType(ref_cond, "BUILD-ACTION-MANIFEST-REF", ref)

    def writeCompilers(self, element: ET.Element, impl: Implementation):
        compilers = impl.getCompilers()
        if len(compilers) > 0:
            child_element = ET.SubElement(element, "COMPILERS")
            for compiler in compilers:
                if isinstance(compiler, Compiler):
                    self.writeCompiler(child_element, compiler)
                else:
                    self.notImplemented("Unsupported Compiler <%s>" % type(compiler))

    def writeCompiler(self, element: ET.Element, compiler: Compiler):
        child_element = ET.SubElement(element, "COMPILER")
        self.writeIdentifiable(child_element, compiler)
        self.setChildElementOptionalLiteral(child_element, "NAME", compiler.getName())
        self.setChildElementOptionalLiteral(child_element, "OPTIONS", compiler.getOptions())
        self.setChildElementOptionalLiteral(child_element, "VENDOR", compiler.getVendor())
        self.setChildElementOptionalLiteral(child_element, "VERSION", compiler.getVersion())

    def writeLinkers(self, element: ET.Element, impl: Implementation):
        linkers = impl.getLinkers()
        if len(linkers) > 0:
            child_element = ET.SubElement(element, "LINKERS")
            for linker in linkers:
                if isinstance(linker, Linker):
                    self.writeLinker(child_element, linker)
                else:
                    self.notImplemented("Unsupported Linker <%s>" % type(linker))

    def writeLinker(self, element: ET.Element, linker: Linker):
        child_element = ET.SubElement(element, "LINKER")
        self.writeIdentifiable(child_element, linker)
        self.setChildElementOptionalLiteral(child_element, "NAME", linker.getName())
        self.setChildElementOptionalLiteral(child_element, "OPTIONS", linker.getOptions())
        self.setChildElementOptionalLiteral(child_element, "VENDOR", linker.getVendor())
        self.setChildElementOptionalLiteral(child_element, "VERSION", linker.getVersion())

    def writeDependencyOnArtifacts(self, element: ET.Element, impl: Implementation, key: str, dependencies: List[DependencyOnArtifact]):
        if len(dependencies) > 0:
            child_element = ET.SubElement(element, key)
            for dependency in dependencies:
                if isinstance(dependency, DependencyOnArtifact):
                    self.writeDependencyOnArtifact(child_element, dependency)
                else:
                    self.notImplemented("Unsupported DependencyOnArtifact <%s>" % type(dependency))

    def writeDependencyOnArtifact(self, element: ET.Element, dependency: DependencyOnArtifact):
        child_element = ET.SubElement(element, "DEPENDENCY-ON-ARTIFACT")
        self.writeIdentifiable(child_element, dependency)
        descriptor = dependency.getArtifactDescriptor()
        if descriptor is not None:
            descriptor_element = ET.SubElement(child_element, "ARTIFACT-DESCRIPTOR")
            self.writeAutosarEngineeringObject(descriptor_element, descriptor)
        usages = dependency.getUsages()
        if len(usages) > 0:
            usages_element = ET.SubElement(child_element, "USAGES")
            for usage in usages:
                self.setChildElementOptionalLiteral(usages_element, "USAGE", usage)

    def writeImplementationHwElementRefs(self, element: ET.Element, impl: Implementation):
        refs = impl.getHwElementRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "HW-ELEMENT-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "HW-ELEMENT-REF", ref)

    def writeSwcImplementation(self, element: ET.Element, impl: SwcImplementation):
        self.logger.debug("writeSwcImplementation %s" % impl.getShortName())
        child_element = ET.SubElement(element, "SWC-IMPLEMENTATION")
        self.writeImplementation(child_element, impl)
        self.setChildElementOptionalRefType(child_element, "BEHAVIOR-REF", impl.getBehaviorRef())

    def writeEndToEndDescriptionDataIds(self, element: ET.Element, parent: EndToEndDescription):
        data_ids = parent.getDataIds()
        if len(data_ids) > 0:
            child_element = ET.SubElement(element, "DATA-IDS")
            for data_id in data_ids:
                self.setChildElementOptionalNumericalValue(child_element, "DATA-ID", data_id)

    def setEndToEndDescription(self, element: ET.Element, key: str, desc: EndToEndDescription):
        if desc is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, desc)
            self.setChildElementOptionalLiteral(child_element, "CATEGORY", desc.getCategory())
            self.writeEndToEndDescriptionDataIds(child_element, desc)
            self.setChildElementOptionalPositiveInteger(child_element, "DATA-ID-MODE", desc.getDataIdMode())
            self.setChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH", desc.getDataLength())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-DELTA-COUNTER-INIT", desc.getMaxDeltaCounterInit())
            self.setChildElementOptionalPositiveInteger(child_element, "CRC-OFFSET", desc.getCrcOffset())
            self.setChildElementOptionalPositiveInteger(child_element, "COUNTER-OFFSET", desc.getCounterOffset())

    def setVariableDataPrototypeInSystemInstanceRef(self, element: ET.Element, key: str, instance_ref: VariableDataPrototypeInSystemInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, key)
            for ref in instance_ref.getContextComponentRefs():
                self.setChildElementOptionalRefType(child_element, "CONTEXT-COMPONENT-REF", ref)
            self.setChildElementOptionalRefType(child_element, "CONTEXT-COMPOSITION-REF", instance_ref.getContextCompositionRef())
            self.setChildElementOptionalRefType(child_element, "CONTEXT-PORT-REF", instance_ref.getContextPortRef())
            self.setChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-REF", instance_ref.getTargetDataPrototypeRef())

    def writeEndToEndProtectionVariablePrototype(self, element: ET.Element, prototype: EndToEndProtectionVariablePrototype):
        if prototype is not None:
            child_element = ET.SubElement(element, "END-TO-END-PROTECTION-VARIABLE-PROTOTYPE")
            self.writeARObjectAttributes(child_element, prototype)
            irefs = prototype.getReceiverIrefs()
            if len(irefs) > 0:
                child_element = ET.SubElement(child_element, "RECEIVER-IREFS")
                for iref in irefs:
                    self.setVariableDataPrototypeInSystemInstanceRef(child_element, "RECEIVER-IREF", iref)
            self.setVariableDataPrototypeInSystemInstanceRef(child_element, "SENDER-IREF", prototype.senderIRef)

    def writeEndToEndProtectionEndToEndProtectionVariablePrototypes(self, element: ET.Element, protection: EndToEndProtection):
        prototypes = protection.getEndToEndProtectionVariablePrototypes()
        if len(prototypes) > 0:
            child_element = ET.SubElement(element, "END-TO-END-PROTECTION-VARIABLE-PROTOTYPES")
            for prototype in prototypes:
                if isinstance(prototype, EndToEndProtectionVariablePrototype):
                    self.writeEndToEndProtectionVariablePrototype(child_element, prototype)
                else:
                    self.notImplemented("Unsupported End To End Protection Variable Prototype <%s>" % type(prototype))

    def writeEndToEndProtectionISignalIPdu(self, element: ET.Element, ipdu: EndToEndProtectionISignalIPdu):
        if ipdu is not None:
            child_element = ET.SubElement(element, "END-TO-END-PROTECTION-I-SIGNAL-I-PDU")
            self.setChildElementOptionalIntegerValue(child_element, "DATA-OFFSET", ipdu.getDataOffset())
            self.setChildElementOptionalRefType(child_element, "I-SIGNAL-GROUP-REF", ipdu.getISignalGroupRef())
            self.setChildElementOptionalRefType(child_element, "I-SIGNAL-I-PDU-REF", ipdu.getISignalIPduRef())

    def writeEndToEndProtectionEndToEndProtectionISignalIPdus(self, element: ET.Element, protection: EndToEndProtection):
        ipdus = protection.getEndToEndProtectionISignalIPdus()
        if len(ipdus) > 0:
            child_element = ET.SubElement(element, "END-TO-END-PROTECTION-I-SIGNAL-I-PDUS")
            for ipdu in ipdus:
                if isinstance(ipdu, EndToEndProtectionISignalIPdu):
                    self.writeEndToEndProtectionISignalIPdu(child_element, ipdu)
                else:
                    self.notImplemented("Unsupported EndToEndProtectionISignalIPdu <%s>" % type(ipdu))

    def writeEndToEndProtection(self, element: ET.Element, protection: EndToEndProtection):
        if protection is not None:
            child_element = ET.SubElement(element, "END-TO-END-PROTECTION")
            self.writeIdentifiable(child_element, protection)
            self.setEndToEndDescription(child_element, "END-TO-END-PROFILE", protection.getEndToEndProfile())
            self.writeEndToEndProtectionEndToEndProtectionISignalIPdus(child_element, protection)
            self.writeEndToEndProtectionEndToEndProtectionVariablePrototypes(child_element, protection)

    def writeEndToEndProtections(self, element: ET.Element, protection_set: EndToEndProtectionSet):
        protections = protection_set.getEndToEndProtections()
        if len(protections) > 0:
            child_element = ET.SubElement(element, "END-TO-END-PROTECTIONS")
            for protection in protections:
                if isinstance(protection, EndToEndProtection):
                    self.writeEndToEndProtection(child_element, protection)

    def writeEndToEndProtectionSet(self, element: ET.Element, protection_set: EndToEndProtectionSet):
        self.logger.debug("writeEndToEndProtectionSet %s" % protection_set.getShortName())
        child_element = ET.SubElement(element, "END-TO-END-PROTECTION-SET")
        self.writeIdentifiable(child_element, protection_set)
        self.writeEndToEndProtections(child_element, protection_set)

    def writeAutosarDataPrototype(self, element: ET.Element, prototype: AutosarDataPrototype):
        self.writeDataPrototype(element, prototype)
        self.setChildElementOptionalRefType(element, "TYPE-TREF", prototype.getTypeTRef())

    def writeVariableDataPrototype(self, element: ET.Element, prototype: VariableDataPrototype):
        self.logger.debug("writeVariableDataPrototype %s" % prototype.getShortName())
        child_element = ET.SubElement(element, "VARIABLE-DATA-PROTOTYPE")
        self.writeAutosarDataPrototype(child_element, prototype)
        self.setChildValueSpecification(child_element, "INIT-VALUE", prototype.getInitValue())

    def writeSenderReceiverInterfaceDataElements(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        data_elements = sr_interface.getDataElements()
        if len(data_elements) > 0:
            data_elements_tag = ET.SubElement(element, "DATA-ELEMENTS")
            for data_element in data_elements:
                if isinstance(data_element, VariableDataPrototype):
                    self.writeVariableDataPrototype(data_elements_tag, data_element)
                else:
                    self.notImplemented("Unsupported Data Element <%s>" % type(data_element))

    def writeSenderReceiverInterfaceInvalidationPolicies(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        policies = sr_interface.getInvalidationPolicies()
        if len(policies) > 0:
            policies_tag = ET.SubElement(element, "INVALIDATION-POLICYS")
            for policy in policies:
                child_element = ET.SubElement(policies_tag, "INVALIDATION-POLICY")
                self.setChildElementOptionalRefType(child_element, "DATA-ELEMENT-REF", policy.getDataElementRef())
                self.setChildElementOptionalLiteral(child_element, "HANDLE-INVALID", policy.getHandleInvalid())

    def writeSenderReceiverInterface(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        self.logger.debug("writeSenderReceiverInterface %s" % sr_interface.getShortName())
        child_element = ET.SubElement(element, "SENDER-RECEIVER-INTERFACE")
        self.writeIdentifiable(child_element, sr_interface)
        self.setChildElementOptionalBooleanValue(child_element, "IS-SERVICE", sr_interface.getIsService())
        self.writeSenderReceiverInterfaceDataElements(child_element, sr_interface)
        self.writeSenderReceiverInterfaceInvalidationPolicies(child_element, sr_interface)

    def writeBswModuleDescriptionImplementedEntryRefs(self, element: ET.Element, desc: BswModuleDescription):
        refs = desc.getImplementedEntryRefs()
        if len(refs) > 0:
            entries_tag = ET.SubElement(element, "PROVIDED-ENTRYS")
            for ref in refs:
                entry_tag = ET.SubElement(entries_tag, "BSW-MODULE-ENTRY-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(entry_tag, "BSW-MODULE-ENTRY-REF", ref)

    def writeModeDeclarationGroupPrototype(self, element: ET.Element, prototype: ModeDeclarationGroupPrototype):
        child_element = ET.SubElement(element, "MODE-DECLARATION-GROUP-PROTOTYPE")
        self.writeIdentifiable(child_element, prototype)
        self.setChildElementOptionalRefType(child_element, "TYPE-TREF", prototype.getTypeTRef())
        self.setChildElementOptionalLiteral(child_element, "SW-CALIBRATION-ACCESS", prototype.getSwCalibrationAccess())

    def writeBswModuleDescriptionProvidedModeGroups(self, element: ET.Element, parent: BswModuleDescription):
        mode_groups = parent.getProvidedModeGroups()
        if len(mode_groups) > 0:
            child_element = ET.SubElement(element, "PROVIDED-MODE-GROUPS")
            for mode_group in mode_groups:
                if isinstance(mode_group, ModeDeclarationGroupPrototype):
                    self.writeModeDeclarationGroupPrototype(child_element, mode_group)
                else:
                    self.notImplemented("Unsupported ProvidedModeGroup <%s>" % type(mode_group))

    def writeBswModuleDescriptionRequiredModeGroups(self, element: ET.Element, desc: BswModuleDescription):
        mode_groups = desc.getRequiredModeGroups()
        if len(mode_groups) > 0:
            child_element = ET.SubElement(element, "REQUIRED-MODE-GROUPS")
            for mode_group in mode_groups:
                if isinstance(mode_group, ModeDeclarationGroupPrototype):
                    self.writeModeDeclarationGroupPrototype(child_element, mode_group)
                else:
                    self.notImplemented("Unsupported ProvidedModeGroup <%s>" % type(mode_group))

    def writeActivationReasons(self, element: ET.Element, entity: ExecutableEntity):
        reasons = entity.getActivationReasons()
        if len(reasons) > 0:
            reasons_tag = ET.SubElement(element, "ACTIVATION-REASONS")
            for reason in reasons:
                if isinstance(reason, ExecutableEntityActivationReason):
                    self.writeExecutableEntityActivationReason(ET.SubElement(reasons_tag, "EXECUTABLE-ENTITY-ACTIVATION-REASON"), reason)
                else:
                    self.notImplemented("Unsupported ExecutableEntityActivationReason <%s>" % type(reason))

    def writeExecutableEntityActivationReason(self, element: ET.Element, reason: ExecutableEntityActivationReason):
        self.writeImplementationProps(element, reason)
        self.setChildElementOptionalPositiveInteger(element, "BIT-POSITION", reason.getBitPosition())

    def writeCanEnterRefs(self, element: ET.Element, entity: ExecutableEntity):
        refs = entity.getCanEnterRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "CAN-ENTER-EXCLUSIVE-AREA-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "CAN-ENTER-EXCLUSIVE-AREA-REF", ref)

    def writeExclusiveAreaNestingOrderRefs(self, element: ET.Element, entity: ExecutableEntity):
        refs = entity.getExclusiveAreaNestingOrderRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "EXCLUSIVE-AREA-NESTING-ORDER-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "EXCLUSIVE-AREA-NESTING-ORDER-REF", ref)

    def writeRunsInsideRefs(self, element: ET.Element, entity: ExecutableEntity):
        refs = entity.getRunsInsideRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "RUNS-INSIDE-EXCLUSIVE-AREA-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "RUNS-INSIDE-EXCLUSIVE-AREA-REF", ref)

    def writeExecutableEntity(self, element: ET.Element, entity: ExecutableEntity):
        self.writeIdentifiable(element, entity)
        self.writeActivationReasons(element, entity)
        self.writeCanEnterRefs(element, entity)
        self.writeExclusiveAreaNestingOrderRefs(element, entity)
        self.setChildElementOptionalTimeValue(element, "MINIMUM-START-INTERVAL", entity.getMinimumStartInterval())
        self.setChildElementOptionalLiteral(element, "REENTRANCY-LEVEL", entity.getReentrancyLevel())
        self.writeRunsInsideRefs(element, entity)
        self.setChildElementOptionalRefType(element, "SW-ADDR-METHOD-REF", entity.getSwAddrMethodRef())

    def writeBswModuleEntityManagedModeGroups(self, element: ET.Element, entity: BswModuleEntity):
        mode_group_refs = entity.getManagedModeGroupRefs()
        if len(mode_group_refs) > 0:
            mode_groups_tag = ET.SubElement(element, "MANAGED-MODE-GROUPS")
            for mode_group_ref in mode_group_refs:
                child_element = ET.SubElement(mode_groups_tag, "MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "MODE-DECLARATION-GROUP-PROTOTYPE-REF", mode_group_ref)

    def writeBswModuleEntityAccessedModeGroups(self, element: ET.Element, entity: BswModuleEntity):
        mode_group_refs = entity.getAccessedModeGroupRefs()
        if len(mode_group_refs) > 0:
            mode_groups_tag = ET.SubElement(element, "ACCESSED-MODE-GROUPS")
            for mode_group_ref in mode_group_refs:
                child_element = ET.SubElement(mode_groups_tag, "MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "MODE-DECLARATION-GROUP-PROTOTYPE-REF", mode_group_ref)

    def writeBswVariableAccess(self, element: ET.Element, access: BswVariableAccess):
        if access is not None:
            child_element = ET.SubElement(element, "BSW-VARIABLE-ACCESS")
            self.writeReferrable(child_element, access)
            self.setChildElementOptionalRefType(child_element, "ACCESSED-VARIABLE-REF", access.getAccessedVariableRef())

    def writeBswModuleEntityDataSendPoints(self, element: ET.Element, entity: BswModuleEntity):
        points = entity.getDataSendPoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "DATA-SEND-POINTS")
            for point in points:
                if isinstance(point, BswVariableAccess):
                    self.writeBswVariableAccess(child_element, point)
                else:
                    self.notImplemented("Unsupported Data Send Point <%s>" % type(point))

    def writeBswModuleEntityDataReceivePoints(self, element: ET.Element, entity: BswModuleEntity):
        points = entity.getDataReceivePoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "DATA-RECEIVE-POINTS")
            for point in points:
                if isinstance(point, BswVariableAccess):
                    self.writeBswVariableAccess(child_element, point)
                else:
                    self.notImplemented("Unsupported Data Receive Point <%s>" % type(point))

    def writeBswModuleEntityIssuedTriggerRefs(self, element: ET.Element, entity: BswModuleEntity):
        refs = entity.getIssuedTriggerRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "ISSUED-TRIGGERS")
            for ref in refs:
                cond_tag = ET.SubElement(child_element, "TRIGGER-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(cond_tag, "TRIGGER-REF", ref)

    def writeBswModuleEntityActivationPointRefs(self, element: ET.Element, entity: BswModuleEntity):
        refs = entity.getActivationPointRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "ACTIVATION-POINTS")
            for ref in refs:
                cond_tag = ET.SubElement(child_element, "BSW-INTERNAL-TRIGGERING-POINT-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(cond_tag, "BSW-INTERNAL-TRIGGERING-POINT-REF", ref)

    def writeBswModuleCallPoint(self, element: ET.Element, point: BswModuleCallPoint):
        self.writeReferrable(element, point)

    def writeBswAsynchronousServerCallPoint(self, element: ET.Element, point: BswAsynchronousServerCallPoint):
        child_element = ET.SubElement(element, "BSW-ASYNCHRONOUS-SERVER-CALL-POINT")
        self.writeBswModuleCallPoint(child_element, point)
        self.setChildElementOptionalRefType(child_element, "CALLED-ENTRY-REF", point.getCalledEntryRef())

    def writeBswAsynchronousServerCallResultPoint(self, element: ET.Element, point: BswAsynchronousServerCallResultPoint):
        child_element = ET.SubElement(element, "BSW-ASYNCHRONOUS-SERVER-CALL-RESULT-POINT")
        self.writeBswModuleCallPoint(child_element, point)
        self.setChildElementOptionalRefType(child_element, "ASYNCHRONOUS-SERVER-CALL-POINT-REF", point.getAsynchronousServerCallPointRef())

    def writeBswSynchronousServerCallPoint(self, element: ET.Element, point: BswSynchronousServerCallPoint):
        child_element = ET.SubElement(element, "BSW-SYNCHRONOUS-SERVER-CALL-POINT")
        self.writeBswModuleCallPoint(child_element, point)
        self.setChildElementOptionalRefType(child_element, "CALLED-ENTRY-REF", point.getCalledEntryRef())

    def writeBswModuleEntityCallPoints(self, element: ET.Element, entity: BswModuleEntity):
        points = entity.getCallPoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "CALL-POINTS")
            for point in points:
                if isinstance(point, BswAsynchronousServerCallResultPoint):
                    self.writeBswAsynchronousServerCallResultPoint(child_element, point)
                elif isinstance(point, BswAsynchronousServerCallPoint):
                    self.writeBswAsynchronousServerCallPoint(child_element, point)
                elif isinstance(point, BswSynchronousServerCallPoint):
                    self.writeBswSynchronousServerCallPoint(child_element, point)
                else:
                    self.notImplemented("Unsupported Call Point <%s>" % type(point))

    def writeBswModuleEntity(self, element: ET.Element, entity: BswModuleEntity):
        self.writeExecutableEntity(element, entity)
        self.writeBswModuleEntityAccessedModeGroups(element, entity)
        self.writeBswModuleEntityActivationPointRefs(element, entity)
        self.writeBswModuleEntityCallPoints(element, entity)
        self.writeBswModuleEntityDataSendPoints(element, entity)
        self.writeBswModuleEntityDataReceivePoints(element, entity)
        self.setChildElementOptionalRefType(element, "IMPLEMENTED-ENTRY-REF", entity.implementedEntryRef)
        self.setChildElementOptionalRefType(element, "SCHEDULER-NAME-PREFIX-REF", entity.getSchedulerNamePrefixRef())
        self.writeBswModuleEntityManagedModeGroups(element, entity)
        self.writeBswModuleEntityIssuedTriggerRefs(element, entity)

    def writeBswCalledEntity(self, element: ET.Element, entity: BswCalledEntity):
        self.logger.debug("Write BswCalledEntity <%s>" % entity.getShortName())
        child_element = ET.SubElement(element, "BSW-CALLED-ENTITY")
        self.writeBswModuleEntity(child_element, entity)

    def writeBswSchedulableEntity(self, element: ET.Element, entity: BswSchedulableEntity):
        self.logger.debug("Write BswSchedulableEntity <%s>" % entity.getShortName())
        child_element = ET.SubElement(element, "BSW-SCHEDULABLE-ENTITY")
        self.writeBswModuleEntity(child_element, entity)

    def setBswInterruptEntity(self, element: ET.Element, entity: BswInterruptEntity):
        self.logger.debug("Write BswInterruptEntity <%s>" % entity.getShortName())
        child_element = ET.SubElement(element, "BSW-INTERRUPT-ENTITY")
        self.writeBswModuleEntity(child_element, entity)
        self.setChildElementOptionalLiteral(child_element, "INTERRUPT-CATEGORY", entity.getInterruptCategory())
        self.setChildElementOptionalLiteral(child_element, "INTERRUPT-SOURCE", entity.getInterruptSource())

    def writeBswInternalBehaviorEntities(self, element: ET.Element, parent: BswInternalBehavior):
        entities = parent.getBswModuleEntities()
        if len(entities) > 0:
            child_element = ET.SubElement(element, "ENTITYS")
            for entity in entities:
                if isinstance(entity, BswCalledEntity):
                    self.writeBswCalledEntity(child_element, entity)
                elif isinstance(entity, BswSchedulableEntity):
                    self.writeBswSchedulableEntity(child_element, entity)
                elif isinstance(entity, BswInterruptEntity):
                    self.setBswInterruptEntity(child_element, entity)
                else:
                    self.notImplemented("Unsupported BswModuleEntity <%s>" % type(entity))

    def writeBswEvent(self, element: ET.Element, event: BswEvent):
        self.writeIdentifiable(element, event)
        self.setChildElementOptionalRefType(element, "ACTIVATION-REASON-REPRESENTATION-REF", event.getActivationReasonRepresentationRef())
        context_limitations = event.getContextLimitationRefs()
        if len(context_limitations) > 0:
            child_element = ET.SubElement(element, "CONTEXT-LIMITATION-REFS")
            for ref in context_limitations:
                self.setChildElementOptionalRefType(child_element, "CONTEXT-LIMITATION-REF", ref)
        disabled_modes = event.getDisabledInModeIRefs()
        if len(disabled_modes) > 0:
            child_element = ET.SubElement(element, "DISABLED-IN-MODE-IREFS")
            for iref in disabled_modes:
                self.setModeInBswModuleDescriptionInstanceRef(child_element, "DISABLED-IN-MODE-IREF", iref)
        self.setChildElementOptionalRefType(element, "STARTS-ON-EVENT-REF", event.getStartsOnEventRef())

    def writeBswScheduleEvent(self, element: ET.Element, event: BswScheduleEvent):
        self.writeBswEvent(element, event)

    def writeBswTimingEvent(self, element: ET.Element, event: BswTimingEvent):
        self.logger.debug("Write BswTimingEvent <%s>" % event.getShortName())
        child_element = ET.SubElement(element, "BSW-TIMING-EVENT")
        self.writeBswScheduleEvent(child_element, event)
        self.setChildElementOptionalTimeValue(child_element, "PERIOD", event.getPeriod())

    def writeBswBackgroundEvent(self, element: ET.Element, event: BswBackgroundEvent):
        self.logger.debug("Write BswTimingEvent <%s>" % event.getShortName())
        child_element = ET.SubElement(element, "BSW-BACKGROUND-EVENT")
        self.writeBswScheduleEvent(child_element, event)

    def writeBswInterruptEvent(self, element: ET.Element, event):
        self.logger.debug("Write BswInterruptEvent <%s>" % event.getShortName())
        child_element = ET.SubElement(element, "BSW-INTERRUPT-EVENT")
        self.writeBswEvent(child_element, event)

    def writeBswOsTaskExecutionEvent(self, element: ET.Element, event: BswOsTaskExecutionEvent):
        self.logger.debug("Write BswOsTaskExecutionEvent <%s>" % event.getShortName())
        child_element = ET.SubElement(element, "BSW-OS-TASK-EXECUTION-EVENT")
        self.writeBswScheduleEvent(child_element, event)

    def writeBswInternalTriggerOccurredEvent(self, element: ET.Element, event: BswInternalTriggerOccurredEvent):
        self.logger.debug("Write BswInternalTriggerOccurredEvent <%s>" % event.getShortName())
        child_element = ET.SubElement(element, "BSW-INTERNAL-TRIGGER-OCCURRED-EVENT")
        self.writeBswScheduleEvent(child_element, event)
        self.setChildElementOptionalRefType(child_element, "EVENT-SOURCE-REF", event.getEventSourceRef())

    def writeBswExternalTriggerOccurredEvent(self, element: ET.Element, event: BswExternalTriggerOccurredEvent):
        self.logger.debug("Write BswExternalTriggerOccurredEvent <%s>" % event.getShortName())
        child_element = ET.SubElement(element, "BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT")
        self.writeBswScheduleEvent(child_element, event)
        self.setChildElementOptionalRefType(child_element, "TRIGGER-REF", event.getTriggerRef())

    def writeBswDataReceivedEvent(self, element: ET.Element, event: BswDataReceivedEvent):
        self.logger.debug("Write BswDataReceivedEvent <%s>" % event.getShortName())
        # Read the Inherit BswScheduleEvent
        child_element = ET.SubElement(element, "BSW-DATA-RECEIVED-EVENT")
        self.writeBswScheduleEvent(child_element, event)
        self.setChildElementOptionalRefType(child_element, "DATA-REF", event.getDataRef())

    def writeBswOperationInvokedEvent(self, element: ET.Element, event: BswOperationInvokedEvent):
        self.logger.debug("Write BswOperationInvokedEvent <%s>" % event.getShortName())
        # Read the Inherit BswScheduleEvent
        child_element = ET.SubElement(element, "BSW-OPERATION-INVOKED-EVENT")
        self.writeBswEvent(child_element, event)
        self.setChildElementOptionalRefType(child_element, "ENTRY-REF", event.getEntryRef())

    def writeBswModeSwitchEvent(self, element: ET.Element, event: BswModeSwitchEvent):
        self.logger.debug("Write BswModeSwitchEvent <%s>" % event.getShortName())
        child_element = ET.SubElement(element, "BSW-MODE-SWITCH-EVENT")
        self.writeBswScheduleEvent(child_element, event)
        self.setChildElementOptionalLiteral(child_element, "ACTIVATION", event.getActivation())
        irefs = event.getModeIRefs()
        if len(irefs) > 0:
            mode_irefs_tag = ET.SubElement(child_element, "MODE-IREFS")
            for iref in irefs:
                self.setModeInBswModuleDescriptionInstanceRef(mode_irefs_tag, "MODE-IREF", iref)

    def writeBswModeManagerErrorEvent(self, element: ET.Element, event: BswModeManagerErrorEvent):
        self.logger.debug("Write BswModeManagerErrorEvent <%s>" % event.getShortName())
        child_element = ET.SubElement(element, "BSW-MODE-MANAGER-ERROR-EVENT")
        self.writeBswScheduleEvent(child_element, event)
        self.setChildElementOptionalRefType(child_element, "MODE-GROUP-REF", event.getModeGroupRef())

    def writeBswModeSwitchedAckEvent(self, element: ET.Element, event: BswModeSwitchedAckEvent):
        self.logger.debug("Write BswModeSwitchedAckEvent <%s>" % event.getShortName())
        child_element = ET.SubElement(element, "BSW-MODE-SWITCHED-ACK-EVENT")
        self.writeBswScheduleEvent(child_element, event)
        self.setChildElementOptionalRefType(child_element, "MODE-GROUP-REF", event.getModeGroupRef())

    def writeBswAsynchronousServerCallReturnsEvent(self, element: ET.Element, event: BswAsynchronousServerCallReturnsEvent):
        self.logger.debug("Write BswAsynchronousServerCallReturnsEvent <%s>" % event.getShortName())
        child_element = ET.SubElement(element, "BSW-ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT")
        self.writeBswScheduleEvent(child_element, event)
        self.setChildElementOptionalRefType(child_element, "EVENT-SOURCE-REF", event.getEventSourceRef())

    def writeBswInternalBehaviorEvents(self, element: ET.Element, parent: BswInternalBehavior):
        events = parent.getBswEvents()
        if len(events) > 0:
            child_element = ET.SubElement(element, "EVENTS")
            for event in events:
                if isinstance(event, BswTimingEvent):
                    self.writeBswTimingEvent(child_element, event)
                elif isinstance(event, BswBackgroundEvent):
                    self.writeBswBackgroundEvent(child_element, event)
                elif isinstance(event, BswOsTaskExecutionEvent):
                    self.writeBswOsTaskExecutionEvent(child_element, event)
                elif isinstance(event, BswInterruptEvent):
                    self.writeBswInterruptEvent(child_element, event)
                elif isinstance(event, BswInternalTriggerOccurredEvent):
                    self.writeBswInternalTriggerOccurredEvent(child_element, event)
                elif isinstance(event, BswExternalTriggerOccurredEvent):
                    self.writeBswExternalTriggerOccurredEvent(child_element, event)
                elif isinstance(event, BswDataReceivedEvent):
                    self.writeBswDataReceivedEvent(child_element, event)
                elif isinstance(event, BswOperationInvokedEvent):
                    self.writeBswOperationInvokedEvent(child_element, event)
                elif isinstance(event, BswModeSwitchEvent):
                    self.writeBswModeSwitchEvent(child_element, event)
                elif isinstance(event, BswModeManagerErrorEvent):
                    self.writeBswModeManagerErrorEvent(child_element, event)
                elif isinstance(event, BswModeSwitchedAckEvent):
                    self.writeBswModeSwitchedAckEvent(child_element, event)
                elif isinstance(event, BswAsynchronousServerCallReturnsEvent):
                    self.writeBswAsynchronousServerCallReturnsEvent(child_element, event)
                else:
                    self.notImplemented("Unsupported BswModuleEntity <%s>" % type(event))

    def setBswModeSenderPolicy(self, element: ET.Element, policy: BswModeSenderPolicy):
        child_element = ET.SubElement(element, "BSW-MODE-SENDER-POLICY")
        self.setBswModeSwitchAckRequest(child_element, "ACK-REQUEST", policy.getAckRequest())
        self.setChildElementOptionalBooleanValue(child_element, "ENHANCED-MODE-API", policy.getEnhancedModeApi())
        self.setChildElementOptionalRefType(child_element, "PROVIDED-MODE-GROUP-REF", policy.getProvidedModeGroupRef())
        self.setChildElementOptionalPositiveInteger(child_element, "QUEUE-LENGTH", policy.getQueueLength())

    def setBswModeSwitchAckRequest(self, element: ET.Element, key: str, request: BswModeSwitchAckRequest):
        if request is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT", request.getTimeout())

    def writeBswInternalBehaviorModeSenderPolicy(self, element: ET.Element, parent: BswInternalBehavior):
        policies = parent.getModeSenderPolicies()
        if len(policies) > 0:
            child_element = ET.SubElement(element, "MODE-SENDER-POLICYS")
            for policy in policies:
                if isinstance(policy, BswModeSenderPolicy):
                    self.setBswModeSenderPolicy(child_element, policy)
                else:
                    self.notImplemented("Unsupported ModeSenderPolicy type <%s>." % type(policy))

    def writeBswInternalBehaviorIncludedModeDeclarationGroupSets(self, element: ET.Element, behavior: BswInternalBehavior):
        group_sets = behavior.getIncludedModeDeclarationGroupSets()
        if len(group_sets) > 0:
            child_element = ET.SubElement(element, "INCLUDED-MODE-DECLARATION-GROUP-SETS")
            for group_set in group_sets:
                self.writeIncludedModeDeclarationGroupSet(child_element, group_set)

    def writeBswApiOptions(self, element: ET.Element, options: BswApiOptions):
        self.writeARObjectAttributes(element, options)
        self.setChildElementOptionalBooleanValue(element, "ENABLE-TAKE-ADDRESS", options.getEnableTakeAddress())

    def writeBswDataReceptionPolicy(self, element: ET.Element, policy: BswDataReceptionPolicy):
        self.writeBswApiOptions(element, policy)
        self.setChildElementOptionalRefType(element, "RECEIVED-DATA-REF", policy.getReceivedDataRef())

    def writeBswQueuedDataReceptionPolicy(self, element: ET.Element, policy: BswQueuedDataReceptionPolicy):
        child_element = ET.SubElement(element, "BSW-QUEUED-DATA-RECEPTION-POLICY")
        self.writeBswDataReceptionPolicy(child_element, policy)
        self.setChildElementOptionalPositiveInteger(child_element, "QUEUE-LENGTH", policy.getQueueLength())

    def writeBswInternalBehaviorReceptionPolicies(self, element: ET.Element, behavior: BswInternalBehavior):
        policies = behavior.getReceptionPolicies()
        if len(policies) > 0:
            child_element = ET.SubElement(element, "RECEPTION-POLICYS")
            for policy in policies:
                if isinstance(policy, BswQueuedDataReceptionPolicy):
                    self.writeBswQueuedDataReceptionPolicy(child_element, policy)
                else:
                    self.notImplemented("Unsupported Reception Policies <%s>" % type(policy))

    def writeBswInternalTriggeringPoint(self, element: ET.Element, point: BswInternalTriggeringPoint):
        child_element = ET.SubElement(element, "BSW-INTERNAL-TRIGGERING-POINT")
        self.writeIdentifiable(child_element, point)

    def writeBswInternalBehaviorInternalTriggeringPoints(self, element: ET.Element, behavior: BswInternalBehavior):
        points = behavior.getInternalTriggeringPoints()
        if len(points) > 0:
            child_element = ET.SubElement(element, "INTERNAL-TRIGGERING-POINTS")
            for point in points:
                if isinstance(point, BswInternalTriggeringPoint):
                    self.writeBswInternalTriggeringPoint(child_element, point)
                else:
                    self.notImplemented("Unsupported Internal Triggering Points <%s>" % type(point))

    def writeBswInternalBehavior(self, element: ET.Element, behavior: BswInternalBehavior):
        child_element = ET.SubElement(element, "BSW-INTERNAL-BEHAVIOR")
        self.writeInternalBehavior(child_element, behavior)
        self.writeBswInternalBehaviorInternalTriggeringPoints(child_element, behavior)
        self.writeBswInternalBehaviorEntities(child_element, behavior)
        self.writeBswInternalBehaviorEvents(child_element, behavior)
        self.writeBswInternalBehaviorModeSenderPolicy(child_element, behavior)
        self.writeBswInternalBehaviorIncludedModeDeclarationGroupSets(child_element, behavior)
        self.writeBswInternalBehaviorReceptionPolicies(child_element, behavior)
        self.writeBswInternalBehaviorSchedulerNamePrefixes(child_element, behavior)
        self.writeBswInternalBehaviorDistinguishedPartitions(child_element, behavior)
        self.writeBswInternalBehaviorServiceDependencies(child_element, behavior)

    def writeBswInternalBehaviorSchedulerNamePrefixes(self, element: ET.Element, behavior: BswInternalBehavior):
        prefixes = behavior.getSchedulerNamePrefixes()
        if len(prefixes) > 0:
            prefixes_tag = ET.SubElement(element, "SCHEDULER-NAME-PREFIXS")
            for prefix in prefixes:
                if isinstance(prefix, BswSchedulerNamePrefix):
                    child = ET.SubElement(prefixes_tag, "BSW-SCHEDULER-NAME-PREFIX")
                    self.writeImplementationProps(child, prefix)
                else:
                    self.notImplemented("Unsupported Scheduler Name Prefix <%s>" % type(prefix))

    def writeBswInternalBehaviorDistinguishedPartitions(self, element: ET.Element, behavior: BswInternalBehavior):
        partitions = behavior.getDistinguishedPartitions()
        if len(partitions) > 0:
            partitions_tag = ET.SubElement(element, "DISTINGUISHED-PARTITIONS")
            for partition in partitions:
                if isinstance(partition, BswDistinguishedPartition):
                    child = ET.SubElement(partitions_tag, "BSW-DISTINGUISHED-PARTITION")
                    self.writeReferrable(child, partition)
                else:
                    self.notImplemented("Unsupported Distinguished Partition <%s>" % type(partition))

    def writeBswModuleDescriptionInternalBehaviors(self, element: ET.Element, desc: BswModuleDescription):
        behaviors = desc.getInternalBehaviors()
        if len(behaviors) > 0:
            child_element = ET.SubElement(element, "INTERNAL-BEHAVIORS")
            for behavior in behaviors:
                if isinstance(behavior, BswInternalBehavior):
                    self.writeBswInternalBehavior(child_element, behavior)
                else:
                    self.notImplemented("Unsupported Internal Behavior <%s>" % type(behavior))

    def writeTrigger(self, element: ET.Element, trigger: Trigger):
        child_element = ET.SubElement(element, "TRIGGER")
        self.writeIdentifiable(child_element, trigger)

    def writeBswModuleDescriptionReleasedTriggers(self, element: ET.Element, desc: BswModuleDescription):
        triggers = desc.getReleasedTriggers()
        if len(triggers) > 0:
            child_element = ET.SubElement(element, "RELEASED-TRIGGERS")
            for trigger in triggers:
                if isinstance(trigger, Trigger):
                    self.writeTrigger(child_element, trigger)
                else:
                    self.notImplemented("Unsupported Released Trigger <%s>" % type(trigger))

    def writeBswModuleDescriptionRequiredTriggers(self, element: ET.Element, desc: BswModuleDescription):
        triggers = desc.getRequiredTriggers()
        if len(triggers) > 0:
            child_element = ET.SubElement(element, "REQUIRED-TRIGGERS")
            for trigger in triggers:
                if isinstance(trigger, Trigger):
                    self.writeTrigger(child_element, trigger)
                else:
                    self.notImplemented("Unsupported Required Trigger <%s>" % type(trigger))

    def writeBswModuleDescriptionProvidedDatas(self, element: ET.Element, desc: BswModuleDescription):
        datas = desc.getProvidedDatas()
        if len(datas) > 0:
            child_element = ET.SubElement(element, "PROVIDED-DATAS")
            for data in datas:
                if isinstance(data, VariableDataPrototype):
                    self.writeVariableDataPrototype(child_element, data)
                else:
                    self.notImplemented("Unsupported Provided Data <%s>" % type(data))

    def writeBswModuleDescriptionRequiredDatas(self, element: ET.Element, desc: BswModuleDescription):
        datas = desc.getRequiredDatas()
        if len(datas) > 0:
            child_element = ET.SubElement(element, "REQUIRED-DATAS")
            for data in datas:
                if isinstance(data, VariableDataPrototype):
                    self.writeVariableDataPrototype(child_element, data)
                else:
                    self.notImplemented("Unsupported Required Data <%s>" % type(data))

    def writeBswModuleClientServerEntry(self, element: ET.Element, entry: BswModuleClientServerEntry):
        if entry is not None:
            child_element = ET.SubElement(element, "BSW-MODULE-CLIENT-SERVER-ENTRY")
            self.writeReferrable(child_element, entry)
            self.setChildElementOptionalRefType(child_element, "ENCAPSULATED-ENTRY-REF", entry.getEncapsulatedEntryRef())
            self.setChildElementOptionalBooleanValue(child_element, "IS-REENTRANT", entry.getIsReentrant())
            self.setChildElementOptionalBooleanValue(child_element, "IS-SYNCHRONOUS", entry.getIsSynchronous())

    def writeBswModuleDescriptionProvidedClientServerEntries(self, element: ET.Element, desc: BswModuleDescription):
        entries = desc.getProvidedClientServerEntries()
        if len(entries) > 0:
            child_element = ET.SubElement(element, "PROVIDED-CLIENT-SERVER-ENTRYS")
            for entry in entries:
                if isinstance(entry, BswModuleClientServerEntry):
                    self.writeBswModuleClientServerEntry(child_element, entry)
                else:
                    self.notImplemented("Unsupported Provided Client Server Entry <%s>" % type(entry))

    def writeBswModuleDescriptionRequiredClientServerEntries(self, element: ET.Element, desc: BswModuleDescription):
        entries = desc.getRequiredClientServerEntries()
        if len(entries) > 0:
            child_element = ET.SubElement(element, "REQUIRED-CLIENT-SERVER-ENTRYS")
            for entry in entries:
                if isinstance(entry, BswModuleClientServerEntry):
                    self.writeBswModuleClientServerEntry(child_element, entry)
                else:
                    self.notImplemented("Unsupported Provided Client Server Entry <%s>" % type(entry))

    def writeBswModuleDescription(self, element: ET.Element, desc: BswModuleDescription):
        self.logger.debug("writeBswModuleDescription %s" % desc.getShortName())
        child_element = ET.SubElement(element, "BSW-MODULE-DESCRIPTION")
        self.writeIdentifiable(child_element, desc)
        self.setChildElementOptionalNumericalValue(child_element, "MODULE-ID", desc.getModuleId())
        self.writeBswModuleDescriptionImplementedEntryRefs(child_element, desc)
        self.writeBswModuleDescriptionProvidedModeGroups(child_element, desc)
        self.writeBswModuleDescriptionRequiredModeGroups(child_element, desc)
        self.writeBswModuleDescriptionProvidedClientServerEntries(child_element, desc)
        self.writeBswModuleDescriptionRequiredClientServerEntries(child_element, desc)
        self.writeBswModuleDescriptionProvidedDatas(child_element, desc)
        self.writeBswModuleDescriptionRequiredDatas(child_element, desc)
        self.writeBswModuleDescriptionInternalBehaviors(child_element, desc)
        self.writeBswModuleDescriptionReleasedTriggers(child_element, desc)
        self.writeBswModuleDescriptionExpectedEntryRefs(child_element, desc)
        self.writeBswModuleDescriptionBswModuleDependencies(child_element, desc)
        self.writeBswModuleDescriptionBswModuleDocumentation(child_element, desc)

    def writeBswModuleDescriptionExpectedEntryRefs(self, element: ET.Element, desc: BswModuleDescription):
        refs = desc.getExpectedEntryRefs()
        if len(refs) > 0:
            entries_tag = ET.SubElement(element, "EXPECTED-ENTRYS")
            for ref in refs:
                entry_tag = ET.SubElement(entries_tag, "BSW-MODULE-ENTRY-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(entry_tag, "BSW-MODULE-ENTRY-REF", ref)

    def writeBswModuleDescriptionBswModuleDependencies(self, element: ET.Element, desc: BswModuleDescription):
        dependencies = desc.getBswModuleDependencies()
        if len(dependencies) > 0:
            container = ET.SubElement(element, "BSW-MODULE-DEPENDENCYS")
            for dependency in dependencies:
                if isinstance(dependency, BswModuleDependency):
                    child_element = ET.SubElement(container, "BSW-MODULE-DEPENDENCY")
                    self.writeIdentifiable(child_element, dependency)
                    self.setChildElementOptionalNumericalValue(child_element, "TARGET-MODULE-ID", dependency.getTargetModuleId())
                    self.setChildElementOptionalRefType(child_element, "TARGET-MODULE-REF", dependency.getTargetModuleRef())
                else:
                    self.notImplemented("Unsupported BswModuleDependency <%s>" % type(dependency))

    def writeBswModuleDescriptionBswModuleDocumentation(self, element: ET.Element, desc: BswModuleDescription):
        documentation = desc.getBswModuleDocumentation()
        if documentation is None:
            return
        container = ET.SubElement(element, "BSW-MODULE-DOCUMENTATIONS")
        child_element = ET.SubElement(container, "SW-COMPONENT-DOCUMENTATION")
        self.writeSwComponentDocumentationElement(child_element, documentation)

    def setSwServiceArg(self, element: ET.Element, key: str, arg: SwServiceArg):
        if arg is not None:
            self.logger.debug("Set SwServiceArg <%s>" % arg.getShortName())
            child_element = ET.SubElement(element, key)
            self.writeIdentifiable(child_element, arg)
            self.setChildElementOptionalLiteral(child_element, "DIRECTION", arg.getDirection())
            self.setValueList(child_element, "SW-ARRAYSIZE", arg.getSwArraysize())
            self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", arg.getSwDataDefProps())

    def writeBswModuleEntryArguments(self, element: ET.Element, entry: BswModuleEntry):
        arguments = entry.getArguments()
        if len(arguments) > 0:
            child_element = ET.SubElement(element, "ARGUMENTS")
            for argument in arguments:
                self.setSwServiceArg(child_element, "SW-SERVICE-ARG", argument)

    def writeBswModuleEntryReturnType(self, element: ET.Element, entry: BswModuleEntry):
        if entry.getReturnType() is not None:
            self.setSwServiceArg(element, "RETURN-TYPE", entry.getReturnType())

    def writeBswModuleEntry(self, element: ET.Element, entry: BswModuleEntry):
        self.logger.debug("writeBswModuleDescription %s" % entry.getShortName())
        child_element = ET.SubElement(element, "BSW-MODULE-ENTRY")
        self.writeIdentifiable(child_element, entry)
        self.setChildElementOptionalNumericalValue(child_element, "SERVICE-ID", entry.getServiceId())
        self.setChildElementOptionalBooleanValue(child_element, "IS-REENTRANT", entry.getIsReentrant())
        self.setChildElementOptionalBooleanValue(child_element, "IS-SYNCHRONOUS", entry.getIsSynchronous())
        self.setChildElementOptionalLiteral(child_element, "CALL-TYPE", entry.getCallType())
        self.setChildElementOptionalLiteral(child_element, "EXECUTION-CONTEXT", entry.getExecutionContext())
        self.setChildElementOptionalLiteral(child_element, "SW-SERVICE-IMPL-POLICY", entry.getSwServiceImplPolicy())
        self.setChildElementOptionalLiteral(child_element, "BSW-ENTRY-KIND", entry.getBswEntryKind())
        self.setChildElementOptionalLiteral(child_element, "ROLE", entry.getRole())
        self.setChildElementOptionalLiteral(child_element, "FUNCTION-PROTOTYPE-EMITTER", entry.getFunctionPrototypeEmitter())
        self.writeBswModuleEntryReturnType(child_element, entry)
        self.writeBswModuleEntryArguments(child_element, entry)

    def setSwcBswRunnableMapping(self, element: ET.SubElement, mapping: SwcBswRunnableMapping):
        child_element = ET.SubElement(element, "SWC-BSW-RUNNABLE-MAPPING")
        self.setChildElementOptionalRefType(child_element, "BSW-ENTITY-REF", mapping.getBswEntityRef())
        self.setChildElementOptionalRefType(child_element, "SWC-RUNNABLE-REF", mapping.getSwcRunnableRef())

    def writeSwcBswRunnableMappings(self, element: ET.Element, parent: SwcBswMapping):
        runnable_mappings = parent.getRunnableMappings()
        if len(runnable_mappings) > 0:
            child_element = ET.SubElement(element, "RUNNABLE-MAPPINGS")
            for mapping in runnable_mappings:
                if isinstance(mapping, SwcBswRunnableMapping):
                    self.setSwcBswRunnableMapping(child_element, mapping)
                else:
                    self.notImplemented("Unsupported Runnable Mapping <%s>" % type(mapping))

    def writeSwcBswSynchronizedModeGroupPrototype(self, element: ET.Element, mode_group: SwcBswSynchronizedModeGroupPrototype):
        child_element = ET.SubElement(element, "SWC-BSW-SYNCHRONIZED-MODE-GROUP-PROTOTYPE")
        self.setChildElementOptionalRefType(child_element, "BSW-MODE-GROUP-REF", mode_group.getBswModeGroupRef())
        self.setPModeGroupInAtomicSwcInstanceRef(child_element, "SWC-MODE-GROUP-IREF", mode_group.getSwcModeGroupIRef())

    def writeSwcBswSynchronizedModeGroups(self, element: ET.Element, parent: SwcBswMapping):
        mode_groups = parent.getSynchronizedModeGroups()
        if len(mode_groups) > 0:
            child_element = ET.SubElement(element, "SYNCHRONIZED-MODE-GROUPS")
            for mode_group in mode_groups:
                if isinstance(mode_group, SwcBswSynchronizedModeGroupPrototype):
                    self.writeSwcBswSynchronizedModeGroupPrototype(child_element, mode_group)
                else:
                    self.notImplemented("Unsupported Synchronized Mode Group <%s>" % type(mode_group))

    def writeSwcBswSynchronizedTrigger(self, element: ET.Element, trigger: SwcBswSynchronizedTrigger):
        child_element = ET.SubElement(element, "SWC-BSW-SYNCHRONIZED-TRIGGER")
        self.setChildElementOptionalRefType(child_element, "BSW-TRIGGER-REF", trigger.getBswTriggerRef())
        self.writePTriggerInAtomicSwcTypeInstanceRef(child_element, "SWC-TRIGGER-IREF", trigger.getSwcTriggerIRef())

    def writeSwcBswSynchronizedTriggers(self, element: ET.Element, parent: SwcBswMapping):
        triggers = parent.getSynchronizedTriggers()
        if len(triggers) > 0:
            child_element = ET.SubElement(element, "SYNCHRONIZED-TRIGGERS")
            for trigger in triggers:
                if isinstance(trigger, SwcBswSynchronizedTrigger):
                    self.writeSwcBswSynchronizedTrigger(child_element, trigger)
                else:
                    self.notImplemented("Unsupported Synchronized Trigger <%s>" % type(trigger))

    def writeSwcBswMapping(self, element: ET.Element, mapping: SwcBswMapping):
        self.logger.debug("writeBswModuleDescription %s" % mapping.getShortName())
        child_element = ET.SubElement(element, "SWC-BSW-MAPPING")
        self.writeIdentifiable(child_element, mapping)
        self.setChildElementOptionalRefType(child_element, "BSW-BEHAVIOR-REF", mapping.getBswBehaviorRef())
        self.writeSwcBswRunnableMappings(child_element, mapping)
        self.writeSwcBswSynchronizedModeGroups(child_element, mapping)
        self.writeSwcBswSynchronizedTriggers(child_element, mapping)
        self.setChildElementOptionalRefType(child_element, "SWC-BEHAVIOR-REF", mapping.getSwcBehaviorRef())

    def writeEngineeringObject(self, element: ET.Element, engineering_obj: EngineeringObject):
        self.writeARObjectAttributes(element, engineering_obj)
        self.setChildElementOptionalLiteral(element, "SHORT-LABEL", engineering_obj.getShortLabel())
        self.setChildElementOptionalLiteral(element, "CATEGORY", engineering_obj.getCategory())
        revision_labels = engineering_obj.getRevisionLabels()
        if len(revision_labels) > 0:
            revision_labels_element = ET.SubElement(element, "REVISION-LABELS")
            for revision_label in revision_labels:
                self.setChildElementOptionalRevisionLabelString(revision_labels_element, "REVISION-LABEL", revision_label)
        self.setChildElementOptionalLiteral(element, "DOMAIN", engineering_obj.getDomain())

    def writeAutosarEngineeringObject(self, element: ET.Element, obj: AutosarEngineeringObject):
        # self.logger.debug("write ArtifactDescriptor %s", obj.getShortLabel())
        child_element = ET.SubElement(element, "AUTOSAR-ENGINEERING-OBJECT")
        self.writeEngineeringObject(child_element, obj)

    def writeArtifactDescriptor(self, element: ET.Element, code_desc: Code):
        artifact_descs = code_desc.getArtifactDescriptors()
        if len(artifact_descs) > 0:
            child_element = ET.SubElement(element, "ARTIFACT-DESCRIPTORS")
            for artifact_desc in artifact_descs:
                if isinstance(artifact_desc, AutosarEngineeringObject):
                    self.writeAutosarEngineeringObject(child_element, artifact_desc)
                else:
                    self.notImplemented("Unsupported Artifact descriptor <%s>" % type(artifact_desc))

    def writeBswImplementationVendorSpecificModuleDefRefs(self, element: ET.Element, parent: BswImplementation):
        refs = parent.getVendorSpecificModuleDefRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "VENDOR-SPECIFIC-MODULE-DEF-REFS")
            if child_element is not None:
                for ref in refs:
                    self.setChildElementOptionalRefType(child_element, "VENDOR-SPECIFIC-MODULE-DEF-REF", ref)

    def writeBswImplementationPreconfiguredConfigurationRefs(self, element: ET.Element, parent: BswImplementation):
        refs = parent.getPreconfiguredConfigurationRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "PRECONFIGURED-CONFIGURATION-REFS")
            if child_element is not None:
                for ref in refs:
                    self.setChildElementOptionalRefType(child_element, "PRECONFIGURED-CONFIGURATION-REF", ref)

    def writeBswImplementationRecommendedConfigurationRefs(self, element: ET.Element, parent: BswImplementation):
        refs = parent.getRecommendedConfigurationRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "RECOMMENDED-CONFIGURATION-REFS")
            if child_element is not None:
                for ref in refs:
                    self.setChildElementOptionalRefType(child_element, "RECOMMENDED-CONFIGURATION-REF", ref)

    def writeBswImplementation(self, element: ET.Element, impl: BswImplementation):
        self.logger.debug("writeBswModuleDescription %s" % impl.getShortName())
        child_element = ET.SubElement(element, "BSW-IMPLEMENTATION")
        self.writeImplementation(child_element, impl)
        self.setChildElementOptionalLiteral(child_element, "AR-RELEASE-VERSION", impl.getArReleaseVersion())
        self.setChildElementOptionalRefType(child_element, "BEHAVIOR-REF", impl.getBehaviorRef())
        self.setChildElementOptionalLiteral(child_element, "VENDOR-API-INFIX", impl.getVendorApiInfix())
        self.writeBswImplementationPreconfiguredConfigurationRefs(child_element, impl)
        self.writeBswImplementationRecommendedConfigurationRefs(child_element, impl)
        self.writeBswImplementationVendorSpecificModuleDefRefs(child_element, impl)

    def writeAbstractImplementationDataTypeElement(self, element: ET.Element, impl_data_type_element: AbstractImplementationDataTypeElement):
        self.writeARElement(element, impl_data_type_element)

    def writeImplementationDataTypeElementSubElements(self, element: ET.Element, parent: ImplementationDataTypeElement):
        sub_elements = parent.getSubElements()
        if len(sub_elements) > 0:
            child_element = ET.SubElement(element, "SUB-ELEMENTS")
            for sub_element in sub_elements:
                if isinstance(sub_element, ImplementationDataTypeElement):
                    self.writeImplementationDataTypeElement(child_element, sub_element)
                else:
                    self.notImplemented("Unsupported ImplementationDataTypeElement SubElement <%s>" % type(sub_element))

    def writeImplementationDataTypeElement(self, element: ET.Element, impl_data_type_element: ImplementationDataTypeElement):
        self.logger.debug("writeImplementationDataTypeElement %s" % impl_data_type_element.getShortName())
        child_element = ET.SubElement(element, "IMPLEMENTATION-DATA-TYPE-ELEMENT")
        self.writeAbstractImplementationDataTypeElement(child_element, impl_data_type_element)
        self.setChildElementOptionalLiteral(child_element, "ARRAY-SIZE", impl_data_type_element.getArraySize())
        self.setChildElementOptionalLiteral(child_element, "ARRAY-SIZE-HANDLING", impl_data_type_element.getArraySizeHandling())
        self.setChildElementOptionalLiteral(child_element, "ARRAY-SIZE-SEMANTICS", impl_data_type_element.getArraySizeSemantics())
        self.writeImplementationDataTypeElementSubElements(child_element, impl_data_type_element)
        self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", impl_data_type_element.getSwDataDefProps())

    def writeImplementationDataTypeSubElements(self, element: ET.Element, parent: ImplementationDataType):
        sub_elements = parent.getSubElements()
        if len(sub_elements) > 0:
            child_element = ET.SubElement(element, "SUB-ELEMENTS")
            for sub_element in sub_elements:
                if isinstance(sub_element, ImplementationDataTypeElement):
                    self.writeImplementationDataTypeElement(child_element, sub_element)
                else:
                    self.notImplemented("Unsupported ImplementationDataType SubElement <%s>" % type(sub_element))

    def writeImplementationProps(self, element: ET.Element, props: ImplementationProps):
        self.writeReferrable(element, props)
        self.setChildElementOptionalLiteral(element, "SYMBOL", props.getSymbol())

    def writeSymbolProps(self, element: ET.Element, props: SymbolProps):
        if props is not None:
            child_element = ET.SubElement(element, "SYMBOL-PROPS")
            self.writeImplementationProps(child_element, props)

    def writeImplementationDataTypeSymbolProps(self, element: ET.Element, data_type: ImplementationDataType):
        self.writeSymbolProps(element, data_type.getSymbolProps())

    def writeImplementationDataType(self, element: ET.Element, data_type: ImplementationDataType):
        self.logger.debug("writeImplementationDataType %s" % data_type.getShortName())
        child_element = ET.SubElement(element, "IMPLEMENTATION-DATA-TYPE")
        self.writeAutosarDataType(child_element, data_type)
        self.setChildElementOptionalLiteral(child_element, "DYNAMIC-ARRAY-SIZE-PROFILE", data_type.getDynamicArraySizeProfile())
        self.setChildElementOptionalBooleanValue(child_element, "IS-STRUCT-WITH-OPTIONAL-ELEMENT", data_type.getIsStructWithOptionalElement())
        self.writeImplementationDataTypeSymbolProps(child_element, data_type)
        self.writeImplementationDataTypeSubElements(child_element, data_type)
        self.setChildElementOptionalLiteral(child_element, "TYPE-EMITTER", data_type.getTypeEmitter())

    def writeArgumentDataPrototype(self, element: ET.Element, prototype: ArgumentDataPrototype):
        child_element = ET.SubElement(element, "ARGUMENT-DATA-PROTOTYPE")
        self.writeAutosarDataPrototype(child_element, prototype)
        self.setChildElementOptionalLiteral(child_element, "DIRECTION", prototype.getDirection())
        self.setChildElementOptionalLiteral(child_element, "SERVER-ARGUMENT-IMPL-POLICY", prototype.getServerArgumentImplPolicy())

    def writeClientServerOperationArguments(self, element: ET.Element, parent: ClientServerOperation):
        arguments = parent.getArguments()
        if len(arguments) > 0:
            child_element = ET.SubElement(element, "ARGUMENTS")
            for argument in arguments:
                if isinstance(argument, ArgumentDataPrototype):
                    self.writeArgumentDataPrototype(child_element, argument)
                else:
                    self.notImplemented("Unsupported Argument <%s>" % type(argument))

    def writeClientServerOperationPossibleErrorRefs(self, element: ET.Element, parent: ClientServerOperation):
        error_refs = parent.getPossibleErrorRefs()
        if len(error_refs) > 0:
            child_element = ET.SubElement(element, "POSSIBLE-ERROR-REFS")
            for error_ref in error_refs:
                self.setChildElementOptionalRefType(child_element, "POSSIBLE-ERROR-REF", error_ref)

    def writeClientServerOperation(self, element: ET.Element, operation: ClientServerOperation):
        self.logger.debug("writeClientServerOperation %s" % operation.getShortName())
        child_element = ET.SubElement(element, "CLIENT-SERVER-OPERATION")
        self.writeIdentifiable(child_element, operation)
        self.writeClientServerOperationArguments(child_element, operation)
        self.setChildElementOptionalBooleanValue(child_element, "DIAG-ARG-INTEGRITY", operation.getDiagArgIntegrity())
        self.writeClientServerOperationPossibleErrorRefs(child_element, operation)

    def writeClientServerInterfaceOperations(self, element: ET.Element, parent: ClientServerInterface):
        operations = parent.getOperations()
        if len(operations) > 0:
            operations_tag = ET.SubElement(element, "OPERATIONS")
            for operation in operations:
                if isinstance(operation, ClientServerOperation):
                    self.writeClientServerOperation(operations_tag, operation)
                else:
                    self.notImplemented("Unsupported Operation <%s>" % type(operation))

    def writeApplicationError(self, element: ET.Element, error: ApplicationError):
        self.logger.debug("writeApplicationError %s" % error.getShortName())
        child_element = ET.SubElement(element, "APPLICATION-ERROR")
        self.writeIdentifiable(child_element, error)
        self.setChildElementOptionalIntegerValue(child_element, "ERROR-CODE", error.getErrorCode())

    def writePossibleErrors(self, element: ET.Element, parent: ClientServerInterface):
        errors = parent.getPossibleErrors()
        if len(errors) > 0:
            errors_tag = ET.SubElement(element, "POSSIBLE-ERRORS")
            for error in errors:
                if isinstance(error, ApplicationError):
                    self.writeApplicationError(errors_tag, error)
                else:
                    self.notImplemented("Unsupported PossibleError %s" % type(error))

    def writePortInterface(self, element: ET.Element, port_interface: PortInterface):
        self.writeIdentifiable(element, port_interface)
        self.setChildElementOptionalBooleanValue(element, "IS-SERVICE", port_interface.isService)
        self.setChildElementOptionalLiteral(element, "SERVICE-KIND", port_interface.serviceKind)

    def writeDataInterface(self, element: ET.Element, interface: DataInterface):
        self.writePortInterface(element, interface)

    def writeParameterInterface(self, element: ET.Element, interface: ParameterInterface):
        self.logger.debug("Write ParameterInterface %s" % interface.getShortName())
        child_element = ET.SubElement(element, "PARAMETER-INTERFACE")
        self.writeDataInterface(child_element, interface)
        self.writeSwcInternalBehaviorParameterDataPrototypes(child_element, "PARAMETERS", interface.getParameters())

    def writeNvDataInterfaceNvDatas(self, element: ET.Element, interface: NvDataInterface):
        nv_datas = interface.getNvDatas()
        if len(nv_datas) > 0:
            child_element = ET.SubElement(element, "NV-DATAS")
            for nv_data in nv_datas:
                if isinstance(nv_data, VariableDataPrototype):
                    self.writeVariableDataPrototype(child_element, nv_data)
                else:
                    self.notImplemented("Unsupported NvData <%s>" % type(nv_data))

    def writeNvDataInterface(self, element: ET.Element, interface: NvDataInterface):
        self.logger.debug("Write NvDataInterface %s" % interface.getShortName())
        child_element = ET.SubElement(element, "NV-DATA-INTERFACE")
        self.writeDataInterface(child_element, interface)
        self.writeNvDataInterfaceNvDatas(child_element, interface)

    def writeClientServerInterface(self, element: ET.Element, cs_interface: ClientServerInterface):
        self.logger.debug("writeClientServerInterface %s" % cs_interface.getShortName())
        child_element = ET.SubElement(element, "CLIENT-SERVER-INTERFACE")
        self.writePortInterface(child_element, cs_interface)
        self.writeClientServerInterfaceOperations(child_element, cs_interface)
        self.writePossibleErrors(child_element, cs_interface)

    def writeApplicationSwComponentType(self, element: ET.Element, sw_component: ApplicationSwComponentType):
        self.logger.debug("writeApplicationSwComponentType %s" % sw_component.getShortName())
        child_element = ET.SubElement(element, "APPLICATION-SW-COMPONENT-TYPE")
        self.writeAtomicSwComponentType(child_element, sw_component)

    def writeEcuAbstractionSwComponentType(self, element: ET.Element, sw_component: EcuAbstractionSwComponentType):
        self.logger.debug("writeEcuAbstractionSwComponentType %s" % sw_component.getShortName())
        child_element = ET.SubElement(element, "ECU-ABSTRACTION-SW-COMPONENT-TYPE")
        self.writeAtomicSwComponentType(child_element, sw_component)
        self.writeHardwareElementRefs(child_element, sw_component.getHardwareElementRefs())

    def setApplicationArrayElement(self, element: ET.Element, array_element: ApplicationArrayElement):
        if array_element is not None:
            child_element = ET.SubElement(element, "ELEMENT")
            self.writeApplicationCompositeElementDataPrototype(child_element, array_element)
            self.setChildElementOptionalLiteral(child_element, "ARRAY-SIZE-HANDLING", array_element.getArraySizeHandling())
            self.setChildElementOptionalLiteral(child_element, "ARRAY-SIZE-SEMANTICS", array_element.getArraySizeSemantics())
            self.setChildElementOptionalRefType(child_element, "INDEX-DATA-TYPE-REF", array_element.getIndexDataTypeRef())
            self.setChildElementOptionalNumericalValue(child_element, "MAX-NUMBER-OF-ELEMENTS", array_element.getMaxNumberOfElements())

    def writeApplicationArrayDataType(self, element: ET.Element, data_type: ApplicationArrayDataType):
        self.logger.debug("writeApplicationArrayDataType %s" % data_type.getShortName())
        child_element = ET.SubElement(element, "APPLICATION-ARRAY-DATA-TYPE")
        self.setApplicationCompositeDataType(child_element, data_type)
        self.setChildElementOptionalLiteral(child_element, "DYNAMIC-ARRAY-SIZE-PROFILE", data_type.getDynamicArraySizeProfile())
        self.setApplicationArrayElement(child_element, data_type.getApplicationArrayElement())

    def setSwRecordLayoutV(self, element: ET.Element, key: str, layout_v: SwRecordLayoutV):
        if layout_v is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", layout_v.getShortLabel())
            self.setChildElementOptionalRefType(child_element, "BASE-TYPE-REF", layout_v.getBaseTypeRef())
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-AXIS", layout_v.getSwRecordLayoutVAxis())
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-PROP", layout_v.getSwRecordLayoutVProp())
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-V-INDEX", layout_v.getSwRecordLayoutVIndex())

    def writeSwRecordLayoutGroupSwRecordLayoutGroupContentType(self, element: ET.Element, group: SwRecordLayoutGroup):
        content = group.getSwRecordLayoutGroupContentType()
        self.setSwRecordLayoutGroup(element, "SW-RECORD-LAYOUT-GROUP", content.getSwRecordLayoutGroup())
        self.setSwRecordLayoutV(element, "SW-RECORD-LAYOUT-V", content.getSwRecordLayoutV())

    def setSwRecordLayoutGroup(self, element: ET.Element, key: str, group: SwRecordLayoutGroup):
        if group is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", group.getShortLabel())
            self.setChildElementOptionalLiteral(child_element, "CATEGORY", group.getCategory())
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-AXIS", group.getSwRecordLayoutGroupAxis())
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-INDEX", group.getSwRecordLayoutGroupIndex())
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-FROM", group.getSwRecordLayoutGroupFrom())
            self.setChildElementOptionalLiteral(child_element, "SW-RECORD-LAYOUT-GROUP-TO", group.getSwRecordLayoutGroupTo())
            self.setChildElementOptionalIntegerValue(child_element, "SW-RECORD-LAYOUT-GROUP-STEP", group.getSwRecordLayoutGroupStep())
            self.writeSwRecordLayoutGroupSwRecordLayoutGroupContentType(child_element, group)

    def writeSwRecordLayout(self, element: ET.Element, layout: SwRecordLayout):
        self.logger.debug("writeSwRecordLayout %s" % layout.getShortName())
        child_element = ET.SubElement(element, "SW-RECORD-LAYOUT")
        self.writeIdentifiable(child_element, layout)
        self.setSwRecordLayoutGroup(child_element, "SW-RECORD-LAYOUT-GROUP", layout.getSwRecordLayoutGroup())

    def writeSwAddrMethod(self, element: ET.Element, method: SwAddrMethod):
        self.logger.debug("writeSwAddrMethod %s" % method.getShortName())
        child_element = ET.SubElement(element, "SW-ADDR-METHOD")
        self.writeIdentifiable(child_element, method)
        self.setChildElementOptionalLiteral(child_element, "MEMORY-ALLOCATION-KEYWORD-POLICY", method.getMemoryAllocationKeywordPolicy())
        options = method.getOptions()
        if len(options) > 0:
            options_tag = ET.SubElement(child_element, "OPTIONS")
            for option in options:
                self.setChildElementOptionalLiteral(options_tag, "OPTION", option)
        self.setChildElementOptionalLiteral(child_element, "SECTION-INITIALIZATION-POLICY", method.getSectionInitializationPolicy())
        self.setChildElementOptionalLiteral(child_element, "SECTION-TYPE", method.getSectionType())

    def writeTriggerInterface(self, element: ET.Element, trigger_if: TriggerInterface):
        self.logger.debug("writeTriggerInterface %s" % trigger_if.getShortName())
        # child_element = ET.SubElement(element, "TRIGGER-INTERFACE")
        # self.writePortInterface()

    def writeServiceSwComponentType(self, element: ET.Element, sw_component: ServiceSwComponentType):
        self.logger.debug("writeServiceSwComponentType %s" % sw_component.getShortName())
        child_element = ET.SubElement(element, "SERVICE-SW-COMPONENT-TYPE")
        self.writeAtomicSwComponentType(child_element, sw_component)

    def writeSensorActuatorSwComponentType(self, element: ET.Element, sw_component: SensorActuatorSwComponentType):
        self.logger.debug("writeSensorActuatorSwComponentType %s" % sw_component.getShortName())
        child_element = ET.SubElement(element, "SENSOR-ACTUATOR-SW-COMPONENT-TYPE")
        self.writeAtomicSwComponentType(child_element, sw_component)
        self.setChildElementOptionalRefType(child_element, "SENSOR-ACTUATOR-REF", sw_component.getSensorActuatorRef())

    def writeServiceProxySwComponentType(self, element: ET.Element, sw_component: ServiceProxySwComponentType):
        self.logger.debug("writeServiceProxySwComponentType %s" % sw_component.getShortName())
        child_element = ET.SubElement(element, "SERVICE-PROXY-SW-COMPONENT-TYPE")
        self.writeAtomicSwComponentType(child_element, sw_component)

    def writeNvBlockSwComponentType(self, element: ET.Element, sw_component: NvBlockSwComponentType):
        self.logger.debug("writeNvBlockSwComponentType %s" % sw_component.getShortName())
        child_element = ET.SubElement(element, "NV-BLOCK-SW-COMPONENT-TYPE")
        self.writeAtomicSwComponentType(child_element, sw_component)
        bulk_descriptors = sw_component.getBulkNvDataDescriptors()
        if len(bulk_descriptors) > 0:
            descriptors_tag = ET.SubElement(child_element, "BULK-NV-DATA-DESCRIPTORS")
            for descriptor in bulk_descriptors:
                self.writeBulkNvDataDescriptor(descriptors_tag, descriptor)
        nv_descriptors = sw_component.getNvBlockDescriptors()
        if len(nv_descriptors) > 0:
            descriptors_tag = ET.SubElement(child_element, "NV-BLOCK-DESCRIPTORS")
            for descriptor in nv_descriptors:
                self.writeNvBlockDescriptor(descriptors_tag, descriptor)

    def writeDataTypeMaps(self, element: ET.Element, parent: DataTypeMappingSet):
        maps = parent.getDataTypeMaps()
        if len(maps) > 0:
            maps_tag = ET.SubElement(element, "DATA-TYPE-MAPS")
            for map in maps:
                child_element = ET.SubElement(maps_tag, "DATA-TYPE-MAP")
                self.writeARObjectAttributes(child_element, map)
                self.setChildElementOptionalRefType(child_element, "APPLICATION-DATA-TYPE-REF", map.getApplicationDataTypeRef())
                self.setChildElementOptionalRefType(child_element, "IMPLEMENTATION-DATA-TYPE-REF", map.getImplementationDataTypeRef())

    def writeModeRequestTypeMaps(self, element: ET.Element, parent: DataTypeMappingSet):
        maps = parent.getModeRequestTypeMaps()
        if len(maps) > 0:
            maps_tag = ET.SubElement(element, "MODE-REQUEST-TYPE-MAPS")
            for map in maps:
                child_element = ET.SubElement(maps_tag, "MODE-REQUEST-TYPE-MAP")
                self.writeARObjectAttributes(child_element, map)
                self.setChildElementOptionalRefType(child_element, "IMPLEMENTATION-DATA-TYPE-REF", map.getImplementationDataTypeRef())
                self.setChildElementOptionalRefType(child_element, "MODE-GROUP-REF", map.getModeGroupRef())

    def writeDataTypeMappingSet(self, element: ET.Element, mapping_set: DataTypeMappingSet):
        self.logger.debug("writeDataTypeMappingSet %s" % mapping_set.getShortName())
        child_element = ET.SubElement(element, "DATA-TYPE-MAPPING-SET")
        self.writeIdentifiable(child_element, mapping_set)
        self.writeDataTypeMaps(child_element, mapping_set)
        self.writeModeRequestTypeMaps(child_element, mapping_set)

    def setModeDeclaration(self, element: ET.Element, mode_declaration: ModeDeclaration):
        child_element = ET.SubElement(element, "MODE-DECLARATION")
        self.writeIdentifiable(child_element, mode_declaration)
        self.setChildElementOptionalPositiveInteger(child_element, "VALUE", mode_declaration.getValue())

    def writeModeDeclarationGroupModeDeclaration(self, element: ET.Element, parent: ModeDeclarationGroup):
        mode_declarations = parent.getModeDeclarations()
        if len(mode_declarations) > 0:
            child_element = ET.SubElement(element, "MODE-DECLARATIONS")
            for mode_declaration in mode_declarations:
                self.setModeDeclaration(child_element, mode_declaration)

    def writeModeErrorBehavior(self, element: ET.Element, key: str, behavior: ModeErrorBehavior):
        if behavior is None:
            return element
        child_element = ET.SubElement(element, key)
        self.setChildElementOptionalRefType(child_element, "DEFAULT-MODE-REF", behavior.getDefaultModeRef())
        self.setChildElementOptionalLiteral(child_element, "ERROR-REACTION-POLICY", behavior.getErrorReactionPolicy())
        return child_element

    def writeModeDeclarationGroupModeTransition(self, element: ET.Element, parent: ModeDeclarationGroup):
        mode_transitions = parent.getModeTransitions()
        if len(mode_transitions) > 0:
            child_element = ET.SubElement(element, "MODE-TRANSITIONS")
            for mode_transition in mode_transitions:
                transition_el = ET.SubElement(child_element, "MODE-TRANSITION")
                self.writeIdentifiable(transition_el, mode_transition)
                self.setChildElementOptionalRefType(transition_el, "ENTERED-MODE-REF", mode_transition.getEnteredModeRef())
                self.setChildElementOptionalRefType(transition_el, "EXITED-MODE-REF", mode_transition.getExitedModeRef())

    def writeModeDeclarationGroup(self, element: ET.Element, group: ModeDeclarationGroup):
        self.logger.debug("writeModeDeclarationGroup %s" % group.getShortName())
        child_element = ET.SubElement(element, "MODE-DECLARATION-GROUP")
        self.writeIdentifiable(child_element, group)
        self.setChildElementOptionalRefType(child_element, "INITIAL-MODE-REF", group.initialModeRef)
        self.writeModeDeclarationGroupModeDeclaration(child_element, group)
        self.writeModeErrorBehavior(child_element, "MODE-MANAGER-ERROR-BEHAVIOR", group.getModeManagerErrorBehavior())
        self.writeModeDeclarationGroupModeTransition(child_element, group)
        self.writeModeErrorBehavior(child_element, "MODE-USER-ERROR-BEHAVIOR", group.getModeUserErrorBehavior())
        self.setChildElementOptionalPositiveInteger(child_element, "ON-TRANSITION-VALUE", group.getOnTransitionValue())

    def writeModeSwitchInterfaceModeGroup(self, element: ET.Element, parent: ModeSwitchInterface):
        mode_group = parent.getModeGroup()
        if mode_group is not None:
            child_element = ET.SubElement(element, "MODE-GROUP")
            self.writeIdentifiable(child_element, mode_group)
            self.setChildElementOptionalRefType(child_element, "TYPE-TREF", mode_group.getTypeTRef())
            self.setChildElementOptionalLiteral(child_element, "SW-CALIBRATION-ACCESS", mode_group.getSwCalibrationAccess())

    def writeModeSwitchInterface(self, element: ET.Element, mode_interface: ModeSwitchInterface):
        self.logger.debug("writeModeSwitchInterface %s" % mode_interface.getShortName())
        child_element = ET.SubElement(element, "MODE-SWITCH-INTERFACE")
        self.writePortInterface(child_element, mode_interface)
        self.writeModeSwitchInterfaceModeGroup(child_element, mode_interface)

    def writeExecutionOrderConstraintOrderedElement(self, element: ET.Element, constraint: ExecutionOrderConstraint):
        order_elements = constraint.getOrderedElements()
        if len(order_elements) > 0:
            child_element = ET.SubElement(element, "ORDERED-ELEMENTS")
            for order_element in order_elements:
                if isinstance(order_element, EOCExecutableEntityRef):
                    self.writeEOCExecutableEntityRef(child_element, order_element)
                elif isinstance(order_element, EOCEventRef):
                    self.writeEOCEventRef(child_element, order_element)
                elif isinstance(order_element, EOCExecutableEntityRefGroup):
                    self.writeEOCExecutableEntityRefGroup(child_element, order_element)
                else:
                    self.notImplemented("Unsupported order element <%s>" % type(order_element))

    def writeExecutionOrderConstraint(self, element: ET.Element, constraint: ExecutionOrderConstraint):
        self.logger.debug("writeExecutionOrderConstraint %s" % constraint.getShortName())
        child_element = ET.SubElement(element, "EXECUTION-ORDER-CONSTRAINT")
        self.writeTimingConstraint(child_element, constraint)
        self.setChildElementOptionalRefType(child_element, "BASE-COMPOSITION-REF", constraint.getBaseCompositionRef())
        self.setChildElementOptionalLiteral(child_element, "EXECUTION-ORDER-CONSTRAINT-TYPE", constraint.getExecutionOrderConstraintType())
        self.setChildElementOptionalBooleanValue(child_element, "IGNORE-ORDER-ALLOWED", constraint.getIgnoreOrderAllowed())
        self.setChildElementOptionalBooleanValue(child_element, "IS-EVENT", constraint.getIsEvent())
        self.writeExecutionOrderConstraintOrderedElement(child_element, constraint)
        self.setChildElementOptionalBooleanValue(child_element, "PERMIT-MULTIPLE-REFERENCES-TO-EE", constraint.getPermitMultipleReferencesToEE())

    def writeTimingConstraintItem(self, parent_element: ET.Element, constraint):
        if isinstance(constraint, ExecutionOrderConstraint):
            self.writeExecutionOrderConstraint(parent_element, constraint)
            return
        tag_map = (
            (AgeConstraint, "AGE-CONSTRAINT", self.writeAgeConstraint),
            (ArbitraryEventTriggering, "ARBITRARY-EVENT-TRIGGERING", self.writeArbitraryEventTriggering),
            (BurstPatternEventTriggering, "BURST-PATTERN-EVENT-TRIGGERING", self.writeBurstPatternEventTriggering),
            (ConcretePatternEventTriggering, "CONCRETE-PATTERN-EVENT-TRIGGERING", self.writeConcretePatternEventTriggering),
            (ExecutionTimeConstraint, "EXECUTION-TIME-CONSTRAINT", self.writeExecutionTimeConstraint),
            (LatencyTimingConstraint, "LATENCY-TIMING-CONSTRAINT", self.writeLatencyTimingConstraint),
            (OffsetTimingConstraint, "OFFSET-TIMING-CONSTRAINT", self.writeOffsetTimingConstraint),
            (PeriodicEventTriggering, "PERIODIC-EVENT-TRIGGERING", self.writePeriodicEventTriggering),
            (SporadicEventTriggering, "SPORADIC-EVENT-TRIGGERING", self.writeSporadicEventTriggering),
            (SynchronizationPointConstraint, "SYNCHRONIZATION-POINT-CONSTRAINT", self.writeSynchronizationPointConstraint),
            (SynchronizationTimingConstraint, "SYNCHRONIZATION-TIMING-CONSTRAINT", self.writeSynchronizationTimingConstraint),
        )
        for cls, tag, writer_method in tag_map:
            if isinstance(constraint, cls):
                child_element = ET.SubElement(parent_element, tag)
                writer_method(child_element, constraint)
                return
        self.notImplemented("Unsupported timing requirement <%s>" % type(constraint).__name__)

    def writeTimingClockItem(self, parent_element: ET.Element, clock):
        tag_map = ((TDLETZoneClock, "TDLET-ZONE-CLOCK", self.writeTDLETZoneClock),)
        for cls, tag, writer_method in tag_map:
            if isinstance(clock, cls):
                child_element = ET.SubElement(parent_element, tag)
                writer_method(child_element, clock)
                return
        self.notImplemented("Unsupported timing clock <%s>" % type(clock).__name__)

    def writeTimingExtension(self, element: ET.Element, extension: TimingExtension):
        clocks = extension.getTimingClocks()
        if len(clocks) > 0:
            clocks_tag = ET.SubElement(element, "TIMING-CLOCKS")
            for clock in clocks:
                self.writeTimingClockItem(clocks_tag, clock)
        sync_accuracies = extension.getTimingClockSyncAccuracies()
        if len(sync_accuracies) > 0:
            sync_accuracies_tag = ET.SubElement(element, "TIMING-CLOCK-SYNC-ACCURACYS")
            for sync_accuracy in sync_accuracies:
                sync_accuracy_tag = ET.SubElement(sync_accuracies_tag, "TIMING-CLOCK-SYNC-ACCURACY")
                self.writeTimingClockSyncAccuracy(sync_accuracy_tag, sync_accuracy)
        conditions = extension.getTimingConditions()
        if len(conditions) > 0:
            conditions_tag = ET.SubElement(element, "TIMING-CONDITIONS")
            for condition in conditions:
                condition_tag = ET.SubElement(conditions_tag, "TIMING-CONDITION")
                self.writeTimingCondition(condition_tag, condition)
        guarantees = extension.getTimingGuarantees()
        if len(guarantees) > 0:
            guarantees_tag = ET.SubElement(element, "TIMING-GUARANTEES")
            for guarantee in guarantees:
                self.writeTimingConstraintItem(guarantees_tag, guarantee)
        requirements = extension.getTimingRequirements()
        if len(requirements) > 0:
            requirements_tag = ET.SubElement(element, "TIMING-REQUIREMENTS")
            for requirement in requirements:
                self.writeTimingConstraintItem(requirements_tag, requirement)
        resource = extension.getTimingResource()
        if resource is not None:
            resource_tag = ET.SubElement(element, "TIMING-RESOURCE")
            self.writeTimingExtensionResource(resource_tag, resource)
        descriptions = extension.getTimingDescriptions()
        if len(descriptions) > 0:
            descriptions_tag = ET.SubElement(element, "TIMING-DESCRIPTIONS")
            for description in descriptions:
                if isinstance(description, TDEventVfbReference):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-VFB-REFERENCE")
                    self.writeTDEventVfbReference(description_tag, description)
                elif isinstance(description, TDEventVariableDataPrototype):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-VARIABLE-DATA-PROTOTYPE")
                    self.writeTDEventVariableDataPrototype(description_tag, description)
                elif isinstance(description, TDEventOperation):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-OPERATION")
                    self.writeTDEventOperation(description_tag, description)
                elif isinstance(description, TDEventModeDeclaration):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-MODE-DECLARATION")
                    self.writeTDEventModeDeclaration(description_tag, description)
                elif isinstance(description, TDEventTrigger):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-TRIGGER")
                    self.writeTDEventTrigger(description_tag, description)
                elif isinstance(description, TDEventSwcInternalBehavior):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-SWC-INTERNAL-BEHAVIOR")
                    self.writeTDEventSwcInternalBehavior(description_tag, description)
                elif isinstance(description, TDEventSwcInternalBehaviorReference):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-SWC-INTERNAL-BEHAVIOR-REFERENCE")
                    self.writeTDEventSwcInternalBehaviorReference(description_tag, description)
                elif isinstance(description, TDEventBswInternalBehavior):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-BSW-INTERNAL-BEHAVIOR")
                    self.writeTDEventBswInternalBehavior(description_tag, description)
                elif isinstance(description, TDEventBswModule):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-BSW-MODULE")
                    self.writeTDEventBswModule(description_tag, description)
                elif isinstance(description, TDEventBswModeDeclaration):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-BSW-MODE-DECLARATION")
                    self.writeTDEventBswModeDeclaration(description_tag, description)
                elif isinstance(description, TDEventComplex):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-COMPLEX")
                    self.writeTDEventComplex(description_tag, description)
                elif isinstance(description, TDEventISignal):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-I-SIGNAL")
                    self.writeTDEventISignal(description_tag, description)
                elif isinstance(description, TDEventIPdu):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-I-PDU")
                    self.writeTDEventIPdu(description_tag, description)
                elif isinstance(description, TDEventFrame):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-FRAME")
                    self.writeTDEventFrame(description_tag, description)
                elif isinstance(description, TDEventFrameEthernet):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-FRAME-ETHERNET")
                    self.writeTDEventFrameEthernet(description_tag, description)
                elif isinstance(description, TDEventFrClusterCycleStart):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-FR-CLUSTER-CYCLE-START")
                    self.writeTDEventFrClusterCycleStart(description_tag, description)
                elif isinstance(description, TDEventTTCanCycleStart):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-TT-CAN-CYCLE-START")
                    self.writeTDEventTTCanCycleStart(description_tag, description)
                elif isinstance(description, TDEventSLLETPort):
                    description_tag = ET.SubElement(descriptions_tag, "TD-EVENT-SLLET-PORT")
                    self.writeTDEventSLLETPort(description_tag, description)

    def writeSwcTiming(self, element: ET.Element, timing: SwcTiming):
        self.logger.debug("writeSWcTiming %s" % timing.getShortName())
        child_element = ET.SubElement(element, "SWC-TIMING")
        self.writeIdentifiable(child_element, timing)
        self.writeTimingExtension(child_element, timing)
        self.setChildElementOptionalRefType(child_element, "BEHAVIOR-REF", timing.getBehaviorRef())

    def writePduToFrameMappings(self, element: ET.Element, parent: Frame):
        mappings = parent.getPduToFrameMappings()
        if len(mappings) > 0:
            mappings_tags = ET.SubElement(element, "PDU-TO-FRAME-MAPPINGS")
            for mapping in mappings:
                child_element = ET.SubElement(mappings_tags, "PDU-TO-FRAME-MAPPING")
                self.writeIdentifiable(child_element, mapping)
                self.setChildElementOptionalLiteral(child_element, "PACKING-BYTE-ORDER", mapping.getPackingByteOrder())
                self.setChildElementOptionalRefType(child_element, "PDU-REF", mapping.getPduRef())
                self.setChildElementOptionalIntegerValue(child_element, "START-POSITION", mapping.getStartPosition())
                self.setChildElementOptionalIntegerValue(child_element, "UPDATE-INDICATION-BIT-POSITION", mapping.getUpdateIndicationBitPosition())

    def writeFrame(self, element: ET.Element, frame: Frame):
        self.writeIdentifiable(element, frame)
        self.setChildElementOptionalNumericalValue(element, "FRAME-LENGTH", frame.frameLength)
        self.writePduToFrameMappings(element, frame)

    def writeLinUnconditionalFrame(self, element: ET.Element, frame: LinUnconditionalFrame):
        self.logger.debug("LinUnconditionalFrame %s" % frame.getShortName())
        child_element = ET.SubElement(element, "LIN-UNCONDITIONAL-FRAME")
        self.writeFrame(child_element, frame)

    def writeNmNode(self, element: ET.Element, nm_node: NmNode):
        self.writeIdentifiable(element, nm_node)
        self.setChildElementOptionalRefType(element, "CONTROLLER-REF", nm_node.getControllerRef())
        self.setChildElementOptionalPositiveInteger(element, "NM-COORD-CLUSTER", nm_node.getNmCoordCluster())
        self.setChildElementOptionalLiteral(element, "NM-COORDINATOR-ROLE", nm_node.getNmCoordinatorRole())
        self.setChildElementOptionalRefType(element, "NM-IF-ECU-REF", nm_node.getNmIfEcuRef())
        self.setChildElementOptionalIntegerValue(element, "NM-NODE-ID", nm_node.getNmNodeId())
        self.setChildElementOptionalBooleanValue(element, "NM-PASSIVE-MODE-ENABLED", nm_node.getNmPassiveModeEnabled())

        refs = nm_node.getRxNmPduRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "RX-NM-PDU-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "RX-NM-PDU-REF", ref)

        refs = nm_node.getTxNmPduRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "TX-NM-PDU-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "TX-NM-PDU-REF", ref)

    def writeCanNmNode(self, element: ET.Element, nm_node: CanNmNode):
        self.logger.debug("write CanNmNode %s" % nm_node.getShortName())
        child_element = ET.SubElement(element, "CAN-NM-NODE")
        self.writeNmNode(child_element, nm_node)
        self.setChildElementOptionalBooleanValue(child_element, "NM-CAR-WAKE-UP-RX-ENABLED", nm_node.getNmCarWakeUpRxEnabled())
        self.setChildElementOptionalFloatValue(child_element, "NM-MSG-CYCLE-OFFSET", nm_node.getNmMsgCycleOffset())
        self.setChildElementOptionalFloatValue(child_element, "NM-MSG-REDUCED-TIME", nm_node.getNmMsgReducedTime())
        self.setRxIdentifierRange(child_element, "NM-RANGE-CONFIG", nm_node.getNmRangeConfig())

    def writeUdpNmNode(self, element: ET.Element, nm_node: UdpNmNode):
        self.logger.debug("write UdpNmNode %s" % nm_node.getShortName())
        child_element = ET.SubElement(element, "UDP-NM-NODE")
        self.writeNmNode(child_element, nm_node)
        self.setChildElementOptionalTimeValue(child_element, "NM-MSG-CYCLE-OFFSET", nm_node.getNmMsgCycleOffset())

    def writeJ1939NmNode(self, element: ET.Element, nm_node: J1939NmNode):
        self.logger.debug("write J1939NmNode %s" % nm_node.getShortName())
        child_element = ET.SubElement(element, "J-1939-NM-NODE")
        self.writeNmNode(child_element, nm_node)
        self.setChildElementOptionalLiteral(child_element, "ADDRESS-CONFIGURATION-CAPABILITY", nm_node.getAddressConfigurationCapability())
        self.setJ1939NodeName(child_element, "NODE-NAME", nm_node.getNodeName())

    def writeNmClusterNmNodes(self, element: ET.Element, parent: NmCluster):
        nodes = parent.getNmNodes()
        if len(nodes) > 0:
            child_element = ET.SubElement(element, "NM-NODES")
            for node in nodes:
                if isinstance(node, CanNmNode):
                    self.writeCanNmNode(child_element, node)
                elif isinstance(node, UdpNmNode):
                    self.writeUdpNmNode(child_element, node)
                elif isinstance(node, J1939NmNode):
                    self.writeJ1939NmNode(child_element, node)
                else:
                    self.notImplemented("Unsupported Nm Node <%s>" % type(node))

    def writeCanNmClusterCoupling(self, element: ET.Element, coupling: CanNmClusterCoupling):
        child_element = ET.SubElement(element, "CAN-NM-CLUSTER-COUPLING")
        refs = coupling.getCoupledClusterRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(child_element, "COUPLED-CLUSTER-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "COUPLED-CLUSTER-REF", ref)
        self.setChildElementOptionalBooleanValue(child_element, "NM-BUSLOAD-REDUCTION-ENABLED", coupling.getNmBusloadReductionEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-IMMEDIATE-RESTART-ENABLED", coupling.getNmImmediateRestartEnabled())

    def writeUdpNmClusterCoupling(self, element: ET.Element, coupling: UdpNmClusterCoupling):
        child_element = ET.SubElement(element, "UDP-NM-CLUSTER-COUPLING")
        refs = coupling.getCoupledClusterRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(child_element, "COUPLED-CLUSTER-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "COUPLED-CLUSTER-REF", ref)
        self.setChildElementOptionalBooleanValue(child_element, "NM-IMMEDIATE-RESTART-ENABLED", coupling.getNmImmediateRestartEnabled())

    def writeNmConfigNmClusterCouplings(self, element: ET.Element, config: NmConfig):
        self.logger.debug("Write NmConfigNmClusterCouplings <%s>" % config.getShortName())
        couplings = config.getNmClusterCouplings()
        if len(couplings) > 0:
            child_element = ET.SubElement(element, "NM-CLUSTER-COUPLINGS")
            for coupling in couplings:
                if isinstance(coupling, CanNmClusterCoupling):
                    self.writeCanNmClusterCoupling(child_element, coupling)
                elif isinstance(coupling, UdpNmClusterCoupling):
                    self.writeUdpNmClusterCoupling(child_element, coupling)
                else:
                    self.notImplemented("Unsupported Nm Cluster Coupling <%s>" % type(coupling))

    def writeNmCluster(self, element: ET.Element, cluster: NmCluster):
        self.logger.debug("Write NmCluster <%s>" % cluster.getShortName())
        self.writeIdentifiable(element, cluster)
        self.setChildElementOptionalRefType(element, "COMMUNICATION-CLUSTER-REF", cluster.communicationClusterRef)
        self.setChildElementOptionalNumericalValue(element, "NM-CHANNEL-ID", cluster.nmChannelId)
        self.setChildElementOptionalBooleanValue(element, "NM-CHANNEL-SLEEP-MASTER", cluster.nmChannelSleepMaster)
        self.writeNmClusterNmNodes(element, cluster)
        self.setChildElementOptionalBooleanValue(element, "NM-SYNCHRONIZING-NETWORK", cluster.getNmSynchronizingNetwork())

    def writeCanNmCluster(self, element: ET.Element, cluster: CanNmCluster):
        self.logger.debug("Write CanNmCluster <%s>" % cluster.getShortName())
        child_element = ET.SubElement(element, "CAN-NM-CLUSTER")
        self.writeNmCluster(child_element, cluster)

        self.setChildElementOptionalBooleanValue(child_element, "NM-BUSLOAD-REDUCTION-ACTIVE", cluster.getNmBusloadReductionActive())
        self.setChildElementOptionalBooleanValue(child_element, "NM-CAR-WAKE-UP-RX-ENABLED", cluster.getNmCarWakeUpRxEnabled())
        self.setChildElementOptionalNumericalValue(child_element, "NM-CBV-POSITION", cluster.getNmCbvPosition())
        self.setChildElementOptionalBooleanValue(child_element, "NM-CHANNEL-ACTIVE", cluster.getNmChannelActive())
        self.setChildElementOptionalFloatValue(child_element, "NM-IMMEDIATE-NM-CYCLE-TIME", cluster.getNmImmediateNmCycleTime())
        self.setChildElementOptionalNumericalValue(child_element, "NM-IMMEDIATE-NM-TRANSMISSIONS", cluster.getNmImmediateNmTransmissions())
        self.setChildElementOptionalFloatValue(child_element, "NM-MESSAGE-TIMEOUT-TIME", cluster.getNmMessageTimeoutTime())
        self.setChildElementOptionalFloatValue(child_element, "NM-MSG-CYCLE-TIME", cluster.getNmMsgCycleTime())
        self.setChildElementOptionalFloatValue(child_element, "NM-NETWORK-TIMEOUT", cluster.getNmNetworkTimeout())
        self.setChildElementOptionalNumericalValue(child_element, "NM-NID-POSITION", cluster.getNmNidPosition())
        self.setChildElementOptionalFloatValue(child_element, "NM-REMOTE-SLEEP-INDICATION-TIME", cluster.getNmRemoteSleepIndicationTime())
        self.setChildElementOptionalFloatValue(child_element, "NM-REPEAT-MESSAGE-TIME", cluster.getNmRepeatMessageTime())
        self.setChildElementOptionalNumericalValue(child_element, "NM-USER-DATA-LENGTH", cluster.getNmUserDataLength())
        self.setChildElementOptionalFloatValue(child_element, "NM-WAIT-BUS-SLEEP-TIME", cluster.getNmWaitBusSleepTime())

    def writeUdpNmCluster(self, element: ET.Element, cluster: UdpNmCluster):
        self.logger.debug("Write UdpNmCluster <%s>" % cluster.getShortName())
        child_element = ET.SubElement(element, "UDP-NM-CLUSTER")
        self.writeNmCluster(child_element, cluster)
        self.setChildElementOptionalIntegerValue(child_element, "NM-CBV-POSITION", cluster.getNmCbvPosition())
        self.setChildElementOptionalBooleanValue(child_element, "NM-CHANNEL-ACTIVE", cluster.getNmChannelActive())
        self.setChildElementOptionalTimeValue(child_element, "NM-IMMEDIATE-NM-CYCLE-TIME", cluster.getNmImmediateNmCycleTime())
        self.setChildElementOptionalPositiveInteger(child_element, "NM-IMMEDIATE-NM-TRANSMISSIONS", cluster.getNmImmediateNmTransmissions())
        self.setChildElementOptionalTimeValue(child_element, "NM-MESSAGE-TIMEOUT-TIME", cluster.getNmMessageTimeoutTime())
        self.setChildElementOptionalTimeValue(child_element, "NM-MSG-CYCLE-TIME", cluster.getNmMsgCycleTime())
        self.setChildElementOptionalTimeValue(child_element, "NM-NETWORK-TIMEOUT", cluster.getNmNetworkTimeout())
        self.setChildElementOptionalIntegerValue(child_element, "NM-NID-POSITION", cluster.getNmNidPosition())
        self.setChildElementOptionalTimeValue(child_element, "NM-REMOTE-SLEEP-INDICATION-TIME", cluster.getNmRemoteSleepIndicationTime())
        self.setChildElementOptionalTimeValue(child_element, "NM-REPEAT-MESSAGE-TIME", cluster.getNmRepeatMessageTime())
        self.setChildElementOptionalTimeValue(child_element, "NM-WAIT-BUS-SLEEP-TIME", cluster.getNmWaitBusSleepTime())
        self.setChildElementOptionalRefType(child_element, "VLAN-REF", cluster.getVlanRef())

    def writeNmConfigNmClusters(self, element: ET.Element, parent: NmConfig):
        clusters = parent.getNmClusters()
        if len(clusters) > 0:
            child_element = ET.SubElement(element, "NM-CLUSTERS")
            for cluster in clusters:
                if isinstance(cluster, CanNmCluster):
                    self.writeCanNmCluster(child_element, cluster)
                elif isinstance(cluster, UdpNmCluster):
                    self.writeUdpNmCluster(child_element, cluster)
                else:
                    self.notImplemented("Unsupported Nm Cluster <%s>" % type(cluster))

    def writeUdpNmEcu(self, element: ET.Element, ecu: UdpNmEcu):
        if ecu is not None:
            child_element = ET.SubElement(element, "UDP-NM-ECU")
            self.setChildElementOptionalBooleanValue(child_element, "NM-SYNCHRONIZATION-POINT-ENABLED", ecu.getNmSynchronizationPointEnabled())

    def writeCanNmEcu(self, element: ET.Element, ecu: CanNmEcu):
        if ecu is not None:
            ET.SubElement(element, "CAN-NM-ECU")

    def writeBusDependentNmEcus(self, element: ET.Element, nm_ecu: NmEcu):
        dependent_nm_ecus = nm_ecu.getBusDependentNmEcus()
        if len(dependent_nm_ecus) > 0:
            child_element = ET.SubElement(element, "BUS-DEPENDENT-NM-ECUS")
            for dependent_nm_ecu in dependent_nm_ecus:
                if isinstance(dependent_nm_ecu, UdpNmEcu):
                    self.writeUdpNmEcu(child_element, dependent_nm_ecu)
                elif isinstance(dependent_nm_ecu, CanNmEcu):
                    self.writeCanNmEcu(child_element, dependent_nm_ecu)
                else:
                    self.notImplemented("Unsupported BusDependentNmEcu <%s>" % type(dependent_nm_ecu))

    def writeNmEcu(self, element: ET.Element, nm_ecu: NmEcu):
        child_element = ET.SubElement(element, "NM-ECU")
        self.writeIdentifiable(child_element, nm_ecu)
        self.writeBusDependentNmEcus(child_element, nm_ecu)
        self.setChildElementOptionalRefType(child_element, "ECU-INSTANCE-REF", nm_ecu.getEcuInstanceRef())
        self.setChildElementOptionalBooleanValue(child_element, "NM-BUS-SYNCHRONIZATION-ENABLED", nm_ecu.getNmBusSynchronizationEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-COM-CONTROL-ENABLED", nm_ecu.getNmComControlEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-NODE-DETECTION-ENABLED", nm_ecu.getNmNodeDetectionEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-NODE-ID-ENABLED", nm_ecu.getNmNodeIdEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-PDU-RX-INDICATION-ENABLED", nm_ecu.getNmPduRxIndicationEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-REMOTE-SLEEP-IND-ENABLED", nm_ecu.getNmRemoteSleepIndEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-REPEAT-MSG-IND-ENABLED", nm_ecu.getNmRepeatMsgIndEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-STATE-CHANGE-IND-ENABLED", nm_ecu.getNmStateChangeIndEnabled())
        self.setChildElementOptionalBooleanValue(child_element, "NM-USER-DATA-ENABLED", nm_ecu.getNmUserDataEnabled())

    def writeNmConfigNmIfEcus(self, element: ET.Element, nm_config: NmConfig):
        ecus = nm_config.getNmIfEcus()
        if len(ecus) > 0:
            child_element = ET.SubElement(element, "NM-IF-ECUS")
            for ecu in ecus:
                if isinstance(ecu, NmEcu):
                    self.writeNmEcu(child_element, ecu)
                else:
                    self.notImplemented("Unsupported NmIfEcus <%s>" % type(ecu))

    def writeNmConfig(self, element: ET.Element, config: NmConfig):
        self.logger.debug("Write NmConfig <%s>" % config.getShortName())
        child_element = ET.SubElement(element, "NM-CONFIG")
        self.writeIdentifiable(child_element, config)
        self.writeNmConfigNmClusters(child_element, config)
        self.writeNmConfigNmClusterCouplings(child_element, config)
        self.writeNmConfigNmIfEcus(child_element, config)

    def writeISignalToIPduMapping(self, element: ET.Element, mapping: ISignalToIPduMapping):
        if mapping is not None:
            child_element = ET.SubElement(element, "I-SIGNAL-TO-I-PDU-MAPPING")
            self.writeIdentifiable(child_element, mapping)
            self.setChildElementOptionalRefType(child_element, "I-SIGNAL-REF", mapping.getISignalRef())
            self.setChildElementOptionalRefType(child_element, "I-SIGNAL-GROUP-REF", mapping.getISignalGroupRef())
            self.setChildElementOptionalLiteral(child_element, "PACKING-BYTE-ORDER", mapping.getPackingByteOrder())
            self.setChildElementOptionalIntegerValue(child_element, "START-POSITION", mapping.getStartPosition())
            self.setChildElementOptionalLiteral(child_element, "TRANSFER-PROPERTY", mapping.getTransferProperty())
            self.setChildElementOptionalNumericalValue(child_element, "UPDATE-INDICATION-BIT-POSITION", mapping.getUpdateIndicationBitPosition())

    def writeNmPduISignalToIPduMappings(self, element: ET.Element, pdu: NmPdu):
        mappings = pdu.getISignalToIPduMappings()
        if len(mappings) > 0:
            child_element = ET.SubElement(element, "I-SIGNAL-TO-I-PDU-MAPPINGS")
            for mapping in mappings:
                if isinstance(mapping, ISignalToIPduMapping):
                    self.writeISignalToIPduMapping(child_element, mapping)
                else:
                    self.notImplemented("Unsupported ISignalToIPduMapping <%s>" % type(mapping))

    def writeNmPdu(self, element: ET.Element, pdu: NmPdu):
        self.logger.debug("Write NmPdu <%s>" % pdu.getShortName())
        child_element = ET.SubElement(element, "NM-PDU")
        self.writePdu(child_element, pdu)
        self.writeNmPduISignalToIPduMappings(child_element, pdu)
        self.setChildElementOptionalBooleanValue(child_element, "NM-DATA-INFORMATION", pdu.getNmDataInformation())
        self.setChildElementOptionalBooleanValue(child_element, "NM-VOTE-INFORMATION", pdu.getNmVoteInformation())
        self.setChildElementOptionalIntegerValue(child_element, "UNUSED-BIT-PATTERN", pdu.getUnusedBitPattern())

    def writeNPdu(self, element: ET.Element, pdu: NPdu):
        self.logger.debug("Write NPdu <%s>" % pdu.getShortName())
        child_element = ET.SubElement(element, "N-PDU")
        self.writePdu(child_element, pdu)

    def writeDcmIPdu(self, element: ET.Element, pdu: DcmIPdu):
        self.logger.debug("Write DcmIPdu <%s>" % pdu.getShortName())
        child_element = ET.SubElement(element, "DCM-I-PDU")
        self.writeIPdu(child_element, pdu)
        self.setChildElementOptionalLiteral(child_element, "DIAG-PDU-TYPE", pdu.getDiagPduType())

    def setSecureCommunicationProps(self, element: ET.Element, key: str, props: SecureCommunicationProps):
        if props is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalPositiveInteger(child_element, "AUTH-DATA-FRESHNESS-LENGTH", props.getAuthDataFreshnessLength())
            self.setChildElementOptionalPositiveInteger(child_element, "AUTH-DATA-FRESHNESS-START-POSITION", props.getAuthDataFreshnessStartPosition())  # noqa E501
            self.setChildElementOptionalPositiveInteger(child_element, "AUTHENTICATION-BUILD-ATTEMPTS", props.getAuthenticationBuildAttempts())
            self.setChildElementOptionalPositiveInteger(child_element, "AUTHENTICATION-RETRIES", props.getAuthenticationRetries())
            self.setChildElementOptionalPositiveInteger(child_element, "DATA-ID", props.getDataId())
            self.setChildElementOptionalPositiveInteger(child_element, "FRESHNESS-VALUE-ID", props.getFreshnessValueId())
            self.setChildElementOptionalPositiveInteger(child_element, "MESSAGE-LINK-LENGTH", props.getMessageLinkLength())
            self.setChildElementOptionalPositiveInteger(child_element, "MESSAGE-LINK-POSITION", props.getMessageLinkPosition())
            self.setChildElementOptionalPositiveInteger(child_element, "SECONDARY-FRESHNESS-VALUE-ID", props.getSecondaryFreshnessValueId())
            self.setChildElementOptionalPositiveInteger(child_element, "SECURED-AREA-LENGTH", props.getSecuredAreaLength())
            self.setChildElementOptionalPositiveInteger(child_element, "SECURED-AREA-OFFSET", props.getSecuredAreaOffset())

    def writeSecuredIPdu(self, element: ET.Element, i_pdu: SecuredIPdu):
        self.logger.debug("Write SecuredIPdu <%s>" % i_pdu.getShortName())
        child_element = ET.SubElement(element, "SECURED-I-PDU")
        self.writeIPdu(child_element, i_pdu)
        self.setChildElementOptionalRefType(child_element, "AUTHENTICATION-PROPS-REF", i_pdu.getAuthenticationPropsRef())
        self.setChildElementOptionalRefType(child_element, "FRESHNESS-PROPS-REF", i_pdu.getFreshnessPropsRef())
        self.setChildElementOptionalRefType(child_element, "PAYLOAD-REF", i_pdu.getPayloadRef())
        self.setSecureCommunicationProps(child_element, "SECURE-COMMUNICATION-PROPS", i_pdu.getSecureCommunicationProps())
        self.setChildElementOptionalBooleanValue(child_element, "USE-AS-CRYPTOGRAPHIC-I-PDU", i_pdu.getUseAsCryptographicIPdu())

    def writeTpConfig(self, element: ET.Element, config: TpConfig):
        self.writeIdentifiable(element, config)
        self.setChildElementOptionalRefType(element, "COMMUNICATION-CLUSTER-REF", config.getCommunicationClusterRef())

    def writeCanTpAddress(self, element: ET.Element, address: CanTpAddress):
        if address is not None:
            child_element = ET.SubElement(element, "CAN-TP-ADDRESS")
            self.writeIdentifiable(child_element, address)
            self.setChildElementOptionalIntegerValue(child_element, "TP-ADDRESS", address.getTpAddress())
            self.setChildElementOptionalIntegerValue(child_element, "TP-ADDRESS-EXTENSION-VALUE", address.getTpAddressExtensionValue())

    def writeCanTpConfigTpAddresses(self, element: ET.Element, config: CanTpConfig):
        addresses = config.getTpAddresses()
        if len(addresses) > 0:
            child_element = ET.SubElement(element, "TP-ADDRESSS")
            for address in addresses:
                if isinstance(address, CanTpAddress):
                    self.writeCanTpAddress(child_element, address)
                else:
                    self.notImplemented("Unsupported TpAddress <%s>" % type(address))

    def writeCanTpChannel(self, element: ET.Element, channel: CanTpChannel):
        if channel is not None:
            child_element = ET.SubElement(element, "CAN-TP-CHANNEL")
            self.writeIdentifiable(child_element, channel)
            self.setChildElementOptionalPositiveInteger(child_element, "CHANNEL-ID", channel.getChannelId())

    def writeCanTpConfigTpChannels(self, element: ET.Element, config: CanTpConfig):
        channels = config.getTpChannels()
        if len(channels) > 0:
            child_element = ET.SubElement(element, "TP-CHANNELS")
            for channel in channels:
                if isinstance(channel, CanTpChannel):
                    self.writeCanTpChannel(child_element, channel)
                else:
                    self.notImplemented("Unsupported TpChannel <%s>" % type(channel))

    def writeTpConnection(self, element: ET.Element, connection: TpConnection):
        self.writeARObjectAttributes(element, connection)
        ident = connection.getIdent()
        if ident is not None:
            child_element = ET.SubElement(element, "IDENT")
            self.writeReferrable(child_element, ident)

    def writeTpConnectionReceiverRefs(self, element: ET.Element, connection: CanTpConnection):
        refs = connection.getReceiverRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "RECEIVER-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "RECEIVER-REF", ref)

    def writeCanTpConnection(self, element: ET.Element, connection: CanTpConnection):
        if connection is not None:
            child_element = ET.SubElement(element, "CAN-TP-CONNECTION")
            self.writeTpConnection(child_element, connection)
            addressing_format = connection.getAddressingFormat()
            if addressing_format is not None:
                addressing_format_element = ET.SubElement(child_element, "ADDRESSING-FORMAT")
                addressing_format_element.text = addressing_format.getValue()
            self.setChildElementOptionalRefType(child_element, "CAN-TP-CHANNEL-REF", connection.getCanTpChannelRef())
            self.setChildElementOptionalBooleanValue(child_element, "CANCELLATION", connection.getCancellation())
            self.setChildElementOptionalRefType(child_element, "DATA-PDU-REF", connection.getDataPduRef())
            self.setChildElementOptionalRefType(child_element, "FLOW-CONTROL-PDU-REF", connection.getFlowControlPduRef())
            self.setChildElementOptionalIntegerValue(child_element, "MAX-BLOCK-SIZE", connection.getMaxBlockSize())
            self.setChildElementOptionalRefType(child_element, "MULTICAST-REF", connection.getMulticastRef())
            self.setChildElementOptionalBooleanValue(child_element, "PADDING-ACTIVATION", connection.getPaddingActivation())
            self.writeTpConnectionReceiverRefs(child_element, connection)
            self.setChildElementOptionalLiteral(child_element, "TA-TYPE", connection.getTaType())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-BR", connection.getTimeoutBr())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-BS", connection.getTimeoutBs())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-CR", connection.getTimeoutCr())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-CS", connection.getTimeoutCs())
            self.setChildElementOptionalRefType(child_element, "TP-SDU-REF", connection.getTpSduRef())
            self.setChildElementOptionalRefType(child_element, "TRANSMITTER-REF", connection.getTransmitterRef())

    def writeCanTpConfigTpConnections(self, element: ET.Element, config: CanTpConfig):
        connections = config.getTpConnections()
        if len(connections) > 0:
            child_element = ET.SubElement(element, "TP-CONNECTIONS")
            for connection in connections:
                if isinstance(connection, CanTpConnection):
                    self.writeCanTpConnection(child_element, connection)
                else:
                    self.notImplemented("Unsupported TpConnection <%s>" % type(connection))

    def writeCanTpEcu(self, element: ET.Element, tp_ecu: CanTpEcu):
        if tp_ecu is not None:
            child_element = ET.SubElement(element, "CAN-TP-ECU")
            self.setChildElementOptionalTimeValue(child_element, "CYCLE-TIME-MAIN-FUNCTION", tp_ecu.getCycleTimeMainFunction())
            self.setChildElementOptionalRefType(child_element, "ECU-INSTANCE-REF", tp_ecu.getEcuInstanceRef())

    def writeCanTpConfigTpEcus(self, element: ET.Element, config: CanTpConfig):
        tp_ecus = config.getTpEcus()
        if len(tp_ecus) > 0:
            child_element = ET.SubElement(element, "TP-ECUS")
            for tp_ecu in tp_ecus:
                if isinstance(tp_ecu, CanTpEcu):
                    self.writeCanTpEcu(child_element, tp_ecu)
                else:
                    self.notImplemented("Unsupported TpEcu <%s>" % type(tp_ecu))

    def writeCanTpNode(self, element: ET.Element, tp_node: CanTpNode):
        if tp_node is not None:
            child_element = ET.SubElement(element, "CAN-TP-NODE")
            self.writeIdentifiable(child_element, tp_node)
            self.setChildElementOptionalRefType(child_element, "CONNECTOR-REF", tp_node.getConnectorRef())
            self.setChildElementOptionalIntegerValue(child_element, "MAX-FC-WAIT", tp_node.getMaxFcWait())
            self.setChildElementOptionalTimeValue(child_element, "ST-MIN", tp_node.getStMin())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-AR", tp_node.getTimeoutAr())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-AS", tp_node.getTimeoutAs())
            self.setChildElementOptionalRefType(child_element, "TP-ADDRESS-REF", tp_node.getTpAddressRef())

    def writeCanTpConfigTpNodes(self, element: ET.Element, config: CanTpConfig):
        tp_nodes = config.getTpNodes()
        if len(tp_nodes) > 0:
            child_element = ET.SubElement(element, "TP-NODES")
            for tp_node in tp_nodes:
                if isinstance(tp_node, CanTpNode):
                    self.writeCanTpNode(child_element, tp_node)
                else:
                    self.notImplemented("Unsupported TpNode <%s>" % type(tp_node))

    def writeCanTpConfig(self, element: ET.Element, config: CanTpConfig):
        self.logger.debug("Write CanTpConfig <%s>" % config.getShortName())
        child_element = ET.SubElement(element, "CAN-TP-CONFIG")
        self.writeTpConfig(child_element, config)
        self.writeCanTpConfigTpAddresses(child_element, config)
        self.writeCanTpConfigTpChannels(child_element, config)
        self.writeCanTpConfigTpConnections(child_element, config)
        self.writeCanTpConfigTpEcus(child_element, config)
        self.writeCanTpConfigTpNodes(child_element, config)

    def writeTpAddress(self, element: ET.Element, address: TpAddress):
        if address is not None:
            child_element = ET.SubElement(element, "TP-ADDRESS")
            self.writeIdentifiable(child_element, address)
            self.setChildElementOptionalIntegerValue(child_element, "TP-ADDRESS", address.getTpAddress())

    def writeLinTpConfigTpAddresses(self, element: ET.Element, config: CanTpConfig):
        addresses = config.getTpAddresses()
        if len(addresses) > 0:
            child_element = ET.SubElement(element, "TP-ADDRESSS")
            for address in addresses:
                if isinstance(address, TpAddress):
                    self.writeTpAddress(child_element, address)
                else:
                    self.notImplemented("Unsupported TpAddress <%s>" % type(address))

    def writeLinTpConnection(self, element: ET.Element, connection: LinTpConnection):
        if connection is not None:
            child_element = ET.SubElement(element, "LIN-TP-CONNECTION")
            self.writeTpConnection(child_element, connection)
            self.setChildElementOptionalRefType(child_element, "DATA-PDU-REF", connection.getDataPduRef())
            self.setChildElementOptionalRefType(child_element, "FLOW-CONTROL-REF", connection.getFlowControlRef())
            self.setChildElementOptionalRefType(child_element, "LIN-TP-N-SDU-REF", connection.getLinTpNSduRef())
            self.writeTpConnectionReceiverRefs(child_element, connection)
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-AS", connection.getTimeoutAs())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-CR", connection.getTimeoutCr())
            self.setChildElementOptionalTimeValue(child_element, "TIMEOUT-CS", connection.getTimeoutCs())
            self.setChildElementOptionalRefType(child_element, "TRANSMITTER-REF", connection.getTransmitterRef())

    def writeLinTpConfigTpConnections(self, element: ET.Element, config: LinTpConfig):
        connections = config.getTpConnections()
        if len(connections) > 0:
            child_element = ET.SubElement(element, "TP-CONNECTIONS")
            for connection in connections:
                if isinstance(connection, LinTpConnection):
                    self.writeLinTpConnection(child_element, connection)
                else:
                    self.notImplemented("Unsupported TpConnection <%s>" % type(connection))

    def writeLinTpNode(self, element: ET.Element, tp_node: LinTpNode):
        if tp_node is not None:
            child_element = ET.SubElement(element, "LIN-TP-NODE")
            self.writeIdentifiable(child_element, tp_node)
            self.setChildElementOptionalRefType(child_element, "CONNECTOR-REF", tp_node.getConnectorRef())
            self.setChildElementOptionalBooleanValue(child_element, "DROP-NOT-REQUESTED-NAD", tp_node.getDropNotRequestedNad())
            self.setChildElementOptionalIntegerValue(child_element, "MAX-NUMBER-OF-RESP-PENDING-FRAMES", tp_node.getMaxNumberOfRespPendingFrames())
            self.setChildElementOptionalTimeValue(child_element, "P-2-MAX", tp_node.getP2Max())
            self.setChildElementOptionalTimeValue(child_element, "P-2-TIMING", tp_node.getP2Timing())
            self.setChildElementOptionalRefType(child_element, "TP-ADDRESS-REF", tp_node.getTpAddressRef())

    def writeLinTpConfigTpNodes(self, element: ET.Element, config: LinTpConfig):
        tp_nodes = config.getTpNodes()
        if len(tp_nodes) > 0:
            child_element = ET.SubElement(element, "TP-NODES")
            for tp_node in tp_nodes:
                if isinstance(tp_node, LinTpNode):
                    self.writeLinTpNode(child_element, tp_node)
                else:
                    self.notImplemented("Unsupported TpNode <%s>" % type(tp_node))

    def writeLinTpConfig(self, element: ET.Element, config: LinTpConfig):
        self.logger.debug("Write LinTpConfig <%s>" % config.getShortName())
        child_element = ET.SubElement(element, "LIN-TP-CONFIG")
        self.writeTpConfig(child_element, config)
        self.writeLinTpConfigTpAddresses(child_element, config)
        self.writeLinTpConfigTpConnections(child_element, config)
        self.writeLinTpConfigTpNodes(child_element, config)

    def writeFrameTriggering(self, element: ET.Element, triggering: FrameTriggering):
        self.writeIdentifiable(element, triggering)
        ref_list = triggering.getFramePortRefs()
        if len(ref_list) > 0:
            frame_port_refs_tag = ET.SubElement(element, "FRAME-PORT-REFS")
            for ref in ref_list:
                self.setChildElementOptionalRefType(frame_port_refs_tag, "FRAME-PORT-REF", ref)
        self.setChildElementOptionalRefType(element, "FRAME-REF", triggering.getFrameRef())

        refs = triggering.getPduTriggeringRefs()
        if len(refs) > 0:
            triggerings_tag = ET.SubElement(element, "PDU-TRIGGERINGS")
            for ref in refs:
                child_element = ET.SubElement(triggerings_tag, "PDU-TRIGGERING-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "PDU-TRIGGERING-REF", ref)

    def writeCanFrameTriggering(self, element: ET.Element, triggering: CanFrameTriggering):
        self.logger.debug("WRite CanFrameTriggering %s" % triggering.getShortName())
        child_element = ET.SubElement(element, "CAN-FRAME-TRIGGERING")
        self.writeFrameTriggering(child_element, triggering)
        timings = triggering.getAbsolutelyScheduledTimings()
        if len(timings) > 0:
            timings_element = ET.SubElement(child_element, "ABSOLUTELY-SCHEDULED-TIMINGS")
            for timing in timings:
                if isinstance(timing, TtcanAbsolutelyScheduledTiming):
                    self.writeTtcanAbsolutelyScheduledTiming(timings_element, timing)
                else:
                    self.notImplemented("Unsupported AbsolutelyScheduledTiming <%s>" % type(timing))
        addressing_mode = triggering.getCanAddressingMode()
        if addressing_mode is not None:
            addressing_mode_element = ET.SubElement(child_element, "CAN-ADDRESSING-MODE")
            addressing_mode_element.text = addressing_mode.getValue()
        rx_behavior = triggering.getCanFrameRxBehavior()
        if rx_behavior is not None:
            rx_behavior_element = ET.SubElement(child_element, "CAN-FRAME-RX-BEHAVIOR")
            rx_behavior_element.text = rx_behavior.getValue()
        tx_behavior = triggering.getCanFrameTxBehavior()
        if tx_behavior is not None:
            tx_behavior_element = ET.SubElement(child_element, "CAN-FRAME-TX-BEHAVIOR")
            tx_behavior_element.text = tx_behavior.getValue()
        props = triggering.getCanXlFrameTriggeringProps()
        if props is not None:
            props_element = ET.SubElement(child_element, "CAN-XL-FRAME-TRIGGERING-PROPS")
            self.setChildElementOptionalPositiveInteger(props_element, "ACCEPTANCE-FIELD", props.getAcceptanceField())
            self.setChildElementOptionalPositiveInteger(props_element, "PRIORITY-ID", props.getPriorityId())
            self.setChildElementOptionalPositiveInteger(props_element, "SDU-TYPE", props.getSduType())
            self.setChildElementOptionalPositiveInteger(props_element, "VCID", props.getVcid())
        self.setChildElementOptionalNumericalValue(child_element, "IDENTIFIER", triggering.getIdentifier())
        self.setChildElementOptionalBooleanValue(child_element, "J-1939-REQUESTABLE", triggering.getJ1939requestable())
        self.setRxIdentifierRange(child_element, "RX-IDENTIFIER-RANGE", triggering.getRxIdentifierRange())
        self.setChildElementOptionalPositiveInteger(child_element, "RX-MASK", triggering.getRxMask())
        self.setChildElementOptionalPositiveInteger(child_element, "TX-MASK", triggering.getTxMask())

    def writeLinFrameTriggering(self, element: ET.Element, triggering: LinFrameTriggering):
        self.logger.debug("Write LinFrameTriggering %s" % triggering.getShortName())
        child_element = ET.SubElement(element, "LIN-FRAME-TRIGGERING")
        self.writeFrameTriggering(child_element, triggering)
        self.setChildElementOptionalNumericalValue(child_element, "IDENTIFIER", triggering.getIdentifier())
        self.setChildElementOptionalLiteral(child_element, "LIN-CHECKSUM", triggering.getLinChecksum())

    def writeCommunicationCycle(self, element: ET.Element, cycle: CommunicationCycle):
        self.writeARObjectAttributes(element, cycle)

    def writeCycleRepetition(self, element: ET.Element, cycle: CycleRepetition):
        if cycle is not None:
            child_element = ET.SubElement(element, "CYCLE-REPETITION")
            self.writeCommunicationCycle(child_element, cycle)
            self.setChildElementOptionalIntegerValue(child_element, "BASE-CYCLE", cycle.getBaseCycle())
            self.setChildElementOptionalLiteral(child_element, "CYCLE-REPETITION", cycle.getCycleRepetition())

    def writeFlexrayAbsolutelyScheduledTimingCommunicationCycle(self, element: ET.Element, timing: FlexrayAbsolutelyScheduledTiming):
        cycle = timing.getCommunicationCycle()
        if cycle is not None:
            child_element = ET.SubElement(element, "COMMUNICATION-CYCLE")
            if isinstance(cycle, CycleRepetition):
                self.writeCycleRepetition(child_element, cycle)
            else:
                self.notImplemented("Unsupported CommunicationCycle <%s>" % type(child_element))

    def writeFlexrayAbsolutelyScheduledTiming(self, element: ET.Element, timing: FlexrayAbsolutelyScheduledTiming):
        if timing is not None:
            child_element = ET.SubElement(element, "FLEXRAY-ABSOLUTELY-SCHEDULED-TIMING")
            self.writeARObjectAttributes(child_element, timing)
            self.writeFlexrayAbsolutelyScheduledTimingCommunicationCycle(child_element, timing)
            self.setChildElementOptionalPositiveInteger(child_element, "SLOT-ID", timing.getSlotID())

    def writeFlexrayFrameTriggeringAbsolutelyScheduledTimings(self, element: ET.Element, triggering: FlexrayFrameTriggering):
        timings = triggering.getAbsolutelyScheduledTimings()
        if len(timings) > 0:
            child_element = ET.SubElement(element, "ABSOLUTELY-SCHEDULED-TIMINGS")
            for timing in timings:
                if isinstance(timing, FlexrayAbsolutelyScheduledTiming):
                    self.writeFlexrayAbsolutelyScheduledTiming(child_element, timing)
                else:
                    self.notImplemented("Unsupported AbsolutelyScheduledTiming <%s>" % type(timing))

    def writeTtcanAbsolutelyScheduledTimingCommunicationCycle(self, element: ET.Element, timing: TtcanAbsolutelyScheduledTiming):
        cycle = timing.getCommunicationCycle()
        if cycle is not None:
            child_element = ET.SubElement(element, "COMMUNICATION-CYCLE")
            if isinstance(cycle, CycleRepetition):
                self.writeCycleRepetition(child_element, cycle)
            else:
                self.notImplemented("Unsupported CommunicationCycle <%s>" % type(cycle))

    def writeTtcanAbsolutelyScheduledTiming(self, element: ET.Element, timing: TtcanAbsolutelyScheduledTiming):
        if timing is not None:
            child_element = ET.SubElement(element, "TTCAN-ABSOLUTELY-SCHEDULED-TIMING")
            self.writeARObjectAttributes(child_element, timing)
            self.writeTtcanAbsolutelyScheduledTimingCommunicationCycle(child_element, timing)
            self.setChildElementOptionalIntegerValue(child_element, "TIME-MARK", timing.getTimeMark())
            self.setChildElementOptionalLiteral(child_element, "TRIGGER", timing.getTrigger())

    def writeFlexrayFrameTriggering(self, element: ET.Element, triggering: FlexrayFrameTriggering):
        self.logger.debug("Write FlexrayFrameTriggering %s" % triggering.getShortName())
        child_element = ET.SubElement(element, "FLEXRAY-FRAME-TRIGGERING")
        self.writeFrameTriggering(child_element, triggering)
        self.writeFlexrayFrameTriggeringAbsolutelyScheduledTimings(child_element, triggering)
        self.setChildElementOptionalBooleanValue(child_element, "ALLOW-DYNAMIC-L-SDU-LENGTH", triggering.getAllowDynamicLSduLength())
        self.setChildElementOptionalPositiveInteger(child_element, "MESSAGE-ID", triggering.getMessageId())
        self.setChildElementOptionalBooleanValue(child_element, "PAYLOAD-PREAMBLE-INDICATOR", triggering.getPayloadPreambleIndicator())

    def writeISignalTriggering(self, element: ET.Element, triggering: ISignalTriggering):
        self.logger.debug("Write ISignalTriggering %s" % triggering.getShortName())
        child_element = ET.SubElement(element, "I-SIGNAL-TRIGGERING")
        self.writeIdentifiable(child_element, triggering)
        self.setChildElementOptionalRefType(child_element, "I-SIGNAL-GROUP-REF", triggering.getISignalGroupRef())
        ref_list = triggering.getISignalPortRefs()
        if len(ref_list) > 0:
            i_signal_port_refs_tag = ET.SubElement(child_element, "I-SIGNAL-PORT-REFS")
            for ref in ref_list:
                self.setChildElementOptionalRefType(i_signal_port_refs_tag, "I-SIGNAL-PORT-REF", ref)
        self.setChildElementOptionalRefType(child_element, "I-SIGNAL-REF", triggering.getISignalRef())

    def writePduTriggering(self, element: ET.Element, triggering: PduTriggering):
        self.logger.debug("Write PduTriggering %s" % triggering.getShortName())
        child_element = ET.SubElement(element, "PDU-TRIGGERING")
        self.writeIdentifiable(child_element, triggering)
        ref_list = triggering.getIPduPortRefs()
        if len(ref_list) > 0:
            i_pdu_port_refs_tag = ET.SubElement(child_element, "I-PDU-PORT-REFS")
            for ref in ref_list:
                self.setChildElementOptionalRefType(i_pdu_port_refs_tag, "I-PDU-PORT-REF", ref)
        self.setChildElementOptionalRefType(child_element, "I-PDU-REF", triggering.getIPduRef())

        refs = triggering.getISignalTriggeringRefs()
        if len(refs) > 0:
            triggerings_tag = ET.SubElement(child_element, "I-SIGNAL-TRIGGERINGS")
            for ref in refs:
                conditional_tag = ET.SubElement(triggerings_tag, "I-SIGNAL-TRIGGERING-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(conditional_tag, "I-SIGNAL-TRIGGERING-REF", ref)
        self.setChildElementOptionalRefType(child_element, "SEC-OC-CRYPTO-MAPPING-REF", triggering.getSecOcCryptoMappingRef())

        conditions = triggering.getTriggerIPduSendConditions()
        if len(conditions) > 0:
            conditions_tag = ET.SubElement(child_element, "TRIGGER-I-PDU-SEND-CONDITIONS")
            for condition in conditions:
                if isinstance(condition, TriggerIPduSendCondition):
                    self.writeTriggerIPduSendCondition(conditions_tag, condition)
                else:
                    self.notImplemented("Unsupported TriggerIPduSendCondition <%s>" % type(condition))

    def writeTriggerIPduSendCondition(self, element: ET.Element, condition: TriggerIPduSendCondition):
        child_element = ET.SubElement(element, "TRIGGER-I-PDU-SEND-CONDITION")
        refs = condition.getModeDeclarationRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(child_element, "MODE-DECLARATION-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "MODE-DECLARATION-REF", ref)

    def writePhysicalChannelCommConnectorRefs(self, element, channel):
        connectors = channel.getCommConnectorRefs()
        if len(connectors) > 0:
            connectors_tag = ET.SubElement(element, "COMM-CONNECTORS")
            for connector in connectors:
                child_element = ET.SubElement(connectors_tag, "COMMUNICATION-CONNECTOR-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "COMMUNICATION-CONNECTOR-REF", connector)

    def writePhysicalChannelFrameTriggerings(self, element, channel):
        triggerings = channel.getFrameTriggerings()
        if len(triggerings) > 0:
            triggerings_tag = ET.SubElement(element, "FRAME-TRIGGERINGS")
            for triggering in triggerings:
                if isinstance(triggering, CanFrameTriggering):
                    self.writeCanFrameTriggering(triggerings_tag, triggering)
                elif isinstance(triggering, LinFrameTriggering):
                    self.writeLinFrameTriggering(triggerings_tag, triggering)
                elif isinstance(triggering, FlexrayFrameTriggering):
                    self.writeFlexrayFrameTriggering(triggerings_tag, triggering)
                else:
                    self.notImplemented("Unsupported Frame Triggering <%s>" % type(triggering))

    def writePhysicalChannelISignalTriggerings(self, element, channel):
        triggerings = channel.getISignalTriggerings()
        if len(triggerings) > 0:
            triggerings_tag = ET.SubElement(element, "I-SIGNAL-TRIGGERINGS")
            for triggering in triggerings:
                if isinstance(triggering, ISignalTriggering):
                    self.writeISignalTriggering(triggerings_tag, triggering)
                else:
                    self.notImplemented("Unsupported ISignalTriggering <%s>" % type(triggering))

    def writePhysicalChannelPduTriggerings(self, element, channel):
        triggerings = channel.getPduTriggerings()
        if len(triggerings) > 0:
            triggerings_tag = ET.SubElement(element, "PDU-TRIGGERINGS")
            for triggering in triggerings:
                if isinstance(triggering, PduTriggering):
                    self.writePduTriggering(triggerings_tag, triggering)
                else:
                    self.notImplemented("Unsupported PduTriggering <%s>" % type(triggering))

    def writePhysicalChannelManagedPhysicalChannelRefs(self, element, channel):
        refs = channel.getManagedPhysicalChannelRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "MANAGED-PHYSICAL-CHANNEL-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "MANAGED-PHYSICAL-CHANNEL-REF", ref)

    def writePhysicalChannel(self, element: ET.Element, channel: PhysicalChannel):
        self.writeIdentifiable(element, channel)

        self.writePhysicalChannelCommConnectorRefs(element, channel)
        self.writePhysicalChannelFrameTriggerings(element, channel)
        self.writePhysicalChannelISignalTriggerings(element, channel)
        self.writePhysicalChannelPduTriggerings(element, channel)
        self.writePhysicalChannelManagedPhysicalChannelRefs(element, channel)

    def writeCanPhysicalChannel(self, element: ET.Element, channel: CanPhysicalChannel):
        self.logger.debug("Set CanPhysicalChannel %s" % channel.getShortName())
        child_element = ET.SubElement(element, "CAN-PHYSICAL-CHANNEL")
        self.writePhysicalChannel(child_element, channel)

    def writeScheduleTableEntry(self, element: ET.Element, entry: ScheduleTableEntry):
        self.writeDocumentationBlock(element, "INTRODUCTION", entry.getIntroduction())
        self.setChildElementOptionalTimeValue(element, "DELAY", entry.getDelay())
        self.setChildElementOptionalIntegerValue(element, "POSITION-IN-TABLE", entry.getPositionInTable())

    def setApplicationEntry(self, element: ET.Element, key: str, entry: ApplicationEntry):
        if entry is not None:
            child_element = ET.SubElement(element, key)
            self.writeScheduleTableEntry(child_element, entry)
            self.setChildElementOptionalRefType(child_element, "FRAME-TRIGGERING-REF", entry.getFrameTriggeringRef())

    def writeLinConfigurationEntry(self, element: ET.Element, entry: LinConfigurationEntry):
        self.setChildElementOptionalRefType(element, "ASSIGNED-CONTROLLER-REF", entry.getAssignedControllerRef())
        self.setChildElementOptionalRefType(element, "ASSIGNED-LIN-SLAVE-CONFIG-REF", entry.getAssignedLinSlaveConfigRef())

    def setFreeFormat(self, element: ET.Element, key: str, entry: FreeFormat):
        if entry is not None:
            child_element = ET.SubElement(element, key)
            self.writeScheduleTableEntry(child_element, entry)
            if len(entry.getByteValues()) > 0:
                byte_values_element = ET.SubElement(child_element, "BYTE-VALUES")
                for byte_value in entry.getByteValues():
                    self.setChildElementOptionalIntegerValue(byte_values_element, "BYTE-VALUE", byte_value)

    def setAssignFrameId(self, element: ET.Element, key: str, entry: AssignFrameId):
        if entry is not None:
            child_element = ET.SubElement(element, key)
            self.writeScheduleTableEntry(child_element, entry)
            self.writeLinConfigurationEntry(child_element, entry)
            self.setChildElementOptionalRefType(child_element, "ASSIGNED-FRAME-TRIGGERING-REF", entry.getAssignedFrameTriggeringRef())

    def setUnassignFrameId(self, element: ET.Element, key: str, entry: UnassignFrameId):
        if entry is not None:
            child_element = ET.SubElement(element, key)
            self.writeScheduleTableEntry(child_element, entry)
            self.writeLinConfigurationEntry(child_element, entry)
            self.setChildElementOptionalRefType(child_element, "UNASSIGNED-FRAME-TRIGGERING-REF", entry.getUnassignedFrameTriggeringRef())

    def setAssignFrameIdRange(self, element: ET.Element, key: str, entry: AssignFrameIdRange):
        if entry is not None:
            child_element = ET.SubElement(element, key)
            self.writeScheduleTableEntry(child_element, entry)
            self.writeLinConfigurationEntry(child_element, entry)
            frame_pids = entry.getFramePids()
            if len(frame_pids) > 0:
                frame_pids_element = ET.SubElement(child_element, "FRAME-PIDS")
                for frame_pid in frame_pids:
                    frame_pid_element = ET.SubElement(frame_pids_element, "FRAME-PID")
                    self.setChildElementOptionalIntegerValue(frame_pid_element, "INDEX", frame_pid.getIndex())
                    self.setChildElementOptionalPositiveInteger(frame_pid_element, "PID", frame_pid.getPid())
            self.setChildElementOptionalIntegerValue(child_element, "START-INDEX", entry.getStartIndex())

    def setAssignNad(self, element: ET.Element, key: str, entry: AssignNad):
        if entry is not None:
            child_element = ET.SubElement(element, key)
            self.writeScheduleTableEntry(child_element, entry)
            self.writeLinConfigurationEntry(child_element, entry)
            self.setChildElementOptionalIntegerValue(child_element, "NEW-NAD", entry.getNewNad())

    def setConditionalChangeNad(self, element: ET.Element, key: str, entry: ConditionalChangeNad):
        if entry is not None:
            child_element = ET.SubElement(element, key)
            self.writeScheduleTableEntry(child_element, entry)
            self.writeLinConfigurationEntry(child_element, entry)
            self.setChildElementOptionalIntegerValue(child_element, "BYTE", entry.getByte())
            self.setChildElementOptionalPositiveInteger(child_element, "ID", entry.getId())
            self.setChildElementOptionalIntegerValue(child_element, "INVERT", entry.getInvert())
            self.setChildElementOptionalIntegerValue(child_element, "MASK", entry.getMask())
            self.setChildElementOptionalIntegerValue(child_element, "NEW-NAD", entry.getNewNad())

    def setSaveConfigurationEntry(self, element: ET.Element, key: str, entry: SaveConfigurationEntry):
        if entry is not None:
            child_element = ET.SubElement(element, key)
            self.writeScheduleTableEntry(child_element, entry)
            self.writeLinConfigurationEntry(child_element, entry)

    def setDataDumpEntry(self, element: ET.Element, key: str, entry: DataDumpEntry):
        if entry is not None:
            child_element = ET.SubElement(element, key)
            self.writeScheduleTableEntry(child_element, entry)
            self.writeLinConfigurationEntry(child_element, entry)
            if len(entry.getByteValues()) > 0:
                byte_values_element = ET.SubElement(child_element, "BYTE-VALUES")
                for byte_value in entry.getByteValues():
                    self.setChildElementOptionalIntegerValue(byte_values_element, "BYTE-VALUE", byte_value)

    def writeLinScheduleTableTableEntries(self, element: ET.Element, table: LinScheduleTable):
        entries = table.getTableEntries()
        if len(entries) > 0:
            child_element = ET.SubElement(element, "TABLE-ENTRYS")
            for entry in entries:
                if isinstance(entry, ApplicationEntry):
                    self.setApplicationEntry(child_element, "APPLICATION-ENTRY", entry)
                elif isinstance(entry, FreeFormat):
                    self.setFreeFormat(child_element, "FREE-FORMAT", entry)
                elif isinstance(entry, AssignFrameIdRange):
                    self.setAssignFrameIdRange(child_element, "ASSIGN-FRAME-ID-RANGE", entry)
                elif isinstance(entry, AssignFrameId):
                    self.setAssignFrameId(child_element, "ASSIGN-FRAME-ID", entry)
                elif isinstance(entry, UnassignFrameId):
                    self.setUnassignFrameId(child_element, "UNASSIGN-FRAME-ID", entry)
                elif isinstance(entry, AssignNad):
                    self.setAssignNad(child_element, "ASSIGN-NAD", entry)
                elif isinstance(entry, ConditionalChangeNad):
                    self.setConditionalChangeNad(child_element, "CONDITIONAL-CHANGE-NAD", entry)
                elif isinstance(entry, SaveConfigurationEntry):
                    self.setSaveConfigurationEntry(child_element, "SAVE-CONFIGURATION-ENTRY", entry)
                elif isinstance(entry, DataDumpEntry):
                    self.setDataDumpEntry(child_element, "DATA-DUMP-ENTRY", entry)
                else:
                    self.notImplemented("Unsupported Schedule Table <%s>" % type(entry))

    def writeLinScheduleTable(self, element: ET.Element, table: LinScheduleTable):
        child_element = ET.SubElement(element, "LIN-SCHEDULE-TABLE")
        self.writeIdentifiable(child_element, table)
        self.setChildElementOptionalLiteral(child_element, "RESUME-POSITION", table.getResumePosition())
        self.setChildElementOptionalLiteral(child_element, "RUN-MODE", table.getRunMode())
        self.writeLinScheduleTableTableEntries(child_element, table)

    def writeLinPhysicalChannelScheduleTables(self, element: ET.Element, channel: LinPhysicalChannel):
        tables = channel.getScheduleTables()
        if len(tables) > 0:
            child_element = ET.SubElement(element, "SCHEDULE-TABLES")
            for table in tables:
                if isinstance(table, LinScheduleTable):
                    self.writeLinScheduleTable(child_element, table)
                else:
                    self.notImplemented("Unsupported Schedule Table <%s>" % type(table))

    def writeLinPhysicalChannel(self, element: ET.Element, channel: LinPhysicalChannel):
        self.logger.debug("Set LinPhysicalChannel %s" % channel.getShortName())
        child_element = ET.SubElement(element, "LIN-PHYSICAL-CHANNEL")
        self.writePhysicalChannel(child_element, channel)
        self.writeLinPhysicalChannelScheduleTables(child_element, channel)

    def setIpv6Configuration(self, element: ET.Element, configuration: Ipv6Configuration):
        if configuration is not None:
            child_element = ET.SubElement(element, "IPV-6-CONFIGURATION")
            self.setChildElementOptionalPositiveInteger(child_element, "ASSIGNMENT-PRIORITY", configuration.getAssignmentPriority())
            self.setChildElementOptionalLiteral(child_element, "DEFAULT-ROUTER", configuration.getDefaultRouter())
            addresses = configuration.getDnsServerAddresses()
            if len(addresses) > 0:
                dns_element = ET.SubElement(child_element, "DNS-SERVER-ADDRESSES")
                for address in addresses:
                    self.setChildElementOptionalLiteral(dns_element, "DNS-SERVER-ADDRESS", address)
            self.setChildElementOptionalBooleanValue(child_element, "ENABLE-ANYCAST", configuration.getEnableAnycast())
            self.setChildElementOptionalPositiveInteger(child_element, "HOP-COUNT", configuration.getHopCount())
            self.setChildElementOptionalLiteral(child_element, "IP-ADDRESS-KEEP-BEHAVIOR", configuration.getIpAddressKeepBehavior())
            self.setChildElementOptionalPositiveInteger(child_element, "IP-ADDRESS-PREFIX-LENGTH", configuration.getIpAddressPrefixLength())
            self.setChildElementOptionalLiteral(child_element, "IPV-6-ADDRESS", configuration.getIpv6Address())
            self.setChildElementOptionalLiteral(child_element, "IPV-6-ADDRESS-SOURCE", configuration.getIpv6AddressSource())

    def writeNetworkEndPointNetworkEndPointAddresses(self, element: ET.Element, addresses: List[NetworkEndpointAddress]):
        if len(addresses) > 0:
            child_element = ET.SubElement(element, "NETWORK-ENDPOINT-ADDRESSES")
            for address in addresses:
                if isinstance(address, Ipv6Configuration):
                    self.setIpv6Configuration(child_element, address)
                else:
                    self.notImplemented("Unsupported Network EndPoint Address <%s>" % type(address))

    def setDoIpEntity(self, element: ET.Element, key: str, entity: DoIpEntity):
        if entity is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "DO-IP-ENTITY-ROLE", entity.getDoIpEntityRole())

    def setTimeSynchronization(self, element: ET.Element, key: str, sync: TimeSynchronization):
        if sync is not None:
            child_element = ET.SubElement(element, key)
            client = sync.getTimeSyncClient()
            if client is not None:
                client_element = ET.SubElement(child_element, "TIME-SYNC-CLIENT")
                self.setChildElementOptionalLiteral(client_element, "TIME-SYNC-TECHNOLOGY", client.getTimeSyncTechnology())
                self.writeTimeSyncClientConfigurationOrderedMasters(client_element, client)
            server = sync.getTimeSyncServer()
            if server is not None:
                server_element = ET.SubElement(child_element, "TIME-SYNC-SERVER")
                self.writeReferrable(server_element, server)
                self.setChildElementOptionalLiteral(server_element, "TIME-SYNC-TECHNOLOGY", server.getTimeSyncTechnology())

    def writeTimeSyncClientConfigurationOrderedMasters(self, element: ET.Element, client: TimeSyncClientConfiguration):
        masters = client.getOrderedMasters()
        if len(masters) > 0:
            list_element = ET.SubElement(element, "ORDERED-MASTER-LIST")
            for master in masters:
                if master is not None:
                    master_element = ET.SubElement(list_element, "ORDERED-MASTER")
                    self.writeARObjectAttributes(master_element, master)
                    self.setChildElementOptionalPositiveInteger(master_element, "INDEX", master.getIndex())
                    self.setChildElementOptionalRefType(master_element, "TIME-SYNC-SERVER-REF", master.getTimeSyncServer())

    def setInfrastructureServices(self, element: ET.Element, key: str, services: InfrastructureServices):
        if services is not None:
            child_element = ET.SubElement(element, key)
            self.setDoIpEntity(child_element, "DO-IP-ENTITY", services.getDoIpEntity())
            self.setTimeSynchronization(child_element, "TIME-SYNCHRONIZATION", services.getTimeSynchronization())

    def writeNetworkEndPoint(self, element: ET.Element, end_point: NetworkEndpoint):
        self.logger.debug("Set NetworkEndpoint %s" % end_point.getShortName())
        child_element = ET.SubElement(element, "NETWORK-ENDPOINT")
        self.writeIdentifiable(child_element, end_point)
        self.setInfrastructureServices(child_element, "INFRASTRUCTURE-SERVICES", end_point.getInfrastructureServices())
        self.writeNetworkEndPointNetworkEndPointAddresses(child_element, end_point.getNetworkEndpointAddresses())
        self.setChildElementOptionalPositiveInteger(child_element, "PRIORITY", end_point.getPriority())

    def writeEthernetPhysicalChannelNetworkEndPoints(self, element: ET.Element, end_points: List[NetworkEndpoint]):
        if len(end_points) > 0:
            child_element = ET.SubElement(element, "NETWORK-ENDPOINTS")
            for end_point in end_points:
                self.writeNetworkEndPoint(child_element, end_point)

    def setSocketConnectionIpduIdentifier(self, element: ET.Element, identifier: SocketConnectionIpduIdentifier):
        if identifier is not None:
            child_element = ET.SubElement(element, "SOCKET-CONNECTION-IPDU-IDENTIFIER")
            self.setChildElementOptionalPositiveInteger(child_element, "HEADER-ID", identifier.getHeaderId())
            self.setChildElementOptionalTimeValue(child_element, "PDU-COLLECTION-PDU-TIMEOUT", identifier.getPduCollectionPduTimeout())
            self.setChildElementOptionalLiteral(child_element, "PDU-COLLECTION-SEMANTICS", identifier.getPduCollectionSemantics())
            self.setChildElementOptionalLiteral(child_element, "PDU-COLLECTION-TRIGGER", identifier.getPduCollectionTrigger())
            self.setChildElementOptionalRefType(child_element, "PDU-REF", identifier.getPduRef())
            self.setChildElementOptionalRefType(child_element, "PDU-TRIGGERING-REF", identifier.getPduTriggeringRef())
            routing_group_refs = identifier.getRoutingGroupRefs()
            if len(routing_group_refs) > 0:
                refs_element = ET.SubElement(child_element, "ROUTING-GROUP-REFS")
                for ref in routing_group_refs:
                    self.setChildElementOptionalRefType(refs_element, "ROUTING-GROUP-REF", ref)

    def setSocketConnectionPdus(self, element: ET.Element, key: str, pdus: List[SocketConnectionIpduIdentifier]):
        if len(pdus) > 0:
            child_element = ET.SubElement(element, key)
            for pdu in pdus:
                if isinstance(pdu, SocketConnectionIpduIdentifier):
                    self.setSocketConnectionIpduIdentifier(child_element, pdu)
                else:
                    self.notImplemented("Unsupported Pdu <%s>" % type(pdu))

    def setSocketConnection(self, element: ET.Element, connection: SocketConnection):
        if connection is not None:
            child_element = ET.SubElement(element, "SOCKET-CONNECTION")
            self.setChildElementOptionalLiteral(child_element, "RUNTIME-PORT-CONFIGURATION", connection.getRuntimePortConfiguration())
            self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", connection.getShortLabel())
            self.setChildElementOptionalRefType(child_element, "ALLOWED-I-PV-6-EXT-HEADERS-REF", connection.getAllowedIPv6ExtHeadersRef())
            self.setChildElementOptionalRefType(child_element, "ALLOWED-TCP-OPTIONS-REF", connection.getAllowedTcpOptionsRef())
            self.setChildElementOptionalBooleanValue(child_element, "CLIENT-IP-ADDR-FROM-CONNECTION-REQUEST", connection.getClientIpAddrFromConnectionRequest())
            self.setChildElementOptionalRefType(child_element, "CLIENT-PORT-REF", connection.getClientPortRef())
            self.setChildElementOptionalBooleanValue(child_element, "CLIENT-PORT-FROM-CONNECTION-REQUEST", connection.getClientPortFromConnectionRequest())
            self.setSocketConnectionPdus(child_element, "PDUS", connection.getPdus())
            self.setChildElementOptionalPositiveInteger(child_element, "PDU-COLLECTION-MAX-BUFFER-SIZE", connection.getPduCollectionMaxBufferSize())
            self.setChildElementOptionalTimeValue(child_element, "PDU-COLLECTION-TIMEOUT", connection.getPduCollectionTimeout())
            self.setChildElementOptionalLiteral(child_element, "RUNTIME-IP-ADDRESS-CONFIGURATION", connection.getRuntimeIpAddressConfiguration())

    def writeSocketConnectionBundleConnections(self, element: ET.Element, bundle: SocketConnectionBundle):
        connections = bundle.getBundledConnections()
        if len(connections) > 0:
            child_element = ET.SubElement(element, "BUNDLED-CONNECTIONS")
            for connection in connections:
                if isinstance(connection, SocketConnection):
                    self.setSocketConnection(child_element, connection)
                else:
                    self.notImplemented("Unsupported Bundled Connection <%s>" % type(connection))

    def writeSocketConnectionBundle(self, element: ET.Element, bundle: SocketConnectionBundle):
        if bundle is not None:
            child_element = ET.SubElement(element, "SOCKET-CONNECTION-BUNDLE")
            self.writeReferrable(child_element, bundle)
            self.writeSocketConnectionBundleConnections(child_element, bundle)
            self.setChildElementOptionalPositiveInteger(child_element, "DIFFERENTIATED-SERVICE-FIELD", bundle.getDifferentiatedServiceField())
            self.setChildElementOptionalPositiveInteger(child_element, "FLOW-LABEL", bundle.getFlowLabel())
            self.setChildElementOptionalBooleanValue(child_element, "PATH-MTU-DISCOVERY-ENABLED", bundle.getPathMtuDiscoveryEnabled())
            self.setSocketConnectionPdus(child_element, "PDUS", bundle.getPdus())
            self.setChildElementOptionalRefType(child_element, "SERVER-PORT-REF", bundle.getServerPortRef())
            self.setChildElementOptionalLiteral(child_element, "UDP-CHECKSUM-HANDLING", bundle.getUdpChecksumHandling())

    def writeTcpOptionFilterSet(self, element: ET.Element, tcp_option_filter_set: TcpOptionFilterSet):
        self.logger.debug("Write TcpOptionFilterSet <%s>" % tcp_option_filter_set.getShortName())
        child_element = ET.SubElement(element, "TCP-OPTION-FILTER-SET")
        self.writeIdentifiable(child_element, tcp_option_filter_set)
        tcp_filter_lists = tcp_option_filter_set.getTcpOptionFilterLists()
        if len(tcp_filter_lists) > 0:
            lists_element = ET.SubElement(child_element, "TCP-OPTION-FILTER-LISTS")
            for tcp_filter_list in tcp_filter_lists:
                if isinstance(tcp_filter_list, TcpOptionFilterList):
                    self.writeTcpOptionFilterList(lists_element, tcp_filter_list)
                else:
                    self.notImplemented("Unsupported TcpOptionFilterList <%s>" % type(tcp_filter_list))

    def writeTcpOptionFilterList(self, element: ET.Element, tcp_filter_list: TcpOptionFilterList):
        child_element = ET.SubElement(element, "TCP-OPTION-FILTER-LIST")
        self.writeIdentifiable(child_element, tcp_filter_list)
        allowed_tcp_options = tcp_filter_list.getAllowedTcpOptions()
        if len(allowed_tcp_options) > 0:
            options_element = ET.SubElement(child_element, "ALLOWED-TCP-OPTIONS")
            for option in allowed_tcp_options:
                self.setChildElementOptionalPositiveInteger(options_element, "ALLOWED-TCP-OPTION", option)

    def writeSoAdConfigConnectionBundles(self, element: ET.Element, config: SoAdConfig):
        bundles = config.getConnectionBundles()
        if len(bundles) > 0:
            child_element = ET.SubElement(element, "CONNECTION-BUNDLES")
            for bundle in bundles:
                if isinstance(bundle, SocketConnectionBundle):
                    self.writeSocketConnectionBundle(child_element, bundle)
                else:
                    self.notImplemented("Unsupported Connection Bundle <%s>" % type(bundle))

    def setTpPort(self, element: ET.SubElement, key: str, port: TpPort):
        if port is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalBooleanValue(child_element, "DYNAMICALLY-ASSIGNED", port.getDynamicallyAssigned())
            self.setChildElementOptionalPositiveInteger(child_element, "PORT-NUMBER", port.getPortNumber())

    def writeUdpTp(self, element: ET.Element, tp: UdpTp):
        child_element = ET.SubElement(element, "UDP-TP")
        self.setTpPort(child_element, "UDP-TP-PORT", tp.getUdpTpPort())

    def writeTcpTp(self, element: ET.Element, tp: TcpTp):
        child_element = ET.SubElement(element, "TCP-TP")
        self.setChildElementOptionalTimeValue(child_element, "KEEP-ALIVE-INTERVAL", tp.getKeepAliveInterval())
        self.setChildElementOptionalPositiveInteger(child_element, "KEEP-ALIVE-PROBES-MAX", tp.getKeepAliveProbesMax())
        self.setChildElementOptionalTimeValue(child_element, "KEEP-ALIVE-TIME", tp.getKeepAliveTime())
        self.setChildElementOptionalBooleanValue(child_element, "KEEP-ALIVES", tp.getKeepAlives())
        self.setChildElementOptionalLiteral(child_element, "NAGLES-ALGORITHM", tp.getNaglesAlgorithm())
        self.setTpPort(child_element, "TCP-TP-PORT", tp.getTcpTpPort())

    def writeGenericTp(self, element: ET.Element, tp: GenericTp):
        child_element = ET.SubElement(element, "GENERIC-TP")
        self.setChildElementOptionalLiteral(child_element, "TP-ADDRESS", tp.getTpAddress())
        self.setChildElementOptionalLiteral(child_element, "TP-TECHNOLOGY", tp.getTpTechnology())

    def writeTransportProtocolConfiguration(self, element: ET.Element, configuration: TransportProtocolConfiguration):
        if configuration is not None:
            child_element = ET.SubElement(element, "TP-CONFIGURATION")
            if isinstance(configuration, UdpTp):
                self.writeUdpTp(child_element, configuration)
            elif isinstance(configuration, TcpTp):
                self.writeTcpTp(child_element, configuration)
            elif isinstance(configuration, GenericTp):
                self.writeGenericTp(child_element, configuration)
            else:
                self.notImplemented("Unsupported TransportProtocolConfiguration <%s>" % type(configuration))

        return configuration

    def writeConsumedEventGroupRoutingGroupRefs(self, element: ET.Element, group: ConsumedEventGroup):
        refs = group.getRoutingGroupRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "ROUTING-GROUP-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "ROUTING-GROUP-REF", ref)

    def setRequestResponseDelay(self, element: ET.Element, key: str, delay: RequestResponseDelay):
        if delay is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalTimeValue(child_element, "MAX-VALUE", delay.getMaxValue())
            self.setChildElementOptionalTimeValue(child_element, "MIN-VALUE", delay.getMinValue())

    def setSdClientConfig(self, element: ET.Element, key: str, config: SdClientConfig):
        if config is not None:
            child_element = ET.SubElement(element, key)

            self.setTagWithOptionalValues(child_element, "CAPABILITY-RECORDS", config.getCapabilityRecords())
            self.setChildElementOptionalPositiveInteger(child_element, "CLIENT-SERVICE-MAJOR-VERSION", config.getClientServiceMajorVersion())
            self.setChildElementOptionalPositiveInteger(child_element, "CLIENT-SERVICE-MINOR-VERSION", config.getClientServiceMinorVersion())
            self.setInitialSdDelayConfig(child_element, "INITIAL-FIND-BEHAVIOR", config.getInitialFindBehavior())
            self.setRequestResponseDelay(child_element, "REQUEST-RESPONSE-DELAY", config.getRequestResponseDelay())
            self.setChildElementOptionalPositiveInteger(child_element, "TTL", config.getTtl())

    def writeConsumedEventGroup(self, element: ET.Element, group: ConsumedEventGroup):
        if group is not None:
            child_element = ET.SubElement(element, "CONSUMED-EVENT-GROUP")
            self.writeIdentifiable(child_element, group)
            self.setChildElementOptionalRefType(child_element, "APPLICATION-ENDPOINT-REF", group.getApplicationEndpointRef())
            self.setChildElementOptionalBooleanValue(child_element, "AUTO-REQUIRE", group.getAutoRequire())
            self.setChildElementOptionalPositiveInteger(child_element, "EVENT-GROUP-IDENTIFIER", group.getEventGroupIdentifier())
            refs = group.getEventMulticastAddressRefs()
            if len(refs) > 0:
                wrapper = ET.SubElement(child_element, "EVENT-MULTICAST-ADDRESSS")
                for ref in refs:
                    cond_tag = ET.SubElement(wrapper, "APPLICATION-ENDPOINT-REF-CONDITIONAL")
                    self.setChildElementOptionalRefType(cond_tag, "APPLICATION-ENDPOINT-REF", ref)
            groups = group.getPduActivationRoutingGroups()
            if len(groups) > 0:
                wrapper = ET.SubElement(child_element, "PDU-ACTIVATION-ROUTING-GROUPS")
                for activation_group in groups:
                    self.setPduActivationRoutingGroup(wrapper, activation_group)
            self.setChildElementOptionalPositiveInteger(child_element, "PRIORITY", group.getPriority())
            self.writeConsumedEventGroupRoutingGroupRefs(child_element, group)
            self.setSdClientConfig(child_element, "SD-CLIENT-CONFIG", group.getSdClientConfig())
            ref = group.getSdClientTimerConfigRef()
            if ref is not None:
                wrapper = ET.SubElement(child_element, "SD-CLIENT-TIMER-CONFIGS")
                cond_tag = ET.SubElement(wrapper, "SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(cond_tag, "SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF", ref)

    def writeConsumedServiceInstanceConsumedEventGroups(self, element: ET.Element, instance: ConsumedServiceInstance):
        groups = instance.getConsumedEventGroups()
        if len(groups) > 0:
            child_element = ET.SubElement(element, "CONSUMED-EVENT-GROUPS")
            for group in groups:
                if isinstance(group, ConsumedEventGroup):
                    self.writeConsumedEventGroup(child_element, group)
                else:
                    self.notImplemented("Unsupported ConsumedEventGroups <%s>" % type(group))

    def setSomeipServiceVersions(self, element: ET.Element, key: str, versions: List[SomeipServiceVersion]):
        if versions:
            wrapper = ET.SubElement(element, key)
            for version in versions:
                child_element = ET.SubElement(wrapper, "SOMEIP-SERVICE-VERSION")
                self.setChildElementOptionalPositiveInteger(child_element, "MAJOR-VERSION", version.getMajorVersion())
                self.setChildElementOptionalPositiveInteger(child_element, "MINOR-VERSION", version.getMinorVersion())

    def writeAbstractServiceInstanceMethodActivationRoutingGroups(self, element: ET.Element, instance: AbstractServiceInstance):
        group = instance.getMethodActivationRoutingGroup()
        if group is not None:
            wrapper = ET.SubElement(element, "METHOD-ACTIVATION-ROUTING-GROUPS")
            self.setPduActivationRoutingGroup(wrapper, group)

    def writeConsumedServiceInstance(self, element: ET.Element, instance: ConsumedServiceInstance):
        if instance is not None:
            child_element = ET.SubElement(element, "CONSUMED-SERVICE-INSTANCE")
            self.writeIdentifiable(child_element, instance)
            refs = instance.getAllowedServiceProviderRefs()
            if len(refs) > 0:
                wrapper = ET.SubElement(child_element, "ALLOWED-SERVICE-PROVIDERS")
                for ref in refs:
                    cond_tag = ET.SubElement(wrapper, "NETWORK-ENDPOINT-REF-CONDITIONAL")
                    self.setChildElementOptionalRefType(cond_tag, "NETWORK-ENDPOINT-REF", ref)
            self.setChildElementOptionalBooleanValue(child_element, "AUTO-REQUIRE", instance.getAutoRequire())
            self.setSomeipServiceVersions(child_element, "BLOCKLISTED-VERSIONS", instance.getBlocklistedVersions())
            self.setTagWithOptionalValues(child_element, "CAPABILITY-RECORDS", instance.getCapabilityRecords())
            self.writeConsumedServiceInstanceConsumedEventGroups(child_element, instance)
            ref = instance.getEventMulticastSubscriptionAddressRef()
            if ref is not None:
                wrapper = ET.SubElement(child_element, "EVENT-MULTICAST-SUBSCRIPTION-ADDRESSS")
                cond_tag = ET.SubElement(wrapper, "APPLICATION-ENDPOINT-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(cond_tag, "APPLICATION-ENDPOINT-REF", ref)
            self.setChildElementOptionalLiteral(child_element, "INSTANCE-IDENTIFIER", instance.getInstanceIdentifier())
            refs = instance.getLocalUnicastAddressRefs()
            if len(refs) > 0:
                wrapper = ET.SubElement(child_element, "LOCAL-UNICAST-ADDRESSS")
                for ref in refs:
                    cond_tag = ET.SubElement(wrapper, "APPLICATION-ENDPOINT-REF-CONDITIONAL")
                    self.setChildElementOptionalRefType(cond_tag, "APPLICATION-ENDPOINT-REF", ref)
            self.setChildElementOptionalPositiveInteger(child_element, "MAJOR-VERSION", instance.getMajorVersion())
            self.writeAbstractServiceInstanceMethodActivationRoutingGroups(child_element, instance)
            self.setChildElementOptionalLiteral(child_element, "MINOR-VERSION", instance.getMinorVersion())
            self.setChildElementOptionalRefType(child_element, "PROVIDED-SERVICE-INSTANCE-REF", instance.getProvidedServiceInstanceRef())
            refs = instance.getRemoteUnicastAddressRefs()
            if len(refs) > 0:
                wrapper = ET.SubElement(child_element, "REMOTE-UNICAST-ADDRESSS")
                for ref in refs:
                    cond_tag = ET.SubElement(wrapper, "APPLICATION-ENDPOINT-REF-CONDITIONAL")
                    self.setChildElementOptionalRefType(cond_tag, "APPLICATION-ENDPOINT-REF", ref)
            refs = instance.getRoutingGroupRefs()
            if len(refs) > 0:
                routing_groups_element = ET.SubElement(child_element, "ROUTING-GROUP-REFS")
                for ref in refs:
                    self.setChildElementOptionalRefType(routing_groups_element, "ROUTING-GROUP-REF", ref)
            self.setSdClientConfig(child_element, "SD-CLIENT-CONFIG", instance.getSdClientConfig())
            ref = instance.getSdClientTimerConfigRef()
            if ref is not None:
                wrapper = ET.SubElement(child_element, "SD-CLIENT-TIMER-CONFIGS")
                cond_tag = ET.SubElement(wrapper, "SOMEIP-SD-CLIENT-SERVICE-INSTANCE-CONFIG-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(cond_tag, "SOMEIP-SD-CLIENT-SERVICE-INSTANCE-CONFIG-REF", ref)
            self.setChildElementOptionalPositiveInteger(child_element, "SERVICE-IDENTIFIER", instance.getServiceIdentifier())
            self.setChildElementOptionalLiteral(child_element, "VERSION-DRIVEN-FIND-BEHAVIOR", instance.getVersionDrivenFindBehavior())

    def writeSocketAddressApplicationEndpointConsumedServiceInstances(self, element: ET.Element, end_point: ApplicationEndpoint):
        instances = end_point.getConsumedServiceInstances()
        if len(instances) > 0:
            child_element = ET.SubElement(element, "CONSUMED-SERVICE-INSTANCES")
            for instance in instances:
                if isinstance(instance, ConsumedServiceInstance):
                    self.writeConsumedServiceInstance(child_element, instance)
                else:
                    self.notImplemented("Unsupported ConsumedServiceInstances <%s>" % type(instance))

    def setInitialSdDelayConfig(self, element: ET.Element, key: str, config: InitialSdDelayConfig):
        if config is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalTimeValue(child_element, "INITIAL-DELAY-MAX-VALUE", config.getInitialDelayMaxValue())
            self.setChildElementOptionalTimeValue(child_element, "INITIAL-DELAY-MIN-VALUE", config.getInitialDelayMinValue())
            self.setChildElementOptionalTimeValue(child_element, "INITIAL-REPETITIONS-BASE-DELAY", config.getInitialRepetitionsBaseDelay())
            self.setChildElementOptionalPositiveInteger(child_element, "INITIAL-REPETITIONS-MAX", config.getInitialRepetitionsMax())

    def setSdServerConfig(self, element: ET.Element, key: str, config: SdServerConfig):
        if config is not None:
            child_element = ET.SubElement(element, key)
            self.setInitialSdDelayConfig(child_element, "INITIAL-OFFER-BEHAVIOR", config.getInitialOfferBehavior())
            self.setChildElementOptionalTimeValue(child_element, "OFFER-CYCLIC-DELAY", config.getOfferCyclicDelay())
            self.setRequestResponseDelay(child_element, "REQUEST-RESPONSE-DELAY", config.getRequestResponseDelay())
            self.setChildElementOptionalPositiveInteger(child_element, "SERVER-SERVICE-MAJOR-VERSION", config.getServerServiceMajorVersion())
            self.setChildElementOptionalPositiveInteger(child_element, "SERVER-SERVICE-MINOR-VERSION", config.getServerServiceMinorVersion())
            self.setChildElementOptionalPositiveInteger(child_element, "TTL", config.getTtl())

    def setTagWithOptionalValue(self, element: ET.Element, key: str, tag: TagWithOptionalValue):
        if tag is not None:
            child_element = ET.SubElement(element, key)
            self.writeARObjectAttributes(child_element, tag)
            self.setChildElementOptionalString(child_element, "KEY", tag.getKey())
            self.setChildElementOptionalIntegerValue(child_element, "SEQUENCE-OFFSET", tag.getSequenceOffset())
            self.setChildElementOptionalString(child_element, "VALUE", tag.getValue())

    def setTagWithOptionalValues(self, element: ET.Element, key: str, tags: List[TagWithOptionalValue]):
        if len(tags) > 0:
            wrapper = ET.SubElement(element, key)
            for tag in tags:
                self.setTagWithOptionalValue(wrapper, "TAG-WITH-OPTIONAL-VALUE", tag)

    def writeSomeipSdClientServiceInstanceConfig(self, element: ET.Element, config: SomeipSdClientServiceInstanceConfig):
        self.logger.debug("Write SomeipSdClientServiceInstanceConfig <%s>" % config.getShortName())
        child_element = ET.SubElement(element, "SOME-IP-SD-CLIENT-SERVICE-INSTANCE-CONFIG")
        self.writeIdentifiable(child_element, config)
        self.setInitialSdDelayConfig(child_element, "INITIAL-FIND-BEHAVIOR", config.getInitialFindBehavior())
        self.setChildElementOptionalPositiveInteger(child_element, "PRIORITY", config.getPriority())
        self.setChildElementOptionalPositiveInteger(child_element, "SERVICE-FIND-TIME-TO-LIVE", config.getServiceFindTimeToLive())

    def writeSomeipSdClientEventGroupTimingConfig(self, element: ET.Element, config: SomeipSdClientEventGroupTimingConfig):
        self.logger.debug("Write SomeipSdClientEventGroupTimingConfig <%s>" % config.getShortName())
        child_element = ET.SubElement(element, "SOME-IP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG")
        self.writeIdentifiable(child_element, config)
        self.setRequestResponseDelay(child_element, "REQUEST-RESPONSE-DELAY", config.getRequestResponseDelay())
        self.setChildElementOptionalTimeValue(child_element, "SUBSCRIBE-EVENTGROUP-RETRY-DELAY", config.getSubscribeEventgroupRetryDelay())
        self.setChildElementOptionalPositiveInteger(child_element, "SUBSCRIBE-EVENTGROUP-RETRY-MAX", config.getSubscribeEventgroupRetryMax())
        self.setChildElementOptionalPositiveInteger(child_element, "TIME-TO-LIVE", config.getTimeToLive())

    def writeSomeipSdServerEventGroupTimingConfig(self, element: ET.Element, config: SomeipSdServerEventGroupTimingConfig):
        self.logger.debug("Write SomeipSdServerEventGroupTimingConfig <%s>" % config.getShortName())
        child_element = ET.SubElement(element, "SOME-IP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG")
        self.writeIdentifiable(child_element, config)
        self.setRequestResponseDelay(child_element, "REQUEST-RESPONSE-DELAY", config.getRequestResponseDelay())

    def writeEventHandler(self, element: ET.Element, handler: EventHandler):
        if handler is not None:
            child_element = ET.SubElement(element, "EVENT-HANDLER")
            self.writeIdentifiable(child_element, handler)

            refs = handler.getConsumedEventGroupRefs()
            if len(refs) > 0:
                refs_tag = ET.SubElement(child_element, "CONSUMED-EVENT-GROUP-REFS")
                for ref in refs:
                    self.setChildElementOptionalRefType(refs_tag, "CONSUMED-EVENT-GROUP-REF", ref)

            self.setChildElementOptionalPositiveInteger(child_element, "EVENT-GROUP-IDENTIFIER", handler.getEventGroupIdentifier())

            ref = handler.getEventMulticastAddressRef()
            if ref is not None:
                wrapper = ET.SubElement(child_element, "EVENT-MULTICAST-ADDRESSS")
                cond_tag = ET.SubElement(wrapper, "APPLICATION-ENDPOINT-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(cond_tag, "APPLICATION-ENDPOINT-REF", ref)

            self.setChildElementOptionalPositiveInteger(child_element, "MULTICAST-THRESHOLD", handler.getMulticastThreshold())

            groups = handler.getPduActivationRoutingGroups()
            if len(groups) > 0:
                groups_tag = ET.SubElement(child_element, "PDU-ACTIVATION-ROUTING-GROUPS")
                for group in groups:
                    self.setPduActivationRoutingGroup(groups_tag, group)

            refs = handler.getRoutingGroupRefs()
            if len(refs) > 0:
                refs_tag = ET.SubElement(child_element, "ROUTING-GROUP-REFS")
                for ref in refs:
                    self.setChildElementOptionalRefType(refs_tag, "ROUTING-GROUP-REF", ref)
            self.setSdServerConfig(child_element, "SD-SERVER-CONFIG", handler.getSdServerConfig())

            ref = handler.getSdServerEgTimingConfigRef()
            if ref is not None:
                wrapper = ET.SubElement(child_element, "SD-SERVER-EG-TIMING-CONFIGS")
                cond_tag = ET.SubElement(wrapper, "SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(cond_tag, "SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG-REF", ref)

    def writeProvidedServiceInstanceEventHandlers(self, element: ET.Element, instance: ProvidedServiceInstance):
        handlers = instance.getEventHandlers()
        if len(handlers) > 0:
            child_element = ET.SubElement(element, "EVENT-HANDLERS")
            for handler in handlers:
                if isinstance(handler, EventHandler):
                    self.writeEventHandler(child_element, handler)
                else:
                    self.notImplemented("Unsupported Event Handler <%s>" % type(handler))

    def writeProvidedServiceInstance(self, element: ET.Element, instance: ProvidedServiceInstance):
        if instance is not None:
            child_element = ET.SubElement(element, "PROVIDED-SERVICE-INSTANCE")
            self.writeIdentifiable(child_element, instance)
            self.setTagWithOptionalValues(child_element, "CAPABILITY-RECORDS", instance.getCapabilityRecords())
            self.writeProvidedServiceInstanceEventHandlers(child_element, instance)
            self.setChildElementOptionalPositiveInteger(child_element, "INSTANCE-IDENTIFIER", instance.getInstanceIdentifier())
            self.setChildElementOptionalPositiveInteger(child_element, "LOAD-BALANCING-PRIORITY", instance.getLoadBalancingPriority())
            self.setChildElementOptionalPositiveInteger(child_element, "LOAD-BALANCING-WEIGHT", instance.getLoadBalancingWeight())
            refs = instance.getLocalUnicastAddressRefs()
            if len(refs) > 0:
                wrapper = ET.SubElement(child_element, "LOCAL-UNICAST-ADDRESSS")
                for ref in refs:
                    cond_tag = ET.SubElement(wrapper, "APPLICATION-ENDPOINT-REF-CONDITIONAL")
                    self.setChildElementOptionalRefType(cond_tag, "APPLICATION-ENDPOINT-REF", ref)
            self.setChildElementOptionalPositiveInteger(child_element, "MAJOR-VERSION", instance.getMajorVersion())
            self.writeAbstractServiceInstanceMethodActivationRoutingGroups(child_element, instance)
            self.setChildElementOptionalPositiveInteger(child_element, "MINOR-VERSION", instance.getMinorVersion())
            self.setChildElementOptionalPositiveInteger(child_element, "PRIORITY", instance.getPriority())
            refs = instance.getRemoteMulticastSubscriptionAddressRefs()
            if len(refs) > 0:
                wrapper = ET.SubElement(child_element, "REMOTE-MULTICAST-SUBSCRIPTION-ADDRESSS")
                for ref in refs:
                    cond_tag = ET.SubElement(wrapper, "APPLICATION-ENDPOINT-REF-CONDITIONAL")
                    self.setChildElementOptionalRefType(cond_tag, "APPLICATION-ENDPOINT-REF", ref)
            refs = instance.getRemoteUnicastAddressRefs()
            if len(refs) > 0:
                wrapper = ET.SubElement(child_element, "REMOTE-UNICAST-ADDRESSS")
                for ref in refs:
                    cond_tag = ET.SubElement(wrapper, "APPLICATION-ENDPOINT-REF-CONDITIONAL")
                    self.setChildElementOptionalRefType(cond_tag, "APPLICATION-ENDPOINT-REF", ref)
            refs = instance.getRoutingGroupRefs()
            if len(refs) > 0:
                routing_groups_element = ET.SubElement(child_element, "ROUTING-GROUP-REFS")
                for ref in refs:
                    self.setChildElementOptionalRefType(routing_groups_element, "ROUTING-GROUP-REF", ref)
            self.setSdServerConfig(child_element, "SD-SERVER-CONFIG", instance.getSdServerConfig())
            ref = instance.getSdServerTimerConfigRef()
            if ref is not None:
                wrapper = ET.SubElement(child_element, "SD-SERVER-TIMER-CONFIGS")
                cond_tag = ET.SubElement(wrapper, "SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(cond_tag, "SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG-REF", ref)
            refs = instance.getAllowedServiceConsumerRefs()
            if len(refs) > 0:
                wrapper = ET.SubElement(child_element, "ALLOWED-SERVICE-CONSUMERS")
                for ref in refs:
                    cond_tag = ET.SubElement(wrapper, "NETWORK-ENDPOINT-REF-CONDITIONAL")
                    self.setChildElementOptionalRefType(cond_tag, "NETWORK-ENDPOINT-REF", ref)
            self.setChildElementOptionalBooleanValue(child_element, "AUTO-AVAILABLE", instance.getAutoAvailable())
            self.setChildElementOptionalPositiveInteger(child_element, "SERVICE-IDENTIFIER", instance.getServiceIdentifier())

    def writeSocketAddressApplicationEndpointProvidedServiceInstance(self, element: ET.Element, end_point: ApplicationEndpoint):
        instances = end_point.getProvidedServiceInstances()
        if len(instances) > 0:
            child_element = ET.SubElement(element, "PROVIDED-SERVICE-INSTANCES")
            for instance in instances:
                if isinstance(instance, ProvidedServiceInstance):
                    self.writeProvidedServiceInstance(child_element, instance)
                else:
                    self.notImplemented("Unsupported ConsumedServiceInstances <%s>" % type(instance))

    def writeSocketAddressApplicationEndpoint(self, element: ET.Element, address: SocketAddress):
        end_point = address.getApplicationEndpoint()
        if end_point is not None:
            child_element = ET.SubElement(element, "APPLICATION-ENDPOINT")
            self.writeIdentifiable(child_element, end_point)
            self.writeSocketAddressApplicationEndpointConsumedServiceInstances(child_element, end_point)
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-NUMBER-OF-CONNECTIONS", end_point.getMaxNumberOfConnections())
            self.setChildElementOptionalRefType(child_element, "NETWORK-ENDPOINT-REF", end_point.getNetworkEndpointRef())
            self.setChildElementOptionalPositiveInteger(child_element, "PRIORITY", end_point.getPriority())
            self.writeSocketAddressApplicationEndpointProvidedServiceInstance(child_element, end_point)
            self.setChildElementOptionalRefType(child_element, "TLS-CRYPTO-MAPPING-REF", end_point.getTlsCryptoMappingRef())
            self.writeTransportProtocolConfiguration(child_element, end_point.getTpConfiguration())

    def writeSocketAddressMulticastConnectorRefs(self, element: ET.Element, address: SocketAddress):
        refs = address.getMulticastConnectorRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "MULTICAST-CONNECTOR-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "MULTICAST-CONNECTOR-REF", ref)

    def writeSocketAddress(self, element: ET.Element, address: SocketAddress):
        child_element = ET.SubElement(element, "SOCKET-ADDRESS")
        self.writeIdentifiable(child_element, address)
        self.setChildElementOptionalRefType(child_element, "ALLOWED-I-PV-6-EXT-HEADERS-REF", address.getAllowedIPv6ExtHeadersRef())
        self.setChildElementOptionalRefType(child_element, "ALLOWED-TCP-OPTIONS-REF", address.getAllowedTcpOptionsRef())
        self.writeSocketAddressApplicationEndpoint(child_element, address)
        self.setChildElementOptionalRefType(child_element, "CONNECTOR-REF", address.getConnectorRef())
        self.setChildElementOptionalPositiveInteger(child_element, "DIFFERENTIATED-SERVICE-FIELD", address.getDifferentiatedServiceField())
        self.setChildElementOptionalPositiveInteger(child_element, "FLOW-LABEL", address.getFlowLabel())
        self.writeSocketAddressMulticastConnectorRefs(child_element, address)
        self.setChildElementOptionalBooleanValue(child_element, "PATH-MTU-DISCOVERY-ENABLED", address.getPathMtuDiscoveryEnabled())
        self.setChildElementOptionalPositiveInteger(child_element, "PDU-COLLECTION-MAX-BUFFER-SIZE", address.getPduCollectionMaxBufferSize())
        self.setChildElementOptionalTimeValue(child_element, "PDU-COLLECTION-TIMEOUT", address.getPduCollectionTimeout())
        connections = address.getStaticSocketConnections()
        if len(connections) > 0:
            wrapper = ET.SubElement(child_element, "STATIC-SOCKET-CONNECTIONS")
            for connection in connections:
                self.setStaticSocketConnection(wrapper, connection)
        self.setChildElementOptionalLiteral(child_element, "UDP-CHECKSUM-HANDLING", address.getUdpChecksumHandling())

    def writeSoAdConfigSocketAddresses(self, element: ET.Element, config: SoAdConfig):
        addresses = config.getSocketAddresses()
        if len(addresses) > 0:
            child_element = ET.SubElement(element, "SOCKET-ADDRESSS")
            for address in addresses:
                if isinstance(address, SocketAddress):
                    self.writeSocketAddress(child_element, address)
                else:
                    self.notImplemented("Unsupported Socket Address <%s>" % type(address))

    def writeSoAdConfigConnections(self, element: ET.Element, config: SoAdConfig):
        connections = config.getConnections()
        if len(connections) > 0:
            child_element = ET.SubElement(element, "CONNECTIONS")
            for connection in connections:
                if isinstance(connection, SocketConnection):
                    self.setSocketConnection(child_element, connection)
                else:
                    self.notImplemented("Unsupported Connection <%s>" % type(connection))

    def writeSoAdConfig(self, element: ET.Element, key: str, config: SoAdConfig):
        if config is not None:
            child_element = ET.SubElement(element, key)
            self.writeSoAdConfigConnections(child_element, config)
            self.writeSoAdConfigConnectionBundles(child_element, config)
            self.writeSoAdConfigSocketAddresses(child_element, config)

    def writeEthernetPhysicalChannelVlan(self, element: ET.Element, channel: EthernetPhysicalChannel):
        vlan = channel.getVlan()
        if vlan is not None:
            child_element = ET.SubElement(element, "VLAN")
            self.writeIdentifiable(child_element, vlan)
            self.setChildElementOptionalPositiveInteger(child_element, "VLAN-IDENTIFIER", vlan.getVlanIdentifier())

    def writeEthernetPhysicalChannel(self, element: ET.Element, channel: EthernetPhysicalChannel):
        self.logger.debug("Set EthernetPhysicalChannel %s" % channel.getShortName())
        child_element = ET.SubElement(element, "ETHERNET-PHYSICAL-CHANNEL")
        self.writePhysicalChannel(child_element, channel)
        self.writeEthernetPhysicalChannelNetworkEndPoints(child_element, channel.getNetworkEndpoints())
        self.writeSoAdConfig(child_element, "SO-AD-CONFIG", channel.getSoAdConfig())
        self.writeEthernetPhysicalChannelVlan(child_element, channel)

    def writeFlexrayPhysicalChannel(self, element: ET.Element, channel: FlexrayPhysicalChannel):
        self.logger.debug("Set FlexrayPhysicalChannel %s" % channel.getShortName())
        child_element = ET.SubElement(element, "FLEXRAY-PHYSICAL-CHANNEL")
        self.writePhysicalChannel(child_element, channel)
        self.setChildElementOptionalLiteral(child_element, "CHANNEL-NAME", channel.getChannelName())

    def writeCommunicationClusterPhysicalChannels(self, element: ET.Element, cluster: CommunicationCluster):
        channels = cluster.getPhysicalChannels()
        if len(channels) > 0:
            child_element = ET.SubElement(element, "PHYSICAL-CHANNELS")
            for channel in channels:
                if isinstance(channel, CanPhysicalChannel):
                    self.writeCanPhysicalChannel(child_element, channel)
                elif isinstance(channel, LinPhysicalChannel):
                    self.writeLinPhysicalChannel(child_element, channel)
                elif isinstance(channel, EthernetPhysicalChannel):
                    self.writeEthernetPhysicalChannel(child_element, channel)
                elif isinstance(channel, FlexrayPhysicalChannel):
                    self.writeFlexrayPhysicalChannel(child_element, channel)
                else:
                    self.notImplemented("Unsupported Physical Channel <%s>" % type(channel))

    def writeCommunicationCluster(self, element: ET.Element, cluster: CommunicationCluster):
        self.setChildElementOptionalNumericalValue(element, "BAUDRATE", cluster.getBaudrate())
        self.writeCommunicationClusterPhysicalChannels(element, cluster)
        self.setChildElementOptionalLiteral(element, "PROTOCOL-NAME", cluster.getProtocolName())
        self.setChildElementOptionalLiteral(element, "PROTOCOL-VERSION", cluster.getProtocolVersion())

    def setCanClusterBusOffRecovery(self, element: ET.Element, key: str, recovery: CanClusterBusOffRecovery):
        if recovery is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalPositiveInteger(child_element, "BOR-COUNTER-L-1-TO-L-2", recovery.getBorCounterL1ToL2())
            self.setChildElementOptionalTimeValue(child_element, "BOR-TIME-L-1", recovery.getBorTimeL1())
            self.setChildElementOptionalTimeValue(child_element, "BOR-TIME-L-2", recovery.getBorTimeL2())

    def writeAbstractCanCluster(self, element: ET.Element, cluster: AbstractCanCluster):
        self.setCanClusterBusOffRecovery(element, "BUS-OFF-RECOVERY", cluster.getBusOffRecovery())
        self.setChildElementOptionalNumericalValue(element, "CAN-FD-BAUDRATE", cluster.getCanFdBaudrate())
        self.setChildElementOptionalNumericalValue(element, "CAN-XL-BAUDRATE", cluster.getCanXlBaudrate())

    def writeLinCluster(self, element: ET.Element, cluster: LinCluster):
        if cluster is not None:
            self.logger.debug("LinCluster %s" % cluster.getShortName())
            child_element = ET.SubElement(element, "LIN-CLUSTER")
            self.writeIdentifiable(child_element, cluster)

            child_element = ET.SubElement(child_element, "LIN-CLUSTER-VARIANTS")
            child_element = ET.SubElement(child_element, "LIN-CLUSTER-CONDITIONAL")
            self.writeCommunicationCluster(child_element, cluster)

    def writeCanCluster(self, element: ET.Element, cluster: CanCluster):
        if cluster is not None:
            self.logger.debug("CanCluster %s" % cluster.getShortName())
            child_element = ET.SubElement(element, "CAN-CLUSTER")
            self.writeIdentifiable(child_element, cluster)

            child_element = ET.SubElement(child_element, "CAN-CLUSTER-VARIANTS")
            child_element = ET.SubElement(child_element, "CAN-CLUSTER-CONDITIONAL")
            self.writeCommunicationCluster(child_element, cluster)
            self.writeAbstractCanCluster(child_element, cluster)

    def writeFlexrayCluster(self, element: ET.Element, cluster: FlexrayCluster):
        if cluster is not None:
            self.logger.debug("Write FlexrayCluster <%s>" % cluster.getShortName())
            child_element = ET.SubElement(element, "FLEXRAY-CLUSTER")
            self.writeIdentifiable(child_element, cluster)

            child_element = ET.SubElement(child_element, "FLEXRAY-CLUSTER-VARIANTS")
            child_element = ET.SubElement(child_element, "FLEXRAY-CLUSTER-CONDITIONAL")
            self.writeCommunicationCluster(child_element, cluster)

            self.setChildElementOptionalIntegerValue(child_element, "ACTION-POINT-OFFSET", cluster.getActionPointOffset())
            self.setChildElementOptionalTimeValue(child_element, "BIT", cluster.getBit())
            self.setChildElementOptionalIntegerValue(child_element, "CAS-RX-LOW-MAX", cluster.getCasRxLowMax())
            self.setChildElementOptionalIntegerValue(child_element, "COLD-START-ATTEMPTS", cluster.getColdStartAttempts())
            self.setChildElementOptionalTimeValue(child_element, "CYCLE", cluster.getCycle())
            self.setChildElementOptionalIntegerValue(child_element, "CYCLE-COUNT-MAX", cluster.getCycleCountMax())
            self.setChildElementOptionalBooleanValue(child_element, "DETECT-NIT-ERROR", cluster.getDetectNitError())
            self.setChildElementOptionalIntegerValue(child_element, "DYNAMIC-SLOT-IDLE-PHASE", cluster.getDynamicSlotIdlePhase())
            self.setChildElementOptionalIntegerValue(child_element, "IGNORE-AFTER-TX", cluster.getIgnoreAfterTx())
            self.setChildElementOptionalIntegerValue(child_element, "LISTEN-NOISE", cluster.getListenNoise())
            self.setChildElementOptionalIntegerValue(child_element, "MACRO-PER-CYCLE", cluster.getMacroPerCycle())
            self.setChildElementOptionalTimeValue(child_element, "MACROTICK-DURATION", cluster.getMacrotickDuration())
            self.setChildElementOptionalIntegerValue(child_element, "MAX-WITHOUT-CLOCK-CORRECTION-FATAL", cluster.getMaxWithoutClockCorrectionFatal())
            self.setChildElementOptionalIntegerValue(child_element, "MAX-WITHOUT-CLOCK-CORRECTION-PASSIVE", cluster.getMaxWithoutClockCorrectionPassive())  # noqa E501
            self.setChildElementOptionalIntegerValue(child_element, "MINISLOT-ACTION-POINT-OFFSET", cluster.getMinislotActionPointOffset())
            self.setChildElementOptionalIntegerValue(child_element, "MINISLOT-DURATION", cluster.getMinislotDuration())
            self.setChildElementOptionalIntegerValue(child_element, "NETWORK-IDLE-TIME", cluster.getNetworkIdleTime())
            self.setChildElementOptionalIntegerValue(child_element, "NETWORK-MANAGEMENT-VECTOR-LENGTH", cluster.getNetworkManagementVectorLength())
            self.setChildElementOptionalIntegerValue(child_element, "NUMBER-OF-MINISLOTS", cluster.getNumberOfMinislots())
            self.setChildElementOptionalIntegerValue(child_element, "NUMBER-OF-STATIC-SLOTS", cluster.getNumberOfStaticSlots())
            self.setChildElementOptionalIntegerValue(child_element, "OFFSET-CORRECTION-START", cluster.getOffsetCorrectionStart())
            self.setChildElementOptionalIntegerValue(child_element, "PAYLOAD-LENGTH-STATIC", cluster.getPayloadLengthStatic())
            self.setChildElementOptionalIntegerValue(child_element, "SAFETY-MARGIN", cluster.getSafetyMargin())
            self.setChildElementOptionalTimeValue(child_element, "SAMPLE-CLOCK-PERIOD", cluster.getSampleClockPeriod())
            self.setChildElementOptionalIntegerValue(child_element, "STATIC-SLOT-DURATION", cluster.getStaticSlotDuration())
            self.setChildElementOptionalIntegerValue(child_element, "SYMBOL-WINDOW", cluster.getSymbolWindow())
            self.setChildElementOptionalIntegerValue(child_element, "SYMBOL-WINDOW-ACTION-POINT-OFFSET", cluster.getSymbolWindowActionPointOffset())
            self.setChildElementOptionalIntegerValue(child_element, "SYNC-FRAME-ID-COUNT-MAX", cluster.getSyncFrameIdCountMax())
            self.setChildElementOptionalFloatValue(child_element, "TRANCEIVER-STANDBY-DELAY", cluster.getTranceiverStandbyDelay())  # noqa E501
            self.setChildElementOptionalIntegerValue(child_element, "TRANSMISSION-START-SEQUENCE-DURATION", cluster.getTransmissionStartSequenceDuration())  # noqa E501
            self.setChildElementOptionalIntegerValue(child_element, "WAKEUP-RX-IDLE", cluster.getWakeupRxIdle())
            self.setChildElementOptionalIntegerValue(child_element, "WAKEUP-RX-LOW", cluster.getWakeupRxLow())
            self.setChildElementOptionalIntegerValue(child_element, "WAKEUP-RX-WINDOW", cluster.getWakeupRxWindow())
            self.setChildElementOptionalIntegerValue(child_element, "WAKEUP-TX-ACTIVE", cluster.getWakeupTxActive())
            self.setChildElementOptionalIntegerValue(child_element, "WAKEUP-TX-IDLE", cluster.getWakeupTxIdle())

    def writeCollectionElementRefs(self, element: ET.Element, collection: Collection):
        refs = collection.getElementRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "ELEMENT-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "ELEMENT-REF", ref)

    def writeCollectionSourceElementRefs(self, element: ET.Element, collection: Collection):
        refs = collection.getSourceElementRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "SOURCE-ELEMENT-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "SOURCE-ELEMENT-REF", ref)

    def writeCollection(self, element: ET.Element, collection: Collection):
        if collection is not None:
            child_element = ET.SubElement(element, "COLLECTION")
            self.writeARElement(child_element, collection)
            self.setChildElementOptionalLiteral(child_element, "AUTO-COLLECT", collection.getAutoCollect())
            self.setChildElementOptionalLiteral(child_element, "ELEMENT-ROLE", collection.getElementRole())
            self.writeCollectionElementRefs(child_element, collection)
            self.writeCollectionSourceElementRefs(child_element, collection)

    def writeKeywordClassifications(self, element: ET.Element, keyword: Keyword):
        classifications = keyword.getClassifications()
        if len(classifications) > 0:
            child_element = ET.SubElement(element, "CLASSIFICATIONS")
            for classification in classifications:
                self.setChildElementOptionalLiteral(child_element, "CLASSIFICATION", classification)

    def writeKeyword(self, element: ET.Element, keyword: Keyword):
        if keyword is not None:
            # self.logger.debug("Write Keyword <%s>" % keyword.getShortName())
            child_element = ET.SubElement(element, "KEYWORD")
            self.writeIdentifiable(child_element, keyword)
            self.setChildElementOptionalLiteral(child_element, "ABBR-NAME", keyword.getAbbrName())
            self.writeKeywordClassifications(child_element, keyword)

    def writeKeywordSetKeywords(self, element: ET.Element, keyword_set: KeywordSet):
        keywords = keyword_set.getKeywords()
        if len(keywords) > 0:
            child_element = ET.SubElement(element, "KEYWORDS")
            for keyword in keywords:
                if isinstance(keyword, Keyword):
                    self.writeKeyword(child_element, keyword)
                else:
                    self.notImplemented("Unsupported Keyword <%s>" % type(keyword))

    def writeKeywordSet(self, element: ET.Element, keyword_set: KeywordSet):
        if keyword_set is not None:
            self.logger.debug("Write KeywordSet <%s>" % keyword_set.getShortName())
            child_element = ET.SubElement(element, "KEYWORD-SET")
            self.writeARElement(child_element, keyword_set)
            self.writeKeywordSetKeywords(child_element, keyword_set)

    def writePortPrototypeBlueprint(self, element: ET.Element, blueprint: PortPrototypeBlueprint):
        if blueprint is not None:
            self.logger.debug("Write PortPrototypeBlueprint <%s>" % blueprint.getShortName())
            child_element = ET.SubElement(element, "PORT-PROTOTYPE-BLUEPRINT")
            self.writeARElement(child_element, blueprint)
            self.setChildElementOptionalRefType(child_element, "INTERFACE-REF", blueprint.getInterfaceRef())

    def writeModeDeclarationMappingFirstModeRefs(self, element: ET.Element, mapping: ModeDeclarationMapping):
        ref_links = mapping.getFirstModeRefs()
        if len(ref_links) > 0:
            child_element = ET.SubElement(element, "FIRST-MODE-REFS")
            for ref_link in ref_links:
                self.setChildElementOptionalRefType(child_element, "FIRST-MODE-REF", ref_link)

    def writeModeDeclarationMapping(self, element: ET.Element, mapping: ModeDeclarationMapping):
        # self.logger.debug("Read ModeDeclarationMapping <%s>" % mapping.getShortName())
        if mapping is not None:
            child_element = ET.SubElement(element, "MODE-DECLARATION-MAPPING")
            self.writeIdentifiable(child_element, mapping)
            self.writeModeDeclarationMappingFirstModeRefs(child_element, mapping)
            self.setChildElementOptionalRefType(child_element, "SECOND-MODE-REF", mapping.getSecondModeRef())

    def writeModeDeclarationMappingSetModeDeclarationMappings(self, element: ET.Element, mapping_set: ModeDeclarationMappingSet):
        mappings = mapping_set.getModeDeclarationMappings()
        if len(mappings) > 0:
            child_element = ET.SubElement(element, "MODE-DECLARATION-MAPPINGS")
            for mapping in mappings:
                if isinstance(mapping, ModeDeclarationMapping):
                    self.writeModeDeclarationMapping(child_element, mapping)
                else:
                    self.notImplemented("Unsupported ModeDeclarationMapping <%s>" % type(mapping))

    def writeModeDeclarationMappingSet(self, element: ET.Element, mapping_set: ModeDeclarationMappingSet):
        if mapping_set is not None:
            self.logger.debug("Write ModeDeclarationMappingSet <%s>" % mapping_set.getShortName())
            child_element = ET.SubElement(element, "MODE-DECLARATION-MAPPING-SET")
            self.writeARElement(child_element, mapping_set)
            self.writeModeDeclarationMappingSetModeDeclarationMappings(element, mapping_set)

    def writeEcucDefinitionElement(self, element: ET.Element, def_element: EcucDefinitionElement):
        self.writeARElement(element, def_element)
        self.writeEcucConditionSpecification(element, def_element.getEcucCond())
        self.writeEcucValidationConditions(element, def_element.getEcucValidationConds())
        self.setChildElementOptionalPositiveInteger(element, "LOWER-MULTIPLICITY", def_element.getLowerMultiplicity())
        self.setChildElementOptionalPositiveInteger(element, "UPPER-MULTIPLICITY", def_element.getUpperMultiplicity())
        self.setChildElementOptionalLiteral(element, "SCOPE", def_element.getScope())

    def writeEcucModuleDefSupportedConfigVariants(self, element: ET.Element, module_def: EcucModuleDef):
        variants = module_def.getSupportedConfigVariants()
        if len(variants) > 0:
            child_element = ET.SubElement(element, "SUPPORTED-CONFIG-VARIANTS")
            for variant in variants:
                self.setChildElementOptionalLiteral(child_element, "SUPPORTED-CONFIG-VARIANT", variant)

    def writeEcucAbstractConfigurationClass(self, element: ET.Element, cfg_class: EcucAbstractConfigurationClass):
        self.writeARObjectAttributes(element, cfg_class)
        self.setChildElementOptionalLiteral(element, "CONFIG-CLASS", cfg_class.getConfigClass())
        self.setChildElementOptionalLiteral(element, "CONFIG-VARIANT", cfg_class.getConfigVariant())

    def writeEcucMultiplicityConfigurationClass(self, element: ET.Element, cfg_class: EcucMultiplicityConfigurationClass):
        if cfg_class is not None:
            child_element = ET.SubElement(element, "ECUC-MULTIPLICITY-CONFIGURATION-CLASS")
            self.writeEcucAbstractConfigurationClass(child_element, cfg_class)

    def setEcucMultiplicityConfigClasses(self, element: ET.Element, cfg_classes: List[EcucMultiplicityConfigurationClass]):
        if len(cfg_classes) > 0:
            child_element = ET.SubElement(element, "MULTIPLICITY-CONFIG-CLASSES")
            for cfg_class in cfg_classes:
                if isinstance(cfg_class, EcucMultiplicityConfigurationClass):
                    self.writeEcucMultiplicityConfigurationClass(child_element, cfg_class)
                else:
                    self.notImplemented("Unsupported MultiplicityConfigClass <%s>" % type(cfg_class))

    def writeEcucValueConfigurationClass(self, element: ET.Element, cfg_class: EcucValueConfigurationClass):
        if cfg_class is not None:
            child_element = ET.SubElement(element, "ECUC-VALUE-CONFIGURATION-CLASS")
            self.writeEcucAbstractConfigurationClass(child_element, cfg_class)

    def setEcuValueConfigurationClasses(self, element: ET.Element, cfg_classes: List[EcucValueConfigurationClass]):
        if len(cfg_classes) > 0:
            child_element = ET.SubElement(element, "VALUE-CONFIG-CLASSES")
            for cfg_class in cfg_classes:
                if isinstance(cfg_class, EcucValueConfigurationClass):
                    self.writeEcucValueConfigurationClass(child_element, cfg_class)
                else:
                    self.notImplemented("Unsupported ValueConfigClass <%s>" % type(cfg_class))

    def writeEcucCommonAttributes(self, element: ET.Element, common_attrs: EcucCommonAttributes):
        self.writeEcucDefinitionElement(element, common_attrs)
        self.setEcucMultiplicityConfigClasses(element, common_attrs.getMultiplicityConfigClasses())
        self.setChildElementOptionalLiteral(element, "ORIGIN", common_attrs.getOrigin())
        self.setChildElementOptionalBooleanValue(element, "POST-BUILD-VARIANT-MULTIPLICITY", common_attrs.getPostBuildVariantMultiplicity())
        self.setChildElementOptionalBooleanValue(element, "POST-BUILD-VARIANT-VALUE", common_attrs.getPostBuildVariantValue())
        self.setChildElementOptionalBooleanValue(element, "REQUIRES-INDEX", common_attrs.getRequiresIndex())
        self.setEcuValueConfigurationClasses(element, common_attrs.getValueConfigClasses())

    def writeEcucParameterDef(self, element: ET.Element, param_def: EcucParameterDef):
        self.writeEcucCommonAttributes(element, param_def)
        self.writeEcucDerivationSpecification(element, param_def.getDerivation())
        self.setChildElementOptionalBooleanValue(element, "SYMBOLIC-NAME-VALUE", param_def.getSymbolicNameValue())
        self.setChildElementOptionalBooleanValue(element, "WITH-AUTO", param_def.getWithAuto())

    def writeEcucAddInfoParamDef(self, element: ET.Element, param_def: EcucAddInfoParamDef):
        if param_def is not None:
            child_element = ET.SubElement(element, "ECUC-ADD-INFO-PARAM-DEF")
            self.writeEcucParameterDef(child_element, param_def)

    def writeEcucDerivationSpecification(self, element: ET.Element, derivation: Optional[EcucDerivationSpecification]):
        if derivation is None:
            return
        child_element = ET.SubElement(element, "DERIVATION")
        self.writeEcucParameterDerivationFormula(child_element, derivation.getCalculationFormula())
        queries = derivation.getEcucQueries()
        if len(queries) > 0:
            queries_element = ET.SubElement(child_element, "ECUC-QUERYS")
            for query in queries:
                query_element = ET.SubElement(queries_element, "ECUC-QUERY")
                self.writeEcucQuery(query_element, query)
        self.setMlFormula(child_element, "INFORMAL-FORMULA", derivation.getInformalFormula())

    def writeEcucParameterDerivationFormula(self, element: ET.Element, formula: Optional[EcucParameterDerivationFormula]):
        if formula is None:
            return
        formula_element = ET.SubElement(element, "CALCULATION-FORMULA")
        self.setChildElementOptionalRefType(formula_element, "ECUC-QUERY-REF", formula.getEcucQueryRef())
        self.setChildElementOptionalRefType(formula_element, "ECUC-QUERY-STRING-REF", formula.getEcucQueryStringRef())

    def writeEcucConditionFormula(self, element: ET.Element, key: str, formula: Optional[EcucConditionFormula]):
        if formula is None:
            return
        formula_element = ET.SubElement(element, key)
        self.setChildElementOptionalRefType(formula_element, "ECUC-QUERY-REF", formula.getEcucQueryRef())
        self.setChildElementOptionalRefType(formula_element, "ECUC-QUERY-STRING-REF", formula.getEcucQueryStringRef())

    def writeEcucConditionSpecification(self, element: ET.Element, cond: Optional[EcucConditionSpecification]):
        if cond is None:
            return
        child_element = ET.SubElement(element, "ECUC-COND")
        self.writeEcucConditionFormula(child_element, "CONDITION-FORMULA", cond.getConditionFormula())
        queries = cond.getEcucQueries()
        if len(queries) > 0:
            queries_element = ET.SubElement(child_element, "ECUC-QUERYS")
            for query in queries:
                query_element = ET.SubElement(queries_element, "ECUC-QUERY")
                self.writeEcucQuery(query_element, query)
        self.setMlFormula(child_element, "INFORMAL-FORMULA", cond.getInformalFormula())

    def writeEcucValidationCondition(self, element: ET.Element, vc: Optional[EcucValidationCondition]):
        if vc is None:
            return
        self.writeIdentifiable(element, vc)
        queries = vc.getEcucQueries()
        if len(queries) > 0:
            queries_element = ET.SubElement(element, "ECUC-QUERYS")
            for query in queries:
                query_element = ET.SubElement(queries_element, "ECUC-QUERY")
                self.writeEcucQuery(query_element, query)
        self.writeEcucConditionFormula(element, "VALIDATION-FORMULA", vc.getValidationFormula())

    def writeEcucValidationConditions(self, element: ET.Element, conds: List[EcucValidationCondition]):
        if len(conds) > 0:
            child_element = ET.SubElement(element, "ECUC-VALIDATION-CONDS")
            for vc in conds:
                vc_element = ET.SubElement(child_element, "ECUC-VALIDATION-CONDITION")
                self.writeEcucValidationCondition(vc_element, vc)

    def writeEcucQuery(self, element: ET.Element, query: EcucQuery):
        self.writeIdentifiable(element, query)
        expr = query.getEcucQueryExpression()
        if expr is not None:
            expr_element = ET.SubElement(element, "ECUC-QUERY-EXPRESSION")
            self.setChildElementOptionalRefType(expr_element, "CONFIG-ELEMENT-DEF-GLOBAL-REF", expr.getConfigElementDefGlobalRef())
            self.setChildElementOptionalRefType(expr_element, "CONFIG-ELEMENT-DEF-LOCAL-REF", expr.getConfigElementDefLocalRef())

    def writeEcucBooleanParamDef(self, element: ET.Element, param_def: EcucBooleanParamDef):
        if param_def is not None:
            child_element = ET.SubElement(element, "ECUC-BOOLEAN-PARAM-DEF")
            self.writeEcucParameterDef(child_element, param_def)
            self.setChildElementOptionalBooleanValue(child_element, "DEFAULT-VALUE", param_def.getDefaultValue())

    def writeEcucAbstractStringParamDef(self, element: ET.Element, param_def: EcucAbstractStringParamDef):
        self.writeEcucParameterDef(element, param_def)
        self.setChildElementOptionalLiteral(element, "DEFAULT-VALUE", param_def.getDefaultValue())
        self.setChildElementOptionalIntegerValue(element, "MAX-LENGTH", param_def.getMaxLength())
        self.setChildElementOptionalIntegerValue(element, "MIN-LENGTH", param_def.getMinLength())
        self.setChildElementOptionalLiteral(element, "REGULAR-EXPRESSION", param_def.getRegularExpression())

    def writeEcucStringParamDef(self, element: ET.Element, param_def: EcucStringParamDef):
        if param_def is not None:
            child_element = ET.SubElement(element, "ECUC-STRING-PARAM-DEF")
            self.writeEcucParameterDef(child_element, param_def)
            variants_tag = ET.SubElement(child_element, "ECUC-STRING-PARAM-DEF-VARIANTS")
            cond_tag = ET.SubElement(variants_tag, "ECUC-STRING-PARAM-DEF-CONDITIONAL")
            self.writeEcucAbstractStringParamDef(cond_tag, param_def)

    def writeEcucIntegerParamDef(self, element: ET.Element, param_def: EcucIntegerParamDef):
        if param_def is not None:
            child_element = ET.SubElement(element, "ECUC-INTEGER-PARAM-DEF")
            self.writeEcucParameterDef(child_element, param_def)
            self.setChildElementOptionalIntegerValue(child_element, "DEFAULT-VALUE", param_def.getDefaultValue())
            self.setChildElementOptionalIntegerValue(child_element, "MAX", param_def.getMax())
            self.setChildElementOptionalIntegerValue(child_element, "MIN", param_def.getMin())

    def writeEcucFloatParamDef(self, element: ET.Element, param_def: EcucFloatParamDef):
        if param_def is not None:
            child_element = ET.SubElement(element, "ECUC-FLOAT-PARAM-DEF")
            self.writeEcucParameterDef(child_element, param_def)
            self.setChildElementOptionalFloatValue(child_element, "DEFAULT-VALUE", param_def.getDefaultValue())
            self.setChildLimitElement(child_element, "MAX", param_def.getMax())
            self.setChildLimitElement(child_element, "MIN", param_def.getMin())

    def writeEcucEnumerationLiteralDef(self, element: ET.Element, literal: EcucEnumerationLiteralDef):
        if literal is not None:
            child_element = ET.SubElement(element, "ECUC-ENUMERATION-LITERAL-DEF")
            self.writeIdentifiable(child_element, literal)
            self.writeEcucConditionSpecification(child_element, literal.getEcucCond())
            self.setChildElementOptionalLiteral(child_element, "ORIGIN", literal.getOrigin())

    def writeEcucEnumerationParamDefLiterals(self, element: ET.Element, param_def: EcucEnumerationParamDef):
        literals = param_def.getLiterals()
        if len(literals) > 0:
            child_element = ET.SubElement(element, "LITERALS")
            for literal in literals:
                if isinstance(literal, EcucEnumerationLiteralDef):
                    self.writeEcucEnumerationLiteralDef(child_element, literal)
                else:
                    self.notImplemented("Unsupported EnumerationLiteral <%s>" % type(literal))

    def writeEcucEnumerationParamDef(self, element: ET.Element, param_def: EcucEnumerationParamDef):
        if param_def is not None:
            child_element = ET.SubElement(element, "ECUC-ENUMERATION-PARAM-DEF")
            self.writeEcucParameterDef(child_element, param_def)
            self.setChildElementOptionalLiteral(child_element, "DEFAULT-VALUE", param_def.getDefaultValue())
            self.writeEcucEnumerationParamDefLiterals(child_element, param_def)

    def writeEcucFunctionNameDef(self, element: ET.Element, param_def: EcucFunctionNameDef):
        if param_def is not None:
            child_element = ET.SubElement(element, "ECUC-FUNCTION-NAME-DEF")
            self.writeEcucParameterDef(child_element, param_def)
            variants_tag = ET.SubElement(child_element, "ECUC-FUNCTION-NAME-DEF-VARIANTS")
            cond_tag = ET.SubElement(variants_tag, "ECUC-FUNCTION-NAME-DEF-CONDITIONAL")
            self.writeEcucAbstractStringParamDef(cond_tag, param_def)

    def writeEcucMultilineStringParamDef(self, element: ET.Element, param_def: EcucMultilineStringParamDef):
        if param_def is not None:
            child_element = ET.SubElement(element, "ECUC-MULTILINE-STRING-PARAM-DEF")
            self.writeEcucParameterDef(child_element, param_def)
            variants_tag = ET.SubElement(child_element, "ECUC-MULTILINE-STRING-PARAM-DEF-VARIANTS")
            cond_tag = ET.SubElement(variants_tag, "ECUC-MULTILINE-STRING-PARAM-DEF-CONDITIONAL")
            self.writeEcucAbstractStringParamDef(cond_tag, param_def)

    def writeEcucContainerDefParameters(self, element: ET.Element, container_def: EcucParamConfContainerDef):
        parameters = container_def.getParameters()
        if len(parameters) > 0:
            child_element = ET.SubElement(element, "PARAMETERS")
            for parameter in parameters:
                if isinstance(parameter, EcucBooleanParamDef):
                    self.writeEcucBooleanParamDef(child_element, parameter)
                elif isinstance(parameter, EcucAddInfoParamDef):
                    self.writeEcucAddInfoParamDef(child_element, parameter)
                elif isinstance(parameter, EcucStringParamDef):
                    self.writeEcucStringParamDef(child_element, parameter)
                elif isinstance(parameter, EcucIntegerParamDef):
                    self.writeEcucIntegerParamDef(child_element, parameter)
                elif isinstance(parameter, EcucFloatParamDef):
                    self.writeEcucFloatParamDef(child_element, parameter)
                elif isinstance(parameter, EcucEnumerationParamDef):
                    self.writeEcucEnumerationParamDef(child_element, parameter)
                elif isinstance(parameter, EcucFunctionNameDef):
                    self.writeEcucFunctionNameDef(child_element, parameter)
                elif isinstance(parameter, EcucMultilineStringParamDef):
                    self.writeEcucMultilineStringParamDef(child_element, parameter)
                else:
                    self.notImplemented("Unsupported Parameter <%s>" % type(parameter))

    def writeEcucContainerDef(self, element: ET.Element, container_def: EcucContainerDef):
        self.writeEcucDefinitionElement(element, container_def)
        self.setEcucDestinationUriRefs(element, container_def.getDestinationUriRefs())
        self.setEcucMultiplicityConfigClasses(element, container_def.getMultiplicityConfigClasses())
        self.setChildElementOptionalLiteral(element, "ORIGIN", container_def.getOrigin())
        self.setChildElementOptionalBooleanValue(element, "POST-BUILD-VARIANT-MULTIPLICITY", container_def.getPostBuildVariantMultiplicity())
        self.setChildElementOptionalBooleanValue(element, "REQUIRES-INDEX", container_def.getRequiresIndex())

    def setEcucDestinationUriRefs(self, element: ET.Element, uri_refs: List[EcucDestinationUriDefRefType]):
        if len(uri_refs) > 0:
            child_element = ET.SubElement(element, "DESTINATION-URI-REFS")
            for uri_ref in uri_refs:
                if isinstance(uri_ref, EcucDestinationUriDefRefType):
                    ref_element = ET.SubElement(child_element, "DESTINATION-URI-REF")
                    base = uri_ref.getBase()
                    if base is not None:
                        ref_element.attrib["BASE"] = base
                    dest = uri_ref.getDest()
                    if dest is not None:
                        ref_element.attrib["DEST"] = dest
                    if uri_ref.value is not None:
                        ref_element.text = uri_ref.value
                else:
                    self.notImplemented("Unsupported DestinationUriRef <%s>" % type(uri_ref))

    def writeEcucAbstractReferenceDef(self, element: ET.Element, reference: EcucAbstractReferenceDef):
        self.writeEcucCommonAttributes(element, reference)
        self.setChildElementOptionalBooleanValue(element, "WITH-AUTO", reference.getWithAuto())

    def writeEcucAbstractInternalReferenceDef(self, element: ET.Element, reference: EcucAbstractInternalReferenceDef):
        self.writeEcucAbstractReferenceDef(element, reference)
        self.setChildElementOptionalBooleanValue(element, "REQUIRES-SYMBOLIC-NAME-VALUE", reference.getRequiresSymbolicNameValue())

    def writeEcucAbstractExternalReferenceDef(self, element: ET.Element, reference: EcucAbstractExternalReferenceDef):
        self.writeEcucAbstractReferenceDef(element, reference)

    def writeEcucSymbolicNameReferenceDef(self, element: ET.Element, reference: EcucSymbolicNameReferenceDef):
        if reference is not None:
            child_element = ET.SubElement(element, "ECUC-SYMBOLIC-NAME-REFERENCE-DEF")
            self.writeEcucAbstractInternalReferenceDef(child_element, reference)
            self.setChildElementOptionalRefType(child_element, "DESTINATION-REF", reference.getDestinationRef())

    def writeEcucReferenceDef(self, element: ET.Element, reference: EcucReferenceDef):
        if reference is not None:
            child_element = ET.SubElement(element, "ECUC-REFERENCE-DEF")
            self.writeEcucAbstractInternalReferenceDef(child_element, reference)
            self.setChildElementOptionalRefType(child_element, "DESTINATION-REF", reference.getDestinationRef())

    def writeEcucChoiceReferenceDef(self, element: ET.Element, reference: EcucChoiceReferenceDef):
        if reference is not None:
            child_element = ET.SubElement(element, "ECUC-CHOICE-REFERENCE-DEF")
            self.writeEcucAbstractInternalReferenceDef(child_element, reference)
            destination_refs = reference.getDestinationRefs()
            if len(destination_refs) > 0:
                refs_element = ET.SubElement(child_element, "DESTINATION-REFS")
                for destination_ref in destination_refs:
                    self.setChildElementOptionalRefType(refs_element, "DESTINATION-REF", destination_ref)

    def writeEcucInstanceReferenceDef(self, element: ET.Element, reference: EcucInstanceReferenceDef):
        if reference is not None:
            child_element = ET.SubElement(element, "ECUC-INSTANCE-REFERENCE-DEF")
            self.writeEcucAbstractExternalReferenceDef(child_element, reference)
            self.setChildElementOptionalLiteral(child_element, "DESTINATION-CONTEXT", reference.getDestinationContext())
            self.setChildElementOptionalLiteral(child_element, "DESTINATION-TYPE", reference.getDestinationType())

    def writeEcucContainerDefReferences(self, element: ET.Element, container_def: EcucContainerDef):
        references = container_def.getReferences()
        if len(references) > 0:
            child_element = ET.SubElement(element, "REFERENCES")
            for reference in references:
                if isinstance(reference, EcucSymbolicNameReferenceDef):
                    self.writeEcucSymbolicNameReferenceDef(child_element, reference)
                elif isinstance(reference, EcucReferenceDef):
                    self.writeEcucReferenceDef(child_element, reference)
                elif isinstance(reference, EcucChoiceReferenceDef):
                    self.writeEcucChoiceReferenceDef(child_element, reference)
                elif isinstance(reference, EcucInstanceReferenceDef):
                    self.writeEcucInstanceReferenceDef(child_element, reference)
                else:
                    self.notImplemented("Unsupported Reference <%s>" % type(reference))

    def writeEcucContainerDefSubContainers(self, element: ET.Element, container_def: EcucParamConfContainerDef):
        sub_containers = container_def.getSubContainers()
        if len(sub_containers) > 0:
            child_element = ET.SubElement(element, "SUB-CONTAINERS")
            for sub_container in sub_containers:
                if isinstance(sub_container, EcucParamConfContainerDef):
                    self.writeEcucParamConfContainerDef(child_element, sub_container)
                elif isinstance(sub_container, EcucChoiceContainerDef):
                    self.writeEcucChoiceContainerDef(child_element, sub_container)
                else:
                    self.notImplemented("Unsupported SubContainer <%s>" % type(sub_container))

    def writeEcucParamConfContainerDef(self, element: ET.Element, container_def: EcucParamConfContainerDef):
        if container_def is not None:
            child_element = ET.SubElement(element, "ECUC-PARAM-CONF-CONTAINER-DEF")
            self.writeEcucContainerDef(child_element, container_def)
            self.writeEcucContainerDefParameters(child_element, container_def)
            self.writeEcucContainerDefReferences(child_element, container_def)
            self.writeEcucContainerDefSubContainers(child_element, container_def)

    def writeEcucChoiceContainerDefChoices(self, element: ET.Element, container_def: EcucChoiceContainerDef):
        choices = container_def.getChoices()
        if len(choices) > 0:
            child_element = ET.SubElement(element, "CHOICES")
            for choice in choices:
                if isinstance(choice, EcucParamConfContainerDef):
                    self.writeEcucParamConfContainerDef(child_element, choice)
                else:
                    self.notImplemented("Unsupported Choice <%s>" % type(choice))

    def writeEcucChoiceContainerDef(self, element: ET.Element, container_def: EcucChoiceContainerDef):
        if container_def is not None:
            child_element = ET.SubElement(element, "ECUC-CHOICE-CONTAINER-DEF")
            self.writeEcucContainerDef(child_element, container_def)
            self.writeEcucChoiceContainerDefChoices(child_element, container_def)

    def writeEcucModuleDefContainers(self, element: ET.Element, module_def: EcucModuleDef):
        container_defs = module_def.getContainers()
        child_element = ET.SubElement(element, "CONTAINERS")
        for container_def in container_defs:
            if isinstance(container_def, EcucParamConfContainerDef):
                self.writeEcucParamConfContainerDef(child_element, container_def)
            elif isinstance(container_def, EcucChoiceContainerDef):
                self.writeEcucChoiceContainerDef(child_element, container_def)
            else:
                self.notImplemented("Unsupported Container <%s>" % type(container_def))

    def writeEcucModuleDef(self, element: ET.Element, module_def: EcucModuleDef):
        if module_def is not None:
            self.logger.debug("Write EcucModuleDef <%s>" % module_def.getShortName())
            child_element = ET.SubElement(element, "ECUC-MODULE-DEF")
            self.writeEcucDefinitionElement(child_element, module_def)
            self.setChildElementOptionalLiteral(child_element, "API-SERVICE-PREFIX", module_def.getApiServicePrefix())
            self.setChildElementOptionalBooleanValue(child_element, "POST-BUILD-VARIANT-SUPPORT", module_def.getPostBuildVariantSupport())
            self.setChildElementOptionalRefType(child_element, "REFINED-MODULE-DEF-REF", module_def.getRefinedModuleDefRef())
            self.writeEcucModuleDefSupportedConfigVariants(child_element, module_def)
            self.writeEcucModuleDefContainers(child_element, module_def)

    def writeEcucDefinitionCollectionModuleRefs(self, element: ET.Element, collection: EcucDefinitionCollection):
        module_refs = collection.getModuleRefs()
        if len(module_refs) > 0:
            child_element = ET.SubElement(element, "MODULE-REFS")
            for module_ref in module_refs:
                self.setChildElementOptionalRefType(child_element, "MODULE-REF", module_ref)

    def writeEcucDefinitionCollection(self, element: ET.Element, collection: EcucDefinitionCollection):
        if collection is not None:
            self.logger.debug("Write EcucDefinitionCollection <%s>" % collection.getShortName())
            child_element = ET.SubElement(element, "ECUC-DEFINITION-COLLECTION")
            self.writeARElement(child_element, collection)
            self.writeEcucDefinitionCollectionModuleRefs(child_element, collection)

    def writeEcucDestinationUriDefSet(self, element: ET.Element, uri_def_set: EcucDestinationUriDefSet):
        if uri_def_set is not None:
            self.logger.debug("Write EcucDestinationUriDefSet <%s>" % uri_def_set.getShortName())
            child_element = ET.SubElement(element, "ECUC-DESTINATION-URI-DEF-SET")
            self.writeARElement(child_element, uri_def_set)
            uri_defs = uri_def_set.getDestinationUriDefs()
            if len(uri_defs) > 0:
                defs_element = ET.SubElement(child_element, "DESTINATION-URI-DEFS")
                for uri_def in uri_defs:
                    self.writeEcucDestinationUriDef(defs_element, uri_def)

    def writeEcucDestinationUriDef(self, element: ET.Element, uri_def: EcucDestinationUriDef):
        if uri_def is not None:
            self.logger.debug("Write EcucDestinationUriDef <%s>" % uri_def.getShortName())
            child_element = ET.SubElement(element, "ECUC-DESTINATION-URI-DEF")
            self.writeIdentifiable(child_element, uri_def)
            self.writeEcucDestinationUriPolicy(child_element, uri_def.getDestinationUriPolicy())

    def writeEcucDestinationUriPolicy(self, element: ET.Element, policy: EcucDestinationUriPolicy):
        if policy is None:
            return
        self.logger.debug("Write EcucDestinationUriPolicy")
        child_element = ET.SubElement(element, "DESTINATION-URI-POLICY")
        self.writeARObjectAttributes(child_element, policy)
        containers = policy.getContainers()
        if len(containers) > 0:
            containers_element = ET.SubElement(child_element, "CONTAINERS")
            for container in containers:
                if isinstance(container, EcucParamConfContainerDef):
                    self.writeEcucParamConfContainerDef(containers_element, container)
                elif isinstance(container, EcucChoiceContainerDef):
                    self.writeEcucChoiceContainerDef(containers_element, container)
                else:
                    self.notImplemented("Unsupported DestinationUriPolicy Container <%s>" % type(container))
        nesting_contract = policy.getDestinationUriNestingContract()
        if nesting_contract is not None:
            contract_element = ET.SubElement(child_element, "DESTINATION-URI-NESTING-CONTRACT")
            contract_element.text = nesting_contract.getValue()
        self.writeEcucDestinationUriPolicyParameters(child_element, policy)
        self.writeEcucDestinationUriPolicyReferences(child_element, policy)

    def writeEcucDestinationUriPolicyParameters(self, element: ET.Element, policy: EcucDestinationUriPolicy):
        parameters = policy.getParameters()
        if len(parameters) > 0:
            parameters_element = ET.SubElement(element, "PARAMETERS")
            for parameter in parameters:
                if isinstance(parameter, EcucBooleanParamDef):
                    self.writeEcucBooleanParamDef(parameters_element, parameter)
                elif isinstance(parameter, EcucStringParamDef):
                    self.writeEcucStringParamDef(parameters_element, parameter)
                elif isinstance(parameter, EcucIntegerParamDef):
                    self.writeEcucIntegerParamDef(parameters_element, parameter)
                elif isinstance(parameter, EcucFloatParamDef):
                    self.writeEcucFloatParamDef(parameters_element, parameter)
                elif isinstance(parameter, EcucEnumerationParamDef):
                    self.writeEcucEnumerationParamDef(parameters_element, parameter)
                elif isinstance(parameter, EcucFunctionNameDef):
                    self.writeEcucFunctionNameDef(parameters_element, parameter)
                elif isinstance(parameter, EcucMultilineStringParamDef):
                    self.writeEcucMultilineStringParamDef(parameters_element, parameter)
                else:
                    self.notImplemented("Unsupported DestinationUriPolicy Parameter <%s>" % type(parameter))

    def writeEcucDestinationUriPolicyReferences(self, element: ET.Element, policy: EcucDestinationUriPolicy):
        references = policy.getReferences()
        if len(references) > 0:
            references_element = ET.SubElement(element, "REFERENCES")
            for reference in references:
                if isinstance(reference, EcucSymbolicNameReferenceDef):
                    self.writeEcucSymbolicNameReferenceDef(references_element, reference)
                elif isinstance(reference, EcucReferenceDef):
                    self.writeEcucReferenceDef(references_element, reference)
                elif isinstance(reference, EcucChoiceReferenceDef):
                    self.writeEcucChoiceReferenceDef(references_element, reference)
                elif isinstance(reference, EcucInstanceReferenceDef):
                    self.writeEcucInstanceReferenceDef(references_element, reference)
                else:
                    self.notImplemented("Unsupported DestinationUriPolicy Reference <%s>" % type(reference))

    def writeMacMulticastGroup(self, element: ET.Element, group: MacMulticastGroup):
        if group is not None:
            child_element = ET.SubElement(element, "MAC-MULTICAST-GROUP")
            self.writeIdentifiable(child_element, group)
            self.setChildElementOptionalLiteral(child_element, "MAC-MULTICAST-ADDRESS", group.getMacMulticastAddress())

    def writeEthernetClusterMacMulticastGroups(self, element: ET.Element, cluster: EthernetCluster):
        groups = cluster.getMacMulticastGroups()
        if len(groups) > 0:
            child_element = ET.SubElement(element, "MAC-MULTICAST-GROUPS")
            for group in groups:
                if isinstance(group, MacMulticastGroup):
                    self.writeMacMulticastGroup(child_element, group)
                else:
                    self.notImplemented("Unsupported assigned data type <%s>" % type(group))

    def writeCouplingPortConnection(self, element: ET.Element, connection: CouplingPortConnection):
        child_element = ET.SubElement(element, "COUPLING-PORT-CONNECTION")
        self.setChildElementOptionalRefType(child_element, "FIRST-PORT-REF", connection.getFirstPortRef())
        node_ports = connection.getNodePortRefs()
        if len(node_ports) > 0:
            node_ports_element = ET.SubElement(child_element, "NODE-PORTS")
            for ref in node_ports:
                conditional_element = ET.SubElement(node_ports_element, "COUPLING-PORT-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(conditional_element, "COUPLING-PORT-REF", ref)
        self.setChildElementOptionalPositiveInteger(child_element, "PLCA-LOCAL-NODE-COUNT", connection.getPlcaLocalNodeCount())
        self.setChildElementOptionalPositiveInteger(child_element, "PLCA-TRANSMIT-OPPORTUNITY-TIMER", connection.getPlcaTransmitOpportunityTimer())
        self.setChildElementOptionalRefType(child_element, "SECOND-PORT-REF", connection.getSecondPortRef())

    def writeEthernetClusterCouplingPortConnections(self, element: ET.Element, cluster: EthernetCluster):
        connections = cluster.getCouplingPortConnections()
        if len(connections) > 0:
            connections_element = ET.SubElement(element, "COUPLING-PORT-CONNECTIONS")
            for connection in connections:
                if isinstance(connection, CouplingPortConnection):
                    self.writeCouplingPortConnection(connections_element, connection)
                else:
                    self.notImplemented("Unsupported CouplingPortConnection <%s>" % type(connection))

    def writeEthernetCluster(self, element: ET.Element, cluster: EthernetCluster):
        self.logger.debug("Set EthernetCluster %s" % cluster.getShortName())
        child_element = ET.SubElement(element, "ETHERNET-CLUSTER")
        self.writeARElement(child_element, cluster)

        child_element = ET.SubElement(child_element, "ETHERNET-CLUSTER-VARIANTS")
        child_element = ET.SubElement(child_element, "ETHERNET-CLUSTER-CONDITIONAL")
        self.writeCommunicationCluster(child_element, cluster)
        self.setChildElementOptionalTimeValue(child_element, "COUPLING-PORT-STARTUP-ACTIVE-TIME", cluster.getCouplingPortStartupActiveTime())
        self.setChildElementOptionalTimeValue(child_element, "COUPLING-PORT-SWITCHOFF-DELAY", cluster.getCouplingPortSwitchoffDelay())
        self.writeEthernetClusterMacMulticastGroups(child_element, cluster)
        self.writeEthernetClusterCouplingPortConnections(child_element, cluster)

    def writeCanFrame(self, element: ET.Element, frame: CanFrame):
        self.logger.debug("Write CanFrame %s" % frame.getShortName())
        child_element = ET.SubElement(element, "CAN-FRAME")
        self.writeFrame(child_element, frame)

    def writeCommConnectorPort(self, element: ET.Element, port: CommConnectorPort):
        self.writeIdentifiable(element, port)
        self.setChildElementOptionalLiteral(element, "COMMUNICATION-DIRECTION", port.getCommunicationDirection())

    def writeFramePort(self, element: ET.Element, port: FramePort):
        child_element = ET.SubElement(element, "FRAME-PORT")
        self.writeCommConnectorPort(child_element, port)

    def writeIPduPort(self, element: ET.Element, port: IPduPort):
        child_element = ET.SubElement(element, "I-PDU-PORT")
        self.writeCommConnectorPort(child_element, port)
        self.setChildElementOptionalLiteral(child_element, "I-PDU-SIGNAL-PROCESSING", port.getIPduSignalProcessing())
        self.setChildElementOptionalBooleanValue(child_element, "RX-SECURITY-VERIFICATION", port.getRxSecurityVerification())
        self.setChildElementOptionalTimeValue(child_element, "TIMESTAMP-RX-ACCEPTANCE-WINDOW", port.getTimestampRxAcceptanceWindow())
        self.setChildElementOptionalBooleanValue(child_element, "USE-AUTH-DATA-FRESHNESS", port.getUseAuthDataFreshness())

    def writeISignalPort(self, element: ET.Element, port: ISignalPort):
        child_element = ET.SubElement(element, "I-SIGNAL-PORT")
        self.writeCommConnectorPort(child_element, port)
        self.setChildElementOptionalTimeValue(child_element, "TIMEOUT", port.getTimeout())

    def writeCommunicationConnectorEcuCommPortInstances(self, element: ET.Element, connector: CommunicationConnector):
        self.logger.debug("write EcuCommPortInstances of CommunicationConnector %s" % connector.getShortName())
        ports = connector.getEcuCommPortInstances()
        if len(ports) > 0:
            instances_tag = ET.SubElement(element, "ECU-COMM-PORT-INSTANCES")
            for port in ports:
                if isinstance(port, FramePort):
                    self.writeFramePort(instances_tag, port)
                elif isinstance(port, IPduPort):
                    self.writeIPduPort(instances_tag, port)
                elif isinstance(port, ISignalPort):
                    self.writeISignalPort(instances_tag, port)
                else:
                    self.notImplemented("Unsupported CommConnectorPort <%s>" % type(port))

    def writeCommunicationController(self, element: ET.Element, controller: CommunicationController):
        self.setChildElementOptionalBooleanValue(element, "WAKE-UP-BY-CONTROLLER-SUPPORTED", controller.getWakeUpByControllerSupported())

    def setCanControllerFdConfiguration(self, element: ET.Element, key: str, configuration: CanControllerFdConfiguration):
        if configuration is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalIntegerValue(child_element, "PADDING-VALUE", configuration.getPaddingValue())
            self.setChildElementOptionalIntegerValue(child_element, "PROP-SEG", configuration.getPropSeg())
            self.setChildElementOptionalIntegerValue(child_element, "SSP-OFFSET", configuration.getSspOffset())
            self.setChildElementOptionalIntegerValue(child_element, "SYNC-JUMP-WIDTH", configuration.getSyncJumpWidth())
            self.setChildElementOptionalIntegerValue(child_element, "TIME-SEG1", configuration.getTimeSeg1())
            self.setChildElementOptionalIntegerValue(child_element, "TIME-SEG2", configuration.getTimeSeg2())
            self.setChildElementOptionalBooleanValue(child_element, "TX-BIT-RATE-SWITCH", configuration.getTxBitRateSwitch())

    def setFlexrayFifoRange(self, element: ET.Element, key: str, fifo_range: FlexrayFifoRange):
        if fifo_range is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalIntegerValue(child_element, "RANGE-MAX", fifo_range.getRangeMax())
            self.setChildElementOptionalIntegerValue(child_element, "RANGE-MIN", fifo_range.getRangeMin())

    def setFlexrayFifoConfiguration(self, element: ET.Element, key: str, configuration: FlexrayFifoConfiguration):
        if configuration is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalBooleanValue(child_element, "ADMIT-WITHOUT-MESSAGE-ID", configuration.getAdmitWithoutMessageId())
            self.setChildElementOptionalIntegerValue(child_element, "BASE-CYCLE", configuration.getBaseCycle())
            self.setChildElementOptionalRefType(child_element, "CHANNEL-REF", configuration.getChannelRef())
            self.setChildElementOptionalIntegerValue(child_element, "CYCLE-REPETITION", configuration.getCycleRepetition())
            self.setChildElementOptionalIntegerValue(child_element, "FIFO-DEPTH", configuration.getFifoDepth())
            for fifo_range in configuration.getFlexrayFifoRanges():
                self.setFlexrayFifoRange(child_element, "FLEXRAY-FIFO-RANGE", fifo_range)
            self.setChildElementOptionalIntegerValue(child_element, "MSG-ID-MASK", configuration.getMsgIdMask())
            self.setChildElementOptionalIntegerValue(child_element, "MSG-ID-MATCH", configuration.getMsgIdMatch())

    def setCanControllerFdConfigurationRequirements(self, element: ET.Element, key: str, requirements: CanControllerFdConfigurationRequirements):
        if requirements is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalIntegerValue(child_element, "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT", requirements.getMaxNumberOfTimeQuantaPerBit())  # noqa E501
            self.setChildElementOptionalFloatValue(child_element, "MAX-SAMPLE-POINT", requirements.getMaxSamplePoint())
            self.setChildElementOptionalFloatValue(child_element, "MAX-SYNC-JUMP-WIDTH", requirements.getMaxSyncJumpWidth())
            self.setChildElementOptionalTimeValue(child_element, "MAX-TRCV-DELAY-COMPENSATION-OFFSET", requirements.getMaxTrcvDelayCompensationOffset())  # noqa E501
            self.setChildElementOptionalIntegerValue(child_element, "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT", requirements.getMinNumberOfTimeQuantaPerBit())  # noqa E501
            self.setChildElementOptionalFloatValue(child_element, "MIN-SAMPLE-POINT", requirements.getMinSamplePoint())
            self.setChildElementOptionalFloatValue(child_element, "MIN-SYNC-JUMP-WIDTH", requirements.getMinSyncJumpWidth())
            self.setChildElementOptionalTimeValue(child_element, "MIN-TRCV-DELAY-COMPENSATION-OFFSET", requirements.getMinTrcvDelayCompensationOffset())  # noqa E501
            self.setChildElementOptionalBooleanValue(child_element, "TX-BIT-RATE-SWITCH", requirements.getTxBitRateSwitch())

    def setCanControllerXlConfiguration(self, element: ET.Element, key: str, configuration: CanControllerXlConfiguration):
        if configuration is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalBooleanValue(child_element, "ERROR-SIGNALING-ENABLED", configuration.getErrorSignalingEnabled())
            self.setChildElementOptionalIntegerValue(child_element, "PROP-SEG", configuration.getPropSeg())
            self.setChildElementOptionalIntegerValue(child_element, "PWM-L", configuration.getPwmL())
            self.setChildElementOptionalIntegerValue(child_element, "PWM-O", configuration.getPwmO())
            self.setChildElementOptionalIntegerValue(child_element, "PWM-S", configuration.getPwmS())
            self.setChildElementOptionalIntegerValue(child_element, "SSP-OFFSET", configuration.getSspOffset())
            self.setChildElementOptionalIntegerValue(child_element, "SYNC-JUMP-WIDTH", configuration.getSyncJumpWidth())
            self.setChildElementOptionalIntegerValue(child_element, "TIME-SEG1", configuration.getTimeSeg1())
            self.setChildElementOptionalIntegerValue(child_element, "TIME-SEG2", configuration.getTimeSeg2())
            self.setChildElementOptionalBooleanValue(child_element, "TRCV-PWM-MODE-ENABLED", configuration.getTrcvPwmModeEnabled())

    def setCanControllerXlConfigurationRequirements(self, element: ET.Element, key: str, requirements: CanControllerXlConfigurationRequirements):
        if requirements is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalBooleanValue(child_element, "ERROR-SIGNALING-ENABLED", requirements.getErrorSignalingEnabled())
            self.setChildElementOptionalIntegerValue(child_element, "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT", requirements.getMaxNumberOfTimeQuantaPerBit())
            self.setChildElementOptionalIntegerValue(child_element, "MAX-PWM-L", requirements.getMaxPwmL())
            self.setChildElementOptionalIntegerValue(child_element, "MAX-PWM-O", requirements.getMaxPwmO())
            self.setChildElementOptionalIntegerValue(child_element, "MAX-PWM-S", requirements.getMaxPwmS())
            self.setChildElementOptionalFloatValue(child_element, "MAX-SAMPLE-POINT", requirements.getMaxSamplePoint())
            self.setChildElementOptionalFloatValue(child_element, "MAX-SYNC-JUMP-WIDTH", requirements.getMaxSyncJumpWidth())
            self.setChildElementOptionalTimeValue(child_element, "MAX-TRCV-DELAY-COMPENSATION-OFFSET", requirements.getMaxTrcvDelayCompensationOffset())
            self.setChildElementOptionalIntegerValue(child_element, "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT", requirements.getMinNumberOfTimeQuantaPerBit())
            self.setChildElementOptionalIntegerValue(child_element, "MIN-PWM-L", requirements.getMinPwmL())
            self.setChildElementOptionalIntegerValue(child_element, "MIN-PWM-O", requirements.getMinPwmO())
            self.setChildElementOptionalIntegerValue(child_element, "MIN-PWM-S", requirements.getMinPwmS())
            self.setChildElementOptionalFloatValue(child_element, "MIN-SAMPLE-POINT", requirements.getMinSamplePoint())
            self.setChildElementOptionalFloatValue(child_element, "MIN-SYNC-JUMP-WIDTH", requirements.getMinSyncJumpWidth())
            self.setChildElementOptionalTimeValue(child_element, "MIN-TRCV-DELAY-COMPENSATION-OFFSET", requirements.getMinTrcvDelayCompensationOffset())
            self.setChildElementOptionalBooleanValue(child_element, "TRCV-PWM-MODE-ENABLED", requirements.getTrcvPwmModeEnabled())

    def writeAbstractCanCommunicationControllerAttributes(self, element: ET.Element, attributes: AbstractCanCommunicationControllerAttributes):
        self.setCanControllerFdConfiguration(element, "CAN-CONTROLLER-FD-CONFIGURATION", attributes.getCanControllerFdAttributes())
        self.setCanControllerFdConfigurationRequirements(element, "CAN-CONTROLLER-FD-REQUIREMENTS", attributes.getCanControllerFdRequirements())
        self.setCanControllerXlConfiguration(element, "CAN-CONTROLLER-XL-CONFIGURATION", attributes.getCanControllerXlAttributes())
        self.setCanControllerXlConfigurationRequirements(element, "CAN-CONTROLLER-XL-REQUIREMENTS", attributes.getCanControllerXlRequirements())

    def writeCanControllerConfigurationRequirements(self, element: ET.Element, requirements: CanControllerConfigurationRequirements):
        if requirements is not None:
            child_element = ET.SubElement(element, "CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS")
            self.writeAbstractCanCommunicationControllerAttributes(child_element, requirements)
            self.setChildElementOptionalIntegerValue(child_element, "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT", requirements.getMaxNumberOfTimeQuantaPerBit())  # noqa E501
            self.setChildElementOptionalFloatValue(child_element, "MAX-SAMPLE-POINT", requirements.getMaxSamplePoint())
            self.setChildElementOptionalFloatValue(child_element, "MAX-SYNC-JUMP-WIDTH", requirements.getMaxSyncJumpWidth())
            self.setChildElementOptionalIntegerValue(child_element, "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT", requirements.getMinNumberOfTimeQuantaPerBit())  # noqa E501
            self.setChildElementOptionalFloatValue(child_element, "MIN-SAMPLE-POINT", requirements.getMinSamplePoint())
            self.setChildElementOptionalFloatValue(child_element, "MIN-SYNC-JUMP-WIDTH", requirements.getMinSyncJumpWidth())

    def writeAbstractCanCommunicationControllerCanControllerAttributes(self, element: ET.Element, controller: AbstractCanCommunicationController):
        attributes = controller.getCanControllerAttributes()
        if attributes is not None:
            child_element = ET.SubElement(element, "CAN-CONTROLLER-ATTRIBUTES")
            if isinstance(attributes, CanControllerConfigurationRequirements):
                self.writeCanControllerConfigurationRequirements(child_element, attributes)
            else:
                self.notImplemented("Unsupported CanControllerAttributes <%s>" % type(attributes))

    def writeAbstractCanCommunicationController(self, element: ET.Element, controller: AbstractCanCommunicationController):
        self.writeCommunicationController(element, controller)
        self.writeAbstractCanCommunicationControllerCanControllerAttributes(element, controller)

    def writeCanCommunicationController(self, element: ET.Element, controller: CanCommunicationController):
        child_element = ET.SubElement(element, "CAN-COMMUNICATION-CONTROLLER")
        self.logger.debug("Write CanCommunicationController %s" % controller.getShortName())
        self.writeIdentifiable(child_element, controller)
        variants_tag = ET.SubElement(child_element, "CAN-COMMUNICATION-CONTROLLER-VARIANTS")
        cond_tag = ET.SubElement(variants_tag, "CAN-COMMUNICATION-CONTROLLER-CONDITIONAL")
        self.writeAbstractCanCommunicationController(cond_tag, controller)

    def writeCouplingPortSchedulerCouplingPortStructuralElement(self, element: ET.Element, item: CouplingPortStructuralElement):
        self.writeIdentifiable(element, item)

    def writeCouplingPortFifo(self, element: ET.Element, fifo: CouplingPortFifo):
        if fifo is not None:
            child_element = ET.SubElement(element, "COUPLING-PORT-FIFO")
            self.writeCouplingPortSchedulerCouplingPortStructuralElement(child_element, fifo)
            classes = fifo.getAssignedTrafficClasses()
            if len(classes) > 0:
                classes_element = ET.SubElement(child_element, "ASSIGNED-TRAFFIC-CLASSS")
                for value in classes:
                    self.setChildElementOptionalPositiveInteger(classes_element, "ASSIGNED-TRAFFIC-CLASS", value)
            self.setChildElementOptionalPositiveInteger(child_element, "MINIMUM-FIFO-LENGTH", fifo.getMinimumFifoLength())
            self.writeCouplingPortFifoShaper(child_element, fifo)

    def writeCouplingPortFifoShaper(self, element: ET.Element, fifo: CouplingPortFifo):
        shaper = fifo.getShaper()
        if shaper is not None:
            shaper_element = ET.SubElement(element, "SHAPER")
            tag = CouplingPortAbstractShaper.getShaperTag(type(shaper))
            if tag is None:
                self.notImplemented("Unsupported CouplingPort shaper <%s>" % type(shaper).__name__)
                return
            child = ET.SubElement(shaper_element, tag)
            self.writeIdentifiable(child, shaper)

    def writeCouplingPortScheduler(self, element: ET.Element, scheduler: CouplingPortScheduler):
        if scheduler is not None:
            child_element = ET.SubElement(element, "COUPLING-PORT-SCHEDULER")
            self.writeCouplingPortSchedulerCouplingPortStructuralElement(child_element, scheduler)
            self.setChildElementOptionalLiteral(child_element, "PORT-SCHEDULER", scheduler.getPortScheduler())

    def writeCouplingPortDetailsCouplingPortStructuralElements(self, element: ET.Element, details: CouplingPortDetails):
        items = details.getCouplingPortStructuralElements()
        if len(items) > 0:
            child_element = ET.SubElement(element, "COUPLING-PORT-STRUCTURAL-ELEMENTS")
            for item in items:
                if isinstance(item, CouplingPortFifo):
                    self.writeCouplingPortFifo(child_element, item)
                elif isinstance(item, CouplingPortScheduler):
                    self.writeCouplingPortScheduler(child_element, item)
                else:
                    self.notImplemented("Unsupported CouplingPortStructuralElement <%s>" % type(item))

    def writeEthernetPriorityRegeneration(self, element: ET.Element, regeneration: EthernetPriorityRegeneration):
        if regeneration is not None:
            child_element = ET.SubElement(element, "ETHERNET-PRIORITY-REGENERATION")
            self.writeReferrable(child_element, regeneration)
            self.setChildElementOptionalPositiveInteger(child_element, "INGRESS-PRIORITY", regeneration.getIngressPriority())
            self.setChildElementOptionalPositiveInteger(child_element, "REGENERATED-PRIORITY", regeneration.getRegeneratedPriority())

    def writeCouplingPortDetailsEthernetPriorityRegenerations(self, element: ET.Element, details: CouplingPortDetails):
        regenerations = details.getEthernetPriorityRegenerations()
        if len(regenerations) > 0:
            child_element = ET.SubElement(element, "ETHERNET-PRIORITY-REGENERATIONS")
            for regeneration in regenerations:
                if isinstance(regeneration, EthernetPriorityRegeneration):
                    self.writeEthernetPriorityRegeneration(child_element, regeneration)
                else:
                    self.notImplemented("Unsupported EthernetPriorityRegeneration <%s>" % type(regeneration))

    def writeCouplingPortTrafficClassAssignment(self, element: ET.Element, assignment: CouplingPortTrafficClassAssignment):
        child_element = ET.SubElement(element, "COUPLING-PORT-TRAFFIC-CLASS-ASSIGNMENT")
        self.writeReferrable(child_element, assignment)
        for priority in assignment.getPriorities():
            self.setChildElementOptionalPositiveInteger(child_element, "PRIORITY", priority)
        self.setChildElementOptionalPositiveInteger(child_element, "TRAFFIC-CLASS", assignment.getTrafficClass())

    def writeCouplingPortDetailsEthernetTrafficClassAssignments(self, element: ET.Element, details: CouplingPortDetails):
        assignments = details.getEthernetTrafficClassAssignments()
        if len(assignments) > 0:
            child_element = ET.SubElement(element, "ETHERNET-TRAFFIC-CLASS-ASSIGNMENTS")
            for assignment in assignments:
                if isinstance(assignment, CouplingPortTrafficClassAssignment):
                    self.writeCouplingPortTrafficClassAssignment(child_element, assignment)
                else:
                    self.notImplemented("Unsupported CouplingPortTrafficClassAssignment <%s>" % type(assignment))

    def writeCouplingPortDetailsRatePolicys(self, element: ET.Element, details: CouplingPortDetails):
        rate_policies = details.getRatePolicies()
        if len(rate_policies) > 0:
            child_element = ET.SubElement(element, "RATE-POLICYS")
            for rate_policy in rate_policies:
                if isinstance(rate_policy, CouplingPortRatePolicy):
                    self.writeCouplingPortRatePolicy(child_element, rate_policy)
                else:
                    self.notImplemented("Unsupported CouplingPortRatePolicy <%s>" % type(rate_policy))

    def writeCouplingPortRatePolicy(self, element: ET.Element, policy: CouplingPortRatePolicy):
        child_element = ET.SubElement(element, "COUPLING-PORT-RATE-POLICY")
        self.setChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH", policy.getDataLength())
        self.setChildElementOptionalLiteral(child_element, "POLICY-ACTION", policy.getPolicyAction())
        self.setChildElementOptionalPositiveInteger(child_element, "PRIORITY", policy.getPriority())
        self.setChildElementOptionalTimeValue(child_element, "TIME-INTERVAL", policy.getTimeInterval())
        vlan_refs = policy.getVlanRefs()
        if len(vlan_refs) > 0:
            wrapper = ET.SubElement(child_element, "V-LAN-REFS")
            for vlan_ref in vlan_refs:
                self.setChildElementOptionalRefType(wrapper, "V-LAN-REF", vlan_ref)

    def setPlcaProps(self, element: ET.Element, key: str, props: PlcaProps):
        if props is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalPositiveInteger(child_element, "PLCA-LOCAL-NODE-ID", props.getPlcaLocalNodeId())
            self.setChildElementOptionalPositiveInteger(child_element, "PLCA-MAX-BURST-COUNT", props.getPlcaMaxBurstCount())
            self.setChildElementOptionalPositiveInteger(child_element, "PLCA-MAX-BURST-TIMER", props.getPlcaMaxBurstTimer())

    def setGlobalTimeProps(self, element: ET.Element, key: str, props: GlobalTimeCouplingPortProps):
        if props is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalTimeValue(child_element, "PROPAGATION-DELAY", props.getPropagationDelay())

    def writeMacSecGlobalKayProps(self, element: ET.Element, props: MacSecGlobalKayProps):
        child_element = ET.SubElement(element, "MAC-SEC-GLOBAL-KAY-PROPS")
        self.writeARElement(child_element, props)
        ether_types = props.getBypassEtherTypes()
        if len(ether_types) > 0:
            wrapper = ET.SubElement(child_element, "BYPASS-ETHER-TYPES")
            for value in ether_types:
                self.setChildElementOptionalPositiveInteger(wrapper, "BYPASS-ETHER-TYPE", value)
        vlans = props.getBypassVlans()
        if len(vlans) > 0:
            wrapper = ET.SubElement(child_element, "BYPASS-VLANS")
            for value in vlans:
                self.setChildElementOptionalPositiveInteger(wrapper, "BYPASS-VLAN", value)

    def writeMacSecCipherSuiteConfig(self, element: ET.Element, config: MacSecCipherSuiteConfig):
        child_element = ET.SubElement(element, "MAC-SEC-CIPHER-SUITE-CONFIG")
        self.setChildElementOptionalString(child_element, "CIPHER-SUITE", config.getCipherSuite())
        self.setChildElementOptionalPositiveInteger(child_element, "CIPHER-SUITE-PRIORITY", config.getCipherSuitePriority())

    def writeMacSecCryptoAlgoConfig(self, element: ET.Element, config: MacSecCryptoAlgoConfig):
        child_element = ET.SubElement(element, "MAC-SEC-CRYPTO-ALGO-CONFIG")
        self.setChildElementOptionalLiteral(child_element, "CAPABILITY", config.getCapability())
        cipher_configs = config.getCipherSuiteConfigs()
        if len(cipher_configs) > 0:
            wrapper = ET.SubElement(child_element, "CIPHER-SUITE-CONFIGS")
            for cipher_config in cipher_configs:
                self.writeMacSecCipherSuiteConfig(wrapper, cipher_config)
        self.setChildElementOptionalLiteral(child_element, "CONFIDENTIALITY-OFFSET", config.getConfidentialityOffset())
        self.setChildElementOptionalBooleanValue(child_element, "REPLAY-PROTECTION", config.getReplayProtection())
        self.setChildElementOptionalPositiveInteger(child_element, "REPLAY-PROTECTION-WINDOW", config.getReplayProtectionWindow())

    def writeMacSecKayParticipant(self, element: ET.Element, participant: MacSecKayParticipant):
        child_element = ET.SubElement(element, "MAC-SEC-KAY-PARTICIPANT")
        self.writeIdentifiable(child_element, participant)
        self.setChildElementOptionalRefType(child_element, "CKN-REF", participant.getCkn())
        config = participant.getCryptoAlgoConfig()
        if config is not None:
            algo_element = ET.SubElement(child_element, "CRYPTO-ALGO-CONFIG")
            self.setChildElementOptionalLiteral(algo_element, "CAPABILITY", config.getCapability())
            cipher_configs = config.getCipherSuiteConfigs()
            if len(cipher_configs) > 0:
                wrapper = ET.SubElement(algo_element, "CIPHER-SUITE-CONFIGS")
                for cipher_config in cipher_configs:
                    self.writeMacSecCipherSuiteConfig(wrapper, cipher_config)
            self.setChildElementOptionalLiteral(algo_element, "CONFIDENTIALITY-OFFSET", config.getConfidentialityOffset())
            self.setChildElementOptionalBooleanValue(algo_element, "REPLAY-PROTECTION", config.getReplayProtection())
            self.setChildElementOptionalPositiveInteger(algo_element, "REPLAY-PROTECTION-WINDOW", config.getReplayProtectionWindow())
        self.setChildElementOptionalRefType(child_element, "SAK-REF", participant.getSak())

    def setMacSecLocalKayProps(self, element: ET.Element, key: str, props: MacSecLocalKayProps):
        if props is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "DESTINATION-MAC-ADDRESS", props.getDestinationMacAddress())
            self.setChildElementOptionalRefType(child_element, "GLOBAL-KAY-PROPS", props.getGlobalKayProps())
            self.setChildElementOptionalPositiveInteger(child_element, "KEY-SERVER-PRIORITY", props.getKeyServerPriority())
            refs = props.getMkaParticipant()
            if len(refs) > 0:
                refs_element = ET.SubElement(child_element, "MKA-PARTICIPANT-REFS")
                for ref in refs:
                    self.setChildElementOptionalRefType(refs_element, "MKA-PARTICIPANT-REF", ref)
            self.setChildElementOptionalLiteral(child_element, "ROLE", props.getRole())
            self.setChildElementOptionalLiteral(child_element, "SOURCE-MAC-ADDRESS", props.getSourceMacAddress())

    def setMacSecProps(self, element: ET.Element, key: str, props: MacSecProps):
        if props is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalBooleanValue(child_element, "AUTO-START", props.getAutoStart())
            self.setMacSecLocalKayProps(child_element, "MAC-SEC-KAY-CONFIG", props.getMacSecKayConfig())
            self.setChildElementOptionalLiteral(child_element, "ON-FAIL-PERMISSIVE-MODE", props.getOnFailPermissiveMode())
            self.setChildElementOptionalTimeValue(child_element, "ON-FAIL-PERMISSIVE-MODE-TIMEOUT", props.getOnFailPermissiveModeTimeout())
            self.setChildElementOptionalTimeValue(child_element, "SAK-REKEY-TIME-SPAN", props.getSakRekeyTimeSpan())

    def setCouplingPortDetails(self, element: ET.Element, key: str, details: CouplingPortDetails):
        if details is not None:
            child_element = ET.SubElement(element, key)
            self.writeCouplingPortDetailsCouplingPortStructuralElements(child_element, details)
            self.writeCouplingPortDetailsEthernetPriorityRegenerations(child_element, details)
            self.writeCouplingPortDetailsEthernetTrafficClassAssignments(child_element, details)
            self.setGlobalTimeProps(child_element, "GLOBAL-TIME-PROPS", details.getGlobalTimeProps())
            self.setChildElementOptionalRefType(child_element, "LAST-EGRESS-SCHEDULER-REF", details.getLastEgressSchedulerRef())
            self.writeCouplingPortDetailsRatePolicys(child_element, details)

    def setDhcpServerConfiguration(self, element: ET.Element, key: str, config: DhcpServerConfiguration):
        if config is not None:
            child_element = ET.SubElement(element, key)
            self.setIpv4DhcpServerConfiguration(child_element, "IPV-4-DHCP-SERVER-CONFIGURATION", config.getIpv4DhcpServerConfiguration())
            self.setIpv6DhcpServerConfiguration(child_element, "IPV-6-DHCP-SERVER-CONFIGURATION", config.getIpv6DhcpServerConfiguration())

    def setIpv4DhcpServerConfiguration(self, element: ET.Element, key: str, config: Ipv4DhcpServerConfiguration):
        if config is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "ADDRESS-RANGE-LOWER-BOUND", config.getAddressRangeLowerBound())
            self.setChildElementOptionalLiteral(child_element, "ADDRESS-RANGE-UPPER-BOUND", config.getAddressRangeUpperBound())
            self.setChildElementOptionalLiteral(child_element, "DEFAULT-GATEWAY", config.getDefaultGateway())
            self.setChildElementOptionalTimeValue(child_element, "DEFAULT-LEASE-TIME", config.getDefaultLeaseTime())
            addresses = config.getDnsServerAddresses()
            if len(addresses) > 0:
                dns_element = ET.SubElement(child_element, "DNS-SERVER-ADDRESSES")
                for address in addresses:
                    self.setChildElementOptionalLiteral(dns_element, "DNS-SERVER-ADDRESS", address)
            self.setChildElementOptionalLiteral(child_element, "NETWORK-MASK", config.getNetworkMask())

    def setPduActivationRoutingGroup(self, element: ET.Element, group: PduActivationRoutingGroup):
        if group is not None:
            child_element = ET.SubElement(element, "PDU-ACTIVATION-ROUTING-GROUP")
            self.writeIdentifiable(child_element, group)
            self.setChildElementOptionalLiteral(child_element, "EVENT-GROUP-CONTROL-TYPE", group.getEventGroupControlType())
            refs = group.getIPduIdentifierTcpRefs()
            if len(refs) > 0:
                refs_element = ET.SubElement(child_element, "I-PDU-IDENTIFIER-TCP-REFS")
                for ref in refs:
                    self.setChildElementOptionalRefType(refs_element, "I-PDU-IDENTIFIER-TCP-REF", ref)
            refs = group.getIPduIdentifierUdpRefs()
            if len(refs) > 0:
                refs_element = ET.SubElement(child_element, "I-PDU-IDENTIFIER-UDP-REFS")
                for ref in refs:
                    self.setChildElementOptionalRefType(refs_element, "I-PDU-IDENTIFIER-UDP-REF", ref)

    def setStaticSocketConnection(self, element: ET.Element, connection: StaticSocketConnection):
        if connection is not None:
            child_element = ET.SubElement(element, "STATIC-SOCKET-CONNECTION")
            self.writeIdentifiable(child_element, connection)
            refs = connection.getIPduIdentifierRefs()
            if len(refs) > 0:
                refs_element = ET.SubElement(child_element, "I-PDU-IDENTIFIERS")
                for ref in refs:
                    conditional_element = ET.SubElement(refs_element, "SO-CON-I-PDU-IDENTIFIER-REF-CONDITIONAL")
                    self.setChildElementOptionalRefType(conditional_element, "SO-CON-I-PDU-IDENTIFIER-REF", ref)
            if connection.getRemoteAddressRef() is not None:
                remote_element = ET.SubElement(child_element, "REMOTE-ADDRESSS")
                conditional_element = ET.SubElement(remote_element, "SOCKET-ADDRESS-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(conditional_element, "SOCKET-ADDRESS-REF", connection.getRemoteAddressRef())
            self.setChildElementOptionalTimeValue(child_element, "TCP-CONNECT-TIMEOUT", connection.getTcpConnectTimeout())
            self.setChildElementOptionalLiteral(child_element, "TCP-ROLE", connection.getTcpRole())

    def setIpv6DhcpServerConfiguration(self, element: ET.Element, key: str, config: Ipv6DhcpServerConfiguration):
        if config is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "ADDRESS-RANGE-LOWER-BOUND", config.getAddressRangeLowerBound())
            self.setChildElementOptionalLiteral(child_element, "ADDRESS-RANGE-UPPER-BOUND", config.getAddressRangeUpperBound())
            self.setChildElementOptionalLiteral(child_element, "DEFAULT-GATEWAY", config.getDefaultGateway())
            self.setChildElementOptionalTimeValue(child_element, "DEFAULT-LEASE-TIME", config.getDefaultLeaseTime())
            addresses = config.getDnsServerAddresses()
            if len(addresses) > 0:
                dns_element = ET.SubElement(child_element, "DNS-SERVER-ADDRESSES")
                for address in addresses:
                    self.setChildElementOptionalLiteral(dns_element, "DNS-SERVER-ADDRESS", address)
            self.setChildElementOptionalLiteral(child_element, "NETWORK-MASK", config.getNetworkMask())

    def writeVlanMembership(self, element: ET.Element, membership: VlanMembership):
        if membership is not None:
            child_element = ET.SubElement(element, "VLAN-MEMBERSHIP")
            self.setChildElementOptionalLiteral(child_element, "SEND-ACTIVITY", membership.getSendActivity())
            self.setChildElementOptionalRefType(child_element, "VLAN-REF", membership.getVlanRef())
            self.setDhcpServerConfiguration(child_element, "DHCP-ADDRESS-ASSIGNMENT", membership.getDhcpAddressAssignment())

    def writeCouplingPortVlanMemberships(self, element: ET.Element, port: CouplingPort):
        memberships = port.getVlanMemberships()
        if len(memberships) > 0:
            child_element = ET.SubElement(element, "VLAN-MEMBERSHIPS")
            for membership in memberships:
                if isinstance(membership, VlanMembership):
                    self.writeVlanMembership(child_element, membership)
                else:
                    self.notImplemented("Unsupported VlanMembership <%s>" % type(membership))

    def writeCouplingPort(self, element: ET.Element, port: CouplingPort):
        child_element = ET.SubElement(element, "COUPLING-PORT")
        self.writeIdentifiable(child_element, port)
        self.setChildElementOptionalLiteral(child_element, "CONNECTION-NEGOTIATION-BEHAVIOR", port.getConnectionNegotiationBehavior())
        self.setCouplingPortDetails(child_element, "COUPLING-PORT-DETAILS", port.getCouplingPortDetails())
        self.setChildElementOptionalLiteral(child_element, "COUPLING-PORT-ROLE", port.getCouplingPortRole())
        self.setChildElementOptionalRefType(child_element, "DEFAULT-VLAN-REF", port.getDefaultVlanRef())
        self.setChildElementOptionalLiteral(child_element, "MAC-LAYER-TYPE", port.getMacLayerType())

        refs = port.getMacMulticastAddressRefs()
        if len(refs) > 0:
            refs_element = ET.SubElement(child_element, "MAC-MULTICAST-ADDRESS-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_element, "MAC-MULTICAST-ADDRESS-REF", ref)

        for props in port.getMacSecProps():
            self.setMacSecProps(child_element, "MAC-SEC-PROPS", props)
        self.setChildElementOptionalLiteral(child_element, "PHYSICAL-LAYER-TYPE", port.getPhysicalLayerType())
        self.setPlcaProps(child_element, "PLCA-PROPS", port.getPlcaProps())

        refs = port.getPncMappingRefs()
        if len(refs) > 0:
            refs_element = ET.SubElement(child_element, "PNC-MAPPING-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_element, "PNC-MAPPING-REF", ref)
        self.setChildElementOptionalLiteral(child_element, "RECEIVE-ACTIVITY", port.getReceiveActivity())
        self.writeCouplingPortVlanMemberships(child_element, port)
        self.setChildElementOptionalRefType(child_element, "VLAN-MODIFIER-REF", port.getVlanModifierRef())
        self.setChildElementOptionalRefType(child_element, "WAKEUP-SLEEP-ON-DATALINE-CONFIG-REF", port.getWakeupSleepOnDatalineConfigRef())

    def writeEthernetCommunicationControllerCouplingPorts(self, element: ET.Element, controller: EthernetCommunicationController):
        ports = controller.getCouplingPorts()
        if len(ports) > 0:
            child_element = ET.SubElement(element, "COUPLING-PORTS")
            for port in ports:
                if isinstance(port, CouplingPort):
                    self.writeCouplingPort(child_element, port)
                else:
                    self.notImplemented("Unsupported Coupling Port <%s>" % type(port))

    def writeEthernetCommunicationController(self, element: ET.Element, controller: EthernetCommunicationController):
        child_element = ET.SubElement(element, "ETHERNET-COMMUNICATION-CONTROLLER")
        self.logger.debug("Write EthernetCommunicationController %s" % controller.getShortName())
        self.writeIdentifiable(child_element, controller)
        variants_tag = ET.SubElement(child_element, "ETHERNET-COMMUNICATION-CONTROLLER-VARIANTS")
        cond_tag = ET.SubElement(variants_tag, "ETHERNET-COMMUNICATION-CONTROLLER-CONDITIONAL")
        self.writeCommunicationController(cond_tag, controller)
        self.setChildElementOptionalRefType(cond_tag, "CAN-XL-CONFIG-REF", controller.getCanXlConfigRef())
        self.writeEthernetCommunicationControllerCouplingPorts(cond_tag, controller)
        self.setChildElementOptionalLiteral(cond_tag, "MAC-LAYER-TYPE", controller.getMacLayerType())
        self.setChildElementOptionalLiteral(cond_tag, "MAC-UNICAST-ADDRESS", controller.getMacUnicastAddress())
        self.setChildElementOptionalIntegerValue(cond_tag, "MAXIMUM-RECEIVE-BUFFER-LENGTH", controller.getMaximumReceiveBufferLength())
        self.setChildElementOptionalIntegerValue(cond_tag, "MAXIMUM-TRANSMIT-BUFFER-LENGTH", controller.getMaximumTransmitBufferLength())
        self.setChildElementOptionalBooleanValue(cond_tag, "SLAVE-ACT-AS-PASSIVE-COMMUNICATION-SLAVE", controller.getSlaveActAsPassiveCommunicationSlave())

    def writeEcuInstanceCommControllers(self, element: ET.Element, instance: EcuInstance):
        controllers = instance.getCommControllers()
        if len(controllers) > 0:
            child_element = ET.SubElement(element, "COMM-CONTROLLERS")
            for controller in controllers:
                if isinstance(controller, CanCommunicationController):
                    self.writeCanCommunicationController(child_element, controller)
                elif isinstance(controller, EthernetCommunicationController):
                    self.writeEthernetCommunicationController(child_element, controller)
                elif isinstance(controller, LinMaster):
                    self.writeLinMaster(child_element, controller)
                elif isinstance(controller, FlexrayCommunicationController):
                    self.writeFlexrayCommunicationController(child_element, controller)
                else:
                    self.notImplemented("Unsupported Communication Controller <%s>" % type(controller))

    def writeCommunicationConnector(self, element: ET.Element, connector: CommunicationConnector):
        self.writeIdentifiable(element, connector)
        self.setChildElementOptionalRefType(element, "COMM-CONTROLLER-REF", connector.getCommControllerRef())
        self.setChildElementOptionalBooleanValue(element, "CREATE-ECU-WAKEUP-SOURCE", connector.getCreateEcuWakeupSource())
        self.setChildElementOptionalBooleanValue(element, "DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED", connector.getDynamicPncToChannelMappingEnabled())
        self.writeCommunicationConnectorEcuCommPortInstances(element, connector)
        masks = connector.getPncFilterArrayMasks()
        if len(masks) > 0:
            masks_tag = ET.SubElement(element, "PNC-FILTER-ARRAY-MASKS")
            for mask in masks:
                mask_value = PositiveInteger()
                mask_value.setValue(mask)
                self.setChildElementOptionalPositiveInteger(masks_tag, "PNC-FILTER-ARRAY-MASK", mask_value)
        self.setChildElementOptionalLiteral(element, "PNC-GATEWAY-TYPE", connector.getPncGatewayType())

    def writeCanCommunicationConnector(self, element: ET.Element, connector: CanCommunicationConnector):
        self.logger.debug("Write CanCommunicationConnector %s" % connector.getShortName())
        self.writeCommunicationConnector(element, connector)

    def writeEthernetCommunicationConnector(self, element: ET.Element, connector: EthernetCommunicationConnector):
        self.logger.debug("Write EthernetCommunicationConnector %s" % connector.getShortName())
        self.writeCommunicationConnector(element, connector)
        self.setChildElementOptionalRefType(element, "ETH-IP-PROPS-REF", connector.getEthIpPropsRef())
        self.setChildElementOptionalPositiveInteger(element, "MAXIMUM-TRANSMISSION-UNIT", connector.getMaximumTransmissionUnit())
        self.setChildElementOptionalPositiveInteger(element, "NEIGHBOR-CACHE-SIZE", connector.getNeighborCacheSize())
        self.setChildElementOptionalBooleanValue(element, "PATH-MTU-ENABLED", connector.getPathMtuEnabled())
        self.setChildElementOptionalTimeValue(element, "PATH-MTU-TIMEOUT", connector.getPathMtuTimeout())

    def writeLinCommunicationConnector(self, element: ET.Element, connector: LinCommunicationConnector):
        self.logger.debug("Write LinCommunicationConnector %s" % connector.getShortName())
        self.writeCommunicationConnector(element, connector)

    def writeFlexrayCommunicationConnector(self, element: ET.Element, connector: FlexrayCommunicationConnector):
        self.logger.debug("Write FlexrayCommunicationConnector %s" % connector.getShortName())
        self.writeCommunicationConnector(element, connector)

    def writeEcuInstanceConnectors(self, element: ET.Element, instance: EcuInstance):
        connectors = instance.getConnectors()
        if len(connectors) > 0:
            connectors_tag = ET.SubElement(element, "CONNECTORS")
            for connector in connectors:
                if isinstance(connector, CanCommunicationConnector):
                    child_element = ET.SubElement(connectors_tag, "CAN-COMMUNICATION-CONNECTOR")
                    self.writeCanCommunicationConnector(child_element, connector)
                elif isinstance(connector, EthernetCommunicationConnector):
                    child_element = ET.SubElement(connectors_tag, "ETHERNET-COMMUNICATION-CONNECTOR")
                    self.writeEthernetCommunicationConnector(child_element, connector)
                elif isinstance(connector, LinCommunicationConnector):
                    child_element = ET.SubElement(connectors_tag, "LIN-COMMUNICATION-CONNECTOR")
                    self.writeLinCommunicationConnector(child_element, connector)
                elif isinstance(connector, FlexrayCommunicationConnector):
                    child_element = ET.SubElement(connectors_tag, "FLEXRAY-COMMUNICATION-CONNECTOR")
                    self.writeFlexrayCommunicationConnector(child_element, connector)
                else:
                    self.notImplemented("Unsupported Communication connector <%s>" % type(connector))

    def writeEcuInstanceAssociatedComIPduGroupRefs(self, element: ET.Element, instance: EcuInstance):
        refs = instance.getAssociatedComIPduGroupRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "ASSOCIATED-COM-I-PDU-GROUP-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "ASSOCIATED-COM-I-PDU-GROUP-REF", ref)

    def writeEcuInstanceAssociatedConsumedProvidedServiceInstanceGroupRefs(self, element: ET.Element, instance: EcuInstance):
        refs = instance.getAssociatedConsumedProvidedServiceInstanceGroupRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "ASSOCIATED-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "ASSOCIATED-CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF", ref)

    def writeEcuInstanceAssociatedPdurIPduGroupRefs(self, element: ET.Element, instance: EcuInstance):
        refs = instance.getAssociatedPdurIPduGroupRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "ASSOCIATED-PDUR-I-PDU-GROUP-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "ASSOCIATED-PDUR-I-PDU-GROUP-REF", ref)

    def writeEcuInstanceEcuTaskProxyRefs(self, element: ET.Element, instance: EcuInstance):
        refs = instance.getEcuTaskProxyRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "ECU-TASK-PROXY-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "ECU-TASK-PROXY-REF", ref)

    def writeEcuInstanceFirewallRuleRefs(self, element: ET.Element, instance: EcuInstance):
        refs = instance.getFirewallRuleRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "FIREWALL-RULE-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "FIREWALL-RULE-REF", ref)

    def writeEcuInstance(self, element: ET.Element, instance: EcuInstance):
        self.logger.debug("EcuInstance %s" % instance.getShortName())
        child_element = ET.SubElement(element, "ECU-INSTANCE")
        self.writeIdentifiable(child_element, instance)
        self.writeEcuInstanceAssociatedComIPduGroupRefs(child_element, instance)
        self.writeEcuInstanceAssociatedConsumedProvidedServiceInstanceGroupRefs(child_element, instance)
        self.writeEcuInstanceAssociatedPdurIPduGroupRefs(child_element, instance)
        self.setChildElementOptionalBooleanValue(child_element, "CHANNEL-SYNCHRONOUS-WAKEUP", instance.getChannelSynchronousWakeup())
        self.setChildElementOptionalTimeValue(child_element, "COM-CONFIGURATION-GW-TIME-BASE", instance.getComConfigurationGwTimeBase())
        self.setChildElementOptionalTimeValue(child_element, "COM-CONFIGURATION-RX-TIME-BASE", instance.getComConfigurationRxTimeBase())
        self.setChildElementOptionalTimeValue(child_element, "COM-CONFIGURATION-TX-TIME-BASE", instance.getComConfigurationTxTimeBase())
        self.setChildElementOptionalBooleanValue(child_element, "COM-ENABLE-MDT-FOR-CYCLIC-TRANSMISSION", instance.getComEnableMDTForCyclicTransmission())  # noqa E501
        self.writeEcuInstanceCommControllers(child_element, instance)
        self.writeEcuInstanceConnectors(child_element, instance)
        self.writeEcuInstanceEcuTaskProxyRefs(child_element, instance)
        self.setChildElementOptionalBooleanValue(child_element, "ETH-SWITCH-PORT-GROUP-DERIVATION", instance.getEthSwitchPortGroupDerivation())
        self.writeEcuInstanceFirewallRuleRefs(child_element, instance)
        self.setChildElementOptionalBooleanValue(child_element, "PNC-NM-REQUEST", instance.getPncNmRequest())
        self.setChildElementOptionalTimeValue(child_element, "PNC-PREPARE-SLEEP-TIMER", instance.getPncPrepareSleepTimer())
        self.setChildElementOptionalBooleanValue(child_element, "PNC-SYNCHRONOUS-WAKEUP", instance.getPncSynchronousWakeup())
        self.setChildElementOptionalTimeValue(child_element, "PN-RESET-TIME", instance.getPnResetTime())
        self.setChildElementOptionalBooleanValue(child_element, "SLEEP-MODE-SUPPORTED", instance.getSleepModeSupported())
        self.setChildElementOptionalRefType(child_element, "TCP-IP-ICMP-PROPS", instance.getTcpIpIcmpPropsRef())
        self.setChildElementOptionalRefType(child_element, "TCP-IP-PROPS", instance.getTcpIpPropsRef())
        self.setChildElementOptionalLiteral(child_element, "V-2-X-SUPPORTED", instance.getV2xSupported())
        self.setChildElementOptionalBooleanValue(child_element, "WAKE-UP-OVER-BUS-SUPPORTED", instance.getWakeUpOverBusSupported())

    def writeSystemSignalGroup(self, element: ET.Element, group: SystemSignalGroup):
        self.logger.debug("Write SystemSignalGroup %s" % group.getShortName())
        child_element = ET.SubElement(element, "SYSTEM-SIGNAL-GROUP")
        self.writeIdentifiable(child_element, group)
        signal_refs = group.getSystemSignalRefs()
        if len(signal_refs) > 0:
            signal_refs_tag = ET.SubElement(child_element, "SYSTEM-SIGNAL-REFS")
            for signal_ref in signal_refs:
                self.setChildElementOptionalRefType(signal_refs_tag, "SYSTEM-SIGNAL-REF", signal_ref)
        self.setChildElementOptionalRefType(child_element, "TRANSFORMING-SYSTEM-SIGNAL-REF", group.getTransformingSystemSignalRef())

    def writeSenderReceiverToSignalMapping(self, element: ET.Element, mapping: SenderReceiverToSignalMapping):
        child_element = ET.SubElement(element, "SENDER-RECEIVER-TO-SIGNAL-MAPPING")
        self.setChildElementOptionalLiteral(child_element, "COMMUNICATION-DIRECTION", mapping.getCommunicationDirection())
        self.setVariableDataPrototypeInSystemInstanceRef(child_element, "DATA-ELEMENT-IREF", mapping.getDataElementIRef())
        self.setChildElementOptionalRefType(child_element, "SYSTEM-SIGNAL-REF", mapping.getSystemSignalRef())

    def writeSenderRecCompositeTypeMapping(self, element: ET.Element, mapping: SenderRecCompositeTypeMapping):
        self.writeARObjectAttributes(element, mapping)

    def writeSenderRecRecordElementMapping(self, element: ET.Element, mapping: SenderRecRecordElementMapping):
        if mapping is not None:
            child_element = ET.SubElement(element, "SENDER-REC-RECORD-ELEMENT-MAPPING")
            self.writeARObjectAttributes(child_element, mapping)
            self.setChildElementOptionalRefType(child_element, "APPLICATION-RECORD-ELEMENT-REF", mapping.getApplicationRecordElementRef())
            self.setChildElementOptionalRefType(child_element, "IMPLEMENTATION-RECORD-ELEMENT-REF", mapping.getImplementationRecordElementRef())
            self.setChildElementOptionalRefType(child_element, "SYSTEM-SIGNAL-REF", mapping.getSystemSignalRef())

    def writeSenderRecArrayTypeMappingRecordElementMapping(self, element: ET.Element, mapping: SenderRecRecordTypeMapping):
        record_element_mappings = mapping.getRecordElementMappings()
        if len(record_element_mappings) > 0:
            child_element = ET.SubElement(element, "RECORD-ELEMENT-MAPPINGS")
            for record_element_mapping in record_element_mappings:
                if isinstance(record_element_mapping, SenderRecRecordElementMapping):
                    self.writeSenderRecRecordElementMapping(child_element, record_element_mapping)
                else:
                    self.notImplemented("Unsupported RecordElementMapping %s" % type(record_element_mapping))

    def writeSenderRecRecordTypeMapping(self, element: ET.Element, mapping: SenderRecRecordTypeMapping):
        if mapping is not None:
            child_element = ET.SubElement(element, "SENDER-REC-RECORD-TYPE-MAPPING")
            self.writeSenderRecCompositeTypeMapping(child_element, mapping)
            self.writeSenderRecArrayTypeMappingRecordElementMapping(child_element, mapping)

    def writeSenderReceiverToSignalGroupMappingTypeMapping(self, element: ET.Element, mapping: SenderReceiverToSignalGroupMapping):
        type_mapping = mapping.getTypeMapping()
        if type_mapping is not None:
            child_element = ET.SubElement(element, "TYPE-MAPPING")
            if isinstance(type_mapping, SenderRecRecordTypeMapping):
                self.writeSenderRecRecordTypeMapping(child_element, type_mapping)
            else:
                self.notImplemented("Unsupported Type Mapping %s" % type(type_mapping))

    def writeSenderReceiverToSignalGroupMapping(self, element: ET.Element, mapping: SenderReceiverToSignalGroupMapping):
        child_element = ET.SubElement(element, "SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING")
        self.setVariableDataPrototypeInSystemInstanceRef(child_element, "DATA-ELEMENT-IREF", mapping.getDataElementIRef())
        self.setChildElementOptionalRefType(child_element, "SIGNAL-GROUP-REF", mapping.getSignalGroupRef())
        self.writeSenderReceiverToSignalGroupMappingTypeMapping(child_element, mapping)

    def writeSystemMappingDataMappings(self, element: ET.Element, system_mapping: SystemMapping):
        data_mappings = system_mapping.getDataMappings()
        if len(data_mappings) > 0:
            child_element = ET.SubElement(element, "DATA-MAPPINGS")
            for data_mapping in data_mappings:
                if isinstance(data_mapping, SenderReceiverToSignalMapping):
                    self.writeSenderReceiverToSignalMapping(child_element, data_mapping)
                elif isinstance(data_mapping, SenderReceiverToSignalGroupMapping):
                    self.writeSenderReceiverToSignalGroupMapping(child_element, data_mapping)
                else:
                    self.notImplemented("Unsupported Data Mapping %s" % type(data_mapping))

    def setSwcToEcuMapping(self, element: ET.Element, mapping: SwcToEcuMapping):
        child_element = ET.SubElement(element, "SWC-TO-ECU-MAPPING")
        self.writeIdentifiable(child_element, mapping)
        irefs = mapping.getComponentIRefs()
        if len(irefs) > 0:
            irefs_tag = ET.SubElement(child_element, "COMPONENT-IREFS")
            for iref in irefs:
                self.setComponentInSystemInstanceRef(irefs_tag, "COMPONENT-IREF", iref)
        self.setChildElementOptionalRefType(child_element, "ECU-INSTANCE-REF", mapping.getEcuInstanceRef())

    def writeSystemMappingSwMappings(self, element: ET.Element, system_mapping: SystemMapping):
        sw_mappings = system_mapping.getSwMappings()
        if len(sw_mappings) > 0:
            child_element = ET.SubElement(element, "SW-MAPPINGS")
            for sw_mapping in sw_mappings:
                if isinstance(sw_mapping, SwcToEcuMapping):
                    self.setSwcToEcuMapping(child_element, sw_mapping)
                else:
                    self.notImplemented("Unsupported Sw Mapping %s" % type(sw_mapping))

    def writeEcuMapping(self, element: ET.Element, mapping: ECUMapping):
        self.logger.debug("Write ECUMapping <%s>" % mapping.getShortName())
        if mapping is not None:
            child_element = ET.SubElement(element, "ECU-MAPPING")
            self.writeIdentifiable(child_element, mapping)
            self.setChildElementOptionalRefType(child_element, "ECU-INSTANCE-REF", mapping.getEcuInstanceRef())
            self.setChildElementOptionalRefType(child_element, "ECU-REF", mapping.getEcuRef())

    def writeSystemMappingEcuResourceMappings(self, element: ET.Element, mapping: SystemMapping):
        ecu_resource_mappings = mapping.getEcuResourceMappings()
        if len(ecu_resource_mappings) > 0:
            child_element = ET.SubElement(element, "ECU-RESOURCE-MAPPINGS")
            for ecu_resource_mapping in ecu_resource_mappings:
                if isinstance(ecu_resource_mapping, ECUMapping):
                    self.writeEcuMapping(child_element, ecu_resource_mapping)
                else:
                    self.notImplemented("Unsupported Sw Mapping %s" % type(ecu_resource_mapping))

    def writeSwcToImplMapping(self, element: ET.Element, mapping: SwcToImplMapping):
        if mapping is not None:
            child_element = ET.SubElement(element, "SWC-TO-IMPL-MAPPING")
            self.writeIdentifiable(child_element, mapping)
            self.setChildElementOptionalRefType(child_element, "COMPONENT-IMPLEMENTATION-REF", mapping.getComponentImplementationRef())
            irefs = mapping.getComponentIRefs()
            if len(irefs) > 0:
                irefs_tag = ET.SubElement(child_element, "COMPONENT-IREFS")
                for iref in irefs:
                    self.setComponentInSystemInstanceRef(irefs_tag, "COMPONENT-IREF", iref)

    def writeSystemMappingSwImplMappings(self, element: ET.Element, mapping: SystemMapping):
        sw_impl_mappings = mapping.getSwImplMappings()
        if len(sw_impl_mappings) > 0:
            child_element = ET.SubElement(element, "SW-IMPL-MAPPINGS")
            for sw_impl_mapping in sw_impl_mappings:
                if isinstance(sw_impl_mapping, SwcToImplMapping):
                    self.writeSwcToImplMapping(child_element, sw_impl_mapping)
                else:
                    self.notImplemented("Unsupported SwImplMapping <%s>" % type(sw_impl_mapping))

    def writeSystemMapping(self, element: ET.Element, mapping: SystemMapping):
        self.logger.debug("Write SystemMapping <%s>" % mapping.getShortName())
        child_element = ET.SubElement(element, "SYSTEM-MAPPING")
        self.writeIdentifiable(child_element, mapping)
        self.writeSystemMappingDataMappings(child_element, mapping)
        self.writeSystemMappingEcuResourceMappings(child_element, mapping)
        self.writeSystemMappingSwImplMappings(child_element, mapping)
        self.writeSystemMappingSwMappings(child_element, mapping)

    def writeSystemMappings(self, element: ET.Element, system: System):
        mappings = system.getMappings()
        if len(mappings) > 0:
            mappings_tag = ET.SubElement(element, "MAPPINGS")
            for mapping in mappings:
                if isinstance(mapping, SystemMapping):
                    self.writeSystemMapping(mappings_tag, mapping)
                else:
                    self.notImplemented("Unsupported Mapping %s" % type(mapping))

    def writeRootSwCompositionPrototype(self, element: ET.Element, system: System):
        prototype = system.getRootSoftwareComposition()
        if prototype is not None:
            self.logger.debug("Write RootSwCompositionPrototype <%s>" % prototype.getShortName())
            child_element = ET.SubElement(element, "ROOT-SOFTWARE-COMPOSITIONS")
            child_element = ET.SubElement(child_element, "ROOT-SW-COMPOSITION-PROTOTYPE")
            self.writeIdentifiable(child_element, prototype)
            calibration_refs = prototype.getCalibrationParameterValueSetRefs()
            if len(calibration_refs) > 0:
                calibration_wrapper = ET.SubElement(child_element, "CALIBRATION-PARAMETER-VALUE-SET-REFS")
                for ref in calibration_refs:
                    self.setChildElementOptionalRefType(calibration_wrapper, "CALIBRATION-PARAMETER-VALUE-SET-REF", ref)
            self.setChildElementOptionalRefType(child_element, "FLAT-MAP-REF", prototype.getFlatMapRef())
            self.setChildElementOptionalRefType(child_element, "SOFTWARE-COMPOSITION-TREF", prototype.getSoftwareCompositionTRef())

    def writeSystemFibexElementRefs(self, element: ET.Element, system: System):
        refs = system.getFibexElementRefs()
        if len(refs) > 0:
            fibex_elements_tag = ET.SubElement(element, "FIBEX-ELEMENTS")
            for ref in refs:
                child_element = ET.SubElement(fibex_elements_tag, "FIBEX-ELEMENT-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "FIBEX-ELEMENT-REF", ref)

    def writeSystem(self, element: ET.Element, system: System):
        self.logger.debug("Write System %s" % system.getShortName())
        child_element = ET.SubElement(element, "SYSTEM")
        self.writeARElement(child_element, system)
        self.setChildElementOptionalLiteral(child_element, "ECU-EXTRACT-VERSION", system.getEcuExtractVersion())
        self.writeSystemFibexElementRefs(child_element, system)
        self.writeSystemMappings(child_element, system)
        self.writeRootSwCompositionPrototype(child_element, system)
        self.setChildElementOptionalRevisionLabelString(child_element, "SYSTEM-VERSION", system.getSystemVersion())

    def writePhysicalDimension(self, element: ET.Element, dimension: PhysicalDimension):
        self.logger.debug("Set PhysicalDimension %s" % dimension.getShortName())
        child_element = ET.SubElement(element, "PHYSICAL-DIMENSION")
        self.writeARElement(child_element, dimension)
        self.setChildElementOptionalNumericalValue(child_element, "LENGTH-EXP", dimension.getLengthExp())
        self.setChildElementOptionalNumericalValue(child_element, "LUMINOUS-INTENSITY-EXP", dimension.getLuminousIntensityExp())
        self.setChildElementOptionalNumericalValue(child_element, "MASS-EXP", dimension.getMassExp())
        self.setChildElementOptionalNumericalValue(child_element, "MOLAR-AMOUNT-EXP", dimension.getMolarAmountExp())
        self.setChildElementOptionalNumericalValue(child_element, "TEMPERATURE-EXP", dimension.getTemperatureExp())
        self.setChildElementOptionalNumericalValue(child_element, "TIME-EXP", dimension.getTimeExp())
        self.setChildElementOptionalNumericalValue(child_element, "CURRENT-EXP", dimension.getCurrentExp())

    def setFlatInstanceDescriptor(self, element: ET.Element, desc: FlatInstanceDescriptor):
        self.logger.debug("Set FlatInstanceDescriptor %s" % desc.getShortName())
        child_element = ET.SubElement(element, "FLAT-INSTANCE-DESCRIPTOR")
        self.writeIdentifiable(child_element, desc)
        self.setAnyInstanceRef(child_element, "UPSTREAM-REFERENCE-IREF", desc.getUpstreamReferenceIRef())
        self.setAnyInstanceRef(child_element, "ECU-EXTRACT-REFERENCE-IREF", desc.getEcuExtractReferenceIRef())

    def writeFlatMapInstances(self, element: ET.Element, map: FlatMap):
        instances = map.getInstances()
        if len(instances) > 0:
            child_element = ET.SubElement(element, "INSTANCES")
            for instance in instances:
                if isinstance(instance, FlatInstanceDescriptor):
                    self.setFlatInstanceDescriptor(child_element, instance)
                else:
                    self.notImplemented("Unsupported Flat Map Instances <%s>" % type(instance))

    def writeFlatMap(self, element: ET.Element, map: FlatMap):
        self.logger.debug("Set FlatMap %s" % map.getShortName())
        child_element = ET.SubElement(element, "FLAT-MAP")
        self.writeARElement(child_element, map)
        self.writeFlatMapInstances(child_element, map)

    def setDataPrototypeMapping(self, element: ET.Element, mapping: DataPrototypeMapping):
        child_element = ET.SubElement(element, "DATA-PROTOTYPE-MAPPING")
        self.setChildElementOptionalRefType(child_element, "FIRST-DATA-PROTOTYPE-REF", mapping.getFirstDataPrototypeRef())
        self.setChildElementOptionalRefType(child_element, "FIRST-TO-SECOND-DATA-TRANSFORMATION-REF", mapping.getFirstToSecondDataTransformationRef())
        self.setChildElementOptionalRefType(child_element, "SECOND-DATA-PROTOTYPE-REF", mapping.getSecondDataPrototypeRef())
        self.setChildElementOptionalRefType(child_element, "SECOND-TO-FIRST-DATA-TRANSFORMATION-REF", mapping.getSecondToFirstDataTransformationRef())
        sub_elements = mapping.getSubElementMappings()
        if len(sub_elements) > 0:
            sub_tag = ET.SubElement(child_element, "SUB-ELEMENT-MAPPINGS")
            for sub_element in sub_elements:
                self.setSubElementMapping(sub_tag, sub_element)
        text_tables = mapping.getTextTableMappings()
        if len(text_tables) > 0:
            text_tag = ET.SubElement(child_element, "TEXT-TABLE-MAPPINGS")
            for text_table in text_tables:
                self.setTextTableMapping(text_tag, text_table)

    def setSubElementMapping(self, element: ET.Element, mapping: SubElementMapping):
        child_element = ET.SubElement(element, "SUB-ELEMENT-MAPPING")
        first = mapping.getFirstElement()
        if first is not None:
            first_tag = ET.SubElement(child_element, "FIRST-ELEMENTS")
            iref_tag = ET.SubElement(first_tag, "APPLICATION-COMPOSITE-DATA-TYPE-SUB-ELEMENT-REF")
            self.setApplicationCompositeElementInPortInterfaceInstanceRef(iref_tag, "APPLICATION-COMPOSITE-ELEMENT-IREF", first)
        second = mapping.getSecondElement()
        if second is not None:
            second_tag = ET.SubElement(child_element, "SECOND-ELEMENTS")
            iref_tag = ET.SubElement(second_tag, "APPLICATION-COMPOSITE-DATA-TYPE-SUB-ELEMENT-REF")
            self.setApplicationCompositeElementInPortInterfaceInstanceRef(iref_tag, "APPLICATION-COMPOSITE-ELEMENT-IREF", second)
        text_tables = mapping.getTextTableMappings()
        if len(text_tables) > 0:
            text_tag = ET.SubElement(child_element, "TEXT-TABLE-MAPPINGS")
            for text_table in text_tables:
                self.setTextTableMapping(text_tag, text_table)

    def setTextTableMapping(self, element: ET.Element, mapping: TextTableMapping):
        child_element = ET.SubElement(element, "TEXT-TABLE-MAPPING")
        self.setChildElementOptionalPositiveInteger(child_element, "BITFIELD-TEXT-TABLE-MASK-FIRST", mapping.getBitfieldTextTableMaskFirst())
        self.setChildElementOptionalPositiveInteger(child_element, "BITFIELD-TEXT-TABLE-MASK-SECOND", mapping.getBitfieldTextTableMaskSecond())
        self.setChildElementOptionalBooleanValue(child_element, "IDENTICAL-MAPPING", mapping.getIdenticalMapping())
        self.setChildElementOptionalLiteral(child_element, "MAPPING-DIRECTION", mapping.getMappingDirection())

    def setDataPrototypeMappings(self, element: ET.Element, key: str, mappings: List[DataPrototypeMapping]):
        if len(mappings) > 0:
            child_element = ET.SubElement(element, key)
            for mapping in mappings:
                self.setDataPrototypeMapping(child_element, mapping)

    def writeVariableAndParameterInterfaceMapping(self, element: ET.Element, mapping: VariableAndParameterInterfaceMapping):
        # self.logger.debug("Write VariableAndParameterInterfaceMapping %s" % mapping.getShortName())
        child_element = ET.SubElement(element, "VARIABLE-AND-PARAMETER-INTERFACE-MAPPING")
        self.writeIdentifiable(child_element, mapping)
        self.setDataPrototypeMappings(child_element, "DATA-MAPPINGS", mapping.getDataMappings())

    def writeClientServerOperationMapping(self, element: ET.Element, mapping: ClientServerOperationMapping):
        child_element = ET.SubElement(element, "CLIENT-SERVER-OPERATION-MAPPING")
        self.setChildElementOptionalRefType(child_element, "FIRST-OPERATION-REF", mapping.getFirstOperationRef())
        self.setChildElementOptionalRefType(child_element, "SECOND-OPERATION-REF", mapping.getSecondOperationRef())

    def writeClientServerInterfaceMappingOperationMappings(self, element: ET.Element, mapping: ClientServerInterfaceMapping):
        operation_mappings = mapping.getOperationMappings()
        if len(operation_mappings) > 0:
            child_element = ET.SubElement(element, "OPERATION-MAPPINGS")
            for operation_mapping in operation_mappings:
                if isinstance(operation_mapping, ClientServerOperationMapping):
                    self.writeClientServerOperationMapping(child_element, operation_mapping)
                else:
                    self.notImplemented("Unsupported Operation Mapping <%s>" % type(operation_mapping))

    def writeClientServerInterfaceMapping(self, element: ET.Element, mapping: ClientServerInterfaceMapping):
        # self.logger.debug("Read ClientServerInterfaceMapping %s" % mapping.getShortName())
        if mapping is not None:
            child_element = ET.SubElement(element, "CLIENT-SERVER-INTERFACE-MAPPING")
            self.writeIdentifiable(child_element, mapping)
            self.writeClientServerInterfaceMappingOperationMappings(child_element, mapping)

    def writeModeInterfaceMappingModeMapping(self, element: ET.Element, mapping: ModeInterfaceMapping):
        mode_mapping = mapping.getModeMapping()
        if mode_mapping is not None:
            child_element = ET.SubElement(element, "MODE-MAPPING")
            self.setChildElementOptionalRefType(child_element, "FIRST-MODE-GROUP-REF", mode_mapping.getFirstModeGroupRef())
            self.setChildElementOptionalRefType(child_element, "MODE-DECLARATION-MAPPING-SET-REF", mode_mapping.getModeDeclarationMappingSetRef())
            self.setChildElementOptionalRefType(child_element, "SECOND-MODE-GROUP-REF", mode_mapping.getSecondModeGroupRef())

    def writeModeInterfaceMapping(self, element: ET.Element, mapping: ModeInterfaceMapping):
        # self.logger.debug("Read ClientServerInterfaceMapping %s" % mapping.getShortName())
        if mapping is not None:
            child_element = ET.SubElement(element, "MODE-INTERFACE-MAPPING")
            self.writeIdentifiable(child_element, mapping)
            self.writeModeInterfaceMappingModeMapping(child_element, mapping)

    def writePortInterfaceMappings(self, element: ET.Element, mapping_set: PortInterfaceMappingSet):
        mappings = mapping_set.getPortInterfaceMappings()
        if len(mappings) > 0:
            child_element = ET.SubElement(element, "PORT-INTERFACE-MAPPINGS")
            for mapping in mappings:
                if isinstance(mapping, VariableAndParameterInterfaceMapping):
                    self.writeVariableAndParameterInterfaceMapping(child_element, mapping)
                elif isinstance(mapping, ClientServerInterfaceMapping):
                    self.writeClientServerInterfaceMapping(child_element, mapping)
                elif isinstance(mapping, ModeInterfaceMapping):
                    self.writeModeInterfaceMapping(child_element, mapping)
                else:
                    self.notImplemented("Unsupported PortInterfaceMapping <%s>" % type(mapping))

    def writePortInterfaceMappingSet(self, element: ET.Element, mapping_set: PortInterfaceMappingSet):
        self.logger.debug("Set PortInterfaceMappingSet %s" % mapping_set.getShortName())
        child_element = ET.SubElement(element, "PORT-INTERFACE-MAPPING-SET")
        self.writeARElement(child_element, mapping_set)
        self.writePortInterfaceMappings(child_element, mapping_set)

    def setISignalMappings(self, element: ET.Element, mappings: List[ISignalMapping]):
        if len(mappings) > 0:
            mappings_tag = ET.SubElement(element, "SIGNAL-MAPPINGS")
            for mapping in mappings:
                child_element = ET.SubElement(mappings_tag, "I-SIGNAL-MAPPING")
                self.setChildElementOptionalRefType(child_element, "SOURCE-SIGNAL-REF", mapping.getSourceSignalRef())
                self.setChildElementOptionalRefType(child_element, "TARGET-SIGNAL-REF", mapping.getTargetSignalRef())

    def setTargetIPduRef(self, element: ET.Element, key: str, i_pdu_ref: TargetIPduRef):
        if i_pdu_ref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "TARGET-I-PDU-REF", i_pdu_ref.getTargetIPdu())

    def setIPduMappings(self, element: ET.Element, mappings: List[IPduMapping]):
        if len(mappings) > 0:
            mappings_tag = ET.SubElement(element, "I-PDU-MAPPINGS")
            for mapping in mappings:
                child_element = ET.SubElement(mappings_tag, "I-PDU-MAPPING")
                self.setChildElementOptionalRefType(child_element, "SOURCE-I-PDU-REF", mapping.getSourceIpduRef())
                self.setTargetIPduRef(child_element, "TARGET-I-PDU", mapping.getTargetIPdu())

    def writeGateway(self, element: ET.Element, gateway: Gateway):
        self.logger.debug("Gateway %s" % gateway.getShortName())
        child_element = ET.SubElement(element, "GATEWAY")
        self.writeIdentifiable(child_element, gateway)
        self.setChildElementOptionalRefType(child_element, "ECU-REF", gateway.ecuRef)
        self.setIPduMappings(child_element, gateway.getIPduMappings())
        self.setISignalMappings(child_element, gateway.getSignalMappings())

    def writeISignal(self, element: ET.Element, signal: ISignal):
        self.logger.debug("ISignal %s" % signal.getShortName())
        child_element = ET.SubElement(element, "I-SIGNAL")
        self.writeIdentifiable(child_element, signal)
        self.writeISignalDataTransformation(child_element, signal)
        self.setChildElementOptionalLiteral(child_element, "DATA-TYPE-POLICY", signal.getDataTypePolicy())
        self.setChildElementOptionalLiteral(child_element, "I-SIGNAL-TYPE", signal.getISignalType())
        self.setChildValueSpecification(child_element, "INIT-VALUE", signal.getInitValue())
        self.setChildElementOptionalNumericalValue(child_element, "LENGTH", signal.getLength())
        self.setSwDataDefProps(child_element, "NETWORK-REPRESENTATION-PROPS", signal.getNetworkRepresentationProps())
        self.setChildElementOptionalRefType(child_element, "SYSTEM-SIGNAL-REF", signal.getSystemSignalRef())
        self.setChildValueSpecification(child_element, "TIMEOUT-SUBSTITUTION-VALUE", signal.getTimeoutSubstitutionValue())
        self.writeISignalProps(child_element, signal)
        self.writeISignalTransformationISignalProps(child_element, signal)

    def writeISignalProps(self, element: ET.Element, signal: ISignal):
        props = signal.getISignalProps()
        if props is not None:
            child_element = ET.SubElement(element, "I-SIGNAL-PROPS")
            self.setChildElementOptionalLiteral(child_element, "HANDLE-OUT-OF-RANGE", props.getHandleOutOfRange())

    def writeISignalDataTransformation(self, element: ET.Element, signal: ISignal):
        data_transformation_ref = signal.getDataTransformationRef()
        if data_transformation_ref is not None:
            child_element = ET.SubElement(element, "DATA-TRANSFORMATIONS")
            ref_conditional_element = ET.SubElement(child_element, "DATA-TRANSFORMATION-REF-CONDITIONAL")
            self.setChildElementOptionalRefType(ref_conditional_element, "DATA-TRANSFORMATION-REF", data_transformation_ref)

    def writeISignalTransformationISignalProps(self, element: ET.Element, signal: ISignal):
        props_list = signal.getTransformationISignalProps()
        if len(props_list) > 0:
            child_element = ET.SubElement(element, "TRANSFORMATION-I-SIGNAL-PROPSS")
            for props in props_list:
                if isinstance(props, EndToEndTransformationISignalProps):
                    self.writeEndToEndTransformationISignalProps(child_element, props)
                else:
                    self.notImplemented("Unsupported TransformationISignalProps %s" % type(props))

    def writeEcucValueCollectionEcucValues(self, element: ET.Element, collection: EcucValueCollection):
        value_refs = collection.getEcucValueRefs()
        if len(value_refs) > 0:
            ecuc_values_tag = ET.SubElement(element, "ECUC-VALUES")
            for value_ref in value_refs:
                child_element = ET.SubElement(ecuc_values_tag, "ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "ECUC-MODULE-CONFIGURATION-VALUES-REF", value_ref)

    def writeEcucValueCollection(self, element: ET.Element, collection: EcucValueCollection):
        self.logger.debug("EcucValueCollection %s" % collection.getShortName())
        child_element = ET.SubElement(element, "ECUC-VALUE-COLLECTION")
        self.writeIdentifiable(child_element, collection)
        self.setChildElementOptionalRefType(child_element, "ECU-EXTRACT-REF", collection.getEcuExtractRef())
        self.writeEcucValueCollectionEcucValues(child_element, collection)

    def writeEcucContainerValueSubContainers(self, element: ET.Element, container: EcucContainerValue):
        sub_containers = container.getSubContainers()
        if len(sub_containers) > 0:
            sub_containers_tag = ET.SubElement(element, "SUB-CONTAINERS")
            for sub_container in sub_containers:
                if isinstance(sub_container, EcucContainerValue):
                    self.writeEcucContainValue(sub_containers_tag, sub_container)
                else:
                    self.notImplemented("Unsupported Sub Container %s" % type(container))

    def writeEcucParameterValue(self, element: ET.Element, param_value: EcucParameterValue):
        self.setChildElementOptionalRefType(element, "DEFINITION-REF", param_value.getDefinition())
        self.setChildElementOptionalPositiveInteger(element, "INDEX", param_value.getIndex())
        self.setAnnotations(element, param_value.getAnnotations())
        self.setChildElementOptionalBooleanValue(element, "IS-AUTO-VALUE", param_value.getIsAutoValue())

    def setEcucTextualParamValue(self, element: ET.Element, param_value: EcucTextualParamValue):
        child_element = ET.SubElement(element, "ECUC-TEXTUAL-PARAM-VALUE")
        self.writeEcucParameterValue(child_element, param_value)
        self.setChildElementOptionalLiteral(child_element, "VALUE", param_value.getValue())

    def setEcucNumericalParamValue(self, element: ET.Element, param_value: EcucNumericalParamValue):
        child_element = ET.SubElement(element, "ECUC-NUMERICAL-PARAM-VALUE")
        self.writeEcucParameterValue(child_element, param_value)
        self.setChildElementOptionalNumerical(child_element, "VALUE", param_value.getValue())

    def setEcucAddInfoParamValue(self, element: ET.Element, param_value: EcucAddInfoParamValue):
        child_element = ET.SubElement(element, "ECUC-ADD-INFO-PARAM-VALUE")
        self.writeEcucParameterValue(child_element, param_value)
        self.writeDocumentationBlock(child_element, "VALUE", param_value.getValue())

    def writeEcucContainerValueParameterValues(self, element: ET.Element, container_value: EcucContainerValue):
        param_values = container_value.getParameterValues()
        if len(param_values) > 0:
            child_element = ET.SubElement(element, "PARAMETER-VALUES")
            for param_value in param_values:
                if isinstance(param_value, EcucTextualParamValue):
                    self.setEcucTextualParamValue(child_element, param_value)
                elif isinstance(param_value, EcucNumericalParamValue):
                    self.setEcucNumericalParamValue(child_element, param_value)
                elif isinstance(param_value, EcucAddInfoParamValue):
                    self.setEcucAddInfoParamValue(child_element, param_value)
                else:
                    self.notImplemented("Unsupported EcucParameterValue <%s>" % type(param_value))

    def writeEcucAbstractReferenceValue(self, element: ET.Element, value: EcucAbstractReferenceValue):
        self.setChildElementOptionalRefType(element, "DEFINITION-REF", value.getDefinitionRef())
        self.setChildElementOptionalPositiveInteger(element, "INDEX", value.getIndex())
        self.setAnnotations(element, value.getAnnotations())
        self.setChildElementOptionalBooleanValue(element, "IS-AUTO-VALUE", value.getIsAutoValue())

    def setEcucReferenceValue(self, element: ET.Element, value=None):
        if value is not None:
            child_element = ET.SubElement(element, "ECUC-REFERENCE-VALUE")
            self.writeEcucAbstractReferenceValue(child_element, value)
            self.setChildElementOptionalRefType(child_element, "VALUE-REF", value.getValueRef())
            if len(child_element) == 0:
                element.remove(child_element)
        return value

    def setAnyInstanceRef(self, element: ET.Element, key, instance_ref: AnyInstanceRef):
        if instance_ref is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "BASE-REF", instance_ref.getBaseRef())
            for ref in instance_ref.getContextElementRefs():
                self.setChildElementOptionalRefType(child_element, "CONTEXT-ELEMENT-REF", ref)
            self.setChildElementOptionalRefType(child_element, "TARGET-REF", instance_ref.getTargetRef())
        return instance_ref

    def setEcucInstanceReferenceValue(self, element: ET.Element, value: EcucInstanceReferenceValue):
        child_element = ET.SubElement(element, "ECUC-INSTANCE-REFERENCE-VALUE")
        self.writeEcucAbstractReferenceValue(child_element, value)
        self.setAnyInstanceRef(child_element, "VALUE-IREF", value.getValueIRef())
        return value

    def writeEcucContainerValueReferenceValues(self, element: ET.Element, container_value: EcucContainerValue):
        reference_values = container_value.getReferenceValues()
        if len(reference_values) > 0:
            child_element = ET.SubElement(element, "REFERENCE-VALUES")
            for reference_value in reference_values:
                if isinstance(reference_value, EcucReferenceValue):
                    self.setEcucReferenceValue(child_element, reference_value)
                elif isinstance(reference_value, EcucInstanceReferenceValue):
                    self.setEcucInstanceReferenceValue(child_element, reference_value)
                else:
                    self.notImplemented("Unsupported EcucParameterValue <%s>" % type(reference_value))

    def writeEcucContainValue(self, element: ET.Element, container_value: EcucContainerValue):
        self.logger.debug("EcucContainerValue %s" % container_value.getShortName())
        child_element = ET.SubElement(element, "ECUC-CONTAINER-VALUE")
        self.writeIdentifiable(child_element, container_value)
        self.setChildElementOptionalRefType(child_element, "DEFINITION-REF", container_value.getDefinitionRef())
        self.setChildElementOptionalPositiveInteger(child_element, "INDEX", container_value.getIndex())
        self.writeEcucContainerValueParameterValues(child_element, container_value)
        self.writeEcucContainerValueReferenceValues(child_element, container_value)
        self.writeEcucContainerValueSubContainers(child_element, container_value)

    def writeEcucModuleConfigurationValuesContainers(self, element: ET.Element, value: EcucModuleConfigurationValues):
        containers = value.getContainers()
        if len(containers) > 0:
            containers_tag = ET.SubElement(element, "CONTAINERS")
            for container in containers:
                if isinstance(container, EcucContainerValue):
                    self.writeEcucContainValue(containers_tag, container)
                else:
                    self.notImplemented("Unsupported Container %s" % type(container))

    def writeEcucModuleConfigurationValues(self, element: ET.Element, values: EcucModuleConfigurationValues):
        self.logger.debug("EcucModuleConfigurationValues %s" % values.getShortName())
        child_element = ET.SubElement(element, "ECUC-MODULE-CONFIGURATION-VALUES")
        self.writeIdentifiable(child_element, values)
        self.setChildElementOptionalRefType(child_element, "DEFINITION-REF", values.getDefinition())
        self.setChildElementOptionalLiteral(child_element, "ECUC-DEF-EDITION", values.getEcucDefEdition())
        self.setChildElementOptionalLiteral(child_element, "IMPLEMENTATION-CONFIG-VARIANT", values.getImplementationConfigVariant())
        self.setChildElementOptionalRefType(child_element, "MODULE-DESCRIPTION-REF", values.getModuleDescription())
        self.setChildElementOptionalBooleanValue(child_element, "POST-BUILD-VARIANT-USED", values.getPostBuildVariantUsed())
        self.writeEcucModuleConfigurationValuesContainers(child_element, values)

    def writeSwSystemconst(self, element: ET.Element, const: SwSystemconst):
        self.logger.debug("SwSystemConst %s" % const.getShortName())
        child_element = ET.SubElement(element, "SW-SYSTEMCONST")
        self.writeIdentifiable(child_element, const)
        self.setSwDataDefProps(child_element, "SW-DATA-DEF-PROPS", const.getSwDataDefProps())

    def writeSwSystemconstValue(self, element: ET.Element, value: SwSystemconstValue):
        child_element = ET.SubElement(element, "SW-SYSTEMCONST-VALUE")
        self.setAnnotations(child_element, value.getAnnotations())
        self.setChildElementOptionalRefType(child_element, "SW-SYSTEMCONST-REF", value.getSwSystemconstRef())
        self.setChildElementOptionalNumericalValue(child_element, "VALUE", value.getValue())

    def writeSwSystemconstantValueSetSwSystemconstantValues(self, element: ET.Element, value_set: SwSystemconstantValueSet):
        values = value_set.getSwSystemconstantValues()
        if len(values) > 0:
            values_element = ET.SubElement(element, "SW-SYSTEMCONSTANT-VALUES")
            for value in values:
                self.writeSwSystemconstValue(values_element, value)

    def writeSwSystemconstantValueSet(self, element: ET.Element, value_set: SwSystemconstantValueSet):
        self.logger.debug("SwSystemconstantValueSet %s" % value_set.getShortName())
        child_element = ET.SubElement(element, "SW-SYSTEMCONSTANT-VALUE-SET")
        self.writeIdentifiable(child_element, value_set)
        self.writeSwSystemconstantValueSetSwSystemconstantValues(child_element, value_set)

    def writePredefinedVariantIncludedVariantRefs(self, element: ET.Element, variant: PredefinedVariant):
        refs = variant.getIncludedVariantRefs()
        if len(refs) > 0:
            refs_element = ET.SubElement(element, "INCLUDED-VARIANT-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(
                    refs_element,
                    "INCLUDED-VARIANT-REF",
                    ref,
                )

    def writePredefinedVariantPostBuildVariantCriterionValueSetRefs(self, element: ET.Element, variant: PredefinedVariant):
        refs = variant.getPostBuildVariantCriterionValueSetRefs()
        if len(refs) > 0:
            refs_element = ET.SubElement(
                element,
                "POST-BUILD-VARIANT-CRITERION-VALUE-SET-REFS",
            )
            for ref in refs:
                self.setChildElementOptionalRefType(
                    refs_element,
                    "POST-BUILD-VARIANT-CRITERION-VALUE-SET-REF",
                    ref,
                )

    def writePredefinedVariantSwSystemconstantValueSetRefs(self, element: ET.Element, variant: PredefinedVariant):
        refs = variant.getSwSystemconstantValueSetRefs()
        if len(refs) > 0:
            refs_element = ET.SubElement(
                element,
                "SW-SYSTEMCONSTANT-VALUE-SET-REFS",
            )
            for ref in refs:
                self.setChildElementOptionalRefType(
                    refs_element,
                    "SW-SYSTEMCONSTANT-VALUE-SET-REF",
                    ref,
                )

    def writePredefinedVariant(self, element: ET.Element, variant: PredefinedVariant):
        self.logger.debug("PredefinedVariant %s" % variant.getShortName())
        child_element = ET.SubElement(element, "PREDEFINED-VARIANT")
        self.writeIdentifiable(child_element, variant)
        self.writePredefinedVariantIncludedVariantRefs(child_element, variant)
        self.writePredefinedVariantPostBuildVariantCriterionValueSetRefs(child_element, variant)
        self.writePredefinedVariantSwSystemconstantValueSetRefs(child_element, variant)

    def writePostBuildVariantCriterion(self, element: ET.Element, criterion: PostBuildVariantCriterion):
        self.logger.debug("PostBuildVariantCriterion %s" % criterion.getShortName())
        child_element = ET.SubElement(element, "POST-BUILD-VARIANT-CRITERION")
        self.writeIdentifiable(child_element, criterion)
        self.setChildElementOptionalRefType(
            child_element,
            "COMPU-METHOD-REF",
            criterion.getCompuMethodRef(),
        )

    def writeISignalGroupISignalRef(self, element: ET.Element, group: ISignalGroup):
        signal_refs = group.getISignalRefs()
        if len(signal_refs) > 0:
            child_element = ET.SubElement(element, "I-SIGNAL-REFS")
            for signal_ref in signal_refs:
                self.setChildElementOptionalRefType(child_element, "I-SIGNAL-REF", signal_ref)

    def writeISignalGroupComBasedSignalGroupTransformation(self, element: ET.Element, group: ISignalGroup):
        ref = group.getComBasedSignalGroupTransformationRef()
        if ref is not None:
            com_based_element = ET.SubElement(element, "COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS")
            cond_element = ET.SubElement(com_based_element, "DATA-TRANSFORMATION-REF-CONDITIONAL")
            self.setChildElementOptionalRefType(cond_element, "DATA-TRANSFORMATION-REF", ref)

    def writeTransformationISignalProps(self, element: ET.Element, props: TransformationISignalProps):
        self.writeDescribable(element, props)
        self.setChildElementOptionalLiteral(element, "CS-ERROR-REACTION", props.getCsErrorReaction())
        dp_props_list = props.getDataPrototypeTransformationProps()
        if len(dp_props_list) > 0:
            child_element = ET.SubElement(element, "DATA-PROTOTYPE-TRANSFORMATION-PROPSS")
            for dp_props in dp_props_list:
                self.writeDataPrototypeTransformationProps(child_element, dp_props)

    def writeDataPrototypeInPortInterfaceRef(self, element: ET.Element, ref: DataPrototypeInPortInterfaceRef):
        child_element = ET.SubElement(element, "DATA-PROTOTYPE-IN-PORT-INTERFACE-REF")
        self.writeARObjectAttributes(child_element, ref)
        self.setChildElementOptionalPositiveInteger(child_element, "TAG-ID", ref.getTagId())
        cs_ref = ref.getDataPrototypeInClientServerInterface()
        if cs_ref is not None:
            self.writeDataPrototypeInClientServerInterfaceInstanceRef(child_element, cs_ref)

    def writeDataPrototypeInSenderReceiverInterfaceInstanceRef(self, element: ET.Element, iref: DataPrototypeInSenderReceiverInterfaceInstanceRef):
        child_element = ET.SubElement(element, "DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-REF")
        self.writeARObjectAttributes(child_element, iref)
        self.setChildElementOptionalRefType(child_element, "BASE", iref.getBaseRef())
        for ctx in iref.getContextDataPrototypeInSrRefs():
            ctx_element = ET.SubElement(child_element, "CONTEXT-DATA-PROTOTYPE-IN-SR")
            self.setChildElementOptionalRefType(ctx_element, "CONTEXT-DATA-PROTOTYPE-IN-SR", ctx)
        self.setChildElementOptionalRefType(child_element, "ROOT-DATA-PROTOTYPE-IN-SR", iref.getRootDataPrototypeInSrRef())
        self.setChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-IN-SR", iref.getTargetDataPrototypeInSrRef())

    def writeDataPrototypeInClientServerInterfaceInstanceRef(self, element: ET.Element, iref: DataPrototypeInClientServerInterfaceInstanceRef):
        child_element = ET.SubElement(element, "DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-REF")
        self.writeARObjectAttributes(child_element, iref)
        self.setChildElementOptionalRefType(child_element, "BASE", iref.getBaseRef())
        for ctx in iref.getContextDataPrototypeInCsRefs():
            ctx_element = ET.SubElement(child_element, "CONTEXT-DATA-PROTOTYPE-IN-CS")
            self.setChildElementOptionalRefType(ctx_element, "CONTEXT-DATA-PROTOTYPE-IN-CS", ctx)
        self.setChildElementOptionalRefType(child_element, "ROOT-DATA-PROTOTYPE-IN-CS", iref.getRootDataPrototypeInCsRef())
        self.setChildElementOptionalRefType(child_element, "TARGET-DATA-PROTOTYPE-IN-CS", iref.getTargetDataPrototypeInCsRef())

    def writeDataPrototypeTransformationProps(self, element: ET.Element, props: DataPrototypeTransformationProps):
        child_element = ET.SubElement(element, "DATA-PROTOTYPE-TRANSFORMATION-PROPS")
        self.writeARObjectAttributes(child_element, props)
        dp_ref = props.getDataPrototypeInPortInterfaceRef()
        if dp_ref is not None:
            self.writeDataPrototypeInPortInterfaceRef(child_element, dp_ref)
        self.setSwDataDefProps(child_element, "NETWORK-REPRESENTATION-PROPS", props.getNetworkRepresentationProps())
        self.setChildElementOptionalRefType(child_element, "TRANSFORMATION-PROPS", props.getTransformationProps())

    def writeEndToEndTransformationISignalPropsDataIds(self, element: ET.Element, props: EndToEndTransformationISignalProps):
        ids = props.getDataIds()
        if len(ids) > 0:
            child_element = ET.SubElement(element, "DATA-IDS")
            for id in ids:
                self.setChildElementOptionalPositiveInteger(child_element, "DATA-ID", id)

    def writeEndToEndTransformationISignalProps(self, element: ET.Element, props: EndToEndTransformationISignalProps):
        if props is not None:
            props_element = ET.SubElement(element, "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS")
            variant_element = ET.SubElement(props_element, "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS")
            child_element = ET.SubElement(variant_element, "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL")
            self.writeTransformationISignalProps(child_element, props)
            self.setChildElementOptionalRefType(child_element, "TRANSFORMER-REF", props.getTransformerRef())
            self.writeEndToEndTransformationISignalPropsDataIds(child_element, props)
            self.setChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH", props.getDataLength())

    def writeISignalGroupTransformationISignalProps(self, element: ET.Element, group: ISignalGroup):
        props_list = group.getTransformationISignalProps()
        if len(props_list) > 0:
            child_element = ET.SubElement(element, "TRANSFORMATION-I-SIGNAL-PROPSS")
            for props in props_list:
                if isinstance(props, EndToEndTransformationISignalProps):
                    self.writeEndToEndTransformationISignalProps(child_element, props)
                else:
                    self.notImplemented("Unsupported TransformationISignalProps %s" % type(props))

    def writeISignalGroup(self, element: ET.Element, group: ISignalGroup):
        self.logger.debug("ISignalGroup %s" % group.getShortName())
        child_element = ET.SubElement(element, "I-SIGNAL-GROUP")
        self.writeIdentifiable(child_element, group)
        self.writeISignalGroupComBasedSignalGroupTransformation(child_element, group)
        self.writeISignalGroupISignalRef(child_element, group)
        self.setChildElementOptionalRefType(child_element, "SYSTEM-SIGNAL-GROUP-REF", group.getSystemSignalGroupRef())
        self.writeISignalGroupTransformationISignalProps(child_element, group)

    def writeISignalIPduGroup(self, element: ET.Element, group: ISignalIPduGroup):
        self.logger.debug("Set ISignalIPduGroup %s" % group.getShortName())
        child_element = ET.SubElement(element, "I-SIGNAL-I-PDU-GROUP")
        self.writeIdentifiable(child_element, group)
        self.setChildElementOptionalLiteral(child_element, "COMMUNICATION-DIRECTION", group.getCommunicationDirection())
        self.setChildElementOptionalLiteral(child_element, "COMMUNICATION-MODE", group.getCommunicationMode())
        group_refs = group.getContainedISignalIPduGroupRefs()
        if len(group_refs) > 0:
            pdu_refs_tag = ET.SubElement(child_element, "CONTAINED-I-SIGNAL-I-PDU-GROUP-REFS")
            for pdu_ref in group_refs:
                self.setChildElementOptionalRefType(pdu_refs_tag, "CONTAINED-I-SIGNAL-I-PDU-GROUP-REF", pdu_ref)
        pdu_refs = group.getISignalIPduRefs()
        if len(pdu_refs) > 0:
            pdu_refs_tag = ET.SubElement(child_element, "I-SIGNAL-I-PDUS")
            for pdu_ref in pdu_refs:
                ref_conditional_tag = ET.SubElement(pdu_refs_tag, "I-SIGNAL-I-PDU-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(ref_conditional_tag, "I-SIGNAL-I-PDU-REF", pdu_ref)

    def writeSystemSignal(self, element: ET.Element, signal: SystemSignal):
        self.logger.debug("SystemSignal %s" % signal.getShortName())
        child_element = ET.SubElement(element, "SYSTEM-SIGNAL")
        self.writeIdentifiable(child_element, signal)
        self.setChildElementOptionalBooleanValue(child_element, "DYNAMIC-LENGTH", signal.getDynamicLength())
        self.setSwDataDefProps(child_element, "PHYSICAL-PROPS", signal.getPhysicalProps())

    def writeSignalServiceTranslationPropsSet(self, element: ET.Element, props_set: SignalServiceTranslationPropsSet):
        self.logger.debug("SignalServiceTranslationPropsSet %s" % props_set.getShortName())
        child_element = ET.SubElement(element, "SIGNAL-SERVICE-TRANSLATION-PROPS-SET")
        self.writeIdentifiable(child_element, props_set)
        props_list = props_set.getSignalServiceTranslationProps()
        if len(props_list) > 0:
            for props in props_list:
                self.writeSignalServiceTranslationProps(child_element, props)

    def writeSignalServiceTranslationProps(self, element: ET.Element, props: SignalServiceTranslationProps):
        self.logger.debug("SignalServiceTranslationProps %s" % props.getShortName())
        child_element = ET.SubElement(element, "SIGNAL-SERVICE-TRANSLATION-PROPS")
        self.writeIdentifiable(child_element, props)
        consumed_event_group_refs = props.getControlConsumedEventGroupRefs()
        if len(consumed_event_group_refs) > 0:
            refs_tag = ET.SubElement(child_element, "CONTROL-CONSUMED-EVENT-GROUP-REFS")
            for ref in consumed_event_group_refs:
                self.setChildElementOptionalRefType(refs_tag, "CONTROL-CONSUMED-EVENT-GROUP-REF", ref)
        pnc_refs = props.getControlPncRefs()
        if len(pnc_refs) > 0:
            refs_tag = ET.SubElement(child_element, "CONTROL-PNC-REFS")
            for ref in pnc_refs:
                self.setChildElementOptionalRefType(refs_tag, "CONTROL-PNC-REF", ref)
        provided_event_group_refs = props.getControlProvidedEventGroupRefs()
        if len(provided_event_group_refs) > 0:
            refs_tag = ET.SubElement(child_element, "CONTROL-PROVIDED-EVENT-GROUP-REFS")
            for ref in provided_event_group_refs:
                self.setChildElementOptionalRefType(refs_tag, "CONTROL-PROVIDED-EVENT-GROUP-REF", ref)
        self.setChildElementOptionalLiteral(child_element, "SERVICE-CONTROL", props.getServiceControl())
        event_props_list = props.getSignalServiceTranslationEventProps()
        if len(event_props_list) > 0:
            for event_props in event_props_list:
                self.writeSignalServiceTranslationEventProps(child_element, event_props)

    def writeSignalServiceTranslationEventProps(self, element: ET.Element, event_props: SignalServiceTranslationEventProps):
        self.logger.debug("SignalServiceTranslationEventProps %s" % event_props.getShortName())
        child_element = ET.SubElement(element, "SIGNAL-SERVICE-TRANSLATION-EVENT-PROPS")
        self.writeIdentifiable(child_element, event_props)
        element_props_list = event_props.getSignalServiceTranslationElementProps()
        if len(element_props_list) > 0:
            for element_props in element_props_list:
                self.writeSignalServiceTranslationElementProps(child_element, element_props)
        self.setChildElementOptionalBooleanValue(child_element, "SAFE-TRANSLATION", event_props.getSafeTranslation())
        self.setChildElementOptionalBooleanValue(child_element, "SECURE-TRANSLATION", event_props.getSecureTranslation())
        self.setVariableDataPrototypeInSystemInstanceRef(child_element, "TRANSLATION-TARGET", event_props.getTranslationTarget())

    def writeSignalServiceTranslationElementProps(self, element: ET.Element, element_props: SignalServiceTranslationElementProps):
        self.logger.debug("SignalServiceTranslationElementProps %s" % element_props.getShortName())
        child_element = ET.SubElement(element, "SIGNAL-SERVICE-TRANSLATION-ELEMENT-PROPS")
        self.writeIdentifiable(child_element, element_props)
        self.setDataFilter(child_element, "FILTER", element_props.getFilter())
        self.setChildElementOptionalBooleanValue(child_element, "TRANSMISSION-TRIGGER", element_props.getTransmissionTrigger())

    def writeGenericEthernetFrame(self, element: ET.Element, frame: GenericEthernetFrame):
        self.logger.debug("Write GenericEthernetFrame %s" % frame.getShortName())
        child_element = ET.SubElement(element, "ETHERNET-FRAME")
        self.writeFrame(child_element, frame)

    def setLifeCyclePeriod(self, element: ET.Element, key: str, period: LifeCyclePeriod):
        if period is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRevisionLabelString(child_element, "AR-RELEASE-VERSION", period.getArReleaseVersion())

    def writeLifeCycleInfoUseInsteadRefs(self, element: ET.Element, info: LifeCycleInfo):
        refs = info.getUseInsteadRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "USE-INSTEAD-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "USE-INSTEAD-REF", ref)

    def writeLifeCycleInfo(self, element: ET.Element, info: LifeCycleInfo):
        if info is not None:
            child_element = ET.SubElement(element, "LIFE-CYCLE-INFO")
            self.writeARObjectAttributes(child_element, info)
            self.setChildElementOptionalRefType(child_element, "LC-OBJECT-REF", info.getLcObjectRef())
            self.setChildElementOptionalRefType(child_element, "LC-STATE-REF", info.getLcStateRef())
            self.setLifeCyclePeriod(child_element, "PERIOD-BEGIN", info.getPeriodBegin())
            self.writeDocumentationBlock(child_element, "REMARK", info.getRemark())
            self.writeLifeCycleInfoUseInsteadRefs(child_element, info)

    def writeLifeCycleInfoSetLifeCycleInfos(self, element: ET.Element, info_set: LifeCycleInfoSet):
        infos = info_set.getLifeCycleInfos()
        if len(infos) > 0:
            child_element = ET.SubElement(element, "LIFE-CYCLE-INFOS")
            for info in infos:
                if isinstance(info, LifeCycleInfo):
                    self.writeLifeCycleInfo(child_element, info)
                else:
                    self.notImplemented("Unsupported Life Cycle Info <%s>" % type(info))

    def writeLifeCycleInfoSet(self, element: ET.Element, info_set: LifeCycleInfoSet):
        if info_set is not None:
            self.logger.debug("Write LifeCycleInfoSet %s" % info_set.getShortName())
            child_element = ET.SubElement(element, "LIFE-CYCLE-INFO-SET")
            self.writeIdentifiable(child_element, info_set)
            self.setChildElementOptionalRefType(child_element, "DEFAULT-LC-STATE-REF", info_set.getDefaultLcStateRef())
            self.writeLifeCycleInfoSetLifeCycleInfos(child_element, info_set)
            self.setChildElementOptionalRefType(child_element, "USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF", info_set.getUsedLifeCycleStateDefinitionGroupRef())

    def writeDiagnosticConnectionFunctionalRequestRefs(self, element: ET.Element, connection: DiagnosticConnection):
        refs = connection.getFunctionalRequestRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "FUNCTIONAL-REQUEST-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(refs_tag, "FUNCTIONAL-REQUEST-REF", ref)

    def writeDiagnosticConnection(self, element: ET.Element, connection: DiagnosticConnection):
        self.logger.debug("Write DiagnosticConnection %s" % connection.getShortName())
        child_element = ET.SubElement(element, "DIAGNOSTIC-CONNECTION")
        self.writeIdentifiable(child_element, connection)
        self.writeDiagnosticConnectionFunctionalRequestRefs(child_element, connection)
        self.setChildElementOptionalRefType(child_element, "PHYSICAL-REQUEST-REF", connection.getPhysicalRequestRef())
        self.setChildElementOptionalRefType(child_element, "RESPONSE-REF", connection.getResponseOnEventRef())

    def writeDiagnosticServiceTableDiagnosticConnectionRefs(self, element: ET.Element, table: DiagnosticServiceTable):
        refs = table.getDiagnosticConnectionRefs()
        if len(refs) > 0:
            refs_tag = ET.SubElement(element, "DIAGNOSTIC-CONNECTIONS")
            for ref in refs:
                child_element = ET.SubElement(refs_tag, "DIAGNOSTIC-CONNECTION-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(child_element, "DIAGNOSTIC-CONNECTION-REF", ref)

    def writeDiagnosticServiceTable(self, element: ET.Element, table: DiagnosticServiceTable):
        self.logger.debug("Write DiagnosticServiceTable %s" % table.getShortName())
        child_element = ET.SubElement(element, "DIAGNOSTIC-SERVICE-TABLE")
        self.writeIdentifiable(child_element, table)
        self.writeDiagnosticServiceTableDiagnosticConnectionRefs(child_element, table)
        self.setChildElementOptionalRefType(child_element, "ECU-INSTANCE-REF", table.getEcuInstanceRef())

    def writePdu(self, element: ET.Element, pdu: Pdu):
        self.writeIdentifiable(element, pdu)
        self.setChildElementOptionalBooleanValue(element, "HAS-DYNAMIC-LENGTH", pdu.getHasDynamicLength())
        self.setChildElementOptionalNumericalValue(element, "LENGTH", pdu.getLength())

    def writeContainedIPduProps(self, element: ET.Element, props: ContainedIPduProps):
        if props is not None:
            child_element = ET.SubElement(element, "CONTAINED-I-PDU-PROPS")
            self.setChildElementOptionalLiteral(child_element, "COLLECTION-SEMANTICS", props.getCollectionSemantics())
            self.setChildElementOptionalPositiveInteger(child_element, "HEADER-ID-LONG-HEADER", props.getHeaderIdLongHeader())
            self.setChildElementOptionalPositiveInteger(child_element, "HEADER-ID-SHORT-HEADER", props.getHeaderIdShortHeader())
            self.setChildElementOptionalNumericalValue(child_element, "OFFSET", props.getOffset())
            self.setChildElementOptionalNumericalValue(child_element, "TIMEOUT", props.getTimeout())
            self.setChildElementOptionalLiteral(child_element, "TRIGGER", props.getTrigger())
            self.setChildElementOptionalNumericalValue(child_element, "UPDATE-INDICATION-BIT-POSITION", props.getUpdateIndicationBitPosition())

    def writeIPdu(self, element: ET.Element, pdu: IPdu):
        self.writePdu(element, pdu)
        self.writeContainedIPduProps(element, pdu.getContainedIPduProps())

    def writeSegmentPosition(self, element: ET.Element, position: SegmentPosition):
        if position is not None:
            child_element = ET.SubElement(element, "SEGMENT-POSITION")
            self.setChildElementOptionalLiteral(child_element, "SEGMENT-BYTE-ORDER", position.getSegmentByteOrder())
            self.setChildElementOptionalIntegerValue(child_element, "SEGMENT-LENGTH", position.getSegmentLength())
            self.setChildElementOptionalIntegerValue(child_element, "SEGMENT-POSITION", position.getSegmentPosition())

    def writeMultiplexedPartSegmentPositions(self, element: ET.Element, part: MultiplexedPart):
        positions = part.getSegmentPositions()
        if len(positions) > 0:
            child_element = ET.SubElement(element, "SEGMENT-POSITIONS")
            for position in positions:
                if isinstance(position, SegmentPosition):
                    self.writeSegmentPosition(child_element, position)
                else:
                    self.notImplemented("Unsupported DynamicPart <%s>" % type(position))

    def writeMultiplexedPart(self, element: ET.Element, part: MultiplexedPart):
        self.writeMultiplexedPartSegmentPositions(element, part)

    def writeDynamicPartAlternative(self, element: ET.Element, alternative: DynamicPartAlternative):
        if alternative is not None:
            child_element = ET.SubElement(element, "DYNAMIC-PART-ALTERNATIVE")
            self.setChildElementOptionalRefType(child_element, "I-PDU-REF", alternative.getIPduRef())
            self.setChildElementOptionalBooleanValue(child_element, "INITIAL-DYNAMIC-PART", alternative.getInitialDynamicPart())
            self.setChildElementOptionalIntegerValue(child_element, "SELECTOR-FIELD-CODE", alternative.getSelectorFieldCode())

    def writeDynamicPartDynamicPartAlternatives(self, element: ET.Element, part: DynamicPart):
        alternatives = part.getDynamicPartAlternatives()
        if len(alternatives) > 0:
            child_element = ET.SubElement(element, "DYNAMIC-PART-ALTERNATIVES")
            for alternative in alternatives:
                if isinstance(alternative, DynamicPartAlternative):
                    self.writeDynamicPartAlternative(child_element, alternative)
                else:
                    self.notImplemented("Unsupported DynamicPartAlternative <%s>" % type(alternative))

    def writeDynamicPart(self, element: ET.Element, part: DynamicPart):
        child_element = ET.SubElement(element, "DYNAMIC-PART")
        self.writeMultiplexedPart(child_element, part)
        self.writeDynamicPartDynamicPartAlternatives(child_element, part)

    def writeMultiplexedIPduDynamicParts(self, element: ET.Element, ipdu: MultiplexedIPdu):
        part = ipdu.getDynamicPart()
        if part is not None:
            child_element = ET.SubElement(element, "DYNAMIC-PARTS")
            if isinstance(part, DynamicPart):
                self.writeDynamicPart(child_element, part)
            else:
                self.notImplemented("Unsupported DynamicPart <%s>" % type(part))

    def writeStaticPart(self, element: ET.Element, part: StaticPart):
        child_element = ET.SubElement(element, "STATIC-PART")
        self.writeMultiplexedPart(child_element, part)
        self.setChildElementOptionalRefType(child_element, "I-PDU-REF", part.getIPduRef())

    def writeMultiplexedIPduStaticParts(self, element: ET.Element, ipdu: MultiplexedIPdu):
        part = ipdu.getStaticPart()
        if part is not None:
            child_element = ET.SubElement(element, "STATIC-PARTS")
            if isinstance(part, StaticPart):
                self.writeStaticPart(child_element, part)
            else:
                self.notImplemented("Unsupported StaticPart <%s>" % type(part))

    def writeMultiplexedIPdu(self, element: ET.Element, ipdu: MultiplexedIPdu):
        self.logger.debug("Write MultiplexedIPdu <%s>" % ipdu.getShortName())
        child_element = ET.SubElement(element, "MULTIPLEXED-I-PDU")
        self.writeIPdu(child_element, ipdu)
        self.writeMultiplexedIPduDynamicParts(child_element, ipdu)
        self.setChildElementOptionalLiteral(child_element, "SELECTOR-FIELD-BYTE-ORDER", ipdu.getSelectorFieldByteOrder())
        self.setChildElementOptionalIntegerValue(child_element, "SELECTOR-FIELD-LENGTH", ipdu.getSelectorFieldLength())
        self.setChildElementOptionalIntegerValue(child_element, "SELECTOR-FIELD-START-POSITION", ipdu.getSelectorFieldStartPosition())
        self.writeMultiplexedIPduStaticParts(child_element, ipdu)
        self.setChildElementOptionalLiteral(child_element, "TRIGGER-MODE", ipdu.getTriggerMode())
        self.setChildElementOptionalIntegerValue(child_element, "UNUSED-BIT-PATTERN", ipdu.getUnusedBitPattern())

    def writeUserDefinedIPdu(self, element: ET.Element, ipdu: UserDefinedIPdu):
        self.logger.debug("Write UserDefinedIPdu <%s>" % ipdu.getShortName())
        child_element = ET.SubElement(element, "USER-DEFINED-I-PDU")
        self.writeIPdu(child_element, ipdu)
        self.setChildElementOptionalLiteral(child_element, "CDD-TYPE", ipdu.getCddType())

    def writeUserDefinedPdu(self, element: ET.Element, pdu: UserDefinedPdu):
        self.logger.debug("Write UserDefinedPdu <%s>" % pdu.getShortName())
        child_element = ET.SubElement(element, "USER-DEFINED-PDU")
        self.writePdu(child_element, pdu)
        self.setChildElementOptionalLiteral(child_element, "CDD-TYPE", pdu.getCddType())

    def writeGeneralPurposePdu(self, element: ET.Element, pdu: GeneralPurposePdu):
        self.logger.debug("Write GeneralPurposePdu <%s>" % pdu.getShortName())
        child_element = ET.SubElement(element, "GENERAL-PURPOSE-PDU")
        self.writePdu(child_element, pdu)

    def writeGeneralPurposeIPdu(self, element: ET.Element, i_pdu: GeneralPurposeIPdu):
        self.logger.debug("Write GeneralPurposeIPdu <%s>" % i_pdu.getShortName())
        child_element = ET.SubElement(element, "GENERAL-PURPOSE-I-PDU")
        self.writeIPdu(child_element, i_pdu)

    def writeSecureCommunicationAuthenticationProps(self, element: ET.Element, props: SecureCommunicationAuthenticationProps):
        chile_element = ET.SubElement(element, "SECURE-COMMUNICATION-AUTHENTICATION-PROPS")
        self.writeIdentifiable(chile_element, props)
        self.setChildElementOptionalPositiveInteger(chile_element, "AUTH-INFO-TX-LENGTH", props.getAuthInfoTxLength())

    def writeSecureCommunicationPropsSetAuthenticationProps(self, element: ET.Element, props_set: SecureCommunicationPropsSet):
        propses = props_set.getAuthenticationProps()
        if len(propses) > 0:
            child_element = ET.SubElement(element, "AUTHENTICATION-PROPSS")
            for props in propses:
                if isinstance(props, SecureCommunicationAuthenticationProps):
                    self.writeSecureCommunicationAuthenticationProps(child_element, props)
                else:
                    self.notImplemented("Unsupported AuthenticationProps <%s>" % type(props))

    def writeSecureCommunicationFreshnessProps(self, element: ET.Element, props: SecureCommunicationFreshnessProps):
        child_element = ET.SubElement(element, "SECURE-COMMUNICATION-FRESHNESS-PROPS")
        self.writeIdentifiable(child_element, props)
        self.setChildElementOptionalPositiveInteger(child_element, "FRESHNESS-COUNTER-SYNC-ATTEMPTS", props.getFreshnessCounterSyncAttempts())
        self.setChildElementOptionalPositiveInteger(child_element, "FRESHNESS-TIMESTAMP-TIME-PERIOD-FACTOR", props.getFreshnessTimestampTimePeriodFactor())
        self.setChildElementOptionalPositiveInteger(child_element, "FRESHNESS-VALUE-LENGTH", props.getFreshnessValueLength())
        self.setChildElementOptionalPositiveInteger(child_element, "FRESHNESS-VALUE-TX-LENGTH", props.getFreshnessValueTxLength())
        self.setChildElementOptionalBooleanValue(child_element, "USE-FRESHNESS-TIMESTAMP", props.getUseFreshnessTimestamp())

    def writeSecureCommunicationPropsSetFreshnessProps(self, element: ET.Element, props_set: SecureCommunicationPropsSet):
        propses = props_set.getFreshnessProps()
        if len(propses) > 0:
            child_element = ET.SubElement(element, "FRESHNESS-PROPSS")
            for props in propses:
                if isinstance(props, SecureCommunicationFreshnessProps):
                    self.writeSecureCommunicationFreshnessProps(child_element, props)
                else:
                    self.notImplemented("Unsupported FreshnessProps <%s>" % type(props))

    def writeSecureCommunicationPropsSet(self, element: ET.Element, set: SecureCommunicationPropsSet):
        self.logger.debug("Write SecureCommunicationPropsSet %s" % set.getShortName())
        child_element = ET.SubElement(element, "SECURE-COMMUNICATION-PROPS-SET")
        self.writeIdentifiable(child_element, set)
        self.writeSecureCommunicationPropsSetAuthenticationProps(child_element, set)
        self.writeSecureCommunicationPropsSetFreshnessProps(child_element, set)

    def writeSoAdRoutingGroup(self, element: ET.Element, group: SoAdRoutingGroup):
        self.logger.debug("Write SoAdRoutingGroup <%s>" % group.getShortName())
        child_element = ET.SubElement(element, "SO-AD-ROUTING-GROUP")
        self.writeIdentifiable(child_element, group)
        self.setChildElementOptionalLiteral(child_element, "EVENT-GROUP-CONTROL-TYPE", group.getEventGroupControlType())

    def writeDoIpLogicAddress(self, element: ET.Element, address: DoIpLogicAddress):
        if address is not None:
            child_element = ET.SubElement(element, "DO-IP-LOGIC-ADDRESS")
            self.writeIdentifiable(child_element, address)
            self.setChildElementOptionalIntegerValue(child_element, "ADDRESS", address.getAddress())

    def writeDoIpTpConfigDoIpLogicAddresses(self, element: ET.Element, config: DoIpTpConfig):
        addresses = config.getDoIpLogicAddresses()
        if len(addresses) > 0:
            child_element = ET.SubElement(element, "DO-IP-LOGIC-ADDRESSS")
            for address in addresses:
                if isinstance(address, DoIpLogicAddress):
                    self.writeDoIpLogicAddress(child_element, address)
                else:
                    self.notImplemented("Unsupported DoIpLogicAddress <%s>" % type(address))

    def writeDoIpTpConnection(self, element: ET.Element, connection: DoIpTpConnection):
        if connection is not None:
            child_element = ET.SubElement(element, "DO-IP-TP-CONNECTION")
            self.writeTpConnection(child_element, connection)
            self.setChildElementOptionalRefType(child_element, "DO-IP-SOURCE-ADDRESS-REF", connection.getDoIpSourceAddressRef())
            self.setChildElementOptionalRefType(child_element, "DO-IP-TARGET-ADDRESS-REF", connection.getDoIpTargetAddressRef())
            self.setChildElementOptionalRefType(child_element, "TP-SDU-REF", connection.getTpSduRef())

    def writeDoIpTpConfigTpConnections(self, element: ET.Element, config: DoIpTpConfig):
        connections = config.getTpConnections()
        if len(connections) > 0:
            child_element = ET.SubElement(element, "TP-CONNECTIONS")
            for address in connections:
                if isinstance(address, DoIpTpConnection):
                    self.writeDoIpTpConnection(child_element, address)
                else:
                    self.notImplemented("Unsupported TpConnection <%s>" % type(address))

    def writeDoIpTpConfig(self, element: ET.Element, config: DoIpTpConfig):
        self.logger.debug("Write DoIpTpConfig <%s>" % config.getShortName())
        child_element = ET.SubElement(element, "DO-IP-TP-CONFIG")
        self.writeTpConfig(child_element, config)
        self.writeDoIpTpConfigDoIpLogicAddresses(child_element, config)
        self.writeDoIpTpConfigTpConnections(child_element, config)

    def writeHwDescriptionEntityHwCategoryRefs(self, element: ET.Element, entity: HwDescriptionEntity):
        refs = entity.getHwCategoryRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "HW-CATEGORY-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "HW-CATEGORY-REF", ref)

    def writeHwAttributeValue(self, element: ET.Element, attribute_value: HwAttributeValue):
        child_element = ET.SubElement(element, "HW-ATTRIBUTE-VALUE")
        self.writeARObjectAttributes(child_element, attribute_value)
        self.setChildElementOptionalRefType(child_element, "HW-ATTRIBUTE-DEF-REF", attribute_value.getHwAttributeDefRef())

    def writeHwDescriptionEntityHwAttributeValues(self, element: ET.Element, entity: HwDescriptionEntity):
        attribute_values = entity.getHwAttributeValues()
        if len(attribute_values) > 0:
            child_element = ET.SubElement(element, "HW-ATTRIBUTE-VALUES")
            for attribute_value in attribute_values:
                self.writeHwAttributeValue(child_element, attribute_value)

    def writeHwDescriptionEntity(self, element: ET.Element, entity: HwDescriptionEntity):
        self.writeReferrable(element, entity)
        self.setChildElementOptionalRefType(element, "HW-TYPE-REF", entity.getHwTypeRef())
        self.writeHwDescriptionEntityHwCategoryRefs(element, entity)
        self.writeHwDescriptionEntityHwAttributeValues(element, entity)

    def writeHwPinGroup(self, element: ET.SubElement, pin_group: HwPinGroup):
        if pin_group is not None:
            child_element = ET.SubElement(element, "HW-PIN-GROUP")
            self.writeHwDescriptionEntity(child_element, pin_group)

    def writeHwPin(self, parent: ET.Element, hw_pin: HwPin):
        if hw_pin is not None:
            child_element = ET.SubElement(parent, "HW-PIN")
            self.writeHwDescriptionEntity(child_element, hw_pin)
            function_names = hw_pin.getFunctionNames()
            if len(function_names) > 0:
                function_names_element = ET.SubElement(child_element, "FUNCTION-NAMES")
                for function_name in function_names:
                    function_name_element = ET.SubElement(function_names_element, "FUNCTION-NAME")
                    function_name_element.text = function_name
            packaging_pin_name = hw_pin.getPackagingPinName()
            if packaging_pin_name is not None:
                packaging_pin_name_element = ET.SubElement(child_element, "PACKAGING-PIN-NAME")
                packaging_pin_name_element.text = packaging_pin_name
            self.setChildElementOptionalIntegerValue(child_element, "PIN-NUMBER", hw_pin.getPinNumber())

    def writeHwElementHwPinGroups(self, element: ET.Element, hw_element: HwElement):
        pin_groups = hw_element.getHwPinGroups()
        if len(pin_groups) > 0:
            child_element = ET.SubElement(element, "HW-PIN-GROUPS")
            for pin_group in pin_groups:
                if isinstance(pin_group, HwPinGroup):
                    self.writeHwPinGroup(child_element, pin_group)
                else:
                    self.notImplemented("Unsupported Hw Pin Group <%s>" % type(pin_group))

    def writeHwPinConnector(self, parent: ET.Element, pin: HwPinConnector):
        child_element = ET.SubElement(parent, "HW-PIN-CONNECTION")
        self.writeDescribable(child_element, pin)
        for ref in pin.getHwPinRefs():
            self.setChildElementOptionalRefType(child_element, "HW-PIN-REF", ref)

    def writeHwPinGroupConnector(self, parent: ET.Element, group: HwPinGroupConnector):
        child_element = ET.SubElement(parent, "HW-PIN-GROUP-CONNECTION")
        self.writeDescribable(child_element, group)
        for connection in group.getHwPinConnections():
            self.writeHwPinConnector(child_element, connection)
        for ref in group.getHwPinGroupRefs():
            self.setChildElementOptionalRefType(child_element, "HW-PIN-GROUP-REF", ref)

    def writeHwElementConnector(self, parent: ET.Element, connector: HwElementConnector):
        child_element = ET.SubElement(parent, "HW-ELEMENT-CONNECTOR")
        self.writeDescribable(child_element, connector)
        for ref in connector.getHwElementRefs():
            self.setChildElementOptionalRefType(child_element, "HW-ELEMENT-REF", ref)
        for connection in connector.getHwPinConnections():
            self.writeHwPinConnector(child_element, connection)
        for group in connector.getHwPinGroupConnections():
            self.writeHwPinGroupConnector(child_element, group)

    def writeHwElementHwElementConnections(self, element: ET.Element, hw_element: HwElement):
        connections = hw_element.getHwElementConnections()
        if len(connections) > 0:
            child_element = ET.SubElement(element, "HW-ELEMENT-CONNECTIONS")
            for connector in connections:
                if isinstance(connector, HwElementConnector):
                    self.writeHwElementConnector(child_element, connector)
                else:
                    self.notImplemented("Unsupported Hw Element Connector <%s>" % type(connector))

    def writeHwElementHwNestedElementRefs(self, element: ET.Element, hw_element: HwElement):
        nested_element_refs = hw_element.getNestedElementRefs()
        if len(nested_element_refs) > 0:
            child_element = ET.SubElement(element, "NESTED-ELEMENTS")
            for ref in nested_element_refs:
                conditional = ET.SubElement(child_element, "HW-ELEMENT-REF-CONDITIONAL")
                self.setChildElementOptionalRefType(conditional, "HW-ELEMENT-REF", ref)

    def writeHwElement(self, element: ET.Element, hw_element: HwElement):
        if hw_element is not None:
            self.logger.debug("Write HwElement <%s>" % hw_element.getShortName())
            child_element = ET.SubElement(element, "HW-ELEMENT")
            self.writeHwDescriptionEntity(child_element, hw_element)
            self.writeHwElementHwPinGroups(child_element, hw_element)
            self.writeHwElementHwElementConnections(child_element, hw_element)
            self.writeHwElementHwNestedElementRefs(child_element, hw_element)

    def writeHwAttributeDef(self, element: ET.Element, attribute_def: HwAttributeDef):
        if attribute_def is not None:
            child_element = ET.SubElement(element, "HW-ATTRIBUTE-DEF")
            self.writeIdentifiable(child_element, attribute_def)
            self.setChildElementOptionalBooleanValue(child_element, "IS-REQUIRED", attribute_def.getIsRequired())
            self.setChildElementOptionalRefType(child_element, "UNIT-REF", attribute_def.getUnitRef())
            self.writeHwAttributeDefHwAttributeLiterals(child_element, attribute_def)

    def writeHwAttributeDefHwAttributeLiterals(self, element: ET.Element, attribute_def: HwAttributeDef):
        literals = attribute_def.getHwAttributeLiterals()
        if len(literals) > 0:
            child_element = ET.SubElement(element, "HW-ATTRIBUTE-LITERALS")
            for literal_def in literals:
                self.writeHwAttributeLiteralDef(child_element, literal_def)

    def writeHwAttributeLiteralDef(self, element: ET.Element, literal_def):
        if literal_def is not None:
            child_element = ET.SubElement(element, "HW-ATTRIBUTE-LITERAL-DEF")
            self.writeIdentifiable(child_element, literal_def)
            self.setChildElementOptionalString(child_element, "VALUE", literal_def.getValue())

    def writeHwCategoryHwAttributeDef(self, element: ET.Element, hw_category: HwCategory):
        attribute_defs = hw_category.getHwAttributeDefs()
        if len(attribute_defs) > 0:
            child_element = ET.SubElement(element, "HW-ATTRIBUTE-DEFS")
            for attribute_def in attribute_defs:
                if isinstance(attribute_def, HwAttributeDef):
                    self.writeHwAttributeDef(child_element, attribute_def)
                else:
                    self.notImplemented("Unsupported Hw Attribute Defs <%s>" % type(attribute_def))

    def writeHwCategory(self, element: ET.Element, hw_category: HwCategory):
        self.logger.debug("write HwCategory <%s>" % hw_category.getShortName())
        child_element = ET.SubElement(element, "HW-CATEGORY")
        self.writeARElement(child_element, hw_category)
        self.writeHwCategoryHwAttributeDef(child_element, hw_category)

    def writeHwType(self, element: ET.Element, type: HwType):
        self.logger.debug("Write HwType <%s>" % type.getShortName())
        child_element = ET.SubElement(element, "HW-TYPE")
        self.writeReferrable(child_element, type)

    def writeLinCommunicationController(self, element: ET.Element, controller: LinCommunicationController):
        self.writeCommunicationController(element, controller)
        self.setChildElementOptionalLiteral(element, "PROTOCOL-VERSION", controller.getProtocolVersion())

    def writeLinMaster(self, element: ET.Element, controller: LinMaster):
        self.logger.debug("Write LinMaster <%s>" % controller.getShortName())
        child_element = ET.SubElement(element, "LIN-MASTER")
        self.writeIdentifiable(child_element, controller)
        variants_tag = ET.SubElement(child_element, "LIN-MASTER-VARIANTS")
        cond_tag = ET.SubElement(variants_tag, "LIN-MASTER-CONDITIONAL")
        self.writeLinCommunicationController(cond_tag, controller)
        slaves = controller.getLinSlaves()
        if len(slaves) > 0:
            slaves_tag = ET.SubElement(cond_tag, "LIN-SLAVES")
            for slave in slaves:
                self.setLinSlaveConfig(slaves_tag, "LIN-SLAVE-CONFIG", slave)
        self.setChildElementOptionalTimeValue(cond_tag, "TIME-BASE", controller.getTimeBase())
        self.setChildElementOptionalTimeValue(cond_tag, "TIME-BASE-JITTER", controller.getTimeBaseJitter())

    def setLinErrorResponse(self, element: ET.Element, key: str, response: LinErrorResponse):
        if response is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "RESPONSE-ERROR-REF", response.getResponseErrorRef())

    def setLinConfigurableFrame(self, element: ET.Element, key: str, frame: LinConfigurableFrame):
        if frame is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "FRAME-REF", frame.getFrameRef())
            self.setChildElementOptionalPositiveInteger(child_element, "MESSAGE-ID", frame.getMessageId())

    def setCanXlFrameTriggeringProps(self, element: ET.Element, key: str, props: CanXlFrameTriggeringProps):
        if props is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalPositiveInteger(child_element, "ACCEPTANCE-FIELD", props.getAcceptanceField())
            self.setChildElementOptionalPositiveInteger(child_element, "PRIORITY-ID", props.getPriorityId())
            self.setChildElementOptionalPositiveInteger(child_element, "SDU-TYPE", props.getSduType())
            self.setChildElementOptionalPositiveInteger(child_element, "VCID", props.getVcid())

    def setLinOrderedConfigurableFrame(self, element: ET.Element, key: str, frame: LinOrderedConfigurableFrame):
        if frame is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalRefType(child_element, "FRAME-REF", frame.getFrameRef())
            self.setChildElementOptionalIntegerValue(child_element, "INDEX", frame.getIndex())

    def setLinSlaveConfig(self, element: ET.Element, key: str, config: LinSlaveConfig):
        if config is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalIntegerValue(child_element, "CONFIGURED-NAD", config.getConfiguredNad())
            self.setChildElementOptionalPositiveInteger(child_element, "FUNCTION-ID", config.getFunctionId())
            if config.getIdent() is not None:
                ident_element = ET.SubElement(child_element, "IDENT")
                self.writeReferrable(ident_element, config.getIdent())
            self.setChildElementOptionalIntegerValue(child_element, "INITIAL-NAD", config.getInitialNad())
            frames = config.getLinConfigurableFrames()
            if len(frames) > 0:
                frames_wrapper = ET.SubElement(child_element, "LIN-CONFIGURABLE-FRAMES")
                for frame in frames:
                    self.setLinConfigurableFrame(frames_wrapper, "LIN-CONFIGURABLE-FRAME", frame)
            self.setLinErrorResponse(child_element, "LIN-ERROR-RESPONSE", config.getLinErrorResponse())
            ordered_frames = config.getLinOrderedConfigurableFrames()
            if len(ordered_frames) > 0:
                ordered_wrapper = ET.SubElement(child_element, "LIN-ORDERED-CONFIGURABLE-FRAMES")
                for frame in ordered_frames:
                    self.setLinOrderedConfigurableFrame(ordered_wrapper, "LIN-ORDERED-CONFIGURABLE-FRAME", frame)
            self.setChildElementOptionalLiteral(child_element, "PROTOCOL-VERSION", config.getProtocolVersion())
            self.setChildElementOptionalPositiveInteger(child_element, "SUPPLIER-ID", config.getSupplierId())
            self.setChildElementOptionalPositiveInteger(child_element, "VARIANT-ID", config.getVariantId())

    def writeISignalToPduMappings(self, element: ET.Element, parent: ISignalIPdu):
        mappings = parent.getISignalToPduMappings()
        if len(mappings) > 0:
            mappings_tag = ET.SubElement(element, "I-SIGNAL-TO-PDU-MAPPINGS")
            for mapping in mappings:
                child_element = ET.SubElement(mappings_tag, "I-SIGNAL-TO-I-PDU-MAPPING")
                self.writeIdentifiable(child_element, mapping)
                self.setChildElementOptionalRefType(child_element, "I-SIGNAL-REF", mapping.getISignalRef())
                self.setChildElementOptionalRefType(child_element, "I-SIGNAL-GROUP-REF", mapping.getISignalGroupRef())
                self.setChildElementOptionalLiteral(child_element, "PACKING-BYTE-ORDER", mapping.getPackingByteOrder())
                self.setChildElementOptionalNumericalValue(child_element, "START-POSITION", mapping.getStartPosition())
                self.setChildElementOptionalLiteral(child_element, "TRANSFER-PROPERTY", mapping.getTransferProperty())
                self.setChildElementOptionalNumericalValue(child_element, "UPDATE-INDICATION-BIT-POSITION", mapping.getUpdateIndicationBitPosition())

    def setDataFilter(self, element: ET.Element, key: str, filter: DataFilter):
        if filter is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalLiteral(child_element, "DATA-FILTER-TYPE", filter.getDataFilterType())
            self.setChildElementOptionalIntegerValue(child_element, "MASK", filter.getMask())
            self.setChildElementOptionalIntegerValue(child_element, "X", filter.getX())

    def setTransmissionModeConditions(self, element: ET.Element, key: str, conditions: List[TransmissionModeCondition]):
        if len(conditions) > 0:
            conditions_tag = ET.SubElement(element, key)
            for condition in conditions:
                child_element = ET.SubElement(conditions_tag, "TRANSMISSION-MODE-CONDITION")
                self.setDataFilter(child_element, "DATA-FILTER", condition.getDataFilter())
                self.setChildElementOptionalRefType(child_element, "I-SIGNAL-IN-I-PDU-REF", condition.getISignalInIPduRef())

    def setTimeRangeType(self, element: ET.Element, key: str, time_range: TimeRangeType):
        if time_range is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalTimeValue(child_element, "VALUE", time_range.getValue())

    def setEventControlledTiming(self, element: ET.Element, key: str, timing: EventControlledTiming):
        if timing is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalIntegerValue(child_element, "NUMBER-OF-REPETITIONS", timing.getNumberOfRepetitions())
            self.setTimeRangeType(child_element, "REPETITION-PERIOD", timing.getRepetitionPeriod())

    def setCyclicTiming(self, element: ET.Element, key: str, timing: CyclicTiming):
        if timing is not None:
            child_element = ET.SubElement(element, key)
            self.setTimeRangeType(child_element, "TIME-OFFSET", timing.getTimeOffset())
            self.setTimeRangeType(child_element, "TIME-PERIOD", timing.getTimePeriod())

    def setTransmissionModeTiming(self, element: ET.Element, key: str, timing: TransmissionModeTiming):
        if timing is not None:
            self.logger.debug("Set TransmissionModeTiming of <%s>" % key)
            child_element = ET.SubElement(element, key)
            self.setCyclicTiming(child_element, "CYCLIC-TIMING", timing.getCyclicTiming())
            self.setEventControlledTiming(child_element, "EVENT-CONTROLLED-TIMING", timing.getEventControlledTiming())

    def setTransmissionModeDeclaration(self, element: ET.Element, key: str, decl: TransmissionModeDeclaration):
        if decl is not None:
            child_element = ET.SubElement(element, key)
            self.setTransmissionModeConditions(child_element, "TRANSMISSION-MODE-CONDITIONS", decl.getTransmissionModeConditions())
            self.setTransmissionModeTiming(child_element, "TRANSMISSION-MODE-FALSE-TIMING", decl.getTransmissionModeFalseTiming())
            self.setTransmissionModeTiming(child_element, "TRANSMISSION-MODE-TRUE-TIMING", decl.getTransmissionModeTrueTiming())

    def setISignalIPduIPduTimingSpecification(self, element: ET.Element, timing: IPduTiming):
        if timing is not None:
            spec_tag = ET.SubElement(element, "I-PDU-TIMING-SPECIFICATIONS")
            child_element = ET.SubElement(spec_tag, "I-PDU-TIMING")
            self.setChildElementOptionalTimeValue(child_element, "MINIMUM-DELAY", timing.getMinimumDelay())
            self.setTransmissionModeDeclaration(child_element, "TRANSMISSION-MODE-DECLARATION", timing.getTransmissionModeDeclaration())

    def writeISignalIPdu(self, element: ET.Element, ipdu: ISignalIPdu):
        self.logger.debug("ISignalIPdu %s" % ipdu.getShortName())
        child_element = ET.SubElement(element, "I-SIGNAL-I-PDU")
        self.writeIdentifiable(child_element, ipdu)
        self.setChildElementOptionalNumericalValue(child_element, "LENGTH", ipdu.getLength())
        self.setISignalIPduIPduTimingSpecification(child_element, ipdu.getIPduTimingSpecification())
        self.writeISignalToPduMappings(child_element, ipdu)
        self.setChildElementOptionalIntegerValue(child_element, "UNUSED-BIT-PATTERN", ipdu.getUnusedBitPattern())

    def writeFlexrayFrame(self, element: ET.Element, frame: FlexrayFrame):
        if frame is not None:
            self.logger.debug("Write FlexrayFrame <%s>" % frame.getShortName())
            child_element = ET.SubElement(element, "FLEXRAY-FRAME")
            self.writeFrame(child_element, frame)

    def writeFlexrayCommunicationController(self, element: ET.Element, controller: FlexrayCommunicationController):
        if controller is not None:
            self.logger.debug("Write FlexrayCommunicationController <%s>" % controller.getShortName())
            controller_element = ET.SubElement(element, "FLEXRAY-COMMUNICATION-CONTROLLER")
            self.writeIdentifiable(controller_element, controller)
            variant_element = ET.SubElement(controller_element, "FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS")
            child_element = ET.SubElement(variant_element, "FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL")
            self.writeCommunicationController(controller_element, controller)
            self.setChildElementOptionalIntegerValue(child_element, "ACCEPTED-STARTUP-RANGE", controller.getAcceptedStartupRange())
            self.setChildElementOptionalBooleanValue(child_element, "ALLOW-HALT-DUE-TO-CLOCK", controller.getAllowHaltDueToClock())
            self.setChildElementOptionalIntegerValue(child_element, "ALLOW-PASSIVE-TO-ACTIVE", controller.getAllowPassiveToActive())
            self.setChildElementOptionalIntegerValue(child_element, "CLUSTER-DRIFT-DAMPING", controller.getClusterDriftDamping())
            self.setChildElementOptionalIntegerValue(child_element, "DECODING-CORRECTION", controller.getDecodingCorrection())
            self.setChildElementOptionalIntegerValue(child_element, "DELAY-COMPENSATION-A", controller.getDelayCompensationA())
            self.setChildElementOptionalIntegerValue(child_element, "DELAY-COMPENSATION-B", controller.getDelayCompensationB())
            self.setChildElementOptionalBooleanValue(child_element, "KEY-SLOT-ONLY-ENABLED", controller.getKeySlotOnlyEnabled())
            self.setChildElementOptionalBooleanValue(child_element, "KEY-SLOT-USED-FOR-START-UP", controller.getKeySlotUsedForStartUp())
            self.setChildElementOptionalBooleanValue(child_element, "KEY-SLOT-USED-FOR-SYNC", controller.getKeySlotUsedForSync())
            self.setChildElementOptionalIntegerValue(child_element, "LATEST-TX", controller.getLatestTX())
            self.setChildElementOptionalIntegerValue(child_element, "LISTEN-TIMEOUT", controller.getListenTimeout())
            self.setChildElementOptionalIntegerValue(child_element, "MACRO-INITIAL-OFFSET-A", controller.getMacroInitialOffsetA())
            self.setChildElementOptionalIntegerValue(child_element, "MACRO-INITIAL-OFFSET-B", controller.getMacroInitialOffsetB())
            self.setChildElementOptionalIntegerValue(child_element, "MAXIMUM-DYNAMIC-PAYLOAD-LENGTH", controller.getMaximumDynamicPayloadLength())
            self.setChildElementOptionalIntegerValue(child_element, "MICRO-INITIAL-OFFSET-A", controller.getMicroInitialOffsetA())
            self.setChildElementOptionalIntegerValue(child_element, "MICRO-INITIAL-OFFSET-B", controller.getMicroInitialOffsetB())
            self.setChildElementOptionalIntegerValue(child_element, "MICRO-PER-CYCLE", controller.getMicroPerCycle())
            self.setChildElementOptionalTimeValue(child_element, "MICROTICK-DURATION", controller.getMicrotickDuration())
            self.setChildElementOptionalIntegerValue(child_element, "OFFSET-CORRECTION-OUT", controller.getOffsetCorrectionOut())
            self.setChildElementOptionalIntegerValue(child_element, "RATE-CORRECTION-OUT", controller.getRateCorrectionOut())
            self.setChildElementOptionalIntegerValue(child_element, "SAMPLES-PER-MICROTICK", controller.getSamplesPerMicrotick())
            self.setChildElementOptionalIntegerValue(child_element, "EXTERN-OFFSET-CORRECTION", controller.getExternOffsetCorrection())
            self.setChildElementOptionalIntegerValue(child_element, "EXTERN-RATE-CORRECTION", controller.getExternRateCorrection())
            self.setChildElementOptionalBooleanValue(child_element, "EXTERNAL-SYNC", controller.getExternalSync())
            self.setChildElementOptionalBooleanValue(child_element, "FALL-BACK-INTERNAL", controller.getFallBackInternal())
            fifos = controller.getFlexrayFifos()
            if len(fifos) > 0:
                fifos_element = ET.SubElement(child_element, "FLEXRAY-FIFOS")
                for fifo in fifos:
                    self.setFlexrayFifoConfiguration(fifos_element, "FLEXRAY-FIFO-CONFIGURATION", fifo)
            self.setChildElementOptionalIntegerValue(child_element, "KEY-SLOT-ID", controller.getKeySlotID())
            self.setChildElementOptionalBooleanValue(child_element, "NM-VECTOR-EARLY-UPDATE", controller.getNmVectorEarlyUpdate())
            self.setChildElementOptionalIntegerValue(child_element, "SECOND-KEY-SLOT-ID", controller.getSecondKeySlotId())
            self.setChildElementOptionalBooleanValue(child_element, "TWO-KEY-SLOT-MODE", controller.getTwoKeySlotMode())
            self.setChildElementOptionalIntegerValue(child_element, "WAKE-UP-PATTERN", controller.getWakeUpPattern())

    def writeDataTransformationTransformerChainRefs(self, element: ET.Element, dtf: DataTransformation):
        refs = dtf.getTransformerChainRefs()
        if len(refs) > 0:
            child_element = ET.SubElement(element, "TRANSFORMER-CHAIN-REFS")
            for ref in refs:
                self.setChildElementOptionalRefType(child_element, "TRANSFORMER-CHAIN-REF", ref)

    def writeDataTransformation(self, element: ET.Element, dtf: DataTransformation):
        if dtf is not None:
            child_element = ET.SubElement(element, "DATA-TRANSFORMATION")
            self.writeIdentifiable(child_element, dtf)
            self.setChildElementOptionalLiteral(child_element, "DATA-TRANSFORMATION-KIND", dtf.getDataTransformationKind())
            self.setChildElementOptionalBooleanValue(child_element, "EXECUTE-DESPITE-DATA-UNAVAILABILITY", dtf.getExecuteDespiteDataUnavailability())
            self.writeDataTransformationTransformerChainRefs(child_element, dtf)

    def writeDataTransformationSetDataTransformations(self, element: ET.Element, dtf_set: DataTransformationSet):
        dtfs = dtf_set.getDataTransformations()
        if len(dtfs) > 0:
            child_element = ET.SubElement(element, "DATA-TRANSFORMATIONS")
            for dtf in dtfs:
                if isinstance(dtf, DataTransformation):
                    self.writeDataTransformation(child_element, dtf)
                else:
                    self.notImplemented("Unsupported DataTransformation <%s>" % type(dtf))

    def writeDataTransformationSetTransformationTechnologies(self, element: ET.Element, dtf_set: DataTransformationSet):
        techs = dtf_set.getTransformationTechnologies()
        if len(techs) > 0:
            child_element = ET.SubElement(element, "TRANSFORMATION-TECHNOLOGYS")
            for tech in techs:
                if isinstance(tech, TransformationTechnology):
                    self.writeTransformationTechnology(child_element, tech)
                else:
                    self.notImplemented("Unsupported TransformationTechnology <%s>" % type(tech))

    def setBufferProperties(self, element: ET.Element, key: str, properties: BufferProperties):
        if properties is not None:
            child_element = ET.SubElement(element, key)
            self.setChildElementOptionalIntegerValue(child_element, "HEADER-LENGTH", properties.getHeaderLength())
            self.setChildElementOptionalBooleanValue(child_element, "IN-PLACE", properties.getInPlace())

    def writeDescribable(self, element: ET.Element, desc: Describable):
        self.writeARObjectAttributes(element, desc)
        self.setMultiLanguageOverviewParagraph(element, "DESC", desc.getDesc())
        self.setChildElementOptionalLiteral(element, "CATEGORY", desc.getCategory())
        self.writeDocumentationBlock(element, "INTRODUCTION", desc.getIntroduction())
        self.setAdminData(element, desc.getAdminData())

    def writeTransformationDescription(self, element: ET.Element, desc: TransformationDescription):
        self.writeDescribable(element, desc)

    def writeEndToEndTransformationDescription(self, element: ET.Element, desc: EndToEndTransformationDescription):
        if desc is not None:
            child_element = ET.SubElement(element, "END-TO-END-TRANSFORMATION-DESCRIPTION")
            self.writeTransformationDescription(child_element, desc)
            self.setChildElementOptionalBooleanValue(child_element, "CLEAR-FROM-VALID-TO-INVALID", desc.getClearFromValidToInvalid())
            self.setChildElementOptionalPositiveInteger(child_element, "COUNTER-OFFSET", desc.getCounterOffset())
            self.setChildElementOptionalPositiveInteger(child_element, "CRC-OFFSET", desc.getCrcOffset())
            self.setChildElementOptionalLiteral(child_element, "DATA-ID-MODE", desc.getDataIdMode())
            self.setChildElementOptionalPositiveInteger(child_element, "DATA-ID-NIBBLE-OFFSET", desc.getDataIdNibbleOffset())
            self.setChildElementOptionalRefType(child_element, "E-2-E-PROFILE-COMPATIBILITY-PROPS-REF", desc.getE2eProfileCompatibilityPropsRef())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-DELTA-COUNTER", desc.getMaxDeltaCounter())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-ERROR-STATE-INIT", desc.getMaxErrorStateInit())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-ERROR-STATE-INVALID", desc.getMaxErrorStateInvalid())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-ERROR-STATE-VALID", desc.getMaxErrorStateValid())
            self.setChildElementOptionalPositiveInteger(child_element, "MAX-NO-NEW-OR-REPEATED-DATA", desc.getMaxNoNewOrRepeatedData())
            self.setChildElementOptionalPositiveInteger(child_element, "MIN-OK-STATE-INIT", desc.getMinOkStateInit())
            self.setChildElementOptionalPositiveInteger(child_element, "MIN-OK-STATE-INVALID", desc.getMinOkStateInvalid())
            self.setChildElementOptionalPositiveInteger(child_element, "MIN-OK-STATE-VALID", desc.getMinOkStateValid())
            self.setChildElementOptionalPositiveInteger(child_element, "OFFSET", desc.getOffset())
            self.setChildElementOptionalLiteral(child_element, "PROFILE-BEHAVIOR", desc.getProfileBehavior())
            self.setChildElementOptionalLiteral(child_element, "PROFILE-NAME", desc.getProfileName())
            self.setChildElementOptionalPositiveInteger(child_element, "SYNC-COUNTER-INIT", desc.getSyncCounterInit())
            self.setChildElementOptionalPositiveInteger(child_element, "UPPER-HEADER-BITS-TO-SHIFT", desc.getUpperHeaderBitsToShift())
            self.setChildElementOptionalPositiveInteger(child_element, "WINDOW-SIZE-INIT", desc.getWindowSizeInit())
            self.setChildElementOptionalPositiveInteger(child_element, "WINDOW-SIZE-INVALID", desc.getWindowSizeInvalid())
            self.setChildElementOptionalPositiveInteger(child_element, "WINDOW-SIZE-VALID", desc.getWindowSizeValid())

    def writeTransformationTechnologyTransformationDescriptions(self, element: ET.Element, tech: TransformationTechnology):
        desc = tech.getTransformationDescription()
        if desc is not None:
            child_element = ET.SubElement(element, "TRANSFORMATION-DESCRIPTIONS")
            if isinstance(desc, EndToEndTransformationDescription):
                self.writeEndToEndTransformationDescription(child_element, desc)
            else:
                self.notImplemented("Unsupported TransformationDescription <%s>" % type(desc))

    def writeTransformationTechnology(self, element: ET.Element, tech: TransformationTechnology):
        if tech is not None:
            child_element = ET.SubElement(element, "TRANSFORMATION-TECHNOLOGY")
            self.writeIdentifiable(child_element, tech)
            self.setBufferProperties(child_element, "BUFFER-PROPERTIES", tech.getBufferProperties())
            self.setChildElementOptionalBooleanValue(child_element, "HAS-INTERNAL-STATE", tech.getHasInternalState())
            self.setChildElementOptionalBooleanValue(child_element, "NEEDS-ORIGINAL-DATA", tech.getNeedsOriginalData())
            self.setChildElementOptionalLiteral(child_element, "PROTOCOL", tech.getProtocol())
            self.writeTransformationTechnologyTransformationDescriptions(child_element, tech)
            self.setChildElementOptionalLiteral(child_element, "TRANSFORMER-CLASS", tech.getTransformerClass())
            self.setChildElementOptionalLiteral(child_element, "VERSION", tech.getVersion())

    def writeDataTransformationSet(self, element: ET.Element, dtf_set: DataTransformationSet):
        if dtf_set is not None:
            child_element = ET.SubElement(element, "DATA-TRANSFORMATION-SET")
            self.writeIdentifiable(child_element, dtf_set)
            self.writeDataTransformationSetDataTransformations(child_element, dtf_set)
            self.writeDataTransformationSetTransformationTechnologies(child_element, dtf_set)

    def writeE2EProfileCompatibilityProps(self, element: ET.Element, props: E2EProfileCompatibilityProps):
        if props is not None:
            child_element = ET.SubElement(element, "E-2-E-PROFILE-COMPATIBILITY-PROPS")
            self.writeIdentifiable(child_element, props)
            self.setChildElementOptionalBooleanValue(child_element, "TRANSIT-TO-INVALID-EXTENDED", props.getTransitToInvalidExtended())

    def writeARPackageElement(self, element: ET.Element, ar_element: ARElement):
        if isinstance(ar_element, ComplexDeviceDriverSwComponentType):
            self.writeComplexDeviceDriverSwComponentType(element, ar_element)
        elif isinstance(ar_element, SwcImplementation):
            self.writeSwcImplementation(element, ar_element)
        elif isinstance(ar_element, TcpOptionFilterSet):
            self.writeTcpOptionFilterSet(element, ar_element)
        elif isinstance(ar_element, CompositionSwComponentType):
            self.writeCompositionSwComponentType(element, ar_element)
        elif isinstance(ar_element, ApplicationPrimitiveDataType):
            self.writeApplicationPrimitiveDataType(element, ar_element)
        elif isinstance(ar_element, ApplicationRecordDataType):
            self.writeApplicationRecordDataType(element, ar_element)
        elif isinstance(ar_element, SwBaseType):
            self.writeSwBaseType(element, ar_element)
        elif isinstance(ar_element, CompuMethod):
            self.writeCompuMethod(element, ar_element)
        elif isinstance(ar_element, ConstantSpecification):
            self.writeConstantSpecification(element, ar_element)
        elif isinstance(ar_element, DataConstr):
            self.writeDataConstr(element, ar_element)
        elif isinstance(ar_element, EndToEndProtectionSet):
            self.writeEndToEndProtectionSet(element, ar_element)
        elif isinstance(ar_element, SenderReceiverInterface):
            self.writeSenderReceiverInterface(element, ar_element)
        elif isinstance(ar_element, Unit):
            self.writeUnit(element, ar_element)
        elif isinstance(ar_element, BswModuleDescription):
            self.writeBswModuleDescription(element, ar_element)
        elif isinstance(ar_element, BswModuleEntry):
            self.writeBswModuleEntry(element, ar_element)
        elif isinstance(ar_element, SwcBswMapping):
            self.writeSwcBswMapping(element, ar_element)
        elif isinstance(ar_element, BswImplementation):
            self.writeBswImplementation(element, ar_element)
        elif isinstance(ar_element, ImplementationDataType):
            self.writeImplementationDataType(element, ar_element)
        elif isinstance(ar_element, ClientServerInterface):
            self.writeClientServerInterface(element, ar_element)
        elif isinstance(ar_element, ApplicationSwComponentType):
            self.writeApplicationSwComponentType(element, ar_element)
        elif isinstance(ar_element, EcuAbstractionSwComponentType):
            self.writeEcuAbstractionSwComponentType(element, ar_element)
        elif isinstance(ar_element, ApplicationArrayDataType):
            self.writeApplicationArrayDataType(element, ar_element)
        elif isinstance(ar_element, SwRecordLayout):
            self.writeSwRecordLayout(element, ar_element)
        elif isinstance(ar_element, SwAddrMethod):
            self.writeSwAddrMethod(element, ar_element)
        elif isinstance(ar_element, TriggerInterface):
            self.writeTriggerInterface(element, ar_element)
        elif isinstance(ar_element, ServiceSwComponentType):
            self.writeServiceSwComponentType(element, ar_element)
        elif isinstance(ar_element, SensorActuatorSwComponentType):
            self.writeSensorActuatorSwComponentType(element, ar_element)
        elif isinstance(ar_element, NvBlockSwComponentType):
            self.writeNvBlockSwComponentType(element, ar_element)
        elif isinstance(ar_element, ServiceProxySwComponentType):
            self.writeServiceProxySwComponentType(element, ar_element)
        elif isinstance(ar_element, DataTypeMappingSet):
            self.writeDataTypeMappingSet(element, ar_element)
        elif isinstance(ar_element, ModeDeclarationGroup):
            self.writeModeDeclarationGroup(element, ar_element)
        elif isinstance(ar_element, ModeSwitchInterface):
            self.writeModeSwitchInterface(element, ar_element)
        elif isinstance(ar_element, SwcTiming):
            self.writeSwcTiming(element, ar_element)
        elif isinstance(ar_element, LinUnconditionalFrame):
            self.writeLinUnconditionalFrame(element, ar_element)
        elif isinstance(ar_element, NmConfig):
            self.writeNmConfig(element, ar_element)
        elif isinstance(ar_element, NmPdu):
            self.writeNmPdu(element, ar_element)
        elif isinstance(ar_element, NPdu):
            self.writeNPdu(element, ar_element)
        elif isinstance(ar_element, DcmIPdu):
            self.writeDcmIPdu(element, ar_element)
        elif isinstance(ar_element, SecuredIPdu):
            self.writeSecuredIPdu(element, ar_element)
        elif isinstance(ar_element, CanTpConfig):
            self.writeCanTpConfig(element, ar_element)
        elif isinstance(ar_element, LinTpConfig):
            self.writeLinTpConfig(element, ar_element)
        elif isinstance(ar_element, LinCluster):
            self.writeLinCluster(element, ar_element)
        elif isinstance(ar_element, CanCluster):
            self.writeCanCluster(element, ar_element)
        elif isinstance(ar_element, CanFrame):
            self.writeCanFrame(element, ar_element)
        elif isinstance(ar_element, Gateway):
            self.writeGateway(element, ar_element)
        elif isinstance(ar_element, ISignal):
            self.writeISignal(element, ar_element)
        elif isinstance(ar_element, System):
            self.writeSystem(element, ar_element)
        elif isinstance(ar_element, EcuInstance):
            self.writeEcuInstance(element, ar_element)
        elif isinstance(ar_element, ISignalIPdu):
            self.writeISignalIPdu(element, ar_element)
        elif isinstance(ar_element, SystemSignal):
            self.writeSystemSignal(element, ar_element)
        elif isinstance(ar_element, SignalServiceTranslationPropsSet):
            self.writeSignalServiceTranslationPropsSet(element, ar_element)
        elif isinstance(ar_element, ParameterInterface):
            self.writeParameterInterface(element, ar_element)
        elif isinstance(ar_element, NvDataInterface):
            self.writeNvDataInterface(element, ar_element)
        elif isinstance(ar_element, GenericEthernetFrame):
            self.writeGenericEthernetFrame(element, ar_element)
        elif isinstance(ar_element, LifeCycleInfoSet):
            self.writeLifeCycleInfoSet(element, ar_element)
        elif isinstance(ar_element, PhysicalDimension):
            self.writePhysicalDimension(element, ar_element)
        elif isinstance(ar_element, FlatMap):
            self.writeFlatMap(element, ar_element)
        elif isinstance(ar_element, PortInterfaceMappingSet):
            self.writePortInterfaceMappingSet(element, ar_element)
        elif isinstance(ar_element, EthernetCluster):
            self.writeEthernetCluster(element, ar_element)
        elif isinstance(ar_element, ISignalIPduGroup):
            self.writeISignalIPduGroup(element, ar_element)
        elif isinstance(ar_element, DiagnosticConnection):
            self.writeDiagnosticConnection(element, ar_element)
        elif isinstance(ar_element, DiagnosticServiceTable):
            self.writeDiagnosticServiceTable(element, ar_element)
        elif isinstance(ar_element, Documentation):
            self.writeDocumentation(element, ar_element)
        elif isinstance(ar_element, MultiplexedIPdu):
            self.writeMultiplexedIPdu(element, ar_element)
        elif isinstance(ar_element, UserDefinedIPdu):
            self.writeUserDefinedIPdu(element, ar_element)
        elif isinstance(ar_element, UserDefinedPdu):
            self.writeUserDefinedPdu(element, ar_element)
        elif isinstance(ar_element, GeneralPurposePdu):
            self.writeGeneralPurposePdu(element, ar_element)
        elif isinstance(ar_element, GeneralPurposeIPdu):
            self.writeGeneralPurposeIPdu(element, ar_element)
        elif isinstance(ar_element, SecureCommunicationPropsSet):
            self.writeSecureCommunicationPropsSet(element, ar_element)
        elif isinstance(ar_element, SoAdRoutingGroup):
            self.writeSoAdRoutingGroup(element, ar_element)
        elif isinstance(ar_element, CanXlProps):
            self.writeCanXlProps(element, ar_element)
        elif isinstance(ar_element, SomeipSdClientServiceInstanceConfig):
            self.writeSomeipSdClientServiceInstanceConfig(element, ar_element)
        elif isinstance(ar_element, SomeipSdClientEventGroupTimingConfig):
            self.writeSomeipSdClientEventGroupTimingConfig(element, ar_element)
        elif isinstance(ar_element, SomeipSdServerEventGroupTimingConfig):
            self.writeSomeipSdServerEventGroupTimingConfig(element, ar_element)
        elif isinstance(ar_element, DoIpTpConfig):
            self.writeDoIpTpConfig(element, ar_element)
        elif isinstance(ar_element, HwElement):
            self.writeHwElement(element, ar_element)
        elif isinstance(ar_element, HwCategory):
            self.writeHwCategory(element, ar_element)
        elif isinstance(ar_element, HwType):
            self.writeHwType(element, ar_element)
        elif isinstance(ar_element, DataTransformationSet):
            self.writeDataTransformationSet(element, ar_element)
        elif isinstance(ar_element, E2EProfileCompatibilityProps):
            self.writeE2EProfileCompatibilityProps(element, ar_element)
        elif isinstance(ar_element, FlexrayFrame):
            self.writeFlexrayFrame(element, ar_element)
        elif isinstance(ar_element, ISignalGroup):
            self.writeISignalGroup(element, ar_element)
        elif isinstance(ar_element, SystemSignalGroup):
            self.writeSystemSignalGroup(element, ar_element)
        elif isinstance(ar_element, FlexrayCluster):
            self.writeFlexrayCluster(element, ar_element)
        elif isinstance(ar_element, Collection):
            self.writeCollection(element, ar_element)
        elif isinstance(ar_element, KeywordSet):
            self.writeKeywordSet(element, ar_element)
        elif isinstance(ar_element, PortPrototypeBlueprint):
            self.writePortPrototypeBlueprint(element, ar_element)
        elif isinstance(ar_element, ModeDeclarationMappingSet):
            self.writeModeDeclarationMappingSet(element, ar_element)
        elif isinstance(ar_element, EcucModuleDef):
            self.writeEcucModuleDef(element, ar_element)
        elif isinstance(ar_element, EcucDefinitionCollection):
            self.writeEcucDefinitionCollection(element, ar_element)
        elif isinstance(ar_element, EcucDestinationUriDefSet):
            self.writeEcucDestinationUriDefSet(element, ar_element)
        elif isinstance(ar_element, EcucModuleConfigurationValues):
            self.writeEcucModuleConfigurationValues(element, ar_element)
        elif isinstance(ar_element, SwSystemconst):
            self.writeSwSystemconst(element, ar_element)
        elif isinstance(ar_element, SwSystemconstantValueSet):
            self.writeSwSystemconstantValueSet(element, ar_element)
        elif isinstance(ar_element, PredefinedVariant):
            self.writePredefinedVariant(element, ar_element)
        elif isinstance(ar_element, PostBuildVariantCriterion):
            self.writePostBuildVariantCriterion(element, ar_element)
        elif isinstance(ar_element, McFunction):
            self.writeMcFunction(element, ar_element)
        elif isinstance(ar_element, McGroup):
            self.writeMcGroup(element, ar_element)
        elif isinstance(ar_element, DataPrototypeGroup):
            self.writeDataPrototypeGroup(element, ar_element)
        elif isinstance(ar_element, RunnableEntityGroup):
            self.writeRunnableEntityGroup(element, ar_element)
        elif isinstance(ar_element, ConsistencyNeeds):
            self.writeConsistencyNeeds(element, ar_element)
        else:
            self.notImplemented("Unsupported Elements of ARPackage <%s>" % type(ar_element))

    def writeReferenceBases(self, element: ET.Element, bases: List[ReferenceBase]):
        self.logger.debug("Write ReferenceBases")
        if len(bases) > 0:
            bases_tag = ET.SubElement(element, "REFERENCE-BASES")
            for base in bases:
                child_element = ET.SubElement(bases_tag, "REFERENCE-BASE")
                self.setChildElementOptionalLiteral(child_element, "SHORT-LABEL", base.getShortLabel())
                self.setChildElementOptionalBooleanValue(child_element, "IS-DEFAULT", base.getIsDefault())
                self.setChildElementOptionalBooleanValue(child_element, "IS-GLOBAL", base.getIsDefault())
                self.setChildElementOptionalBooleanValue(child_element, "BASE-IS-THIS-PACKAGE", base.getBaseIsThisPackage())
                self.setChildElementOptionalRefType(child_element, "PACKAGE-REF", base.getPackageRef())

    def writeMcFunction(self, element: ET.Element, func: McFunction):
        if func is not None:
            child_element = ET.SubElement(element, "MC-FUNCTION")
            self.writeIdentifiable(child_element, func)
            if func.getDefCalprmSet() is not None:
                def_calprm_set_element = ET.SubElement(child_element, "DEF-CALPRM-SET")
                self.writeMcFunctionDataRefSet(def_calprm_set_element, func.getDefCalprmSet())
            if func.getRefCalprmSet() is not None:
                ref_calprm_set_element = ET.SubElement(child_element, "REF-CALPRM-SET")
                self.writeMcFunctionDataRefSet(ref_calprm_set_element, func.getRefCalprmSet())
            if func.getInMeasurementSet() is not None:
                in_measurement_set_element = ET.SubElement(child_element, "IN-MEASUREMENT-SET")
                self.writeMcFunctionDataRefSet(in_measurement_set_element, func.getInMeasurementSet())
            if func.getLocMeasurementSet() is not None:
                loc_measurement_set_element = ET.SubElement(child_element, "LOC-MEASUREMENT-SET")
                self.writeMcFunctionDataRefSet(loc_measurement_set_element, func.getLocMeasurementSet())
            if func.getOutMeasurementSet() is not None:
                out_measurement_set_element = ET.SubElement(child_element, "OUT-MEASUREMENT-SET")
                self.writeMcFunctionDataRefSet(out_measurement_set_element, func.getOutMeasurementSet())
            sub_function_refs = func.getSubFunctionRefs()
            if len(sub_function_refs) > 0:
                refs_element = ET.SubElement(child_element, "SUB-FUNCTION-REFS")
                for ref in sub_function_refs:
                    self.setChildElementOptionalRefType(refs_element, "SUB-FUNCTION-REF", ref)

    def writeMcFunctionDataRefSet(self, element: ET.Element, data_ref_set: McFunctionDataRefSet):
        variants_element = ET.SubElement(element, "MC-FUNCTION-DATA-REF-SET-VARIANTS")
        conditional_element = ET.SubElement(variants_element, "MC-FUNCTION-DATA-REF-SET-CONDITIONAL")
        flat_map_entry_refs = data_ref_set.getFlatMapEntryRefs()
        if len(flat_map_entry_refs) > 0:
            refs_element = ET.SubElement(conditional_element, "FLAT-MAP-ENTRY-REFS")
            for ref in flat_map_entry_refs:
                self.setChildElementOptionalRefType(refs_element, "FLAT-MAP-ENTRY-REF", ref)
        mc_data_instance_refs = data_ref_set.getMcDataInstanceRefs()
        if len(mc_data_instance_refs) > 0:
            refs_element = ET.SubElement(conditional_element, "MC-DATA-INSTANCE-REFS")
            for ref in mc_data_instance_refs:
                self.setChildElementOptionalRefType(refs_element, "MC-DATA-INSTANCE-REF", ref)

    def writeMcGroup(self, element: ET.Element, group: McGroup):
        if group is not None:
            child_element = ET.SubElement(element, "MC-GROUP")
            self.writeIdentifiable(child_element, group)
            sub_group_refs = group.getSubGroupRefs()
            if len(sub_group_refs) > 0:
                refs_element = ET.SubElement(child_element, "SUB-GROUP-REFS")
                for ref in sub_group_refs:
                    self.setChildElementOptionalRefType(refs_element, "SUB-GROUP-REF", ref)
            if group.getRefCalprmSet() is not None:
                ref_calprm_set_element = ET.SubElement(child_element, "REF-CALPRM-SET")
                self.writeMcGroupDataRefSet(ref_calprm_set_element, group.getRefCalprmSet())
            if group.getRefMeasurementSet() is not None:
                ref_measurement_set_element = ET.SubElement(child_element, "REF-MEASUREMENT-SET")
                self.writeMcGroupDataRefSet(ref_measurement_set_element, group.getRefMeasurementSet())
            mc_function_refs = group.getMcFunctionRefs()
            if len(mc_function_refs) > 0:
                refs_element = ET.SubElement(child_element, "MC-FUNCTION-REFS")
                for ref in mc_function_refs:
                    self.setChildElementOptionalRefType(refs_element, "MC-FUNCTION-REF", ref)

    def writeMcGroupDataRefSet(self, element: ET.Element, data_ref_set: McGroupDataRefSet):
        variants_element = ET.SubElement(element, "MC-GROUP-DATA-REF-SET-VARIANTS")
        conditional_element = ET.SubElement(variants_element, "MC-GROUP-DATA-REF-SET-CONDITIONAL")
        flat_map_entry_refs = data_ref_set.getFlatMapEntryRefs()
        if len(flat_map_entry_refs) > 0:
            refs_element = ET.SubElement(conditional_element, "FLAT-MAP-ENTRY-REFS")
            for ref in flat_map_entry_refs:
                self.setChildElementOptionalRefType(refs_element, "FLAT-MAP-ENTRY-REF", ref)
        mc_data_instance_refs = data_ref_set.getMcDataInstanceRefs()
        if len(mc_data_instance_refs) > 0:
            refs_element = ET.SubElement(conditional_element, "MC-DATA-INSTANCE-REFS")
            for ref in mc_data_instance_refs:
                self.setChildElementOptionalRefType(refs_element, "MC-DATA-INSTANCE-REF", ref)

    def setCanControllerConfiguration(self, element: ET.Element, key: str, configuration: CanControllerConfiguration):
        if configuration is not None:
            ET.SubElement(element, key)

    def writeCanXlProps(self, parent: ET.Element, can_xl_props: CanXlProps):
        self.logger.debug("Write CanXlProps %s" % can_xl_props.getShortName())
        element = ET.SubElement(parent, "CAN-XL-PROPS")
        self.writeIdentifiable(element, can_xl_props)
        self.setChildElementOptionalPositiveInteger(element, "CAN-BAUDRATE", can_xl_props.getCanBaudrate())
        self.setCanControllerConfiguration(element, "CAN-CONFIG", can_xl_props.getCanConfig())
        self.setChildElementOptionalPositiveInteger(element, "CAN-FD-BAUDRATE", can_xl_props.getCanFdBaudrate())
        self.setCanControllerFdConfiguration(element, "CAN-FD-CONFIG", can_xl_props.getCanFdConfig())
        self.setChildElementOptionalPositiveInteger(element, "CAN-XL-BAUDRATE", can_xl_props.getCanXlBaudrate())
        self.setCanControllerXlConfiguration(element, "CAN-XL-CONFIG", can_xl_props.getCanXlConfig())
        self.setCanControllerXlConfigurationRequirements(element, "CAN-XL-CONFIG-REQS", can_xl_props.getCanXlConfigReqs())

    def writeARPackage(self, element: ET.Element, pkg: ARPackage):
        self.logger.debug("Write ARPackage %s" % pkg.getFullName())
        child_element = ET.SubElement(element, "AR-PACKAGE")

        self.writeIdentifiable(child_element, pkg)
        self.writeReferenceBases(child_element, pkg.getReferenceBases())
        self.writeARPackageElements(child_element, pkg)
        self.writeARPackages(child_element, pkg.getARPackages())

    def writeARPackageElements(self, element: ET.Element, pkg: ARPackage):
        if pkg.getTotalElement() > 0:
            elements_tag = ET.SubElement(element, "ELEMENTS")

            for ar_element in pkg.getElements():
                if not isinstance(ar_element, ARPackage):
                    self.writeARPackageElement(elements_tag, ar_element)

    def writeARPackages(self, element: ET.Element, pkgs: List[ARPackage]):
        if len(pkgs) > 0:
            child_element = ET.SubElement(element, "AR-PACKAGES")
            for pkg in pkgs:
                if isinstance(pkg, ARPackage):
                    self.writeARPackage(child_element, pkg)
                else:
                    self.notImplemented("Unsupported ARPackage <%s>" % type(pkg))

    def save(self, filename, document: AUTOSAR):
        self.logger.info("Saving %s ..." % filename)

        root = ET.Element("AUTOSAR", self.nsmap)
        root.attrib["xmlns:xsi"] = "http://www.w3.org/2001/XMLSchema-instance"
        if document.schema_location is not None:
            root.attrib["xsi:schemaLocation"] = document.schema_location
        else:
            root.attrib["xsi:schemaLocation"] = "http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd"

        self.setAdminData(root, document.getAdminData())
        self.writeARPackages(root, document.getARPackages())

        self.saveToFile(filename, root)
