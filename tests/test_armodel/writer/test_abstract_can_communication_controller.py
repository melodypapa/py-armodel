"""Writer round-trip tests for AbstractCanCommunicationController (Table 3.12, p.63).

The class is abstract with no own XML element: its XSD group
ABSTRACT-CAN-COMMUNICATION-CONTROLLER (AUTOSAR_00052.xsd line 144) is empty and the
single attribute canControllerAttributes surfaces as CAN-CONTROLLER-ATTRIBUTES in
ABSTRACT-CAN-COMMUNICATION-CONTROLLER-CONTENT (line 196, element at line 203 — a
choice of CAN-CONTROLLER-CONFIGURATION / CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS).
Coverage therefore targets the reusable writeAbstractCanCommunicationController helper
(Rule 0001.7) plus the full concrete CAN-COMMUNICATION-CONTROLLER round-trip through
the CONDITIONAL wrapper; element order per XSD: WAKE-UP-BY-CONTROLLER-SUPPORTED
(COMMUNICATION-CONTROLLER-CONTENT, line 20421) before CAN-CONTROLLER-ATTRIBUTES.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerConfiguration,
    CanControllerConfigurationRequirements,
)
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


def _int(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _new_instance_with_controller(short_name="ctrl"):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    instance = EcuInstance(pkg, "Ecu")
    return instance, instance.createCanCommunicationController(short_name)


def _new_configuration():
    configuration = CanControllerConfiguration()
    configuration.setPropSeg(_int("4"))
    configuration.setSyncJumpWidth(_int("1"))
    configuration.setTimeSeg1(_int("13"))
    configuration.setTimeSeg2(_int("2"))
    return configuration


def _write_and_reread(instance):
    parent = ET.Element("ECU-INSTANCE")
    ARXMLWriter().writeEcuInstanceCommControllers(parent, instance)
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, ET.tostring(parent).decode("utf-8")))

    pkg = AUTOSAR.getInstance().createARPackage("Parsed")
    parsed_instance = EcuInstance(pkg, "Ecu")
    ARXMLParser().readEcuInstanceCommControllers(root[0], parsed_instance)
    return parsed_instance.getCommControllers()


class TestWriteAbstractCanCommunicationController:
    def test_write_none_members_omits_children(self):
        _, controller = _new_instance_with_controller()
        parent = _parent()
        ARXMLWriter().writeAbstractCanCommunicationController(parent, controller)
        assert len(parent) == 0

    def test_write_configuration_attributes_field_values(self):
        _, controller = _new_instance_with_controller()
        controller.setWakeUpByControllerSupported(_boolean(True))
        controller.setCanControllerAttributes(_new_configuration())

        parent = _parent()
        ARXMLWriter().writeAbstractCanCommunicationController(parent, controller)

        assert parent.find("WAKE-UP-BY-CONTROLLER-SUPPORTED").text == "true"
        children = [child.tag for child in parent]
        assert children.index("WAKE-UP-BY-CONTROLLER-SUPPORTED") < children.index("CAN-CONTROLLER-ATTRIBUTES")

        configuration = parent.find("CAN-CONTROLLER-ATTRIBUTES/CAN-CONTROLLER-CONFIGURATION")
        assert configuration is not None
        assert configuration.find("PROP-SEG").text == "4"
        assert configuration.find("SYNC-JUMP-WIDTH").text == "1"
        assert configuration.find("TIME-SEG-1").text == "13"
        assert configuration.find("TIME-SEG-2").text == "2"

    def test_write_requirements_attributes_field_values(self):
        requirements = CanControllerConfigurationRequirements()
        requirements.setMaxNumberOfTimeQuantaPerBit(_int("32"))
        requirements.setMinNumberOfTimeQuantaPerBit(_int("16"))
        _, controller = _new_instance_with_controller()
        controller.setCanControllerAttributes(requirements)

        parent = _parent()
        ARXMLWriter().writeAbstractCanCommunicationController(parent, controller)

        written = parent.find("CAN-CONTROLLER-ATTRIBUTES/CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS")
        assert written is not None
        assert written.find("MAX-NUMBER-OF-TIME-QUANTA-PER-BIT").text == "32"
        assert written.find("MIN-NUMBER-OF-TIME-QUANTA-PER-BIT").text == "16"

    def test_write_base_helper_called_exactly_once(self):
        _, controller = _new_instance_with_controller()
        controller.setWakeUpByControllerSupported(_boolean(True))

        parent = _parent()
        ARXMLWriter().writeAbstractCanCommunicationController(parent, controller)

        assert len(parent.findall("WAKE-UP-BY-CONTROLLER-SUPPORTED")) == 1


class TestAbstractCanCommunicationControllerRoundTrip:
    def test_round_trip_through_can_communication_controller(self):
        _, controller = _new_instance_with_controller("can_ctrl")
        controller.setWakeUpByControllerSupported(_boolean(True))
        controller.setCanControllerAttributes(_new_configuration())

        parsed_controllers = _write_and_reread(controller.getParent())
        assert len(parsed_controllers) == 1
        parsed = parsed_controllers[0]
        assert parsed.getShortName() == "can_ctrl"
        assert parsed.getWakeUpByControllerSupported() is not None
        assert parsed.getWakeUpByControllerSupported().getValue() is True

        attributes = parsed.getCanControllerAttributes()
        assert isinstance(attributes, CanControllerConfiguration)
        assert attributes.getPropSeg().getValue() == 4
        assert attributes.getSyncJumpWidth().getValue() == 1
        assert attributes.getTimeSeg1().getValue() == 13
        assert attributes.getTimeSeg2().getValue() == 2

    def test_round_trip_empty_controller(self):
        instance, _ = _new_instance_with_controller("empty_ctrl")

        parsed_controllers = _write_and_reread(instance)
        assert len(parsed_controllers) == 1
        parsed = parsed_controllers[0]
        assert parsed.getShortName() == "empty_ctrl"
        assert parsed.getWakeUpByControllerSupported() is None
        assert parsed.getCanControllerAttributes() is None
