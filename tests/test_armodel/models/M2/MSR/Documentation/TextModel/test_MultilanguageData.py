"""
This module contains tests for the MultilanguageData module in MSR.Documentation.TextModel.
"""

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LLongName,
    LOverviewParagraph,
    LPlainText,
    LVerbatim,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultilanguageLongName,
    MultiLanguageOverviewParagraph,
    MultiLanguageParagraph,
    MultiLanguagePlainText,
    MultiLanguageVerbatim,
)


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


class TestMultiLanguageVerbatim:
    """Test class for MultiLanguageVerbatim class."""

    def test_multi_language_verbatim_initialization(self):
        """Test that a MultiLanguageVerbatim object can be initialized with default values."""
        multi_lang_verbatim = MultiLanguageVerbatim()
        assert multi_lang_verbatim.allowBreak is None
        assert multi_lang_verbatim.helpEntry is None
        assert multi_lang_verbatim.float is None
        assert multi_lang_verbatim.pgwide is None
        assert multi_lang_verbatim.l5s == []

    def test_multi_language_verbatim_l5s_methods(self):
        """Test adding LVerbatim objects."""
        multi_lang_verbatim = MultiLanguageVerbatim()
        l_verbatim = LVerbatim()

        result = multi_lang_verbatim.addL5(l_verbatim)
        l5s = multi_lang_verbatim.getL5s()
        assert l_verbatim in l5s
        assert result == multi_lang_verbatim

        multi_lang_verbatim.addL5(None)
        assert multi_lang_verbatim.getL5s() == [l_verbatim]

    def test_multi_language_verbatim_allow_break_methods(self):
        """Test the allowBreak getter and setter."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken

        multi_lang_verbatim = MultiLanguageVerbatim()
        allow_break = NameToken().setValue("1")

        result = multi_lang_verbatim.setAllowBreak(allow_break)
        assert multi_lang_verbatim.getAllowBreak() == allow_break
        assert result == multi_lang_verbatim

        multi_lang_verbatim.setAllowBreak(None)
        assert multi_lang_verbatim.getAllowBreak() == allow_break

    def test_multi_language_verbatim_help_entry_methods(self):
        """Test the helpEntry getter and setter."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String

        multi_lang_verbatim = MultiLanguageVerbatim()
        help_entry = String().setValue("help")

        result = multi_lang_verbatim.setHelpEntry(help_entry)
        assert multi_lang_verbatim.getHelpEntry() == help_entry
        assert result == multi_lang_verbatim

        multi_lang_verbatim.setHelpEntry(None)
        assert multi_lang_verbatim.getHelpEntry() == help_entry

    def test_multi_language_verbatim_float_methods(self):
        """Test the float getter and setter."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral

        multi_lang_verbatim = MultiLanguageVerbatim()
        float_value = ARLiteral().setValue("no")

        result = multi_lang_verbatim.setFloat(float_value)
        assert multi_lang_verbatim.getFloat() == float_value
        assert result == multi_lang_verbatim

        multi_lang_verbatim.setFloat(None)
        assert multi_lang_verbatim.getFloat() == float_value

    def test_multi_language_verbatim_pgwide_methods(self):
        """Test the pgwide getter and setter."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral

        multi_lang_verbatim = MultiLanguageVerbatim()
        pgwide = ARLiteral().setValue("noPgwide")

        result = multi_lang_verbatim.setPgwide(pgwide)
        assert multi_lang_verbatim.getPgwide() == pgwide
        assert result == multi_lang_verbatim

        multi_lang_verbatim.setPgwide(None)
        assert multi_lang_verbatim.getPgwide() == pgwide
