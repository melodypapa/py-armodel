"""Writer round-trip tests for CanControllerConfigurationRequirements (Table 3.15, p.65).

XML element order per XSD complexType CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS:
the ABSTRACT-CAN-COMMUNICATION-CONTROLLER-ATTRIBUTES group (FD/XL sub-
configurations) precedes the CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS leaves
(MAX-NUMBER-OF-TIME-QUANTA-PER-BIT, MAX-SAMPLE-POINT, MAX-SYNC-JUMP-WIDTH,
MIN-NUMBER-OF-TIME-QUANTA-PER-BIT, MIN-SAMPLE-POINT, MIN-SYNC-JUMP-WIDTH).
Coverage runs through the spec aggregator AbstractCanCommunicationController.
canControllerAttributes (CAN-CONTROLLER-ATTRIBUTES >
CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS dispatch). No ref/DEST attributes
exist in this class's element set (six 0..1 attr leaves only).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Float, Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanCommunicationController,
    CanControllerConfigurationRequirements,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

LEAF_TAGS = [
    "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT",
    "MAX-SAMPLE-POINT",
    "MAX-SYNC-JUMP-WIDTH",
    "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT",
    "MIN-SAMPLE-POINT",
    "MIN-SYNC-JUMP-WIDTH",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _autosar_root():
    return AUTOSAR.getInstance()


def _int(text):
    value = Integer()
    value.setValue(text)
    return value


def _float(text):
    value = Float()
    value.setValue(text)
    return value


def _new_requirements(max_quanta="32", max_sample="0.8", max_sjw="0.2", min_quanta="16", min_sample="0.7", min_sjw="0.1"):
    req = CanControllerConfigurationRequirements()
    req.setMaxNumberOfTimeQuantaPerBit(_int(max_quanta))
    req.setMaxSamplePoint(_float(max_sample))
    req.setMaxSyncJumpWidth(_float(max_sjw))
    req.setMinNumberOfTimeQuantaPerBit(_int(min_quanta))
    req.setMinSamplePoint(_float(min_sample))
    req.setMinSyncJumpWidth(_float(min_sjw))
    return req


def _wrap(inner):
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))


class TestWriteCanControllerConfigurationRequirements:
    def test_write_none_requirements_omits_element(self):
        controller = CanCommunicationController(parent=_autosar_root(), short_name="ctrl")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeAbstractCanCommunicationControllerCanControllerAttributes(parent, controller)
        assert len(parent) == 0

    def test_write_all_six_fields_in_xsd_order(self):
        controller = CanCommunicationController(parent=_autosar_root(), short_name="ctrl")
        controller.setCanControllerAttributes(_new_requirements())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeAbstractCanCommunicationControllerCanControllerAttributes(parent, controller)
        wrapper = parent.find("CAN-CONTROLLER-ATTRIBUTES")
        assert wrapper is not None
        tag = wrapper.find("CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS")
        assert tag is not None
        assert [child.tag for child in tag] == LEAF_TAGS

    def test_write_field_values(self):
        controller = CanCommunicationController(parent=_autosar_root(), short_name="ctrl")
        controller.setCanControllerAttributes(_new_requirements())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeAbstractCanCommunicationControllerCanControllerAttributes(parent, controller)
        tag = parent.find("CAN-CONTROLLER-ATTRIBUTES").find("CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS")
        assert tag.find("MAX-NUMBER-OF-TIME-QUANTA-PER-BIT").text == "32"
        assert tag.find("MAX-SAMPLE-POINT").text == "0.8"
        assert tag.find("MAX-SYNC-JUMP-WIDTH").text == "0.2"
        assert tag.find("MIN-NUMBER-OF-TIME-QUANTA-PER-BIT").text == "16"
        assert tag.find("MIN-SAMPLE-POINT").text == "0.7"
        assert tag.find("MIN-SYNC-JUMP-WIDTH").text == "0.1"

    def test_write_empty_requirements_omits_child_tags(self):
        controller = CanCommunicationController(parent=_autosar_root(), short_name="ctrl")
        controller.setCanControllerAttributes(CanControllerConfigurationRequirements())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeAbstractCanCommunicationControllerCanControllerAttributes(parent, controller)
        tag = parent.find("CAN-CONTROLLER-ATTRIBUTES").find("CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS")
        assert tag is not None
        assert len(tag) == 0


class TestCanControllerConfigurationRequirementsRoundTrip:
    def test_round_trip_through_controller_attributes_dispatch(self):
        controller = CanCommunicationController(parent=_autosar_root(), short_name="ctrl")
        controller.setCanControllerAttributes(_new_requirements())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeAbstractCanCommunicationControllerCanControllerAttributes(parent, controller)
        inner = ET.tostring(parent).decode("utf-8")

        parsed_controller = CanCommunicationController(parent=_autosar_root(), short_name="ctrl")
        ARXMLParser().readAbstractCanCommunicationControllerCanControllerAttributes(_wrap(inner)[0], parsed_controller)

        req = parsed_controller.getCanControllerAttributes()
        assert isinstance(req, CanControllerConfigurationRequirements)
        assert req.getMaxNumberOfTimeQuantaPerBit().getValue() == 32
        assert req.getMaxSamplePoint().getValue() == 0.8
        assert req.getMaxSyncJumpWidth().getValue() == 0.2
        assert req.getMinNumberOfTimeQuantaPerBit().getValue() == 16
        assert req.getMinSamplePoint().getValue() == 0.7
        assert req.getMinSyncJumpWidth().getValue() == 0.1
        assert isinstance(req.getMaxNumberOfTimeQuantaPerBit(), Integer)
        assert isinstance(req.getMaxSamplePoint(), Float)
