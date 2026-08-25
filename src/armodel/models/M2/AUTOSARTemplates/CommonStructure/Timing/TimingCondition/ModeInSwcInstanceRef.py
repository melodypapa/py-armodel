from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class ModeInSwcInstanceRef(AtpInstanceRef):
    """
    Instance reference to be capable of referencing a ModeDeclaration at a specific Mode Switch Port of a SW-C.

    [constr_6899] Existence of ModeInSwcInstanceRef.base: For each ModeInSwcInstanceRef, the reference to SwComponentType in the role base shall exist at least once at the time when the Swc Timing Description is complete.
    [constr_6855] Existence of ModeInSwcInstanceRef.contextModeDeclarationGroupPrototype: For each ModeInSwcInstanceRef, the reference to ModeDeclarationGroupPrototype in the role contextModeDeclarationGroupPrototype shall exist at least once at the time when the Swc Timing Description is complete.
    [constr_6856] Existence of ModeInSwcInstanceRef.contextPort: For each ModeInSwcInstanceRef, the reference to PortPrototype in the role contextPort shall exist at least once at the time when the Swc Timing Description is complete.
    [constr_6857] Existence of ModeInSwcInstanceRef.targetModeDeclaration: For each ModeInSwcInstanceRef, the reference to ModeDeclaration in the role targetModeDeclaration shall exist at least once at the time when the Swc Timing Description is complete.

    The direct Python base AtpInstanceRef stands in for the abstract spec base ModeInSwcBswInstanceRef (not yet implemented as a model class).
    """

    # ModeInSwcInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.12, p.39
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBaseRef                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setBaseRef                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getContextComponentRefs              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextComponentRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextModeDeclarationGroupPrototypeRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setContextModeDeclarationGroupPrototypeRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextPortRef                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setContextPortRef                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetModeDeclarationRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetModeDeclarationRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Specifies the SW component representing the base of the context. Stereotypes: atpDerived [constr_6899] The reference shall exist at least once at the time when the Swc Timing Description is complete.
        self.baseRef: Optional[RefType] = None

        # Specifies the SW component prototype representing the context.
        self.contextComponentRefs: List[RefType] = []

        # Specifies the mode declaration group prototype that manifests the context. [constr_6855] The reference shall exist at least once at the time when the Swc Timing Description is complete.
        self.contextModeDeclarationGroupPrototypeRef: Optional[RefType] = None

        # Specifies the port prototype representing the context. [constr_6856] The reference shall exist at least once at the time when the Swc Timing Description is complete.
        self.contextPortRef: Optional[RefType] = None

        # Specifies the specific mode declaration in the given context. [constr_6857] The reference shall exist at least once at the time when the Swc Timing Description is complete.
        self.targetModeDeclarationRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """Specifies the SW component representing the base of the context. Stereotypes: atpDerived [constr_6899] The reference shall exist at least once at the time when the Swc Timing Description is complete."""
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "ModeInSwcInstanceRef":
        """Specifies the SW component representing the base of the context. Stereotypes: atpDerived [constr_6899] The reference shall exist at least once at the time when the Swc Timing Description is complete. A None value is a no-op and does not overwrite an existing baseRef."""
        if value is not None:
            self.baseRef = value
        return self

    def getContextComponentRefs(self) -> List[RefType]:
        """Specifies the SW component prototype representing the context."""
        return self.contextComponentRefs

    def addContextComponentRef(self, value: Optional[RefType]) -> "ModeInSwcInstanceRef":
        """Specifies the SW component prototype representing the context. A None value is a no-op and does not append anything."""
        if value is not None:
            self.contextComponentRefs.append(value)
        return self

    def getContextModeDeclarationGroupPrototypeRef(self) -> Optional[RefType]:
        """Specifies the mode declaration group prototype that manifests the context. [constr_6855] The reference shall exist at least once at the time when the Swc Timing Description is complete."""
        return self.contextModeDeclarationGroupPrototypeRef

    def setContextModeDeclarationGroupPrototypeRef(self, value: Optional[RefType]) -> "ModeInSwcInstanceRef":
        """Specifies the mode declaration group prototype that manifests the context. [constr_6855] The reference shall exist at least once at the time when the Swc Timing Description is complete. A None value is a no-op and does not overwrite an existing contextModeDeclarationGroupPrototypeRef."""
        if value is not None:
            self.contextModeDeclarationGroupPrototypeRef = value
        return self

    def getContextPortRef(self) -> Optional[RefType]:
        """Specifies the port prototype representing the context. [constr_6856] The reference shall exist at least once at the time when the Swc Timing Description is complete."""
        return self.contextPortRef

    def setContextPortRef(self, value: Optional[RefType]) -> "ModeInSwcInstanceRef":
        """Specifies the port prototype representing the context. [constr_6856] The reference shall exist at least once at the time when the Swc Timing Description is complete. A None value is a no-op and does not overwrite an existing contextPortRef."""
        if value is not None:
            self.contextPortRef = value
        return self

    def getTargetModeDeclarationRef(self) -> Optional[RefType]:
        """Specifies the specific mode declaration in the given context. [constr_6857] The reference shall exist at least once at the time when the Swc Timing Description is complete."""
        return self.targetModeDeclarationRef

    def setTargetModeDeclarationRef(self, value: Optional[RefType]) -> "ModeInSwcInstanceRef":
        """Specifies the specific mode declaration in the given context. [constr_6857] The reference shall exist at least once at the time when the Swc Timing Description is complete. A None value is a no-op and does not overwrite an existing targetModeDeclarationRef."""
        if value is not None:
            self.targetModeDeclarationRef = value
        return self
