"""Writer round-trip tests for CanControllerFdConfigurationRequirements (Table 3.17, pp.66-67).

XML element order per XSD group CAN-CONTROLLER-FD-CONFIGURATION-REQUIREMENTS
(AUTOSAR_00052.xsd line 14724): MAX-NUMBER-OF-TIME-QUANTA-PER-BIT,
MAX-SAMPLE-POINT, MAX-SYNC-JUMP-WIDTH, MAX-TRCV-DELAY-COMPENSATION-OFFSET,
MIN-NUMBER-OF-TIME-QUANTA-PER-BIT, MIN-SAMPLE-POINT, MIN-SYNC-JUMP-WIDTH,
MIN-TRCV-DELAY-COMPENSATION-OFFSET, PADDING-VALUE, TX-BIT-RATE-SWITCH.
Coverage runs through the spec aggregator AbstractCanCommunicationControllerAttributes
(CAN-CONTROLLER-FD-REQUIREMENTS element, AUTOSAR_00052.xsd line 175). No
ref/DEST attributes exist in this class's element set (ten 0..1 attr leaves
only).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float, Integer, PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerConfigurationRequirements,
    CanControllerFdConfigurationRequirements,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

LEAF_TAGS = [
    "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT",
    "MAX-SAMPLE-POINT",
    "MAX-SYNC-JUMP-WIDTH",
    "MAX-TRCV-DELAY-COMPENSATION-OFFSET",
    "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT",
    "MIN-SAMPLE-POINT",
    "MIN-SYNC-JUMP-WIDTH",
    "MIN-TRCV-DELAY-COMPENSATION-OFFSET",
    "PADDING-VALUE",
    "TX-BIT-RATE-SWITCH",
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


def _float(text):
    value = Float()
    value.setValue(text)
    return value


def _time(text):
    value = TimeValue()
    value.setValue(text)
    return value


def _new_fd_requirements():
    req = CanControllerFdConfigurationRequirements()
    req.setMaxNumberOfTimeQuantaPerBit(_int("32"))
    req.setMaxSamplePoint(_float("0.8"))
    req.setMaxSyncJumpWidth(_float("0.2"))
    req.setMaxTrcvDelayCompensationOffset(_time("0.001"))
    req.setMinNumberOfTimeQuantaPerBit(_int("16"))
    req.setMinSamplePoint(_float("0.7"))
    req.setMinSyncJumpWidth(_float("0.1"))
    req.setMinTrcvDelayCompensationOffset(_time("0.0005"))
    padding = PositiveInteger()
    padding.setValue("8")
    req.setPaddingValue(padding)
    req.setTxBitRateSwitch(Boolean().setValue("true"))
    return req


def _wrap(inner):
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))


def _write_holder(fd_requirements):
    holder = CanControllerConfigurationRequirements()
    holder.setCanControllerFdRequirements(fd_requirements)
    parent = ET.Element("PARENT")
    ARXMLWriter().writeAbstractCanCommunicationControllerAttributes(parent, holder)
    return parent


class TestWriteCanControllerFdConfigurationRequirements:
    def test_write_none_requirements_omits_element(self):
        parent = _write_holder(None)
        assert parent.find("CAN-CONTROLLER-FD-REQUIREMENTS") is None

    def test_write_all_ten_fields_in_xsd_order(self):
        parent = _write_holder(_new_fd_requirements())
        tag = parent.find("CAN-CONTROLLER-FD-REQUIREMENTS")
        assert tag is not None
        assert [child.tag for child in tag] == LEAF_TAGS

    def test_write_field_values(self):
        parent = _write_holder(_new_fd_requirements())
        tag = parent.find("CAN-CONTROLLER-FD-REQUIREMENTS")
        assert tag.find("MAX-NUMBER-OF-TIME-QUANTA-PER-BIT").text == "32"
        assert tag.find("MAX-SAMPLE-POINT").text == "0.8"
        assert tag.find("MAX-SYNC-JUMP-WIDTH").text == "0.2"
        assert tag.find("MAX-TRCV-DELAY-COMPENSATION-OFFSET").text == "0.001"
        assert tag.find("MIN-NUMBER-OF-TIME-QUANTA-PER-BIT").text == "16"
        assert tag.find("MIN-SAMPLE-POINT").text == "0.7"
        assert tag.find("MIN-SYNC-JUMP-WIDTH").text == "0.1"
        assert tag.find("MIN-TRCV-DELAY-COMPENSATION-OFFSET").text == "0.0005"
        assert tag.find("PADDING-VALUE").text == "8"
        assert tag.find("TX-BIT-RATE-SWITCH").text == "true"

    def test_write_empty_requirements_omits_child_tags(self):
        parent = _write_holder(CanControllerFdConfigurationRequirements())
        tag = parent.find("CAN-CONTROLLER-FD-REQUIREMENTS")
        assert tag is not None
        assert len(tag) == 0


class TestCanControllerFdConfigurationRequirementsRoundTrip:
    def test_round_trip_through_fd_requirements_element(self):
        parent = _write_holder(_new_fd_requirements())
        inner = ET.tostring(parent).decode("utf-8")

        holder = CanControllerConfigurationRequirements()
        ARXMLParser().readAbstractCanCommunicationControllerAttributes(_wrap(inner)[0], holder)

        req = holder.getCanControllerFdRequirements()
        assert isinstance(req, CanControllerFdConfigurationRequirements)
        assert req.getMaxNumberOfTimeQuantaPerBit().getValue() == 32
        assert req.getMaxSamplePoint().getValue() == 0.8
        assert req.getMaxSyncJumpWidth().getValue() == 0.2
        assert req.getMaxTrcvDelayCompensationOffset().getValue() == 0.001
        assert req.getMinNumberOfTimeQuantaPerBit().getValue() == 16
        assert req.getMinSamplePoint().getValue() == 0.7
        assert req.getMinSyncJumpWidth().getValue() == 0.1
        assert req.getMinTrcvDelayCompensationOffset().getValue() == 0.0005
        assert req.getPaddingValue().getValue() == 8
        assert req.getTxBitRateSwitch().getValue() is True
        assert isinstance(req.getMaxNumberOfTimeQuantaPerBit(), Integer)
        assert isinstance(req.getMaxSamplePoint(), Float)
        assert isinstance(req.getPaddingValue(), PositiveInteger)
