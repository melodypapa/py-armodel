from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import SubElementRef


class ImplementationDataTypeSubElementRef(SubElementRef):
    """
    This meta-class represents the specialization of SubElementMapping with
    respect to Implementation DataTypes.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ImplementationDataTypeSubElementRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 138, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the referenced implementationDataType Element.
        self._implementation: Optional["ArVariableIn"] = None

    @property
    def implementation(self) -> Optional["ArVariableIn"]:
        """Get implementation (Pythonic accessor)."""
        return self._implementation

    @implementation.setter
    def implementation(self, value: Optional["ArVariableIn"]) -> None:
        """
        Set implementation with validation.

        Args:
            value: The implementation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implementation = None
            return

        if not isinstance(value, ArVariableIn):
            raise TypeError(
                f"implementation must be ArVariableIn or None, got {type(value).__name__}"
            )
        self._implementation = value
        # This represents the referenced ImplementationDataType Element.
        self._parameter: Optional["ArParameterIn"] = None

    @property
    def parameter(self) -> Optional["ArParameterIn"]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter

    @parameter.setter
    def parameter(self, value: Optional["ArParameterIn"]) -> None:
        """
        Set parameter with validation.

        Args:
            value: The parameter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._parameter = None
            return

        if not isinstance(value, ArParameterIn):
            raise TypeError(
                f"parameter must be ArParameterIn or None, got {type(value).__name__}"
            )
        self._parameter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getImplementation(self) -> "ArVariableIn":
        """
        AUTOSAR-compliant getter for implementation.

        Returns:
            The implementation value

        Note:
            Delegates to implementation property (CODING_RULE_V2_00017)
        """
        return self.implementation  # Delegates to property

    def setImplementation(self, value: "ArVariableIn") -> "ImplementationDataTypeSubElementRef":
        """
        AUTOSAR-compliant setter for implementation with method chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Note:
            Delegates to implementation property setter (gets validation automatically)
        """
        self.implementation = value  # Delegates to property setter
        return self

    def getParameter(self) -> "ArParameterIn":
        """
        AUTOSAR-compliant getter for parameter.

        Returns:
            The parameter value

        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    def setParameter(self, value: "ArParameterIn") -> "ImplementationDataTypeSubElementRef":
        """
        AUTOSAR-compliant setter for parameter with method chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Note:
            Delegates to parameter property setter (gets validation automatically)
        """
        self.parameter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_implementation(self, value: Optional["ArVariableIn"]) -> "ImplementationDataTypeSubElementRef":
        """
        Set implementation and return self for chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_implementation("value")
        """
        self.implementation = value  # Use property setter (gets validation)
        return self

    def with_parameter(self, value: Optional["ArParameterIn"]) -> "ImplementationDataTypeSubElementRef":
        """
        Set parameter and return self for chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter("value")
        """
        self.parameter = value  # Use property setter (gets validation)
        return self
