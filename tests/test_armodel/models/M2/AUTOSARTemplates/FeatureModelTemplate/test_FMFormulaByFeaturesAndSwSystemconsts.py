"""
Tests for the FMFormulaByFeaturesAndSwSystemconsts class in the
AUTOSAR FeatureModelTemplate module.
"""

import inspect
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMFormulaByFeaturesAndSwSystemconsts
from armodel.models.M2.AUTOSARTemplates.GenericStructure.FormulaLanguage import FormulaExpression
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import AtpMixedString
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import SwSystemconstDependentFormula


class _ConcreteFormula(FMFormulaByFeaturesAndSwSystemconsts):
    """Test vehicle: the concrete subclass FMConditionByFeaturesAndSwSystemconsts (Table 7.4) is not yet synced, so the abstract base is exercised through a minimal concrete subclass."""

    pass


class TestFMFormulaByFeaturesAndSwSystemconsts:
    """
    Test class for FMFormulaByFeaturesAndSwSystemconsts functionality.
    The class is abstract (Table 7.3 "(abstract)" marker) — defaults and
    accessors are exercised through a minimal concrete subclass until the
    Table 7.4 concrete subclass is synced.
    """

    def test_abstract_class_not_instantiable(self):
        with pytest.raises(TypeError):
            FMFormulaByFeaturesAndSwSystemconsts()

    def test_initialization_via_concrete_subclass(self):
        obj = _ConcreteFormula()
        assert obj.getFeatureRef() is None
        assert obj.getMixedString() is None
        assert obj.getAtpReferences() == []
        assert obj.getAtpStringReferences() is None or obj.getAtpStringReferences() == []

    def test_base_chain(self):
        assert issubclass(FMFormulaByFeaturesAndSwSystemconsts, SwSystemconstDependentFormula)
        assert issubclass(FMFormulaByFeaturesAndSwSystemconsts, FormulaExpression)
        assert issubclass(FMFormulaByFeaturesAndSwSystemconsts, AtpMixedString)

    def test_get_set_feature_ref(self):
        obj = _ConcreteFormula()
        ref = RefType()
        ref.setValue("/FMFeatureModels/Model/FeatureA")

        assert obj.setFeatureRef(ref) is obj
        assert obj.getFeatureRef() == ref
        assert obj.setFeatureRef(None) is obj
        assert obj.getFeatureRef() == ref

    def test_accessor_annotations(self):
        hints = typing.get_type_hints(_ConcreteFormula.getFeatureRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(_ConcreteFormula.setFeatureRef)
        assert hints["value"] == typing.Optional[RefType]

    def test_spec_note(self):
        source = inspect.getsource(FMFormulaByFeaturesAndSwSystemconsts)
        assert '"""An expression that has the syntax of the AUTOSAR formula language and may use references to features or system constants as operands.' in source
        assert "[constr_3667]" in source
        assert "the reference in the role feature shall exist" in source

    def test_feature_ref_docstring(self):
        source = inspect.getsource(_ConcreteFormula.getFeatureRef)
        assert "An expression of type FMFormulaByFeaturesAndSwSystemconsts may refer to FMFeatures." in source
