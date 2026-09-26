"""
Tests for writing FIELD elements via writeFieldContent (Adaptive Platform Field, Table B.9).

Parser counterpart: tests/test_armodel/parser/test_adaptive_field.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.ApplicationDesign.PortInterface import Field
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _field() -> Field:
    field = Field(None, "field")
    field.setHasGetter(Boolean().setValue(True))
    field.setHasNotifier(Boolean().setValue(False))
    field.setHasSetter(Boolean().setValue(True))
    return field


class TestWriteField:
    def test_write_has_flags_in_xsd_order(self, writer):
        element = ET.Element("PARENT")
        writer.writeFieldContent(element, _field())

        assert [c.tag for c in element] == ["SHORT-NAME", "HAS-GETTER", "HAS-NOTIFIER", "HAS-SETTER"]
        assert element.find("HAS-GETTER").text == "true"
        assert element.find("HAS-NOTIFIER").text == "false"
        assert element.find("HAS-SETTER").text == "true"

    def test_write_absent_flags_omit_elements(self, writer):
        element = ET.Element("PARENT")
        writer.writeFieldContent(element, Field(None, "field"))

        assert [c.tag for c in element] == ["SHORT-NAME"]

    def test_round_trip_field_values(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        parent = ET.Element("PARENT")
        writer.writeFieldContent(parent, _field())

        xml_text = ET.tostring(parent, encoding="unicode")
        reparsed = ET.fromstring(xml_text.replace("PARENT", "PARENT xmlns='%s'" % NS, 1))

        field_2 = Field(None, "field")
        ARXMLParser().readField(reparsed, field_2)
        assert field_2.getHasGetter().getValue() is True
        assert field_2.getHasNotifier().getValue() is False
        assert field_2.getHasSetter().getValue() is True
