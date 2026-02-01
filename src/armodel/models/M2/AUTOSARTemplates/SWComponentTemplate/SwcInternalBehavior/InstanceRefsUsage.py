"""
This module contains classes for representing AUTOSAR instance reference usages
in software component internal behavior templates.
"""

from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef

class ArVariableInImplementationDataInstanceRef(ARObject):
    def __init__(self):
        super().__init__()

        self.contextDataPrototypeRefs: List['RefType'] = []
        self.portPrototypeRef: 'RefType' = None
        self.rootVariableDataPrototypeRef: 'RefType' = None
        self.targetDataPrototypeRef: 'RefType' = None

    def getContextDataPrototypeRefs(self):
        return self.contextDataPrototypeRefs

    def setContextDataPrototypeRefs(self, value):
        self.contextDataPrototypeRefs = value
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

class VariableInAtomicSWCTypeInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.baseRef: 'RefType' = None
        self.contextDataPrototypeRefs: List['RefType'] = []
        self.portPrototypeRef: 'RefType' = None
        self.rootVariableDataPrototypeRef: 'RefType' = None
        self.targetDataPrototypeRef: 'RefType' = None

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

        self.baseRef: 'RefType' = None
        self.contextDataPrototypeRef: 'RefType' = None
        self.portPrototypeRef: 'RefType' = None
        self.rootParameterDataPrototypeRef: 'RefType' = None
        self.targetDataPrototypeRef: 'RefType' = None

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


class AutosarParameterRef(ARObject):
    def __init__(self):
        super().__init__()
        
        self.autosarParameterIRef: 'ParameterInAtomicSWCTypeInstanceRef' = None
        self.localParameterRef: 'RefType' = None

    def getAutosarParameterIRef(self):
        return self.autosarParameterIRef

    def setAutosarParameterIRef(self, value):
        self.autosarParameterIRef = value
        return self

    def getLocalParameterRef(self):
        return self.localParameterRef

    def setLocalParameterRef(self, value):
        self.localParameterRef = value
        return self
