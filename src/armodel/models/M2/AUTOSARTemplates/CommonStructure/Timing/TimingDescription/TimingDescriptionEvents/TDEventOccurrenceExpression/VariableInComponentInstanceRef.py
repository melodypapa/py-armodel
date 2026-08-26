from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class VariableInComponentInstanceRef(AtpInstanceRef):
    """
    Instance reference to be capable of referencing a variable of a software component in the context of a component.
    """

    # VariableInComponentInstanceRef method parity checklist:
    # Spec: (XSD-only - AUTOSAR_00052.xsd VARIABLE-IN-COMPONENT-INSTANCE-REF group; no own AUTOSAR table)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getContextComponentRefs             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextComponentRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextPortPrototypeRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setContextPortPrototypeRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRootVariableDataPrototypeRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRootVariableDataPrototypeRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextDataPrototypeRefs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextDataPrototypeRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetDataPrototypeRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetDataPrototypeRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Specifies the SW component prototype representing the context.
        self.contextComponentRefs: List[RefType] = []

        # Specifies the port prototype representing the context.
        self.contextPortPrototypeRef: Optional[RefType] = None

        # Specifies the root variable data prototype representing the context.
        self.rootVariableDataPrototypeRef: Optional[RefType] = None

        # Specifies the application composite element data prototype representing the context.
        self.contextDataPrototypeRefs: List[RefType] = []

        # Specifies the target data prototype (the variable instance target).
        self.targetDataPrototypeRef: Optional[RefType] = None

    def getContextComponentRefs(self) -> List[RefType]:
        """Specifies the SW component prototype representing the context."""
        return self.contextComponentRefs

    def addContextComponentRef(self, value: Optional[RefType]) -> "VariableInComponentInstanceRef":
        """Specifies the SW component prototype representing the context. A None value is a no-op and does not append anything."""
        if value is not None:
            self.contextComponentRefs.append(value)
        return self

    def getContextPortPrototypeRef(self) -> Optional[RefType]:
        """Specifies the port prototype representing the context."""
        return self.contextPortPrototypeRef

    def setContextPortPrototypeRef(self, value: Optional[RefType]) -> "VariableInComponentInstanceRef":
        """Specifies the port prototype representing the context. A None value is a no-op and does not overwrite an existing contextPortPrototypeRef."""
        if value is not None:
            self.contextPortPrototypeRef = value
        return self

    def getRootVariableDataPrototypeRef(self) -> Optional[RefType]:
        """Specifies the root variable data prototype representing the context."""
        return self.rootVariableDataPrototypeRef

    def setRootVariableDataPrototypeRef(self, value: Optional[RefType]) -> "VariableInComponentInstanceRef":
        """Specifies the root variable data prototype representing the context. A None value is a no-op and does not overwrite an existing rootVariableDataPrototypeRef."""
        if value is not None:
            self.rootVariableDataPrototypeRef = value
        return self

    def getContextDataPrototypeRefs(self) -> List[RefType]:
        """Specifies the application composite element data prototype representing the context."""
        return self.contextDataPrototypeRefs

    def addContextDataPrototypeRef(self, value: Optional[RefType]) -> "VariableInComponentInstanceRef":
        """Specifies the application composite element data prototype representing the context. A None value is a no-op and does not append anything."""
        if value is not None:
            self.contextDataPrototypeRefs.append(value)
        return self

    def getTargetDataPrototypeRef(self) -> Optional[RefType]:
        """Specifies the target data prototype (the variable instance target)."""
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value: Optional[RefType]) -> "VariableInComponentInstanceRef":
        """Specifies the target data prototype (the variable instance target). A None value is a no-op and does not overwrite an existing targetDataPrototypeRef."""
        if value is not None:
            self.targetDataPrototypeRef = value
        return self
