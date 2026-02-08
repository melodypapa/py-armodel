from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
)


class DiagnosticComControlClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the
    "Communication Control" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommunicationControl

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 109, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference represents the semantics that all available be affected.
        # It is still necessary to refer to because there could CommunicationClusters
                # in the System Extract not subject to the service "communication to the
                # applicable CommunicationClusters it made sure that only the affected
                # Communication accessed.
        self._allChannels: List["CommunicationCluster"] = []

    @property
    def all_channels(self) -> List["CommunicationCluster"]:
        """Get allChannels (Pythonic accessor)."""
        return self._allChannels
        # This reference represents the semantics that all available channels shall be
                # affected.
        # It is still necessary to refer to because there could VLANs (and thus private
                # EthernetPhysical the System Extract that are not subject to "communication
                # control".
        # to the applicable EthernetPhysicalChannels it made sure that only the
                # affected EthernetPhysical accessed.
        self._allPhysical: List["EthernetPhysical"] = []

    @property
    def all_physical(self) -> List["EthernetPhysical"]:
        """Get allPhysical (Pythonic accessor)."""
        return self._allPhysical
        # This represents the ability to add additional attributes to case that only
        # specific channels are supposed to be.
        self._specificChannel: List["DiagnosticComControl"] = []

    @property
    def specific_channel(self) -> List["DiagnosticComControl"]:
        """Get specificChannel (Pythonic accessor)."""
        return self._specificChannel
        # This attribute represents the ability to add further attributes to the
        # definition of a specific sub-node channel subject to the diagnostic service
        # "communication.
        self._subNode: List["DiagnosticComControl"] = []

    @property
    def sub_node(self) -> List["DiagnosticComControl"]:
        """Get subNode (Pythonic accessor)."""
        return self._subNode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAllChannels(self) -> List["CommunicationCluster"]:
        """
        AUTOSAR-compliant getter for allChannels.

        Returns:
            The allChannels value

        Note:
            Delegates to all_channels property (CODING_RULE_V2_00017)
        """
        return self.all_channels  # Delegates to property

    def getAllPhysical(self) -> List["EthernetPhysical"]:
        """
        AUTOSAR-compliant getter for allPhysical.

        Returns:
            The allPhysical value

        Note:
            Delegates to all_physical property (CODING_RULE_V2_00017)
        """
        return self.all_physical  # Delegates to property

    def getSpecificChannel(self) -> List["DiagnosticComControl"]:
        """
        AUTOSAR-compliant getter for specificChannel.

        Returns:
            The specificChannel value

        Note:
            Delegates to specific_channel property (CODING_RULE_V2_00017)
        """
        return self.specific_channel  # Delegates to property

    def getSubNode(self) -> List["DiagnosticComControl"]:
        """
        AUTOSAR-compliant getter for subNode.

        Returns:
            The subNode value

        Note:
            Delegates to sub_node property (CODING_RULE_V2_00017)
        """
        return self.sub_node  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
