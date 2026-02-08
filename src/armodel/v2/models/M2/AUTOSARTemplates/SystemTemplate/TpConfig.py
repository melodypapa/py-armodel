from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CommunicationCluster,
    FibexElement,
)


class TpConfig(FibexElement, ABC):
    """
    Contains all configuration elements for AUTOSAR TP.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::TpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 587, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TpConfig:
            raise TypeError("TpConfig is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A TpConfig is existing always in the context of exactly one.
        self._communication: Optional["CommunicationCluster"] = None

    @property
    def communication(self) -> Optional["CommunicationCluster"]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional["CommunicationCluster"]) -> None:
        """
        Set communication with validation.

        Args:
            value: The communication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._communication = None
            return

        if not isinstance(value, CommunicationCluster):
            raise TypeError(
                f"communication must be CommunicationCluster or None, got {type(value).__name__}"
            )
        self._communication = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> "CommunicationCluster":
        """
        AUTOSAR-compliant getter for communication.

        Returns:
            The communication value

        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "CommunicationCluster") -> "TpConfig":
        """
        AUTOSAR-compliant setter for communication with method chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Note:
            Delegates to communication property setter (gets validation automatically)
        """
        self.communication = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional["CommunicationCluster"]) -> "TpConfig":
        """
        Set communication and return self for chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_communication("value")
        """
        self.communication = value  # Use property setter (gets validation)
        return self
