"""Tests for the VariationPointProxy class."""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import ConditionByFormula, PostBuildVariantCondition
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import VariationPointProxy


class TestVariationPointProxy:
    """Tests for VariationPointProxy."""

    def _make(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        return VariationPointProxy(ar_root, "TestVariationPointProxy")

    def test_initialization(self):
        proxy = self._make()
        assert proxy.conditionAccess is None
        assert proxy.implementationDataTypeRef is None
        assert proxy.postBuildValueAccessRef is None
        assert proxy.postBuildVariantConditions == []
        assert proxy.valueAccess is None

    def test_get_set_condition_access(self):
        proxy = self._make()
        value = ConditionByFormula()
        assert proxy.setConditionAccess(value) is proxy
        assert proxy.getConditionAccess() is value
        proxy.setConditionAccess(None)
        assert proxy.getConditionAccess() is value

    def test_get_set_implementation_data_type_ref(self):
        proxy = self._make()
        value = RefType()
        value.setValue("/impl")
        assert proxy.setImplementationDataTypeRef(value) is proxy
        assert proxy.getImplementationDataTypeRef() is value
        proxy.setImplementationDataTypeRef(None)
        assert proxy.getImplementationDataTypeRef() is value

    def test_get_set_post_build_value_access_ref(self):
        proxy = self._make()
        value = RefType()
        value.setValue("/pb")
        assert proxy.setPostBuildValueAccessRef(value) is proxy
        assert proxy.getPostBuildValueAccessRef() is value
        proxy.setPostBuildValueAccessRef(None)
        assert proxy.getPostBuildValueAccessRef() is value

    def test_add_get_post_build_variant_conditions(self):
        proxy = self._make()
        value = PostBuildVariantCondition()
        assert proxy.addPostBuildVariantCondition(value) is proxy
        assert proxy.getPostBuildVariantConditions() == [value]
        proxy.addPostBuildVariantCondition(None)
        assert proxy.getPostBuildVariantConditions() == [value]

    def test_get_set_value_access(self):
        proxy = self._make()
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps

        value = SwDataDefProps()
        assert proxy.setValueAccess(value) is proxy
        assert proxy.getValueAccess() is value
        proxy.setValueAccess(None)
        assert proxy.getValueAccess() is value
