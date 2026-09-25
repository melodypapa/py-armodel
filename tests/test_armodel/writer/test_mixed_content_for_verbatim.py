"""Writer tests for MixedContentForVerbatim (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.6) via its L-5 consumer element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Br, EmphasisText, Tt, Xref
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LVerbatim
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageVerbatim
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_l5_with_mixed_content() -> LVerbatim:
    l5 = LVerbatim()
    l5.setL("EN")
    l5.setValue("verbatim text")
    l5.setBr(Br())
    l5.setE(EmphasisText().setValue(String().setValue("emphasized verbatim")))
    l5.setTt(Tt().setValue(String().setValue("technical term")))
    l5.setXref(Xref())
    return l5


class TestMixedContentForVerbatimWriter:
    def test_write_l5_writes_mixed_content_children(self):
        """The Table 9.6 members must be emitted on the L-5 element (BR/E/TT/XREF child elements) in the family display order."""
        element = ET.Element("MULTI-LANGUAGE-VERBATIM")

        ARXMLWriter().setMultiLanguageVerbatim(element, "MULTI-LANGUAGE-VERBATIM", MultiLanguageVerbatim().addL5(_build_l5_with_mixed_content()))

        written = element.find("MULTI-LANGUAGE-VERBATIM/L-5")
        assert written is not None
        assert written.attrib["L"] == "EN"
        assert [child.tag for child in written] == ["BR", "E", "TT", "XREF"]
        assert written.find("E").text == "emphasized verbatim"
        assert written.find("TT").text == "technical term"

    def test_write_l5_without_mixed_content_omits_children(self):
        element = ET.Element("MULTI-LANGUAGE-VERBATIM")
        l5 = LVerbatim()
        l5.setL("DE")
        l5.setValue("plain verbatim")

        ARXMLWriter().setMultiLanguageVerbatim(element, "MULTI-LANGUAGE-VERBATIM", MultiLanguageVerbatim().addL5(l5))

        written = element.find("MULTI-LANGUAGE-VERBATIM/L-5")
        assert written is not None
        assert len(list(written)) == 0

    def test_l5_mixed_content_roundtrip(self):
        """Document-level parse -> write -> re-parse must preserve the mixed-content field values."""
        l5 = _build_l5_with_mixed_content()

        writer_element = ET.Element("ROOT")
        ARXMLWriter().setMultiLanguageVerbatim(writer_element, "MULTI-LANGUAGE-VERBATIM", MultiLanguageVerbatim().addL5(l5))
        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(writer_element, encoding="unicode"))

        result = ARXMLParser().getMultiLanguageVerbatim(parsed, "MULTI-LANGUAGE-VERBATIM")

        assert result is not None
        reread = result.getL5s()[0]
        assert reread.getValue() == "verbatim text"
        assert isinstance(reread.getBr(), Br)
        assert reread.getE().getValue().getValue() == "emphasized verbatim"
        assert reread.getTt().getValue().getValue() == "technical term"
        assert isinstance(reread.getXref(), Xref)
