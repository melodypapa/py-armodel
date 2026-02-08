from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class Tbody(ARObject):
    """
    This meta-class represents a part within a table group. Such a part can be
    the table head, the table body or the table foot.

    Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable::Tbody

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 335, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Indicates how the cells in the rows shall be aligned.
        # inherited from tbody, otherwise it is "TOP".
        self._valign: Optional["ValignEnum"] = None

    @property
    def valign(self) -> Optional["ValignEnum"]:
        """Get valign (Pythonic accessor)."""
        return self._valign

    @valign.setter
    def valign(self, value: Optional["ValignEnum"]) -> None:
        """
        Set valign with validation.

        Args:
            value: The valign to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._valign = None
            return

        if not isinstance(value, ValignEnum):
            raise TypeError(
                f"valign must be ValignEnum or None, got {type(value).__name__}"
            )
        self._valign = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValign(self) -> "ValignEnum":
        """
        AUTOSAR-compliant getter for valign.

        Returns:
            The valign value

        Note:
            Delegates to valign property (CODING_RULE_V2_00017)
        """
        return self.valign  # Delegates to property

    def setValign(self, value: "ValignEnum") -> "Tbody":
        """
        AUTOSAR-compliant setter for valign with method chaining.

        Args:
            value: The valign to set

        Returns:
            self for method chaining

        Note:
            Delegates to valign property setter (gets validation automatically)
        """
        self.valign = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_valign(self, value: Optional["ValignEnum"]) -> "Tbody":
        """
        Set valign and return self for chaining.

        Args:
            value: The valign to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_valign("value")
        """
        self.valign = value  # Use property setter (gets validation)
        return self
