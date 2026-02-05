"""
This module contains instance reference classes for data elements in AUTOSAR software component internal behavior templates.
"""

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpInstanceRef,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class VariableInAtomicSWCTypeInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.baseRef: RefType = None
        self.contextDataPrototypeRefs: List[RefType] = []
        self.portPrototypeRef: RefType = None
        self.rootVariableDataPrototypeRef: RefType = None
        self.targetDataPrototypeRef: RefType = None

    def getBaseRef(self):
        return self.baseRef

    def setBaseRef(self, value):
        self.baseRef = value
        return self

    def getContextDataPrototypeRefs(self):
        return self.contextDataPrototypeRefs

    def addContextDataPrototypeRef(self, value):
        self.contextDataPrototypeRefs.append(value)
        return self

    def getPortPrototypeRef(self):
        return self.portPrototypeRef

    def setPortPrototypeRef(self, value):
        self.portPrototypeRef = value
        return self

    def getRootVariableDataPrototypeRef(self):
        return self.rootVariableDataPrototypeRef

    def setRootVariableDataPrototypeRef(self, value):
        self.rootVariableDataPrototypeRef = value
        return self

    def getTargetDataPrototypeRef(self):
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value):
        self.targetDataPrototypeRef = value
        return self


class ParameterInAtomicSWCTypeInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.baseRef: RefType = None
        self.contextDataPrototypeRef: RefType = None
        self.portPrototypeRef: RefType = None
        self.rootParameterDataPrototypeRef: RefType = None
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

    def getPortPrototypeRef(self):
        return self.portPrototypeRef

    def setPortPrototypeRef(self, value):
        self.portPrototypeRef = value
        return self

    def getRootParameterDataPrototypeRef(self):
        return self.rootParameterDataPrototypeRef

    def setRootParameterDataPrototypeRef(self, value):
        self.rootParameterDataPrototypeRef = value
        return self

    def getTargetDataPrototypeRef(self):
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value):
        self.targetDataPrototypeRef = value
        return self

__all__ = [
    'VariableInAtomicSWCTypeInstanceRef',
    'ParameterInAtomicSWCTypeInstanceRef',
]
