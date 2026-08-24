"""
This module contains the AnyInstanceRef class for AUTOSAR models
in the GenericStructure module.
"""

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef


class AnyInstanceRef(AtpInstanceRef):
    """
    Describes a reference to any instance in an AUTOSAR model. This is the most generic form of an instance ref. Refer to the superclass notes for more details.
    """

    # AnyInstanceRef method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.57, p.328
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBaseRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBaseRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextElementRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextElementRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This is the base from which navigation path begins. Stereotypes: atpDerived
        self.baseRef: Optional[RefType] = None

        # This is one step in the navigation path specified by the instance ref.
        self.contextElementRefs: List[RefType] = []

        # This is the target of the instance ref.
        self.targetRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        This is the base from which navigation path begins. Stereotypes: atpDerived
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "AnyInstanceRef":
        """
        This is the base from which navigation path begins. Stereotypes: atpDerived
        A None value is a no-op and does not overwrite an existing baseRef.
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextElementRefs(self) -> List[RefType]:
        """
        This is one step in the navigation path specified by the instance ref.
        """
        return self.contextElementRefs

    def addContextElementRef(self, value: Optional[RefType]) -> "AnyInstanceRef":
        """
        This is one step in the navigation path specified by the instance ref.
        """
        if value is not None:
            self.contextElementRefs.append(value)
        return self

    def getTargetRef(self) -> Optional[RefType]:
        """
        This is the target of the instance ref.
        """
        return self.targetRef

    def setTargetRef(self, value: Optional[RefType]) -> "AnyInstanceRef":
        """
        This is the target of the instance ref.
        A None value is a no-op and does not overwrite an existing targetRef.
        """
        if value is not None:
            self.targetRef = value
        return self
