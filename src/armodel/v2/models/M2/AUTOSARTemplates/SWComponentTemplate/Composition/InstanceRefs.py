"""
This module contains classes for representing AUTOSAR instance references
in composition contexts. These classes are used for referencing ports and
operations within compositions and atomic SWC instances.
"""

from typing import Union

from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpInstanceRef,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class PortInCompositionTypeInstanceRef(AtpInstanceRef, ABC):
    def __init__(self) -> None:
        if type(self) is PortInCompositionTypeInstanceRef:
            raise TypeError("PortInCompositionTypeInstanceRef is an abstract class.")

        super().__init__()

        self.abstractContextComponentRef: Union[Union[RefType, None] , None] = None
        self.baseRef: Union[Union[RefType, None] , None] = None
        self.targetPortRef: Union[Union[RefType, None] , None] = None

    def getAbstractContextComponentRef(self):
        return self.abstractContextComponentRef

    def setAbstractContextComponentRef(self, value):
        self.abstractContextComponentRef = value
        return self

    def getBaseRef(self):
        return self.baseRef

    def setBaseRef(self, value):
        self.baseRef = value
        return self

    def getTargetPortRef(self):
        return self.targetPortRef

    def setTargetPortRef(self, value):
        self.targetPortRef = value
        return self


class PPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    def __init__(self) -> None:
        super().__init__()

        self.contextComponentRef: Union[Union[RefType, None] , None] = None
        self.targetPPortRef: Union[Union[RefType, None] , None] = None

    def getContextComponentRef(self):
        return self.contextComponentRef

    def setContextComponentRef(self, value):
        self.contextComponentRef = value
        return self

    def getTargetPPortRef(self):
        return self.targetPPortRef

    def setTargetPPortRef(self, value):
        self.targetPPortRef = value
        return self


class RPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    def __init__(self) -> None:
        super().__init__()

        self.contextComponentRef: Union[Union[RefType, None] , None] = None
        self.targetRPortRef: Union[Union[RefType, None] , None] = None

    def getContextComponentRef(self):
        return self.contextComponentRef

    def setContextComponentRef(self, value):
        self.contextComponentRef = value
        return self

    def getTargetRPortRef(self):
        return self.targetRPortRef

    def setTargetRPortRef(self, value):
        self.targetRPortRef = value
        return self
