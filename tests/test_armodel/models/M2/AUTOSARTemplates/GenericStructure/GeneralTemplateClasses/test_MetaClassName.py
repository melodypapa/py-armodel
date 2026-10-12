"""
This module contains tests for the MetaClassName class
in the AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    MetaClassName,
)


class TestMetaClassName:
    """
    Test class for MetaClassName functionality.
    """

    def test_initialization(self):
        meta_class_name = MetaClassName()
        assert meta_class_name is not None
        assert meta_class_name._value is None

    def test_subclass_of_arliteral(self):
        meta_class_name = MetaClassName()
        assert isinstance(meta_class_name, ARLiteral)

    def test_set_get_value(self):
        meta_class_name = MetaClassName()
        assert meta_class_name.setValue("ComM") is meta_class_name
        assert meta_class_name.getValue() == "ComM"

    def test_set_value_none_no_op(self):
        meta_class_name = MetaClassName()
        meta_class_name.setValue("ComM")
        assert meta_class_name.setValue(None) is meta_class_name
        assert meta_class_name.getValue() == "ComM"
