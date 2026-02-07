"""
This module contains classes for representing AUTOSAR software component implementation
elements in software component templates.
"""

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    Implementation,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
    String,
)


class SwcImplementation(Implementation):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.behaviorRef: Union[Union[RefType, None] , None] = None
        self.perInstanceMemorySizes = []
        self.requiredRTEVendor: Union[Union[String, None] , None] = None

    def getBehaviorRef(self):
        return self.behaviorRef

    def setBehaviorRef(self, value):
        self.behaviorRef = value
        return self

    def getPerInstanceMemorySizes(self):
        return self.perInstanceMemorySizes

    def addPerInstanceMemorySize(self, value):
        self.perInstanceMemorySizes.append(value)
        return self

    def getRequiredRTEVendor(self):
        return self.requiredRTEVendor

    def setRequiredRTEVendor(self, value):
        self.requiredRTEVendor = value
        return self
