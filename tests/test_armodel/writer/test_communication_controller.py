"""Writer round-trip tests for the abstract CommunicationController base (SystemTemplate Table 3.3, p.53).

XML element order per XSD groups COMMUNICATION-CONTROLLER and
COMMUNICATION-CONTROLLER-CONTENT (AUTOSAR_00052.xsd l.20388/l.20421): the base
group contributes VARIATION-POINT (emitted by writeIdentifiable), the content
group contributes WAKE-UP-BY-CONTROLLER-SUPPORTED. Coverage runs through the
COMM-CONTROLLERS dispatch on LinMaster, a concrete CommunicationController.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
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


def _boolean(value):
    value_obj = Boolean()
    value_obj.setValue(value)
    return value_obj


def _new_instance_with_controller(with_wake_up=True, with_variation_point=False):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    instance = EcuInstance(pkg, "Ecu")
    controller = instance.createLinMaster("ctrl")
    if with_wake_up:
        controller.setWakeUpByControllerSupported(_boolean(True))
    if with_variation_point:
        variation_point = VariationPoint()
        variation_point.setShortLabel(Identifier().setValue("vp1"))
        controller.setVariationPoint(variation_point)
    return instance


def _write_instance(instance):
    parent = ET.Element("ECU-INSTANCE")
    ARXMLWriter().writeEcuInstanceCommControllers(parent, instance)
    return parent


class TestWriteCommunicationController:
    def test_write_wake_up_value(self):
        parent = _write_instance(_new_instance_with_controller())
        controller_tag = parent.find("COMM-CONTROLLERS/LIN-MASTER")
        assert controller_tag is not None
        assert controller_tag.find("LIN-MASTER-VARIANTS/LIN-MASTER-CONDITIONAL/WAKE-UP-BY-CONTROLLER-SUPPORTED").text == "true"

    def test_write_variation_point_before_content(self):
        parent = _write_instance(_new_instance_with_controller(with_variation_point=True))
        controller_tag = parent.find("COMM-CONTROLLERS/LIN-MASTER")
        children = [child.tag for child in controller_tag]
        assert children.index("VARIATION-POINT") < children.index("LIN-MASTER-VARIANTS")
        assert controller_tag.find("VARIATION-POINT/SHORT-LABEL").text == "vp1"

    def test_write_empty_controller_omits_base_elements(self):
        parent = _write_instance(_new_instance_with_controller(with_wake_up=False))
        controller_tag = parent.find("COMM-CONTROLLERS/LIN-MASTER")
        assert controller_tag.find("VARIATION-POINT") is None
        assert controller_tag.find(".//WAKE-UP-BY-CONTROLLER-SUPPORTED") is None

    def test_round_trip_preserves_wake_up_value(self):
        instance = _new_instance_with_controller()
        parent = _write_instance(instance)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))

        parsed_instance = EcuInstance(AUTOSAR.getInstance().createARPackage("Parsed"), "Ecu")
        ARXMLParser().readEcuInstanceCommControllers(root[0], parsed_instance)

        controller = parsed_instance.getCommControllers()[0]
        assert controller.getWakeUpByControllerSupported() is not None
        assert controller.getWakeUpByControllerSupported().getValue() is True

    def test_round_trip_preserves_variation_point(self):
        instance = _new_instance_with_controller(with_variation_point=True)
        parent = _write_instance(instance)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))

        parsed_instance = EcuInstance(AUTOSAR.getInstance().createARPackage("Parsed"), "Ecu")
        ARXMLParser().readEcuInstanceCommControllers(root[0], parsed_instance)

        controller = parsed_instance.getCommControllers()[0]
        assert controller.getVariationPoint() is not None
        assert controller.getVariationPoint().getShortLabel().getValue() == "vp1"
        assert controller.getWakeUpByControllerSupported().getValue() is True

    def test_round_trip_empty_controller(self):
        instance = _new_instance_with_controller(with_wake_up=False)
        parent = _write_instance(instance)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))

        parsed_instance = EcuInstance(AUTOSAR.getInstance().createARPackage("Parsed"), "Ecu")
        ARXMLParser().readEcuInstanceCommControllers(root[0], parsed_instance)

        controller = parsed_instance.getCommControllers()[0]
        assert controller.getShortName() == "ctrl"
        assert controller.getWakeUpByControllerSupported() is None
        assert controller.getVariationPoint() is None
