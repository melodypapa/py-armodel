from typing import Dict, List

from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import PortAPIOption
from .....M2.AUTOSARTemplates.CommonStructure.InternalBehavior import InternalBehavior
from .....M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory import PerInstanceMemory
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import AsynchronousServerCallReturnsEvent, BackgroundEvent, DataReceivedEvent, InitEvent, InternalTriggerOccurredEvent, ModeSwitchedAckEvent, OperationInvokedEvent, RTEEvent, SwcModeSwitchEvent, TimingEvent
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import SwcServiceDependency
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Boolean, RefType, ARBoolean
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
    
class AsynchronousServerCallResultPoint(AbstractAccessPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.asynchronousServerCallPointRef = None              # type: RefType

    def getAsynchronousServerCallPointRef(self):
        return self.asynchronousServerCallPointRef

    def setAsynchronousServerCallPointRef(self, value):
        self.asynchronousServerCallPointRef = value
        return self    

class AsynchronousServerCallPoint(ServerCallPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

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
        self.asynchronousServerCallResultPoints = []    # type: List[AsynchronousServerCallResultPoint]
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
            self.addElement(access)
        return self.getElement(short_name)
    
    def createSynchronousServerCallPoint(self, short_name: str) -> SynchronousServerCallPoint:
        if (short_name not in self.serverCallPoints):
            point = SynchronousServerCallPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name)
            #self.serverCallPoints[short_name] = server_call_point
        #return self.serverCallPoints[short_name]

    def createAsynchronousServerCallPoint(self, short_name: str) -> AsynchronousServerCallPoint:
        if (short_name not in self.serverCallPoints):
            point = AsynchronousServerCallPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name)
            #self.serverCallPoints[short_name] = server_call_point
        #return self.serverCallPoints[short_name]
    
    def createAsynchronousServerCallResultPoint(self, short_name: str) -> AsynchronousServerCallResultPoint:
        if (short_name not in self.serverCallPoints):
            point = AsynchronousServerCallResultPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name)

    def getSynchronousServerCallPoint(self) -> List[SynchronousServerCallPoint]:
        return list(sorted(filter(lambda a: isinstance(a, SynchronousServerCallPoint), self.elements.values()), key= lambda o:o.getShortName()))
    
    def getAsynchronousServerCallPoint(self) -> List[AsynchronousServerCallPoint]:
        return list(sorted(filter(lambda a: isinstance(a, AsynchronousServerCallPoint), self.elements.values()), key= lambda o:o.getShortName()))
    
    def getAsynchronousServerCallResultPoints(self) -> List[AsynchronousServerCallResultPoint]:
        return list(sorted(filter(lambda a: isinstance(a, AsynchronousServerCallResultPoint), self.elements.values()), key= lambda o:o.getShortName()))

    def getServerCallPoints(self) -> List[ServerCallPoint]:
        return list(sorted(filter(lambda a: isinstance(a, ServerCallPoint), self.elements.values()), key= lambda o:o.getShortName()))

    def createInternalTriggeringPoint(self, short_name: str) -> InternalTriggeringPoint:
        if (short_name not in self.elements):
            point = InternalTriggeringPoint(self, short_name)
            self.elements[point.short_name] = point
        return self.elements[short_name]

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
        self.variationPointProxies = []                             # type: VariationPointProxy

    def getArTypedPerInstanceMemories(self) -> List[VariableDataPrototype]:
        return self.arTypedPerInstanceMemories
    
    def createArTypedPerInstanceMemory(self, short_name: str) -> VariableDataPrototype:
        if (short_name not in self.elements):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.arTypedPerInstanceMemories.append(prototype)
        return self.getElement(short_name)

    def getExplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        return self.explicitInterRunnableVariables
    
    def createExplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        if (short_name not in self.elements):
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

    def createOperationInvokedEvent(self, short_name: str) -> OperationInvokedEvent:
        if (short_name not in self.elements):
            event = OperationInvokedEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name)

    def createTimingEvent(self, short_name: str) -> TimingEvent:
        if (short_name not in self.elements):
            event = TimingEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name)

    def createInitEvent(self, short_name: str) -> InitEvent:
        if (short_name not in self.elements):
            event = InitEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name)
    
    def createAsynchronousServerCallReturnsEvent(self, short_name: str) -> AsynchronousServerCallReturnsEvent:
        if (short_name not in self.elements):
            event = AsynchronousServerCallReturnsEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name)

    def createDataReceivedEvent(self, short_name: str) -> DataReceivedEvent:
        if (short_name not in self.elements):
            event = DataReceivedEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name)

    def createSwcModeSwitchEvent(self, short_name: str) -> SwcModeSwitchEvent:
        if (short_name not in self.elements):
            event = SwcModeSwitchEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name)

    def createInternalTriggerOccurredEvent(self, short_name: str) -> InternalTriggerOccurredEvent:
        if (short_name not in self.elements):
            event = InternalTriggerOccurredEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name)

    def createSwcServiceDependency(self, short_name: str) -> SwcServiceDependency:
        if (short_name not in self.elements):
            event = SwcServiceDependency(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]
    
    def createModeSwitchedAckEvent(self, short_name: str) -> ModeSwitchedAckEvent:
        if (short_name not in self.elements):
            event = ModeSwitchedAckEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name)
    
    def createBackgroundEvent(self, short_name: str) -> BackgroundEvent:
        if (short_name not in self.elements):
            event = BackgroundEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name)

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
    
    def getModeSwitchedAckEvents(self) -> List[ModeSwitchedAckEvent]:
        return sorted(filter(lambda c: isinstance(c, ModeSwitchedAckEvent), self.elements.values()), key= lambda e: e.short_name)
    
    def getBackgroundEvents(self) -> List[BackgroundEvent]:
        return sorted(filter(lambda c: isinstance(c, BackgroundEvent), self.elements.values()), key= lambda e: e.short_name)

    def getSwcServiceDependencies(self) -> List[SwcServiceDependency]:
        return sorted(filter(lambda c: isinstance(c, SwcServiceDependency), self.elements.values()), key= lambda e: e.short_name)

    def getEvent(self, short_name: str) -> RTEEvent:
        if (not isinstance(self.elements[short_name], RTEEvent)):
            raise ValueError("Invalid Event Type <%s> of <%s>" % type(self.elements[short_name]), short_name)
        return self.elements[short_name]

    def createImplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        if (short_name not in self.elements):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.implicitInterRunnableVariables.append(prototype)
        return self.getElement(short_name)

    def createPerInstanceMemory(self, short_name: str) -> PerInstanceMemory:
        if (short_name not in self.elements):
            memory = PerInstanceMemory(self, short_name)
            self.addElement(memory)
            self.perInstanceMemories.append(memory)
        return self.getElement(short_name)

    def createPerInstanceParameter(self, short_name: str) -> ParameterDataPrototype:
        if (short_name not in self.elements):
            prototype = ParameterDataPrototype(self, short_name)
            self.addElement(prototype)
            self.perInstanceParameters.append(prototype)
        return self.getElement(short_name)

    def getVariableDataPrototypes(self) -> List[VariableDataPrototype]:
        return sorted(filter(lambda c: isinstance(c, VariableDataPrototype), self.elements.values()), key=lambda e: e.short_name)

    def createRunnableEntity(self, short_name: str) -> RunnableEntity:
        if (short_name not in self.elements):
            runnable = RunnableEntity(self, short_name)
            self.addElement(runnable)
        return self.getElement(short_name)

    def getRunnableEntities(self) -> List[RunnableEntity]:
        return sorted(filter(lambda c: isinstance(c, RunnableEntity), self.elements.values()), key=lambda r: r.short_name)

    def getRunnableEntity(self, short_name) -> RunnableEntity:
        return self.elements[short_name]
    
    def getSharedParameters(self) -> List[ParameterDataPrototype]:
        return self.sharedParameters
    
    def createSharedParameter(self, short_name: str) -> ParameterDataPrototype:
        if (short_name not in self.elements):
            memory = ParameterDataPrototype(self, short_name)
            self.addElement(memory)
            self.sharedParameters.append(memory)
        return self.getElement(short_name) 

    def getSupportsMultipleInstantiation(self):
        return self.supportsMultipleInstantiation

    def setSupportsMultipleInstantiation(self, value):
        self.supportsMultipleInstantiation = value
        return self
