"""Parser tests for GeneralAnnotation (AUTOSAR_CP_TPS_SoftwareComponentTemplate, Table 4.56, p.163).

XML element order per XSD group GENERAL-ANNOTATION (AUTOSAR_00052.xsd l.63742):
LABEL, ANNOTATION-ORIGIN, ANNOTATION-TEXT (xml.sequenceOffset=20/30/40).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _annotation_element(inner):
    xml = "<ANNOTATION xmlns='%s'>%s</ANNOTATION>" % (NS, inner)
    return ET.fromstring(xml)


class TestReadGeneralAnnotation:
    def test_read_all_fields(self):
        element = _annotation_element(
            "<LABEL><L-4 L='en'>Headline</L-4></LABEL>" "<ANNOTATION-ORIGIN>manual</ANNOTATION-ORIGIN>" "<ANNOTATION-TEXT><P><L-1 L='en'>note text</L-1></P></ANNOTATION-TEXT>"
        )
        annotation = Annotation()
        ARXMLParser().readGeneralAnnotation(element, annotation)

        assert isinstance(annotation.getAnnotationOrigin(), String)
        assert annotation.getAnnotationOrigin().getValue() == "manual"
        assert annotation.getLabel() is not None
        assert annotation.getLabel().getL4s()[0].getValue() == "Headline"
        assert annotation.getAnnotationText() is not None
        assert annotation.getAnnotationText().getPs()[0].getL1s()[0].getValue() == "note text"

    def test_read_empty_annotation_yields_none_members(self):
        element = _annotation_element("")
        annotation = Annotation()
        ARXMLParser().readGeneralAnnotation(element, annotation)

        assert annotation.getAnnotationOrigin() is None
        assert annotation.getAnnotationText() is None
        assert annotation.getLabel() is None
