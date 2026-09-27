"""
Tests for parsing FIELD elements via readField (Adaptive Platform Field, Table B.9).

Writer counterpart: tests/test_armodel/writer/test_adaptive_field.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.ApplicationDesign.PortInterface import Field
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _parse_field(parser: ARXMLParser, inner: str) -> Field:
    element = ET.fromstring(
        f"""<FIELD xmlns='{NS}'>
            <SHORT-NAME>field</SHORT-NAME>
            {inner}
        </FIELD>"""
    )
    field = Field(None, "field")
    parser.readField(element, field)
    return field


class TestReadField:
    def test_read_has_flags(self, parser):
        field = _parse_field(
            parser,
            "<HAS-GETTER>true</HAS-GETTER>" "<HAS-NOTIFIER>false</HAS-NOTIFIER>" "<HAS-SETTER>true</HAS-SETTER>",
        )
        assert field.getHasGetter().getValue() is True
        assert field.getHasNotifier().getValue() is False
        assert field.getHasSetter().getValue() is True

    def test_read_absent_flags(self, parser):
        field = _parse_field(parser, "")
        assert field.getHasGetter() is None
        assert field.getHasNotifier() is None
        assert field.getHasSetter() is None

    def test_read_short_name(self, parser):
        field = _parse_field(parser, "")
        assert field.getShortName() == "field"
