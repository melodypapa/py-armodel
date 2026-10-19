"""Reader tests for IndentSample (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.13).

The reader entry point getIndentSample must populate itemLabelPos, the L-2 list and the
inherited ARObject attributes (S/T) — asserting field values and the concrete type, not
just wrapper presence.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import IndentSample, ItemLabelPosEnum
from armodel.parser.arxml_parser import ARXMLParser

NS = "{http://autosar.org/schema/r4.0}"


def _block(inner):
    return ET.fromstring('<DOCUMENTATION-BLOCK xmlns="http://autosar.org/schema/r4.0">' + inner + "</DOCUMENTATION-BLOCK>")


def _indent_sample_element(attrs="", inner=""):
    block = _block(f"<INDENT-SAMPLE {attrs}>{inner}</INDENT-SAMPLE>")
    return block.find(f".//{NS}INDENT-SAMPLE")


class TestIndentSampleParser:
    def test_read_full_indent_sample_populates_all_members(self):
        """ITEM-LABEL-POS, the L-2 list and the inherited ARObject attributes all land on the model (field values, not wrapper presence)."""
        parser = ARXMLParser()
        element = _indent_sample_element('ITEM-LABEL-POS="NEWLINE" S="CKS"', '<L-2 L="EN">sample1</L-2><L-2 L="DE">sample2</L-2>')

        indent_sample = parser.getIndentSample(element)

        assert isinstance(indent_sample, IndentSample)
        assert indent_sample.getItemLabelPos().getValue() == ItemLabelPosEnum.NEWLINE
        assert indent_sample.getChecksum().getValue() == "CKS"
        assert [l2.getValue() for l2 in indent_sample.getL2s()] == ["sample1", "sample2"]

    def test_read_empty_indent_sample_leaves_optional_members_unset(self):
        """An empty <INDENT-SAMPLE/> reads with itemLabelPos unset and an empty L-2 list (both are minOccurs=0 in the XSD)."""
        parser = ARXMLParser()

        indent_sample = parser.getIndentSample(_indent_sample_element())

        assert isinstance(indent_sample, IndentSample)
        assert indent_sample.getItemLabelPos() is None
        assert indent_sample.getL2s() == []

    def test_read_indent_sample_through_labeled_list(self):
        """The consumer path getLabeledList populates the INDENT-SAMPLE through getIndentSample (Rule 0001.7)."""
        parser = ARXMLParser()
        element = _block('<LABELED-LIST><INDENT-SAMPLE ITEM-LABEL-POS="NO-NEWLINE"><L-2 L="EN">sample1</L-2></INDENT-SAMPLE></LABELED-LIST>')

        indent_sample = parser.getLabeledList(element, "LABELED-LIST").getIndentSample()

        assert indent_sample.getItemLabelPos().getValue() == "NO-NEWLINE"
        assert indent_sample.getL2s()[0].getValue() == "sample1"
