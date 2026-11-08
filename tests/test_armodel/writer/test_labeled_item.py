"""Writer tests for LabeledItem (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.12).

The writer entry point setLabeledItem must emit HELP-ENTRY as an attribute, then
ITEM-LABEL, the inline DOCUMENTATION-BLOCK content and VARIATION-POINT in the XSD
LABELED-ITEM sequence (sequenceOffsets 20 / 30 / 10000), and the document-level
round-trip must preserve the concrete LabeledItem type and every field value with
XSD validation ON.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, NameTokens, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.MSR.Documentation.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import LabeledItem, LabeledList
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph, LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph, MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _parent():
    return ET.Element("PARENT")


class TestLabeledItemWriter:
    def test_write_emits_children_in_xsd_order(self):
        """The XSD LABELED-ITEM group order is ITEM-LABEL (offset 20), the inline DOCUMENTATION-BLOCK (offset 30), then VARIATION-POINT (offset 10000); HELP-ENTRY is an attribute."""
        labeled_item = _build_labeled_item("li1", "lbl1", "c1")
        vp = VariationPoint()
        vp.setShortLabel(Identifier().setValue("DVP"))
        labeled_item.setVariationPoint(vp)

        parent = _parent()
        ARXMLWriter().setLabeledItem(parent, labeled_item)

        element = parent[0]
        assert element.tag == "LABELED-ITEM"
        assert element.attrib["HELP-ENTRY"] == "li1"
        assert [child.tag for child in element] == ["ITEM-LABEL", "P", "VARIATION-POINT"]
        assert element[0].find("L-2").text == "lbl1"
        assert element[1].find("L-1").text == "c1"
        assert element[2].find("SHORT-LABEL").text == "DVP"

    def test_write_empty_labeled_item_emits_bare_element(self):
        """An empty LabeledItem emits a bare <LABELED-ITEM/> (all members are optional)."""
        parent = _parent()
        ARXMLWriter().setLabeledItem(parent, LabeledItem())

        assert len(parent) == 1
        assert parent[0].tag == "LABELED-ITEM"
        assert len(parent[0]) == 0
        assert parent[0].attrib == {}

    def test_write_read_round_trip(self):
        """save → reload preserves the concrete LabeledItem type and every field value (XSD validation ON)."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")

        labeled_item = _build_labeled_item("li1", "lbl1", "c1")
        labeled_item.setSi(NameTokens().setValue("SIVAL"))
        vp = VariationPoint()
        vp.setShortLabel(Identifier().setValue("DVP"))
        labeled_item.setVariationPoint(vp)

        labeled_list = LabeledList()
        labeled_list.addLabeledItem(labeled_item)
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
            reparsed = swc_2.getIntroduction().getLabeledList().getLabeledItems()[0]

            assert isinstance(reparsed, LabeledItem)
            assert reparsed.getHelpEntry().getValue() == "li1"
            assert reparsed.getSi().getValue() == "SIVAL"
            assert reparsed.getItemLabel().getL2s()[0].getValue() == "lbl1"
            assert reparsed.getItemContents().getPs()[0].getL1s()[0].getValue() == "c1"
            assert reparsed.getVariationPoint().getShortLabel().getValue() == "DVP"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


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
    block = DocumentationBlock()
    paragraph = MultiLanguageParagraph()
    l1 = LParagraph()
    l1.setL("EN")
    l1.setValue(text)
    paragraph.addL1(l1)
    block.addP(paragraph)
    return block
