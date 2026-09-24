"""
Tests for writing MODE-SWITCHED-ACK elements — ModeSwitchedAckRequest, Table 4.80 (p.190, R23-11).

ModeSwitchedAckRequest (Base = ARObject) carries the optional TIMEOUT attribute
(TIME-VALUE, 0..1). Writer element order must follow the XSD sequenceOffset
(AUTOSAR_00052.xsd group MODE-SWITCHED-ACK-REQUEST: TIMEOUT is the only element).
The wrapper is emitted only when modeSwitchedAck is set; the comspec-level
round-trip goes through ModeSwitchSenderComSpec.

Round-trip counterpart: tests/test_armodel/parser/test_mode_switched_ack_request.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ModeSwitchedAckRequest, ModeSwitchSenderComSpec
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _time_value(val):
    t = TimeValue()
    t.setValue(val)
    return t


class TestWriteModeSwitchedAckRequest:
    """Tests for setModeSwitchedAckRequest — own element field values (Table 4.80)."""

    def test_write_field_values(self, writer):
        """Test that TIMEOUT is emitted with the field value."""
        request = ModeSwitchedAckRequest()
        request.setTimeout(_time_value(0.5))
        parent = ET.Element("PARENT")

        writer.setModeSwitchedAckRequest(parent, "MODE-SWITCHED-ACK", request)

        child = parent.find("MODE-SWITCHED-ACK")
        assert child is not None
        assert child.find("TIMEOUT").text == "0.5"

    def test_write_none_emits_nothing(self, writer):
        """Test that a None modeSwitchedAck emits no MODE-SWITCHED-ACK element."""
        parent = ET.Element("PARENT")

        writer.setModeSwitchedAckRequest(parent, "MODE-SWITCHED-ACK", None)

        assert len(parent) == 0

    def test_write_unset_fields_emits_empty_wrapper(self, writer):
        """Test that a set-but-empty request emits the wrapper without child elements."""
        request = ModeSwitchedAckRequest()
        parent = ET.Element("PARENT")

        writer.setModeSwitchedAckRequest(parent, "MODE-SWITCHED-ACK", request)

        child = parent.find("MODE-SWITCHED-ACK")
        assert child is not None
        assert len(child) == 0


class TestModeSwitchedAckRoundTrip:
    """Round-trip through the ModeSwitchSenderComSpec aggregation (set → save → reload → assert)."""

    def test_round_trip_field_values(self, writer):
        """Test that modeSwitchedAck field values survive a comspec-level write/read cycle."""
        com_spec = ModeSwitchSenderComSpec()
        request = ModeSwitchedAckRequest()
        request.setTimeout(_time_value(2.5))
        com_spec.setModeSwitchedAck(request)

        parent = ET.Element("PARENT")
        writer.writeModeSwitchSenderComSpec(parent, com_spec)
        com_spec_element = parent.find("MODE-SWITCH-SENDER-COM-SPEC")

        xml_text = ET.tostring(com_spec_element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("MODE-SWITCH-SENDER-COM-SPEC", "MODE-SWITCH-SENDER-COM-SPEC xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = ARXMLParser().getModeSwitchSenderComSpec(reloaded_element)
        assert reloaded is not None
        reloaded_ack = reloaded.getModeSwitchedAck()
        assert reloaded_ack is not None
        assert reloaded_ack.getTimeout() is not None
        assert reloaded_ack.getTimeout().getValue() == 2.5

    def test_round_trip_ar_object_attributes(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) survive the write/read cycle."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String

        request = ModeSwitchedAckRequest()
        checksum = String()
        checksum.setValue("abc123")
        request.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T12:00:00+00:00")
        request.setTimestamp(timestamp)

        parent = ET.Element("PARENT")
        writer.setModeSwitchedAckRequest(parent, "MODE-SWITCHED-ACK", request)
        element = parent.find("MODE-SWITCHED-ACK")
        assert element is not None
        assert element.attrib.get("S") is not None
        assert element.attrib.get("T") is not None

        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring("<PARENT xmlns='http://autosar.org/schema/r4.0'>%s</PARENT>" % xml_text)
        reloaded = ARXMLParser().getModeSwitchedAckRequest(reloaded_element, "MODE-SWITCHED-ACK")
        assert reloaded is not None
        assert reloaded.getChecksum() is not None
        assert reloaded.getChecksum().getValue() == "abc123"
        assert reloaded.getTimestamp() is not None

    def test_round_trip_absent_ack(self, writer):
        """Test that an unset modeSwitchedAck emits no MODE-SWITCHED-ACK and reloads as None."""
        com_spec = ModeSwitchSenderComSpec()

        parent = ET.Element("PARENT")
        writer.writeModeSwitchSenderComSpec(parent, com_spec)
        com_spec_element = parent.find("MODE-SWITCH-SENDER-COM-SPEC")
        assert com_spec_element.find("MODE-SWITCHED-ACK") is None

        xml_text = ET.tostring(com_spec_element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("MODE-SWITCH-SENDER-COM-SPEC", "MODE-SWITCH-SENDER-COM-SPEC xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = ARXMLParser().getModeSwitchSenderComSpec(reloaded_element)
        assert reloaded is not None
        assert reloaded.getModeSwitchedAck() is None
