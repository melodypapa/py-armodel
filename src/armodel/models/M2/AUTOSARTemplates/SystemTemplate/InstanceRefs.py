# This module contains AUTOSAR System Template classes for instance references
# It defines variable and component instance references used in system modeling

from typing import List
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef


class VariableDataPrototypeInSystemInstanceRef(AtpInstanceRef):
    """
    Instance reference to a VariableDataPrototype in the context of a
    system model.
    """
    # VariableDataPrototypeInSystemInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] getContextComponentRefs      [x] impl  [ ] docstring  [ ] test
    # [ ] addContextComponentRef       [x] impl  [ ] docstring  [ ] test
    # [ ] getContextCompositionRef     [x] impl  [ ] docstring  [ ] test
    # [ ] setContextCompositionRef     [x] impl  [ ] docstring  [ ] test
    # [ ] getContextPortRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setContextPortRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetDataPrototypeRef    [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetDataPrototypeRef    [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.baseRef: RefType = None
        self.contextComponentRefs: List[RefType] = []
        self.contextCompositionRef: RefType = None
        self.contextPortRef: RefType = None
        self.targetDataPrototypeRef: RefType = None

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
    """
    Instance reference to a component in the context of a system model.
    """
    # ComponentInSystemInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] getContextComponentRefs      [x] impl  [ ] docstring  [ ] test
    # [ ] addContextComponentRef       [x] impl  [ ] docstring  [ ] test
    # [ ] getContextCompositionRef     [x] impl  [ ] docstring  [ ] test
    # [ ] setContextCompositionRef     [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetComponentRef        [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetComponentRef        [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        super().__init__()

        self.baseRef: RefType = None
        self.contextComponentRefs: List[RefType] = []
        self.contextCompositionRef: RefType = None
        self.targetComponentRef: RefType = None

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
