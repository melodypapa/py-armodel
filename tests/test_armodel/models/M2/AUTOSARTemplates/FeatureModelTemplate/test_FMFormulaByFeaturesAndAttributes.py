"""
Tests for the FMFormulaByFeaturesAndAttributes class in the
AUTOSAR FeatureModelTemplate module.
"""

import inspect
import re
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndAttributes, FMFormulaByFeaturesAndAttributes
from armodel.models.M2.AUTOSARTemplates.GenericStructure.FormulaLanguage import FormulaExpression
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import AtpMixedString


class TestFMFormulaByFeaturesAndAttributes:
    """
    Test class for FMFormulaByFeaturesAndAttributes functionality.
    The class is abstract (Table 7.1 "(abstract)" marker) — defaults and
    accessors are exercised through its concrete subclass
    FMConditionByFeaturesAndAttributes.
    """

    def test_abstract_class_not_instantiable(self):
        with pytest.raises(TypeError):
            FMFormulaByFeaturesAndAttributes()

    def test_initialization_via_concrete_subclass(self):
        obj = FMConditionByFeaturesAndAttributes()
        assert obj.getAttributeRef() is None
        assert obj.getFeatureRef() is None
        assert obj.getMixedString() is None
        assert obj.getAtpReferences() == []
        assert obj.getAtpStringReferences() == []

    def test_get_set_attribute_ref(self):
        obj = FMConditionByFeaturesAndAttributes()
        ref = RefType()
        ref.setValue("/FMAttributeDefModels/Model/AttributeA")

        assert obj.setAttributeRef(ref) is obj
        assert obj.getAttributeRef() == ref
        assert obj.setAttributeRef(None) is obj
        assert obj.getAttributeRef() == ref

    def test_get_set_feature_ref(self):
        obj = FMConditionByFeaturesAndAttributes()
        ref = RefType()
        ref.setValue("/FMFeatureModels/Model/FeatureA")

        assert obj.setFeatureRef(ref) is obj
        assert obj.getFeatureRef() == ref
        assert obj.setFeatureRef(None) is obj
        assert obj.getFeatureRef() == ref

    def test_ref_annotations(self):
        """
        Rule 0003: the 0..1 ref accessors carry the spec Optional[RefType]
        hints, resolvable at runtime on Python 3.8 (bpo-39291).
        """
        hints_get = typing.get_type_hints(FMConditionByFeaturesAndAttributes.getAttributeRef)
        assert hints_get["return"] == typing.Optional[RefType]

        hints_set = typing.get_type_hints(FMConditionByFeaturesAndAttributes.setAttributeRef)
        assert hints_set["value"] == typing.Optional[RefType]

        hints_get = typing.get_type_hints(FMConditionByFeaturesAndAttributes.getFeatureRef)
        assert hints_get["return"] == typing.Optional[RefType]

        hints_set = typing.get_type_hints(FMConditionByFeaturesAndAttributes.setFeatureRef)
        assert hints_set["value"] == typing.Optional[RefType]


class TestFMFormulaByFeaturesAndAttributesSpecContract:
    """
    Spec-contract pins for FMFormulaByFeaturesAndAttributes (R23-11
    AUTOSAR_FO_TPS_FeatureModelExchangeFormat Table 7.1, p.61). Field-to-spec
    cross-check both directions: the table has exactly two attribute rows —
    attribute (FMAttributeDef, 0..1, ref) and feature (FMFeature, 0..1, ref);
    the ref targets are missing from the model, so the fields carry RefType.
    """

    def test_class_docstring_verbatim(self):
        """
        Rule 0001.4 / 0012.2.4: class docstring == spec Table 7.1 Note verbatim.
        """
        note = "An expression that has the syntax of the AUTOSAR formula language but uses only references to features or feature attributes (not system constants) as operands."
        assert FMFormulaByFeaturesAndAttributes.__doc__ == note

    def test_exact_own_field_set(self):
        """
        Rule 0001.3 / 0001.11: Table 7.1 declares exactly two attribute rows in
        displayed order — attribute then feature — mapped to the Kind-suffixed
        fields attributeRef and featureRef.
        """
        fields = re.findall(r"self\.(\w+)\s*:", inspect.getsource(FMFormulaByFeaturesAndAttributes.__init__))
        assert fields == ["attributeRef", "featureRef"]

    def test_init_no_type_comments(self):
        """
        Rule 0003: no # type: comments anywhere in __init__.
        """
        src = inspect.getsource(FMFormulaByFeaturesAndAttributes.__init__)
        assert "# type:" not in src

    def test_base_chain(self):
        """
        Rule 0001.2: the spec Base row is ARObject, FormulaExpression — the
        most-derived base FormulaExpression is the direct Python base; the
        ARObject and AtpMixedString (<<atpMixedString>>) ancestry is in the MRO.
        """
        assert FMFormulaByFeaturesAndAttributes.__bases__ == (FormulaExpression,)
        for base in (ARObject, AtpMixedString, FormulaExpression):
            assert base in FMFormulaByFeaturesAndAttributes.__mro__

    def test_abstract_guard_message(self):
        with pytest.raises(TypeError, match="abstract class"):
            FMFormulaByFeaturesAndAttributes()

    def test_own_accessor_order(self):
        """
        Rule 0001.11: accessor pairs grouped per attribute in spec row order —
        attribute (get/set) then feature (get/set).
        """
        accessors = re.findall(r"def (get\w+|set\w+|create\w+|add\w+)", inspect.getsource(FMFormulaByFeaturesAndAttributes))
        assert accessors == ["getAttributeRef", "setAttributeRef", "getFeatureRef", "setFeatureRef"]

    def test_no_init_docstring(self):
        """Rule 0012.2.5.2: __init__ carries no docstring."""
        assert FMFormulaByFeaturesAndAttributes.__init__.__doc__ is None

    def test_concrete_subclass_rebased(self):
        """
        Rule 0001.2 / Rule 0012.3 re-base: the Table 7.2 Base row is ARObject,
        FMFormulaByFeaturesAndAttributes, FormulaExpression — once the base
        class exists, FMConditionByFeaturesAndAttributes derives from it
        (most-derived base), keeping the FormulaExpression ancestry in the MRO.
        """
        assert FMConditionByFeaturesAndAttributes.__bases__ == (FMFormulaByFeaturesAndAttributes,)
        for base in (ARObject, AtpMixedString, FormulaExpression, FMFormulaByFeaturesAndAttributes):
            assert base in FMConditionByFeaturesAndAttributes.__mro__
