"""
This module contains classes for representing AUTOSAR instance references
in the SWComponentTemplate module. These classes are used for referencing
elements within atomic SWCs and compositions, particularly for mode groups
and data elements in instance contexts.
"""

from abc import ABC
from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class ModeGroupInAtomicSwcInstanceRef(AtpInstanceRef, ABC):
    def __init__(self):
        
        if type(self) == ModeGroupInAtomicSwcInstanceRef:
            raise TypeError("ModeGroupInAtomicSwcInstanceRef is an abstract class.")
        
        super().__init__()

        self.baseRef: RefType = None
        self.contextPortRef: RefType = None
        self.targetRef: RefType = None

    def getBaseRef(self):
        return self.baseRef

    def setBaseRef(self, value):
        self.baseRef = value
        return self

    def getContextPortRef(self):
        return self.contextPortRef

    def setContextPortRef(self, value):
        self.contextPortRef = value
        return self

    def getTargetRef(self):
        return self.targetRef

    def setTargetRef(self, value):
        self.targetRef = value
        return self


class PModeGroupInAtomicSwcInstanceRef(ModeGroupInAtomicSwcInstanceRef):
    def __init__(self):
        super().__init__()

        self.contextPPortRef: RefType = None
        self.targetModeGroupRef: RefType = None

    def getContextPPortRef(self):
        return self.contextPPortRef

    def setContextPPortRef(self, value):
        self.contextPPortRef = value
        return self

    def getTargetModeGroupRef(self):
        return self.targetModeGroupRef

    def setTargetModeGroupRef(self, value):
        self.targetModeGroupRef = value
        return self

class RModeGroupInAtomicSWCInstanceRef(ModeGroupInAtomicSwcInstanceRef):
    def __init__(self):
        super().__init__()

        self.contextRPortRef: RefType = None
        self.targetModeGroupRef: RefType = None

    def getContextRPortRef(self):
        return self.contextRPortRef

    def setContextRPortRef(self, value):
        self.contextRPortRef = value
        return self

    def getTargetModeGroupRef(self):
        return self.targetModeGroupRef

    def setTargetModeGroupRef(self, value):
        self.targetModeGroupRef = value
        return self


class RModeInAtomicSwcInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.baseRef: RefType = None
        self.contextModeDeclarationGroupPrototypeRef: RefType = None
        self.contextPortRef: RefType = None
        self.targetModeDeclarationRef: RefType = None

    def getBaseRef(self):
        return self.baseRef

    def setBaseRef(self, value):
        self.baseRef = value
        return self

    def getContextModeDeclarationGroupPrototypeRef(self):
        return self.contextModeDeclarationGroupPrototypeRef

    def setContextModeDeclarationGroupPrototypeRef(self, value):
        self.contextModeDeclarationGroupPrototypeRef = value
        return self

    def getContextPortRef(self):
        return self.contextPortRef

    def setContextPortRef(self, value):
        self.contextPortRef = value
        return self

    def getTargetModeDeclarationRef(self):
        return self.targetModeDeclarationRef

    def setTargetModeDeclarationRef(self, value):
        self.targetModeDeclarationRef = value
        return self
    
class VariableInAtomicSwcInstanceRef(AtpInstanceRef, ABC):
    def __init__(self):
        if type(self) == VariableInAtomicSwcInstanceRef:
            raise TypeError("VariableInAtomicSwcInstanceRef is an abstract class.")

        super().__init__()

        self.abstractTargetDataElementRef: RefType = None
        self.baseRef: RefType = None
        self.contextPortRef: RefType = None

class RVariableInAtomicSwcInstanceRef(VariableInAtomicSwcInstanceRef):
    def __init__(self):
        super().__init__()

        self.contextRPortRef: RefType = None
        self.targetDataElementRef: RefType = None

    def getContextRPortRef(self):
        return self.contextRPortRef

    def setContextRPortRef(self, value):
        self.contextRPortRef = value
        return self

    def getTargetDataElementRef(self):
        return self.targetDataElementRef

    def setTargetDataElementRef(self, value):
        self.targetDataElementRef = value
        return self

class InnerPortGroupInCompositionInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.baseRef: RefType = None
        self.contextRefs = []
        self.targetRef: RefType = None

    def getBaseRef(self):
        return self.baseRef

    def setBaseRef(self, value):
        self.baseRef = value
        return self

    def getContextRefs(self):
        return self.contextRefs

    def addContextRefs(self, value):
        self.contextRefs.append(value)
        return self

    def getTargetRef(self):
        return self.targetRef

    def setTargetRef(self, value):
        self.targetRef = value
        return self


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

