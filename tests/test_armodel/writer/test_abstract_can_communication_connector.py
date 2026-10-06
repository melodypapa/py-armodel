"""Writer round-trip tests for AbstractCanCommunicationConnector (Table 3.22, p.73).

The class is abstract with no own attribute rows (Table 3.22 renders the
Attribute header only) and its XSD group ABSTRACT-CAN-COMMUNICATION-CONNECTOR
(AUTOSAR_00052.xsd line 135) is an empty <xsd:sequence/>: the abstract level
contributes no XML elements of its own. Coverage therefore runs through the
concrete CAN-COMMUNICATION-CONNECTOR emission (the CONNECTORS dispatch on
writeEcuInstanceConnectors, whose writeCanCommunicationConnector entry helper
calls the base writeCommunicationConnector helper exactly once) and asserts the
abstract level neither adds nor drops elements: the CAN-COMMUNICATION-CONNECTOR
children go straight from the IDENTIFIABLE SHORT-NAME to the base
COMMUNICATION-CONNECTOR group and the subclass CAN-COMMUNICATION-CONNECTOR
group, with empty wrappers omitted.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import AbstractCanCommunicationConnector, CanCommunicationConnector
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
    connector = instance.createCanCommunicationConnector("conn")
    if full:
        connector.setCommControllerRef(_ref("/can/ctrl", "CAN-COMMUNICATION-CONTROLLER"))
        connector.setCreateEcuWakeupSource(_boolean(True))
        connector.setDynamicPncToChannelMappingEnabled(_boolean(False))
        connector.createFramePort("fp").setCommunicationDirection(CommunicationDirectionType().setValue(CommunicationDirectionType.IN))
        connector.addPncFilterArrayMask(_pos_int("255"))
        connector.addPncFilterArrayMask(_pos_int("1"))
        connector.setPncGatewayType(_gateway_type(PncGatewayTypeEnum.ACTIVE))
        connector.setPncWakeupCanId(_pos_int("401"))
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


class TestWriteAbstractCanCommunicationConnector:
    def test_writes_instance_of_abstract_can_communication_connector_without_abstract_level_elements(self):
        instance = _new_instance_with_connector(full=True)

        parent = _write_instance(instance)
        connector_tag = parent.find("CONNECTORS/CAN-COMMUNICATION-CONNECTOR")
        assert connector_tag is not None

        tags = [child.tag for child in connector_tag]
        assert tags == ["SHORT-NAME"] + BASE_XSD_ORDER + ["PNC-WAKEUP-CAN-ID"]

        ref = connector_tag.find("COMM-CONTROLLER-REF")
        assert len(connector_tag.findall("COMM-CONTROLLER-REF")) == 1
        assert ref.get("DEST") == "CAN-COMMUNICATION-CONTROLLER"
        assert ref.text == "/can/ctrl"
        assert connector_tag.find("CREATE-ECU-WAKEUP-SOURCE").text == "true"
        assert connector_tag.find("PNC-GATEWAY-TYPE").text == "ACTIVE"
        assert connector_tag.find("PNC-WAKEUP-CAN-ID").text == "401"

    def test_write_empty_connector_emits_no_abstract_level_elements(self):
        instance = _new_instance_with_connector(full=False)

        parent = _write_instance(instance)
        connector_tag = parent.find("CONNECTORS/CAN-COMMUNICATION-CONNECTOR")
        assert connector_tag is not None
        assert [child.tag for child in connector_tag] == ["SHORT-NAME"]

    def test_round_trip_full(self):
        instance = _new_instance_with_connector(full=True)

        connectors = _reread_instance(_write_instance(instance))
        assert len(connectors) == 1
        connector = connectors[0]
        assert isinstance(connector, AbstractCanCommunicationConnector)
        assert isinstance(connector, CanCommunicationConnector)

        ref = connector.getCommControllerRef()
        assert ref.getValue() == "/can/ctrl"
        assert ref.getDest() == "CAN-COMMUNICATION-CONTROLLER"
        assert connector.getCreateEcuWakeupSource().getValue() is True
        assert connector.getDynamicPncToChannelMappingEnabled().getValue() is False

        ports = connector.getEcuCommPortInstances()
        assert len(ports) == 1
        assert ports[0].getShortName() == "fp"
        assert ports[0].getCommunicationDirection().getValue() == "IN"

        assert [mask.getValue() for mask in connector.getPncFilterArrayMasks()] == [255, 1]
        assert connector.getPncGatewayType().getValue() == "ACTIVE"
        assert connector.getPncWakeupCanId().getValue() == 401

    def test_round_trip_empty(self):
        instance = _new_instance_with_connector(full=False)

        connectors = _reread_instance(_write_instance(instance))
        assert len(connectors) == 1
        connector = connectors[0]
        assert isinstance(connector, AbstractCanCommunicationConnector)

        assert connector.getCommControllerRef() is None
        assert connector.getCreateEcuWakeupSource() is None
        assert connector.getDynamicPncToChannelMappingEnabled() is None
        assert connector.getEcuCommPortInstances() == []
        assert connector.getPncFilterArrayMasks() == []
        assert connector.getPncGatewayType() is None
