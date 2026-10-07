"""Writer tests for SoftwareContext (writeSoftwareContext) and the write→parse round-trip."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import SoftwareContext
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


def _full_context():
    context = SoftwareContext()
    context.setInput(String().setValue("port 4711"))
    context.setState(String().setValue("WARM_START"))
    return context


def _qualify_namespaces(element):
    """Qualify every plain tag with the AUTOSAR namespace so the namespace-aware parser can read it back."""
    for el in element.iter():
        if not el.tag.startswith("{"):
            el.tag = "{%s}%s" % (NS, el.tag)
    return element


class TestWriteSoftwareContext:
    def test_write_field_values(self, writer):
        parent = ET.Element("PARENT")
        writer.writeSoftwareContext(parent, _full_context())
        assert len(parent) == 1
        element = parent[0]
        assert element.tag == "SOFTWARE-CONTEXT"
        assert element.find("INPUT").text == "port 4711"
        assert element.find("STATE").text == "WARM_START"

    def test_write_xsd_element_order(self, writer):
        """Children follow the XSD sequence of group SOFTWARE-CONTEXT (AUTOSAR_00052.xsd L109295)."""
        parent = ET.Element("PARENT")
        writer.writeSoftwareContext(parent, _full_context())
        tags = [child.tag for child in parent[0]]
        assert tags == ["INPUT", "STATE"]

    def test_write_none_context(self, writer):
        parent = ET.Element("PARENT")
        writer.writeSoftwareContext(parent, None)
        assert len(parent) == 0

    def test_round_trip(self, writer):
        parent = ET.Element("PARENT")
        writer.writeSoftwareContext(parent, _full_context())
        parsed_parent = ET.fromstring(ET.tostring(_qualify_namespaces(parent), default_namespace=NS))
        context_2 = SoftwareContext()
        ARXMLParser().readSoftwareContext(parsed_parent[0], context_2)
        assert context_2.getInput().getValue() == "port 4711"
        assert context_2.getState().getValue() == "WARM_START"
