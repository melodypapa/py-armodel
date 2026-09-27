"""
This module contains tests for the SingleLanguageData module in MSR.Documentation.TextModel.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import (
    AtpMixedString,
)
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData import (
    SingleLanguageLongName,
)


class TestSingleLanguageLongName:
    """Test class for SingleLanguageLongName class."""

    def test_single_language_long_name_initialization(self):
        """Test that a SingleLanguageLongName object can be initialized with default values."""
        single_lang_long_name = SingleLanguageLongName()
        assert single_lang_long_name.mixedString is None
        assert single_lang_long_name.e is None
        assert single_lang_long_name.ie is None
        assert single_lang_long_name.sub is None
        assert single_lang_long_name.sup is None
        assert single_lang_long_name.tt is None

    def test_single_language_long_name_base_anchoring(self):
        """The <<atpMixedString>> mixed text rides the AtpMixedString mixin inherited from MixedContentForLongName (2026-09-27 unification)."""
        assert issubclass(SingleLanguageLongName, AtpMixedString)

    def test_single_language_long_name_mixed_string_methods(self):
        """Test the mixedString getter and setter."""
        single_lang_long_name = SingleLanguageLongName()

        result = single_lang_long_name.setMixedString("Engine")
        assert single_lang_long_name.getMixedString() == "Engine"
        assert result == single_lang_long_name

        single_lang_long_name.setMixedString(None)
        assert single_lang_long_name.getMixedString() == "Engine"
