"""
Tests for readAbstractVariationRestriction (AbstractVariationRestriction, Table 4.38).

Round-trip counterpart: tests/test_armodel/writer/test_abstract_variation_restriction.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes import (
    AbstractVariationRestriction,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class _Derived(AbstractVariationRestriction):
    pass


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadAbstractVariationRestriction:
    """
    Test readAbstractVariationRestriction.
    """

    def test_read_members(self, parser):
        element = ET.fromstring(
            f"""<RESTRICTION xmlns='{NS}'>
                <VARIATION>true</VARIATION>
                <VALID-BINDING-TIMES>
                    <VALID-BINDING-TIME>POST-BUILD</VALID-BINDING-TIME>
                    <VALID-BINDING-TIME>PRE-COMPILE-TIME</VALID-BINDING-TIME>
                </VALID-BINDING-TIMES>
            </RESTRICTION>"""
        )
        restriction = _Derived()
        parser.readAbstractVariationRestriction(element, restriction)

        assert restriction.getVariation() is not None
        assert restriction.getVariation().getValue() is True
        assert len(restriction.getValidBindingTimes()) == 2
        assert restriction.getValidBindingTimes()[0].getValue() == "POST-BUILD"
        assert restriction.getValidBindingTimes()[1].getValue() == "PRE-COMPILE-TIME"

    def test_read_empty(self, parser):
        element = ET.fromstring(f"<RESTRICTION xmlns='{NS}'/>")
        restriction = _Derived()
        parser.readAbstractVariationRestriction(element, restriction)

        assert restriction.getVariation() is None
        assert restriction.getValidBindingTimes() == []
