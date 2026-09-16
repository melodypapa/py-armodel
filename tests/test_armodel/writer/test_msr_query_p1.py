"""Writer tests for MsrQueryP1 (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.82)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.Chapters import TopicContent
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryP1, MsrQueryProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_full_query() -> MsrQueryP1:
    props = MsrQueryProps().setMsrQueryName(String().setValue("paragraph-query"))
    return MsrQueryP1().setMsrQueryProps(props).setMsrQueryResultP1(TopicContent())


class TestMsrQueryP1Writer:
    def test_write_msr_query_p1_writes_members_in_xsd_order(self):
        element = ET.Element("PARENT")

        ARXMLWriter().writeMsrQueryP1(element, _build_full_query())

        written = element.find("MSR-QUERY-P1")
        assert written is not None
        assert [child.tag for child in written] == ["MSR-QUERY-PROPS", "TOPIC-CONTENT"]
        assert written.find("MSR-QUERY-PROPS/MSR-QUERY-NAME").text == "paragraph-query"

    def test_write_msr_query_p1_empty_omits_optional_children(self):
        element = ET.Element("PARENT")

        ARXMLWriter().writeMsrQueryP1(element, MsrQueryP1())

        written = element.find("MSR-QUERY-P1")
        assert written is not None
        assert list(written) == []

    def test_msr_query_p1_write_read_roundtrip(self):
        writer_element = ET.Element("PARENT")
        ARXMLWriter().writeMsrQueryP1(writer_element, _build_full_query())
        writer_element.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(writer_element, encoding="unicode"))

        result = ARXMLParser().getMsrQueryP1(parsed, "MSR-QUERY-P1")

        assert result.getMsrQueryProps().getMsrQueryName().getValue() == "paragraph-query"
        assert result.getMsrQueryResultP1() is not None
