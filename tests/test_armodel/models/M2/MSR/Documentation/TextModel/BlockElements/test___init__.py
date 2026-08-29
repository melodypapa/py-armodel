"""
This module contains tests for the DocumentationBlock module in MSR.Documentation.BlockElements.
"""

from armodel.models.M2.MSR.Documentation.BlockElements.Figure import MlFigure
from armodel.models.M2.MSR.Documentation.BlockElements.Formula import MlFormula
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import ARList, DefList, LabeledList
from armodel.models.M2.MSR.Documentation.BlockElements.Note import Note
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import StructuredReq, TraceableText
from armodel.models.M2.MSR.Documentation.MsrQuery import MsrQueryP2
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph, MultiLanguageVerbatim


class TestDocumentationBlock:
    """Test class for DocumentationBlock class."""

    def test_documentation_block_initialization(self):
        """Test that a DocumentationBlock object can be initialized with default values."""
        documentation_block = DocumentationBlock()
        assert documentation_block.defList is None
        assert documentation_block.figures == []
        assert documentation_block.formula is None
        assert documentation_block.labeledList is None
        assert documentation_block.lists == []
        assert documentation_block.msrQueryP2 is None
        assert documentation_block.note is None
        assert documentation_block.ps == []
        assert documentation_block.structuredReq is None
        assert documentation_block.trace is None
        assert documentation_block.verbatim is None

    def test_documentation_block_def_list_methods(self):
        """Test the defList getter and setter."""
        documentation_block = DocumentationBlock()
        def_list = DefList()

        result = documentation_block.setDefList(def_list)
        assert documentation_block.getDefList() == def_list
        assert result == documentation_block

        documentation_block.setDefList(None)
        assert documentation_block.getDefList() == def_list

    def test_documentation_block_figures_methods(self):
        """Test adding figures."""
        documentation_block = DocumentationBlock()
        figure = MlFigure()

        result = documentation_block.addFigure(figure)
        figures = documentation_block.getFigures()
        assert figure in figures
        assert result == documentation_block

        documentation_block.addFigure(None)
        assert documentation_block.getFigures() == [figure]

    def test_documentation_block_formula_methods(self):
        """Test the formula getter and setter."""
        documentation_block = DocumentationBlock()
        formula = MlFormula()

        result = documentation_block.setFormula(formula)
        assert documentation_block.getFormula() == formula
        assert result == documentation_block

        documentation_block.setFormula(None)
        assert documentation_block.getFormula() == formula

    def test_documentation_block_labeled_list_methods(self):
        """Test the labeledList getter and setter."""
        documentation_block = DocumentationBlock()
        labeled_list = LabeledList()

        result = documentation_block.setLabeledList(labeled_list)
        assert documentation_block.getLabeledList() == labeled_list
        assert result == documentation_block

        documentation_block.setLabeledList(None)
        assert documentation_block.getLabeledList() == labeled_list

    def test_documentation_block_lists_methods(self):
        """Test adding lists."""
        documentation_block = DocumentationBlock()
        ar_list = ARList()

        result = documentation_block.addList(ar_list)
        lists = documentation_block.getLists()
        assert ar_list in lists
        assert result == documentation_block

        documentation_block.addList(None)
        assert documentation_block.getLists() == [ar_list]

    def test_documentation_block_msr_query_p2_methods(self):
        """Test the msrQueryP2 getter and setter."""
        documentation_block = DocumentationBlock()
        msr_query = MsrQueryP2()

        result = documentation_block.setMsrQueryP2(msr_query)
        assert documentation_block.getMsrQueryP2() == msr_query
        assert result == documentation_block

        documentation_block.setMsrQueryP2(None)
        assert documentation_block.getMsrQueryP2() == msr_query

    def test_documentation_block_note_methods(self):
        """Test the note getter and setter."""
        documentation_block = DocumentationBlock()
        note = Note()

        result = documentation_block.setNote(note)
        assert documentation_block.getNote() == note
        assert result == documentation_block

        documentation_block.setNote(None)
        assert documentation_block.getNote() == note

    def test_documentation_block_ps_methods(self):
        """Test adding paragraphs."""
        documentation_block = DocumentationBlock()
        paragraph = MultiLanguageParagraph()

        result = documentation_block.addP(paragraph)
        ps = documentation_block.getPs()
        assert paragraph in ps
        assert result == documentation_block

        documentation_block.addP(None)
        assert documentation_block.getPs() == [paragraph]

    def test_documentation_block_structured_req_methods(self):
        """Test the structuredReq getter and setter."""
        documentation_block = DocumentationBlock()
        structured_req = StructuredReq()

        result = documentation_block.setStructuredReq(structured_req)
        assert documentation_block.getStructuredReq() == structured_req
        assert result == documentation_block

        documentation_block.setStructuredReq(None)
        assert documentation_block.getStructuredReq() == structured_req

    def test_documentation_block_trace_methods(self):
        """Test the trace getter and setter."""
        documentation_block = DocumentationBlock()
        trace = TraceableText()

        result = documentation_block.setTrace(trace)
        assert documentation_block.getTrace() == trace
        assert result == documentation_block

        documentation_block.setTrace(None)
        assert documentation_block.getTrace() == trace

    def test_documentation_block_verbatim_methods(self):
        """Test the verbatim getter and setter."""
        documentation_block = DocumentationBlock()
        verbatim = MultiLanguageVerbatim()

        result = documentation_block.setVerbatim(verbatim)
        assert documentation_block.getVerbatim() == verbatim
        assert result == documentation_block

        documentation_block.setVerbatim(None)
        assert documentation_block.getVerbatim() == verbatim
