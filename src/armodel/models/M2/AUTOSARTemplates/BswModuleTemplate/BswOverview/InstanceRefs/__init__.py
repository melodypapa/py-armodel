from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from typing import Optional


class ModeInBswModuleDescriptionInstanceRef(AtpInstanceRef):
    """
    Instance reference to a mode declaration of a BswModuleDescription, reached
    through a ModeDeclarationGroup.

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 323, Classic Platform
      R23-11)
    """

    # ModeInBswModuleDescriptionInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table C.37
    # [x] __init__                          [x] impl  [x] docstring  [x] test
    # [x] getBaseRef                        [x] impl  [x] docstring  [x] test
    # [x] setBaseRef                        [x] impl  [x] docstring  [x] test
    # [x] getContextModeDeclarationGroupRef [x] impl  [x] docstring  [x] test
    # [x] setContextModeDeclarationGroupRef [x] impl  [x] docstring  [x] test
    # [x] getTargetModeRef                  [x] impl  [x] docstring  [x] test
    # [x] setTargetModeRef                  [x] impl  [x] docstring  [x] test

    def __init__(self):
        super().__init__()

        # The BswModuleDescription that contains the referenced mode.
        # Stereotypes: atpDerived; Tags: xml.sequenceOffset=10.
        self.baseRef: Optional[RefType] = None

        # The context ModeDeclarationGroup through which the mode is referenced.
        # Tags: xml.sequenceOffset=20.
        self.contextModeDeclarationGroupRef: Optional[RefType] = None

        # The target mode declaration. Tags: xml.sequenceOffset=30.
        self.targetModeRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """Gets the reference to the BswModuleDescription containing the mode."""
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "ModeInBswModuleDescriptionInstanceRef":
        """Sets the base BswModuleDescription reference. No-op when None; returns self."""
        if value is not None:
            self.baseRef = value
        return self

    def getContextModeDeclarationGroupRef(self) -> Optional[RefType]:
        """Gets the reference to the context ModeDeclarationGroup."""
        return self.contextModeDeclarationGroupRef

    def setContextModeDeclarationGroupRef(self, value: Optional[RefType]) -> "ModeInBswModuleDescriptionInstanceRef":
        """Sets the context ModeDeclarationGroup reference. No-op when None; returns self."""
        if value is not None:
            self.contextModeDeclarationGroupRef = value
        return self

    def getTargetModeRef(self) -> Optional[RefType]:
        """Gets the reference to the target mode declaration."""
        return self.targetModeRef

    def setTargetModeRef(self, value: Optional[RefType]) -> "ModeInBswModuleDescriptionInstanceRef":
        """Sets the target mode reference. No-op when None; returns self."""
        if value is not None:
            self.targetModeRef = value
        return self


__all__ = ["ModeInBswModuleDescriptionInstanceRef"]
