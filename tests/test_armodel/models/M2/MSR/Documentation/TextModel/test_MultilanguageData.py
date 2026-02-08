"""
This module contains tests for the MultilanguageData module in MSR.Documentation.TextModel.
"""
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LLongName,
    LOverviewParagraph,
    LPlainText,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import *


class TestMultiLanguageParagraph:
    """Test class for MultiLanguageParagraph class."""

    def test_multi_language_paragraph_initialization(self):
        """Test that a MultiLanguageParagraph object can be initialized with default values."""
        multi_lang_paragraph = MultiLanguageParagraph()
        assert multi_lang_paragraph.l1 == []

    def test_multi_language_paragraph_l1_methods(self):
        """Test adding and getting LLongName objects."""
        multi_lang_paragraph = MultiLanguageParagraph()
        l_long_name = LLongName()

        result = multi_lang_paragraph.addL1(l_long_name)
        l1s = multi_lang_paragraph.getL1s()
        assert l_long_name in l1s
        assert result == multi_lang_paragraph


class TestMultiLanguageOverviewParagraph:
    """Test class for MultiLanguageOverviewParagraph class."""

    def test_multi_language_overview_paragraph_initialization(self):
        """Test that a MultiLanguageOverviewParagraph object can be initialized with default values."""
        multi_lang_overview_paragraph = MultiLanguageOverviewParagraph()
        assert multi_lang_overview_paragraph.l2 == []

    def test_multi_language_overview_paragraph_l2_methods(self):
        """Test adding and getting LOverviewParagraph objects."""
        multi_lang_overview_paragraph = MultiLanguageOverviewParagraph()
        l_overview_paragraph = LOverviewParagraph()

        result = multi_lang_overview_paragraph.addL2(l_overview_paragraph)
        l2s = multi_lang_overview_paragraph.getL2s()
        assert l_overview_paragraph in l2s
        assert result == multi_lang_overview_paragraph


class TestMultilanguageLongName:
    """Test class for MultilanguageLongName class."""

    def test_multilanguage_long_name_initialization(self):
        """Test that a MultilanguageLongName object can be initialized with default values."""
        multilang_long_name = MultilanguageLongName()
        assert multilang_long_name.l4 == []

    def test_multilanguage_long_name_l4_methods(self):
        """Test adding and getting LLongName objects."""
        multilang_long_name = MultilanguageLongName()
        l_long_name = LLongName()

        result = multilang_long_name.addL4(l_long_name)
        l4s = multilang_long_name.getL4s()
        assert l_long_name in l4s
        assert result == multilang_long_name


class TestMultiLanguagePlainText:
    """Test class for MultiLanguagePlainText class."""

    def test_multi_language_plain_text_initialization(self):
        """Test that a MultiLanguagePlainText object can be initialized with default values."""
        multi_lang_plain_text = MultiLanguagePlainText()
        assert multi_lang_plain_text.l10s == []

    def test_multi_language_plain_text_l10s_methods(self):
        """Test adding LPlainText objects."""
        multi_lang_plain_text = MultiLanguagePlainText()
        l_plain_text = LPlainText()

        result = multi_lang_plain_text.addL10(l_plain_text)
        l10s = multi_lang_plain_text.getL10s()
        assert l_plain_text in l10s
        assert result == multi_lang_plain_text
