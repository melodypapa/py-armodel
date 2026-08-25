from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class ModeInBswInstanceRef(ARObject):
    """
    Instance reference to be capable of referencing a specific ModeDeclaration of a ModeDeclarationGroupPrototype utilized in a BSW module.

    [constr_6853] Existence of ModeInBswInstanceRef.contextModeDeclarationGroupPrototype: For each ModeInBswInstanceRef, the reference to ModeDeclarationGroupPrototype in the role contextModeDeclarationGroupPrototype shall exist at least once at the time when the Bsw Timing Description is complete.
    [constr_6854] Existence of ModeInBswInstanceRef.targetModeDeclaration: For each ModeInBswInstanceRef, the reference to ModeDeclaration in the role targetModeDeclaration shall exist at least once at the time when the Bsw Timing Description is complete.
    """

    # ModeInBswInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.11, p.38
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getContextBswImplementationRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setContextBswImplementationRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextModeDeclarationGroupPrototypeRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setContextModeDeclarationGroupPrototypeRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetModeDeclarationRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetModeDeclarationRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Specifies the BSW implementation that manifests the context.
        self.contextBswImplementationRef: Optional[RefType] = None

        # Specifies the mode declaration group prototype that manifests the context. [constr_6853] The reference shall exist at least once at the time when the Bsw Timing Description is complete.
        self.contextModeDeclarationGroupPrototypeRef: Optional[RefType] = None

        # Specifies the specific mode declaration in the given context. [constr_6854] The reference shall exist at least once at the time when the Bsw Timing Description is complete.
        self.targetModeDeclarationRef: Optional[RefType] = None

    def getContextBswImplementationRef(self) -> Optional[RefType]:
        """Specifies the BSW implementation that manifests the context."""
        return self.contextBswImplementationRef

    def setContextBswImplementationRef(self, value: Optional[RefType]) -> "ModeInBswInstanceRef":
        """Specifies the BSW implementation that manifests the context. A None value is a no-op and does not overwrite an existing contextBswImplementationRef."""
        if value is not None:
            self.contextBswImplementationRef = value
        return self

    def getContextModeDeclarationGroupPrototypeRef(self) -> Optional[RefType]:
        """Specifies the mode declaration group prototype that manifests the context. [constr_6853] The reference shall exist at least once at the time when the Bsw Timing Description is complete."""
        return self.contextModeDeclarationGroupPrototypeRef

    def setContextModeDeclarationGroupPrototypeRef(self, value: Optional[RefType]) -> "ModeInBswInstanceRef":
        """Specifies the mode declaration group prototype that manifests the context. [constr_6853] The reference shall exist at least once at the time when the Bsw Timing Description is complete. A None value is a no-op and does not overwrite an existing contextModeDeclarationGroupPrototypeRef."""
        if value is not None:
            self.contextModeDeclarationGroupPrototypeRef = value
        return self

    def getTargetModeDeclarationRef(self) -> Optional[RefType]:
        """Specifies the specific mode declaration in the given context. [constr_6854] The reference shall exist at least once at the time when the Bsw Timing Description is complete."""
        return self.targetModeDeclarationRef

    def setTargetModeDeclarationRef(self, value: Optional[RefType]) -> "ModeInBswInstanceRef":
        """Specifies the specific mode declaration in the given context. [constr_6854] The reference shall exist at least once at the time when the Bsw Timing Description is complete. A None value is a no-op and does not overwrite an existing targetModeDeclarationRef."""
        if value is not None:
            self.targetModeDeclarationRef = value
        return self
