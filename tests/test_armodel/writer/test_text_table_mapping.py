"""
Tests for writing TEXT-TABLE-MAPPING elements (TextTableMapping, Table 4.36) incl.
the VALUE-PAIRS wrapper (TextTableValuePair, Table 4.38), plus a write -> re-parse
round-trip.

Reader counterpart: tests/test_armodel/parser/test_text_table_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    Boolean,
    Numerical,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    TextTableMapping,
    TextTableValuePair,
)
from armodel.parser.arxml_parser import ARXMLParser
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


class TestWriteTextTableMapping:
    """Test the XML shape produced by setTextTableMapping (Table 4.36)."""

    def test_write_full(self, writer):
        """All scalars plus the VALUE-PAIRS wrapper with two pairs are emitted."""
        mapping = TextTableMapping()
        mapping.setBitfieldTextTableMaskFirst(_positive_integer("8"))
        mapping.setBitfieldTextTableMaskSecond(_positive_integer("16"))
        mapping.setIdenticalMapping(_boolean(True))
        mapping.setMappingDirection(_literal("bidirectional"))
        first = TextTableValuePair()
        first.setFirstValue(_numerical("1"))
        first.setSecondValue(_numerical("2"))
        second = TextTableValuePair()
        second.setFirstValue(_numerical("3"))
        mapping.addValuePair(first)
        mapping.addValuePair(second)

        parent = ET.fromstring(f"<PARENT xmlns='{NS}'/>")
        writer.setTextTableMapping(parent, mapping)
        element = parent[0]

        assert element.tag == "TEXT-TABLE-MAPPING"
        assert element.findtext("BITFIELD-TEXT-TABLE-MASK-FIRST") == "8"
        assert element.findtext("BITFIELD-TEXT-TABLE-MASK-SECOND") == "16"
        assert element.findtext("IDENTICAL-MAPPING") == "true"
        assert element.findtext("MAPPING-DIRECTION") == "bidirectional"

        value_pairs = element.find("VALUE-PAIRS")
        assert value_pairs is not None
        pairs = value_pairs.findall("TEXT-TABLE-VALUE-PAIR")
        assert len(pairs) == 2
        assert pairs[0].findtext("FIRST-VALUE") == "1"
        assert pairs[0].findtext("SECOND-VALUE") == "2"
        assert pairs[1].findtext("FIRST-VALUE") == "3"
        assert pairs[1].find("SECOND-VALUE") is None

    def test_write_empty(self, writer):
        """No value pairs means no VALUE-PAIRS element at all."""
        mapping = TextTableMapping()
        mapping.setIdenticalMapping(_boolean(True))

        parent = ET.fromstring(f"<PARENT xmlns='{NS}'/>")
        writer.setTextTableMapping(parent, mapping)

        element = parent[0]
        assert element.find("VALUE-PAIRS") is None
        assert element.findtext("IDENTICAL-MAPPING") == "true"

    def test_round_trip_with_value_pairs(self, writer):
        """write -> serialize -> parse keeps every field value."""
        mapping = TextTableMapping()
        mapping.setBitfieldTextTableMaskFirst(_positive_integer("8"))
        mapping.setIdenticalMapping(_boolean(True))
        mapping.setMappingDirection(_literal("firstToSecond"))
        pair = TextTableValuePair()
        pair.setFirstValue(_numerical("1"))
        pair.setSecondValue(_numerical("2"))
        mapping.addValuePair(pair)

        parent = ET.fromstring("<PARENT/>")
        writer.setTextTableMapping(parent, mapping)
        inner_children = "".join(ET.tostring(child, encoding="unicode") for child in parent[0])
        element = ET.fromstring(f"<TEXT-TABLE-MAPPING xmlns='{NS}'>{inner_children}</TEXT-TABLE-MAPPING>")

        parser = ARXMLParser(options={"warning": True})
        reparsed = parser.getTextTableMapping(element)

        assert reparsed.getBitfieldTextTableMaskFirst().getValue() == 8
        assert reparsed.getIdenticalMapping().getValue() is True
        assert reparsed.getMappingDirection().getValue() == "firstToSecond"
        assert len(reparsed.getValuePairs()) == 1
        assert reparsed.getValuePairs()[0].getFirstValue().getValue() == "1"
        assert reparsed.getValuePairs()[0].getSecondValue().getValue() == "2"


def _positive_integer(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


def _boolean(value):
    result = Boolean()
    result.setValue(value)
    return result


def _literal(text):
    result = ARLiteral()
    result.setValue(text)
    return result


def _numerical(text):
    result = Numerical()
    result.setValue(text)
    return result
