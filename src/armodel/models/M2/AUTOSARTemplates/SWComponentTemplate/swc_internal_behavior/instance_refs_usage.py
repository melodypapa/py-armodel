from typing import List

from ...GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ...GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ...GenericStructure.AbstractStructure import AtpInstanceRef

class ArVariableInImplementationDataInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.contextDataPrototypeRefs = []              # type: List[RefType]
        self.portPrototypeRef = None                    # type: RefType
        self.rootVariableDataPrototypeRef = None        # type: RefType
        self.targetDataPrototypeRef = None              # type: RefType

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

        self.baseRef = None                             # type: RefType
        self.contextDataPrototypeRefs = []              # type: List[RefType]
        self.portPrototypeRef = None                    # type: RefType
        self.rootVariableDataPrototypeRef = None        # type: RefType
        self.targetDataPrototypeRef = None              # type: RefType

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
    
class AutosarVariableRef(ARObject):
    def __init__(self):
        super().__init__()

        self.autosarVariableIRef = None             # type: VariableInAtomicSWCTypeInstanceRef 
        self.autosarVariableInImplDatatype = None   # type: ArVariableInImplementationDataInstanceRef
        self.localVariableRef = None

    def getAutosarVariableIRef(self):
        return self.autosarVariableIRef

    def setAutosarVariableIRef(self, value):
        self.autosarVariableIRef = value
        return self

    def getAutosarVariableInImplDatatype(self):
        return self.autosarVariableInImplDatatype

    def setAutosarVariableInImplDatatype(self, value):
        self.autosarVariableInImplDatatype = value
        return self

    def getLocalVariableRef(self):
        return self.localVariableRef

    def setLocalVariableRef(self, value):
        self.localVariableRef = value
        return self


class ParameterInAtomicSWCTypeInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.baseRef = None                                         # type: RefType
        self.contextDataPrototypeRef = None                         # type: RefType
        self.portPrototypeRef = None                                # type: RefType
        self.rootParameterDataPrototypeRef = None                   # type: RefType
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

        self.autosar_parameter_iref = None          # type: ParameterInAtomicSWCTypeInstanceRef
        self.local_parameter_ref = None             # type: RefType