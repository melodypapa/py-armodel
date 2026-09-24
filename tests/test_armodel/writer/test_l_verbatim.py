"""Writer tests for the LVerbatim class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.89)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LVerbatim
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageVerbatim
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_l_verbatim() -> LVerbatim:
    l5 = LVerbatim()
    l5.setL("EN")
    l5.setValue("verbatim text")
    return l5


class TestLVerbatimWriter:
    def test_write_l5_writes_l_attrib_and_text(self):
        """The l5 aggregation must serialize as the L-5 element with the L XML attribute and the text content (XSD 00052 L-VERBATIM, mixed=true)."""
        element = ET.Element("MULTI-LANGUAGE-VERBATIM")

        ARXMLWriter().setMultiLanguageVerbatim(element, "MULTI-LANGUAGE-VERBATIM", MultiLanguageVerbatim().addL5(_build_l_verbatim()))

        written = element.find("MULTI-LANGUAGE-VERBATIM/L-5")
        assert written is not None
        assert written.attrib["L"] == "EN"
        assert written.text == "verbatim text"

    def test_write_l5_without_l_omits_attrib(self):
        element = ET.Element("MULTI-LANGUAGE-VERBATIM")
        l5 = LVerbatim()
        l5.setValue("no language")

        ARXMLWriter().setMultiLanguageVerbatim(element, "MULTI-LANGUAGE-VERBATIM", MultiLanguageVerbatim().addL5(l5))

        written = element.find("MULTI-LANGUAGE-VERBATIM/L-5")
        assert written is not None
        assert "L" not in written.attrib
        assert written.text == "no language"

    def test_write_empty_wrapper_has_no_l5_children(self):
        element = ET.Element("ROOT")

        ARXMLWriter().setMultiLanguageVerbatim(element, "MULTI-LANGUAGE-VERBATIM", MultiLanguageVerbatim())

        written = element.find("MULTI-LANGUAGE-VERBATIM")
        assert written is not None
        assert written.find("L-5") is None

    def test_l_verbatim_write_read_roundtrip(self):
        writer_element = ET.Element("ROOT")
        ARXMLWriter().setMultiLanguageVerbatim(writer_element, "MULTI-LANGUAGE-VERBATIM", MultiLanguageVerbatim().addL5(_build_l_verbatim()))
        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(writer_element, encoding="unicode"))

        result = ARXMLParser().getMultiLanguageVerbatim(parsed, "MULTI-LANGUAGE-VERBATIM")

        assert result is not None
        l5 = result.getL5s()[0]
        assert isinstance(l5, LVerbatim)
        assert l5.getL() == "EN"
        assert l5.getValue() == "verbatim text"
