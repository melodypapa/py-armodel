"""Writer round-trip tests for NotAvailableValueSpecification (Table 5.116)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import NotAvailableValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
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


def _parent():
    return ET.Element("PARENT")


def test_write_not_available_value_specification(writer):
    parent = _parent()
    spec = NotAvailableValueSpecification()
    spec.setDefaultPattern(PositiveInteger().setValue("4"))

    writer.writeNotAvailableValueSpecification(parent, spec)

    tag = parent.find("NOT-AVAILABLE-VALUE-SPECIFICATION")
    assert tag is not None
    dp = tag.find("DEFAULT-PATTERN")
    assert dp is not None
    assert dp.text == "4"


def test_write_not_available_value_specification_empty(writer):
    parent = _parent()
    writer.writeNotAvailableValueSpecification(parent, NotAvailableValueSpecification())

    tag = parent.find("NOT-AVAILABLE-VALUE-SPECIFICATION")
    assert tag is not None
    assert tag.find("DEFAULT-PATTERN") is None


def test_not_available_value_specification_round_trip(writer):
    spec = NotAvailableValueSpecification()
    spec.setDefaultPattern(PositiveInteger().setValue("4"))

    parent = _parent()
    writer.writeNotAvailableValueSpecification(parent, spec)

    xml_text = ET.tostring(parent, encoding="unicode")
    reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

    parser = ARXMLParser()
    reloaded = parser.getValueSpecification(reparsed[0], "NOT-AVAILABLE-VALUE-SPECIFICATION")
    assert isinstance(reloaded, NotAvailableValueSpecification)
    assert reloaded.getDefaultPattern().getValue() == 4
