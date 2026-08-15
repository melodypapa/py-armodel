"""
This module contains tests for the Ecuc* classes in the
AUTOSAR ECUCParameterDefTemplate module.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucAbstractConfigurationClass,
    EcucAbstractExternalReferenceDef,
    EcucAbstractInternalReferenceDef,
    EcucAbstractReferenceDef,
    EcucAbstractStringParamDef,
    EcucAddInfoParamDef,
    EcucBooleanParamDef,
    EcucChoiceContainerDef,
    EcucChoiceReferenceDef,
    EcucCommonAttributes,
    EcucConditionFormula,
    EcucConditionSpecification,
    EcucConfigurationClassEnum,
    EcucConfigurationVariantEnum,
    EcucContainerDef,
    EcucDefinitionCollection,
    EcucDefinitionElement,
    EcucDerivationSpecification,
    EcucDestinationUriDef,
    EcucDestinationUriDefRefType,
    EcucDestinationUriDefSet,
    EcucDestinationUriPolicy,
    EcucEnumerationLiteralDef,
    EcucEnumerationParamDef,
    EcucFloatParamDef,
    EcucForeignReferenceDef,
    EcucFunctionNameDef,
    EcucInstanceReferenceDef,
    EcucIntegerParamDef,
    EcucLinkerSymbolDef,
    EcucModuleDef,
    EcucMultilineStringParamDef,
    EcucMultiplicityConfigurationClass,
    EcucParamConfContainerDef,
    EcucParameterDef,
    EcucParameterDerivationFormula,
    EcucQuery,
    EcucQueryExpression,
    EcucReferenceDef,
    EcucScopeEnum,
    EcucStringParamDef,
    EcucSymbolicNameReferenceDef,
    EcucUriReferenceDef,
    EcucValidationCondition,
    EcucValueConfigurationClass,
)


def _instantiate(cls, name="sn"):
    return cls(AUTOSAR.getInstance().createARPackage("Pkg_" + cls.__name__), name)


class TestEcucValidationCondition:
    def test_instantiation(self):
        assert _instantiate(EcucValidationCondition, "EcucValidationCondition").getShortName() == "EcucValidationCondition"


class TestEcucSymbolicNameReferenceDef:
    def test_instantiation(self):
        assert _instantiate(EcucSymbolicNameReferenceDef, "EcucSymbolicNameReferenceDef").getShortName() == "EcucSymbolicNameReferenceDef"


class TestEcucChoiceReferenceDef:
    def test_instantiation(self):
        assert _instantiate(EcucChoiceReferenceDef, "EcucChoiceReferenceDef").getShortName() == "EcucChoiceReferenceDef"


class TestEcucReferenceDef:
    def test_instantiation(self):
        assert _instantiate(EcucReferenceDef, "EcucReferenceDef").getShortName() == "EcucReferenceDef"


class TestEcucUriReferenceDef:
    def test_instantiation(self):
        assert _instantiate(EcucUriReferenceDef, "EcucUriReferenceDef").getShortName() == "EcucUriReferenceDef"


class TestEcucForeignReferenceDef:
    def test_instantiation(self):
        assert _instantiate(EcucForeignReferenceDef, "EcucForeignReferenceDef").getShortName() == "EcucForeignReferenceDef"


class TestEcucInstanceReferenceDef:
    def test_instantiation(self):
        assert _instantiate(EcucInstanceReferenceDef, "EcucInstanceReferenceDef").getShortName() == "EcucInstanceReferenceDef"


class TestEcucStringParamDef:
    def test_instantiation(self):
        assert _instantiate(EcucStringParamDef, "EcucStringParamDef").getShortName() == "EcucStringParamDef"


class TestEcucFunctionNameDef:
    def test_instantiation(self):
        assert _instantiate(EcucFunctionNameDef, "EcucFunctionNameDef").getShortName() == "EcucFunctionNameDef"


class TestEcucIntegerParamDef:
    def test_instantiation(self):
        assert _instantiate(EcucIntegerParamDef, "EcucIntegerParamDef").getShortName() == "EcucIntegerParamDef"


class TestEcucEnumerationLiteralDef:
    def test_instantiation(self):
        assert _instantiate(EcucEnumerationLiteralDef, "EcucEnumerationLiteralDef").getShortName() == "EcucEnumerationLiteralDef"


class TestEcucEnumerationParamDef:
    def test_instantiation(self):
        assert _instantiate(EcucEnumerationParamDef, "EcucEnumerationParamDef").getShortName() == "EcucEnumerationParamDef"


class TestEcucFloatParamDef:
    def test_instantiation(self):
        assert _instantiate(EcucFloatParamDef, "EcucFloatParamDef").getShortName() == "EcucFloatParamDef"


class TestEcucChoiceContainerDef:
    def test_instantiation(self):
        assert _instantiate(EcucChoiceContainerDef, "EcucChoiceContainerDef").getShortName() == "EcucChoiceContainerDef"


class TestEcucParamConfContainerDef:
    def test_instantiation(self):
        assert _instantiate(EcucParamConfContainerDef, "EcucParamConfContainerDef").getShortName() == "EcucParamConfContainerDef"


class TestEcucAddInfoParamDef:
    def test_instantiation(self):
        assert _instantiate(EcucAddInfoParamDef, "EcucAddInfoParamDef").getShortName() == "EcucAddInfoParamDef"


class TestEcucDefinitionCollection:
    def test_instantiation(self):
        assert _instantiate(EcucDefinitionCollection, "EcucDefinitionCollection").getShortName() == "EcucDefinitionCollection"


class TestEcucDestinationUriDef:
    def test_instantiation(self):
        assert _instantiate(EcucDestinationUriDef, "EcucDestinationUriDef").getShortName() == "EcucDestinationUriDef"


class TestEcucDestinationUriDefSet:
    def test_instantiation(self):
        assert _instantiate(EcucDestinationUriDefSet, "EcucDestinationUriDefSet").getShortName() == "EcucDestinationUriDefSet"


class TestEcucQuery:
    def test_instantiation(self):
        assert _instantiate(EcucQuery, "EcucQuery").getShortName() == "EcucQuery"


class TestEcucModuleDef:
    def test_instantiation(self):
        assert _instantiate(EcucModuleDef, "EcucModuleDef").getShortName() == "EcucModuleDef"


class TestEcucBooleanParamDef:
    def test_instantiation(self):
        assert _instantiate(EcucBooleanParamDef, "EcucBooleanParamDef").getShortName() == "EcucBooleanParamDef"


class TestEcucLinkerSymbolDef:
    def test_instantiation(self):
        assert _instantiate(EcucLinkerSymbolDef, "EcucLinkerSymbolDef").getShortName() == "EcucLinkerSymbolDef"


class TestEcucMultilineStringParamDef:
    def test_instantiation(self):
        assert _instantiate(EcucMultilineStringParamDef, "EcucMultilineStringParamDef").getShortName() == "EcucMultilineStringParamDef"


class TestEcucDestinationUriDefRefType:
    def test_instantiation(self):
        assert isinstance(EcucDestinationUriDefRefType(), EcucDestinationUriDefRefType)


class TestEcucConfigurationClassEnum:
    def test_instantiation(self):
        assert isinstance(EcucConfigurationClassEnum(), EcucConfigurationClassEnum)


class TestEcucConfigurationVariantEnum:
    def test_instantiation(self):
        assert isinstance(EcucConfigurationVariantEnum(), EcucConfigurationVariantEnum)


class TestEcucMultiplicityConfigurationClass:
    def test_instantiation(self):
        assert isinstance(EcucMultiplicityConfigurationClass(), EcucMultiplicityConfigurationClass)


class TestEcucValueConfigurationClass:
    def test_instantiation(self):
        assert isinstance(EcucValueConfigurationClass(), EcucValueConfigurationClass)


class TestEcucDerivationSpecification:
    def test_instantiation(self):
        assert isinstance(EcucDerivationSpecification(), EcucDerivationSpecification)


class TestEcucConditionFormula:
    def test_instantiation(self):
        assert isinstance(EcucConditionFormula(), EcucConditionFormula)


class TestEcucDestinationUriPolicy:
    def test_instantiation(self):
        assert isinstance(EcucDestinationUriPolicy(), EcucDestinationUriPolicy)


class TestEcucParameterDerivationFormula:
    def test_instantiation(self):
        assert isinstance(EcucParameterDerivationFormula(), EcucParameterDerivationFormula)


class TestEcucQueryExpression:
    def test_instantiation(self):
        assert isinstance(EcucQueryExpression(), EcucQueryExpression)


class TestEcucConditionSpecification:
    def test_instantiation(self):
        assert isinstance(EcucConditionSpecification(), EcucConditionSpecification)


class TestEcucScopeEnum:
    def test_instantiation(self):
        assert isinstance(EcucScopeEnum(), EcucScopeEnum)


class TestEcucDefinitionElement:
    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            _instantiate(EcucDefinitionElement)


class TestEcucContainerDef:
    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            _instantiate(EcucContainerDef)


class TestEcucCommonAttributes:
    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            _instantiate(EcucCommonAttributes)

    def _make(self):
        class _Concrete(EcucCommonAttributes):
            pass

        return _Concrete(AUTOSAR.getInstance().createARPackage("Pkg_TestECA"), "sn")

    def test_initialization_defaults(self):
        obj = self._make()
        assert obj.getMultiplicityConfigClasses() == []
        assert obj.getOrigin() is None
        assert obj.getPostBuildVariantMultiplicity() is None
        assert obj.getPostBuildVariantValue() is None
        assert obj.getRequiresIndex() is None
        assert obj.getValueConfigClasses() == []

    def test_get_set_origin_roundtrip(self):
        obj = self._make()
        assert obj.setOrigin("AUTOSAR_ECUC") is obj
        assert obj.getOrigin() == "AUTOSAR_ECUC"

    def test_set_origin_none_noop(self):
        obj = self._make()
        obj.setOrigin("AUTOSAR_ECUC")
        obj.setOrigin(None)
        assert obj.getOrigin() == "AUTOSAR_ECUC"

    def test_get_set_post_build_variant_multiplicity_roundtrip(self):
        obj = self._make()
        assert obj.setPostBuildVariantMultiplicity(True) is obj
        assert obj.getPostBuildVariantMultiplicity() is True

    def test_set_post_build_variant_multiplicity_none_noop(self):
        obj = self._make()
        obj.setPostBuildVariantMultiplicity(True)
        obj.setPostBuildVariantMultiplicity(None)
        assert obj.getPostBuildVariantMultiplicity() is True

    def test_get_set_post_build_variant_value_roundtrip(self):
        obj = self._make()
        assert obj.setPostBuildVariantValue(False) is obj
        assert obj.getPostBuildVariantValue() is False

    def test_set_post_build_variant_value_none_noop(self):
        obj = self._make()
        obj.setPostBuildVariantValue(False)
        obj.setPostBuildVariantValue(None)
        assert obj.getPostBuildVariantValue() is False

    def test_get_set_requires_index_roundtrip(self):
        obj = self._make()
        assert obj.setRequiresIndex(True) is obj
        assert obj.getRequiresIndex() is True

    def test_set_requires_index_none_noop(self):
        obj = self._make()
        obj.setRequiresIndex(True)
        obj.setRequiresIndex(None)
        assert obj.getRequiresIndex() is True

    def test_add_multiplicity_config_class(self):
        obj = self._make()
        item = EcucMultiplicityConfigurationClass()
        assert obj.addMultiplicityConfigClass(item) is obj
        assert obj.getMultiplicityConfigClasses() == [item]

    def test_add_multiplicity_config_class_none_noop(self):
        obj = self._make()
        obj.addMultiplicityConfigClass(None)
        assert obj.getMultiplicityConfigClasses() == []

    def test_add_value_config_class(self):
        obj = self._make()
        item = EcucValueConfigurationClass()
        assert obj.addValueConfigClass(item) is obj
        assert obj.getValueConfigClasses() == [item]

    def test_add_value_config_class_none_noop(self):
        obj = self._make()
        obj.addValueConfigClass(None)
        assert obj.getValueConfigClasses() == []


class TestEcucParameterDef:
    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            _instantiate(EcucParameterDef)


class TestEcucAbstractReferenceDef:
    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            _instantiate(EcucAbstractReferenceDef)


class TestEcucAbstractInternalReferenceDef:
    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            _instantiate(EcucAbstractInternalReferenceDef)


class TestEcucAbstractExternalReferenceDef:
    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            _instantiate(EcucAbstractExternalReferenceDef)


class TestEcucAbstractStringParamDef:
    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            _instantiate(EcucAbstractStringParamDef)

    def _make(self):
        class _Concrete(EcucAbstractStringParamDef):
            pass

        return _Concrete(AUTOSAR.getInstance().createARPackage("Pkg_TestEASPD"), "sn")

    def test_initialization_defaults(self):
        obj = self._make()
        assert obj.getDefaultValue() is None
        assert obj.getMaxLength() is None
        assert obj.getMinLength() is None
        assert obj.getRegularExpression() is None

    def test_get_set_default_value_roundtrip(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import VerbatimString

        obj = self._make()
        value = VerbatimString().setValue("default_value")
        assert obj.setDefaultValue(value) is obj
        assert obj.getDefaultValue() == value

    def test_set_default_value_none_noop(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import VerbatimString

        obj = self._make()
        value = VerbatimString().setValue("default_value")
        obj.setDefaultValue(value)
        obj.setDefaultValue(None)
        assert obj.getDefaultValue() == value

    def test_get_set_max_length_roundtrip(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

        obj = self._make()
        value = PositiveInteger().setValue("100")
        assert obj.setMaxLength(value) is obj
        assert obj.getMaxLength() == value

    def test_set_max_length_none_noop(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

        obj = self._make()
        value = PositiveInteger().setValue("100")
        obj.setMaxLength(value)
        obj.setMaxLength(None)
        assert obj.getMaxLength() == value

    def test_get_set_min_length_roundtrip(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

        obj = self._make()
        value = PositiveInteger().setValue("1")
        assert obj.setMinLength(value) is obj
        assert obj.getMinLength() == value

    def test_set_min_length_none_noop(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

        obj = self._make()
        value = PositiveInteger().setValue("1")
        obj.setMinLength(value)
        obj.setMinLength(None)
        assert obj.getMinLength() == value

    def test_get_set_regular_expression_roundtrip(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RegularExpression

        obj = self._make()
        value = RegularExpression().setValue("[a-zA-Z]*")
        assert obj.setRegularExpression(value) is obj
        assert obj.getRegularExpression() == value

    def test_set_regular_expression_none_noop(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RegularExpression

        obj = self._make()
        value = RegularExpression().setValue("[a-zA-Z]*")
        obj.setRegularExpression(value)
        obj.setRegularExpression(None)
        assert obj.getRegularExpression() == value


class TestEcucAbstractConfigurationClass:
    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            EcucAbstractConfigurationClass()
