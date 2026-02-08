from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import CouplingElementAbstractDetails


class CouplingElementSwitchDetails(CouplingElementAbstractDetails):
    """
    Collection of specific details for the CouplingElement of couplingType
    switch.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingElementSwitchDetails

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 133, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of Flow Metering Entries.
        # atp.
        # Status=candidate.
        self._flowMetering: List["SwitchFlowMetering"] = []

    @property
    def flow_metering(self) -> List["SwitchFlowMetering"]:
        """Get flowMetering (Pythonic accessor)."""
        return self._flowMetering
        # Collection of Stream Filter Entries.
        # atp.
        # Status=candidate.
        self._streamFilter: List["SwitchStreamFilterEntry"] = []

    @property
    def stream_filter(self) -> List["SwitchStreamFilterEntry"]:
        """Get streamFilter (Pythonic accessor)."""
        return self._streamFilter
        # Collection of Stream Gate Entries.
        self._streamGate: List["SwitchStreamGateEntry"] = []

    @property
    def stream_gate(self) -> List["SwitchStreamGateEntry"]:
        """Get streamGate (Pythonic accessor)."""
        return self._streamGate
        # Collection of switch stream identification entries.
        # Tags: atp.
        # Status=candidate (ordered).
        self._switchStream: List["SwitchStream"] = []

    @property
    def switch_stream(self) -> List["SwitchStream"]:
        """Get switchStream (Pythonic accessor)."""
        return self._switchStream
        # Collection of Traffic Shaper Groups.
        # Tags: atp.
        # Status=candidate Entry.
        self._trafficShaper: List["SwitchAsynchronous"] = []

    @property
    def traffic_shaper(self) -> List["SwitchAsynchronous"]:
        """Get trafficShaper (Pythonic accessor)."""
        return self._trafficShaper

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFlowMetering(self) -> List["SwitchFlowMetering"]:
        """
        AUTOSAR-compliant getter for flowMetering.

        Returns:
            The flowMetering value

        Note:
            Delegates to flow_metering property (CODING_RULE_V2_00017)
        """
        return self.flow_metering  # Delegates to property

    def getStreamFilter(self) -> List["SwitchStreamFilterEntry"]:
        """
        AUTOSAR-compliant getter for streamFilter.

        Returns:
            The streamFilter value

        Note:
            Delegates to stream_filter property (CODING_RULE_V2_00017)
        """
        return self.stream_filter  # Delegates to property

    def getStreamGate(self) -> List["SwitchStreamGateEntry"]:
        """
        AUTOSAR-compliant getter for streamGate.

        Returns:
            The streamGate value

        Note:
            Delegates to stream_gate property (CODING_RULE_V2_00017)
        """
        return self.stream_gate  # Delegates to property

    def getSwitchStream(self) -> List["SwitchStream"]:
        """
        AUTOSAR-compliant getter for switchStream.

        Returns:
            The switchStream value

        Note:
            Delegates to switch_stream property (CODING_RULE_V2_00017)
        """
        return self.switch_stream  # Delegates to property

    def getTrafficShaper(self) -> List["SwitchAsynchronous"]:
        """
        AUTOSAR-compliant getter for trafficShaper.

        Returns:
            The trafficShaper value

        Note:
            Delegates to traffic_shaper property (CODING_RULE_V2_00017)
        """
        return self.traffic_shaper  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
