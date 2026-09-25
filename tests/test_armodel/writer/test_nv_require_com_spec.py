"""
Tests for writing NV-REQUIRE-COM-SPEC elements — NvRequireComSpec, Table 4.84 (p.194, R23-11).

NvRequireComSpec (Base = RPortComSpec) carries the optional attributes
initValue (INIT-VALUE 0..1 ValueSpecification aggregation)
and variable (VARIABLE-REF 0..1 reference to a VariableDataPrototype). Writer
element order must follow the XSD sequenceOffset (AUTOSAR_00052.xsd group
NV-REQUIRE-COM-SPEC: INIT-VALUE → VARIABLE-REF).
The comspec-level round-trip goes through the RPortPrototype REQUIRED-COM-SPECS
aggregation (writeRPortComSpec dispatch → readRequiredComSpec dispatch).

Round-trip counterpart: tests/test_armodel/parser/test_nv_require_com_spec.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR, ApplicationSwComponentType
from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, DateTime, RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NvRequireComSpec
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


def _text_value(text):
    value = TextValueSpecification()
    literal = ARLiteral()
    literal.setValue(text)
    value.setValue(literal)
    return value


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestWriteNvRequireComSpec:
    """Tests for writeNvRequireComSpec — own element field values (Table 4.84)."""

    def test_write_field_values(self, writer):
        """Test that both elements are emitted with their field values."""
        com_spec = NvRequireComSpec()
        com_spec.setInitValue(_text_value("0"))
        com_spec.setVariableRef(_ref("/pkg/NvDataInterface/Var", "VARIABLE-DATA-PROTOTYPE"))
        parent = ET.Element("PARENT")

        writer.writeNvRequireComSpec(parent, com_spec)

        child = parent.find("NV-REQUIRE-COM-SPEC")
        assert child is not None
        assert child.find("INIT-VALUE") is not None
        assert child.find("INIT-VALUE/TEXT-VALUE-SPECIFICATION/VALUE").text == "0"
        assert child.find("VARIABLE-REF").text == "/pkg/NvDataInterface/Var"
        assert child.find("VARIABLE-REF").attrib.get("DEST") == "VARIABLE-DATA-PROTOTYPE"

    def test_write_xsd_element_order(self, writer):
        """Test that the emitted element order follows the XSD group sequence."""
        com_spec = NvRequireComSpec()
        com_spec.setInitValue(_text_value("0"))
        com_spec.setVariableRef(_ref("/pkg/NvDataInterface/Var", "VARIABLE-DATA-PROTOTYPE"))
        parent = ET.Element("PARENT")

        writer.writeNvRequireComSpec(parent, com_spec)

        child = parent.find("NV-REQUIRE-COM-SPEC")
        assert [elem.tag for elem in child] == ["INIT-VALUE", "VARIABLE-REF"]

    def test_write_unset_fields_emits_empty_wrapper(self, writer):
        """Test that a set-but-empty com spec emits the wrapper without child elements."""
        com_spec = NvRequireComSpec()
        parent = ET.Element("PARENT")

        writer.writeNvRequireComSpec(parent, com_spec)

        child = parent.find("NV-REQUIRE-COM-SPEC")
        assert child is not None
        assert len(child) == 0


class TestNvRequireComSpecRoundTrip:
    """Round-trip through the RPortPrototype REQUIRED-COM-SPECS aggregation (set → save → reload → assert)."""

    def test_round_trip_field_values(self, writer):
        """Test that both field values survive a comspec-level write/read cycle."""
        com_spec = NvRequireComSpec()
        com_spec.setInitValue(_text_value("0"))
        com_spec.setVariableRef(_ref("/pkg/NvDataInterface/Var", "VARIABLE-DATA-PROTOTYPE"))

        parent = ET.Element("PARENT")
        writer.writeNvRequireComSpec(parent, com_spec)
        element = parent.find("NV-REQUIRE-COM-SPEC")

        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("NV-REQUIRE-COM-SPEC", "NV-REQUIRE-COM-SPEC xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = ARXMLParser().getNvRequireComSpec(reloaded_element)
        assert reloaded is not None
        assert isinstance(reloaded.getInitValue(), TextValueSpecification)
        assert reloaded.getInitValue().getValue().getValue() == "0"
        assert reloaded.getVariableRef() is not None
        assert reloaded.getVariableRef().getValue() == "/pkg/NvDataInterface/Var"
        assert reloaded.getVariableRef().getDest() == "VARIABLE-DATA-PROTOTYPE"

    def test_round_trip_ar_object_attributes(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) survive the write/read cycle."""
        com_spec = NvRequireComSpec()
        checksum = String()
        checksum.setValue("abc123")
        com_spec.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T12:00:00+00:00")
        com_spec.setTimestamp(timestamp)

        parent = ET.Element("PARENT")
        writer.writeNvRequireComSpec(parent, com_spec)
        element = parent.find("NV-REQUIRE-COM-SPEC")
        assert element is not None
        assert element.attrib.get("S") is not None
        assert element.attrib.get("T") is not None

        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("NV-REQUIRE-COM-SPEC", "NV-REQUIRE-COM-SPEC xmlns='http://autosar.org/schema/r4.0'", 1))
        reloaded = ARXMLParser().getNvRequireComSpec(reloaded_element)
        assert reloaded is not None
        assert reloaded.getChecksum() is not None
        assert reloaded.getChecksum().getValue() == "abc123"
        assert reloaded.getTimestamp() is not None

    def test_round_trip_via_required_com_spec_dispatch(self, writer):
        """Test that the REQUIRED-COM-SPECS aggregation survives writeRPortComSpec → readRequiredComSpec with field values."""
        app = ApplicationSwComponentType(parent=AUTOSAR.getInstance(), short_name="App")
        r_port = app.createRPortPrototype("RPort")
        com_spec = NvRequireComSpec()
        com_spec.setInitValue(_text_value("0"))
        com_spec.setVariableRef(_ref("/pkg/NvDataInterface/Var", "VARIABLE-DATA-PROTOTYPE"))
        r_port.addRequiredComSpec(com_spec)

        element = ET.Element("R-PORT-PROTOTYPE")
        writer.setAbstractRequiredPortPrototype(element, r_port)
        wrapper = element.find("REQUIRED-COM-SPECS")
        assert wrapper is not None
        assert wrapper.find("NV-REQUIRE-COM-SPEC") is not None

        xml_text = ET.tostring(wrapper, encoding="unicode")
        reloaded_wrapper = ET.fromstring("<R-PORT-PROTOTYPE xmlns='http://autosar.org/schema/r4.0'>%s</R-PORT-PROTOTYPE>" % xml_text)

        target_app = ApplicationSwComponentType(parent=AUTOSAR.getInstance(), short_name="Target")
        target_r_port = target_app.createRPortPrototype("RPort")
        ARXMLParser().readRequiredComSpec(reloaded_wrapper, target_r_port)
        specs = target_r_port.getRequiredComSpecs()
        assert len(specs) == 1
        reloaded = specs[0]
        assert isinstance(reloaded, NvRequireComSpec)
        assert isinstance(reloaded.getInitValue(), TextValueSpecification)
        assert reloaded.getInitValue().getValue().getValue() == "0"
        assert reloaded.getVariableRef() is not None
        assert reloaded.getVariableRef().getValue() == "/pkg/NvDataInterface/Var"
        assert reloaded.getVariableRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
