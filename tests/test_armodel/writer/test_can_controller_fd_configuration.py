"""Writer round-trip tests for CanControllerFdConfiguration (Table 3.16, p.66).

XML element order per XSD group CAN-CONTROLLER-FD-CONFIGURATION
(AUTOSAR_00052.xsd line 14649): PADDING-VALUE, PROP-SEG, SSP-OFFSET,
SYNC-JUMP-WIDTH, TIME-SEG-1, TIME-SEG-2, TRCV-DELAY-COMPENSATION-OFFSET
(atp.Status="removed" — not in the R23-11 PDF table, Rule 0015),
TX-BIT-RATE-SWITCH. The class is the XSD complexType
CAN-CONTROLLER-FD-CONFIGURATION (line 14711) with no standalone element of
its own; round-trip coverage runs through the spec aggregator
AbstractCanCommunicationControllerAttributes (CAN-CONTROLLER-FD-ATTRIBUTES
element, AUTOSAR_00052.xsd line 169) (Rule 0001.7). No ref/DEST attributes
exist in this class's element set (seven 0..1 attr leaves only).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, DateTime, PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerConfigurationRequirements,
    CanControllerFdConfiguration,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

LEAF_TAGS = [
    "PADDING-VALUE",
    "PROP-SEG",
    "SSP-OFFSET",
    "SYNC-JUMP-WIDTH",
    "TIME-SEG-1",
    "TIME-SEG-2",
    "TX-BIT-RATE-SWITCH",
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


def _new_fd_configuration():
    configuration = CanControllerFdConfiguration()
    configuration.setChecksum(String().setValue("1234"))
    configuration.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
    configuration.setPaddingValue(_pos_int("8"))
    configuration.setPropSeg(_pos_int("4"))
    configuration.setSspOffset(_pos_int("5"))
    configuration.setSyncJumpWidth(_pos_int("1"))
    configuration.setTimeSeg1(_pos_int("13"))
    configuration.setTimeSeg2(_pos_int("2"))
    configuration.setTxBitRateSwitch(_bool("true"))
    return configuration


def _wrap(inner):
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))


def _write_holder(fd_configuration):
    holder = CanControllerConfigurationRequirements()
    holder.setCanControllerFdAttributes(fd_configuration)
    parent = ET.Element("PARENT")
    ARXMLWriter().writeAbstractCanCommunicationControllerAttributes(parent, holder)
    return parent


class TestWriteCanControllerFdConfiguration:
    def test_write_none_configuration_omits_element(self):
        parent = _write_holder(None)
        assert parent.find("CAN-CONTROLLER-FD-ATTRIBUTES") is None

    def test_write_all_seven_fields_in_xsd_order(self):
        parent = _write_holder(_new_fd_configuration())
        tag = parent.find("CAN-CONTROLLER-FD-ATTRIBUTES")
        assert tag is not None
        assert [child.tag for child in tag] == LEAF_TAGS

    def test_write_field_values(self):
        parent = _write_holder(_new_fd_configuration())
        tag = parent.find("CAN-CONTROLLER-FD-ATTRIBUTES")
        assert tag.find("PADDING-VALUE").text == "8"
        assert tag.find("PROP-SEG").text == "4"
        assert tag.find("SSP-OFFSET").text == "5"
        assert tag.find("SYNC-JUMP-WIDTH").text == "1"
        assert tag.find("TIME-SEG-1").text == "13"
        assert tag.find("TIME-SEG-2").text == "2"
        assert tag.find("TX-BIT-RATE-SWITCH").text == "true"
        assert tag.get("S") == "1234"
        assert tag.get("T") == "2024-01-01T00:00:00Z"

    def test_write_empty_configuration_omits_child_tags(self):
        parent = _write_holder(CanControllerFdConfiguration())
        tag = parent.find("CAN-CONTROLLER-FD-ATTRIBUTES")
        assert tag is not None
        assert len(tag) == 0


class TestCanControllerFdConfigurationRoundTrip:
    def test_round_trip_through_fd_attributes_element(self):
        parent = _write_holder(_new_fd_configuration())
        inner = ET.tostring(parent).decode("utf-8")

        holder = CanControllerConfigurationRequirements()
        ARXMLParser().readAbstractCanCommunicationControllerAttributes(_wrap(inner)[0], holder)

        fd = holder.getCanControllerFdAttributes()
        assert isinstance(fd, CanControllerFdConfiguration)
        assert fd.getPaddingValue().getValue() == 8
        assert fd.getPropSeg().getValue() == 4
        assert fd.getSspOffset().getValue() == 5
        assert fd.getSyncJumpWidth().getValue() == 1
        assert fd.getTimeSeg1().getValue() == 13
        assert fd.getTimeSeg2().getValue() == 2
        assert fd.getTxBitRateSwitch().getValue() is True
        assert isinstance(fd.getPaddingValue(), PositiveInteger)
        assert fd.getChecksum().getValue() == "1234"
        assert fd.getTimestamp().getValue() == "2024-01-01T00:00:00Z"
