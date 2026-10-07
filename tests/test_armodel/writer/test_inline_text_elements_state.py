"""
Writer tests for the inline text elements' inherited AR:AR-OBJECT state (S/T).

Rule 0025: setEmphasisText / setIndexEntry / setTt must call writeARObject so
the inherited level round-trips.

Reader counterpart: tests/test_armodel/parser/test_inline_text_elements_state.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    EmphasisText,
    IndexEntry,
    Tt,
)
from armodel.writer.arxml_writer import ARXMLWriter


class TestEmphasisTextState:
    def test_set_emphasistext_writes_s_and_t(self):
        emphasis = EmphasisText()
        emphasis.setChecksum(String().setValue("checksum-1"))
        emphasis.setTimestamp(DateTime().setValue("2023-01-01T00:00:00Z"))

        element = ET.Element("ROOT")
        ARXMLWriter().setEmphasisText(element, "E", emphasis)

        written = element.find("E")
        assert written is not None
        assert written.attrib["S"] == "checksum-1"
        assert written.attrib["T"] == "2023-01-01T00:00:00Z"

    def test_set_emphasistext_without_s_and_t(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setEmphasisText(element, "E", EmphasisText())

        written = element.find("E")
        assert written is not None
        assert "S" not in written.attrib
        assert "T" not in written.attrib


class TestIndexEntryState:
    def test_set_indexentry_writes_s_and_t(self):
        index_entry = IndexEntry()
        index_entry.setChecksum(String().setValue("checksum-2"))
        index_entry.setTimestamp(DateTime().setValue("2023-02-02T00:00:00Z"))

        element = ET.Element("ROOT")
        ARXMLWriter().setIndexEntry(element, "IE", index_entry)

        written = element.find("IE")
        assert written is not None
        assert written.attrib["S"] == "checksum-2"
        assert written.attrib["T"] == "2023-02-02T00:00:00Z"

    def test_set_indexentry_without_s_and_t(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setIndexEntry(element, "IE", IndexEntry())

        written = element.find("IE")
        assert written is not None
        assert "S" not in written.attrib
        assert "T" not in written.attrib


class TestTtState:
    def test_set_tt_writes_s_and_t(self):
        tt = Tt()
        tt.setChecksum(String().setValue("checksum-3"))
        tt.setTimestamp(DateTime().setValue("2023-03-03T00:00:00Z"))

        element = ET.Element("ROOT")
        ARXMLWriter().setTt(element, "TT", tt)

        written = element.find("TT")
        assert written is not None
        assert written.attrib["S"] == "checksum-3"
        assert written.attrib["T"] == "2023-03-03T00:00:00Z"

    def test_set_tt_without_s_and_t(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setTt(element, "TT", Tt())

        written = element.find("TT")
        assert written is not None
        assert "S" not in written.attrib
        assert "T" not in written.attrib
