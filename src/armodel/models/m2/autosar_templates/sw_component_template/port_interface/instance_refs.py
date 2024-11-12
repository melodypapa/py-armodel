from .....ar_ref import RefType
from ...generic_structure.abstract_structure import AtpInstanceRef

class ApplicationCompositeElementInPortInterfaceInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.baseRef = None                                         # type: RefType
        self.contextDataPrototypeRef = None                         # type: RefType
        self.rootDataPrototypeRef = None                            # type: RefType
        self.targetDataPrototypeRef = None                          # type: RefType

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
