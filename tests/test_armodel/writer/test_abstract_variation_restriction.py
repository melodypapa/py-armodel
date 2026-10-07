"""
Tests for writeAbstractVariationRestriction (AbstractVariationRestriction, Table 4.38).

Round-trip counterpart: tests/test_armodel/parser/test_abstract_variation_restriction.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes import (
    AbstractVariationRestriction,
    FullBindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    DateTime,
    String,
)
from armodel.writer.arxml_writer import ARXMLWriter


class _Derived(AbstractVariationRestriction):
    def __init__(self):
        super().__init__()
        from typing import List

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes import FullBindingTimeEnum as _F

        self.validBindingTimes: List[_F] = []


class TestWriteAbstractVariationRestriction:
    """
    Test writeAbstractVariationRestriction.
    """

    def test_write_members(self):
        restriction = _Derived()
        restriction.setVariation(Boolean().setValue(True))
        restriction.addValidBindingTime(FullBindingTimeEnum().setValue(FullBindingTimeEnum.POST_BUILD))
        restriction.addValidBindingTime(FullBindingTimeEnum().setValue(FullBindingTimeEnum.PRE_COMPILE_TIME))

        writer = ARXMLWriter()
        element = ET.Element("RESTRICTION")
        writer.writeAbstractVariationRestriction(element, restriction)

        assert element.find("VARIATION").text == "true"
        times = element.find("VALID-BINDING-TIMES")
        values = [e.text for e in times.findall("VALID-BINDING-TIME")]
        assert values == ["POST-BUILD", "PRE-COMPILE-TIME"]

    def test_write_empty(self):
        restriction = _Derived()
        writer = ARXMLWriter()
        element = ET.Element("RESTRICTION")
        writer.writeAbstractVariationRestriction(element, restriction)

        assert len(list(element)) == 0

    def test_write_s_and_t(self):
        """writeARObject must run so the inherited S/T state is emitted (Rule 0025)."""
        restriction = _Derived()
        restriction.setChecksum(String().setValue("cs-2"))
        restriction.setTimestamp(DateTime().setValue("2023-02-02T00:00:00Z"))

        element = ET.Element("RESTRICTION")
        ARXMLWriter().writeAbstractVariationRestriction(element, restriction)

        assert element.attrib["S"] == "cs-2"
        assert element.attrib["T"] == "2023-02-02T00:00:00Z"
