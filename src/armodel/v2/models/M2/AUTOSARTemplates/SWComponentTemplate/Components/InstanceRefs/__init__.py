"""
This module contains classes for representing AUTOSAR instance references
in the SWComponentTemplate module. These classes are used for referencing
elements within atomic SWCs and compositions, particularly for mode groups
and data elements in instance contexts.
"""

from abc import ABC
from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpInstanceRef,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ModeGroupInAtomicSwcInstanceRef(AtpInstanceRef, ABC):
    def __init__(self) -> None:

        if type(self) is ModeGroupInAtomicSwcInstanceRef:
            raise TypeError("ModeGroupInAtomicSwcInstanceRef is an abstract class.")

        super().__init__()

        self.baseRef: Union[Union[RefType, None] , None] = None
        self.contextPortRef: Union[Union[RefType, None] , None] = None
        self.targetRef: Union[Union[RefType, None] , None] = None

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
    def __init__(self) -> None:
        super().__init__()

        self.contextPPortRef: Union[Union[RefType, None] , None] = None
        self.targetModeGroupRef: Union[Union[RefType, None] , None] = None

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
    def __init__(self) -> None:
        super().__init__()

        self.contextRPortRef: Union[Union[RefType, None] , None] = None
        self.targetModeGroupRef: Union[Union[RefType, None] , None] = None

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
    def __init__(self) -> None:
        super().__init__()

        self.baseRef: Union[Union[RefType, None] , None] = None
        self.contextModeDeclarationGroupPrototypeRef: Union[Union[RefType, None] , None] = None
        self.contextPortRef: Union[Union[RefType, None] , None] = None
        self.targetModeDeclarationRef: Union[Union[RefType, None] , None] = None

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

class VariableInAtomicSwcInstanceRef(AtpInstanceRef, ABC):
    def __init__(self) -> None:
        if type(self) is VariableInAtomicSwcInstanceRef:
            raise TypeError("VariableInAtomicSwcInstanceRef is an abstract class.")

        super().__init__()

        self.abstractTargetDataElementRef: Union[Union[RefType, None] , None] = None
        self.baseRef: Union[Union[RefType, None] , None] = None
        self.contextPortRef: Union[Union[RefType, None] , None] = None

class RVariableInAtomicSwcInstanceRef(VariableInAtomicSwcInstanceRef):
    def __init__(self) -> None:
        super().__init__()

        self.contextRPortRef: Union[Union[RefType, None] , None] = None
        self.targetDataElementRef: Union[Union[RefType, None] , None] = None

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

class InnerPortGroupInCompositionInstanceRef(AtpInstanceRef):
    def __init__(self) -> None:
        super().__init__()

        self.baseRef: Union[Union[RefType, None] , None] = None
        self.contextRefs = []
        self.targetRef: Union[Union[RefType, None] , None] = None

    def getBaseRef(self):
        return self.baseRef

    def setBaseRef(self, value):
        self.baseRef = value
        return self

    def getContextRefs(self):
        return self.contextRefs

    def addContextRefs(self, value):
        self.contextRefs.append(value)
        return self

    def getTargetRef(self):
        return self.targetRef

    def setTargetRef(self, value):
        self.targetRef = value
        return self


class OperationInAtomicSwcInstanceRef(AtpInstanceRef, ABC):
    def __init__(self) -> None:
        if type(self) is OperationInAtomicSwcInstanceRef:
            raise TypeError("OperationInAtomicSwcInstanceRef is an abstract class.")

        super().__init__()

        self.baseRef: Union[Union[RefType, None] , None] = None
        self.contextPortRef: Union[Union[RefType, None] , None] = None
        self.targetOperationRef: Union[Union[RefType, None] , None] = None

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
    def __init__(self) -> None:
        super().__init__()

        self.contextPPortRef: Union[Union[RefType, None] , None] = None
        self.targetProvidedOperationRef: Union[Union[RefType, None] , None] = None

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
    def __init__(self) -> None:
        super().__init__()

        self.contextRPortRef: Union[Union[RefType, None] , None] = None
        self.targetRequiredOperationRef: Union[Union[RefType, None] , None] = None

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






__all__ = [
    'ModeGroupInAtomicSwcInstanceRef',
    'PModeGroupInAtomicSwcInstanceRef',
    'RModeGroupInAtomicSWCInstanceRef',
    'RModeInAtomicSwcInstanceRef',
    'VariableInAtomicSwcInstanceRef',
    'RVariableInAtomicSwcInstanceRef',
    'InnerPortGroupInCompositionInstanceRef',
    'OperationInAtomicSwcInstanceRef',
    'POperationInAtomicSwcInstanceRef',
    'ROperationInAtomicSwcInstanceRef',
]
