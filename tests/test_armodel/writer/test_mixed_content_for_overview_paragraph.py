"""Writer tests for MixedContentForOverviewParagraph (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.3) via its L-2 consumer element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Br, EmphasisText, IndexEntry, Superscript, Tt, Xref, XrefTarget
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData import SlOverviewParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_l2_with_mixed_content() -> LOverviewParagraph:
    l2 = LOverviewParagraph()
    l2.setL("EN")
    l2.setValue("overview text")
    l2.setBr(Br())
    l2.setE(EmphasisText().setValue(String().setValue("emphasized overview")))
    l2.setIe(IndexEntry().setValue(String().setValue("index entry")))
    l2.setSub(Superscript().setValue("sub text"))
    l2.setSup(Superscript().setValue("sup text"))
    l2.setTt(Tt().setValue(String().setValue("technical term")))
    return l2


class TestMixedContentForOverviewParagraphWriter:
    def test_write_l2_writes_mixed_content_children(self):
        """The Table 9.3 members must be emitted on the L-2 element (BR/E/IE/TT child elements, SUB/SUP XML attributes) in the family display order."""
        element = ET.Element("MULTI-LANGUAGE-OVERVIEW-PARAGRAPH")

        ARXMLWriter().setMultiLanguageOverviewParagraph(element, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH", MultiLanguageOverviewParagraph().addL2(_build_l2_with_mixed_content()))

        written = element.find("MULTI-LANGUAGE-OVERVIEW-PARAGRAPH/L-2")
        assert written is not None
        assert written.attrib["L"] == "EN"
        assert written.attrib.get("SUB") == "sub text"
        assert written.attrib.get("SUP") == "sup text"
        assert [child.tag for child in written] == ["BR", "E", "IE", "TT"]
        assert written.find("E").text == "emphasized overview"
        assert written.find("IE").text == "index entry"
        assert written.find("TT").text == "technical term"

    def test_write_l2_without_mixed_content_omits_children(self):
        element = ET.Element("MULTI-LANGUAGE-OVERVIEW-PARAGRAPH")
        l2 = LOverviewParagraph()
        l2.setL("DE")
        l2.setValue("plain overview")

        ARXMLWriter().setMultiLanguageOverviewParagraph(element, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH", MultiLanguageOverviewParagraph().addL2(l2))

        written = element.find("MULTI-LANGUAGE-OVERVIEW-PARAGRAPH/L-2")
        assert written is not None
        assert len(list(written)) == 0
        assert "SUB" not in written.attrib
        assert "SUP" not in written.attrib

    def test_l2_mixed_content_roundtrip(self):
        """Document-level parse -> write -> re-parse must preserve the mixed-content field values."""
        l2 = _build_l2_with_mixed_content()
        l2.setXref(Xref())
        l2.setXrefTarget(XrefTarget(None, "TARGET"))
        trace_ref = RefType()
        trace_ref.setValue("traceable-obj")
        trace_ref.setDest("TRACEABLE")
        l2.setTraceRef(trace_ref)

        writer_element = ET.Element("ROOT")
        ARXMLWriter().setMultiLanguageOverviewParagraph(writer_element, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH", MultiLanguageOverviewParagraph().addL2(l2))
        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(writer_element, encoding="unicode"))

        result = ARXMLParser().getMultiLanguageOverviewParagraph(parsed, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH")

        assert result is not None
        reread = result.getL2s()[0]
        assert reread.getValue() == "overview text"
        assert isinstance(reread.getBr(), Br)
        assert reread.getE().getValue().getValue() == "emphasized overview"
        assert reread.getIe().getValue().getValue() == "index entry"
        assert reread.getSub().getValue() == "sub text"
        assert reread.getSup().getValue() == "sup text"
        assert reread.getTt().getValue().getValue() == "technical term"
        assert isinstance(reread.getXref(), Xref)
        assert isinstance(reread.getXrefTarget(), XrefTarget)
        assert reread.getTraceRef().getValue() == "traceable-obj"
        assert reread.getTraceRef().getDest() == "TRACEABLE"


class TestWriteSlOverviewParagraph:
    def test_write_l2_writes_ft_sl_overview_paragraph(self):
        """The ft member must be emitted as an FT child element (L XML attribute + text + own mixed content) right after BR, per the MCFP writer precedent and the XSD group element order."""
        footnote = SlOverviewParagraph()
        footnote.setL("DE")
        footnote.setValue("footnote text")
        footnote.setTt(Tt().setValue(String().setValue("term in footnote")))
        l2 = _build_l2_with_mixed_content()
        l2.setFt(footnote)

        element = ET.Element("MULTI-LANGUAGE-OVERVIEW-PARAGRAPH")
        ARXMLWriter().setMultiLanguageOverviewParagraph(element, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH", MultiLanguageOverviewParagraph().addL2(l2))

        written = element.find("MULTI-LANGUAGE-OVERVIEW-PARAGRAPH/L-2")
        assert written is not None
        assert [child.tag for child in written] == ["BR", "FT", "E", "IE", "TT"]
        written_ft = written.find("FT")
        assert written_ft.attrib["L"] == "DE"
        assert written_ft.text == "footnote text"
        assert written_ft.find("TT").text == "term in footnote"

    def test_write_l2_without_ft_omits_ft(self):
        l2 = _build_l2_with_mixed_content()

        element = ET.Element("MULTI-LANGUAGE-OVERVIEW-PARAGRAPH")
        ARXMLWriter().setMultiLanguageOverviewParagraph(element, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH", MultiLanguageOverviewParagraph().addL2(l2))

        written = element.find("MULTI-LANGUAGE-OVERVIEW-PARAGRAPH/L-2")
        assert written is not None
        assert written.find("FT") is None

    def test_l2_ft_roundtrip(self):
        """Document-level parse -> write -> re-parse must preserve the footnote field values."""
        footnote = SlOverviewParagraph()
        footnote.setL("DE")
        footnote.setValue("footnote text")
        footnote.setBr(Br())
        footnote.setTt(Tt().setValue(String().setValue("term in footnote")))
        l2 = _build_l2_with_mixed_content()
        l2.setFt(footnote)

        writer_element = ET.Element("ROOT")
        ARXMLWriter().setMultiLanguageOverviewParagraph(writer_element, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH", MultiLanguageOverviewParagraph().addL2(l2))
        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(writer_element, encoding="unicode"))

        result = ARXMLParser().getMultiLanguageOverviewParagraph(parsed, "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH")

        assert result is not None
        reread = result.getL2s()[0]
        assert reread.getValue() == "overview text"
        assert reread.getE().getValue().getValue() == "emphasized overview"
        reread_ft = reread.getFt()
        assert isinstance(reread_ft, SlOverviewParagraph)
        assert reread_ft.getValue() == "footnote text"
        assert reread_ft.getL() == "DE"
        assert isinstance(reread_ft.getBr(), Br)
        assert reread_ft.getTt().getValue().getValue() == "term in footnote"
