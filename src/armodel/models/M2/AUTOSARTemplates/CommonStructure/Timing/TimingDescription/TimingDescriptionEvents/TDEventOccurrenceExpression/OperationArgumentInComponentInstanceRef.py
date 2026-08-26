from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class OperationArgumentInComponentInstanceRef(AtpInstanceRef):
    """
    Instance reference to be capable of referencing an argument of an operation in the context of a component.
    """

    # OperationArgumentInComponentInstanceRef method parity checklist:
    # Spec: (XSD-only - AUTOSAR_00052.xsd OPERATION-ARGUMENT-IN-COMPONENT-INSTANCE-REF group; no own AUTOSAR table)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getContextComponentRefs               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextComponentRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextPortPrototypeRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setContextPortPrototypeRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextOperationRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setContextOperationRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRootArgumentDataPrototypeRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRootArgumentDataPrototypeRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextDataPrototypeRefs           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextDataPrototypeRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetDataPrototypeRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetDataPrototypeRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Specifies the SW component prototype representing the context.
        self.contextComponentRefs: List[RefType] = []

        # Specifies the port prototype representing the context.
        self.contextPortPrototypeRef: Optional[RefType] = None

        # Specifies the client server operation representing the context.
        self.contextOperationRef: Optional[RefType] = None

        # Specifies the root argument data prototype representing the context.
        self.rootArgumentDataPrototypeRef: Optional[RefType] = None

        # Specifies the application composite element data prototype representing the context.
        self.contextDataPrototypeRefs: List[RefType] = []

        # Specifies the target data prototype (the argument instance target).
        self.targetDataPrototypeRef: Optional[RefType] = None

    def getContextComponentRefs(self) -> List[RefType]:
        """Specifies the SW component prototype representing the context."""
        return self.contextComponentRefs

    def addContextComponentRef(self, value: Optional[RefType]) -> "OperationArgumentInComponentInstanceRef":
        """Specifies the SW component prototype representing the context. A None value is a no-op and does not append anything."""
        if value is not None:
            self.contextComponentRefs.append(value)
        return self

    def getContextPortPrototypeRef(self) -> Optional[RefType]:
        """Specifies the port prototype representing the context."""
        return self.contextPortPrototypeRef

    def setContextPortPrototypeRef(self, value: Optional[RefType]) -> "OperationArgumentInComponentInstanceRef":
        """Specifies the port prototype representing the context. A None value is a no-op and does not overwrite an existing contextPortPrototypeRef."""
        if value is not None:
            self.contextPortPrototypeRef = value
        return self

    def getContextOperationRef(self) -> Optional[RefType]:
        """Specifies the client server operation representing the context."""
        return self.contextOperationRef

    def setContextOperationRef(self, value: Optional[RefType]) -> "OperationArgumentInComponentInstanceRef":
        """Specifies the client server operation representing the context. A None value is a no-op and does not overwrite an existing contextOperationRef."""
        if value is not None:
            self.contextOperationRef = value
        return self

    def getRootArgumentDataPrototypeRef(self) -> Optional[RefType]:
        """Specifies the root argument data prototype representing the context."""
        return self.rootArgumentDataPrototypeRef

    def setRootArgumentDataPrototypeRef(self, value: Optional[RefType]) -> "OperationArgumentInComponentInstanceRef":
        """Specifies the root argument data prototype representing the context. A None value is a no-op and does not overwrite an existing rootArgumentDataPrototypeRef."""
        if value is not None:
            self.rootArgumentDataPrototypeRef = value
        return self

    def getContextDataPrototypeRefs(self) -> List[RefType]:
        """Specifies the application composite element data prototype representing the context."""
        return self.contextDataPrototypeRefs

    def addContextDataPrototypeRef(self, value: Optional[RefType]) -> "OperationArgumentInComponentInstanceRef":
        """Specifies the application composite element data prototype representing the context. A None value is a no-op and does not append anything."""
        if value is not None:
            self.contextDataPrototypeRefs.append(value)
        return self

    def getTargetDataPrototypeRef(self) -> Optional[RefType]:
        """Specifies the target data prototype (the argument instance target)."""
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value: Optional[RefType]) -> "OperationArgumentInComponentInstanceRef":
        """Specifies the target data prototype (the argument instance target). A None value is a no-op and does not overwrite an existing targetDataPrototypeRef."""
        if value is not None:
            self.targetDataPrototypeRef = value
        return self
