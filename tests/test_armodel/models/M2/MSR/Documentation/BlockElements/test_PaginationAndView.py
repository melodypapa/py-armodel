"""
This module contains tests for the PaginationAndView module in MSR.Documentation.BlockElements.
"""

import pytest

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    ChapterEnumBreak,
    DocumentViewSelectable,
    KeepWithPreviousEnum,
    Paginateable,
)


class TestChapterEnumBreak:
    """Test class for the ChapterEnumBreak enumeration (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 9.61)."""

    def test_instantiation(self):
        """ChapterEnumBreak shall be instantiable as an AREnum."""
        enum_instance = ChapterEnumBreak()
        assert enum_instance is not None
        assert isinstance(enum_instance, ChapterEnumBreak)

    def test_enum_values_present(self):
        """The two spec literals shall be present with their XSD-backed values."""
        assert ChapterEnumBreak.BREAK == "BREAK"
        assert ChapterEnumBreak.NO_BREAK == "NO-BREAK"

    def test_enum_values_collection(self):
        """getEnumValues shall expose exactly the two spec literals."""
        values = ChapterEnumBreak().getEnumValues()
        assert "BREAK" in values
        assert "NO-BREAK" in values
        assert len(values) == 2

    def test_set_get_value(self):
        """setValue/getValue shall round-trip a spec literal."""
        enum_instance = ChapterEnumBreak().setValue(ChapterEnumBreak.BREAK)
        assert enum_instance.getValue() == "BREAK"

        enum_instance.setValue(ChapterEnumBreak.NO_BREAK)
        assert enum_instance.getValue() == "NO-BREAK"

    def test_validate_enum_value(self):
        """validateEnumValue shall accept spec literals and reject others."""
        enum_instance = ChapterEnumBreak()
        assert enum_instance.validateEnumValue("BREAK") is True
        assert enum_instance.validateEnumValue("NO-BREAK") is True
        assert enum_instance.validateEnumValue("UNKNOWN") is False


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
        chapter_break = ChapterEnumBreak().setValue(ChapterEnumBreak.BREAK)

        result = paginateable.setBreak(chapter_break)
        assert paginateable.getBreak() == chapter_break
        assert result == paginateable

        paginateable.setBreak(None)
        assert paginateable.getBreak() == chapter_break

    def test_paginateable_keep_with_previous_methods(self):
        """Test the keepWithPrevious getter and setter."""

        # Create a concrete subclass for testing
        class ConcretePaginatable(Paginateable):
            def __init__(self):
                super().__init__()

        paginateable = ConcretePaginatable()
        keep_with_prev = KeepWithPreviousEnum().setValue(KeepWithPreviousEnum.KEEP)

        result = paginateable.setKeepWithPrevious(keep_with_prev)
        assert paginateable.getKeepWithPrevious() == keep_with_prev
        assert result == paginateable

        paginateable.setKeepWithPrevious(None)
        assert paginateable.getKeepWithPrevious() == keep_with_prev

    def test_paginateable_defaults(self):
        class ConcretePaginatable(Paginateable):
            def __init__(self):
                super().__init__()

        paginateable = ConcretePaginatable()
        assert paginateable.getBreak() is None
        assert paginateable.getKeepWithPrevious() is None

    def test_enum_values(self):
        assert ChapterEnumBreak().getValue() == ""
        assert ChapterEnumBreak.BREAK == "BREAK"
        assert ChapterEnumBreak.NO_BREAK == "NO-BREAK"
        assert KeepWithPreviousEnum.KEEP == "keep"
        assert KeepWithPreviousEnum.NO_KEEP == "noKeep"
