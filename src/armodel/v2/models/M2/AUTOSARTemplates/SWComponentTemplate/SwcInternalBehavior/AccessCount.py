from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class AccessCount(ARObject):
    """
    This meta-class provides one count value for a AbstractAccessPoint.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount::AccessCount

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 57, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # AbstractAccessPoint for which the count value is.
        self._accessPoint: Optional["AbstractAccessPoint"] = None

    @property
    def access_point(self) -> Optional["AbstractAccessPoint"]:
        """Get accessPoint (Pythonic accessor)."""
        return self._accessPoint

    @access_point.setter
    def access_point(self, value: Optional["AbstractAccessPoint"]) -> None:
        """
        Set accessPoint with validation.

        Args:
            value: The accessPoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accessPoint = None
            return

        if not isinstance(value, AbstractAccessPoint):
            raise TypeError(
                f"accessPoint must be AbstractAccessPoint or None, got {type(value).__name__}"
            )
        self._accessPoint = value
        # This attribute represents the number of determined.
        self._value: Optional["PositiveInteger"] = None

    @property
    def value(self) -> Optional["PositiveInteger"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"value must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessPoint(self) -> "AbstractAccessPoint":
        """
        AUTOSAR-compliant getter for accessPoint.

        Returns:
            The accessPoint value

        Note:
            Delegates to access_point property (CODING_RULE_V2_00017)
        """
        return self.access_point  # Delegates to property

    def setAccessPoint(self, value: "AbstractAccessPoint") -> "AccessCount":
        """
        AUTOSAR-compliant setter for accessPoint with method chaining.

        Args:
            value: The accessPoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to access_point property setter (gets validation automatically)
        """
        self.access_point = value  # Delegates to property setter
        return self

    def getValue(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "PositiveInteger") -> "AccessCount":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_access_point(self, value: Optional["AbstractAccessPoint"]) -> "AccessCount":
        """
        Set accessPoint and return self for chaining.

        Args:
            value: The accessPoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_access_point("value")
        """
        self.access_point = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: Optional["PositiveInteger"]) -> "AccessCount":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self
