from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class AbstractAccessPoint(Identifiable, ABC):
    """
    Abstract class indicating an access point from an ExecutableEntity.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::AccessCount::AbstractAccessPoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 57, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 562, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is AbstractAccessPoint:
            raise TypeError("AbstractAccessPoint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute controls the provision of return values for RTE APIs that
        # correspond to the enclosing access point.
        self._returnValue: Optional["RteApiReturnValue"] = None

    @property
    def return_value(self) -> Optional["RteApiReturnValue"]:
        """Get returnValue (Pythonic accessor)."""
        return self._returnValue

    @return_value.setter
    def return_value(self, value: Optional["RteApiReturnValue"]) -> None:
        """
        Set returnValue with validation.

        Args:
            value: The returnValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._returnValue = None
            return

        if not isinstance(value, RteApiReturnValue):
            raise TypeError(
                f"returnValue must be RteApiReturnValue or None, got {type(value).__name__}"
            )
        self._returnValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReturnValue(self) -> "RteApiReturnValue":
        """
        AUTOSAR-compliant getter for returnValue.

        Returns:
            The returnValue value

        Note:
            Delegates to return_value property (CODING_RULE_V2_00017)
        """
        return self.return_value  # Delegates to property

    def setReturnValue(self, value: "RteApiReturnValue") -> "AbstractAccessPoint":
        """
        AUTOSAR-compliant setter for returnValue with method chaining.

        Args:
            value: The returnValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to return_value property setter (gets validation automatically)
        """
        self.return_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_return_value(self, value: Optional["RteApiReturnValue"]) -> "AbstractAccessPoint":
        """
        Set returnValue and return self for chaining.

        Args:
            value: The returnValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_return_value("value")
        """
        self.return_value = value  # Use property setter (gets validation)
        return self
