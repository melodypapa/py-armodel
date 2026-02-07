from typing import Optional


class CryptoServiceQueue(ARElement):
    """
    This meta-class has the ability to represent a crypto queue.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::CryptoServiceQueue

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 381, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the queue size of the CryptoServiceQueue.
        self._queueSize: Optional["PositiveInteger"] = None

    @property
    def queue_size(self) -> Optional["PositiveInteger"]:
        """Get queueSize (Pythonic accessor)."""
        return self._queueSize

    @queue_size.setter
    def queue_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set queueSize with validation.

        Args:
            value: The queueSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._queueSize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"queueSize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._queueSize = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getQueueSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for queueSize.

        Returns:
            The queueSize value

        Note:
            Delegates to queue_size property (CODING_RULE_V2_00017)
        """
        return self.queue_size  # Delegates to property

    def setQueueSize(self, value: "PositiveInteger") -> "CryptoServiceQueue":
        """
        AUTOSAR-compliant setter for queueSize with method chaining.

        Args:
            value: The queueSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to queue_size property setter (gets validation automatically)
        """
        self.queue_size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_queue_size(self, value: Optional["PositiveInteger"]) -> "CryptoServiceQueue":
        """
        Set queueSize and return self for chaining.

        Args:
            value: The queueSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_queue_size("value")
        """
        self.queue_size = value  # Use property setter (gets validation)
        return self
