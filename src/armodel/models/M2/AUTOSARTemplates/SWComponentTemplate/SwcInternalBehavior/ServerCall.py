"""
This module contains classes for representing AUTOSAR server call points
in software component internal behavior templates.
"""

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import ROperationInAtomicSwcInstanceRef

class ServerCallPoint(AbstractAccessPoint, ABC):

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is ServerCallPoint:
            raise TypeError("ServerCallPoint is an abstract class.")
        super().__init__(parent, short_name)

        self.operationIRef: 'ROperationInAtomicSwcInstanceRef' = None
        self.timeout: float = None

    def getOperationIRef(self):
        return self.operationIRef

    def setOperationIRef(self, value):
        self.operationIRef = value
        return self

    def getTimeout(self):
        return self.timeout

    def setTimeout(self, value):
        self.timeout = value
        return self


class AsynchronousServerCallPoint(ServerCallPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class SynchronousServerCallPoint(ServerCallPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.calledFromWithinExclusiveAreaRef = None
        self.timeout: float = None

    def getCalledFromWithinExclusiveAreaRef(self):
        return self.calledFromWithinExclusiveAreaRef

    def setCalledFromWithinExclusiveAreaRef(self, value):
        self.calledFromWithinExclusiveAreaRef = value
        return self


class AsynchronousServerCallResultPoint(AbstractAccessPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.asynchronousServerCallPointRef = None

    def getAsynchronousServerCallPointRef(self):
        return self.asynchronousServerCallPointRef

    def setAsynchronousServerCallPointRef(self, value):
        self.asynchronousServerCallPointRef = value
        return self
