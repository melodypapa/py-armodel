"""
This module contains classes for representing AUTOSAR runnable entities
in software component internal behavior templates.
"""

from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    ExecutableEntity,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARBoolean,
    ARLiteral,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
    ParameterAccess,
    VariableAccess,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import (
    ModeAccessPoint,
    ModeSwitchPoint,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import (
    AsynchronousServerCallPoint,
    AsynchronousServerCallResultPoint,
    ServerCallPoint,
    SynchronousServerCallPoint,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger import (
    ExternalTriggeringPoint,
    InternalTriggeringPoint,
)


class RunnableEntityArgument(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.symbol = None

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, value):
        self.symbol = value
        return self


class RunnableEntity(ExecutableEntity):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.arguments: List[RunnableEntityArgument] = []
        self.asynchronousServerCallResultPoints: List[AsynchronousServerCallResultPoint] = []
        self.canBeInvokedConcurrently: Union[Union[ARBoolean, None] , None] = None
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
        self.symbol: Union[Union[ARLiteral, None] , None] = None
        self.waitPoints = {}
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
        return self.dataSendPoints

    def createReadLocalVariable(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.readLocalVariables)

    def getReadLocalVariables(self) -> List[VariableAccess]:
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

    def createAsynchronousServerCallPoint(self, short_name: str) -> AsynchronousServerCallPoint:
        if (short_name not in self.serverCallPoints):
            point = AsynchronousServerCallPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name, AsynchronousServerCallPoint)

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
        return sorted(filter(lambda a: isinstance(a, AsynchronousServerCallResultPoint), self.elements), key=lambda o: o.getShortName())

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
