from abc import ABCMeta
from ...GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ..Composition.InstanceRefs import ROperationInAtomicSwcInstanceRef
from .access_count import AbstractAccessPoint


class ServerCallPoint(AbstractAccessPoint, metaclass = ABCMeta):

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.operationIRef = None       # type: ROperationInAtomicSwcInstanceRef
        self.timeout = None             # type: float

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
