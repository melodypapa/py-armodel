from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class ApplicationError(Identifiable):
    """
    This is a user-defined error that is associated with an element of an
    AUTOSAR interface. It is specific for the particular functionality or
    service provided by the AUTOSAR software component.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 108, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1996, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The RTE generator is forced to assign this value to the symbol.
        # Note that for error codes are predefined (see RTE specification).
        self._errorCode: Optional["Integer"] = None

    @property
    def error_code(self) -> Optional["Integer"]:
        """Get errorCode (Pythonic accessor)."""
        return self._errorCode

    @error_code.setter
    def error_code(self, value: Optional["Integer"]) -> None:
        """
        Set errorCode with validation.

        Args:
            value: The errorCode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._errorCode = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"errorCode must be Integer or None, got {type(value).__name__}"
            )
        self._errorCode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getErrorCode(self) -> "Integer":
        """
        AUTOSAR-compliant getter for errorCode.

        Returns:
            The errorCode value

        Note:
            Delegates to error_code property (CODING_RULE_V2_00017)
        """
        return self.error_code  # Delegates to property

    def setErrorCode(self, value: "Integer") -> "ApplicationError":
        """
        AUTOSAR-compliant setter for errorCode with method chaining.

        Args:
            value: The errorCode to set

        Returns:
            self for method chaining

        Note:
            Delegates to error_code property setter (gets validation automatically)
        """
        self.error_code = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_error_code(self, value: Optional["Integer"]) -> "ApplicationError":
        """
        Set errorCode and return self for chaining.

        Args:
            value: The errorCode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_error_code("value")
        """
        self.error_code = value  # Use property setter (gets validation)
        return self
