"""
This module contains classes for representing AUTOSAR software component implementation
elements in software component templates.
"""

from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from ....M2.AUTOSARTemplates.CommonStructure.Implementation import Implementation

class SwcImplementation(Implementation):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.behaviorRef: RefType = None
        self.perInstanceMemorySizes = []
        self.requiredRTEVendor: String = None

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
