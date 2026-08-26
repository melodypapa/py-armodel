"""Tests for writer PDU and transport protocol handlers."""

import xml.etree.cElementTree as ET
from unittest.mock import MagicMock

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import (
    AUTOSAR,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa: E501
    ARBoolean,
    ARLiteral,
    Integer,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (  # noqa: E501
    ContainedIPduProps,
    DcmIPdu,
    ISignalToIPduMapping,
    NmPdu,
    NPdu,
    SecureCommunicationProps,
    SecuredIPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (  # noqa: E501
    CanTpAddress,
    CanTpChannel,
    CanTpConfig,
    CanTpConnection,
    CanTpEcu,
    CanTpNode,
    LinTpConfig,
    LinTpConnection,
    LinTpNode,
    TpAddress,
)
from armodel.writer.arxml_writer import ARXMLWriter


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


def _time(text):
    val = TimeValue()
    val.setValue(text)
    return val


def _bool(text):
    val = ARBoolean()
    val.setValue(text)
    return val


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestWriteISignalToIPduMapping:
    def test_none_mapping(self, writer):
        parent = _parent()
        writer.writeISignalToIPduMapping(parent, None)
        assert len(parent) == 0

    def test_full_mapping(self, writer):
        pkg = _pkg()
        mapping = ISignalToIPduMapping(pkg, "Map")
        mapping.setISignalRef(_ref("I-SIGNAL", "/sigs/s"))
        mapping.setISignalGroupRef(_ref("I-SIGNAL-GROUP", "/sigs/sg"))
        mapping.setPackingByteOrder(_literal("MOST-SIGNIFICANT-BYTE-LAST"))
        mapping.setStartPosition(_int("0"))
        mapping.setTransferProperty(_literal("TRIGGERED"))
        mapping.setUpdateIndicationBitPosition(_int("7"))
        parent = _parent()
        writer.writeISignalToIPduMapping(parent, mapping)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "I-SIGNAL-TO-I-PDU-MAPPING"
        assert child.find("SHORT-NAME").text == "Map"
        assert child.find("I-SIGNAL-REF").text == "/sigs/s"
        assert child.find("I-SIGNAL-GROUP-REF").text == "/sigs/sg"
        assert child.find("PACKING-BYTE-ORDER").text == "MOST-SIGNIFICANT-BYTE-LAST"
        assert child.find("START-POSITION").text == "0"
        assert child.find("TRANSFER-PROPERTY").text == "TRIGGERED"
        assert child.find("UPDATE-INDICATION-BIT-POSITION").text == "7"


class TestWriteNmPduISignalToIPduMappings:
    def test_empty(self, writer):
        pkg = _pkg()
        pdu = NmPdu(pkg, "Nm")
        parent = _parent()
        writer.writeNmPduISignalToIPduMappings(parent, pdu)
        assert len(parent) == 0

    def test_with_mappings(self, writer):
        pkg = _pkg()
        pdu = NmPdu(pkg, "Nm")
        pdu.createISignalToIPduMapping("M1")
        parent = _parent()
        writer.writeNmPduISignalToIPduMappings(parent, pdu)
        assert len(parent) == 1
        assert parent[0].tag == "I-SIGNAL-TO-I-PDU-MAPPINGS"
        assert len(parent[0]) == 1

    def test_unsupported_warns(self):
        w = ARXMLWriter(options={"warning": True})
        pdu = MagicMock()
        pdu.getISignalToIPduMappings.return_value = ["unsupported"]
        parent = _parent()
        w.writeNmPduISignalToIPduMappings(parent, pdu)
        assert len(parent) == 1
        assert parent[0].tag == "I-SIGNAL-TO-I-PDU-MAPPINGS"


class TestWriteNmPdu:
    def test_basic(self, writer):
        pkg = _pkg()
        pdu = NmPdu(pkg, "Nm")
        pdu.setUnusedBitPattern(_int("0"))
        pdu.createISignalToIPduMapping("M1")
        parent = _parent()
        writer.writeNmPdu(parent, pdu)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "NM-PDU"
        assert child.find("SHORT-NAME").text == "Nm"
        assert child.find("UNUSED-BIT-PATTERN").text == "0"
        assert child.find("I-SIGNAL-TO-I-PDU-MAPPINGS") is not None

    def test_nm_information_attrs(self, writer):
        pkg = _pkg()
        pdu = NmPdu(pkg, "Nm")
        pdu.setNmDataInformation(_bool(True))
        pdu.setNmVoteInformation(_bool(False))
        parent = _parent()
        writer.writeNmPdu(parent, pdu)
        child = parent[0]
        assert child.tag == "NM-PDU"
        assert child.find("NM-DATA-INFORMATION").text == "true"
        assert child.find("NM-VOTE-INFORMATION").text == "false"

    def test_nm_pdu_roundtrip(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        NS = "http://autosar.org/schema/r4.0"
        pkg = _pkg()
        pdu = NmPdu(pkg, "Nm")
        pdu.setNmDataInformation(_bool(True))
        pdu.setNmVoteInformation(_bool(False))
        pdu.setUnusedBitPattern(_int("255"))
        mapping = pdu.createISignalToIPduMapping("M1")
        mapping.setISignalRef(_ref("I-SIGNAL", "/sigs/s"))
        mapping.setStartPosition(_int("8"))

        parent = _parent()
        writer.writeNmPdu(parent, pdu)
        xml_str = ET.tostring(parent).decode().replace("<PARENT>", '<PARENT xmlns="%s">' % NS, 1)
        namespaced = ET.fromstring(xml_str)

        reparsed = NmPdu(pkg, "Nm2")
        parser = ARXMLParser()
        ARXMLParser().readNmPdu(parser.find(namespaced, "NM-PDU"), reparsed)
        assert reparsed.getNmDataInformation().getValue() is True
        assert reparsed.getNmVoteInformation().getValue() is False
        assert reparsed.getUnusedBitPattern().getValue() == 255
        mappings = reparsed.getISignalToIPduMappings()
        assert len(mappings) == 1
        assert mappings[0].getShortName() == "M1"
        assert mappings[0].getISignalRef().getValue() == "/sigs/s"
        assert mappings[0].getStartPosition().getValue() == 8


class TestWriteNPdu:
    def test_basic(self, writer):
        pkg = _pkg()
        pdu = NPdu(pkg, "N")
        parent = _parent()
        writer.writeNPdu(parent, pdu)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "N-PDU"
        assert child.find("SHORT-NAME").text == "N"


class TestWriteDcmIPdu:
    def test_basic(self, writer):
        pkg = _pkg()
        pdu = DcmIPdu(pkg, "Dcm")
        pdu.setDiagPduType(_literal("DIAG-REQUEST"))
        parent = _parent()
        writer.writeDcmIPdu(parent, pdu)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "DCM-I-PDU"
        assert child.find("SHORT-NAME").text == "Dcm"
        assert child.find("DIAG-PDU-TYPE").text == "DIAG-REQUEST"


class TestWriteContainedIPduProps:
    def test_none_props(self, writer):
        parent = _parent()
        writer.writeContainedIPduProps(parent, None)
        assert len(parent) == 0

    def test_full_props(self, writer):
        props = ContainedIPduProps()
        props.setCollectionSemantics(_literal("lastIsBest"))
        props.setHeaderIdLongHeader(_pos_int("100"))
        props.setHeaderIdShortHeader(_pos_int("50"))
        props.setOffset(_pos_int("4"))
        props.setTimeout(_pos_int("10"))
        props.setTrigger(_literal("onChange"))
        props.setUpdateIndicationBitPosition(_pos_int("7"))
        parent = _parent()
        writer.writeContainedIPduProps(parent, props)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "CONTAINED-I-PDU-PROPS"
        assert child.find("COLLECTION-SEMANTICS").text == "lastIsBest"
        assert child.find("HEADER-ID-LONG-HEADER").text == "100"
        assert child.find("HEADER-ID-SHORT-HEADER").text == "50"
        assert child.find("OFFSET").text == "4"
        assert child.find("TIMEOUT").text == "10"
        assert child.find("TRIGGER").text == "onChange"
        assert child.find("UPDATE-INDICATION-BIT-POSITION").text == "7"


class TestSetSecureCommunicationProps:
    def test_none(self, writer):
        parent = _parent()
        writer.setSecureCommunicationProps(parent, "SECURE-PROPS", None)
        assert len(parent) == 0

    def test_full_props(self, writer):
        props = SecureCommunicationProps()
        props.setAuthDataFreshnessLength(_pos_int("8"))
        props.setAuthDataFreshnessStartPosition(_pos_int("0"))
        props.setAuthenticationBuildAttempts(_pos_int("2"))
        props.setAuthenticationRetries(_pos_int("3"))
        props.setDataId(_pos_int("1"))
        props.setFreshnessValueId(_pos_int("5"))
        props.setMessageLinkLength(_pos_int("6"))
        props.setMessageLinkPosition(_pos_int("7"))
        props.setSecondaryFreshnessValueId(_pos_int("9"))
        props.setSecuredAreaLength(_pos_int("10"))
        props.setSecuredAreaOffset(_pos_int("11"))
        parent = _parent()
        writer.setSecureCommunicationProps(parent, "SECURE-PROPS", props)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SECURE-PROPS"
        assert child.find("AUTH-DATA-FRESHNESS-LENGTH").text == "8"
        assert child.find("DATA-ID").text == "1"
        assert child.find("MESSAGE-LINK-LENGTH").text == "6"
        assert child.find("SECURED-AREA-OFFSET").text == "11"


class TestWriteSecuredIPdu:
    def test_full(self, writer):
        pkg = _pkg()
        pdu = SecuredIPdu(pkg, "Sec")
        pdu.setAuthenticationPropsRef(_ref("SECURITY-PROPS", "/sp"))
        pdu.setFreshnessPropsRef(_ref("FRESHNESS-PROPS", "/fp"))
        pdu.setPayloadRef(_ref("I-PDU", "/pl"))
        props = SecureCommunicationProps()
        props.setDataId(_pos_int("42"))
        pdu.setSecureCommunicationProps(props)
        pdu.setUseAsCryptographicIPdu(_bool("true"))
        parent = _parent()
        writer.writeSecuredIPdu(parent, pdu)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SECURED-I-PDU"
        assert child.find("SHORT-NAME").text == "Sec"
        assert child.find("AUTHENTICATION-PROPS-REF").text == "/sp"
        assert child.find("FRESHNESS-PROPS-REF").text == "/fp"
        assert child.find("PAYLOAD-REF").text == "/pl"
        assert child.find("USE-AS-CRYPTOGRAPHIC-I-PDU").text == "true"
        assert child.find("SECURE-COMMUNICATION-PROPS") is not None


class TestWriteTpConfig:
    def test_basic(self, writer):
        pkg = _pkg()
        cfg = CanTpConfig(pkg, "CanTp")
        cfg.setCommunicationClusterRef(_ref("CLUSTER", "/c"))
        parent = _parent()
        writer.writeTpConfig(parent, cfg)
        assert parent.find("SHORT-NAME").text == "CanTp"
        assert parent.find("COMMUNICATION-CLUSTER-REF").text == "/c"


class TestWriteCanTpAddress:
    def test_none(self, writer):
        parent = _parent()
        writer.writeCanTpAddress(parent, None)
        assert len(parent) == 0

    def test_full(self, writer):
        pkg = _pkg()
        addr = CanTpAddress(pkg, "Addr")
        addr.setTpAddress(_int("1"))
        addr.setTpAddressExtensionValue(_int("2"))
        parent = _parent()
        writer.writeCanTpAddress(parent, addr)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "CAN-TP-ADDRESS"
        assert child.find("SHORT-NAME").text == "Addr"
        assert child.find("TP-ADDRESS").text == "1"
        assert child.find("TP-ADDRESS-EXTENSION-VALUE").text == "2"

    def test_roundtrip_can_tp_address_fields(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = _pkg()
        addr = CanTpAddress(pkg, "Addr")
        addr.setTpAddress(_int("2047"))
        addr.setTpAddressExtensionValue(_int("5"))
        parent = _parent()
        writer.writeCanTpAddress(parent, addr)

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = CanTpAddress(pkg, "Addr2")
        parser.readCanTpAddress(ET.fromstring(xml_str)[0], reloaded)
        assert reloaded.getTpAddress().getValue() == 2047
        assert reloaded.getTpAddressExtensionValue().getValue() == 5

    def test_roundtrip_can_tp_address_empty_fields(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = _pkg()
        addr = CanTpAddress(pkg, "Addr")
        parent = _parent()
        writer.writeCanTpAddress(parent, addr)

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = CanTpAddress(pkg, "Addr2")
        parser.readCanTpAddress(ET.fromstring(xml_str)[0], reloaded)
        assert reloaded.getTpAddress() is None
        assert reloaded.getTpAddressExtensionValue() is None


class TestWriteCanTpConfigTpAddresses:
    def test_empty(self, writer):
        pkg = _pkg()
        cfg = CanTpConfig(pkg, "Cfg")
        parent = _parent()
        writer.writeCanTpConfigTpAddresses(parent, cfg)
        assert len(parent) == 0

    def test_with_addresses(self, writer):
        pkg = _pkg()
        cfg = CanTpConfig(pkg, "Cfg")
        cfg.createCanTpAddress("A1")
        parent = _parent()
        writer.writeCanTpConfigTpAddresses(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-ADDRESSS"
        assert len(parent[0]) == 1

    def test_unsupported_warns(self):
        w = ARXMLWriter(options={"warning": True})
        cfg = MagicMock()
        cfg.getTpAddresses.return_value = ["unsupported"]
        parent = _parent()
        w.writeCanTpConfigTpAddresses(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-ADDRESSS"


class TestWriteCanTpChannel:
    def test_none(self, writer):
        parent = _parent()
        writer.writeCanTpChannel(parent, None)
        assert len(parent) == 0

    def test_full(self, writer):
        pkg = _pkg()
        ch = CanTpChannel(pkg, "Ch")
        ch.setChannelId(_pos_int("1"))
        parent = _parent()
        writer.writeCanTpChannel(parent, ch)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "CAN-TP-CHANNEL"
        assert child.find("SHORT-NAME").text == "Ch"
        assert child.find("CHANNEL-ID").text == "1"
        assert child.find("CHANNEL-MODE") is None

    def test_roundtrip_can_tp_channel_fields(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = _pkg()
        ch = CanTpChannel(pkg, "Ch")
        ch.setChannelId(_pos_int("7"))
        parent = _parent()
        writer.writeCanTpChannel(parent, ch)

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = CanTpChannel(pkg, "Ch2")
        parser.readCanTpChannel(ET.fromstring(xml_str)[0], reloaded)
        assert reloaded.getChannelId().getValue() == 7

    def test_roundtrip_can_tp_channel_empty_fields(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = _pkg()
        ch = CanTpChannel(pkg, "Ch")
        parent = _parent()
        writer.writeCanTpChannel(parent, ch)

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = CanTpChannel(pkg, "Ch2")
        parser.readCanTpChannel(ET.fromstring(xml_str)[0], reloaded)
        assert reloaded.getChannelId() is None


class TestWriteCanTpConfigTpChannels:
    def test_empty(self, writer):
        pkg = _pkg()
        cfg = CanTpConfig(pkg, "Cfg")
        parent = _parent()
        writer.writeCanTpConfigTpChannels(parent, cfg)
        assert len(parent) == 0

    def test_with_channels(self, writer):
        pkg = _pkg()
        cfg = CanTpConfig(pkg, "Cfg")
        cfg.createCanTpChannel("C1")
        parent = _parent()
        writer.writeCanTpConfigTpChannels(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-CHANNELS"
        assert len(parent[0]) == 1

    def test_unsupported_warns(self):
        w = ARXMLWriter(options={"warning": True})
        cfg = MagicMock()
        cfg.getTpChannels.return_value = ["unsupported"]
        parent = _parent()
        w.writeCanTpConfigTpChannels(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-CHANNELS"


class TestWriteTpConnection:
    def test_without_ident(self, writer):
        conn = CanTpConnection()
        parent = _parent()
        writer.writeTpConnection(parent, conn)
        assert parent.find("IDENT") is None

    def test_with_ident(self, writer):
        conn = CanTpConnection()
        conn.createTpConnectionIdent("ConnIdent")
        parent = _parent()
        writer.writeTpConnection(parent, conn)
        ident = parent.find("IDENT")
        assert ident is not None
        assert ident.find("SHORT-NAME").text == "ConnIdent"


class TestWriteTpConnectionReceiverRefs:
    def test_empty(self, writer):
        conn = CanTpConnection()
        parent = _parent()
        writer.writeTpConnectionReceiverRefs(parent, conn)
        assert len(parent) == 0

    def test_with_refs(self, writer):
        conn = CanTpConnection()
        conn.addReceiverRef(_ref("ECU-INSTANCE", "/r1"))
        conn.addReceiverRef(_ref("ECU-INSTANCE", "/r2"))
        parent = _parent()
        writer.writeTpConnectionReceiverRefs(parent, conn)
        assert len(parent) == 1
        refs = parent[0]
        assert refs.tag == "RECEIVER-REFS"
        assert len(refs) == 2
        assert refs[0].tag == "RECEIVER-REF"
        assert refs[0].text == "/r1"


class TestWriteCanTpConnection:
    def test_none(self, writer):
        parent = _parent()
        writer.writeCanTpConnection(parent, None)
        assert len(parent) == 0

    def test_full(self, writer):
        conn = CanTpConnection()
        conn.createTpConnectionIdent("ConnIdent")
        conn.setAddressingFormat(_literal("MIXED"))
        conn.setCanTpChannelRef(_ref("CAN-TP-CHANNEL", "/ch"))
        conn.setCancellation(_bool("true"))
        conn.setDataPduRef(_ref("I-PDU", "/dp"))
        conn.setFlowControlPduRef(_ref("I-PDU", "/fc"))
        conn.setMaxBlockSize(_int("8"))
        conn.setMulticastRef(_ref("I-PDU", "/mc"))
        conn.setPaddingActivation(_bool("false"))
        conn.addReceiverRef(_ref("ECU-INSTANCE", "/r1"))
        conn.setTaType(_literal("PHYSICAL"))
        conn.setTimeoutBr(_time("0.1"))
        conn.setTimeoutBs(_time("0.2"))
        conn.setTimeoutCr(_time("0.3"))
        conn.setTimeoutCs(_time("0.4"))
        conn.setTpSduRef(_ref("I-PDU", "/sdu"))
        conn.setTransmitterRef(_ref("ECU-INSTANCE", "/tx"))
        parent = _parent()
        writer.writeCanTpConnection(parent, conn)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "CAN-TP-CONNECTION"
        assert child.find("IDENT/SHORT-NAME").text == "ConnIdent"
        assert child.find("ADDRESSING-FORMAT").text == "MIXED"
        assert child.find("CAN-TP-CHANNEL-REF").text == "/ch"
        assert child.find("CANCELLATION").text == "true"
        assert child.find("DATA-PDU-REF").text == "/dp"
        assert child.find("FLOW-CONTROL-PDU-REF").text == "/fc"
        assert child.find("MAX-BLOCK-SIZE").text == "8"
        assert child.find("MULTICAST-REF").text == "/mc"
        assert child.find("PADDING-ACTIVATION").text == "false"
        assert child.find("RECEIVER-REFS/RECEIVER-REF").text == "/r1"
        assert child.find("TA-TYPE").text == "PHYSICAL"
        assert child.find("TIMEOUT-BR").text == "0.1"
        assert child.find("TIMEOUT-BS").text == "0.2"
        assert child.find("TIMEOUT-CR").text == "0.3"
        assert child.find("TIMEOUT-CS").text == "0.4"
        assert child.find("TP-SDU-REF").text == "/sdu"
        assert child.find("TRANSMITTER-REF").text == "/tx"

    def test_roundtrip_can_tp_connection_fields(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        conn = CanTpConnection()
        conn.createTpConnectionIdent("ConnIdent")
        conn.setAddressingFormat(_literal("MIXED"))
        conn.setCanTpChannelRef(_ref("CAN-TP-CHANNEL", "/ch"))
        conn.setCancellation(_bool("true"))
        conn.setDataPduRef(_ref("I-PDU", "/dp"))
        conn.setFlowControlPduRef(_ref("I-PDU", "/fc"))
        conn.setMaxBlockSize(_int("8"))
        conn.setMulticastRef(_ref("I-PDU", "/mc"))
        conn.setPaddingActivation(_bool("false"))
        conn.addReceiverRef(_ref("ECU-INSTANCE", "/r1"))
        conn.addReceiverRef(_ref("ECU-INSTANCE", "/r2"))
        conn.setTaType(_literal("PHYSICAL"))
        conn.setTimeoutBr(_time("0.1"))
        conn.setTimeoutBs(_time("0.2"))
        conn.setTimeoutCr(_time("0.3"))
        conn.setTimeoutCs(_time("0.4"))
        conn.setTpSduRef(_ref("I-PDU", "/sdu"))
        conn.setTransmitterRef(_ref("ECU-INSTANCE", "/tx"))
        parent = _parent()
        writer.writeCanTpConnection(parent, conn)

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = CanTpConnection()
        parser.readCanTpConnection(ET.fromstring(xml_str)[0], reloaded)
        assert reloaded.getIdent() is not None
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import CanTpAddressingFormatType

        assert isinstance(reloaded.getAddressingFormat(), CanTpAddressingFormatType)
        assert reloaded.getAddressingFormat().getValue() == "MIXED"
        assert reloaded.getCanTpChannelRef().getValue() == "/ch"
        assert reloaded.getCancellation().getValue() is True
        assert reloaded.getDataPduRef().getValue() == "/dp"
        assert reloaded.getFlowControlPduRef().getValue() == "/fc"
        assert reloaded.getMaxBlockSize().getValue() == 8
        assert reloaded.getMulticastRef().getValue() == "/mc"
        assert reloaded.getPaddingActivation().getValue() is False
        refs = [r.getValue() for r in reloaded.getReceiverRefs()]
        assert refs == ["/r1", "/r2"]
        assert reloaded.getTaType().getValue() == "PHYSICAL"
        assert reloaded.getTimeoutBr().getValue() == 0.1
        assert reloaded.getTimeoutBs().getValue() == 0.2
        assert reloaded.getTimeoutCr().getValue() == 0.3
        assert reloaded.getTimeoutCs().getValue() == 0.4
        assert reloaded.getTpSduRef().getValue() == "/sdu"
        assert reloaded.getTransmitterRef().getValue() == "/tx"

    def test_roundtrip_can_tp_connection_empty(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        conn = CanTpConnection()
        parent = _parent()
        writer.writeCanTpConnection(parent, conn)

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = CanTpConnection()
        parser.readCanTpConnection(ET.fromstring(xml_str)[0], reloaded)
        assert reloaded.getIdent() is None
        assert reloaded.getAddressingFormat() is None
        assert reloaded.getCancellation() is None
        assert reloaded.getReceiverRefs() == []
        assert reloaded.getTransmitterRef() is None


class TestWriteCanTpConfigTpConnections:
    def test_empty(self, writer):
        pkg = _pkg()
        cfg = CanTpConfig(pkg, "Cfg")
        parent = _parent()
        writer.writeCanTpConfigTpConnections(parent, cfg)
        assert len(parent) == 0

    def test_with_connections(self, writer):
        pkg = _pkg()
        cfg = CanTpConfig(pkg, "Cfg")
        cfg.addTpConnection(CanTpConnection())
        parent = _parent()
        writer.writeCanTpConfigTpConnections(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-CONNECTIONS"
        assert len(parent[0]) == 1

    def test_roundtrip_can_tp_config_full(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = _pkg()
        cfg = CanTpConfig(pkg, "Cfg")
        addr = cfg.createCanTpAddress("Addr")
        addr.setTpAddress(_int("2047"))
        ch = cfg.createCanTpChannel("Ch")
        ch.setChannelId(_pos_int("1"))
        conn = CanTpConnection()
        conn.setTransmitterRef(_ref("ECU-INSTANCE", "/tx"))
        cfg.addTpConnection(conn)
        ecu = CanTpEcu()
        ecu.setCycleTimeMainFunction(_time("0.01"))
        cfg.addTpEcu(ecu)
        node = cfg.createCanTpNode("Node")
        node.setMaxFcWait(_int("10"))
        parent = _parent()
        writer.writeCanTpConfig(parent, cfg)

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = CanTpConfig(pkg, "Cfg2")
        parser.readCanTpConfig(parser.find(ET.fromstring(xml_str), "CAN-TP-CONFIG"), reloaded)
        assert len(reloaded.getTpAddresses()) == 1
        assert reloaded.getTpAddresses()[0].getTpAddress().getValue() == 2047
        assert len(reloaded.getTpChannels()) == 1
        assert reloaded.getTpChannels()[0].getChannelId().getValue() == 1
        assert len(reloaded.getTpConnections()) == 1
        assert reloaded.getTpConnections()[0].getTransmitterRef().getValue() == "/tx"
        assert len(reloaded.getTpEcus()) == 1
        assert reloaded.getTpEcus()[0].getCycleTimeMainFunction().getValue() == 0.01
        assert len(reloaded.getTpNodes()) == 1
        assert reloaded.getTpNodes()[0].getMaxFcWait().getValue() == 10

    def test_unsupported_warns(self):
        w = ARXMLWriter(options={"warning": True})
        cfg = MagicMock()
        cfg.getTpConnections.return_value = ["unsupported"]
        parent = _parent()
        w.writeCanTpConfigTpConnections(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-CONNECTIONS"


class TestWriteCanTpEcu:
    def test_none(self, writer):
        parent = _parent()
        writer.writeCanTpEcu(parent, None)
        assert len(parent) == 0

    def test_full(self, writer):
        ecu = CanTpEcu()
        ecu.setCycleTimeMainFunction(_time("0.01"))
        ecu.setEcuInstanceRef(_ref("ECU-INSTANCE", "/ecu"))
        parent = _parent()
        writer.writeCanTpEcu(parent, ecu)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "CAN-TP-ECU"
        assert child.find("CYCLE-TIME-MAIN-FUNCTION").text == "0.01"
        assert child.find("ECU-INSTANCE-REF").text == "/ecu"

    def test_roundtrip_can_tp_ecu_fields(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        ecu = CanTpEcu()
        ecu.setCycleTimeMainFunction(_time("0.01"))
        ecu.setEcuInstanceRef(_ref("ECU-INSTANCE", "/ecu"))
        parent = _parent()
        writer.writeCanTpEcu(parent, ecu)

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = CanTpEcu()
        parser.readCanTpEcu(ET.fromstring(xml_str)[0], reloaded)
        assert reloaded.getCycleTimeMainFunction().getValue() == 0.01
        assert reloaded.getEcuInstanceRef().getValue() == "/ecu"

    def test_roundtrip_can_tp_ecu_empty_fields(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        ecu = CanTpEcu()
        parent = _parent()
        writer.writeCanTpEcu(parent, ecu)

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = CanTpEcu()
        parser.readCanTpEcu(ET.fromstring(xml_str)[0], reloaded)
        assert reloaded.getCycleTimeMainFunction() is None
        assert reloaded.getEcuInstanceRef() is None


class TestWriteCanTpConfigTpEcus:
    def test_empty(self, writer):
        pkg = _pkg()
        cfg = CanTpConfig(pkg, "Cfg")
        parent = _parent()
        writer.writeCanTpConfigTpEcus(parent, cfg)
        assert len(parent) == 0

    def test_with_ecus(self, writer):
        pkg = _pkg()
        cfg = CanTpConfig(pkg, "Cfg")
        cfg.addTpEcu(CanTpEcu())
        parent = _parent()
        writer.writeCanTpConfigTpEcus(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-ECUS"
        assert len(parent[0]) == 1

    def test_unsupported_warns(self):
        w = ARXMLWriter(options={"warning": True})
        cfg = MagicMock()
        cfg.getTpEcus.return_value = ["unsupported"]
        parent = _parent()
        w.writeCanTpConfigTpEcus(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-ECUS"


class TestWriteCanTpNode:
    def test_none(self, writer):
        parent = _parent()
        writer.writeCanTpNode(parent, None)
        assert len(parent) == 0

    def test_full(self, writer):
        pkg = _pkg()
        node = CanTpNode(pkg, "Node")
        node.setConnectorRef(_ref("ECU-INSTANCE", "/conn"))
        node.setMaxFcWait(_int("10"))
        node.setStMin(_time("0.005"))
        node.setTimeoutAr(_time("0.05"))
        node.setTimeoutAs(_time("0.06"))
        node.setTpAddressRef(_ref("CAN-TP-ADDRESS", "/ta"))
        parent = _parent()
        writer.writeCanTpNode(parent, node)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "CAN-TP-NODE"
        assert child.find("SHORT-NAME").text == "Node"
        assert child.find("CONNECTOR-REF").text == "/conn"
        assert child.find("MAX-FC-WAIT").text == "10"
        assert child.find("ST-MIN").text == "0.005"
        assert child.find("TIMEOUT-AR").text == "0.05"
        assert child.find("TIMEOUT-AS").text == "0.06"
        assert child.find("TP-ADDRESS-REF").text == "/ta"

    def test_roundtrip_can_tp_node_fields(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = _pkg()
        node = CanTpNode(pkg, "Node")
        node.setConnectorRef(_ref("COMMUNICATION-CONNECTOR", "/conn"))
        node.setMaxFcWait(_int("10"))
        node.setStMin(_time("0.005"))
        node.setTimeoutAr(_time("0.05"))
        node.setTimeoutAs(_time("0.06"))
        node.setTpAddressRef(_ref("CAN-TP-ADDRESS", "/ta"))
        parent = _parent()
        writer.writeCanTpNode(parent, node)

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = CanTpNode(pkg, "Node2")
        parser.readCanTpNode(ET.fromstring(xml_str)[0], reloaded)
        assert reloaded.getConnectorRef().getValue() == "/conn"
        assert reloaded.getMaxFcWait().getValue() == 10
        assert reloaded.getStMin().getValue() == 0.005
        assert reloaded.getTimeoutAr().getValue() == 0.05
        assert reloaded.getTimeoutAs().getValue() == 0.06
        assert reloaded.getTpAddressRef().getValue() == "/ta"

    def test_roundtrip_can_tp_node_empty_fields(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = _pkg()
        node = CanTpNode(pkg, "Node")
        parent = _parent()
        writer.writeCanTpNode(parent, node)

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = CanTpNode(pkg, "Node2")
        parser.readCanTpNode(ET.fromstring(xml_str)[0], reloaded)
        assert reloaded.getConnectorRef() is None
        assert reloaded.getMaxFcWait() is None
        assert reloaded.getStMin() is None
        assert reloaded.getTimeoutAr() is None
        assert reloaded.getTimeoutAs() is None
        assert reloaded.getTpAddressRef() is None


class TestWriteCanTpConfigTpNodes:
    def test_empty(self, writer):
        pkg = _pkg()
        cfg = CanTpConfig(pkg, "Cfg")
        parent = _parent()
        writer.writeCanTpConfigTpNodes(parent, cfg)
        assert len(parent) == 0

    def test_with_nodes(self, writer):
        pkg = _pkg()
        cfg = CanTpConfig(pkg, "Cfg")
        cfg.createCanTpNode("N1")
        parent = _parent()
        writer.writeCanTpConfigTpNodes(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-NODES"
        assert len(parent[0]) == 1

    def test_unsupported_warns(self):
        w = ARXMLWriter(options={"warning": True})
        cfg = MagicMock()
        cfg.getTpNodes.return_value = ["unsupported"]
        parent = _parent()
        w.writeCanTpConfigTpNodes(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-NODES"


class TestWriteCanTpConfig:
    def test_full(self, writer):
        pkg = _pkg()
        cfg = CanTpConfig(pkg, "CanTp")
        cfg.setCommunicationClusterRef(_ref("CLUSTER", "/c"))
        cfg.createCanTpAddress("A1")
        cfg.createCanTpChannel("C1")
        cfg.addTpConnection(CanTpConnection())
        cfg.addTpEcu(CanTpEcu())
        cfg.createCanTpNode("N1")
        parent = _parent()
        writer.writeCanTpConfig(parent, cfg)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "CAN-TP-CONFIG"
        assert child.find("SHORT-NAME").text == "CanTp"
        assert child.find("COMMUNICATION-CLUSTER-REF").text == "/c"
        assert child.find("TP-ADDRESSS") is not None
        assert child.find("TP-CHANNELS") is not None
        assert child.find("TP-CONNECTIONS") is not None
        assert child.find("TP-ECUS") is not None
        assert child.find("TP-NODES") is not None


class TestWriteTpAddress:
    def test_none(self, writer):
        parent = _parent()
        writer.writeTpAddress(parent, None)
        assert len(parent) == 0

    def test_full(self, writer):
        pkg = _pkg()
        addr = TpAddress(pkg, "Addr")
        addr.setTpAddress(_int("5"))
        parent = _parent()
        writer.writeTpAddress(parent, addr)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "TP-ADDRESS"
        assert child.find("SHORT-NAME").text == "Addr"
        assert child.find("TP-ADDRESS").text == "5"


class TestWriteLinTpConfigTpAddresses:
    def test_empty(self, writer):
        pkg = _pkg()
        cfg = LinTpConfig(pkg, "Cfg")
        parent = _parent()
        writer.writeLinTpConfigTpAddresses(parent, cfg)
        assert len(parent) == 0

    def test_with_addresses(self, writer):
        pkg = _pkg()
        cfg = LinTpConfig(pkg, "Cfg")
        cfg.createTpAddress("A1")
        parent = _parent()
        writer.writeLinTpConfigTpAddresses(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-ADDRESSS"
        assert len(parent[0]) == 1

    def test_unsupported_warns(self):
        w = ARXMLWriter(options={"warning": True})
        cfg = MagicMock()
        cfg.getTpAddresses.return_value = [CanTpAddress(_pkg(), "X")]
        parent = _parent()
        w.writeLinTpConfigTpAddresses(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-ADDRESSS"


class TestWriteLinTpConnection:
    def test_none(self, writer):
        parent = _parent()
        writer.writeLinTpConnection(parent, None)
        assert len(parent) == 0

    def test_full(self, writer):
        conn = LinTpConnection()
        conn.createTpConnectionIdent("LinIdent")
        conn.setDataPduRef(_ref("I-PDU", "/dp"))
        conn.setFlowControlRef(_ref("I-PDU", "/fc"))
        conn.setLinTpNSduRef(_ref("LIN-TP-N-SDU", "/sdu"))
        conn.addReceiverRef(_ref("ECU-INSTANCE", "/r1"))
        conn.setTimeoutAs(_time("0.1"))
        conn.setTimeoutCr(_time("0.2"))
        conn.setTimeoutCs(_time("0.3"))
        conn.setTransmitterRef(_ref("ECU-INSTANCE", "/tx"))
        parent = _parent()
        writer.writeLinTpConnection(parent, conn)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "LIN-TP-CONNECTION"
        assert child.find("IDENT/SHORT-NAME").text == "LinIdent"
        assert child.find("DATA-PDU-REF").text == "/dp"
        assert child.find("FLOW-CONTROL-REF").text == "/fc"
        assert child.find("LIN-TP-N-SDU-REF").text == "/sdu"
        assert child.find("RECEIVER-REFS/RECEIVER-REF").text == "/r1"
        assert child.find("TIMEOUT-AS").text == "0.1"
        assert child.find("TIMEOUT-CR").text == "0.2"
        assert child.find("TIMEOUT-CS").text == "0.3"
        assert child.find("TRANSMITTER-REF").text == "/tx"


class TestWriteLinTpConfigTpConnections:
    def test_empty(self, writer):
        pkg = _pkg()
        cfg = LinTpConfig(pkg, "Cfg")
        parent = _parent()
        writer.writeLinTpConfigTpConnections(parent, cfg)
        assert len(parent) == 0

    def test_with_connections(self, writer):
        pkg = _pkg()
        cfg = LinTpConfig(pkg, "Cfg")
        cfg.addTpConnection(LinTpConnection())
        parent = _parent()
        writer.writeLinTpConfigTpConnections(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-CONNECTIONS"
        assert len(parent[0]) == 1

    def test_unsupported_warns(self):
        w = ARXMLWriter(options={"warning": True})
        cfg = MagicMock()
        cfg.getTpConnections.return_value = ["unsupported"]
        parent = _parent()
        w.writeLinTpConfigTpConnections(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-CONNECTIONS"


class TestWriteLinTpNode:
    def test_none(self, writer):
        parent = _parent()
        writer.writeLinTpNode(parent, None)
        assert len(parent) == 0

    def test_full(self, writer):
        pkg = _pkg()
        node = LinTpNode(pkg, "LinNode")
        node.setConnectorRef(_ref("ECU-INSTANCE", "/conn"))
        node.setDropNotRequestedNad(_bool("true"))
        node.setMaxNumberOfRespPendingFrames(_int("3"))
        node.setP2Max(_time("0.05"))
        node.setP2Timing(_time("0.025"))
        node.setTpAddressRef(_ref("TP-ADDRESS", "/ta"))
        parent = _parent()
        writer.writeLinTpNode(parent, node)
        child = parent.find("LIN-TP-NODE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "LinNode"
        assert child.find("CONNECTOR-REF").text == "/conn"
        assert child.find("DROP-NOT-REQUESTED-NAD") is not None
        assert child.find("DROP-NOT-REQUESTED-NAD").text == "true"
        assert child.find("MAX-NUMBER-OF-RESP-PENDING-FRAMES").text == "3"
        assert child.find("P-2-MAX").text == "0.05"
        assert child.find("P-2-TIMING").text == "0.025"
        assert child.find("TP-ADDRESS-REF").text == "/ta"

    def test_roundtrip_lin_tp_node_fields(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = _pkg()
        node = LinTpNode(pkg, "LinNode")
        node.setConnectorRef(_ref("COMMUNICATION-CONNECTOR", "/conn"))
        node.setDropNotRequestedNad(_bool("true"))
        node.setMaxNumberOfRespPendingFrames(_int("3"))
        node.setP2Max(_time("0.05"))
        node.setP2Timing(_time("0.025"))
        node.setTpAddressRef(_ref("TP-ADDRESS", "/ta"))
        parent = _parent()
        writer.writeLinTpNode(parent, node)

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = LinTpNode(pkg, "LinNode2")
        parser.readLinTpNode(ET.fromstring(xml_str)[0], reloaded)
        assert reloaded.getConnectorRef().getValue() == "/conn"
        assert reloaded.getDropNotRequestedNad().getValue() is True
        assert reloaded.getMaxNumberOfRespPendingFrames().getValue() == 3
        assert reloaded.getP2Max().getValue() == 0.05
        assert reloaded.getP2Timing().getValue() == 0.025
        assert reloaded.getTpAddressRef().getValue() == "/ta"

    def test_roundtrip_lin_tp_node_empty_fields(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = _pkg()
        node = LinTpNode(pkg, "LinNode")
        parent = _parent()
        writer.writeLinTpNode(parent, node)

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = LinTpNode(pkg, "LinNode2")
        parser.readLinTpNode(ET.fromstring(xml_str)[0], reloaded)
        assert reloaded.getConnectorRef() is None
        assert reloaded.getDropNotRequestedNad() is None
        assert reloaded.getMaxNumberOfRespPendingFrames() is None
        assert reloaded.getP2Max() is None
        assert reloaded.getP2Timing() is None
        assert reloaded.getTpAddressRef() is None


class TestWriteLinTpConfigTpNodes:
    def test_empty(self, writer):
        pkg = _pkg()
        cfg = LinTpConfig(pkg, "Cfg")
        parent = _parent()
        writer.writeLinTpConfigTpNodes(parent, cfg)
        assert len(parent) == 0

    def test_with_nodes(self, writer):
        pkg = _pkg()
        cfg = LinTpConfig(pkg, "Cfg")
        cfg.createLinTpNode("N1")
        parent = _parent()
        writer.writeLinTpConfigTpNodes(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-NODES"
        assert len(parent[0]) == 1

    def test_unsupported_warns(self):
        w = ARXMLWriter(options={"warning": True})
        cfg = MagicMock()
        cfg.getTpNodes.return_value = ["unsupported"]
        parent = _parent()
        w.writeLinTpConfigTpNodes(parent, cfg)
        assert len(parent) == 1
        assert parent[0].tag == "TP-NODES"


class TestWriteLinTpConfig:
    def test_full(self, writer):
        pkg = _pkg()
        cfg = LinTpConfig(pkg, "LinTp")
        cfg.setCommunicationClusterRef(_ref("CLUSTER", "/c"))
        cfg.createTpAddress("A1")
        cfg.addTpConnection(LinTpConnection())
        cfg.createLinTpNode("N1")
        parent = _parent()
        writer.writeLinTpConfig(parent, cfg)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "LIN-TP-CONFIG"
        assert child.find("SHORT-NAME").text == "LinTp"
        assert child.find("COMMUNICATION-CLUSTER-REF").text == "/c"
        assert child.find("TP-ADDRESSS") is not None
        assert child.find("TP-CONNECTIONS") is not None
        assert child.find("TP-NODES") is not None

    def test_empty_wrappers_not_written(self, writer):
        pkg = _pkg()
        cfg = LinTpConfig(pkg, "LinTp")
        parent = _parent()
        writer.writeLinTpConfig(parent, cfg)
        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "LIN-TP-CONFIG"
        assert child.find("TP-ADDRESSS") is None
        assert child.find("TP-CONNECTIONS") is None
        assert child.find("TP-NODES") is None

    def test_roundtrip_lin_tp_config_fields(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = _pkg()
        cfg = LinTpConfig(pkg, "LinTp")
        cfg.setCommunicationClusterRef(_ref("LIN-CLUSTER", "/c"))
        address = cfg.createTpAddress("A1")
        address.setTpAddress(_int("1234"))
        connection = LinTpConnection()
        connection.setTimeoutAs(_time("0.06"))
        cfg.addTpConnection(connection)
        node = cfg.createLinTpNode("N1")
        node.setDropNotRequestedNad(_bool("true"))
        node.setMaxNumberOfRespPendingFrames(_int("3"))
        parent = _parent()
        writer.writeLinTpConfig(parent, cfg)

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = LinTpConfig(pkg, "LinTp2")
        parser.readLinTpConfig(ET.fromstring(xml_str)[0], reloaded)
        assert reloaded.getCommunicationClusterRef().getValue() == "/c"
        assert len(reloaded.getTpAddresses()) == 1
        assert reloaded.getTpAddresses()[0].getTpAddress().getValue() == 1234
        assert len(reloaded.getTpConnections()) == 1
        assert reloaded.getTpConnections()[0].getTimeoutAs().getValue() == 0.06
        assert len(reloaded.getTpNodes()) == 1
        assert reloaded.getTpNodes()[0].getDropNotRequestedNad().getValue() is True
        assert reloaded.getTpNodes()[0].getMaxNumberOfRespPendingFrames().getValue() == 3
