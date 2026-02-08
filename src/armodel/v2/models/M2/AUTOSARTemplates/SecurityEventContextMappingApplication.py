from armodel.v2.models.M2.AUTOSARTemplates.SecurityExtractTemplate import SecurityEventContextMapping

class SecurityEventContextMappingApplication(SecurityEventContextMapping):
    """
    This meta-class represents the ability to associate a collection of security
    events with an IdsM instance and with the executional context of an
    application (e.g. name of SWC on CP or name of SWCL on AP) in which this
    IdsM instance can receive reports for these security events.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventContextMappingApplication

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 42, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to identify the name of the in whose executional
        # context a security event This application can be, for example, a name
        # Software Component (for CP) or a Software Cluster AP).
        self._affected: "String" = None

    @property
    def affected(self) -> "String":
        """Get affected (Pythonic accessor)."""
        return self._affected

    @affected.setter
    def affected(self, value: "String") -> None:
        """
        Set affected with validation.

        Args:
            value: The affected to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, String):
            raise TypeError(
                f"affected must be String, got {type(value).__name__}"
            )
        self._affected = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAffected(self) -> "String":
        """
        AUTOSAR-compliant getter for affected.

        Returns:
            The affected value

        Note:
            Delegates to affected property (CODING_RULE_V2_00017)
        """
        return self.affected  # Delegates to property

    def setAffected(self, value: "String") -> "SecurityEventContextMappingApplication":
        """
        AUTOSAR-compliant setter for affected with method chaining.

        Args:
            value: The affected to set

        Returns:
            self for method chaining

        Note:
            Delegates to affected property setter (gets validation automatically)
        """
        self.affected = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_affected(self, value: "String") -> "SecurityEventContextMappingApplication":
        """
        Set affected and return self for chaining.

        Args:
            value: The affected to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_affected("value")
        """
        self.affected = value  # Use property setter (gets validation)
        return self
