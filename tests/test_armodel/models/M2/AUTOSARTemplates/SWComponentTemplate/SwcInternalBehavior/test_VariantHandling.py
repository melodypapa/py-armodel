"""
This module contains tests for the VariationPointProxy class in the
AUTOSAR SWComponentTemplate.SwcInternalBehavior module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import (
    VariationPointProxy,
)


class TestVariationPointProxy:
    """
    Test class for VariationPointProxy functionality.
    """

    def _make(self, short_name="TestVP"):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        return VariationPointProxy(ar_root, short_name)

    def test_initialization(self):
        obj = self._make()
        assert obj.getShortName() == "TestVP"
        assert obj.getConditionAccess() is None
        assert obj.getImplementationDataTypeRef() is None
        assert obj.getPostBuildValueAccessRef() is None
        assert obj.getPostBuildVariantConditions() == []
        assert obj.getValueAccess() is None

    def test_set_condition_access(self):
        obj = self._make()
        cond = object()
        assert obj.setConditionAccess(cond) is obj
        assert obj.getConditionAccess() is cond

    def test_set_condition_access_none_noop(self):
        obj = self._make()
        cond = object()
        obj.setConditionAccess(cond)
        obj.setConditionAccess(None)
        assert obj.getConditionAccess() is cond

    def test_set_implementation_data_type_ref(self):
        obj = self._make()
        ref = object()
        assert obj.setImplementationDataTypeRef(ref) is obj
        assert obj.getImplementationDataTypeRef() is ref

    def test_set_post_build_value_access_ref(self):
        obj = self._make()
        ref = object()
        assert obj.setPostBuildValueAccessRef(ref) is obj
        assert obj.getPostBuildValueAccessRef() is ref

    def test_post_build_variant_conditions(self):
        obj = self._make()
        cond = object()
        assert obj.addPostBuildVariantCondition(cond) is obj
        assert obj.getPostBuildVariantConditions() == [cond]

    def test_set_value_access(self):
        obj = self._make()
        val = object()
        assert obj.setValueAccess(val) is obj
        assert obj.getValueAccess() is val
