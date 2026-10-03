"""
This module contains tests for the Ecuc* classes in the
AUTOSAR ECUCParameterDefTemplate module.
"""

import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, CIdentifier, RefType, String, UnlimitedInteger
from armodel.models.M2.MSR.Documentation.BlockElements.Formula import MlFormula


def _instantiate(cls, name="sn"):
    return cls(AUTOSAR.getInstance().createARPackage("Pkg_" + cls.__name__), name)


class TestEcucValidationCondition:
    def test_instantiation(self):
        assert _instantiate(EcucValidationCondition, "EcucValidationCondition").getShortName() == "EcucValidationCondition"

    def test_initialization(self):
        vc = EcucValidationCondition(AUTOSAR.getInstance().createARPackage("Pkg"), "VC")
        assert vc.getEcucQueries() == []
        assert vc.getValidationFormula() is None

    def test_create_ecuc_query(self):
        vc = EcucValidationCondition(AUTOSAR.getInstance().createARPackage("Pkg"), "VC")
        query = vc.createEcucQuery("Q1")
        assert query is not None
        assert query.getShortName() == "Q1"
        assert len(vc.getEcucQueries()) == 1
        assert vc.createEcucQuery("Q1") is query
        assert len(vc.getEcucQueries()) == 1
        assert vc.getEcucQuery("Q1") is query
        assert vc.getEcucQuery("Missing") is None

    def test_create_ecuc_query_none_short_name(self):
        vc = EcucValidationCondition(AUTOSAR.getInstance().createARPackage("Pkg"), "VC")
        assert vc.createEcucQuery(None) is None

    def test_get_set_validation_formula(self):
        vc = EcucValidationCondition(AUTOSAR.getInstance().createARPackage("Pkg"), "VC")
        formula = EcucConditionFormula()
        assert vc.setValidationFormula(formula) is vc
        assert vc.getValidationFormula() is formula
        assert vc.setValidationFormula(None) is vc
        assert vc.getValidationFormula() is formula


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
    CLASS_NOTE = "Configuration parameter type for String."

    def test_instantiation(self):
        assert _instantiate(EcucStringParamDef, "EcucStringParamDef").getShortName() == "EcucStringParamDef"

    def test_class_docstring_is_spec_note_verbatim(self):
        assert EcucStringParamDef.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert EcucStringParamDef.__init__.__doc__ is None

    def test_inherits_abstract_string_attrs(self):
        obj = _instantiate(EcucStringParamDef, "Sp")
        assert obj.getDefaultValue() is None
        assert obj.getMaxLength() is None
        assert obj.getMinLength() is None
        assert obj.getRegularExpression() is None


class TestEcucFunctionNameDef:
    def test_instantiation(self):
        assert _instantiate(EcucFunctionNameDef, "EcucFunctionNameDef").getShortName() == "EcucFunctionNameDef"


class TestEcucIntegerParamDef:
    CLASS_NOTE = "Configuration parameter type for Integer."
    DEFAULT_VALUE_NOTE = "Default value of the integer configuration parameter. atpVariation: [RS_ECUC_00083] Stereotypes: atpVariation Tags: vh.latestBindingTime=codeGenerationTime"
    MAX_NOTE = "Max value allowed for the parameter defined. atpVariation: [RS_ECUC_00084] Stereotypes: atpVariation Tags: vh.latestBindingTime=codeGenerationTime"
    MIN_NOTE = "Min value allowed for the parameter defined. atpVariation: [RS_ECUC_00084] Stereotypes: atpVariation Tags: vh.latestBindingTime=codeGenerationTime"

    def test_instantiation(self):
        assert _instantiate(EcucIntegerParamDef, "EcucIntegerParamDef").getShortName() == "EcucIntegerParamDef"

    def test_class_docstring_is_spec_note_verbatim(self):
        assert EcucIntegerParamDef.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert EcucIntegerParamDef.__init__.__doc__ is None

    def test_initialization_defaults(self):
        obj = _instantiate(EcucIntegerParamDef, "Ip")
        assert obj.getDefaultValue() is None
        assert obj.getMax() is None
        assert obj.getMin() is None

    def test_get_set_default_value_roundtrip(self):
        obj = _instantiate(EcucIntegerParamDef, "Ip")
        value = UnlimitedInteger().setValue("4")
        assert obj.setDefaultValue(value) is obj
        assert obj.getDefaultValue() is value
        assert obj.getDefaultValue().getValue() == 4
        obj.setDefaultValue(None)
        assert obj.getDefaultValue() is value

    def test_get_set_max_roundtrip(self):
        obj = _instantiate(EcucIntegerParamDef, "Ip")
        value = UnlimitedInteger().setValue("255")
        assert obj.setMax(value) is obj
        assert obj.getMax() is value
        assert obj.getMax().getValue() == 255
        obj.setMax(None)
        assert obj.getMax() is value

    def test_get_set_min_roundtrip(self):
        obj = _instantiate(EcucIntegerParamDef, "Ip")
        value = UnlimitedInteger().setValue("0")
        assert obj.setMin(value) is obj
        assert obj.getMin() is value
        assert obj.getMin().getValue() == 0
        obj.setMin(None)
        assert obj.getMin() is value

    def test_docstrings_are_spec_notes_verbatim(self):
        obj = _instantiate(EcucIntegerParamDef, "Ip")
        assert obj.getDefaultValue.__doc__ == self.DEFAULT_VALUE_NOTE
        assert inspect.cleandoc(obj.setDefaultValue.__doc__).splitlines()[0] == self.DEFAULT_VALUE_NOTE
        assert obj.getMax.__doc__ == self.MAX_NOTE
        assert inspect.cleandoc(obj.setMax.__doc__).splitlines()[0] == self.MAX_NOTE
        assert obj.getMin.__doc__ == self.MIN_NOTE
        assert inspect.cleandoc(obj.setMin.__doc__).splitlines()[0] == self.MIN_NOTE


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
    CLASS_NOTE = "Used to define configuration containers that provide a choice between several EcucParamConfContainerDef. But in the actual ECU Configuration Values only one instance from the choice list will be present."

    def test_instantiation(self):
        assert _instantiate(EcucChoiceContainerDef, "EcucChoiceContainerDef").getShortName() == "EcucChoiceContainerDef"

    def test_class_docstring_is_spec_note_verbatim(self):
        assert EcucChoiceContainerDef.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert EcucChoiceContainerDef.__init__.__doc__ is None

    def test_initialization_defaults(self):
        obj = _instantiate(EcucChoiceContainerDef, "Ecc")
        assert obj.getChoices() == []

    def test_create_choices_append_and_dedupe(self):
        obj = _instantiate(EcucChoiceContainerDef, "Ecc")
        choice = obj.createEcucParamConfContainerDef("C1")
        assert isinstance(choice, EcucParamConfContainerDef)
        assert obj.getChoices() == [choice]
        assert obj.createEcucParamConfContainerDef("C1") is choice  # duplicate returns existing
        obj.createEcucParamConfContainerDef("C2")
        assert len(obj.getChoices()) == 2


class TestEcucParamConfContainerDef:
    CLASS_NOTE = "Used to define configuration containers that can hierarchically contain other containers and/or parameter definitions."

    def test_instantiation(self):
        assert _instantiate(EcucParamConfContainerDef, "EcucParamConfContainerDef").getShortName() == "EcucParamConfContainerDef"

    def test_class_docstring_is_spec_note_verbatim(self):
        assert EcucParamConfContainerDef.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert EcucParamConfContainerDef.__init__.__doc__ is None

    def test_initialization_defaults(self):
        obj = _instantiate(EcucParamConfContainerDef, "Epc")
        assert obj.getParameters() == []
        assert obj.getReferences() == []
        assert obj.getSubContainers() == []

    def test_create_parameter_factories_append_and_dedupe(self):
        obj = _instantiate(EcucParamConfContainerDef, "Epc")
        param = obj.createEcucIntegerParamDef("P1")
        assert isinstance(param, EcucIntegerParamDef)
        assert obj.getParameters() == [param]
        assert obj.createEcucIntegerParamDef("P1") is param  # duplicate returns existing
        obj.createEcucBooleanParamDef("P2")
        assert len(obj.getParameters()) == 2

    def test_create_reference_factories_append(self):
        obj = _instantiate(EcucParamConfContainerDef, "Epc")
        ref = obj.createEcucReferenceDef("R1")
        assert isinstance(ref, EcucReferenceDef)
        assert obj.getReferences() == [ref]
        obj.createEcucForeignReferenceDef("R2")
        obj.createEcucUriReferenceDef("R3")
        assert len(obj.getReferences()) == 3

    def test_create_sub_containers_append(self):
        obj = _instantiate(EcucParamConfContainerDef, "Epc")
        sub = obj.createEcucParamConfContainerDef("S1")
        assert obj.getSubContainers() == [sub]
        obj.createEcucChoiceContainerDef("S2")
        assert len(obj.getSubContainers()) == 2


class TestEcucAddInfoParamDef:
    def test_instantiation(self):
        assert _instantiate(EcucAddInfoParamDef, "EcucAddInfoParamDef").getShortName() == "EcucAddInfoParamDef"


class TestEcucDefinitionCollection:
    CLASS_NOTE = "This represents the anchor point of an ECU Configuration Parameter Definition within the AUTOSAR templates structure. Tags: atp.recommendedPackage=EcucDefinitionCollections"

    def test_instantiation(self):
        assert _instantiate(EcucDefinitionCollection, "EcucDefinitionCollection").getShortName() == "EcucDefinitionCollection"

    def test_is_atp_blueprintable(self):
        obj = _instantiate(EcucDefinitionCollection, "Ecdc")
        assert isinstance(obj, AtpBlueprintable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert EcucDefinitionCollection.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert EcucDefinitionCollection.__init__.__doc__ is None

    def test_initialization_defaults(self):
        obj = _instantiate(EcucDefinitionCollection, "Ecdc")
        assert obj.getModuleRefs() == []

    def test_add_get_module_refs_roundtrip(self):
        obj = _instantiate(EcucDefinitionCollection, "Ecdc")
        ref = RefType()
        ref.setValue("/EcucModuleDefs/MyModule")
        assert obj.addModuleRef(ref) is obj
        assert obj.getModuleRefs() == [ref]
        obj.addModuleRef(None)
        assert obj.getModuleRefs() == [ref]  # None is a no-op


class TestEcucDestinationUriDef:
    def test_instantiation(self):
        assert _instantiate(EcucDestinationUriDef, "EcucDestinationUriDef").getShortName() == "EcucDestinationUriDef"


class TestEcucDestinationUriDefSet:
    def test_instantiation(self):
        assert _instantiate(EcucDestinationUriDefSet, "EcucDestinationUriDefSet").getShortName() == "EcucDestinationUriDefSet"


class TestEcucQuery:
    def test_instantiation(self):
        assert _instantiate(EcucQuery, "EcucQuery").getShortName() == "EcucQuery"

    def test_initialization(self):
        query = EcucQuery(AUTOSAR.getInstance().createARPackage("Pkg"), "Q")
        assert query.getEcucQueryExpression() is None

    def test_get_set_ecuc_query_expression(self):
        query = EcucQuery(AUTOSAR.getInstance().createARPackage("Pkg"), "Q")
        expr = EcucQueryExpression()
        assert query.setEcucQueryExpression(expr) is query
        assert query.getEcucQueryExpression() is expr
        assert query.setEcucQueryExpression(None) is query
        assert query.getEcucQueryExpression() is expr


class TestEcucModuleDef:
    CLASS_NOTE = "Used as the top-level element for configuration definition for Software Modules, including BSW and RTE as well as ECU Infrastructure. Tags: atp.recommendedPackage=EcucModuleDefs"

    def test_instantiation(self):
        assert _instantiate(EcucModuleDef, "EcucModuleDef").getShortName() == "EcucModuleDef"

    def test_class_docstring_is_spec_note_verbatim(self):
        assert EcucModuleDef.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert EcucModuleDef.__init__.__doc__ is None

    def test_initialization_defaults(self):
        obj = _instantiate(EcucModuleDef, "Emd")
        assert obj.getApiServicePrefix() is None
        assert obj.getContainers() == []
        assert obj.getPostBuildVariantSupport() is None
        assert obj.getRefinedModuleDefRef() is None
        assert obj.getSupportedConfigVariants() == []

    def test_get_set_api_service_prefix_roundtrip(self):
        obj = _instantiate(EcucModuleDef, "Emd")
        prefix = CIdentifier()
        prefix.setValue("Com")
        assert obj.setApiServicePrefix(prefix) is obj
        assert obj.getApiServicePrefix() is prefix
        obj.setApiServicePrefix(None)
        assert obj.getApiServicePrefix() is prefix  # None is a no-op

    def test_get_set_post_build_variant_support_roundtrip(self):
        obj = _instantiate(EcucModuleDef, "Emd")
        value = Boolean()
        value.setValue(True)
        assert obj.setPostBuildVariantSupport(value) is obj
        assert obj.getPostBuildVariantSupport() is value
        obj.setPostBuildVariantSupport(None)
        assert obj.getPostBuildVariantSupport() is value  # None is a no-op

    def test_get_set_refined_module_def_ref_roundtrip(self):
        obj = _instantiate(EcucModuleDef, "Emd")
        ref = RefType()
        ref.setValue("/EcucModuleDefs/Standard")
        assert obj.setRefinedModuleDefRef(ref) is obj
        assert obj.getRefinedModuleDefRef() is ref
        obj.setRefinedModuleDefRef(None)
        assert obj.getRefinedModuleDefRef() is ref  # None is a no-op

    def test_add_get_supported_config_variants(self):
        obj = _instantiate(EcucModuleDef, "Emd")
        variant = EcucConfigurationVariantEnum()
        variant.setValue(EcucConfigurationVariantEnum.VARIANT_POST_BUILD)
        assert obj.addSupportedConfigVariant(variant) is obj
        assert obj.getSupportedConfigVariants() == [variant]
        obj.addSupportedConfigVariant(None)
        assert obj.getSupportedConfigVariants() == [variant]  # None is a no-op

    def test_create_containers_appends_and_dedupes(self):
        obj = _instantiate(EcucModuleDef, "Emd")
        param_container = obj.createEcucParamConfContainerDef("C1")
        assert isinstance(param_container, EcucParamConfContainerDef)
        assert obj.getContainers() == [param_container]
        assert obj.createEcucParamConfContainerDef("C1") is param_container  # duplicate returns existing
        choice_container = obj.createEcucChoiceContainerDef("C2")
        assert isinstance(choice_container, EcucChoiceContainerDef)
        assert obj.getContainers() == [param_container, choice_container]


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

    def test_initialization_and_values(self):
        enum = EcucConfigurationClassEnum()

        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [
            EcucConfigurationClassEnum.LINK,
            EcucConfigurationClassEnum.POST_BUILD,
            EcucConfigurationClassEnum.PRE_COMPILE,
            EcucConfigurationClassEnum.PUBLISHED_INFORMATION,
        ]

    def test_configuration_class_literals(self):
        enum = EcucConfigurationClassEnum()

        assert enum.validateEnumValue(EcucConfigurationClassEnum.LINK)
        assert enum.validateEnumValue(EcucConfigurationClassEnum.POST_BUILD)
        assert enum.validateEnumValue(EcucConfigurationClassEnum.PRE_COMPILE)
        assert enum.validateEnumValue(EcucConfigurationClassEnum.PUBLISHED_INFORMATION)
        assert EcucConfigurationClassEnum.LINK == "Link"
        assert EcucConfigurationClassEnum.POST_BUILD == "PostBuild"
        assert EcucConfigurationClassEnum.PRE_COMPILE == "PreCompile"
        assert EcucConfigurationClassEnum.PUBLISHED_INFORMATION == "PublishedInformation"

        assert enum.setValue(EcucConfigurationClassEnum.PRE_COMPILE) is enum
        assert enum.getValue() == "PreCompile"
        assert enum.validateEnumValue("INVALID") is False

    def test_class_docstring_and_literal_comments_verbatim(self):
        source = inspect.getsource(EcucConfigurationClassEnum)

        assert inspect.cleandoc(EcucConfigurationClassEnum.__doc__) == "Possible configuration classes for the AUTOSAR configuration parameters."
        assert "# Link Time: parts of configuration are delivered from another object code file Tags: atp.EnumerationLiteralIndex=0" in source
        assert "# PostBuildTime: after compilation a configuration parameter can be changed. Tags: atp.EnumerationLiteralIndex=1" in source
        assert "# PreCompile Time: after compilation a configuration parameter can not be changed any more. Tags: atp.EnumerationLiteralIndex=2" in source
        assert "# PublishedInformation is used to specify the fact that certain information is fixed even before the pre-compile stage. Tags: atp.EnumerationLiteralIndex=3" in source


class TestEcucConfigurationVariantEnum:
    CLASS_NOTE = "Specifies the possible Configuration Variants used for AUTOSAR BSW Modules."

    def test_instantiation(self):
        assert isinstance(EcucConfigurationVariantEnum(), EcucConfigurationVariantEnum)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert EcucConfigurationVariantEnum.__doc__ == self.CLASS_NOTE

    def test_literal_members(self):
        assert EcucConfigurationVariantEnum.PRECONFIGURED_CONFIGURATION == "PRECONFIGURED-CONFIGURATION"
        assert EcucConfigurationVariantEnum.RECOMMENDED_CONFIGURATION == "RECOMMENDED-CONFIGURATION"
        assert EcucConfigurationVariantEnum.VARIANT_LINK_TIME == "VARIANT-LINK-TIME"
        assert EcucConfigurationVariantEnum.VARIANT_POST_BUILD == "VARIANT-POST-BUILD"
        assert EcucConfigurationVariantEnum.VARIANT_PRE_COMPILE == "VARIANT-PRE-COMPILE"

    def test_enum_values_in_display_order(self):
        obj = EcucConfigurationVariantEnum()
        assert list(obj.getEnumValues()) == [
            EcucConfigurationVariantEnum.PRECONFIGURED_CONFIGURATION,
            EcucConfigurationVariantEnum.RECOMMENDED_CONFIGURATION,
            EcucConfigurationVariantEnum.VARIANT_LINK_TIME,
            EcucConfigurationVariantEnum.VARIANT_POST_BUILD,
            EcucConfigurationVariantEnum.VARIANT_PRE_COMPILE,
        ]

    def test_set_value(self):
        obj = EcucConfigurationVariantEnum()
        assert obj.setValue(EcucConfigurationVariantEnum.VARIANT_PRE_COMPILE) is obj
        assert obj.getValue() == EcucConfigurationVariantEnum.VARIANT_PRE_COMPILE


class TestEcucMultiplicityConfigurationClass:
    CLASS_NOTE = "Specifies the MultiplicityConfigurationClass of a parameter/reference or a container for each ConfigurationVariant of the EcucModuleDef."

    def test_instantiation(self):
        assert isinstance(EcucMultiplicityConfigurationClass(), EcucMultiplicityConfigurationClass)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert EcucMultiplicityConfigurationClass.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert EcucMultiplicityConfigurationClass.__init__.__doc__ is None


class TestEcucValueConfigurationClass:
    CLASS_NOTE = "Specifies the ValueConfigurationClass of a parameter/reference for each ConfigurationVariant of the EcucModuleDef."

    def test_instantiation(self):
        assert isinstance(EcucValueConfigurationClass(), EcucValueConfigurationClass)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert EcucValueConfigurationClass.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert EcucValueConfigurationClass.__init__.__doc__ is None


class TestEcucDerivationSpecification:
    def test_instantiation(self):
        assert isinstance(EcucDerivationSpecification(), EcucDerivationSpecification)

    def test_initialization(self):
        derivation = EcucDerivationSpecification()
        assert derivation.getCalculationFormula() is None
        assert derivation.getEcucQueries() == []
        assert derivation.getInformalFormula() is None

    def test_get_set_calculation_formula(self):
        derivation = EcucDerivationSpecification()
        formula = EcucParameterDerivationFormula()
        assert derivation.setCalculationFormula(formula) is derivation
        assert derivation.getCalculationFormula() is formula
        assert derivation.setCalculationFormula(None) is derivation
        assert derivation.getCalculationFormula() is formula

    def test_get_set_informal_formula(self):
        derivation = EcucDerivationSpecification()
        informal = MlFormula()
        assert derivation.setInformalFormula(informal) is derivation
        assert derivation.getInformalFormula() is informal
        assert derivation.setInformalFormula(None) is derivation
        assert derivation.getInformalFormula() is informal

    def test_create_ecuc_query(self):
        derivation = EcucDerivationSpecification()
        query = derivation.createEcucQuery("Q1")
        assert query is not None
        assert query.getShortName() == "Q1"
        assert len(derivation.getEcucQueries()) == 1
        assert derivation.createEcucQuery("Q1") is query
        assert len(derivation.getEcucQueries()) == 1
        assert derivation.getEcucQuery("Q1") is query
        assert derivation.getEcucQuery("Missing") is None

    def test_create_ecuc_query_none_short_name(self):
        derivation = EcucDerivationSpecification()
        assert derivation.createEcucQuery(None) is None


class TestEcucConditionFormula:
    def test_instantiation(self):
        assert isinstance(EcucConditionFormula(), EcucConditionFormula)

    def test_initialization(self):
        formula = EcucConditionFormula()
        assert formula.getEcucQueryRef() is None
        assert formula.getEcucQueryStringRef() is None

    def test_get_set_ecuc_query_ref(self):
        formula = EcucConditionFormula()
        ref = RefType()
        ref.setValue("/Ref/Query1")
        ref.setDest("ECUC-QUERY")
        assert formula.setEcucQueryRef(ref) is formula
        assert formula.getEcucQueryRef() is ref
        assert formula.setEcucQueryRef(None) is formula
        assert formula.getEcucQueryRef() is ref

    def test_get_set_ecuc_query_string_ref(self):
        formula = EcucConditionFormula()
        ref = RefType()
        ref.setValue("/Ref/Query2")
        ref.setDest("ECUC-QUERY")
        assert formula.setEcucQueryStringRef(ref) is formula
        assert formula.getEcucQueryStringRef() is ref
        assert formula.setEcucQueryStringRef(None) is formula
        assert formula.getEcucQueryStringRef() is ref


class TestEcucDestinationUriPolicy:
    def test_instantiation(self):
        assert isinstance(EcucDestinationUriPolicy(), EcucDestinationUriPolicy)


class TestEcucParameterDerivationFormula:
    def test_instantiation(self):
        assert isinstance(EcucParameterDerivationFormula(), EcucParameterDerivationFormula)

    def test_initialization(self):
        formula = EcucParameterDerivationFormula()
        assert formula.getEcucQueryRef() is None
        assert formula.getEcucQueryStringRef() is None

    def test_get_set_ecuc_query_ref(self):
        formula = EcucParameterDerivationFormula()
        ref = RefType()
        ref.setValue("/Ref/Query1")
        ref.setDest("ECUC-QUERY")
        assert formula.setEcucQueryRef(ref) is formula
        assert formula.getEcucQueryRef() is ref
        assert formula.setEcucQueryRef(None) is formula
        assert formula.getEcucQueryRef() is ref

    def test_get_set_ecuc_query_string_ref(self):
        formula = EcucParameterDerivationFormula()
        ref = RefType()
        ref.setValue("/Ref/Query2")
        ref.setDest("ECUC-QUERY")
        assert formula.setEcucQueryStringRef(ref) is formula
        assert formula.getEcucQueryStringRef() is ref
        assert formula.setEcucQueryStringRef(None) is formula
        assert formula.getEcucQueryStringRef() is ref


class TestEcucQueryExpression:
    def test_instantiation(self):
        assert isinstance(EcucQueryExpression(), EcucQueryExpression)

    def test_initialization(self):
        expr = EcucQueryExpression()
        assert expr.getConfigElementDefGlobalRef() is None
        assert expr.getConfigElementDefLocalRef() is None

    def test_get_set_refs(self):
        expr = EcucQueryExpression()
        gref = RefType()
        gref.setValue("/Def/Global")
        gref.setDest("ECUC-DEFINITION-ELEMENT")
        lref = RefType()
        lref.setValue("/Def/Local")
        lref.setDest("ECUC-DEFINITION-ELEMENT")
        assert expr.setConfigElementDefGlobalRef(gref) is expr
        assert expr.setConfigElementDefLocalRef(lref) is expr
        assert expr.getConfigElementDefGlobalRef() is gref
        assert expr.getConfigElementDefLocalRef() is lref
        assert expr.setConfigElementDefGlobalRef(None) is expr
        assert expr.getConfigElementDefGlobalRef() is gref


class TestEcucConditionSpecification:
    def test_instantiation(self):
        assert isinstance(EcucConditionSpecification(), EcucConditionSpecification)

    def test_initialization(self):
        cond = EcucConditionSpecification()
        assert cond.getConditionFormula() is None
        assert cond.getEcucQueries() == []
        assert cond.getInformalFormula() is None

    def test_get_set_condition_formula(self):
        cond = EcucConditionSpecification()
        formula = EcucConditionFormula()
        assert cond.setConditionFormula(formula) is cond
        assert cond.getConditionFormula() is formula
        assert cond.setConditionFormula(None) is cond
        assert cond.getConditionFormula() is formula

    def test_create_ecuc_query(self):
        cond = EcucConditionSpecification()
        query = cond.createEcucQuery("Q1")
        assert query is not None
        assert query.getShortName() == "Q1"
        assert len(cond.getEcucQueries()) == 1
        assert cond.createEcucQuery("Q1") is query
        assert len(cond.getEcucQueries()) == 1
        assert cond.getEcucQuery("Q1") is query
        assert cond.getEcucQuery("Missing") is None

    def test_create_ecuc_query_none_short_name(self):
        cond = EcucConditionSpecification()
        assert cond.createEcucQuery(None) is None

    def test_get_set_informal_formula(self):
        cond = EcucConditionSpecification()
        informal = MlFormula()
        assert cond.setInformalFormula(informal) is cond
        assert cond.getInformalFormula() is informal
        assert cond.setInformalFormula(None) is cond
        assert cond.getInformalFormula() is informal


class TestEcucScopeEnum:
    def test_instantiation(self):
        assert isinstance(EcucScopeEnum(), EcucScopeEnum)

    def test_initialization_and_values(self):
        enum = EcucScopeEnum()

        assert isinstance(enum, AREnum)
        assert enum.getEnumValues() == [EcucScopeEnum.ECU, EcucScopeEnum.LOCAL]

    def test_scope_literals(self):
        enum = EcucScopeEnum()

        assert enum.validateEnumValue(EcucScopeEnum.ECU)
        assert enum.validateEnumValue(EcucScopeEnum.LOCAL)
        assert EcucScopeEnum.ECU == "ECU"
        assert EcucScopeEnum.LOCAL == "local"

        assert enum.setValue(EcucScopeEnum.LOCAL) is enum
        assert enum.getValue() == "local"
        assert enum.validateEnumValue("INVALID") is False

    def test_class_docstring_and_literal_comments_verbatim(self):
        source = inspect.getsource(EcucScopeEnum)

        assert inspect.cleandoc(EcucScopeEnum.__doc__) == "Possible scope settings for a configuration element."
        assert "# An element may be shared with other modules. Tags: atp.EnumerationLiteralIndex=0" in source
        assert "# An element is only be applicable for the module it is defined in. Tags: atp.EnumerationLiteralIndex=1" in source


class TestEcucDefinitionElement:
    CLASS_NOTE = "Common class used to express the commonalities of configuration parameters, references and containers. If not stated otherwise the default multiplicity is exactly one mandatory occurrence of the specified element."

    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            _instantiate(EcucDefinitionElement)

    def _make(self):
        class _Concrete(EcucDefinitionElement):
            pass

        return _Concrete(AUTOSAR.getInstance().createARPackage("Pkg_TestEDE"), "sn")

    def test_class_docstring_is_spec_note_verbatim(self):
        assert EcucDefinitionElement.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert EcucDefinitionElement.__init__.__doc__ is None

    def test_initialization_defaults(self):
        obj = self._make()
        assert obj.getEcucCond() is None
        assert obj.getEcucValidationConds() == []
        assert obj.getLowerMultiplicity() is None
        assert obj.getRelatedTraceItemRef() is None
        assert obj.getScope() is None
        assert obj.getUpperMultiplicity() is None
        assert obj.getUpperMultiplicityInfinite() is None

    def test_get_set_lower_multiplicity_roundtrip(self):
        obj = self._make()
        assert obj.setLowerMultiplicity(1) is obj
        assert obj.getLowerMultiplicity() == 1
        obj.setLowerMultiplicity(None)
        assert obj.getLowerMultiplicity() == 1  # None is a no-op

    def test_get_set_related_trace_item_ref_roundtrip(self):
        obj = self._make()
        ref = RefType()
        ref.setValue("/EcucId/Trace")
        assert obj.setRelatedTraceItemRef(ref) is obj
        assert obj.getRelatedTraceItemRef() is ref
        obj.setRelatedTraceItemRef(None)
        assert obj.getRelatedTraceItemRef() is ref  # None is a no-op

    def test_get_set_scope_roundtrip(self):
        obj = self._make()
        scope = EcucScopeEnum()
        scope.setValue(EcucScopeEnum.LOCAL)
        assert obj.setScope(scope) is obj
        assert obj.getScope() is scope
        obj.setScope(None)
        assert obj.getScope() is scope  # None is a no-op

    def test_get_set_upper_multiplicity_roundtrip(self):
        obj = self._make()
        assert obj.setUpperMultiplicity(4) is obj
        assert obj.getUpperMultiplicity() == 4
        obj.setUpperMultiplicity(None)
        assert obj.getUpperMultiplicity() == 4  # None is a no-op

    def test_get_set_upper_multiplicity_infinite_roundtrip(self):
        obj = self._make()
        assert obj.setUpperMultiplicityInfinite(True) is obj
        assert obj.getUpperMultiplicityInfinite() is True
        obj.setUpperMultiplicityInfinite(None)
        assert obj.getUpperMultiplicityInfinite() is True  # None is a no-op

    def test_add_get_ecuc_validation_conds(self):
        obj = self._make()
        cond = EcucValidationCondition(AUTOSAR.getInstance(), "C1")
        assert obj.addEcucValidationCond(cond) is obj
        assert obj.getEcucValidationConds() == [cond]
        obj.addEcucValidationCond(None)
        assert len(obj.getEcucValidationConds()) == 1  # None is a no-op


class TestEcucContainerDef:
    CLASS_NOTE = "Base class used to gather common attributes of configuration container definitions."

    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            _instantiate(EcucContainerDef)

    def _make(self):
        class _Concrete(EcucContainerDef):
            pass

        return _Concrete(AUTOSAR.getInstance().createARPackage("Pkg_TestECD"), "sn")

    def test_class_docstring_is_spec_note_verbatim(self):
        assert EcucContainerDef.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert EcucContainerDef.__init__.__doc__ is None

    def test_initialization_defaults(self):
        obj = self._make()
        assert obj.getDestinationUriRefs() == []
        assert obj.getMultiplicityConfigClasses() == []
        assert obj.getOrigin() is None
        assert obj.getPostBuildVariantMultiplicity() is None
        assert obj.getRequiresIndex() is None

    def test_add_get_destination_uri_refs(self):
        obj = self._make()
        ref = RefType()
        ref.setValue("/EcucDestinationUriDefs/Uri1")
        assert obj.addDestinationUriRef(ref) is obj
        assert obj.getDestinationUriRefs() == [ref]
        obj.addDestinationUriRef(None)
        assert obj.getDestinationUriRefs() == [ref]  # None is a no-op

    def test_add_get_multiplicity_config_classes(self):
        obj = self._make()
        cfg_class = EcucMultiplicityConfigurationClass()
        assert obj.addMultiplicityConfigClass(cfg_class) is obj
        assert obj.getMultiplicityConfigClasses() == [cfg_class]
        obj.addMultiplicityConfigClass(None)
        assert obj.getMultiplicityConfigClasses() == [cfg_class]  # None is a no-op

    def test_get_set_origin_roundtrip(self):
        obj = self._make()
        origin = String()
        origin.setValue("VENDOR")
        assert obj.setOrigin(origin) is obj
        assert obj.getOrigin() is origin
        obj.setOrigin(None)
        assert obj.getOrigin() is origin  # None is a no-op

    def test_get_set_post_build_variant_multiplicity_roundtrip(self):
        obj = self._make()
        value = Boolean()
        value.setValue(True)
        assert obj.setPostBuildVariantMultiplicity(value) is obj
        assert obj.getPostBuildVariantMultiplicity() is value
        obj.setPostBuildVariantMultiplicity(None)
        assert obj.getPostBuildVariantMultiplicity() is value  # None is a no-op

    def test_get_set_requires_index_roundtrip(self):
        obj = self._make()
        value = Boolean()
        value.setValue(False)
        assert obj.setRequiresIndex(value) is obj
        assert obj.getRequiresIndex() is value
        obj.setRequiresIndex(None)
        assert obj.getRequiresIndex() is value  # None is a no-op


class TestEcucCommonAttributes:
    CLASS_NOTE = "Attributes used by Configuration Parameters as well as References."

    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            _instantiate(EcucCommonAttributes)

    def _make(self):
        class _Concrete(EcucCommonAttributes):
            pass

        return _Concrete(AUTOSAR.getInstance().createARPackage("Pkg_TestECA"), "sn")

    def test_class_docstring_is_spec_note_verbatim(self):
        assert EcucCommonAttributes.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert EcucCommonAttributes.__init__.__doc__ is None

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
    CLASS_NOTE = "Abstract class used to define the similarities of all ECU Configuration Parameter types defined as subclasses."

    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            _instantiate(EcucParameterDef)

    def _make(self):
        class _Concrete(EcucParameterDef):
            pass

        return _Concrete(AUTOSAR.getInstance().createARPackage("Pkg_TestEPD"), "sn")

    def test_class_docstring_is_spec_note_verbatim(self):
        assert EcucParameterDef.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert EcucParameterDef.__init__.__doc__ is None

    def test_initialization_defaults(self):
        obj = self._make()
        assert obj.getDerivation() is None
        assert obj.getSymbolicNameValue() is None
        assert obj.getWithAuto() is None

    def test_get_set_derivation_roundtrip(self):
        obj = self._make()
        derivation = EcucDerivationSpecification()
        assert obj.setDerivation(derivation) is obj
        assert obj.getDerivation() is derivation
        obj.setDerivation(None)
        assert obj.getDerivation() is derivation  # None is a no-op

    def test_get_set_symbolic_name_value_roundtrip(self):
        obj = self._make()
        value = Boolean()
        value.setValue(True)
        assert obj.setSymbolicNameValue(value) is obj
        assert obj.getSymbolicNameValue() is value
        obj.setSymbolicNameValue(None)
        assert obj.getSymbolicNameValue() is value  # None is a no-op

    def test_get_set_with_auto_roundtrip(self):
        obj = self._make()
        value = Boolean()
        value.setValue(True)
        assert obj.setWithAuto(value) is obj
        assert obj.getWithAuto() is value
        obj.setWithAuto(None)
        assert obj.getWithAuto() is value  # None is a no-op


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
    CLASS_NOTE = "Specifies the ValueConfigurationClass of a parameter/reference or the MultiplicityConfigurationClass of a parameter/reference or a container for each ConfigurationVariant of the EcucModuleDef."

    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            EcucAbstractConfigurationClass()

    def test_class_docstring_is_spec_note_verbatim(self):
        assert EcucAbstractConfigurationClass.__doc__ == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert EcucAbstractConfigurationClass.__init__.__doc__ is None

    def test_subclass_get_set_roundtrip(self):
        obj = EcucValueConfigurationClass()
        config_class = EcucConfigurationClassEnum()
        config_class.setValue(EcucConfigurationClassEnum.POST_BUILD)
        assert obj.setConfigClass(config_class) is obj
        assert obj.getConfigClass() is config_class
        obj.setConfigClass(None)
        assert obj.getConfigClass() is config_class  # None is a no-op
        variant = EcucConfigurationVariantEnum()
        variant.setValue(EcucConfigurationVariantEnum.VARIANT_POST_BUILD)
        assert obj.setConfigVariant(variant) is obj
        assert obj.getConfigVariant() is variant
        obj.setConfigVariant(None)
        assert obj.getConfigVariant() is variant  # None is a no-op

    def test_initialization_defaults(self):
        obj = EcucMultiplicityConfigurationClass()
        assert obj.getConfigClass() is None
        assert obj.getConfigVariant() is None
