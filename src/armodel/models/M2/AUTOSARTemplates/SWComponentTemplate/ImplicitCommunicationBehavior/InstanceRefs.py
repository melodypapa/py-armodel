"""
This module contains classes for representing AUTOSAR instance references
in the SWComponentTemplate.ImplicitCommunicationBehavior module. These
classes are used for referencing nested DataPrototypeGroups,
RunnableEntityGroups, RunnableEntitys and VariableDataPrototypes in the
context of a CompositionSwComponentType.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class InnerDataPrototypeGroupInCompositionInstanceRef(AtpInstanceRef):
    """
    This meta-class represents the ability to define an InstanceRef to a
    nested DataPrototypeGroup
    """

    # InnerDataPrototypeGroupInCompositionInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.19, p.955
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBaseRef                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setBaseRef                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getContextSwComponentPrototypeRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextSwComponentPrototypeRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetDataPrototypeGroupRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetDataPrototypeGroupRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        """
        Initializes the InnerDataPrototypeGroupInCompositionInstanceRef with
        default values.
        """
        super().__init__()

        # This represents the base of the instanceRef.
        self.baseRef: Optional[RefType] = None

        # This represents the nested structure of SwComponent Prototypes.
        self.contextSwComponentPrototypeRefs: List[RefType] = []

        # This represents the target of the InstanceRef.
        self.targetDataPrototypeGroupRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        This represents the base of the instanceRef.

        Returns:
            Optional[RefType]: The base reference, or None if not set
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "InnerDataPrototypeGroupInCompositionInstanceRef":
        """
        This represents the base of the instanceRef. Only sets the value if it
        is not None, and returns self for method chaining.

        Args:
            value: The base reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextSwComponentPrototypeRefs(self) -> List[RefType]:
        """
        This represents the nested structure of SwComponent Prototypes.

        Returns:
            List of RefType instances representing the context SwComponentPrototypes
        """
        return self.contextSwComponentPrototypeRefs

    def addContextSwComponentPrototypeRef(self, value: RefType) -> "InnerDataPrototypeGroupInCompositionInstanceRef":
        """
        This represents the nested structure of SwComponent Prototypes. Returns
        self for method chaining.

        Args:
            value: The context SwComponentPrototype reference to add

        Returns:
            self for method chaining
        """
        self.contextSwComponentPrototypeRefs.append(value)
        return self

    def getTargetDataPrototypeGroupRef(self) -> Optional[RefType]:
        """
        This represents the target of the InstanceRef.

        Returns:
            Optional[RefType]: The target DataPrototypeGroup reference, or None if not set
        """
        return self.targetDataPrototypeGroupRef

    def setTargetDataPrototypeGroupRef(self, value: Optional[RefType]) -> "InnerDataPrototypeGroupInCompositionInstanceRef":
        """
        This represents the target of the InstanceRef. Only sets the value if it
        is not None, and returns self for method chaining.

        Args:
            value: The target DataPrototypeGroup reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.targetDataPrototypeGroupRef = value
        return self


class InnerRunnableEntityGroupInCompositionInstanceRef(AtpInstanceRef):
    """
    This meta-class represents the ability to define an InstanceRef to a
    nested RunnableEntityGroup.
    """

    # InnerRunnableEntityGroupInCompositionInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.20, p.956
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBaseRef                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setBaseRef                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getContextSwComponentPrototypeRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextSwComponentPrototypeRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetRunnableEntityGroupRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetRunnableEntityGroupRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        """
        Initializes the InnerRunnableEntityGroupInCompositionInstanceRef with
        default values.
        """
        super().__init__()

        # This represents the base of the InstanceRef.
        self.baseRef: Optional[RefType] = None

        # This represents the nested structure of SwComponent Prototypes.
        self.contextSwComponentPrototypeRefs: List[RefType] = []

        # This represents the target association of the InstanceRef.
        self.targetRunnableEntityGroupRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        This represents the base of the InstanceRef.

        Returns:
            Optional[RefType]: The base reference, or None if not set
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "InnerRunnableEntityGroupInCompositionInstanceRef":
        """
        This represents the base of the InstanceRef. Only sets the value if it
        is not None, and returns self for method chaining.

        Args:
            value: The base reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextSwComponentPrototypeRefs(self) -> List[RefType]:
        """
        This represents the nested structure of SwComponent Prototypes.

        Returns:
            List of RefType instances representing the context SwComponentPrototypes
        """
        return self.contextSwComponentPrototypeRefs

    def addContextSwComponentPrototypeRef(self, value: RefType) -> "InnerRunnableEntityGroupInCompositionInstanceRef":
        """
        This represents the nested structure of SwComponent Prototypes. Returns
        self for method chaining.

        Args:
            value: The context SwComponentPrototype reference to add

        Returns:
            self for method chaining
        """
        self.contextSwComponentPrototypeRefs.append(value)
        return self

    def getTargetRunnableEntityGroupRef(self) -> Optional[RefType]:
        """
        This represents the target association of the InstanceRef.

        Returns:
            Optional[RefType]: The target RunnableEntityGroup reference, or None if not set
        """
        return self.targetRunnableEntityGroupRef

    def setTargetRunnableEntityGroupRef(self, value: Optional[RefType]) -> "InnerRunnableEntityGroupInCompositionInstanceRef":
        """
        This represents the target association of the InstanceRef. Only sets the
        value if it is not None, and returns self for method chaining.

        Args:
            value: The target RunnableEntityGroup reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.targetRunnableEntityGroupRef = value
        return self


class RunnableEntityInCompositionInstanceRef(AtpInstanceRef):
    """
    This meta-class represents the ability to define an InstanceRef to a
    RunnableEntity in the context of a CompositionSwComponentType.
    """

    # RunnableEntityInCompositionInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.21, p.956
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBaseRef                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setBaseRef                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getContextSwComponentPrototypeRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextSwComponentPrototypeRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetRunnableEntityRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetRunnableEntityRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        """
        Initializes the RunnableEntityInCompositionInstanceRef with default
        values.
        """
        super().__init__()

        # This represents the base of the InstanceRef.
        self.baseRef: Optional[RefType] = None

        # This represents the nested structure of SwComponent Prototypes.
        self.contextSwComponentPrototypeRefs: List[RefType] = []

        # This represents the target RunnableEntity.
        self.targetRunnableEntityRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        This represents the base of the InstanceRef.

        Returns:
            Optional[RefType]: The base reference, or None if not set
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "RunnableEntityInCompositionInstanceRef":
        """
        This represents the base of the InstanceRef. Only sets the value if it
        is not None, and returns self for method chaining.

        Args:
            value: The base reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextSwComponentPrototypeRefs(self) -> List[RefType]:
        """
        This represents the nested structure of SwComponent Prototypes.

        Returns:
            List of RefType instances representing the context SwComponentPrototypes
        """
        return self.contextSwComponentPrototypeRefs

    def addContextSwComponentPrototypeRef(self, value: RefType) -> "RunnableEntityInCompositionInstanceRef":
        """
        This represents the nested structure of SwComponent Prototypes. Returns
        self for method chaining.

        Args:
            value: The context SwComponentPrototype reference to add

        Returns:
            self for method chaining
        """
        self.contextSwComponentPrototypeRefs.append(value)
        return self

    def getTargetRunnableEntityRef(self) -> Optional[RefType]:
        """
        This represents the target RunnableEntity.

        Returns:
            Optional[RefType]: The target RunnableEntity reference, or None if not set
        """
        return self.targetRunnableEntityRef

    def setTargetRunnableEntityRef(self, value: Optional[RefType]) -> "RunnableEntityInCompositionInstanceRef":
        """
        This represents the target RunnableEntity. Only sets the value if it is
        not None, and returns self for method chaining.

        Args:
            value: The target RunnableEntity reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.targetRunnableEntityRef = value
        return self


class VariableDataPrototypeInCompositionInstanceRef(AtpInstanceRef):
    """
    This meta-class represents the ability to define an InstanceRef to a
    VariableDataPrototype in the context of a CompositionSwComponentType.
    """

    # VariableDataPrototypeInCompositionInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.22, p.959
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBaseRef                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setBaseRef                           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getContextPortPrototypeRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setContextPortPrototypeRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getContextSwComponentPrototypeRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addContextSwComponentPrototypeRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTargetVariableDataPrototypeRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetVariableDataPrototypeRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        """
        Initializes the VariableDataPrototypeInCompositionInstanceRef with
        default values.
        """
        super().__init__()

        # This represents the base of the InstanceRef.
        self.baseRef: Optional[RefType] = None

        # This represents a reference to a context PortPrototype.
        self.contextPortPrototypeRef: Optional[RefType] = None

        # This represents the nested structure of Sw Component Prototypes.
        self.contextSwComponentPrototypeRefs: List[RefType] = []

        # This represents the target VariableDataPrototype.
        self.targetVariableDataPrototypeRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """
        This represents the base of the InstanceRef.

        Returns:
            Optional[RefType]: The base reference, or None if not set
        """
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "VariableDataPrototypeInCompositionInstanceRef":
        """
        This represents the base of the InstanceRef. Only sets the value if it
        is not None, and returns self for method chaining.

        Args:
            value: The base reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.baseRef = value
        return self

    def getContextPortPrototypeRef(self) -> Optional[RefType]:
        """
        This represents a reference to a context PortPrototype.

        Returns:
            Optional[RefType]: The context PortPrototype reference, or None if not set
        """
        return self.contextPortPrototypeRef

    def setContextPortPrototypeRef(self, value: Optional[RefType]) -> "VariableDataPrototypeInCompositionInstanceRef":
        """
        This represents a reference to a context PortPrototype. Only sets the
        value if it is not None, and returns self for method chaining.

        Args:
            value: The context PortPrototype reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.contextPortPrototypeRef = value
        return self

    def getContextSwComponentPrototypeRefs(self) -> List[RefType]:
        """
        This represents the nested structure of Sw Component Prototypes.

        Returns:
            List of RefType instances representing the context SwComponentPrototypes
        """
        return self.contextSwComponentPrototypeRefs

    def addContextSwComponentPrototypeRef(self, value: RefType) -> "VariableDataPrototypeInCompositionInstanceRef":
        """
        This represents the nested structure of Sw Component Prototypes.
        Returns self for method chaining.

        Args:
            value: The context SwComponentPrototype reference to add

        Returns:
            self for method chaining
        """
        self.contextSwComponentPrototypeRefs.append(value)
        return self

    def getTargetVariableDataPrototypeRef(self) -> Optional[RefType]:
        """
        This represents the target VariableDataPrototype.

        Returns:
            Optional[RefType]: The target VariableDataPrototype reference, or None if not set
        """
        return self.targetVariableDataPrototypeRef

    def setTargetVariableDataPrototypeRef(self, value: Optional[RefType]) -> "VariableDataPrototypeInCompositionInstanceRef":
        """
        This represents the target VariableDataPrototype. Only sets the value
        if it is not None, and returns self for method chaining.

        Args:
            value: The target VariableDataPrototype reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.targetVariableDataPrototypeRef = value
        return self
