"""Writer tests for LabeledList (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.11).

The writer entry point setLabeledList must emit INDENT-SAMPLE, the LABELED-ITEM list and
VARIATION-POINT in the XSD LABELED-LIST sequence (sequenceOffsets 20 / 30 / 10000), and
the document-level round-trip must preserve the concrete LabeledList type and every
field value with XSD validation ON.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, NameTokens, String, ViewTokens
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.MSR.Documentation.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import LabeledItem, LabeledList
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import ChapterEnumBreak, KeepWithPreviousEnum
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _parent():
    return ET.Element("DOCUMENTATION-BLOCK")


class TestLabeledListWriter:
    def test_write_emits_children_in_xsd_order(self):
        """Children emit in the XSD LABELED-LIST group order: INDENT-SAMPLE, the LABELED-ITEMs, then VARIATION-POINT (offsets 20/30/10000)."""
        labeled_list = LabeledList()
        indent_sample = _build_indent_sample()
        labeled_list.setIndentSample(indent_sample)
        labeled_list.addLabeledItem(_build_labeled_item("li1", "lbl1", "c1"))
        labeled_list.addLabeledItem(_build_labeled_item("li2", "lbl2", "c2"))
        vp = VariationPoint()
        vp.setShortLabel(Identifier().setValue("DVP"))
        labeled_list.setVariationPoint(vp)

        parent = _parent()
        ARXMLWriter().setLabeledList(parent, labeled_list)

        assert [child.tag for child in parent[0]] == ["INDENT-SAMPLE", "LABELED-ITEM", "LABELED-ITEM", "VARIATION-POINT"]
        assert parent[0][0].attrib["ITEM-LABEL-POS"] == "NEWLINE"
        assert parent[0][1].attrib["HELP-ENTRY"] == "li1"
        assert parent[0][3].find("SHORT-LABEL").text == "DVP"

    def test_write_omits_wrapper_when_none(self):
        """setLabeledList(element, None) emits nothing."""
        parent = _parent()
        ARXMLWriter().setLabeledList(parent, None)

        assert len(parent) == 0

    def test_write_empty_list_emits_wrapper_only(self):
        """An empty LabeledList emits the bare wrapper (legal per the XSD: both elements are minOccurs=0)."""
        parent = _parent()
        ARXMLWriter().setLabeledList(parent, LabeledList())

        assert len(parent) == 1
        assert parent[0].tag == "LABELED-LIST"
        assert len(parent[0]) == 0

    def test_write_read_round_trip(self):
        """save → reload preserves the concrete LabeledList type and every field value (XSD validation ON)."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")

        labeled_list = LabeledList()
        labeled_list.setSi(NameTokens().setValue("SIVAL"))
        labeled_list.setView(ViewTokens().setValue("VIEWVAL"))
        labeled_list.setBreak(ChapterEnumBreak().setValue(ChapterEnumBreak.BREAK))
        labeled_list.setKeepWithPrevious(KeepWithPreviousEnum().setValue(KeepWithPreviousEnum.KEEP))
        labeled_list.setIndentSample(_build_indent_sample())
        labeled_list.addLabeledItem(_build_labeled_item("li1", "lbl1", "c1"))
        labeled_list.addLabeledItem(_build_labeled_item("li2", "lbl2", "c2"))
        vp = VariationPoint()
        vp.setShortLabel(Identifier().setValue("DVP"))
        labeled_list.setVariationPoint(vp)

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
            reparsed = swc_2.getIntroduction().getLabeledList()

            assert isinstance(reparsed, LabeledList)
            assert reparsed.getSi().getValue() == "SIVAL"
            assert reparsed.getView().getValue() == "VIEWVAL"
            assert reparsed.getBreak().getValue() == ChapterEnumBreak.BREAK
            assert reparsed.getKeepWithPrevious().getValue() == KeepWithPreviousEnum.KEEP
            assert reparsed.getIndentSample().getItemLabelPos().getValue() == "NEWLINE"
            assert reparsed.getIndentSample().getL2s()[0].getValue() == "sample"
            items = reparsed.getLabeledItems()
            assert [item.getHelpEntry().getValue() for item in items] == ["li1", "li2"]
            assert items[0].getItemLabel().getL2s()[0].getValue() == "lbl1"
            assert items[1].getItemContents().getPs()[0].getL1s()[0].getValue() == "c2"
            assert reparsed.getVariationPoint().getShortLabel().getValue() == "DVP"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


def _build_indent_sample():
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import IndentSample, ItemLabelPosEnum

    indent_sample = IndentSample()
    indent_sample.setItemLabelPos(ItemLabelPosEnum().setValue(ItemLabelPosEnum.NEWLINE))
    l2 = LOverviewParagraph()
    l2.setL("EN")
    l2.setValue("sample")
    indent_sample.addL2(l2)
    return indent_sample


def _build_labeled_item(help_entry, label, content):
    item = LabeledItem()
    item.setHelpEntry(String().setValue(help_entry))
    item_label = MultiLanguageOverviewParagraph()
    l2 = LOverviewParagraph()
    l2.setL("EN")
    l2.setValue(label)
    item_label.addL2(l2)
    item.setItemLabel(item_label)
    item.setItemContents(_build_contents(content))
    return item


def _build_contents(text):
    from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
    from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph

    block = DocumentationBlock()
    paragraph = MultiLanguageParagraph()
    l1 = LParagraph()
    l1.setL("EN")
    l1.setValue(text)
    paragraph.addL1(l1)
    block.addP(paragraph)
    return block
