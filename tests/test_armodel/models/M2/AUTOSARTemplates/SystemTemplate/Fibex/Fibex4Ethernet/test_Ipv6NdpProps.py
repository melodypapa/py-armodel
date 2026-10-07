"""
Test suite for Ipv6NdpProps (CP_TPS_SystemTemplate Table 3.108, p.151, R23-11).

Validates the member defaults, accessor round-trips, None no-ops, member order
and the verbatim class-level spec Note of the Ipv6NdpProps model class.
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import Ipv6NdpProps

CLASS_NOTE = "This meta-class specifies the configuration options for the Neighbor Discovery Protocol for IPv6."

MEMBER_ORDER = [
    "tcpIpNdpDefaultReachableTime",
    "tcpIpNdpDefaultRetransTimer",
    "tcpIpNdpDefaultRouterListSize",
    "tcpIpNdpDefensiveProcessing",
    "tcpIpNdpDelayFirstProbeTimeValue",
    "tcpIpNdpDestinationCacheSize",
    "tcpIpNdpDynamicHopLimitEnabled",
    "tcpIpNdpDynamicMtuEnabled",
    "tcpIpNdpDynamicReachableTimeEnabled",
    "tcpIpNdpDynamicRetransTimeEnabled",
    "tcpIpNdpMaxRandomFactor",
    "tcpIpNdpMaxRtrSolicitationDelay",
    "tcpIpNdpMaxRtrSolicitations",
    "tcpIpNdpMinRandomFactor",
    "tcpIpNdpNeighborUnreachabilityDetectionEnabled",
    "tcpIpNdpNumMulticastSolicitations",
    "tcpIpNdpNumUnicastSolicitations",
    "tcpIpNdpPacketQueueEnabled",
    "tcpIpNdpPrefixListSize",
    "tcpIpNdpRandomReachableTimeEnabled",
    "tcpIpNdpRndRtrSolicitationDelayEnabled",
    "tcpIpNdpRtrSolicitationInterval",
    "tcpIpNdpSlaacDadNumberOfTransmissions",
    "tcpIpNdpSlaacDadRetransmissionDelay",
    "tcpIpNdpSlaacDelayEnabled",
    "tcpIpNdpSlaacOptimisticDadEnabled",
]

MEMBER_TYPES = {
    "tcpIpNdpDefaultReachableTime": "TimeValue",
    "tcpIpNdpDefaultRetransTimer": "TimeValue",
    "tcpIpNdpDefaultRouterListSize": "PositiveInteger",
    "tcpIpNdpDefensiveProcessing": "Boolean",
    "tcpIpNdpDelayFirstProbeTimeValue": "TimeValue",
    "tcpIpNdpDestinationCacheSize": "PositiveInteger",
    "tcpIpNdpDynamicHopLimitEnabled": "Boolean",
    "tcpIpNdpDynamicMtuEnabled": "Boolean",
    "tcpIpNdpDynamicReachableTimeEnabled": "Boolean",
    "tcpIpNdpDynamicRetransTimeEnabled": "Boolean",
    "tcpIpNdpMaxRandomFactor": "PositiveInteger",
    "tcpIpNdpMaxRtrSolicitationDelay": "TimeValue",
    "tcpIpNdpMaxRtrSolicitations": "PositiveInteger",
    "tcpIpNdpMinRandomFactor": "PositiveInteger",
    "tcpIpNdpNeighborUnreachabilityDetectionEnabled": "Boolean",
    "tcpIpNdpNumMulticastSolicitations": "PositiveInteger",
    "tcpIpNdpNumUnicastSolicitations": "PositiveInteger",
    "tcpIpNdpPacketQueueEnabled": "Boolean",
    "tcpIpNdpPrefixListSize": "PositiveInteger",
    "tcpIpNdpRandomReachableTimeEnabled": "Boolean",
    "tcpIpNdpRndRtrSolicitationDelayEnabled": "Boolean",
    "tcpIpNdpRtrSolicitationInterval": "TimeValue",
    "tcpIpNdpSlaacDadNumberOfTransmissions": "PositiveInteger",
    "tcpIpNdpSlaacDadRetransmissionDelay": "TimeValue",
    "tcpIpNdpSlaacDelayEnabled": "Boolean",
    "tcpIpNdpSlaacOptimisticDadEnabled": "Boolean",
}

TCP_IP_NDP_DEFAULT_REACHABLE_TIME = "Configuration of the ReachableTime (s) specified in [RFC4861 6.3.2. Host Variables]."
TCP_IP_NDP_DEFAULT_RETRANS_TIMER = "Configures the default value (s) for the RetransTimer variable specified in [RFC4861 6.3.2. Host Variables]."
TCP_IP_NDP_DEFAULT_ROUTER_LIST_SIZE = "Maximum number of default router entries."
TCP_IP_NDP_DEFENSIVE_PROCESSING = "If enabled the NDP shall only process Neighbor Advertisements which are received in reaction to a previously transmitted Neighbor Solicitation as well as skipping updates to the Neighbor Cache based on received Neighbor Solicitations. If disabled all Neighbor Advertisements and Solicitations shall be processed as specified in RFC4861."
TCP_IP_NDP_DELAY_FIRST_PROBE_TIME_VALUE = "Delay before sending the first NUD probe in (s)."
TCP_IP_NDP_DESTINATION_CACHE_SIZE = "Maximum number of entries in the destination cache."
TCP_IP_NDP_DYNAMIC_HOP_LIMIT_ENABLED = "If enabled the default hop limit may be reconfigured based on received Router Advertisements."
TCP_IP_NDP_DYNAMIC_MTU_ENABLED = "Allow dynamic reconfiguration of link MTU via Router Advertisements."
TCP_IP_NDP_DYNAMIC_REACHABLE_TIME_ENABLED = "If enabled the default Reachable Time value may be reconfigured based on received Router Advertisements."
TCP_IP_NDP_DYNAMIC_RETRANS_TIME_ENABLED = "If enabled the default Retransmit Timer value may be reconfigured based on received Router Advertisements."
TCP_IP_NDP_MAX_RANDOM_FACTOR = "Maximum random factor used for randomization"
TCP_IP_NDP_MAX_RTR_SOLICITATION_DELAY = "Maximum delay before the first Router Solicitation will be sent after interface initialization in (s)."
TCP_IP_NDP_MAX_RTR_SOLICITATIONS = "Maximum number of Router Solicitations that will be sent before the first Router Advertisement has been received."
TCP_IP_NDP_MIN_RANDOM_FACTOR = "Minimum random factor used for randomization"
TCP_IP_NDP_NEIGHBOR_UNREACHABILITY_DETECTION_ENABLED = (
    "Neighbor Unreachability Detection is used to remove unused entries from the neighbor cache. This feature is a basic feature of NDP and should be turned on."
)
TCP_IP_NDP_NUM_MULTICAST_SOLICITATIONS = "Maximum number of multicast solicitations that will be sent when performing address resolution."
TCP_IP_NDP_NUM_UNICAST_SOLICITATIONS = "Maximum number of unicast solicitations that will be sent when performig Neighbor Unreachability Detection."
TCP_IP_NDP_PACKET_QUEUE_ENABLED = "Enables (TRUE) or disables (FALSE) support of a NDP Packet Queue according to IETF RFC 4861, section 7.2.2."
TCP_IP_NDP_PREFIX_LIST_SIZE = "Maximum number of entries in the on-link prefix list."
TCP_IP_NDP_RANDOM_REACHABLE_TIME_ENABLED = "If enabled the value of ReachableTime will be multiplied with a random value between MIN_RANDOM_FACTOR and MAX_RANDOM_FACTOR in order to prevent multiple nodes from transmitting at exactly the same time."
TCP_IP_NDP_RND_RTR_SOLICITATION_DELAY_ENABLED = "If enabled the first router solicitation will be delayed randomly from [0...MAX_RTR_SOLICITATION_DELAY]. Otherwise the first router solicitation will be sent after exactly MAX_RTR_SOLICITATION_DELAY milliseconds."
TCP_IP_NDP_RTR_SOLICITATION_INTERVAL = "Interval between consecutive Router Solicitations in (s)."
TCP_IP_NDP_SLAAC_DAD_NUMBER_OF_TRANSMISSIONS = "Number of Neighbor Solicitations that have to be unanswered in order to set an autoconfigurated address to PREFERRED (usable) state."
TCP_IP_NDP_SLAAC_DAD_RETRANSMISSION_DELAY = "Sets the maximum value for the address configuration delay (s)."
TCP_IP_NDP_SLAAC_DELAY_ENABLED = "If enabled transmission of the first DAD Neighbor Solicitation will be delayed by a random value from [0...MAX_DAD_DELAY]."
TCP_IP_NDP_SLAAC_OPTIMISTIC_DAD_ENABLED = "Enable Optimistic Duplicate Address Detection (DAD) according to RFC4429."


class TestIpv6NdpProps:
    def test_inheritance(self):
        assert issubclass(Ipv6NdpProps, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(Ipv6NdpProps.__doc__) == CLASS_NOTE

    def test_initialization_defaults(self):
        obj = Ipv6NdpProps()

        assert obj.getTcpIpNdpDefaultReachableTime() is None
        assert obj.getTcpIpNdpDefaultRetransTimer() is None
        assert obj.getTcpIpNdpDefaultRouterListSize() is None
        assert obj.getTcpIpNdpDefensiveProcessing() is None
        assert obj.getTcpIpNdpDelayFirstProbeTimeValue() is None
        assert obj.getTcpIpNdpDestinationCacheSize() is None
        assert obj.getTcpIpNdpDynamicHopLimitEnabled() is None
        assert obj.getTcpIpNdpDynamicMtuEnabled() is None
        assert obj.getTcpIpNdpDynamicReachableTimeEnabled() is None
        assert obj.getTcpIpNdpDynamicRetransTimeEnabled() is None
        assert obj.getTcpIpNdpMaxRandomFactor() is None
        assert obj.getTcpIpNdpMaxRtrSolicitationDelay() is None
        assert obj.getTcpIpNdpMaxRtrSolicitations() is None
        assert obj.getTcpIpNdpMinRandomFactor() is None
        assert obj.getTcpIpNdpNeighborUnreachabilityDetectionEnabled() is None
        assert obj.getTcpIpNdpNumMulticastSolicitations() is None
        assert obj.getTcpIpNdpNumUnicastSolicitations() is None
        assert obj.getTcpIpNdpPacketQueueEnabled() is None
        assert obj.getTcpIpNdpPrefixListSize() is None
        assert obj.getTcpIpNdpRandomReachableTimeEnabled() is None
        assert obj.getTcpIpNdpRndRtrSolicitationDelayEnabled() is None
        assert obj.getTcpIpNdpRtrSolicitationInterval() is None
        assert obj.getTcpIpNdpSlaacDadNumberOfTransmissions() is None
        assert obj.getTcpIpNdpSlaacDadRetransmissionDelay() is None
        assert obj.getTcpIpNdpSlaacDelayEnabled() is None
        assert obj.getTcpIpNdpSlaacOptimisticDadEnabled() is None

    def test_member_annotations(self):
        import ast

        import armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology as ethernet_topology_module

        module_source = open(ethernet_topology_module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "Ipv6NdpProps")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {st.target.attr: ast.get_source_segment(module_source, st.annotation) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)}

        for member in MEMBER_ORDER:
            assert annotations[member] == "Optional[%s]" % MEMBER_TYPES[member]

        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpDefaultReachableTime).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpDefaultReachableTime).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpDefaultRetransTimer).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpDefaultRetransTimer).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpDefaultRouterListSize).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpDefaultRouterListSize).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpDefensiveProcessing).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpDefensiveProcessing).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpDelayFirstProbeTimeValue).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpDelayFirstProbeTimeValue).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpDestinationCacheSize).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpDestinationCacheSize).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpDynamicHopLimitEnabled).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpDynamicHopLimitEnabled).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpDynamicMtuEnabled).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpDynamicMtuEnabled).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpDynamicReachableTimeEnabled).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpDynamicReachableTimeEnabled).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpDynamicRetransTimeEnabled).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpDynamicRetransTimeEnabled).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpMaxRandomFactor).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpMaxRandomFactor).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpMaxRtrSolicitationDelay).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpMaxRtrSolicitationDelay).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpMaxRtrSolicitations).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpMaxRtrSolicitations).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpMinRandomFactor).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpMinRandomFactor).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpNeighborUnreachabilityDetectionEnabled).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpNeighborUnreachabilityDetectionEnabled).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpNumMulticastSolicitations).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpNumMulticastSolicitations).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpNumUnicastSolicitations).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpNumUnicastSolicitations).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpPacketQueueEnabled).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpPacketQueueEnabled).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpPrefixListSize).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpPrefixListSize).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpRandomReachableTimeEnabled).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpRandomReachableTimeEnabled).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpRndRtrSolicitationDelayEnabled).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpRndRtrSolicitationDelayEnabled).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpRtrSolicitationInterval).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpRtrSolicitationInterval).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpSlaacDadNumberOfTransmissions).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpSlaacDadNumberOfTransmissions).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpSlaacDadRetransmissionDelay).get("return") == typing.Optional[TimeValue]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpSlaacDadRetransmissionDelay).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpSlaacDelayEnabled).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpSlaacDelayEnabled).get("return") is Ipv6NdpProps
        assert typing.get_type_hints(Ipv6NdpProps.getTcpIpNdpSlaacOptimisticDadEnabled).get("return") == typing.Optional[Boolean]
        assert typing.get_type_hints(Ipv6NdpProps.setTcpIpNdpSlaacOptimisticDadEnabled).get("return") is Ipv6NdpProps

    def test_member_order(self):
        obj = Ipv6NdpProps()

        members = [k for k in vars(obj) if k in MEMBER_ORDER]
        assert members == MEMBER_ORDER

    def test_get_set_tcp_ip_ndp_default_reachable_time(self):
        obj = Ipv6NdpProps()
        value = TimeValue().setValue(1.0)

        result = obj.setTcpIpNdpDefaultReachableTime(value)
        assert result is obj
        assert obj.getTcpIpNdpDefaultReachableTime() is value

        obj.setTcpIpNdpDefaultReachableTime(None)
        assert obj.getTcpIpNdpDefaultReachableTime() is value

    def test_get_set_tcp_ip_ndp_default_retrans_timer(self):
        obj = Ipv6NdpProps()
        value = TimeValue().setValue(1.0)

        result = obj.setTcpIpNdpDefaultRetransTimer(value)
        assert result is obj
        assert obj.getTcpIpNdpDefaultRetransTimer() is value

        obj.setTcpIpNdpDefaultRetransTimer(None)
        assert obj.getTcpIpNdpDefaultRetransTimer() is value

    def test_get_set_tcp_ip_ndp_default_router_list_size(self):
        obj = Ipv6NdpProps()
        value = PositiveInteger().setValue(4)

        result = obj.setTcpIpNdpDefaultRouterListSize(value)
        assert result is obj
        assert obj.getTcpIpNdpDefaultRouterListSize() is value

        obj.setTcpIpNdpDefaultRouterListSize(None)
        assert obj.getTcpIpNdpDefaultRouterListSize() is value

    def test_get_set_tcp_ip_ndp_defensive_processing(self):
        obj = Ipv6NdpProps()
        value = Boolean().setValue(True)

        result = obj.setTcpIpNdpDefensiveProcessing(value)
        assert result is obj
        assert obj.getTcpIpNdpDefensiveProcessing() is value

        obj.setTcpIpNdpDefensiveProcessing(None)
        assert obj.getTcpIpNdpDefensiveProcessing() is value

    def test_get_set_tcp_ip_ndp_delay_first_probe_time_value(self):
        obj = Ipv6NdpProps()
        value = TimeValue().setValue(1.0)

        result = obj.setTcpIpNdpDelayFirstProbeTimeValue(value)
        assert result is obj
        assert obj.getTcpIpNdpDelayFirstProbeTimeValue() is value

        obj.setTcpIpNdpDelayFirstProbeTimeValue(None)
        assert obj.getTcpIpNdpDelayFirstProbeTimeValue() is value

    def test_get_set_tcp_ip_ndp_destination_cache_size(self):
        obj = Ipv6NdpProps()
        value = PositiveInteger().setValue(4)

        result = obj.setTcpIpNdpDestinationCacheSize(value)
        assert result is obj
        assert obj.getTcpIpNdpDestinationCacheSize() is value

        obj.setTcpIpNdpDestinationCacheSize(None)
        assert obj.getTcpIpNdpDestinationCacheSize() is value

    def test_get_set_tcp_ip_ndp_dynamic_hop_limit_enabled(self):
        obj = Ipv6NdpProps()
        value = Boolean().setValue(True)

        result = obj.setTcpIpNdpDynamicHopLimitEnabled(value)
        assert result is obj
        assert obj.getTcpIpNdpDynamicHopLimitEnabled() is value

        obj.setTcpIpNdpDynamicHopLimitEnabled(None)
        assert obj.getTcpIpNdpDynamicHopLimitEnabled() is value

    def test_get_set_tcp_ip_ndp_dynamic_mtu_enabled(self):
        obj = Ipv6NdpProps()
        value = Boolean().setValue(True)

        result = obj.setTcpIpNdpDynamicMtuEnabled(value)
        assert result is obj
        assert obj.getTcpIpNdpDynamicMtuEnabled() is value

        obj.setTcpIpNdpDynamicMtuEnabled(None)
        assert obj.getTcpIpNdpDynamicMtuEnabled() is value

    def test_get_set_tcp_ip_ndp_dynamic_reachable_time_enabled(self):
        obj = Ipv6NdpProps()
        value = Boolean().setValue(True)

        result = obj.setTcpIpNdpDynamicReachableTimeEnabled(value)
        assert result is obj
        assert obj.getTcpIpNdpDynamicReachableTimeEnabled() is value

        obj.setTcpIpNdpDynamicReachableTimeEnabled(None)
        assert obj.getTcpIpNdpDynamicReachableTimeEnabled() is value

    def test_get_set_tcp_ip_ndp_dynamic_retrans_time_enabled(self):
        obj = Ipv6NdpProps()
        value = Boolean().setValue(True)

        result = obj.setTcpIpNdpDynamicRetransTimeEnabled(value)
        assert result is obj
        assert obj.getTcpIpNdpDynamicRetransTimeEnabled() is value

        obj.setTcpIpNdpDynamicRetransTimeEnabled(None)
        assert obj.getTcpIpNdpDynamicRetransTimeEnabled() is value

    def test_get_set_tcp_ip_ndp_max_random_factor(self):
        obj = Ipv6NdpProps()
        value = PositiveInteger().setValue(4)

        result = obj.setTcpIpNdpMaxRandomFactor(value)
        assert result is obj
        assert obj.getTcpIpNdpMaxRandomFactor() is value

        obj.setTcpIpNdpMaxRandomFactor(None)
        assert obj.getTcpIpNdpMaxRandomFactor() is value

    def test_get_set_tcp_ip_ndp_max_rtr_solicitation_delay(self):
        obj = Ipv6NdpProps()
        value = TimeValue().setValue(1.0)

        result = obj.setTcpIpNdpMaxRtrSolicitationDelay(value)
        assert result is obj
        assert obj.getTcpIpNdpMaxRtrSolicitationDelay() is value

        obj.setTcpIpNdpMaxRtrSolicitationDelay(None)
        assert obj.getTcpIpNdpMaxRtrSolicitationDelay() is value

    def test_get_set_tcp_ip_ndp_max_rtr_solicitations(self):
        obj = Ipv6NdpProps()
        value = PositiveInteger().setValue(4)

        result = obj.setTcpIpNdpMaxRtrSolicitations(value)
        assert result is obj
        assert obj.getTcpIpNdpMaxRtrSolicitations() is value

        obj.setTcpIpNdpMaxRtrSolicitations(None)
        assert obj.getTcpIpNdpMaxRtrSolicitations() is value

    def test_get_set_tcp_ip_ndp_min_random_factor(self):
        obj = Ipv6NdpProps()
        value = PositiveInteger().setValue(4)

        result = obj.setTcpIpNdpMinRandomFactor(value)
        assert result is obj
        assert obj.getTcpIpNdpMinRandomFactor() is value

        obj.setTcpIpNdpMinRandomFactor(None)
        assert obj.getTcpIpNdpMinRandomFactor() is value

    def test_get_set_tcp_ip_ndp_neighbor_unreachability_detection_enabled(self):
        obj = Ipv6NdpProps()
        value = Boolean().setValue(True)

        result = obj.setTcpIpNdpNeighborUnreachabilityDetectionEnabled(value)
        assert result is obj
        assert obj.getTcpIpNdpNeighborUnreachabilityDetectionEnabled() is value

        obj.setTcpIpNdpNeighborUnreachabilityDetectionEnabled(None)
        assert obj.getTcpIpNdpNeighborUnreachabilityDetectionEnabled() is value

    def test_get_set_tcp_ip_ndp_num_multicast_solicitations(self):
        obj = Ipv6NdpProps()
        value = PositiveInteger().setValue(4)

        result = obj.setTcpIpNdpNumMulticastSolicitations(value)
        assert result is obj
        assert obj.getTcpIpNdpNumMulticastSolicitations() is value

        obj.setTcpIpNdpNumMulticastSolicitations(None)
        assert obj.getTcpIpNdpNumMulticastSolicitations() is value

    def test_get_set_tcp_ip_ndp_num_unicast_solicitations(self):
        obj = Ipv6NdpProps()
        value = PositiveInteger().setValue(4)

        result = obj.setTcpIpNdpNumUnicastSolicitations(value)
        assert result is obj
        assert obj.getTcpIpNdpNumUnicastSolicitations() is value

        obj.setTcpIpNdpNumUnicastSolicitations(None)
        assert obj.getTcpIpNdpNumUnicastSolicitations() is value

    def test_get_set_tcp_ip_ndp_packet_queue_enabled(self):
        obj = Ipv6NdpProps()
        value = Boolean().setValue(True)

        result = obj.setTcpIpNdpPacketQueueEnabled(value)
        assert result is obj
        assert obj.getTcpIpNdpPacketQueueEnabled() is value

        obj.setTcpIpNdpPacketQueueEnabled(None)
        assert obj.getTcpIpNdpPacketQueueEnabled() is value

    def test_get_set_tcp_ip_ndp_prefix_list_size(self):
        obj = Ipv6NdpProps()
        value = PositiveInteger().setValue(4)

        result = obj.setTcpIpNdpPrefixListSize(value)
        assert result is obj
        assert obj.getTcpIpNdpPrefixListSize() is value

        obj.setTcpIpNdpPrefixListSize(None)
        assert obj.getTcpIpNdpPrefixListSize() is value

    def test_get_set_tcp_ip_ndp_random_reachable_time_enabled(self):
        obj = Ipv6NdpProps()
        value = Boolean().setValue(True)

        result = obj.setTcpIpNdpRandomReachableTimeEnabled(value)
        assert result is obj
        assert obj.getTcpIpNdpRandomReachableTimeEnabled() is value

        obj.setTcpIpNdpRandomReachableTimeEnabled(None)
        assert obj.getTcpIpNdpRandomReachableTimeEnabled() is value

    def test_get_set_tcp_ip_ndp_rnd_rtr_solicitation_delay_enabled(self):
        obj = Ipv6NdpProps()
        value = Boolean().setValue(True)

        result = obj.setTcpIpNdpRndRtrSolicitationDelayEnabled(value)
        assert result is obj
        assert obj.getTcpIpNdpRndRtrSolicitationDelayEnabled() is value

        obj.setTcpIpNdpRndRtrSolicitationDelayEnabled(None)
        assert obj.getTcpIpNdpRndRtrSolicitationDelayEnabled() is value

    def test_get_set_tcp_ip_ndp_rtr_solicitation_interval(self):
        obj = Ipv6NdpProps()
        value = TimeValue().setValue(1.0)

        result = obj.setTcpIpNdpRtrSolicitationInterval(value)
        assert result is obj
        assert obj.getTcpIpNdpRtrSolicitationInterval() is value

        obj.setTcpIpNdpRtrSolicitationInterval(None)
        assert obj.getTcpIpNdpRtrSolicitationInterval() is value

    def test_get_set_tcp_ip_ndp_slaac_dad_number_of_transmissions(self):
        obj = Ipv6NdpProps()
        value = PositiveInteger().setValue(4)

        result = obj.setTcpIpNdpSlaacDadNumberOfTransmissions(value)
        assert result is obj
        assert obj.getTcpIpNdpSlaacDadNumberOfTransmissions() is value

        obj.setTcpIpNdpSlaacDadNumberOfTransmissions(None)
        assert obj.getTcpIpNdpSlaacDadNumberOfTransmissions() is value

    def test_get_set_tcp_ip_ndp_slaac_dad_retransmission_delay(self):
        obj = Ipv6NdpProps()
        value = TimeValue().setValue(1.0)

        result = obj.setTcpIpNdpSlaacDadRetransmissionDelay(value)
        assert result is obj
        assert obj.getTcpIpNdpSlaacDadRetransmissionDelay() is value

        obj.setTcpIpNdpSlaacDadRetransmissionDelay(None)
        assert obj.getTcpIpNdpSlaacDadRetransmissionDelay() is value

    def test_get_set_tcp_ip_ndp_slaac_delay_enabled(self):
        obj = Ipv6NdpProps()
        value = Boolean().setValue(True)

        result = obj.setTcpIpNdpSlaacDelayEnabled(value)
        assert result is obj
        assert obj.getTcpIpNdpSlaacDelayEnabled() is value

        obj.setTcpIpNdpSlaacDelayEnabled(None)
        assert obj.getTcpIpNdpSlaacDelayEnabled() is value

    def test_get_set_tcp_ip_ndp_slaac_optimistic_dad_enabled(self):
        obj = Ipv6NdpProps()
        value = Boolean().setValue(True)

        result = obj.setTcpIpNdpSlaacOptimisticDadEnabled(value)
        assert result is obj
        assert obj.getTcpIpNdpSlaacOptimisticDadEnabled() is value

        obj.setTcpIpNdpSlaacOptimisticDadEnabled(None)
        assert obj.getTcpIpNdpSlaacOptimisticDadEnabled() is value

    def test_accessor_docstrings(self):
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpDefaultReachableTime.__doc__) == TCP_IP_NDP_DEFAULT_REACHABLE_TIME
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpDefaultReachableTime.__doc__) == (
            TCP_IP_NDP_DEFAULT_REACHABLE_TIME + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpDefaultReachableTime."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpDefaultRetransTimer.__doc__) == TCP_IP_NDP_DEFAULT_RETRANS_TIMER
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpDefaultRetransTimer.__doc__) == (
            TCP_IP_NDP_DEFAULT_RETRANS_TIMER + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpDefaultRetransTimer."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpDefaultRouterListSize.__doc__) == TCP_IP_NDP_DEFAULT_ROUTER_LIST_SIZE
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpDefaultRouterListSize.__doc__) == (
            TCP_IP_NDP_DEFAULT_ROUTER_LIST_SIZE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpDefaultRouterListSize."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpDefensiveProcessing.__doc__) == TCP_IP_NDP_DEFENSIVE_PROCESSING
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpDefensiveProcessing.__doc__) == (
            TCP_IP_NDP_DEFENSIVE_PROCESSING + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpDefensiveProcessing."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpDelayFirstProbeTimeValue.__doc__) == TCP_IP_NDP_DELAY_FIRST_PROBE_TIME_VALUE
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpDelayFirstProbeTimeValue.__doc__) == (
            TCP_IP_NDP_DELAY_FIRST_PROBE_TIME_VALUE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpDelayFirstProbeTimeValue."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpDestinationCacheSize.__doc__) == TCP_IP_NDP_DESTINATION_CACHE_SIZE
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpDestinationCacheSize.__doc__) == (
            TCP_IP_NDP_DESTINATION_CACHE_SIZE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpDestinationCacheSize."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpDynamicHopLimitEnabled.__doc__) == TCP_IP_NDP_DYNAMIC_HOP_LIMIT_ENABLED
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpDynamicHopLimitEnabled.__doc__) == (
            TCP_IP_NDP_DYNAMIC_HOP_LIMIT_ENABLED + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpDynamicHopLimitEnabled."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpDynamicMtuEnabled.__doc__) == TCP_IP_NDP_DYNAMIC_MTU_ENABLED
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpDynamicMtuEnabled.__doc__) == (
            TCP_IP_NDP_DYNAMIC_MTU_ENABLED + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpDynamicMtuEnabled."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpDynamicReachableTimeEnabled.__doc__) == TCP_IP_NDP_DYNAMIC_REACHABLE_TIME_ENABLED
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpDynamicReachableTimeEnabled.__doc__) == (
            TCP_IP_NDP_DYNAMIC_REACHABLE_TIME_ENABLED + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpDynamicReachableTimeEnabled."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpDynamicRetransTimeEnabled.__doc__) == TCP_IP_NDP_DYNAMIC_RETRANS_TIME_ENABLED
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpDynamicRetransTimeEnabled.__doc__) == (
            TCP_IP_NDP_DYNAMIC_RETRANS_TIME_ENABLED + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpDynamicRetransTimeEnabled."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpMaxRandomFactor.__doc__) == TCP_IP_NDP_MAX_RANDOM_FACTOR
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpMaxRandomFactor.__doc__) == (
            TCP_IP_NDP_MAX_RANDOM_FACTOR + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpMaxRandomFactor."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpMaxRtrSolicitationDelay.__doc__) == TCP_IP_NDP_MAX_RTR_SOLICITATION_DELAY
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpMaxRtrSolicitationDelay.__doc__) == (
            TCP_IP_NDP_MAX_RTR_SOLICITATION_DELAY + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpMaxRtrSolicitationDelay."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpMaxRtrSolicitations.__doc__) == TCP_IP_NDP_MAX_RTR_SOLICITATIONS
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpMaxRtrSolicitations.__doc__) == (
            TCP_IP_NDP_MAX_RTR_SOLICITATIONS + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpMaxRtrSolicitations."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpMinRandomFactor.__doc__) == TCP_IP_NDP_MIN_RANDOM_FACTOR
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpMinRandomFactor.__doc__) == (
            TCP_IP_NDP_MIN_RANDOM_FACTOR + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpMinRandomFactor."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpNeighborUnreachabilityDetectionEnabled.__doc__) == TCP_IP_NDP_NEIGHBOR_UNREACHABILITY_DETECTION_ENABLED
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpNeighborUnreachabilityDetectionEnabled.__doc__) == (
            TCP_IP_NDP_NEIGHBOR_UNREACHABILITY_DETECTION_ENABLED + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpNeighborUnreachabilityDetectionEnabled."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpNumMulticastSolicitations.__doc__) == TCP_IP_NDP_NUM_MULTICAST_SOLICITATIONS
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpNumMulticastSolicitations.__doc__) == (
            TCP_IP_NDP_NUM_MULTICAST_SOLICITATIONS + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpNumMulticastSolicitations."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpNumUnicastSolicitations.__doc__) == TCP_IP_NDP_NUM_UNICAST_SOLICITATIONS
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpNumUnicastSolicitations.__doc__) == (
            TCP_IP_NDP_NUM_UNICAST_SOLICITATIONS + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpNumUnicastSolicitations."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpPacketQueueEnabled.__doc__) == TCP_IP_NDP_PACKET_QUEUE_ENABLED
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpPacketQueueEnabled.__doc__) == (
            TCP_IP_NDP_PACKET_QUEUE_ENABLED + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpPacketQueueEnabled."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpPrefixListSize.__doc__) == TCP_IP_NDP_PREFIX_LIST_SIZE
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpPrefixListSize.__doc__) == (
            TCP_IP_NDP_PREFIX_LIST_SIZE + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpPrefixListSize."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpRandomReachableTimeEnabled.__doc__) == TCP_IP_NDP_RANDOM_REACHABLE_TIME_ENABLED
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpRandomReachableTimeEnabled.__doc__) == (
            TCP_IP_NDP_RANDOM_REACHABLE_TIME_ENABLED + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpRandomReachableTimeEnabled."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpRndRtrSolicitationDelayEnabled.__doc__) == TCP_IP_NDP_RND_RTR_SOLICITATION_DELAY_ENABLED
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpRndRtrSolicitationDelayEnabled.__doc__) == (
            TCP_IP_NDP_RND_RTR_SOLICITATION_DELAY_ENABLED + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpRndRtrSolicitationDelayEnabled."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpRtrSolicitationInterval.__doc__) == TCP_IP_NDP_RTR_SOLICITATION_INTERVAL
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpRtrSolicitationInterval.__doc__) == (
            TCP_IP_NDP_RTR_SOLICITATION_INTERVAL + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpRtrSolicitationInterval."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpSlaacDadNumberOfTransmissions.__doc__) == TCP_IP_NDP_SLAAC_DAD_NUMBER_OF_TRANSMISSIONS
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpSlaacDadNumberOfTransmissions.__doc__) == (
            TCP_IP_NDP_SLAAC_DAD_NUMBER_OF_TRANSMISSIONS + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpSlaacDadNumberOfTransmissions."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpSlaacDadRetransmissionDelay.__doc__) == TCP_IP_NDP_SLAAC_DAD_RETRANSMISSION_DELAY
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpSlaacDadRetransmissionDelay.__doc__) == (
            TCP_IP_NDP_SLAAC_DAD_RETRANSMISSION_DELAY + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpSlaacDadRetransmissionDelay."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpSlaacDelayEnabled.__doc__) == TCP_IP_NDP_SLAAC_DELAY_ENABLED
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpSlaacDelayEnabled.__doc__) == (
            TCP_IP_NDP_SLAAC_DELAY_ENABLED + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpSlaacDelayEnabled."
        )
        assert inspect.cleandoc(Ipv6NdpProps.getTcpIpNdpSlaacOptimisticDadEnabled.__doc__) == TCP_IP_NDP_SLAAC_OPTIMISTIC_DAD_ENABLED
        assert inspect.cleandoc(Ipv6NdpProps.setTcpIpNdpSlaacOptimisticDadEnabled.__doc__) == (
            TCP_IP_NDP_SLAAC_OPTIMISTIC_DAD_ENABLED + "\n\nA None value is a no-op and does not overwrite an existing tcpIpNdpSlaacOptimisticDadEnabled."
        )
