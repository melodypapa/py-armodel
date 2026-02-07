"""
This module contains instance reference classes for data elements in AUTOSAR software component internal behavior templates.
"""

from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpInstanceRef,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class VariableInAtomicSWCTypeInstanceRef(AtpInstanceRef):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    def __init__(self) -> None:
        super().__init__()

        self.baseRef: Union[Union[RefType, None] , None] = None
        self.contextDataPrototypeRefs: List[RefType] = []
        self.portPrototypeRef: Union[Union[RefType, None] , None] = None
        self.rootVariableDataPrototypeRef: Union[Union[RefType, None] , None] = None
        self.targetDataPrototypeRef: Union[Union[RefType, None] , None] = None

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


class ParameterInAtomicSWCTypeInstanceRef(AtpInstanceRef):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    def __init__(self) -> None:
        super().__init__()

        self.baseRef: Union[Union[RefType, None] , None] = None
        self.contextDataPrototypeRef: Union[Union[RefType, None] , None] = None
        self.portPrototypeRef: Union[Union[RefType, None] , None] = None
        self.rootParameterDataPrototypeRef: Union[Union[RefType, None] , None] = None
        self.targetDataPrototypeRef: Union[Union[RefType, None] , None] = None

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

__all__ = [
    'VariableInAtomicSWCTypeInstanceRef',
    'ParameterInAtomicSWCTypeInstanceRef',
]
