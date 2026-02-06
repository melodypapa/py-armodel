"""
This module contains classes for representing AUTOSAR access count elements
in software component internal behavior templates.
"""

from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpStructureElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class AbstractAccessPoint(AtpStructureElement, ABC):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractAccessPoint:
            raise TypeError("ARObject is an abstract class.")

        super().__init__(parent, short_name)

        self.returnValueProvision = None

    def getReturnValueProvision(self):
        return self.returnValueProvision

    def setReturnValueProvision(self, value):
        if value is not None:
            self.returnValueProvision = value
        return self
