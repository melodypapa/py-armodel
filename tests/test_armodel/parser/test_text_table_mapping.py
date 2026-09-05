"""
Tests for reading TEXT-TABLE-MAPPING elements (TextTableMapping, Table 4.36) incl.
the VALUE-PAIRS wrapper (TextTableValuePair, Table 4.38) and the MAPPING-DIRECTION
enum value (MappingDirectionEnum, Table 4.37).

Round-trip counterpart: tests/test_armodel/writer/test_text_table_mapping.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TextTableValuePair

NS = "http://autosar.org/schema/r4.0"


class TestReadTextTableMapping:
    """Test TextTableMapping population via getTextTableMapping (Table 4.36)."""

    def test_read_field_values(self, parser):
        """All four scalar attributes plus two VALUE-PAIRS children populate."""
        element = ET.fromstring(
            f"""<TEXT-TABLE-MAPPING xmlns='{NS}'>
                <BITFIELD-TEXT-TABLE-MASK-FIRST>8</BITFIELD-TEXT-TABLE-MASK-FIRST>
                <BITFIELD-TEXT-TABLE-MASK-SECOND>16</BITFIELD-TEXT-TABLE-MASK-SECOND>
                <IDENTICAL-MAPPING>true</IDENTICAL-MAPPING>
                <MAPPING-DIRECTION>bidirectional</MAPPING-DIRECTION>
                <VALUE-PAIRS>
                    <TEXT-TABLE-VALUE-PAIR>
                        <FIRST-VALUE>1</FIRST-VALUE>
                        <SECOND-VALUE>2</SECOND-VALUE>
                    </TEXT-TABLE-VALUE-PAIR>
                    <TEXT-TABLE-VALUE-PAIR>
                        <FIRST-VALUE>3</FIRST-VALUE>
                    </TEXT-TABLE-VALUE-PAIR>
                </VALUE-PAIRS>
            </TEXT-TABLE-MAPPING>"""
        )

        mapping = parser.getTextTableMapping(element)

        assert mapping.getBitfieldTextTableMaskFirst().getValue() == 8
        assert mapping.getBitfieldTextTableMaskSecond().getValue() == 16
        assert mapping.getIdenticalMapping().getValue() is True
        assert mapping.getMappingDirection().getValue() == "bidirectional"

        value_pairs = mapping.getValuePairs()
        assert len(value_pairs) == 2
        assert isinstance(value_pairs[0], TextTableValuePair)
        assert value_pairs[0].getFirstValue().getValue() == "1"
        assert value_pairs[0].getSecondValue().getValue() == "2"
        assert value_pairs[1].getFirstValue().getValue() == "3"
        assert value_pairs[1].getSecondValue() is None

    def test_read_absent_value_pairs(self, parser):
        """A TEXT-TABLE-MAPPING without VALUE-PAIRS leaves valuePairs empty."""
        element = ET.fromstring(
            f"""<TEXT-TABLE-MAPPING xmlns='{NS}'>
                <IDENTICAL-MAPPING>true</IDENTICAL-MAPPING>
            </TEXT-TABLE-MAPPING>"""
        )

        mapping = parser.getTextTableMapping(element)

        assert mapping.getValuePairs() == []
        assert mapping.getMappingDirection() is None

    def test_read_empty_value_pairs_wrapper(self, parser):
        """An empty VALUE-PAIRS wrapper leaves valuePairs empty (empty-wrapper case)."""
        element = ET.fromstring(
            f"""<TEXT-TABLE-MAPPING xmlns='{NS}'>
                <VALUE-PAIRS/>
            </TEXT-TABLE-MAPPING>"""
        )

        mapping = parser.getTextTableMapping(element)

        assert mapping.getValuePairs() == []


def _positive_integer(text):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

    value = PositiveInteger()
    value.setValue(text)
    return value


def _boolean(value):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean

    result = Boolean()
    result.setValue(value)
    return result


def _literal(text):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral

    result = ARLiteral()
    result.setValue(text)
    return result


def _numerical(text):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical

    result = Numerical()
    result.setValue(text)
    return result
