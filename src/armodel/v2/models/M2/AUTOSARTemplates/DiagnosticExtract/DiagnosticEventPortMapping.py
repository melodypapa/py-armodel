from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    BswService,
    DiagnosticEvent,
    DiagnosticSwMapping,
    SwcService,
)


class DiagnosticEventPortMapping(DiagnosticSwMapping):
    """
    Defines to which SWC service ports the DiagnosticEvent is mapped.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEventPortMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 249, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a BswServiceDependency that links Service Needs to
        # BswModuleEntries.
        self._bswService: Optional["BswService"] = None

    @property
    def bsw_service(self) -> Optional["BswService"]:
        """Get bswService (Pythonic accessor)."""
        return self._bswService

    @bsw_service.setter
    def bsw_service(self, value: Optional["BswService"]) -> None:
        """
        Set bswService with validation.

        Args:
            value: The bswService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswService = None
            return

        if not isinstance(value, BswService):
            raise TypeError(
                f"bswService must be BswService or None, got {type(value).__name__}"
            )
        self._bswService = value
        # Reference to the DiagnosticEvent that is assigned to ports.
        self._diagnosticEvent: Optional["DiagnosticEvent"] = None

    @property
    def diagnostic_event(self) -> Optional["DiagnosticEvent"]:
        """Get diagnosticEvent (Pythonic accessor)."""
        return self._diagnosticEvent

    @diagnostic_event.setter
    def diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set diagnosticEvent with validation.

        Args:
            value: The diagnosticEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"diagnosticEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._diagnosticEvent = value
        # Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC
        # service ports.
        self._swcFlatService: Optional["SwcService"] = None

    @property
    def swc_flat_service(self) -> Optional["SwcService"]:
        """Get swcFlatService (Pythonic accessor)."""
        return self._swcFlatService

    @swc_flat_service.setter
    def swc_flat_service(self, value: Optional["SwcService"]) -> None:
        """
        Set swcFlatService with validation.

        Args:
            value: The swcFlatService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcFlatService = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"swcFlatService must be SwcService or None, got {type(value).__name__}"
            )
        self._swcFlatService = value
        # ServiceNeeds to SWC service ports.
        # implemented by: SwcServiceDependency.
        self._swcService: Optional["SwcService"] = None

    @property
    def swc_service(self) -> Optional["SwcService"]:
        """Get swcService (Pythonic accessor)."""
        return self._swcService

    @swc_service.setter
    def swc_service(self, value: Optional["SwcService"]) -> None:
        """
        Set swcService with validation.

        Args:
            value: The swcService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcService = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"swcService must be SwcService or None, got {type(value).__name__}"
            )
        self._swcService = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswService(self) -> "BswService":
        """
        AUTOSAR-compliant getter for bswService.

        Returns:
            The bswService value

        Note:
            Delegates to bsw_service property (CODING_RULE_V2_00017)
        """
        return self.bsw_service  # Delegates to property

    def setBswService(self, value: "BswService") -> "DiagnosticEventPortMapping":
        """
        AUTOSAR-compliant setter for bswService with method chaining.

        Args:
            value: The bswService to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_service property setter (gets validation automatically)
        """
        self.bsw_service = value  # Delegates to property setter
        return self

    def getDiagnosticEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for diagnosticEvent.

        Returns:
            The diagnosticEvent value

        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> "DiagnosticEventPortMapping":
        """
        AUTOSAR-compliant setter for diagnosticEvent with method chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_event property setter (gets validation automatically)
        """
        self.diagnostic_event = value  # Delegates to property setter
        return self

    def getSwcFlatService(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for swcFlatService.

        Returns:
            The swcFlatService value

        Note:
            Delegates to swc_flat_service property (CODING_RULE_V2_00017)
        """
        return self.swc_flat_service  # Delegates to property

    def setSwcFlatService(self, value: "SwcService") -> "DiagnosticEventPortMapping":
        """
        AUTOSAR-compliant setter for swcFlatService with method chaining.

        Args:
            value: The swcFlatService to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_flat_service property setter (gets validation automatically)
        """
        self.swc_flat_service = value  # Delegates to property setter
        return self

    def getSwcService(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for swcService.

        Returns:
            The swcService value

        Note:
            Delegates to swc_service property (CODING_RULE_V2_00017)
        """
        return self.swc_service  # Delegates to property

    def setSwcService(self, value: "SwcService") -> "DiagnosticEventPortMapping":
        """
        AUTOSAR-compliant setter for swcService with method chaining.

        Args:
            value: The swcService to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_service property setter (gets validation automatically)
        """
        self.swc_service = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_service(self, value: Optional["BswService"]) -> "DiagnosticEventPortMapping":
        """
        Set bswService and return self for chaining.

        Args:
            value: The bswService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_service("value")
        """
        self.bsw_service = value  # Use property setter (gets validation)
        return self

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticEventPortMapping":
        """
        Set diagnosticEvent and return self for chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_event("value")
        """
        self.diagnostic_event = value  # Use property setter (gets validation)
        return self

    def with_swc_flat_service(self, value: Optional["SwcService"]) -> "DiagnosticEventPortMapping":
        """
        Set swcFlatService and return self for chaining.

        Args:
            value: The swcFlatService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_flat_service("value")
        """
        self.swc_flat_service = value  # Use property setter (gets validation)
        return self

    def with_swc_service(self, value: Optional["SwcService"]) -> "DiagnosticEventPortMapping":
        """
        Set swcService and return self for chaining.

        Args:
            value: The swcService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_service("value")
        """
        self.swc_service = value  # Use property setter (gets validation)
        return self
