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


class TestEcucAbstractConfigurationClass:
    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            EcucAbstractConfigurationClass()
