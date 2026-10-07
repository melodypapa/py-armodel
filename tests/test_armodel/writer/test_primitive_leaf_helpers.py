"""
Writer tests: ARLiteral primitives are emitted through the typed leaf helpers
setChildElementOptional<Cls> (Rule 0013.2), carrying the inherited T timestamp.

Reader counterpart: tests/test_armodel/parser/test_primitive_leaf_helpers.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
)
from armodel.writer.arxml_writer import ARXMLWriter


class TestCategoryStringLeaf:
    def test_writes_concrete_type_and_t(self):
        value = CategoryString()
        value.setValue("SW-COMPONENT-TYPE")
        value.timestamp = "2023-05-05T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalCategoryString(element, "CATEGORY", value)

        written = element.find("CATEGORY")
        assert written is not None
        assert written.text == "SW-COMPONENT-TYPE"
        assert written.attrib["T"] == "2023-05-05T00:00:00Z"

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalCategoryString(element, "CATEGORY", None)

        assert element.find("CATEGORY") is None
