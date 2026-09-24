"""
Tests for writing MODE-SWITCH-RECEIVER-COM-SPEC elements — ModeSwitchReceiverComSpec, Table 4.81 (p.191, R23-11).

ModeSwitchReceiverComSpec (Base = RPortComSpec) carries the optional attributes
enhancedModeApi (BOOLEAN 0..1), modeGroup (MODE-GROUP-REF 0..1) and
supportsAsynchronousModeSwitch (BOOLEAN 0..1). Writer element order must follow
the XSD sequenceOffset (AUTOSAR_00052.xsd group MODE-SWITCH-RECEIVER-COM-SPEC:
ENHANCED-MODE-API → MODE-GROUP-REF → SUPPORTS-ASYNCHRONOUS-MODE-SWITCH).
The comspec-level round-trip goes through the RPortPrototype REQUIRED-COM-SPECS
aggregation (writeRPortComSpec dispatch → readRequiredComSpec dispatch).

Round-trip counterpart: tests/test_armodel/parser/test_mode_switch_receiver_com_spec.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR, ApplicationSwComponentType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import ModeSwitchReceiverComSpec
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


class TestWriteModeSwitchReceiverComSpec:
    """Tests for setModeSwitchReceiverComSpec — own element field values (Table 4.81)."""

    def test_write_field_values(self, writer):
        """Test that all three elements are emitted with their field values."""
        com_spec = ModeSwitchReceiverComSpec()
        com_spec.setEnhancedModeApi(_boolean(True))
        com_spec.setModeGroupRef(_ref("/mdg/Group", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        com_spec.setSupportsAsynchronousModeSwitch(_boolean(False))
        parent = ET.Element("PARENT")

        writer.setModeSwitchReceiverComSpec(parent, com_spec)

        child = parent.find("MODE-SWITCH-RECEIVER-COM-SPEC")
        assert child is not None
        assert child.find("ENHANCED-MODE-API").text == "true"
        assert child.find("MODE-GROUP-REF").text == "/mdg/Group"
        assert child.find("MODE-GROUP-REF").attrib.get("DEST") == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert child.find("SUPPORTS-ASYNCHRONOUS-MODE-SWITCH").text == "false"

    def test_write_xsd_element_order(self, writer):
        """Test that the emitted element order follows the XSD group sequence."""
        com_spec = ModeSwitchReceiverComSpec()
        com_spec.setEnhancedModeApi(_boolean(True))
        com_spec.setModeGroupRef(_ref("/mdg/Group", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        com_spec.setSupportsAsynchronousModeSwitch(_boolean(False))
        parent = ET.Element("PARENT")

        writer.setModeSwitchReceiverComSpec(parent, com_spec)

        child = parent.find("MODE-SWITCH-RECEIVER-COM-SPEC")
        assert [elem.tag for elem in child] == ["ENHANCED-MODE-API", "MODE-GROUP-REF", "SUPPORTS-ASYNCHRONOUS-MODE-SWITCH"]

    def test_write_unset_fields_emits_empty_wrapper(self, writer):
        """Test that a set-but-empty com spec emits the wrapper without child elements."""
        com_spec = ModeSwitchReceiverComSpec()
        parent = ET.Element("PARENT")

        writer.setModeSwitchReceiverComSpec(parent, com_spec)

        child = parent.find("MODE-SWITCH-RECEIVER-COM-SPEC")
        assert child is not None
        assert len(child) == 0


class TestModeSwitchReceiverComSpecRoundTrip:
    """Round-trip through the RPortPrototype REQUIRED-COM-SPECS aggregation (set → save → reload → assert)."""

    def test_round_trip_field_values(self, writer):
        """Test that all three field values survive a comspec-level write/read cycle."""
        com_spec = ModeSwitchReceiverComSpec()
        com_spec.setEnhancedModeApi(_boolean(True))
        com_spec.setModeGroupRef(_ref("/mdg/Group", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        com_spec.setSupportsAsynchronousModeSwitch(_boolean(False))

        parent = ET.Element("PARENT")
        writer.setModeSwitchReceiverComSpec(parent, com_spec)
        element = parent.find("MODE-SWITCH-RECEIVER-COM-SPEC")

        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("MODE-SWITCH-RECEIVER-COM-SPEC", "MODE-SWITCH-RECEIVER-COM-SPEC xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = ARXMLParser().getModeSwitchReceiverComSpec(reloaded_element)
        assert reloaded is not None
        assert reloaded.getEnhancedModeApi() is not None
        assert reloaded.getEnhancedModeApi().getValue() is True
        assert reloaded.getModeGroupRef() is not None
        assert reloaded.getModeGroupRef().getValue() == "/mdg/Group"
        assert reloaded.getModeGroupRef().getDest() == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert reloaded.getSupportsAsynchronousModeSwitch() is not None
        assert reloaded.getSupportsAsynchronousModeSwitch().getValue() is False

    def test_round_trip_ar_object_attributes(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) survive the write/read cycle."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String

        com_spec = ModeSwitchReceiverComSpec()
        checksum = String()
        checksum.setValue("abc123")
        com_spec.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T12:00:00+00:00")
        com_spec.setTimestamp(timestamp)

        parent = ET.Element("PARENT")
        writer.setModeSwitchReceiverComSpec(parent, com_spec)
        element = parent.find("MODE-SWITCH-RECEIVER-COM-SPEC")
        assert element is not None
        assert element.attrib.get("S") is not None
        assert element.attrib.get("T") is not None

        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("MODE-SWITCH-RECEIVER-COM-SPEC", "MODE-SWITCH-RECEIVER-COM-SPEC xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = ARXMLParser().getModeSwitchReceiverComSpec(reloaded_element)
        assert reloaded is not None
        assert reloaded.getChecksum() is not None
        assert reloaded.getChecksum().getValue() == "abc123"
        assert reloaded.getTimestamp() is not None

    def test_round_trip_via_required_com_spec_dispatch(self, writer):
        """Test that the REQUIRED-COM-SPECS aggregation survives writeRPortComSpec → readRequiredComSpec with field values."""
        app = ApplicationSwComponentType(parent=AUTOSAR.getInstance(), short_name="App")
        r_port = app.createRPortPrototype("RPort")
        com_spec = ModeSwitchReceiverComSpec()
        com_spec.setEnhancedModeApi(_boolean(True))
        com_spec.setModeGroupRef(_ref("/mdg/Group", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        r_port.addRequiredComSpec(com_spec)

        element = ET.Element("R-PORT-PROTOTYPE")
        writer.setAbstractRequiredPortPrototype(element, r_port)
        wrapper = element.find("REQUIRED-COM-SPECS")
        assert wrapper is not None
        assert wrapper.find("MODE-SWITCH-RECEIVER-COM-SPEC") is not None

        xml_text = ET.tostring(wrapper, encoding="unicode")
        reloaded_wrapper = ET.fromstring("<R-PORT-PROTOTYPE xmlns='http://autosar.org/schema/r4.0'>%s</R-PORT-PROTOTYPE>" % xml_text)

        target_app = ApplicationSwComponentType(parent=AUTOSAR.getInstance(), short_name="Target")
        target_r_port = target_app.createRPortPrototype("RPort")
        ARXMLParser().readRequiredComSpec(reloaded_wrapper, target_r_port)
        specs = target_r_port.getRequiredComSpecs()
        assert len(specs) == 1
        reloaded = specs[0]
        assert isinstance(reloaded, ModeSwitchReceiverComSpec)
        assert reloaded.getEnhancedModeApi() is not None
        assert reloaded.getEnhancedModeApi().getValue() is True
        assert reloaded.getModeGroupRef() is not None
        assert reloaded.getModeGroupRef().getValue() == "/mdg/Group"
        assert reloaded.getSupportsAsynchronousModeSwitch() is None
