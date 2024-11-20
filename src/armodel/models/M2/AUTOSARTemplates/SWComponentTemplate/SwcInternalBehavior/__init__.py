from typing import Dict, List

from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import PortAPIOption
from .....M2.AUTOSARTemplates.CommonStructure.InternalBehavior import InternalBehavior
from .....M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory import PerInstanceMemory
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import DataReceivedEvent, InitEvent, InternalTriggerOccurredEvent, OperationInvokedEvent, RTEEvent, SwcModeSwitchEvent, TimingEvent
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import SwcServiceDependency
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType, ARBoolean
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import ParameterAccess, VariableAccess
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import ServerCallPoint
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import ModeAccessPoint, ModeSwitchPoint
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger import InternalTriggeringPoint
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ExecutableEntity

class RunnableEntityArgument(ARObject):
    def __init__(self):
        super().__init__()

        self.symbol = None                                      # type: ARLiteral

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, value):
        self.symbol = value
        return self

class AsynchronousServerCallPoint(ServerCallPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class AsynchronousServerCallResultPoint(ServerCallPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.asynchronousServerCallPointRef = None              # type: RefType

    def getAsynchronousServerCallPointRef(self):
        return self.asynchronousServerCallPointRef

    def setAsynchronousServerCallPointRef(self, value):
        self.asynchronousServerCallPointRef = value
        return self

class SynchronousServerCallPoint(ServerCallPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.calledFromWithinExclusiveAreaRef = None            # type: RefType

    def getCalledFromWithinExclusiveAreaRef(self):
        return self.calledFromWithinExclusiveAreaRef

    def setCalledFromWithinExclusiveAreaRef(self, value):
        self.calledFromWithinExclusiveAreaRef = value
        return self

class RunnableEntity(ExecutableEntity):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.arguments = []                             # type: List[RunnableEntityArgument]
        self.canBeInvokedConcurrently = None            # type: ARBoolean
        self.dataReadAccesses = {}                      # type: Dict[str, VariableAccess]
        self.dataReceivePointByArguments = {}           # type: Dict[str, VariableAccess]
        self.dataReceivePointByValues = {}              # type: Dict[str, VariableAccess]
        self.dataSendPoints = {}                        # type: Dict[str, VariableAccess]
        self.dataWriteAccesses = {}                     # type: Dict[str, VariableAccess]
        self.externalTriggeringPoints = {}              # type: Dict[str, ExternalTriggeringPoint]
        self.internalTriggeringPoints = {}              # type: Dict[str, InternalTriggeringPoint]
        self.modeAccessPoints = []                      # type: List[ModeAccessPoint]
        self.modeSwitchPoints = []                      # type: List[ModeSwitchPoint]
        self.parameterAccesses = {}                     # type: Dict[str, ParameterAccess]
        self.readLocalVariables = {}                    # type: Dict[str, VariableAccess]
        self.serverCallPoints = {}                      # type: Dict[str, ServerCallPoint]
        self.symbol = None                              # type: ARLiteral
        self.waitPoints = {}                            # type: Dict[str, WaitPoint]
        self.writtenLocalVariables = {}               # type: Dict[str, VariableAccess]

    def _createVariableAccess(self, short_name, variable_accesses: Dict[str, VariableAccess]):
        if (short_name not in self.elements):
            variable_access = VariableAccess(self, short_name)
            variable_accesses[short_name] = variable_access
        return variable_accesses[short_name]
    
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
        return sorted(self.dataReadAccesses.values(), key=lambda v: v.short_name)
    
    def createDataWriteAccess(self, short_name: str) -> VariableAccess:
       return self._createVariableAccess(short_name, self.dataWriteAccesses)

    def getDataWriteAccesses(self) -> List[VariableAccess]:
        return sorted(self.dataWriteAccesses.values(), key=lambda v: v.short_name)

    def createDataReceivePointByArgument(self, short_name: str) -> VariableAccess:
       return self._createVariableAccess(short_name, self.dataReceivePointByArguments)

    def getDataReceivePointByArguments(self) -> List[VariableAccess]:
        return sorted(self.dataReceivePointByArguments.values(), key=lambda v: v.short_name)

    def createDataReceivePointByValue(self, short_name: str) -> VariableAccess:
       return self._createVariableAccess(short_name, self.dataReceivePointByValues)

    def getDataReceivePointByValues(self) -> List[VariableAccess]:
        return sorted(self.dataReceivePointByValues.values(), key=lambda v: v.short_name)

    def createDataSendPoint(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.dataSendPoints)

    def getDataSendPoints(self) -> List[VariableAccess]:
        return sorted(self.dataSendPoints.values(), key=lambda v: v.short_name)

    def createReadLocalVariable(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.readLocalVariables)

    def getReadLocalVariables(self) -> List[VariableAccess]:
        return sorted(self.readLocalVariables.values(), key=lambda v: v.short_name)

    def createWrittenLocalVariable(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.writtenLocalVariables)

    def getWrittenLocalVariables(self) -> List[VariableAccess]:
        return sorted(self.writtenLocalVariables.values(), key=lambda v: v.short_name)
    
    def getParameterAccesses(self) -> List[ParameterAccess]:
        return list(sorted(filter(lambda a: isinstance(a, ParameterAccess), self.elements.values()), key= lambda o:o.short_name))
    
    def createParameterAccess(self, short_name: str) -> ParameterAccess:
        if (short_name not in self.elements):
            access = ParameterAccess(self, short_name)
            self.elements[short_name] = access
        return self.elements[short_name]
    
    def createSynchronousServerCallPoint(self, short_name: str) -> SynchronousServerCallPoint:
        if (short_name not in self.serverCallPoints):
            server_call_point = SynchronousServerCallPoint(self, short_name)
            self.serverCallPoints[short_name] = server_call_point
        return self.serverCallPoints[short_name]

    def createAsynchronousServerCallPoint(self, short_name: str) -> AsynchronousServerCallPoint:
        if (short_name not in self.serverCallPoints):
            server_call_point = AsynchronousServerCallPoint(self, short_name)
            self.serverCallPoints[short_name] = server_call_point
        return self.serverCallPoints[short_name]

    def getSynchronousServerCallPoint(self) -> List[ServerCallPoint]:
        return filter(lambda o: isinstance(o, SynchronousServerCallPoint), self.getServerCallPoints())
    
    def getAsynchronousServerCallPoint(self) -> List[ServerCallPoint]:
        return filter(lambda o: isinstance(o, AsynchronousServerCallPoint), self.getServerCallPoints())

    def getServerCallPoints(self) -> List[ServerCallPoint]:
        return sorted(self.serverCallPoints.values(), key=lambda v: v.short_name)

    def createInternalTriggeringPoint(self, short_name: str) -> InternalTriggeringPoint:
        if (short_name not in self.elements):
            point = InternalTriggeringPoint(self, short_name)
            self.elements[point.short_name] = point
        return self.elements[point.short_name]

    def getInternalTriggeringPoints(self) -> List[InternalTriggeringPoint]:
        return filter(lambda o: isinstance(o, InternalTriggeringPoint), self.elements)
    
    def getModeAccessPoints(self) -> List[ModeAccessPoint]:
        return self.modeAccessPoints
    
    def addModeAccessPoint(self, value):
        self.modeAccessPoints.append(value)
    
    def getModeSwitchPoints(self) -> List[ModeSwitchPoint]:
        return list(sorted(filter(lambda a: isinstance(a, ModeSwitchPoint), self.elements.values()), key= lambda o:o.short_name))
    
    def createModeSwitchPoint(self, short_name: str) -> ModeSwitchPoint:
        if (short_name not in self.elements):
            access = ModeSwitchPoint(self, short_name)
            self.elements[short_name] = access
            self.modeSwitchPoints.append(access)
        return self.elements[short_name]
    
    def getSymbol(self):
        return self.symbol

    def setSymbol(self, value):
        self.symbol = value
        return self


class SwcInternalBehavior(InternalBehavior):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.handle_termination_and_restart = None      # type: str
        self.supports_multiple_instantiation = None     # type: ARBoolean
        self.explicit_inter_runnable_variables = []     # type: List[VariableDataPrototype]
        self.implicit_inter_runnable_variables = []     # type: List[VariableDataPrototype]
        self.per_instance_memories = []                 # type: List[PerInstanceMemory]
        self.per_instance_parameters = []               # type: List[ParameterDataPrototype]
        self.port_api_options = []                      # type: List[PortAPIOption]
        self.included_data_type_sets = []               # type: List[IncludedDataTypeSet]

    def getExplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        return self.explicit_inter_runnable_variables

    def getImplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        return self.implicit_inter_runnable_variables

    def getPerInstanceMemories(self) -> List[PerInstanceMemory]:
        return self.per_instance_memories

    def getPerInstanceParameters(self) -> List[ParameterDataPrototype]:
        return self.per_instance_parameters

    def addPortAPIOption(self, option: PortAPIOption):
        self.port_api_options.append(option)

    def getPortAPIOptions(self) -> List[PortAPIOption]:
        return self.port_api_options

    def addIncludedDataTypeSet(self, set: IncludedDataTypeSet):
        self.included_data_type_sets.append(set)

    def getIncludedDataTypeSets(self) -> List[IncludedDataTypeSet]:
        return self.included_data_type_sets

    def createOperationInvokedEvent(self, short_name: str) -> OperationInvokedEvent:
        if (short_name not in self.elements):
            event = OperationInvokedEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def createTimingEvent(self, short_name: str) -> TimingEvent:
        if (short_name not in self.elements):
            event = TimingEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def createInitEvent(self, short_name: str) -> InitEvent:
        if (short_name not in self.elements):
            event = InitEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def createDataReceivedEvent(self, short_name: str) -> DataReceivedEvent:
        if (short_name not in self.elements):
            event = DataReceivedEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def createSwcModeSwitchEvent(self, short_name: str) -> SwcModeSwitchEvent:
        if (short_name not in self.elements):
            event = SwcModeSwitchEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def createInternalTriggerOccurredEvent(self, short_name: str) -> InternalTriggerOccurredEvent:
        if (short_name not in self.elements):
            event = InternalTriggerOccurredEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def createSwcServiceDependency(self, short_name: str) -> SwcServiceDependency:
        if (short_name not in self.elements):
            event = SwcServiceDependency(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getRteEvents(self) -> List[RTEEvent]:
        return sorted(filter(lambda c: isinstance(c, RTEEvent), self.elements.values()), key=lambda e: e.short_name)

    def getOperationInvokedEvents(self) -> List[OperationInvokedEvent]:
        return sorted(filter(lambda c: isinstance(c, OperationInvokedEvent), self.elements.values()), key=lambda e: e.short_name)

    def getInitEvents(self) -> List[InitEvent]:
        return sorted(filter(lambda c: isinstance(c, InitEvent), self.elements.values()), key=lambda e: e.short_name)

    def getTimingEvents(self) -> List[TimingEvent]:
        return sorted(filter(lambda c: isinstance(c, TimingEvent), self.elements.values()), key=lambda e: e.short_name)

    def getDataReceivedEvents(self) -> List[DataReceivedEvent]:
        return sorted(filter(lambda c: isinstance(c, DataReceivedEvent), self.elements.values()), key=lambda e: e.short_name)

    def getSwcModeSwitchEvents(self) -> List[SwcModeSwitchEvent]:
        return sorted(filter(lambda c: isinstance(c, SwcModeSwitchEvent), self.elements.values()), key=lambda e: e.short_name)

    def getInternalTriggerOccurredEvents(self) -> List[InternalTriggerOccurredEvent]:
        return sorted(filter(lambda c: isinstance(c, InternalTriggerOccurredEvent), self.elements.values()), key= lambda e: e.short_name)

    def getSwcServiceDependencies(self) -> List[SwcServiceDependency]:
        return sorted(filter(lambda c: isinstance(c, SwcServiceDependency), self.elements.values()), key= lambda e: e.short_name)

    def getEvent(self, short_name: str) -> RTEEvent:
        if (not isinstance(self.elements[short_name], RTEEvent)):
            raise ValueError("Invalid Event Type <%s> of <%s>" % type(self.elements[short_name]), short_name)
        return self.elements[short_name]

    def createExplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        if (short_name not in self.elements):
            prototype = VariableDataPrototype(self, short_name)
            self.elements[short_name] = prototype
            self.explicit_inter_runnable_variables.append(prototype)
        return self.elements[short_name]

    def createImplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        if (short_name not in self.elements):
            prototype = VariableDataPrototype(self, short_name)
            self.elements[short_name] = prototype
            self.implicit_inter_runnable_variables.append(prototype)
        return self.elements[short_name]

    def createPerInstanceMemory(self, short_name: str) -> PerInstanceMemory:
        if (short_name not in self.elements):
            memory = PerInstanceMemory(self, short_name)
            self.elements[short_name] = memory
            self.per_instance_memories.append(memory)
        return self.elements[short_name]

    def createPerInstanceParameter(self, short_name: str) -> ParameterDataPrototype:
        if (short_name not in self.elements):
            prototype = ParameterDataPrototype(self, short_name)
            self.elements[short_name] = prototype
            self.per_instance_parameters.append(prototype)
        return self.elements[short_name]

    def getVariableDataPrototypes(self) -> List[VariableDataPrototype]:
        return sorted(filter(lambda c: isinstance(c, VariableDataPrototype), self.elements.values()), key=lambda e: e.short_name)

    def createRunnableEntity(self, short_name: str) -> RunnableEntity:
        if (short_name not in self.elements):
            runnable = RunnableEntity(self, short_name)
            self.elements[short_name] = runnable
        return self.elements[short_name]

    def getRunnableEntities(self) -> List[RunnableEntity]:
        return sorted(filter(lambda c: isinstance(c, RunnableEntity), self.elements.values()), key=lambda r: r.short_name)

    def getRunnableEntity(self, short_name) -> RunnableEntity:
        return self.elements[short_name]

