"""
This module contains tests for the PaginationAndView module in MSR.Documentation.TextModel.BlockElements.
"""
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import *


class TestDocumentViewSelectable:
    """Test class for DocumentViewSelectable class."""
    
    def test_document_view_selectable_initialization(self):
        """Test that a DocumentViewSelectable object can be initialized."""
        doc_view_selectable = DocumentViewSelectable()
        assert doc_view_selectable is not None


class TestPaginateable:
    """Test class for Paginateable class."""
    
    def test_paginateable_initialization(self):
        """Test that a Paginateable object can be initialized with default values."""
        paginateable = Paginateable()
        assert paginateable.chapterBreak is None
        assert paginateable.keepWithPrevious is None
    
    def test_paginateable_break_methods(self):
        """Test the chapterBreak getter and setter."""
        paginateable = Paginateable()
        chapter_break = "break"
        
        result = paginateable.setBreak(chapter_break)
        assert paginateable.getBreak() == chapter_break
        assert result == paginateable
    
    def test_paginateable_keep_with_previous_methods(self):
        """Test the keepWithPrevious getter and setter."""
        paginateable = Paginateable()
        keep_with_prev = "keep"
        
        result = paginateable.setKeepWithPrevious(keep_with_prev)
        assert paginateable.getKeepWithPrevious() == keep_with_prev
        assert result == paginateable