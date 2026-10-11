"""
This module contains tests for the CIdentifierWithIndex class
in the AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    CIdentifierWithIndex,
)


class TestCIdentifierWithIndex:
    """
    Test class for CIdentifierWithIndex functionality.
    """

    def test_initialization(self):
        c_identifier_with_index = CIdentifierWithIndex()
        assert c_identifier_with_index is not None
        assert c_identifier_with_index._value is None

    def test_subclass_of_arliteral(self):
        c_identifier_with_index = CIdentifierWithIndex()
        assert isinstance(c_identifier_with_index, ARLiteral)

    def test_set_get_value(self):
        c_identifier_with_index = CIdentifierWithIndex()
        assert c_identifier_with_index.setValue("MotorSpeed[3]") is c_identifier_with_index
        assert c_identifier_with_index.getValue() == "MotorSpeed[3]"

    def test_set_value_none_no_op(self):
        c_identifier_with_index = CIdentifierWithIndex()
        c_identifier_with_index.setValue("MotorSpeed[3]")
        assert c_identifier_with_index.setValue(None) is c_identifier_with_index
        assert c_identifier_with_index.getValue() == "MotorSpeed[3]"
