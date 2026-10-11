"""
This module contains tests for the AnyInstanceRef class in the
AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import (
    AnyInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import (
    VariationPointCapable,
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
        assert obj.getVariationPoint() is None

    def test_set_get_base_ref(self):
        obj = AnyInstanceRef()
        value = RefType().setValue("/Pkg/Base").setDest("SW-COMPONENT-PROTOTYPE")
        assert obj.setBaseRef(value) is obj
        assert obj.getBaseRef() is value
        # None is a no-op and does not overwrite an existing baseRef
        assert obj.setBaseRef(None) is obj
        assert obj.getBaseRef() is value

    def test_context_element_refs(self):
        obj = AnyInstanceRef()
        first = RefType().setValue("/Pkg/Base/Step1").setDest("SW-COMPONENT-PROTOTYPE")
        second = RefType().setValue("/Pkg/Base/Step2").setDest("SW-COMPONENT-PROTOTYPE")
        assert obj.addContextElementRef(first) is obj
        assert obj.addContextElementRef(second) is obj
        assert obj.getContextElementRefs() == [first, second]
        # None is a no-op and does not add to contextElementRefs
        assert obj.addContextElementRef(None) is obj
        assert obj.getContextElementRefs() == [first, second]

    def test_set_get_target_ref(self):
        obj = AnyInstanceRef()
        value = RefType().setValue("/Pkg/Target").setDest("R-PORT-PROTOTYPE")
        assert obj.setTargetRef(value) is obj
        assert obj.getTargetRef() is value
        # None is a no-op and does not overwrite an existing targetRef
        assert obj.setTargetRef(None) is obj
        assert obj.getTargetRef() is value

    def test_is_variation_point_capable(self):
        """Table 9.57 carries no own variationPoint row; the XSD group ANY-INSTANCE-REF
        declares VARIATION-POINT, so capability comes from the mixin (Rule 0020)."""
        assert isinstance(AnyInstanceRef(), VariationPointCapable)

    def test_variation_point_base_accessors(self):
        obj = AnyInstanceRef()
        value = object()
        assert obj.setVariationPoint(value) is obj
        assert obj.getVariationPoint() is value
        # None is a no-op and does not overwrite an existing variationPoint
        assert obj.setVariationPoint(None) is obj
        assert obj.getVariationPoint() is value
