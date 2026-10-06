"""Writer round-trip tests for LinCommunicationController (Table 3.37, p.93).

The class is abstract with no own XML element: its XSD group
LIN-COMMUNICATION-CONTROLLER (AUTOSAR_00052.xsd line 77049) is empty and the single
attribute protocolVersion surfaces as PROTOCOL-VERSION in
LIN-COMMUNICATION-CONTROLLER-CONTENT (line 77058), carried inside the
LIN-MASTER-CONDITIONAL / LIN-SLAVE-CONDITIONAL wrappers of the concrete subclasses
LinMaster / LinSlave. Coverage therefore targets the reusable
writeLinCommunicationController helper (Rule 0001.7) plus the full concrete
LIN-MASTER round-trip through the CONDITIONAL wrapper and the EcuInstance
COMM-CONTROLLERS dispatch; element order per XSD:
WAKE-UP-BY-CONTROLLER-SUPPORTED (COMMUNICATION-CONTROLLER-CONTENT) before
PROTOCOL-VERSION.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _parent():
    return ET.Element("PARENT")


def _boolean(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _string(value):
    string = String()
    string.setValue(value)
    return string


def _new_instance_with_master(short_name="ctrl"):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    instance = EcuInstance(pkg, "Ecu")
    return instance, instance.createLinMaster(short_name)


def _write_and_reread(instance):
    parent = ET.Element("ECU-INSTANCE")
    ARXMLWriter().writeEcuInstanceCommControllers(parent, instance)
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, ET.tostring(parent).decode("utf-8")))

    pkg = AUTOSAR.getInstance().createARPackage("Parsed")
    parsed_instance = EcuInstance(pkg, "Ecu")
    ARXMLParser().readEcuInstanceCommControllers(root[0], parsed_instance)
    return parsed_instance.getCommControllers()


class TestWriteLinCommunicationController:
    def test_write_none_members_omits_children(self):
        _, controller = _new_instance_with_master()

        parent = _parent()
        ARXMLWriter().writeLinCommunicationController(parent, controller)

        assert len(parent) == 0

    def test_write_protocol_version_field_value(self):
        _, controller = _new_instance_with_master()
        controller.setWakeUpByControllerSupported(_boolean(True))
        controller.setProtocolVersion(_string("LIN22"))

        parent = _parent()
        ARXMLWriter().writeLinCommunicationController(parent, controller)

        assert parent.find("PROTOCOL-VERSION").text == "LIN22"
        children = [child.tag for child in parent]
        assert children.index("WAKE-UP-BY-CONTROLLER-SUPPORTED") < children.index("PROTOCOL-VERSION")

    def test_write_base_helper_called_exactly_once(self):
        _, controller = _new_instance_with_master()
        controller.setWakeUpByControllerSupported(_boolean(True))

        parent = _parent()
        ARXMLWriter().writeLinCommunicationController(parent, controller)

        assert len(parent.findall("WAKE-UP-BY-CONTROLLER-SUPPORTED")) == 1


class TestLinCommunicationControllerRoundTrip:
    def test_round_trip_through_lin_master(self):
        _, controller = _new_instance_with_master("lin_ctrl")
        controller.setWakeUpByControllerSupported(_boolean(True))
        controller.setProtocolVersion(_string("LIN22"))

        parsed_controllers = _write_and_reread(controller.getParent())
        assert len(parsed_controllers) == 1
        parsed = parsed_controllers[0]
        assert parsed.getShortName() == "lin_ctrl"
        assert parsed.getWakeUpByControllerSupported() is not None
        assert parsed.getWakeUpByControllerSupported().getValue() is True
        assert parsed.getProtocolVersion() is not None
        assert parsed.getProtocolVersion().getValue() == "LIN22"

    def test_round_trip_empty_controller(self):
        instance, _ = _new_instance_with_master("empty_ctrl")

        parsed_controllers = _write_and_reread(instance)
        assert len(parsed_controllers) == 1
        parsed = parsed_controllers[0]
        assert parsed.getShortName() == "empty_ctrl"
        assert parsed.getWakeUpByControllerSupported() is None
        assert parsed.getProtocolVersion() is None
