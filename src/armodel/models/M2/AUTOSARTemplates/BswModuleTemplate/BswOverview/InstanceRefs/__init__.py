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
    Aggregated by BswEvent.disabledInMode, BswModeSwitchEvent.mode,
    DiagnosticEnvBswModeElement.mode.
    """

    # ModeInBswModuleDescriptionInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table C.37, p.323
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBaseRef                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setBaseRef                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getContextModeDeclarationGroupRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setContextModeDeclarationGroupRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetModeRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetModeRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The BswModuleDescription that is the base of this instance ref.
        # Stereotypes: atpDerived (derived attribute, no XML element).
        self.baseRef: Optional[RefType] = None

        # This represents the context ModeDeclarationGroupPrototype.
        self.contextModeDeclarationGroupRef: Optional[RefType] = None

        # This represents the target mode declaration.
        self.targetModeRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        Gets the reference to the base BswModuleDescription.
        Derived attribute (atpDerived), so it has no XML element.

        Returns:
            RefType referencing the BswModuleDescription, or None if not set
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "ModeInBswModuleDescriptionInstanceRef":
        """
        Sets the reference to the base BswModuleDescription.
        A None value is a no-op and does not overwrite an existing reference.
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextModeDeclarationGroupRef(self) -> Optional[RefType]:
        """
        Gets the reference to the context ModeDeclarationGroupPrototype.

        Returns:
            RefType referencing the ModeDeclarationGroupPrototype, or None if not set
        """
        return self.contextModeDeclarationGroupRef

    def setContextModeDeclarationGroupRef(self, value: Optional[RefType]) -> "ModeInBswModuleDescriptionInstanceRef":
        """
        Sets the reference to the context ModeDeclarationGroupPrototype.
        A None value is a no-op and does not overwrite an existing reference.
        """
        if value is not None:
            self.contextModeDeclarationGroupRef = value
        return self

    def getTargetModeRef(self) -> Optional[RefType]:
        """
        Gets the reference to the target mode declaration.

        Returns:
            RefType referencing the ModeDeclaration, or None if not set
        """
        return self.targetModeRef

    def setTargetModeRef(self, value: Optional[RefType]) -> "ModeInBswModuleDescriptionInstanceRef":
        """
        Sets the reference to the target mode declaration.
        A None value is a no-op and does not overwrite an existing reference.
        """
        if value is not None:
            self.targetModeRef = value
        return self


__all__ = ["ModeInBswModuleDescriptionInstanceRef"]
