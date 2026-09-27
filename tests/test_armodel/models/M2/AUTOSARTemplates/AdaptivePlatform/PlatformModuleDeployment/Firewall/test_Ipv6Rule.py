import inspect
import typing
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import IcmpRule, Ipv6Rule, NetworkLayerRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Ip6AddressString, PositiveInteger

DESTINATION_IP_ADDRESS_NOTE = "Filter to match packets with the destination IPv6 address."
DESTINATION_NETWORK_MASK_NOTE = "Filter to match packets with the destination IPv6 address range. The destinationIpAddress with the destinationNetworkMask defines the MAC address range."
FLOW_LABEL_NOTE = "Filter to match packets with a defined flow label."
HOP_LIMIT_NOTE = "Filter to match packets with a minimum hop limit."
ICMP_RULE_NOTE = "Configuration of filter rules for ICMP (Internet Control Message Protocol)."
NEXT_HEADER_NOTE = "Filter to match packets with a defined type of an extension header."
SOURCE_IP_ADDRESS_NOTE = "Filter to match packets with the source IPv6 address."
SOURCE_NETWORK_MASK_NOTE = "Filter to match packets with the source IPv6 address range. The sourceIpAddress with the sourceNetworkMask defines the IP address range."
TRAFFIC_CLASS_NOTE = "Filter to match packets with a defined traffic class or priority."


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


def _ip6_address(value):
    a = Ip6AddressString()
    a.setValue(value)
    return a


class TestIpv6Rule:
    def test_defaults_in_spec_displayed_order(self):
        obj = Ipv6Rule()
        assert isinstance(obj, ARObject)
        assert isinstance(obj, NetworkLayerRule)
        assert obj.getDestinationIpAddress() is None
        assert obj.getDestinationNetworkMask() is None
        assert obj.getFlowLabel() is None
        assert obj.getHopLimit() is None
        assert obj.getIcmpRule() is None
        assert obj.getNextHeader() is None
        assert obj.getSourceIpAddress() is None
        assert obj.getSourceNetworkMask() is None
        assert obj.getTrafficClass() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        assert Ipv6Rule.__doc__.strip() == "Configuration of filter rules on IPv6 level. Tags: atp.Status=candidate"

    def test_docstrings_are_spec_note_verbatim(self):
        assert inspect.cleandoc(Ipv6Rule.getDestinationIpAddress.__doc__) == DESTINATION_IP_ADDRESS_NOTE
        assert inspect.cleandoc(Ipv6Rule.setDestinationIpAddress.__doc__) == DESTINATION_IP_ADDRESS_NOTE + "\nA None value is a no-op and does not overwrite an existing destinationIpAddress."
        assert inspect.cleandoc(Ipv6Rule.getDestinationNetworkMask.__doc__) == DESTINATION_NETWORK_MASK_NOTE
        assert inspect.cleandoc(Ipv6Rule.setDestinationNetworkMask.__doc__) == DESTINATION_NETWORK_MASK_NOTE + "\nA None value is a no-op and does not overwrite an existing destinationNetworkMask."
        assert inspect.cleandoc(Ipv6Rule.getFlowLabel.__doc__) == FLOW_LABEL_NOTE
        assert inspect.cleandoc(Ipv6Rule.setFlowLabel.__doc__) == FLOW_LABEL_NOTE + "\nA None value is a no-op and does not overwrite an existing flowLabel."
        assert inspect.cleandoc(Ipv6Rule.getHopLimit.__doc__) == HOP_LIMIT_NOTE
        assert inspect.cleandoc(Ipv6Rule.setHopLimit.__doc__) == HOP_LIMIT_NOTE + "\nA None value is a no-op and does not overwrite an existing hopLimit."
        assert inspect.cleandoc(Ipv6Rule.getIcmpRule.__doc__) == ICMP_RULE_NOTE
        assert inspect.cleandoc(Ipv6Rule.setIcmpRule.__doc__) == ICMP_RULE_NOTE + "\nA None value is a no-op and does not overwrite an existing icmpRule."
        assert inspect.cleandoc(Ipv6Rule.getNextHeader.__doc__) == NEXT_HEADER_NOTE
        assert inspect.cleandoc(Ipv6Rule.setNextHeader.__doc__) == NEXT_HEADER_NOTE + "\nA None value is a no-op and does not overwrite an existing nextHeader."
        assert inspect.cleandoc(Ipv6Rule.getSourceIpAddress.__doc__) == SOURCE_IP_ADDRESS_NOTE
        assert inspect.cleandoc(Ipv6Rule.setSourceIpAddress.__doc__) == SOURCE_IP_ADDRESS_NOTE + "\nA None value is a no-op and does not overwrite an existing sourceIpAddress."
        assert inspect.cleandoc(Ipv6Rule.getSourceNetworkMask.__doc__) == SOURCE_NETWORK_MASK_NOTE
        assert inspect.cleandoc(Ipv6Rule.setSourceNetworkMask.__doc__) == SOURCE_NETWORK_MASK_NOTE + "\nA None value is a no-op and does not overwrite an existing sourceNetworkMask."
        assert inspect.cleandoc(Ipv6Rule.getTrafficClass.__doc__) == TRAFFIC_CLASS_NOTE
        assert inspect.cleandoc(Ipv6Rule.setTrafficClass.__doc__) == TRAFFIC_CLASS_NOTE + "\nA None value is a no-op and does not overwrite an existing trafficClass."

    def test_get_set_round_trip_and_none_noop(self):
        obj = Ipv6Rule()
        destination_ip_address = _ip6_address("2001:db8::1")
        destination_network_mask = _ip6_address("ffff:ffff:ffff::")
        flow_label = _pos_int(1048576)
        hop_limit = _pos_int(64)
        icmp_rule = IcmpRule()
        next_header = _pos_int(58)
        source_ip_address = _ip6_address("fe80::1")
        source_network_mask = _ip6_address("ffff::")
        traffic_class = _pos_int(46)

        assert obj.setDestinationIpAddress(destination_ip_address) is obj
        assert obj.setDestinationNetworkMask(destination_network_mask) is obj
        assert obj.setFlowLabel(flow_label) is obj
        assert obj.setHopLimit(hop_limit) is obj
        assert obj.setIcmpRule(icmp_rule) is obj
        assert obj.setNextHeader(next_header) is obj
        assert obj.setSourceIpAddress(source_ip_address) is obj
        assert obj.setSourceNetworkMask(source_network_mask) is obj
        assert obj.setTrafficClass(traffic_class) is obj

        assert obj.getDestinationIpAddress() is destination_ip_address
        assert obj.getDestinationNetworkMask() is destination_network_mask
        assert obj.getFlowLabel() is flow_label
        assert obj.getHopLimit() is hop_limit
        assert obj.getIcmpRule() is icmp_rule
        assert obj.getNextHeader() is next_header
        assert obj.getSourceIpAddress() is source_ip_address
        assert obj.getSourceNetworkMask() is source_network_mask
        assert obj.getTrafficClass() is traffic_class

        obj.setDestinationIpAddress(None)
        obj.setDestinationNetworkMask(None)
        obj.setFlowLabel(None)
        obj.setHopLimit(None)
        obj.setIcmpRule(None)
        obj.setNextHeader(None)
        obj.setSourceIpAddress(None)
        obj.setSourceNetworkMask(None)
        obj.setTrafficClass(None)
        assert obj.getDestinationIpAddress() is destination_ip_address
        assert obj.getDestinationNetworkMask() is destination_network_mask
        assert obj.getFlowLabel() is flow_label
        assert obj.getHopLimit() is hop_limit
        assert obj.getIcmpRule() is icmp_rule
        assert obj.getNextHeader() is next_header
        assert obj.getSourceIpAddress() is source_ip_address
        assert obj.getSourceNetworkMask() is source_network_mask
        assert obj.getTrafficClass() is traffic_class

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(Ipv6Rule.setDestinationIpAddress)
        assert hints["return"] is Ipv6Rule
        assert hints["value"] == Optional[Ip6AddressString]
        hints = typing.get_type_hints(Ipv6Rule.setIcmpRule)
        assert hints["return"] is Ipv6Rule
        assert hints["value"] == Optional[IcmpRule]
        hints = typing.get_type_hints(Ipv6Rule.setTrafficClass)
        assert hints["return"] is Ipv6Rule
        assert hints["value"] == Optional[PositiveInteger]
