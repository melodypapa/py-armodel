"""
This module contains classes for representing AUTOSAR port API options
in software component internal behavior templates.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType, TRefType
from typing import List, Optional


class PortDefinedArgumentValue(ARObject):
    """
    A PortDefinedArgumentValue is passed to a RunnableEntity dealing with the ClientServerOperations provided by a given PortPrototype. Note that this is restricted to PPortPrototypes of a ClientServer Interface.
    """

    # PortDefinedArgumentValue method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.45, p.593 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getValue          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValue          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getValueTypeTRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValueTypeTRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Specifies the actual value.
        self.value: Optional[ValueSpecification] = None

        # The implementation type of this argument value. It should not be composite type or a pointer. Stereotypes: isOfType
        self.valueTypeTRef: Optional[TRefType] = None

    def getValue(self) -> Optional[ValueSpecification]:
        """
        Specifies the actual value.
        """
        return self.value

    def setValue(self, value: Optional[ValueSpecification]) -> "PortDefinedArgumentValue":
        """
        Specifies the actual value.
        A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self

    def getValueTypeTRef(self) -> Optional[TRefType]:
        """
        The implementation type of this argument value. It should not be composite type or a pointer. Stereotypes: isOfType
        """
        return self.valueTypeTRef

    def setValueTypeTRef(self, value: Optional[TRefType]) -> "PortDefinedArgumentValue":
        """
        The implementation type of this argument value. It should not be composite type or a pointer. Stereotypes: isOfType
        A None value is a no-op and does not overwrite an existing value type reference.
        """
        if value is not None:
            self.valueTypeTRef = value
        return self


class PortAPIOption(ARObject, VariationPointCapable):
    """
    Port API options that define the API configuration for a specific port
    of an atomic software component.
    """

    # PortAPIOption method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getEnableTakeAddress         [x] impl  [x] docstring  [ ] test
    # [ ] setEnableTakeAddress         [x] impl  [x] docstring  [ ] test
    # [ ] getErrorHandling             [x] impl  [x] docstring  [ ] test
    # [ ] setErrorHandling             [x] impl  [x] docstring  [ ] test
    # [ ] getIndirectAPI               [x] impl  [x] docstring  [ ] test
    # [ ] setIndirectAPI               [x] impl  [x] docstring  [ ] test
    # [ ] getPortRef                   [x] impl  [x] docstring  [ ] test
    # [ ] setPortRef                   [x] impl  [x] docstring  [ ] test
    # [ ] getPortArgValues             [x] impl  [x] docstring  [ ] test
    # [ ] addPortArgValue              [x] impl  [x] docstring  [ ] test
    # [ ] getSupportedFeatures         [x] impl  [x] docstring  [ ] test
    # [ ] addSupportedFeature          [x] impl  [x] docstring  [ ] test
    # [ ] getTransformerStatusForwarding [x] impl  [x] docstring  [ ] test
    # [ ] setTransformerStatusForwarding [x] impl  [x] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.enableTakeAddress: Boolean = None
        self.errorHandling = None
        self.indirectAPI: Boolean = None
        self.portRef: RefType = None
        self.portArgValues: List["PortDefinedArgumentValue"] = []
        self.supportedFeatures = []
        self.transformerStatusForwarding = None

    def getEnableTakeAddress(self):
        """
        Gets whether the address-taking feature is enabled.

        Returns:
            Boolean: True if address-taking is enabled
        """
        return self.enableTakeAddress

    def setEnableTakeAddress(self, value):
        """
        Sets whether the address-taking feature is enabled.

        Args:
            value: The enable value to set

        Returns:
            self for method chaining
        """
        self.enableTakeAddress = value
        return self

    def getErrorHandling(self):
        """
        Gets the error handling setting.

        Returns:
            The error handling setting
        """
        return self.errorHandling

    def setErrorHandling(self, value):
        """
        Sets the error handling setting.

        Args:
            value: The error handling setting to set

        Returns:
            self for method chaining
        """
        self.errorHandling = value
        return self

    def getIndirectAPI(self):
        """
        Gets whether indirect API is used.

        Returns:
            Boolean: True if indirect API is used
        """
        return self.indirectAPI

    def setIndirectAPI(self, value):
        """
        Sets whether indirect API is used.

        Args:
            value: The indirect API setting to set

        Returns:
            self for method chaining
        """
        self.indirectAPI = value
        return self

    def getPortRef(self):
        """
        Gets the port reference.

        Returns:
            RefType: The port reference
        """
        return self.portRef

    def setPortRef(self, value):
        """
        Sets the port reference.

        Args:
            value: The port reference to set

        Returns:
            self for method chaining
        """
        self.portRef = value
        return self

    def getPortArgValues(self):
        """
        Gets the list of port argument values.

        Returns:
            List[PortDefinedArgumentValue]: The port argument values
        """
        return self.portArgValues

    def addPortArgValue(self, value):
        """
        Adds a port argument value.

        Args:
            value: The port argument value to add

        Returns:
            self for method chaining
        """
        self.portArgValues.append(value)
        return self

    def getSupportedFeatures(self):
        """
        Gets the list of supported features.

        Returns:
            The list of supported features
        """
        return self.supportedFeatures

    def addSupportedFeature(self, value):
        """
        Adds a supported feature.

        Args:
            value: The supported feature to add

        Returns:
            self for method chaining
        """
        self.supportedFeatures.append(value)
        return self

    def getTransformerStatusForwarding(self):
        """
        Gets the transformer status forwarding setting.

        Returns:
            The transformer status forwarding setting
        """
        return self.transformerStatusForwarding

    def setTransformerStatusForwarding(self, value):
        """
        Sets the transformer status forwarding setting.

        Args:
            value: The transformer status forwarding setting to set

        Returns:
            self for method chaining
        """
        self.transformerStatusForwarding = value
        return self
