"""Writer tests for MixedContentForParagraph."""

from xml.etree import ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Br, Std, Tt, Xdoc
from armodel.writer.arxml_writer import ARXMLWriter


class ConcreteContent:
    br = None
    std = None
    tt = None
    xdoc = None

    def getBr(self):
        return self.br

    def getE(self):
        return None

    def getFt(self):
        return None

    def getIe(self):
        return None

    def getStd(self):
        return self.std

    def getSub(self):
        return None

    def getSup(self):
        return None

    def getTraceRef(self):
        return None

    def getTt(self):
        return self.tt

    def getXdoc(self):
        return self.xdoc

    def getXfile(self):
        return None

    def getXref(self):
        return None

    def getXrefTarget(self):
        return None


class TestMixedContentForParagraphWriter:
    def test_write_mixed_content_for_paragraph(self):
        content = ConcreteContent()
        content.br = Br()
        content.tt = Tt().setValue(String().setValue("term"))
        parent = ET.Element("P")

        ARXMLWriter().writeMixedContentForParagraph(parent, content)

        assert parent.find("BR") is not None
        assert parent.find("TT").text == "term"

    def test_write_mixed_content_for_paragraph_std_and_xdoc_child_elements(self):
        content = ConcreteContent()
        content.std = Std(None, "STD").setSubtitle(String().setValue("standard")).setState(String().setValue("final")).setDate(DateTime().setValue("2026-09-12"))
        content.xdoc = Xdoc(None, "XDOC").setNumber(String().setValue("DOC-1")).setPublisher(String().setValue("Publisher"))
        parent = ET.Element("P")

        ARXMLWriter().writeMixedContentForParagraph(parent, content)

        written_std = parent.find("STD")
        assert written_std.attrib == {}
        assert written_std.find("SUBTITLE").text == "standard"
        assert written_std.find("STATE").text == "final"
        assert written_std.find("DATE").text == "2026-09-12"
        written_xdoc = parent.find("XDOC")
        assert written_xdoc.attrib == {}
        assert written_xdoc.find("NUMBER").text == "DOC-1"
        assert written_xdoc.find("PUBLISHER").text == "Publisher"
