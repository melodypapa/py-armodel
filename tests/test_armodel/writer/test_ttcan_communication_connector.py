"""Writer round-trip tests for TtcanCommunicationConnector (Table 3.27, p.77).

The class has no own attribute rows and its XSD group TTCAN-COMMUNICATION-CONNECTOR
(AUTOSAR_00052.xsd line 126966) is an empty <xsd:sequence/>: the concrete level
contributes no XML elements of its own and the complexType (line 126975) is a flat
sequence of heritage groups (no VARIANTS wrapper). writeTtcanCommunicationConnector
emits the TTCAN-COMMUNICATION-CONNECTOR element and calls the base
writeCommunicationConnector helper exactly once. The class is emitted as a concrete
element of the EcuInstance CONNECTORS choice (line 50399, Rule 0001.7): dispatch
coverage runs through the TtcanCommunicationConnector isinstance branch on
writeEcuInstanceConnectors.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import TtcanCommunicationConnector
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import CommunicationDirectionType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance, PncGatewayTypeEnum
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

BASE_XSD_ORDER = ["COMM-CONTROLLER-REF", "CREATE-ECU-WAKEUP-SOURCE", "DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED", "ECU-COMM-PORT-INSTANCES", "PNC-FILTER-ARRAY-MASKS", "PNC-GATEWAY-TYPE"]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


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


def _new_instance_with_connector(full):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    instance = EcuInstance(pkg, "Ecu")
    connector = instance.createTtcanCommunicationConnector("ttcan_conn")
    if full:
        connector.setCommControllerRef(_ref("/ecu/ttcan_ctl", "TTCAN-COMMUNICATION-CONTROLLER"))
        connector.setCreateEcuWakeupSource(_boolean(True))
        connector.setDynamicPncToChannelMappingEnabled(_boolean(False))
        connector.createFramePort("fp").setCommunicationDirection(CommunicationDirectionType().setValue(CommunicationDirectionType.IN))
        connector.addPncFilterArrayMask(_pos_int("255"))
        connector.addPncFilterArrayMask(_pos_int("1"))
        connector.setPncGatewayType(_gateway_type(PncGatewayTypeEnum.ACTIVE))
    return instance


def _write_instance(instance):
    parent = ET.Element("ECU-INSTANCE")
    ARXMLWriter().writeEcuInstanceConnectors(parent, instance)
    return parent


def _reread_instance(parent):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, ET.tostring(parent).decode("utf-8")))
    pkg = AUTOSAR.getInstance().createARPackage("Parsed")
    parsed_instance = EcuInstance(pkg, "Ecu")
    ARXMLParser().readEcuInstanceConnectors(root[0], parsed_instance)
    return parsed_instance.getConnectors()


class TestWriteTtcanCommunicationConnector:
    def test_entry_point_emits_short_name_and_base_level_only(self):
        connector = _new_instance_with_connector(full=True).getConnectors()[0]

        parent = ET.Element("PARENT")
        child_element = ET.SubElement(parent, "TTCAN-COMMUNICATION-CONNECTOR")
        ARXMLWriter().writeTtcanCommunicationConnector(child_element, connector)
        connector_tag = parent.find("TTCAN-COMMUNICATION-CONNECTOR")

        assert connector_tag is not None
        assert [child.tag for child in connector_tag] == ["SHORT-NAME"] + BASE_XSD_ORDER

    def test_entry_point_writes_field_values(self):
        connector = _new_instance_with_connector(full=True).getConnectors()[0]

        parent = ET.Element("PARENT")
        child_element = ET.SubElement(parent, "TTCAN-COMMUNICATION-CONNECTOR")
        ARXMLWriter().writeTtcanCommunicationConnector(child_element, connector)
        connector_tag = parent.find("TTCAN-COMMUNICATION-CONNECTOR")

        ref = connector_tag.find("COMM-CONTROLLER-REF")
        assert ref.get("DEST") == "TTCAN-COMMUNICATION-CONTROLLER"
        assert ref.text == "/ecu/ttcan_ctl"
        assert connector_tag.find("CREATE-ECU-WAKEUP-SOURCE").text == "true"
        assert connector_tag.find("DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED").text == "false"
        assert connector_tag.find("ECU-COMM-PORT-INSTANCES/FRAME-PORT/SHORT-NAME").text == "fp"
        masks = connector_tag.findall("PNC-FILTER-ARRAY-MASKS/PNC-FILTER-ARRAY-MASK")
        assert [mask.text for mask in masks] == ["255", "1"]
        assert connector_tag.find("PNC-GATEWAY-TYPE").text == "active"

    def test_bare_connector_emits_short_name_only(self):
        connector = _new_instance_with_connector(full=False).getConnectors()[0]

        parent = ET.Element("PARENT")
        child_element = ET.SubElement(parent, "TTCAN-COMMUNICATION-CONNECTOR")
        ARXMLWriter().writeTtcanCommunicationConnector(child_element, connector)
        connector_tag = parent.find("TTCAN-COMMUNICATION-CONNECTOR")

        assert connector_tag is not None
        assert [child.tag for child in connector_tag] == ["SHORT-NAME"]
        for tag in BASE_XSD_ORDER:
            assert connector_tag.find(tag) is None, tag

    def test_ecu_instance_consumer_emits_connectors_choice(self):
        instance = _new_instance_with_connector(full=True)
        parent = _write_instance(instance)

        connectors_tag = parent.find("CONNECTORS")
        connector_element = connectors_tag.find("TTCAN-COMMUNICATION-CONNECTOR")
        assert connector_element is not None
        assert connector_element.find("SHORT-NAME").text == "ttcan_conn"
        assert connector_element.find("COMM-CONTROLLER-REF").text == "/ecu/ttcan_ctl"

    def test_ecu_instance_consumer_keeps_can_branch_disjoint(self):
        instance = _new_instance_with_connector(full=False)
        instance.createCanCommunicationConnector("can_conn")
        parent = _write_instance(instance)

        connectors_tag = parent.find("CONNECTORS")
        assert connectors_tag.find("TTCAN-COMMUNICATION-CONNECTOR/SHORT-NAME").text == "ttcan_conn"
        assert connectors_tag.find("CAN-COMMUNICATION-CONNECTOR/SHORT-NAME").text == "can_conn"

    def test_round_trip_full(self):
        instance = _new_instance_with_connector(full=True)

        connectors = _reread_instance(_write_instance(instance))
        assert len(connectors) == 1
        connector = connectors[0]
        assert isinstance(connector, TtcanCommunicationConnector)

        ref = connector.getCommControllerRef()
        assert ref.getValue() == "/ecu/ttcan_ctl"
        assert ref.getDest() == "TTCAN-COMMUNICATION-CONTROLLER"
        assert connector.getCreateEcuWakeupSource().getValue() is True
        assert connector.getDynamicPncToChannelMappingEnabled().getValue() is False

        ports = connector.getEcuCommPortInstances()
        assert len(ports) == 1
        assert ports[0].getShortName() == "fp"
        assert ports[0].getCommunicationDirection().getValue() == "in"

        assert [mask.getValue() for mask in connector.getPncFilterArrayMasks()] == [255, 1]
        assert connector.getPncGatewayType().getValue() == "active"

    def test_round_trip_empty(self):
        instance = _new_instance_with_connector(full=False)

        connectors = _reread_instance(_write_instance(instance))
        assert len(connectors) == 1
        connector = connectors[0]
        assert isinstance(connector, TtcanCommunicationConnector)

        assert connector.getCommControllerRef() is None
        assert connector.getCreateEcuWakeupSource() is None
        assert connector.getDynamicPncToChannelMappingEnabled() is None
        assert connector.getEcuCommPortInstances() == []
        assert connector.getPncFilterArrayMasks() == []
        assert connector.getPncGatewayType() is None
