from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    IdsCommonElement,
    SymbolProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SecurityEventDefinition(IdsCommonElement):
    """
    This meta-class defines a security-related event as part of the intrusion
    detection system.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventDefinition

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 259, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 17, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation defines optionally an alternative Event for the
        # SecurityEventDefinition in case there is a shortNames.
        self._eventSymbol: Optional["SymbolProps"] = None

    @property
    def event_symbol(self) -> Optional["SymbolProps"]:
        """Get eventSymbol (Pythonic accessor)."""
        return self._eventSymbol

    @event_symbol.setter
    def event_symbol(self, value: Optional["SymbolProps"]) -> None:
        """
        Set eventSymbol with validation.

        Args:
            value: The eventSymbol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventSymbol = None
            return

        if not isinstance(value, SymbolProps):
            raise TypeError(
                f"eventSymbol must be SymbolProps or None, got {type(value).__name__}"
            )
        self._eventSymbol = value
        # This attribute represents the numerical identification of security event.
        # The identification shall be the scope of the IDS.
        self._id: Optional["PositiveInteger"] = None

    @property
    def id(self) -> Optional["PositiveInteger"]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set id with validation.

        Args:
            value: The id to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._id = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"id must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._id = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventSymbol(self) -> "SymbolProps":
        """
        AUTOSAR-compliant getter for eventSymbol.

        Returns:
            The eventSymbol value

        Note:
            Delegates to event_symbol property (CODING_RULE_V2_00017)
        """
        return self.event_symbol  # Delegates to property

    def setEventSymbol(self, value: "SymbolProps") -> "SecurityEventDefinition":
        """
        AUTOSAR-compliant setter for eventSymbol with method chaining.

        Args:
            value: The eventSymbol to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_symbol property setter (gets validation automatically)
        """
        self.event_symbol = value  # Delegates to property setter
        return self

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> "SecurityEventDefinition":
        """
        AUTOSAR-compliant setter for id with method chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Note:
            Delegates to id property setter (gets validation automatically)
        """
        self.id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_symbol(self, value: Optional["SymbolProps"]) -> "SecurityEventDefinition":
        """
        Set eventSymbol and return self for chaining.

        Args:
            value: The eventSymbol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_symbol("value")
        """
        self.event_symbol = value  # Use property setter (gets validation)
        return self

    def with_id(self, value: Optional["PositiveInteger"]) -> "SecurityEventDefinition":
        """
        Set id and return self for chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_id("value")
        """
        self.id = value  # Use property setter (gets validation)
        return self
