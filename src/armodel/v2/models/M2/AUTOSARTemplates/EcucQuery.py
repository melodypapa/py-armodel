from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class EcucQuery(Identifiable):
    """
    Defines a query to the ECUC Description.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucQuery

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 89, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the EcucQuery used in the calculation formula or condition formula.
        self._ecucQuery: Optional["EcucQueryExpression"] = None

    @property
    def ecuc_query(self) -> Optional["EcucQueryExpression"]:
        """Get ecucQuery (Pythonic accessor)."""
        return self._ecucQuery

    @ecuc_query.setter
    def ecuc_query(self, value: Optional["EcucQueryExpression"]) -> None:
        """
        Set ecucQuery with validation.

        Args:
            value: The ecucQuery to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecucQuery = None
            return

        if not isinstance(value, EcucQueryExpression):
            raise TypeError(
                f"ecucQuery must be EcucQueryExpression or None, got {type(value).__name__}"
            )
        self._ecucQuery = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcucQuery(self) -> "EcucQueryExpression":
        """
        AUTOSAR-compliant getter for ecucQuery.

        Returns:
            The ecucQuery value

        Note:
            Delegates to ecuc_query property (CODING_RULE_V2_00017)
        """
        return self.ecuc_query  # Delegates to property

    def setEcucQuery(self, value: "EcucQueryExpression") -> "EcucQuery":
        """
        AUTOSAR-compliant setter for ecucQuery with method chaining.

        Args:
            value: The ecucQuery to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecuc_query property setter (gets validation automatically)
        """
        self.ecuc_query = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecuc_query(self, value: Optional["EcucQueryExpression"]) -> "EcucQuery":
        """
        Set ecucQuery and return self for chaining.

        Args:
            value: The ecucQuery to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecuc_query("value")
        """
        self.ecuc_query = value  # Use property setter (gets validation)
        return self
