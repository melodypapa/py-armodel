"""
This module contains classes for representing AUTOSAR data elements
in software component internal behavior templates.
"""

from __future__ import annotations

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
    The presence of a ParameterAccess implies that a RunnableEntity needs access to a ParameterDataPrototype.
    """

    # ParameterAccess method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.40, p.586
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAccessedParameter  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAccessedParameter  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwDataDefProps     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwDataDefProps     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the accessed calibration parameter.
        self.accessedParameter: Optional[AutosarParameterRef] = None

        # This allows denote instance and access specific properties, mainly input values and common axis. Stereotypes: atpSplitable Tags: atp.Splitkey=swDataDefProps
        self.swDataDefProps: Optional[SwDataDefProps] = None

    def getAccessedParameter(self) -> Optional[AutosarParameterRef]:
        """Reference to the accessed calibration parameter."""
        return self.accessedParameter

    def setAccessedParameter(self, value: Optional[AutosarParameterRef]) -> ParameterAccess:
        """Reference to the accessed calibration parameter. A None value is a no-op and does not overwrite an existing accessedParameter."""
        if value is not None:
            self.accessedParameter = value
        return self

    def getSwDataDefProps(self) -> Optional[SwDataDefProps]:
        """This allows denote instance and access specific properties, mainly input values and common axis. Stereotypes: atpSplitable Tags: atp.Splitkey=swDataDefProps"""
        return self.swDataDefProps

    def setSwDataDefProps(self, value: Optional[SwDataDefProps]) -> ParameterAccess:
        """This allows denote instance and access specific properties, mainly input values and common axis. Stereotypes: atpSplitable Tags: atp.Splitkey=swDataDefProps A None value is a no-op and does not overwrite an existing swDataDefProps."""
        if value is not None:
            self.swDataDefProps = value
        return self


class VariableAccess(AbstractAccessPoint, VariationPointCapable):
    """
    The presence of a VariableAccess implies that a RunnableEntity needs access to a VariableDataPrototype. The kind of access is specified by the role in which the class is used.
    """

    # VariableAccess method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.33, p.567
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAccessedVariable   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAccessedVariable   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getScope              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setScope              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This denotes the accessed variable.
        self.accessedVariable: Optional[AutosarVariableRef] = None

        # This attribute allows for constraining the scope of the corresponding communication. For example, it possible to express whether the communication is intended to cross the boundary of an ECU or whether it is intended not to cross the boundary of a single partition.
        self.scope: Optional[ARLiteral] = None

    def getAccessedVariable(self) -> Optional[AutosarVariableRef]:
        """This denotes the accessed variable."""
        return self.accessedVariable

    def setAccessedVariable(self, value: Optional[AutosarVariableRef]) -> VariableAccess:
        """This denotes the accessed variable. A None value is a no-op and does not overwrite an existing accessedVariable."""
        if value is not None:
            self.accessedVariable = value
        return self

    def getScope(self) -> Optional[ARLiteral]:
        """This attribute allows for constraining the scope of the corresponding communication. For example, it possible to express whether the communication is intended to cross the boundary of an ECU or whether it is intended not to cross the boundary of a single partition."""
        return self.scope

    def setScope(self, value: Optional[ARLiteral]) -> VariableAccess:
        """This attribute allows for constraining the scope of the corresponding communication. For example, it possible to express whether the communication is intended to cross the boundary of an ECU or whether it is intended not to cross the boundary of a single partition. A None value is a no-op and does not overwrite an existing scope."""
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

    def addContextDataPrototypeRef(self, value: Optional[RefType]) -> ArVariableInImplementationDataInstanceRef:
        """This is a context in case there are subelements with explicit types. The reference has to be ordered to properly reflect the nested structure. A None value is a no-op and does not append anything."""
        if value is not None:
            self.contextDataPrototypeRefs.append(value)
        return self

    def getPortPrototypeRef(self) -> Optional[RefType]:
        """This is the port providing/receiving the root of the variable."""
        return self.portPrototypeRef

    def setPortPrototypeRef(self, value: Optional[RefType]) -> ArVariableInImplementationDataInstanceRef:
        """This is the port providing/receiving the root of the variable. A None value is a no-op and does not overwrite an existing portPrototypeRef."""
        if value is not None:
            self.portPrototypeRef = value
        return self

    def getRootVariableDataPrototypeRef(self) -> Optional[RefType]:
        """This refers to the VariableDataPrototype typed by the ImplementationDatatype in which the target can be found."""
        return self.rootVariableDataPrototypeRef

    def setRootVariableDataPrototypeRef(self, value: Optional[RefType]) -> ArVariableInImplementationDataInstanceRef:
        """This refers to the VariableDataPrototype typed by the ImplementationDatatype in which the target can be found. A None value is a no-op and does not overwrite an existing rootVariableDataPrototypeRef."""
        if value is not None:
            self.rootVariableDataPrototypeRef = value
        return self

    def getTargetDataPrototypeRef(self) -> Optional[RefType]:
        """This reference points to the target ImplementationDataTypeElement."""
        return self.targetDataPrototypeRef

    def setTargetDataPrototypeRef(self, value: Optional[RefType]) -> ArVariableInImplementationDataInstanceRef:
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
        self.localVariableRef: VariableInAtomicSWCTypeInstanceRef = None

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
