from typing import Dict, List

from armodel.models_v2.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    ExecutableEntity,
    InternalBehavior,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARBoolean,
    ARLiteral,
    Boolean,
    RefType,
)
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    ParameterDataPrototype,
    VariableDataPrototype,
)
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import (
    AbstractAccessPoint,
)
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
    AutosarParameterRef,
    AutosarVariableRef,
    ParameterAccess,
    VariableAccess,
)
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import (
    IncludedDataTypeSet,
)
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import (
    IncludedModeDeclarationGroupSet,
    ModeAccessPoint,
    ModeSwitchPoint,
)
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory import (
    PerInstanceMemory,
)
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import (
    PortAPIOption,
)
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import (
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
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RunnableEntity import (
    RunnableEntity,
    RunnableEntityArgument,
)
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import (
    AsynchronousServerCallPoint,
    AsynchronousServerCallResultPoint,
    ServerCallPoint,
    SynchronousServerCallPoint,
)
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import (
    SwcServiceDependency,
)
from armodel.models_v2.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger import (
    ExternalTriggeringPoint,
    InternalTriggeringPoint,
)


class SwcInternalBehavior(InternalBehavior):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.arguments: List[RunnableEntityArgument] = []
        self.asynchronousServerCallResultPoints: List[AsynchronousServerCallResultPoint] = []
        self.canBeInvokedConcurrently: ARBoolean = None
        self.dataReadAccesses: List[VariableAccess] = []
        self.dataReceivePointByArguments: List[VariableAccess] = []
        self.dataReceivePointByValues: List[VariableAccess] = []
        self.dataSendPoints: List[VariableAccess] = []
        self.dataWriteAccesses: List[VariableAccess] = []
        self.externalTriggeringPoints: List[ExternalTriggeringPoint] = []
        self.internalTriggeringPoints: List[InternalTriggeringPoint] = []
        self.modeAccessPoints: List[ModeAccessPoint] = []
        self.modeSwitchPoints: List[ModeSwitchPoint] = []
        self.parameterAccesses: List[ParameterAccess] = []
        self.readLocalVariables: List[VariableAccess] = []
        self.serverCallPoints: List[ServerCallPoint] = []
        self.symbol: ARLiteral = None
        self.waitPoints = {}            # type: Dict[str, WaitPoint]
        self.writtenLocalVariables: List[VariableAccess] = []

    def _createVariableAccess(self, short_name, variable_accesses: List[VariableAccess]):
        if not self.IsElementExists(short_name):
            variable_access = VariableAccess(self, short_name)
            self.addElement(variable_access)
            variable_accesses.append(variable_access)
        return self.getElement(short_name, VariableAccess)

    def getArguments(self):
        return self.arguments

    def addArgument(self, value):
        self.arguments.append(value)
        return self

    def getCanBeInvokedConcurrently(self):
        return self.canBeInvokedConcurrently

    def setCanBeInvokedConcurrently(self, value):
        self.canBeInvokedConcurrently = value
        return self

    def createDataReadAccess(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.dataReadAccesses)

    def getDataReadAccesses(self) -> List[VariableAccess]:
        return sorted(self.dataReadAccesses, key=lambda v: v.short_name)

    def createDataWriteAccess(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.dataWriteAccesses)

    def getDataWriteAccesses(self) -> List[VariableAccess]:
        return sorted(self.dataWriteAccesses, key=lambda v: v.short_name)

    def createDataReceivePointByArgument(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.dataReceivePointByArguments)

    def getDataReceivePointByArguments(self) -> List[VariableAccess]:
        return sorted(self.dataReceivePointByArguments, key=lambda v: v.short_name)

    def createDataReceivePointByValue(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.dataReceivePointByValues)

    def getDataReceivePointByValues(self) -> List[VariableAccess]:
        return sorted(self.dataReceivePointByValues, key=lambda v: v.short_name)

    def createDataSendPoint(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.dataSendPoints)

    def getDataSendPoints(self) -> List[VariableAccess]:
        # return sorted(self.dataSendPoints.values(), key=lambda v: v.short_name)
        return self.dataSendPoints

    def createReadLocalVariable(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.readLocalVariables)

    def getReadLocalVariables(self) -> List[VariableAccess]:
        # return sorted(self.readLocalVariables.values(), key=lambda v: v.short_name)
        return self.readLocalVariables

    def createWrittenLocalVariable(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.writtenLocalVariables)

    def getWrittenLocalVariables(self) -> List[VariableAccess]:
        return self.writtenLocalVariables

    def getParameterAccesses(self) -> List[ParameterAccess]:
        return sorted(filter(lambda a: isinstance(a, ParameterAccess), self.elements), key=lambda o: o.short_name)

    def createParameterAccess(self, short_name: str) -> ParameterAccess:
        if not self.IsElementExists(short_name):
            access = ParameterAccess(self, short_name)
            self.addElement(access)
        return self.getElement(short_name)

    def createSynchronousServerCallPoint(self, short_name: str) -> SynchronousServerCallPoint:
        if (short_name not in self.serverCallPoints):
            point = SynchronousServerCallPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name)
        # self.serverCallPoints[short_name] = server_call_point
        # return self.serverCallPoints[short_name]

    def createAsynchronousServerCallPoint(self, short_name: str) -> AsynchronousServerCallPoint:
        if (short_name not in self.serverCallPoints):
            point = AsynchronousServerCallPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name, AsynchronousServerCallPoint)
        # self.serverCallPoints[short_name] = server_call_point
        # return self.serverCallPoints[short_name]

    def createAsynchronousServerCallResultPoint(self, short_name: str) -> AsynchronousServerCallResultPoint:
        if (short_name not in self.serverCallPoints):
            point = AsynchronousServerCallResultPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name)

    def getSynchronousServerCallPoint(self) -> List[SynchronousServerCallPoint]:
        return sorted(filter(lambda a: isinstance(a, SynchronousServerCallPoint), self.elements), key=lambda o: o.getShortName())

    def getAsynchronousServerCallPoint(self) -> List[AsynchronousServerCallPoint]:
        return sorted(filter(lambda a: isinstance(a, AsynchronousServerCallPoint), self.elements), key=lambda o: o.getShortName())

    def getAsynchronousServerCallResultPoints(self) -> List[AsynchronousServerCallResultPoint]:
        return list(sorted(filter(lambda a: isinstance(a, AsynchronousServerCallResultPoint), self.elements), key=lambda o: o.getShortName())) # noqa E501

    def getServerCallPoints(self) -> List[ServerCallPoint]:
        return sorted(filter(lambda a: isinstance(a, ServerCallPoint), self.elements), key=lambda o: o.getShortName())

    def createInternalTriggeringPoint(self, short_name: str) -> InternalTriggeringPoint:
        if not self.IsElementExists(short_name):
            point = InternalTriggeringPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name, InternalTriggeringPoint)

    def getInternalTriggeringPoints(self) -> List[InternalTriggeringPoint]:
        return filter(lambda o: isinstance(o, InternalTriggeringPoint), self.elements)

    def getModeAccessPoints(self) -> List[ModeAccessPoint]:
        return self.modeAccessPoints

    def addModeAccessPoint(self, value):
        self.modeAccessPoints.append(value)

    def getModeSwitchPoints(self) -> List[ModeSwitchPoint]:
        return sorted(filter(lambda a: isinstance(a, ModeSwitchPoint), self.elements), key=lambda o: o.short_name)

    def createModeSwitchPoint(self, short_name: str) -> ModeSwitchPoint:
        if not self.IsElementExists(short_name):
            access = ModeSwitchPoint(self, short_name)
            self.addElement(access)
            self.modeSwitchPoints.append(access)
        return self.getElement(short_name, ModeSwitchPoint)

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, value):
        self.symbol = value
        return self


class SwcInternalBehavior(InternalBehavior):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.arTypedPerInstanceMemories = []                        # type: List[VariableDataPrototype]
        self.events = []                                            # type: List[RTEEvent]
        self.exclusiveAreaPolicies = []                             # type: List[SwcExclusiveAreaPolicy]
        self.explicitInterRunnableVariables = []                    # type: List[VariableDataPrototype]
        self.handleTerminationAndRestart = None                     # type: str
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
        self.supportsMultipleInstantiation = None                   # type: Boolean
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

    def addPortAPIOption(self, option: PortAPIOption):
        self.portAPIOptions.append(option)

    def getPortAPIOptions(self) -> List[PortAPIOption]:
        return self.portAPIOptions

    def addIncludedDataTypeSet(self, set: IncludedDataTypeSet):
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
    'SwcInternalBehavior',
    'SwcInternalBehavior',
]
