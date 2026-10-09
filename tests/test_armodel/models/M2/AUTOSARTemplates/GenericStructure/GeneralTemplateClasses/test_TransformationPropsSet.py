"""
This module contains tests for the TransformationPropsSet class in the
AUTOSAR GenericStructure.GeneralTemplateClasses.ARPackage module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    TransformationPropsSet,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    SOMEIPTransformationProps,
    UserDefinedTransformationProps,
)


class TestTransformationPropsSet:
    """
    Test class for TransformationPropsSet functionality.
    """

    def test_initialization(self):
        obj = TransformationPropsSet(None, "Test")
        assert isinstance(obj, TransformationPropsSet)
        assert obj.getTransformationProps() == []

    def test_create_someip_transformation_props(self):
        obj = TransformationPropsSet(None, "Test")
        child = obj.createSOMEIPTransformationProps("Props1")
        assert isinstance(child, SOMEIPTransformationProps)
        assert child.getParent() is obj
        assert obj.getTransformationProps() == [child]

    def test_create_user_defined_transformation_props(self):
        obj = TransformationPropsSet(None, "Test")
        child = obj.createUserDefinedTransformationProps("Props2")
        assert isinstance(child, UserDefinedTransformationProps)
        assert child.getParent() is obj
        assert obj.getTransformationProps() == [child]

    def test_create_appends_multiple_props(self):
        obj = TransformationPropsSet(None, "Test")
        first = obj.createSOMEIPTransformationProps("Props1")
        second = obj.createUserDefinedTransformationProps("Props2")
        assert obj.getTransformationProps() == [first, second]
