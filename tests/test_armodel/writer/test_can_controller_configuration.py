"""Writer round-trip tests for CanControllerConfiguration (Table 3.14, p.64).

XML element order per XSD complexType CAN-CONTROLLER-CONFIGURATION: the
ABSTRACT-CAN-COMMUNICATION-CONTROLLER-ATTRIBUTES group (FD/XL sub-
configurations) precedes the CAN-CONTROLLER-CONFIGURATION leaves
(PROP-SEG, SYNC-JUMP-WIDTH, TIME-SEG-1, TIME-SEG-2).
Coverage runs through both spec aggregators: CanXlProps.canConfig (CAN-CONFIG)
and AbstractCanCommunicationController.canControllerAttributes
(CAN-CONTROLLER-ATTRIBUTES > CAN-CONTROLLER-CONFIGURATION dispatch).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationController, CanControllerConfiguration, CanXlProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

CONFIG_TAGS = ["PROP-SEG", "SYNC-JUMP-WIDTH", "TIME-SEG-1", "TIME-SEG-2"]


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


def _new_config(prop_seg="8", sync_jump_width="1", time_seg1="13", time_seg2="2"):
    config = CanControllerConfiguration()
    config.setPropSeg(_int(prop_seg))
    config.setSyncJumpWidth(_int(sync_jump_width))
    config.setTimeSeg1(_int(time_seg1))
    config.setTimeSeg2(_int(time_seg2))
    return config


def _wrap(inner):
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))


class TestWriteCanControllerConfiguration:
    def test_write_none_config_omits_element(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setCanControllerConfiguration(parent, "CAN-CONFIG", None)
        assert len(parent) == 0

    def test_write_all_four_fields_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setCanControllerConfiguration(parent, "CAN-CONFIG", _new_config())
        tag = parent.find("CAN-CONFIG")
        assert tag is not None
        assert [child.tag for child in tag] == CONFIG_TAGS

    def test_write_field_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setCanControllerConfiguration(parent, "CAN-CONFIG", _new_config())
        tag = parent.find("CAN-CONFIG")
        assert tag.find("PROP-SEG").text == "8"
        assert tag.find("SYNC-JUMP-WIDTH").text == "1"
        assert tag.find("TIME-SEG-1").text == "13"
        assert tag.find("TIME-SEG-2").text == "2"

    def test_write_empty_config_omits_child_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setCanControllerConfiguration(parent, "CAN-CONFIG", CanControllerConfiguration())
        tag = parent.find("CAN-CONFIG")
        assert tag is not None
        assert len(tag) == 0

    def test_write_config_through_controller_attributes_dispatch(self):
        controller = CanCommunicationController(parent=_autosar_root(), short_name="ctrl")
        controller.setCanControllerAttributes(_new_config("4", "2", "6", "3"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeAbstractCanCommunicationControllerCanControllerAttributes(parent, controller)
        wrapper = parent.find("CAN-CONTROLLER-ATTRIBUTES")
        assert wrapper is not None
        tag = wrapper.find("CAN-CONTROLLER-CONFIGURATION")
        assert tag is not None
        assert [child.tag for child in tag] == CONFIG_TAGS
        assert tag.find("PROP-SEG").text == "4"
        assert tag.find("SYNC-JUMP-WIDTH").text == "2"
        assert tag.find("TIME-SEG-1").text == "6"
        assert tag.find("TIME-SEG-2").text == "3"

    def test_write_none_controller_attributes_omits_wrapper(self):
        controller = CanCommunicationController(parent=_autosar_root(), short_name="ctrl")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeAbstractCanCommunicationControllerCanControllerAttributes(parent, controller)
        assert len(parent) == 0


class TestCanControllerConfigurationRoundTrip:
    def test_round_trip_through_can_xl_props(self):
        props = CanXlProps(_autosar_root(), "Props")
        props.setCanConfig(_new_config())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanXlProps(parent, props)
        inner = ET.tostring(parent).decode("utf-8")

        parsed_props = CanXlProps(_autosar_root(), "Parsed")
        ARXMLParser().readCanXlProps(_wrap(inner)[0][0], parsed_props)

        config = parsed_props.getCanConfig()
        assert isinstance(config, CanControllerConfiguration)
        assert config.getPropSeg().getValue() == 8
        assert config.getSyncJumpWidth().getValue() == 1
        assert config.getTimeSeg1().getValue() == 13
        assert config.getTimeSeg2().getValue() == 2
        assert isinstance(config.getPropSeg(), Integer)

    def test_round_trip_through_controller_attributes_dispatch(self):
        controller = CanCommunicationController(parent=_autosar_root(), short_name="ctrl")
        controller.setCanControllerAttributes(_new_config("4", "2", "6", "3"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeAbstractCanCommunicationControllerCanControllerAttributes(parent, controller)
        inner = ET.tostring(parent).decode("utf-8")

        parsed_controller = CanCommunicationController(parent=_autosar_root(), short_name="ctrl")
        ARXMLParser().readAbstractCanCommunicationControllerCanControllerAttributes(_wrap(inner)[0], parsed_controller)

        config = parsed_controller.getCanControllerAttributes()
        assert isinstance(config, CanControllerConfiguration)
        assert config.getPropSeg().getValue() == 4
        assert config.getSyncJumpWidth().getValue() == 2
        assert config.getTimeSeg1().getValue() == 6
        assert config.getTimeSeg2().getValue() == 3
