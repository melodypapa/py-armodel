"""Writer tests for MsrQueryProps (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.85)."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryArg, MsrQueryProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_full_props() -> MsrQueryProps:
    props = MsrQueryProps().setMsrQueryName(String().setValue("MyQuery")).setComment(String().setValue("a comment"))
    props.addMsrQueryArg(MsrQueryArg().setSi(String().setValue("a1")).setArg(String().setValue("v1")))
    props.addMsrQueryArg(MsrQueryArg().setSi(String().setValue("a2")).setArg(String().setValue("v2")))
    return props


def _parse(element: ET.Element) -> MsrQueryProps:
    written = element.find("MSR-QUERY-PROPS")
    assert written is not None
    written.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
    return ARXMLParser().getMsrQueryProps(ET.fromstring(ET.tostring(written, encoding="unicode")))


class TestMsrQueryPropsWriter:
    def test_write_msr_query_props_writes_members_in_xsd_order(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setMsrQueryProps(element, _build_full_props())

        written = element.find("MSR-QUERY-PROPS")
        assert written is not None
        assert [child.tag for child in written] == ["MSR-QUERY-NAME", "MSR-QUERY-ARG", "MSR-QUERY-ARG", "COMMENT"]

    def test_write_msr_query_props_none_emits_nothing(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setMsrQueryProps(element, None)

        assert list(element) == []

    def test_write_msr_query_props_empty_omits_optional_children(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setMsrQueryProps(element, MsrQueryProps())

        written = element.find("MSR-QUERY-PROPS")
        assert written is not None
        assert list(written) == []

    def test_msr_query_props_write_read_roundtrip(self):
        element = ET.Element("PARENT")
        ARXMLWriter().setMsrQueryProps(element, _build_full_props())

        result = _parse(element)

        assert result.getMsrQueryName().getValue() == "MyQuery"
        assert result.getComment().getValue() == "a comment"
        assert [(arg.getSi().getValue(), arg.getArg().getValue()) for arg in result.getMsrQueryArgs()] == [("a1", "v1"), ("a2", "v2")]

    def test_incoming_wire_order_is_read(self):
        element = ET.fromstring(
            """<MSR-QUERY-PROPS xmlns="http://autosar.org/schema/r4.0">
<MSR-QUERY-NAME>MyQuery</MSR-QUERY-NAME>
<MSR-QUERY-ARG SI="a1"><ARG>v1</ARG></MSR-QUERY-ARG>
<MSR-QUERY-ARG SI="a2"><ARG>v2</ARG></MSR-QUERY-ARG>
<COMMENT>a comment</COMMENT></MSR-QUERY-PROPS>"""
        )

        result = ARXMLParser().getMsrQueryProps(element)

        assert result.getMsrQueryName().getValue() == "MyQuery"
        assert result.getComment().getValue() == "a comment"
        assert [arg.getArg().getValue() for arg in result.getMsrQueryArgs()] == ["v1", "v2"]
