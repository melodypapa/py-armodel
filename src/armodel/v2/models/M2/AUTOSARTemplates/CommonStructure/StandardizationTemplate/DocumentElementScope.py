from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DataFormatElement,
    SpecElementReference,
    Traceable,
)


class DocumentElementScope(SpecElementReference):
    """
    Specifies if a specification element such as a requirement, specification,
    deliverable, artifact, task definition or activity is in scope of this data
    exchange point. The DocumentElementScope may reference all specification
    elements that have a name or ID. The only exception are Meta Classes, Meta
    Attribute and constraints which are handled in the Data Format Tailoring
    section of the Profile of Data Exchange Point. Elements of Autosar
    specification documents are referenced via their ID (requirement,
    specification items) or name (deliverable, artifact, task definition or
    activity)

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchange::DocumentElementScope

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 97, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a custom defined specification element.
        self._custom: Optional["Traceable"] = None

    @property
    def custom(self) -> Optional["Traceable"]:
        """Get custom (Pythonic accessor)."""
        return self._custom

    @custom.setter
    def custom(self, value: Optional["Traceable"]) -> None:
        """
        Set custom with validation.

        Args:
            value: The custom to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._custom = None
            return

        if not isinstance(value, Traceable):
            raise TypeError(
                f"custom must be Traceable or None, got {type(value).__name__}"
            )
        self._custom = value
        # Data Format Element that is implied by this element in the Used to share one
        # rationale for more.
        self._tailoring: List["DataFormatElement"] = []

    @property
    def tailoring(self) -> List["DataFormatElement"]:
        """Get tailoring (Pythonic accessor)."""
        return self._tailoring

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCustom(self) -> "Traceable":
        """
        AUTOSAR-compliant getter for custom.

        Returns:
            The custom value

        Note:
            Delegates to custom property (CODING_RULE_V2_00017)
        """
        return self.custom  # Delegates to property

    def setCustom(self, value: "Traceable") -> "DocumentElementScope":
        """
        AUTOSAR-compliant setter for custom with method chaining.

        Args:
            value: The custom to set

        Returns:
            self for method chaining

        Note:
            Delegates to custom property setter (gets validation automatically)
        """
        self.custom = value  # Delegates to property setter
        return self

    def getTailoring(self) -> List["DataFormatElement"]:
        """
        AUTOSAR-compliant getter for tailoring.

        Returns:
            The tailoring value

        Note:
            Delegates to tailoring property (CODING_RULE_V2_00017)
        """
        return self.tailoring  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_custom(self, value: Optional["Traceable"]) -> "DocumentElementScope":
        """
        Set custom and return self for chaining.

        Args:
            value: The custom to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_custom("value")
        """
        self.custom = value  # Use property setter (gets validation)
        return self
