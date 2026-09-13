import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Tt
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


class TestWriteLParagraph:
    def test_writes_value_language_and_mixed_content(self, writer):
        mlp = MultiLanguageParagraph()
        l1 = LParagraph().setValue("text").setL("en")
        l1.setTt(Tt().setValue(String().setValue("term")))
        mlp.addL1(l1)
        parent = ET.Element("P")

        writer.writeLParagraphs(parent, mlp)

        element = parent.find("L-1")
        assert element is not None
        assert element.attrib["L"] == "en"
        assert element.text == "text"
        assert element.find("TT").text == "term"

    def test_writes_empty_optional_content(self, writer):
        mlp = MultiLanguageParagraph()
        mlp.addL1(LParagraph())
        parent = ET.Element("P")

        writer.writeLParagraphs(parent, mlp)

        element = parent.find("L-1")
        assert element is not None
        assert "L" not in element.attrib
        assert len(element) == 0

    def test_writes_footnote(self, writer):
        mlp = MultiLanguageParagraph()
        l1 = LParagraph().setValue("text")
        l1.setFt(LParagraph().setValue("footnote"))
        mlp.addL1(l1)
        parent = ET.Element("P")

        writer.writeLParagraphs(parent, mlp)

        element = parent.find("L-1")
        assert element.find("FT").text == "footnote"
