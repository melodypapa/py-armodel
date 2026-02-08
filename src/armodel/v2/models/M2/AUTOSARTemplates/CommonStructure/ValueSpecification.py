from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class ValueSpecification(ARObject, ABC):
    """
    Base class for expressions leading to a value which can be used to
    initialize a data object.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 333, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 433, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2076, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is ValueSpecification:
            raise TypeError("ValueSpecification is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This can be used to identify particular value specifications readers, for
        # example elements of a record type.
        self._shortLabel: Optional["Identifier"] = None

    @property
    def short_label(self) -> Optional["Identifier"]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional["Identifier"]) -> None:
        """
        Set shortLabel with validation.

        Args:
            value: The shortLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortLabel = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"shortLabel must be Identifier or None, got {type(value).__name__}"
            )
        self._shortLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getShortLabel(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "Identifier") -> "ValueSpecification":
        """
        AUTOSAR-compliant setter for shortLabel with method chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to short_label property setter (gets validation automatically)
        """
        self.short_label = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_short_label(self, value: Optional["Identifier"]) -> "ValueSpecification":
        """
        Set shortLabel and return self for chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_label("value")
        """
        self.short_label = value  # Use property setter (gets validation)
        return self
