"""
Tests for the FMConditionByFeaturesAndSwSystemconsts class in the
AUTOSAR FeatureModelTemplate module.
"""

import inspect

from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndSwSystemconsts, FMFormulaByFeaturesAndSwSystemconsts
from armodel.models.M2.AUTOSARTemplates.GenericStructure.FormulaLanguage import FormulaExpression
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import SwSystemconstDependentFormula


class TestFMConditionByFeaturesAndSwSystemconsts:
    """
    Test class for FMConditionByFeaturesAndSwSystemconsts functionality.
    Table 7.4 is a concrete class with zero attribute rows (dash placeholder) —
    the member surface is entirely inherited from the Table 7.3 base
    (featureRef) and SwSystemconstDependentFormula (syscRef/syscStringRef).
    """

    def test_instantiable(self):
        obj = FMConditionByFeaturesAndSwSystemconsts()
        assert obj.getFeatureRef() is None
        assert obj.getSyscRef() is None
        assert obj.getSyscStringRef() is None
        assert obj.getMixedString() is None

    def test_base_chain(self):
        assert issubclass(FMConditionByFeaturesAndSwSystemconsts, FMFormulaByFeaturesAndSwSystemconsts)
        assert issubclass(FMConditionByFeaturesAndSwSystemconsts, SwSystemconstDependentFormula)
        assert issubclass(FMConditionByFeaturesAndSwSystemconsts, FormulaExpression)

    def test_no_own_members_beyond_inherited(self):
        source = inspect.getsource(FMConditionByFeaturesAndSwSystemconsts)
        assert "self.featureRef" not in source
        assert "self.syscRef" not in source

    def test_get_set_feature_ref(self):
        obj = FMConditionByFeaturesAndSwSystemconsts()
        ref = RefType()
        ref.setValue("/FMFeatureModels/Model/FeatureA")

        assert obj.setFeatureRef(ref) is obj
        assert obj.getFeatureRef() == ref

    def test_spec_note(self):
        source = inspect.getsource(FMConditionByFeaturesAndSwSystemconsts)
        assert '"""A boolean expression that has the syntax of the AUTOSAR formula language and may use references to features or system constants as operands.' in source
        assert "[TPS_FMDT_00050]" in source
