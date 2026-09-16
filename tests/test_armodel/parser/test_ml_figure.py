"""Reader tests for the MlFigure class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.24)."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser


class TestMlFigureParser:
    def test_get_ml_figures_reads_all_members(self):
        parser = ARXMLParser()
        element = ET.fromstring(
            '<PARENT xmlns="http://autosar.org/schema/r4.0">'
            '<FIGURE S="checksum" T="timestamp" SI="si-tokens" VIEW="view-tokens" BREAK="BREAK"'
            ' KEEP-WITH-PREVIOUS="KEEP" FRAME="ALL" HELP-ENTRY="help-topic" PGWIDE="pgwide">'
            "<FIGURE-CAPTION><SHORT-NAME>cap</SHORT-NAME></FIGURE-CAPTION>"
            '<L-GRAPHIC L="en"><GRAPHIC FILENAME="image.png"/></L-GRAPHIC>'
            '<VERBATIM ALLOWBREAK="1"><L-5 L="en">keep  spacing</L-5></VERBATIM>'
            "</FIGURE></PARENT>"
        )

        figures = parser.getMlFigures(element, "FIGURE")

        assert len(figures) == 1
        figure = figures[0]
        assert figure.getChecksum().getValue() == "checksum"
        assert figure.getTimestamp().getValue() == "timestamp"
        assert figure.getSi().getValue() == "si-tokens"
        assert figure.getView().getValue() == "view-tokens"
        assert figure.getBreak().getValue() == "BREAK"
        assert figure.getKeepWithPrevious().getValue() == "KEEP"
        assert figure.getFrame().getValue() == "ALL"
        assert figure.getHelpEntry().getValue() == "help-topic"
        assert figure.getPgwide().getValue() == "pgwide"
        caption = figure.getFigureCaption()
        assert caption is not None
        assert caption.getShortName() == "cap"
        l_graphics = figure.getLGraphics()
        assert len(l_graphics) == 1
        assert l_graphics[0].getL() == "en"
        assert l_graphics[0].getGraphic().getFilename().getValue() == "image.png"
        verbatim = figure.getVerbatim()
        assert verbatim is not None
        assert verbatim.getAllowBreak().getValue() == "1"
        assert len(verbatim.getL5s()) == 1
        assert verbatim.getL5s()[0].getValue() == "keep  spacing"

    def test_get_ml_figures_minimal_returns_defaults(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"><FIGURE/></PARENT>')

        figures = parser.getMlFigures(element, "FIGURE")

        assert len(figures) == 1
        figure = figures[0]
        assert figure.getFigureCaption() is None
        assert figure.getFrame() is None
        assert figure.getHelpEntry() is None
        assert figure.getLGraphics() == []
        assert figure.getPgwide() is None
        assert figure.getVerbatim() is None

    def test_get_ml_figures_missing_returns_empty(self):
        parser = ARXMLParser()
        element = ET.fromstring('<PARENT xmlns="http://autosar.org/schema/r4.0"/>')

        assert parser.getMlFigures(element, "FIGURE") == []
