"""
This module contains classes for representing AUTOSAR server call points
in software component internal behavior templates.
"""

from abc import ABCMeta
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import ROperationInAtomicSwcInstanceRef

class ServerCallPoint(AbstractAccessPoint, metaclass=ABCMeta):

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
