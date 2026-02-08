from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.ApplicationCompositeElementDataPrototype import (
    ApplicationCompositeElementDataPrototype,
    )


class ApplicationRecordElement(ApplicationCompositeElementDataPrototype):
    """
    Describes the properties of one particular element of an application record
    data type.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes::ApplicationRecordElement

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 261, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1997, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 43, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the ability to declare the as optional.
        # This that, at runtime, the ApplicationRecord or may not have a valid value
                # and shall ignored.
        # runtime software provides means to set as not valid at the sending a
                # communication and determine its validity at the.
        self._isOptional: Optional["Boolean"] = None

    @property
    def is_optional(self) -> Optional["Boolean"]:
        """Get isOptional (Pythonic accessor)."""
        return self._isOptional

    @is_optional.setter
    def is_optional(self, value: Optional["Boolean"]) -> None:
        """
        Set isOptional with validation.

        Args:
            value: The isOptional to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isOptional = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isOptional must be Boolean or None, got {type(value).__name__}"
            )
        self._isOptional = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIsOptional(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isOptional.

        Returns:
            The isOptional value

        Note:
            Delegates to is_optional property (CODING_RULE_V2_00017)
        """
        return self.is_optional  # Delegates to property

    def setIsOptional(self, value: "Boolean") -> "ApplicationRecordElement":
        """
        AUTOSAR-compliant setter for isOptional with method chaining.

        Args:
            value: The isOptional to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_optional property setter (gets validation automatically)
        """
        self.is_optional = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_is_optional(self, value: Optional["Boolean"]) -> "ApplicationRecordElement":
        """
        Set isOptional and return self for chaining.

        Args:
            value: The isOptional to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_optional("value")
        """
        self.is_optional = value  # Use property setter (gets validation)
        return self
