"""
This module contains tests for the StrongRevisionLabelString class
in the AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    StrongRevisionLabelString,
)


class TestStrongRevisionLabelString:
    """
    Test class for StrongRevisionLabelString functionality.
    """

    def test_initialization(self):
        strong_revision_label_string = StrongRevisionLabelString()
        assert strong_revision_label_string is not None
        assert strong_revision_label_string._value is None

    def test_subclass_of_arliteral(self):
        strong_revision_label_string = StrongRevisionLabelString()
        assert isinstance(strong_revision_label_string, ARLiteral)

    def test_set_get_value(self):
        strong_revision_label_string = StrongRevisionLabelString()
        assert strong_revision_label_string.setValue("1.0.0-alpha+001") is strong_revision_label_string
        assert strong_revision_label_string.getValue() == "1.0.0-alpha+001"

    def test_set_value_none_no_op(self):
        strong_revision_label_string = StrongRevisionLabelString()
        strong_revision_label_string.setValue("1.0.0-alpha+001")
        assert strong_revision_label_string.setValue(None) is strong_revision_label_string
        assert strong_revision_label_string.getValue() == "1.0.0-alpha+001"
