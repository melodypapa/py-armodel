from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import SpecElementReference
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class SpecElementScope(SpecElementReference, ABC):
    """
    This class defines if a specification element is relevant within the context
    of this data exchange point.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Common::SpecElementScope

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 84, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is SpecElementScope:
            raise TypeError("SpecElementScope is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # indicates, if a specification element is relevant for this point.
        # It is relevant if inScope==true.
        # It is or don’t care if inScope=false.
        self._inScope: Optional["Boolean"] = None

    @property
    def in_scope(self) -> Optional["Boolean"]:
        """Get inScope (Pythonic accessor)."""
        return self._inScope

    @in_scope.setter
    def in_scope(self, value: Optional["Boolean"]) -> None:
        """
        Set inScope with validation.

        Args:
            value: The inScope to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._inScope = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"inScope must be Boolean or None, got {type(value).__name__}"
            )
        self._inScope = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInScope(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for inScope.

        Returns:
            The inScope value

        Note:
            Delegates to in_scope property (CODING_RULE_V2_00017)
        """
        return self.in_scope  # Delegates to property

    def setInScope(self, value: "Boolean") -> "SpecElementScope":
        """
        AUTOSAR-compliant setter for inScope with method chaining.

        Args:
            value: The inScope to set

        Returns:
            self for method chaining

        Note:
            Delegates to in_scope property setter (gets validation automatically)
        """
        self.in_scope = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_in_scope(self, value: Optional["Boolean"]) -> "SpecElementScope":
        """
        Set inScope and return self for chaining.

        Args:
            value: The inScope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_in_scope("value")
        """
        self.in_scope = value  # Use property setter (gets validation)
        return self
