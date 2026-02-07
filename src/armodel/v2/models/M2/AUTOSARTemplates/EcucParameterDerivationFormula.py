from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class EcucParameterDerivationFormula(ARObject):
    """
    This formula is intended to specify how an ecu parameter can be derived from
    other information in the Autosar Templates.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucParameterDerivationFormula

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 88, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This indicates that the referenced query shall return a.
        self._ecucQuery: Optional["EcucQuery"] = None

    @property
    def ecuc_query(self) -> Optional["EcucQuery"]:
        """Get ecucQuery (Pythonic accessor)."""
        return self._ecucQuery

    @ecuc_query.setter
    def ecuc_query(self, value: Optional["EcucQuery"]) -> None:
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

        if not isinstance(value, EcucQuery):
            raise TypeError(
                f"ecucQuery must be EcucQuery or None, got {type(value).__name__}"
            )
        self._ecucQuery = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcucQuery(self) -> "EcucQuery":
        """
        AUTOSAR-compliant getter for ecucQuery.

        Returns:
            The ecucQuery value

        Note:
            Delegates to ecuc_query property (CODING_RULE_V2_00017)
        """
        return self.ecuc_query  # Delegates to property

    def setEcucQuery(self, value: "EcucQuery") -> "EcucParameterDerivationFormula":
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

    def with_ecuc_query(self, value: Optional["EcucQuery"]) -> "EcucParameterDerivationFormula":
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
