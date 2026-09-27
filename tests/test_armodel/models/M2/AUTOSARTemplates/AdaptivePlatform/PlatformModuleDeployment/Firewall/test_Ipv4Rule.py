import inspect
import typing
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import IcmpRule, Ipv4Rule, NetworkLayerRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Ip4AddressString, PositiveInteger

CHECKSUM_VERIFICATION_NOTE = "Defines whether a Ipv4 header checksum verification is performed or not."
DESTINATION_IP_ADDRESS_NOTE = "Filter to match packets with the destination IPv4 address."
DESTINATION_NETWORK_MASK_NOTE = "Filter to match packets with the destination IPv4 address range. The destinationIpAddress with the destinationNetworkMask defines the IP address range."
DIFFERENTIATED_SERVICE_CODE_POINT_NOTE = "Filter to match packets with a DSCP value."
DO_NOT_FRAGMENT_NOTE = "Filter to match packets that have the doNotFragment bit in the Header set."
EXPLICIT_CONGESTION_NOTIFICATION_NOTE = "Filter to match packets with a ECN code point."
ICMP_RULE_NOTE = "Configuration of filter rules for ICMP (Internet Control Message Protocol)."
INTERNET_HEADER_LENGTH_NOTE = "Filter to match packets with a minimum ipv4 header length."
MORE_FRAGMENTS_NOTE = "Filter to match packets that have the moreFragments flag in the Header set."
PROTOCOL_NOTE = "Filter to match packets with a IP protocol number ."
SOURCE_IP_ADDRESS_NOTE = "Filter to match packets with the source IPv4 address."
SOURCE_NETWORK_MASK_NOTE = "Filter to match packets with the source IPv4 address range. The sourceIpAddress with the sourceNetworkMask defines the IP address range."
TTL_MAX_NOTE = "Filter to match packets with a maximum ttl value (TimeToLive defines the lifetime of data on the network)."
TTL_MIN_NOTE = "Filter to match packets with a minimum ttl value (TimeToLive defines the lifetime of data on the network)."


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


def _boolean(value):
    b = Boolean()
    b.setValue(value)
    return b


def _ip4_address(value):
    a = Ip4AddressString()
    a.setValue(value)
    return a


class TestIpv4Rule:
    def test_defaults_in_spec_displayed_order(self):
        obj = Ipv4Rule()
        assert isinstance(obj, ARObject)
        assert isinstance(obj, NetworkLayerRule)
        assert obj.getChecksumVerification() is None
        assert obj.getDestinationIpAddress() is None
        assert obj.getDestinationNetworkMask() is None
        assert obj.getDifferentiatedServiceCodePoint() is None
        assert obj.getDoNotFragment() is None
        assert obj.getExplicitCongestionNotification() is None
        assert obj.getIcmpRule() is None
        assert obj.getInternetHeaderLength() is None
        assert obj.getMoreFragments() is None
        assert obj.getProtocol() is None
        assert obj.getSourceIpAddress() is None
        assert obj.getSourceNetworkMask() is None
        assert obj.getTtlMax() is None
        assert obj.getTtlMin() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        assert Ipv4Rule.__doc__.strip() == "Configuration of filter rules on IPv4 level. Tags: atp.Status=candidate"

    def test_docstrings_are_spec_note_verbatim(self):
        assert inspect.cleandoc(Ipv4Rule.getChecksumVerification.__doc__) == CHECKSUM_VERIFICATION_NOTE
        assert inspect.cleandoc(Ipv4Rule.setChecksumVerification.__doc__) == CHECKSUM_VERIFICATION_NOTE + "\nA None value is a no-op and does not overwrite an existing checksumVerification."
        assert inspect.cleandoc(Ipv4Rule.getDestinationIpAddress.__doc__) == DESTINATION_IP_ADDRESS_NOTE
        assert inspect.cleandoc(Ipv4Rule.setDestinationIpAddress.__doc__) == DESTINATION_IP_ADDRESS_NOTE + "\nA None value is a no-op and does not overwrite an existing destinationIpAddress."
        assert inspect.cleandoc(Ipv4Rule.getDestinationNetworkMask.__doc__) == DESTINATION_NETWORK_MASK_NOTE
        assert inspect.cleandoc(Ipv4Rule.setDestinationNetworkMask.__doc__) == DESTINATION_NETWORK_MASK_NOTE + "\nA None value is a no-op and does not overwrite an existing destinationNetworkMask."
        assert inspect.cleandoc(Ipv4Rule.getDifferentiatedServiceCodePoint.__doc__) == DIFFERENTIATED_SERVICE_CODE_POINT_NOTE
        assert (
            inspect.cleandoc(Ipv4Rule.setDifferentiatedServiceCodePoint.__doc__)
            == DIFFERENTIATED_SERVICE_CODE_POINT_NOTE + "\nA None value is a no-op and does not overwrite an existing differentiatedServiceCodePoint."
        )
        assert inspect.cleandoc(Ipv4Rule.getDoNotFragment.__doc__) == DO_NOT_FRAGMENT_NOTE
        assert inspect.cleandoc(Ipv4Rule.setDoNotFragment.__doc__) == DO_NOT_FRAGMENT_NOTE + "\nA None value is a no-op and does not overwrite an existing doNotFragment."
        assert inspect.cleandoc(Ipv4Rule.getExplicitCongestionNotification.__doc__) == EXPLICIT_CONGESTION_NOTIFICATION_NOTE
        assert (
            inspect.cleandoc(Ipv4Rule.setExplicitCongestionNotification.__doc__)
            == EXPLICIT_CONGESTION_NOTIFICATION_NOTE + "\nA None value is a no-op and does not overwrite an existing explicitCongestionNotification."
        )
        assert inspect.cleandoc(Ipv4Rule.getIcmpRule.__doc__) == ICMP_RULE_NOTE
        assert inspect.cleandoc(Ipv4Rule.setIcmpRule.__doc__) == ICMP_RULE_NOTE + "\nA None value is a no-op and does not overwrite an existing icmpRule."
        assert inspect.cleandoc(Ipv4Rule.getInternetHeaderLength.__doc__) == INTERNET_HEADER_LENGTH_NOTE
        assert inspect.cleandoc(Ipv4Rule.setInternetHeaderLength.__doc__) == INTERNET_HEADER_LENGTH_NOTE + "\nA None value is a no-op and does not overwrite an existing internetHeaderLength."
        assert inspect.cleandoc(Ipv4Rule.getMoreFragments.__doc__) == MORE_FRAGMENTS_NOTE
        assert inspect.cleandoc(Ipv4Rule.setMoreFragments.__doc__) == MORE_FRAGMENTS_NOTE + "\nA None value is a no-op and does not overwrite an existing moreFragments."
        assert inspect.cleandoc(Ipv4Rule.getProtocol.__doc__) == PROTOCOL_NOTE
        assert inspect.cleandoc(Ipv4Rule.setProtocol.__doc__) == PROTOCOL_NOTE + "\nA None value is a no-op and does not overwrite an existing protocol."
        assert inspect.cleandoc(Ipv4Rule.getSourceIpAddress.__doc__) == SOURCE_IP_ADDRESS_NOTE
        assert inspect.cleandoc(Ipv4Rule.setSourceIpAddress.__doc__) == SOURCE_IP_ADDRESS_NOTE + "\nA None value is a no-op and does not overwrite an existing sourceIpAddress."
        assert inspect.cleandoc(Ipv4Rule.getSourceNetworkMask.__doc__) == SOURCE_NETWORK_MASK_NOTE
        assert inspect.cleandoc(Ipv4Rule.setSourceNetworkMask.__doc__) == SOURCE_NETWORK_MASK_NOTE + "\nA None value is a no-op and does not overwrite an existing sourceNetworkMask."
        assert inspect.cleandoc(Ipv4Rule.getTtlMax.__doc__) == TTL_MAX_NOTE
        assert inspect.cleandoc(Ipv4Rule.setTtlMax.__doc__) == TTL_MAX_NOTE + "\nA None value is a no-op and does not overwrite an existing ttlMax."
        assert inspect.cleandoc(Ipv4Rule.getTtlMin.__doc__) == TTL_MIN_NOTE
        assert inspect.cleandoc(Ipv4Rule.setTtlMin.__doc__) == TTL_MIN_NOTE + "\nA None value is a no-op and does not overwrite an existing ttlMin."

    def test_get_set_round_trip_and_none_noop(self):
        obj = Ipv4Rule()
        checksum_verification = _boolean(True)
        destination_ip_address = _ip4_address("192.168.0.1")
        destination_network_mask = _ip4_address("255.255.255.0")
        differentiated_service_code_point = _pos_int(46)
        do_not_fragment = _boolean(False)
        explicit_congestion_notification = _pos_int(2)
        icmp_rule = IcmpRule()
        internet_header_length = _pos_int(5)
        more_fragments = _boolean(True)
        protocol = _pos_int(6)
        source_ip_address = _ip4_address("10.0.0.1")
        source_network_mask = _ip4_address("255.0.0.0")
        ttl_max = _pos_int(64)
        ttl_min = _pos_int(32)

        assert obj.setChecksumVerification(checksum_verification) is obj
        assert obj.setDestinationIpAddress(destination_ip_address) is obj
        assert obj.setDestinationNetworkMask(destination_network_mask) is obj
        assert obj.setDifferentiatedServiceCodePoint(differentiated_service_code_point) is obj
        assert obj.setDoNotFragment(do_not_fragment) is obj
        assert obj.setExplicitCongestionNotification(explicit_congestion_notification) is obj
        assert obj.setIcmpRule(icmp_rule) is obj
        assert obj.setInternetHeaderLength(internet_header_length) is obj
        assert obj.setMoreFragments(more_fragments) is obj
        assert obj.setProtocol(protocol) is obj
        assert obj.setSourceIpAddress(source_ip_address) is obj
        assert obj.setSourceNetworkMask(source_network_mask) is obj
        assert obj.setTtlMax(ttl_max) is obj
        assert obj.setTtlMin(ttl_min) is obj

        assert obj.getChecksumVerification() is checksum_verification
        assert obj.getDestinationIpAddress() is destination_ip_address
        assert obj.getDestinationNetworkMask() is destination_network_mask
        assert obj.getDifferentiatedServiceCodePoint() is differentiated_service_code_point
        assert obj.getDoNotFragment() is do_not_fragment
        assert obj.getExplicitCongestionNotification() is explicit_congestion_notification
        assert obj.getIcmpRule() is icmp_rule
        assert obj.getInternetHeaderLength() is internet_header_length
        assert obj.getMoreFragments() is more_fragments
        assert obj.getProtocol() is protocol
        assert obj.getSourceIpAddress() is source_ip_address
        assert obj.getSourceNetworkMask() is source_network_mask
        assert obj.getTtlMax() is ttl_max
        assert obj.getTtlMin() is ttl_min

        obj.setChecksumVerification(None)
        obj.setDestinationIpAddress(None)
        obj.setDestinationNetworkMask(None)
        obj.setDifferentiatedServiceCodePoint(None)
        obj.setDoNotFragment(None)
        obj.setExplicitCongestionNotification(None)
        obj.setIcmpRule(None)
        obj.setInternetHeaderLength(None)
        obj.setMoreFragments(None)
        obj.setProtocol(None)
        obj.setSourceIpAddress(None)
        obj.setSourceNetworkMask(None)
        obj.setTtlMax(None)
        obj.setTtlMin(None)
        assert obj.getChecksumVerification() is checksum_verification
        assert obj.getDestinationIpAddress() is destination_ip_address
        assert obj.getDestinationNetworkMask() is destination_network_mask
        assert obj.getDifferentiatedServiceCodePoint() is differentiated_service_code_point
        assert obj.getDoNotFragment() is do_not_fragment
        assert obj.getExplicitCongestionNotification() is explicit_congestion_notification
        assert obj.getIcmpRule() is icmp_rule
        assert obj.getInternetHeaderLength() is internet_header_length
        assert obj.getMoreFragments() is more_fragments
        assert obj.getProtocol() is protocol
        assert obj.getSourceIpAddress() is source_ip_address
        assert obj.getSourceNetworkMask() is source_network_mask
        assert obj.getTtlMax() is ttl_max
        assert obj.getTtlMin() is ttl_min

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(Ipv4Rule.setChecksumVerification)
        assert hints["return"] is Ipv4Rule
        assert hints["value"] == Optional[Boolean]
        hints = typing.get_type_hints(Ipv4Rule.setDestinationIpAddress)
        assert hints["return"] is Ipv4Rule
        assert hints["value"] == Optional[Ip4AddressString]
        hints = typing.get_type_hints(Ipv4Rule.setIcmpRule)
        assert hints["return"] is Ipv4Rule
        assert hints["value"] == Optional[IcmpRule]
        hints = typing.get_type_hints(Ipv4Rule.setTtlMax)
        assert hints["return"] is Ipv4Rule
        assert hints["value"] == Optional[PositiveInteger]
