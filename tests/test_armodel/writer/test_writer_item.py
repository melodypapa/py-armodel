"""
Reader/writer round-trip tests for the ITEM element of an ARList (Table 9.9, Item).

The <ITEM> element lives inside a <LIST> element and is written/read by the
ARList-owned helpers (writer setListElement / parser getListElements), which
currently map the ITEM content to a DocumentationBlock directly. The
spec-faithful Item wrapper (Item.itemContents + VARIATION-POINT) is not yet
dispatched on either layer — that wiring is the ARList row's scope.
"""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import ARList
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestItemRoundTrip:
    def _make_paragraph(self, value):
        paragraph = MultiLanguageParagraph()
        l1 = LParagraph()
        l1.setL("EN")
        l1.setValue(value)
        paragraph.addL1(l1)
        return paragraph

    def test_round_trip(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")

        intro = DocumentationBlock()
        ar_list = ARList()

        item_contents = DocumentationBlock()
        item_contents.addP(self._make_paragraph("list item text"))
        nested_list = ARList()
        nested_contents = DocumentationBlock()
        nested_contents.addP(self._make_paragraph("nested item text"))
        nested_list.addItem(nested_contents)
        item_contents.addList(nested_list)

        ar_list.addItem(item_contents)
        intro.addList(ar_list)
        swc.setIntroduction(intro)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            intro_2 = swc_2.getIntroduction()
            parsed_list = intro_2.getLists()[0]
            assert parsed_list is not None
            items = parsed_list.getItems()
            assert len(items) == 1
            assert items[0].getPs()[0].getL1s()[0].getValue() == "list item text"
            nested = items[0].getLists()[0]
            assert nested.getItems()[0].getPs()[0].getL1s()[0].getValue() == "nested item text"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty_list(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")

        intro = DocumentationBlock()
        ar_list = ARList()
        intro.addList(ar_list)
        swc.setIntroduction(intro)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            intro_2 = swc_2.getIntroduction()
            assert intro_2.getLists()[0].getItems() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
