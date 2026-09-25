"""
Tests for writing MODE-SWITCH-SENDER-COM-SPEC elements — ModeSwitchSenderComSpec, Table 4.79 (p.190, R23-11).

ModeSwitchSenderComSpec (Base = PPortComSpec) carries the optional attributes
enhancedModeApi (BOOLEAN 0..1), modeGroup (MODE-GROUP-REF 0..1),
modeSwitchedAck (MODE-SWITCHED-ACK 0..1 aggregation) and queueLength
(QUEUE-LENGTH 0..1 PositiveInteger). Writer element order must follow the XSD
sequenceOffset (AUTOSAR_00052.xsd group MODE-SWITCH-SENDER-COM-SPEC:
ENHANCED-MODE-API → MODE-GROUP-REF → MODE-SWITCHED-ACK → QUEUE-LENGTH).
The comspec-level round-trip goes through the PPortPrototype PROVIDED-COM-SPECS
aggregation (writePPortComSpec dispatch → readProvidedComSpec dispatch).

Round-trip counterpart: tests/test_armodel/parser/test_mode_switch_sender_com_spec.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR, ApplicationSwComponentType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType, TimeValue
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


def _boolean(val):
    b = Boolean()
    b.setValue(val)
    return b


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _ack_request():
    request = ModeSwitchedAckRequest()
    timeout = TimeValue()
    timeout.setValue(0.5)
    request.setTimeout(timeout)
    return request


def _queue_length(val):
    ql = PositiveInteger()
    ql.setValue(val)
    return ql


class TestWriteModeSwitchSenderComSpec:
    """Tests for writeModeSwitchSenderComSpec — own element field values (Table 4.79)."""

    def test_write_field_values(self, writer):
        """Test that all four elements are emitted with their field values."""
        com_spec = ModeSwitchSenderComSpec()
        com_spec.setEnhancedModeApi(_boolean(True))
        com_spec.setModeGroupRef(_ref("/mdg/Group", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        com_spec.setModeSwitchedAck(_ack_request())
        com_spec.setQueueLength(_queue_length(4))
        parent = ET.Element("PARENT")

        writer.writeModeSwitchSenderComSpec(parent, com_spec)

        child = parent.find("MODE-SWITCH-SENDER-COM-SPEC")
        assert child is not None
        assert child.find("ENHANCED-MODE-API").text == "true"
        assert child.find("MODE-GROUP-REF").text == "/mdg/Group"
        assert child.find("MODE-GROUP-REF").attrib.get("DEST") == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert child.find("MODE-SWITCHED-ACK") is not None
        assert child.find("MODE-SWITCHED-ACK").find("TIMEOUT").text == "0.5"
        assert child.find("QUEUE-LENGTH").text == "4"

    def test_write_xsd_element_order(self, writer):
        """Test that the emitted element order follows the XSD group sequence."""
        com_spec = ModeSwitchSenderComSpec()
        com_spec.setEnhancedModeApi(_boolean(True))
        com_spec.setModeGroupRef(_ref("/mdg/Group", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        com_spec.setModeSwitchedAck(_ack_request())
        com_spec.setQueueLength(_queue_length(4))
        parent = ET.Element("PARENT")

        writer.writeModeSwitchSenderComSpec(parent, com_spec)

        child = parent.find("MODE-SWITCH-SENDER-COM-SPEC")
        assert [elem.tag for elem in child] == ["ENHANCED-MODE-API", "MODE-GROUP-REF", "MODE-SWITCHED-ACK", "QUEUE-LENGTH"]

    def test_write_unset_fields_emits_empty_wrapper(self, writer):
        """Test that a set-but-empty com spec emits the wrapper without child elements."""
        com_spec = ModeSwitchSenderComSpec()
        parent = ET.Element("PARENT")

        writer.writeModeSwitchSenderComSpec(parent, com_spec)

        child = parent.find("MODE-SWITCH-SENDER-COM-SPEC")
        assert child is not None
        assert len(child) == 0


class TestModeSwitchSenderComSpecRoundTrip:
    """Round-trip through the PPortPrototype PROVIDED-COM-SPECS aggregation (set → save → reload → assert)."""

    def test_round_trip_field_values(self, writer):
        """Test that all four field values survive a comspec-level write/read cycle."""
        com_spec = ModeSwitchSenderComSpec()
        com_spec.setEnhancedModeApi(_boolean(True))
        com_spec.setModeGroupRef(_ref("/mdg/Group", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        com_spec.setModeSwitchedAck(_ack_request())
        com_spec.setQueueLength(_queue_length(4))

        parent = ET.Element("PARENT")
        writer.writeModeSwitchSenderComSpec(parent, com_spec)
        element = parent.find("MODE-SWITCH-SENDER-COM-SPEC")

        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("MODE-SWITCH-SENDER-COM-SPEC", "MODE-SWITCH-SENDER-COM-SPEC xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = ARXMLParser().getModeSwitchSenderComSpec(reloaded_element)
        assert reloaded is not None
        assert reloaded.getEnhancedModeApi() is not None
        assert reloaded.getEnhancedModeApi().getValue() is True
        assert reloaded.getModeGroupRef() is not None
        assert reloaded.getModeGroupRef().getValue() == "/mdg/Group"
        assert reloaded.getModeGroupRef().getDest() == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert reloaded.getModeSwitchedAck() is not None
        assert reloaded.getModeSwitchedAck().getTimeout() is not None
        assert reloaded.getModeSwitchedAck().getTimeout().getValue() == 0.5
        assert isinstance(reloaded.getQueueLength(), PositiveInteger)
        assert reloaded.getQueueLength().getValue() == 4

    def test_round_trip_ar_object_attributes(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) survive the write/read cycle."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String

        com_spec = ModeSwitchSenderComSpec()
        checksum = String()
        checksum.setValue("abc123")
        com_spec.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T12:00:00+00:00")
        com_spec.setTimestamp(timestamp)

        parent = ET.Element("PARENT")
        writer.writeModeSwitchSenderComSpec(parent, com_spec)
        element = parent.find("MODE-SWITCH-SENDER-COM-SPEC")
        assert element is not None
        assert element.attrib.get("S") is not None
        assert element.attrib.get("T") is not None

        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("MODE-SWITCH-SENDER-COM-SPEC", "MODE-SWITCH-SENDER-COM-SPEC xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = ARXMLParser().getModeSwitchSenderComSpec(reloaded_element)
        assert reloaded is not None
        assert reloaded.getChecksum() is not None
        assert reloaded.getChecksum().getValue() == "abc123"
        assert reloaded.getTimestamp() is not None

    def test_round_trip_via_provided_com_spec_dispatch(self, writer):
        """Test that the PROVIDED-COM-SPECS aggregation survives writePPortComSpec → readProvidedComSpec with field values."""
        app = ApplicationSwComponentType(parent=AUTOSAR.getInstance(), short_name="App")
        p_port = app.createPPortPrototype("PPort")
        com_spec = ModeSwitchSenderComSpec()
        com_spec.setEnhancedModeApi(_boolean(True))
        com_spec.setModeGroupRef(_ref("/mdg/Group", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        com_spec.setQueueLength(_queue_length(4))
        p_port.addProvidedComSpec(com_spec)

        element = ET.Element("P-PORT-PROTOTYPE")
        writer.setAbstractProvidedPortPrototype(element, p_port)
        wrapper = element.find("PROVIDED-COM-SPECS")
        assert wrapper is not None
        assert wrapper.find("MODE-SWITCH-SENDER-COM-SPEC") is not None

        xml_text = ET.tostring(wrapper, encoding="unicode")
        reloaded_wrapper = ET.fromstring("<P-PORT-PROTOTYPE xmlns='http://autosar.org/schema/r4.0'>%s</P-PORT-PROTOTYPE>" % xml_text)

        target_app = ApplicationSwComponentType(parent=AUTOSAR.getInstance(), short_name="Target")
        target_p_port = target_app.createPPortPrototype("PPort")
        ARXMLParser().readProvidedComSpec(reloaded_wrapper, target_p_port)
        specs = target_p_port.getProvidedComSpecs()
        assert len(specs) == 1
        reloaded = specs[0]
        assert isinstance(reloaded, ModeSwitchSenderComSpec)
        assert reloaded.getEnhancedModeApi() is not None
        assert reloaded.getEnhancedModeApi().getValue() is True
        assert reloaded.getModeGroupRef() is not None
        assert reloaded.getModeGroupRef().getValue() == "/mdg/Group"
        assert reloaded.getModeSwitchedAck() is None
        assert reloaded.getQueueLength() is not None
        assert reloaded.getQueueLength().getValue() == 4
