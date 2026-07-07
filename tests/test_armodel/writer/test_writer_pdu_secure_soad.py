"""Tests for writer PDU, SecureCommunication, SoAd, and DoIp handlers."""
import xml.etree.cElementTree as ET
from unittest.mock import MagicMock
import pytest
from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    SegmentPosition,
    MultiplexedPart,
    StaticPart,
    DynamicPartAlternative,
    DynamicPart,
    MultiplexedIPdu,
    UserDefinedIPdu,
    UserDefinedPdu,
    GeneralPurposePdu,
    GeneralPurposeIPdu,
    SecureCommunicationPropsSet,
    SecureCommunicationAuthenticationProps,
    SecureCommunicationFreshnessProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    SoAdRoutingGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    DoIpLogicAddress,
    DoIpTpConnection,
    DoIpTpConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    ARBoolean,
    Integer,
    PositiveInteger,
    RefType,
    ARNumerical,
)


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _pkg():
    autosar = AUTOSAR.getInstance()
    return autosar.createARPackage("Pkg")


def _literal(text):
    val = ARLiteral()
    val.setValue(text)
    return val


def _int(text):
    val = Integer()
    val.setValue(text)
    return val


def _pos_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _bool(text):
    val = ARBoolean()
    val.setValue(text)
    return val


def _numerical(text):
    val = ARNumerical()
    val.setValue(text)
    return val


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestWritePdu:
    def test_with_all_attributes(self, writer):
        pkg = _pkg()
        pdu = pkg.createGeneralPurposePdu("pdu")
        pdu.setHasDynamicLength(_bool("true"))
        pdu.setLength(_int("64"))
        parent = _parent()
        child_elem = ET.SubElement(parent, "GENERAL-PURPOSE-PDU")
        writer.writePdu(child_elem, pdu)
        assert child_elem.find("SHORT-NAME").text == "pdu"
        assert child_elem.find("HAS-DYNAMIC-LENGTH").text == "true"
        assert child_elem.find("LENGTH").text == "64"

    def test_with_optional_attributes(self, writer):
        pkg = _pkg()
        pdu = pkg.createGeneralPurposePdu("pdu")
        parent = _parent()
        child_elem = ET.SubElement(parent, "GENERAL-PURPOSE-PDU")
        writer.writePdu(child_elem, pdu)
        assert child_elem.find("SHORT-NAME").text == "pdu"
        assert child_elem.find("HAS-DYNAMIC-LENGTH") is None
        assert child_elem.find("LENGTH") is None


class TestWriteIPdu:
    def test_basic_ipdu(self, writer):
        pkg = _pkg()
        ipdu = pkg.createGeneralPurposeIPdu("ipdu")
        ipdu.setLength(_int("128"))
        parent = _parent()
        child_elem = ET.SubElement(parent, "GENERAL-PURPOSE-I-PDU")
        writer.writeIPdu(child_elem, ipdu)
        assert child_elem.find("SHORT-NAME").text == "ipdu"
        assert child_elem.find("LENGTH").text == "128"


class TestWriteSegmentPosition:
    def test_none(self, writer):
        parent = _parent()
        writer.writeSegmentPosition(parent, None)
        assert len(parent) == 0

    def test_with_all_attributes(self, writer):
        position = SegmentPosition()
        position.setSegmentByteOrder(_literal("OPAQUE"))
        position.setSegmentLength(_int("8"))
        position.setSegmentPosition(_int("0"))
        parent = _parent()
        writer.writeSegmentPosition(parent, position)
        child = parent.find("SEGMENT-POSITION")
        assert child is not None
        assert child.find("SEGMENT-BYTE-ORDER").text == "OPAQUE"
        assert child.find("SEGMENT-LENGTH").text == "8"
        assert child.find("SEGMENT-POSITION").text == "0"

    def test_with_optional_attributes(self, writer):
        position = SegmentPosition()
        parent = _parent()
        writer.writeSegmentPosition(parent, position)
        child = parent.find("SEGMENT-POSITION")
        assert child is not None
        assert child.find("SEGMENT-BYTE-ORDER") is None
        assert child.find("SEGMENT-LENGTH") is None


class TestWriteMultiplexedPartSegmentPositions:
    def test_empty(self, writer):
        part = StaticPart()
        parent = _parent()
        writer.writeMultiplexedPartSegmentPositions(parent, part)
        assert len(parent) == 0

    def test_with_positions(self, writer):
        part = StaticPart()
        pos1 = SegmentPosition()
        pos1.setSegmentLength(_int("8"))
        pos2 = SegmentPosition()
        pos2.setSegmentLength(_int("16"))
        part.addSegmentPosition(pos1)
        part.addSegmentPosition(pos2)
        parent = _parent()
        writer.writeMultiplexedPartSegmentPositions(parent, part)
        positions_elem = parent.find("SEGMENT-POSITIONS")
        assert positions_elem is not None
        positions = positions_elem.findall("SEGMENT-POSITION")
        assert len(positions) == 2


class TestWriteMultiplexedPart:
    def test_with_positions(self, writer):
        part = StaticPart()
        pos = SegmentPosition()
        pos.setSegmentLength(_int("8"))
        part.addSegmentPosition(pos)
        parent = _parent()
        writer.writeMultiplexedPart(parent, part)
        positions_elem = parent.find("SEGMENT-POSITIONS")
        assert positions_elem is not None


class TestWriteDynamicPartAlternative:
    def test_none(self, writer):
        parent = _parent()
        writer.writeDynamicPartAlternative(parent, None)
        assert len(parent) == 0

    def test_with_all_attributes(self, writer):
        alt = DynamicPartAlternative()
        alt.setIPduRef(_ref("I-PDU", "/ipdu"))
        alt.setInitialDynamicPart(_bool("true"))
        alt.setSelectorFieldCode(_int("1"))
        parent = _parent()
        writer.writeDynamicPartAlternative(parent, alt)
        child = parent.find("DYNAMIC-PART-ALTERNATIVE")
        assert child is not None
        assert child.find("I-PDU-REF") is not None
        assert child.find("INITIAL-DYNAMIC-PART").text == "true"
        assert child.find("SELECTOR-FIELD-CODE").text == "1"


class TestWriteDynamicPartDynamicPartAlternatives:
    def test_empty(self, writer):
        part = DynamicPart()
        parent = _parent()
        writer.writeDynamicPartDynamicPartAlternatives(parent, part)
        assert len(parent) == 0

    def test_with_alternatives(self, writer):
        part = DynamicPart()
        alt1 = DynamicPartAlternative()
        alt1.setSelectorFieldCode(_int("1"))
        alt2 = DynamicPartAlternative()
        alt2.setSelectorFieldCode(_int("2"))
        part.addDynamicPartAlternative(alt1)
        part.addDynamicPartAlternative(alt2)
        parent = _parent()
        writer.writeDynamicPartDynamicPartAlternatives(parent, part)
        alts_elem = parent.find("DYNAMIC-PART-ALTERNATIVES")
        assert alts_elem is not None
        alts = alts_elem.findall("DYNAMIC-PART-ALTERNATIVE")
        assert len(alts) == 2


class TestWriteDynamicPart:
    def test_full(self, writer):
        part = DynamicPart()
        alt = DynamicPartAlternative()
        alt.setSelectorFieldCode(_int("1"))
        part.addDynamicPartAlternative(alt)
        pos = SegmentPosition()
        pos.setSegmentLength(_int("8"))
        part.addSegmentPosition(pos)
        parent = _parent()
        writer.writeDynamicPart(parent, part)
        child = parent.find("DYNAMIC-PART")
        assert child is not None
        assert child.find("SEGMENT-POSITIONS") is not None
        assert child.find("DYNAMIC-PART-ALTERNATIVES") is not None


class TestWriteMultiplexedIPduDynamicParts:
    def test_none(self, writer):
        pkg = _pkg()
        ipdu = MultiplexedIPdu(pkg, "ipdu")
        parent = _parent()
        writer.writeMultiplexedIPduDynamicParts(parent, ipdu)
        assert len(parent) == 0

    def test_with_dynamic_part(self, writer):
        pkg = _pkg()
        ipdu = MultiplexedIPdu(pkg, "ipdu")
        part = DynamicPart()
        alt = DynamicPartAlternative()
        alt.setSelectorFieldCode(_int("1"))
        part.addDynamicPartAlternative(alt)
        ipdu.setDynamicPart(part)
        parent = _parent()
        writer.writeMultiplexedIPduDynamicParts(parent, ipdu)
        parts_elem = parent.find("DYNAMIC-PARTS")
        assert parts_elem is not None
        assert parts_elem.find("DYNAMIC-PART") is not None


class TestWriteStaticPart:
    def test_full(self, writer):
        part = StaticPart()
        part.setIPduRef(_ref("I-PDU", "/ipdu"))
        pos = SegmentPosition()
        pos.setSegmentLength(_int("8"))
        part.addSegmentPosition(pos)
        parent = _parent()
        writer.writeStaticPart(parent, part)
        child = parent.find("STATIC-PART")
        assert child is not None
        assert child.find("SEGMENT-POSITIONS") is not None
        assert child.find("I-PDU-REF") is not None


class TestWriteMultiplexedIPduStaticParts:
    def test_none(self, writer):
        pkg = _pkg()
        ipdu = MultiplexedIPdu(pkg, "ipdu")
        parent = _parent()
        writer.writeMultiplexedIPduStaticParts(parent, ipdu)
        assert len(parent) == 0

    def test_with_static_part(self, writer):
        pkg = _pkg()
        ipdu = MultiplexedIPdu(pkg, "ipdu")
        part = StaticPart()
        part.setIPduRef(_ref("I-PDU", "/ipdu"))
        ipdu.setStaticPart(part)
        parent = _parent()
        writer.writeMultiplexedIPduStaticParts(parent, ipdu)
        parts_elem = parent.find("STATIC-PARTS")
        assert parts_elem is not None
        assert parts_elem.find("STATIC-PART") is not None


class TestWriteMultiplexedIPdu:
    def test_full(self, writer):
        pkg = _pkg()
        ipdu = MultiplexedIPdu(pkg, "muxIpdu")
        ipdu.setLength(_int("64"))
        ipdu.setSelectorFieldByteOrder(_literal("OPAQUE"))
        ipdu.setSelectorFieldLength(_int("4"))
        ipdu.setSelectorFieldStartPosition(_int("0"))
        ipdu.setTriggerMode(_literal("TRIGGERED"))
        ipdu.setUnusedBitPattern(_int("0"))
        dyn_part = DynamicPart()
        alt = DynamicPartAlternative()
        alt.setSelectorFieldCode(_int("1"))
        dyn_part.addDynamicPartAlternative(alt)
        ipdu.setDynamicPart(dyn_part)
        static_part = StaticPart()
        static_part.setIPduRef(_ref("I-PDU", "/static"))
        ipdu.setStaticPart(static_part)
        parent = _parent()
        writer.writeMultiplexedIPdu(parent, ipdu)
        child = parent.find("MULTIPLEXED-I-PDU")
        assert child is not None
        assert child.find("SHORT-NAME").text == "muxIpdu"
        assert child.find("LENGTH").text == "64"
        assert child.find("SELECTOR-FIELD-BYTE-ORDER").text == "OPAQUE"
        assert child.find("SELECTOR-FIELD-LENGTH").text == "4"
        assert child.find("SELECTOR-FIELD-START-POSITION").text == "0"
        assert child.find("TRIGGER-MODE").text == "TRIGGERED"
        assert child.find("UNUSED-BIT-PATTERN").text == "0"
        assert child.find("DYNAMIC-PARTS") is not None
        assert child.find("STATIC-PARTS") is not None


class TestWriteUserDefinedIPdu:
    def test_full(self, writer):
        pkg = _pkg()
        ipdu = UserDefinedIPdu(pkg, "userIpdu")
        ipdu.setLength(_int("32"))
        ipdu.setCddType(_literal("MyCDD"))
        parent = _parent()
        writer.writeUserDefinedIPdu(parent, ipdu)
        child = parent.find("USER-DEFINED-I-PDU")
        assert child is not None
        assert child.find("SHORT-NAME").text == "userIpdu"
        assert child.find("LENGTH").text == "32"
        assert child.find("CDD-TYPE").text == "MyCDD"


class TestWriteUserDefinedPdu:
    def test_full(self, writer):
        pkg = _pkg()
        pdu = UserDefinedPdu(pkg, "userPdu")
        pdu.setLength(_int("32"))
        pdu.setCddType(_literal("MyCDD"))
        parent = _parent()
        writer.writeUserDefinedPdu(parent, pdu)
        child = parent.find("USER-DEFINED-PDU")
        assert child is not None
        assert child.find("SHORT-NAME").text == "userPdu"
        assert child.find("LENGTH").text == "32"
        assert child.find("CDD-TYPE").text == "MyCDD"


class TestWriteGeneralPurposePdu:
    def test_full(self, writer):
        pkg = _pkg()
        pdu = GeneralPurposePdu(pkg, "gpPdu")
        pdu.setLength(_int("64"))
        parent = _parent()
        writer.writeGeneralPurposePdu(parent, pdu)
        child = parent.find("GENERAL-PURPOSE-PDU")
        assert child is not None
        assert child.find("SHORT-NAME").text == "gpPdu"
        assert child.find("LENGTH").text == "64"


class TestWriteGeneralPurposeIPdu:
    def test_full(self, writer):
        pkg = _pkg()
        ipdu = GeneralPurposeIPdu(pkg, "gpIpdu")
        ipdu.setLength(_int("128"))
        parent = _parent()
        writer.writeGeneralPurposeIPdu(parent, ipdu)
        child = parent.find("GENERAL-PURPOSE-I-PDU")
        assert child is not None
        assert child.find("SHORT-NAME").text == "gpIpdu"
        assert child.find("LENGTH").text == "128"


class TestWriteSecureCommunicationAuthenticationProps:
    def test_with_mock(self, writer):
        props = MagicMock()
        auth_algo = MagicMock()
        auth_algo.setValue.return_value = None
        props.getAuthAlgorithm.return_value = auth_algo
        tx_len = MagicMock()
        tx_len.setValue.return_value = None
        props.getAuthInfoTxLength.return_value = tx_len
        parent = _parent()
        writer.writeSecureCommunicationAuthenticationProps(parent, props)
        child = parent.find("SECURE-COMMUNICATION-AUTHENTICATION-PROPS")
        assert child is not None


class TestWriteSecureCommunicationPropsSetAuthenticationProps:
    def test_empty(self, writer):
        props_set = MagicMock()
        props_set.getAuthenticationProps.return_value = []
        parent = _parent()
        writer.writeSecureCommunicationPropsSetAuthenticationProps(
            parent, props_set
        )
        assert len(parent) == 0

    def test_with_props(self, writer):
        props_set = MagicMock()
        pkg = _pkg()
        props = SecureCommunicationAuthenticationProps(pkg, "authProps")
        auth_algo = MagicMock()
        props.getAuthAlgorithm = MagicMock(return_value=auth_algo)
        tx_len = MagicMock()
        props.getAuthInfoTxLength = MagicMock(return_value=tx_len)
        props_set.getAuthenticationProps.return_value = [props]
        parent = _parent()
        writer.writeSecureCommunicationPropsSetAuthenticationProps(
            parent, props_set
        )
        props_elem = parent.find("AUTHENTICATION-PROPSS")
        assert props_elem is not None
        auth_props = props_elem.find("SECURE-COMMUNICATION-AUTHENTICATION-PROPS")
        assert auth_props is not None
        assert auth_props.find("SHORT-NAME").text == "authProps"


class TestWriteSecureCommunicationFreshnessProps:
    def test_with_real_props(self, writer):
        pkg = _pkg()
        props = SecureCommunicationFreshnessProps(pkg, "freshProps")
        props.setFreshnessValueLength(_pos_int("16"))
        props.setFreshnessValueTxLength(_pos_int("8"))
        parent = _parent()
        writer.writeSecureCommunicationFreshnessProps(parent, props)
        child = parent.find("SECURE-COMMUNICATION-FRESHNESS-PROPS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "freshProps"
        assert child.find("FRESHNESS-VALUE-LENGTH") is not None
        assert child.find("FRESHNESS-VALUE-TX-LENGTH") is not None


class TestWriteSecureCommunicationPropsSetFreshnessProps:
    def test_empty(self, writer):
        props_set = MagicMock()
        props_set.getFreshnessProps.return_value = []
        parent = _parent()
        writer.writeSecureCommunicationPropsSetFreshnessProps(parent, props_set)
        assert len(parent) == 0

    def test_with_props(self, writer):
        props_set = MagicMock()
        pkg = _pkg()
        props = SecureCommunicationFreshnessProps(pkg, "freshProps")
        props.setFreshnessValueLength(_pos_int("16"))
        props_set.getFreshnessProps.return_value = [props]
        parent = _parent()
        writer.writeSecureCommunicationPropsSetFreshnessProps(parent, props_set)
        props_elem = parent.find("FRESHNESS-PROPSS")
        assert props_elem is not None
        assert props_elem.find("SECURE-COMMUNICATION-FRESHNESS-PROPS") is not None


class TestWriteSecureCommunicationPropsSet:
    def test_full(self, writer):
        pkg = _pkg()
        props_set = SecureCommunicationPropsSet(pkg, "secureSet")
        props_set.getAuthenticationProps = MagicMock(return_value=[])
        props_set.getFreshnessProps = MagicMock(return_value=[])
        parent = _parent()
        writer.writeSecureCommunicationPropsSet(parent, props_set)
        child = parent.find("SECURE-COMMUNICATION-PROPS-SET")
        assert child is not None
        assert child.find("SHORT-NAME").text == "secureSet"


class TestWriteSoAdRoutingGroup:
    def test_full(self, writer):
        pkg = _pkg()
        group = SoAdRoutingGroup(pkg, "soadGroup")
        group.setEventGroupControlType(_literal("ENABLED"))
        parent = _parent()
        writer.writeSoAdRoutingGroup(parent, group)
        child = parent.find("SO-AD-ROUTING-GROUP")
        assert child is not None
        assert child.find("SHORT-NAME").text == "soadGroup"
        assert child.find("EVENT-GROUP-CONTROL-TYPE").text == "ENABLED"


class TestWriteDoIpLogicAddress:
    def test_none(self, writer):
        parent = _parent()
        writer.writeDoIpLogicAddress(parent, None)
        assert len(parent) == 0

    def test_full(self, writer):
        pkg = _pkg()
        config = DoIpTpConfig(pkg, "doipConfig")
        address = config.createDoIpLogicAddress("logicAddr")
        address.setAddress(_int("0xE00"))
        parent = _parent()
        writer.writeDoIpLogicAddress(parent, address)
        child = parent.find("DO-IP-LOGIC-ADDRESS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "logicAddr"
        assert child.find("ADDRESS").text == "0xE00"


class TestWriteDoIpTpConfigDoIpLogicAddresses:
    def test_empty(self, writer):
        pkg = _pkg()
        config = DoIpTpConfig(pkg, "doipConfig")
        parent = _parent()
        writer.writeDoIpTpConfigDoIpLogicAddresses(parent, config)
        assert len(parent) == 0

    def test_with_addresses(self, writer):
        pkg = _pkg()
        config = DoIpTpConfig(pkg, "doipConfig")
        addr1 = config.createDoIpLogicAddress("addr1")
        addr1.setAddress(_int("0xE00"))
        addr2 = config.createDoIpLogicAddress("addr2")
        addr2.setAddress(_int("0xE01"))
        parent = _parent()
        writer.writeDoIpTpConfigDoIpLogicAddresses(parent, config)
        addresses_elem = parent.find("DO-IP-LOGIC-ADDRESSS")
        assert addresses_elem is not None
        addresses = addresses_elem.findall("DO-IP-LOGIC-ADDRESS")
        assert len(addresses) == 2


class TestWriteDoIpTpConnection:
    def test_none(self, writer):
        parent = _parent()
        writer.writeDoIpTpConnection(parent, None)
        assert len(parent) == 0

    def test_full(self, writer):
        conn = DoIpTpConnection()
        conn.createTpConnectionIdent("connIdent")
        conn.setDoIpSourceAddressRef(_ref("DO-IP-LOGIC-ADDRESS", "/src"))
        conn.setDoIpTargetAddressRef(_ref("DO-IP-LOGIC-ADDRESS", "/tgt"))
        conn.setTpSduRef(_ref("I-PDU", "/sdu"))
        parent = _parent()
        writer.writeDoIpTpConnection(parent, conn)
        child = parent.find("DO-IP-TP-CONNECTION")
        assert child is not None
        assert child.find("DO-IP-SOURCE-ADDRESS-REF") is not None
        assert child.find("DO-IP-TARGET-ADDRESS-REF") is not None
        assert child.find("TP-SDU-REF") is not None


class TestWriteDoIpTpConfigTpConnections:
    def test_empty(self, writer):
        pkg = _pkg()
        config = DoIpTpConfig(pkg, "doipConfig")
        parent = _parent()
        writer.writeDoIpTpConfigTpConnections(parent, config)
        assert len(parent) == 0

    def test_with_connections(self, writer):
        pkg = _pkg()
        config = DoIpTpConfig(pkg, "doipConfig")
        conn1 = DoIpTpConnection()
        conn1.createTpConnectionIdent("conn1")
        conn1.setDoIpSourceAddressRef(_ref("DO-IP-LOGIC-ADDRESS", "/src1"))
        config.addTpConnection(conn1)
        conn2 = DoIpTpConnection()
        conn2.createTpConnectionIdent("conn2")
        conn2.setDoIpSourceAddressRef(_ref("DO-IP-LOGIC-ADDRESS", "/src2"))
        config.addTpConnection(conn2)
        parent = _parent()
        writer.writeDoIpTpConfigTpConnections(parent, config)
        conns_elem = parent.find("TP-CONNECTIONS")
        assert conns_elem is not None
        conns = conns_elem.findall("DO-IP-TP-CONNECTION")
        assert len(conns) == 2


class TestWriteDoIpTpConfig:
    def test_full(self, writer):
        pkg = _pkg()
        config = DoIpTpConfig(pkg, "doipConfig")
        config.setCommunicationClusterRef(
            _ref("ETHERNET-CLUSTER", "/cluster")
        )
        addr = config.createDoIpLogicAddress("addr")
        addr.setAddress(_int("0xE00"))
        conn = DoIpTpConnection()
        conn.createTpConnectionIdent("conn")
        config.addTpConnection(conn)
        parent = _parent()
        writer.writeDoIpTpConfig(parent, config)
        child = parent.find("DO-IP-TP-CONFIG")
        assert child is not None
        assert child.find("SHORT-NAME").text == "doipConfig"
        assert child.find("COMMUNICATION-CLUSTER-REF") is not None
        assert child.find("DO-IP-LOGIC-ADDRESSS") is not None
        assert child.find("TP-CONNECTIONS") is not None