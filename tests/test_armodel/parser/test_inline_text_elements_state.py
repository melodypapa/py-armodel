"""
Reader tests for the inline text elements' inherited AR:AR-OBJECT state (S/T).

Rule 0025: readEmphasisText / readIndexEntry / readTt must call readARObject so
the inherited level round-trips.

Writer counterpart: tests/test_armodel/writer/test_inline_text_elements_state.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    EmphasisText,
    IndexEntry,
    Tt,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestEmphasisTextState:
    def test_read_emphasistext_reads_s_and_t(self):
        element = ET.fromstring(f"""<E xmlns='{NS}' S="checksum-1" T="2023-01-01T00:00:00Z">text</E>""")

        emphasis = ARXMLParser().readEmphasisText(element)

        assert isinstance(emphasis, EmphasisText)
        assert emphasis.getChecksum() is not None
        assert emphasis.getChecksum().getValue() == "checksum-1"
        assert emphasis.getTimestamp() is not None
        assert emphasis.getTimestamp().getValue() == "2023-01-01T00:00:00Z"

    def test_read_emphasistext_without_s_and_t(self):
        element = ET.fromstring(f"""<E xmlns='{NS}'>text</E>""")

        emphasis = ARXMLParser().readEmphasisText(element)

        assert emphasis.getChecksum() is None
        assert emphasis.getTimestamp() is None


class TestIndexEntryState:
    def test_read_indexentry_reads_s_and_t(self):
        element = ET.fromstring(f"""<IE xmlns='{NS}' S="checksum-2" T="2023-02-02T00:00:00Z">text</IE>""")

        index_entry = ARXMLParser().readIndexEntry(element)

        assert isinstance(index_entry, IndexEntry)
        assert index_entry.getChecksum() is not None
        assert index_entry.getChecksum().getValue() == "checksum-2"
        assert index_entry.getTimestamp() is not None
        assert index_entry.getTimestamp().getValue() == "2023-02-02T00:00:00Z"

    def test_read_indexentry_without_s_and_t(self):
        element = ET.fromstring(f"""<IE xmlns='{NS}'>text</IE>""")

        index_entry = ARXMLParser().readIndexEntry(element)

        assert index_entry.getChecksum() is None
        assert index_entry.getTimestamp() is None
