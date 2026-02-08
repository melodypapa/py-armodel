"""
This module contains tests for the DocumentationBlock module in MSR.Documentation.TextModel.BlockElements.
"""
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import MlFigure
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import (
    ARList,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultiLanguageParagraph,
)


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
        def_list = "definition_list"

        result = documentation_block.setDefList(def_list)
        assert documentation_block.getDefList() == def_list
        assert result == documentation_block

    def test_documentation_block_figures_methods(self):
        """Test adding figures."""
        documentation_block = DocumentationBlock()
        figure = MlFigure()

        result = documentation_block.addFigure(figure)
        figures = documentation_block.getFigures()
        assert figure in figures
        assert result == documentation_block

    def test_documentation_block_formula_methods(self):
        """Test the formula getter and setter."""
        documentation_block = DocumentationBlock()
        formula = "E=mc^2"

        result = documentation_block.setFormula(formula)
        assert documentation_block.getFormula() == formula
        assert result == documentation_block

    def test_documentation_block_labeled_list_methods(self):
        """Test the labeledList getter and setter."""
        documentation_block = DocumentationBlock()
        labeled_list = "labeled_list"

        result = documentation_block.setLabeledList(labeled_list)
        assert documentation_block.getLabeledList() == labeled_list
        assert result == documentation_block

    def test_documentation_block_lists_methods(self):
        """Test adding lists."""
        documentation_block = DocumentationBlock()
        ar_list = ARList()

        result = documentation_block.addList(ar_list)
        lists = documentation_block.getLists()
        assert ar_list in lists
        assert result == documentation_block

    def test_documentation_block_msr_query_p2_methods(self):
        """Test the msrQueryP2 getter and setter."""
        documentation_block = DocumentationBlock()
        msr_query = "query"

        result = documentation_block.setMsrQueryP2(msr_query)
        assert documentation_block.getMsrQueryP2() == msr_query
        assert result == documentation_block

    def test_documentation_block_note_methods(self):
        """Test the note getter and setter."""
        documentation_block = DocumentationBlock()
        note = "note_text"

        result = documentation_block.setNote(note)
        assert documentation_block.getNote() == note
        assert result == documentation_block

    def test_documentation_block_ps_methods(self):
        """Test adding paragraphs."""
        documentation_block = DocumentationBlock()
        paragraph = MultiLanguageParagraph()

        result = documentation_block.addP(paragraph)
        ps = documentation_block.getPs()
        assert paragraph in ps
        assert result == documentation_block

    def test_documentation_block_structured_req_methods(self):
        """Test the structuredReq getter and setter."""
        documentation_block = DocumentationBlock()
        structured_req = "structured_requirement"

        result = documentation_block.setStructuredReq(structured_req)
        assert documentation_block.getStructuredReq() == structured_req
        assert result == documentation_block

    def test_documentation_block_trace_methods(self):
        """Test the trace getter and setter."""
        documentation_block = DocumentationBlock()
        trace = "traceable_text"

        result = documentation_block.setTrace(trace)
        assert documentation_block.getTrace() == trace
        assert result == documentation_block

    def test_documentation_block_verbatim_methods(self):
        """Test the verbatim getter and setter."""
        documentation_block = DocumentationBlock()
        verbatim = "verbatim_text"

        result = documentation_block.setVerbatim(verbatim)
        assert documentation_block.getVerbatim() == verbatim
        assert result == documentation_block
