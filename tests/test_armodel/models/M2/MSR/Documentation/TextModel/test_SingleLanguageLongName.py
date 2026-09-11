"""
This module contains tests for the SingleLanguageData module in MSR.Documentation.TextModel.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData import (
    SingleLanguageLongName,
)


class TestSingleLanguageLongName:
    """Test class for SingleLanguageLongName class."""

    def test_single_language_long_name_initialization(self):
        """Test that a SingleLanguageLongName object can be initialized with default values."""
        single_lang_long_name = SingleLanguageLongName()
        assert single_lang_long_name.value is None
        assert single_lang_long_name.e is None
        assert single_lang_long_name.ie is None
        assert single_lang_long_name.sub is None
        assert single_lang_long_name.sup is None
        assert single_lang_long_name.tt is None

    def test_single_language_long_name_value_methods(self):
        """Test the value getter and setter."""
        single_lang_long_name = SingleLanguageLongName()
        value = String().setValue("Engine")

        result = single_lang_long_name.setValue(value)
        assert single_lang_long_name.getValue() == value
        assert result == single_lang_long_name

        single_lang_long_name.setValue(None)
        assert single_lang_long_name.getValue() == value
