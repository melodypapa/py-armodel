"""
This module contains tests for the AnyInstanceRef class in the
AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import (
    AnyInstanceRef,
)


class TestAnyInstanceRef:
    """
    Test class for AnyInstanceRef functionality.
    """

    def test_initialization(self):
        obj = AnyInstanceRef()
        assert obj.getBaseRef() is None
        assert obj.getContextElementRefs() == []
        assert obj.getTargetRef() is None

    def test_set_get_base_ref(self):
        obj = AnyInstanceRef()
        assert obj.setBaseRef("base") is obj
        assert obj.getBaseRef() == "base"

    def test_context_element_refs(self):
        obj = AnyInstanceRef()
        assert obj.addContextElementRef("ctx") is obj
        assert obj.getContextElementRefs() == ["ctx"]

    def test_set_get_target_ref(self):
        obj = AnyInstanceRef()
        assert obj.setTargetRef("target") is obj
        assert obj.getTargetRef() == "target"
