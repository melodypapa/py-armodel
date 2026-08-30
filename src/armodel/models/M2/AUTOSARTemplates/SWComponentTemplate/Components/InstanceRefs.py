"""
This module contains classes for representing AUTOSAR instance references
in the SWComponentTemplate module. These classes are used for referencing
elements within atomic SWCs and compositions, particularly for mode groups
and data elements in instance contexts.
"""

from abc import ABC
from typing import Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class ModeGroupInAtomicSwcInstanceRef(AtpInstanceRef, ABC):
    """
    Abstract base class for mode group instance references within an atomic
    software component type.
    """

    # ModeGroupInAtomicSwcInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] getContextPortRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setContextPortRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetRef                 [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetRef                 [x] impl  [ ] docstring  [ ] test

    def __init__(self):

        if type(self) is ModeGroupInAtomicSwcInstanceRef:
            raise TypeError("ModeGroupInAtomicSwcInstanceRef is an abstract class.")

        super().__init__()

        self.baseRef: RefType = None
        self.contextPortRef: RefType = None
        self.targetRef: RefType = None

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
    """
    Instance reference to a mode group in an atomic software component
    through a PPortPrototype.
    """

    # PModeGroupInAtomicSwcInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getContextPPortRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setContextPPortRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetModeGroupRef        [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetModeGroupRef        [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.contextPPortRef: RefType = None
        self.targetModeGroupRef: RefType = None

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
    """
    Instance reference to a mode group in an atomic software component
    through an RPortPrototype.
    """

    # RModeGroupInAtomicSWCInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getContextRPortRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setContextRPortRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetModeGroupRef        [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetModeGroupRef        [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.contextRPortRef: RefType = None
        self.targetModeGroupRef: RefType = None

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
    """
    Instance reference to a mode declaration in an atomic software component
    through an RPortPrototype.
    """

    # RModeInAtomicSwcInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] getContextModeDeclarationGroupPrototypeRef [x] impl  [ ] docstring  [ ] test
    # [ ] setContextModeDeclarationGroupPrototypeRef [x] impl  [ ] docstring  [ ] test
    # [ ] getContextPortRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setContextPortRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetModeDeclarationRef  [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetModeDeclarationRef  [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.baseRef: RefType = None
        self.contextModeDeclarationGroupPrototypeRef: RefType = None
        self.contextPortRef: RefType = None
        self.targetModeDeclarationRef: RefType = None

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


class TriggerInAtomicSwcInstanceRef(AtpInstanceRef, ABC):
    """
    Abstract base class for instance references to a Trigger in an atomic
    software component type, referencing the trigger through a port of the
    atomic SWC (concretized by PTriggerInAtomicSwcTypeInstanceRef and
    RTriggerInAtomicSwcInstanceRef).
    """

    # TriggerInAtomicSwcInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.5, p.944
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getBaseRef                   [x] impl  [x] docstring  [x] test
    # [x] setBaseRef                   [x] impl  [x] docstring  [x] test
    # [x] getContextPortRef            [x] impl  [x] docstring  [x] test
    # [x] setContextPortRef            [x] impl  [x] docstring  [x] test
    # [x] getTargetRef                 [x] impl  [x] docstring  [x] test
    # [x] setTargetRef                 [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the TriggerInAtomicSwcInstanceRef with default values.
        """
        if type(self) is TriggerInAtomicSwcInstanceRef:
            raise TypeError("TriggerInAtomicSwcInstanceRef is an abstract class.")

        super().__init__()

        # The AtomicSwComponentType in which the referenced Trigger lives.
        # Stereotypes: atpDerived (derived attribute, no XML element).
        self.baseRef: Optional[RefType] = None

        # The context port through which the referenced Trigger is reached.
        # Stereotypes: atpAbstract (concretized by the subclasses' contextPPort/contextRPort).
        self.contextPortRef: Optional[RefType] = None

        # The Trigger that is referenced through the context port.
        # Stereotypes: atpAbstract (concretized by the subclasses' targetTrigger).
        self.targetRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        Gets the reference to the AtomicSwComponentType in which the referenced
        Trigger lives. Derived attribute (atpDerived), so it has no XML element.

        Returns:
            Optional[RefType]: The atomic SWC reference
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "TriggerInAtomicSwcInstanceRef":
        """
        Sets the reference to the AtomicSwComponentType in which the referenced
        Trigger lives. Only sets the value if it is not None, and returns self
        for method chaining.

        Args:
            value: The atomic SWC reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextPortRef(self) -> Optional[RefType]:
        """
        Gets the context port through which the referenced Trigger is reached.
        Abstract attribute (atpAbstract), concretized by the subclasses.

        Returns:
            Optional[RefType]: The context port reference
        """
        return self.contextPortRef

    def setContextPortRef(self, value: Optional[RefType]) -> "TriggerInAtomicSwcInstanceRef":
        """
        Sets the context port through which the referenced Trigger is reached.
        Only sets the value if it is not None, and returns self for method
        chaining.

        Args:
            value: The context port reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.contextPortRef = value
        return self

    def getTargetRef(self) -> Optional[RefType]:
        """
        Gets the Trigger that is referenced through the context port. Abstract
        attribute (atpAbstract), concretized by the subclasses' targetTrigger.

        Returns:
            Optional[RefType]: The target trigger reference
        """
        return self.targetRef

    def setTargetRef(self, value: Optional[RefType]) -> "TriggerInAtomicSwcInstanceRef":
        """
        Sets the Trigger that is referenced through the context port. Only sets
        the value if it is not None, and returns self for method chaining.

        Args:
            value: The target trigger reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.targetRef = value
        return self


class PTriggerInAtomicSwcTypeInstanceRef(TriggerInAtomicSwcInstanceRef):
    """
    Instance reference to a Trigger in an atomic software component type
    through a provided port (PPortPrototype), used e.g. by
    SwcBswSynchronizedTrigger.swcTrigger.
    """

    # PTriggerInAtomicSwcTypeInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.7, p.946
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getContextPPortRef           [x] impl  [x] docstring  [x] test
    # [x] setContextPPortRef           [x] impl  [x] docstring  [x] test
    # [x] getTargetTriggerRef          [x] impl  [x] docstring  [x] test
    # [x] setTargetTriggerRef          [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the PTriggerInAtomicSwcTypeInstanceRef with default values.
        """
        super().__init__()

        # The provided port (PPortPrototype) through which the Trigger is referenced.
        self.contextPPortRef: Optional[RefType] = None

        # The Trigger that is referenced through the provided port.
        self.targetTriggerRef: Optional[RefType] = None

    def getContextPPortRef(self) -> Optional[RefType]:
        """
        Gets the provided port (PPortPrototype) through which the referenced
        Trigger is reached.

        Returns:
            Optional[RefType]: The provided port reference
        """
        return self.contextPPortRef

    def setContextPPortRef(self, value: Optional[RefType]) -> "PTriggerInAtomicSwcTypeInstanceRef":
        """
        Sets the provided port (PPortPrototype) through which the referenced
        Trigger is reached. Only sets the value if it is not None, and returns
        self for method chaining.

        Args:
            value: The provided port reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.contextPPortRef = value
        return self

    def getTargetTriggerRef(self) -> Optional[RefType]:
        """
        Gets the Trigger that is referenced through the provided port.

        Returns:
            Optional[RefType]: The target trigger reference
        """
        return self.targetTriggerRef

    def setTargetTriggerRef(self, value: Optional[RefType]) -> "PTriggerInAtomicSwcTypeInstanceRef":
        """
        Sets the Trigger that is referenced through the provided port. Only
        sets the value if it is not None, and returns self for method chaining.

        Args:
            value: The target trigger reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.targetTriggerRef = value
        return self


class VariableInAtomicSwcInstanceRef(AtpInstanceRef, ABC):
    """
    Abstract base class for variable instance references within an atomic
    software component type.
    """

    # VariableInAtomicSwcInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is VariableInAtomicSwcInstanceRef:
            raise TypeError("VariableInAtomicSwcInstanceRef is an abstract class.")

        super().__init__()

        self.abstractTargetDataElementRef: RefType = None
        self.baseRef: RefType = None
        self.contextPortRef: RefType = None


class RVariableInAtomicSwcInstanceRef(VariableInAtomicSwcInstanceRef):
    """
    Instance reference to a variable in an atomic software component
    through an RPortPrototype.
    """

    # RVariableInAtomicSwcInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getContextRPortRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setContextRPortRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetDataElementRef      [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetDataElementRef      [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.contextRPortRef: RefType = None
        self.targetDataElementRef: RefType = None

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
    """
    Instance reference to a port group within a composition software
    component type.
    """

    # InnerPortGroupInCompositionInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] getContextRefs               [x] impl  [ ] docstring  [ ] test
    # [ ] addContextRefs               [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetRef                 [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetRef                 [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.baseRef: RefType = None
        self.contextRefs = []
        self.targetRef: RefType = None

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
    """
    Abstract base class for operation instance references within an atomic
    software component type.
    """

    # OperationInAtomicSwcInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setBaseRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] getContextPortRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setContextPortRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetOperationRef        [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetOperationRef        [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is OperationInAtomicSwcInstanceRef:
            raise TypeError("OperationInAtomicSwcInstanceRef is an abstract class.")

        super().__init__()

        self.baseRef: RefType = None
        self.contextPortRef: RefType = None
        self.targetOperationRef: RefType = None

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
    """
    Instance reference to a provided operation in an atomic software
    component through a PPortPrototype.
    """

    # POperationInAtomicSwcInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getContextPPortRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setContextPPortRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetProvidedOperationRef [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetProvidedOperationRef [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.contextPPortRef: RefType = None
        self.targetProvidedOperationRef: RefType = None

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
    """
    Instance reference to a required operation in an atomic software
    component through an RPortPrototype.
    """

    # ROperationInAtomicSwcInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getContextRPortRef           [x] impl  [ ] docstring  [ ] test
    # [ ] setContextRPortRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getTargetRequiredOperationRef [x] impl  [ ] docstring  [ ] test
    # [ ] setTargetRequiredOperationRef [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.contextRPortRef: RefType = None
        self.targetRequiredOperationRef: RefType = None

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
