import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements import Tgroup
from armodel.parser.arxml_parser import ARXMLParser


class TestTgroup:
    def test_read_tgroup(self):
        element = ET.fromstring(
            '<TGROUP xmlns="http://autosar.org/schema/r4.0" S="checksum" T="timestamp" ALIGN="CENTER" COLS="2" COLSEP="1" ROWSEP="0">'
            '<COLSPEC COLNUM="1" />'
            "<THEAD><ROW /></THEAD>"
            "<TFOOT><ROW /></TFOOT>"
            "<TBODY><ROW /></TBODY>"
            "</TGROUP>"
        )
        tgroup = Tgroup()

        ARXMLParser().readTgroup(element, tgroup)

        assert tgroup.getChecksum().getValue() == "checksum"
        assert tgroup.getTimestamp().getValue() == "timestamp"
        assert tgroup.getAlign().getValue() == "CENTER"
        assert tgroup.getCols().getValue() == 2
        assert tgroup.getColsep().getValue() == "1"
        assert tgroup.getRowsep().getValue() == "0"
        assert len(tgroup.getColspecs()) == 1
        assert len(tgroup.getThead().getRows()) == 1
        assert len(tgroup.getTfoot().getRows()) == 1
        assert len(tgroup.getTbody().getRows()) == 1

    def test_read_tgroup_without_optional_content(self):
        tgroup = Tgroup()

        ARXMLParser().readTgroup(ET.fromstring('<TGROUP xmlns="http://autosar.org/schema/r4.0" COLS="1" />'), tgroup)

        assert tgroup.getColspecs() == []
        assert tgroup.getThead() is None
        assert tgroup.getTfoot() is None
        assert tgroup.getTbody() is None
