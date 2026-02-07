# This module contains AUTOSAR System Template classes for instance references
# It defines variable and component instance references used in system modeling

from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpInstanceRef,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class VariableDataPrototypeInSystemInstanceRef(AtpInstanceRef):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    def __init__(self) -> None:
        super().__init__()

        self.baseRef: Union[Union[RefType, None] , None] = None
        self.contextComponentRefs: List[RefType] = []
        self.contextCompositionRef: Union[Union[RefType, None] , None] = None
        self.contextPortRef: Union[Union[RefType, None] , None] = None
        self.targetDataPrototypeRef: Union[Union[RefType, None] , None] = None

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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    def __init__(self) -> None:
        super().__init__()

        self.baseRef: Union[Union[RefType, None] , None] = None
        self.contextComponentRefs: List[RefType] = []
        self.contextCompositionRef: Union[Union[RefType, None] , None] = None
        self.targetComponentRef: Union[Union[RefType, None] , None] = None

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
