"""Writer tests for IndentSample (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.13).

The writer entry point setIndentSample must emit ITEM-LABEL-POS as an attribute and the
L-2 list in the XSD INDENT-SAMPLE sequence (sequenceOffset 20), and the document-level
round-trip must preserve the concrete IndentSample type and every field value with XSD
validation ON.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.MSR.Documentation.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import IndentSample, ItemLabelPosEnum, LabeledList
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _parent():
    return ET.Element("LABELED-LIST")


class TestIndentSampleWriter:
    def test_write_emits_children_in_xsd_order(self):
        """ITEM-LABEL-POS is an attribute; the L-2 elements emit in XSD order (sequenceOffset 20)."""
        indent_sample = _build_indent_sample("NEWLINE", ["sample1", "sample2"])

        parent = _parent()
        ARXMLWriter().setIndentSample(parent, indent_sample)

        element = parent[0]
        assert element.tag == "INDENT-SAMPLE"
        assert element.attrib["ITEM-LABEL-POS"] == "NEWLINE"
        assert [child.tag for child in element] == ["L-2", "L-2"]
        assert [child.text for child in element] == ["sample1", "sample2"]

    def test_write_empty_indent_sample_emits_bare_element(self):
        """An empty IndentSample emits a bare <INDENT-SAMPLE/> (both members are optional)."""
        parent = _parent()
        ARXMLWriter().setIndentSample(parent, IndentSample())

        assert len(parent) == 1
        assert parent[0].tag == "INDENT-SAMPLE"
        assert len(parent[0]) == 0
        assert parent[0].attrib == {}

    def test_write_read_round_trip(self):
        """save → reload preserves the concrete IndentSample type and every field value (XSD validation ON)."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")

        labeled_list = LabeledList()
        labeled_list.setIndentSample(_build_indent_sample("NO-NEWLINE", ["sample1", "sample2"]))

        intro = DocumentationBlock()
        intro.setLabeledList(labeled_list)
        swc.setIntroduction(intro)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            reparsed = swc_2.getIntroduction().getLabeledList().getIndentSample()

            assert isinstance(reparsed, IndentSample)
            assert reparsed.getItemLabelPos().getValue() == "NO-NEWLINE"
            assert [l2.getValue() for l2 in reparsed.getL2s()] == ["sample1", "sample2"]
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


def _build_indent_sample(item_label_pos, samples):
    indent_sample = IndentSample()
    indent_sample.setItemLabelPos(ItemLabelPosEnum().setValue(item_label_pos))
    for sample in samples:
        l2 = LOverviewParagraph()
        l2.setL("EN")
        l2.setValue(sample)
        indent_sample.addL2(l2)
    return indent_sample
