"""Tests for MultiplexedIPdu and SecureCommunication handler gaps."""
import xml.etree.ElementTree as ET
from unittest.mock import MagicMock
import pytest
from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


@pytest.fixture
def warning_parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser(options={"warning": True})


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _autosar_root():
    return AUTOSAR.getInstance()


class TestMultiplexedPartHandlers:
    """Tests for MultiplexedPart, DynamicPart, StaticPart handlers."""

    def test_readMultiplexedPartSegmentPositions_with_segment(self, parser):
        from armodel.models import DynamicPart
        part = DynamicPart()
        element = _snip(
            "<SEGMENT-POSITIONS>"
            "<SEGMENT-POSITION>"
            "<SEGMENT-BYTE-ORDER>MOST-SIGNIFICANT-BYTE-LAST</SEGMENT-BYTE-ORDER>"
            "<SEGMENT-LENGTH>8</SEGMENT-LENGTH>"
            "<SEGMENT-POSITION>0</SEGMENT-POSITION>"
            "</SEGMENT-POSITION>"
            "</SEGMENT-POSITIONS>",
        )
        parser.readMultiplexedPartSegmentPositions(element, part)
        positions = part.getSegmentPositions()
        assert len(positions) == 1
        assert positions[0].getSegmentByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-LAST"
        assert positions[0].getSegmentLength().getValue() == 8
        assert positions[0].getSegmentPosition().getValue() == 0

    def test_readMultiplexedPartSegmentPositions_empty(self, parser):
        from armodel.models import DynamicPart
        part = DynamicPart()
        element = _snip("")
        parser.readMultiplexedPartSegmentPositions(element, part)
        assert len(part.getSegmentPositions()) == 0

    def test_readMultiplexedPartSegmentPositions_unknown_warning(self, warning_parser):
        from armodel.models import DynamicPart
        part = DynamicPart()
        element = _snip(
            "<SEGMENT-POSITIONS>"
            "<UNKNOWN-SEGMENT>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-SEGMENT>"
            "</SEGMENT-POSITIONS>",
        )
        warning_parser.readMultiplexedPartSegmentPositions(element, part)
        assert len(part.getSegmentPositions()) == 0

    def test_readMultiplexedPart_delegates(self, parser):
        from armodel.models import DynamicPart
        part = DynamicPart()
        element = _snip(
            "<SEGMENT-POSITIONS>"
            "<SEGMENT-POSITION>"
            "<SEGMENT-LENGTH>4</SEGMENT-LENGTH>"
            "</SEGMENT-POSITION>"
            "</SEGMENT-POSITIONS>",
        )
        parser.readMultiplexedPart(element, part)
        assert len(part.getSegmentPositions()) == 1

    def test_readDynamicPartAlternative_sets_fields(self, parser):
        from armodel.models import DynamicPartAlternative
        alternative = DynamicPartAlternative()
        element = _snip(
            '<I-PDU-REF DEST="I-PDU">/pdus/DynAlt</I-PDU-REF>'
            '<INITIAL-DYNAMIC-PART>true</INITIAL-DYNAMIC-PART>'
            '<SELECTOR-FIELD-CODE>1</SELECTOR-FIELD-CODE>',
        )
        parser.readDynamicPartAlternative(element, alternative)
        assert alternative.getIPduRef() is not None
        assert alternative.getIPduRef().getValue() == "/pdus/DynAlt"
        assert alternative.getIPduRef().getDest() == "I-PDU"
        assert alternative.getInitialDynamicPart() is not None
        assert alternative.getSelectorFieldCode() is not None
        assert alternative.getSelectorFieldCode().getValue() == 1

    def test_readDynamicPartAlternative_empty(self, parser):
        from armodel.models import DynamicPartAlternative
        alternative = DynamicPartAlternative()
        element = _snip("")
        parser.readDynamicPartAlternative(element, alternative)
        assert alternative.getIPduRef() is None
        assert alternative.getInitialDynamicPart() is None
        assert alternative.getSelectorFieldCode() is None

    def test_readDynamicPartDynamicPartAlternatives_with_alternative(self, parser):
        from armodel.models import DynamicPart
        part = DynamicPart()
        element = _snip(
            "<DYNAMIC-PART-ALTERNATIVES>"
            "<DYNAMIC-PART-ALTERNATIVE>"
            '<I-PDU-REF DEST="I-PDU">/pdus/A1</I-PDU-REF>'
            '<SELECTOR-FIELD-CODE>2</SELECTOR-FIELD-CODE>'
            "</DYNAMIC-PART-ALTERNATIVE>"
            "</DYNAMIC-PART-ALTERNATIVES>",
        )
        parser.readDynamicPartDynamicPartAlternatives(element, part)
        alternatives = part.getDynamicPartAlternatives()
        assert len(alternatives) == 1
        assert alternatives[0].getIPduRef().getValue() == "/pdus/A1"

    def test_readDynamicPartDynamicPartAlternatives_unknown_warning(self, warning_parser):
        from armodel.models import DynamicPart
        part = DynamicPart()
        element = _snip(
            "<DYNAMIC-PART-ALTERNATIVES>"
            "<UNKNOWN-ALT>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-ALT>"
            "</DYNAMIC-PART-ALTERNATIVES>",
        )
        warning_parser.readDynamicPartDynamicPartAlternatives(element, part)
        assert len(part.getDynamicPartAlternatives()) == 0

    def test_readDynamicPart_delegates(self, parser):
        from armodel.models import DynamicPart
        part = DynamicPart()
        element = _snip(
            "<SEGMENT-POSITIONS>"
            "<SEGMENT-POSITION>"
            "<SEGMENT-LENGTH>4</SEGMENT-LENGTH>"
            "</SEGMENT-POSITION>"
            "</SEGMENT-POSITIONS>"
            "<DYNAMIC-PART-ALTERNATIVES>"
            "<DYNAMIC-PART-ALTERNATIVE>"
            '<SELECTOR-FIELD-CODE>1</SELECTOR-FIELD-CODE>'
            "</DYNAMIC-PART-ALTERNATIVE>"
            "</DYNAMIC-PART-ALTERNATIVES>",
        )
        parser.readDynamicPart(element, part)
        assert len(part.getSegmentPositions()) == 1
        assert len(part.getDynamicPartAlternatives()) == 1

    def test_readStaticPart_sets_fields(self, parser):
        from armodel.models import StaticPart
        part = StaticPart()
        element = _snip(
            "<SEGMENT-POSITIONS>"
            "<SEGMENT-POSITION>"
            "<SEGMENT-LENGTH>8</SEGMENT-LENGTH>"
            "</SEGMENT-POSITION>"
            "</SEGMENT-POSITIONS>"
            '<I-PDU-REF DEST="I-PDU">/pdus/Static</I-PDU-REF>',
        )
        parser.readStaticPart(element, part)
        assert len(part.getSegmentPositions()) == 1
        assert part.getIPduRef() is not None
        assert part.getIPduRef().getValue() == "/pdus/Static"


class TestMultiplexedIPduHandlers:
    """Tests for MultiplexedIPdu dynamic/static part handlers."""

    def test_readMultiplexedIPduDynamicParts_with_part(self, parser):
        from armodel.models import MultiplexedIPdu
        ipdu = MultiplexedIPdu(parent=_autosar_root(), short_name="muxIPdu")
        element = _snip(
            "<DYNAMIC-PARTS>"
            "<DYNAMIC-PART>"
            "<DYNAMIC-PART-ALTERNATIVES>"
            "<DYNAMIC-PART-ALTERNATIVE>"
            '<SELECTOR-FIELD-CODE>1</SELECTOR-FIELD-CODE>'
            "</DYNAMIC-PART-ALTERNATIVE>"
            "</DYNAMIC-PART-ALTERNATIVES>"
            "</DYNAMIC-PART>"
            "</DYNAMIC-PARTS>",
        )
        parser.readMultiplexedIPduDynamicParts(element, ipdu)
        assert ipdu.getDynamicPart() is not None
        assert len(ipdu.getDynamicPart().getDynamicPartAlternatives()) == 1

    def test_readMultiplexedIPduDynamicParts_unknown_warning(self, warning_parser):
        from armodel.models import MultiplexedIPdu
        ipdu = MultiplexedIPdu(parent=_autosar_root(), short_name="muxIPdu")
        element = _snip(
            "<DYNAMIC-PARTS>"
            "<UNKNOWN-PART>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-PART>"
            "</DYNAMIC-PARTS>",
        )
        warning_parser.readMultiplexedIPduDynamicParts(element, ipdu)
        assert ipdu.getDynamicPart() is None

    def test_readMultiplexedIPduStaticParts_with_part(self, parser):
        from armodel.models import MultiplexedIPdu
        ipdu = MultiplexedIPdu(parent=_autosar_root(), short_name="muxIPdu")
        element = _snip(
            "<STATIC-PARTS>"
            "<STATIC-PART>"
            '<I-PDU-REF DEST="I-PDU">/pdus/Static</I-PDU-REF>'
            "</STATIC-PART>"
            "</STATIC-PARTS>",
        )
        parser.readMultiplexedIPduStaticParts(element, ipdu)
        assert ipdu.getStaticPart() is not None
        assert ipdu.getStaticPart().getIPduRef().getValue() == "/pdus/Static"

    def test_readMultiplexedIPduStaticParts_unknown_warning(self, warning_parser):
        from armodel.models import MultiplexedIPdu
        ipdu = MultiplexedIPdu(parent=_autosar_root(), short_name="muxIPdu")
        element = _snip(
            "<STATIC-PARTS>"
            "<UNKNOWN-PART>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-PART>"
            "</STATIC-PARTS>",
        )
        warning_parser.readMultiplexedIPduStaticParts(element, ipdu)
        assert ipdu.getStaticPart() is None

    def test_readMultiplexedIPdu_full(self, parser):
        from armodel.models import MultiplexedIPdu
        ipdu = MultiplexedIPdu(parent=_autosar_root(), short_name="muxIPdu")
        element = _snip(
            "<SHORT-NAME>muxIPdu</SHORT-NAME>"
            "<DYNAMIC-PARTS>"
            "<DYNAMIC-PART>"
            "<DYNAMIC-PART-ALTERNATIVES>"
            "<DYNAMIC-PART-ALTERNATIVE>"
            '<SELECTOR-FIELD-CODE>1</SELECTOR-FIELD-CODE>'
            "</DYNAMIC-PART-ALTERNATIVE>"
            "</DYNAMIC-PART-ALTERNATIVES>"
            "</DYNAMIC-PART>"
            "</DYNAMIC-PARTS>"
            "<SELECTOR-FIELD-BYTE-ORDER>MOST-SIGNIFICANT-BYTE-LAST</SELECTOR-FIELD-BYTE-ORDER>"
            "<SELECTOR-FIELD-LENGTH>4</SELECTOR-FIELD-LENGTH>"
            "<SELECTOR-FIELD-START-POSITION>0</SELECTOR-FIELD-START-POSITION>"
            "<STATIC-PARTS>"
            "<STATIC-PART>"
            '<I-PDU-REF DEST="I-PDU">/pdus/Static</I-PDU-REF>'
            "</STATIC-PART>"
            "</STATIC-PARTS>"
            "<TRIGGER-MODE>ONE-SHOT</TRIGGER-MODE>"
            "<UNUSED-BIT-PATTERN>255</UNUSED-BIT-PATTERN>",
            root_tag="MULTIPLEXED-I-PDU",
        )
        parser.readMultiplexedIPdu(element, ipdu)
        assert ipdu.getShortName() == "muxIPdu"
        assert ipdu.getDynamicPart() is not None
        assert ipdu.getStaticPart() is not None
        assert ipdu.getSelectorFieldByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-LAST"
        assert ipdu.getSelectorFieldLength().getValue() == 4
        assert ipdu.getSelectorFieldStartPosition().getValue() == 0
        assert ipdu.getTriggerMode().getValue() == "ONE-SHOT"
        assert ipdu.getUnusedBitPattern().getValue() == 255


class TestUserDefinedAndGeneralPurposePduHandlers:
    """Tests for UserDefinedIPdu, UserDefinedPdu, GeneralPurposePdu, GeneralPurposeIPdu."""

    def test_readUserDefinedIPdu_sets_cddType(self, parser):
        from armodel.models import UserDefinedIPdu
        ipdu = UserDefinedIPdu(parent=_autosar_root(), short_name="udIPdu")
        element = _snip(
            "<SHORT-NAME>udIPdu</SHORT-NAME>"
            "<CDD-TYPE>MyCdd</CDD-TYPE>",
            root_tag="USER-DEFINED-I-PDU",
        )
        parser.readUserDefinedIPdu(element, ipdu)
        assert ipdu.getShortName() == "udIPdu"
        assert ipdu.getCddType() is not None
        assert ipdu.getCddType().getValue() == "MyCdd"

    def test_readUserDefinedIPdu_empty(self, parser):
        from armodel.models import UserDefinedIPdu
        ipdu = UserDefinedIPdu(parent=_autosar_root(), short_name="udIPdu")
        element = _snip(
            "<SHORT-NAME>udIPdu</SHORT-NAME>",
            root_tag="USER-DEFINED-I-PDU",
        )
        parser.readUserDefinedIPdu(element, ipdu)
        assert ipdu.getCddType() is None

    def test_readUserDefinedPdu_sets_cddType(self, parser):
        from armodel.models import UserDefinedPdu
        pdu = UserDefinedPdu(parent=_autosar_root(), short_name="udPdu")
        element = _snip(
            "<SHORT-NAME>udPdu</SHORT-NAME>"
            "<CDD-TYPE>MyCdd</CDD-TYPE>",
            root_tag="USER-DEFINED-PDU",
        )
        parser.readUserDefinedPdu(element, pdu)
        assert pdu.getShortName() == "udPdu"
        assert pdu.getCddType() is not None
        assert pdu.getCddType().getValue() == "MyCdd"

    def test_readUserDefinedPdu_empty(self, parser):
        from armodel.models import UserDefinedPdu
        pdu = UserDefinedPdu(parent=_autosar_root(), short_name="udPdu")
        element = _snip(
            "<SHORT-NAME>udPdu</SHORT-NAME>",
            root_tag="USER-DEFINED-PDU",
        )
        parser.readUserDefinedPdu(element, pdu)
        assert pdu.getCddType() is None

    def test_readGeneralPurposePdu_minimal(self, parser):
        from armodel.models import GeneralPurposePdu
        pdu = GeneralPurposePdu(parent=_autosar_root(), short_name="gpPdu")
        element = _snip(
            "<SHORT-NAME>gpPdu</SHORT-NAME>",
            root_tag="GENERAL-PURPOSE-PDU",
        )
        parser.readGeneralPurposePdu(element, pdu)
        assert pdu.getShortName() == "gpPdu"

    def test_readGeneralPurposeIPdu_minimal(self, parser):
        from armodel.models import GeneralPurposeIPdu
        ipdu = GeneralPurposeIPdu(parent=_autosar_root(), short_name="gpIPdu")
        element = _snip(
            "<SHORT-NAME>gpIPdu</SHORT-NAME>",
            root_tag="GENERAL-PURPOSE-I-PDU",
        )
        parser.readGeneralPurposeIPdu(element, ipdu)
        assert ipdu.getShortName() == "gpIPdu"


class TestSecureCommunicationHandlers:
    """Tests for SecureCommunication props handlers."""

    def test_readSecureCommunicationAuthenticationProps_with_mock(self, parser):
        props = MagicMock()
        element = _snip(
            "<SHORT-NAME>authProps</SHORT-NAME>"
            "<AUTH-ALGORITHM>AES-128</AUTH-ALGORITHM>"
            "<AUTH-INFO-TX-LENGTH>16</AUTH-INFO-TX-LENGTH>",
            root_tag="SECURE-COMMUNICATION-AUTHENTICATION-PROPS",
        )
        parser.readSecureCommunicationAuthenticationProps(element, props)
        assert props.setAuthAlgorithm.called
        assert props.setAuthAlgorithm.return_value.setAuthInfoTxLength.called

    def test_readSecureCommunicationAuthenticationProps_empty_with_mock(self, parser):
        props = MagicMock()
        element = _snip(
            "<SHORT-NAME>authProps</SHORT-NAME>",
            root_tag="SECURE-COMMUNICATION-AUTHENTICATION-PROPS",
        )
        parser.readSecureCommunicationAuthenticationProps(element, props)
        assert props.setAuthAlgorithm.called
        assert props.setAuthAlgorithm.return_value.setAuthInfoTxLength.called

    def test_readSecureCommunicationPropsSetAuthenticationProps_with_props(self, parser):
        props_set = MagicMock()
        props_set.createSecureCommunicationAuthenticationProps.return_value = MagicMock()
        element = _snip(
            "<AUTHENTICATION-PROPSS>"
            "<SECURE-COMMUNICATION-AUTHENTICATION-PROPS>"
            "<SHORT-NAME>authProps</SHORT-NAME>"
            "<AUTH-ALGORITHM>AES-128</AUTH-ALGORITHM>"
            "</SECURE-COMMUNICATION-AUTHENTICATION-PROPS>"
            "</AUTHENTICATION-PROPSS>",
        )
        parser.readSecureCommunicationPropsSetAuthenticationProps(element, props_set)
        props_set.createSecureCommunicationAuthenticationProps.assert_called_once_with("authProps")

    def test_readSecureCommunicationPropsSetAuthenticationProps_unknown_warning(self, warning_parser):
        from armodel.models import SecureCommunicationPropsSet
        props_set = SecureCommunicationPropsSet(parent=_autosar_root(), short_name="propsSet")
        element = _snip(
            "<AUTHENTICATION-PROPSS>"
            "<UNKNOWN-AUTH-PROPS>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-AUTH-PROPS>"
            "</AUTHENTICATION-PROPSS>",
        )
        warning_parser.readSecureCommunicationPropsSetAuthenticationProps(element, props_set)

    def test_readSecureCommunicationFreshnessProps_sets_fields(self, parser):
        from armodel.models import SecureCommunicationFreshnessProps
        props = SecureCommunicationFreshnessProps(parent=_autosar_root(), short_name="freshProps")
        element = _snip(
            "<SHORT-NAME>freshProps</SHORT-NAME>"
            "<FRESHNESS-VALUE-LENGTH>16</FRESHNESS-VALUE-LENGTH>"
            "<FRESHNESS-VALUE-TX-LENGTH>8</FRESHNESS-VALUE-TX-LENGTH>",
            root_tag="SECURE-COMMUNICATION-FRESHNESS-PROPS",
        )
        parser.readSecureCommunicationFreshnessProps(element, props)
        assert props.getShortName() == "freshProps"
        assert props.getFreshnessValueLength() is not None
        assert props.getFreshnessValueLength().getValue() == "16"
        assert props.getFreshnessValueTxLength() is not None
        assert props.getFreshnessValueTxLength().getValue() == 8

    def test_readSecureCommunicationFreshnessProps_empty(self, parser):
        from armodel.models import SecureCommunicationFreshnessProps
        props = SecureCommunicationFreshnessProps(parent=_autosar_root(), short_name="freshProps")
        element = _snip(
            "<SHORT-NAME>freshProps</SHORT-NAME>",
            root_tag="SECURE-COMMUNICATION-FRESHNESS-PROPS",
        )
        parser.readSecureCommunicationFreshnessProps(element, props)
        assert props.getFreshnessValueLength() is None
        assert props.getFreshnessValueTxLength() is None

    def test_readSecureCommunicationPropsSetFreshnessProps_with_props(self, parser):
        props_set = MagicMock()
        props_set.createSecureCommunicationFreshnessProps.return_value = MagicMock()
        element = _snip(
            "<FRESHNESS-PROPSS>"
            "<SECURE-COMMUNICATION-FRESHNESS-PROPS>"
            "<SHORT-NAME>freshProps</SHORT-NAME>"
            "<FRESHNESS-VALUE-LENGTH>16</FRESHNESS-VALUE-LENGTH>"
            "</SECURE-COMMUNICATION-FRESHNESS-PROPS>"
            "</FRESHNESS-PROPSS>",
        )
        parser.readSecureCommunicationPropsSetFreshnessProps(element, props_set)
        props_set.createSecureCommunicationFreshnessProps.assert_called_once_with("freshProps")

    def test_readSecureCommunicationPropsSetFreshnessProps_unknown_warning(self, warning_parser):
        from armodel.models import SecureCommunicationPropsSet
        props_set = SecureCommunicationPropsSet(parent=_autosar_root(), short_name="propsSet")
        element = _snip(
            "<FRESHNESS-PROPSS>"
            "<UNKNOWN-FRESH-PROPS>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-FRESH-PROPS>"
            "</FRESHNESS-PROPSS>",
        )
        warning_parser.readSecureCommunicationPropsSetFreshnessProps(element, props_set)

    def test_readSecureCommunicationPropsSet_minimal(self, parser):
        from armodel.models import SecureCommunicationPropsSet
        props_set = SecureCommunicationPropsSet(parent=_autosar_root(), short_name="propsSet")
        element = _snip(
            "<SHORT-NAME>propsSet</SHORT-NAME>",
            root_tag="SECURE-COMMUNICATION-PROPS-SET",
        )
        parser.readSecureCommunicationPropsSet(element, props_set)
        assert props_set.getShortName() == "propsSet"


class TestSoAdRoutingGroupHandler:
    """Tests for readSoAdRoutingGroup."""

    def test_readSoAdRoutingGroup_sets_eventGroupControlType(self, parser):
        from armodel.models import SoAdRoutingGroup
        group = SoAdRoutingGroup(parent=_autosar_root(), short_name="routeGroup")
        element = _snip(
            "<SHORT-NAME>routeGroup</SHORT-NAME>"
            "<EVENT-GROUP-CONTROL-TYPE>POSITIVE</EVENT-GROUP-CONTROL-TYPE>",
            root_tag="SO-AD-ROUTING-GROUP",
        )
        parser.readSoAdRoutingGroup(element, group)
        assert group.getShortName() == "routeGroup"
        assert group.getEventGroupControlType() is not None
        assert group.getEventGroupControlType().getValue() == "POSITIVE"

    def test_readSoAdRoutingGroup_empty(self, parser):
        from armodel.models import SoAdRoutingGroup
        group = SoAdRoutingGroup(parent=_autosar_root(), short_name="routeGroup")
        element = _snip(
            "<SHORT-NAME>routeGroup</SHORT-NAME>",
            root_tag="SO-AD-ROUTING-GROUP",
        )
        parser.readSoAdRoutingGroup(element, group)
        assert group.getEventGroupControlType() is None


class TestDoIpHandlers:
    """Tests for DoIpLogicAddress, DoIpTpConnection, DoIpTpConfig handlers."""

    def test_readDoIpLogicAddress_sets_address(self, parser):
        from armodel.models import DoIpLogicAddress
        address = DoIpLogicAddress(parent=_autosar_root(), short_name="doIpAddr")
        element = _snip(
            "<SHORT-NAME>doIpAddr</SHORT-NAME>"
            "<ADDRESS>0x0E80</ADDRESS>",
            root_tag="DO-IP-LOGIC-ADDRESS",
        )
        parser.readDoIpLogicAddress(element, address)
        assert address.getShortName() == "doIpAddr"
        assert address.getAddress() is not None
        assert address.getAddress().getValue() == 0x0E80

    def test_readDoIpLogicAddress_empty(self, parser):
        from armodel.models import DoIpLogicAddress
        address = DoIpLogicAddress(parent=_autosar_root(), short_name="doIpAddr")
        element = _snip(
            "<SHORT-NAME>doIpAddr</SHORT-NAME>",
            root_tag="DO-IP-LOGIC-ADDRESS",
        )
        parser.readDoIpLogicAddress(element, address)
        assert address.getAddress() is None

    def test_readDoIpTpConfigDoIpLogicAddresses_with_address(self, parser):
        from armodel.models import DoIpTpConfig
        config = DoIpTpConfig(parent=_autosar_root(), short_name="doIpConfig")
        element = _snip(
            "<DO-IP-LOGIC-ADDRESSS>"
            "<DO-IP-LOGIC-ADDRESS>"
            "<SHORT-NAME>logicAddr</SHORT-NAME>"
            "<ADDRESS>0x0E80</ADDRESS>"
            "</DO-IP-LOGIC-ADDRESS>"
            "</DO-IP-LOGIC-ADDRESSS>",
        )
        parser.readDoIpTpConfigDoIpLogicAddresses(element, config)
        addresses = config.getDoIpLogicAddresses()
        assert len(addresses) == 1
        assert addresses[0].getShortName() == "logicAddr"
        assert addresses[0].getAddress().getValue() == 0x0E80

    def test_readDoIpTpConfigDoIpLogicAddresses_unknown_warning(self, warning_parser):
        from armodel.models import DoIpTpConfig
        config = DoIpTpConfig(parent=_autosar_root(), short_name="doIpConfig")
        element = _snip(
            "<DO-IP-LOGIC-ADDRESSS>"
            "<UNKNOWN-ADDRESS>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-ADDRESS>"
            "</DO-IP-LOGIC-ADDRESSS>",
        )
        warning_parser.readDoIpTpConfigDoIpLogicAddresses(element, config)
        assert len(config.getDoIpLogicAddresses()) == 0

    def test_readDoIpTpConnection_sets_refs(self, parser):
        from armodel.models import DoIpTpConnection
        connection = DoIpTpConnection()
        element = _snip(
            '<DO-IP-SOURCE-ADDRESS-REF DEST="DO-IP-LOGIC-ADDRESS">/doIp/srcAddr</DO-IP-SOURCE-ADDRESS-REF>'
            '<DO-IP-TARGET-ADDRESS-REF DEST="DO-IP-LOGIC-ADDRESS">/doIp/tgtAddr</DO-IP-TARGET-ADDRESS-REF>'
            '<TP-SDU-REF DEST="I-PDU">/pdus/sdu</TP-SDU-REF>',
            root_tag="DO-IP-TP-CONNECTION",
        )
        parser.readDoIpTpConnection(element, connection)
        assert connection.getDoIpSourceAddressRef() is not None
        assert connection.getDoIpSourceAddressRef().getValue() == "/doIp/srcAddr"
        assert connection.getDoIpTargetAddressRef() is not None
        assert connection.getDoIpTargetAddressRef().getValue() == "/doIp/tgtAddr"
        assert connection.getTpSduRef() is not None
        assert connection.getTpSduRef().getValue() == "/pdus/sdu"

    def test_readDoIpTpConnection_empty(self, parser):
        from armodel.models import DoIpTpConnection
        connection = DoIpTpConnection()
        element = _snip("", root_tag="DO-IP-TP-CONNECTION")
        parser.readDoIpTpConnection(element, connection)
        assert connection.getDoIpSourceAddressRef() is None
        assert connection.getDoIpTargetAddressRef() is None
        assert connection.getTpSduRef() is None

    def test_readDoIpTpConfigTpConnections_with_connection(self, parser):
        from armodel.models import DoIpTpConfig
        config = DoIpTpConfig(parent=_autosar_root(), short_name="doIpConfig")
        element = _snip(
            "<TP-CONNECTIONS>"
            "<DO-IP-TP-CONNECTION>"
            '<DO-IP-SOURCE-ADDRESS-REF DEST="DO-IP-LOGIC-ADDRESS">/doIp/src</DO-IP-SOURCE-ADDRESS-REF>'
            '<DO-IP-TARGET-ADDRESS-REF DEST="DO-IP-LOGIC-ADDRESS">/doIp/tgt</DO-IP-TARGET-ADDRESS-REF>'
            "</DO-IP-TP-CONNECTION>"
            "</TP-CONNECTIONS>",
        )
        parser.readDoIpTpConfigTpConnections(element, config)
        connections = config.getTpConnections()
        assert len(connections) == 1
        assert connections[0].getDoIpSourceAddressRef().getValue() == "/doIp/src"
        assert connections[0].getDoIpTargetAddressRef().getValue() == "/doIp/tgt"

    def test_readDoIpTpConfigTpConnections_unknown_warning(self, warning_parser):
        from armodel.models import DoIpTpConfig
        config = DoIpTpConfig(parent=_autosar_root(), short_name="doIpConfig")
        element = _snip(
            "<TP-CONNECTIONS>"
            "<UNKNOWN-CONNECTION>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-CONNECTION>"
            "</TP-CONNECTIONS>",
        )
        warning_parser.readDoIpTpConfigTpConnections(element, config)
        assert len(config.getTpConnections()) == 0
