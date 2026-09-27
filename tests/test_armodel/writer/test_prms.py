"""Writer tests for the Prms/GeneralParameter/PrmChar family (Table 9.74 + XSD-only members)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, String
from armodel.models.M2.MSR.AsamHdo.Units import SingleLanguageUnitNames
from armodel.models.M2.MSR.Documentation.BlockElements.GerneralParameters import (
    GeneralParameter,
    PrmChar,
    PrmCharAbsTol,
    PrmCharMinTypMax,
    PrmCharNumericalContents,
    PrmCharTextualContents,
    Prms,
)
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import ChapterEnumBreak
from armodel.models.M2.MSR.Documentation.Chapters import ChapterContent
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_full_prms() -> Prms:
    prms = Prms().setBreak(ChapterEnumBreak().setValue("break"))
    label = MultilanguageLongName()
    l4 = LLongName()
    l4.setL("EN")
    l4.setValue("parameter table")
    label.addL4(l4)
    prms.setLabel(label)

    char = PrmChar()
    cond = DocumentationBlock()
    char.setCond(cond)
    char.setRemark(DocumentationBlock())
    numerical = PrmCharNumericalContents()
    abs_tol = PrmCharAbsTol()
    abs_tol.setAbs(Numerical().setValue("50"))
    abs_tol.setTol(Numerical().setValue("0.5"))
    numerical.setAbsTol(abs_tol)
    char.setNumericalContents(numerical)

    prm = GeneralParameter(prms, "p1")
    prm.addPrmChar(char)
    prms.addPrm(prm)
    prms.addPrm(GeneralParameter(prms, "p2"))
    return prms


class TestPrmsWriter:
    def test_write_prms_element_structure(self):
        """The parameter table serializes as <PRMS> with XSD order LABEL → PRM and the numerical choice inlined."""
        writer = ARXMLWriter()
        element = ET.Element("CHAPTER-CONTENT")
        writer.writePrms(element, _build_full_prms())

        prms_element = element.find("PRMS")
        assert prms_element is not None
        assert prms_element.attrib["BREAK"] == "break"
        assert [child.tag for child in prms_element][:2] == ["LABEL", "PRM"]
        assert prms_element.find("LABEL/L-4").text == "parameter table"
        prm_elements = prms_element.findall("PRM")
        assert len(prm_elements) == 2
        char_element = prm_elements[0].find("PRM-CHAR")
        assert char_element is not None
        assert [child.tag for child in char_element] == ["COND", "ABS", "TOL", "REMARK"]
        assert char_element.find("ABS").text == "50"
        assert char_element.find("TOL").text == "0.5"
        assert prm_elements[1].find("PRM-CHAR") is None

    def test_write_min_typ_max_and_textual(self):
        """The MIN/TYP/MAX alternative plus PRM-UNIT and the textual TEXT alternative serialize in group order."""
        writer = ARXMLWriter()
        element = ET.Element("CHAPTER-CONTENT")

        numerical = PrmCharNumericalContents()
        mtm = PrmCharMinTypMax()
        mtm.setMin(Numerical().setValue("1"))
        mtm.setTyp(Numerical().setValue("2"))
        mtm.setMax(Numerical().setValue("3"))
        numerical.setMinTypMax(mtm)
        numerical.setPrmUnit(SingleLanguageUnitNames().setMixedString("nm"))
        char = PrmChar().setNumericalContents(numerical)
        prm = GeneralParameter(None, "p1").addPrmChar(char)
        writer.writePrms(element, Prms().addPrm(prm))

        char_element = element.find("PRMS/PRM/PRM-CHAR")
        assert [child.tag for child in char_element] == ["MIN", "TYP", "MAX", "PRM-UNIT"]
        assert char_element.find("PRM-UNIT").text == "nm"

        textual_char = PrmChar().setTextualContents(PrmCharTextualContents().setText(String().setValue("revision A")))
        textual_prm = GeneralParameter(None, "p2").addPrmChar(textual_char)
        writer.writePrms(element, Prms().addPrm(textual_prm))
        textual_element = element.findall("PRMS")[1].find("PRM/PRM-CHAR")
        assert [child.tag for child in textual_element] == ["TEXT"]
        assert textual_element.find("TEXT").text == "revision A"

    def test_write_minimal_omits_empty_children(self):
        """An empty parameter table serializes a bare <PRMS> element (no LABEL, no PRM)."""
        writer = ARXMLWriter()
        element = ET.Element("CHAPTER-CONTENT")
        writer.writePrms(element, Prms())

        prms_element = element.find("PRMS")
        assert prms_element is not None
        assert len(list(prms_element)) == 0

    def test_round_trip_through_chapter_content(self):
        """Write → parse round-trip preserves the parameter table through CHAPTER-CONTENT."""
        writer = ARXMLWriter()
        chapter_content = ChapterContent().setPrms(_build_full_prms())
        element = ET.Element("CHAPTER-MODEL")
        writer.writeChapterContent(element, chapter_content)
        element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(element, encoding="unicode"))
        content_element = parsed[0]

        parser = ARXMLParser()
        result = parser.readChapterContent(content_element, None)

        prms = result.getPrms()
        assert prms is not None
        assert prms.getBreak().getValue() == "break"
        assert prms.getLabel().getL4s()[0].getValue() == "parameter table"
        prm = prms.getPrms()[0]
        assert prm.getShortName() == "p1"
        numerical = prm.getPrmChars()[0].getNumericalContents()
        assert numerical.getAbsTol().getAbs().getValue() == 50
        assert numerical.getAbsTol().getTol().getValue() == 0.5
