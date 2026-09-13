"""Writer tests for MixedContentForParagraph."""

from xml.etree import ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Br, Tt
from armodel.writer.arxml_writer import ARXMLWriter


class TestMixedContentForParagraphWriter:
    def test_write_mixed_content_for_paragraph(self):
        class ConcreteContent:
            def getBr(self):
                return self.br

            def getE(self):
                return None

            def getFt(self):
                return None

            def getIe(self):
                return None

            def getStd(self):
                return None

            def getSub(self):
                return None

            def getSup(self):
                return None

            def getTraceRef(self):
                return None

            def getTt(self):
                return self.tt

            def getXdoc(self):
                return None

            def getXfile(self):
                return None

            def getXref(self):
                return None

            def getXrefTarget(self):
                return None

        content = ConcreteContent()
        content.br = Br()
        content.tt = Tt().setValue(String().setValue("term"))
        parent = ET.Element("P")

        ARXMLWriter().writeMixedContentForParagraph(parent, content)

        assert parent.find("BR") is not None
        assert parent.find("TT").text == "term"
