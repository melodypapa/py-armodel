"""
This module contains classes for representing AUTOSAR data elements
in software component internal behavior templates.
"""

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import (
    ParameterInAtomicSWCTypeInstanceRef,
    VariableInAtomicSWCTypeInstanceRef,
)

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class ParameterAccess(AbstractAccessPoint, VariationPointCapable):
    """
    A ParameterAccess represents the access to a parameter data prototype
    within the internal behavior of an atomic software component.
    """

    # ParameterAccess method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAccessedParameter         [x] impl  [x] docstring  [ ] test
    # [ ] setAccessedParameter         [x] impl  [x] docstring  [ ] test
    # [ ] getSwDataDefProps            [x] impl  [x] docstring  [ ] test
    # [ ] setSwDataDefProps            [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.accessedParameter: "AutosarParameterRef" = None
        self.swDataDefProps: "SwDataDefProps" = None

    def getAccessedParameter(self):
        """
        Gets the accessed parameter.

        Returns:
            The accessed parameter reference
        """
        return self.accessedParameter

    def setAccessedParameter(self, value):
        """
        Sets the accessed parameter.

        Args:
            value: The accessed parameter reference to set

        Returns:
            self for method chaining
        """
        self.accessedParameter = value
        return self

    def getSwDataDefProps(self):
        """
        Gets the software data definition properties.

        Returns:
            SwDataDefProps: The software data definition properties
        """
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        """
        Sets the software data definition properties.

        Args:
            value: The software data definition properties to set

        Returns:
            self for method chaining
        """
        self.swDataDefProps = value
        return self


class VariableAccess(AbstractAccessPoint, VariationPointCapable):
    """
    The presence of a VariableAccess implies that a RunnableEntity needs access to a VariableDataPrototype. The kind of access is specified by the role in which the class is used.
    """

    # VariableAccess method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.33, p.567
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAccessedVariableRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAccessedVariableRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getScope                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setScope                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name):
        super().__init__(parent, short_name)

        # This denotes the accessed variable.
        self.accessedVariableRef: Optional["AutosarVariableRef"] = None

        # This attribute allows for constraining the scope of the corresponding communication. For example, it possible to express whether the communication is intended to cross the boundary of an ECU or whether it is intended not to cross the boundary of a single partition.
        self.scope: Optional[ARLiteral] = None

    def getAccessedVariableRef(self) -> Optional["AutosarVariableRef"]:
        """
        Gets the accessed variable.

        This denotes the accessed variable.

        Returns:
            AutosarVariableRef, or None if not set
        """
        return self.accessedVariableRef

    def setAccessedVariableRef(self, value: Optional["AutosarVariableRef"]) -> "VariableAccess":
        """
        Sets the accessed variable.
        A None value is a no-op and does not overwrite an existing accessed variable.

        This denotes the accessed variable.

        Args:
            value: The AutosarVariableRef to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.accessedVariableRef = value
        return self

    def getScope(self) -> Optional[ARLiteral]:
        """
        Gets the scope of the corresponding communication.

        This attribute allows for constraining the scope of the corresponding communication. For example, it possible to express whether the communication is intended to cross the boundary of an ECU or whether it is intended not to cross the boundary of a single partition.

        Returns:
            ARLiteral, or None if not set
        """
        return self.scope

    def setScope(self, value: Optional[ARLiteral]) -> "VariableAccess":
        """
        Sets the scope of the corresponding communication.
        A None value is a no-op and does not overwrite an existing scope.

        This attribute allows for constraining the scope of the corresponding communication. For example, it possible to express whether the communication is intended to cross the boundary of an ECU or whether it is intended not to cross the boundary of a single partition.

        Args:
            value: The ARLiteral to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.scope = value
        return self


class ArVariableInImplementationDataInstanceRef(ARObject):
    """
    A reference to an AUTOSAR variable in the context of an implementation
    data type instance.
    """

    # ArVariableInImplementationDataInstanceRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getContextDataPrototypeRefs  [x] impl  [x] docstring  [ ] test
    # [ ] setContextDataPrototypeRefs  [x] impl  [x] docstring  [ ] test
    # [ ] getPortPrototypeRef          [x] impl  [x] docstring  [ ] test
    # [ ] setPortPrototypeRef          [x] impl  [x] docstring  [ ] test
    # [ ] getRootVariableDataPrototypeRef [x] impl  [x] docstring  [ ] test
    # [ ] setRootVariableDataPrototypeRef [x] impl  [x] docstring  [ ] test
    # [ ] getTargetDataPrototypeRef    [x] impl  [x] docstring  [ ] test
    # [ ] setTargetDataPrototypeRef    [x] impl  [x] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.contextDataPrototypeRefs: List[RefType] = []
        self.portPrototypeRef: RefType = None
        self.rootVariableDataPrototypeRef: RefType = None
        self.targetDataPrototypeRef: RefType = None

    def getContextDataPrototypeRefs(self):
        """
        Gets the list of context data prototype references.

        Returns:
            List[RefType]: The list of context data prototype references
        """
        return self.contextDataPrototypeRefs

    def setContextDataPrototypeRefs(self, value):
        """
        Sets the list of context data prototype references.

        Args:
            value: The list of context data prototype references to set

        Returns:
            self for method chaining
        """
        self.contextDataPrototypeRefs = value
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


class AutosarParameterRef(ARObject):
    """
    A reference to an AUTOSAR parameter.
    """

    # AutosarParameterRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAutosarParameterIRef      [x] impl  [x] docstring  [ ] test
    # [ ] setAutosarParameterIRef      [x] impl  [x] docstring  [ ] test
    # [ ] getLocalParameterRef         [x] impl  [x] docstring  [ ] test
    # [ ] setLocalParameterRef         [x] impl  [x] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.autosarParameterIRef: "ParameterInAtomicSWCTypeInstanceRef" = None
        self.localParameterRef: RefType = None

    def getAutosarParameterIRef(self):
        """
        Gets the AUTOSAR parameter instance reference.

        Returns:
            ParameterInAtomicSWCTypeInstanceRef: The AUTOSAR parameter instance
                reference
        """
        return self.autosarParameterIRef

    def setAutosarParameterIRef(self, value):
        """
        Sets the AUTOSAR parameter instance reference.

        Args:
            value: The AUTOSAR parameter instance reference to set

        Returns:
            self for method chaining
        """
        self.autosarParameterIRef = value
        return self

    def getLocalParameterRef(self):
        """
        Gets the local parameter reference.

        Returns:
            RefType: The local parameter reference
        """
        return self.localParameterRef

    def setLocalParameterRef(self, value):
        """
        Sets the local parameter reference.

        Args:
            value: The local parameter reference to set

        Returns:
            self for method chaining
        """
        self.localParameterRef = value
        return self


class AutosarVariableRef(ARObject):
    """
    A reference to a variable used in the context of AUTOSAR software component
    internal behavior.
    """

    # AutosarVariableRef method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAutosarVariableIRef       [x] impl  [x] docstring  [ ] test
    # [ ] setAutosarVariableIRef       [x] impl  [x] docstring  [ ] test
    # [ ] getAutosarVariableInImplDatatype [x] impl  [x] docstring  [ ] test
    # [ ] setAutosarVariableInImplDatatype [x] impl  [ ] docstring  [ ] test
    # [ ] getLocalVariableRef          [x] impl  [x] docstring  [ ] test
    # [ ] setLocalVariableRef          [x] impl  [x] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.autosarVariableIRef: VariableInAtomicSWCTypeInstanceRef = None
        self.autosarVariableInImplDatatype: ArVariableInImplementationDataInstanceRef = None
        self.localVariableRef: "VariableInAtomicSWCTypeInstanceRef" = None

    def getAutosarVariableIRef(self) -> VariableInAtomicSWCTypeInstanceRef:
        """
        Gets the AUTOSAR variable instance reference.

        Returns:
            VariableInAtomicSWCTypeInstanceRef: The AUTOSAR variable instance reference
        """
        return self.autosarVariableIRef

    def setAutosarVariableIRef(self, value):
        """
        Sets the AUTOSAR variable instance reference.

        Args:
            value: The AUTOSAR variable instance reference to set

        Returns:
            self for method chaining
        """
        self.autosarVariableIRef = value
        return self

    def getAutosarVariableInImplDatatype(self) -> ArVariableInImplementationDataInstanceRef:
        """Get the autosarVariableInImplDatatype attribute."""
        return self.autosarVariableInImplDatatype

    def setAutosarVariableInImplDatatype(self, value):
        self.autosarVariableInImplDatatype = value
        return self

    def getLocalVariableRef(self):
        """
        Gets the local variable reference.

        Returns:
            The local variable reference
        """
        return self.localVariableRef

    def setLocalVariableRef(self, value):
        """
        Sets the local variable reference.

        Args:
            value: The local variable reference to set

        Returns:
            self for method chaining
        """
        self.localVariableRef = value
        return self
