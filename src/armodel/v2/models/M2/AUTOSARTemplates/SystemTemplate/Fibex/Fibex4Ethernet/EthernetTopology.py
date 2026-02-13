"""
AUTOSAR Package - EthernetTopology

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
"""
from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    Ip4AddressString,
    Ip6AddressString,
    PositiveInteger,
    RefType,
    String,
    UriString,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Describable,
    Identifiable,
    Referrable,
)
    FibexElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommunicationConnector,
    PhysicalChannel,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
    TimeValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    AbstractCanPhysicalChannel,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    SoAdConfig,
)



class EthernetPhysicalChannel(PhysicalChannel):
    """
    The EthernetPhysicalChannel represents a VLAN or an untagged channel. An
    untagged channel is modeled as an EthernetPhysicalChannel without an
    aggregated VLAN.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthernetPhysicalChannel

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 314, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 105, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of NetworkEndpoints that are used in the VLan.
        # atpSplitable.
        self._network: List[NetworkEndpoint] = []

    @property
    def network(self) -> List[NetworkEndpoint]:
        """Get network (Pythonic accessor)."""
        return self._network
        # SoAd Configuration for one specific Physical Channel.
        self._soAdConfig: Optional[SoAdConfig] = None

    @property
    def so_ad_config(self) -> Optional[SoAdConfig]:
        """Get soAdConfig (Pythonic accessor)."""
        return self._soAdConfig

    @so_ad_config.setter
    def so_ad_config(self, value: Optional[SoAdConfig]) -> None:
        """
        Set soAdConfig with validation.

        Args:
            value: The soAdConfig to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._soAdConfig = None
            return

        if not isinstance(value, SoAdConfig):
            raise TypeError(
                f"soAdConfig must be SoAdConfig or None, got {type(value).__name__}"
            )
        self._soAdConfig = value
        self._vlan: Optional[VlanConfig] = None

    @property
    def vlan(self) -> Optional[VlanConfig]:
        """Get vlan (Pythonic accessor)."""
        return self._vlan

    @vlan.setter
    def vlan(self, value: Optional[VlanConfig]) -> None:
        """
        Set vlan with validation.

        Args:
            value: The vlan to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlan = None
            return

        if not isinstance(value, VlanConfig):
            raise TypeError(
                f"vlan must be VlanConfig or None, got {type(value).__name__}"
            )
        self._vlan = value

    def with_network(self, value):
        """
        Set network and return self for chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network("value")
        """
        self.network = value  # Use property setter (gets validation)
        return self

    def with_firewall_rule(self, value):
        """
        Set firewall_rule and return self for chaining.

        Args:
            value: The firewall_rule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_firewall_rule("value")
        """
        self.firewall_rule = value  # Use property setter (gets validation)
        return self

    def with_mac_sec_props(self, value):
        """
        Set mac_sec_props and return self for chaining.

        Args:
            value: The mac_sec_props to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mac_sec_props("value")
        """
        self.mac_sec_props = value  # Use property setter (gets validation)
        return self

    def with_pnc_mapping(self, value):
        """
        Set pnc_mapping and return self for chaining.

        Args:
            value: The pnc_mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pnc_mapping("value")
        """
        self.pnc_mapping = value  # Use property setter (gets validation)
        return self

    def with_node_port(self, value):
        """
        Set node_port and return self for chaining.

        Args:
            value: The node_port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_node_port("value")
        """
        self.node_port = value  # Use property setter (gets validation)
        return self

    def with_rate_policy(self, value):
        """
        Set rate_policy and return self for chaining.

        Args:
            value: The rate_policy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rate_policy("value")
        """
        self.rate_policy = value  # Use property setter (gets validation)
        return self

    def with_v_lan(self, value):
        """
        Set v_lan and return self for chaining.

        Args:
            value: The v_lan to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_v_lan("value")
        """
        self.v_lan = value  # Use property setter (gets validation)
        return self

    def with_dns_server(self, value):
        """
        Set dns_server and return self for chaining.

        Args:
            value: The dns_server to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dns_server("value")
        """
        self.dns_server = value  # Use property setter (gets validation)
        return self

    def with_dns_server(self, value):
        """
        Set dns_server and return self for chaining.

        Args:
            value: The dns_server to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dns_server("value")
        """
        self.dns_server = value  # Use property setter (gets validation)
        return self

    def with_egress_port(self, value):
        """
        Set egress_port and return self for chaining.

        Args:
            value: The egress_port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_egress_port("value")
        """
        self.egress_port = value  # Use property setter (gets validation)
        return self

    def with_ingress_port(self, value):
        """
        Set ingress_port and return self for chaining.

        Args:
            value: The ingress_port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ingress_port("value")
        """
        self.ingress_port = value  # Use property setter (gets validation)
        return self

    def with_destination_port(self, value):
        """
        Set destination_port and return self for chaining.

        Args:
            value: The destination_port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_port("value")
        """
        self.destination_port = value  # Use property setter (gets validation)
        return self

    def with_source_port(self, value):
        """
        Set source_port and return self for chaining.

        Args:
            value: The source_port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source_port("value")
        """
        self.source_port = value  # Use property setter (gets validation)
        return self

    def with_egress_port(self, value):
        """
        Set egress_port and return self for chaining.

        Args:
            value: The egress_port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_egress_port("value")
        """
        self.egress_port = value  # Use property setter (gets validation)
        return self

    def with_ethernet(self, value):
        """
        Set ethernet and return self for chaining.

        Args:
            value: The ethernet to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ethernet("value")
        """
        self.ethernet = value  # Use property setter (gets validation)
        return self

    def with_consumed(self, value):
        """
        Set consumed and return self for chaining.

        Args:
            value: The consumed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_consumed("value")
        """
        self.consumed = value  # Use property setter (gets validation)
        return self

    def with_provided_service(self, value):
        """
        Set provided_service and return self for chaining.

        Args:
            value: The provided_service to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provided_service("value")
        """
        self.provided_service = value  # Use property setter (gets validation)
        return self

    def with_network(self, value):
        """
        Set network and return self for chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network("value")
        """
        self.network = value  # Use property setter (gets validation)
        return self

    def with_ordered_master(self, value):
        """
        Set ordered_master and return self for chaining.

        Args:
            value: The ordered_master to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ordered_master("value")
        """
        self.ordered_master = value  # Use property setter (gets validation)
        return self

    def with_predecessor(self, value):
        """
        Set predecessor and return self for chaining.

        Args:
            value: The predecessor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_predecessor("value")
        """
        self.predecessor = value  # Use property setter (gets validation)
        return self

    def with_switch_stream(self, value):
        """
        Set switch_stream and return self for chaining.

        Args:
            value: The switch_stream to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_switch_stream("value")
        """
        self.switch_stream = value  # Use property setter (gets validation)
        return self

    def with_dns_server(self, value):
        """
        Set dns_server and return self for chaining.

        Args:
            value: The dns_server to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dns_server("value")
        """
        self.dns_server = value  # Use property setter (gets validation)
        return self

    def with_dns_server(self, value):
        """
        Set dns_server and return self for chaining.

        Args:
            value: The dns_server to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dns_server("value")
        """
        self.dns_server = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNetwork(self) -> List[NetworkEndpoint]:
        """
        AUTOSAR-compliant getter for network.

        Returns:
            The network value

        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def getSoAdConfig(self) -> "SoAdConfig":
        """
        AUTOSAR-compliant getter for soAdConfig.

        Returns:
            The soAdConfig value

        Note:
            Delegates to so_ad_config property (CODING_RULE_V2_00017)
        """
        return self.so_ad_config  # Delegates to property

    def setSoAdConfig(self, value: "SoAdConfig") -> EthernetPhysicalChannel:
        """
        AUTOSAR-compliant setter for soAdConfig with method chaining.

        Args:
            value: The soAdConfig to set

        Returns:
            self for method chaining

        Note:
            Delegates to so_ad_config property setter (gets validation automatically)
        """
        self.so_ad_config = value  # Delegates to property setter
        return self

    def getVlan(self) -> VlanConfig:
        """
        AUTOSAR-compliant getter for vlan.

        Returns:
            The vlan value

        Note:
            Delegates to vlan property (CODING_RULE_V2_00017)
        """
        return self.vlan  # Delegates to property

    def setVlan(self, value: VlanConfig) -> EthernetPhysicalChannel:
        """
        AUTOSAR-compliant setter for vlan with method chaining.

        Args:
            value: The vlan to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan property setter (gets validation automatically)
        """
        self.vlan = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_so_ad_config(self, value: Optional[SoAdConfig]) -> EthernetPhysicalChannel:
        """
        Set soAdConfig and return self for chaining.

        Args:
            value: The soAdConfig to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_so_ad_config("value")
        """
        self.so_ad_config = value  # Use property setter (gets validation)
        return self

    def with_vlan(self, value: Optional[VlanConfig]) -> EthernetPhysicalChannel:
        """
        Set vlan and return self for chaining.

        Args:
            value: The vlan to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan("value")
        """
        self.vlan = value  # Use property setter (gets validation)
        return self



class EthernetCluster(ARObject):
    """
    Ethernet-specific cluster attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthernetCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 103, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Switch off delay for CouplingPorts in seconds.
        # It denotes delay of switching off couplingPorts after the request off a
                # couplingPort was issued.
        # (e.
        # g.
        # switch off of ports).
        self._couplingPort: Optional[TimeValue] = None

    @property
    def coupling_port(self) -> Optional[TimeValue]:
        """Get couplingPort (Pythonic accessor)."""
        return self._couplingPort

    @coupling_port.setter
    def coupling_port(self, value: Optional[TimeValue]) -> None:
        """
        Set couplingPort with validation.

        Args:
            value: The couplingPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._couplingPort = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"couplingPort must be TimeValue or None, got {type(value).__name__}"
            )
        self._couplingPort = value
        self._macMulticast: List[RefType] = []

    @property
    def mac_multicast(self) -> List[RefType]:
        """Get macMulticast (Pythonic accessor)."""
        return self._macMulticast

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCouplingPort(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for couplingPort.

        Returns:
            The couplingPort value

        Note:
            Delegates to coupling_port property (CODING_RULE_V2_00017)
        """
        return self.coupling_port  # Delegates to property

    def setCouplingPort(self, value: TimeValue) -> EthernetCluster:
        """
        AUTOSAR-compliant setter for couplingPort with method chaining.

        Args:
            value: The couplingPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to coupling_port property setter (gets validation automatically)
        """
        self.coupling_port = value  # Delegates to property setter
        return self

    def getMacMulticast(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for macMulticast.

        Returns:
            The macMulticast value

        Note:
            Delegates to mac_multicast property (CODING_RULE_V2_00017)
        """
        return self.mac_multicast  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_coupling_port(self, value: Optional[TimeValue]) -> EthernetCluster:
        """
        Set couplingPort and return self for chaining.

        Args:
            value: The couplingPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_coupling_port("value")
        """
        self.coupling_port = value  # Use property setter (gets validation)
        return self



class MacMulticastGroup(Identifiable):
    """
    Per EthernetCluster globally defined MacMulticastGroup. One sender can
    handle many receivers simultaneously if the receivers have all the same
    macMulticastAddress. The addresses need to be unique for the particular
    EthernetCluster.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::MacMulticastGroup

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 103, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A multicast MAC address (Media Access Control is a identifier for a group of
        # hosts in a network.
        self._macMulticast: Optional[MacAddressString] = None

    @property
    def mac_multicast(self) -> Optional[MacAddressString]:
        """Get macMulticast (Pythonic accessor)."""
        return self._macMulticast

    @mac_multicast.setter
    def mac_multicast(self, value: Optional[MacAddressString]) -> None:
        """
        Set macMulticast with validation.

        Args:
            value: The macMulticast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macMulticast = None
            return

        if not isinstance(value, MacAddressString):
            raise TypeError(
                f"macMulticast must be MacAddressString or None, got {type(value).__name__}"
            )
        self._macMulticast = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMacMulticast(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for macMulticast.

        Returns:
            The macMulticast value

        Note:
            Delegates to mac_multicast property (CODING_RULE_V2_00017)
        """
        return self.mac_multicast  # Delegates to property

    def setMacMulticast(self, value: "MacAddressString") -> MacMulticastGroup:
        """
        AUTOSAR-compliant setter for macMulticast with method chaining.

        Args:
            value: The macMulticast to set

        Returns:
            self for method chaining

        Note:
            Delegates to mac_multicast property setter (gets validation automatically)
        """
        self.mac_multicast = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mac_multicast(self, value: Optional[MacAddressString]) -> MacMulticastGroup:
        """
        Set macMulticast and return self for chaining.

        Args:
            value: The macMulticast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mac_multicast("value")
        """
        self.mac_multicast = value  # Use property setter (gets validation)
        return self



class VlanConfig(Identifiable):
    """
    VLAN Configuration attributes

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::VlanConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 106, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A VLAN is identified by this attribute according to IEEE allowed values range
                # is from 0.
        # 4095.
        self._vlanIdentifier: Optional[PositiveInteger] = None

    @property
    def vlan_identifier(self) -> Optional[PositiveInteger]:
        """Get vlanIdentifier (Pythonic accessor)."""
        return self._vlanIdentifier

    @vlan_identifier.setter
    def vlan_identifier(self, value: Optional[PositiveInteger]) -> None:
        """
        Set vlanIdentifier with validation.

        Args:
            value: The vlanIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlanIdentifier = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"vlanIdentifier must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._vlanIdentifier = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getVlanIdentifier(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for vlanIdentifier.

        Returns:
            The vlanIdentifier value

        Note:
            Delegates to vlan_identifier property (CODING_RULE_V2_00017)
        """
        return self.vlan_identifier  # Delegates to property

    def setVlanIdentifier(self, value: PositiveInteger) -> VlanConfig:
        """
        AUTOSAR-compliant setter for vlanIdentifier with method chaining.

        Args:
            value: The vlanIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan_identifier property setter (gets validation automatically)
        """
        self.vlan_identifier = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_vlan_identifier(self, value: Optional[PositiveInteger]) -> VlanConfig:
        """
        Set vlanIdentifier and return self for chaining.

        Args:
            value: The vlanIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan_identifier("value")
        """
        self.vlan_identifier = value  # Use property setter (gets validation)
        return self



class CouplingElement(FibexElement):
    """
    A CouplingElement is used to connect EcuInstances to the VLAN of an
    EthernetCluster. Coupling Elements can reach from a simple hub to a complex
    managed switch or even devices with functionalities in higher layers. A
    CouplingElement that is not related to an EcuInstance occurs as a dedicated
    single device.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingElement

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 107, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This relationship defines to which cluster the Coupling belongs.
        self._communication: Optional[EthernetCluster] = None

    @property
    def communication(self) -> Optional[EthernetCluster]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional[EthernetCluster]) -> None:
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

        if not isinstance(value, EthernetCluster):
            raise TypeError(
                f"communication must be EthernetCluster or None, got {type(value).__name__}"
            )
        self._communication = value
        # Stereotypes: atpSplitable; atpVariation 2090 Document ID 63:
                # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._coupling: Optional[CouplingElement] = None

    @property
    def coupling(self) -> Optional[CouplingElement]:
        """Get coupling (Pythonic accessor)."""
        return self._coupling

    @coupling.setter
    def coupling(self, value: Optional[CouplingElement]) -> None:
        """
        Set coupling with validation.

        Args:
            value: The coupling to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._coupling = None
            return

        if not isinstance(value, CouplingElement):
            raise TypeError(
                f"coupling must be CouplingElement or None, got {type(value).__name__}"
            )
        self._coupling = value
        # EcuInstances or other atpVariation.
        self._couplingPort: List[CouplingPort] = []

    @property
    def coupling_port(self) -> List[CouplingPort]:
        """Get couplingPort (Pythonic accessor)."""
        return self._couplingPort
        # Describes the coupling type of this CouplingElement.
        self._couplingType: Optional[CouplingElementEnum] = None

    @property
    def coupling_type(self) -> Optional[CouplingElementEnum]:
        """Get couplingType (Pythonic accessor)."""
        return self._couplingType

    @coupling_type.setter
    def coupling_type(self, value: Optional[CouplingElementEnum]) -> None:
        """
        Set couplingType with validation.

        Args:
            value: The couplingType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._couplingType = None
            return

        if not isinstance(value, CouplingElementEnum):
            raise TypeError(
                f"couplingType must be CouplingElementEnum or None, got {type(value).__name__}"
            )
        self._couplingType = value
        self._ecuInstance: Optional[EcuInstance] = None

    @property
    def ecu_instance(self) -> Optional[EcuInstance]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional[EcuInstance]) -> None:
        """
        Set ecuInstance with validation.

        Args:
            value: The ecuInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuInstance = None
            return

        if not isinstance(value, EcuInstance):
            raise TypeError(
                f"ecuInstance must be EcuInstance or None, got {type(value).__name__}"
            )
        self._ecuInstance = value
        self._firewallRule: List["StateDependentFirewall"] = []

    @property
    def firewall_rule(self) -> List["StateDependentFirewall"]:
        """Get firewallRule (Pythonic accessor)."""
        return self._firewallRule

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> EthernetCluster:
        """
        AUTOSAR-compliant getter for communication.

        Returns:
            The communication value

        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: EthernetCluster) -> CouplingElement:
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

    def getCoupling(self) -> CouplingElement:
        """
        AUTOSAR-compliant getter for coupling.

        Returns:
            The coupling value

        Note:
            Delegates to coupling property (CODING_RULE_V2_00017)
        """
        return self.coupling  # Delegates to property

    def setCoupling(self, value: CouplingElement) -> CouplingElement:
        """
        AUTOSAR-compliant setter for coupling with method chaining.

        Args:
            value: The coupling to set

        Returns:
            self for method chaining

        Note:
            Delegates to coupling property setter (gets validation automatically)
        """
        self.coupling = value  # Delegates to property setter
        return self

    def getCouplingPort(self) -> List[CouplingPort]:
        """
        AUTOSAR-compliant getter for couplingPort.

        Returns:
            The couplingPort value

        Note:
            Delegates to coupling_port property (CODING_RULE_V2_00017)
        """
        return self.coupling_port  # Delegates to property

    def getCouplingType(self) -> CouplingElementEnum:
        """
        AUTOSAR-compliant getter for couplingType.

        Returns:
            The couplingType value

        Note:
            Delegates to coupling_type property (CODING_RULE_V2_00017)
        """
        return self.coupling_type  # Delegates to property

    def setCouplingType(self, value: CouplingElementEnum) -> CouplingElement:
        """
        AUTOSAR-compliant setter for couplingType with method chaining.

        Args:
            value: The couplingType to set

        Returns:
            self for method chaining

        Note:
            Delegates to coupling_type property setter (gets validation automatically)
        """
        self.coupling_type = value  # Delegates to property setter
        return self

    def getEcuInstance(self) -> EcuInstance:
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: EcuInstance) -> CouplingElement:
        """
        AUTOSAR-compliant setter for ecuInstance with method chaining.

        Args:
            value: The ecuInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_instance property setter (gets validation automatically)
        """
        self.ecu_instance = value  # Delegates to property setter
        return self

    def getFirewallRule(self) -> List["StateDependentFirewall"]:
        """
        AUTOSAR-compliant getter for firewallRule.

        Returns:
            The firewallRule value

        Note:
            Delegates to firewall_rule property (CODING_RULE_V2_00017)
        """
        return self.firewall_rule  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional[EthernetCluster]) -> CouplingElement:
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

    def with_coupling(self, value: Optional[CouplingElement]) -> CouplingElement:
        """
        Set coupling and return self for chaining.

        Args:
            value: The coupling to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_coupling("value")
        """
        self.coupling = value  # Use property setter (gets validation)
        return self

    def with_coupling_type(self, value: Optional[CouplingElementEnum]) -> CouplingElement:
        """
        Set couplingType and return self for chaining.

        Args:
            value: The couplingType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_coupling_type("value")
        """
        self.coupling_type = value  # Use property setter (gets validation)
        return self

    def with_ecu_instance(self, value: Optional[EcuInstance]) -> CouplingElement:
        """
        Set ecuInstance and return self for chaining.

        Args:
            value: The ecuInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_instance("value")
        """
        self.ecu_instance = value  # Use property setter (gets validation)
        return self



class CouplingPort(Identifiable):
    """
    A CouplingPort is used to connect a CouplingElement with an EcuInstance or
    two CouplingElements with each other via a CouplingPortConnection.
    Optionally, the CouplingPort may also have a reference to a
    macMulticastGroup and a defaultVLAN.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPort

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 109, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the connection negotiation of the CouplingPort.
        self._connection: Optional[EthernetConnection] = None

    @property
    def connection(self) -> Optional[EthernetConnection]:
        """Get connection (Pythonic accessor)."""
        return self._connection

    @connection.setter
    def connection(self, value: Optional[EthernetConnection]) -> None:
        """
        Set connection with validation.

        Args:
            value: The connection to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._connection = None
            return

        if not isinstance(value, EthernetConnection):
            raise TypeError(
                f"connection must be EthernetConnection or None, got {type(value).__name__}"
            )
        self._connection = value
        self._couplingPort: Optional[CouplingPortRoleEnum] = None

    @property
    def coupling_port(self) -> Optional[CouplingPortRoleEnum]:
        """Get couplingPort (Pythonic accessor)."""
        return self._couplingPort

    @coupling_port.setter
    def coupling_port(self, value: Optional[CouplingPortRoleEnum]) -> None:
        """
        Set couplingPort with validation.

        Args:
            value: The couplingPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._couplingPort = None
            return

        if not isinstance(value, CouplingPortRoleEnum):
            raise TypeError(
                f"couplingPort must be CouplingPortRoleEnum or None, got {type(value).__name__}"
            )
        self._couplingPort = value
        # A Port VLAN ID is a default that is assigned to an access CouplingPort to
                # VLAN segment to which this port is if a CouplingPort has not been any VLAN
                # memberships, the virtual VLAN ID (pvid) becomes the default VLAN the ports
                # connection.
        # is added for incoming untagged the port (ingress tagging).
        # For outgoing this identifier, the tag is removed at the untagging, depending
                # on the Vlan.
        self._defaultVlan: Optional[EthernetPhysical] = None

    @property
    def default_vlan(self) -> Optional[EthernetPhysical]:
        """Get defaultVlan (Pythonic accessor)."""
        return self._defaultVlan

    @default_vlan.setter
    def default_vlan(self, value: Optional[EthernetPhysical]) -> None:
        """
        Set defaultVlan with validation.

        Args:
            value: The defaultVlan to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultVlan = None
            return

        if not isinstance(value, EthernetPhysical):
            raise TypeError(
                f"defaultVlan must be EthernetPhysical or None, got {type(value).__name__}"
            )
        self._defaultVlan = value
        self._macLayerTypeEnum: Optional[EthernetMacLayerType] = None

    @property
    def mac_layer_type_enum(self) -> Optional[EthernetMacLayerType]:
        """Get macLayerTypeEnum (Pythonic accessor)."""
        return self._macLayerTypeEnum

    @mac_layer_type_enum.setter
    def mac_layer_type_enum(self, value: Optional[EthernetMacLayerType]) -> None:
        """
        Set macLayerTypeEnum with validation.

        Args:
            value: The macLayerTypeEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macLayerTypeEnum = None
            return

        if not isinstance(value, EthernetMacLayerType):
            raise TypeError(
                f"macLayerTypeEnum must be EthernetMacLayerType or None, got {type(value).__name__}"
            )
        self._macLayerTypeEnum = value
        # This is a static further addresses may be learned.
        self._macMulticast: List[RefType] = []

    @property
    def mac_multicast(self) -> List[RefType]:
        """Get macMulticast (Pythonic accessor)."""
        return self._macMulticast
        # Properties to configure MACsec (Media access control the MKA (MACsec Key
        # Agreement) for the.
        self._macSecProps: List["MacSecProps"] = []

    @property
    def mac_sec_props(self) -> List["MacSecProps"]:
        """Get macSecProps (Pythonic accessor)."""
        return self._macSecProps
        # Specifies the physical layer type of the CouplingPort.
        self._physicalLayer: Optional[EthernetPhysicalLayer] = None

    @property
    def physical_layer(self) -> Optional[EthernetPhysicalLayer]:
        """Get physicalLayer (Pythonic accessor)."""
        return self._physicalLayer

    @physical_layer.setter
    def physical_layer(self, value: Optional[EthernetPhysicalLayer]) -> None:
        """
        Set physicalLayer with validation.

        Args:
            value: The physicalLayer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physicalLayer = None
            return

        if not isinstance(value, EthernetPhysicalLayer):
            raise TypeError(
                f"physicalLayer must be EthernetPhysicalLayer or None, got {type(value).__name__}"
            )
        self._physicalLayer = value
        # 10-BASE-T1S used and PLCA is enabled on the Coupling.
        self._plcaProps: Optional[PlcaProps] = None

    @property
    def plca_props(self) -> Optional[PlcaProps]:
        """Get plcaProps (Pythonic accessor)."""
        return self._plcaProps

    @plca_props.setter
    def plca_props(self, value: Optional[PlcaProps]) -> None:
        """
        Set plcaProps with validation.

        Args:
            value: The plcaProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._plcaProps = None
            return

        if not isinstance(value, PlcaProps):
            raise TypeError(
                f"plcaProps must be PlcaProps or None, got {type(value).__name__}"
            )
        self._plcaProps = value
        self._pncMapping: List[RefType] = []

    @property
    def pnc_mapping(self) -> List[RefType]:
        """Get pncMapping (Pythonic accessor)."""
        return self._pncMapping
        # Defines the handling of frames at the ingress port.
        self._receiveActivity: Optional[EthernetSwitchVlan] = None

    @property
    def receive_activity(self) -> Optional[EthernetSwitchVlan]:
        """Get receiveActivity (Pythonic accessor)."""
        return self._receiveActivity

    @receive_activity.setter
    def receive_activity(self, value: Optional[EthernetSwitchVlan]) -> None:
        """
        Set receiveActivity with validation.

        Args:
            value: The receiveActivity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._receiveActivity = None
            return

        if not isinstance(value, EthernetSwitchVlan):
            raise TypeError(
                f"receiveActivity must be EthernetSwitchVlan or None, got {type(value).__name__}"
            )
        self._receiveActivity = value
        self._vlan: List[VlanMembership] = []

    @property
    def vlan(self) -> List[VlanMembership]:
        """Get vlan (Pythonic accessor)."""
        return self._vlan
        # All incoming messages at this CouplingPort shall be with this VLAN Id.
        # This tagging is performed the message already has a VLAN tag untagged, an
                # existing VLAN tag will be overwritten.
        # is XOR with CoupligPort.
        # defaultVlan.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._vlanModifier: Optional[EthernetPhysical] = None

    @property
    def vlan_modifier(self) -> Optional[EthernetPhysical]:
        """Get vlanModifier (Pythonic accessor)."""
        return self._vlanModifier

    @vlan_modifier.setter
    def vlan_modifier(self, value: Optional[EthernetPhysical]) -> None:
        """
        Set vlanModifier with validation.

        Args:
            value: The vlanModifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlanModifier = None
            return

        if not isinstance(value, EthernetPhysical):
            raise TypeError(
                f"vlanModifier must be EthernetPhysical or None, got {type(value).__name__}"
            )
        self._vlanModifier = value
        self._wakeupSleep: Optional[EthernetWakeupSleep] = None

    @property
    def wakeup_sleep(self) -> Optional[EthernetWakeupSleep]:
        """Get wakeupSleep (Pythonic accessor)."""
        return self._wakeupSleep

    @wakeup_sleep.setter
    def wakeup_sleep(self, value: Optional[EthernetWakeupSleep]) -> None:
        """
        Set wakeupSleep with validation.

        Args:
            value: The wakeupSleep to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeupSleep = None
            return

        if not isinstance(value, EthernetWakeupSleep):
            raise TypeError(
                f"wakeupSleep must be EthernetWakeupSleep or None, got {type(value).__name__}"
            )
        self._wakeupSleep = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnection(self) -> EthernetConnection:
        """
        AUTOSAR-compliant getter for connection.

        Returns:
            The connection value

        Note:
            Delegates to connection property (CODING_RULE_V2_00017)
        """
        return self.connection  # Delegates to property

    def setConnection(self, value: EthernetConnection) -> CouplingPort:
        """
        AUTOSAR-compliant setter for connection with method chaining.

        Args:
            value: The connection to set

        Returns:
            self for method chaining

        Note:
            Delegates to connection property setter (gets validation automatically)
        """
        self.connection = value  # Delegates to property setter
        return self

    def getCouplingPort(self) -> CouplingPortRoleEnum:
        """
        AUTOSAR-compliant getter for couplingPort.

        Returns:
            The couplingPort value

        Note:
            Delegates to coupling_port property (CODING_RULE_V2_00017)
        """
        return self.coupling_port  # Delegates to property

    def setCouplingPort(self, value: CouplingPortRoleEnum) -> CouplingPort:
        """
        AUTOSAR-compliant setter for couplingPort with method chaining.

        Args:
            value: The couplingPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to coupling_port property setter (gets validation automatically)
        """
        self.coupling_port = value  # Delegates to property setter
        return self

    def getDefaultVlan(self) -> EthernetPhysical:
        """
        AUTOSAR-compliant getter for defaultVlan.

        Returns:
            The defaultVlan value

        Note:
            Delegates to default_vlan property (CODING_RULE_V2_00017)
        """
        return self.default_vlan  # Delegates to property

    def setDefaultVlan(self, value: EthernetPhysical) -> CouplingPort:
        """
        AUTOSAR-compliant setter for defaultVlan with method chaining.

        Args:
            value: The defaultVlan to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_vlan property setter (gets validation automatically)
        """
        self.default_vlan = value  # Delegates to property setter
        return self

    def getMacLayerTypeEnum(self) -> EthernetMacLayerType:
        """
        AUTOSAR-compliant getter for macLayerTypeEnum.

        Returns:
            The macLayerTypeEnum value

        Note:
            Delegates to mac_layer_type_enum property (CODING_RULE_V2_00017)
        """
        return self.mac_layer_type_enum  # Delegates to property

    def setMacLayerTypeEnum(self, value: EthernetMacLayerType) -> CouplingPort:
        """
        AUTOSAR-compliant setter for macLayerTypeEnum with method chaining.

        Args:
            value: The macLayerTypeEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to mac_layer_type_enum property setter (gets validation automatically)
        """
        self.mac_layer_type_enum = value  # Delegates to property setter
        return self

    def getMacMulticast(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for macMulticast.

        Returns:
            The macMulticast value

        Note:
            Delegates to mac_multicast property (CODING_RULE_V2_00017)
        """
        return self.mac_multicast  # Delegates to property

    def getMacSecProps(self) -> List["MacSecProps"]:
        """
        AUTOSAR-compliant getter for macSecProps.

        Returns:
            The macSecProps value

        Note:
            Delegates to mac_sec_props property (CODING_RULE_V2_00017)
        """
        return self.mac_sec_props  # Delegates to property

    def getPhysicalLayer(self) -> EthernetPhysicalLayer:
        """
        AUTOSAR-compliant getter for physicalLayer.

        Returns:
            The physicalLayer value

        Note:
            Delegates to physical_layer property (CODING_RULE_V2_00017)
        """
        return self.physical_layer  # Delegates to property

    def setPhysicalLayer(self, value: EthernetPhysicalLayer) -> CouplingPort:
        """
        AUTOSAR-compliant setter for physicalLayer with method chaining.

        Args:
            value: The physicalLayer to set

        Returns:
            self for method chaining

        Note:
            Delegates to physical_layer property setter (gets validation automatically)
        """
        self.physical_layer = value  # Delegates to property setter
        return self

    def getPlcaProps(self) -> PlcaProps:
        """
        AUTOSAR-compliant getter for plcaProps.

        Returns:
            The plcaProps value

        Note:
            Delegates to plca_props property (CODING_RULE_V2_00017)
        """
        return self.plca_props  # Delegates to property

    def setPlcaProps(self, value: PlcaProps) -> CouplingPort:
        """
        AUTOSAR-compliant setter for plcaProps with method chaining.

        Args:
            value: The plcaProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to plca_props property setter (gets validation automatically)
        """
        self.plca_props = value  # Delegates to property setter
        return self

    def getPncMapping(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for pncMapping.

        Returns:
            The pncMapping value

        Note:
            Delegates to pnc_mapping property (CODING_RULE_V2_00017)
        """
        return self.pnc_mapping  # Delegates to property

    def getReceiveActivity(self) -> EthernetSwitchVlan:
        """
        AUTOSAR-compliant getter for receiveActivity.

        Returns:
            The receiveActivity value

        Note:
            Delegates to receive_activity property (CODING_RULE_V2_00017)
        """
        return self.receive_activity  # Delegates to property

    def setReceiveActivity(self, value: EthernetSwitchVlan) -> CouplingPort:
        """
        AUTOSAR-compliant setter for receiveActivity with method chaining.

        Args:
            value: The receiveActivity to set

        Returns:
            self for method chaining

        Note:
            Delegates to receive_activity property setter (gets validation automatically)
        """
        self.receive_activity = value  # Delegates to property setter
        return self

    def getVlan(self) -> List[VlanMembership]:
        """
        AUTOSAR-compliant getter for vlan.

        Returns:
            The vlan value

        Note:
            Delegates to vlan property (CODING_RULE_V2_00017)
        """
        return self.vlan  # Delegates to property

    def getVlanModifier(self) -> EthernetPhysical:
        """
        AUTOSAR-compliant getter for vlanModifier.

        Returns:
            The vlanModifier value

        Note:
            Delegates to vlan_modifier property (CODING_RULE_V2_00017)
        """
        return self.vlan_modifier  # Delegates to property

    def setVlanModifier(self, value: EthernetPhysical) -> CouplingPort:
        """
        AUTOSAR-compliant setter for vlanModifier with method chaining.

        Args:
            value: The vlanModifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan_modifier property setter (gets validation automatically)
        """
        self.vlan_modifier = value  # Delegates to property setter
        return self

    def getWakeupSleep(self) -> EthernetWakeupSleep:
        """
        AUTOSAR-compliant getter for wakeupSleep.

        Returns:
            The wakeupSleep value

        Note:
            Delegates to wakeup_sleep property (CODING_RULE_V2_00017)
        """
        return self.wakeup_sleep  # Delegates to property

    def setWakeupSleep(self, value: EthernetWakeupSleep) -> CouplingPort:
        """
        AUTOSAR-compliant setter for wakeupSleep with method chaining.

        Args:
            value: The wakeupSleep to set

        Returns:
            self for method chaining

        Note:
            Delegates to wakeup_sleep property setter (gets validation automatically)
        """
        self.wakeup_sleep = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_connection(self, value: Optional[EthernetConnection]) -> CouplingPort:
        """
        Set connection and return self for chaining.

        Args:
            value: The connection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_connection("value")
        """
        self.connection = value  # Use property setter (gets validation)
        return self

    def with_coupling_port(self, value: Optional[CouplingPortRoleEnum]) -> CouplingPort:
        """
        Set couplingPort and return self for chaining.

        Args:
            value: The couplingPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_coupling_port("value")
        """
        self.coupling_port = value  # Use property setter (gets validation)
        return self

    def with_default_vlan(self, value: Optional[EthernetPhysical]) -> CouplingPort:
        """
        Set defaultVlan and return self for chaining.

        Args:
            value: The defaultVlan to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_vlan("value")
        """
        self.default_vlan = value  # Use property setter (gets validation)
        return self

    def with_mac_layer_type_enum(self, value: Optional[EthernetMacLayerType]) -> CouplingPort:
        """
        Set macLayerTypeEnum and return self for chaining.

        Args:
            value: The macLayerTypeEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mac_layer_type_enum("value")
        """
        self.mac_layer_type_enum = value  # Use property setter (gets validation)
        return self

    def with_physical_layer(self, value: Optional[EthernetPhysicalLayer]) -> CouplingPort:
        """
        Set physicalLayer and return self for chaining.

        Args:
            value: The physicalLayer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_physical_layer("value")
        """
        self.physical_layer = value  # Use property setter (gets validation)
        return self

    def with_plca_props(self, value: Optional[PlcaProps]) -> CouplingPort:
        """
        Set plcaProps and return self for chaining.

        Args:
            value: The plcaProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_plca_props("value")
        """
        self.plca_props = value  # Use property setter (gets validation)
        return self

    def with_receive_activity(self, value: Optional[EthernetSwitchVlan]) -> CouplingPort:
        """
        Set receiveActivity and return self for chaining.

        Args:
            value: The receiveActivity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_receive_activity("value")
        """
        self.receive_activity = value  # Use property setter (gets validation)
        return self

    def with_vlan_modifier(self, value: Optional[EthernetPhysical]) -> CouplingPort:
        """
        Set vlanModifier and return self for chaining.

        Args:
            value: The vlanModifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan_modifier("value")
        """
        self.vlan_modifier = value  # Use property setter (gets validation)
        return self

    def with_wakeup_sleep(self, value: Optional[EthernetWakeupSleep]) -> CouplingPort:
        """
        Set wakeupSleep and return self for chaining.

        Args:
            value: The wakeupSleep to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup_sleep("value")
        """
        self.wakeup_sleep = value  # Use property setter (gets validation)
        return self



class VlanMembership(ARObject):
    """
    Static logical channel or VLAN binding to a switch-port. The reference to an
    EthernetPhysicalChannel without a VLAN defined represents the handling of
    untagged frames. (cid:53) 111 of 2090 Document ID 63:
    AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::VlanMembership

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 111, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Standard output-priority outgoing Frames will be tagged priority that
                # received frames are assigned the VLAN Id (defaultVlan).
        # The values from effort) to 7 (highest) are allowed.
        # modifyVlan and an already tagged received actual priority of the received
                # frame is not.
        self._defaultPriority: Optional[PositiveInteger] = None

    @property
    def default_priority(self) -> Optional[PositiveInteger]:
        """Get defaultPriority (Pythonic accessor)."""
        return self._defaultPriority

    @default_priority.setter
    def default_priority(self, value: Optional[PositiveInteger]) -> None:
        """
        Set defaultPriority with validation.

        Args:
            value: The defaultPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultPriority = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"defaultPriority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._defaultPriority = value
                # SwitchPort.
        # If no dhcpAddress provided all DHCP-Discover messages this Port will be
                # discarded by the DHCP.
        self._dhcpAddress: Optional[DhcpServerConfiguration] = None

    @property
    def dhcp_address(self) -> Optional[DhcpServerConfiguration]:
        """Get dhcpAddress (Pythonic accessor)."""
        return self._dhcpAddress

    @dhcp_address.setter
    def dhcp_address(self, value: Optional[DhcpServerConfiguration]) -> None:
        """
        Set dhcpAddress with validation.

        Args:
            value: The dhcpAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dhcpAddress = None
            return

        if not isinstance(value, DhcpServer):
            raise TypeError(
                f"dhcpAddress must be DhcpServer or None, got {type(value).__name__}"
            )
        self._dhcpAddress = value
        # (sentTagged) without a VLAN tag (sentUntagged) be dropped at this port
        # (notSent or VLAN not this list).
        self._sendActivity: Optional[EthernetSwitchVlan] = None

    @property
    def send_activity(self) -> Optional[EthernetSwitchVlan]:
        """Get sendActivity (Pythonic accessor)."""
        return self._sendActivity

    @send_activity.setter
    def send_activity(self, value: Optional[EthernetSwitchVlan]) -> None:
        """
        Set sendActivity with validation.

        Args:
            value: The sendActivity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sendActivity = None
            return

        if not isinstance(value, EthernetSwitchVlan):
            raise TypeError(
                f"sendActivity must be EthernetSwitchVlan or None, got {type(value).__name__}"
            )
        self._sendActivity = value
        self._vlan: Optional[EthernetPhysical] = None

    @property
    def vlan(self) -> Optional[EthernetPhysical]:
        """Get vlan (Pythonic accessor)."""
        return self._vlan

    @vlan.setter
    def vlan(self, value: Optional[EthernetPhysical]) -> None:
        """
        Set vlan with validation.

        Args:
            value: The vlan to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlan = None
            return

        if not isinstance(value, EthernetPhysical):
            raise TypeError(
                f"vlan must be EthernetPhysical or None, got {type(value).__name__}"
            )
        self._vlan = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultPriority(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for defaultPriority.

        Returns:
            The defaultPriority value

        Note:
            Delegates to default_priority property (CODING_RULE_V2_00017)
        """
        return self.default_priority  # Delegates to property

    def setDefaultPriority(self, value: PositiveInteger) -> VlanMembership:
        """
        AUTOSAR-compliant setter for defaultPriority with method chaining.

        Args:
            value: The defaultPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_priority property setter (gets validation automatically)
        """
        self.default_priority = value  # Delegates to property setter
        return self

    def getDhcpAddress(self) -> DhcpServerConfiguration:
        """
        AUTOSAR-compliant getter for dhcpAddress.

        Returns:
            The dhcpAddress value

        Note:
            Delegates to dhcp_address property (CODING_RULE_V2_00017)
        """
        return self.dhcp_address  # Delegates to property

    def setDhcpAddress(self, value: DhcpServerConfiguration) -> VlanMembership:
        """
        AUTOSAR-compliant setter for dhcpAddress with method chaining.

        Args:
            value: The dhcpAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to dhcp_address property setter (gets validation automatically)
        """
        self.dhcp_address = value  # Delegates to property setter
        return self

    def getSendActivity(self) -> EthernetSwitchVlan:
        """
        AUTOSAR-compliant getter for sendActivity.

        Returns:
            The sendActivity value

        Note:
            Delegates to send_activity property (CODING_RULE_V2_00017)
        """
        return self.send_activity  # Delegates to property

    def setSendActivity(self, value: EthernetSwitchVlan) -> VlanMembership:
        """
        AUTOSAR-compliant setter for sendActivity with method chaining.

        Args:
            value: The sendActivity to set

        Returns:
            self for method chaining

        Note:
            Delegates to send_activity property setter (gets validation automatically)
        """
        self.send_activity = value  # Delegates to property setter
        return self

    def getVlan(self) -> EthernetPhysical:
        """
        AUTOSAR-compliant getter for vlan.

        Returns:
            The vlan value

        Note:
            Delegates to vlan property (CODING_RULE_V2_00017)
        """
        return self.vlan  # Delegates to property

    def setVlan(self, value: EthernetPhysical) -> VlanMembership:
        """
        AUTOSAR-compliant setter for vlan with method chaining.

        Args:
            value: The vlan to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan property setter (gets validation automatically)
        """
        self.vlan = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_priority(self, value: Optional[PositiveInteger]) -> VlanMembership:
        """
        Set defaultPriority and return self for chaining.

        Args:
            value: The defaultPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_priority("value")
        """
        self.default_priority = value  # Use property setter (gets validation)
        return self

    def with_dhcp_address(self, value: Optional[DhcpServerConfiguration]) -> VlanMembership:
        """
        Set dhcpAddress and return self for chaining.

        Args:
            value: The dhcpAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dhcp_address("value")
        """
        self.dhcp_address = value  # Use property setter (gets validation)
        return self

    def with_send_activity(self, value: Optional[EthernetSwitchVlan]) -> VlanMembership:
        """
        Set sendActivity and return self for chaining.

        Args:
            value: The sendActivity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_send_activity("value")
        """
        self.send_activity = value  # Use property setter (gets validation)
        return self

    def with_vlan(self, value: Optional[EthernetPhysical]) -> VlanMembership:
        """
        Set vlan and return self for chaining.

        Args:
            value: The vlan to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan("value")
        """
        self.vlan = value  # Use property setter (gets validation)
        return self



class CouplingPortConnection(ARObject):
    """
    Connection between two CouplingPorts (firstPort and secondPort) or between a
    collection of Ports that are all referenced by the portCollection reference.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 112, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the first CouplingPort that is connected via 2090 Document ID
        # 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._firstPort: Optional[CouplingPort] = None

    @property
    def first_port(self) -> Optional[CouplingPort]:
        """Get firstPort (Pythonic accessor)."""
        return self._firstPort

    @first_port.setter
    def first_port(self, value: Optional[CouplingPort]) -> None:
        """
        Set firstPort with validation.

        Args:
            value: The firstPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstPort = None
            return

        if not isinstance(value, CouplingPort):
            raise TypeError(
                f"firstPort must be CouplingPort or None, got {type(value).__name__}"
            )
        self._firstPort = value
        # This be used to describe a 10BASE-T1S where several CouplingPorts of
                # connected via atpVariation.
        self._nodePort: List[CouplingPort] = []

    @property
    def node_port(self) -> List[CouplingPort]:
        """Get nodePort (Pythonic accessor)."""
        return self._nodePort
        # Defines the number of communication participants in 10BASE-T1S and the
        # nodePort reference is used.
        self._plcaLocalNode: Optional[PositiveInteger] = None

    @property
    def plca_local_node(self) -> Optional[PositiveInteger]:
        """Get plcaLocalNode (Pythonic accessor)."""
        return self._plcaLocalNode

    @plca_local_node.setter
    def plca_local_node(self, value: Optional[PositiveInteger]) -> None:
        """
        Set plcaLocalNode with validation.

        Args:
            value: The plcaLocalNode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._plcaLocalNode = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"plcaLocalNode must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._plcaLocalNode = value
        # or not.
        self._plcaTransmit: Optional[PositiveInteger] = None

    @property
    def plca_transmit(self) -> Optional[PositiveInteger]:
        """Get plcaTransmit (Pythonic accessor)."""
        return self._plcaTransmit

    @plca_transmit.setter
    def plca_transmit(self, value: Optional[PositiveInteger]) -> None:
        """
        Set plcaTransmit with validation.

        Args:
            value: The plcaTransmit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._plcaTransmit = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"plcaTransmit must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._plcaTransmit = value
        # CouplingPortConnection.
        self._secondPort: Optional[CouplingPort] = None

    @property
    def second_port(self) -> Optional[CouplingPort]:
        """Get secondPort (Pythonic accessor)."""
        return self._secondPort

    @second_port.setter
    def second_port(self, value: Optional[CouplingPort]) -> None:
        """
        Set secondPort with validation.

        Args:
            value: The secondPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondPort = None
            return

        if not isinstance(value, CouplingPort):
            raise TypeError(
                f"secondPort must be CouplingPort or None, got {type(value).__name__}"
            )
        self._secondPort = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstPort(self) -> CouplingPort:
        """
        AUTOSAR-compliant getter for firstPort.

        Returns:
            The firstPort value

        Note:
            Delegates to first_port property (CODING_RULE_V2_00017)
        """
        return self.first_port  # Delegates to property

    def setFirstPort(self, value: CouplingPort) -> CouplingPortConnection:
        """
        AUTOSAR-compliant setter for firstPort with method chaining.

        Args:
            value: The firstPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_port property setter (gets validation automatically)
        """
        self.first_port = value  # Delegates to property setter
        return self

    def getNodePort(self) -> List[CouplingPort]:
        """
        AUTOSAR-compliant getter for nodePort.

        Returns:
            The nodePort value

        Note:
            Delegates to node_port property (CODING_RULE_V2_00017)
        """
        return self.node_port  # Delegates to property

    def getPlcaLocalNode(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for plcaLocalNode.

        Returns:
            The plcaLocalNode value

        Note:
            Delegates to plca_local_node property (CODING_RULE_V2_00017)
        """
        return self.plca_local_node  # Delegates to property

    def setPlcaLocalNode(self, value: PositiveInteger) -> CouplingPortConnection:
        """
        AUTOSAR-compliant setter for plcaLocalNode with method chaining.

        Args:
            value: The plcaLocalNode to set

        Returns:
            self for method chaining

        Note:
            Delegates to plca_local_node property setter (gets validation automatically)
        """
        self.plca_local_node = value  # Delegates to property setter
        return self

    def getPlcaTransmit(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for plcaTransmit.

        Returns:
            The plcaTransmit value

        Note:
            Delegates to plca_transmit property (CODING_RULE_V2_00017)
        """
        return self.plca_transmit  # Delegates to property

    def setPlcaTransmit(self, value: PositiveInteger) -> CouplingPortConnection:
        """
        AUTOSAR-compliant setter for plcaTransmit with method chaining.

        Args:
            value: The plcaTransmit to set

        Returns:
            self for method chaining

        Note:
            Delegates to plca_transmit property setter (gets validation automatically)
        """
        self.plca_transmit = value  # Delegates to property setter
        return self

    def getSecondPort(self) -> CouplingPort:
        """
        AUTOSAR-compliant getter for secondPort.

        Returns:
            The secondPort value

        Note:
            Delegates to second_port property (CODING_RULE_V2_00017)
        """
        return self.second_port  # Delegates to property

    def setSecondPort(self, value: CouplingPort) -> CouplingPortConnection:
        """
        AUTOSAR-compliant setter for secondPort with method chaining.

        Args:
            value: The secondPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to second_port property setter (gets validation automatically)
        """
        self.second_port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_port(self, value: Optional[CouplingPort]) -> CouplingPortConnection:
        """
        Set firstPort and return self for chaining.

        Args:
            value: The firstPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_port("value")
        """
        self.first_port = value  # Use property setter (gets validation)
        return self

    def with_plca_local_node(self, value: Optional[PositiveInteger]) -> CouplingPortConnection:
        """
        Set plcaLocalNode and return self for chaining.

        Args:
            value: The plcaLocalNode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_plca_local_node("value")
        """
        self.plca_local_node = value  # Use property setter (gets validation)
        return self

    def with_plca_transmit(self, value: Optional[PositiveInteger]) -> CouplingPortConnection:
        """
        Set plcaTransmit and return self for chaining.

        Args:
            value: The plcaTransmit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_plca_transmit("value")
        """
        self.plca_transmit = value  # Use property setter (gets validation)
        return self

    def with_second_port(self, value: Optional[CouplingPort]) -> CouplingPortConnection:
        """
        Set secondPort and return self for chaining.

        Args:
            value: The secondPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_port("value")
        """
        self.second_port = value  # Use property setter (gets validation)
        return self



class EthernetCommunicationController(ARObject):
    """
    Ethernet specific communication port attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthernetCommunicationController

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 115, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If the Ethernet frames handled by this Ethernet are to be tunneled through
        # XL, then this reference shall refer to the Abstract aggregates the Can the
        # physical CAN XL channel used for tunneling.
        self._canXlConfig: Optional[AbstractCanPhysicalChannel] = None

    @property
    def can_xl_config(self) -> Optional[AbstractCanPhysicalChannel]:
        """Get canXlConfig (Pythonic accessor)."""
        return self._canXlConfig

    @can_xl_config.setter
    def can_xl_config(self, value: Optional[AbstractCanPhysicalChannel]) -> None:
        """
        Set canXlConfig with validation.

        Args:
            value: The canXlConfig to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canXlConfig = None
            return

        if not isinstance(value, AbstractCan):
            raise TypeError(
                f"canXlConfig must be AbstractCan or None, got {type(value).__name__}"
            )
        self._canXlConfig = value
        # g.
        # a switch).
        self._couplingPort: List[CouplingPort] = []

    @property
    def coupling_port(self) -> List[CouplingPort]:
        """Get couplingPort (Pythonic accessor)."""
        return self._couplingPort
        # Specifies the mac layer type of the ethernet controller.
        self._macLayerType: Optional[EthernetMacLayerType] = None

    @property
    def mac_layer_type(self) -> Optional[EthernetMacLayerType]:
        """Get macLayerType (Pythonic accessor)."""
        return self._macLayerType

    @mac_layer_type.setter
    def mac_layer_type(self, value: Optional[EthernetMacLayerType]) -> None:
        """
        Set macLayerType with validation.

        Args:
            value: The macLayerType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macLayerType = None
            return

        if not isinstance(value, EthernetMacLayerType):
            raise TypeError(
                f"macLayerType must be EthernetMacLayerType or None, got {type(value).__name__}"
            )
        self._macLayerType = value
        # EthernetCommunication the network.
        self._macUnicast: Optional[MacAddressString] = None

    @property
    def mac_unicast(self) -> Optional[MacAddressString]:
        """Get macUnicast (Pythonic accessor)."""
        return self._macUnicast

    @mac_unicast.setter
    def mac_unicast(self, value: Optional[MacAddressString]) -> None:
        """
        Set macUnicast with validation.

        Args:
            value: The macUnicast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macUnicast = None
            return

        if not isinstance(value, MacAddressString):
            raise TypeError(
                f"macUnicast must be MacAddressString or None, got {type(value).__name__}"
            )
        self._macUnicast = value
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._maximum: Optional[Integer] = None

    @property
    def maximum(self) -> Optional[Integer]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional[Integer]) -> None:
        """
        Set maximum with validation.

        Args:
            value: The maximum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximum = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maximum must be Integer or int or None, got {type(value).__name__}"
            )
        self._maximum = value
                # slave on the connected Physical This is used for EthernetCommunication that
                # use Ethernet hardware which supports sleep on the network (e.
        # g.
        # Open Alliance Ethernet hardware).
        self._slaveActAs: Optional[Boolean] = None

    @property
    def slave_act_as(self) -> Optional[Boolean]:
        """Get slaveActAs (Pythonic accessor)."""
        return self._slaveActAs

    @slave_act_as.setter
    def slave_act_as(self, value: Optional[Boolean]) -> None:
        """
        Set slaveActAs with validation.

        Args:
            value: The slaveActAs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._slaveActAs = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"slaveActAs must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._slaveActAs = value
        # down and indicated to the communication stack.
        self._slaveQualified: Optional[TimeValue] = None

    @property
    def slave_qualified(self) -> Optional[TimeValue]:
        """Get slaveQualified (Pythonic accessor)."""
        return self._slaveQualified

    @slave_qualified.setter
    def slave_qualified(self, value: Optional[TimeValue]) -> None:
        """
        Set slaveQualified with validation.

        Args:
            value: The slaveQualified to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._slaveQualified = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"slaveQualified must be TimeValue or None, got {type(value).__name__}"
            )
        self._slaveQualified = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCanXlConfig(self) -> AbstractCanPhysicalChannel:
        """
        AUTOSAR-compliant getter for canXlConfig.

        Returns:
            The canXlConfig value

        Note:
            Delegates to can_xl_config property (CODING_RULE_V2_00017)
        """
        return self.can_xl_config  # Delegates to property

    def setCanXlConfig(self, value: AbstractCanPhysicalChannel) -> EthernetCommunicationController:
        """
        AUTOSAR-compliant setter for canXlConfig with method chaining.

        Args:
            value: The canXlConfig to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_xl_config property setter (gets validation automatically)
        """
        self.can_xl_config = value  # Delegates to property setter
        return self

    def getCouplingPort(self) -> List[CouplingPort]:
        """
        AUTOSAR-compliant getter for couplingPort.

        Returns:
            The couplingPort value

        Note:
            Delegates to coupling_port property (CODING_RULE_V2_00017)
        """
        return self.coupling_port  # Delegates to property

    def getMacLayerType(self) -> EthernetMacLayerType:
        """
        AUTOSAR-compliant getter for macLayerType.

        Returns:
            The macLayerType value

        Note:
            Delegates to mac_layer_type property (CODING_RULE_V2_00017)
        """
        return self.mac_layer_type  # Delegates to property

    def setMacLayerType(self, value: EthernetMacLayerType) -> EthernetCommunicationController:
        """
        AUTOSAR-compliant setter for macLayerType with method chaining.

        Args:
            value: The macLayerType to set

        Returns:
            self for method chaining

        Note:
            Delegates to mac_layer_type property setter (gets validation automatically)
        """
        self.mac_layer_type = value  # Delegates to property setter
        return self

    def getMacUnicast(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for macUnicast.

        Returns:
            The macUnicast value

        Note:
            Delegates to mac_unicast property (CODING_RULE_V2_00017)
        """
        return self.mac_unicast  # Delegates to property

    def setMacUnicast(self, value: "MacAddressString") -> EthernetCommunicationController:
        """
        AUTOSAR-compliant setter for macUnicast with method chaining.

        Args:
            value: The macUnicast to set

        Returns:
            self for method chaining

        Note:
            Delegates to mac_unicast property setter (gets validation automatically)
        """
        self.mac_unicast = value  # Delegates to property setter
        return self

    def getMaximum(self) -> Integer:
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: Integer) -> EthernetCommunicationController:
        """
        AUTOSAR-compliant setter for maximum with method chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum property setter (gets validation automatically)
        """
        self.maximum = value  # Delegates to property setter
        return self

    def getSlaveActAs(self) -> Boolean:
        """
        AUTOSAR-compliant getter for slaveActAs.

        Returns:
            The slaveActAs value

        Note:
            Delegates to slave_act_as property (CODING_RULE_V2_00017)
        """
        return self.slave_act_as  # Delegates to property

    def setSlaveActAs(self, value: Boolean) -> EthernetCommunicationController:
        """
        AUTOSAR-compliant setter for slaveActAs with method chaining.

        Args:
            value: The slaveActAs to set

        Returns:
            self for method chaining

        Note:
            Delegates to slave_act_as property setter (gets validation automatically)
        """
        self.slave_act_as = value  # Delegates to property setter
        return self

    def getSlaveQualified(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for slaveQualified.

        Returns:
            The slaveQualified value

        Note:
            Delegates to slave_qualified property (CODING_RULE_V2_00017)
        """
        return self.slave_qualified  # Delegates to property

    def setSlaveQualified(self, value: TimeValue) -> EthernetCommunicationController:
        """
        AUTOSAR-compliant setter for slaveQualified with method chaining.

        Args:
            value: The slaveQualified to set

        Returns:
            self for method chaining

        Note:
            Delegates to slave_qualified property setter (gets validation automatically)
        """
        self.slave_qualified = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_can_xl_config(self, value: Optional[AbstractCanPhysicalChannel]) -> EthernetCommunicationController:
        """
        Set canXlConfig and return self for chaining.

        Args:
            value: The canXlConfig to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_xl_config("value")
        """
        self.can_xl_config = value  # Use property setter (gets validation)
        return self

    def with_mac_layer_type(self, value: Optional[EthernetMacLayerType]) -> EthernetCommunicationController:
        """
        Set macLayerType and return self for chaining.

        Args:
            value: The macLayerType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mac_layer_type("value")
        """
        self.mac_layer_type = value  # Use property setter (gets validation)
        return self

    def with_mac_unicast(self, value: Optional[MacAddressString]) -> EthernetCommunicationController:
        """
        Set macUnicast and return self for chaining.

        Args:
            value: The macUnicast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mac_unicast("value")
        """
        self.mac_unicast = value  # Use property setter (gets validation)
        return self

    def with_maximum(self, value: Optional[Integer]) -> EthernetCommunicationController:
        """
        Set maximum and return self for chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum("value")
        """
        self.maximum = value  # Use property setter (gets validation)
        return self

    def with_slave_act_as(self, value: Optional[Boolean]) -> EthernetCommunicationController:
        """
        Set slaveActAs and return self for chaining.

        Args:
            value: The slaveActAs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_slave_act_as("value")
        """
        self.slave_act_as = value  # Use property setter (gets validation)
        return self

    def with_slave_qualified(self, value: Optional[TimeValue]) -> EthernetCommunicationController:
        """
        Set slaveQualified and return self for chaining.

        Args:
            value: The slaveQualified to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_slave_qualified("value")
        """
        self.slave_qualified = value  # Use property setter (gets validation)
        return self



class EthernetCommunicationConnector(CommunicationConnector):
    """
    Ethernet specific attributes to the CommunicationConnector.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthernetCommunicationConnector

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 117, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # EcuInstance specific IP attributes.
        self._ethIpProps: Optional[EthIpProps] = None

    @property
    def eth_ip_props(self) -> Optional[EthIpProps]:
        """Get ethIpProps (Pythonic accessor)."""
        return self._ethIpProps

    @eth_ip_props.setter
    def eth_ip_props(self, value: Optional[EthIpProps]) -> None:
        """
        Set ethIpProps with validation.

        Args:
            value: The ethIpProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ethIpProps = None
            return

        if not isinstance(value, EthIpProps):
            raise TypeError(
                f"ethIpProps must be EthIpProps or None, got {type(value).__name__}"
            )
        self._ethIpProps = value
        self._maximum: Optional[PositiveInteger] = None

    @property
    def maximum(self) -> Optional[PositiveInteger]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maximum with validation.

        Args:
            value: The maximum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximum = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maximum must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maximum = value
        # entries.
        self._neighborCache: Optional[PositiveInteger] = None

    @property
    def neighbor_cache(self) -> Optional[PositiveInteger]:
        """Get neighborCache (Pythonic accessor)."""
        return self._neighborCache

    @neighbor_cache.setter
    def neighbor_cache(self, value: Optional[PositiveInteger]) -> None:
        """
        Set neighborCache with validation.

        Args:
            value: The neighborCache to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._neighborCache = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"neighborCache must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._neighborCache = value
        # a MTU value for address.
        self._pathMtu: Optional[Boolean] = None

    @property
    def path_mtu(self) -> Optional[Boolean]:
        """Get pathMtu (Pythonic accessor)."""
        return self._pathMtu

    @path_mtu.setter
    def path_mtu(self, value: Optional[Boolean]) -> None:
        """
        Set pathMtu with validation.

        Args:
            value: The pathMtu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pathMtu = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"pathMtu must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._pathMtu = value
        # after n seconds.
        self._pathMtuTimeout: Optional[TimeValue] = None

    @property
    def path_mtu_timeout(self) -> Optional[TimeValue]:
        """Get pathMtuTimeout (Pythonic accessor)."""
        return self._pathMtuTimeout

    @path_mtu_timeout.setter
    def path_mtu_timeout(self, value: Optional[TimeValue]) -> None:
        """
        Set pathMtuTimeout with validation.

        Args:
            value: The pathMtuTimeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pathMtuTimeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"pathMtuTimeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._pathMtuTimeout = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEthIpProps(self) -> EthIpProps:
        """
        AUTOSAR-compliant getter for ethIpProps.

        Returns:
            The ethIpProps value

        Note:
            Delegates to eth_ip_props property (CODING_RULE_V2_00017)
        """
        return self.eth_ip_props  # Delegates to property

    def setEthIpProps(self, value: EthIpProps) -> EthernetCommunicationConnector:
        """
        AUTOSAR-compliant setter for ethIpProps with method chaining.

        Args:
            value: The ethIpProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to eth_ip_props property setter (gets validation automatically)
        """
        self.eth_ip_props = value  # Delegates to property setter
        return self

    def getMaximum(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: PositiveInteger) -> EthernetCommunicationConnector:
        """
        AUTOSAR-compliant setter for maximum with method chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum property setter (gets validation automatically)
        """
        self.maximum = value  # Delegates to property setter
        return self

    def getNeighborCache(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for neighborCache.

        Returns:
            The neighborCache value

        Note:
            Delegates to neighbor_cache property (CODING_RULE_V2_00017)
        """
        return self.neighbor_cache  # Delegates to property

    def setNeighborCache(self, value: PositiveInteger) -> EthernetCommunicationConnector:
        """
        AUTOSAR-compliant setter for neighborCache with method chaining.

        Args:
            value: The neighborCache to set

        Returns:
            self for method chaining

        Note:
            Delegates to neighbor_cache property setter (gets validation automatically)
        """
        self.neighbor_cache = value  # Delegates to property setter
        return self

    def getPathMtu(self) -> Boolean:
        """
        AUTOSAR-compliant getter for pathMtu.

        Returns:
            The pathMtu value

        Note:
            Delegates to path_mtu property (CODING_RULE_V2_00017)
        """
        return self.path_mtu  # Delegates to property

    def setPathMtu(self, value: Boolean) -> EthernetCommunicationConnector:
        """
        AUTOSAR-compliant setter for pathMtu with method chaining.

        Args:
            value: The pathMtu to set

        Returns:
            self for method chaining

        Note:
            Delegates to path_mtu property setter (gets validation automatically)
        """
        self.path_mtu = value  # Delegates to property setter
        return self

    def getPathMtuTimeout(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for pathMtuTimeout.

        Returns:
            The pathMtuTimeout value

        Note:
            Delegates to path_mtu_timeout property (CODING_RULE_V2_00017)
        """
        return self.path_mtu_timeout  # Delegates to property

    def setPathMtuTimeout(self, value: TimeValue) -> EthernetCommunicationConnector:
        """
        AUTOSAR-compliant setter for pathMtuTimeout with method chaining.

        Args:
            value: The pathMtuTimeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to path_mtu_timeout property setter (gets validation automatically)
        """
        self.path_mtu_timeout = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_eth_ip_props(self, value: Optional[EthIpProps]) -> EthernetCommunicationConnector:
        """
        Set ethIpProps and return self for chaining.

        Args:
            value: The ethIpProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_eth_ip_props("value")
        """
        self.eth_ip_props = value  # Use property setter (gets validation)
        return self

    def with_maximum(self, value: Optional[PositiveInteger]) -> EthernetCommunicationConnector:
        """
        Set maximum and return self for chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum("value")
        """
        self.maximum = value  # Use property setter (gets validation)
        return self

    def with_neighbor_cache(self, value: Optional[PositiveInteger]) -> EthernetCommunicationConnector:
        """
        Set neighborCache and return self for chaining.

        Args:
            value: The neighborCache to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_neighbor_cache("value")
        """
        self.neighbor_cache = value  # Use property setter (gets validation)
        return self

    def with_path_mtu(self, value: Optional[Boolean]) -> EthernetCommunicationConnector:
        """
        Set pathMtu and return self for chaining.

        Args:
            value: The pathMtu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_path_mtu("value")
        """
        self.path_mtu = value  # Use property setter (gets validation)
        return self

    def with_path_mtu_timeout(self, value: Optional[TimeValue]) -> EthernetCommunicationConnector:
        """
        Set pathMtuTimeout and return self for chaining.

        Args:
            value: The pathMtuTimeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_path_mtu_timeout("value")
        """
        self.path_mtu_timeout = value  # Use property setter (gets validation)
        return self



class CouplingPortDetails(ARObject):
    """
    Defines details of a CouplingPort. May be used to configure the structures
    of a switch.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortDetails

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 121, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collects all the structural parts at which a CouplingPort may be
        # configurable.
        self._couplingPort: List["CouplingPortStructural"] = []

    @property
    def coupling_port(self) -> List["CouplingPortStructural"]:
        """Get couplingPort (Pythonic accessor)."""
        return self._couplingPort
        # is replaced by regenerated priority.
        self._ethernetPriority: "EthernetPriority" = None

    @property
    def ethernet_priority(self) -> "EthernetPriority":
        """Get ethernetPriority (Pythonic accessor)."""
        return self._ethernetPriority

    @ethernet_priority.setter
    def ethernet_priority(self, value: "EthernetPriority") -> None:
        """
        Set ethernetPriority with validation.

        Args:
            value: The ethernetPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, EthernetPriority):
            raise TypeError(
                f"ethernetPriority must be EthernetPriority, got {type(value).__name__}"
            )
        self._ethernetPriority = value

    @property
    def ethernet_traffic(self) -> "CouplingPortTraffic":
        """Get ethernetTraffic (Pythonic accessor)."""
        return self._ethernetTraffic

    @ethernet_traffic.setter
    def ethernet_traffic(self, value: "CouplingPortTraffic") -> None:
        """
        Set ethernetTraffic with validation.

        Args:
            value: The ethernetTraffic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, CouplingPortTraffic):
            raise TypeError(
                f"ethernetTraffic must be CouplingPortTraffic, got {type(value).__name__}"
            )
        self._ethernetTraffic = value
                # Time Sync.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._globalTime: Optional[GlobalTimeCouplingPortConfiguration] = None

    @property
    def global_time(self) -> Optional[GlobalTimeCouplingPortConfiguration]:
        """Get globalTime (Pythonic accessor)."""
        return self._globalTime

    @global_time.setter
    def global_time(self, value: Optional[GlobalTimeCouplingPortConfiguration]) -> None:
        """
        Set globalTime with validation.

        Args:
            value: The globalTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._globalTime = None
            return

        if not isinstance(value, GlobalTimeCoupling):
            raise TypeError(
                f"globalTime must be GlobalTimeCoupling or None, got {type(value).__name__}"
            )
        self._globalTime = value
        self._lastEgress: Optional[CouplingPortScheduler] = None

    @property
    def last_egress(self) -> Optional[CouplingPortScheduler]:
        """Get lastEgress (Pythonic accessor)."""
        return self._lastEgress

    @last_egress.setter
    def last_egress(self, value: Optional[CouplingPortScheduler]) -> None:
        """
        Set lastEgress with validation.

        Args:
            value: The lastEgress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lastEgress = None
            return

        if not isinstance(value, CouplingPortScheduler):
            raise TypeError(
                f"lastEgress must be CouplingPortScheduler or None, got {type(value).__name__}"
            )
        self._lastEgress = value
        self._ratePolicy: List[CouplingPortRatePolicy] = []

    @property
    def rate_policy(self) -> List[CouplingPortRatePolicy]:
        """Get ratePolicy (Pythonic accessor)."""
        return self._ratePolicy

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCouplingPort(self) -> List["CouplingPortStructural"]:
        """
        AUTOSAR-compliant getter for couplingPort.

        Returns:
            The couplingPort value

        Note:
            Delegates to coupling_port property (CODING_RULE_V2_00017)
        """
        return self.coupling_port  # Delegates to property

    def getEthernetPriority(self) -> "EthernetPriority":
        """
        AUTOSAR-compliant getter for ethernetPriority.

        Returns:
            The ethernetPriority value

        Note:
            Delegates to ethernet_priority property (CODING_RULE_V2_00017)
        """
        return self.ethernet_priority  # Delegates to property

    def setEthernetPriority(self, value: "EthernetPriority") -> CouplingPortDetails:
        """
        AUTOSAR-compliant setter for ethernetPriority with method chaining.

        Args:
            value: The ethernetPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to ethernet_priority property setter (gets validation automatically)
        """
        self.ethernet_priority = value  # Delegates to property setter
        return self

    def getEthernetTraffic(self) -> "CouplingPortTraffic":
        """
        AUTOSAR-compliant getter for ethernetTraffic.

        Returns:
            The ethernetTraffic value

        Note:
            Delegates to ethernet_traffic property (CODING_RULE_V2_00017)
        """
        return self.ethernet_traffic  # Delegates to property

    def setEthernetTraffic(self, value: "CouplingPortTraffic") -> CouplingPortDetails:
        """
        AUTOSAR-compliant setter for ethernetTraffic with method chaining.

        Args:
            value: The ethernetTraffic to set

        Returns:
            self for method chaining

        Note:
            Delegates to ethernet_traffic property setter (gets validation automatically)
        """
        self.ethernet_traffic = value  # Delegates to property setter
        return self

    def getGlobalTime(self) -> GlobalTimeCouplingPortConfiguration:
        """
        AUTOSAR-compliant getter for globalTime.

        Returns:
            The globalTime value

        Note:
            Delegates to global_time property (CODING_RULE_V2_00017)
        """
        return self.global_time  # Delegates to property

    def setGlobalTime(self, value: GlobalTimeCouplingPortConfiguration) -> CouplingPortDetails:
        """
        AUTOSAR-compliant setter for globalTime with method chaining.

        Args:
            value: The globalTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to global_time property setter (gets validation automatically)
        """
        self.global_time = value  # Delegates to property setter
        return self

    def getLastEgress(self) -> CouplingPortScheduler:
        """
        AUTOSAR-compliant getter for lastEgress.

        Returns:
            The lastEgress value

        Note:
            Delegates to last_egress property (CODING_RULE_V2_00017)
        """
        return self.last_egress  # Delegates to property

    def setLastEgress(self, value: CouplingPortScheduler) -> CouplingPortDetails:
        """
        AUTOSAR-compliant setter for lastEgress with method chaining.

        Args:
            value: The lastEgress to set

        Returns:
            self for method chaining

        Note:
            Delegates to last_egress property setter (gets validation automatically)
        """
        self.last_egress = value  # Delegates to property setter
        return self

    def getRatePolicy(self) -> List[CouplingPortRatePolicy]:
        """
        AUTOSAR-compliant getter for ratePolicy.

        Returns:
            The ratePolicy value

        Note:
            Delegates to rate_policy property (CODING_RULE_V2_00017)
        """
        return self.rate_policy  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ethernet_priority(self, value: "EthernetPriority") -> CouplingPortDetails:
        """
        Set ethernetPriority and return self for chaining.

        Args:
            value: The ethernetPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ethernet_priority("value")
        """
        self.ethernet_priority = value  # Use property setter (gets validation)
        return self

    def with_ethernet_traffic(self, value: "CouplingPortTraffic") -> CouplingPortDetails:
        """
        Set ethernetTraffic and return self for chaining.

        Args:
            value: The ethernetTraffic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ethernet_traffic("value")
        """
        self.ethernet_traffic = value  # Use property setter (gets validation)
        return self

    def with_global_time(self, value: Optional[GlobalTimeCouplingPortConfiguration]) -> CouplingPortDetails:
        """
        Set globalTime and return self for chaining.

        Args:
            value: The globalTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_global_time("value")
        """
        self.global_time = value  # Use property setter (gets validation)
        return self

    def with_last_egress(self, value: Optional[CouplingPortScheduler]) -> CouplingPortDetails:
        """
        Set lastEgress and return self for chaining.

        Args:
            value: The lastEgress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_last_egress("value")
        """
        self.last_egress = value  # Use property setter (gets validation)
        return self



class CouplingPortStructuralElement(Identifiable, ABC):
    """
    General class to define structural elements a CouplingPort may consist of.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortStructuralElement

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 122, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is CouplingPortStructuralElement:
            raise TypeError("CouplingPortStructuralElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CouplingPortRatePolicy(ARObject):
    """
    Defines a rate policy on a CouplingPort.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortRatePolicy

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 124, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Amount of data in bytes (excluding header information) be received to define
        # the rate policy.
        self._dataLength: Optional[PositiveInteger] = None

    @property
    def data_length(self) -> Optional[PositiveInteger]:
        """Get dataLength (Pythonic accessor)."""
        return self._dataLength

    @data_length.setter
    def data_length(self, value: Optional[PositiveInteger]) -> None:
        """
        Set dataLength with validation.

        Args:
            value: The dataLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"dataLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._dataLength = value
        self._policyAction: Optional[CouplingPortRatePolicy] = None

    @property
    def policy_action(self) -> Optional[CouplingPortRatePolicy]:
        """Get policyAction (Pythonic accessor)."""
        return self._policyAction

    @policy_action.setter
    def policy_action(self, value: Optional[CouplingPortRatePolicy]) -> None:
        """
        Set policyAction with validation.

        Args:
            value: The policyAction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._policyAction = None
            return

        if not isinstance(value, CouplingPortRatePolicy):
            raise TypeError(
                f"policyAction must be CouplingPortRatePolicy or None, got {type(value).__name__}"
            )
        self._policyAction = value
        # given this rate policy is not considering.
        self._priority: Optional[PositiveInteger] = None

    @property
    def priority(self) -> Optional[PositiveInteger]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional[PositiveInteger]) -> None:
        """
        Set priority with validation.

        Args:
            value: The priority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priority = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._priority = value
        self._timeInterval: Optional[TimeValue] = None

    @property
    def time_interval(self) -> Optional[TimeValue]:
        """Get timeInterval (Pythonic accessor)."""
        return self._timeInterval

    @time_interval.setter
    def time_interval(self, value: Optional[TimeValue]) -> None:
        """
        Set timeInterval with validation.

        Args:
            value: The timeInterval to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeInterval = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeInterval must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeInterval = value
        # If VLAN is given this rate policy is not considering VLAN.
        self._vLan: List[EthernetPhysical] = []

    @property
    def v_lan(self) -> List[EthernetPhysical]:
        """Get vLan (Pythonic accessor)."""
        return self._vLan

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataLength(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for dataLength.

        Returns:
            The dataLength value

        Note:
            Delegates to data_length property (CODING_RULE_V2_00017)
        """
        return self.data_length  # Delegates to property

    def setDataLength(self, value: PositiveInteger) -> CouplingPortRatePolicy:
        """
        AUTOSAR-compliant setter for dataLength with method chaining.

        Args:
            value: The dataLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_length property setter (gets validation automatically)
        """
        self.data_length = value  # Delegates to property setter
        return self

    def getPolicyAction(self) -> CouplingPortRatePolicy:
        """
        AUTOSAR-compliant getter for policyAction.

        Returns:
            The policyAction value

        Note:
            Delegates to policy_action property (CODING_RULE_V2_00017)
        """
        return self.policy_action  # Delegates to property

    def setPolicyAction(self, value: CouplingPortRatePolicy) -> CouplingPortRatePolicy:
        """
        AUTOSAR-compliant setter for policyAction with method chaining.

        Args:
            value: The policyAction to set

        Returns:
            self for method chaining

        Note:
            Delegates to policy_action property setter (gets validation automatically)
        """
        self.policy_action = value  # Delegates to property setter
        return self

    def getPriority(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: PositiveInteger) -> CouplingPortRatePolicy:
        """
        AUTOSAR-compliant setter for priority with method chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    def getTimeInterval(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeInterval.

        Returns:
            The timeInterval value

        Note:
            Delegates to time_interval property (CODING_RULE_V2_00017)
        """
        return self.time_interval  # Delegates to property

    def setTimeInterval(self, value: TimeValue) -> CouplingPortRatePolicy:
        """
        AUTOSAR-compliant setter for timeInterval with method chaining.

        Args:
            value: The timeInterval to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_interval property setter (gets validation automatically)
        """
        self.time_interval = value  # Delegates to property setter
        return self

    def getVLan(self) -> List[EthernetPhysical]:
        """
        AUTOSAR-compliant getter for vLan.

        Returns:
            The vLan value

        Note:
            Delegates to v_lan property (CODING_RULE_V2_00017)
        """
        return self.v_lan  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_length(self, value: Optional[PositiveInteger]) -> CouplingPortRatePolicy:
        """
        Set dataLength and return self for chaining.

        Args:
            value: The dataLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_length("value")
        """
        self.data_length = value  # Use property setter (gets validation)
        return self

    def with_policy_action(self, value: Optional[CouplingPortRatePolicy]) -> CouplingPortRatePolicy:
        """
        Set policyAction and return self for chaining.

        Args:
            value: The policyAction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_policy_action("value")
        """
        self.policy_action = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> CouplingPortRatePolicy:
        """
        Set priority and return self for chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self

    def with_time_interval(self, value: Optional[TimeValue]) -> CouplingPortRatePolicy:
        """
        Set timeInterval and return self for chaining.

        Args:
            value: The timeInterval to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_interval("value")
        """
        self.time_interval = value  # Use property setter (gets validation)
        return self



class EthernetPriorityRegeneration(Referrable):
    """
    Defines a priority regeneration where the ingressPriority is replaced by
    regeneratedPriority. The ethernetPriorityRegeneration is optional in case no
    priority regeneration shall be performed. In case a
    ethernetPriorityRegeneration is defined it shall have 8 mappings, one for
    each priority.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthernetPriorityRegeneration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 128, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Message priority of the incoming message.
        self._ingressPriority: Optional[PositiveInteger] = None

    @property
    def ingress_priority(self) -> Optional[PositiveInteger]:
        """Get ingressPriority (Pythonic accessor)."""
        return self._ingressPriority

    @ingress_priority.setter
    def ingress_priority(self, value: Optional[PositiveInteger]) -> None:
        """
        Set ingressPriority with validation.

        Args:
            value: The ingressPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ingressPriority = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"ingressPriority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._ingressPriority = value
        # 0-7.
        self._regenerated: Optional[PositiveInteger] = None

    @property
    def regenerated(self) -> Optional[PositiveInteger]:
        """Get regenerated (Pythonic accessor)."""
        return self._regenerated

    @regenerated.setter
    def regenerated(self, value: Optional[PositiveInteger]) -> None:
        """
        Set regenerated with validation.

        Args:
            value: The regenerated to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._regenerated = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"regenerated must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._regenerated = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIngressPriority(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for ingressPriority.

        Returns:
            The ingressPriority value

        Note:
            Delegates to ingress_priority property (CODING_RULE_V2_00017)
        """
        return self.ingress_priority  # Delegates to property

    def setIngressPriority(self, value: PositiveInteger) -> EthernetPriorityRegeneration:
        """
        AUTOSAR-compliant setter for ingressPriority with method chaining.

        Args:
            value: The ingressPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to ingress_priority property setter (gets validation automatically)
        """
        self.ingress_priority = value  # Delegates to property setter
        return self

    def getRegenerated(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for regenerated.

        Returns:
            The regenerated value

        Note:
            Delegates to regenerated property (CODING_RULE_V2_00017)
        """
        return self.regenerated  # Delegates to property

    def setRegenerated(self, value: PositiveInteger) -> EthernetPriorityRegeneration:
        """
        AUTOSAR-compliant setter for regenerated with method chaining.

        Args:
            value: The regenerated to set

        Returns:
            self for method chaining

        Note:
            Delegates to regenerated property setter (gets validation automatically)
        """
        self.regenerated = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ingress_priority(self, value: Optional[PositiveInteger]) -> EthernetPriorityRegeneration:
        """
        Set ingressPriority and return self for chaining.

        Args:
            value: The ingressPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ingress_priority("value")
        """
        self.ingress_priority = value  # Use property setter (gets validation)
        return self

    def with_regenerated(self, value: Optional[PositiveInteger]) -> EthernetPriorityRegeneration:
        """
        Set regenerated and return self for chaining.

        Args:
            value: The regenerated to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_regenerated("value")
        """
        self.regenerated = value  # Use property setter (gets validation)
        return self



class CouplingPortTrafficClassAssignment(Referrable):
    """
    Defines the assignment of Traffic Class to a frame.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortTrafficClassAssignment

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 128, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._priority: PositiveInteger = None

    @property
    def priority(self) -> PositiveInteger:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: PositiveInteger) -> None:
        """
        Set priority with validation.

        Args:
            value: The priority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priority must be PositiveInteger or str, got {type(value).__name__}"
            )
        self._priority = value
        self._trafficClass: Optional[PositiveInteger] = None

    @property
    def traffic_class(self) -> Optional[PositiveInteger]:
        """Get trafficClass (Pythonic accessor)."""
        return self._trafficClass

    @traffic_class.setter
    def traffic_class(self, value: Optional[PositiveInteger]) -> None:
        """
        Set trafficClass with validation.

        Args:
            value: The trafficClass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trafficClass = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"trafficClass must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._trafficClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPriority(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: PositiveInteger) -> CouplingPortTrafficClassAssignment:
        """
        AUTOSAR-compliant setter for priority with method chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    def getTrafficClass(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for trafficClass.

        Returns:
            The trafficClass value

        Note:
            Delegates to traffic_class property (CODING_RULE_V2_00017)
        """
        return self.traffic_class  # Delegates to property

    def setTrafficClass(self, value: PositiveInteger) -> CouplingPortTrafficClassAssignment:
        """
        AUTOSAR-compliant setter for trafficClass with method chaining.

        Args:
            value: The trafficClass to set

        Returns:
            self for method chaining

        Note:
            Delegates to traffic_class property setter (gets validation automatically)
        """
        self.traffic_class = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_priority(self, value: PositiveInteger) -> CouplingPortTrafficClassAssignment:
        """
        Set priority and return self for chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self

    def with_traffic_class(self, value: Optional[PositiveInteger]) -> CouplingPortTrafficClassAssignment:
        """
        Set trafficClass and return self for chaining.

        Args:
            value: The trafficClass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_traffic_class("value")
        """
        self.traffic_class = value  # Use property setter (gets validation)
        return self



class DhcpServerConfiguration(ARObject):
    """
    Defines the configuration of DHCP servers that are running on the network
    endpoint. It is possible that an Ipv4DhcpServer and an Ipv6DhcpServer run on
    the same Ecu.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::DhcpServerConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 131, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Configuration of a IPv4 DHCP server that runs on the network endpoint.
        self._ipv4DhcpServer: Optional[Ipv4DhcpServerConfiguration] = None

    @property
    def ipv4_dhcp_server(self) -> Optional[Ipv4DhcpServerConfiguration]:
        """Get ipv4DhcpServer (Pythonic accessor)."""
        return self._ipv4DhcpServer

    @ipv4_dhcp_server.setter
    def ipv4_dhcp_server(self, value: Optional[Ipv4DhcpServerConfiguration]) -> None:
        """
        Set ipv4DhcpServer with validation.

        Args:
            value: The ipv4DhcpServer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv4DhcpServer = None
            return

        if not isinstance(value, Ipv4DhcpServer):
            raise TypeError(
                f"ipv4DhcpServer must be Ipv4DhcpServer or None, got {type(value).__name__}"
            )
        self._ipv4DhcpServer = value
        # Configuration of a IPv6 DHCP server that runs on the network endpoint.
        self._ipv6DhcpServer: Optional[Ipv6DhcpServerConfiguration] = None

    @property
    def ipv6_dhcp_server(self) -> Optional[Ipv6DhcpServerConfiguration]:
        """Get ipv6DhcpServer (Pythonic accessor)."""
        return self._ipv6DhcpServer

    @ipv6_dhcp_server.setter
    def ipv6_dhcp_server(self, value: Optional[Ipv6DhcpServerConfiguration]) -> None:
        """
        Set ipv6DhcpServer with validation.

        Args:
            value: The ipv6DhcpServer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv6DhcpServer = None
            return

        if not isinstance(value, Ipv6DhcpServer):
            raise TypeError(
                f"ipv6DhcpServer must be Ipv6DhcpServer or None, got {type(value).__name__}"
            )
        self._ipv6DhcpServer = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIpv4DhcpServer(self) -> Ipv4DhcpServerConfiguration:
        """
        AUTOSAR-compliant getter for ipv4DhcpServer.

        Returns:
            The ipv4DhcpServer value

        Note:
            Delegates to ipv4_dhcp_server property (CODING_RULE_V2_00017)
        """
        return self.ipv4_dhcp_server  # Delegates to property

    def setIpv4DhcpServer(self, value: Ipv4DhcpServerConfiguration) -> DhcpServerConfiguration:
        """
        AUTOSAR-compliant setter for ipv4DhcpServer with method chaining.

        Args:
            value: The ipv4DhcpServer to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv4_dhcp_server property setter (gets validation automatically)
        """
        self.ipv4_dhcp_server = value  # Delegates to property setter
        return self

    def getIpv6DhcpServer(self) -> Ipv6DhcpServerConfiguration:
        """
        AUTOSAR-compliant getter for ipv6DhcpServer.

        Returns:
            The ipv6DhcpServer value

        Note:
            Delegates to ipv6_dhcp_server property (CODING_RULE_V2_00017)
        """
        return self.ipv6_dhcp_server  # Delegates to property

    def setIpv6DhcpServer(self, value: Ipv6DhcpServerConfiguration) -> DhcpServerConfiguration:
        """
        AUTOSAR-compliant setter for ipv6DhcpServer with method chaining.

        Args:
            value: The ipv6DhcpServer to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv6_dhcp_server property setter (gets validation automatically)
        """
        self.ipv6_dhcp_server = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ipv4_dhcp_server(self, value: Optional[Ipv4DhcpServerConfiguration]) -> DhcpServerConfiguration:
        """
        Set ipv4DhcpServer and return self for chaining.

        Args:
            value: The ipv4DhcpServer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv4_dhcp_server("value")
        """
        self.ipv4_dhcp_server = value  # Use property setter (gets validation)
        return self

    def with_ipv6_dhcp_server(self, value: Optional[Ipv6DhcpServerConfiguration]) -> DhcpServerConfiguration:
        """
        Set ipv6DhcpServer and return self for chaining.

        Args:
            value: The ipv6DhcpServer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv6_dhcp_server("value")
        """
        self.ipv6_dhcp_server = value  # Use property setter (gets validation)
        return self



class Ipv4DhcpServerConfiguration(Describable):
    """
    Defines the configuration of a IPv4 DHCP server that runs on the network
    endpoint.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv4DhcpServerConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 131, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Upper range of IP addresses to be issued to DHCP Pv4 Address.
        # Notation: 255.
        # 255.
        # 255.
        # 255.
        self._addressRange: Optional[Ip4AddressString] = None

    @property
    def address_range(self) -> Optional[Ip4AddressString]:
        """Get addressRange (Pythonic accessor)."""
        return self._addressRange

    @address_range.setter
    def address_range(self, value: Optional[Ip4AddressString]) -> None:
        """
        Set addressRange with validation.

        Args:
            value: The addressRange to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._addressRange = None
            return

        if not isinstance(value, Ip4AddressString):
            raise TypeError(
                f"addressRange must be Ip4AddressString or None, got {type(value).__name__}"
            )
        self._addressRange = value
        # Notation.
        self._defaultGateway: Optional[Ip4AddressString] = None

    @property
    def default_gateway(self) -> Optional[Ip4AddressString]:
        """Get defaultGateway (Pythonic accessor)."""
        return self._defaultGateway

    @default_gateway.setter
    def default_gateway(self, value: Optional[Ip4AddressString]) -> None:
        """
        Set defaultGateway with validation.

        Args:
            value: The defaultGateway to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultGateway = None
            return

        if not isinstance(value, Ip4AddressString):
            raise TypeError(
                f"defaultGateway must be Ip4AddressString or None, got {type(value).__name__}"
            )
        self._defaultGateway = value
        self._defaultLease: Optional[TimeValue] = None

    @property
    def default_lease(self) -> Optional[TimeValue]:
        """Get defaultLease (Pythonic accessor)."""
        return self._defaultLease

    @default_lease.setter
    def default_lease(self, value: Optional[TimeValue]) -> None:
        """
        Set defaultLease with validation.

        Args:
            value: The defaultLease to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultLease = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"defaultLease must be TimeValue or None, got {type(value).__name__}"
            )
        self._defaultLease = value
        # Notation.
        self._dnsServer: List[Ip4AddressString] = []

    @property
    def dns_server(self) -> List[Ip4AddressString]:
        """Get dnsServer (Pythonic accessor)."""
        return self._dnsServer
        # Default network mask to be used by DHCP clients.
        self._networkMask: Optional[Ip4AddressString] = None

    @property
    def network_mask(self) -> Optional[Ip4AddressString]:
        """Get networkMask (Pythonic accessor)."""
        return self._networkMask

    @network_mask.setter
    def network_mask(self, value: Optional[Ip4AddressString]) -> None:
        """
        Set networkMask with validation.

        Args:
            value: The networkMask to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._networkMask = None
            return

        if not isinstance(value, Ip4AddressString):
            raise TypeError(
                f"networkMask must be Ip4AddressString or None, got {type(value).__name__}"
            )
        self._networkMask = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAddressRange(self) -> Ip4AddressString:
        """
        AUTOSAR-compliant getter for addressRange.

        Returns:
            The addressRange value

        Note:
            Delegates to address_range property (CODING_RULE_V2_00017)
        """
        return self.address_range  # Delegates to property

    def setAddressRange(self, value: Ip4AddressString) -> Ipv4DhcpServerConfiguration:
        """
        AUTOSAR-compliant setter for addressRange with method chaining.

        Args:
            value: The addressRange to set

        Returns:
            self for method chaining

        Note:
            Delegates to address_range property setter (gets validation automatically)
        """
        self.address_range = value  # Delegates to property setter
        return self

    def getDefaultGateway(self) -> Ip4AddressString:
        """
        AUTOSAR-compliant getter for defaultGateway.

        Returns:
            The defaultGateway value

        Note:
            Delegates to default_gateway property (CODING_RULE_V2_00017)
        """
        return self.default_gateway  # Delegates to property

    def setDefaultGateway(self, value: Ip4AddressString) -> Ipv4DhcpServerConfiguration:
        """
        AUTOSAR-compliant setter for defaultGateway with method chaining.

        Args:
            value: The defaultGateway to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_gateway property setter (gets validation automatically)
        """
        self.default_gateway = value  # Delegates to property setter
        return self

    def getDefaultLease(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for defaultLease.

        Returns:
            The defaultLease value

        Note:
            Delegates to default_lease property (CODING_RULE_V2_00017)
        """
        return self.default_lease  # Delegates to property

    def setDefaultLease(self, value: TimeValue) -> Ipv4DhcpServerConfiguration:
        """
        AUTOSAR-compliant setter for defaultLease with method chaining.

        Args:
            value: The defaultLease to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_lease property setter (gets validation automatically)
        """
        self.default_lease = value  # Delegates to property setter
        return self

    def getDnsServer(self) -> List[Ip4AddressString]:
        """
        AUTOSAR-compliant getter for dnsServer.

        Returns:
            The dnsServer value

        Note:
            Delegates to dns_server property (CODING_RULE_V2_00017)
        """
        return self.dns_server  # Delegates to property

    def getNetworkMask(self) -> Ip4AddressString:
        """
        AUTOSAR-compliant getter for networkMask.

        Returns:
            The networkMask value

        Note:
            Delegates to network_mask property (CODING_RULE_V2_00017)
        """
        return self.network_mask  # Delegates to property

    def setNetworkMask(self, value: Ip4AddressString) -> Ipv4DhcpServerConfiguration:
        """
        AUTOSAR-compliant setter for networkMask with method chaining.

        Args:
            value: The networkMask to set

        Returns:
            self for method chaining

        Note:
            Delegates to network_mask property setter (gets validation automatically)
        """
        self.network_mask = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_address_range(self, value: Optional[Ip4AddressString]) -> Ipv4DhcpServerConfiguration:
        """
        Set addressRange and return self for chaining.

        Args:
            value: The addressRange to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_address_range("value")
        """
        self.address_range = value  # Use property setter (gets validation)
        return self

    def with_default_gateway(self, value: Optional[Ip4AddressString]) -> Ipv4DhcpServerConfiguration:
        """
        Set defaultGateway and return self for chaining.

        Args:
            value: The defaultGateway to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_gateway("value")
        """
        self.default_gateway = value  # Use property setter (gets validation)
        return self

    def with_default_lease(self, value: Optional[TimeValue]) -> Ipv4DhcpServerConfiguration:
        """
        Set defaultLease and return self for chaining.

        Args:
            value: The defaultLease to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_lease("value")
        """
        self.default_lease = value  # Use property setter (gets validation)
        return self

    def with_network_mask(self, value: Optional[Ip4AddressString]) -> Ipv4DhcpServerConfiguration:
        """
        Set networkMask and return self for chaining.

        Args:
            value: The networkMask to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network_mask("value")
        """
        self.network_mask = value  # Use property setter (gets validation)
        return self



class Ipv6DhcpServerConfiguration(Describable):
    """
    Defines the configuration of a IPv6 DHCP server that runs on the network
    endpoint.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv6DhcpServerConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 132, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Upper range of IP addresses to be issued to DHCP IPv6 Address.
        # Notation: FFFF:.
        # :FFFF.
        self._addressRange: Optional[Ip6AddressString] = None

    @property
    def address_range(self) -> Optional[Ip6AddressString]:
        """Get addressRange (Pythonic accessor)."""
        return self._addressRange

    @address_range.setter
    def address_range(self, value: Optional[Ip6AddressString]) -> None:
        """
        Set addressRange with validation.

        Args:
            value: The addressRange to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._addressRange = None
            return

        if not isinstance(value, Ip6AddressString):
            raise TypeError(
                f"addressRange must be Ip6AddressString or None, got {type(value).__name__}"
            )
        self._addressRange = value
        # Notation.
        self._defaultGateway: Optional[Ip6AddressString] = None

    @property
    def default_gateway(self) -> Optional[Ip6AddressString]:
        """Get defaultGateway (Pythonic accessor)."""
        return self._defaultGateway

    @default_gateway.setter
    def default_gateway(self, value: Optional[Ip6AddressString]) -> None:
        """
        Set defaultGateway with validation.

        Args:
            value: The defaultGateway to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultGateway = None
            return

        if not isinstance(value, Ip6AddressString):
            raise TypeError(
                f"defaultGateway must be Ip6AddressString or None, got {type(value).__name__}"
            )
        self._defaultGateway = value
        self._defaultLease: Optional[TimeValue] = None

    @property
    def default_lease(self) -> Optional[TimeValue]:
        """Get defaultLease (Pythonic accessor)."""
        return self._defaultLease

    @default_lease.setter
    def default_lease(self, value: Optional[TimeValue]) -> None:
        """
        Set defaultLease with validation.

        Args:
            value: The defaultLease to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultLease = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"defaultLease must be TimeValue or None, got {type(value).__name__}"
            )
        self._defaultLease = value
        # Notation:.
        self._dnsServer: List[Ip6AddressString] = []

    @property
    def dns_server(self) -> List[Ip6AddressString]:
        """Get dnsServer (Pythonic accessor)."""
        return self._dnsServer
        # Default network mask to be used by DHCP clients.
        self._networkMask: Optional[Ip6AddressString] = None

    @property
    def network_mask(self) -> Optional[Ip6AddressString]:
        """Get networkMask (Pythonic accessor)."""
        return self._networkMask

    @network_mask.setter
    def network_mask(self, value: Optional[Ip6AddressString]) -> None:
        """
        Set networkMask with validation.

        Args:
            value: The networkMask to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._networkMask = None
            return

        if not isinstance(value, Ip6AddressString):
            raise TypeError(
                f"networkMask must be Ip6AddressString or None, got {type(value).__name__}"
            )
        self._networkMask = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAddressRange(self) -> Ip6AddressString:
        """
        AUTOSAR-compliant getter for addressRange.

        Returns:
            The addressRange value

        Note:
            Delegates to address_range property (CODING_RULE_V2_00017)
        """
        return self.address_range  # Delegates to property

    def setAddressRange(self, value: Ip6AddressString) -> Ipv6DhcpServerConfiguration:
        """
        AUTOSAR-compliant setter for addressRange with method chaining.

        Args:
            value: The addressRange to set

        Returns:
            self for method chaining

        Note:
            Delegates to address_range property setter (gets validation automatically)
        """
        self.address_range = value  # Delegates to property setter
        return self

    def getDefaultGateway(self) -> Ip6AddressString:
        """
        AUTOSAR-compliant getter for defaultGateway.

        Returns:
            The defaultGateway value

        Note:
            Delegates to default_gateway property (CODING_RULE_V2_00017)
        """
        return self.default_gateway  # Delegates to property

    def setDefaultGateway(self, value: Ip6AddressString) -> Ipv6DhcpServerConfiguration:
        """
        AUTOSAR-compliant setter for defaultGateway with method chaining.

        Args:
            value: The defaultGateway to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_gateway property setter (gets validation automatically)
        """
        self.default_gateway = value  # Delegates to property setter
        return self

    def getDefaultLease(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for defaultLease.

        Returns:
            The defaultLease value

        Note:
            Delegates to default_lease property (CODING_RULE_V2_00017)
        """
        return self.default_lease  # Delegates to property

    def setDefaultLease(self, value: TimeValue) -> Ipv6DhcpServerConfiguration:
        """
        AUTOSAR-compliant setter for defaultLease with method chaining.

        Args:
            value: The defaultLease to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_lease property setter (gets validation automatically)
        """
        self.default_lease = value  # Delegates to property setter
        return self

    def getDnsServer(self) -> List[Ip6AddressString]:
        """
        AUTOSAR-compliant getter for dnsServer.

        Returns:
            The dnsServer value

        Note:
            Delegates to dns_server property (CODING_RULE_V2_00017)
        """
        return self.dns_server  # Delegates to property

    def getNetworkMask(self) -> Ip6AddressString:
        """
        AUTOSAR-compliant getter for networkMask.

        Returns:
            The networkMask value

        Note:
            Delegates to network_mask property (CODING_RULE_V2_00017)
        """
        return self.network_mask  # Delegates to property

    def setNetworkMask(self, value: Ip6AddressString) -> Ipv6DhcpServerConfiguration:
        """
        AUTOSAR-compliant setter for networkMask with method chaining.

        Args:
            value: The networkMask to set

        Returns:
            self for method chaining

        Note:
            Delegates to network_mask property setter (gets validation automatically)
        """
        self.network_mask = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_address_range(self, value: Optional[Ip6AddressString]) -> Ipv6DhcpServerConfiguration:
        """
        Set addressRange and return self for chaining.

        Args:
            value: The addressRange to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_address_range("value")
        """
        self.address_range = value  # Use property setter (gets validation)
        return self

    def with_default_gateway(self, value: Optional[Ip6AddressString]) -> Ipv6DhcpServerConfiguration:
        """
        Set defaultGateway and return self for chaining.

        Args:
            value: The defaultGateway to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_gateway("value")
        """
        self.default_gateway = value  # Use property setter (gets validation)
        return self

    def with_default_lease(self, value: Optional[TimeValue]) -> Ipv6DhcpServerConfiguration:
        """
        Set defaultLease and return self for chaining.

        Args:
            value: The defaultLease to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_lease("value")
        """
        self.default_lease = value  # Use property setter (gets validation)
        return self

    def with_network_mask(self, value: Optional[Ip6AddressString]) -> Ipv6DhcpServerConfiguration:
        """
        Set networkMask and return self for chaining.

        Args:
            value: The networkMask to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network_mask("value")
        """
        self.network_mask = value  # Use property setter (gets validation)
        return self



class CouplingElementAbstractDetails(Identifiable, ABC):
    """
    Collection of specific details for the CouplingElement.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingElementAbstractDetails

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 133, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is CouplingElementAbstractDetails:
            raise TypeError("CouplingElementAbstractDetails is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SwitchStreamIdentification(Identifiable):
    """
    SwitchStreamIdentification

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::SwitchStreamIdentification

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 135, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the CouplingPort to be taken into account as role for this
        # SwitchStreamIdentification.
        self._egressPort: List[CouplingPort] = []

    @property
    def egress_port(self) -> List[CouplingPort]:
        """Get egressPort (Pythonic accessor)."""
        return self._egressPort
        # Enables Blocking all frames from the MAC address.
        # atp.
        # Status=candidate.
        self._filterActionBlock: Optional[Boolean] = None

    @property
    def filter_action_block(self) -> Optional[Boolean]:
        """Get filterActionBlock (Pythonic accessor)."""
        return self._filterActionBlock

    @filter_action_block.setter
    def filter_action_block(self, value: Optional[Boolean]) -> None:
        """
        Set filterActionBlock with validation.

        Args:
            value: The filterActionBlock to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filterActionBlock = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"filterActionBlock must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._filterActionBlock = value
        # forwarding process for an Ethernet frame.
        self._filterActionDest: Optional[SwitchStreamFilterEnum] = None

    @property
    def filter_action_dest(self) -> Optional[SwitchStreamFilterEnum]:
        """Get filterActionDest (Pythonic accessor)."""
        return self._filterActionDest

    @filter_action_dest.setter
    def filter_action_dest(self, value: Optional[SwitchStreamFilterEnum]) -> None:
        """
        Set filterActionDest with validation.

        Args:
            value: The filterActionDest to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filterActionDest = None
            return

        if not isinstance(value, SwitchStreamFilter):
            raise TypeError(
                f"filterActionDest must be SwitchStreamFilter or None, got {type(value).__name__}"
            )
        self._filterActionDest = value
        # atp.
        # Status=candidate.
        self._filterActionDrop: Optional[Boolean] = None

    @property
    def filter_action_drop(self) -> Optional[Boolean]:
        """Get filterActionDrop (Pythonic accessor)."""
        return self._filterActionDrop

    @filter_action_drop.setter
    def filter_action_drop(self, value: Optional[Boolean]) -> None:
        """
        Set filterActionDrop with validation.

        Args:
            value: The filterActionDrop to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filterActionDrop = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"filterActionDrop must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._filterActionDrop = value
        self._filterActionVlan: Optional[PositiveInteger] = None

    @property
    def filter_action_vlan(self) -> Optional[PositiveInteger]:
        """Get filterActionVlan (Pythonic accessor)."""
        return self._filterActionVlan

    @filter_action_vlan.setter
    def filter_action_vlan(self, value: Optional[PositiveInteger]) -> None:
        """
        Set filterActionVlan with validation.

        Args:
            value: The filterActionVlan to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filterActionVlan = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"filterActionVlan must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._filterActionVlan = value
        # SwitchStreamIdentification.
        self._ingressPort: List[CouplingPort] = []

    @property
    def ingress_port(self) -> List[CouplingPort]:
        """Get ingressPort (Pythonic accessor)."""
        return self._ingressPort
        # Definition of a stream filter rule for this SwitchStream.
        self._streamFilter: Optional[SwitchStreamFilterRule] = None

    @property
    def stream_filter(self) -> Optional[SwitchStreamFilterRule]:
        """Get streamFilter (Pythonic accessor)."""
        return self._streamFilter

    @stream_filter.setter
    def stream_filter(self, value: Optional[SwitchStreamFilterRule]) -> None:
        """
        Set streamFilter with validation.

        Args:
            value: The streamFilter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._streamFilter = None
            return

        if not isinstance(value, SwitchStreamFilterRule):
            raise TypeError(
                f"streamFilter must be SwitchStreamFilterRule or None, got {type(value).__name__}"
            )
        self._streamFilter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEgressPort(self) -> List[CouplingPort]:
        """
        AUTOSAR-compliant getter for egressPort.

        Returns:
            The egressPort value

        Note:
            Delegates to egress_port property (CODING_RULE_V2_00017)
        """
        return self.egress_port  # Delegates to property

    def getFilterActionBlock(self) -> Boolean:
        """
        AUTOSAR-compliant getter for filterActionBlock.

        Returns:
            The filterActionBlock value

        Note:
            Delegates to filter_action_block property (CODING_RULE_V2_00017)
        """
        return self.filter_action_block  # Delegates to property

    def setFilterActionBlock(self, value: Boolean) -> SwitchStreamIdentification:
        """
        AUTOSAR-compliant setter for filterActionBlock with method chaining.

        Args:
            value: The filterActionBlock to set

        Returns:
            self for method chaining

        Note:
            Delegates to filter_action_block property setter (gets validation automatically)
        """
        self.filter_action_block = value  # Delegates to property setter
        return self

    def getFilterActionDest(self) -> SwitchStreamFilterEnum:
        """
        AUTOSAR-compliant getter for filterActionDest.

        Returns:
            The filterActionDest value

        Note:
            Delegates to filter_action_dest property (CODING_RULE_V2_00017)
        """
        return self.filter_action_dest  # Delegates to property

    def setFilterActionDest(self, value: SwitchStreamFilterEnum) -> SwitchStreamIdentification:
        """
        AUTOSAR-compliant setter for filterActionDest with method chaining.

        Args:
            value: The filterActionDest to set

        Returns:
            self for method chaining

        Note:
            Delegates to filter_action_dest property setter (gets validation automatically)
        """
        self.filter_action_dest = value  # Delegates to property setter
        return self

    def getFilterActionDrop(self) -> Boolean:
        """
        AUTOSAR-compliant getter for filterActionDrop.

        Returns:
            The filterActionDrop value

        Note:
            Delegates to filter_action_drop property (CODING_RULE_V2_00017)
        """
        return self.filter_action_drop  # Delegates to property

    def setFilterActionDrop(self, value: Boolean) -> SwitchStreamIdentification:
        """
        AUTOSAR-compliant setter for filterActionDrop with method chaining.

        Args:
            value: The filterActionDrop to set

        Returns:
            self for method chaining

        Note:
            Delegates to filter_action_drop property setter (gets validation automatically)
        """
        self.filter_action_drop = value  # Delegates to property setter
        return self

    def getFilterActionVlan(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for filterActionVlan.

        Returns:
            The filterActionVlan value

        Note:
            Delegates to filter_action_vlan property (CODING_RULE_V2_00017)
        """
        return self.filter_action_vlan  # Delegates to property

    def setFilterActionVlan(self, value: PositiveInteger) -> SwitchStreamIdentification:
        """
        AUTOSAR-compliant setter for filterActionVlan with method chaining.

        Args:
            value: The filterActionVlan to set

        Returns:
            self for method chaining

        Note:
            Delegates to filter_action_vlan property setter (gets validation automatically)
        """
        self.filter_action_vlan = value  # Delegates to property setter
        return self

    def getIngressPort(self) -> List[CouplingPort]:
        """
        AUTOSAR-compliant getter for ingressPort.

        Returns:
            The ingressPort value

        Note:
            Delegates to ingress_port property (CODING_RULE_V2_00017)
        """
        return self.ingress_port  # Delegates to property

    def getStreamFilter(self) -> SwitchStreamFilterRule:
        """
        AUTOSAR-compliant getter for streamFilter.

        Returns:
            The streamFilter value

        Note:
            Delegates to stream_filter property (CODING_RULE_V2_00017)
        """
        return self.stream_filter  # Delegates to property

    def setStreamFilter(self, value: SwitchStreamFilterRule) -> SwitchStreamIdentification:
        """
        AUTOSAR-compliant setter for streamFilter with method chaining.

        Args:
            value: The streamFilter to set

        Returns:
            self for method chaining

        Note:
            Delegates to stream_filter property setter (gets validation automatically)
        """
        self.stream_filter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_filter_action_block(self, value: Optional[Boolean]) -> SwitchStreamIdentification:
        """
        Set filterActionBlock and return self for chaining.

        Args:
            value: The filterActionBlock to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_filter_action_block("value")
        """
        self.filter_action_block = value  # Use property setter (gets validation)
        return self

    def with_filter_action_dest(self, value: Optional[SwitchStreamFilterEnum]) -> SwitchStreamIdentification:
        """
        Set filterActionDest and return self for chaining.

        Args:
            value: The filterActionDest to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_filter_action_dest("value")
        """
        self.filter_action_dest = value  # Use property setter (gets validation)
        return self

    def with_filter_action_drop(self, value: Optional[Boolean]) -> SwitchStreamIdentification:
        """
        Set filterActionDrop and return self for chaining.

        Args:
            value: The filterActionDrop to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_filter_action_drop("value")
        """
        self.filter_action_drop = value  # Use property setter (gets validation)
        return self

    def with_filter_action_vlan(self, value: Optional[PositiveInteger]) -> SwitchStreamIdentification:
        """
        Set filterActionVlan and return self for chaining.

        Args:
            value: The filterActionVlan to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_filter_action_vlan("value")
        """
        self.filter_action_vlan = value  # Use property setter (gets validation)
        return self

    def with_stream_filter(self, value: Optional[SwitchStreamFilterRule]) -> SwitchStreamIdentification:
        """
        Set streamFilter and return self for chaining.

        Args:
            value: The streamFilter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_stream_filter("value")
        """
        self.stream_filter = value  # Use property setter (gets validation)
        return self



class SwitchStreamFilterRule(Identifiable):
    """
    SwitchStreamIdentification

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::SwitchStreamFilterRule

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 136, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of a filter rule on the data link layer.
        # Tags: atp.
        # Status=candidate.
        self._dataLinkLayer: Optional[StreamFilterRuleDataLinkLayer] = None

    @property
    def data_link_layer(self) -> Optional[StreamFilterRuleDataLinkLayer]:
        """Get dataLinkLayer (Pythonic accessor)."""
        return self._dataLinkLayer

    @data_link_layer.setter
    def data_link_layer(self, value: Optional[StreamFilterRuleDataLinkLayer]) -> None:
        """
        Set dataLinkLayer with validation.

        Args:
            value: The dataLinkLayer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataLinkLayer = None
            return

        if not isinstance(value, StreamFilterRuleData):
            raise TypeError(
                f"dataLinkLayer must be StreamFilterRuleData or None, got {type(value).__name__}"
            )
        self._dataLinkLayer = value
        # Tags: atp.
        # Status=candidate.
        self._ieee1722Tp: Optional[StreamFilterIEEE1722Configuration] = None

    @property
    def ieee1722_tp(self) -> Optional[StreamFilterIEEE1722Configuration]:
        """Get ieee1722Tp (Pythonic accessor)."""
        return self._ieee1722Tp

    @ieee1722_tp.setter
    def ieee1722_tp(self, value: Optional[StreamFilterIEEE1722Configuration]) -> None:
        """
        Set ieee1722Tp with validation.

        Args:
            value: The ieee1722Tp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ieee1722Tp = None
            return

        if not isinstance(value, StreamFilterIEEE1722):
            raise TypeError(
                f"ieee1722Tp must be StreamFilterIEEE1722 or None, got {type(value).__name__}"
            )
        self._ieee1722Tp = value
        # Definition of a filter rule IP and TP.
        self._ipTpRule: Optional[StreamFilterRuleIpTp] = None

    @property
    def ip_tp_rule(self) -> Optional[StreamFilterRuleIpTp]:
        """Get ipTpRule (Pythonic accessor)."""
        return self._ipTpRule

    @ip_tp_rule.setter
    def ip_tp_rule(self, value: Optional[StreamFilterRuleIpTp]) -> None:
        """
        Set ipTpRule with validation.

        Args:
            value: The ipTpRule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipTpRule = None
            return

        if not isinstance(value, StreamFilterRuleIpTp):
            raise TypeError(
                f"ipTpRule must be StreamFilterRuleIpTp or None, got {type(value).__name__}"
            )
        self._ipTpRule = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataLinkLayer(self) -> StreamFilterRuleDataLinkLayer:
        """
        AUTOSAR-compliant getter for dataLinkLayer.

        Returns:
            The dataLinkLayer value

        Note:
            Delegates to data_link_layer property (CODING_RULE_V2_00017)
        """
        return self.data_link_layer  # Delegates to property

    def setDataLinkLayer(self, value: StreamFilterRuleDataLinkLayer) -> SwitchStreamFilterRule:
        """
        AUTOSAR-compliant setter for dataLinkLayer with method chaining.

        Args:
            value: The dataLinkLayer to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_link_layer property setter (gets validation automatically)
        """
        self.data_link_layer = value  # Delegates to property setter
        return self

    def getIeee1722Tp(self) -> StreamFilterIEEE1722Configuration:
        """
        AUTOSAR-compliant getter for ieee1722Tp.

        Returns:
            The ieee1722Tp value

        Note:
            Delegates to ieee1722_tp property (CODING_RULE_V2_00017)
        """
        return self.ieee1722_tp  # Delegates to property

    def setIeee1722Tp(self, value: StreamFilterIEEE1722Configuration) -> SwitchStreamFilterRule:
        """
        AUTOSAR-compliant setter for ieee1722Tp with method chaining.

        Args:
            value: The ieee1722Tp to set

        Returns:
            self for method chaining

        Note:
            Delegates to ieee1722_tp property setter (gets validation automatically)
        """
        self.ieee1722_tp = value  # Delegates to property setter
        return self

    def getIpTpRule(self) -> StreamFilterRuleIpTp:
        """
        AUTOSAR-compliant getter for ipTpRule.

        Returns:
            The ipTpRule value

        Note:
            Delegates to ip_tp_rule property (CODING_RULE_V2_00017)
        """
        return self.ip_tp_rule  # Delegates to property

    def setIpTpRule(self, value: StreamFilterRuleIpTp) -> SwitchStreamFilterRule:
        """
        AUTOSAR-compliant setter for ipTpRule with method chaining.

        Args:
            value: The ipTpRule to set

        Returns:
            self for method chaining

        Note:
            Delegates to ip_tp_rule property setter (gets validation automatically)
        """
        self.ip_tp_rule = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_link_layer(self, value: Optional[StreamFilterRuleDataLinkLayer]) -> SwitchStreamFilterRule:
        """
        Set dataLinkLayer and return self for chaining.

        Args:
            value: The dataLinkLayer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_link_layer("value")
        """
        self.data_link_layer = value  # Use property setter (gets validation)
        return self

    def with_ieee1722_tp(self, value: Optional[StreamFilterIEEE1722Configuration]) -> SwitchStreamFilterRule:
        """
        Set ieee1722Tp and return self for chaining.

        Args:
            value: The ieee1722Tp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ieee1722_tp("value")
        """
        self.ieee1722_tp = value  # Use property setter (gets validation)
        return self

    def with_ip_tp_rule(self, value: Optional[StreamFilterRuleIpTp]) -> SwitchStreamFilterRule:
        """
        Set ipTpRule and return self for chaining.

        Args:
            value: The ipTpRule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ip_tp_rule("value")
        """
        self.ip_tp_rule = value  # Use property setter (gets validation)
        return self



class StreamFilterRuleDataLinkLayer(ARObject):
    """
    Configuration of filter rules on the DataLink layer

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::StreamFilterRuleDataLinkLayer

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 137, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Filter to match packets with the destination MAC address/ mask.
        self._destinationMac: Optional[StreamFilterMACConfiguration] = None

    @property
    def destination_mac(self) -> Optional[StreamFilterMACConfiguration]:
        """Get destinationMac (Pythonic accessor)."""
        return self._destinationMac

    @destination_mac.setter
    def destination_mac(self, value: Optional[StreamFilterMACConfiguration]) -> None:
        """
        Set destinationMac with validation.

        Args:
            value: The destinationMac to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationMac = None
            return

        if not isinstance(value, StreamFilterMAC):
            raise TypeError(
                f"destinationMac must be StreamFilterMAC or None, got {type(value).__name__}"
            )
        self._destinationMac = value
        self._etherType: Optional[PositiveInteger] = None

    @property
    def ether_type(self) -> Optional[PositiveInteger]:
        """Get etherType (Pythonic accessor)."""
        return self._etherType

    @ether_type.setter
    def ether_type(self, value: Optional[PositiveInteger]) -> None:
        """
        Set etherType with validation.

        Args:
            value: The etherType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._etherType = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"etherType must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._etherType = value
        self._sourceMac: Optional[StreamFilterMACConfiguration] = None

    @property
    def source_mac(self) -> Optional[StreamFilterMACConfiguration]:
        """Get sourceMac (Pythonic accessor)."""
        return self._sourceMac

    @source_mac.setter
    def source_mac(self, value: Optional[StreamFilterMACConfiguration]) -> None:
        """
        Set sourceMac with validation.

        Args:
            value: The sourceMac to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceMac = None
            return

        if not isinstance(value, StreamFilterMAC):
            raise TypeError(
                f"sourceMac must be StreamFilterMAC or None, got {type(value).__name__}"
            )
        self._sourceMac = value
        self._vlanId: Optional[PositiveInteger] = None

    @property
    def vlan_id(self) -> Optional[PositiveInteger]:
        """Get vlanId (Pythonic accessor)."""
        return self._vlanId

    @vlan_id.setter
    def vlan_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set vlanId with validation.

        Args:
            value: The vlanId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlanId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"vlanId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._vlanId = value
        self._vlanPriority: Optional[PositiveInteger] = None

    @property
    def vlan_priority(self) -> Optional[PositiveInteger]:
        """Get vlanPriority (Pythonic accessor)."""
        return self._vlanPriority

    @vlan_priority.setter
    def vlan_priority(self, value: Optional[PositiveInteger]) -> None:
        """
        Set vlanPriority with validation.

        Args:
            value: The vlanPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlanPriority = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"vlanPriority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._vlanPriority = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationMac(self) -> StreamFilterMACConfiguration:
        """
        AUTOSAR-compliant getter for destinationMac.

        Returns:
            The destinationMac value

        Note:
            Delegates to destination_mac property (CODING_RULE_V2_00017)
        """
        return self.destination_mac  # Delegates to property

    def setDestinationMac(self, value: StreamFilterMACConfiguration) -> StreamFilterRuleDataLinkLayer:
        """
        AUTOSAR-compliant setter for destinationMac with method chaining.

        Args:
            value: The destinationMac to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination_mac property setter (gets validation automatically)
        """
        self.destination_mac = value  # Delegates to property setter
        return self

    def getEtherType(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for etherType.

        Returns:
            The etherType value

        Note:
            Delegates to ether_type property (CODING_RULE_V2_00017)
        """
        return self.ether_type  # Delegates to property

    def setEtherType(self, value: PositiveInteger) -> StreamFilterRuleDataLinkLayer:
        """
        AUTOSAR-compliant setter for etherType with method chaining.

        Args:
            value: The etherType to set

        Returns:
            self for method chaining

        Note:
            Delegates to ether_type property setter (gets validation automatically)
        """
        self.ether_type = value  # Delegates to property setter
        return self

    def getSourceMac(self) -> StreamFilterMACConfiguration:
        """
        AUTOSAR-compliant getter for sourceMac.

        Returns:
            The sourceMac value

        Note:
            Delegates to source_mac property (CODING_RULE_V2_00017)
        """
        return self.source_mac  # Delegates to property

    def setSourceMac(self, value: StreamFilterMACConfiguration) -> StreamFilterRuleDataLinkLayer:
        """
        AUTOSAR-compliant setter for sourceMac with method chaining.

        Args:
            value: The sourceMac to set

        Returns:
            self for method chaining

        Note:
            Delegates to source_mac property setter (gets validation automatically)
        """
        self.source_mac = value  # Delegates to property setter
        return self

    def getVlanId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for vlanId.

        Returns:
            The vlanId value

        Note:
            Delegates to vlan_id property (CODING_RULE_V2_00017)
        """
        return self.vlan_id  # Delegates to property

    def setVlanId(self, value: PositiveInteger) -> StreamFilterRuleDataLinkLayer:
        """
        AUTOSAR-compliant setter for vlanId with method chaining.

        Args:
            value: The vlanId to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan_id property setter (gets validation automatically)
        """
        self.vlan_id = value  # Delegates to property setter
        return self

    def getVlanPriority(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for vlanPriority.

        Returns:
            The vlanPriority value

        Note:
            Delegates to vlan_priority property (CODING_RULE_V2_00017)
        """
        return self.vlan_priority  # Delegates to property

    def setVlanPriority(self, value: PositiveInteger) -> StreamFilterRuleDataLinkLayer:
        """
        AUTOSAR-compliant setter for vlanPriority with method chaining.

        Args:
            value: The vlanPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan_priority property setter (gets validation automatically)
        """
        self.vlan_priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination_mac(self, value: Optional[StreamFilterMACConfiguration]) -> StreamFilterRuleDataLinkLayer:
        """
        Set destinationMac and return self for chaining.

        Args:
            value: The destinationMac to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_mac("value")
        """
        self.destination_mac = value  # Use property setter (gets validation)
        return self

    def with_ether_type(self, value: Optional[PositiveInteger]) -> StreamFilterRuleDataLinkLayer:
        """
        Set etherType and return self for chaining.

        Args:
            value: The etherType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ether_type("value")
        """
        self.ether_type = value  # Use property setter (gets validation)
        return self

    def with_source_mac(self, value: Optional[StreamFilterMACConfiguration]) -> StreamFilterRuleDataLinkLayer:
        """
        Set sourceMac and return self for chaining.

        Args:
            value: The sourceMac to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source_mac("value")
        """
        self.source_mac = value  # Use property setter (gets validation)
        return self

    def with_vlan_id(self, value: Optional[PositiveInteger]) -> StreamFilterRuleDataLinkLayer:
        """
        Set vlanId and return self for chaining.

        Args:
            value: The vlanId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan_id("value")
        """
        self.vlan_id = value  # Use property setter (gets validation)
        return self

    def with_vlan_priority(self, value: Optional[PositiveInteger]) -> StreamFilterRuleDataLinkLayer:
        """
        Set vlanPriority and return self for chaining.

        Args:
            value: The vlanPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan_priority("value")
        """
        self.vlan_priority = value  # Use property setter (gets validation)
        return self



class StreamFilterMACAddress(ARObject):
    """
    Configuration of filter rules on the DataLink layer

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::StreamFilterMACAddress

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 137, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Filter to match packets with the MAC address range.
        # atp.
        # Status=candidate.
        self._macAddress: Optional[MacAddressString] = None

    @property
    def mac_address(self) -> Optional[MacAddressString]:
        """Get macAddress (Pythonic accessor)."""
        return self._macAddress

    @mac_address.setter
    def mac_address(self, value: Optional[MacAddressString]) -> None:
        """
        Set macAddress with validation.

        Args:
            value: The macAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macAddress = None
            return

        if not isinstance(value, MacAddressString):
            raise TypeError(
                f"macAddress must be MacAddressString or None, got {type(value).__name__}"
            )
        self._macAddress = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMacAddress(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for macAddress.

        Returns:
            The macAddress value

        Note:
            Delegates to mac_address property (CODING_RULE_V2_00017)
        """
        return self.mac_address  # Delegates to property

    def setMacAddress(self, value: "MacAddressString") -> StreamFilterMACAddress:
        """
        AUTOSAR-compliant setter for macAddress with method chaining.

        Args:
            value: The macAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to mac_address property setter (gets validation automatically)
        """
        self.mac_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mac_address(self, value: Optional[MacAddressString]) -> StreamFilterMACAddress:
        """
        Set macAddress and return self for chaining.

        Args:
            value: The macAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mac_address("value")
        """
        self.mac_address = value  # Use property setter (gets validation)
        return self



class StreamFilterRuleIpTp(ARObject):
    """
    Configuration of filter rules for IP and TP.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::StreamFilterRuleIpTp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 137, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Filter to match packets with the destination IPv6 address range.
        self._destination: Optional[StreamFilterIpv6Configuration] = None

    @property
    def destination(self) -> Optional[StreamFilterIpv6Configuration]:
        """Get destination (Pythonic accessor)."""
        return self._destination

    @destination.setter
    def destination(self, value: Optional[StreamFilterIpv6Configuration]) -> None:
        """
        Set destination with validation.

        Args:
            value: The destination to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destination = None
            return

        if not isinstance(value, StreamFilterIpv6):
            raise TypeError(
                f"destination must be StreamFilterIpv6 or None, got {type(value).__name__}"
            )
        self._destination = value
        self._destinationPort: List[StreamFilterPortRange] = []

    @property
    def destination_port(self) -> List[StreamFilterPortRange]:
        """Get destinationPort (Pythonic accessor)."""
        return self._destinationPort
        # Filter to match packets with the source IPv6 address range.
        self._source: Optional[StreamFilterIpv6Configuration] = None

    @property
    def source(self) -> Optional[StreamFilterIpv6Configuration]:
        """Get source (Pythonic accessor)."""
        return self._source

    @source.setter
    def source(self, value: Optional[StreamFilterIpv6Configuration]) -> None:
        """
        Set source with validation.

        Args:
            value: The source to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._source = None
            return

        if not isinstance(value, StreamFilterIpv6):
            raise TypeError(
                f"source must be StreamFilterIpv6 or None, got {type(value).__name__}"
            )
        self._source = value
        self._sourcePort: List[StreamFilterPortRange] = []

    @property
    def source_port(self) -> List[StreamFilterPortRange]:
        """Get sourcePort (Pythonic accessor)."""
        return self._sourcePort

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestination(self) -> StreamFilterIpv6Configuration:
        """
        AUTOSAR-compliant getter for destination.

        Returns:
            The destination value

        Note:
            Delegates to destination property (CODING_RULE_V2_00017)
        """
        return self.destination  # Delegates to property

    def setDestination(self, value: StreamFilterIpv6Configuration) -> StreamFilterRuleIpTp:
        """
        AUTOSAR-compliant setter for destination with method chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination property setter (gets validation automatically)
        """
        self.destination = value  # Delegates to property setter
        return self

    def getDestinationPort(self) -> List[StreamFilterPortRange]:
        """
        AUTOSAR-compliant getter for destinationPort.

        Returns:
            The destinationPort value

        Note:
            Delegates to destination_port property (CODING_RULE_V2_00017)
        """
        return self.destination_port  # Delegates to property

    def getSource(self) -> StreamFilterIpv6Configuration:
        """
        AUTOSAR-compliant getter for source.

        Returns:
            The source value

        Note:
            Delegates to source property (CODING_RULE_V2_00017)
        """
        return self.source  # Delegates to property

    def setSource(self, value: StreamFilterIpv6Configuration) -> StreamFilterRuleIpTp:
        """
        AUTOSAR-compliant setter for source with method chaining.

        Args:
            value: The source to set

        Returns:
            self for method chaining

        Note:
            Delegates to source property setter (gets validation automatically)
        """
        self.source = value  # Delegates to property setter
        return self

    def getSourcePort(self) -> List[StreamFilterPortRange]:
        """
        AUTOSAR-compliant getter for sourcePort.

        Returns:
            The sourcePort value

        Note:
            Delegates to source_port property (CODING_RULE_V2_00017)
        """
        return self.source_port  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination(self, value: Optional[StreamFilterIpv6Configuration]) -> StreamFilterRuleIpTp:
        """
        Set destination and return self for chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination("value")
        """
        self.destination = value  # Use property setter (gets validation)
        return self

    def with_source(self, value: Optional[StreamFilterIpv6Configuration]) -> StreamFilterRuleIpTp:
        """
        Set source and return self for chaining.

        Args:
            value: The source to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source("value")
        """
        self.source = value  # Use property setter (gets validation)
        return self



class StreamFilterIpv4Address(ARObject):
    """
    IPv4 address range definition.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::StreamFilterIpv4Address

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 138, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Filter to match packets with the IPv4 address range.
        # atp.
        # Status=candidate.
        self._ipv4Address: Optional[Ip4AddressString] = None

    @property
    def ipv4_address(self) -> Optional[Ip4AddressString]:
        """Get ipv4Address (Pythonic accessor)."""
        return self._ipv4Address

    @ipv4_address.setter
    def ipv4_address(self, value: Optional[Ip4AddressString]) -> None:
        """
        Set ipv4Address with validation.

        Args:
            value: The ipv4Address to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv4Address = None
            return

        if not isinstance(value, Ip4AddressString):
            raise TypeError(
                f"ipv4Address must be Ip4AddressString or None, got {type(value).__name__}"
            )
        self._ipv4Address = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIpv4Address(self) -> Ip4AddressString:
        """
        AUTOSAR-compliant getter for ipv4Address.

        Returns:
            The ipv4Address value

        Note:
            Delegates to ipv4_address property (CODING_RULE_V2_00017)
        """
        return self.ipv4_address  # Delegates to property

    def setIpv4Address(self, value: Ip4AddressString) -> StreamFilterIpv4Address:
        """
        AUTOSAR-compliant setter for ipv4Address with method chaining.

        Args:
            value: The ipv4Address to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv4_address property setter (gets validation automatically)
        """
        self.ipv4_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ipv4_address(self, value: Optional[Ip4AddressString]) -> StreamFilterIpv4Address:
        """
        Set ipv4Address and return self for chaining.

        Args:
            value: The ipv4Address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv4_address("value")
        """
        self.ipv4_address = value  # Use property setter (gets validation)
        return self



class StreamFilterIpv6Address(ARObject):
    """
    IPv6 address range definition.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::StreamFilterIpv6Address

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 138, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Filter to match packets with the IPv6 address range.
        # atp.
        # Status=candidate.
        self._ipv6Address: Optional[Ip6AddressString] = None

    @property
    def ipv6_address(self) -> Optional[Ip6AddressString]:
        """Get ipv6Address (Pythonic accessor)."""
        return self._ipv6Address

    @ipv6_address.setter
    def ipv6_address(self, value: Optional[Ip6AddressString]) -> None:
        """
        Set ipv6Address with validation.

        Args:
            value: The ipv6Address to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv6Address = None
            return

        if not isinstance(value, Ip6AddressString):
            raise TypeError(
                f"ipv6Address must be Ip6AddressString or None, got {type(value).__name__}"
            )
        self._ipv6Address = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIpv6Address(self) -> Ip6AddressString:
        """
        AUTOSAR-compliant getter for ipv6Address.

        Returns:
            The ipv6Address value

        Note:
            Delegates to ipv6_address property (CODING_RULE_V2_00017)
        """
        return self.ipv6_address  # Delegates to property

    def setIpv6Address(self, value: Ip6AddressString) -> StreamFilterIpv6Address:
        """
        AUTOSAR-compliant setter for ipv6Address with method chaining.

        Args:
            value: The ipv6Address to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv6_address property setter (gets validation automatically)
        """
        self.ipv6_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ipv6_address(self, value: Optional[Ip6AddressString]) -> StreamFilterIpv6Address:
        """
        Set ipv6Address and return self for chaining.

        Args:
            value: The ipv6Address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv6_address("value")
        """
        self.ipv6_address = value  # Use property setter (gets validation)
        return self



class StreamFilterPortRange(ARObject):
    """
    Configuration of filter rules for IP and TP.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::StreamFilterPortRange

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 139, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Filter to match packets with the maximum UDP/TCP port.
        self._max: Optional[PositiveInteger] = None

    @property
    def max(self) -> Optional[PositiveInteger]:
        """Get max (Pythonic accessor)."""
        return self._max

    @max.setter
    def max(self, value: Optional[PositiveInteger]) -> None:
        """
        Set max with validation.

        Args:
            value: The max to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._max = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"max must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._max = value
        self._min: Optional[PositiveInteger] = None

    @property
    def min(self) -> Optional[PositiveInteger]:
        """Get min (Pythonic accessor)."""
        return self._min

    @min.setter
    def min(self, value: Optional[PositiveInteger]) -> None:
        """
        Set min with validation.

        Args:
            value: The min to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._min = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"min must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._min = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMax(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for max.

        Returns:
            The max value

        Note:
            Delegates to max property (CODING_RULE_V2_00017)
        """
        return self.max  # Delegates to property

    def setMax(self, value: PositiveInteger) -> StreamFilterPortRange:
        """
        AUTOSAR-compliant setter for max with method chaining.

        Args:
            value: The max to set

        Returns:
            self for method chaining

        Note:
            Delegates to max property setter (gets validation automatically)
        """
        self.max = value  # Delegates to property setter
        return self

    def getMin(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for min.

        Returns:
            The min value

        Note:
            Delegates to min property (CODING_RULE_V2_00017)
        """
        return self.min  # Delegates to property

    def setMin(self, value: PositiveInteger) -> StreamFilterPortRange:
        """
        AUTOSAR-compliant setter for min with method chaining.

        Args:
            value: The min to set

        Returns:
            self for method chaining

        Note:
            Delegates to min property setter (gets validation automatically)
        """
        self.min = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max(self, value: Optional[PositiveInteger]) -> StreamFilterPortRange:
        """
        Set max and return self for chaining.

        Args:
            value: The max to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max("value")
        """
        self.max = value  # Use property setter (gets validation)
        return self

    def with_min(self, value: Optional[PositiveInteger]) -> StreamFilterPortRange:
        """
        Set min and return self for chaining.

        Args:
            value: The min to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min("value")
        """
        self.min = value  # Use property setter (gets validation)
        return self



class StreamFilterIEEE1722Tp(ARObject):
    """
    Configuration of filter rules for IP and TP.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::StreamFilterIEEE1722Tp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 139, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Filter to match IEEE1722Tp packets with the stream Id as 64bit stream id.
        self._streamId: Optional[PositiveUnlimitedInteger] = None

    @property
    def stream_id(self) -> Optional[PositiveUnlimitedInteger]:
        """Get streamId (Pythonic accessor)."""
        return self._streamId

    @stream_id.setter
    def stream_id(self, value: Optional[PositiveUnlimitedInteger]) -> None:
        """
        Set streamId with validation.

        Args:
            value: The streamId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._streamId = None
            return

        if not isinstance(value, PositiveUnlimitedInteger):
            raise TypeError(
                f"streamId must be PositiveUnlimitedInteger or None, got {type(value).__name__}"
            )
        self._streamId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getStreamId(self) -> PositiveUnlimitedInteger:
        """
        AUTOSAR-compliant getter for streamId.

        Returns:
            The streamId value

        Note:
            Delegates to stream_id property (CODING_RULE_V2_00017)
        """
        return self.stream_id  # Delegates to property

    def setStreamId(self, value: PositiveUnlimitedInteger) -> StreamFilterIEEE1722Tp:
        """
        AUTOSAR-compliant setter for streamId with method chaining.

        Args:
            value: The streamId to set

        Returns:
            self for method chaining

        Note:
            Delegates to stream_id property setter (gets validation automatically)
        """
        self.stream_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_stream_id(self, value: Optional[PositiveUnlimitedInteger]) -> StreamFilterIEEE1722Tp:
        """
        Set streamId and return self for chaining.

        Args:
            value: The streamId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_stream_id("value")
        """
        self.stream_id = value  # Use property setter (gets validation)
        return self



class SwitchStreamFilterActionDestPortModification(Identifiable):
    """
    Defines the action to modify the destination port(s) determined by the frame
    forwarding process for an particular Ethernet frame. Either the egress
    destination of an Ethernet frame is extended or overwritten.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::SwitchStreamFilterActionDestPortModification

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 140, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the egress ports used as the target of the to modify the egress
        # port.
        self._egressPort: List[CouplingPort] = []

    @property
    def egress_port(self) -> List[CouplingPort]:
        """Get egressPort (Pythonic accessor)."""
        return self._egressPort
        # Defines the method to modify the egress destination.
        # overwrite or extend the egress destination.
        # atp.
        # Status=candidate.
        self._modification: Optional[SwitchStreamFilterEnum] = None

    @property
    def modification(self) -> Optional[SwitchStreamFilterEnum]:
        """Get modification (Pythonic accessor)."""
        return self._modification

    @modification.setter
    def modification(self, value: Optional[SwitchStreamFilterEnum]) -> None:
        """
        Set modification with validation.

        Args:
            value: The modification to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modification = None
            return

        if not isinstance(value, SwitchStreamFilter):
            raise TypeError(
                f"modification must be SwitchStreamFilter or None, got {type(value).__name__}"
            )
        self._modification = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEgressPort(self) -> List[CouplingPort]:
        """
        AUTOSAR-compliant getter for egressPort.

        Returns:
            The egressPort value

        Note:
            Delegates to egress_port property (CODING_RULE_V2_00017)
        """
        return self.egress_port  # Delegates to property

    def getModification(self) -> SwitchStreamFilterEnum:
        """
        AUTOSAR-compliant getter for modification.

        Returns:
            The modification value

        Note:
            Delegates to modification property (CODING_RULE_V2_00017)
        """
        return self.modification  # Delegates to property

    def setModification(self, value: SwitchStreamFilterEnum) -> SwitchStreamFilterActionDestPortModification:
        """
        AUTOSAR-compliant setter for modification with method chaining.

        Args:
            value: The modification to set

        Returns:
            self for method chaining

        Note:
            Delegates to modification property setter (gets validation automatically)
        """
        self.modification = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_modification(self, value: Optional[SwitchStreamFilterEnum]) -> SwitchStreamFilterActionDestPortModification:
        """
        Set modification and return self for chaining.

        Args:
            value: The modification to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_modification("value")
        """
        self.modification = value  # Use property setter (gets validation)
        return self



class SwitchStreamFilterEntry(Identifiable):
    """
    Defines a Stream Filter Entry.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::SwitchStreamFilterEntry

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 141, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the Asynchronous Traffic Shaper (ATS).
        # Tags: atp.
        # Status=candidate Shaper.
        self._asynchronous: Optional[CouplingPort] = None

    @property
    def asynchronous(self) -> Optional[CouplingPort]:
        """Get asynchronous (Pythonic accessor)."""
        return self._asynchronous

    @asynchronous.setter
    def asynchronous(self, value: Optional[CouplingPort]) -> None:
        """
        Set asynchronous with validation.

        Args:
            value: The asynchronous to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._asynchronous = None
            return

        if not isinstance(value, CouplingPort):
            raise TypeError(
                f"asynchronous must be CouplingPort or None, got {type(value).__name__}"
            )
        self._asynchronous = value
        self._filterPriority: Optional[PositiveInteger] = None

    @property
    def filter_priority(self) -> Optional[PositiveInteger]:
        """Get filterPriority (Pythonic accessor)."""
        return self._filterPriority

    @filter_priority.setter
    def filter_priority(self, value: Optional[PositiveInteger]) -> None:
        """
        Set filterPriority with validation.

        Args:
            value: The filterPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filterPriority = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"filterPriority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._filterPriority = value
        # atp.
        # Status=candidate.
        self._flowMetering: Optional[SwitchFlowMeteringEnum] = None

    @property
    def flow_metering(self) -> Optional[SwitchFlowMeteringEnum]:
        """Get flowMetering (Pythonic accessor)."""
        return self._flowMetering

    @flow_metering.setter
    def flow_metering(self, value: Optional[SwitchFlowMeteringEnum]) -> None:
        """
        Set flowMetering with validation.

        Args:
            value: The flowMetering to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._flowMetering = None
            return

        if not isinstance(value, SwitchFlowMetering):
            raise TypeError(
                f"flowMetering must be SwitchFlowMetering or None, got {type(value).__name__}"
            )
        self._flowMetering = value
        # processed by the.
        self._maxSduSize: Optional[PositiveInteger] = None

    @property
    def max_sdu_size(self) -> Optional[PositiveInteger]:
        """Get maxSduSize (Pythonic accessor)."""
        return self._maxSduSize

    @max_sdu_size.setter
    def max_sdu_size(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maxSduSize with validation.

        Args:
            value: The maxSduSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSduSize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxSduSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxSduSize = value
        self._streamGate: Optional[SwitchStreamGateEntry] = None

    @property
    def stream_gate(self) -> Optional[SwitchStreamGateEntry]:
        """Get streamGate (Pythonic accessor)."""
        return self._streamGate

    @stream_gate.setter
    def stream_gate(self, value: Optional[SwitchStreamGateEntry]) -> None:
        """
        Set streamGate with validation.

        Args:
            value: The streamGate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._streamGate = None
            return

        if not isinstance(value, SwitchStreamGateEntry):
            raise TypeError(
                f"streamGate must be SwitchStreamGateEntry or None, got {type(value).__name__}"
            )
        self._streamGate = value
                # SwitchStreamIdentification.
        # atp.
        # Status=candidate.
        self._stream: Optional[Boolean] = None

    @property
    def stream(self) -> Optional[Boolean]:
        """Get stream (Pythonic accessor)."""
        return self._stream

    @stream.setter
    def stream(self, value: Optional[Boolean]) -> None:
        """
        Set stream with validation.

        Args:
            value: The stream to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._stream = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"stream must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._stream = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAsynchronous(self) -> CouplingPort:
        """
        AUTOSAR-compliant getter for asynchronous.

        Returns:
            The asynchronous value

        Note:
            Delegates to asynchronous property (CODING_RULE_V2_00017)
        """
        return self.asynchronous  # Delegates to property

    def setAsynchronous(self, value: CouplingPort) -> SwitchStreamFilterEntry:
        """
        AUTOSAR-compliant setter for asynchronous with method chaining.

        Args:
            value: The asynchronous to set

        Returns:
            self for method chaining

        Note:
            Delegates to asynchronous property setter (gets validation automatically)
        """
        self.asynchronous = value  # Delegates to property setter
        return self

    def getFilterPriority(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for filterPriority.

        Returns:
            The filterPriority value

        Note:
            Delegates to filter_priority property (CODING_RULE_V2_00017)
        """
        return self.filter_priority  # Delegates to property

    def setFilterPriority(self, value: PositiveInteger) -> SwitchStreamFilterEntry:
        """
        AUTOSAR-compliant setter for filterPriority with method chaining.

        Args:
            value: The filterPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to filter_priority property setter (gets validation automatically)
        """
        self.filter_priority = value  # Delegates to property setter
        return self

    def getFlowMetering(self) -> SwitchFlowMeteringEnum:
        """
        AUTOSAR-compliant getter for flowMetering.

        Returns:
            The flowMetering value

        Note:
            Delegates to flow_metering property (CODING_RULE_V2_00017)
        """
        return self.flow_metering  # Delegates to property

    def setFlowMetering(self, value: SwitchFlowMeteringEnum) -> SwitchStreamFilterEntry:
        """
        AUTOSAR-compliant setter for flowMetering with method chaining.

        Args:
            value: The flowMetering to set

        Returns:
            self for method chaining

        Note:
            Delegates to flow_metering property setter (gets validation automatically)
        """
        self.flow_metering = value  # Delegates to property setter
        return self

    def getMaxSduSize(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maxSduSize.

        Returns:
            The maxSduSize value

        Note:
            Delegates to max_sdu_size property (CODING_RULE_V2_00017)
        """
        return self.max_sdu_size  # Delegates to property

    def setMaxSduSize(self, value: PositiveInteger) -> SwitchStreamFilterEntry:
        """
        AUTOSAR-compliant setter for maxSduSize with method chaining.

        Args:
            value: The maxSduSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_sdu_size property setter (gets validation automatically)
        """
        self.max_sdu_size = value  # Delegates to property setter
        return self

    def getStreamGate(self) -> SwitchStreamGateEntry:
        """
        AUTOSAR-compliant getter for streamGate.

        Returns:
            The streamGate value

        Note:
            Delegates to stream_gate property (CODING_RULE_V2_00017)
        """
        return self.stream_gate  # Delegates to property

    def setStreamGate(self, value: SwitchStreamGateEntry) -> SwitchStreamFilterEntry:
        """
        AUTOSAR-compliant setter for streamGate with method chaining.

        Args:
            value: The streamGate to set

        Returns:
            self for method chaining

        Note:
            Delegates to stream_gate property setter (gets validation automatically)
        """
        self.stream_gate = value  # Delegates to property setter
        return self

    def getStream(self) -> Boolean:
        """
        AUTOSAR-compliant getter for stream.

        Returns:
            The stream value

        Note:
            Delegates to stream property (CODING_RULE_V2_00017)
        """
        return self.stream  # Delegates to property

    def setStream(self, value: Boolean) -> SwitchStreamFilterEntry:
        """
        AUTOSAR-compliant setter for stream with method chaining.

        Args:
            value: The stream to set

        Returns:
            self for method chaining

        Note:
            Delegates to stream property setter (gets validation automatically)
        """
        self.stream = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_asynchronous(self, value: Optional[CouplingPort]) -> SwitchStreamFilterEntry:
        """
        Set asynchronous and return self for chaining.

        Args:
            value: The asynchronous to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_asynchronous("value")
        """
        self.asynchronous = value  # Use property setter (gets validation)
        return self

    def with_filter_priority(self, value: Optional[PositiveInteger]) -> SwitchStreamFilterEntry:
        """
        Set filterPriority and return self for chaining.

        Args:
            value: The filterPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_filter_priority("value")
        """
        self.filter_priority = value  # Use property setter (gets validation)
        return self

    def with_flow_metering(self, value: Optional[SwitchFlowMeteringEnum]) -> SwitchStreamFilterEntry:
        """
        Set flowMetering and return self for chaining.

        Args:
            value: The flowMetering to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_flow_metering("value")
        """
        self.flow_metering = value  # Use property setter (gets validation)
        return self

    def with_max_sdu_size(self, value: Optional[PositiveInteger]) -> SwitchStreamFilterEntry:
        """
        Set maxSduSize and return self for chaining.

        Args:
            value: The maxSduSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_sdu_size("value")
        """
        self.max_sdu_size = value  # Use property setter (gets validation)
        return self

    def with_stream_gate(self, value: Optional[SwitchStreamGateEntry]) -> SwitchStreamFilterEntry:
        """
        Set streamGate and return self for chaining.

        Args:
            value: The streamGate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_stream_gate("value")
        """
        self.stream_gate = value  # Use property setter (gets validation)
        return self

    def with_stream(self, value: Optional[Boolean]) -> SwitchStreamFilterEntry:
        """
        Set stream and return self for chaining.

        Args:
            value: The stream to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_stream("value")
        """
        self.stream = value  # Use property setter (gets validation)
        return self



class SwitchAsynchronousTrafficShaperGroupEntry(Identifiable):
    """
    Defines an Asynchronous Traffic Shapter (ATS) Group for a switch.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::SwitchAsynchronousTrafficShaperGroupEntry

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 142, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the maximum duration limit for which frames can in a switch (in
        # seconds).
        self._maximum: Optional[PositiveInteger] = None

    @property
    def maximum(self) -> Optional[PositiveInteger]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maximum with validation.

        Args:
            value: The maximum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximum = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maximum must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maximum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaximum(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: PositiveInteger) -> SwitchAsynchronousTrafficShaperGroupEntry:
        """
        AUTOSAR-compliant setter for maximum with method chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum property setter (gets validation automatically)
        """
        self.maximum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_maximum(self, value: Optional[PositiveInteger]) -> SwitchAsynchronousTrafficShaperGroupEntry:
        """
        Set maximum and return self for chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum("value")
        """
        self.maximum = value  # Use property setter (gets validation)
        return self



class SwitchStreamGateEntry(Identifiable):
    """
    Defines a Asynchronous Traffic Shapter (ATS) Group for a switch.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::SwitchStreamGateEntry

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 142, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Internal Priority Value (IPV), a priority value that the assigned traffic
        # class.
        self._internalPriority: Optional[PositiveInteger] = None

    @property
    def internal_priority(self) -> Optional[PositiveInteger]:
        """Get internalPriority (Pythonic accessor)."""
        return self._internalPriority

    @internal_priority.setter
    def internal_priority(self, value: Optional[PositiveInteger]) -> None:
        """
        Set internalPriority with validation.

        Args:
            value: The internalPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._internalPriority = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"internalPriority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._internalPriority = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInternalPriority(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for internalPriority.

        Returns:
            The internalPriority value

        Note:
            Delegates to internal_priority property (CODING_RULE_V2_00017)
        """
        return self.internal_priority  # Delegates to property

    def setInternalPriority(self, value: PositiveInteger) -> SwitchStreamGateEntry:
        """
        AUTOSAR-compliant setter for internalPriority with method chaining.

        Args:
            value: The internalPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to internal_priority property setter (gets validation automatically)
        """
        self.internal_priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_internal_priority(self, value: Optional[PositiveInteger]) -> SwitchStreamGateEntry:
        """
        Set internalPriority and return self for chaining.

        Args:
            value: The internalPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_internal_priority("value")
        """
        self.internal_priority = value  # Use property setter (gets validation)
        return self



class SwitchFlowMeteringEntry(Identifiable):
    """
    Defines a Flow Metering Entry for a switch.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::SwitchFlowMeteringEntry

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 143, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether color-aware or color-blind mode shall be.
        self._colorMode: Optional[FlowMeteringColorModeEnum] = None

    @property
    def color_mode(self) -> Optional[FlowMeteringColorModeEnum]:
        """Get colorMode (Pythonic accessor)."""
        return self._colorMode

    @color_mode.setter
    def color_mode(self, value: Optional[FlowMeteringColorModeEnum]) -> None:
        """
        Set colorMode with validation.

        Args:
            value: The colorMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._colorMode = None
            return

        if not isinstance(value, FlowMeteringColor):
            raise TypeError(
                f"colorMode must be FlowMeteringColor or None, got {type(value).__name__}"
            )
        self._colorMode = value
        self._committedBurst: Optional[PositiveInteger] = None

    @property
    def committed_burst(self) -> Optional[PositiveInteger]:
        """Get committedBurst (Pythonic accessor)."""
        return self._committedBurst

    @committed_burst.setter
    def committed_burst(self, value: Optional[PositiveInteger]) -> None:
        """
        Set committedBurst with validation.

        Args:
            value: The committedBurst to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._committedBurst = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"committedBurst must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._committedBurst = value
        # second.
        self._committed: Optional[PositiveInteger] = None

    @property
    def committed(self) -> Optional[PositiveInteger]:
        """Get committed (Pythonic accessor)."""
        return self._committed

    @committed.setter
    def committed(self, value: Optional[PositiveInteger]) -> None:
        """
        Set committed with validation.

        Args:
            value: The committed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._committed = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"committed must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._committed = value
        # the second bucket as.
        self._couplingFlag: Optional[Boolean] = None

    @property
    def coupling_flag(self) -> Optional[Boolean]:
        """Get couplingFlag (Pythonic accessor)."""
        return self._couplingFlag

    @coupling_flag.setter
    def coupling_flag(self, value: Optional[Boolean]) -> None:
        """
        Set couplingFlag with validation.

        Args:
            value: The couplingFlag to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._couplingFlag = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"couplingFlag must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._couplingFlag = value
        self._excessBurst: Optional[PositiveInteger] = None

    @property
    def excess_burst(self) -> Optional[PositiveInteger]:
        """Get excessBurst (Pythonic accessor)."""
        return self._excessBurst

    @excess_burst.setter
    def excess_burst(self, value: Optional[PositiveInteger]) -> None:
        """
        Set excessBurst with validation.

        Args:
            value: The excessBurst to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._excessBurst = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"excessBurst must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._excessBurst = value
        # second.
        self._excess: Optional[PositiveInteger] = None

    @property
    def excess(self) -> Optional[PositiveInteger]:
        """Get excess (Pythonic accessor)."""
        return self._excess

    @excess.setter
    def excess(self, value: Optional[PositiveInteger]) -> None:
        """
        Set excess with validation.

        Args:
            value: The excess to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._excess = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"excess must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._excess = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getColorMode(self) -> FlowMeteringColorModeEnum:
        """
        AUTOSAR-compliant getter for colorMode.

        Returns:
            The colorMode value

        Note:
            Delegates to color_mode property (CODING_RULE_V2_00017)
        """
        return self.color_mode  # Delegates to property

    def setColorMode(self, value: FlowMeteringColorModeEnum) -> SwitchFlowMeteringEntry:
        """
        AUTOSAR-compliant setter for colorMode with method chaining.

        Args:
            value: The colorMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to color_mode property setter (gets validation automatically)
        """
        self.color_mode = value  # Delegates to property setter
        return self

    def getCommittedBurst(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for committedBurst.

        Returns:
            The committedBurst value

        Note:
            Delegates to committed_burst property (CODING_RULE_V2_00017)
        """
        return self.committed_burst  # Delegates to property

    def setCommittedBurst(self, value: PositiveInteger) -> SwitchFlowMeteringEntry:
        """
        AUTOSAR-compliant setter for committedBurst with method chaining.

        Args:
            value: The committedBurst to set

        Returns:
            self for method chaining

        Note:
            Delegates to committed_burst property setter (gets validation automatically)
        """
        self.committed_burst = value  # Delegates to property setter
        return self

    def getCommitted(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for committed.

        Returns:
            The committed value

        Note:
            Delegates to committed property (CODING_RULE_V2_00017)
        """
        return self.committed  # Delegates to property

    def setCommitted(self, value: PositiveInteger) -> SwitchFlowMeteringEntry:
        """
        AUTOSAR-compliant setter for committed with method chaining.

        Args:
            value: The committed to set

        Returns:
            self for method chaining

        Note:
            Delegates to committed property setter (gets validation automatically)
        """
        self.committed = value  # Delegates to property setter
        return self

    def getCouplingFlag(self) -> Boolean:
        """
        AUTOSAR-compliant getter for couplingFlag.

        Returns:
            The couplingFlag value

        Note:
            Delegates to coupling_flag property (CODING_RULE_V2_00017)
        """
        return self.coupling_flag  # Delegates to property

    def setCouplingFlag(self, value: Boolean) -> SwitchFlowMeteringEntry:
        """
        AUTOSAR-compliant setter for couplingFlag with method chaining.

        Args:
            value: The couplingFlag to set

        Returns:
            self for method chaining

        Note:
            Delegates to coupling_flag property setter (gets validation automatically)
        """
        self.coupling_flag = value  # Delegates to property setter
        return self

    def getExcessBurst(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for excessBurst.

        Returns:
            The excessBurst value

        Note:
            Delegates to excess_burst property (CODING_RULE_V2_00017)
        """
        return self.excess_burst  # Delegates to property

    def setExcessBurst(self, value: PositiveInteger) -> SwitchFlowMeteringEntry:
        """
        AUTOSAR-compliant setter for excessBurst with method chaining.

        Args:
            value: The excessBurst to set

        Returns:
            self for method chaining

        Note:
            Delegates to excess_burst property setter (gets validation automatically)
        """
        self.excess_burst = value  # Delegates to property setter
        return self

    def getExcess(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for excess.

        Returns:
            The excess value

        Note:
            Delegates to excess property (CODING_RULE_V2_00017)
        """
        return self.excess  # Delegates to property

    def setExcess(self, value: PositiveInteger) -> SwitchFlowMeteringEntry:
        """
        AUTOSAR-compliant setter for excess with method chaining.

        Args:
            value: The excess to set

        Returns:
            self for method chaining

        Note:
            Delegates to excess property setter (gets validation automatically)
        """
        self.excess = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_color_mode(self, value: Optional[FlowMeteringColorModeEnum]) -> SwitchFlowMeteringEntry:
        """
        Set colorMode and return self for chaining.

        Args:
            value: The colorMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_color_mode("value")
        """
        self.color_mode = value  # Use property setter (gets validation)
        return self

    def with_committed_burst(self, value: Optional[PositiveInteger]) -> SwitchFlowMeteringEntry:
        """
        Set committedBurst and return self for chaining.

        Args:
            value: The committedBurst to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_committed_burst("value")
        """
        self.committed_burst = value  # Use property setter (gets validation)
        return self

    def with_committed(self, value: Optional[PositiveInteger]) -> SwitchFlowMeteringEntry:
        """
        Set committed and return self for chaining.

        Args:
            value: The committed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_committed("value")
        """
        self.committed = value  # Use property setter (gets validation)
        return self

    def with_coupling_flag(self, value: Optional[Boolean]) -> SwitchFlowMeteringEntry:
        """
        Set couplingFlag and return self for chaining.

        Args:
            value: The couplingFlag to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_coupling_flag("value")
        """
        self.coupling_flag = value  # Use property setter (gets validation)
        return self

    def with_excess_burst(self, value: Optional[PositiveInteger]) -> SwitchFlowMeteringEntry:
        """
        Set excessBurst and return self for chaining.

        Args:
            value: The excessBurst to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_excess_burst("value")
        """
        self.excess_burst = value  # Use property setter (gets validation)
        return self

    def with_excess(self, value: Optional[PositiveInteger]) -> SwitchFlowMeteringEntry:
        """
        Set excess and return self for chaining.

        Args:
            value: The excess to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_excess("value")
        """
        self.excess = value  # Use property setter (gets validation)
        return self



class EthIpProps(ARElement):
    """
    This meta-class is used to configure the EcuInstance specific IP attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthIpProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 146, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Configuration options for IPv4.
        self._ipv4Props: Optional[Ipv4Props] = None

    @property
    def ipv4_props(self) -> Optional[Ipv4Props]:
        """Get ipv4Props (Pythonic accessor)."""
        return self._ipv4Props

    @ipv4_props.setter
    def ipv4_props(self, value: Optional[Ipv4Props]) -> None:
        """
        Set ipv4Props with validation.

        Args:
            value: The ipv4Props to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv4Props = None
            return

        if not isinstance(value, Ipv4Props):
            raise TypeError(
                f"ipv4Props must be Ipv4Props or None, got {type(value).__name__}"
            )
        self._ipv4Props = value
        # Configuration options for IPv6.
        self._ipv6Props: Optional[Ipv6Props] = None

    @property
    def ipv6_props(self) -> Optional[Ipv6Props]:
        """Get ipv6Props (Pythonic accessor)."""
        return self._ipv6Props

    @ipv6_props.setter
    def ipv6_props(self, value: Optional[Ipv6Props]) -> None:
        """
        Set ipv6Props with validation.

        Args:
            value: The ipv6Props to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv6Props = None
            return

        if not isinstance(value, Ipv6Props):
            raise TypeError(
                f"ipv6Props must be Ipv6Props or None, got {type(value).__name__}"
            )
        self._ipv6Props = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIpv4Props(self) -> Ipv4Props:
        """
        AUTOSAR-compliant getter for ipv4Props.

        Returns:
            The ipv4Props value

        Note:
            Delegates to ipv4_props property (CODING_RULE_V2_00017)
        """
        return self.ipv4_props  # Delegates to property

    def setIpv4Props(self, value: Ipv4Props) -> EthIpProps:
        """
        AUTOSAR-compliant setter for ipv4Props with method chaining.

        Args:
            value: The ipv4Props to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv4_props property setter (gets validation automatically)
        """
        self.ipv4_props = value  # Delegates to property setter
        return self

    def getIpv6Props(self) -> Ipv6Props:
        """
        AUTOSAR-compliant getter for ipv6Props.

        Returns:
            The ipv6Props value

        Note:
            Delegates to ipv6_props property (CODING_RULE_V2_00017)
        """
        return self.ipv6_props  # Delegates to property

    def setIpv6Props(self, value: Ipv6Props) -> EthIpProps:
        """
        AUTOSAR-compliant setter for ipv6Props with method chaining.

        Args:
            value: The ipv6Props to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv6_props property setter (gets validation automatically)
        """
        self.ipv6_props = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ipv4_props(self, value: Optional[Ipv4Props]) -> EthIpProps:
        """
        Set ipv4Props and return self for chaining.

        Args:
            value: The ipv4Props to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv4_props("value")
        """
        self.ipv4_props = value  # Use property setter (gets validation)
        return self

    def with_ipv6_props(self, value: Optional[Ipv6Props]) -> EthIpProps:
        """
        Set ipv6Props and return self for chaining.

        Args:
            value: The ipv6Props to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv6_props("value")
        """
        self.ipv6_props = value  # Use property setter (gets validation)
        return self



class Ipv4Props(ARObject):
    """
    This meta-class specifies the configuration options for IPv4.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv4Props

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 146, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Configuration properties for the ARP (Address Resolution.
        self._arpProps: Optional[Ipv4ArpProps] = None

    @property
    def arp_props(self) -> Optional[Ipv4ArpProps]:
        """Get arpProps (Pythonic accessor)."""
        return self._arpProps

    @arp_props.setter
    def arp_props(self, value: Optional[Ipv4ArpProps]) -> None:
        """
        Set arpProps with validation.

        Args:
            value: The arpProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arpProps = None
            return

        if not isinstance(value, Ipv4ArpProps):
            raise TypeError(
                f"arpProps must be Ipv4ArpProps or None, got {type(value).__name__}"
            )
        self._arpProps = value
        self._autoIpProps: Optional[Ipv4AutoIpProps] = None

    @property
    def auto_ip_props(self) -> Optional[Ipv4AutoIpProps]:
        """Get autoIpProps (Pythonic accessor)."""
        return self._autoIpProps

    @auto_ip_props.setter
    def auto_ip_props(self, value: Optional[Ipv4AutoIpProps]) -> None:
        """
        Set autoIpProps with validation.

        Args:
            value: The autoIpProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._autoIpProps = None
            return

        if not isinstance(value, Ipv4AutoIpProps):
            raise TypeError(
                f"autoIpProps must be Ipv4AutoIpProps or None, got {type(value).__name__}"
            )
        self._autoIpProps = value
        self._fragmentation: Optional[Ipv4FragmentationHandlingEnum] = None

    @property
    def fragmentation(self) -> Optional[Ipv4FragmentationHandlingEnum]:
        """Get fragmentation (Pythonic accessor)."""
        return self._fragmentation

    @fragmentation.setter
    def fragmentation(self, value: Optional[Ipv4FragmentationHandlingEnum]) -> None:
        """
        Set fragmentation with validation.

        Args:
            value: The fragmentation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fragmentation = None
            return

        if not isinstance(value, Ipv4Fragmentation):
            raise TypeError(
                f"fragmentation must be Ipv4Fragmentation or None, got {type(value).__name__}"
            )
        self._fragmentation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArpProps(self) -> Ipv4ArpProps:
        """
        AUTOSAR-compliant getter for arpProps.

        Returns:
            The arpProps value

        Note:
            Delegates to arp_props property (CODING_RULE_V2_00017)
        """
        return self.arp_props  # Delegates to property

    def setArpProps(self, value: Ipv4ArpProps) -> Ipv4Props:
        """
        AUTOSAR-compliant setter for arpProps with method chaining.

        Args:
            value: The arpProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to arp_props property setter (gets validation automatically)
        """
        self.arp_props = value  # Delegates to property setter
        return self

    def getAutoIpProps(self) -> Ipv4AutoIpProps:
        """
        AUTOSAR-compliant getter for autoIpProps.

        Returns:
            The autoIpProps value

        Note:
            Delegates to auto_ip_props property (CODING_RULE_V2_00017)
        """
        return self.auto_ip_props  # Delegates to property

    def setAutoIpProps(self, value: Ipv4AutoIpProps) -> Ipv4Props:
        """
        AUTOSAR-compliant setter for autoIpProps with method chaining.

        Args:
            value: The autoIpProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to auto_ip_props property setter (gets validation automatically)
        """
        self.auto_ip_props = value  # Delegates to property setter
        return self

    def getFragmentation(self) -> Ipv4FragmentationHandlingEnum:
        """
        AUTOSAR-compliant getter for fragmentation.

        Returns:
            The fragmentation value

        Note:
            Delegates to fragmentation property (CODING_RULE_V2_00017)
        """
        return self.fragmentation  # Delegates to property

    def setFragmentation(self, value: Ipv4FragmentationHandlingEnum) -> Ipv4Props:
        """
        AUTOSAR-compliant setter for fragmentation with method chaining.

        Args:
            value: The fragmentation to set

        Returns:
            self for method chaining

        Note:
            Delegates to fragmentation property setter (gets validation automatically)
        """
        self.fragmentation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_arp_props(self, value: Optional[Ipv4ArpProps]) -> Ipv4Props:
        """
        Set arpProps and return self for chaining.

        Args:
            value: The arpProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_arp_props("value")
        """
        self.arp_props = value  # Use property setter (gets validation)
        return self

    def with_auto_ip_props(self, value: Optional[Ipv4AutoIpProps]) -> Ipv4Props:
        """
        Set autoIpProps and return self for chaining.

        Args:
            value: The autoIpProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_auto_ip_props("value")
        """
        self.auto_ip_props = value  # Use property setter (gets validation)
        return self

    def with_fragmentation(self, value: Optional[Ipv4FragmentationHandlingEnum]) -> Ipv4Props:
        """
        Set fragmentation and return self for chaining.

        Args:
            value: The fragmentation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fragmentation("value")
        """
        self.fragmentation = value  # Use property setter (gets validation)
        return self



class Ipv4ArpProps(ARObject):
    """
    Specifies the configuration options for the ARP (Address Resolution
    Protocol).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv4ArpProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 146, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the number of gratuitous ARP which shall be sent on
        # assignment of a new IP.
        self._tcpIpArpNum: Optional[PositiveInteger] = None

    @property
    def tcp_ip_arp_num(self) -> Optional[PositiveInteger]:
        """Get tcpIpArpNum (Pythonic accessor)."""
        return self._tcpIpArpNum

    @tcp_ip_arp_num.setter
    def tcp_ip_arp_num(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpIpArpNum with validation.

        Args:
            value: The tcpIpArpNum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpArpNum = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpIpArpNum must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpIpArpNum = value
                # according to IETF RFC 2.
        # 3.
        # 2.
        # 2.
        self._tcpIpArpPacket: Optional[Boolean] = None

    @property
    def tcp_ip_arp_packet(self) -> Optional[Boolean]:
        """Get tcpIpArpPacket (Pythonic accessor)."""
        return self._tcpIpArpPacket

    @tcp_ip_arp_packet.setter
    def tcp_ip_arp_packet(self, value: Optional[Boolean]) -> None:
        """
        Set tcpIpArpPacket with validation.

        Args:
            value: The tcpIpArpPacket to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpArpPacket = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"tcpIpArpPacket must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._tcpIpArpPacket = value
        # After the transmission of an request the TcpIp shall skip the transmission of
                # any requests to the same destination within a tcpIpArpRequestTimeout seconds.
        # (IETF RFC 2.
        # 3.
        # 2.
        # 1).
        self._tcpIpArp: Optional[TimeValue] = None

    @property
    def tcp_ip_arp(self) -> Optional[TimeValue]:
        """Get tcpIpArp (Pythonic accessor)."""
        return self._tcpIpArp

    @tcp_ip_arp.setter
    def tcp_ip_arp(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpIpArp with validation.

        Args:
            value: The tcpIpArp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpArp = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpArp must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpArp = value
        # is removed.
        self._tcpIpArpTable: Optional[TimeValue] = None

    @property
    def tcp_ip_arp_table(self) -> Optional[TimeValue]:
        """Get tcpIpArpTable (Pythonic accessor)."""
        return self._tcpIpArpTable

    @tcp_ip_arp_table.setter
    def tcp_ip_arp_table(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpIpArpTable with validation.

        Args:
            value: The tcpIpArpTable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpArpTable = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpArpTable must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpArpTable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpArpNum(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpIpArpNum.

        Returns:
            The tcpIpArpNum value

        Note:
            Delegates to tcp_ip_arp_num property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_arp_num  # Delegates to property

    def setTcpIpArpNum(self, value: PositiveInteger) -> Ipv4ArpProps:
        """
        AUTOSAR-compliant setter for tcpIpArpNum with method chaining.

        Args:
            value: The tcpIpArpNum to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_arp_num property setter (gets validation automatically)
        """
        self.tcp_ip_arp_num = value  # Delegates to property setter
        return self

    def getTcpIpArpPacket(self) -> Boolean:
        """
        AUTOSAR-compliant getter for tcpIpArpPacket.

        Returns:
            The tcpIpArpPacket value

        Note:
            Delegates to tcp_ip_arp_packet property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_arp_packet  # Delegates to property

    def setTcpIpArpPacket(self, value: Boolean) -> Ipv4ArpProps:
        """
        AUTOSAR-compliant setter for tcpIpArpPacket with method chaining.

        Args:
            value: The tcpIpArpPacket to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_arp_packet property setter (gets validation automatically)
        """
        self.tcp_ip_arp_packet = value  # Delegates to property setter
        return self

    def getTcpIpArp(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpIpArp.

        Returns:
            The tcpIpArp value

        Note:
            Delegates to tcp_ip_arp property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_arp  # Delegates to property

    def setTcpIpArp(self, value: TimeValue) -> Ipv4ArpProps:
        """
        AUTOSAR-compliant setter for tcpIpArp with method chaining.

        Args:
            value: The tcpIpArp to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_arp property setter (gets validation automatically)
        """
        self.tcp_ip_arp = value  # Delegates to property setter
        return self

    def getTcpIpArpTable(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpIpArpTable.

        Returns:
            The tcpIpArpTable value

        Note:
            Delegates to tcp_ip_arp_table property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_arp_table  # Delegates to property

    def setTcpIpArpTable(self, value: TimeValue) -> Ipv4ArpProps:
        """
        AUTOSAR-compliant setter for tcpIpArpTable with method chaining.

        Args:
            value: The tcpIpArpTable to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_arp_table property setter (gets validation automatically)
        """
        self.tcp_ip_arp_table = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_arp_num(self, value: Optional[PositiveInteger]) -> Ipv4ArpProps:
        """
        Set tcpIpArpNum and return self for chaining.

        Args:
            value: The tcpIpArpNum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_arp_num("value")
        """
        self.tcp_ip_arp_num = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_arp_packet(self, value: Optional[Boolean]) -> Ipv4ArpProps:
        """
        Set tcpIpArpPacket and return self for chaining.

        Args:
            value: The tcpIpArpPacket to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_arp_packet("value")
        """
        self.tcp_ip_arp_packet = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_arp(self, value: Optional[TimeValue]) -> Ipv4ArpProps:
        """
        Set tcpIpArp and return self for chaining.

        Args:
            value: The tcpIpArp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_arp("value")
        """
        self.tcp_ip_arp = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_arp_table(self, value: Optional[TimeValue]) -> Ipv4ArpProps:
        """
        Set tcpIpArpTable and return self for chaining.

        Args:
            value: The tcpIpArpTable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_arp_table("value")
        """
        self.tcp_ip_arp_table = value  # Use property setter (gets validation)
        return self



class Ipv4AutoIpProps(ARObject):
    """
    Specifies the configuration options for Auto-IP (automatic private IP
    addressing).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv4AutoIpProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 147, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the time in seconds Auto-IP waits startup, before
                # beginning with ARP probing.
        # This delay to give DHCP time to acquire a lease in case a is present.
        self._tcpIpAutoIpInit: Optional[TimeValue] = None

    @property
    def tcp_ip_auto_ip_init(self) -> Optional[TimeValue]:
        """Get tcpIpAutoIpInit (Pythonic accessor)."""
        return self._tcpIpAutoIpInit

    @tcp_ip_auto_ip_init.setter
    def tcp_ip_auto_ip_init(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpIpAutoIpInit with validation.

        Args:
            value: The tcpIpAutoIpInit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpAutoIpInit = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpAutoIpInit must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpAutoIpInit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpAutoIpInit(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpIpAutoIpInit.

        Returns:
            The tcpIpAutoIpInit value

        Note:
            Delegates to tcp_ip_auto_ip_init property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_auto_ip_init  # Delegates to property

    def setTcpIpAutoIpInit(self, value: TimeValue) -> Ipv4AutoIpProps:
        """
        AUTOSAR-compliant setter for tcpIpAutoIpInit with method chaining.

        Args:
            value: The tcpIpAutoIpInit to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_auto_ip_init property setter (gets validation automatically)
        """
        self.tcp_ip_auto_ip_init = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_auto_ip_init(self, value: Optional[TimeValue]) -> Ipv4AutoIpProps:
        """
        Set tcpIpAutoIpInit and return self for chaining.

        Args:
            value: The tcpIpAutoIpInit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_auto_ip_init("value")
        """
        self.tcp_ip_auto_ip_init = value  # Use property setter (gets validation)
        return self



class Ipv4FragmentationProps(ARObject):
    """
    Specifies the configuration options for IPv4 packet
    fragmentation/reassembly.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv4FragmentationProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 147, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Enables (TRUE) or disables (FALSE) support for of incoming datagrams that are
        # fragmented to IETF RFC 815 (IP Datagram Reassembly.
        self._tcpIpIp: Optional[Boolean] = None

    @property
    def tcp_ip_ip(self) -> Optional[Boolean]:
        """Get tcpIpIp (Pythonic accessor)."""
        return self._tcpIpIp

    @tcp_ip_ip.setter
    def tcp_ip_ip(self, value: Optional[Boolean]) -> None:
        """
        Set tcpIpIp with validation.

        Args:
            value: The tcpIpIp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIp = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"tcpIpIp must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._tcpIpIp = value
        # parallel.
        self._tcpIpIpNum: Optional[PositiveInteger] = None

    @property
    def tcp_ip_ip_num(self) -> Optional[PositiveInteger]:
        """Get tcpIpIpNum (Pythonic accessor)."""
        return self._tcpIpIpNum

    @tcp_ip_ip_num.setter
    def tcp_ip_ip_num(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpIpIpNum with validation.

        Args:
            value: The tcpIpIpNum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIpNum = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpIpIpNum must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpIpIpNum = value
        self._tcpIpIpReass: Optional[TimeValue] = None

    @property
    def tcp_ip_ip_reass(self) -> Optional[TimeValue]:
        """Get tcpIpIpReass (Pythonic accessor)."""
        return self._tcpIpIpReass

    @tcp_ip_ip_reass.setter
    def tcp_ip_ip_reass(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpIpIpReass with validation.

        Args:
            value: The tcpIpIpReass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIpReass = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpIpReass must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpIpReass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpIp(self) -> Boolean:
        """
        AUTOSAR-compliant getter for tcpIpIp.

        Returns:
            The tcpIpIp value

        Note:
            Delegates to tcp_ip_ip property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ip  # Delegates to property

    def setTcpIpIp(self, value: Boolean) -> Ipv4FragmentationProps:
        """
        AUTOSAR-compliant setter for tcpIpIp with method chaining.

        Args:
            value: The tcpIpIp to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ip property setter (gets validation automatically)
        """
        self.tcp_ip_ip = value  # Delegates to property setter
        return self

    def getTcpIpIpNum(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpIpIpNum.

        Returns:
            The tcpIpIpNum value

        Note:
            Delegates to tcp_ip_ip_num property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ip_num  # Delegates to property

    def setTcpIpIpNum(self, value: PositiveInteger) -> Ipv4FragmentationProps:
        """
        AUTOSAR-compliant setter for tcpIpIpNum with method chaining.

        Args:
            value: The tcpIpIpNum to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ip_num property setter (gets validation automatically)
        """
        self.tcp_ip_ip_num = value  # Delegates to property setter
        return self

    def getTcpIpIpReass(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpIpIpReass.

        Returns:
            The tcpIpIpReass value

        Note:
            Delegates to tcp_ip_ip_reass property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ip_reass  # Delegates to property

    def setTcpIpIpReass(self, value: TimeValue) -> Ipv4FragmentationProps:
        """
        AUTOSAR-compliant setter for tcpIpIpReass with method chaining.

        Args:
            value: The tcpIpIpReass to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ip_reass property setter (gets validation automatically)
        """
        self.tcp_ip_ip_reass = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_ip(self, value: Optional[Boolean]) -> Ipv4FragmentationProps:
        """
        Set tcpIpIp and return self for chaining.

        Args:
            value: The tcpIpIp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ip("value")
        """
        self.tcp_ip_ip = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ip_num(self, value: Optional[PositiveInteger]) -> Ipv4FragmentationProps:
        """
        Set tcpIpIpNum and return self for chaining.

        Args:
            value: The tcpIpIpNum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ip_num("value")
        """
        self.tcp_ip_ip_num = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ip_reass(self, value: Optional[TimeValue]) -> Ipv4FragmentationProps:
        """
        Set tcpIpIpReass and return self for chaining.

        Args:
            value: The tcpIpIpReass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ip_reass("value")
        """
        self.tcp_ip_ip_reass = value  # Use property setter (gets validation)
        return self



class Ipv6Props(ARObject):
    """
    This meta-class specifies the configuration options for IPv6.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv6Props

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 147, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Configuration properties for DHCPv6.
        self._dhcpProps: Optional[Dhcpv6Props] = None

    @property
    def dhcp_props(self) -> Optional[Dhcpv6Props]:
        """Get dhcpProps (Pythonic accessor)."""
        return self._dhcpProps

    @dhcp_props.setter
    def dhcp_props(self, value: Optional[Dhcpv6Props]) -> None:
        """
        Set dhcpProps with validation.

        Args:
            value: The dhcpProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dhcpProps = None
            return

        if not isinstance(value, Dhcpv6Props):
            raise TypeError(
                f"dhcpProps must be Dhcpv6Props or None, got {type(value).__name__}"
            )
        self._dhcpProps = value
        self._fragmentation: Optional[Ipv6FragmentationHandlingEnum] = None

    @property
    def fragmentation(self) -> Optional[Ipv6FragmentationHandlingEnum]:
        """Get fragmentation (Pythonic accessor)."""
        return self._fragmentation

    @fragmentation.setter
    def fragmentation(self, value: Optional[Ipv6FragmentationHandlingEnum]) -> None:
        """
        Set fragmentation with validation.

        Args:
            value: The fragmentation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fragmentation = None
            return

        if not isinstance(value, Ipv6Fragmentation):
            raise TypeError(
                f"fragmentation must be Ipv6Fragmentation or None, got {type(value).__name__}"
            )
        self._fragmentation = value
        self._ndpProps: Optional[Ipv6NdpProps] = None

    @property
    def ndp_props(self) -> Optional[Ipv6NdpProps]:
        """Get ndpProps (Pythonic accessor)."""
        return self._ndpProps

    @ndp_props.setter
    def ndp_props(self, value: Optional[Ipv6NdpProps]) -> None:
        """
        Set ndpProps with validation.

        Args:
            value: The ndpProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ndpProps = None
            return

        if not isinstance(value, Ipv6NdpProps):
            raise TypeError(
                f"ndpProps must be Ipv6NdpProps or None, got {type(value).__name__}"
            )
        self._ndpProps = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDhcpProps(self) -> Dhcpv6Props:
        """
        AUTOSAR-compliant getter for dhcpProps.

        Returns:
            The dhcpProps value

        Note:
            Delegates to dhcp_props property (CODING_RULE_V2_00017)
        """
        return self.dhcp_props  # Delegates to property

    def setDhcpProps(self, value: Dhcpv6Props) -> Ipv6Props:
        """
        AUTOSAR-compliant setter for dhcpProps with method chaining.

        Args:
            value: The dhcpProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to dhcp_props property setter (gets validation automatically)
        """
        self.dhcp_props = value  # Delegates to property setter
        return self

    def getFragmentation(self) -> Ipv6FragmentationHandlingEnum:
        """
        AUTOSAR-compliant getter for fragmentation.

        Returns:
            The fragmentation value

        Note:
            Delegates to fragmentation property (CODING_RULE_V2_00017)
        """
        return self.fragmentation  # Delegates to property

    def setFragmentation(self, value: Ipv6FragmentationHandlingEnum) -> Ipv6Props:
        """
        AUTOSAR-compliant setter for fragmentation with method chaining.

        Args:
            value: The fragmentation to set

        Returns:
            self for method chaining

        Note:
            Delegates to fragmentation property setter (gets validation automatically)
        """
        self.fragmentation = value  # Delegates to property setter
        return self

    def getNdpProps(self) -> Ipv6NdpProps:
        """
        AUTOSAR-compliant getter for ndpProps.

        Returns:
            The ndpProps value

        Note:
            Delegates to ndp_props property (CODING_RULE_V2_00017)
        """
        return self.ndp_props  # Delegates to property

    def setNdpProps(self, value: Ipv6NdpProps) -> Ipv6Props:
        """
        AUTOSAR-compliant setter for ndpProps with method chaining.

        Args:
            value: The ndpProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to ndp_props property setter (gets validation automatically)
        """
        self.ndp_props = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dhcp_props(self, value: Optional[Dhcpv6Props]) -> Ipv6Props:
        """
        Set dhcpProps and return self for chaining.

        Args:
            value: The dhcpProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dhcp_props("value")
        """
        self.dhcp_props = value  # Use property setter (gets validation)
        return self

    def with_fragmentation(self, value: Optional[Ipv6FragmentationHandlingEnum]) -> Ipv6Props:
        """
        Set fragmentation and return self for chaining.

        Args:
            value: The fragmentation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fragmentation("value")
        """
        self.fragmentation = value  # Use property setter (gets validation)
        return self

    def with_ndp_props(self, value: Optional[Ipv6NdpProps]) -> Ipv6Props:
        """
        Set ndpProps and return self for chaining.

        Args:
            value: The ndpProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ndp_props("value")
        """
        self.ndp_props = value  # Use property setter (gets validation)
        return self



class Ipv6FragmentationProps(ARObject):
    """
    This meta-class specifies the configuration options for IPv6 packet
    fragmentation/reassembly.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv6FragmentationProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 148, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the timeout in seconds after which an datagram gets discarded.
        self._tcpIpIp: Optional[TimeValue] = None

    @property
    def tcp_ip_ip(self) -> Optional[TimeValue]:
        """Get tcpIpIp (Pythonic accessor)."""
        return self._tcpIpIp

    @tcp_ip_ip.setter
    def tcp_ip_ip(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpIpIp with validation.

        Args:
            value: The tcpIpIp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIp = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpIp must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpIp = value
        self._tcpIpIpReassemblyBufferSize: Optional[PositiveInteger] = None

    @property
    def tcp_ip_ip_reassembly_buffer_size(self) -> Optional[PositiveInteger]:
        """Get tcpIpIpReassemblyBufferSize (Pythonic accessor)."""
        return self._tcpIpIpReassemblyBufferSize

    @tcp_ip_ip_reassembly_buffer_size.setter
    def tcp_ip_ip_reassembly_buffer_size(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpIpIpReassemblyBufferSize with validation.

        Args:
            value: The tcpIpIpReassemblyBufferSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIpReassemblyBufferSize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpIpIpReassemblyBufferSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpIpIpReassemblyBufferSize = value
                # do not fit into the MTU and thus be fragmented.
        # of 0 disables tx fragmentation.
        self._tcpIpIpTx: Optional[PositiveInteger] = None

    @property
    def tcp_ip_ip_tx(self) -> Optional[PositiveInteger]:
        """Get tcpIpIpTx (Pythonic accessor)."""
        return self._tcpIpIpTx

    @tcp_ip_ip_tx.setter
    def tcp_ip_ip_tx(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpIpIpTx with validation.

        Args:
            value: The tcpIpIpTx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIpTx = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpIpIpTx must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpIpIpTx = value
        self._tcpIpIpTxFragmentBufferSize: Optional[PositiveInteger] = None

    @property
    def tcp_ip_ip_tx_fragment_buffer_size(self) -> Optional[PositiveInteger]:
        """Get tcpIpIpTxFragmentBufferSize (Pythonic accessor)."""
        return self._tcpIpIpTxFragmentBufferSize

    @tcp_ip_ip_tx_fragment_buffer_size.setter
    def tcp_ip_ip_tx_fragment_buffer_size(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpIpIpTxFragmentBufferSize with validation.

        Args:
            value: The tcpIpIpTxFragmentBufferSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIpTxFragmentBufferSize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpIpIpTxFragmentBufferSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpIpIpTxFragmentBufferSize = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpIp(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpIpIp.

        Returns:
            The tcpIpIp value

        Note:
            Delegates to tcp_ip_ip property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ip  # Delegates to property

    def setTcpIpIp(self, value: TimeValue) -> Ipv6FragmentationProps:
        """
        AUTOSAR-compliant setter for tcpIpIp with method chaining.

        Args:
            value: The tcpIpIp to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ip property setter (gets validation automatically)
        """
        self.tcp_ip_ip = value  # Delegates to property setter
        return self

    def getTcpIpIpReassemblyBufferSize(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpIpIpReassemblyBufferSize.

        Returns:
            The tcpIpIpReassemblyBufferSize value

        Note:
            Delegates to tcp_ip_ip_reassembly_buffer_size property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ip_reassembly_buffer_size  # Delegates to property

    def setTcpIpIpReassemblyBufferSize(self, value: PositiveInteger) -> Ipv6FragmentationProps:
        """
        AUTOSAR-compliant setter for tcpIpIpReassemblyBufferSize with method chaining.

        Args:
            value: The tcpIpIpReassemblyBufferSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ip_reassembly_buffer_size property setter (gets validation automatically)
        """
        self.tcp_ip_ip_reassembly_buffer_size = value  # Delegates to property setter
        return self

    def getTcpIpIpTx(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpIpIpTx.

        Returns:
            The tcpIpIpTx value

        Note:
            Delegates to tcp_ip_ip_tx property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ip_tx  # Delegates to property

    def setTcpIpIpTx(self, value: PositiveInteger) -> Ipv6FragmentationProps:
        """
        AUTOSAR-compliant setter for tcpIpIpTx with method chaining.

        Args:
            value: The tcpIpIpTx to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ip_tx property setter (gets validation automatically)
        """
        self.tcp_ip_ip_tx = value  # Delegates to property setter
        return self

    def getTcpIpIpTxFragmentBufferSize(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpIpIpTxFragmentBufferSize.

        Returns:
            The tcpIpIpTxFragmentBufferSize value

        Note:
            Delegates to tcp_ip_ip_tx_fragment_buffer_size property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ip_tx_fragment_buffer_size  # Delegates to property

    def setTcpIpIpTxFragmentBufferSize(self, value: PositiveInteger) -> Ipv6FragmentationProps:
        """
        AUTOSAR-compliant setter for tcpIpIpTxFragmentBufferSize with method chaining.

        Args:
            value: The tcpIpIpTxFragmentBufferSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ip_tx_fragment_buffer_size property setter (gets validation automatically)
        """
        self.tcp_ip_ip_tx_fragment_buffer_size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_ip(self, value: Optional[TimeValue]) -> Ipv6FragmentationProps:
        """
        Set tcpIpIp and return self for chaining.

        Args:
            value: The tcpIpIp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ip("value")
        """
        self.tcp_ip_ip = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ip_reassembly_buffer_size(self, value: Optional[PositiveInteger]) -> Ipv6FragmentationProps:
        """
        Set tcpIpIpReassemblyBufferSize and return self for chaining.

        Args:
            value: The tcpIpIpReassemblyBufferSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ip_reassembly_buffer_size("value")
        """
        self.tcp_ip_ip_reassembly_buffer_size = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ip_tx(self, value: Optional[PositiveInteger]) -> Ipv6FragmentationProps:
        """
        Set tcpIpIpTx and return self for chaining.

        Args:
            value: The tcpIpIpTx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ip_tx("value")
        """
        self.tcp_ip_ip_tx = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ip_tx_fragment_buffer_size(self, value: Optional[PositiveInteger]) -> Ipv6FragmentationProps:
        """
        Set tcpIpIpTxFragmentBufferSize and return self for chaining.

        Args:
            value: The tcpIpIpTxFragmentBufferSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ip_tx_fragment_buffer_size("value")
        """
        self.tcp_ip_ip_tx_fragment_buffer_size = value  # Use property setter (gets validation)
        return self



class Dhcpv6Props(ARObject):
    """
    This meta-class specifies the configuration options for DHCPv6.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Dhcpv6Props

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 149, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Minimum delay in seconds before the first Confirm will be sent.
        self._tcpIpDhcp: Optional[TimeValue] = None

    @property
    def tcp_ip_dhcp(self) -> Optional[TimeValue]:
        """Get tcpIpDhcp (Pythonic accessor)."""
        return self._tcpIpDhcp

    @tcp_ip_dhcp.setter
    def tcp_ip_dhcp(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpIpDhcp with validation.

        Args:
            value: The tcpIpDhcp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpDhcp = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpDhcp must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpDhcp = value
        self._tcpIpDhcpV6Inf: Optional[TimeValue] = None

    @property
    def tcp_ip_dhcp_v6_inf(self) -> Optional[TimeValue]:
        """Get tcpIpDhcpV6Inf (Pythonic accessor)."""
        return self._tcpIpDhcpV6Inf

    @tcp_ip_dhcp_v6_inf.setter
    def tcp_ip_dhcp_v6_inf(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpIpDhcpV6Inf with validation.

        Args:
            value: The tcpIpDhcpV6Inf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpDhcpV6Inf = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpDhcpV6Inf must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpDhcpV6Inf = value
        # Minimum delay (s) before the first Solicit message will be.
        self._tcpIpDhcpV6Sol: Optional[TimeValue] = None

    @property
    def tcp_ip_dhcp_v6_sol(self) -> Optional[TimeValue]:
        """Get tcpIpDhcpV6Sol (Pythonic accessor)."""
        return self._tcpIpDhcpV6Sol

    @tcp_ip_dhcp_v6_sol.setter
    def tcp_ip_dhcp_v6_sol(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpIpDhcpV6Sol with validation.

        Args:
            value: The tcpIpDhcpV6Sol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpDhcpV6Sol = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpDhcpV6Sol must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpDhcpV6Sol = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpDhcp(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpIpDhcp.

        Returns:
            The tcpIpDhcp value

        Note:
            Delegates to tcp_ip_dhcp property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_dhcp  # Delegates to property

    def setTcpIpDhcp(self, value: TimeValue) -> Dhcpv6Props:
        """
        AUTOSAR-compliant setter for tcpIpDhcp with method chaining.

        Args:
            value: The tcpIpDhcp to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_dhcp property setter (gets validation automatically)
        """
        self.tcp_ip_dhcp = value  # Delegates to property setter
        return self

    def getTcpIpDhcpV6Inf(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpIpDhcpV6Inf.

        Returns:
            The tcpIpDhcpV6Inf value

        Note:
            Delegates to tcp_ip_dhcp_v6_inf property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_dhcp_v6_inf  # Delegates to property

    def setTcpIpDhcpV6Inf(self, value: TimeValue) -> Dhcpv6Props:
        """
        AUTOSAR-compliant setter for tcpIpDhcpV6Inf with method chaining.

        Args:
            value: The tcpIpDhcpV6Inf to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_dhcp_v6_inf property setter (gets validation automatically)
        """
        self.tcp_ip_dhcp_v6_inf = value  # Delegates to property setter
        return self

    def getTcpIpDhcpV6Sol(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpIpDhcpV6Sol.

        Returns:
            The tcpIpDhcpV6Sol value

        Note:
            Delegates to tcp_ip_dhcp_v6_sol property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_dhcp_v6_sol  # Delegates to property

    def setTcpIpDhcpV6Sol(self, value: TimeValue) -> Dhcpv6Props:
        """
        AUTOSAR-compliant setter for tcpIpDhcpV6Sol with method chaining.

        Args:
            value: The tcpIpDhcpV6Sol to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_dhcp_v6_sol property setter (gets validation automatically)
        """
        self.tcp_ip_dhcp_v6_sol = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_dhcp(self, value: Optional[TimeValue]) -> Dhcpv6Props:
        """
        Set tcpIpDhcp and return self for chaining.

        Args:
            value: The tcpIpDhcp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_dhcp("value")
        """
        self.tcp_ip_dhcp = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_dhcp_v6_inf(self, value: Optional[TimeValue]) -> Dhcpv6Props:
        """
        Set tcpIpDhcpV6Inf and return self for chaining.

        Args:
            value: The tcpIpDhcpV6Inf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_dhcp_v6_inf("value")
        """
        self.tcp_ip_dhcp_v6_inf = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_dhcp_v6_sol(self, value: Optional[TimeValue]) -> Dhcpv6Props:
        """
        Set tcpIpDhcpV6Sol and return self for chaining.

        Args:
            value: The tcpIpDhcpV6Sol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_dhcp_v6_sol("value")
        """
        self.tcp_ip_dhcp_v6_sol = value  # Use property setter (gets validation)
        return self



class Ipv6NdpProps(ARObject):
    """
    This meta-class specifies the configuration options for the Neighbor
    Discovery Protocol for IPv6.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv6NdpProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 150, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Configures the default value (s) for the RetransTimer specified in [RFC4861
                # 6.
        # 3.
        # 2.
        # Host Variables].
        self._tcpIpNdpDefault: Optional[TimeValue] = None

    @property
    def tcp_ip_ndp_default(self) -> Optional[TimeValue]:
        """Get tcpIpNdpDefault (Pythonic accessor)."""
        return self._tcpIpNdpDefault

    @tcp_ip_ndp_default.setter
    def tcp_ip_ndp_default(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpIpNdpDefault with validation.

        Args:
            value: The tcpIpNdpDefault to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpDefault = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpNdpDefault must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpNdpDefault = value
        self._tcpIpNdpDefaultRouterListSize: Optional[PositiveInteger] = None

    @property
    def tcp_ip_ndp_default_router_list_size(self) -> Optional[PositiveInteger]:
        """Get tcpIpNdpDefaultRouterListSize (Pythonic accessor)."""
        return self._tcpIpNdpDefaultRouterListSize

    @tcp_ip_ndp_default_router_list_size.setter
    def tcp_ip_ndp_default_router_list_size(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpIpNdpDefaultRouterListSize with validation.

        Args:
            value: The tcpIpNdpDefaultRouterListSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpDefaultRouterListSize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpIpNdpDefaultRouterListSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpIpNdpDefaultRouterListSize = value
        # between MIN_RANDOM_FACTOR MAX_RANDOM_FACTOR in order to prevent nodes from
        # transmitting at exactly the same time.
        self._tcpIpNdp: Optional[Boolean] = None

    @property
    def tcp_ip_ndp(self) -> Optional[Boolean]:
        """Get tcpIpNdp (Pythonic accessor)."""
        return self._tcpIpNdp

    @tcp_ip_ndp.setter
    def tcp_ip_ndp(self, value: Optional[Boolean]) -> None:
        """
        Set tcpIpNdp with validation.

        Args:
            value: The tcpIpNdp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdp = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"tcpIpNdp must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._tcpIpNdp = value
        self._tcpIpNdpDelayFirstProbeTimeValue: Optional[TimeValue] = None

    @property
    def tcp_ip_ndp_delay_first_probe_time_value(self) -> Optional[TimeValue]:
        """Get tcpIpNdpDelayFirstProbeTimeValue (Pythonic accessor)."""
        return self._tcpIpNdpDelayFirstProbeTimeValue

    @tcp_ip_ndp_delay_first_probe_time_value.setter
    def tcp_ip_ndp_delay_first_probe_time_value(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpIpNdpDelayFirstProbeTimeValue with validation.

        Args:
            value: The tcpIpNdpDelayFirstProbeTimeValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpDelayFirstProbeTimeValue = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpNdpDelayFirstProbeTimeValue must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpNdpDelayFirstProbeTimeValue = value
        self._tcpIpNdpMaxRandomFactor: Optional[PositiveInteger] = None

    @property
    def tcp_ip_ndp_max_random_factor(self) -> Optional[PositiveInteger]:
        """Get tcpIpNdpMaxRandomFactor (Pythonic accessor)."""
        return self._tcpIpNdpMaxRandomFactor

    @tcp_ip_ndp_max_random_factor.setter
    def tcp_ip_ndp_max_random_factor(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpIpNdpMaxRandomFactor with validation.

        Args:
            value: The tcpIpNdpMaxRandomFactor to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpMaxRandomFactor = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpIpNdpMaxRandomFactor must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpIpNdpMaxRandomFactor = value
        # Advertisement has been received.
        self._tcpIpNdpMaxRtr: Optional[PositiveInteger] = None

    @property
    def tcp_ip_ndp_max_rtr(self) -> Optional[PositiveInteger]:
        """Get tcpIpNdpMaxRtr (Pythonic accessor)."""
        return self._tcpIpNdpMaxRtr

    @tcp_ip_ndp_max_rtr.setter
    def tcp_ip_ndp_max_rtr(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpIpNdpMaxRtr with validation.

        Args:
            value: The tcpIpNdpMaxRtr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpMaxRtr = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpIpNdpMaxRtr must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpIpNdpMaxRtr = value
        self._tcpIpNdpMinRandomFactor: Optional[PositiveInteger] = None

    @property
    def tcp_ip_ndp_min_random_factor(self) -> Optional[PositiveInteger]:
        """Get tcpIpNdpMinRandomFactor (Pythonic accessor)."""
        return self._tcpIpNdpMinRandomFactor

    @tcp_ip_ndp_min_random_factor.setter
    def tcp_ip_ndp_min_random_factor(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpIpNdpMinRandomFactor with validation.

        Args:
            value: The tcpIpNdpMinRandomFactor to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpMinRandomFactor = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpIpNdpMinRandomFactor must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpIpNdpMinRandomFactor = value
        # Unreachability Detection.
        self._tcpIpNdpNum: Optional[PositiveInteger] = None

    @property
    def tcp_ip_ndp_num(self) -> Optional[PositiveInteger]:
        """Get tcpIpNdpNum (Pythonic accessor)."""
        return self._tcpIpNdpNum

    @tcp_ip_ndp_num.setter
    def tcp_ip_ndp_num(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpIpNdpNum with validation.

        Args:
            value: The tcpIpNdpNum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpNum = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpIpNdpNum must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpIpNdpNum = value
        # RFC 4861, section.
        self._tcpIpNdpPacket: Optional[Boolean] = None

    @property
    def tcp_ip_ndp_packet(self) -> Optional[Boolean]:
        """Get tcpIpNdpPacket (Pythonic accessor)."""
        return self._tcpIpNdpPacket

    @tcp_ip_ndp_packet.setter
    def tcp_ip_ndp_packet(self, value: Optional[Boolean]) -> None:
        """
        Set tcpIpNdpPacket with validation.

        Args:
            value: The tcpIpNdpPacket to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpPacket = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"tcpIpNdpPacket must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._tcpIpNdpPacket = value
        self._tcpIpNdpPrefix: Optional[PositiveInteger] = None

    @property
    def tcp_ip_ndp_prefix(self) -> Optional[PositiveInteger]:
        """Get tcpIpNdpPrefix (Pythonic accessor)."""
        return self._tcpIpNdpPrefix

    @tcp_ip_ndp_prefix.setter
    def tcp_ip_ndp_prefix(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpIpNdpPrefix with validation.

        Args:
            value: The tcpIpNdpPrefix to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpPrefix = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpIpNdpPrefix must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpIpNdpPrefix = value
        # MAX_RTR_SOLICITATION_DELAY].
        # the first router solicitation will be sent after milliseconds.
        self._tcpIpNdpRndRtr: Optional[Boolean] = None

    @property
    def tcp_ip_ndp_rnd_rtr(self) -> Optional[Boolean]:
        """Get tcpIpNdpRndRtr (Pythonic accessor)."""
        return self._tcpIpNdpRndRtr

    @tcp_ip_ndp_rnd_rtr.setter
    def tcp_ip_ndp_rnd_rtr(self, value: Optional[Boolean]) -> None:
        """
        Set tcpIpNdpRndRtr with validation.

        Args:
            value: The tcpIpNdpRndRtr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpRndRtr = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"tcpIpNdpRndRtr must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._tcpIpNdpRndRtr = value
        self._tcpIpNdpRtr: Optional[TimeValue] = None

    @property
    def tcp_ip_ndp_rtr(self) -> Optional[TimeValue]:
        """Get tcpIpNdpRtr (Pythonic accessor)."""
        return self._tcpIpNdpRtr

    @tcp_ip_ndp_rtr.setter
    def tcp_ip_ndp_rtr(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpIpNdpRtr with validation.

        Args:
            value: The tcpIpNdpRtr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpRtr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpNdpRtr must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpNdpRtr = value
        self._tcpIpNdpSlaac: Optional[Boolean] = None

    @property
    def tcp_ip_ndp_slaac(self) -> Optional[Boolean]:
        """Get tcpIpNdpSlaac (Pythonic accessor)."""
        return self._tcpIpNdpSlaac

    @tcp_ip_ndp_slaac.setter
    def tcp_ip_ndp_slaac(self, value: Optional[Boolean]) -> None:
        """
        Set tcpIpNdpSlaac with validation.

        Args:
            value: The tcpIpNdpSlaac to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpSlaac = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"tcpIpNdpSlaac must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._tcpIpNdpSlaac = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpNdpDefault(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpIpNdpDefault.

        Returns:
            The tcpIpNdpDefault value

        Note:
            Delegates to tcp_ip_ndp_default property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_default  # Delegates to property

    def setTcpIpNdpDefault(self, value: TimeValue) -> Ipv6NdpProps:
        """
        AUTOSAR-compliant setter for tcpIpNdpDefault with method chaining.

        Args:
            value: The tcpIpNdpDefault to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_default property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_default = value  # Delegates to property setter
        return self

    def getTcpIpNdpDefaultRouterListSize(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpIpNdpDefaultRouterListSize.

        Returns:
            The tcpIpNdpDefaultRouterListSize value

        Note:
            Delegates to tcp_ip_ndp_default_router_list_size property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_default_router_list_size  # Delegates to property

    def setTcpIpNdpDefaultRouterListSize(self, value: PositiveInteger) -> Ipv6NdpProps:
        """
        AUTOSAR-compliant setter for tcpIpNdpDefaultRouterListSize with method chaining.

        Args:
            value: The tcpIpNdpDefaultRouterListSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_default_router_list_size property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_default_router_list_size = value  # Delegates to property setter
        return self

    def getTcpIpNdp(self) -> Boolean:
        """
        AUTOSAR-compliant getter for tcpIpNdp.

        Returns:
            The tcpIpNdp value

        Note:
            Delegates to tcp_ip_ndp property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp  # Delegates to property

    def setTcpIpNdp(self, value: Boolean) -> Ipv6NdpProps:
        """
        AUTOSAR-compliant setter for tcpIpNdp with method chaining.

        Args:
            value: The tcpIpNdp to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp property setter (gets validation automatically)
        """
        self.tcp_ip_ndp = value  # Delegates to property setter
        return self

    def getTcpIpNdpDelayFirstProbeTimeValue(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpIpNdpDelayFirstProbeTimeValue.

        Returns:
            The tcpIpNdpDelayFirstProbeTimeValue value

        Note:
            Delegates to tcp_ip_ndp_delay_first_probe_time_value property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_delay_first_probe_time_value  # Delegates to property

    def setTcpIpNdpDelayFirstProbeTimeValue(self, value: TimeValue) -> Ipv6NdpProps:
        """
        AUTOSAR-compliant setter for tcpIpNdpDelayFirstProbeTimeValue with method chaining.

        Args:
            value: The tcpIpNdpDelayFirstProbeTimeValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_delay_first_probe_time_value property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_delay_first_probe_time_value = value  # Delegates to property setter
        return self

    def getTcpIpNdpMaxRandomFactor(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpIpNdpMaxRandomFactor.

        Returns:
            The tcpIpNdpMaxRandomFactor value

        Note:
            Delegates to tcp_ip_ndp_max_random_factor property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_max_random_factor  # Delegates to property

    def setTcpIpNdpMaxRandomFactor(self, value: PositiveInteger) -> Ipv6NdpProps:
        """
        AUTOSAR-compliant setter for tcpIpNdpMaxRandomFactor with method chaining.

        Args:
            value: The tcpIpNdpMaxRandomFactor to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_max_random_factor property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_max_random_factor = value  # Delegates to property setter
        return self

    def getTcpIpNdpMaxRtr(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpIpNdpMaxRtr.

        Returns:
            The tcpIpNdpMaxRtr value

        Note:
            Delegates to tcp_ip_ndp_max_rtr property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_max_rtr  # Delegates to property

    def setTcpIpNdpMaxRtr(self, value: PositiveInteger) -> Ipv6NdpProps:
        """
        AUTOSAR-compliant setter for tcpIpNdpMaxRtr with method chaining.

        Args:
            value: The tcpIpNdpMaxRtr to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_max_rtr property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_max_rtr = value  # Delegates to property setter
        return self

    def getTcpIpNdpMinRandomFactor(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpIpNdpMinRandomFactor.

        Returns:
            The tcpIpNdpMinRandomFactor value

        Note:
            Delegates to tcp_ip_ndp_min_random_factor property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_min_random_factor  # Delegates to property

    def setTcpIpNdpMinRandomFactor(self, value: PositiveInteger) -> Ipv6NdpProps:
        """
        AUTOSAR-compliant setter for tcpIpNdpMinRandomFactor with method chaining.

        Args:
            value: The tcpIpNdpMinRandomFactor to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_min_random_factor property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_min_random_factor = value  # Delegates to property setter
        return self

    def getTcpIpNdpNum(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpIpNdpNum.

        Returns:
            The tcpIpNdpNum value

        Note:
            Delegates to tcp_ip_ndp_num property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_num  # Delegates to property

    def setTcpIpNdpNum(self, value: PositiveInteger) -> Ipv6NdpProps:
        """
        AUTOSAR-compliant setter for tcpIpNdpNum with method chaining.

        Args:
            value: The tcpIpNdpNum to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_num property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_num = value  # Delegates to property setter
        return self

    def getTcpIpNdpPacket(self) -> Boolean:
        """
        AUTOSAR-compliant getter for tcpIpNdpPacket.

        Returns:
            The tcpIpNdpPacket value

        Note:
            Delegates to tcp_ip_ndp_packet property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_packet  # Delegates to property

    def setTcpIpNdpPacket(self, value: Boolean) -> Ipv6NdpProps:
        """
        AUTOSAR-compliant setter for tcpIpNdpPacket with method chaining.

        Args:
            value: The tcpIpNdpPacket to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_packet property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_packet = value  # Delegates to property setter
        return self

    def getTcpIpNdpPrefix(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpIpNdpPrefix.

        Returns:
            The tcpIpNdpPrefix value

        Note:
            Delegates to tcp_ip_ndp_prefix property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_prefix  # Delegates to property

    def setTcpIpNdpPrefix(self, value: PositiveInteger) -> Ipv6NdpProps:
        """
        AUTOSAR-compliant setter for tcpIpNdpPrefix with method chaining.

        Args:
            value: The tcpIpNdpPrefix to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_prefix property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_prefix = value  # Delegates to property setter
        return self

    def getTcpIpNdpRndRtr(self) -> Boolean:
        """
        AUTOSAR-compliant getter for tcpIpNdpRndRtr.

        Returns:
            The tcpIpNdpRndRtr value

        Note:
            Delegates to tcp_ip_ndp_rnd_rtr property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_rnd_rtr  # Delegates to property

    def setTcpIpNdpRndRtr(self, value: Boolean) -> Ipv6NdpProps:
        """
        AUTOSAR-compliant setter for tcpIpNdpRndRtr with method chaining.

        Args:
            value: The tcpIpNdpRndRtr to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_rnd_rtr property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_rnd_rtr = value  # Delegates to property setter
        return self

    def getTcpIpNdpRtr(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpIpNdpRtr.

        Returns:
            The tcpIpNdpRtr value

        Note:
            Delegates to tcp_ip_ndp_rtr property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_rtr  # Delegates to property

    def setTcpIpNdpRtr(self, value: TimeValue) -> Ipv6NdpProps:
        """
        AUTOSAR-compliant setter for tcpIpNdpRtr with method chaining.

        Args:
            value: The tcpIpNdpRtr to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_rtr property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_rtr = value  # Delegates to property setter
        return self

    def getTcpIpNdpSlaac(self) -> Boolean:
        """
        AUTOSAR-compliant getter for tcpIpNdpSlaac.

        Returns:
            The tcpIpNdpSlaac value

        Note:
            Delegates to tcp_ip_ndp_slaac property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_slaac  # Delegates to property

    def setTcpIpNdpSlaac(self, value: Boolean) -> Ipv6NdpProps:
        """
        AUTOSAR-compliant setter for tcpIpNdpSlaac with method chaining.

        Args:
            value: The tcpIpNdpSlaac to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_slaac property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_slaac = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_ndp_default(self, value: Optional[TimeValue]) -> Ipv6NdpProps:
        """
        Set tcpIpNdpDefault and return self for chaining.

        Args:
            value: The tcpIpNdpDefault to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_default("value")
        """
        self.tcp_ip_ndp_default = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_default_router_list_size(self, value: Optional[PositiveInteger]) -> Ipv6NdpProps:
        """
        Set tcpIpNdpDefaultRouterListSize and return self for chaining.

        Args:
            value: The tcpIpNdpDefaultRouterListSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_default_router_list_size("value")
        """
        self.tcp_ip_ndp_default_router_list_size = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp(self, value: Optional[Boolean]) -> Ipv6NdpProps:
        """
        Set tcpIpNdp and return self for chaining.

        Args:
            value: The tcpIpNdp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp("value")
        """
        self.tcp_ip_ndp = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_delay_first_probe_time_value(self, value: Optional[TimeValue]) -> Ipv6NdpProps:
        """
        Set tcpIpNdpDelayFirstProbeTimeValue and return self for chaining.

        Args:
            value: The tcpIpNdpDelayFirstProbeTimeValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_delay_first_probe_time_value("value")
        """
        self.tcp_ip_ndp_delay_first_probe_time_value = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_max_random_factor(self, value: Optional[PositiveInteger]) -> Ipv6NdpProps:
        """
        Set tcpIpNdpMaxRandomFactor and return self for chaining.

        Args:
            value: The tcpIpNdpMaxRandomFactor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_max_random_factor("value")
        """
        self.tcp_ip_ndp_max_random_factor = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_max_rtr(self, value: Optional[PositiveInteger]) -> Ipv6NdpProps:
        """
        Set tcpIpNdpMaxRtr and return self for chaining.

        Args:
            value: The tcpIpNdpMaxRtr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_max_rtr("value")
        """
        self.tcp_ip_ndp_max_rtr = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_min_random_factor(self, value: Optional[PositiveInteger]) -> Ipv6NdpProps:
        """
        Set tcpIpNdpMinRandomFactor and return self for chaining.

        Args:
            value: The tcpIpNdpMinRandomFactor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_min_random_factor("value")
        """
        self.tcp_ip_ndp_min_random_factor = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_num(self, value: Optional[PositiveInteger]) -> Ipv6NdpProps:
        """
        Set tcpIpNdpNum and return self for chaining.

        Args:
            value: The tcpIpNdpNum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_num("value")
        """
        self.tcp_ip_ndp_num = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_packet(self, value: Optional[Boolean]) -> Ipv6NdpProps:
        """
        Set tcpIpNdpPacket and return self for chaining.

        Args:
            value: The tcpIpNdpPacket to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_packet("value")
        """
        self.tcp_ip_ndp_packet = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_prefix(self, value: Optional[PositiveInteger]) -> Ipv6NdpProps:
        """
        Set tcpIpNdpPrefix and return self for chaining.

        Args:
            value: The tcpIpNdpPrefix to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_prefix("value")
        """
        self.tcp_ip_ndp_prefix = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_rnd_rtr(self, value: Optional[Boolean]) -> Ipv6NdpProps:
        """
        Set tcpIpNdpRndRtr and return self for chaining.

        Args:
            value: The tcpIpNdpRndRtr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_rnd_rtr("value")
        """
        self.tcp_ip_ndp_rnd_rtr = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_rtr(self, value: Optional[TimeValue]) -> Ipv6NdpProps:
        """
        Set tcpIpNdpRtr and return self for chaining.

        Args:
            value: The tcpIpNdpRtr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_rtr("value")
        """
        self.tcp_ip_ndp_rtr = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_slaac(self, value: Optional[Boolean]) -> Ipv6NdpProps:
        """
        Set tcpIpNdpSlaac and return self for chaining.

        Args:
            value: The tcpIpNdpSlaac to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_slaac("value")
        """
        self.tcp_ip_ndp_slaac = value  # Use property setter (gets validation)
        return self



class EthTcpIpProps(ARElement):
    """
    This meta-class is used to configure the EcuInstance specific TcpIp Stack
    attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthTcpIpProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 153, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # TCP configuration properties.
        self._tcpProps: Optional[TcpProps] = None

    @property
    def tcp_props(self) -> Optional[TcpProps]:
        """Get tcpProps (Pythonic accessor)."""
        return self._tcpProps

    @tcp_props.setter
    def tcp_props(self, value: Optional[TcpProps]) -> None:
        """
        Set tcpProps with validation.

        Args:
            value: The tcpProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpProps = None
            return

        if not isinstance(value, TcpProps):
            raise TypeError(
                f"tcpProps must be TcpProps or None, got {type(value).__name__}"
            )
        self._tcpProps = value
        self._udpProps: Optional[UdpProps] = None

    @property
    def udp_props(self) -> Optional[UdpProps]:
        """Get udpProps (Pythonic accessor)."""
        return self._udpProps

    @udp_props.setter
    def udp_props(self, value: Optional[UdpProps]) -> None:
        """
        Set udpProps with validation.

        Args:
            value: The udpProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._udpProps = None
            return

        if not isinstance(value, UdpProps):
            raise TypeError(
                f"udpProps must be UdpProps or None, got {type(value).__name__}"
            )
        self._udpProps = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpProps(self) -> TcpProps:
        """
        AUTOSAR-compliant getter for tcpProps.

        Returns:
            The tcpProps value

        Note:
            Delegates to tcp_props property (CODING_RULE_V2_00017)
        """
        return self.tcp_props  # Delegates to property

    def setTcpProps(self, value: TcpProps) -> EthTcpIpProps:
        """
        AUTOSAR-compliant setter for tcpProps with method chaining.

        Args:
            value: The tcpProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_props property setter (gets validation automatically)
        """
        self.tcp_props = value  # Delegates to property setter
        return self

    def getUdpProps(self) -> UdpProps:
        """
        AUTOSAR-compliant getter for udpProps.

        Returns:
            The udpProps value

        Note:
            Delegates to udp_props property (CODING_RULE_V2_00017)
        """
        return self.udp_props  # Delegates to property

    def setUdpProps(self, value: UdpProps) -> EthTcpIpProps:
        """
        AUTOSAR-compliant setter for udpProps with method chaining.

        Args:
            value: The udpProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to udp_props property setter (gets validation automatically)
        """
        self.udp_props = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_props(self, value: Optional[TcpProps]) -> EthTcpIpProps:
        """
        Set tcpProps and return self for chaining.

        Args:
            value: The tcpProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_props("value")
        """
        self.tcp_props = value  # Use property setter (gets validation)
        return self

    def with_udp_props(self, value: Optional[UdpProps]) -> EthTcpIpProps:
        """
        Set udpProps and return self for chaining.

        Args:
            value: The udpProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_udp_props("value")
        """
        self.udp_props = value  # Use property setter (gets validation)
        return self



class UdpProps(ARObject):
    """
    This meta-class specifies the configuration options for UDP (User Datagram
    Protocol).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::UdpProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 154, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Default Time-to-live value of outgoing UDP packets.
        self._udpTtl: Optional[PositiveInteger] = None

    @property
    def udp_ttl(self) -> Optional[PositiveInteger]:
        """Get udpTtl (Pythonic accessor)."""
        return self._udpTtl

    @udp_ttl.setter
    def udp_ttl(self, value: Optional[PositiveInteger]) -> None:
        """
        Set udpTtl with validation.

        Args:
            value: The udpTtl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._udpTtl = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"udpTtl must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._udpTtl = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getUdpTtl(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for udpTtl.

        Returns:
            The udpTtl value

        Note:
            Delegates to udp_ttl property (CODING_RULE_V2_00017)
        """
        return self.udp_ttl  # Delegates to property

    def setUdpTtl(self, value: PositiveInteger) -> UdpProps:
        """
        AUTOSAR-compliant setter for udpTtl with method chaining.

        Args:
            value: The udpTtl to set

        Returns:
            self for method chaining

        Note:
            Delegates to udp_ttl property setter (gets validation automatically)
        """
        self.udp_ttl = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_udp_ttl(self, value: Optional[PositiveInteger]) -> UdpProps:
        """
        Set udpTtl and return self for chaining.

        Args:
            value: The udpTtl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_udp_ttl("value")
        """
        self.udp_ttl = value  # Use property setter (gets validation)
        return self



class TcpProps(ARObject):
    """
    This meta-class specifies the configuration options for TCP (Transmission
    Control Protocol).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TcpProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 154, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Enables (TRUE) or disables (FALSE) support of TCP avoidance algorithm
        # according to IETF RFC.
        self._tcpCongestion: Optional[Boolean] = None

    @property
    def tcp_congestion(self) -> Optional[Boolean]:
        """Get tcpCongestion (Pythonic accessor)."""
        return self._tcpCongestion

    @tcp_congestion.setter
    def tcp_congestion(self, value: Optional[Boolean]) -> None:
        """
        Set tcpCongestion with validation.

        Args:
            value: The tcpCongestion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpCongestion = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"tcpCongestion must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._tcpCongestion = value
        self._tcpDelayedAck: Optional[TimeValue] = None

    @property
    def tcp_delayed_ack(self) -> Optional[TimeValue]:
        """Get tcpDelayedAck (Pythonic accessor)."""
        return self._tcpDelayedAck

    @tcp_delayed_ack.setter
    def tcp_delayed_ack(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpDelayedAck with validation.

        Args:
            value: The tcpDelayedAck to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpDelayedAck = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpDelayedAck must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpDelayedAck = value
        # 5681.
        self._tcpFast: Optional[Boolean] = None

    @property
    def tcp_fast(self) -> Optional[Boolean]:
        """Get tcpFast (Pythonic accessor)."""
        return self._tcpFast

    @tcp_fast.setter
    def tcp_fast(self, value: Optional[Boolean]) -> None:
        """
        Set tcpFast with validation.

        Args:
            value: The tcpFast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpFast = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"tcpFast must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._tcpFast = value
                # connection termination), i.
        # e.
        # waiting in FINWAIT-2 for a connection from the remote TCP.
        self._tcpFin: Optional[TimeValue] = None

    @property
    def tcp_fin(self) -> Optional[TimeValue]:
        """Get tcpFin (Pythonic accessor)."""
        return self._tcpFin

    @tcp_fin.setter
    def tcp_fin(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpFin with validation.

        Args:
            value: The tcpFin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpFin = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpFin must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpFin = value
        # considered data) and the first.
        self._tcpKeepAlive: Optional[TimeValue] = None

    @property
    def tcp_keep_alive(self) -> Optional[TimeValue]:
        """Get tcpKeepAlive (Pythonic accessor)."""
        return self._tcpKeepAlive

    @tcp_keep_alive.setter
    def tcp_keep_alive(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpKeepAlive with validation.

        Args:
            value: The tcpKeepAlive to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpKeepAlive = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpKeepAlive must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpKeepAlive = value
        # This only valid if tcpRetransmissionTimeout is This parameter also applies
                # for FIN.
        self._tcpMaxRtx: Optional[PositiveInteger] = None

    @property
    def tcp_max_rtx(self) -> Optional[PositiveInteger]:
        """Get tcpMaxRtx (Pythonic accessor)."""
        return self._tcpMaxRtx

    @tcp_max_rtx.setter
    def tcp_max_rtx(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpMaxRtx with validation.

        Args:
            value: The tcpMaxRtx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpMaxRtx = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpMaxRtx must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpMaxRtx = value
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._tcpMsl: Optional[TimeValue] = None

    @property
    def tcp_msl(self) -> Optional[TimeValue]:
        """Get tcpMsl (Pythonic accessor)."""
        return self._tcpMsl

    @tcp_msl.setter
    def tcp_msl(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpMsl with validation.

        Args:
            value: The tcpMsl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpMsl = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpMsl must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpMsl = value
                # 1122 (chapter 4.
        # 2.
        # 3.
        # 4 Send Data).
        # If enabled the Nagle’s algorithm is default for all TCP sockets, but can be
                # Socket (with the attribute TcpTp.
        # nagle.
        self._tcpNagle: Optional[Boolean] = None

    @property
    def tcp_nagle(self) -> Optional[Boolean]:
        """Get tcpNagle (Pythonic accessor)."""
        return self._tcpNagle

    @tcp_nagle.setter
    def tcp_nagle(self, value: Optional[Boolean]) -> None:
        """
        Set tcpNagle with validation.

        Args:
            value: The tcpNagle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpNagle = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"tcpNagle must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._tcpNagle = value
        self._tcpReceiveWindowMax: Optional[PositiveInteger] = None

    @property
    def tcp_receive_window_max(self) -> Optional[PositiveInteger]:
        """Get tcpReceiveWindowMax (Pythonic accessor)."""
        return self._tcpReceiveWindowMax

    @tcp_receive_window_max.setter
    def tcp_receive_window_max(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpReceiveWindowMax with validation.

        Args:
            value: The tcpReceiveWindowMax to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpReceiveWindowMax = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpReceiveWindowMax must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpReceiveWindowMax = value
        # If the timeout is disabled, no TCP segments be retransmitted.
        self._tcp: Optional[TimeValue] = None

    @property
    def tcp(self) -> Optional[TimeValue]:
        """Get tcp (Pythonic accessor)."""
        return self._tcp

    @tcp.setter
    def tcp(self, value: Optional[TimeValue]) -> None:
        """
        Set tcp with validation.

        Args:
            value: The tcp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcp = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcp must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcp = value
        # to IETF RFC 5681.
        self._tcpSlowStart: Optional[Boolean] = None

    @property
    def tcp_slow_start(self) -> Optional[Boolean]:
        """Get tcpSlowStart (Pythonic accessor)."""
        return self._tcpSlowStart

    @tcp_slow_start.setter
    def tcp_slow_start(self, value: Optional[Boolean]) -> None:
        """
        Set tcpSlowStart with validation.

        Args:
            value: The tcpSlowStart to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpSlowStart = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"tcpSlowStart must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._tcpSlowStart = value
        self._tcpSynMaxRtx: Optional[PositiveInteger] = None

    @property
    def tcp_syn_max_rtx(self) -> Optional[PositiveInteger]:
        """Get tcpSynMaxRtx (Pythonic accessor)."""
        return self._tcpSynMaxRtx

    @tcp_syn_max_rtx.setter
    def tcp_syn_max_rtx(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpSynMaxRtx with validation.

        Args:
            value: The tcpSynMaxRtx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpSynMaxRtx = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpSynMaxRtx must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpSynMaxRtx = value
        # e.
        # maximum time waiting in a confirming connection request having both received
                # and sent a.
        self._tcpSynReceived: Optional[TimeValue] = None

    @property
    def tcp_syn_received(self) -> Optional[TimeValue]:
        """Get tcpSynReceived (Pythonic accessor)."""
        return self._tcpSynReceived

    @tcp_syn_received.setter
    def tcp_syn_received(self, value: Optional[TimeValue]) -> None:
        """
        Set tcpSynReceived with validation.

        Args:
            value: The tcpSynReceived to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpSynReceived = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpSynReceived must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpSynReceived = value
        self._tcpTtl: Optional[PositiveInteger] = None

    @property
    def tcp_ttl(self) -> Optional[PositiveInteger]:
        """Get tcpTtl (Pythonic accessor)."""
        return self._tcpTtl

    @tcp_ttl.setter
    def tcp_ttl(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpTtl with validation.

        Args:
            value: The tcpTtl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpTtl = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpTtl must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpTtl = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpCongestion(self) -> Boolean:
        """
        AUTOSAR-compliant getter for tcpCongestion.

        Returns:
            The tcpCongestion value

        Note:
            Delegates to tcp_congestion property (CODING_RULE_V2_00017)
        """
        return self.tcp_congestion  # Delegates to property

    def setTcpCongestion(self, value: Boolean) -> TcpProps:
        """
        AUTOSAR-compliant setter for tcpCongestion with method chaining.

        Args:
            value: The tcpCongestion to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_congestion property setter (gets validation automatically)
        """
        self.tcp_congestion = value  # Delegates to property setter
        return self

    def getTcpDelayedAck(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpDelayedAck.

        Returns:
            The tcpDelayedAck value

        Note:
            Delegates to tcp_delayed_ack property (CODING_RULE_V2_00017)
        """
        return self.tcp_delayed_ack  # Delegates to property

    def setTcpDelayedAck(self, value: TimeValue) -> TcpProps:
        """
        AUTOSAR-compliant setter for tcpDelayedAck with method chaining.

        Args:
            value: The tcpDelayedAck to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_delayed_ack property setter (gets validation automatically)
        """
        self.tcp_delayed_ack = value  # Delegates to property setter
        return self

    def getTcpFast(self) -> Boolean:
        """
        AUTOSAR-compliant getter for tcpFast.

        Returns:
            The tcpFast value

        Note:
            Delegates to tcp_fast property (CODING_RULE_V2_00017)
        """
        return self.tcp_fast  # Delegates to property

    def setTcpFast(self, value: Boolean) -> TcpProps:
        """
        AUTOSAR-compliant setter for tcpFast with method chaining.

        Args:
            value: The tcpFast to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_fast property setter (gets validation automatically)
        """
        self.tcp_fast = value  # Delegates to property setter
        return self

    def getTcpFin(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpFin.

        Returns:
            The tcpFin value

        Note:
            Delegates to tcp_fin property (CODING_RULE_V2_00017)
        """
        return self.tcp_fin  # Delegates to property

    def setTcpFin(self, value: TimeValue) -> TcpProps:
        """
        AUTOSAR-compliant setter for tcpFin with method chaining.

        Args:
            value: The tcpFin to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_fin property setter (gets validation automatically)
        """
        self.tcp_fin = value  # Delegates to property setter
        return self

    def getTcpKeepAlive(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpKeepAlive.

        Returns:
            The tcpKeepAlive value

        Note:
            Delegates to tcp_keep_alive property (CODING_RULE_V2_00017)
        """
        return self.tcp_keep_alive  # Delegates to property

    def setTcpKeepAlive(self, value: TimeValue) -> TcpProps:
        """
        AUTOSAR-compliant setter for tcpKeepAlive with method chaining.

        Args:
            value: The tcpKeepAlive to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_keep_alive property setter (gets validation automatically)
        """
        self.tcp_keep_alive = value  # Delegates to property setter
        return self

    def getTcpMaxRtx(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpMaxRtx.

        Returns:
            The tcpMaxRtx value

        Note:
            Delegates to tcp_max_rtx property (CODING_RULE_V2_00017)
        """
        return self.tcp_max_rtx  # Delegates to property

    def setTcpMaxRtx(self, value: PositiveInteger) -> TcpProps:
        """
        AUTOSAR-compliant setter for tcpMaxRtx with method chaining.

        Args:
            value: The tcpMaxRtx to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_max_rtx property setter (gets validation automatically)
        """
        self.tcp_max_rtx = value  # Delegates to property setter
        return self

    def getTcpMsl(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpMsl.

        Returns:
            The tcpMsl value

        Note:
            Delegates to tcp_msl property (CODING_RULE_V2_00017)
        """
        return self.tcp_msl  # Delegates to property

    def setTcpMsl(self, value: TimeValue) -> TcpProps:
        """
        AUTOSAR-compliant setter for tcpMsl with method chaining.

        Args:
            value: The tcpMsl to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_msl property setter (gets validation automatically)
        """
        self.tcp_msl = value  # Delegates to property setter
        return self

    def getTcpNagle(self) -> Boolean:
        """
        AUTOSAR-compliant getter for tcpNagle.

        Returns:
            The tcpNagle value

        Note:
            Delegates to tcp_nagle property (CODING_RULE_V2_00017)
        """
        return self.tcp_nagle  # Delegates to property

    def setTcpNagle(self, value: Boolean) -> TcpProps:
        """
        AUTOSAR-compliant setter for tcpNagle with method chaining.

        Args:
            value: The tcpNagle to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_nagle property setter (gets validation automatically)
        """
        self.tcp_nagle = value  # Delegates to property setter
        return self

    def getTcpReceiveWindowMax(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpReceiveWindowMax.

        Returns:
            The tcpReceiveWindowMax value

        Note:
            Delegates to tcp_receive_window_max property (CODING_RULE_V2_00017)
        """
        return self.tcp_receive_window_max  # Delegates to property

    def setTcpReceiveWindowMax(self, value: PositiveInteger) -> TcpProps:
        """
        AUTOSAR-compliant setter for tcpReceiveWindowMax with method chaining.

        Args:
            value: The tcpReceiveWindowMax to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_receive_window_max property setter (gets validation automatically)
        """
        self.tcp_receive_window_max = value  # Delegates to property setter
        return self

    def getTcp(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcp.

        Returns:
            The tcp value

        Note:
            Delegates to tcp property (CODING_RULE_V2_00017)
        """
        return self.tcp  # Delegates to property

    def setTcp(self, value: TimeValue) -> TcpProps:
        """
        AUTOSAR-compliant setter for tcp with method chaining.

        Args:
            value: The tcp to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp property setter (gets validation automatically)
        """
        self.tcp = value  # Delegates to property setter
        return self

    def getTcpSlowStart(self) -> Boolean:
        """
        AUTOSAR-compliant getter for tcpSlowStart.

        Returns:
            The tcpSlowStart value

        Note:
            Delegates to tcp_slow_start property (CODING_RULE_V2_00017)
        """
        return self.tcp_slow_start  # Delegates to property

    def setTcpSlowStart(self, value: Boolean) -> TcpProps:
        """
        AUTOSAR-compliant setter for tcpSlowStart with method chaining.

        Args:
            value: The tcpSlowStart to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_slow_start property setter (gets validation automatically)
        """
        self.tcp_slow_start = value  # Delegates to property setter
        return self

    def getTcpSynMaxRtx(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpSynMaxRtx.

        Returns:
            The tcpSynMaxRtx value

        Note:
            Delegates to tcp_syn_max_rtx property (CODING_RULE_V2_00017)
        """
        return self.tcp_syn_max_rtx  # Delegates to property

    def setTcpSynMaxRtx(self, value: PositiveInteger) -> TcpProps:
        """
        AUTOSAR-compliant setter for tcpSynMaxRtx with method chaining.

        Args:
            value: The tcpSynMaxRtx to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_syn_max_rtx property setter (gets validation automatically)
        """
        self.tcp_syn_max_rtx = value  # Delegates to property setter
        return self

    def getTcpSynReceived(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcpSynReceived.

        Returns:
            The tcpSynReceived value

        Note:
            Delegates to tcp_syn_received property (CODING_RULE_V2_00017)
        """
        return self.tcp_syn_received  # Delegates to property

    def setTcpSynReceived(self, value: TimeValue) -> TcpProps:
        """
        AUTOSAR-compliant setter for tcpSynReceived with method chaining.

        Args:
            value: The tcpSynReceived to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_syn_received property setter (gets validation automatically)
        """
        self.tcp_syn_received = value  # Delegates to property setter
        return self

    def getTcpTtl(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpTtl.

        Returns:
            The tcpTtl value

        Note:
            Delegates to tcp_ttl property (CODING_RULE_V2_00017)
        """
        return self.tcp_ttl  # Delegates to property

    def setTcpTtl(self, value: PositiveInteger) -> TcpProps:
        """
        AUTOSAR-compliant setter for tcpTtl with method chaining.

        Args:
            value: The tcpTtl to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ttl property setter (gets validation automatically)
        """
        self.tcp_ttl = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_congestion(self, value: Optional[Boolean]) -> TcpProps:
        """
        Set tcpCongestion and return self for chaining.

        Args:
            value: The tcpCongestion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_congestion("value")
        """
        self.tcp_congestion = value  # Use property setter (gets validation)
        return self

    def with_tcp_delayed_ack(self, value: Optional[TimeValue]) -> TcpProps:
        """
        Set tcpDelayedAck and return self for chaining.

        Args:
            value: The tcpDelayedAck to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_delayed_ack("value")
        """
        self.tcp_delayed_ack = value  # Use property setter (gets validation)
        return self

    def with_tcp_fast(self, value: Optional[Boolean]) -> TcpProps:
        """
        Set tcpFast and return self for chaining.

        Args:
            value: The tcpFast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_fast("value")
        """
        self.tcp_fast = value  # Use property setter (gets validation)
        return self

    def with_tcp_fin(self, value: Optional[TimeValue]) -> TcpProps:
        """
        Set tcpFin and return self for chaining.

        Args:
            value: The tcpFin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_fin("value")
        """
        self.tcp_fin = value  # Use property setter (gets validation)
        return self

    def with_tcp_keep_alive(self, value: Optional[TimeValue]) -> TcpProps:
        """
        Set tcpKeepAlive and return self for chaining.

        Args:
            value: The tcpKeepAlive to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_keep_alive("value")
        """
        self.tcp_keep_alive = value  # Use property setter (gets validation)
        return self

    def with_tcp_max_rtx(self, value: Optional[PositiveInteger]) -> TcpProps:
        """
        Set tcpMaxRtx and return self for chaining.

        Args:
            value: The tcpMaxRtx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_max_rtx("value")
        """
        self.tcp_max_rtx = value  # Use property setter (gets validation)
        return self

    def with_tcp_msl(self, value: Optional[TimeValue]) -> TcpProps:
        """
        Set tcpMsl and return self for chaining.

        Args:
            value: The tcpMsl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_msl("value")
        """
        self.tcp_msl = value  # Use property setter (gets validation)
        return self

    def with_tcp_nagle(self, value: Optional[Boolean]) -> TcpProps:
        """
        Set tcpNagle and return self for chaining.

        Args:
            value: The tcpNagle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_nagle("value")
        """
        self.tcp_nagle = value  # Use property setter (gets validation)
        return self

    def with_tcp_receive_window_max(self, value: Optional[PositiveInteger]) -> TcpProps:
        """
        Set tcpReceiveWindowMax and return self for chaining.

        Args:
            value: The tcpReceiveWindowMax to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_receive_window_max("value")
        """
        self.tcp_receive_window_max = value  # Use property setter (gets validation)
        return self

    def with_tcp(self, value: Optional[TimeValue]) -> TcpProps:
        """
        Set tcp and return self for chaining.

        Args:
            value: The tcp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp("value")
        """
        self.tcp = value  # Use property setter (gets validation)
        return self

    def with_tcp_slow_start(self, value: Optional[Boolean]) -> TcpProps:
        """
        Set tcpSlowStart and return self for chaining.

        Args:
            value: The tcpSlowStart to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_slow_start("value")
        """
        self.tcp_slow_start = value  # Use property setter (gets validation)
        return self

    def with_tcp_syn_max_rtx(self, value: Optional[PositiveInteger]) -> TcpProps:
        """
        Set tcpSynMaxRtx and return self for chaining.

        Args:
            value: The tcpSynMaxRtx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_syn_max_rtx("value")
        """
        self.tcp_syn_max_rtx = value  # Use property setter (gets validation)
        return self

    def with_tcp_syn_received(self, value: Optional[TimeValue]) -> TcpProps:
        """
        Set tcpSynReceived and return self for chaining.

        Args:
            value: The tcpSynReceived to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_syn_received("value")
        """
        self.tcp_syn_received = value  # Use property setter (gets validation)
        return self

    def with_tcp_ttl(self, value: Optional[PositiveInteger]) -> TcpProps:
        """
        Set tcpTtl and return self for chaining.

        Args:
            value: The tcpTtl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ttl("value")
        """
        self.tcp_ttl = value  # Use property setter (gets validation)
        return self



class EthTcpIpIcmpProps(ARElement):
    """
    This meta-class is used to configure the EcuInstance specific ICMP (Internet
    Control Message Protocol) attributes

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthTcpIpIcmpProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 156, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ICMPv4 configuration properties.
        self._icmpV4Props: Optional[TcpIpIcmpv4Props] = None

    @property
    def icmp_v4_props(self) -> Optional[TcpIpIcmpv4Props]:
        """Get icmpV4Props (Pythonic accessor)."""
        return self._icmpV4Props

    @icmp_v4_props.setter
    def icmp_v4_props(self, value: Optional[TcpIpIcmpv4Props]) -> None:
        """
        Set icmpV4Props with validation.

        Args:
            value: The icmpV4Props to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._icmpV4Props = None
            return

        if not isinstance(value, TcpIpIcmpv4Props):
            raise TypeError(
                f"icmpV4Props must be TcpIpIcmpv4Props or None, got {type(value).__name__}"
            )
        self._icmpV4Props = value
        # ICMPv6 configuration properties.
        self._icmpV6Props: Optional[TcpIpIcmpv6Props] = None

    @property
    def icmp_v6_props(self) -> Optional[TcpIpIcmpv6Props]:
        """Get icmpV6Props (Pythonic accessor)."""
        return self._icmpV6Props

    @icmp_v6_props.setter
    def icmp_v6_props(self, value: Optional[TcpIpIcmpv6Props]) -> None:
        """
        Set icmpV6Props with validation.

        Args:
            value: The icmpV6Props to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._icmpV6Props = None
            return

        if not isinstance(value, TcpIpIcmpv6Props):
            raise TypeError(
                f"icmpV6Props must be TcpIpIcmpv6Props or None, got {type(value).__name__}"
            )
        self._icmpV6Props = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIcmpV4Props(self) -> TcpIpIcmpv4Props:
        """
        AUTOSAR-compliant getter for icmpV4Props.

        Returns:
            The icmpV4Props value

        Note:
            Delegates to icmp_v4_props property (CODING_RULE_V2_00017)
        """
        return self.icmp_v4_props  # Delegates to property

    def setIcmpV4Props(self, value: TcpIpIcmpv4Props) -> EthTcpIpIcmpProps:
        """
        AUTOSAR-compliant setter for icmpV4Props with method chaining.

        Args:
            value: The icmpV4Props to set

        Returns:
            self for method chaining

        Note:
            Delegates to icmp_v4_props property setter (gets validation automatically)
        """
        self.icmp_v4_props = value  # Delegates to property setter
        return self

    def getIcmpV6Props(self) -> TcpIpIcmpv6Props:
        """
        AUTOSAR-compliant getter for icmpV6Props.

        Returns:
            The icmpV6Props value

        Note:
            Delegates to icmp_v6_props property (CODING_RULE_V2_00017)
        """
        return self.icmp_v6_props  # Delegates to property

    def setIcmpV6Props(self, value: TcpIpIcmpv6Props) -> EthTcpIpIcmpProps:
        """
        AUTOSAR-compliant setter for icmpV6Props with method chaining.

        Args:
            value: The icmpV6Props to set

        Returns:
            self for method chaining

        Note:
            Delegates to icmp_v6_props property setter (gets validation automatically)
        """
        self.icmp_v6_props = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_icmp_v4_props(self, value: Optional[TcpIpIcmpv4Props]) -> EthTcpIpIcmpProps:
        """
        Set icmpV4Props and return self for chaining.

        Args:
            value: The icmpV4Props to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_icmp_v4_props("value")
        """
        self.icmp_v4_props = value  # Use property setter (gets validation)
        return self

    def with_icmp_v6_props(self, value: Optional[TcpIpIcmpv6Props]) -> EthTcpIpIcmpProps:
        """
        Set icmpV6Props and return self for chaining.

        Args:
            value: The icmpV6Props to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_icmp_v6_props("value")
        """
        self.icmp_v6_props = value  # Use property setter (gets validation)
        return self



class TcpIpIcmpv4Props(ARObject):
    """
    This meta-class specifies the configuration options for ICMPv4 (Internet
    Control Message Protocol).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TcpIpIcmpv4Props

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 156, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute enables or disables transmission of ICMP reply message in case
        # of a ICMP echo reception.
        self._tcpIpIcmp: Optional[Boolean] = None

    @property
    def tcp_ip_icmp(self) -> Optional[Boolean]:
        """Get tcpIpIcmp (Pythonic accessor)."""
        return self._tcpIpIcmp

    @tcp_ip_icmp.setter
    def tcp_ip_icmp(self, value: Optional[Boolean]) -> None:
        """
        Set tcpIpIcmp with validation.

        Args:
            value: The tcpIpIcmp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIcmp = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"tcpIpIcmp must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._tcpIpIcmp = value
                # used.
        # It specifies the default of outgoing ICMP packets.
        self._tcpIpIcmpV4Ttl: Optional[PositiveInteger] = None

    @property
    def tcp_ip_icmp_v4_ttl(self) -> Optional[PositiveInteger]:
        """Get tcpIpIcmpV4Ttl (Pythonic accessor)."""
        return self._tcpIpIcmpV4Ttl

    @tcp_ip_icmp_v4_ttl.setter
    def tcp_ip_icmp_v4_ttl(self, value: Optional[PositiveInteger]) -> None:
        """
        Set tcpIpIcmpV4Ttl with validation.

        Args:
            value: The tcpIpIcmpV4Ttl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIcmpV4Ttl = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tcpIpIcmpV4Ttl must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tcpIpIcmpV4Ttl = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpIcmp(self) -> Boolean:
        """
        AUTOSAR-compliant getter for tcpIpIcmp.

        Returns:
            The tcpIpIcmp value

        Note:
            Delegates to tcp_ip_icmp property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_icmp  # Delegates to property

    def setTcpIpIcmp(self, value: Boolean) -> TcpIpIcmpv4Props:
        """
        AUTOSAR-compliant setter for tcpIpIcmp with method chaining.

        Args:
            value: The tcpIpIcmp to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_icmp property setter (gets validation automatically)
        """
        self.tcp_ip_icmp = value  # Delegates to property setter
        return self

    def getTcpIpIcmpV4Ttl(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for tcpIpIcmpV4Ttl.

        Returns:
            The tcpIpIcmpV4Ttl value

        Note:
            Delegates to tcp_ip_icmp_v4_ttl property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_icmp_v4_ttl  # Delegates to property

    def setTcpIpIcmpV4Ttl(self, value: PositiveInteger) -> TcpIpIcmpv4Props:
        """
        AUTOSAR-compliant setter for tcpIpIcmpV4Ttl with method chaining.

        Args:
            value: The tcpIpIcmpV4Ttl to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_icmp_v4_ttl property setter (gets validation automatically)
        """
        self.tcp_ip_icmp_v4_ttl = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_icmp(self, value: Optional[Boolean]) -> TcpIpIcmpv4Props:
        """
        Set tcpIpIcmp and return self for chaining.

        Args:
            value: The tcpIpIcmp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_icmp("value")
        """
        self.tcp_ip_icmp = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_icmp_v4_ttl(self, value: Optional[PositiveInteger]) -> TcpIpIcmpv4Props:
        """
        Set tcpIpIcmpV4Ttl and return self for chaining.

        Args:
            value: The tcpIpIcmpV4Ttl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_icmp_v4_ttl("value")
        """
        self.tcp_ip_icmp_v4_ttl = value  # Use property setter (gets validation)
        return self



class TcpIpIcmpv6Props(ARObject):
    """
    This meta-class specifies the configuration options for ICMPv6 (Internet
    Control Message Protocol).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TcpIpIcmpv6Props

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 156, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If enabled an ICMPv6 parameter problem message will sent if a received packet
        # has been dropped due to options or headers that are found in the packet.
        self._tcpIpIcmp: Optional[Boolean] = None

    @property
    def tcp_ip_icmp(self) -> Optional[Boolean]:
        """Get tcpIpIcmp (Pythonic accessor)."""
        return self._tcpIpIcmp

    @tcp_ip_icmp.setter
    def tcp_ip_icmp(self, value: Optional[Boolean]) -> None:
        """
        Set tcpIpIcmp with validation.

        Args:
            value: The tcpIpIcmp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIcmp = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"tcpIpIcmp must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._tcpIpIcmp = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpIcmp(self) -> Boolean:
        """
        AUTOSAR-compliant getter for tcpIpIcmp.

        Returns:
            The tcpIpIcmp value

        Note:
            Delegates to tcp_ip_icmp property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_icmp  # Delegates to property

    def setTcpIpIcmp(self, value: Boolean) -> TcpIpIcmpv6Props:
        """
        AUTOSAR-compliant setter for tcpIpIcmp with method chaining.

        Args:
            value: The tcpIpIcmp to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_icmp property setter (gets validation automatically)
        """
        self.tcp_ip_icmp = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_icmp(self, value: Optional[Boolean]) -> TcpIpIcmpv6Props:
        """
        Set tcpIpIcmp and return self for chaining.

        Args:
            value: The tcpIpIcmp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_icmp("value")
        """
        self.tcp_ip_icmp = value  # Use property setter (gets validation)
        return self



class EthernetWakeupSleepOnDatalineConfig(Identifiable):
    """
    EthernetWakeupSleepOnDatalineConfigSet is the main element that aggregates
    different config set regarding the wakeup and sleep on data line. An
    EthernetWakeupSleepOnDatalineConfigSet could aggregate multiple different
    configurations regarding the wakeup and sleep on dataline
    (EthernetWakeupSleepOnDatalineConfig).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthernetWakeupSleepOnDatalineConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 158, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Delay in seconds to perform a sleep request if the hardware (PHY) detect a
                # pending wake-up.
        # This to avoid the race condition, if a sleep was a wake-up of a neighboring
                # PHY was a local wake-up connection (e.
        # g.
        # I/O pin).
        self._sleepMode: Optional[TimeValue] = None

    @property
    def sleep_mode(self) -> Optional[TimeValue]:
        """Get sleepMode (Pythonic accessor)."""
        return self._sleepMode

    @sleep_mode.setter
    def sleep_mode(self, value: Optional[TimeValue]) -> None:
        """
        Set sleepMode with validation.

        Args:
            value: The sleepMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sleepMode = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"sleepMode must be TimeValue or None, got {type(value).__name__}"
            )
        self._sleepMode = value
        # This used to retry a synchronized shutdown of the Ethernet hardware (PHY) of
                # the link partner.
        self._sleepRepetition: Optional[TimeValue] = None

    @property
    def sleep_repetition(self) -> Optional[TimeValue]:
        """Get sleepRepetition (Pythonic accessor)."""
        return self._sleepRepetition

    @sleep_repetition.setter
    def sleep_repetition(self, value: Optional[TimeValue]) -> None:
        """
        Set sleepRepetition with validation.

        Args:
            value: The sleepRepetition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sleepRepetition = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"sleepRepetition must be TimeValue or None, got {type(value).__name__}"
            )
        self._sleepRepetition = value
        # If a sleep is by the linked communication partner, the sleep is until the
                # count of repetitions exceed.
        # If count of the Ethernet hardware (PHY) transit without acknowledgement of
                # the connected link.
        self._sleep: Optional[PositiveInteger] = None

    @property
    def sleep(self) -> Optional[PositiveInteger]:
        """Get sleep (Pythonic accessor)."""
        return self._sleep

    @sleep.setter
    def sleep(self, value: Optional[PositiveInteger]) -> None:
        """
        Set sleep with validation.

        Args:
            value: The sleep to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sleep = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"sleep must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._sleep = value
        # g.
        # 100BASE-T1).
        # If disabled, then a is not forwarded to the physical dataline.
        self._wakeupForward: Optional[Boolean] = None

    @property
    def wakeup_forward(self) -> Optional[Boolean]:
        """Get wakeupForward (Pythonic accessor)."""
        return self._wakeupForward

    @wakeup_forward.setter
    def wakeup_forward(self, value: Optional[Boolean]) -> None:
        """
        Set wakeupForward with validation.

        Args:
            value: The wakeupForward to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeupForward = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"wakeupForward must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._wakeupForward = value
        # g.
        # I/O pin) shall be detected by the Ethernet If disabled, Ethernet hardware is
                # not a local wake-up.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._wakeupLocal: Optional[Boolean] = None

    @property
    def wakeup_local(self) -> Optional[Boolean]:
        """Get wakeupLocal (Pythonic accessor)."""
        return self._wakeupLocal

    @wakeup_local.setter
    def wakeup_local(self, value: Optional[Boolean]) -> None:
        """
        Set wakeupLocal with validation.

        Args:
            value: The wakeupLocal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeupLocal = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"wakeupLocal must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._wakeupLocal = value
        # g.
        # 100BASE-T1) shall be detected by hardware (PHY).
        # If disabled, Ethernet not reaction on a remote wake-up.
        self._wakeupRemote: Optional[Boolean] = None

    @property
    def wakeup_remote(self) -> Optional[Boolean]:
        """Get wakeupRemote (Pythonic accessor)."""
        return self._wakeupRemote

    @wakeup_remote.setter
    def wakeup_remote(self, value: Optional[Boolean]) -> None:
        """
        Set wakeupRemote with validation.

        Args:
            value: The wakeupRemote to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeupRemote = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"wakeupRemote must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._wakeupRemote = value
        # This is used to the reliability in the network, such that an ECU initiates
                # the wake-up does repeat the wake-up and the probability that affected ECUs
                # receive the.
        self._wakeup: Optional[PositiveInteger] = None

    @property
    def wakeup(self) -> Optional[PositiveInteger]:
        """Get wakeup (Pythonic accessor)."""
        return self._wakeup

    @wakeup.setter
    def wakeup(self, value: Optional[PositiveInteger]) -> None:
        """
        Set wakeup with validation.

        Args:
            value: The wakeup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeup = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"wakeup must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._wakeup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSleepMode(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for sleepMode.

        Returns:
            The sleepMode value

        Note:
            Delegates to sleep_mode property (CODING_RULE_V2_00017)
        """
        return self.sleep_mode  # Delegates to property

    def setSleepMode(self, value: TimeValue) -> EthernetWakeupSleepOnDatalineConfig:
        """
        AUTOSAR-compliant setter for sleepMode with method chaining.

        Args:
            value: The sleepMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to sleep_mode property setter (gets validation automatically)
        """
        self.sleep_mode = value  # Delegates to property setter
        return self

    def getSleepRepetition(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for sleepRepetition.

        Returns:
            The sleepRepetition value

        Note:
            Delegates to sleep_repetition property (CODING_RULE_V2_00017)
        """
        return self.sleep_repetition  # Delegates to property

    def setSleepRepetition(self, value: TimeValue) -> EthernetWakeupSleepOnDatalineConfig:
        """
        AUTOSAR-compliant setter for sleepRepetition with method chaining.

        Args:
            value: The sleepRepetition to set

        Returns:
            self for method chaining

        Note:
            Delegates to sleep_repetition property setter (gets validation automatically)
        """
        self.sleep_repetition = value  # Delegates to property setter
        return self

    def getSleep(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for sleep.

        Returns:
            The sleep value

        Note:
            Delegates to sleep property (CODING_RULE_V2_00017)
        """
        return self.sleep  # Delegates to property

    def setSleep(self, value: PositiveInteger) -> EthernetWakeupSleepOnDatalineConfig:
        """
        AUTOSAR-compliant setter for sleep with method chaining.

        Args:
            value: The sleep to set

        Returns:
            self for method chaining

        Note:
            Delegates to sleep property setter (gets validation automatically)
        """
        self.sleep = value  # Delegates to property setter
        return self

    def getWakeupForward(self) -> Boolean:
        """
        AUTOSAR-compliant getter for wakeupForward.

        Returns:
            The wakeupForward value

        Note:
            Delegates to wakeup_forward property (CODING_RULE_V2_00017)
        """
        return self.wakeup_forward  # Delegates to property

    def setWakeupForward(self, value: Boolean) -> EthernetWakeupSleepOnDatalineConfig:
        """
        AUTOSAR-compliant setter for wakeupForward with method chaining.

        Args:
            value: The wakeupForward to set

        Returns:
            self for method chaining

        Note:
            Delegates to wakeup_forward property setter (gets validation automatically)
        """
        self.wakeup_forward = value  # Delegates to property setter
        return self

    def getWakeupLocal(self) -> Boolean:
        """
        AUTOSAR-compliant getter for wakeupLocal.

        Returns:
            The wakeupLocal value

        Note:
            Delegates to wakeup_local property (CODING_RULE_V2_00017)
        """
        return self.wakeup_local  # Delegates to property

    def setWakeupLocal(self, value: Boolean) -> EthernetWakeupSleepOnDatalineConfig:
        """
        AUTOSAR-compliant setter for wakeupLocal with method chaining.

        Args:
            value: The wakeupLocal to set

        Returns:
            self for method chaining

        Note:
            Delegates to wakeup_local property setter (gets validation automatically)
        """
        self.wakeup_local = value  # Delegates to property setter
        return self

    def getWakeupRemote(self) -> Boolean:
        """
        AUTOSAR-compliant getter for wakeupRemote.

        Returns:
            The wakeupRemote value

        Note:
            Delegates to wakeup_remote property (CODING_RULE_V2_00017)
        """
        return self.wakeup_remote  # Delegates to property

    def setWakeupRemote(self, value: Boolean) -> EthernetWakeupSleepOnDatalineConfig:
        """
        AUTOSAR-compliant setter for wakeupRemote with method chaining.

        Args:
            value: The wakeupRemote to set

        Returns:
            self for method chaining

        Note:
            Delegates to wakeup_remote property setter (gets validation automatically)
        """
        self.wakeup_remote = value  # Delegates to property setter
        return self

    def getWakeup(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for wakeup.

        Returns:
            The wakeup value

        Note:
            Delegates to wakeup property (CODING_RULE_V2_00017)
        """
        return self.wakeup  # Delegates to property

    def setWakeup(self, value: PositiveInteger) -> EthernetWakeupSleepOnDatalineConfig:
        """
        AUTOSAR-compliant setter for wakeup with method chaining.

        Args:
            value: The wakeup to set

        Returns:
            self for method chaining

        Note:
            Delegates to wakeup property setter (gets validation automatically)
        """
        self.wakeup = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sleep_mode(self, value: Optional[TimeValue]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        Set sleepMode and return self for chaining.

        Args:
            value: The sleepMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sleep_mode("value")
        """
        self.sleep_mode = value  # Use property setter (gets validation)
        return self

    def with_sleep_repetition(self, value: Optional[TimeValue]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        Set sleepRepetition and return self for chaining.

        Args:
            value: The sleepRepetition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sleep_repetition("value")
        """
        self.sleep_repetition = value  # Use property setter (gets validation)
        return self

    def with_sleep(self, value: Optional[PositiveInteger]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        Set sleep and return self for chaining.

        Args:
            value: The sleep to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sleep("value")
        """
        self.sleep = value  # Use property setter (gets validation)
        return self

    def with_wakeup_forward(self, value: Optional[Boolean]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        Set wakeupForward and return self for chaining.

        Args:
            value: The wakeupForward to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup_forward("value")
        """
        self.wakeup_forward = value  # Use property setter (gets validation)
        return self

    def with_wakeup_local(self, value: Optional[Boolean]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        Set wakeupLocal and return self for chaining.

        Args:
            value: The wakeupLocal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup_local("value")
        """
        self.wakeup_local = value  # Use property setter (gets validation)
        return self

    def with_wakeup_remote(self, value: Optional[Boolean]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        Set wakeupRemote and return self for chaining.

        Args:
            value: The wakeupRemote to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup_remote("value")
        """
        self.wakeup_remote = value  # Use property setter (gets validation)
        return self

    def with_wakeup(self, value: Optional[PositiveInteger]) -> EthernetWakeupSleepOnDatalineConfig:
        """
        Set wakeup and return self for chaining.

        Args:
            value: The wakeup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup("value")
        """
        self.wakeup = value  # Use property setter (gets validation)
        return self



class EthernetWakeupSleepOnDatalineConfigSet(FibexElement):
    """
    This meta-class is the main element that aggregates different config set
    regarding the ethernet wakeup and sleep on data line.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthernetWakeupSleepOnDatalineConfigSet

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 159, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The relationship defines a collection of EthernetWakeup SleepOnDatalineConfig
        # configurations which are.
        self._ethernet: List[EthernetWakeupSleep] = []

    @property
    def ethernet(self) -> List[EthernetWakeupSleep]:
        """Get ethernet (Pythonic accessor)."""
        return self._ethernet

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEthernet(self) -> List[EthernetWakeupSleep]:
        """
        AUTOSAR-compliant getter for ethernet.

        Returns:
            The ethernet value

        Note:
            Delegates to ethernet property (CODING_RULE_V2_00017)
        """
        return self.ethernet  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class PlcaProps(ARObject):
    """
    This meta-class allows to configure the PLCA (Physical Layer Collision
    Avoidance) in case 10-BASE-T1S Ethernet is used and PLCA is enabled on the
    CouplingPort (PHY).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::PlcaProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 169, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the node ID when the PLCA mode 10BASE-T1S is used.
        self._plcaLocalNode: Optional[PositiveInteger] = None

    @property
    def plca_local_node(self) -> Optional[PositiveInteger]:
        """Get plcaLocalNode (Pythonic accessor)."""
        return self._plcaLocalNode

    @plca_local_node.setter
    def plca_local_node(self, value: Optional[PositiveInteger]) -> None:
        """
        Set plcaLocalNode with validation.

        Args:
            value: The plcaLocalNode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._plcaLocalNode = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"plcaLocalNode must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._plcaLocalNode = value
        # This configuration can different from one ECU to another within the PLCA For
                # PLCA burst mode to work properly should be set greater than one IPG.
        self._plcaMaxBurst: Optional[PositiveInteger] = None

    @property
    def plca_max_burst(self) -> Optional[PositiveInteger]:
        """Get plcaMaxBurst (Pythonic accessor)."""
        return self._plcaMaxBurst

    @plca_max_burst.setter
    def plca_max_burst(self, value: Optional[PositiveInteger]) -> None:
        """
        Set plcaMaxBurst with validation.

        Args:
            value: The plcaMaxBurst to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._plcaMaxBurst = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"plcaMaxBurst must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._plcaMaxBurst = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPlcaLocalNode(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for plcaLocalNode.

        Returns:
            The plcaLocalNode value

        Note:
            Delegates to plca_local_node property (CODING_RULE_V2_00017)
        """
        return self.plca_local_node  # Delegates to property

    def setPlcaLocalNode(self, value: PositiveInteger) -> PlcaProps:
        """
        AUTOSAR-compliant setter for plcaLocalNode with method chaining.

        Args:
            value: The plcaLocalNode to set

        Returns:
            self for method chaining

        Note:
            Delegates to plca_local_node property setter (gets validation automatically)
        """
        self.plca_local_node = value  # Delegates to property setter
        return self

    def getPlcaMaxBurst(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for plcaMaxBurst.

        Returns:
            The plcaMaxBurst value

        Note:
            Delegates to plca_max_burst property (CODING_RULE_V2_00017)
        """
        return self.plca_max_burst  # Delegates to property

    def setPlcaMaxBurst(self, value: PositiveInteger) -> PlcaProps:
        """
        AUTOSAR-compliant setter for plcaMaxBurst with method chaining.

        Args:
            value: The plcaMaxBurst to set

        Returns:
            self for method chaining

        Note:
            Delegates to plca_max_burst property setter (gets validation automatically)
        """
        self.plca_max_burst = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_plca_local_node(self, value: Optional[PositiveInteger]) -> PlcaProps:
        """
        Set plcaLocalNode and return self for chaining.

        Args:
            value: The plcaLocalNode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_plca_local_node("value")
        """
        self.plca_local_node = value  # Use property setter (gets validation)
        return self

    def with_plca_max_burst(self, value: Optional[PositiveInteger]) -> PlcaProps:
        """
        Set plcaMaxBurst and return self for chaining.

        Args:
            value: The plcaMaxBurst to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_plca_max_burst("value")
        """
        self.plca_max_burst = value  # Use property setter (gets validation)
        return self



class ApplicationEndpoint(Identifiable):
    """
    An application endpoint is the endpoint on an Ecu in terms of application
    addressing (e.g. socket). The application endpoint represents e.g. the
    listen socket in client-server-based communication.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::ApplicationEndpoint

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 457, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Consumed service instances.
        # Tags: atp.
        # Status=obsolete.
        self._consumed: List["ConsumedService"] = []

    @property
    def consumed(self) -> List["ConsumedService"]:
        """Get consumed (Pythonic accessor)."""
        return self._consumed
        # This attribute defines the maximal number of clients the is able to deal with
                # in case of Service Discovery.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._maxNumberOf: Optional[PositiveInteger] = None

    @property
    def max_number_of(self) -> Optional[PositiveInteger]:
        """Get maxNumberOf (Pythonic accessor)."""
        return self._maxNumberOf

    @max_number_of.setter
    def max_number_of(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maxNumberOf with validation.

        Args:
            value: The maxNumberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOf = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxNumberOf must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxNumberOf = value
        self._networkEndpoint: Optional[NetworkEndpoint] = None

    @property
    def network_endpoint(self) -> Optional[NetworkEndpoint]:
        """Get networkEndpoint (Pythonic accessor)."""
        return self._networkEndpoint

    @network_endpoint.setter
    def network_endpoint(self, value: Optional[NetworkEndpoint]) -> None:
        """
        Set networkEndpoint with validation.

        Args:
            value: The networkEndpoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._networkEndpoint = None
            return

        if not isinstance(value, NetworkEndpoint):
            raise TypeError(
                f"networkEndpoint must be NetworkEndpoint or None, got {type(value).__name__}"
            )
        self._networkEndpoint = value
        self._priority: Optional[PositiveInteger] = None

    @property
    def priority(self) -> Optional[PositiveInteger]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional[PositiveInteger]) -> None:
        """
        Set priority with validation.

        Args:
            value: The priority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priority = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._priority = value
        # Tags: atp.
        # Status=obsolete.
        self._providedService: List["ProvidedService"] = []

    @property
    def provided_service(self) -> List["ProvidedService"]:
        """Get providedService (Pythonic accessor)."""
        return self._providedService
        # This reference identifies the applicable TlsCryptoService Mapping that adds
        # the ability for TLS-based encryption enclosing ApplicationEndpoint.
        self._tlsCrypto: Optional[TlsCryptoServiceEnum] = None

    @property
    def tls_crypto(self) -> Optional[TlsCryptoServiceEnum]:
        """Get tlsCrypto (Pythonic accessor)."""
        return self._tlsCrypto

    @tls_crypto.setter
    def tls_crypto(self, value: Optional[TlsCryptoServiceEnum]) -> None:
        """
        Set tlsCrypto with validation.

        Args:
            value: The tlsCrypto to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tlsCrypto = None
            return

        if not isinstance(value, TlsCryptoService):
            raise TypeError(
                f"tlsCrypto must be TlsCryptoService or None, got {type(value).__name__}"
            )
        self._tlsCrypto = value
        self._tpConfigurationConfiguration: Optional[TransportProtocolEnum] = None

    @property
    def tp_configuration_configuration(self) -> Optional[TransportProtocolEnum]:
        """Get tpConfigurationConfiguration (Pythonic accessor)."""
        return self._tpConfigurationConfiguration

    @tp_configuration_configuration.setter
    def tp_configuration_configuration(self, value: Optional[TransportProtocolEnum]) -> None:
        """
        Set tpConfigurationConfiguration with validation.

        Args:
            value: The tpConfigurationConfiguration to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpConfigurationConfiguration = None
            return

        if not isinstance(value, TransportProtocol):
            raise TypeError(
                f"tpConfigurationConfiguration must be TransportProtocol or None, got {type(value).__name__}"
            )
        self._tpConfigurationConfiguration = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConsumed(self) -> List["ConsumedService"]:
        """
        AUTOSAR-compliant getter for consumed.

        Returns:
            The consumed value

        Note:
            Delegates to consumed property (CODING_RULE_V2_00017)
        """
        return self.consumed  # Delegates to property

    def getMaxNumberOf(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maxNumberOf.

        Returns:
            The maxNumberOf value

        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: PositiveInteger) -> ApplicationEndpoint:
        """
        AUTOSAR-compliant setter for maxNumberOf with method chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of property setter (gets validation automatically)
        """
        self.max_number_of = value  # Delegates to property setter
        return self

    def getNetworkEndpoint(self) -> NetworkEndpoint:
        """
        AUTOSAR-compliant getter for networkEndpoint.

        Returns:
            The networkEndpoint value

        Note:
            Delegates to network_endpoint property (CODING_RULE_V2_00017)
        """
        return self.network_endpoint  # Delegates to property

    def setNetworkEndpoint(self, value: NetworkEndpoint) -> ApplicationEndpoint:
        """
        AUTOSAR-compliant setter for networkEndpoint with method chaining.

        Args:
            value: The networkEndpoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to network_endpoint property setter (gets validation automatically)
        """
        self.network_endpoint = value  # Delegates to property setter
        return self

    def getPriority(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: PositiveInteger) -> ApplicationEndpoint:
        """
        AUTOSAR-compliant setter for priority with method chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    def getProvidedService(self) -> List["ProvidedService"]:
        """
        AUTOSAR-compliant getter for providedService.

        Returns:
            The providedService value

        Note:
            Delegates to provided_service property (CODING_RULE_V2_00017)
        """
        return self.provided_service  # Delegates to property

    def getTlsCrypto(self) -> TlsCryptoServiceEnum:
        """
        AUTOSAR-compliant getter for tlsCrypto.

        Returns:
            The tlsCrypto value

        Note:
            Delegates to tls_crypto property (CODING_RULE_V2_00017)
        """
        return self.tls_crypto  # Delegates to property

    def setTlsCrypto(self, value: TlsCryptoServiceEnum) -> ApplicationEndpoint:
        """
        AUTOSAR-compliant setter for tlsCrypto with method chaining.

        Args:
            value: The tlsCrypto to set

        Returns:
            self for method chaining

        Note:
            Delegates to tls_crypto property setter (gets validation automatically)
        """
        self.tls_crypto = value  # Delegates to property setter
        return self

    def getTpConfigurationConfiguration(self) -> TransportProtocolEnum:
        """
        AUTOSAR-compliant getter for tpConfigurationConfiguration.

        Returns:
            The tpConfigurationConfiguration value

        Note:
            Delegates to tp_configuration_configuration property (CODING_RULE_V2_00017)
        """
        return self.tp_configuration_configuration  # Delegates to property

    def setTpConfigurationConfiguration(self, value: TransportProtocolEnum) -> ApplicationEndpoint:
        """
        AUTOSAR-compliant setter for tpConfigurationConfiguration with method chaining.

        Args:
            value: The tpConfigurationConfiguration to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_configuration_configuration property setter (gets validation automatically)
        """
        self.tp_configuration_configuration = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_number_of(self, value: Optional[PositiveInteger]) -> ApplicationEndpoint:
        """
        Set maxNumberOf and return self for chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of("value")
        """
        self.max_number_of = value  # Use property setter (gets validation)
        return self

    def with_network_endpoint(self, value: Optional[NetworkEndpoint]) -> ApplicationEndpoint:
        """
        Set networkEndpoint and return self for chaining.

        Args:
            value: The networkEndpoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network_endpoint("value")
        """
        self.network_endpoint = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> ApplicationEndpoint:
        """
        Set priority and return self for chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self

    def with_tls_crypto(self, value: Optional[TlsCryptoServiceEnum]) -> ApplicationEndpoint:
        """
        Set tlsCrypto and return self for chaining.

        Args:
            value: The tlsCrypto to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tls_crypto("value")
        """
        self.tls_crypto = value  # Use property setter (gets validation)
        return self

    def with_tp_configuration_configuration(self, value: Optional[TransportProtocolEnum]) -> ApplicationEndpoint:
        """
        Set tpConfigurationConfiguration and return self for chaining.

        Args:
            value: The tpConfigurationConfiguration to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_configuration_configuration("value")
        """
        self.tp_configuration_configuration = value  # Use property setter (gets validation)
        return self



class TransportProtocolConfiguration(ARObject, ABC):
    """
    Transport Protocol configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TransportProtocolConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 459, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TransportProtocolConfiguration:
            raise TypeError("TransportProtocolConfiguration is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TpPort(ARObject):
    """
    Dynamic or direct assignment of a PortNumber.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TpPort

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 461, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Indicates whether the source port is dynamically.
        self._dynamically: Optional[Boolean] = None

    @property
    def dynamically(self) -> Optional[Boolean]:
        """Get dynamically (Pythonic accessor)."""
        return self._dynamically

    @dynamically.setter
    def dynamically(self, value: Optional[Boolean]) -> None:
        """
        Set dynamically with validation.

        Args:
            value: The dynamically to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamically = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"dynamically must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._dynamically = value
        self._portNumber: Optional[PositiveInteger] = None

    @property
    def port_number(self) -> Optional[PositiveInteger]:
        """Get portNumber (Pythonic accessor)."""
        return self._portNumber

    @port_number.setter
    def port_number(self, value: Optional[PositiveInteger]) -> None:
        """
        Set portNumber with validation.

        Args:
            value: The portNumber to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._portNumber = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"portNumber must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._portNumber = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDynamically(self) -> Boolean:
        """
        AUTOSAR-compliant getter for dynamically.

        Returns:
            The dynamically value

        Note:
            Delegates to dynamically property (CODING_RULE_V2_00017)
        """
        return self.dynamically  # Delegates to property

    def setDynamically(self, value: Boolean) -> TpPort:
        """
        AUTOSAR-compliant setter for dynamically with method chaining.

        Args:
            value: The dynamically to set

        Returns:
            self for method chaining

        Note:
            Delegates to dynamically property setter (gets validation automatically)
        """
        self.dynamically = value  # Delegates to property setter
        return self

    def getPortNumber(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for portNumber.

        Returns:
            The portNumber value

        Note:
            Delegates to port_number property (CODING_RULE_V2_00017)
        """
        return self.port_number  # Delegates to property

    def setPortNumber(self, value: PositiveInteger) -> TpPort:
        """
        AUTOSAR-compliant setter for portNumber with method chaining.

        Args:
            value: The portNumber to set

        Returns:
            self for method chaining

        Note:
            Delegates to port_number property setter (gets validation automatically)
        """
        self.port_number = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dynamically(self, value: Optional[Boolean]) -> TpPort:
        """
        Set dynamically and return self for chaining.

        Args:
            value: The dynamically to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dynamically("value")
        """
        self.dynamically = value  # Use property setter (gets validation)
        return self

    def with_port_number(self, value: Optional[PositiveInteger]) -> TpPort:
        """
        Set portNumber and return self for chaining.

        Args:
            value: The portNumber to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_number("value")
        """
        self.port_number = value  # Use property setter (gets validation)
        return self



class NetworkEndpoint(Identifiable):
    """
    The network endpoint defines the network addressing (e.g. IP-Address or MAC
    multicast address).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::NetworkEndpoint

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 463, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the fully qualified domain name (FQDN) e.
        # g.
        self._fullyQualified: Optional[String] = None

    @property
    def fully_qualified(self) -> Optional[String]:
        """Get fullyQualified (Pythonic accessor)."""
        return self._fullyQualified

    @fully_qualified.setter
    def fully_qualified(self, value: Optional[String]) -> None:
        """
        Set fullyQualified with validation.

        Args:
            value: The fullyQualified to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fullyQualified = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"fullyQualified must be String or str or None, got {type(value).__name__}"
            )
        self._fullyQualified = value
        self._infrastructure: Optional[InfrastructureServices] = None

    @property
    def infrastructure(self) -> Optional[InfrastructureServices]:
        """Get infrastructure (Pythonic accessor)."""
        return self._infrastructure

    @infrastructure.setter
    def infrastructure(self, value: Optional[InfrastructureServices]) -> None:
        """
        Set infrastructure with validation.

        Args:
            value: The infrastructure to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._infrastructure = None
            return

        if not isinstance(value, InfrastructureServices):
            raise TypeError(
                f"infrastructure must be InfrastructureServices or None, got {type(value).__name__}"
            )
        self._infrastructure = value
        self._ipSecConfig: Optional[IPSecConfiguration] = None

    @property
    def ip_sec_config(self) -> Optional[IPSecConfiguration]:
        """Get ipSecConfig (Pythonic accessor)."""
        return self._ipSecConfig

    @ip_sec_config.setter
    def ip_sec_config(self, value: Optional[IPSecConfiguration]) -> None:
        """
        Set ipSecConfig with validation.

        Args:
            value: The ipSecConfig to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipSecConfig = None
            return

        if not isinstance(value, IPSecConfig):
            raise TypeError(
                f"ipSecConfig must be IPSecConfig or None, got {type(value).__name__}"
            )
        self._ipSecConfig = value
        # Tags: xml.
        # name Address Plural=NETWORK-ENDPOINT-ADDRESSES.
        self._network: List[NetworkEndpoint] = []

    @property
    def network(self) -> List[NetworkEndpoint]:
        """Get network (Pythonic accessor)."""
        return self._network
        # Defines the frame priority where values from 0 (best 7 (highest) are allowed.
        self._priority: Optional[PositiveInteger] = None

    @property
    def priority(self) -> Optional[PositiveInteger]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional[PositiveInteger]) -> None:
        """
        Set priority with validation.

        Args:
            value: The priority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priority = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._priority = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFullyQualified(self) -> String:
        """
        AUTOSAR-compliant getter for fullyQualified.

        Returns:
            The fullyQualified value

        Note:
            Delegates to fully_qualified property (CODING_RULE_V2_00017)
        """
        return self.fully_qualified  # Delegates to property

    def setFullyQualified(self, value: String) -> NetworkEndpoint:
        """
        AUTOSAR-compliant setter for fullyQualified with method chaining.

        Args:
            value: The fullyQualified to set

        Returns:
            self for method chaining

        Note:
            Delegates to fully_qualified property setter (gets validation automatically)
        """
        self.fully_qualified = value  # Delegates to property setter
        return self

    def getInfrastructure(self) -> InfrastructureServices:
        """
        AUTOSAR-compliant getter for infrastructure.

        Returns:
            The infrastructure value

        Note:
            Delegates to infrastructure property (CODING_RULE_V2_00017)
        """
        return self.infrastructure  # Delegates to property

    def setInfrastructure(self, value: InfrastructureServices) -> NetworkEndpoint:
        """
        AUTOSAR-compliant setter for infrastructure with method chaining.

        Args:
            value: The infrastructure to set

        Returns:
            self for method chaining

        Note:
            Delegates to infrastructure property setter (gets validation automatically)
        """
        self.infrastructure = value  # Delegates to property setter
        return self

    def getIpSecConfig(self) -> IPSecConfiguration:
        """
        AUTOSAR-compliant getter for ipSecConfig.

        Returns:
            The ipSecConfig value

        Note:
            Delegates to ip_sec_config property (CODING_RULE_V2_00017)
        """
        return self.ip_sec_config  # Delegates to property

    def setIpSecConfig(self, value: IPSecConfiguration) -> NetworkEndpoint:
        """
        AUTOSAR-compliant setter for ipSecConfig with method chaining.

        Args:
            value: The ipSecConfig to set

        Returns:
            self for method chaining

        Note:
            Delegates to ip_sec_config property setter (gets validation automatically)
        """
        self.ip_sec_config = value  # Delegates to property setter
        return self

    def getNetwork(self) -> List[NetworkEndpoint]:
        """
        AUTOSAR-compliant getter for network.

        Returns:
            The network value

        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def getPriority(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: PositiveInteger) -> NetworkEndpoint:
        """
        AUTOSAR-compliant setter for priority with method chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_fully_qualified(self, value: Optional[String]) -> NetworkEndpoint:
        """
        Set fullyQualified and return self for chaining.

        Args:
            value: The fullyQualified to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fully_qualified("value")
        """
        self.fully_qualified = value  # Use property setter (gets validation)
        return self

    def with_infrastructure(self, value: Optional[InfrastructureServices]) -> NetworkEndpoint:
        """
        Set infrastructure and return self for chaining.

        Args:
            value: The infrastructure to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_infrastructure("value")
        """
        self.infrastructure = value  # Use property setter (gets validation)
        return self

    def with_ip_sec_config(self, value: Optional[IPSecConfiguration]) -> NetworkEndpoint:
        """
        Set ipSecConfig and return self for chaining.

        Args:
            value: The ipSecConfig to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ip_sec_config("value")
        """
        self.ip_sec_config = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> NetworkEndpoint:
        """
        Set priority and return self for chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self



class NetworkEndpointAddress(ARObject, ABC):
    """
    To build a valid network endpoint address there has to be either one MAC
    multicast group reference or an ipv4 configuration or an ipv6 configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::NetworkEndpointAddress

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 464, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is NetworkEndpointAddress:
            raise TypeError("NetworkEndpointAddress is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class InfrastructureServices(ARObject):
    """
    Defines the network infrastructure services provided or consumed.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::InfrastructureServices

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 469, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether a infrastructure service that runs on the is a DoIP-Entity.
        self._doIpEntity: Optional[DoIpEntity] = None

    @property
    def do_ip_entity(self) -> Optional[DoIpEntity]:
        """Get doIpEntity (Pythonic accessor)."""
        return self._doIpEntity

    @do_ip_entity.setter
    def do_ip_entity(self, value: Optional[DoIpEntity]) -> None:
        """
        Set doIpEntity with validation.

        Args:
            value: The doIpEntity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._doIpEntity = None
            return

        if not isinstance(value, DoIpEntity):
            raise TypeError(
                f"doIpEntity must be DoIpEntity or None, got {type(value).__name__}"
            )
        self._doIpEntity = value
        self._time: Optional[TimeSynchronization] = None

    @property
    def time(self) -> Optional[TimeSynchronization]:
        """Get time (Pythonic accessor)."""
        return self._time

    @time.setter
    def time(self, value: Optional[TimeSynchronization]) -> None:
        """
        Set time with validation.

        Args:
            value: The time to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._time = None
            return

        if not isinstance(value, TimeSynchronization):
            raise TypeError(
                f"time must be TimeSynchronization or None, got {type(value).__name__}"
            )
        self._time = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDoIpEntity(self) -> DoIpEntity:
        """
        AUTOSAR-compliant getter for doIpEntity.

        Returns:
            The doIpEntity value

        Note:
            Delegates to do_ip_entity property (CODING_RULE_V2_00017)
        """
        return self.do_ip_entity  # Delegates to property

    def setDoIpEntity(self, value: DoIpEntity) -> InfrastructureServices:
        """
        AUTOSAR-compliant setter for doIpEntity with method chaining.

        Args:
            value: The doIpEntity to set

        Returns:
            self for method chaining

        Note:
            Delegates to do_ip_entity property setter (gets validation automatically)
        """
        self.do_ip_entity = value  # Delegates to property setter
        return self

    def getTime(self) -> TimeSynchronization:
        """
        AUTOSAR-compliant getter for time.

        Returns:
            The time value

        Note:
            Delegates to time property (CODING_RULE_V2_00017)
        """
        return self.time  # Delegates to property

    def setTime(self, value: TimeSynchronization) -> InfrastructureServices:
        """
        AUTOSAR-compliant setter for time with method chaining.

        Args:
            value: The time to set

        Returns:
            self for method chaining

        Note:
            Delegates to time property setter (gets validation automatically)
        """
        self.time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_do_ip_entity(self, value: Optional[DoIpEntity]) -> InfrastructureServices:
        """
        Set doIpEntity and return self for chaining.

        Args:
            value: The doIpEntity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_do_ip_entity("value")
        """
        self.do_ip_entity = value  # Use property setter (gets validation)
        return self

    def with_time(self, value: Optional[TimeSynchronization]) -> InfrastructureServices:
        """
        Set time and return self for chaining.

        Args:
            value: The time to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time("value")
        """
        self.time = value  # Use property setter (gets validation)
        return self



class TimeSynchronization(ARObject):
    """
    Defines the servers / clients in a time synchronised network.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TimeSynchronization

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 469, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Configuration of the time synchronisation client.
        self._timeSyncClientConfiguration: Optional[TimeSyncClientConfiguration] = None

    @property
    def time_sync_client_configuration(self) -> Optional[TimeSyncClientConfiguration]:
        """Get timeSyncClientConfiguration (Pythonic accessor)."""
        return self._timeSyncClientConfiguration

    @time_sync_client_configuration.setter
    def time_sync_client_configuration(self, value: Optional[TimeSyncClientConfiguration]) -> None:
        """
        Set timeSyncClientConfiguration with validation.

        Args:
            value: The timeSyncClientConfiguration to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSyncClientConfiguration = None
            return

        if not isinstance(value, TimeSyncClient):
            raise TypeError(
                f"timeSyncClientConfiguration must be TimeSyncClient or None, got {type(value).__name__}"
            )
        self._timeSyncClientConfiguration = value
        self._timeSyncServerConfiguration: Optional[TimeSyncServerConfiguration] = None

    @property
    def time_sync_server_configuration(self) -> Optional[TimeSyncServerConfiguration]:
        """Get timeSyncServerConfiguration (Pythonic accessor)."""
        return self._timeSyncServerConfiguration

    @time_sync_server_configuration.setter
    def time_sync_server_configuration(self, value: Optional[TimeSyncServerConfiguration]) -> None:
        """
        Set timeSyncServerConfiguration with validation.

        Args:
            value: The timeSyncServerConfiguration to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSyncServerConfiguration = None
            return

        if not isinstance(value, TimeSyncServer):
            raise TypeError(
                f"timeSyncServerConfiguration must be TimeSyncServer or None, got {type(value).__name__}"
            )
        self._timeSyncServerConfiguration = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimeSyncClientConfiguration(self) -> TimeSyncClientConfiguration:
        """
        AUTOSAR-compliant getter for timeSyncClientConfiguration.

        Returns:
            The timeSyncClientConfiguration value

        Note:
            Delegates to time_sync_client_configuration property (CODING_RULE_V2_00017)
        """
        return self.time_sync_client_configuration  # Delegates to property

    def setTimeSyncClientConfiguration(self, value: TimeSyncClientConfiguration) -> TimeSynchronization:
        """
        AUTOSAR-compliant setter for timeSyncClientConfiguration with method chaining.

        Args:
            value: The timeSyncClientConfiguration to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_sync_client_configuration property setter (gets validation automatically)
        """
        self.time_sync_client_configuration = value  # Delegates to property setter
        return self

    def getTimeSyncServerConfiguration(self) -> TimeSyncServerConfiguration:
        """
        AUTOSAR-compliant getter for timeSyncServerConfiguration.

        Returns:
            The timeSyncServerConfiguration value

        Note:
            Delegates to time_sync_server_configuration property (CODING_RULE_V2_00017)
        """
        return self.time_sync_server_configuration  # Delegates to property

    def setTimeSyncServerConfiguration(self, value: TimeSyncServerConfiguration) -> TimeSynchronization:
        """
        AUTOSAR-compliant setter for timeSyncServerConfiguration with method chaining.

        Args:
            value: The timeSyncServerConfiguration to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_sync_server_configuration property setter (gets validation automatically)
        """
        self.time_sync_server_configuration = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_time_sync_client_configuration(self, value: Optional[TimeSyncClientConfiguration]) -> TimeSynchronization:
        """
        Set timeSyncClientConfiguration and return self for chaining.

        Args:
            value: The timeSyncClientConfiguration to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_sync_client_configuration("value")
        """
        self.time_sync_client_configuration = value  # Use property setter (gets validation)
        return self

    def with_time_sync_server_configuration(self, value: Optional[TimeSyncServerConfiguration]) -> TimeSynchronization:
        """
        Set timeSyncServerConfiguration and return self for chaining.

        Args:
            value: The timeSyncServerConfiguration to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_sync_server_configuration("value")
        """
        self.time_sync_server_configuration = value  # Use property setter (gets validation)
        return self



class TimeSyncClientConfiguration(ARObject):
    """
    Defines the configuration of the time synchronisation client.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TimeSyncClientConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 469, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines a list of ordered NetworkEndpoints.
        # xml.
        # namePlural=ORDERED-MASTER-LIST.
        self._orderedMaster: List[OrderedMaster] = []

    @property
    def ordered_master(self) -> List[OrderedMaster]:
        """Get orderedMaster (Pythonic accessor)."""
        return self._orderedMaster
        # Defines the time synchronisation technology used.
        self._timeSync: Optional[TimeSyncTechnologyEnum] = None

    @property
    def time_sync(self) -> Optional[TimeSyncTechnologyEnum]:
        """Get timeSync (Pythonic accessor)."""
        return self._timeSync

    @time_sync.setter
    def time_sync(self, value: Optional[TimeSyncTechnologyEnum]) -> None:
        """
        Set timeSync with validation.

        Args:
            value: The timeSync to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSync = None
            return

        if not isinstance(value, TimeSyncTechnology):
            raise TypeError(
                f"timeSync must be TimeSyncTechnology or None, got {type(value).__name__}"
            )
        self._timeSync = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOrderedMaster(self) -> List[OrderedMaster]:
        """
        AUTOSAR-compliant getter for orderedMaster.

        Returns:
            The orderedMaster value

        Note:
            Delegates to ordered_master property (CODING_RULE_V2_00017)
        """
        return self.ordered_master  # Delegates to property

    def getTimeSync(self) -> TimeSyncTechnologyEnum:
        """
        AUTOSAR-compliant getter for timeSync.

        Returns:
            The timeSync value

        Note:
            Delegates to time_sync property (CODING_RULE_V2_00017)
        """
        return self.time_sync  # Delegates to property

    def setTimeSync(self, value: TimeSyncTechnologyEnum) -> TimeSyncClientConfiguration:
        """
        AUTOSAR-compliant setter for timeSync with method chaining.

        Args:
            value: The timeSync to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_sync property setter (gets validation automatically)
        """
        self.time_sync = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_time_sync(self, value: Optional[TimeSyncTechnologyEnum]) -> TimeSyncClientConfiguration:
        """
        Set timeSync and return self for chaining.

        Args:
            value: The timeSync to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_sync("value")
        """
        self.time_sync = value  # Use property setter (gets validation)
        return self



class TimeSyncServerConfiguration(Referrable):
    """
    Defines the configuration of the time synchronisation server.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TimeSyncServerConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 470, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Server Priority.
        self._priority: Optional[PositiveInteger] = None

    @property
    def priority(self) -> Optional[PositiveInteger]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional[PositiveInteger]) -> None:
        """
        Set priority with validation.

        Args:
            value: The priority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priority = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._priority = value
        self._syncInterval: Optional[TimeValue] = None

    @property
    def sync_interval(self) -> Optional[TimeValue]:
        """Get syncInterval (Pythonic accessor)."""
        return self._syncInterval

    @sync_interval.setter
    def sync_interval(self, value: Optional[TimeValue]) -> None:
        """
        Set syncInterval with validation.

        Args:
            value: The syncInterval to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncInterval = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"syncInterval must be TimeValue or None, got {type(value).__name__}"
            )
        self._syncInterval = value
        self._timeSyncServerIdentifier: Optional[String] = None

    @property
    def time_sync_server_identifier(self) -> Optional[String]:
        """Get timeSyncServerIdentifier (Pythonic accessor)."""
        return self._timeSyncServerIdentifier

    @time_sync_server_identifier.setter
    def time_sync_server_identifier(self, value: Optional[String]) -> None:
        """
        Set timeSyncServerIdentifier with validation.

        Args:
            value: The timeSyncServerIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSyncServerIdentifier = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"timeSyncServerIdentifier must be String or str or None, got {type(value).__name__}"
            )
        self._timeSyncServerIdentifier = value
        # Possible values are: NTP_RFC958, PTP_ AVB_ others.
        self._timeSync: Optional[TimeSyncTechnologyEnum] = None

    @property
    def time_sync(self) -> Optional[TimeSyncTechnologyEnum]:
        """Get timeSync (Pythonic accessor)."""
        return self._timeSync

    @time_sync.setter
    def time_sync(self, value: Optional[TimeSyncTechnologyEnum]) -> None:
        """
        Set timeSync with validation.

        Args:
            value: The timeSync to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSync = None
            return

        if not isinstance(value, TimeSyncTechnology):
            raise TypeError(
                f"timeSync must be TimeSyncTechnology or None, got {type(value).__name__}"
            )
        self._timeSync = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPriority(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: PositiveInteger) -> TimeSyncServerConfiguration:
        """
        AUTOSAR-compliant setter for priority with method chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    def getSyncInterval(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for syncInterval.

        Returns:
            The syncInterval value

        Note:
            Delegates to sync_interval property (CODING_RULE_V2_00017)
        """
        return self.sync_interval  # Delegates to property

    def setSyncInterval(self, value: TimeValue) -> TimeSyncServerConfiguration:
        """
        AUTOSAR-compliant setter for syncInterval with method chaining.

        Args:
            value: The syncInterval to set

        Returns:
            self for method chaining

        Note:
            Delegates to sync_interval property setter (gets validation automatically)
        """
        self.sync_interval = value  # Delegates to property setter
        return self

    def getTimeSyncServerIdentifier(self) -> String:
        """
        AUTOSAR-compliant getter for timeSyncServerIdentifier.

        Returns:
            The timeSyncServerIdentifier value

        Note:
            Delegates to time_sync_server_identifier property (CODING_RULE_V2_00017)
        """
        return self.time_sync_server_identifier  # Delegates to property

    def setTimeSyncServerIdentifier(self, value: String) -> TimeSyncServerConfiguration:
        """
        AUTOSAR-compliant setter for timeSyncServerIdentifier with method chaining.

        Args:
            value: The timeSyncServerIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_sync_server_identifier property setter (gets validation automatically)
        """
        self.time_sync_server_identifier = value  # Delegates to property setter
        return self

    def getTimeSync(self) -> TimeSyncTechnologyEnum:
        """
        AUTOSAR-compliant getter for timeSync.

        Returns:
            The timeSync value

        Note:
            Delegates to time_sync property (CODING_RULE_V2_00017)
        """
        return self.time_sync  # Delegates to property

    def setTimeSync(self, value: TimeSyncTechnologyEnum) -> TimeSyncServerConfiguration:
        """
        AUTOSAR-compliant setter for timeSync with method chaining.

        Args:
            value: The timeSync to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_sync property setter (gets validation automatically)
        """
        self.time_sync = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_priority(self, value: Optional[PositiveInteger]) -> TimeSyncServerConfiguration:
        """
        Set priority and return self for chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self

    def with_sync_interval(self, value: Optional[TimeValue]) -> TimeSyncServerConfiguration:
        """
        Set syncInterval and return self for chaining.

        Args:
            value: The syncInterval to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sync_interval("value")
        """
        self.sync_interval = value  # Use property setter (gets validation)
        return self

    def with_time_sync_server_identifier(self, value: Optional[String]) -> TimeSyncServerConfiguration:
        """
        Set timeSyncServerIdentifier and return self for chaining.

        Args:
            value: The timeSyncServerIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_sync_server_identifier("value")
        """
        self.time_sync_server_identifier = value  # Use property setter (gets validation)
        return self

    def with_time_sync(self, value: Optional[TimeSyncTechnologyEnum]) -> TimeSyncServerConfiguration:
        """
        Set timeSync and return self for chaining.

        Args:
            value: The timeSync to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_sync("value")
        """
        self.time_sync = value  # Use property setter (gets validation)
        return self



class OrderedMaster(ARObject):
    """
    Element in the network endpoint list.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::OrderedMaster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 470, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the order of the network endpoint list (e.
        # g.
        # 0, 1, 2,.
        self._index: Optional[PositiveInteger] = None

    @property
    def index(self) -> Optional[PositiveInteger]:
        """Get index (Pythonic accessor)."""
        return self._index

    @index.setter
    def index(self, value: Optional[PositiveInteger]) -> None:
        """
        Set index with validation.

        Args:
            value: The index to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._index = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"index must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._index = value
        self._timeSyncServerConfiguration: Optional[TimeSyncServerConfiguration] = None

    @property
    def time_sync_server_configuration(self) -> Optional[TimeSyncServerConfiguration]:
        """Get timeSyncServerConfiguration (Pythonic accessor)."""
        return self._timeSyncServerConfiguration

    @time_sync_server_configuration.setter
    def time_sync_server_configuration(self, value: Optional[TimeSyncServerConfiguration]) -> None:
        """
        Set timeSyncServerConfiguration with validation.

        Args:
            value: The timeSyncServerConfiguration to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSyncServerConfiguration = None
            return

        if not isinstance(value, TimeSyncServer):
            raise TypeError(
                f"timeSyncServerConfiguration must be TimeSyncServer or None, got {type(value).__name__}"
            )
        self._timeSyncServerConfiguration = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIndex(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for index.

        Returns:
            The index value

        Note:
            Delegates to index property (CODING_RULE_V2_00017)
        """
        return self.index  # Delegates to property

    def setIndex(self, value: PositiveInteger) -> OrderedMaster:
        """
        AUTOSAR-compliant setter for index with method chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Note:
            Delegates to index property setter (gets validation automatically)
        """
        self.index = value  # Delegates to property setter
        return self

    def getTimeSyncServerConfiguration(self) -> TimeSyncServerConfiguration:
        """
        AUTOSAR-compliant getter for timeSyncServerConfiguration.

        Returns:
            The timeSyncServerConfiguration value

        Note:
            Delegates to time_sync_server_configuration property (CODING_RULE_V2_00017)
        """
        return self.time_sync_server_configuration  # Delegates to property

    def setTimeSyncServerConfiguration(self, value: TimeSyncServerConfiguration) -> OrderedMaster:
        """
        AUTOSAR-compliant setter for timeSyncServerConfiguration with method chaining.

        Args:
            value: The timeSyncServerConfiguration to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_sync_server_configuration property setter (gets validation automatically)
        """
        self.time_sync_server_configuration = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_index(self, value: Optional[PositiveInteger]) -> OrderedMaster:
        """
        Set index and return self for chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_index("value")
        """
        self.index = value  # Use property setter (gets validation)
        return self

    def with_time_sync_server_configuration(self, value: Optional[TimeSyncServerConfiguration]) -> OrderedMaster:
        """
        Set timeSyncServerConfiguration and return self for chaining.

        Args:
            value: The timeSyncServerConfiguration to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_sync_server_configuration("value")
        """
        self.time_sync_server_configuration = value  # Use property setter (gets validation)
        return self



class DoIpEntity(ARObject):
    """
    ECU providing this infrastructure service is a DoIP-Entity.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::DoIpEntity

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 471, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Identifies the role in terms of DoIP this network-node has.
        self._doIpEntityRole: Optional[DoIpEntityRoleEnum] = None

    @property
    def do_ip_entity_role(self) -> Optional[DoIpEntityRoleEnum]:
        """Get doIpEntityRole (Pythonic accessor)."""
        return self._doIpEntityRole

    @do_ip_entity_role.setter
    def do_ip_entity_role(self, value: Optional[DoIpEntityRoleEnum]) -> None:
        """
        Set doIpEntityRole with validation.

        Args:
            value: The doIpEntityRole to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._doIpEntityRole = None
            return

        if not isinstance(value, DoIpEntityRoleEnum):
            raise TypeError(
                f"doIpEntityRole must be DoIpEntityRoleEnum or None, got {type(value).__name__}"
            )
        self._doIpEntityRole = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDoIpEntityRole(self) -> DoIpEntityRoleEnum:
        """
        AUTOSAR-compliant getter for doIpEntityRole.

        Returns:
            The doIpEntityRole value

        Note:
            Delegates to do_ip_entity_role property (CODING_RULE_V2_00017)
        """
        return self.do_ip_entity_role  # Delegates to property

    def setDoIpEntityRole(self, value: DoIpEntityRoleEnum) -> DoIpEntity:
        """
        AUTOSAR-compliant setter for doIpEntityRole with method chaining.

        Args:
            value: The doIpEntityRole to set

        Returns:
            self for method chaining

        Note:
            Delegates to do_ip_entity_role property setter (gets validation automatically)
        """
        self.do_ip_entity_role = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_do_ip_entity_role(self, value: Optional[DoIpEntityRoleEnum]) -> DoIpEntity:
        """
        Set doIpEntityRole and return self for chaining.

        Args:
            value: The doIpEntityRole to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_do_ip_entity_role("value")
        """
        self.do_ip_entity_role = value  # Use property setter (gets validation)
        return self



class GlobalTimeCouplingPortProps(ARObject):
    """
    Defines properties for the usage of the CouplingPort in the scope of Global
    Time Sync.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::GlobalTimeCouplingPortProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 875, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If cyclic propagation delay measurement is enabled, this represents the
        # default value of the propagation the first actually measured propagation
        # delay is cyclic propagation delay measurement is parameter defines a fixed
        # value for the.
        self._propagation: Optional[TimeValue] = None

    @property
    def propagation(self) -> Optional[TimeValue]:
        """Get propagation (Pythonic accessor)."""
        return self._propagation

    @propagation.setter
    def propagation(self, value: Optional[TimeValue]) -> None:
        """
        Set propagation with validation.

        Args:
            value: The propagation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._propagation = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"propagation must be TimeValue or None, got {type(value).__name__}"
            )
        self._propagation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPropagation(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for propagation.

        Returns:
            The propagation value

        Note:
            Delegates to propagation property (CODING_RULE_V2_00017)
        """
        return self.propagation  # Delegates to property

    def setPropagation(self, value: TimeValue) -> GlobalTimeCouplingPortProps:
        """
        AUTOSAR-compliant setter for propagation with method chaining.

        Args:
            value: The propagation to set

        Returns:
            self for method chaining

        Note:
            Delegates to propagation property setter (gets validation automatically)
        """
        self.propagation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_propagation(self, value: Optional[TimeValue]) -> GlobalTimeCouplingPortProps:
        """
        Set propagation and return self for chaining.

        Args:
            value: The propagation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_propagation("value")
        """
        self.propagation = value  # Use property setter (gets validation)
        return self



class CouplingPortAsynchronousTrafficShaper(Identifiable):
    """
    Defines an Asynchronous Traffic Shaper (ATS) for the CouplingPort egress
    structure.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortAsynchronousTrafficShaper

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2012, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum token capacity of the token bucket in bit.
        # atp.
        # Status=candidate.
        self._committedBurst: Optional[PositiveInteger] = None

    @property
    def committed_burst(self) -> Optional[PositiveInteger]:
        """Get committedBurst (Pythonic accessor)."""
        return self._committedBurst

    @committed_burst.setter
    def committed_burst(self, value: Optional[PositiveInteger]) -> None:
        """
        Set committedBurst with validation.

        Args:
            value: The committedBurst to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._committedBurst = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"committedBurst must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._committedBurst = value
        # second.
        self._committed: Optional[PositiveInteger] = None

    @property
    def committed(self) -> Optional[PositiveInteger]:
        """Get committed (Pythonic accessor)."""
        return self._committed

    @committed.setter
    def committed(self, value: Optional[PositiveInteger]) -> None:
        """
        Set committed with validation.

        Args:
            value: The committed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._committed = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"committed must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._committed = value
                # part of.
        # atp.
        # Status=candidate.
        self._trafficShaper: Optional[SwitchAsynchronousEnum] = None

    @property
    def traffic_shaper(self) -> Optional[SwitchAsynchronousEnum]:
        """Get trafficShaper (Pythonic accessor)."""
        return self._trafficShaper

    @traffic_shaper.setter
    def traffic_shaper(self, value: Optional[SwitchAsynchronousEnum]) -> None:
        """
        Set trafficShaper with validation.

        Args:
            value: The trafficShaper to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trafficShaper = None
            return

        if not isinstance(value, SwitchAsynchronous):
            raise TypeError(
                f"trafficShaper must be SwitchAsynchronous or None, got {type(value).__name__}"
            )
        self._trafficShaper = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommittedBurst(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for committedBurst.

        Returns:
            The committedBurst value

        Note:
            Delegates to committed_burst property (CODING_RULE_V2_00017)
        """
        return self.committed_burst  # Delegates to property

    def setCommittedBurst(self, value: PositiveInteger) -> CouplingPortAsynchronousTrafficShaper:
        """
        AUTOSAR-compliant setter for committedBurst with method chaining.

        Args:
            value: The committedBurst to set

        Returns:
            self for method chaining

        Note:
            Delegates to committed_burst property setter (gets validation automatically)
        """
        self.committed_burst = value  # Delegates to property setter
        return self

    def getCommitted(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for committed.

        Returns:
            The committed value

        Note:
            Delegates to committed property (CODING_RULE_V2_00017)
        """
        return self.committed  # Delegates to property

    def setCommitted(self, value: PositiveInteger) -> CouplingPortAsynchronousTrafficShaper:
        """
        AUTOSAR-compliant setter for committed with method chaining.

        Args:
            value: The committed to set

        Returns:
            self for method chaining

        Note:
            Delegates to committed property setter (gets validation automatically)
        """
        self.committed = value  # Delegates to property setter
        return self

    def getTrafficShaper(self) -> SwitchAsynchronousEnum:
        """
        AUTOSAR-compliant getter for trafficShaper.

        Returns:
            The trafficShaper value

        Note:
            Delegates to traffic_shaper property (CODING_RULE_V2_00017)
        """
        return self.traffic_shaper  # Delegates to property

    def setTrafficShaper(self, value: SwitchAsynchronousEnum) -> CouplingPortAsynchronousTrafficShaper:
        """
        AUTOSAR-compliant setter for trafficShaper with method chaining.

        Args:
            value: The trafficShaper to set

        Returns:
            self for method chaining

        Note:
            Delegates to traffic_shaper property setter (gets validation automatically)
        """
        self.traffic_shaper = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_committed_burst(self, value: Optional[PositiveInteger]) -> CouplingPortAsynchronousTrafficShaper:
        """
        Set committedBurst and return self for chaining.

        Args:
            value: The committedBurst to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_committed_burst("value")
        """
        self.committed_burst = value  # Use property setter (gets validation)
        return self

    def with_committed(self, value: Optional[PositiveInteger]) -> CouplingPortAsynchronousTrafficShaper:
        """
        Set committed and return self for chaining.

        Args:
            value: The committed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_committed("value")
        """
        self.committed = value  # Use property setter (gets validation)
        return self

    def with_traffic_shaper(self, value: Optional[SwitchAsynchronousEnum]) -> CouplingPortAsynchronousTrafficShaper:
        """
        Set trafficShaper and return self for chaining.

        Args:
            value: The trafficShaper to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_traffic_shaper("value")
        """
        self.traffic_shaper = value  # Use property setter (gets validation)
        return self



class CouplingPortCreditBasedShaper(Identifiable):
    """
    Defines a Credit Based Shaper (CBS) for the CouplingPort egress structure.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortCreditBasedShaper

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2013, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the increase of credit in bits per second for the.
        self._idleSlope: Optional[PositiveInteger] = None

    @property
    def idle_slope(self) -> Optional[PositiveInteger]:
        """Get idleSlope (Pythonic accessor)."""
        return self._idleSlope

    @idle_slope.setter
    def idle_slope(self, value: Optional[PositiveInteger]) -> None:
        """
        Set idleSlope with validation.

        Args:
            value: The idleSlope to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._idleSlope = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"idleSlope must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._idleSlope = value
        self._lowerBoundary: Optional[PositiveInteger] = None

    @property
    def lower_boundary(self) -> Optional[PositiveInteger]:
        """Get lowerBoundary (Pythonic accessor)."""
        return self._lowerBoundary

    @lower_boundary.setter
    def lower_boundary(self, value: Optional[PositiveInteger]) -> None:
        """
        Set lowerBoundary with validation.

        Args:
            value: The lowerBoundary to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lowerBoundary = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"lowerBoundary must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._lowerBoundary = value
        self._upperBoundary: Optional[PositiveInteger] = None

    @property
    def upper_boundary(self) -> Optional[PositiveInteger]:
        """Get upperBoundary (Pythonic accessor)."""
        return self._upperBoundary

    @upper_boundary.setter
    def upper_boundary(self, value: Optional[PositiveInteger]) -> None:
        """
        Set upperBoundary with validation.

        Args:
            value: The upperBoundary to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upperBoundary = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"upperBoundary must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._upperBoundary = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIdleSlope(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for idleSlope.

        Returns:
            The idleSlope value

        Note:
            Delegates to idle_slope property (CODING_RULE_V2_00017)
        """
        return self.idle_slope  # Delegates to property

    def setIdleSlope(self, value: PositiveInteger) -> CouplingPortCreditBasedShaper:
        """
        AUTOSAR-compliant setter for idleSlope with method chaining.

        Args:
            value: The idleSlope to set

        Returns:
            self for method chaining

        Note:
            Delegates to idle_slope property setter (gets validation automatically)
        """
        self.idle_slope = value  # Delegates to property setter
        return self

    def getLowerBoundary(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for lowerBoundary.

        Returns:
            The lowerBoundary value

        Note:
            Delegates to lower_boundary property (CODING_RULE_V2_00017)
        """
        return self.lower_boundary  # Delegates to property

    def setLowerBoundary(self, value: PositiveInteger) -> CouplingPortCreditBasedShaper:
        """
        AUTOSAR-compliant setter for lowerBoundary with method chaining.

        Args:
            value: The lowerBoundary to set

        Returns:
            self for method chaining

        Note:
            Delegates to lower_boundary property setter (gets validation automatically)
        """
        self.lower_boundary = value  # Delegates to property setter
        return self

    def getUpperBoundary(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for upperBoundary.

        Returns:
            The upperBoundary value

        Note:
            Delegates to upper_boundary property (CODING_RULE_V2_00017)
        """
        return self.upper_boundary  # Delegates to property

    def setUpperBoundary(self, value: PositiveInteger) -> CouplingPortCreditBasedShaper:
        """
        AUTOSAR-compliant setter for upperBoundary with method chaining.

        Args:
            value: The upperBoundary to set

        Returns:
            self for method chaining

        Note:
            Delegates to upper_boundary property setter (gets validation automatically)
        """
        self.upper_boundary = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_idle_slope(self, value: Optional[PositiveInteger]) -> CouplingPortCreditBasedShaper:
        """
        Set idleSlope and return self for chaining.

        Args:
            value: The idleSlope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_idle_slope("value")
        """
        self.idle_slope = value  # Use property setter (gets validation)
        return self

    def with_lower_boundary(self, value: Optional[PositiveInteger]) -> CouplingPortCreditBasedShaper:
        """
        Set lowerBoundary and return self for chaining.

        Args:
            value: The lowerBoundary to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lower_boundary("value")
        """
        self.lower_boundary = value  # Use property setter (gets validation)
        return self

    def with_upper_boundary(self, value: Optional[PositiveInteger]) -> CouplingPortCreditBasedShaper:
        """
        Set upperBoundary and return self for chaining.

        Args:
            value: The upperBoundary to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_upper_boundary("value")
        """
        self.upper_boundary = value  # Use property setter (gets validation)
        return self



class CouplingPortScheduler(CouplingPortStructuralElement):
    """
    Defines a scheduler for the CouplingPort egress structure.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortScheduler

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 123, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the schedule algorithm to be used.
        self._portSchedulerSchedulerEnum: Optional[EthernetCouplingPortConfiguration] = None

    @property
    def port_scheduler_scheduler_enum(self) -> Optional[EthernetCouplingPortConfiguration]:
        """Get portSchedulerSchedulerEnum (Pythonic accessor)."""
        return self._portSchedulerSchedulerEnum

    @port_scheduler_scheduler_enum.setter
    def port_scheduler_scheduler_enum(self, value: Optional[EthernetCouplingPortConfiguration]) -> None:
        """
        Set portSchedulerSchedulerEnum with validation.

        Args:
            value: The portSchedulerSchedulerEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._portSchedulerSchedulerEnum = None
            return

        if not isinstance(value, EthernetCouplingPort):
            raise TypeError(
                f"portSchedulerSchedulerEnum must be EthernetCouplingPort or None, got {type(value).__name__}"
            )
        self._portSchedulerSchedulerEnum = value
        # The first element has the highest priority.
        # The following elements have.
        self._predecessor: List["CouplingPortStructural"] = []

    @property
    def predecessor(self) -> List["CouplingPortStructural"]:
        """Get predecessor (Pythonic accessor)."""
        return self._predecessor

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPortSchedulerSchedulerEnum(self) -> EthernetCouplingPortConfiguration:
        """
        AUTOSAR-compliant getter for portSchedulerSchedulerEnum.

        Returns:
            The portSchedulerSchedulerEnum value

        Note:
            Delegates to port_scheduler_scheduler_enum property (CODING_RULE_V2_00017)
        """
        return self.port_scheduler_scheduler_enum  # Delegates to property

    def setPortSchedulerSchedulerEnum(self, value: EthernetCouplingPortConfiguration) -> CouplingPortScheduler:
        """
        AUTOSAR-compliant setter for portSchedulerSchedulerEnum with method chaining.

        Args:
            value: The portSchedulerSchedulerEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to port_scheduler_scheduler_enum property setter (gets validation automatically)
        """
        self.port_scheduler_scheduler_enum = value  # Delegates to property setter
        return self

    def getPredecessor(self) -> List["CouplingPortStructural"]:
        """
        AUTOSAR-compliant getter for predecessor.

        Returns:
            The predecessor value

        Note:
            Delegates to predecessor property (CODING_RULE_V2_00017)
        """
        return self.predecessor  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_port_scheduler_scheduler_enum(self, value: Optional[EthernetCouplingPortConfiguration]) -> CouplingPortScheduler:
        """
        Set portSchedulerSchedulerEnum and return self for chaining.

        Args:
            value: The portSchedulerSchedulerEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_scheduler_scheduler_enum("value")
        """
        self.port_scheduler_scheduler_enum = value  # Use property setter (gets validation)
        return self



class CouplingPortShaper(CouplingPortStructuralElement):
    """
    Defines a shaper for the CouplingPort egress structure.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortShaper

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 123, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the increase of credit in bits per second for the.
        self._idleSlope: Optional[PositiveInteger] = None

    @property
    def idle_slope(self) -> Optional[PositiveInteger]:
        """Get idleSlope (Pythonic accessor)."""
        return self._idleSlope

    @idle_slope.setter
    def idle_slope(self, value: Optional[PositiveInteger]) -> None:
        """
        Set idleSlope with validation.

        Args:
            value: The idleSlope to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._idleSlope = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"idleSlope must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._idleSlope = value
        self._predecessorFifo: CouplingPortFifo = None

    @property
    def predecessor_fifo(self) -> CouplingPortFifo:
        """Get predecessorFifo (Pythonic accessor)."""
        return self._predecessorFifo

    @predecessor_fifo.setter
    def predecessor_fifo(self, value: CouplingPortFifo) -> None:
        """
        Set predecessorFifo with validation.

        Args:
            value: The predecessorFifo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, CouplingPortFifo):
            raise TypeError(
                f"predecessorFifo must be CouplingPortFifo, got {type(value).__name__}"
            )
        self._predecessorFifo = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIdleSlope(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for idleSlope.

        Returns:
            The idleSlope value

        Note:
            Delegates to idle_slope property (CODING_RULE_V2_00017)
        """
        return self.idle_slope  # Delegates to property

    def setIdleSlope(self, value: PositiveInteger) -> CouplingPortShaper:
        """
        AUTOSAR-compliant setter for idleSlope with method chaining.

        Args:
            value: The idleSlope to set

        Returns:
            self for method chaining

        Note:
            Delegates to idle_slope property setter (gets validation automatically)
        """
        self.idle_slope = value  # Delegates to property setter
        return self

    def getPredecessorFifo(self) -> CouplingPortFifo:
        """
        AUTOSAR-compliant getter for predecessorFifo.

        Returns:
            The predecessorFifo value

        Note:
            Delegates to predecessor_fifo property (CODING_RULE_V2_00017)
        """
        return self.predecessor_fifo  # Delegates to property

    def setPredecessorFifo(self, value: CouplingPortFifo) -> CouplingPortShaper:
        """
        AUTOSAR-compliant setter for predecessorFifo with method chaining.

        Args:
            value: The predecessorFifo to set

        Returns:
            self for method chaining

        Note:
            Delegates to predecessor_fifo property setter (gets validation automatically)
        """
        self.predecessor_fifo = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_idle_slope(self, value: Optional[PositiveInteger]) -> CouplingPortShaper:
        """
        Set idleSlope and return self for chaining.

        Args:
            value: The idleSlope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_idle_slope("value")
        """
        self.idle_slope = value  # Use property setter (gets validation)
        return self

    def with_predecessor_fifo(self, value: CouplingPortFifo) -> CouplingPortShaper:
        """
        Set predecessorFifo and return self for chaining.

        Args:
            value: The predecessorFifo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_predecessor_fifo("value")
        """
        self.predecessor_fifo = value  # Use property setter (gets validation)
        return self



class CouplingPortFifo(CouplingPortStructuralElement):
    """
    Defines a FIFO for the CouplingPort egress structure.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPortFifo

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 124, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._assignedTraffic: PositiveInteger = None

    @property
    def assigned_traffic(self) -> PositiveInteger:
        """Get assignedTraffic (Pythonic accessor)."""
        return self._assignedTraffic

    @assigned_traffic.setter
    def assigned_traffic(self, value: PositiveInteger) -> None:
        """
        Set assignedTraffic with validation.

        Args:
            value: The assignedTraffic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"assignedTraffic must be PositiveInteger or str, got {type(value).__name__}"
            )
        self._assignedTraffic = value
        # An actual configuration/ may use a bigger value.
        self._minimumFifo: Optional[PositiveInteger] = None

    @property
    def minimum_fifo(self) -> Optional[PositiveInteger]:
        """Get minimumFifo (Pythonic accessor)."""
        return self._minimumFifo

    @minimum_fifo.setter
    def minimum_fifo(self, value: Optional[PositiveInteger]) -> None:
        """
        Set minimumFifo with validation.

        Args:
            value: The minimumFifo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumFifo = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minimumFifo must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minimumFifo = value
        self._shaper: Optional[CouplingPortAbstract] = None

    @property
    def shaper(self) -> Optional[CouplingPortAbstract]:
        """Get shaper (Pythonic accessor)."""
        return self._shaper

    @shaper.setter
    def shaper(self, value: Optional[CouplingPortAbstract]) -> None:
        """
        Set shaper with validation.

        Args:
            value: The shaper to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shaper = None
            return

        if not isinstance(value, CouplingPortAbstract):
            raise TypeError(
                f"shaper must be CouplingPortAbstract or None, got {type(value).__name__}"
            )
        self._shaper = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssignedTraffic(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for assignedTraffic.

        Returns:
            The assignedTraffic value

        Note:
            Delegates to assigned_traffic property (CODING_RULE_V2_00017)
        """
        return self.assigned_traffic  # Delegates to property

    def setAssignedTraffic(self, value: PositiveInteger) -> CouplingPortFifo:
        """
        AUTOSAR-compliant setter for assignedTraffic with method chaining.

        Args:
            value: The assignedTraffic to set

        Returns:
            self for method chaining

        Note:
            Delegates to assigned_traffic property setter (gets validation automatically)
        """
        self.assigned_traffic = value  # Delegates to property setter
        return self

    def getMinimumFifo(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for minimumFifo.

        Returns:
            The minimumFifo value

        Note:
            Delegates to minimum_fifo property (CODING_RULE_V2_00017)
        """
        return self.minimum_fifo  # Delegates to property

    def setMinimumFifo(self, value: PositiveInteger) -> CouplingPortFifo:
        """
        AUTOSAR-compliant setter for minimumFifo with method chaining.

        Args:
            value: The minimumFifo to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum_fifo property setter (gets validation automatically)
        """
        self.minimum_fifo = value  # Delegates to property setter
        return self

    def getShaper(self) -> CouplingPortAbstract:
        """
        AUTOSAR-compliant getter for shaper.

        Returns:
            The shaper value

        Note:
            Delegates to shaper property (CODING_RULE_V2_00017)
        """
        return self.shaper  # Delegates to property

    def setShaper(self, value: CouplingPortAbstract) -> CouplingPortFifo:
        """
        AUTOSAR-compliant setter for shaper with method chaining.

        Args:
            value: The shaper to set

        Returns:
            self for method chaining

        Note:
            Delegates to shaper property setter (gets validation automatically)
        """
        self.shaper = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_assigned_traffic(self, value: PositiveInteger) -> CouplingPortFifo:
        """
        Set assignedTraffic and return self for chaining.

        Args:
            value: The assignedTraffic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assigned_traffic("value")
        """
        self.assigned_traffic = value  # Use property setter (gets validation)
        return self

    def with_minimum_fifo(self, value: Optional[PositiveInteger]) -> CouplingPortFifo:
        """
        Set minimumFifo and return self for chaining.

        Args:
            value: The minimumFifo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum_fifo("value")
        """
        self.minimum_fifo = value  # Use property setter (gets validation)
        return self

    def with_shaper(self, value: Optional[CouplingPortAbstract]) -> CouplingPortFifo:
        """
        Set shaper and return self for chaining.

        Args:
            value: The shaper to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_shaper("value")
        """
        self.shaper = value  # Use property setter (gets validation)
        return self



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
        self._flowMetering: List[SwitchFlowMeteringEnum] = []

    @property
    def flow_metering(self) -> List[SwitchFlowMeteringEnum]:
        """Get flowMetering (Pythonic accessor)."""
        return self._flowMetering
        # Collection of Stream Filter Entries.
        # atp.
        # Status=candidate.
        self._streamFilter: List[SwitchStreamFilterEntry] = []

    @property
    def stream_filter(self) -> List[SwitchStreamFilterEntry]:
        """Get streamFilter (Pythonic accessor)."""
        return self._streamFilter
        # Collection of Stream Gate Entries.
        self._streamGate: List[SwitchStreamGateEntry] = []

    @property
    def stream_gate(self) -> List[SwitchStreamGateEntry]:
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
        self._trafficShaper: List[SwitchAsynchronousEnum] = []

    @property
    def traffic_shaper(self) -> List[SwitchAsynchronousEnum]:
        """Get trafficShaper (Pythonic accessor)."""
        return self._trafficShaper

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFlowMetering(self) -> List[SwitchFlowMeteringEnum]:
        """
        AUTOSAR-compliant getter for flowMetering.

        Returns:
            The flowMetering value

        Note:
            Delegates to flow_metering property (CODING_RULE_V2_00017)
        """
        return self.flow_metering  # Delegates to property

    def getStreamFilter(self) -> List[SwitchStreamFilterEntry]:
        """
        AUTOSAR-compliant getter for streamFilter.

        Returns:
            The streamFilter value

        Note:
            Delegates to stream_filter property (CODING_RULE_V2_00017)
        """
        return self.stream_filter  # Delegates to property

    def getStreamGate(self) -> List[SwitchStreamGateEntry]:
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

    def getTrafficShaper(self) -> List[SwitchAsynchronousEnum]:
        """
        AUTOSAR-compliant getter for trafficShaper.

        Returns:
            The trafficShaper value

        Note:
            Delegates to traffic_shaper property (CODING_RULE_V2_00017)
        """
        return self.traffic_shaper  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class GenericTp(TransportProtocolConfiguration):
    """
    Content Model for a generic transport protocol.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::GenericTp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 459, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Transport Protocol dependent Address.
        self._tpAddress: Optional[String] = None

    @property
    def tp_address(self) -> Optional[String]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress

    @tp_address.setter
    def tp_address(self, value: Optional[String]) -> None:
        """
        Set tpAddress with validation.

        Args:
            value: The tpAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpAddress = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"tpAddress must be String or str or None, got {type(value).__name__}"
            )
        self._tpAddress = value
        self._tpTechnology: Optional[String] = None

    @property
    def tp_technology(self) -> Optional[String]:
        """Get tpTechnology (Pythonic accessor)."""
        return self._tpTechnology

    @tp_technology.setter
    def tp_technology(self, value: Optional[String]) -> None:
        """
        Set tpTechnology with validation.

        Args:
            value: The tpTechnology to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpTechnology = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"tpTechnology must be String or str or None, got {type(value).__name__}"
            )
        self._tpTechnology = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpAddress(self) -> String:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def setTpAddress(self, value: String) -> GenericTp:
        """
        AUTOSAR-compliant setter for tpAddress with method chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_address property setter (gets validation automatically)
        """
        self.tp_address = value  # Delegates to property setter
        return self

    def getTpTechnology(self) -> String:
        """
        AUTOSAR-compliant getter for tpTechnology.

        Returns:
            The tpTechnology value

        Note:
            Delegates to tp_technology property (CODING_RULE_V2_00017)
        """
        return self.tp_technology  # Delegates to property

    def setTpTechnology(self, value: String) -> GenericTp:
        """
        AUTOSAR-compliant setter for tpTechnology with method chaining.

        Args:
            value: The tpTechnology to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_technology property setter (gets validation automatically)
        """
        self.tp_technology = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tp_address(self, value: Optional[String]) -> GenericTp:
        """
        Set tpAddress and return self for chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_address("value")
        """
        self.tp_address = value  # Use property setter (gets validation)
        return self

    def with_tp_technology(self, value: Optional[String]) -> GenericTp:
        """
        Set tpTechnology and return self for chaining.

        Args:
            value: The tpTechnology to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_technology("value")
        """
        self.tp_technology = value  # Use property setter (gets validation)
        return self



class TcpUdpConfig(TransportProtocolConfiguration, ABC):
    """
    Tcp or Udp Transport Protocol Configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TcpUdpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 459, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TcpUdpConfig:
            raise TypeError("TcpUdpConfig is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class RtpTp(TransportProtocolConfiguration):
    """
    RTP over UDP or over TCP as transport protocol.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::RtpTp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 460, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Synchronization source identifier uniquely identifies the a stream.
        # The synchronization sources within RTP session will be unique.
        self._ssrc: Optional[PositiveInteger] = None

    @property
    def ssrc(self) -> Optional[PositiveInteger]:
        """Get ssrc (Pythonic accessor)."""
        return self._ssrc

    @ssrc.setter
    def ssrc(self, value: Optional[PositiveInteger]) -> None:
        """
        Set ssrc with validation.

        Args:
            value: The ssrc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ssrc = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"ssrc must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._ssrc = value
        self._tcpUdpConfig: Optional[TcpUdpConfig] = None

    @property
    def tcp_udp_config(self) -> Optional[TcpUdpConfig]:
        """Get tcpUdpConfig (Pythonic accessor)."""
        return self._tcpUdpConfig

    @tcp_udp_config.setter
    def tcp_udp_config(self, value: Optional[TcpUdpConfig]) -> None:
        """
        Set tcpUdpConfig with validation.

        Args:
            value: The tcpUdpConfig to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpUdpConfig = None
            return

        if not isinstance(value, TcpUdpConfig):
            raise TypeError(
                f"tcpUdpConfig must be TcpUdpConfig or None, got {type(value).__name__}"
            )
        self._tcpUdpConfig = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSsrc(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for ssrc.

        Returns:
            The ssrc value

        Note:
            Delegates to ssrc property (CODING_RULE_V2_00017)
        """
        return self.ssrc  # Delegates to property

    def setSsrc(self, value: PositiveInteger) -> RtpTp:
        """
        AUTOSAR-compliant setter for ssrc with method chaining.

        Args:
            value: The ssrc to set

        Returns:
            self for method chaining

        Note:
            Delegates to ssrc property setter (gets validation automatically)
        """
        self.ssrc = value  # Delegates to property setter
        return self

    def getTcpUdpConfig(self) -> TcpUdpConfig:
        """
        AUTOSAR-compliant getter for tcpUdpConfig.

        Returns:
            The tcpUdpConfig value

        Note:
            Delegates to tcp_udp_config property (CODING_RULE_V2_00017)
        """
        return self.tcp_udp_config  # Delegates to property

    def setTcpUdpConfig(self, value: TcpUdpConfig) -> RtpTp:
        """
        AUTOSAR-compliant setter for tcpUdpConfig with method chaining.

        Args:
            value: The tcpUdpConfig to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_udp_config property setter (gets validation automatically)
        """
        self.tcp_udp_config = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ssrc(self, value: Optional[PositiveInteger]) -> RtpTp:
        """
        Set ssrc and return self for chaining.

        Args:
            value: The ssrc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ssrc("value")
        """
        self.ssrc = value  # Use property setter (gets validation)
        return self

    def with_tcp_udp_config(self, value: Optional[TcpUdpConfig]) -> RtpTp:
        """
        Set tcpUdpConfig and return self for chaining.

        Args:
            value: The tcpUdpConfig to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_udp_config("value")
        """
        self.tcp_udp_config = value  # Use property setter (gets validation)
        return self



class Ieee1722Tp(TransportProtocolConfiguration):
    """
    Content Model for IEEE 1722 configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ieee1722Tp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 460, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the time when content shall be presented (in The actual absolute time
                # is creation time plus presentation time.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._relative: Optional[TimeValue] = None

    @property
    def relative(self) -> Optional[TimeValue]:
        """Get relative (Pythonic accessor)."""
        return self._relative

    @relative.setter
    def relative(self, value: Optional[TimeValue]) -> None:
        """
        Set relative with validation.

        Args:
            value: The relative to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._relative = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"relative must be TimeValue or None, got {type(value).__name__}"
            )
        self._relative = value
        self._streamIdentifier: Optional[PositiveInteger] = None

    @property
    def stream_identifier(self) -> Optional[PositiveInteger]:
        """Get streamIdentifier (Pythonic accessor)."""
        return self._streamIdentifier

    @stream_identifier.setter
    def stream_identifier(self, value: Optional[PositiveInteger]) -> None:
        """
        Set streamIdentifier with validation.

        Args:
            value: The streamIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._streamIdentifier = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"streamIdentifier must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._streamIdentifier = value
        self._subType: Optional[PositiveInteger] = None

    @property
    def sub_type(self) -> Optional[PositiveInteger]:
        """Get subType (Pythonic accessor)."""
        return self._subType

    @sub_type.setter
    def sub_type(self, value: Optional[PositiveInteger]) -> None:
        """
        Set subType with validation.

        Args:
            value: The subType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._subType = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"subType must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._subType = value
        self._version: Optional[PositiveInteger] = None

    @property
    def version(self) -> Optional[PositiveInteger]:
        """Get version (Pythonic accessor)."""
        return self._version

    @version.setter
    def version(self, value: Optional[PositiveInteger]) -> None:
        """
        Set version with validation.

        Args:
            value: The version to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._version = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"version must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._version = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRelative(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for relative.

        Returns:
            The relative value

        Note:
            Delegates to relative property (CODING_RULE_V2_00017)
        """
        return self.relative  # Delegates to property

    def setRelative(self, value: TimeValue) -> Ieee1722Tp:
        """
        AUTOSAR-compliant setter for relative with method chaining.

        Args:
            value: The relative to set

        Returns:
            self for method chaining

        Note:
            Delegates to relative property setter (gets validation automatically)
        """
        self.relative = value  # Delegates to property setter
        return self

    def getStreamIdentifier(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for streamIdentifier.

        Returns:
            The streamIdentifier value

        Note:
            Delegates to stream_identifier property (CODING_RULE_V2_00017)
        """
        return self.stream_identifier  # Delegates to property

    def setStreamIdentifier(self, value: PositiveInteger) -> Ieee1722Tp:
        """
        AUTOSAR-compliant setter for streamIdentifier with method chaining.

        Args:
            value: The streamIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to stream_identifier property setter (gets validation automatically)
        """
        self.stream_identifier = value  # Delegates to property setter
        return self

    def getSubType(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for subType.

        Returns:
            The subType value

        Note:
            Delegates to sub_type property (CODING_RULE_V2_00017)
        """
        return self.sub_type  # Delegates to property

    def setSubType(self, value: PositiveInteger) -> Ieee1722Tp:
        """
        AUTOSAR-compliant setter for subType with method chaining.

        Args:
            value: The subType to set

        Returns:
            self for method chaining

        Note:
            Delegates to sub_type property setter (gets validation automatically)
        """
        self.sub_type = value  # Delegates to property setter
        return self

    def getVersion(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for version.

        Returns:
            The version value

        Note:
            Delegates to version property (CODING_RULE_V2_00017)
        """
        return self.version  # Delegates to property

    def setVersion(self, value: PositiveInteger) -> Ieee1722Tp:
        """
        AUTOSAR-compliant setter for version with method chaining.

        Args:
            value: The version to set

        Returns:
            self for method chaining

        Note:
            Delegates to version property setter (gets validation automatically)
        """
        self.version = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_relative(self, value: Optional[TimeValue]) -> Ieee1722Tp:
        """
        Set relative and return self for chaining.

        Args:
            value: The relative to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_relative("value")
        """
        self.relative = value  # Use property setter (gets validation)
        return self

    def with_stream_identifier(self, value: Optional[PositiveInteger]) -> Ieee1722Tp:
        """
        Set streamIdentifier and return self for chaining.

        Args:
            value: The streamIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_stream_identifier("value")
        """
        self.stream_identifier = value  # Use property setter (gets validation)
        return self

    def with_sub_type(self, value: Optional[PositiveInteger]) -> Ieee1722Tp:
        """
        Set subType and return self for chaining.

        Args:
            value: The subType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_type("value")
        """
        self.sub_type = value  # Use property setter (gets validation)
        return self

    def with_version(self, value: Optional[PositiveInteger]) -> Ieee1722Tp:
        """
        Set version and return self for chaining.

        Args:
            value: The version to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_version("value")
        """
        self.version = value  # Use property setter (gets validation)
        return self



class HttpTp(TransportProtocolConfiguration):
    """
    Http over TCP as transport protocol.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::HttpTp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 461, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Descriptor for the transported content.
        self._contentType: Optional[String] = None

    @property
    def content_type(self) -> Optional[String]:
        """Get contentType (Pythonic accessor)."""
        return self._contentType

    @content_type.setter
    def content_type(self, value: Optional[String]) -> None:
        """
        Set contentType with validation.

        Args:
            value: The contentType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contentType = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"contentType must be String or str or None, got {type(value).__name__}"
            )
        self._contentType = value
        # g.
        # 1.
        # 1).
        self._protocolVersion: Optional[String] = None

    @property
    def protocol_version(self) -> Optional[String]:
        """Get protocolVersion (Pythonic accessor)."""
        return self._protocolVersion

    @protocol_version.setter
    def protocol_version(self, value: Optional[String]) -> None:
        """
        Set protocolVersion with validation.

        Args:
            value: The protocolVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._protocolVersion = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"protocolVersion must be String or str or None, got {type(value).__name__}"
            )
        self._protocolVersion = value
        self._requestMethod: Optional[RequestMethodEnum] = None

    @property
    def request_method(self) -> Optional[RequestMethodEnum]:
        """Get requestMethod (Pythonic accessor)."""
        return self._requestMethod

    @request_method.setter
    def request_method(self, value: Optional[RequestMethodEnum]) -> None:
        """
        Set requestMethod with validation.

        Args:
            value: The requestMethod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requestMethod = None
            return

        if not isinstance(value, RequestMethodEnum):
            raise TypeError(
                f"requestMethod must be RequestMethodEnum or None, got {type(value).__name__}"
            )
        self._requestMethod = value
        self._tcpTpConfig: Optional[TcpTp] = None

    @property
    def tcp_tp_config(self) -> Optional[TcpTp]:
        """Get tcpTpConfig (Pythonic accessor)."""
        return self._tcpTpConfig

    @tcp_tp_config.setter
    def tcp_tp_config(self, value: Optional[TcpTp]) -> None:
        """
        Set tcpTpConfig with validation.

        Args:
            value: The tcpTpConfig to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpTpConfig = None
            return

        if not isinstance(value, TcpTp):
            raise TypeError(
                f"tcpTpConfig must be TcpTp or None, got {type(value).__name__}"
            )
        self._tcpTpConfig = value
        self._uri: Optional[UriString] = None

    @property
    def uri(self) -> Optional[UriString]:
        """Get uri (Pythonic accessor)."""
        return self._uri

    @uri.setter
    def uri(self, value: Optional[UriString]) -> None:
        """
        Set uri with validation.

        Args:
            value: The uri to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._uri = None
            return

        if not isinstance(value, UriString):
            raise TypeError(
                f"uri must be UriString or None, got {type(value).__name__}"
            )
        self._uri = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContentType(self) -> String:
        """
        AUTOSAR-compliant getter for contentType.

        Returns:
            The contentType value

        Note:
            Delegates to content_type property (CODING_RULE_V2_00017)
        """
        return self.content_type  # Delegates to property

    def setContentType(self, value: String) -> HttpTp:
        """
        AUTOSAR-compliant setter for contentType with method chaining.

        Args:
            value: The contentType to set

        Returns:
            self for method chaining

        Note:
            Delegates to content_type property setter (gets validation automatically)
        """
        self.content_type = value  # Delegates to property setter
        return self

    def getProtocolVersion(self) -> String:
        """
        AUTOSAR-compliant getter for protocolVersion.

        Returns:
            The protocolVersion value

        Note:
            Delegates to protocol_version property (CODING_RULE_V2_00017)
        """
        return self.protocol_version  # Delegates to property

    def setProtocolVersion(self, value: String) -> HttpTp:
        """
        AUTOSAR-compliant setter for protocolVersion with method chaining.

        Args:
            value: The protocolVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to protocol_version property setter (gets validation automatically)
        """
        self.protocol_version = value  # Delegates to property setter
        return self

    def getRequestMethod(self) -> RequestMethodEnum:
        """
        AUTOSAR-compliant getter for requestMethod.

        Returns:
            The requestMethod value

        Note:
            Delegates to request_method property (CODING_RULE_V2_00017)
        """
        return self.request_method  # Delegates to property

    def setRequestMethod(self, value: RequestMethodEnum) -> HttpTp:
        """
        AUTOSAR-compliant setter for requestMethod with method chaining.

        Args:
            value: The requestMethod to set

        Returns:
            self for method chaining

        Note:
            Delegates to request_method property setter (gets validation automatically)
        """
        self.request_method = value  # Delegates to property setter
        return self

    def getTcpTpConfig(self) -> TcpTp:
        """
        AUTOSAR-compliant getter for tcpTpConfig.

        Returns:
            The tcpTpConfig value

        Note:
            Delegates to tcp_tp_config property (CODING_RULE_V2_00017)
        """
        return self.tcp_tp_config  # Delegates to property

    def setTcpTpConfig(self, value: TcpTp) -> HttpTp:
        """
        AUTOSAR-compliant setter for tcpTpConfig with method chaining.

        Args:
            value: The tcpTpConfig to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_tp_config property setter (gets validation automatically)
        """
        self.tcp_tp_config = value  # Delegates to property setter
        return self

    def getUri(self) -> UriString:
        """
        AUTOSAR-compliant getter for uri.

        Returns:
            The uri value

        Note:
            Delegates to uri property (CODING_RULE_V2_00017)
        """
        return self.uri  # Delegates to property

    def setUri(self, value: UriString) -> HttpTp:
        """
        AUTOSAR-compliant setter for uri with method chaining.

        Args:
            value: The uri to set

        Returns:
            self for method chaining

        Note:
            Delegates to uri property setter (gets validation automatically)
        """
        self.uri = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_content_type(self, value: Optional[String]) -> HttpTp:
        """
        Set contentType and return self for chaining.

        Args:
            value: The contentType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_content_type("value")
        """
        self.content_type = value  # Use property setter (gets validation)
        return self

    def with_protocol_version(self, value: Optional[String]) -> HttpTp:
        """
        Set protocolVersion and return self for chaining.

        Args:
            value: The protocolVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_protocol_version("value")
        """
        self.protocol_version = value  # Use property setter (gets validation)
        return self

    def with_request_method(self, value: Optional[RequestMethodEnum]) -> HttpTp:
        """
        Set requestMethod and return self for chaining.

        Args:
            value: The requestMethod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request_method("value")
        """
        self.request_method = value  # Use property setter (gets validation)
        return self

    def with_tcp_tp_config(self, value: Optional[TcpTp]) -> HttpTp:
        """
        Set tcpTpConfig and return self for chaining.

        Args:
            value: The tcpTpConfig to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_tp_config("value")
        """
        self.tcp_tp_config = value  # Use property setter (gets validation)
        return self

    def with_uri(self, value: Optional[UriString]) -> HttpTp:
        """
        Set uri and return self for chaining.

        Args:
            value: The uri to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uri("value")
        """
        self.uri = value  # Use property setter (gets validation)
        return self



class Ipv4Configuration(NetworkEndpointAddress):
    """
    Internet Protocol version 4 (IPv4) configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv4Configuration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 465, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Priority of assignment (1 is highest).
        # If a new address an assignment method with a higher priority is overwrites
                # the IP address previously assigned assignment method with a lower priority.
        self._assignment: Optional[PositiveInteger] = None

    @property
    def assignment(self) -> Optional[PositiveInteger]:
        """Get assignment (Pythonic accessor)."""
        return self._assignment

    @assignment.setter
    def assignment(self, value: Optional[PositiveInteger]) -> None:
        """
        Set assignment with validation.

        Args:
            value: The assignment to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._assignment = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"assignment must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._assignment = value
        self._defaultGateway: Optional[Ip4AddressString] = None

    @property
    def default_gateway(self) -> Optional[Ip4AddressString]:
        """Get defaultGateway (Pythonic accessor)."""
        return self._defaultGateway

    @default_gateway.setter
    def default_gateway(self, value: Optional[Ip4AddressString]) -> None:
        """
        Set defaultGateway with validation.

        Args:
            value: The defaultGateway to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultGateway = None
            return

        if not isinstance(value, Ip4AddressString):
            raise TypeError(
                f"defaultGateway must be Ip4AddressString or None, got {type(value).__name__}"
            )
        self._defaultGateway = value
        # xml.
        # namePlural=DNS-SERVER-ADDRESSES.
        self._dnsServer: List[Ip4AddressString] = []

    @property
    def dns_server(self) -> List[Ip4AddressString]:
        """Get dnsServer (Pythonic accessor)."""
        return self._dnsServer
        # Defines the lifetime of a dynamically fetched IP address.
        self._ipAddressKeep: Optional[IpAddressKeepEnum] = None

    @property
    def ip_address_keep(self) -> Optional[IpAddressKeepEnum]:
        """Get ipAddressKeep (Pythonic accessor)."""
        return self._ipAddressKeep

    @ip_address_keep.setter
    def ip_address_keep(self, value: Optional[IpAddressKeepEnum]) -> None:
        """
        Set ipAddressKeep with validation.

        Args:
            value: The ipAddressKeep to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipAddressKeep = None
            return

        if not isinstance(value, IpAddressKeepEnum):
            raise TypeError(
                f"ipAddressKeep must be IpAddressKeepEnum or None, got {type(value).__name__}"
            )
        self._ipAddressKeep = value
        self._ipv4Address: Optional[Ipv4AddressSourceEnum] = None

    @property
    def ipv4_address(self) -> Optional[Ipv4AddressSourceEnum]:
        """Get ipv4Address (Pythonic accessor)."""
        return self._ipv4Address

    @ipv4_address.setter
    def ipv4_address(self, value: Optional[Ipv4AddressSourceEnum]) -> None:
        """
        Set ipv4Address with validation.

        Args:
            value: The ipv4Address to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv4Address = None
            return

        if not isinstance(value, Ipv4AddressSource):
            raise TypeError(
                f"ipv4Address must be Ipv4AddressSource or None, got {type(value).__name__}"
            )
        self._ipv4Address = value
        # Network mask.
        # Notation 255.
        # 255.
        # 255.
        # 255.
        self._networkMask: Optional[Ip4AddressString] = None

    @property
    def network_mask(self) -> Optional[Ip4AddressString]:
        """Get networkMask (Pythonic accessor)."""
        return self._networkMask

    @network_mask.setter
    def network_mask(self, value: Optional[Ip4AddressString]) -> None:
        """
        Set networkMask with validation.

        Args:
            value: The networkMask to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._networkMask = None
            return

        if not isinstance(value, Ip4AddressString):
            raise TypeError(
                f"networkMask must be Ip4AddressString or None, got {type(value).__name__}"
            )
        self._networkMask = value
        # 255).
        # The purpose of the TimeToLive to avoid a situation in which an undeliverable
                # circulating on a system.
        self._ttl: Optional[PositiveInteger] = None

    @property
    def ttl(self) -> Optional[PositiveInteger]:
        """Get ttl (Pythonic accessor)."""
        return self._ttl

    @ttl.setter
    def ttl(self, value: Optional[PositiveInteger]) -> None:
        """
        Set ttl with validation.

        Args:
            value: The ttl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ttl = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"ttl must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._ttl = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssignment(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for assignment.

        Returns:
            The assignment value

        Note:
            Delegates to assignment property (CODING_RULE_V2_00017)
        """
        return self.assignment  # Delegates to property

    def setAssignment(self, value: PositiveInteger) -> Ipv4Configuration:
        """
        AUTOSAR-compliant setter for assignment with method chaining.

        Args:
            value: The assignment to set

        Returns:
            self for method chaining

        Note:
            Delegates to assignment property setter (gets validation automatically)
        """
        self.assignment = value  # Delegates to property setter
        return self

    def getDefaultGateway(self) -> Ip4AddressString:
        """
        AUTOSAR-compliant getter for defaultGateway.

        Returns:
            The defaultGateway value

        Note:
            Delegates to default_gateway property (CODING_RULE_V2_00017)
        """
        return self.default_gateway  # Delegates to property

    def setDefaultGateway(self, value: Ip4AddressString) -> Ipv4Configuration:
        """
        AUTOSAR-compliant setter for defaultGateway with method chaining.

        Args:
            value: The defaultGateway to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_gateway property setter (gets validation automatically)
        """
        self.default_gateway = value  # Delegates to property setter
        return self

    def getDnsServer(self) -> List[Ip4AddressString]:
        """
        AUTOSAR-compliant getter for dnsServer.

        Returns:
            The dnsServer value

        Note:
            Delegates to dns_server property (CODING_RULE_V2_00017)
        """
        return self.dns_server  # Delegates to property

    def getIpAddressKeep(self) -> IpAddressKeepEnum:
        """
        AUTOSAR-compliant getter for ipAddressKeep.

        Returns:
            The ipAddressKeep value

        Note:
            Delegates to ip_address_keep property (CODING_RULE_V2_00017)
        """
        return self.ip_address_keep  # Delegates to property

    def setIpAddressKeep(self, value: IpAddressKeepEnum) -> Ipv4Configuration:
        """
        AUTOSAR-compliant setter for ipAddressKeep with method chaining.

        Args:
            value: The ipAddressKeep to set

        Returns:
            self for method chaining

        Note:
            Delegates to ip_address_keep property setter (gets validation automatically)
        """
        self.ip_address_keep = value  # Delegates to property setter
        return self

    def getIpv4Address(self) -> Ipv4AddressSourceEnum:
        """
        AUTOSAR-compliant getter for ipv4Address.

        Returns:
            The ipv4Address value

        Note:
            Delegates to ipv4_address property (CODING_RULE_V2_00017)
        """
        return self.ipv4_address  # Delegates to property

    def setIpv4Address(self, value: Ipv4AddressSourceEnum) -> Ipv4Configuration:
        """
        AUTOSAR-compliant setter for ipv4Address with method chaining.

        Args:
            value: The ipv4Address to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv4_address property setter (gets validation automatically)
        """
        self.ipv4_address = value  # Delegates to property setter
        return self

    def getNetworkMask(self) -> Ip4AddressString:
        """
        AUTOSAR-compliant getter for networkMask.

        Returns:
            The networkMask value

        Note:
            Delegates to network_mask property (CODING_RULE_V2_00017)
        """
        return self.network_mask  # Delegates to property

    def setNetworkMask(self, value: Ip4AddressString) -> Ipv4Configuration:
        """
        AUTOSAR-compliant setter for networkMask with method chaining.

        Args:
            value: The networkMask to set

        Returns:
            self for method chaining

        Note:
            Delegates to network_mask property setter (gets validation automatically)
        """
        self.network_mask = value  # Delegates to property setter
        return self

    def getTtl(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for ttl.

        Returns:
            The ttl value

        Note:
            Delegates to ttl property (CODING_RULE_V2_00017)
        """
        return self.ttl  # Delegates to property

    def setTtl(self, value: PositiveInteger) -> Ipv4Configuration:
        """
        AUTOSAR-compliant setter for ttl with method chaining.

        Args:
            value: The ttl to set

        Returns:
            self for method chaining

        Note:
            Delegates to ttl property setter (gets validation automatically)
        """
        self.ttl = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_assignment(self, value: Optional[PositiveInteger]) -> Ipv4Configuration:
        """
        Set assignment and return self for chaining.

        Args:
            value: The assignment to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assignment("value")
        """
        self.assignment = value  # Use property setter (gets validation)
        return self

    def with_default_gateway(self, value: Optional[Ip4AddressString]) -> Ipv4Configuration:
        """
        Set defaultGateway and return self for chaining.

        Args:
            value: The defaultGateway to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_gateway("value")
        """
        self.default_gateway = value  # Use property setter (gets validation)
        return self

    def with_ip_address_keep(self, value: Optional[IpAddressKeepEnum]) -> Ipv4Configuration:
        """
        Set ipAddressKeep and return self for chaining.

        Args:
            value: The ipAddressKeep to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ip_address_keep("value")
        """
        self.ip_address_keep = value  # Use property setter (gets validation)
        return self

    def with_ipv4_address(self, value: Optional[Ipv4AddressSourceEnum]) -> Ipv4Configuration:
        """
        Set ipv4Address and return self for chaining.

        Args:
            value: The ipv4Address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv4_address("value")
        """
        self.ipv4_address = value  # Use property setter (gets validation)
        return self

    def with_network_mask(self, value: Optional[Ip4AddressString]) -> Ipv4Configuration:
        """
        Set networkMask and return self for chaining.

        Args:
            value: The networkMask to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network_mask("value")
        """
        self.network_mask = value  # Use property setter (gets validation)
        return self

    def with_ttl(self, value: Optional[PositiveInteger]) -> Ipv4Configuration:
        """
        Set ttl and return self for chaining.

        Args:
            value: The ttl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ttl("value")
        """
        self.ttl = value  # Use property setter (gets validation)
        return self



class Ipv6Configuration(NetworkEndpointAddress):
    """
    Internet Protocol version 6 (IPv6) configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv6Configuration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 466, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Priority of assignment (1 is highest).
        # If a new address an assignment method with a higher priority is overwrites
                # the IP address previously assigned assignment method with a lower priority.
        self._assignment: Optional[PositiveInteger] = None

    @property
    def assignment(self) -> Optional[PositiveInteger]:
        """Get assignment (Pythonic accessor)."""
        return self._assignment

    @assignment.setter
    def assignment(self, value: Optional[PositiveInteger]) -> None:
        """
        Set assignment with validation.

        Args:
            value: The assignment to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._assignment = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"assignment must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._assignment = value
        self._defaultRouter: Optional[Ip6AddressString] = None

    @property
    def default_router(self) -> Optional[Ip6AddressString]:
        """Get defaultRouter (Pythonic accessor)."""
        return self._defaultRouter

    @default_router.setter
    def default_router(self, value: Optional[Ip6AddressString]) -> None:
        """
        Set defaultRouter with validation.

        Args:
            value: The defaultRouter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultRouter = None
            return

        if not isinstance(value, Ip6AddressString):
            raise TypeError(
                f"defaultRouter must be Ip6AddressString or None, got {type(value).__name__}"
            )
        self._defaultRouter = value
        # xml.
        # namePlural=DNS-SERVER-ADDRESSES.
        self._dnsServer: List[Ip6AddressString] = []

    @property
    def dns_server(self) -> List[Ip6AddressString]:
        """Get dnsServer (Pythonic accessor)."""
        return self._dnsServer
        # This attribute is used to enable anycast addressing (i.
        # e.
        # to multiple receivers).
        self._enableAnycast: Optional[Boolean] = None

    @property
    def enable_anycast(self) -> Optional[Boolean]:
        """Get enableAnycast (Pythonic accessor)."""
        return self._enableAnycast

    @enable_anycast.setter
    def enable_anycast(self, value: Optional[Boolean]) -> None:
        """
        Set enableAnycast with validation.

        Args:
            value: The enableAnycast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enableAnycast = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"enableAnycast must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._enableAnycast = value
        # The hop count n means gateways separate the source host from the (Range 0.
        # 255).
        self._hopCount: Optional[PositiveInteger] = None

    @property
    def hop_count(self) -> Optional[PositiveInteger]:
        """Get hopCount (Pythonic accessor)."""
        return self._hopCount

    @hop_count.setter
    def hop_count(self, value: Optional[PositiveInteger]) -> None:
        """
        Set hopCount with validation.

        Args:
            value: The hopCount to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hopCount = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"hopCount must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._hopCount = value
        self._ipAddressKeep: Optional[IpAddressKeepEnum] = None

    @property
    def ip_address_keep(self) -> Optional[IpAddressKeepEnum]:
        """Get ipAddressKeep (Pythonic accessor)."""
        return self._ipAddressKeep

    @ip_address_keep.setter
    def ip_address_keep(self, value: Optional[IpAddressKeepEnum]) -> None:
        """
        Set ipAddressKeep with validation.

        Args:
            value: The ipAddressKeep to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipAddressKeep = None
            return

        if not isinstance(value, IpAddressKeepEnum):
            raise TypeError(
                f"ipAddressKeep must be IpAddressKeepEnum or None, got {type(value).__name__}"
            )
        self._ipAddressKeep = value
        # prefix.
        self._ipAddressPrefix: Optional[PositiveInteger] = None

    @property
    def ip_address_prefix(self) -> Optional[PositiveInteger]:
        """Get ipAddressPrefix (Pythonic accessor)."""
        return self._ipAddressPrefix

    @ip_address_prefix.setter
    def ip_address_prefix(self, value: Optional[PositiveInteger]) -> None:
        """
        Set ipAddressPrefix with validation.

        Args:
            value: The ipAddressPrefix to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipAddressPrefix = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"ipAddressPrefix must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._ipAddressPrefix = value
        self._ipv6Address: Optional[Ipv6AddressSourceEnum] = None

    @property
    def ipv6_address(self) -> Optional[Ipv6AddressSourceEnum]:
        """Get ipv6Address (Pythonic accessor)."""
        return self._ipv6Address

    @ipv6_address.setter
    def ipv6_address(self, value: Optional[Ipv6AddressSourceEnum]) -> None:
        """
        Set ipv6Address with validation.

        Args:
            value: The ipv6Address to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv6Address = None
            return

        if not isinstance(value, Ipv6AddressSource):
            raise TypeError(
                f"ipv6Address must be Ipv6AddressSource or None, got {type(value).__name__}"
            )
        self._ipv6Address = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssignment(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for assignment.

        Returns:
            The assignment value

        Note:
            Delegates to assignment property (CODING_RULE_V2_00017)
        """
        return self.assignment  # Delegates to property

    def setAssignment(self, value: PositiveInteger) -> Ipv6Configuration:
        """
        AUTOSAR-compliant setter for assignment with method chaining.

        Args:
            value: The assignment to set

        Returns:
            self for method chaining

        Note:
            Delegates to assignment property setter (gets validation automatically)
        """
        self.assignment = value  # Delegates to property setter
        return self

    def getDefaultRouter(self) -> Ip6AddressString:
        """
        AUTOSAR-compliant getter for defaultRouter.

        Returns:
            The defaultRouter value

        Note:
            Delegates to default_router property (CODING_RULE_V2_00017)
        """
        return self.default_router  # Delegates to property

    def setDefaultRouter(self, value: Ip6AddressString) -> Ipv6Configuration:
        """
        AUTOSAR-compliant setter for defaultRouter with method chaining.

        Args:
            value: The defaultRouter to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_router property setter (gets validation automatically)
        """
        self.default_router = value  # Delegates to property setter
        return self

    def getDnsServer(self) -> List[Ip6AddressString]:
        """
        AUTOSAR-compliant getter for dnsServer.

        Returns:
            The dnsServer value

        Note:
            Delegates to dns_server property (CODING_RULE_V2_00017)
        """
        return self.dns_server  # Delegates to property

    def getEnableAnycast(self) -> Boolean:
        """
        AUTOSAR-compliant getter for enableAnycast.

        Returns:
            The enableAnycast value

        Note:
            Delegates to enable_anycast property (CODING_RULE_V2_00017)
        """
        return self.enable_anycast  # Delegates to property

    def setEnableAnycast(self, value: Boolean) -> Ipv6Configuration:
        """
        AUTOSAR-compliant setter for enableAnycast with method chaining.

        Args:
            value: The enableAnycast to set

        Returns:
            self for method chaining

        Note:
            Delegates to enable_anycast property setter (gets validation automatically)
        """
        self.enable_anycast = value  # Delegates to property setter
        return self

    def getHopCount(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for hopCount.

        Returns:
            The hopCount value

        Note:
            Delegates to hop_count property (CODING_RULE_V2_00017)
        """
        return self.hop_count  # Delegates to property

    def setHopCount(self, value: PositiveInteger) -> Ipv6Configuration:
        """
        AUTOSAR-compliant setter for hopCount with method chaining.

        Args:
            value: The hopCount to set

        Returns:
            self for method chaining

        Note:
            Delegates to hop_count property setter (gets validation automatically)
        """
        self.hop_count = value  # Delegates to property setter
        return self

    def getIpAddressKeep(self) -> IpAddressKeepEnum:
        """
        AUTOSAR-compliant getter for ipAddressKeep.

        Returns:
            The ipAddressKeep value

        Note:
            Delegates to ip_address_keep property (CODING_RULE_V2_00017)
        """
        return self.ip_address_keep  # Delegates to property

    def setIpAddressKeep(self, value: IpAddressKeepEnum) -> Ipv6Configuration:
        """
        AUTOSAR-compliant setter for ipAddressKeep with method chaining.

        Args:
            value: The ipAddressKeep to set

        Returns:
            self for method chaining

        Note:
            Delegates to ip_address_keep property setter (gets validation automatically)
        """
        self.ip_address_keep = value  # Delegates to property setter
        return self

    def getIpAddressPrefix(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for ipAddressPrefix.

        Returns:
            The ipAddressPrefix value

        Note:
            Delegates to ip_address_prefix property (CODING_RULE_V2_00017)
        """
        return self.ip_address_prefix  # Delegates to property

    def setIpAddressPrefix(self, value: PositiveInteger) -> Ipv6Configuration:
        """
        AUTOSAR-compliant setter for ipAddressPrefix with method chaining.

        Args:
            value: The ipAddressPrefix to set

        Returns:
            self for method chaining

        Note:
            Delegates to ip_address_prefix property setter (gets validation automatically)
        """
        self.ip_address_prefix = value  # Delegates to property setter
        return self

    def getIpv6Address(self) -> Ipv6AddressSourceEnum:
        """
        AUTOSAR-compliant getter for ipv6Address.

        Returns:
            The ipv6Address value

        Note:
            Delegates to ipv6_address property (CODING_RULE_V2_00017)
        """
        return self.ipv6_address  # Delegates to property

    def setIpv6Address(self, value: Ipv6AddressSourceEnum) -> Ipv6Configuration:
        """
        AUTOSAR-compliant setter for ipv6Address with method chaining.

        Args:
            value: The ipv6Address to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv6_address property setter (gets validation automatically)
        """
        self.ipv6_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_assignment(self, value: Optional[PositiveInteger]) -> Ipv6Configuration:
        """
        Set assignment and return self for chaining.

        Args:
            value: The assignment to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assignment("value")
        """
        self.assignment = value  # Use property setter (gets validation)
        return self

    def with_default_router(self, value: Optional[Ip6AddressString]) -> Ipv6Configuration:
        """
        Set defaultRouter and return self for chaining.

        Args:
            value: The defaultRouter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_router("value")
        """
        self.default_router = value  # Use property setter (gets validation)
        return self

    def with_enable_anycast(self, value: Optional[Boolean]) -> Ipv6Configuration:
        """
        Set enableAnycast and return self for chaining.

        Args:
            value: The enableAnycast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enable_anycast("value")
        """
        self.enable_anycast = value  # Use property setter (gets validation)
        return self

    def with_hop_count(self, value: Optional[PositiveInteger]) -> Ipv6Configuration:
        """
        Set hopCount and return self for chaining.

        Args:
            value: The hopCount to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_hop_count("value")
        """
        self.hop_count = value  # Use property setter (gets validation)
        return self

    def with_ip_address_keep(self, value: Optional[IpAddressKeepEnum]) -> Ipv6Configuration:
        """
        Set ipAddressKeep and return self for chaining.

        Args:
            value: The ipAddressKeep to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ip_address_keep("value")
        """
        self.ip_address_keep = value  # Use property setter (gets validation)
        return self

    def with_ip_address_prefix(self, value: Optional[PositiveInteger]) -> Ipv6Configuration:
        """
        Set ipAddressPrefix and return self for chaining.

        Args:
            value: The ipAddressPrefix to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ip_address_prefix("value")
        """
        self.ip_address_prefix = value  # Use property setter (gets validation)
        return self

    def with_ipv6_address(self, value: Optional[Ipv6AddressSourceEnum]) -> Ipv6Configuration:
        """
        Set ipv6Address and return self for chaining.

        Args:
            value: The ipv6Address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv6_address("value")
        """
        self.ipv6_address = value  # Use property setter (gets validation)
        return self



class MacMulticastConfiguration(NetworkEndpointAddress):
    """
    References a per cluster globally defined MAC-Multicast-Group.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::MacMulticastConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 467, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a macMulticastGroup.
        self._macMulticastGroup: Optional[RefType] = None

    @property
    def mac_multicast_group(self) -> Optional[RefType]:
        """Get macMulticastGroup (Pythonic accessor)."""
        return self._macMulticastGroup

    @mac_multicast_group.setter
    def mac_multicast_group(self, value: Optional[RefType]) -> None:
        """
        Set macMulticastGroup with validation.

        Args:
            value: The macMulticastGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macMulticastGroup = None
            return

        self._macMulticastGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMacMulticastGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for macMulticastGroup.

        Returns:
            The macMulticastGroup value

        Note:
            Delegates to mac_multicast_group property (CODING_RULE_V2_00017)
        """
        return self.mac_multicast_group  # Delegates to property

    def setMacMulticastGroup(self, value: RefType) -> MacMulticastConfiguration:
        """
        AUTOSAR-compliant setter for macMulticastGroup with method chaining.

        Args:
            value: The macMulticastGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to mac_multicast_group property setter (gets validation automatically)
        """
        self.mac_multicast_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mac_multicast_group(self, value: Optional[RefType]) -> MacMulticastConfiguration:
        """
        Set macMulticastGroup and return self for chaining.

        Args:
            value: The macMulticastGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mac_multicast_group("value")
        """
        self.mac_multicast_group = value  # Use property setter (gets validation)
        return self



class UdpTp(TcpUdpConfig):
    """
    Content Model for UDP configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::UdpTp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 459, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Udp Port configuration.
        self._udpTpPort: Optional[TpPort] = None

    @property
    def udp_tp_port(self) -> Optional[TpPort]:
        """Get udpTpPort (Pythonic accessor)."""
        return self._udpTpPort

    @udp_tp_port.setter
    def udp_tp_port(self, value: Optional[TpPort]) -> None:
        """
        Set udpTpPort with validation.

        Args:
            value: The udpTpPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._udpTpPort = None
            return

        if not isinstance(value, TpPort):
            raise TypeError(
                f"udpTpPort must be TpPort or None, got {type(value).__name__}"
            )
        self._udpTpPort = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getUdpTpPort(self) -> TpPort:
        """
        AUTOSAR-compliant getter for udpTpPort.

        Returns:
            The udpTpPort value

        Note:
            Delegates to udp_tp_port property (CODING_RULE_V2_00017)
        """
        return self.udp_tp_port  # Delegates to property

    def setUdpTpPort(self, value: TpPort) -> UdpTp:
        """
        AUTOSAR-compliant setter for udpTpPort with method chaining.

        Args:
            value: The udpTpPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to udp_tp_port property setter (gets validation automatically)
        """
        self.udp_tp_port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_udp_tp_port(self, value: Optional[TpPort]) -> UdpTp:
        """
        Set udpTpPort and return self for chaining.

        Args:
            value: The udpTpPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_udp_tp_port("value")
        """
        self.udp_tp_port = value  # Use property setter (gets validation)
        return self



class TcpTp(TcpUdpConfig):
    """
    Content Model for TCP configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TcpTp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 460, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum number of times that TCP retransmits an data segment before aborting
        # the connection.
        self._keepAlive: Optional[PositiveInteger] = None

    @property
    def keep_alive(self) -> Optional[PositiveInteger]:
        """Get keepAlive (Pythonic accessor)."""
        return self._keepAlive

    @keep_alive.setter
    def keep_alive(self, value: Optional[PositiveInteger]) -> None:
        """
        Set keepAlive with validation.

        Args:
            value: The keepAlive to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keepAlive = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"keepAlive must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._keepAlive = value
        self._keepAlives: Optional[Boolean] = None

    @property
    def keep_alives(self) -> Optional[Boolean]:
        """Get keepAlives (Pythonic accessor)."""
        return self._keepAlives

    @keep_alives.setter
    def keep_alives(self, value: Optional[Boolean]) -> None:
        """
        Set keepAlives with validation.

        Args:
            value: The keepAlives to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keepAlives = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"keepAlives must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._keepAlives = value
        # probe.
        self._keepAliveTime: Optional[TimeValue] = None

    @property
    def keep_alive_time(self) -> Optional[TimeValue]:
        """Get keepAliveTime (Pythonic accessor)."""
        return self._keepAliveTime

    @keep_alive_time.setter
    def keep_alive_time(self, value: Optional[TimeValue]) -> None:
        """
        Set keepAliveTime with validation.

        Args:
            value: The keepAliveTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keepAliveTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"keepAliveTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._keepAliveTime = value
        self._naglesAlgorithm: Optional[Boolean] = None

    @property
    def nagles_algorithm(self) -> Optional[Boolean]:
        """Get naglesAlgorithm (Pythonic accessor)."""
        return self._naglesAlgorithm

    @nagles_algorithm.setter
    def nagles_algorithm(self, value: Optional[Boolean]) -> None:
        """
        Set naglesAlgorithm with validation.

        Args:
            value: The naglesAlgorithm to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._naglesAlgorithm = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"naglesAlgorithm must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._naglesAlgorithm = value
        self._receiveWindowMin: Optional[PositiveInteger] = None

    @property
    def receive_window_min(self) -> Optional[PositiveInteger]:
        """Get receiveWindowMin (Pythonic accessor)."""
        return self._receiveWindowMin

    @receive_window_min.setter
    def receive_window_min(self, value: Optional[PositiveInteger]) -> None:
        """
        Set receiveWindowMin with validation.

        Args:
            value: The receiveWindowMin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._receiveWindowMin = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"receiveWindowMin must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._receiveWindowMin = value
        # If the tcp is not defined or set to "INF", no shall be re-transmitted.
        self._tcp: Optional[TimeValue] = None

    @property
    def tcp(self) -> Optional[TimeValue]:
        """Get tcp (Pythonic accessor)."""
        return self._tcp

    @tcp.setter
    def tcp(self, value: Optional[TimeValue]) -> None:
        """
        Set tcp with validation.

        Args:
            value: The tcp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcp = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcp must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcp = value
        self._tcpTpPort: Optional[TpPort] = None

    @property
    def tcp_tp_port(self) -> Optional[TpPort]:
        """Get tcpTpPort (Pythonic accessor)."""
        return self._tcpTpPort

    @tcp_tp_port.setter
    def tcp_tp_port(self, value: Optional[TpPort]) -> None:
        """
        Set tcpTpPort with validation.

        Args:
            value: The tcpTpPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpTpPort = None
            return

        if not isinstance(value, TpPort):
            raise TypeError(
                f"tcpTpPort must be TpPort or None, got {type(value).__name__}"
            )
        self._tcpTpPort = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getKeepAlive(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for keepAlive.

        Returns:
            The keepAlive value

        Note:
            Delegates to keep_alive property (CODING_RULE_V2_00017)
        """
        return self.keep_alive  # Delegates to property

    def setKeepAlive(self, value: PositiveInteger) -> TcpTp:
        """
        AUTOSAR-compliant setter for keepAlive with method chaining.

        Args:
            value: The keepAlive to set

        Returns:
            self for method chaining

        Note:
            Delegates to keep_alive property setter (gets validation automatically)
        """
        self.keep_alive = value  # Delegates to property setter
        return self

    def getKeepAlives(self) -> Boolean:
        """
        AUTOSAR-compliant getter for keepAlives.

        Returns:
            The keepAlives value

        Note:
            Delegates to keep_alives property (CODING_RULE_V2_00017)
        """
        return self.keep_alives  # Delegates to property

    def setKeepAlives(self, value: Boolean) -> TcpTp:
        """
        AUTOSAR-compliant setter for keepAlives with method chaining.

        Args:
            value: The keepAlives to set

        Returns:
            self for method chaining

        Note:
            Delegates to keep_alives property setter (gets validation automatically)
        """
        self.keep_alives = value  # Delegates to property setter
        return self

    def getKeepAliveTime(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for keepAliveTime.

        Returns:
            The keepAliveTime value

        Note:
            Delegates to keep_alive_time property (CODING_RULE_V2_00017)
        """
        return self.keep_alive_time  # Delegates to property

    def setKeepAliveTime(self, value: TimeValue) -> TcpTp:
        """
        AUTOSAR-compliant setter for keepAliveTime with method chaining.

        Args:
            value: The keepAliveTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to keep_alive_time property setter (gets validation automatically)
        """
        self.keep_alive_time = value  # Delegates to property setter
        return self

    def getNaglesAlgorithm(self) -> Boolean:
        """
        AUTOSAR-compliant getter for naglesAlgorithm.

        Returns:
            The naglesAlgorithm value

        Note:
            Delegates to nagles_algorithm property (CODING_RULE_V2_00017)
        """
        return self.nagles_algorithm  # Delegates to property

    def setNaglesAlgorithm(self, value: Boolean) -> TcpTp:
        """
        AUTOSAR-compliant setter for naglesAlgorithm with method chaining.

        Args:
            value: The naglesAlgorithm to set

        Returns:
            self for method chaining

        Note:
            Delegates to nagles_algorithm property setter (gets validation automatically)
        """
        self.nagles_algorithm = value  # Delegates to property setter
        return self

    def getReceiveWindowMin(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for receiveWindowMin.

        Returns:
            The receiveWindowMin value

        Note:
            Delegates to receive_window_min property (CODING_RULE_V2_00017)
        """
        return self.receive_window_min  # Delegates to property

    def setReceiveWindowMin(self, value: PositiveInteger) -> TcpTp:
        """
        AUTOSAR-compliant setter for receiveWindowMin with method chaining.

        Args:
            value: The receiveWindowMin to set

        Returns:
            self for method chaining

        Note:
            Delegates to receive_window_min property setter (gets validation automatically)
        """
        self.receive_window_min = value  # Delegates to property setter
        return self

    def getTcp(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for tcp.

        Returns:
            The tcp value

        Note:
            Delegates to tcp property (CODING_RULE_V2_00017)
        """
        return self.tcp  # Delegates to property

    def setTcp(self, value: TimeValue) -> TcpTp:
        """
        AUTOSAR-compliant setter for tcp with method chaining.

        Args:
            value: The tcp to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp property setter (gets validation automatically)
        """
        self.tcp = value  # Delegates to property setter
        return self

    def getTcpTpPort(self) -> TpPort:
        """
        AUTOSAR-compliant getter for tcpTpPort.

        Returns:
            The tcpTpPort value

        Note:
            Delegates to tcp_tp_port property (CODING_RULE_V2_00017)
        """
        return self.tcp_tp_port  # Delegates to property

    def setTcpTpPort(self, value: TpPort) -> TcpTp:
        """
        AUTOSAR-compliant setter for tcpTpPort with method chaining.

        Args:
            value: The tcpTpPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_tp_port property setter (gets validation automatically)
        """
        self.tcp_tp_port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_keep_alive(self, value: Optional[PositiveInteger]) -> TcpTp:
        """
        Set keepAlive and return self for chaining.

        Args:
            value: The keepAlive to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_keep_alive("value")
        """
        self.keep_alive = value  # Use property setter (gets validation)
        return self

    def with_keep_alives(self, value: Optional[Boolean]) -> TcpTp:
        """
        Set keepAlives and return self for chaining.

        Args:
            value: The keepAlives to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_keep_alives("value")
        """
        self.keep_alives = value  # Use property setter (gets validation)
        return self

    def with_keep_alive_time(self, value: Optional[TimeValue]) -> TcpTp:
        """
        Set keepAliveTime and return self for chaining.

        Args:
            value: The keepAliveTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_keep_alive_time("value")
        """
        self.keep_alive_time = value  # Use property setter (gets validation)
        return self

    def with_nagles_algorithm(self, value: Optional[Boolean]) -> TcpTp:
        """
        Set naglesAlgorithm and return self for chaining.

        Args:
            value: The naglesAlgorithm to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nagles_algorithm("value")
        """
        self.nagles_algorithm = value  # Use property setter (gets validation)
        return self

    def with_receive_window_min(self, value: Optional[PositiveInteger]) -> TcpTp:
        """
        Set receiveWindowMin and return self for chaining.

        Args:
            value: The receiveWindowMin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_receive_window_min("value")
        """
        self.receive_window_min = value  # Use property setter (gets validation)
        return self

    def with_tcp(self, value: Optional[TimeValue]) -> TcpTp:
        """
        Set tcp and return self for chaining.

        Args:
            value: The tcp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp("value")
        """
        self.tcp = value  # Use property setter (gets validation)
        return self

    def with_tcp_tp_port(self, value: Optional[TpPort]) -> TcpTp:
        """
        Set tcpTpPort and return self for chaining.

        Args:
            value: The tcpTpPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_tp_port("value")
        """
        self.tcp_tp_port = value  # Use property setter (gets validation)
        return self


class CouplingElementEnum(AREnum):
    """
    CouplingElementEnum enumeration

Identifies the Coupling type. Aggregated by CouplingElement.couplingType

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # A device that is used to connect segments of a LAN. In Hubs frames are "broadcasted" to every one of its ports.
    hub = "0"

    # A device that routes frames between different networks.
    router = "1"

    # A device that filters and forwards frames between different LAN segments.
    switch = "2"



class EthernetConnectionNegotiationEnum(AREnum):
    """
    EthernetConnectionNegotiationEnum enumeration

Specifies connection negotiation types of Ethernet transceiver links. Aggregated by CouplingPort.connectionNegotiationBehavior

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # Automatic Negotiation
    auto = "0"

    # Master
    master = "1"

    # Slave
    slave = "2"



class EthernetMacLayerTypeEnum(AREnum):
    """
    EthernetMacLayerTypeEnum enumeration

Specifies MAC (Media Access Control) Layer types. Aggregated by CouplingPort.macLayerType, EthernetCommunicationController.macLayerType

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # Mac layer interface (data) bandwith class 1Gbit/s (e.g. GMII, RGMII, SGMII, RvGMII, USGMII)
    xGMII = "1"

    # Mac layer interface (data) bandwith class 100Mbit/s and 10Mbit/s (e.g. RMII, RvMII, SMII, RvMII)
    xMII = "0"

    # Mac layer interface (data) bandwith class 10Gbit/s
    xXGMII = "2"



class EthernetPhysicalLayerTypeEnum(AREnum):
    """
    EthernetPhysicalLayerTypeEnum enumeration

Specifies physical layer types of Ethernet transceiver links. Aggregated by CouplingPort.physicalLayerType

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # Ethernet Standard (IEEE 802.3ab) to support 1Gbit/s over 4 twisted pairs.
    _1000BASE_T = "6"

    # Ethernet Standard (IEEE 802.3bp) to support 1Gbit/s over a single twisted pair cable.
    _1000BASE_T1 = "8"

    # Ethernet Standard (IEEE 802.3bw) to support 100Mbit/s over a single twisted pair cable.
    _100BASE_T1 = "7"

    # Ethernet Standard (IEEE 802.3u) to support 100Mbit/s over two twisted pairs.
    _100BASE_TX = "5"

    # Physical layer interface 10BASE-T1S (10Mbit/s, 2 pairs). Used for automotive.
    _10BASE_T1S = "10"

    # Ethernet Standard (IEEE 802.11p) to support wireless communication in vehicular environments.
    iEEE802_11P = "9"



class EthernetSwitchVlanIngressTagEnum(AREnum):
    """
    EthernetSwitchVlanIngressTagEnum enumeration

Defines the possible tagging behavior at an ingress port. Aggregated by CouplingPort.receiveActivity

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # Drop if untagged.
    dropUntagged = "1"

    # Forward with the same VLAN as received. Also untagged frames will be forwarded as untagged.
    forwardAsIs = "0"



class EthernetCouplingPortSchedulerEnum(AREnum):
    """
    EthernetCouplingPortSchedulerEnum enumeration

Defines the schedule algorithm to be used. Aggregated by CouplingPortScheduler.portScheduler

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # Schedule algorithm "deficit round robin"
    deficitRoundRobin = "0"

    # Schedule algorithm "strict priority"
    strictPriority = "1"

    # Schedule algorithm "weighted round robin"
    weightedRoundRobin = "2"



class CouplingPortRatePolicyActionEnum(AREnum):
    """
    CouplingPortRatePolicyActionEnum enumeration

Defines the action to be performed when a rate policy is violated. Aggregated by CouplingPortRatePolicy.policyAction

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # If the rate policy is violated the CouplingPort this CouplingPortRatePolicy is defined on shall block all frames from the MAC-Address the violation was caused by.
    blockSource = "1"

    # If the rate policy is violated the frame shall be dropped.
    dropFrame = "0"



class EthernetSwitchVlanEgressTaggingEnum(AREnum):
    """
    EthernetSwitchVlanEgressTaggingEnum enumeration

Defines the VLAN tag sending behavior. Aggregated by VlanMembership.sendActivity

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # will not be sent sentTagged sent with its VLAN tag sentUntagged sent without a VLAN tag
    notSent = "2"



class SwitchStreamFilterActionPortModificationEnum(AREnum):
    """
    SwitchStreamFilterActionPortModificationEnum enumeration

Definition how the SwitchStreamFilterActionPortModification is applied. Tags: atp.Status=candidate Aggregated by SwitchStreamFilterActionDestPortModification.modification

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # Extend the egress destination of an Ethernet frame.
    extend = "0"

    # Overwrite the egress destination of an Ethernet frame.
    overwrite = "1"



class FlowMeteringColorModeEnum(AREnum):
    """
    FlowMeteringColorModeEnum enumeration

Defines whether Flow Metering color-aware or color-blind mode is used. Tags: atp.Status=candidate Aggregated by SwitchFlowMeteringEntry.colorMode

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # Flow Metering color aware mode.
    colorAware = "1"

    # Template
    System = "None"

    # CP R23-11
    AUTOSAR = "None"

    # Flow Metering color blind mode.
    colorBlind = "0"



class Ipv4AddressSourceEnum(AREnum):
    """
    Ipv4AddressSourceEnum enumeration

Defines how the node obtains its IPv4-Address. Aggregated by Ipv4Configuration.ipv4AddressSource

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # AutoIP is used to dynamically assign IP addresses at device startup.
    autoIp = "0"

    # Linklocal IPv4 Address Assignment using DoIP Parameters
    autoIp_doip = "2"

    # DHCP is a service for the automatic IP configuration of a client.
    dhcpv4 = "3"

    # The IP Address shall be declared manually.
    fixed = "4"



class IpAddressKeepEnum(AREnum):
    """
    IpAddressKeepEnum enumeration

Defines the behavior after a dynamic IP address has been assigned. Aggregated by Ipv4Configuration.ipAddressKeepBehavior, Ipv6Configuration.ipAddressKeepBehavior (cid:53) 465 of 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11 (cid:52)

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # After a dynamic IP address has been assigned just use it for this session.
    forget = "0"

    # After a dynamic IP address has been assigned store the address persistently.
    storePersistently = "1"



class Ipv6AddressSourceEnum(AREnum):
    """
    Ipv6AddressSourceEnum enumeration

Defines how the node obtains its IPv6-Address. Aggregated by Ipv6Configuration.ipv6AddressSource

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # DHCP is a service for the automatic IP configuration of a client.
    dhcpv6 = "0"

    # The IP Address shall be declared manually.
    fixed = "1"

    # LinkLocal is intended only for communications within the segment of a local network (a link) or a
    linkLocal = "2"

    # Linklocal IPv6 Address Assignment using DoIP Parameters
    linkLocal_doip = "3"

    # IPv6 Stateless Autoconfiguration.
    routerAdvertisement = "4"



class TimeSyncTechnologyEnum(AREnum):
    """
    TimeSyncTechnologyEnum enumeration

Timesynchronization. Server/Client configuration. Aggregated by TimeSyncClientConfiguration.timeSyncTechnology, TimeSyncServerConfiguration.timeSync Technology

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # Template
    System = "None"

    # CP R23-11
    AUTOSAR = "None"

    # Ethernet AVB compliant IEEE802.1AS Precision Time Protocol
    avb_ieee802_1AS = "0"

    # Network Time Protocol (NTP)
    ntp_rfc958 = "1"

    # Precision Time Protocol (PTP) IEEE 1588-2002
    ptp_ieee1588_2002 = "2"

    # Precision Time Protocol (PTP) IEEE 1588-2008
    ptp_ieee1588_2008 = "3"



class DoIpEntityRoleEnum(AREnum):
    """
    DoIpEntityRoleEnum enumeration

DoIP role a network-node has. Aggregated by DoIpEntity.doIpEntityRole

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # Network node is a DoIP gateway that accepts external connections.
    edgeNode = "0"

    # Network node is a Gateway between the DoIP network and other networks.
    gateway = "1"

    # Network node is a DoIp node.
    node = "2"



class CouplingPortRoleEnum(AREnum):
    """
    CouplingPortRoleEnum enumeration

Defines the role a CouplingPort takes in the context of a CouplingElement. Aggregated by CouplingPort.couplingPortRole

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology
    """
    # The hostPort is connected to an ECU (host ecu). The host ECU controls the connected Coupling
    hostPortElement = "0"

    # A CoupingPort can be a standardPort that is used to connect the CouplingElement with Coupling Ports outside the ECU.
    standardPort = "2"

    # A CouplingPort can be connected to another CouplingPort of a CouplingElement located on the same cascaded switch.
    upLinkPortECU = "1"
