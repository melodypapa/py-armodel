"""Writer round-trip tests for CommConnectorPort (Table 6.1)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    CommConnectorPort,
    CommunicationDirectionType,
    FramePort,
    IPduPort,
    IPduSignalProcessingEnum,
    ISignalPort,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _parent():
    return MockParent()


def _namespaced(element: ET.Element) -> ET.Element:
    xml_text = ET.tostring(element, encoding="unicode")
    return ET.fromstring(xml_text.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))


def _full_port() -> FramePort:
    port = FramePort(_parent(), "fp")
    direction = CommunicationDirectionType()
    direction.setValue(CommunicationDirectionType.IN)
    port.setCommunicationDirection(direction)
    return port


class TestCommConnectorPort:
    def test_inheritance(self):
        parent = _parent()
        port = FramePort(parent, "fp")
        assert isinstance(port, CommConnectorPort)

    def test_write_comm_connector_port(self, writer):
        parent = ET.Element("PARENT")
        writer.writeFramePort(parent, _full_port())

        tag = parent.find("FRAME-PORT")
        assert tag is not None
        assert tag.find("SHORT-NAME") is not None
        assert tag.find("COMMUNICATION-DIRECTION") is not None
        assert tag.find("COMMUNICATION-DIRECTION").text == "in"

    def test_write_comm_connector_port_empty(self, writer):
        parent = ET.Element("PARENT")
        writer.writeFramePort(parent, FramePort(_parent(), "fp"))

        tag = parent.find("FRAME-PORT")
        assert tag is not None
        assert tag.find("COMMUNICATION-DIRECTION") is None

    def test_comm_connector_port_round_trip(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.writeFramePort(parent, _full_port())

        reloaded = FramePort(MockParent(), "fp")
        parser.readFramePort(_namespaced(parent)[0], reloaded)

        assert isinstance(reloaded, CommConnectorPort)
        assert reloaded.getShortName() == "fp"
        assert reloaded.getCommunicationDirection() is not None
        assert reloaded.getCommunicationDirection().getValue() == "in"

    def test_comm_connector_port_round_trip_empty(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.writeFramePort(parent, FramePort(_parent(), "fp"))

        reloaded = FramePort(MockParent(), "fp")
        parser.readFramePort(_namespaced(parent)[0], reloaded)

        assert reloaded.getCommunicationDirection() is None

    def test_frame_port_dispatch_round_trip(self, writer, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationConnector

        connector = CanCommunicationConnector(_parent(), "conn")
        connector.createFramePort("fp")
        direction = CommunicationDirectionType()
        direction.setValue(CommunicationDirectionType.OUT)
        connector.getEcuCommPortInstances()[0].setCommunicationDirection(direction)

        parent = ET.Element("PARENT")
        writer.writeCommunicationConnectorEcuCommPortInstances(parent, connector)

        instances_tag = parent.find("ECU-COMM-PORT-INSTANCES")
        assert instances_tag is not None
        frame_port_tag = instances_tag.find("FRAME-PORT")
        assert frame_port_tag is not None
        assert frame_port_tag.find("SHORT-NAME") is not None
        assert frame_port_tag.find("COMMUNICATION-DIRECTION") is not None
        assert frame_port_tag.find("COMMUNICATION-DIRECTION").text == "out"

        reloaded = CanCommunicationConnector(_parent(), "conn")
        parser.readCommunicationConnectorEcuCommPortInstances(_namespaced(parent), reloaded)
        ports = reloaded.getEcuCommPortInstances()
        assert len(ports) == 1
        assert isinstance(ports[0], FramePort)
        assert ports[0].getShortName() == "fp"
        assert ports[0].getCommunicationDirection().getValue() == "out"

    def test_ipdu_port_round_trip(self, writer, parser):
        port = IPduPort(MockParent(), "ip")
        direction = CommunicationDirectionType()
        direction.setValue(CommunicationDirectionType.OUT)
        port.setCommunicationDirection(direction)
        processing = IPduSignalProcessingEnum()
        processing.setValue(IPduSignalProcessingEnum.ENUM_DEFERRED)
        port.setIPduSignalProcessing(processing)
        rx_security = Boolean()
        rx_security.setValue(True)
        port.setRxSecurityVerification(rx_security)
        window = TimeValue()
        window.setValue("0.05")
        port.setTimestampRxAcceptanceWindow(window)
        use_auth = Boolean()
        use_auth.setValue(False)
        port.setUseAuthDataFreshness(use_auth)

        parent = ET.Element("PARENT")
        writer.writeIPduPort(parent, port)

        reloaded = IPduPort(MockParent(), "ip")
        parser.readIPduPort(_namespaced(parent)[0], reloaded)

        assert isinstance(reloaded, CommConnectorPort)
        assert reloaded.getShortName() == "ip"
        assert reloaded.getCommunicationDirection().getValue() == "out"
        assert reloaded.getIPduSignalProcessing().getValue() == "deferred"
        assert reloaded.getRxSecurityVerification().getValue() is True
        assert float(reloaded.getTimestampRxAcceptanceWindow().getValue()) == 0.05
        assert reloaded.getUseAuthDataFreshness().getValue() is False

    def test_ipdu_port_round_trip_empty(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.writeIPduPort(parent, IPduPort(MockParent(), "ip"))

        tag = parent.find("I-PDU-PORT")
        assert tag.find("COMMUNICATION-DIRECTION") is None
        assert tag.find("I-PDU-SIGNAL-PROCESSING") is None
        assert tag.find("RX-SECURITY-VERIFICATION") is None
        assert tag.find("TIMESTAMP-RX-ACCEPTANCE-WINDOW") is None
        assert tag.find("USE-AUTH-DATA-FRESHNESS") is None

        reloaded = IPduPort(MockParent(), "ip")
        parser.readIPduPort(_namespaced(parent)[0], reloaded)

        assert reloaded.getCommunicationDirection() is None
        assert reloaded.getIPduSignalProcessing() is None
        assert reloaded.getRxSecurityVerification() is None
        assert reloaded.getTimestampRxAcceptanceWindow() is None
        assert reloaded.getUseAuthDataFreshness() is None

    def test_ipdu_port_key_id_not_serialized(self, writer):
        port = IPduPort(MockParent(), "ip")
        assert not hasattr(port, "keyId")

        parent = ET.Element("PARENT")
        writer.writeIPduPort(parent, port)

        xml_text = ET.tostring(parent, encoding="unicode")
        assert "KEY-ID" not in xml_text


# ==================== ISignalPort (Table 6.5, p.306) ====================


def _full_isignal_port() -> ISignalPort:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter, DataFilterTypeEnum
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import HandleInvalidEnum
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalPort

    port = ISignalPort(_parent(), "isp")
    data_filter = DataFilter()
    data_filter.setDataFilterType(DataFilterTypeEnum().setValue(DataFilterTypeEnum.ALWAYS))
    port.setDataFilter(data_filter)
    ref = RefType()
    ref.dest = "DDS-CP-QOS-PROFILE"
    ref.value = "/profiles/p1"
    port.setDdsQosProfileRef(ref)
    first_timeout = TimeValue()
    first_timeout.value = 5.0
    port.setFirstTimeout(first_timeout)
    port.setHandleInvalid(HandleInvalidEnum().setValue(HandleInvalidEnum.KEEP))
    timeout = TimeValue()
    timeout.value = 1.0
    port.setTimeout(timeout)
    return port


class TestISignalPort:
    def test_write_isignal_port_full(self, writer):
        parent = ET.Element("PARENT")
        writer.writeISignalPort(parent, _full_isignal_port())

        tag = parent.find("I-SIGNAL-PORT")
        assert tag is not None
        assert tag.find("SHORT-NAME") is not None

        data_filter = tag.find("DATA-FILTER")
        assert data_filter is not None
        assert data_filter.find("DATA-FILTER-TYPE").text == "ALWAYS"

        ref = tag.find("DDS-QOS-PROFILE-REF")
        assert ref is not None
        assert ref.get("DEST") == "DDS-CP-QOS-PROFILE"
        assert ref.text == "/profiles/p1"

        assert tag.find("FIRST-TIMEOUT").text == "5.0"
        assert tag.find("HANDLE-INVALID").text == "keep"
        assert tag.find("TIMEOUT").text == "1.0"

        children = [child.tag for child in tag if child.tag in ("DATA-FILTER", "DDS-QOS-PROFILE-REF", "FIRST-TIMEOUT", "HANDLE-INVALID", "TIMEOUT")]
        assert children == ["DATA-FILTER", "DDS-QOS-PROFILE-REF", "FIRST-TIMEOUT", "HANDLE-INVALID", "TIMEOUT"]

    def test_write_isignal_port_empty(self, writer):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalPort

        parent = ET.Element("PARENT")
        writer.writeISignalPort(parent, ISignalPort(_parent(), "isp"))

        tag = parent.find("I-SIGNAL-PORT")
        assert tag is not None
        assert tag.find("DATA-FILTER") is None
        assert tag.find("DDS-QOS-PROFILE-REF") is None
        assert tag.find("FIRST-TIMEOUT") is None
        assert tag.find("HANDLE-INVALID") is None
        assert tag.find("TIMEOUT") is None

    def test_isignal_port_round_trip(self, writer):
        parser = ARXMLParser()
        parent = ET.Element("PARENT")
        writer.writeISignalPort(parent, _full_isignal_port())

        port = _full_isignal_port().__class__(_parent(), "isp2")
        parser.readISignalPort(_namespaced(parent.find("I-SIGNAL-PORT")), port)
        assert port.getDataFilter().getDataFilterType().getValue() == "ALWAYS"
        assert port.getDdsQosProfileRef().getValue() == "/profiles/p1"
        assert port.getFirstTimeout().getValue() == 5.0
        assert port.getHandleInvalid().getValue() == "keep"
        assert port.getTimeout().getValue() == 1.0
