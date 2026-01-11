"""
This module contains classes for representing AUTOSAR instance references
in port interface contexts. These classes are used for referencing data
elements within port interfaces and compositions.
"""

from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from .....M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef

class ApplicationCompositeElementInPortInterfaceInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.baseRef: RefType = None
        self.contextDataPrototypeRef: RefType = None
        self.rootDataPrototypeRef: RefType = None
        self.targetDataPrototypeRef: RefType = None

    def getBaseRef(self):
        return self.baseRef

    def setBaseRef(self, value):
        self.baseRef = value
        return self

    def getContextDataPrototypeRef(self):
        return self.contextDataPrototypeRef

    def setContextDataPrototypeRef(self, value):
        self.contextDataPrototypeRef = value
        return self

    def getRootDataPrototypeRef(self):
        return self.rootDataPrototypeRef

    def setRootDataPrototypeRef(self, value):
        self.rootDataPrototypeRef = value
        return self

    def getTargetDataPrototypeRef(self):
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value):
        self.targetDataPrototypeRef = value
        return self
