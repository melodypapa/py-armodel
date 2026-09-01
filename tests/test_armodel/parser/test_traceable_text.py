"""Reader tests for TraceableText."""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import TraceableText
from armodel.parser.arxml_parser import ARXMLParser


class TestTraceableTextReader:
    def test_read_traceable_text_populates_text_and_trace_refs(self):
        element = ET.fromstring(
            "<ROOT xmlns='http://autosar.org/schema/r4.0'>"
            "<TRACE>"
            "<SHORT-NAME>REQ-1</SHORT-NAME>"
            "<TEXT><P><L-1 L='EN'>requirement text</L-1></P></TEXT>"
            "<TRACE-REFS><TRACE-REF BASE='AUTOSAR' DEST='TRACEABLE-TEXT'>/REQ/BASE</TRACE-REF></TRACE-REFS>"
            "</TRACE>"
            "</ROOT>"
        )

        traceable_text = ARXMLParser().getTraceableText(element, "TRACE")

        assert isinstance(traceable_text, TraceableText)
        assert traceable_text.getShortName() == "REQ-1"
        assert traceable_text.getText().getPs()[0].getL1s()[0].getValue() == "requirement text"
        assert traceable_text.getTraceRefs()[0].getValue() == "/REQ/BASE"
        assert traceable_text.getTraceRefs()[0].getBase() == "AUTOSAR"
        assert traceable_text.getTraceRefs()[0].getDest() == "TRACEABLE-TEXT"
