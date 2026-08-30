"""
This module contains classes for representing AUTOSAR instance reference usages
in software component internal behavior templates.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef


class VariableInAtomicSWCTypeInstanceRef(AtpInstanceRef):
    """
    A reference to a variable data prototype in the context of an atomic
    software component type instance.
    """

    # VariableInAtomicSWCTypeInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBaseRef                   [x] impl  [x] docstring  [ ] test
    # [ ] setBaseRef                   [x] impl  [x] docstring  [ ] test
    # [ ] getContextDataPrototypeRefs  [x] impl  [x] docstring  [ ] test
    # [ ] addContextDataPrototypeRef   [x] impl  [x] docstring  [ ] test
    # [ ] getPortPrototypeRef          [x] impl  [x] docstring  [ ] test
    # [ ] setPortPrototypeRef          [x] impl  [x] docstring  [ ] test
    # [ ] getRootVariableDataPrototypeRef [x] impl  [x] docstring  [ ] test
    # [ ] setRootVariableDataPrototypeRef [x] impl  [x] docstring  [ ] test
    # [ ] getTargetDataPrototypeRef    [x] impl  [x] docstring  [ ] test
    # [ ] setTargetDataPrototypeRef    [x] impl  [x] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.baseRef: RefType = None
        self.contextDataPrototypeRefs: List[RefType] = []
        self.portPrototypeRef: RefType = None
        self.rootVariableDataPrototypeRef: RefType = None
        self.targetDataPrototypeRef: RefType = None

    def getBaseRef(self):
        """
        Gets the base reference.

        Returns:
            RefType: The base reference
        """
        return self.baseRef

    def setBaseRef(self, value):
        """
        Sets the base reference.

        Args:
            value: The base reference to set

        Returns:
            self for method chaining
        """
        self.baseRef = value
        return self

    def getContextDataPrototypeRefs(self):
        """
        Gets the list of context data prototype references.

        Returns:
            List[RefType]: The list of context data prototype references
        """
        return self.contextDataPrototypeRefs

    def addContextDataPrototypeRef(self, value):
        """
        Adds a context data prototype reference.

        Args:
            value: The context data prototype reference to add

        Returns:
            self for method chaining
        """
        self.contextDataPrototypeRefs.append(value)
        return self

    def getPortPrototypeRef(self):
        """
        Gets the port prototype reference.

        Returns:
            RefType: The port prototype reference
        """
        return self.portPrototypeRef

    def setPortPrototypeRef(self, value):
        """
        Sets the port prototype reference.

        Args:
            value: The port prototype reference to set

        Returns:
            self for method chaining
        """
        self.portPrototypeRef = value
        return self

    def getRootVariableDataPrototypeRef(self):
        """
        Gets the root variable data prototype reference.

        Returns:
            RefType: The root variable data prototype reference
        """
        return self.rootVariableDataPrototypeRef

    def setRootVariableDataPrototypeRef(self, value):
        """
        Sets the root variable data prototype reference.

        Args:
            value: The root variable data prototype reference to set

        Returns:
            self for method chaining
        """
        self.rootVariableDataPrototypeRef = value
        return self

    def getTargetDataPrototypeRef(self):
        """
        Gets the target data prototype reference.

        Returns:
            RefType: The target data prototype reference
        """
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value):
        """
        Sets the target data prototype reference.

        Args:
            value: The target data prototype reference to set

        Returns:
            self for method chaining
        """
        self.targetDataPrototypeRef = value
        return self


class ParameterInAtomicSWCTypeInstanceRef(AtpInstanceRef):
    """
    This class implements an instance reference which can be applied for variables as well as for parameters.
    """

    # ParameterInAtomicSWCTypeInstanceRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.36, p.319
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setBaseRef                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBaseRef                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addContextDataPrototypeRef  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getContextDataPrototypeRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPortPrototypeRef         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getPortPrototypeRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRootParameterDataPrototypeRef [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getRootParameterDataPrototypeRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTargetDataPrototypeRef   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getTargetDataPrototypeRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # Stereotypes: atpDerived
        self.baseRef: Optional[RefType] = None

        # This ist the context in a compositeDataType.
        self.contextDataPrototypeRefs: List[RefType] = []

        # This is the port providing the variable or the entry point to the variable structure.
        self.portPrototypeRef: Optional[RefType] = None

        # This represents the entry point for references into a CompositeDataType.
        self.rootParameterDataPrototypeRef: Optional[RefType] = None

        # This is the target parameter element. Note that this must be nested in ParameterDataPrototype. The target must be one of ParameterDataPrototype, ApplicationCompositeElementDataPrototype.
        self.targetDataPrototypeRef: Optional[RefType] = None

    def setBaseRef(self, value: Optional[RefType]) -> "ParameterInAtomicSWCTypeInstanceRef":
        """
        Stereotypes: atpDerived

        A None value is a no-op and does not overwrite an existing baseRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.baseRef = value
        return self

    def getBaseRef(self) -> Optional[RefType]:
        """
        Stereotypes: atpDerived

        Returns:
            The base reference, or None if not set
        """
        return self.baseRef

    def addContextDataPrototypeRef(self, value: Optional[RefType]) -> "ParameterInAtomicSWCTypeInstanceRef":
        """
        This ist the context in a compositeDataType.

        A None value is a no-op and does not add a contextDataPrototypeRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.contextDataPrototypeRefs.append(value)
        return self

    def getContextDataPrototypeRefs(self) -> List[RefType]:
        """
        This ist the context in a compositeDataType.

        Returns:
            The ordered list of context data prototype references
        """
        return self.contextDataPrototypeRefs

    def setPortPrototypeRef(self, value: Optional[RefType]) -> "ParameterInAtomicSWCTypeInstanceRef":
        """
        This is the port providing the variable or the entry point to the variable structure.

        A None value is a no-op and does not overwrite an existing portPrototypeRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.portPrototypeRef = value
        return self

    def getPortPrototypeRef(self) -> Optional[RefType]:
        """
        This is the port providing the variable or the entry point to the variable structure.

        Returns:
            The port prototype reference, or None if not set
        """
        return self.portPrototypeRef

    def setRootParameterDataPrototypeRef(self, value: Optional[RefType]) -> "ParameterInAtomicSWCTypeInstanceRef":
        """
        This represents the entry point for references into a CompositeDataType.

        A None value is a no-op and does not overwrite an existing rootParameterDataPrototypeRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rootParameterDataPrototypeRef = value
        return self

    def getRootParameterDataPrototypeRef(self) -> Optional[RefType]:
        """
        This represents the entry point for references into a CompositeDataType.

        Returns:
            The root parameter data prototype reference, or None if not set
        """
        return self.rootParameterDataPrototypeRef

    def setTargetDataPrototypeRef(self, value: Optional[RefType]) -> "ParameterInAtomicSWCTypeInstanceRef":
        """
        This is the target parameter element. Note that this must be nested in ParameterDataPrototype. The target must be one of ParameterDataPrototype, ApplicationCompositeElementDataPrototype.

        A None value is a no-op and does not overwrite an existing targetDataPrototypeRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.targetDataPrototypeRef = value
        return self

    def getTargetDataPrototypeRef(self) -> Optional[RefType]:
        """
        This is the target parameter element. Note that this must be nested in ParameterDataPrototype. The target must be one of ParameterDataPrototype, ApplicationCompositeElementDataPrototype.

        Returns:
            The target data prototype reference, or None if not set
        """
        return self.targetDataPrototypeRef
