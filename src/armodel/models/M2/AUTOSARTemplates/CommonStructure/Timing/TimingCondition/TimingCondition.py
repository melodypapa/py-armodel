from __future__ import annotations

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class ModeInSwcBswInstanceRef(ARObject, ABC):
    """
    Abstract base of ModeInBswInstanceRef and ModeInSwcInstanceRef.

    This class has no own AUTOSAR table; it is defined only as the common
    (abstract) base in the XSD group for the ModeIn* instance references used by
    TimingModeInstance.modeInstance. It is never serialized directly - the
    concrete subclasses ModeInBswInstanceRef and ModeInSwcInstanceRef carry the
    actual attributes and XML elements.
    """

    # ModeInSwcBswInstanceRef method parity checklist:
    # Spec: (XSD-only - no own AUTOSAR table)
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [ ] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        if type(self) is ModeInSwcBswInstanceRef:
            raise TypeError("ModeInSwcBswInstanceRef is an abstract class.")
        super().__init__()


class ModeInBswInstanceRef(ModeInSwcBswInstanceRef):
    """
    Instance reference to be capable of referencing a specific ModeDeclaration of a ModeDeclarationGroupPrototype utilized in a BSW module.

    [constr_6853] Existence of ModeInBswInstanceRef.contextModeDeclarationGroupPrototype: For each ModeInBswInstanceRef, the reference to ModeDeclarationGroupPrototype in the role contextModeDeclarationGroupPrototype shall exist at least once at the time when the Bsw Timing Description is complete.
    [constr_6854] Existence of ModeInBswInstanceRef.targetModeDeclaration: For each ModeInBswInstanceRef, the reference to ModeDeclaration in the role targetModeDeclaration shall exist at least once at the time when the Bsw Timing Description is complete.
    """

    # ModeInBswInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.11, p.38
    # Spec verified: R23-11
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


class ModeInSwcInstanceRef(AtpInstanceRef, ModeInSwcBswInstanceRef):
    """
    Instance reference to be capable of referencing a ModeDeclaration at a specific Mode Switch Port of a SW-C.

    [constr_6899] Existence of ModeInSwcInstanceRef.base: For each ModeInSwcInstanceRef, the reference to SwComponentType in the role base shall exist at least once at the time when the Swc Timing Description is complete.
    [constr_6855] Existence of ModeInSwcInstanceRef.contextModeDeclarationGroupPrototype: For each ModeInSwcInstanceRef, the reference to ModeDeclarationGroupPrototype in the role contextModeDeclarationGroupPrototype shall exist at least once at the time when the Swc Timing Description is complete.
    [constr_6856] Existence of ModeInSwcInstanceRef.contextPort: For each ModeInSwcInstanceRef, the reference to PortPrototype in the role contextPort shall exist at least once at the time when the Swc Timing Description is complete.
    [constr_6857] Existence of ModeInSwcInstanceRef.targetModeDeclaration: For each ModeInSwcInstanceRef, the reference to ModeDeclaration in the role targetModeDeclaration shall exist at least once at the time when the Swc Timing Description is complete.

    The Python bases AtpInstanceRef and ModeInSwcBswInstanceRef jointly stand in for the abstract spec base ModeInSwcBswInstanceRef.
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


class OperationArgumentInComponentInstanceRef(AtpInstanceRef):
    """
    Instance reference to be capable of referencing an argument of an operation in the context of a component.
    """

    # OperationArgumentInComponentInstanceRef method parity checklist:
    # Spec: (XSD-only - AUTOSAR_00046.xsd OPERATION-ARGUMENT-IN-COMPONENT-INSTANCE-REF group; no own AUTOSAR table)
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


class VariableInComponentInstanceRef(AtpInstanceRef):
    """
    Instance reference to be capable of referencing a variable of a software component in the context of a component.
    """

    # VariableInComponentInstanceRef method parity checklist:
    # Spec: (XSD-only - AUTOSAR_00046.xsd VARIABLE-IN-COMPONENT-INSTANCE-REF group; no own AUTOSAR table)
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


class TimingModeInstance(Identifiable):
    """
    This class specifies the mode declaration to be checked in a specific instance of a mode declaration group. This is used in a timing condition formula as an operand of the unary timing function TIMEX_mode Active to check whether the mode declaration is active at the point in time this expression is evaluated.
    """

    # TimingModeInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.10, p.37
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getModeInstance          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setModeInstance          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # This refers to a specific mode declaration in the given context.
        # Aggregates ModeInBswInstanceRef or ModeInSwcInstanceRef (polymorphic choice); both derive from the abstract ModeInSwcBswInstanceRef.
        self.modeInstance: Optional[ModeInSwcBswInstanceRef] = None

    def getModeInstance(self) -> Optional[ModeInSwcBswInstanceRef]:
        """This refers to a specific mode declaration in the given context."""
        return self.modeInstance

    def setModeInstance(self, value: Optional[ModeInSwcBswInstanceRef]) -> "TimingModeInstance":
        """This refers to a specific mode declaration in the given context. A None value is a no-op and does not overwrite an existing modeInstance."""
        if value is not None:
            self.modeInstance = value
        return self


class TimingCondition(Identifiable):
    """
    A TimingCondition describes a dependency on a specific condition. The element owns an expression which describes the timing condition dependency.
    """

    # TimingCondition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.7, p.35
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getTimingConditionFormula  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimingConditionFormula  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # This is the expression describing the dependency on a specific condition.
        self.timingConditionFormula: Optional[TimingConditionFormula] = None

    def getTimingConditionFormula(self) -> Optional[TimingConditionFormula]:
        """This is the expression describing the dependency on a specific condition."""
        return self.timingConditionFormula

    def setTimingConditionFormula(self, value: Optional[TimingConditionFormula]) -> "TimingCondition":
        """This is the expression describing the dependency on a specific condition. A None value is a no-op and does not overwrite an existing formula."""
        if value is not None:
            self.timingConditionFormula = value
        return self


class TimingConditionFormula(Referrable):
    """
    A TimingConditionFormula describes a specific dependency. The expression shall be a boolean expression addressing modes, variables, arguments, and/or events.
    """

    # TimingConditionFormula method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.8, p.35
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getText                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setText                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingArgumentRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimingArgumentRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingConditionRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimingConditionRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingEventRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimingEventRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingModeRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimingModeRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingVariableRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimingVariableRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This refers to an argument of an operation call.
        self.timingArgumentRef: Optional[RefType] = None

        # This refers to a timing condition that is part of an expression describing the dependency on a specific condition.
        self.timingConditionRef: Optional[RefType] = None

        # This refers to a timing event.
        self.timingEventRef: Optional[RefType] = None

        # This refers to a mode declaration.
        self.timingModeRef: Optional[RefType] = None

        # This refers to a variable.
        self.timingVariableRef: Optional[RefType] = None

        self._text: Optional[str] = None

    def getText(self) -> Optional[str]:
        """Returns the mixed string content (the boolean expression) of this <<atpMixedString>> TimingConditionFormula."""
        return self._text

    def setText(self, value: Optional[str]) -> "TimingConditionFormula":
        """Sets the mixed string content (the boolean expression) of this <<atpMixedString>> TimingConditionFormula. A None value is a no-op and does not overwrite an existing value."""
        if value is not None:
            self._text = value
        return self

    def getTimingArgumentRef(self) -> Optional[RefType]:
        """This refers to an argument of an operation call."""
        return self.timingArgumentRef

    def setTimingArgumentRef(self, value: Optional[RefType]) -> "TimingConditionFormula":
        """This refers to an argument of an operation call. A None value is a no-op and does not overwrite an existing timingArgumentRef."""
        if value is not None:
            self.timingArgumentRef = value
        return self

    def getTimingConditionRef(self) -> Optional[RefType]:
        """This refers to a timing condition that is part of an expression describing the dependency on a specific condition."""
        return self.timingConditionRef

    def setTimingConditionRef(self, value: Optional[RefType]) -> "TimingConditionFormula":
        """This refers to a timing condition that is part of an expression describing the dependency on a specific condition. A None value is a no-op and does not overwrite an existing timingConditionRef."""
        if value is not None:
            self.timingConditionRef = value
        return self

    def getTimingEventRef(self) -> Optional[RefType]:
        """This refers to a timing event."""
        return self.timingEventRef

    def setTimingEventRef(self, value: Optional[RefType]) -> "TimingConditionFormula":
        """This refers to a timing event. A None value is a no-op and does not overwrite an existing timingEventRef."""
        if value is not None:
            self.timingEventRef = value
        return self

    def getTimingModeRef(self) -> Optional[RefType]:
        """This refers to a mode declaration."""
        return self.timingModeRef

    def setTimingModeRef(self, value: Optional[RefType]) -> "TimingConditionFormula":
        """This refers to a mode declaration. A None value is a no-op and does not overwrite an existing timingModeRef."""
        if value is not None:
            self.timingModeRef = value
        return self

    def getTimingVariableRef(self) -> Optional[RefType]:
        """This refers to a variable."""
        return self.timingVariableRef

    def setTimingVariableRef(self, value: Optional[RefType]) -> "TimingConditionFormula":
        """This refers to a variable. A None value is a no-op and does not overwrite an existing timingVariableRef."""
        if value is not None:
            self.timingVariableRef = value
        return self


class TimingExtensionResource(Identifiable):
    """
    A TimingExtensionResource provides the capability to contain instance references referred from within a timing condition formula.
    """

    # TimingExtensionResource method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.9, p.36
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createTimingArgument     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingArguments       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createTimingMode         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingModes           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createTimingVariable     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingVariables       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This refers to an instance reference of an argument of an operation call.
        self.timingArguments: List[AutosarOperationArgumentInstance] = []

        # This refers to an instance reference of a mode declaration.
        self.timingModes: List[TimingModeInstance] = []

        # This refers to an instance reference of a variable.
        self.timingVariables: List[AutosarVariableInstance] = []

    def createTimingArgument(self, short_name: str) -> AutosarOperationArgumentInstance:
        """This refers to an instance reference of an argument of an operation call."""
        if not self.IsElementExists(short_name):
            argument = AutosarOperationArgumentInstance(self, short_name)
            self.addElement(argument)
            self.timingArguments.append(argument)
        return self.getElement(short_name, AutosarOperationArgumentInstance)

    def getTimingArguments(self) -> List[AutosarOperationArgumentInstance]:
        """This refers to an instance reference of an argument of an operation call."""
        return self.timingArguments

    def createTimingMode(self, short_name: str) -> TimingModeInstance:
        """This refers to an instance reference of a mode declaration."""
        if not self.IsElementExists(short_name):
            mode = TimingModeInstance(self, short_name)
            self.addElement(mode)
            self.timingModes.append(mode)
        return self.getElement(short_name, TimingModeInstance)

    def getTimingModes(self) -> List[TimingModeInstance]:
        """This refers to an instance reference of a mode declaration."""
        return self.timingModes

    def createTimingVariable(self, short_name: str) -> AutosarVariableInstance:
        """This refers to an instance reference of a variable."""
        if not self.IsElementExists(short_name):
            variable = AutosarVariableInstance(self, short_name)
            self.addElement(variable)
            self.timingVariables.append(variable)
        return self.getElement(short_name, AutosarVariableInstance)

    def getTimingVariables(self) -> List[AutosarVariableInstance]:
        """This refers to an instance reference of a variable."""
        return self.timingVariables


class AutosarVariableInstance(Identifiable):
    """
    This class represents a reference to a variable instance within AUTOSAR. This way it is possible to reference a variable instance in the occurrence expression formula. The variable instance can target to one of the following variables: • a variable provided via a PortPrototype as whole • an element inside of a composite variable provided via a PortPrototype
    """

    # AutosarVariableInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.52, p.85
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # variableInstanceIRef is an InstanceRef (VariableInComponentInstanceRef), read/written via its own reader/writer.
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getVariableInstanceIRef      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setVariableInstanceIRef      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This is the reference to the instanceRef definition. InstanceRef implemented by: VariableInComponentInstanceRef
        self.variableInstanceIRef: Optional[VariableInComponentInstanceRef] = None

    def getVariableInstanceIRef(self) -> Optional[VariableInComponentInstanceRef]:
        """This is the reference to the instanceRef definition. InstanceRef implemented by: VariableInComponentInstanceRef."""
        return self.variableInstanceIRef

    def setVariableInstanceIRef(self, value: Optional[VariableInComponentInstanceRef]) -> "AutosarVariableInstance":
        """This is the reference to the instanceRef definition. InstanceRef implemented by: VariableInComponentInstanceRef. A None value is a no-op and does not overwrite an existing variableInstanceIRef."""
        if value is not None:
            self.variableInstanceIRef = value
        return self


class AutosarOperationArgumentInstance(Identifiable):
    """
    This class represents a reference to an argument instance. This way it is possible to reference an argument instance in the occurrence expression formula. The argument instance can target to one of the following arguments: • a whole argument used in an operation of a PortPrototype with ClientServerInterface • an element inside of a composite argument used in an operation of a PortPrototype with ClientServer Interface
    """

    # AutosarOperationArgumentInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.53, p.85
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # operationArgumentInstanceIRef is an InstanceRef (OperationArgumentInComponentInstanceRef), read/written via its own reader/writer.
    # [x] __init__                               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getOperationArgumentInstanceIRef       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setOperationArgumentInstanceIRef       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This is the reference to the instanceRef definition. InstanceRef implemented by: OperationArgumentInComponentInstanceRef
        self.operationArgumentInstanceIRef: Optional[OperationArgumentInComponentInstanceRef] = None

    def getOperationArgumentInstanceIRef(self) -> Optional[OperationArgumentInComponentInstanceRef]:
        """This is the reference to the instanceRef definition. InstanceRef implemented by: OperationArgumentInComponentInstanceRef."""
        return self.operationArgumentInstanceIRef

    def setOperationArgumentInstanceIRef(self, value: Optional[OperationArgumentInComponentInstanceRef]) -> "AutosarOperationArgumentInstance":
        """This is the reference to the instanceRef definition. InstanceRef implemented by: OperationArgumentInComponentInstanceRef. A None value is a no-op and does not overwrite an existing operationArgumentInstanceIRef."""
        if value is not None:
            self.operationArgumentInstanceIRef = value
        return self
