
from abc import ABCMeta

from .....ar_ref import RefType
from ...GenericStructure.AbstractStructure import AtpInstanceRef


class PortInCompositionTypeInstanceRef(AtpInstanceRef, metaclass = ABCMeta):
    def __init__(self):
        if type(self) == PortInCompositionTypeInstanceRef:
            raise NotImplementedError("PortInCompositionTypeInstanceRef is an abstract class.")
        
        super().__init__()

        self.abstractContextComponentRef = None                 # type: RefType
        self.baseRef = None                                     # type: RefType
        self.targetPortRef = None                               # type: RefType

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
    def __init__(self):
        super().__init__()

        self.contextComponentRef = None                         # type: RefType
        self.targetPPortRef = None                              # type: RefType

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
    def __init__(self):
        super().__init__()

        self.contextComponentRef = None                         # type: RefType
        self.targetRPortRef = None                              # type: RefType

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

class OperationInAtomicSwcInstanceRef(AtpInstanceRef, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == OperationInAtomicSwcInstanceRef:
            raise NotImplementedError("OperationInAtomicSwcInstanceRef is an abstract class.")
        
        super().__init__()

        self.baseRef = None                         # type: RefType
        self.contextPortRef = None                  # type: RefType
        self.targetOperationRef = None              # type: RefType

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
    def __init__(self):
        super().__init__()

        self.contextPPortRef = None                 # type: RefType
        self.targetProvidedOperationRef = None      # type: RefType

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
    def __init__(self):
        super().__init__()

        self.contextRPortRef = None                     # type: RefType
        self.targetRequiredOperationRef = None          # type: RefType

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
