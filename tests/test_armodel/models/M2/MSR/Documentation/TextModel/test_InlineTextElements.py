"""This module contains tests for the InlineTextElements module in MSR.Documentation.TextModel."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, String
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    EmphasisText,
    IndexEntry,
    Superscript,
    Tt,
)


class TestSuperscript:
    """Test class for Superscript class."""

    def test_superscript_initialization(self):
        """Test that a Superscript object can be initialized."""
        superscript = Superscript()
        assert superscript is not None


class TestTt:
    """Test class for Tt class."""

    def test_tt_initialization(self):
        """Test that a Tt object can be initialized with default values."""
        tt = Tt()
        assert tt.value is None
        assert tt.texRender is None
        assert tt.type is None

    def test_tt_value_methods(self):
        """Test the value getter and setter."""
        tt = Tt()
        value = String().setValue("MyClass")

        result = tt.setValue(value)
        assert tt.getValue() == value
        assert result == tt

        tt.setValue(None)
        assert tt.getValue() == value

    def test_tt_tex_render_methods(self):
        """Test the texRender getter and setter."""
        tt = Tt()
        render = String().setValue("My\\sep{}Class")

        result = tt.setTexRender(render)
        assert tt.getTexRender() == render
        assert result == tt

        tt.setTexRender(None)
        assert tt.getTexRender() == render

    def test_tt_type_methods(self):
        """Test the type getter and setter."""
        tt = Tt()
        term_type = NameToken().setValue("VARIABLE")

        result = tt.setType(term_type)
        assert tt.getType() == term_type
        assert result == tt

        tt.setType(None)
        assert tt.getType() == term_type


class TestIndexEntry:
    """Test class for IndexEntry class."""

    def test_index_entry_initialization(self):
        """Test that an IndexEntry object can be initialized with default values."""
        index_entry = IndexEntry()
        assert index_entry.value is None
        assert index_entry.sub is None
        assert index_entry.sup is None

    def test_index_entry_value_methods(self):
        """Test the value getter and setter."""
        index_entry = IndexEntry()
        value = String().setValue("index")

        result = index_entry.setValue(value)
        assert index_entry.getValue() == value
        assert result == index_entry

        index_entry.setValue(None)
        assert index_entry.getValue() == value

    def test_index_entry_sub_methods(self):
        """Test the sub getter and setter."""
        index_entry = IndexEntry()
        sub = Superscript()

        result = index_entry.setSub(sub)
        assert index_entry.getSub() == sub
        assert result == index_entry

        index_entry.setSub(None)
        assert index_entry.getSub() == sub

    def test_index_entry_sup_methods(self):
        """Test the sup getter and setter."""
        index_entry = IndexEntry()
        sup = Superscript()

        result = index_entry.setSup(sup)
        assert index_entry.getSup() == sup
        assert result == index_entry

        index_entry.setSup(None)
        assert index_entry.getSup() == sup


class TestEmphasisText:
    """Test class for EmphasisText class."""

    def test_emphasis_text_initialization(self):
        """Test that an EmphasisText object can be initialized with default values."""
        emphasis_text = EmphasisText()
        assert emphasis_text.value is None
        assert emphasis_text.color is None
        assert emphasis_text.font is None
        assert emphasis_text.sub is None
        assert emphasis_text.sup is None
        assert emphasis_text.tt is None
        assert emphasis_text.type is None

    def test_emphasis_text_value_methods(self):
        """Test the value getter and setter."""
        emphasis_text = EmphasisText()
        value = String().setValue("emphasized")

        result = emphasis_text.setValue(value)
        assert emphasis_text.getValue() == value
        assert result == emphasis_text

        emphasis_text.setValue(None)
        assert emphasis_text.getValue() == value

    def test_emphasis_text_color_methods(self):
        """Test the color getter and setter."""
        emphasis_text = EmphasisText()
        color = String().setValue("FF0000")

        result = emphasis_text.setColor(color)
        assert emphasis_text.getColor() == color
        assert result == emphasis_text

        emphasis_text.setColor(None)
        assert emphasis_text.getColor() == color

    def test_emphasis_text_font_methods(self):
        """Test the font getter and setter."""
        emphasis_text = EmphasisText()
        font = String().setValue("BOLD")

        result = emphasis_text.setFont(font)
        assert emphasis_text.getFont() == font
        assert result == emphasis_text

        emphasis_text.setFont(None)
        assert emphasis_text.getFont() == font

    def test_emphasis_text_sub_methods(self):
        """Test the sub getter and setter."""
        emphasis_text = EmphasisText()
        sub = Superscript()

        result = emphasis_text.setSub(sub)
        assert emphasis_text.getSub() == sub
        assert result == emphasis_text

        emphasis_text.setSub(None)
        assert emphasis_text.getSub() == sub

    def test_emphasis_text_sup_methods(self):
        """Test the sup getter and setter."""
        emphasis_text = EmphasisText()
        sup = Superscript()

        result = emphasis_text.setSup(sup)
        assert emphasis_text.getSup() == sup
        assert result == emphasis_text

        emphasis_text.setSup(None)
        assert emphasis_text.getSup() == sup

    def test_emphasis_text_tt_methods(self):
        """Test the tt getter and setter."""
        emphasis_text = EmphasisText()
        tt = Tt()

        result = emphasis_text.setTt(tt)
        assert emphasis_text.getTt() == tt
        assert result == emphasis_text

        emphasis_text.setTt(None)
        assert emphasis_text.getTt() == tt

    def test_emphasis_text_type_methods(self):
        """Test the type getter and setter."""
        emphasis_text = EmphasisText()
        emphasis_type = String().setValue("BOLD")

        result = emphasis_text.setType(emphasis_type)
        assert emphasis_text.getType() == emphasis_type
        assert result == emphasis_text

        emphasis_text.setType(None)
        assert emphasis_text.getType() == emphasis_type
