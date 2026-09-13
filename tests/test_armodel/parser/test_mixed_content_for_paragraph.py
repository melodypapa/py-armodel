"""Reader tests for MixedContentForParagraph."""

from xml.etree import ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestMixedContentForParagraphParser:
    def test_read_mixed_content_for_paragraph(self):
        class ConcreteContent:
            def setBr(self, value):
                self.br = value

            def setE(self, value):
                self.e = value

            def setFt(self, value):
                self.ft = value

            def setIe(self, value):
                self.ie = value

            def setStd(self, value):
                self.std = value

            def setSub(self, value):
                self.sub = value

            def setSup(self, value):
                self.sup = value

            def setTraceRef(self, value):
                self.traceRef = value

            def setTt(self, value):
                self.tt = value

            def setXdoc(self, value):
                self.xdoc = value

            def setXfile(self, value):
                self.xfile = value

            def setXref(self, value):
                self.xref = value

            def setXrefTarget(self, value):
                self.xrefTarget = value

        content = ConcreteContent()
        element = ET.fromstring('<P xmlns="http://autosar.org/schema/r4.0"><BR/><TT>term</TT></P>')

        ARXMLParser().readMixedContentForParagraph(element, content)

        assert content.br is not None
        assert content.tt.getValue().getValue() == "term"
