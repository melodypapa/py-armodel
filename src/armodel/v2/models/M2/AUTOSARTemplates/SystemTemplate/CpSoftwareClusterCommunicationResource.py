from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import CpSoftwareClusterResource


class CpSoftwareClusterCommunicationResource(CpSoftwareClusterResource):
    """
    Represents a single resource required or provided by a CP Software Cluster
    which relates to the port based communication on VFB level.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::CpSoftwareClusterCommunicationResource

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 902, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation supports the further qualification of the enclosing
        # CpSoftwareClusterCommunicationRecource by of additional attributes depending
        # on the nature of.
        self._communication: Optional["CpSoftwareCluster"] = None

    @property
    def communication(self) -> Optional["CpSoftwareCluster"]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional["CpSoftwareCluster"]) -> None:
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

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"communication must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._communication = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for communication.

        Returns:
            The communication value

        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "CpSoftwareCluster") -> "CpSoftwareClusterCommunicationResource":
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

    def with_communication(self, value: Optional["CpSoftwareCluster"]) -> "CpSoftwareClusterCommunicationResource":
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
