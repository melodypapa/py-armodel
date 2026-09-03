"""
Regression tests for AtpStructureElement (Table 5.5) reader/writer coverage.

AtpStructureElement is abstract and Table 5.5 lists no Attribute rows; the XSD
group ATP-STRUCTURE-ELEMENT (AUTOSAR_00052.xsd l.7606) is an empty
`<xsd:sequence/>`. The class therefore owns no XML element of its own and has no
dedicated readAtpStructureElement/writeAtpStructureElement — inherited members
are reached through the shared readIdentifiable/writeIdentifiable helpers.
Steps 5/6 are N/A; these tests pin that N/A contract and cover the heritage
regression (the class re-parented AtpBlueprintable -> (AtpClassifier,
AtpFeature), so every inherited member now arrives through AtpClassifier ->
AtpFeature -> Identifiable).
"""

import logging
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class ConcreteAtpStructureElement(AtpStructureElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    writer.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    return writer


def _make_parser() -> ARXMLParser:
    return ARXMLParser(options={"warning": True})


def _populated() -> ConcreteAtpStructureElement:
    AUTOSAR.getInstance().new()
    parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    obj = ConcreteAtpStructureElement(parent, "MyStructureElement")
    obj.setCategory("TestCategory")
    obj.setUuid(String().setValue("DCE:2fac1234-31f8-11b4-a222-08002b34c003"))
    return obj


class TestAtpStructureElementReaderWriter:
    """Confirm AtpStructureElement has no own XML element mapping."""

    def test_no_dedicated_reader_writer_methods(self):
        assert not hasattr(ARXMLParser, "readAtpStructureElement")
        assert not hasattr(ARXMLWriter, "writeAtpStructureElement")

    def test_round_trip_inherited_members_through_new_mro(self):
        """
        Table 5.5 re-parents the class to (AtpClassifier, AtpFeature); the
        Identifiable members must still round-trip through that chain.
        """
        writer = _make_writer()
        element = ET.Element("AR-ELEMENT")
        element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"

        src = _populated()
        assert src.getAtpFeatures() == []
        writer.writeIdentifiable(element, src)

        reparsed = ET.fromstring(ET.tostring(element))
        dst = ConcreteAtpStructureElement(AUTOSAR.getInstance().getARPackages()[0], "MyStructureElement")
        _make_parser().readIdentifiable(reparsed, dst)

        assert dst.getUuid().getValue() == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        assert dst.getCategory().getValue() == "TestCategory"
        assert dst.getAtpFeatures() == []
