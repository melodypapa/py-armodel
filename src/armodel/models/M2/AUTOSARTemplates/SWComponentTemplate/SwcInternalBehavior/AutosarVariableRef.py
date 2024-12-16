from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import ArVariableInImplementationDataInstanceRef, VariableInAtomicSWCTypeInstanceRef

class AutosarVariableRef(ARObject):
    def __init__(self):
        super().__init__()

        self.autosarVariableIRef = None                             # type: VariableInAtomicSWCTypeInstanceRef 
        self.autosarVariableInImplDatatype = None                   # type: ArVariableInImplementationDataInstanceRef
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