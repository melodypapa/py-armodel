from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SecurityExtractTemplate import SecurityEventContextMapping


class SecurityEventContextMappingBswModule(SecurityEventContextMapping):
    """
    This meta-class represents the ability to associate a collection of security
    events with an IdsM instance and with the executional context of a BSW
    module in which this IdsM instance can receive reports for these security
    events.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventContextMappingBswModule

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 38, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to identify the name of the BSW in whose executional
        # context a security event can set of BSW module names is standardized by.
        self._affectedBsw: Optional["String"] = None

    @property
    def affected_bsw(self) -> Optional["String"]:
        """Get affectedBsw (Pythonic accessor)."""
        return self._affectedBsw

    @affected_bsw.setter
    def affected_bsw(self, value: Optional["String"]) -> None:
        """
        Set affectedBsw with validation.

        Args:
            value: The affectedBsw to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._affectedBsw = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"affectedBsw must be String or None, got {type(value).__name__}"
            )
        self._affectedBsw = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAffectedBsw(self) -> "String":
        """
        AUTOSAR-compliant getter for affectedBsw.

        Returns:
            The affectedBsw value

        Note:
            Delegates to affected_bsw property (CODING_RULE_V2_00017)
        """
        return self.affected_bsw  # Delegates to property

    def setAffectedBsw(self, value: "String") -> "SecurityEventContextMappingBswModule":
        """
        AUTOSAR-compliant setter for affectedBsw with method chaining.

        Args:
            value: The affectedBsw to set

        Returns:
            self for method chaining

        Note:
            Delegates to affected_bsw property setter (gets validation automatically)
        """
        self.affected_bsw = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_affected_bsw(self, value: Optional["String"]) -> "SecurityEventContextMappingBswModule":
        """
        Set affectedBsw and return self for chaining.

        Args:
            value: The affectedBsw to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_affected_bsw("value")
        """
        self.affected_bsw = value  # Use property setter (gets validation)
        return self
