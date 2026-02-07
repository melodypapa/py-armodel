from abc import ABC
from typing import TYPE_CHECKING, List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARBoolean,
    ARLiteral,
    Boolean,
    RefType,
)

if TYPE_CHECKING:
    from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
        ExecutableEntity,
        InternalBehavior,
    )


def _get_internal_behavior_base():
    """Lazy import of InternalBehavior to avoid circular import."""
    from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
        InternalBehavior,
    )
    return InternalBehavior


def _get_executable_entity_base():
    """Lazy import of ExecutableEntity to avoid circular import."""
    from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
        ExecutableEntity,
    )
    return ExecutableEntity
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    ParameterDataPrototype,
    VariableDataPrototype,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import (
    AbstractAccessPoint,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
    AutosarParameterRef,
    AutosarVariableRef,
    ParameterAccess,
    VariableAccess,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import (
    IncludedDataTypeSet,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import (
    IncludedModeDeclarationGroupSet,
    ModeAccessPoint,
    ModeSwitchPoint,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory import (
    PerInstanceMemory,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import (
    PortAPIOption,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import (
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
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RunnableEntity import (
    RunnableEntity,
    RunnableEntityArgument,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import (
    AsynchronousServerCallPoint,
    AsynchronousServerCallResultPoint,
    ServerCallPoint,
    SynchronousServerCallPoint,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import (
    SwcServiceDependency,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger import (
    ExternalTriggeringPoint,
    InternalTriggeringPoint,
)


class SwcInternalBehavior(ABC):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        # Lazy import to avoid circular dependency
        InternalBehavior = _get_internal_behavior_base()
        InternalBehavior.__init__(self, parent, short_name)

        self.arTypedPerInstanceMemories = []                        # type: List[VariableDataPrototype]
        self.events = []                                            # type: List[RTEEvent]
        self.exclusiveAreaPolicies = []                             # type: List[SwcExclusiveAreaPolicy]
        self.explicitInterRunnableVariables = []                    # type: List[VariableDataPrototype]
        self.handleTerminationAndRestart: Union[str, None] = None
        self.implicitInterRunnableVariables = []                    # type: List[VariableDataPrototype]
        self.includedDataTypeSets = []                              # type: List[IncludedDataTypeSet]
        self.includedModeDeclarationGroupSets = []                  # type: List[IncludedModeDeclarationGroupSet]
        self.instantiationDataDefProps = []                         # type: List[InstantiationDataDefProps]
        self.perInstanceMemories = []                               # type: List[PerInstanceMemory]
        self.perInstanceParameters = []                             # type: List[ParameterDataPrototype]
        self.portAPIOptions = []                                    # type: List[PortAPIOption]
        self.runnables = []                                         # type: List[RunnableEntity]
        self.serviceDependencies = []                               # type: List[SwcServiceDependency]
        self.sharedParameters = []                                  # type: List[ParameterDataPrototype]
        self.supportsMultipleInstantiation: Union[Boolean, None] = None
        self.variationPointProxies = []                             # type: List[VariationPointProxy]

    def getArTypedPerInstanceMemories(self) -> List[VariableDataPrototype]:
        return self.arTypedPerInstanceMemories

    def createArTypedPerInstanceMemory(self, short_name: str) -> VariableDataPrototype:
        if not self.IsElementExists(short_name):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.arTypedPerInstanceMemories.append(prototype)
        return self.getElement(short_name)

    def getExplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        return self.explicitInterRunnableVariables

    def createExplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        if not self.IsElementExists(short_name):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.explicitInterRunnableVariables.append(prototype)
        return self.getElement(short_name)

    def getHandleTerminationAndRestart(self):
        return self.handleTerminationAndRestart

    def setHandleTerminationAndRestart(self, value):
        self.handleTerminationAndRestart = value
        return self

    def getImplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        return self.implicitInterRunnableVariables

    def getPerInstanceMemories(self) -> List[PerInstanceMemory]:
        return self.perInstanceMemories

    def getPerInstanceParameters(self) -> List[ParameterDataPrototype]:
        return self.perInstanceParameters

    def addPortAPIOption(self, option: PortAPIOption) -> None:
        self.portAPIOptions.append(option)

    def getPortAPIOptions(self) -> List[PortAPIOption]:
        return self.portAPIOptions

    def addIncludedDataTypeSet(self, set: IncludedDataTypeSet) -> None:
        self.includedDataTypeSets.append(set)

    def getIncludedDataTypeSets(self) -> List[IncludedDataTypeSet]:
        return self.includedDataTypeSets

    def getIncludedModeDeclarationGroupSets(self):
        return self.includedModeDeclarationGroupSets

    def addIncludedModeDeclarationGroupSet(self, value):
        if value is not None:
            self.includedModeDeclarationGroupSets.append(value)
        return self

    def createOperationInvokedEvent(self, short_name: str) -> OperationInvokedEvent:
        if not self.IsElementExists(short_name):
            event = OperationInvokedEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, OperationInvokedEvent)

    def createTimingEvent(self, short_name: str) -> TimingEvent:
        if not self.IsElementExists(short_name):
            event = TimingEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, TimingEvent)

    def createInitEvent(self, short_name: str) -> InitEvent:
        if not self.IsElementExists(short_name):
            event = InitEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, InitEvent)

    def createAsynchronousServerCallReturnsEvent(self, short_name: str) -> AsynchronousServerCallReturnsEvent:
        if not self.IsElementExists(short_name):
            event = AsynchronousServerCallReturnsEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, AsynchronousServerCallReturnsEvent)

    def createDataReceivedEvent(self, short_name: str) -> DataReceivedEvent:
        if not self.IsElementExists(short_name):
            event = DataReceivedEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, DataReceivedEvent)

    def createSwcModeSwitchEvent(self, short_name: str) -> SwcModeSwitchEvent:
        if not self.IsElementExists(short_name):
            event = SwcModeSwitchEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, SwcModeSwitchEvent)

    def createInternalTriggerOccurredEvent(self, short_name: str) -> InternalTriggerOccurredEvent:
        if not self.IsElementExists(short_name):
            event = InternalTriggerOccurredEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, InternalTriggerOccurredEvent)

    def createSwcServiceDependency(self, short_name: str) -> SwcServiceDependency:
        if not self.IsElementExists(short_name):
            event = SwcServiceDependency(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, SwcServiceDependency)

    def createModeSwitchedAckEvent(self, short_name: str) -> ModeSwitchedAckEvent:
        if not self.IsElementExists(short_name):
            event = ModeSwitchedAckEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, ModeSwitchedAckEvent)

    def createBackgroundEvent(self, short_name: str) -> BackgroundEvent:
        if not self.IsElementExists(short_name):
            event = BackgroundEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, BackgroundEvent)

    def createDataSendCompletedEvent(self, short_name: str) -> DataSendCompletedEvent:
        if not self.IsElementExists(short_name):
            event = DataSendCompletedEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, DataSendCompletedEvent)

    def getRteEvents(self) -> List[RTEEvent]:
        return sorted(filter(lambda c: isinstance(c, RTEEvent), self.elements), key=lambda e: e.short_name)

    def getOperationInvokedEvents(self) -> List[OperationInvokedEvent]:
        return sorted(filter(lambda c: isinstance(c, OperationInvokedEvent), self.elements), key=lambda e: e.short_name)

    def getInitEvents(self) -> List[InitEvent]:
        return sorted(filter(lambda c: isinstance(c, InitEvent), self.elements), key=lambda e: e.short_name)

    def getTimingEvents(self) -> List[TimingEvent]:
        return sorted(filter(lambda c: isinstance(c, TimingEvent), self.elements), key=lambda e: e.short_name)

    def getDataReceivedEvents(self) -> List[DataReceivedEvent]:
        return sorted(filter(lambda c: isinstance(c, DataReceivedEvent), self.elements), key=lambda e: e.short_name)

    def getSwcModeSwitchEvents(self) -> List[SwcModeSwitchEvent]:
        return sorted(filter(lambda c: isinstance(c, SwcModeSwitchEvent), self.elements), key=lambda e: e.short_name)

    def getInternalTriggerOccurredEvents(self) -> List[InternalTriggerOccurredEvent]:
        return sorted(filter(lambda c: isinstance(c, InternalTriggerOccurredEvent), self.elements), key=lambda e: e.short_name)

    def getModeSwitchedAckEvents(self) -> List[ModeSwitchedAckEvent]:
        return sorted(filter(lambda c: isinstance(c, ModeSwitchedAckEvent), self.elements), key=lambda e: e.short_name)

    def getBackgroundEvents(self) -> List[BackgroundEvent]:
        return sorted(filter(lambda c: isinstance(c, BackgroundEvent), self.elements), key=lambda e: e.short_name)

    def getDataSendCompletedEvents(self) -> List[DataSendCompletedEvent]:
        return sorted(filter(lambda c: isinstance(c, DataSendCompletedEvent), self.elements), key=lambda e: e.short_name)

    def getSwcServiceDependencies(self) -> List[SwcServiceDependency]:
        return sorted(filter(lambda c: isinstance(c, SwcServiceDependency), self.elements), key=lambda e: e.short_name)

    def getEvent(self, short_name: str) -> RTEEvent:
        '''
        if (not isinstance(self.elements[short_name], RTEEvent)):
            raise ValueError("Invalid Event Type <%s> of <%s>" %
                             type(self.elements[short_name]), short_name)
        return self.elements[short_name]'
        '''
        return self.getElement(short_name, RTEEvent)

    def createImplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        if not self.IsElementExists(short_name):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.implicitInterRunnableVariables.append(prototype)
        return self.getElement(short_name)

    def createPerInstanceMemory(self, short_name: str) -> PerInstanceMemory:
        if not self.IsElementExists(short_name):
            memory = PerInstanceMemory(self, short_name)
            self.addElement(memory)
            self.perInstanceMemories.append(memory)
        return self.getElement(short_name)

    def createPerInstanceParameter(self, short_name: str) -> ParameterDataPrototype:
        if not self.IsElementExists(short_name):
            prototype = ParameterDataPrototype(self, short_name)
            self.addElement(prototype)
            self.perInstanceParameters.append(prototype)
        return self.getElement(short_name)

    def getVariableDataPrototypes(self) -> List[VariableDataPrototype]:
        return sorted(filter(lambda c: isinstance(c, VariableDataPrototype), self.elements), key=lambda e: e.short_name)

    def createRunnableEntity(self, short_name: str) -> RunnableEntity:
        if not self.IsElementExists(short_name):
            runnable = RunnableEntity(self, short_name)
            self.addElement(runnable)
        return self.getElement(short_name)

    def getRunnableEntities(self) -> List[RunnableEntity]:
        return sorted(filter(lambda c: isinstance(c, RunnableEntity), self.elements), key=lambda r: r.short_name)

    def getRunnableEntity(self, short_name) -> RunnableEntity:
        return self.getElement(short_name, RunnableEntity)

    def getSharedParameters(self) -> List[ParameterDataPrototype]:
        return self.sharedParameters

    def createSharedParameter(self, short_name: str) -> ParameterDataPrototype:
        if not self.IsElementExists(short_name):
            memory = ParameterDataPrototype(self, short_name)
            self.addElement(memory)
            self.sharedParameters.append(memory)
        return self.getElement(short_name)

    def getSupportsMultipleInstantiation(self):
        return self.supportsMultipleInstantiation

    def setSupportsMultipleInstantiation(self, value):
        self.supportsMultipleInstantiation = value
        return self


__all__ = [
    'AbstractAccessPoint',
    'ARBoolean',
    'ARLiteral',
    'AsynchronousServerCallPoint',
    'AsynchronousServerCallResultPoint',
    'AutosarParameterRef',
    'AutosarVariableRef',
    'BackgroundEvent',
    'Boolean',
    'DataReceivedEvent',
    'DataSendCompletedEvent',
    'ExecutableEntity',
    'ExternalTriggeringPoint',
    'IncludedDataTypeSet',
    'IncludedModeDeclarationGroupSet',
    'InitEvent',
    'InternalBehavior',
    'InternalTriggerOccurredEvent',
    'InternalTriggeringPoint',
    'ModeAccessPoint',
    'ModeSwitchPoint',
    'ModeSwitchedAckEvent',
    'OperationInvokedEvent',
    'ParameterAccess',
    'ParameterDataPrototype',
    'PerInstanceMemory',
    'PortAPIOption',
    'RefType',
    'RTEEvent',
    'RunnableEntity',
    'RunnableEntityArgument',
    'ServerCallPoint',
    'SwcInternalBehavior',
    'SwcModeSwitchEvent',
    'SwcServiceDependency',
    'SynchronousServerCallPoint',
    'TimingEvent',
    'VariableAccess',
    'VariableDataPrototype',
]


class SwcExclusiveAreaPolicy(ARObject):
    """Policy for SWC exclusive area management."""
    def __init__(self) -> None:
        super().__init__()
        self.policy: Union[str, None] = None

    def getPolicy(self):
        return self.policy

    def setPolicy(self, value):
        if value is not None:
            self.policy = value
        return self


class InstantiationDataDefProps(ARObject):
    """Instantiation-specific data definition properties."""
    def __init__(self) -> None:
        super().__init__()
        self.baseTypeRef: Union[RefType, None] = None

    def getBaseTypeRef(self):
        return self.baseTypeRef

    def setBaseTypeRef(self, value):
        if value is not None:
            self.baseTypeRef = value
        return self


class VariationPointProxy(ARObject):
    """Proxy for variation point handling."""
    def __init__(self) -> None:
        super().__init__()
        self.condition: Union[str, None] = None

    def getCondition(self):
        return self.condition

    def setCondition(self, value):
        if value is not None:
            self.condition = value
        return self

