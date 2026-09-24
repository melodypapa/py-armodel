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
        self.swDataDefProps: SwDataDefProps = None

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
    This class represents the ability to navigate into a data element inside of an VariableDataPrototype which is typed by an ImplementationDatatype. Note that it shall not be used if the target is the VariableDataPrototype itself (e.g. if its a primitive). Note that this class follows the pattern of an InstanceRef but is not implemented based on the abstract classes because the ImplementationDataType isn't either, especially because ImplementationDataType Element isn't derived from AtpPrototype.
    """

    # ArVariableInImplementationDataInstanceRef method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.37, p.322 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getContextDataPrototypeRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addContextDataPrototypeRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPortPrototypeRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPortPrototypeRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRootVariableDataPrototypeRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRootVariableDataPrototypeRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTargetDataPrototypeRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTargetDataPrototypeRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure.
        self.contextDataPrototypeRefs: List[RefType] = []

        # This is the port providing/receiving the root of the variable.
        self.portPrototypeRef: Optional[RefType] = None

        # This refers to the VariableDataPrototype typed by the ImplementationDatatype in which the target can be found.
        self.rootVariableDataPrototypeRef: Optional[RefType] = None

        # This reference points to the target ImplementationDataTypeElement.
        self.targetDataPrototypeRef: Optional[RefType] = None

    def getContextDataPrototypeRefs(self) -> List[RefType]:
        """This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure."""
        return self.contextDataPrototypeRefs

    def addContextDataPrototypeRef(self, value: Optional[RefType]) -> "ArVariableInImplementationDataInstanceRef":
        """This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. A None value is a no-op and does not append anything."""
        if value is not None:
            self.contextDataPrototypeRefs.append(value)
        return self

    def getPortPrototypeRef(self) -> Optional[RefType]:
        """This is the port providing/receiving the root of the variable."""
        return self.portPrototypeRef

    def setPortPrototypeRef(self, value: Optional[RefType]) -> "ArVariableInImplementationDataInstanceRef":
        """This is the port providing/receiving the root of the variable. A None value is a no-op and does not overwrite an existing portPrototypeRef."""
        if value is not None:
            self.portPrototypeRef = value
        return self

    def getRootVariableDataPrototypeRef(self) -> Optional[RefType]:
        """This refers to the VariableDataPrototype typed by the ImplementationDatatype in which the target can be found."""
        return self.rootVariableDataPrototypeRef

    def setRootVariableDataPrototypeRef(self, value: Optional[RefType]) -> "ArVariableInImplementationDataInstanceRef":
        """This refers to the VariableDataPrototype typed by the ImplementationDatatype in which the target can be found. A None value is a no-op and does not overwrite an existing rootVariableDataPrototypeRef."""
        if value is not None:
            self.rootVariableDataPrototypeRef = value
        return self

    def getTargetDataPrototypeRef(self) -> Optional[RefType]:
        """This reference points to the target ImplementationDataTypeElement."""
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value: Optional[RefType]) -> "ArVariableInImplementationDataInstanceRef":
        """This reference points to the target ImplementationDataTypeElement. A None value is a no-op and does not overwrite an existing targetDataPrototypeRef."""
        if value is not None:
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

        self.autosarParameterIRef: ParameterInAtomicSWCTypeInstanceRef = None
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
    This class represents a reference to a variable within AUTOSAR which can be one of the following use cases: localVariable: • localVariable which is used as whole (e.g. InterRunnableVariable, inputValue for curve) autosarVariable: • a variable provided via Port which is used as whole (e.g. dataAccesspoints) • an element inside of a composite local variable typed by ApplicationDatatype (e.g. inputValue for a curve) • an element inside of a composite variable provided via Port and typed by ApplicationDatatype (e.g. inputValue for a curve) autosarVariableInImplDatatype: • an element inside of a composite local variable typed by ImplementationDatatype (e.g. nvramData mapping) • an element inside of a composite variable provided via Port and typed by ImplementationDatatype (e.g. inputValue for a curve)
    """

    # AutosarVariableRef method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.33, p.316
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAutosarVariableIRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAutosarVariableIRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAutosarVariableInImplDatatype [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAutosarVariableInImplDatatype [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLocalVariableRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLocalVariableRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This references a variable which is provided by a port and/or which is part of a CompositeDataType. InstanceRef implemented by: VariableInAtomicSWCTypeInstanceRef
        self.autosarVariableIRef: Optional[VariableInAtomicSWCTypeInstanceRef] = None

        # This is used if the target variable is inside of variableDataPrototype typed by an ImplementationDataType.
        self.autosarVariableInImplDatatype: Optional[ArVariableInImplementationDataInstanceRef] = None

        # This reference is used if the variable is local to the current component. It would also be possible to use the instance refence here. Such an instance ref would not have a contextElement, since the current instance is the context. But the local instance is a special case which may provide further optimization. Therefore an explicit reference is provided for this case.
        self.localVariableRef: Optional[RefType] = None

    def getAutosarVariableIRef(self) -> Optional[VariableInAtomicSWCTypeInstanceRef]:
        """This references a variable which is provided by a port and/or which is part of a CompositeDataType. InstanceRef implemented by: VariableInAtomicSWCTypeInstanceRef"""
        return self.autosarVariableIRef

    def setAutosarVariableIRef(self, value: Optional[VariableInAtomicSWCTypeInstanceRef]) -> "AutosarVariableRef":
        """This references a variable which is provided by a port and/or which is part of a CompositeDataType. InstanceRef implemented by: VariableInAtomicSWCTypeInstanceRef. A None value is a no-op and does not overwrite an existing autosarVariableIRef."""
        if value is not None:
            self.autosarVariableIRef = value
        return self

    def getAutosarVariableInImplDatatype(self) -> Optional[ArVariableInImplementationDataInstanceRef]:
        """This is used if the target variable is inside of variableDataPrototype typed by an ImplementationDataType."""
        return self.autosarVariableInImplDatatype

    def setAutosarVariableInImplDatatype(self, value: Optional[ArVariableInImplementationDataInstanceRef]) -> "AutosarVariableRef":
        """This is used if the target variable is inside of variableDataPrototype typed by an ImplementationDataType. A None value is a no-op and does not overwrite an existing autosarVariableInImplDatatype."""
        if value is not None:
            self.autosarVariableInImplDatatype = value
        return self

    def getLocalVariableRef(self) -> Optional[RefType]:
        """This reference is used if the variable is local to the current component. It would also be possible to use the instance refence here. Such an instance ref would not have a contextElement, since the current instance is the context. But the local instance is a special case which may provide further optimization. Therefore an explicit reference is provided for this case."""
        return self.localVariableRef

    def setLocalVariableRef(self, value: Optional[RefType]) -> "AutosarVariableRef":
        """This reference is used if the variable is local to the current component. It would also be possible to use the instance refence here. Such an instance ref would not have a contextElement, since the current instance is the context. But the local instance is a special case which may provide further optimization. Therefore an explicit reference is provided for this case. A None value is a no-op and does not overwrite an existing localVariableRef."""
        if value is not None:
            self.localVariableRef = value
        return self
