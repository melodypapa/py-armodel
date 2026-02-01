"""
This module contains classes for representing AUTOSAR instance references
in the SWComponentTemplate module. These classes are used for referencing
elements within atomic SWCs and compositions, particularly for mode groups
and data elements in instance contexts.
"""

from abc import ABC
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

