"""
Tests for round-tripping Identifiable attributes (Table 4.4) through
writeIdentifiable / readIdentifiable.
"""

import logging
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultiLanguageOverviewParagraph,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class ConcreteIdentifiable(Identifiable):
    def __init__(self):
        AUTOSAR.getInstance().new()
        parent = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        super().__init__(parent, "TestIdentifiable")


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    writer.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    return writer


def _make_parser() -> ARXMLParser:
    return ARXMLParser(options={"warning": True})


def _populated() -> ConcreteIdentifiable:
    obj = ConcreteIdentifiable()
    obj.setAdminData(AdminData())
    obj.addAnnotation(Annotation())
    obj.setCategory("TestCategory")
    obj.setDesc(MultiLanguageOverviewParagraph())
    obj.setIntroduction(DocumentationBlock())
    obj.setUuid(String().setValue("DCE:2fac1234-31f8-11b4-a222-08002b34c003"))
    return obj


class TestWriteIdentifiable:
    def test_write_identifiable_fields(self):
        writer = _make_writer()
        element = ET.Element("AR-ELEMENT")

        obj = _populated()
        writer.writeIdentifiable(element, obj)

        assert element.attrib.get("UUID") == "DCE:2fac1234-31f8-11b4-a222-08002b34c003"
        assert element.find("ADMIN-DATA") is not None
        assert element.find("ANNOTATIONS") is not None
        assert element.find("CATEGORY") is not None
        assert element.find("CATEGORY").text == "TestCategory"
        assert element.find("DESC") is not None
        assert element.find("INTRODUCTION") is not None

    def test_write_empty_optional_fields(self):
        writer = _make_writer()
        element = ET.Element("AR-ELEMENT")

        obj = ConcreteIdentifiable()
        writer.writeIdentifiable(element, obj)

        assert "UUID" not in element.attrib
        assert element.find("ADMIN-DATA") is None
        assert element.find("CATEGORY") is None
        assert element.find("DESC") is None
        assert element.find("INTRODUCTION") is None
        assert element.find("ANNOTATIONS") is None
        assert element.find("VARIATION-POINT") is None


class TestRoundTripIdentifiable:
    def test_round_trip_fields(self):
        writer = _make_writer()
        element = ET.Element("AR-ELEMENT")
        # The writer records the namespace as a literal xmlns attribute; on a real
        # parse -> write -> re-parse the parser applies it as a default namespace.
        # Mirror that here so the reader's namespaced find() locates child elements.
        element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"

        src = _populated()
        writer.writeIdentifiable(element, src)

        reparsed = ET.fromstring(ET.tostring(element))

        parser = _make_parser()
        dst = ConcreteIdentifiable()
        parser.readIdentifiable(reparsed, dst)

        assert dst.getUuid().getValue() == src.getUuid().getValue()
        assert dst.getCategory() is not None
        assert dst.getCategory().getValue() == "TestCategory"
        assert dst.getAdminData() is not None
        assert dst.getDesc() is not None
        assert dst.getIntroduction() is not None
        annotations = dst.getAnnotations()
        assert len(annotations) == 1
