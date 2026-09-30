"""
Tests for writeAbstractValueRestriction (AbstractValueRestriction, Table 4.37).

Round-trip counterpart: tests/test_armodel/parser/test_abstract_value_restriction.py
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
from armodel.writer.arxml_writer import ARXMLWriter


class _Derived(AbstractValueRestriction):
    pass


class TestWriteAbstractValueRestriction:
    """
    Test writeAbstractValueRestriction.
    """

    def test_write_members(self):
        restriction = _Derived()
        restriction.setMax(Limit().setValue("10.0"))
        restriction.setMaxLength(PositiveInteger().setValue(5))
        restriction.setMin(Limit().setValue("0.0"))
        restriction.setMinLength(PositiveInteger().setValue(1))
        restriction.setPattern(RegularExpression().setValue("[0-9]+"))

        writer = ARXMLWriter()
        element = ET.Element("RESTRICTION")
        writer.writeAbstractValueRestriction(element, restriction)

        assert element.find("MAX").text == "10.0"
        assert element.find("MAX-LENGTH").text == "5"
        assert element.find("MIN").text == "0.0"
        assert element.find("MIN-LENGTH").text == "1"
        assert element.find("PATTERN").text == "[0-9]+"

    def test_write_empty(self):
        restriction = _Derived()
        writer = ARXMLWriter()
        element = ET.Element("RESTRICTION")
        writer.writeAbstractValueRestriction(element, restriction)

        assert len(list(element)) == 0
