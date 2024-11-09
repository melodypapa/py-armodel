from abc import ABCMeta
from .....ar_ref import AtpInstanceRef, RefType


class ModeGroupInAtomicSwcInstanceRef(AtpInstanceRef, metaclass = ABCMeta):
    def __init__(self):
        
        if type(self) == ModeGroupInAtomicSwcInstanceRef:
            raise NotImplementedError("ModeGroupInAtomicSwcInstanceRef is an abstract class.")
        
        super().__init__()

        self.baseRef = None                         # type: RefType
        self.contextPortRef = None                  # type: RefType
        self.targetRef = None                       # type: RefType

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

        self.contextPPortRef = None                         # type: RefType
        self.targetModeGroupRef = None                      # type: RefType

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

        self.contextRPortRef = None                                  # type: RefType
        self.targetModeGroupRef = None                               # type: RefType

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

        self.baseRef = None                                         # type: RefType
        self.contextModeDeclarationGroupPrototypeRef = None         # type: RefType
        self.contextPortRef = None                                  # type: RefType
        self.targetModeDeclarationRef = None                        # type: RefType

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
    
class VariableInAtomicSwcInstanceRef(AtpInstanceRef, metaclass = ABCMeta):
    def __init__(self):
        if type(self) == VariableInAtomicSwcInstanceRef:
            raise NotImplementedError("VariableInAtomicSwcInstanceRef is an abstract class.")

        super().__init__()

        self.abstractTargetDataElementRef = None                # type: RefType
        self.baseRef = None                                     # type: RefType
        self.contextPortRef = None                              # type: RefType

class RVariableInAtomicSwcInstanceRef(VariableInAtomicSwcInstanceRef):
    def __init__(self):
        super().__init__()

        self.contextRPortRef = None              # type: RefType
        self.targetDataElementRef = None         # type: RefType

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
