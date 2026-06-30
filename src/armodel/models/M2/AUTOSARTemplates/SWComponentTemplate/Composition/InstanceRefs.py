"""
This module contains classes for representing AUTOSAR instance references
in composition contexts. These classes are used for referencing ports and
operations within compositions and atomic SWC instances.
"""

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef

class PortInCompositionTypeInstanceRef(AtpInstanceRef, ABC):
    """
    Abstract base class for port instance references within a composition
    software component type.
    """

    def __init__(self):
        if type(self) is PortInCompositionTypeInstanceRef:
            raise TypeError("PortInCompositionTypeInstanceRef is an abstract class.")
        
        super().__init__()

        self.abstractContextComponentRef: RefType = None
        self.baseRef: RefType = None
        self.targetPortRef: RefType = None

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
    """
    Instance reference to a PPortPrototype within a composition software
    component type.
    """

    def __init__(self):
        super().__init__()

        self.contextComponentRef: RefType = None
        self.targetPPortRef: RefType = None

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
    """
    Instance reference to an RPortPrototype within a composition software
    component type.
    """

    def __init__(self):
        super().__init__()

        self.contextComponentRef: RefType = None
        self.targetRPortRef: RefType = None

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

class OperationInAtomicSwcInstanceRef(AtpInstanceRef, ABC):
    """
    Abstract base class for operation instance references within an atomic
    software component type.
    """

    def __init__(self):
        if type(self) is OperationInAtomicSwcInstanceRef:
            raise TypeError("OperationInAtomicSwcInstanceRef is an abstract class.")
        
        super().__init__()

        self.baseRef: RefType = None
        self.contextPortRef: RefType = None
        self.targetOperationRef: RefType = None

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

    def getTargetOperationRef(self):
        return self.targetOperationRef

    def setTargetOperationRef(self, value):
        self.targetOperationRef = value
        return self

class POperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    """
    Instance reference to a provided operation in an atomic software
    component through a PPortPrototype.
    """

    def __init__(self):
        super().__init__()

        self.contextPPortRef: RefType = None
        self.targetProvidedOperationRef: RefType = None

    def getContextPPortRef(self):
        return self.contextPPortRef

    def setContextPPortRef(self, value):
        self.contextPPortRef = value
        return self

    def getTargetProvidedOperationRef(self):
        return self.targetProvidedOperationRef

    def setTargetProvidedOperationRef(self, value):
        self.targetProvidedOperationRef = value
        return self


class ROperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    """
    Instance reference to a required operation in an atomic software
    component through an RPortPrototype.
    """

    def __init__(self):
        super().__init__()

        self.contextRPortRef: RefType = None
        self.targetRequiredOperationRef: RefType = None

    def getContextRPortRef(self):
        return self.contextRPortRef

    def setContextRPortRef(self, value):
        self.contextRPortRef = value
        return self

    def getTargetRequiredOperationRef(self):
        return self.targetRequiredOperationRef

    def setTargetRequiredOperationRef(self, value):
        self.targetRequiredOperationRef = value
        return self
