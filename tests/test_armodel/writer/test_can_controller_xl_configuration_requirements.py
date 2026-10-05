"""Writer round-trip tests for CanControllerXlConfigurationRequirements (Table 3.19, p.72).

XML element order per XSD group CAN-CONTROLLER-XL-CONFIGURATION-REQUIREMENTS
(AUTOSAR_00052.xsd line 14902): ERROR-SIGNALING-ENABLED,
MAX-NUMBER-OF-TIME-QUANTA-PER-BIT, MAX-PWM-L, MAX-PWM-O, MAX-PWM-S,
MAX-SAMPLE-POINT, MAX-SYNC-JUMP-WIDTH, MAX-TRCV-DELAY-COMPENSATION-OFFSET,
MIN-NUMBER-OF-TIME-QUANTA-PER-BIT, MIN-PWM-L, MIN-PWM-O, MIN-PWM-S,
MIN-SAMPLE-POINT, MIN-SYNC-JUMP-WIDTH, MIN-TRCV-DELAY-COMPENSATION-OFFSET,
TRCV-PWM-MODE-ENABLED. The class is the XSD complexType
CAN-CONTROLLER-XL-CONFIGURATION-REQUIREMENTS (line 15016) with no standalone
element of its own; round-trip coverage runs through the spec aggregator
AbstractCanCommunicationControllerAttributes (CAN-CONTROLLER-XL-REQUIREMENTS
element, AUTOSAR_00052.xsd line 187) (Rule 0001.7). No ref/DEST attributes
exist in this class's element set (sixteen 0..1 attr leaves only).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, DateTime, Float, Integer, PositiveInteger, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerConfigurationRequirements,
    CanControllerXlConfigurationRequirements,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

LEAF_TAGS = [
    "ERROR-SIGNALING-ENABLED",
    "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT",
    "MAX-PWM-L",
    "MAX-PWM-O",
    "MAX-PWM-S",
    "MAX-SAMPLE-POINT",
    "MAX-SYNC-JUMP-WIDTH",
    "MAX-TRCV-DELAY-COMPENSATION-OFFSET",
    "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT",
    "MIN-PWM-L",
    "MIN-PWM-O",
    "MIN-PWM-S",
    "MIN-SAMPLE-POINT",
    "MIN-SYNC-JUMP-WIDTH",
    "MIN-TRCV-DELAY-COMPENSATION-OFFSET",
    "TRCV-PWM-MODE-ENABLED",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _int(text):
    value = Integer()
    value.setValue(text)
    return value


def _pos_int(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


def _float(text):
    value = Float()
    value.setValue(text)
    return value


def _time(text):
    value = TimeValue()
    value.setValue(text)
    return value


def _new_xl_requirements():
    req = CanControllerXlConfigurationRequirements()
    req.setChecksum(String().setValue("1234"))
    req.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
    req.setErrorSignalingEnabled(Boolean().setValue("true"))
    req.setMaxNumberOfTimeQuantaPerBit(_int("32"))
    req.setMaxPwmL(_pos_int("100"))
    req.setMaxPwmO(_pos_int("20"))
    req.setMaxPwmS(_pos_int("30"))
    req.setMaxSamplePoint(_float("0.8"))
    req.setMaxSyncJumpWidth(_float("0.2"))
    req.setMaxTrcvDelayCompensationOffset(_time("0.001"))
    req.setMinNumberOfTimeQuantaPerBit(_int("16"))
    req.setMinPwmL(_pos_int("3"))
    req.setMinPwmO(_pos_int("4"))
    req.setMinPwmS(_pos_int("5"))
    req.setMinSamplePoint(_float("0.7"))
    req.setMinSyncJumpWidth(_float("0.1"))
    req.setMinTrcvDelayCompensationOffset(_time("0.0005"))
    req.setTrcvPwmModeEnabled(Boolean().setValue("false"))
    return req


def _wrap(inner):
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))


def _write_holder(xl_requirements):
    holder = CanControllerConfigurationRequirements()
    holder.setCanControllerXlRequirements(xl_requirements)
    parent = ET.Element("PARENT")
    ARXMLWriter().writeAbstractCanCommunicationControllerAttributes(parent, holder)
    return parent


class TestWriteCanControllerXlConfigurationRequirements:
    def test_write_none_requirements_omits_element(self):
        parent = _write_holder(None)
        assert parent.find("CAN-CONTROLLER-XL-REQUIREMENTS") is None

    def test_write_all_sixteen_fields_in_xsd_order(self):
        parent = _write_holder(_new_xl_requirements())
        tag = parent.find("CAN-CONTROLLER-XL-REQUIREMENTS")
        assert tag is not None
        assert [child.tag for child in tag] == LEAF_TAGS

    def test_write_field_values(self):
        parent = _write_holder(_new_xl_requirements())
        tag = parent.find("CAN-CONTROLLER-XL-REQUIREMENTS")
        assert tag.find("ERROR-SIGNALING-ENABLED").text == "true"
        assert tag.find("MAX-NUMBER-OF-TIME-QUANTA-PER-BIT").text == "32"
        assert tag.find("MAX-PWM-L").text == "100"
        assert tag.find("MAX-PWM-O").text == "20"
        assert tag.find("MAX-PWM-S").text == "30"
        assert tag.find("MAX-SAMPLE-POINT").text == "0.8"
        assert tag.find("MAX-SYNC-JUMP-WIDTH").text == "0.2"
        assert tag.find("MAX-TRCV-DELAY-COMPENSATION-OFFSET").text == "0.001"
        assert tag.find("MIN-NUMBER-OF-TIME-QUANTA-PER-BIT").text == "16"
        assert tag.find("MIN-PWM-L").text == "3"
        assert tag.find("MIN-PWM-O").text == "4"
        assert tag.find("MIN-PWM-S").text == "5"
        assert tag.find("MIN-SAMPLE-POINT").text == "0.7"
        assert tag.find("MIN-SYNC-JUMP-WIDTH").text == "0.1"
        assert tag.find("MIN-TRCV-DELAY-COMPENSATION-OFFSET").text == "0.0005"
        assert tag.find("TRCV-PWM-MODE-ENABLED").text == "false"
        assert tag.get("S") == "1234"
        assert tag.get("T") == "2024-01-01T00:00:00Z"

    def test_write_empty_requirements_omits_child_tags(self):
        parent = _write_holder(CanControllerXlConfigurationRequirements())
        tag = parent.find("CAN-CONTROLLER-XL-REQUIREMENTS")
        assert tag is not None
        assert len(tag) == 0


class TestCanControllerXlConfigurationRequirementsRoundTrip:
    def test_round_trip_through_xl_requirements_element(self):
        parent = _write_holder(_new_xl_requirements())
        inner = ET.tostring(parent).decode("utf-8")

        holder = CanControllerConfigurationRequirements()
        ARXMLParser().readAbstractCanCommunicationControllerAttributes(_wrap(inner)[0], holder)

        req = holder.getCanControllerXlRequirements()
        assert isinstance(req, CanControllerXlConfigurationRequirements)
        assert req.getErrorSignalingEnabled().getValue() is True
        assert req.getMaxNumberOfTimeQuantaPerBit().getValue() == 32
        assert req.getMaxPwmL().getValue() == 100
        assert req.getMaxPwmO().getValue() == 20
        assert req.getMaxPwmS().getValue() == 30
        assert req.getMaxSamplePoint().getValue() == 0.8
        assert req.getMaxSyncJumpWidth().getValue() == 0.2
        assert req.getMaxTrcvDelayCompensationOffset().getValue() == 0.001
        assert req.getMinNumberOfTimeQuantaPerBit().getValue() == 16
        assert req.getMinPwmL().getValue() == 3
        assert req.getMinPwmO().getValue() == 4
        assert req.getMinPwmS().getValue() == 5
        assert req.getMinSamplePoint().getValue() == 0.7
        assert req.getMinSyncJumpWidth().getValue() == 0.1
        assert req.getMinTrcvDelayCompensationOffset().getValue() == 0.0005
        assert req.getTrcvPwmModeEnabled().getValue() is False
        assert isinstance(req.getMaxPwmL(), PositiveInteger)
        assert isinstance(req.getMinPwmS(), PositiveInteger)
        assert req.getChecksum().getValue() == "1234"
        assert req.getTimestamp().getValue() == "2024-01-01T00:00:00Z"
