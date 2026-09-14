import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Tt
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import SlParagraph
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


class TestWriteSlParagraph:
    def test_writes_value_language_and_mixed_content(self, writer):
        paragraph = SlParagraph().setL("en").setValue("text")
        paragraph.setTt(Tt().setValue(String().setValue("term")))
        parent = ET.Element("ROOT")

        writer.writeSlParagraph(parent, paragraph)

        element = parent.find("SL-PARAGRAPH")
        assert element is not None
        assert element.attrib["L"] == "en"
        assert element.text == "text"
        assert element.find("TT").text == "term"

    def test_writes_empty_optional_content(self, writer):
        parent = ET.Element("ROOT")

        writer.writeSlParagraph(parent, SlParagraph())

        element = parent.find("SL-PARAGRAPH")
        assert element is not None
        assert "L" not in element.attrib
        assert len(element) == 0

    def test_writes_footnote(self, writer):
        paragraph = SlParagraph().setValue("text")
        paragraph.setFt(SlParagraph().setValue("footnote"))
        parent = ET.Element("ROOT")

        writer.writeSlParagraph(parent, paragraph)

        element = parent.find("SL-PARAGRAPH")
        assert element.find("FT").text == "footnote"
