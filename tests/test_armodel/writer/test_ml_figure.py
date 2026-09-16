"""Writer tests for the MlFigure class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.24)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, String
from armodel.models.M2.MSR.Documentation.BlockElements import Caption
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import Graphic, LGraphic, MlFigure
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import FrameEnum, PgwideEnum
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import ChapterEnumBreak, KeepWithPreviousEnum
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LVerbatim
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageVerbatim
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_full_ml_figure() -> MlFigure:
    figure = MlFigure()
    figure.setSi(NameToken().setValue("si-tokens"))
    figure.setView(NameToken().setValue("view-tokens"))
    figure.setBreak(ChapterEnumBreak().setValue(ChapterEnumBreak.BREAK))
    figure.setKeepWithPrevious(KeepWithPreviousEnum().setValue(KeepWithPreviousEnum.KEEP))
    figure.setFrame(FrameEnum().setValue(FrameEnum.ALL))
    figure.setHelpEntry(String().setValue("help-topic"))
    figure.setPgwide(PgwideEnum().setValue(PgwideEnum.PGWIDE))
    caption = Caption(None, "cap")
    figure.setFigureCaption(caption)
    l_graphic = LGraphic()
    l_graphic.setL("en")
    graphic = Graphic()
    graphic.setFilename(NameToken().setValue("image.png"))
    l_graphic.setGraphic(graphic)
    figure.addLGraphics(l_graphic)
    verbatim = MultiLanguageVerbatim()
    verbatim.setAllowBreak(NameToken().setValue("1"))
    l5 = LVerbatim()
    l5.setL("en")
    l5.setValue("keep  spacing")
    verbatim.addL5(l5)
    figure.setVerbatim(verbatim)
    return figure


class TestMlFigureWriter:
    def test_set_ml_figures_writes_members_in_xsd_order(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setMlFigures(element, "FIGURE", [_build_full_ml_figure()])

        written = element.find("FIGURE")
        assert written is not None
        assert written.attrib["SI"] == "si-tokens"
        assert written.attrib["VIEW"] == "view-tokens"
        assert written.attrib["BREAK"] == "BREAK"
        assert written.attrib["KEEP-WITH-PREVIOUS"] == "KEEP"
        assert written.attrib["FRAME"] == "ALL"
        assert written.attrib["HELP-ENTRY"] == "help-topic"
        assert written.attrib["PGWIDE"] == "pgwide"
        # XSD ML-FIGURE group order: FIGURE-CAPTION, L-GRAPHIC, VERBATIM
        assert list(child.tag for child in written) == ["FIGURE-CAPTION", "L-GRAPHIC", "VERBATIM"]
        caption_el = written.find("FIGURE-CAPTION")
        assert caption_el.find("SHORT-NAME").text == "cap"
        l_graphic_el = written.find("L-GRAPHIC")
        assert l_graphic_el.attrib["L"] == "en"
        assert l_graphic_el.find("GRAPHIC").attrib["FILENAME"] == "image.png"
        verbatim_el = written.find("VERBATIM")
        assert verbatim_el.attrib["ALLOWBREAK"] == "1"

    def test_set_ml_figures_empty_omits_members(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setMlFigures(element, "FIGURE", [MlFigure()])

        written = element.find("FIGURE")
        assert written is not None
        assert written.attrib == {}
        assert len(list(written)) == 0

    def test_ml_figure_write_read_roundtrip(self):
        writer_element = ET.Element("PARENT")
        ARXMLWriter().setMlFigures(writer_element, "FIGURE", [_build_full_ml_figure()])

        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        xml_bytes = ET.tostring(writer_element, encoding="unicode")
        parsed = ET.fromstring(xml_bytes)

        figure = ARXMLParser().getMlFigures(parsed, "FIGURE")[0]

        assert figure.getFrame().getValue() == "ALL"
        assert figure.getHelpEntry().getValue() == "help-topic"
        assert figure.getPgwide().getValue() == "pgwide"
        assert figure.getBreak().getValue() == "BREAK"
        assert figure.getKeepWithPrevious().getValue() == "KEEP"
        assert figure.getSi().getValue() == "si-tokens"
        assert figure.getView().getValue() == "view-tokens"
        assert figure.getFigureCaption().getShortName() == "cap"
        assert figure.getLGraphics()[0].getGraphic().getFilename().getValue() == "image.png"
        assert figure.getVerbatim().getAllowBreak().getValue() == "1"
        assert figure.getVerbatim().getL5s()[0].getValue() == "keep  spacing"
