"""Writer round-trip tests for UserDefinedCommunicationConnector (Table 3.131, p.180).

XML element order per XSD USER-DEFINED-COMMUNICATION-CONNECTOR (AUTOSAR_00052.xsd
line 128622): heritage groups (SHORT-NAME via writeIdentifiable) first, then the
inherited COMMUNICATION-CONNECTOR group content in sequenceOffset order
(COMM-CONTROLLER-REF, CREATE-ECU-WAKEUP-SOURCE, DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED,
ECU-COMM-PORT-INSTANCES, PNC-FILTER-ARRAY-MASKS, PNC-GATEWAY-TYPE); the
USER-DEFINED-COMMUNICATION-CONNECTOR own group (lines 128603-128611) is an empty
sequence — no atpVariation wrapper.
writeUserDefinedCommunicationConnector calls the reusable writeCommunicationConnector
helper exactly once (the writeTtcanCommunicationConnector leveling — the CONNECTORS
dispatch creates the SubElement).

Verifies that a UserDefinedCommunicationConnector created on an EcuInstance survives
a full set -> save -> reload cycle with its inherited CommunicationConnector
attributes intact, including the bare-connector case.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport import UserDefinedCommunicationConnector
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance, PncGatewayTypeEnum
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

COMMUNICATION_CONNECTOR_XSD_ORDER = [
    "SHORT-NAME",
    "COMM-CONTROLLER-REF",
    "CREATE-ECU-WAKEUP-SOURCE",
    "ECU-COMM-PORT-INSTANCES",
    "PNC-FILTER-ARRAY-MASKS",
    "PNC-GATEWAY-TYPE",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser(options={"warning": True})


def _reload(parser, path):
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    parser.load(path, document)
    return document


def _new_connector(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    ecu = pkg.createEcuInstance("Ecu")
    return UserDefinedCommunicationConnector(ecu, name)


def _full_connector():
    connector = _new_connector("UserDefinedCommunicationConnector")
    comm_controller_ref = RefType()
    comm_controller_ref.setDest("CAN-COMMUNICATION-CONTROLLER")
    comm_controller_ref.setValue("/EcuInst/Ctrl")
    connector.setCommControllerRef(comm_controller_ref)
    wakeup_flag = Boolean()
    wakeup_flag.setValue(True)
    connector.setCreateEcuWakeupSource(wakeup_flag)
    connector.createISignalPort("Port")
    mask = PositiveInteger()
    mask.setValue("255")
    connector.addPncFilterArrayMask(mask)
    gateway_type = PncGatewayTypeEnum()
    gateway_type.setValue(PncGatewayTypeEnum.ACTIVE)
    connector.setPncGatewayType(gateway_type)
    return connector


def _write_connector(connector):
    element = ET.Element("USER-DEFINED-COMMUNICATION-CONNECTOR")
    ARXMLWriter().writeUserDefinedCommunicationConnector(element, connector)
    return element


def _namespaced(element):
    xml_text = ET.tostring(element, encoding="unicode")
    return ET.fromstring(xml_text.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))


class TestWriteUserDefinedCommunicationConnector:
    def test_entry_point_emits_short_name(self):
        element = _write_connector(_full_connector())

        assert element.find("SHORT-NAME").text == "UserDefinedCommunicationConnector"

    def test_entry_point_writes_inherited_levels_in_xsd_order_exactly_once(self):
        element = _write_connector(_full_connector())

        assert [child.tag for child in element] == COMMUNICATION_CONNECTOR_XSD_ORDER

        # direct children only — a nested I-SIGNAL-PORT legitimately carries its own SHORT-NAME
        for tag in COMMUNICATION_CONNECTOR_XSD_ORDER:
            assert len(element.findall(tag)) == 1, tag

    def test_entry_point_writes_field_values(self):
        element = _write_connector(_full_connector())

        comm_controller_ref = element.find("COMM-CONTROLLER-REF")
        assert comm_controller_ref.get("DEST") == "CAN-COMMUNICATION-CONTROLLER"
        assert comm_controller_ref.text == "/EcuInst/Ctrl"
        assert element.find("CREATE-ECU-WAKEUP-SOURCE").text == "true"
        assert element.find("ECU-COMM-PORT-INSTANCES/I-SIGNAL-PORT/SHORT-NAME").text == "Port"
        assert element.find("PNC-FILTER-ARRAY-MASKS/PNC-FILTER-ARRAY-MASK").text == "255"
        assert element.find("PNC-GATEWAY-TYPE").text == "ACTIVE"

    def test_bare_connector_emits_short_name_only(self):
        element = _write_connector(_new_connector("Connector"))

        assert element.find("SHORT-NAME").text == "Connector"
        assert [child.tag for child in element] == ["SHORT-NAME"]

    def test_round_trip_full_through_user_defined_communication_connector(self):
        element = _write_connector(_full_connector())
        reloaded = _new_connector("UserDefinedCommunicationConnector")
        ARXMLParser().readUserDefinedCommunicationConnector(_namespaced(element), reloaded)

        assert reloaded.getShortName() == "UserDefinedCommunicationConnector"
        comm_controller_ref = reloaded.getCommControllerRef()
        assert comm_controller_ref.getValue() == "/EcuInst/Ctrl"
        assert comm_controller_ref.getDest() == "CAN-COMMUNICATION-CONTROLLER"
        assert reloaded.getCreateEcuWakeupSource().getValue() is True
        ports = reloaded.getEcuCommPortInstances()
        assert len(ports) == 1
        assert ports[0].getShortName() == "Port"
        masks = reloaded.getPncFilterArrayMasks()
        assert len(masks) == 1
        assert masks[0].getValue() == 255
        assert reloaded.getPncGatewayType().getValue() == "ACTIVE"

    def test_round_trip_empty_through_user_defined_communication_connector(self):
        element = _write_connector(_new_connector("Connector"))
        reloaded = _new_connector("Connector")
        ARXMLParser().readUserDefinedCommunicationConnector(_namespaced(element), reloaded)

        assert reloaded.getShortName() == "Connector"
        assert reloaded.getCommControllerRef() is None
        assert reloaded.getEcuCommPortInstances() == []
        assert reloaded.getPncFilterArrayMasks() == []


def test_round_trip_full(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    ecu = pkg.createEcuInstance("Ecu")
    connector = ecu.createUserDefinedCommunicationConnector("UserDefinedCommunicationConnector")
    comm_controller_ref = RefType()
    comm_controller_ref.setDest("CAN-COMMUNICATION-CONTROLLER")
    comm_controller_ref.setValue("/EcuInst/Ctrl")
    connector.setCommControllerRef(comm_controller_ref)
    wakeup_flag = Boolean()
    wakeup_flag.setValue(True)
    connector.setCreateEcuWakeupSource(wakeup_flag)
    connector.createISignalPort("Port")
    mask = PositiveInteger()
    mask.setValue("255")
    connector.addPncFilterArrayMask(mask)
    gateway_type = PncGatewayTypeEnum()
    gateway_type.setValue(PncGatewayTypeEnum.ACTIVE)
    connector.setPncGatewayType(gateway_type)

    out_file = str(tmp_path / "user_defined_communication_connector.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_pkg = document.find("Pkg")
    assert re_pkg is not None

    re_ecu = re_pkg.getReferrableElement("Ecu", EcuInstance)
    assert re_ecu is not None

    re_connectors = re_ecu.getConnectors()
    assert len(re_connectors) == 1
    re_connector = re_connectors[0]
    assert isinstance(re_connector, UserDefinedCommunicationConnector)
    assert re_connector.getShortName() == "UserDefinedCommunicationConnector"
    re_comm_controller_ref = re_connector.getCommControllerRef()
    assert re_comm_controller_ref.getValue() == "/EcuInst/Ctrl"
    assert re_comm_controller_ref.getDest() == "CAN-COMMUNICATION-CONTROLLER"
    assert re_connector.getCreateEcuWakeupSource().getValue() is True
    re_ports = re_connector.getEcuCommPortInstances()
    assert len(re_ports) == 1
    assert re_ports[0].getShortName() == "Port"
    re_masks = re_connector.getPncFilterArrayMasks()
    assert len(re_masks) == 1
    assert re_masks[0].getValue() == 255
    assert re_connector.getPncGatewayType().getValue() == "ACTIVE"


def test_round_trip_empty(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    ecu = pkg.createEcuInstance("Ecu")
    ecu.createUserDefinedCommunicationConnector("EmptyConnector")

    out_file = str(tmp_path / "user_defined_communication_connector_empty.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_pkg = document.find("Pkg")

    re_ecu = re_pkg.getReferrableElement("Ecu", EcuInstance)
    re_connectors = re_ecu.getConnectors()
    assert len(re_connectors) == 1
    assert isinstance(re_connectors[0], UserDefinedCommunicationConnector)
    assert re_connectors[0].getShortName() == "EmptyConnector"
    assert re_connectors[0].getCommControllerRef() is None
    assert re_connectors[0].getEcuCommPortInstances() == []
    assert re_connectors[0].getPncFilterArrayMasks() == []
