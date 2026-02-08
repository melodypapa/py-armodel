"""
This module contains tests for the PaginationAndView module in MSR.Documentation.TextModel.BlockElements.
"""
import pytest

from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import *


class TestDocumentViewSelectable:
    """Test class for DocumentViewSelectable class."""

    def test_document_view_selectable_initialization(self):
        """Test that DocumentViewSelectable is abstract and cannot be instantiated directly."""
        # Test that DocumentViewSelectable cannot be instantiated directly
        with pytest.raises(TypeError, match="DocumentViewSelectable is an abstract class"):
            DocumentViewSelectable()

        # Test that Paginateable is also abstract
        with pytest.raises(TypeError, match="Paginateable is an abstract class"):
            Paginateable()


class TestPaginateable:
    """Test class for Paginateable class."""

    def test_paginateable_is_abstract(self):
        """Test that Paginateable is abstract and cannot be instantiated directly."""
        with pytest.raises(TypeError, match="Paginateable is an abstract class"):
            Paginateable()

    def test_paginateable_subclass_can_be_instantiated(self):
        """Test that a concrete subclass of Paginateable can be instantiated."""
        # Create a simple concrete subclass for testing
        class ConcretePaginatable(Paginateable):
            def __init__(self):
                super().__init__()

        concrete = ConcretePaginatable()
        assert concrete is not None
        assert isinstance(concrete, DocumentViewSelectable)
        assert isinstance(concrete, Paginateable)

    def test_paginateable_break_methods(self):
        """Test the chapterBreak getter and setter."""
        # Create a concrete subclass for testing
        class ConcretePaginatable(Paginateable):
            def __init__(self):
                super().__init__()

        paginateable = ConcretePaginatable()
        chapter_break = "break"

        result = paginateable.setBreak(chapter_break)
        assert paginateable.getBreak() == chapter_break
        assert result == paginateable

    def test_paginateable_keep_with_previous_methods(self):
        """Test the keepWithPrevious getter and setter."""
        # Create a concrete subclass for testing
        class ConcretePaginatable(Paginateable):
            def __init__(self):
                super().__init__()

        paginateable = ConcretePaginatable()
        keep_with_prev = "keep"

        result = paginateable.setKeepWithPrevious(keep_with_prev)
        assert paginateable.getKeepWithPrevious() == keep_with_prev
        assert result == paginateable
