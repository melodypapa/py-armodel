
from typing import Dict, List

from ...GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral

from .data_elements import ParameterAccess, VariableAccess
from .server_call import ServerCallPoint
from .mode_declaration_group import ModeAccessPoint, ModeSwitchPoint
from .trigger import InternalTriggeringPoint

from ...GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ...GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean
from ...CommonStructure.InternalBehavior import ExecutableEntity
from ...GenericStructure.GeneralTemplateClasses.ArObject import ARObject


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

