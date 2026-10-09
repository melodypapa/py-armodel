"""
This module contains the AnyInstanceRef class for AUTOSAR models
in the GenericStructure module.
"""

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable


class AnyInstanceRef(AtpInstanceRef, VariationPointCapable):
    """
    Describes a reference to any instance in an AUTOSAR model. This is the most generic form of an instance ref. Refer to the superclass notes for more details.
    """

    # AnyInstanceRef method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.57, p.328
    # Spec verified: R23-11
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


class FunctionGroupStateInFunctionGroupSetInstanceRef(AtpInstanceRef):
    """
    Instance reference to a ModeDeclaration within a ModeDeclarationGroupPrototype (Adaptive Platform machine/FG state block list entry).
    """

    # FunctionGroupStateInFunctionGroupSetInstanceRef method parity checklist:
    # Spec: XSD-only (no own PDF/markdown table in the repo corpus) — AUTOSAR_00052.xsd group
    # FUNCTION-GROUP-STATE-IN-FUNCTION-GROUP-SET-INSTANCE-REF (pull-in — the
    # SecurityEventStateFilter.blockIfStateActiveAp iref member type)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextModeDeclarationGroupPrototypeRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContextModeDeclarationGroupPrototypeRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetModeDeclarationRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetModeDeclarationRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        self.contextModeDeclarationGroupPrototypeRef: Optional[RefType] = None

        self.targetModeDeclarationRef: Optional[RefType] = None

    def getContextModeDeclarationGroupPrototypeRef(self) -> Optional[RefType]:
        return self.contextModeDeclarationGroupPrototypeRef

    def setContextModeDeclarationGroupPrototypeRef(self, value: Optional[RefType]) -> "FunctionGroupStateInFunctionGroupSetInstanceRef":
        if value is not None:
            self.contextModeDeclarationGroupPrototypeRef = value
        return self

    def getTargetModeDeclarationRef(self) -> Optional[RefType]:
        return self.targetModeDeclarationRef

    def setTargetModeDeclarationRef(self, value: Optional[RefType]) -> "FunctionGroupStateInFunctionGroupSetInstanceRef":
        if value is not None:
            self.targetModeDeclarationRef = value
        return self
