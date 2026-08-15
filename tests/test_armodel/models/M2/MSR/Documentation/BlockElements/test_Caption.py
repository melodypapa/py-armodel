"""This module contains tests for the Caption module in MSR.Documentation.BlockElements."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.MSR.Documentation.BlockElements import Caption
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultiLanguageOverviewParagraph,
)


class TestCaption:
    """Test class for Caption class."""

    def test_caption_initialization(self):
        """Test that a Caption object can be initialized with default values."""
        parent_obj = ARPackage(None, "parent_test")
        caption = Caption(parent_obj, "test_name")
        assert caption.desc is None

    def test_caption_desc_methods(self):
        """Test the desc getter and setter."""
        parent_obj = ARPackage(None, "parent_test")
        caption = Caption(parent_obj, "test_name")
        desc = MultiLanguageOverviewParagraph()

        result = caption.setDesc(desc)
        assert caption.getDesc() == desc
        assert result == caption

        caption.setDesc(None)
        assert caption.getDesc() == desc
