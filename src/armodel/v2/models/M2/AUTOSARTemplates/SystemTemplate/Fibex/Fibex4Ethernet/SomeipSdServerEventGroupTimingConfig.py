from typing import Optional


class SomeipSdServerEventGroupTimingConfig(ARElement):
    """
    EventGroup specific timing configuration settings.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::SomeipSdServerEventGroupTimingConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 517, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The Service Discovery shall delay answers to unicast triggered by multicast
                # messages (e.
        # g.
        # after Offer Service).
        self._request: Optional["RequestResponseDelay"] = None

    @property
    def request(self) -> Optional["RequestResponseDelay"]:
        """Get request (Pythonic accessor)."""
        return self._request

    @request.setter
    def request(self, value: Optional["RequestResponseDelay"]) -> None:
        """
        Set request with validation.

        Args:
            value: The request to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._request = None
            return

        if not isinstance(value, RequestResponseDelay):
            raise TypeError(
                f"request must be RequestResponseDelay or None, got {type(value).__name__}"
            )
        self._request = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequest(self) -> "RequestResponseDelay":
        """
        AUTOSAR-compliant getter for request.

        Returns:
            The request value

        Note:
            Delegates to request property (CODING_RULE_V2_00017)
        """
        return self.request  # Delegates to property

    def setRequest(self, value: "RequestResponseDelay") -> "SomeipSdServerEventGroupTimingConfig":
        """
        AUTOSAR-compliant setter for request with method chaining.

        Args:
            value: The request to set

        Returns:
            self for method chaining

        Note:
            Delegates to request property setter (gets validation automatically)
        """
        self.request = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_request(self, value: Optional["RequestResponseDelay"]) -> "SomeipSdServerEventGroupTimingConfig":
        """
        Set request and return self for chaining.

        Args:
            value: The request to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request("value")
        """
        self.request = value  # Use property setter (gets validation)
        return self
