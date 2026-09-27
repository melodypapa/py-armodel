"""Reader tests for the Prms/GeneralParameter/PrmChar family (Table 9.74 + XSD-only members)."""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser

NS = 'xmlns="http://autosar.org/schema/r4.0"'


class TestPrmsParser:
    def test_read_prms_full(self):
        """A full parameter table (label, two prm entries with numerical abs-tol characteristics) populates the model."""
        parser = ARXMLParser()
        element = ET.fromstring(
            f"<CHAPTER-CONTENT {NS}>"
            '<PRMS BREAK="break">'
            '<LABEL><L-4 L="EN">parameter table</L-4></LABEL>'
            "<PRM><SHORT-NAME>p1</SHORT-NAME>"
            '<PRM-CHAR><COND><P><L-1 L="EN">under condition</L-1></P></COND>'
            "<ABS>50</ABS><TOL>0.5</TOL>"
            '<REMARK><P><L-1 L="EN">remark text</L-1></P></REMARK></PRM-CHAR>'
            "</PRM>"
            "<PRM><SHORT-NAME>p2</SHORT-NAME></PRM>"
            "</PRMS>"
            "</CHAPTER-CONTENT>"
        )

        result = parser.readChapterContent(element, None)

        prms = result.getPrms()
        assert prms is not None
        assert prms.getBreak() is not None and prms.getBreak().getValue() == "break"
        assert prms.getLabel().getL4s()[0].getValue() == "parameter table"
        prms_list = prms.getPrms()
        assert len(prms_list) == 2
        assert prms_list[0].getShortName() == "p1"
        chars = prms_list[0].getPrmChars()
        assert len(chars) == 1
        numerical = chars[0].getNumericalContents()
        assert numerical is not None
        assert numerical.getAbsTol().getAbs().getValue() == 50
        assert numerical.getAbsTol().getTol().getValue() == 0.5
        assert chars[0].getCond() is not None
        assert chars[0].getRemark() is not None
        assert prms_list[1].getShortName() == "p2"
        assert prms_list[1].getPrmChars() == []

    def test_read_prms_min_typ_max(self):
        """The MIN/TYP/MAX alternative of the numerical contents choice populates minTypMax."""
        parser = ARXMLParser()
        element = ET.fromstring(
            f"<CHAPTER-CONTENT {NS}>"
            "<PRMS>"
            "<PRM><SHORT-NAME>p1</SHORT-NAME>"
            "<PRM-CHAR><MIN>1</MIN><TYP>2</TYP><MAX>3</MAX><PRM-UNIT>nm</PRM-UNIT></PRM-CHAR>"
            "</PRM>"
            "</PRMS>"
            "</CHAPTER-CONTENT>"
        )

        result = parser.readChapterContent(element, None)

        char = result.getPrms().getPrms()[0].getPrmChars()[0]
        numerical = char.getNumericalContents()
        assert numerical is not None
        assert numerical.getAbsTol() is None
        mtm = numerical.getMinTypMax()
        assert mtm is not None
        assert mtm.getMin().getValue() == 1
        assert mtm.getTyp().getValue() == 2
        assert mtm.getMax().getValue() == 3
        assert numerical.getPrmUnit().getMixedString() == "nm"

    def test_read_prms_textual(self):
        """The TEXT alternative populates textualContents (string value)."""
        parser = ARXMLParser()
        element = ET.fromstring(f"<CHAPTER-CONTENT {NS}>" "<PRMS>" "<PRM><SHORT-NAME>p1</SHORT-NAME>" "<PRM-CHAR><TEXT>revision A</TEXT></PRM-CHAR>" "</PRM>" "</PRMS>" "</CHAPTER-CONTENT>")

        result = parser.readChapterContent(element, None)

        char = result.getPrms().getPrms()[0].getPrmChars()[0]
        textual = char.getTextualContents()
        assert textual is not None
        assert textual.getText().getValue() == "revision A"
        assert char.getNumericalContents() is None

    def test_read_no_prms_leaves_field_none(self):
        """A CHAPTER-CONTENT without PRMS leaves the prms field None (empty-wrapper tolerance)."""
        parser = ARXMLParser()
        element = ET.fromstring(f"<CHAPTER-CONTENT {NS}/>")
        result = parser.readChapterContent(element, None)
        assert result.getPrms() is None
