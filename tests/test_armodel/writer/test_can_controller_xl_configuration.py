"""Writer round-trip tests for CanControllerXlConfiguration (Table 3.18, p.71).

XML element order per XSD group CAN-CONTROLLER-XL-CONFIGURATION
(AUTOSAR_00052.xsd line 14811): ERROR-SIGNALING-ENABLED, PROP-SEG, PWM-L,
PWM-O, PWM-S, SSP-OFFSET, SYNC-JUMP-WIDTH, TIME-SEG-1, TIME-SEG-2,
TRCV-PWM-MODE-ENABLED. The class is the XSD complexType
CAN-CONTROLLER-XL-CONFIGURATION (line 14889) with no standalone element of
its own; round-trip coverage runs through the spec aggregator
AbstractCanCommunicationControllerAttributes (CAN-CONTROLLER-XL-ATTRIBUTES
element, AUTOSAR_00052.xsd line 181) (Rule 0001.7). No ref/DEST attributes
exist in this class's element set (ten 0..1 attr leaves only).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, DateTime, PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerConfigurationRequirements,
    CanControllerXlConfiguration,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

LEAF_TAGS = [
    "ERROR-SIGNALING-ENABLED",
    "PROP-SEG",
    "PWM-L",
    "PWM-O",
    "PWM-S",
    "SSP-OFFSET",
    "SYNC-JUMP-WIDTH",
    "TIME-SEG-1",
    "TIME-SEG-2",
    "TRCV-PWM-MODE-ENABLED",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _pos_int(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _new_xl_configuration():
    configuration = CanControllerXlConfiguration()
    configuration.setChecksum(String().setValue("1234"))
    configuration.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
    configuration.setErrorSignalingEnabled(_bool("true"))
    configuration.setPropSeg(_pos_int("4"))
    configuration.setPwmL(_pos_int("100"))
    configuration.setPwmO(_pos_int("20"))
    configuration.setPwmS(_pos_int("30"))
    configuration.setSspOffset(_pos_int("5"))
    configuration.setSyncJumpWidth(_pos_int("1"))
    configuration.setTimeSeg1(_pos_int("61"))
    configuration.setTimeSeg2(_pos_int("14"))
    configuration.setTrcvPwmModeEnabled(_bool("false"))
    return configuration


def _wrap(inner):
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))


def _write_holder(xl_configuration):
    holder = CanControllerConfigurationRequirements()
    holder.setCanControllerXlAttributes(xl_configuration)
    parent = ET.Element("PARENT")
    ARXMLWriter().writeAbstractCanCommunicationControllerAttributes(parent, holder)
    return parent


class TestWriteCanControllerXlConfiguration:
    def test_write_none_configuration_omits_element(self):
        parent = _write_holder(None)
        assert parent.find("CAN-CONTROLLER-XL-ATTRIBUTES") is None

    def test_write_all_ten_fields_in_xsd_order(self):
        parent = _write_holder(_new_xl_configuration())
        tag = parent.find("CAN-CONTROLLER-XL-ATTRIBUTES")
        assert tag is not None
        assert [child.tag for child in tag] == LEAF_TAGS

    def test_write_field_values(self):
        parent = _write_holder(_new_xl_configuration())
        tag = parent.find("CAN-CONTROLLER-XL-ATTRIBUTES")
        assert tag.find("ERROR-SIGNALING-ENABLED").text == "true"
        assert tag.find("PROP-SEG").text == "4"
        assert tag.find("PWM-L").text == "100"
        assert tag.find("PWM-O").text == "20"
        assert tag.find("PWM-S").text == "30"
        assert tag.find("SSP-OFFSET").text == "5"
        assert tag.find("SYNC-JUMP-WIDTH").text == "1"
        assert tag.find("TIME-SEG-1").text == "61"
        assert tag.find("TIME-SEG-2").text == "14"
        assert tag.find("TRCV-PWM-MODE-ENABLED").text == "false"
        assert tag.get("S") == "1234"
        assert tag.get("T") == "2024-01-01T00:00:00Z"

    def test_write_empty_configuration_omits_child_tags(self):
        parent = _write_holder(CanControllerXlConfiguration())
        tag = parent.find("CAN-CONTROLLER-XL-ATTRIBUTES")
        assert tag is not None
        assert len(tag) == 0


class TestCanControllerXlConfigurationRoundTrip:
    def test_round_trip_through_xl_attributes_element(self):
        parent = _write_holder(_new_xl_configuration())
        inner = ET.tostring(parent).decode("utf-8")

        holder = CanControllerConfigurationRequirements()
        ARXMLParser().readAbstractCanCommunicationControllerAttributes(_wrap(inner)[0], holder)

        xl = holder.getCanControllerXlAttributes()
        assert isinstance(xl, CanControllerXlConfiguration)
        assert xl.getErrorSignalingEnabled().getValue() is True
        assert xl.getPropSeg().getValue() == 4
        assert xl.getPwmL().getValue() == 100
        assert xl.getPwmO().getValue() == 20
        assert xl.getPwmS().getValue() == 30
        assert xl.getSspOffset().getValue() == 5
        assert xl.getSyncJumpWidth().getValue() == 1
        assert xl.getTimeSeg1().getValue() == 61
        assert xl.getTimeSeg2().getValue() == 14
        assert xl.getTrcvPwmModeEnabled().getValue() is False
        assert isinstance(xl.getPropSeg(), PositiveInteger)
        assert xl.getChecksum().getValue() == "1234"
        assert xl.getTimestamp().getValue() == "2024-01-01T00:00:00Z"
