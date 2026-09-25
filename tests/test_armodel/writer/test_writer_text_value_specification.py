"""Reader/writer round-trip tests for TextValueSpecification (Table 5.113)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, VerbatimString
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


def _text(value: str) -> VerbatimString:
    text = VerbatimString()
    text.setValue(value)
    return text


def _parent():
    return ET.Element("PARENT")


def test_write_text_value_specification(writer):
    parent = _parent()
    spec = TextValueSpecification()
    spec.setShortLabel(Identifier().setValue("tvs"))
    spec.setValue(_text("ON"))

    writer.writeTextValueSpecification(parent, spec)

    tag = parent.find("TEXT-VALUE-SPECIFICATION")
    assert tag is not None
    children = list(tag)
    assert [child.tag for child in children] == ["SHORT-LABEL", "VALUE"]
    assert children[0].text == "tvs"
    assert children[1].text == "ON"


def test_write_text_value_specification_empty(writer):
    parent = _parent()
    writer.writeTextValueSpecification(parent, TextValueSpecification())

    tag = parent.find("TEXT-VALUE-SPECIFICATION")
    assert tag is not None
    assert tag.find("VALUE") is None


def test_text_value_specification_round_trip(writer):
    spec = TextValueSpecification()
    spec.setShortLabel(Identifier().setValue("tvs"))
    spec.setValue(_text("ON"))

    parent = _parent()
    writer.writeTextValueSpecification(parent, spec)

    xml_text = ET.tostring(parent, encoding="unicode")
    reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

    parser = ARXMLParser()
    reloaded = parser.getValueSpecification(reparsed[0], "TEXT-VALUE-SPECIFICATION")
    assert isinstance(reloaded, TextValueSpecification)
    assert isinstance(reloaded.getValue(), VerbatimString)
    assert reloaded.getShortLabel().getValue() == "tvs"
    assert reloaded.getValue().getValue() == "ON"
