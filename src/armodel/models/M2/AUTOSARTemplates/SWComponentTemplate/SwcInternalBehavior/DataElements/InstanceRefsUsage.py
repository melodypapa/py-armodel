"""
This module contains classes for representing AUTOSAR instance reference usages
in software component internal behavior templates.
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef


class VariableInAtomicSWCTypeInstanceRef(AtpInstanceRef):
    """"""

    # VariableInAtomicSWCTypeInstanceRef method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.18, p.953 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBaseRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBaseRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getContextDataPrototypeRefs  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addContextDataPrototypeRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPortPrototypeRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPortPrototypeRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRootVariableDataPrototypeRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRootVariableDataPrototypeRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetDataPrototypeRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetDataPrototypeRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Stereotypes: atpDerived Tags: xml.sequenceOffset=10
        self.baseRef: Optional[RefType] = None

        # This is the context in a compositeDataType. Tags: xml.sequenceOffset=40
        self.contextDataPrototypeRefs: List[RefType] = []

        # This is the port providing the parameter or the entry point to the parameter structure. Tags: xml.sequenceOffset=20
        self.portPrototypeRef: Optional[RefType] = None

        # Tags: xml.sequenceOffset=30
        self.rootVariableDataPrototypeRef: Optional[RefType] = None

        # This is the target of the instance ref. Note that it shall be one of ApplicationCompositeElementDataPrototype of VariableDataPrototype. Tags: xml.sequenceOffset=50
        self.targetDataPrototypeRef: Optional[RefType] = None

    def getBaseRef(self) -> Optional[RefType]:
        """Stereotypes: atpDerived Tags: xml.sequenceOffset=10"""
        return self.baseRef

    def setBaseRef(self, value: Optional[RefType]) -> "VariableInAtomicSWCTypeInstanceRef":
        """Stereotypes: atpDerived Tags: xml.sequenceOffset=10. A None value is a no-op."""
        if value is not None:
            self.baseRef = value
        return self

    def getContextDataPrototypeRefs(self) -> List[RefType]:
        """This is the context in a compositeDataType. Tags: xml.sequenceOffset=40"""
        return self.contextDataPrototypeRefs

    def addContextDataPrototypeRef(self, value: Optional[RefType]) -> "VariableInAtomicSWCTypeInstanceRef":
        """This is the context in a compositeDataType. Tags: xml.sequenceOffset=40. A None value is a no-op."""
        if value is not None:
            self.contextDataPrototypeRefs.append(value)
        return self

    def getPortPrototypeRef(self) -> Optional[RefType]:
        """This is the port providing the parameter or the entry point to the parameter structure. Tags: xml.sequenceOffset=20"""
        return self.portPrototypeRef

    def setPortPrototypeRef(self, value: Optional[RefType]) -> "VariableInAtomicSWCTypeInstanceRef":
        """This is the port providing the parameter or the entry point to the parameter structure. Tags: xml.sequenceOffset=20. A None value is a no-op."""
        if value is not None:
            self.portPrototypeRef = value
        return self

    def getRootVariableDataPrototypeRef(self) -> Optional[RefType]:
        """Tags: xml.sequenceOffset=30"""
        return self.rootVariableDataPrototypeRef

    def setRootVariableDataPrototypeRef(self, value: Optional[RefType]) -> "VariableInAtomicSWCTypeInstanceRef":
        """Tags: xml.sequenceOffset=30. A None value is a no-op."""
        if value is not None:
            self.rootVariableDataPrototypeRef = value
        return self

    def getTargetDataPrototypeRef(self) -> Optional[RefType]:
        """
        This is the target of the instance ref. Note that it shall be one of ApplicationCompositeElementDataPrototype of VariableDataPrototype. Tags: xml.sequenceOffset=50
        """
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value: Optional[RefType]) -> "VariableInAtomicSWCTypeInstanceRef":
        """
        This is the target of the instance ref. Note that it shall be one of ApplicationCompositeElementDataPrototype of VariableDataPrototype. Tags: xml.sequenceOffset=50
        A None value is a no-op and does not overwrite an existing targetDataPrototypeRef.
        """
        if value is not None:
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
