"""Reader/writer round-trip tests for DocumentationBlock child elements (Table 9.1)."""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, String
from armodel.models.M2.MSR.Documentation.BlockElements.Formula import MlFormula
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import FloatEnum, PgwideEnum
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import DefItem, DefList, LabeledItem, LabeledList
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.Note import Note, NoteTypeEnum
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.RequirementsTracing import StructuredReq, TraceableText
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph, LVerbatim
from armodel.models.M2.MSR.Documentation.TextModel.MsrQuery import MsrQueryArg, MsrQueryP2, MsrQueryProps
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph, MultiLanguageParagraph, MultiLanguageVerbatim
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestDocumentationBlockRoundTrip:
    def _build(self, document):
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")

        intro = DocumentationBlock()

        paragraph = MultiLanguageParagraph()
        l1 = LOverviewParagraph()
        l1.setL("EN")
        l1.setValue("paragraph text")
        paragraph.addL1(l1)
        intro.addP(paragraph)

        note_text = DocumentationBlock()
        note_paragraph = MultiLanguageParagraph()
        l1_note = LOverviewParagraph()
        l1_note.setL("EN")
        l1_note.setValue("note paragraph")
        note_paragraph.addL1(l1_note)
        note_text.addP(note_paragraph)
        note = Note()
        note.setNoteType(NoteTypeEnum().setValue(NoteTypeEnum.HINT))
        note.setNoteText(note_text)
        intro.setNote(note)

        trace_text = DocumentationBlock()
        trace_paragraph = MultiLanguageParagraph()
        l1_trace = LOverviewParagraph()
        l1_trace.setL("EN")
        l1_trace.setValue("trace paragraph")
        trace_paragraph.addL1(l1_trace)
        trace_text.addP(trace_paragraph)
        trace = TraceableText()
        trace.setText(trace_text)
        intro.setTrace(trace)

        structured_req = StructuredReq()
        structured_req.setDate(String().setValue("2023-11-01"))
        structured_req.setImportance(String().setValue("high"))
        structured_req.setIssuedBy(String().setValue("AUTOSAR"))
        structured_req.setType(String().setValue("enhancement"))
        intro.setStructuredReq(structured_req)

        def_item = DefItem()
        def_list = DefList()
        def_list.addDefItem(def_item)
        intro.setDefList(def_list)

        labeled_item = LabeledItem()
        item_label = MultiLanguageOverviewParagraph()
        l2 = LOverviewParagraph()
        l2.setL("EN")
        l2.setValue("label")
        item_label.addL2(l2)
        labeled_item.setItemLabel(item_label)
        labeled_list = LabeledList()
        labeled_list.addLabeledItem(labeled_item)
        intro.setLabeledList(labeled_list)

        verbatim = MultiLanguageVerbatim()
        l5 = LVerbatim()
        l5.setL("EN")
        l5.setValue("verbatim text")
        verbatim.addL5(l5)
        verbatim.setFloat(FloatEnum().setValue(FloatEnum.NO_FLOAT))
        verbatim.setPgwide(PgwideEnum().setValue(PgwideEnum.PGWIDE))
        intro.setVerbatim(verbatim)

        msr_query_arg = MsrQueryArg()
        msr_query_arg.setArg(String().setValue("value"))
        msr_query_arg.setSi(NameToken().setValue("ARG"))
        msr_query_props = MsrQueryProps()
        msr_query_props.setMsrQueryName(String().setValue("QUERY"))
        msr_query_props.addMsrQueryArg(msr_query_arg)
        msr_query_p2 = MsrQueryP2()
        msr_query_p2.setMsrQueryProps(msr_query_props)
        intro.setMsrQueryP2(msr_query_p2)

        intro.setFormula(MlFormula())

        swc.setIntroduction(intro)
        return swc

    def test_round_trip(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        self._build(document)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            intro = swc_2.getIntroduction()
            assert intro is not None
            assert len(intro.getPs()) == 1
            assert intro.getPs()[0].getL1s()[0].getValue() == "paragraph text"

            note = intro.getNote()
            assert note is not None
            assert note.getNoteType().getValue() == "hint"
            assert note.getNoteText().getPs()[0].getL1s()[0].getValue() == "note paragraph"

            trace = intro.getTrace()
            assert trace is not None
            assert trace.getText().getPs()[0].getL1s()[0].getValue() == "trace paragraph"

            structured_req = intro.getStructuredReq()
            assert structured_req is not None
            assert structured_req.getImportance().getValue() == "high"
            assert structured_req.getIssuedBy().getValue() == "AUTOSAR"

            def_list = intro.getDefList()
            assert def_list is not None
            assert len(def_list.getDefItems()) == 1

            labeled_list = intro.getLabeledList()
            assert labeled_list is not None
            assert labeled_list.getLabeledItems()[0].getItemLabel().getL2s()[0].getValue() == "label"

            verbatim = intro.getVerbatim()
            assert verbatim is not None
            assert verbatim.getL5s()[0].getValue() == "verbatim text"
            assert verbatim.getFloat().getValue() == "noFloat"
            assert verbatim.getPgwide().getValue() == "pgwide"

            msr_query_p2 = intro.getMsrQueryP2()
            assert msr_query_p2 is not None
            assert msr_query_p2.getMsrQueryProps().getMsrQueryName().getValue() == "QUERY"
            assert msr_query_p2.getMsrQueryProps().getMsrQueryArgs()[0].getArg().getValue() == "value"

            assert intro.getFormula() is not None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")
        swc.setIntroduction(DocumentationBlock())

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            intro = swc_2.getIntroduction()
            assert intro.getPs() == []
            assert intro.getDefList() is None
            assert intro.getNote() is None
            assert intro.getTrace() is None
            assert intro.getStructuredReq() is None
            assert intro.getLabeledList() is None
            assert intro.getVerbatim() is None
            assert intro.getMsrQueryP2() is None
            assert intro.getFormula() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
