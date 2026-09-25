"""Reader/writer round-trip tests for NumericalValueSpecification (Table 5.114)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NumericalValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, Identifier
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


def _numerical(text: str) -> ARNumerical:
    numerical = ARNumerical()
    numerical.setValue(text)
    return numerical


def _parent():
    return ET.Element("PARENT")


def test_write_numerical_value_specification(writer):
    parent = _parent()
    spec = NumericalValueSpecification()
    spec.setShortLabel(Identifier().setValue("nvs"))
    spec.setValue(_numerical("3.14"))

    writer.writeNumericalValueSpecification(parent, spec)

    tag = parent.find("NUMERICAL-VALUE-SPECIFICATION")
    assert tag is not None
    children = list(tag)
    assert [child.tag for child in children] == ["SHORT-LABEL", "VALUE"]
    assert children[0].text == "nvs"
    assert children[1].text == "3.14"


def test_write_numerical_value_specification_empty(writer):
    parent = _parent()
    writer.writeNumericalValueSpecification(parent, NumericalValueSpecification())

    tag = parent.find("NUMERICAL-VALUE-SPECIFICATION")
    assert tag is not None
    assert tag.find("VALUE") is None


def test_numerical_value_specification_round_trip(writer):
    spec = NumericalValueSpecification()
    spec.setShortLabel(Identifier().setValue("nvs"))
    spec.setValue(_numerical("3.14"))

    parent = _parent()
    writer.writeNumericalValueSpecification(parent, spec)

    xml_text = ET.tostring(parent, encoding="unicode")
    reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

    parser = ARXMLParser()
    reloaded = parser.getValueSpecification(reparsed[0], "NUMERICAL-VALUE-SPECIFICATION")
    assert isinstance(reloaded, NumericalValueSpecification)
    assert reloaded.getShortLabel().getValue() == "nvs"
    assert reloaded.getValue().getValue() == 3.14
