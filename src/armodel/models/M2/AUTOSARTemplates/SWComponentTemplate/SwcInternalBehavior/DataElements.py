"""
This module contains classes for representing AUTOSAR data elements
in software component internal behavior templates.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import AutosarVariableRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import AutosarParameterRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from typing import Optional


class ParameterAccess(AbstractAccessPoint):
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


class VariableAccess(AbstractAccessPoint):
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
