"""
This module contains classes for representing AUTOSAR access count elements
in software component internal behavior templates.
"""

from abc import ABC

from ...GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ...GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AbstractAccessPoint(Identifiable, ABC):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AbstractAccessPoint:
            raise TypeError("ARObject is an abstract class.")
        
        super().__init__(parent, short_name)

        self.returnValueProvision = None

    def getReturnValueProvision(self):
        return self.returnValueProvision

    def setReturnValueProvision(self, value):
        if value is not None:
            self.returnValueProvision = value
        return self
