"""Writer round-trip tests for GeneralAnnotation (AUTOSAR_CP_TPS_SoftwareComponentTemplate, Table 4.56, p.163).

XML element order per XSD group GENERAL-ANNOTATION (AUTOSAR_00052.xsd l.63742):
LABEL, ANNOTATION-ORIGIN, ANNOTATION-TEXT (xml.sequenceOffset=20/30/40).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LEnum, LLongName, LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName, MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _literal(value):
    literal = String()
    literal.setValue(value)
    return literal


def _new_annotation():
    annotation = Annotation()

    label = MultilanguageLongName()
    l4 = LLongName()
    l4.setL(LEnum.EN)
    l4.setValue("Headline")
    label.addL4(l4)
    annotation.setLabel(label)

    annotation.setAnnotationOrigin(_literal("manual"))

    block = DocumentationBlock()
    paragraph = MultiLanguageParagraph()
    l1 = LParagraph()
    l1.setL(LEnum.EN)
    l1.setValue("note text")
    paragraph.addL1(l1)
    block.addP(paragraph)
    annotation.setAnnotationText(block)
    return annotation


class TestWriteGeneralAnnotation:
    def test_write_all_fields(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeGeneralAnnotation(parent, _new_annotation())
        assert [child.tag for child in parent] == ["LABEL", "ANNOTATION-ORIGIN", "ANNOTATION-TEXT"]
        assert parent.find("ANNOTATION-ORIGIN").text == "manual"
        assert parent.find("ANNOTATION-TEXT/P/L-1").text == "note text"

    def test_write_empty_annotation_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeGeneralAnnotation(parent, Annotation())
        assert len(list(parent)) == 0

    def test_round_trip_preserves_all_values(self):
        annotation = _new_annotation()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeGeneralAnnotation(parent, annotation)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

        parsed = Annotation()
        ARXMLParser().readGeneralAnnotation(root[0], parsed)

        assert [child.tag.split("}")[-1] for child in root[0]] == ["LABEL", "ANNOTATION-ORIGIN", "ANNOTATION-TEXT"]
        assert parsed.getLabel() is not None
        assert parsed.getLabel().getL4s()[0].getValue() == "Headline"
        assert parsed.getAnnotationOrigin().getValue() == "manual"
        assert parsed.getAnnotationText() is not None
        assert parsed.getAnnotationText().getPs()[0].getL1s()[0].getValue() == "note text"
