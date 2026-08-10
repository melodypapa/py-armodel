"""
This module contains tests for the LanguageDataModel module in MSR.Documentation.TextModel.
"""

import pytest

from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import EmphasisText, IndexEntry, Superscript, Tt
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LanguageSpecific,
    LEnum,
    LLongName,
    LOverviewParagraph,
    LParagraph,
    LPlainText,
)


class TestLEnum:
    """Test class for LEnum class."""

    def test_l_enum_members(self):
        """Test that LEnum has the expected members."""
        assert LEnum.AA == "aa"
        assert LEnum.EN == "en"
        assert LEnum.DE == "de"
        assert LEnum.FOR_ALL == "forAll"

    def test_l_enum_values(self):
        """Test that LEnum values are all valid."""
        l_enum = LEnum()
        assert l_enum.validateEnumValue("en")
        assert l_enum.validateEnumValue("de")
        assert not l_enum.validateEnumValue("xx")

    def test_l_enum_initialization(self):
        """Test that an LEnum object can be initialized."""
        l_enum = LEnum()
        assert l_enum is not None


class TestLanguageSpecific:
    """Test class for LanguageSpecific abstract class."""

    def test_language_specific_abstract_class(self):
        """Test that LanguageSpecific cannot be instantiated directly."""
        # This should raise NotImplementedError
        with pytest.raises(TypeError):
            LanguageSpecific()

    def test_language_specific_initialization(self):
        """Test that a concrete subclass can be initialized with default values."""

        # Create a concrete subclass for testing
        class ConcreteLanguageSpecific(LanguageSpecific):
            def __init__(self):
                super().__init__()

        concrete_lang_spec = ConcreteLanguageSpecific()
        assert concrete_lang_spec.l is None
        assert concrete_lang_spec.value == ""

    def test_language_specific_l_methods(self):
        """Test the l getter and setter."""

        class ConcreteLanguageSpecific(LanguageSpecific):
            def __init__(self):
                super().__init__()

        concrete_lang_spec = ConcreteLanguageSpecific()
        l_val = LEnum()

        result = concrete_lang_spec.setL(l_val)
        assert concrete_lang_spec.getL() == l_val
        assert result == concrete_lang_spec

        concrete_lang_spec.setL(None)
        assert concrete_lang_spec.getL() == l_val

    def test_language_specific_value_methods(self):
        """Test the value getter and setter."""

        class ConcreteLanguageSpecific(LanguageSpecific):
            def __init__(self):
                super().__init__()

        concrete_lang_spec = ConcreteLanguageSpecific()
        value = "test_value"

        result = concrete_lang_spec.setValue(value)
        assert concrete_lang_spec.getValue() == value
        assert result == concrete_lang_spec

        concrete_lang_spec.setValue(None)
        assert concrete_lang_spec.getValue() == value


class TestLOverviewParagraph:
    """Test class for LOverviewParagraph class."""

    def test_l_overview_paragraph_initialization(self):
        """Test that an LOverviewParagraph object can be initialized."""
        l_overview_paragraph = LOverviewParagraph()
        assert l_overview_paragraph.l is None
        assert l_overview_paragraph.value == ""


class TestLParagraph:
    """Test class for LParagraph class."""

    def test_l_paragraph_initialization(self):
        """Test that an LParagraph object can be initialized."""
        l_paragraph = LParagraph()
        assert l_paragraph.l is None
        assert l_paragraph.value == ""


class TestLLongName:
    """Test class for LLongName class."""

    def test_l_long_name_initialization(self):
        """Test that an LLongName object can be initialized."""
        l_long_name = LLongName()
        assert l_long_name.l is None
        assert l_long_name.value == ""
        assert l_long_name.e is None
        assert l_long_name.ie is None
        assert l_long_name.sub is None
        assert l_long_name.sup is None
        assert l_long_name.tt is None
        assert l_long_name.blueprintValue is None

    def test_l_long_name_e_methods(self):
        """Test the e getter and setter."""
        l_long_name = LLongName()
        e = EmphasisText()

        result = l_long_name.setE(e)
        assert l_long_name.getE() == e
        assert result == l_long_name

        l_long_name.setE(None)
        assert l_long_name.getE() == e

    def test_l_long_name_ie_methods(self):
        """Test the ie getter and setter."""
        l_long_name = LLongName()
        ie = IndexEntry()

        result = l_long_name.setIe(ie)
        assert l_long_name.getIe() == ie
        assert result == l_long_name

        l_long_name.setIe(None)
        assert l_long_name.getIe() == ie

    def test_l_long_name_sub_methods(self):
        """Test the sub getter and setter."""
        l_long_name = LLongName()
        sub = Superscript()

        result = l_long_name.setSub(sub)
        assert l_long_name.getSub() == sub
        assert result == l_long_name

        l_long_name.setSub(None)
        assert l_long_name.getSub() == sub

    def test_l_long_name_sup_methods(self):
        """Test the sup getter and setter."""
        l_long_name = LLongName()
        sup = Superscript()

        result = l_long_name.setSup(sup)
        assert l_long_name.getSup() == sup
        assert result == l_long_name

        l_long_name.setSup(None)
        assert l_long_name.getSup() == sup

    def test_l_long_name_tt_methods(self):
        """Test the tt getter and setter."""
        l_long_name = LLongName()
        tt = Tt()

        result = l_long_name.setTt(tt)
        assert l_long_name.getTt() == tt
        assert result == l_long_name

        l_long_name.setTt(None)
        assert l_long_name.getTt() == tt

    def test_l_long_name_blueprint_value_methods(self):
        """Test the blueprintValue getter and setter."""
        l_long_name = LLongName()
        value = "StringName"

        result = l_long_name.setBlueprintValue(value)
        assert l_long_name.getBlueprintValue() == value
        assert result == l_long_name

        l_long_name.setBlueprintValue(None)
        assert l_long_name.getBlueprintValue() == value


class TestLPlainText:
    """Test class for LPlainText class."""

    def test_l_plain_text_initialization(self):
        """Test that an LPlainText object can be initialized."""
        l_plain_text = LPlainText()
        assert l_plain_text.l is None
        assert l_plain_text.value == ""
