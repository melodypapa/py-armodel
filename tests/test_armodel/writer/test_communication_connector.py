"""Writer round-trip tests for CommunicationConnector (Table 3.4, p.54).

XML element order per XSD group COMMUNICATION-CONNECTOR: COMM-CONTROLLER-REF,
CREATE-ECU-WAKEUP-SOURCE, DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED,
ECU-COMM-PORT-INSTANCES, PNC-FILTER-ARRAY-MASKS, PNC-GATEWAY-TYPE.
Coverage runs through the CONNECTORS dispatch on writeEcuInstanceConnectors.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import CommunicationDirectionType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import PncGatewayTypeEnum
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = ["COMM-CONTROLLER-REF", "CREATE-ECU-WAKEUP-SOURCE", "DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED", "ECU-COMM-PORT-INSTANCES", "PNC-FILTER-ARRAY-MASKS", "PNC-GATEWAY-TYPE"]


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


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _pos_int(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


def _boolean(value):
    value_obj = Boolean()
    value_obj.setValue(value)
    return value_obj


def _gateway_type(member):
    enum = PncGatewayTypeEnum()
    enum.setValue(member)
    return enum


def _full_connector():
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationConnector

    connector = CanCommunicationConnector(MockParent(), "conn")
    connector.setCommControllerRef(_ref("/can/ctrl", "CAN-COMMUNICATION-CONTROLLER"))
    connector.setCreateEcuWakeupSource(_boolean(True))
    connector.setDynamicPncToChannelMappingEnabled(_boolean(False))
    connector.createFramePort("fp").setCommunicationDirection(CommunicationDirectionType().setValue(CommunicationDirectionType.IN))
    connector.addPncFilterArrayMask(_pos_int("255"))
    connector.addPncFilterArrayMask(_pos_int("1"))
    connector.setPncGatewayType(_gateway_type(PncGatewayTypeEnum.ACTIVE))
    return connector


def _bare_connector():
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationConnector

    return CanCommunicationConnector(MockParent(), "conn")


def _write_connector(connector):
    parent = ET.Element("PARENT")
    connector_tag = ET.SubElement(parent, "CAN-COMMUNICATION-CONNECTOR")
    ARXMLWriter().writeCanCommunicationConnector(connector_tag, connector)
    return parent


def _namespaced_connector_tag(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteCommunicationConnector:
    def test_write_all_six_elements_in_xsd_order(self, writer):
        parent = _write_connector(_full_connector())
        connector_tag = parent.find("CAN-COMMUNICATION-CONNECTOR")
        assert connector_tag is not None
        tags = [child.tag for child in connector_tag]
        assert tags == ["SHORT-NAME"] + XSD_ORDER

    def test_write_field_values(self, writer):
        parent = _write_connector(_full_connector())
        connector_tag = parent.find("CAN-COMMUNICATION-CONNECTOR")

        ref = connector_tag.find("COMM-CONTROLLER-REF")
        assert ref.get("DEST") == "CAN-COMMUNICATION-CONTROLLER"
        assert ref.text == "/can/ctrl"

        assert connector_tag.find("CREATE-ECU-WAKEUP-SOURCE").text == "true"
        assert connector_tag.find("DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED").text == "false"

        instances = connector_tag.find("ECU-COMM-PORT-INSTANCES")
        assert instances is not None
        frame_port = instances.find("FRAME-PORT")
        assert frame_port is not None
        assert frame_port.find("SHORT-NAME").text == "fp"

        masks = connector_tag.find("PNC-FILTER-ARRAY-MASKS")
        assert masks is not None
        assert [mask.text for mask in masks.findall("PNC-FILTER-ARRAY-MASK")] == ["255", "1"]

        assert connector_tag.find("PNC-GATEWAY-TYPE").text == "ACTIVE"

    def test_write_omits_empty_wrappers_and_optional_elements(self, writer):
        parent = _write_connector(_bare_connector())
        connector_tag = parent.find("CAN-COMMUNICATION-CONNECTOR")
        assert connector_tag is not None
        assert connector_tag.find("COMM-CONTROLLER-REF") is None
        assert connector_tag.find("CREATE-ECU-WAKEUP-SOURCE") is None
        assert connector_tag.find("DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED") is None
        assert connector_tag.find("ECU-COMM-PORT-INSTANCES") is None
        assert connector_tag.find("PNC-FILTER-ARRAY-MASKS") is None
        assert connector_tag.find("PNC-GATEWAY-TYPE") is None

    def test_round_trip_full(self, writer, parser):
        parent = _write_connector(_full_connector())
        reloaded = _bare_connector()
        parser.readCanCommunicationConnector(_namespaced_connector_tag(parent), reloaded)

        ref = reloaded.getCommControllerRef()
        assert ref is not None
        assert ref.getValue() == "/can/ctrl"
        assert ref.getDest() == "CAN-COMMUNICATION-CONTROLLER"

        assert reloaded.getCreateEcuWakeupSource().getValue() is True
        assert reloaded.getDynamicPncToChannelMappingEnabled().getValue() is False

        ports = reloaded.getEcuCommPortInstances()
        assert len(ports) == 1
        assert ports[0].getShortName() == "fp"
        assert ports[0].getCommunicationDirection().getValue() == "IN"

        masks = reloaded.getPncFilterArrayMasks()
        assert [mask.getValue() for mask in masks] == [255, 1]

        assert reloaded.getPncGatewayType().getValue() == "ACTIVE"

    def test_round_trip_empty(self, writer, parser):
        parent = _write_connector(_bare_connector())
        reloaded = _bare_connector()
        parser.readCanCommunicationConnector(_namespaced_connector_tag(parent), reloaded)

        assert reloaded.getCommControllerRef() is None
        assert reloaded.getCreateEcuWakeupSource() is None
        assert reloaded.getDynamicPncToChannelMappingEnabled() is None
        assert reloaded.getEcuCommPortInstances() == []
        assert reloaded.getPncFilterArrayMasks() == []
        assert reloaded.getPncGatewayType() is None
