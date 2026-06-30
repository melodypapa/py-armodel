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


class ParameterAccess(AbstractAccessPoint):
    """
    A ParameterAccess represents the access to a parameter data prototype
    within the internal behavior of an atomic software component.
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.accessedParameter: 'AutosarParameterRef' = None
        self.swDataDefProps: 'SwDataDefProps' = None

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
    A VariableAccess represents the access to a variable data prototype
    within the internal behavior of an atomic software component.
    """

    def __init__(self, parent: ARObject, short_name):
        super().__init__(parent, short_name)

        self.accessedVariableRef: 'AutosarVariableRef' = None
        self.scope: ARLiteral = None

    def getAccessedVariableRef(self) -> 'AutosarVariableRef':
        """
        Gets the accessed variable reference.

        Returns:
            AutosarVariableRef: The accessed variable reference
        """
        return self.accessedVariableRef

    def setAccessedVariableRef(self, value: 'AutosarVariableRef'):
        """
        Sets the accessed variable reference.

        Args:
            value: The accessed variable reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.accessedVariableRef = value
        return self

    def getScope(self):
        """
        Gets the scope of the variable access.

        Returns:
            The scope
        """
        return self.scope

    def setScope(self, value):
        """
        Sets the scope of the variable access.

        Args:
            value: The scope to set

        Returns:
            self for method chaining
        """
        self.scope = value
        return self
