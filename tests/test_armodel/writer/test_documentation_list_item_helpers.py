"""Writer tests for the DocumentationBlock list-item helpers (DefItem / LabeledItem / IndentSample).

R23-11 (AUTOSAR_00052.xsd) declares their attributes as HELP-ENTRY (attributeGroups
DEF-ITEM / LABELED-ITEM) and ITEM-LABEL-POS (attributeGroup INDENT-SAMPLE) — not the
HELPENTRY / ITEMLABELPOS spellings this writer used to emit.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameTokens, String, ViewTokens
from armodel.models.M2.MSR.Documentation.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import DefList, IndentSample, ItemLabelPosEnum, LabeledItem, LabeledList
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import ChapterEnumBreak, KeepWithPreviousEnum
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName, LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName, MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _make_block(value):
    block = DocumentationBlock()
    paragraph = MultiLanguageParagraph()
    l1 = LParagraph()
    l1.setL("EN")
    l1.setValue(value)
    paragraph.addL1(l1)
    block.addP(paragraph)
    return block


class TestDocumentationListItemHelpersWriter:
    def test_writes_help_entry_on_def_item(self):
        """attributeGroup DEF-ITEM declares HELP-ENTRY (AUTOSAR_00052.xsd)."""
        writer = _writer()
        parent = ET.Element("PARENT")
        def_list = DefList()
        def_item = def_list.createDefItem("d1")
        def_item.setHelpEntry(String().setValue("def-topic"))

        writer.writeDefItem(parent, def_item)

        assert parent.find("DEF-ITEM").attrib["HELP-ENTRY"] == "def-topic"

    def test_writes_help_entry_on_labeled_item(self):
        """attributeGroup LABELED-ITEM declares HELP-ENTRY (AUTOSAR_00052.xsd)."""
        writer = _writer()
        parent = ET.Element("PARENT")
        labeled_item = LabeledItem()
        labeled_item.setHelpEntry(String().setValue("li-topic"))

        writer.setLabeledItem(parent, labeled_item)

        assert parent.find("LABELED-ITEM").attrib["HELP-ENTRY"] == "li-topic"

    def test_writes_item_label_pos_on_indent_sample(self):
        """attributeGroup INDENT-SAMPLE declares ITEM-LABEL-POS (AUTOSAR_00052.xsd)."""
        writer = _writer()
        parent = ET.Element("PARENT")
        indent_sample = IndentSample()
        indent_sample.setItemLabelPos(ItemLabelPosEnum().setValue(ItemLabelPosEnum.NEWLINE))

        writer.setIndentSample(parent, indent_sample)

        assert parent.find("INDENT-SAMPLE").attrib["ITEM-LABEL-POS"] == "NEWLINE"

    def test_write_read_round_trip_preserves_def_item_attributes(self):
        """Full write → parse round-trip: SHORT-NAME, LONG-NAME, SI/VIEW/BREAK/KEEP-WITH-PREVIOUS, HELP-ENTRY and the DEF payload all survive."""
        writer = _writer()
        parent = ET.Element("PARENT")
        def_list = DefList()
        def_item = def_list.createDefItem("d1")
        long_name = MultilanguageLongName()
        l4 = LLongName()
        l4.setL("EN")
        l4.setValue("Definition")
        long_name.addL4(l4)
        def_item.setLongName(long_name)
        def_item.setSi(NameTokens().setValue("SIVAL"))
        def_item.setView(ViewTokens().setValue("VIEWVAL"))
        def_item.setBreak(ChapterEnumBreak().setValue(ChapterEnumBreak.BREAK))
        def_item.setKeepWithPrevious(KeepWithPreviousEnum().setValue(KeepWithPreviousEnum.KEEP))
        def_item.setHelpEntry(String().setValue("def-topic"))
        def_item.setDef(_make_block("def text"))

        writer.writeDefList(parent, def_list)
        parent.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(parent, encoding="unicode"))

        reloaded = ARXMLParser().readDefList(parsed, "DEF-LIST").getDefItems()[0]
        assert reloaded.getShortName() == "d1"
        assert reloaded.getLongName().getL4s()[0].getValue() == "Definition"
        assert reloaded.getSi().getValue() == "SIVAL"
        assert reloaded.getView().getValue() == "VIEWVAL"
        assert reloaded.getBreak().getValue() == ChapterEnumBreak.BREAK
        assert reloaded.getKeepWithPrevious().getValue() == KeepWithPreviousEnum.KEEP
        assert reloaded.getHelpEntry().getValue() == "def-topic"
        assert reloaded.getDef().getPs()[0].getL1s()[0].getValue() == "def text"

    def test_document_round_trip_preserves_def_item_state_with_xsd_validation_on(self):
        """save → reload with XSD validation ON preserves LONG-NAME, SI/VIEW/BREAK/KEEP-WITH-PREVIOUS and the own attributes."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")

        def_list = DefList()
        def_item = def_list.createDefItem("d1")
        long_name = MultilanguageLongName()
        l4 = LLongName()
        l4.setL("EN")
        l4.setValue("Definition")
        long_name.addL4(l4)
        def_item.setLongName(long_name)
        def_item.setSi(NameTokens().setValue("SIVAL"))
        def_item.setView(ViewTokens().setValue("VIEWVAL"))
        def_item.setBreak(ChapterEnumBreak().setValue(ChapterEnumBreak.BREAK))
        def_item.setKeepWithPrevious(KeepWithPreviousEnum().setValue(KeepWithPreviousEnum.KEEP))
        def_item.setHelpEntry(String().setValue("def-topic"))
        def_item.setDef(_make_block("def text"))
        intro = DocumentationBlock()
        intro.setDefList(def_list)
        swc.setIntroduction(intro)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            reparsed = swc_2.getIntroduction().getDefList().getDefItems()[0]

            assert reparsed.getShortName() == "d1"
            assert reparsed.getLongName().getL4s()[0].getValue() == "Definition"
            assert reparsed.getSi().getValue() == "SIVAL"
            assert reparsed.getView().getValue() == "VIEWVAL"
            assert reparsed.getBreak().getValue() == ChapterEnumBreak.BREAK
            assert reparsed.getKeepWithPrevious().getValue() == KeepWithPreviousEnum.KEEP
            assert reparsed.getHelpEntry().getValue() == "def-topic"
            assert reparsed.getDef().getPs()[0].getL1s()[0].getValue() == "def text"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_write_read_round_trip_preserves_labeled_item_and_indent_sample_attributes(self):
        """Full write → parse round-trip: LABELED-ITEM HELP-ENTRY and INDENT-SAMPLE ITEM-LABEL-POS both survive."""
        writer = _writer()
        parent = ET.Element("PARENT")
        labeled_list = LabeledList()
        indent_sample = IndentSample()
        indent_sample.setItemLabelPos(ItemLabelPosEnum().setValue(ItemLabelPosEnum.NEWLINE))
        labeled_list.setIndentSample(indent_sample)
        labeled_item = LabeledItem()
        labeled_item.setHelpEntry(String().setValue("li-topic"))
        labeled_list.addLabeledItem(labeled_item)

        writer.setLabeledList(parent, labeled_list)
        parent.attrib["xmlns"] = "http://autosar.org/schema/r4.0"
        parsed = ET.fromstring(ET.tostring(parent, encoding="unicode"))

        reloaded = ARXMLParser().getLabeledList(parsed, "LABELED-LIST")
        assert reloaded.getIndentSample().getItemLabelPos().getValue() == ItemLabelPosEnum.NEWLINE
        assert reloaded.getLabeledItems()[0].getHelpEntry().getValue() == "li-topic"
