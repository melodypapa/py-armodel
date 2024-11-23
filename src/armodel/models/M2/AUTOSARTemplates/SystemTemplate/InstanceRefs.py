from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef

class VariableDataPrototypeInSystemInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.baseRef = None                                         # type: RefType
        self.contextComponentRefs = []                              # type: List[RefType]
        self.contextCompositionRef = None                           # type: RefType
        self.contextPortRef = None                                  # type: RefType
        self.targetDataPrototypeRef = None                          # type: RefType

    def getBaseRef(self):
        return self.baseRef

    def setBaseRef(self, value):
        self.baseRef = value
        return self

    def getContextComponentRefs(self):
        return self.contextComponentRefs

    def addContextComponentRef(self, value):
        self.contextComponentRefs.append(value)
        return self

    def getContextCompositionRef(self):
        return self.contextCompositionRef

    def setContextCompositionRef(self, value):
        self.contextCompositionRef = value
        return self

    def getContextPortRef(self):
        return self.contextPortRef

    def setContextPortRef(self, value):
        self.contextPortRef = value
        return self

    def getTargetDataPrototypeRef(self):
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value):
        self.targetDataPrototypeRef = value
        return self

class ComponentInSystemInstanceRef(AtpInstanceRef):
    def __init__(self):
        super().__init__()

        self.baseRef = None                         # type: RefType
        self.contextComponentRefs = []              # type: List[RefType]
        self.contextCompositionRef = None           # type: RefType
        self.targetComponentRef = None              # type: RefType

    def getBaseRef(self):
        return self.baseRef

    def setBaseRef(self, value):
        self.baseRef = value
        return self

    def getContextComponentRefs(self):
        return self.contextComponentRefs

    def addContextComponentRef(self, value):
        self.contextComponentRefs.append(value)
        return self

    def getContextCompositionRef(self):
        return self.contextCompositionRef

    def setContextCompositionRef(self, value):
        self.contextCompositionRef = value
        return self

    def getTargetComponentRef(self):
        return self.targetComponentRef

    def setTargetComponentRef(self, value):
        self.targetComponentRef = value
        return self
