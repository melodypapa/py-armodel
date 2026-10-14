"""
This module contains tests for the StrongRevisionLabelString class
in the AUTOSAR GenericStructure module.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    StrongRevisionLabelString,
)


class TestStrongRevisionLabelString:
    """
    Test class for StrongRevisionLabelString functionality (Table 4.64).
    """

    def test_initialization(self):
        strong_revision_label_string = StrongRevisionLabelString()
        assert strong_revision_label_string is not None
        assert strong_revision_label_string._value is None

    def test_subclass_of_arliteral(self):
        strong_revision_label_string = StrongRevisionLabelString()
        assert isinstance(strong_revision_label_string, ARLiteral)

    def test_set_value(self):
        strong_revision_label_string = StrongRevisionLabelString().setValue("1.0.0-alpha+001")
        assert strong_revision_label_string.getValue() == "1.0.0-alpha+001"

    @pytest.mark.parametrize(
        "pattern_value",
        [
            "1.0.0-alpha+001",
            "1.0.0+20130313144700",
            "1.0.0-beta+exp.sha.5114f85",
            "1.0.0",
            "0.0.0",
        ],
    )
    def test_pattern_value_round_trip(self, pattern_value):
        """
        The first three values are the Table 4.64 Note's own `Legal patterns are for example:` list;
        the last two exercise the bare three-integer form the Note describes (MajorVersion.MinorVersion.PatchVersion).
        Each satisfies the XSD `STRONG-REVISION-LABEL-STRING--SIMPLE` `xsd:pattern` facet.
        """
        strong_revision_label_string = StrongRevisionLabelString()
        result = strong_revision_label_string.setValue(pattern_value)
        assert result is strong_revision_label_string
        assert strong_revision_label_string.getValue() == pattern_value

    def test_set_get_value(self):
        strong_revision_label_string = StrongRevisionLabelString()
        assert strong_revision_label_string.setValue("1.0.0-alpha+001") is strong_revision_label_string
        assert strong_revision_label_string.getValue() == "1.0.0-alpha+001"

    def test_set_value_none_no_op(self):
        strong_revision_label_string = StrongRevisionLabelString()
        strong_revision_label_string.setValue("1.0.0-alpha+001")
        assert strong_revision_label_string.setValue(None) is strong_revision_label_string
        assert strong_revision_label_string.getValue() == "1.0.0-alpha+001"
