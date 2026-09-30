"""
Tests for readAbstractValueRestriction (AbstractValueRestriction, Table 4.37).

Round-trip counterpart: tests/test_armodel/writer/test_abstract_value_restriction.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes import (
    AbstractValueRestriction,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    PositiveInteger,
    RegularExpression,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class _Derived(AbstractValueRestriction):
    pass


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadAbstractValueRestriction:
    """
    Test readAbstractValueRestriction.
    """

    def test_read_members(self, parser):
        element = ET.fromstring(
            f"""<RESTRICTION xmlns='{NS}'>
                <MAX INTERVAL-TYPE="INCLUSIVE">10.0</MAX>
                <MAX-LENGTH>5</MAX-LENGTH>
                <MIN INTERVAL-TYPE="INCLUSIVE">0.0</MIN>
                <MIN-LENGTH>1</MIN-LENGTH>
                <PATTERN>[0-9]+</PATTERN>
            </RESTRICTION>"""
        )
        restriction = _Derived()
        parser.readAbstractValueRestriction(element, restriction)

        assert restriction.getMax() is not None
        assert restriction.getMax().getValue() == "10.0"
        assert restriction.getMaxLength().getValue() == 5
        assert restriction.getMin().getValue() == "0.0"
        assert restriction.getMinLength().getValue() == 1
        assert restriction.getPattern().getValue() == "[0-9]+"

    def test_read_empty(self, parser):
        element = ET.fromstring(f"<RESTRICTION xmlns='{NS}'/>")
        restriction = _Derived()
        parser.readAbstractValueRestriction(element, restriction)

        assert restriction.getMax() is None
        assert restriction.getMaxLength() is None
        assert restriction.getMin() is None
        assert restriction.getMinLength() is None
        assert restriction.getPattern() is None
