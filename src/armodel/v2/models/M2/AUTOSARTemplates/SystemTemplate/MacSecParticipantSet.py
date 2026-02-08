from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class MacSecParticipantSet(ARElement):
    """
    Collection of MACsec Kay Participants on an Ethernet Link.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::MacSecParticipantSet

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 174, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the EthernetCluster (Link) on which the KaY located.
        self._ethernetCluster: Optional["EthernetCluster"] = None

    @property
    def ethernet_cluster(self) -> Optional["EthernetCluster"]:
        """Get ethernetCluster (Pythonic accessor)."""
        return self._ethernetCluster

    @ethernet_cluster.setter
    def ethernet_cluster(self, value: Optional["EthernetCluster"]) -> None:
        """
        Set ethernetCluster with validation.

        Args:
            value: The ethernetCluster to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ethernetCluster = None
            return

        if not isinstance(value, EthernetCluster):
            raise TypeError(
                f"ethernetCluster must be EthernetCluster or None, got {type(value).__name__}"
            )
        self._ethernetCluster = value
        # Configuration of a MKA Participant.
        self._mkaParticipant: List["MacSecKayParticipant"] = []

    @property
    def mka_participant(self) -> List["MacSecKayParticipant"]:
        """Get mkaParticipant (Pythonic accessor)."""
        return self._mkaParticipant

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEthernetCluster(self) -> "EthernetCluster":
        """
        AUTOSAR-compliant getter for ethernetCluster.

        Returns:
            The ethernetCluster value

        Note:
            Delegates to ethernet_cluster property (CODING_RULE_V2_00017)
        """
        return self.ethernet_cluster  # Delegates to property

    def setEthernetCluster(self, value: "EthernetCluster") -> "MacSecParticipantSet":
        """
        AUTOSAR-compliant setter for ethernetCluster with method chaining.

        Args:
            value: The ethernetCluster to set

        Returns:
            self for method chaining

        Note:
            Delegates to ethernet_cluster property setter (gets validation automatically)
        """
        self.ethernet_cluster = value  # Delegates to property setter
        return self

    def getMkaParticipant(self) -> List["MacSecKayParticipant"]:
        """
        AUTOSAR-compliant getter for mkaParticipant.

        Returns:
            The mkaParticipant value

        Note:
            Delegates to mka_participant property (CODING_RULE_V2_00017)
        """
        return self.mka_participant  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ethernet_cluster(self, value: Optional["EthernetCluster"]) -> "MacSecParticipantSet":
        """
        Set ethernetCluster and return self for chaining.

        Args:
            value: The ethernetCluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ethernet_cluster("value")
        """
        self.ethernet_cluster = value  # Use property setter (gets validation)
        return self
