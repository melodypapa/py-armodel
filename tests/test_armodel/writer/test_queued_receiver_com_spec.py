"""
Tests for writing QUEUED-RECEIVER-COM-SPEC elements — QueuedReceiverComSpec, Table 4.63 (p.173, R23-11).

QueuedReceiverComSpec (Base = ARObject + RPortComSpec + ReceiverComSpec) carries the
single own attribute queueLength (QUEUE-LENGTH 0..1 PositiveInteger). Writer element
order must follow the XSD sequence (AUTOSAR_00052.xsd complexType QUEUED-RECEIVER-COM-SPEC:
AR-OBJECT → R-PORT-COM-SPEC (empty) → RECEIVER-COM-SPEC group → QUEUED-RECEIVER-COM-SPEC
group), so QUEUE-LENGTH is emitted after every inherited ReceiverComSpec element.
The comspec-level round-trip goes through the RPortPrototype REQUIRED-COM-SPECS
aggregation (writeRPortComSpec dispatch → readRequiredComSpec dispatch).

Round-trip counterpart: tests/test_armodel/parser/test_queued_receiver_com_spec.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR, ApplicationSwComponentType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import QueuedReceiverComSpec
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


def _queue_length(value):
    queue_length = PositiveInteger()
    queue_length.setValue(value)
    return queue_length


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestWriteQueuedReceiverComSpec:
    """Tests for writeQueuedReceiverComSpec — own element field values (Table 4.63)."""

    def test_write_field_value(self, writer):
        """Test that QUEUE-LENGTH is emitted with its value read through the getter."""
        com_spec = QueuedReceiverComSpec()
        com_spec.setQueueLength(_queue_length("5"))
        parent = ET.Element("PARENT")

        writer.writeQueuedReceiverComSpec(parent, com_spec)

        child = parent.find("QUEUED-RECEIVER-COM-SPEC")
        assert child is not None
        assert child.find("QUEUE-LENGTH") is not None
        assert child.find("QUEUE-LENGTH").text == "5"

    def test_write_xsd_element_order(self, writer):
        """Test that QUEUE-LENGTH is emitted after the inherited ReceiverComSpec elements (XSD group order)."""
        com_spec = QueuedReceiverComSpec()
        com_spec.setDataElementRef(_ref("/pkg/Interface/Data", "VARIABLE-DATA-PROTOTYPE"))
        com_spec.setQueueLength(_queue_length("5"))
        parent = ET.Element("PARENT")

        writer.writeQueuedReceiverComSpec(parent, com_spec)

        child = parent.find("QUEUED-RECEIVER-COM-SPEC")
        assert [elem.tag for elem in child] == ["DATA-ELEMENT-REF", "QUEUE-LENGTH"]

    def test_write_unset_fields_emits_empty_wrapper(self, writer):
        """Test that a set-but-empty com spec emits the wrapper without child elements."""
        com_spec = QueuedReceiverComSpec()
        parent = ET.Element("PARENT")

        writer.writeQueuedReceiverComSpec(parent, com_spec)

        child = parent.find("QUEUED-RECEIVER-COM-SPEC")
        assert child is not None
        assert len(child) == 0


class TestQueuedReceiverComSpecRoundTrip:
    """Round-trip through the RPortPrototype REQUIRED-COM-SPECS aggregation (set → save → reload → assert)."""

    def test_round_trip_field_value(self, writer):
        """Test that the queueLength field value survives a comspec-level write/read cycle."""
        com_spec = QueuedReceiverComSpec()
        com_spec.setQueueLength(_queue_length("5"))

        parent = ET.Element("PARENT")
        writer.writeQueuedReceiverComSpec(parent, com_spec)
        element = parent.find("QUEUED-RECEIVER-COM-SPEC")

        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("QUEUED-RECEIVER-COM-SPEC", "QUEUED-RECEIVER-COM-SPEC xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = ARXMLParser().getQueuedReceiverComSpec(reloaded_element)
        assert reloaded is not None
        assert isinstance(reloaded.getQueueLength(), PositiveInteger)
        assert reloaded.getQueueLength().getValue() == 5

    def test_round_trip_ar_object_attributes(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) survive the write/read cycle."""
        com_spec = QueuedReceiverComSpec()
        checksum = String()
        checksum.setValue("abc123")
        com_spec.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T12:00:00+00:00")
        com_spec.setTimestamp(timestamp)

        parent = ET.Element("PARENT")
        writer.writeQueuedReceiverComSpec(parent, com_spec)
        element = parent.find("QUEUED-RECEIVER-COM-SPEC")
        assert element is not None
        assert element.attrib.get("S") is not None
        assert element.attrib.get("T") is not None

        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("QUEUED-RECEIVER-COM-SPEC", "QUEUED-RECEIVER-COM-SPEC xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = ARXMLParser().getQueuedReceiverComSpec(reloaded_element)
        assert reloaded is not None
        assert reloaded.getChecksum() is not None
        assert reloaded.getChecksum().getValue() == "abc123"
        assert reloaded.getTimestamp() is not None

    def test_round_trip_via_required_com_spec_dispatch(self, writer):
        """Test that the REQUIRED-COM-SPECS aggregation survives writeRPortComSpec → readRequiredComSpec with field values."""
        app = ApplicationSwComponentType(parent=AUTOSAR.getInstance(), short_name="App")
        r_port = app.createRPortPrototype("RPort")
        com_spec = QueuedReceiverComSpec()
        com_spec.setQueueLength(_queue_length("5"))
        r_port.addRequiredComSpec(com_spec)

        element = ET.Element("R-PORT-PROTOTYPE")
        writer.setAbstractRequiredPortPrototype(element, r_port)
        wrapper = element.find("REQUIRED-COM-SPECS")
        assert wrapper is not None
        assert wrapper.find("QUEUED-RECEIVER-COM-SPEC") is not None

        xml_text = ET.tostring(wrapper, encoding="unicode")
        reloaded_wrapper = ET.fromstring("<R-PORT-PROTOTYPE xmlns='http://autosar.org/schema/r4.0'>%s</R-PORT-PROTOTYPE>" % xml_text)

        target_app = ApplicationSwComponentType(parent=AUTOSAR.getInstance(), short_name="Target")
        target_r_port = target_app.createRPortPrototype("RPort")
        ARXMLParser().readRequiredComSpec(reloaded_wrapper, target_r_port)
        specs = target_r_port.getRequiredComSpecs()
        assert len(specs) == 1
        reloaded = specs[0]
        assert isinstance(reloaded, QueuedReceiverComSpec)
        assert isinstance(reloaded.getQueueLength(), PositiveInteger)
        assert reloaded.getQueueLength().getValue() == 5
