from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import (
    CpSoftwareClusterCommunicationResourceProps,
)


class ClientServerOperationComProps(CpSoftwareClusterCommunicationResourceProps):
    """
    Defines additional attributes for the implementation of Client Server
    communication between software clusters

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 903, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Length of call request queue on the server side.
        # The implemented by the SwCluC.
        # The value shall be equal to 1.
        # Setting the value of queueLength to that incoming requests are rejected while
                # that arrived earlier is being processed.
        self._queueLength: Optional["PositiveInteger"] = None

    @property
    def queue_length(self) -> Optional["PositiveInteger"]:
        """Get queueLength (Pythonic accessor)."""
        return self._queueLength

    @queue_length.setter
    def queue_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set queueLength with validation.

        Args:
            value: The queueLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._queueLength = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"queueLength must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._queueLength = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getQueueLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for queueLength.

        Returns:
            The queueLength value

        Note:
            Delegates to queue_length property (CODING_RULE_V2_00017)
        """
        return self.queue_length  # Delegates to property

    def setQueueLength(self, value: "PositiveInteger") -> "ClientServerOperationComProps":
        """
        AUTOSAR-compliant setter for queueLength with method chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to queue_length property setter (gets validation automatically)
        """
        self.queue_length = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_queue_length(self, value: Optional["PositiveInteger"]) -> "ClientServerOperationComProps":
        """
        Set queueLength and return self for chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_queue_length("value")
        """
        self.queue_length = value  # Use property setter (gets validation)
        return self
