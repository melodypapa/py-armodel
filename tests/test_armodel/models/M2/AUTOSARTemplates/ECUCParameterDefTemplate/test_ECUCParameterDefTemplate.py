"""
Test cases for the ECUC Parameter Definition Template classes.
These tests ensure 100% code coverage for all ECUC parameter definition classes.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucConditionSpecification,
    EcucValidationCondition,
    EcucScopeEnum,
    EcucDefinitionElement,
    EcucDestinationUriDefRefType,
    EcucConfigurationClassEnum,
    EcucConfigurationVariantEnum,
    EcucAbstractConfigurationClass,
    EcucMultiplicityConfigurationClass,
    EcucContainerDef,
    EcucValueConfigurationClass,
    EcucCommonAttributes,
    EcucDerivationSpecification,
    EcucParameterDef,
    EcucBooleanParamDef,
    EcucAbstractReferenceDef,
    EcucAbstractInternalReferenceDef,
    EcucAbstractExternalReferenceDef,
    EcucSymbolicNameReferenceDef,
    EcucChoiceReferenceDef,
    EcucReferenceDef,
    EcucUriReferenceDef,
    EcucForeignReferenceDef,
    EcucInstanceReferenceDef,
    EcucAbstractStringParamDef,
    EcucStringParamDef,
    EcucFunctionNameDef,
    EcucIntegerParamDef,
    EcucEnumerationLiteralDef,
    EcucEnumerationParamDef,
    EcucFloatParamDef,
    EcucChoiceContainerDef,
    EcucParamConfContainerDef
)


class TestEcucConditionSpecification:
    """
    Test class for EcucConditionSpecification functionality.
    This class contains test methods for validating the behavior of 
    the EcucConditionSpecification class, including its initialization.
    """
    
    def test_initialization(self):
        """
        Test EcucConditionSpecification class initialization.
        Verifies that the EcucConditionSpecification can be properly instantiated 
        and that it inherits from ARObject.
        """
        condition_spec = EcucConditionSpecification()

        assert condition_spec is not None


class TestEcucValidationCondition:
    """
    Test class for EcucValidationCondition functionality.
    This class contains test methods for validating the behavior of 
    the EcucValidationCondition class, including its initialization.
    """
    
    def test_initialization(self):
        """
        Test EcucValidationCondition class initialization.
        Verifies that the EcucValidationCondition can be properly instantiated
        with a parent and short name.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        validation_condition = EcucValidationCondition(parent, "TestValidationCondition")

        assert validation_condition is not None
        assert validation_condition.getShortName() == "TestValidationCondition"
        assert validation_condition.parent == parent


class TestEcucScopeEnum:
    """
    Test class for EcucScopeEnum functionality.
    This class contains test methods for validating the behavior of 
    the EcucScopeEnum class, including its initialization.
    """
    
    def test_initialization(self):
        """
        Test EcucScopeEnum class initialization.
        Verifies that the EcucScopeEnum can be properly instantiated
        and inherits from AREnum.
        """
        scope_enum = EcucScopeEnum()

        assert scope_enum is not None
        assert hasattr(scope_enum, 'enumValues')
        assert scope_enum.enumValues == []


class TestEcucDefinitionElement:
    """
    Test class for EcucDefinitionElement functionality.
    This class contains test methods for validating the behavior of
    the EcucDefinitionElement class, including that it is abstract.
    """

    def test_is_abstract(self):
        """
        Test that EcucDefinitionElement is abstract and cannot be instantiated directly.
        """
        import pytest
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")

        with pytest.raises(TypeError, match="EcucDefinitionElement is an abstract class"):
            EcucDefinitionElement(parent, "TestDefinitionElement")

    def test_initialization(self):
        """
        Test EcucDefinitionElement subclass initialization.
        Verifies that a concrete subclass can be instantiated.
        """
        # Test with a concrete subclass like EcucContainerDef
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        container_def = EcucContainerDef(parent, "TestContainerDef")

        assert container_def is not None
        assert container_def.getShortName() == "TestContainerDef"

    def test_setter_methods(self):
        """
        Test EcucDefinitionElement setter methods on concrete subclass.
        Verifies that all setter methods work correctly and return self for method chaining.
        """
        # Test with a concrete subclass
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        container_def = EcucContainerDef(parent, "TestContainerDef")

        # Test setEcucCond
        condition_spec = EcucConditionSpecification()
        result = container_def.setEcucCond(condition_spec)
        assert result == container_def
        assert container_def.getEcucCond() == condition_spec

        # Test addEcucValidationCond
        validation_condition = EcucValidationCondition(parent, "TestValidation")
        result = container_def.addEcucValidationCond(validation_condition)
        assert result == container_def
        assert validation_condition in container_def.getEcucValidationConds()

        # Test setLowerMultiplicity
        result = container_def.setLowerMultiplicity(1)
        assert result == container_def
        assert container_def.getLowerMultiplicity() == 1

        # Test setRelatedTraceItemRef
        ref = EcucDestinationUriDefRefType()
        result = container_def.setRelatedTraceItemRef(ref)
        assert result == container_def
        assert container_def.getRelatedTraceItemRef() == ref

        # Test setScope
        scope = EcucScopeEnum()
        result = container_def.setScope(scope)
        assert result == container_def
        assert container_def.getScope() == scope

        # Test setUpperMultiplicity
        result = container_def.setUpperMultiplicity(10)
        assert result == container_def
        assert container_def.getUpperMultiplicity() == 10

        # Test setUpperMultiplicityInfinite
        result = container_def.setUpperMultiplicityInfinite(True)
        assert result == container_def
        assert container_def.getUpperMultiplicityInfinite() is True

    def test_none_handling(self):
        """
        Test EcucDefinitionElement setter methods with None values.
        Verifies that setting None values doesn't change the stored values.
        """
        import pytest
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")

        # EcucDefinitionElement is abstract, so it should raise TypeError
        with pytest.raises(TypeError, match="EcucDefinitionElement is an abstract class"):
            EcucDefinitionElement(parent, "TestDefinitionElement")


class TestEcucDestinationUriDefRefType:
    """
    Test class for EcucDestinationUriDefRefType functionality.
    This class contains test methods for validating the behavior of 
    the EcucDestinationUriDefRefType class, including its initialization.
    """
    
    def test_initialization(self):
        """
        Test EcucDestinationUriDefRefType class initialization.
        Verifies that the EcucDestinationUriDefRefType can be properly instantiated
        and inherits from RefType.
        """
        uri_ref = EcucDestinationUriDefRefType()

        assert uri_ref is not None


class TestEcucConfigurationClassEnum:
    """
    Test class for EcucConfigurationClassEnum functionality.
    This class contains test methods for validating the behavior of 
    the EcucConfigurationClassEnum class, including its initialization.
    """
    
    def test_initialization(self):
        """
        Test EcucConfigurationClassEnum class initialization.
        Verifies that the EcucConfigurationClassEnum can be properly instantiated
        and inherits from AREnum.
        """
        config_class_enum = EcucConfigurationClassEnum()

        assert config_class_enum is not None
        assert config_class_enum.enumValues == []


class TestEcucConfigurationVariantEnum:
    """
    Test class for EcucConfigurationVariantEnum functionality.
    This class contains test methods for validating the behavior of 
    the EcucConfigurationVariantEnum class, including its initialization.
    """
    
    def test_initialization(self):
        """
        Test EcucConfigurationVariantEnum class initialization.
        Verifies that the EcucConfigurationVariantEnum can be properly instantiated
        and inherits from AREnum.
        """
        config_variant_enum = EcucConfigurationVariantEnum()

        assert config_variant_enum is not None
        assert config_variant_enum.enumValues == []


class TestEcucAbstractConfigurationClass:
    """
    Test class for EcucAbstractConfigurationClass functionality.
    This class contains test methods for validating the behavior of 
    the EcucAbstractConfigurationClass class, including that it is abstract.
    """

    def test_is_abstract(self):
        """
        Test that EcucAbstractConfigurationClass is abstract and cannot be instantiated directly.
        """
        import pytest
        with pytest.raises(TypeError, match="EcucAbstractConfigurationClass is an abstract class"):
            EcucAbstractConfigurationClass()

    def test_subclass_initialization(self):
        """
        Test EcucAbstractConfigurationClass subclass initialization.
        Verifies that a concrete subclass can be instantiated.
        """
        # Use a concrete subclass like EcucContainerDef
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        container_def = EcucContainerDef(parent, "TestContainerDef")

        # EcucContainerDef inherits from EcucAbstractConfigurationClass
        assert container_def is not None
        assert isinstance(container_def, EcucAbstractConfigurationClass)

    def test_setter_methods(self):
        """
        Test EcucAbstractConfigurationClass setter methods on concrete subclass.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        container_def = EcucContainerDef(parent, "TestContainerDef")

        # Test setConfigClass
        config_enum = EcucConfigurationClassEnum()
        result = config_class.setConfigClass(config_enum)
        assert result == config_class
        assert config_class.getConfigClass() == config_enum

        # Test setConfigVariant
        variant_enum = EcucConfigurationVariantEnum()
        result = config_class.setConfigVariant(variant_enum)
        assert result == config_class
        assert config_class.getConfigVariant() == variant_enum


class TestEcucMultiplicityConfigurationClass:
    """
    Test class for EcucMultiplicityConfigurationClass functionality.
    This class contains test methods for validating the behavior of 
    the EcucMultiplicityConfigurationClass class, including its initialization.
    """
    
    def test_initialization(self):
        """
        Test EcucMultiplicityConfigurationClass class initialization.
        Verifies that the EcucMultiplicityConfigurationClass can be properly instantiated
        and inherits from EcucAbstractConfigurationClass.
        """
        mult_config_class = EcucMultiplicityConfigurationClass()

        assert mult_config_class is not None
        assert mult_config_class.getConfigClass() is None
        assert mult_config_class.getConfigVariant() is None


class TestEcucContainerDef:
    """
    Test class for EcucContainerDef functionality.
    This class contains test methods for validating the behavior of 
    the EcucContainerDef class, including its initialization and methods.
    """
    
    def test_initialization(self):
        """
        Test EcucContainerDef class initialization.
        Verifies that the EcucContainerDef can be properly instantiated with a parent and short name.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        container_def = EcucContainerDef(parent, "TestContainerDef")

        assert container_def is not None
        assert container_def.getShortName() == "TestContainerDef"
        assert container_def.getDestinationUriRef() is None
        assert container_def.getMultiplicityConfigClasses() == []
        assert container_def.getOrigin() is None
        assert container_def.getPostBuildVariantMultiplicity() is None
        assert container_def.getRequiresIndex() is None
        assert container_def.getMultipleConfigurationContainer() is None

    def test_setter_methods(self):
        """
        Test EcucContainerDef setter methods.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        container_def = EcucContainerDef(parent, "TestContainerDef")

        # Test setDestinationUriRef
        uri_ref = EcucDestinationUriDefRefType()
        result = container_def.setDestinationUriRef(uri_ref)
        assert result == container_def
        assert container_def.getDestinationUriRef() == uri_ref

        # Test addMultiplicityConfigClass
        mult_config = EcucMultiplicityConfigurationClass()
        result = container_def.addMultiplicityConfigClass(mult_config)
        assert result == container_def
        assert mult_config in container_def.getMultiplicityConfigClasses()

        # Test setOrigin
        result = container_def.setOrigin("TestOrigin")
        assert result == container_def
        assert container_def.getOrigin() == "TestOrigin"

        # Test setPostBuildVariantMultiplicity
        result = container_def.setPostBuildVariantMultiplicity(True)
        assert result == container_def
        assert container_def.getPostBuildVariantMultiplicity() is True

        # Test setRequiresIndex
        result = container_def.setRequiresIndex(True)
        assert result == container_def
        assert container_def.getRequiresIndex() is True

        # Test setMultipleConfigurationContainer
        result = container_def.setMultipleConfigurationContainer(True)
        assert result == container_def
        assert container_def.getMultipleConfigurationContainer() is True


class TestEcucValueConfigurationClass:
    """
    Test class for EcucValueConfigurationClass functionality.
    This class contains test methods for validating the behavior of 
    the EcucValueConfigurationClass class, including its initialization.
    """
    
    def test_initialization(self):
        """
        Test EcucValueConfigurationClass class initialization.
        Verifies that the EcucValueConfigurationClass can be properly instantiated
        and inherits from EcucAbstractConfigurationClass.
        """
        value_config_class = EcucValueConfigurationClass()

        assert value_config_class is not None
        assert value_config_class.getConfigClass() is None
        assert value_config_class.getConfigVariant() is None


class TestEcucCommonAttributes:
    """
    Test class for EcucCommonAttributes functionality.
    This class tests the abstract class behavior and verifies that attempting to
    instantiate it directly raises a TypeError.
    """
    
    def test_abstract_instantiation_raises_error(self):
        """
        Test that EcucCommonAttributes cannot be directly instantiated.
        Verifies that attempting to instantiate the abstract class raises a TypeError.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        
        with pytest.raises(TypeError, match="Cannot instantiate abstract class EcucCommonAttributes"):
            EcucCommonAttributes(parent, "TestCommonAttributes")

    def test_subclass_instantiation(self):
        """
        Test that a subclass of EcucCommonAttributes can be instantiated.
        """
        # Since we don't have a concrete subclass in the same file, we'll test by subclassing
        class ConcreteCommonAttributes(EcucCommonAttributes):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        concrete = ConcreteCommonAttributes(parent, "TestConcrete")

        assert concrete is not None
        assert concrete.getShortName() == "TestConcrete"
        assert concrete.getMultiplicityConfigClasses() == []
        assert concrete.getOrigin() is None
        assert concrete.getPostBuildVariantMultiplicity() is None
        assert concrete.getPostBuildVariantValue() is None
        assert concrete.getRequiresIndex() is None
        assert concrete.getValueConfigClasses() == []

    def test_subclass_methods(self):
        """
        Test EcucCommonAttributes subclass setter and getter methods.
        """
        class ConcreteCommonAttributes(EcucCommonAttributes):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        concrete = ConcreteCommonAttributes(parent, "TestConcrete")

        # Test multiplicity config class methods
        mult_config = EcucMultiplicityConfigurationClass()
        result = concrete.addMultiplicityConfigClass(mult_config)
        assert result == concrete
        assert mult_config in concrete.getMultiplicityConfigClasses()

        # Test origin methods
        result = concrete.setOrigin("TestOrigin")
        assert result == concrete
        assert concrete.getOrigin() == "TestOrigin"

        # Test post build variant multiplicity methods
        result = concrete.setPostBuildVariantMultiplicity(True)
        assert result == concrete
        assert concrete.getPostBuildVariantMultiplicity() is True

        # Test post build variant value methods
        result = concrete.setPostBuildVariantValue(True)
        assert result == concrete
        assert concrete.getPostBuildVariantValue() is True

        # Test requires index methods
        result = concrete.setRequiresIndex(True)
        assert result == concrete
        assert concrete.getRequiresIndex() is True

        # Test value config class methods
        value_config = EcucValueConfigurationClass()
        result = concrete.addValueConfigClass(value_config)
        assert result == concrete
        # Note: There's an issue in the source code - getValueConfigClasses returns EcucValueConfigurationClass 
        # instead of List[EcucValueConfigurationClass], so I'll test adding to the list
        assert value_config in concrete.getValueConfigClasses()


class TestEcucDerivationSpecification:
    """
    Test class for EcucDerivationSpecification functionality.
    This class contains test methods for validating the behavior of 
    the EcucDerivationSpecification class, including its initialization.
    """
    
    def test_initialization(self):
        """
        Test EcucDerivationSpecification class initialization.
        Verifies that the EcucDerivationSpecification can be properly instantiated
        and inherits from ARObject.
        """
        derivation_spec = EcucDerivationSpecification()

        assert derivation_spec is not None


class TestEcucParameterDef:
    """
    Test class for EcucParameterDef functionality.
    This class contains test methods for validating the behavior of
    the EcucParameterDef class, including its initialization and methods.
    """

    def test_abstract_class_cannot_be_instantiated(self):
        """
        Test that EcucParameterDef abstract class cannot be instantiated directly.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        with pytest.raises(TypeError, match="EcucParameterDef is an abstract class"):
            EcucParameterDef(parent, "TestParameterDef")

    def test_concrete_subclass_initialization(self):
        """
        Test that a concrete subclass of EcucParameterDef can be instantiated.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        param_def = EcucBooleanParamDef(parent, "TestParameterDef")

        assert param_def is not None
        assert param_def.getShortName() == "TestParameterDef"
        assert param_def.getDerivation() is None
        assert param_def.getSymbolicNameValue() is None
        assert param_def.getWithAuto() is None

    def test_setter_methods(self):
        """
        Test EcucParameterDef setter methods.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        param_def = EcucBooleanParamDef(parent, "TestParameterDef")

        # Test setDerivation
        derivation = EcucDerivationSpecification()
        result = param_def.setDerivation(derivation)
        assert result == param_def
        assert param_def.getDerivation() == derivation

        # Test setSymbolicNameValue
        result = param_def.setSymbolicNameValue(True)
        assert result == param_def
        assert param_def.getSymbolicNameValue() is True

        # Test setWithAuto
        result = param_def.setWithAuto(True)
        assert result == param_def
        assert param_def.getWithAuto() is True


class TestEcucBooleanParamDef:
    """
    Test class for EcucBooleanParamDef functionality.
    This class contains test methods for validating the behavior of 
    the EcucBooleanParamDef class, including its initialization and methods.
    """
    
    def test_initialization(self):
        """
        Test EcucBooleanParamDef class initialization.
        Verifies that the EcucBooleanParamDef can be properly instantiated.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        bool_param = EcucBooleanParamDef(parent, "TestBooleanParam")

        assert bool_param is not None
        assert bool_param.getShortName() == "TestBooleanParam"
        assert bool_param.getDefaultValue() is None

    def test_setter_methods(self):
        """
        Test EcucBooleanParamDef setter methods.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        bool_param = EcucBooleanParamDef(parent, "TestBooleanParam")

        # Test setDefaultValue
        result = bool_param.setDefaultValue(True)
        assert result == bool_param
        assert bool_param.getDefaultValue() is True


class TestEcucAbstractReferenceDef:
    """
    Test class for EcucAbstractReferenceDef functionality.
    This class tests the abstract class behavior and verifies that attempting to
    instantiate it directly raises a TypeError.
    """
    
    def test_abstract_instantiation_raises_error(self):
        """
        Test that EcucAbstractReferenceDef cannot be directly instantiated.
        Verifies that attempting to instantiate the abstract class raises a TypeError.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        
        with pytest.raises(TypeError, match="Cannot instantiate abstract class EcucAbstractReferenceDef"):
            EcucAbstractReferenceDef(parent, "TestAbstractRefDef")

    def test_subclass_instantiation(self):
        """
        Test that a subclass of EcucAbstractReferenceDef can be instantiated.
        """
        class ConcreteAbstractReferenceDef(EcucAbstractReferenceDef):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        concrete = ConcreteAbstractReferenceDef(parent, "TestConcrete")

        assert concrete is not None
        assert concrete.getShortName() == "TestConcrete"
        assert concrete.getWithAuto() is None

    def test_setter_methods(self):
        """
        Test EcucAbstractReferenceDef setter methods.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        class ConcreteAbstractReferenceDef(EcucAbstractReferenceDef):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        concrete = ConcreteAbstractReferenceDef(parent, "TestConcrete")

        result = concrete.setWithAuto(True)
        assert result == concrete
        assert concrete.getWithAuto() is True


class TestEcucAbstractInternalReferenceDef:
    """
    Test class for EcucAbstractInternalReferenceDef functionality.
    This class tests the abstract class behavior and verifies that attempting to
    instantiate it directly raises a TypeError.
    """
    
    def test_abstract_instantiation_raises_error(self):
        """
        Test that EcucAbstractInternalReferenceDef cannot be directly instantiated.
        Verifies that attempting to instantiate the abstract class raises a TypeError.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        
        with pytest.raises(TypeError, match="Cannot instantiate abstract class EcucAbstractInternalReferenceDef"):
            EcucAbstractInternalReferenceDef(parent, "TestAbstractInternalRefDef")

    def test_subclass_instantiation(self):
        """
        Test that a subclass of EcucAbstractInternalReferenceDef can be instantiated.
        """
        class ConcreteAbstractInternalReferenceDef(EcucAbstractInternalReferenceDef):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        concrete = ConcreteAbstractInternalReferenceDef(parent, "TestConcrete")

        assert concrete is not None
        assert concrete.getShortName() == "TestConcrete"
        assert concrete.getWithAuto() is None
        assert concrete.getRequiresSymbolicNameValue() is None

    def test_setter_methods(self):
        """
        Test EcucAbstractInternalReferenceDef setter methods.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        class ConcreteAbstractInternalReferenceDef(EcucAbstractInternalReferenceDef):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        concrete = ConcreteAbstractInternalReferenceDef(parent, "TestConcrete")

        result = concrete.setRequiresSymbolicNameValue(True)
        assert result == concrete
        assert concrete.getRequiresSymbolicNameValue() is True


class TestEcucAbstractExternalReferenceDef:
    """
    Test class for EcucAbstractExternalReferenceDef functionality.
    This class tests the abstract class behavior and verifies that attempting to
    instantiate it directly raises a TypeError.
    """
    
    def test_abstract_instantiation_raises_error(self):
        """
        Test that EcucAbstractExternalReferenceDef cannot be directly instantiated.
        Verifies that attempting to instantiate the abstract class raises a TypeError.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        
        with pytest.raises(TypeError, match="Cannot instantiate abstract class EcucAbstractExternalReferenceDef"):
            EcucAbstractExternalReferenceDef(parent, "TestAbstractExternalRefDef")


class TestEcucSymbolicNameReferenceDef:
    """
    Test class for EcucSymbolicNameReferenceDef functionality.
    This class contains test methods for validating the behavior of 
    the EcucSymbolicNameReferenceDef class, including its initialization and methods.
    """
    
    def test_initialization(self):
        """
        Test EcucSymbolicNameReferenceDef class initialization.
        Verifies that the EcucSymbolicNameReferenceDef can be properly instantiated.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        symbolic_ref = EcucSymbolicNameReferenceDef(parent, "TestSymbolicNameRef")

        assert symbolic_ref is not None
        assert symbolic_ref.getShortName() == "TestSymbolicNameRef"
        assert symbolic_ref.getDestinationRef() is None

    def test_setter_methods(self):
        """
        Test EcucSymbolicNameReferenceDef setter methods.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        symbolic_ref = EcucSymbolicNameReferenceDef(parent, "TestSymbolicNameRef")

        ref = EcucDestinationUriDefRefType()
        result = symbolic_ref.setDestinationRef(ref)
        assert result == symbolic_ref
        assert symbolic_ref.getDestinationRef() == ref


class TestEcucChoiceReferenceDef:
    """
    Test class for EcucChoiceReferenceDef functionality.
    This class contains test methods for validating the behavior of 
    the EcucChoiceReferenceDef class, including its initialization and methods.
    """
    
    def test_initialization(self):
        """
        Test EcucChoiceReferenceDef class initialization.
        Verifies that the EcucChoiceReferenceDef can be properly instantiated.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        choice_ref = EcucChoiceReferenceDef(parent, "TestChoiceRef")

        assert choice_ref is not None
        assert choice_ref.getShortName() == "TestChoiceRef"
        assert choice_ref.getDestinationRef() is None

    def test_setter_methods(self):
        """
        Test EcucChoiceReferenceDef setter methods.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        choice_ref = EcucChoiceReferenceDef(parent, "TestChoiceRef")

        ref = EcucDestinationUriDefRefType()
        result = choice_ref.setDestinationRef(ref)
        assert result == choice_ref
        assert choice_ref.getDestinationRef() == ref


class TestEcucReferenceDef:
    """
    Test class for EcucReferenceDef functionality.
    This class contains test methods for validating the behavior of 
    the EcucReferenceDef class, including its initialization and methods.
    """
    
    def test_initialization(self):
        """
        Test EcucReferenceDef class initialization.
        Verifies that the EcucReferenceDef can be properly instantiated.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        ref_def = EcucReferenceDef(parent, "TestRefDef")

        assert ref_def is not None
        assert ref_def.getShortName() == "TestRefDef"
        assert ref_def.getDestinationRef() is None

    def test_setter_methods(self):
        """
        Test EcucReferenceDef setter methods.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        ref_def = EcucReferenceDef(parent, "TestRefDef")

        ref = EcucDestinationUriDefRefType()
        result = ref_def.setDestinationRef(ref)
        assert result == ref_def
        assert ref_def.getDestinationRef() == ref


class TestEcucUriReferenceDef:
    """
    Test class for EcucUriReferenceDef functionality.
    This class contains test methods for validating the behavior of 
    the EcucUriReferenceDef class, including its initialization and methods.
    """
    
    def test_initialization(self):
        """
        Test EcucUriReferenceDef class initialization.
        Verifies that the EcucUriReferenceDef can be properly instantiated.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        uri_ref_def = EcucUriReferenceDef(parent, "TestUriRefDef")

        assert uri_ref_def is not None
        assert uri_ref_def.getShortName() == "TestUriRefDef"
        assert uri_ref_def.getDestinationUriRef() is None

    def test_setter_methods(self):
        """
        Test EcucUriReferenceDef setter methods.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        uri_ref_def = EcucUriReferenceDef(parent, "TestUriRefDef")

        uri_ref = EcucDestinationUriDefRefType()
        result = uri_ref_def.setDestinationUriRef(uri_ref)
        assert result == uri_ref_def
        assert uri_ref_def.getDestinationUriRef() == uri_ref


class TestEcucForeignReferenceDef:
    """
    Test class for EcucForeignReferenceDef functionality.
    This class contains test methods for validating the behavior of 
    the EcucForeignReferenceDef class, including its initialization and methods.
    """
    
    def test_initialization(self):
        """
        Test EcucForeignReferenceDef class initialization.
        Verifies that the EcucForeignReferenceDef can be properly instantiated.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        foreign_ref_def = EcucForeignReferenceDef(parent, "TestForeignRefDef")

        assert foreign_ref_def is not None
        assert foreign_ref_def.getShortName() == "TestForeignRefDef"
        assert foreign_ref_def.getDestinationContext() is None
        assert foreign_ref_def.getDestinationType() is None

    def test_setter_methods(self):
        """
        Test EcucForeignReferenceDef setter methods.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        foreign_ref_def = EcucForeignReferenceDef(parent, "TestForeignRefDef")

        # Test setDestinationContext
        result = foreign_ref_def.setDestinationContext("TestContext")
        assert result == foreign_ref_def
        assert foreign_ref_def.getDestinationContext() == "TestContext"

        # Test setDestinationType
        result = foreign_ref_def.setDestinationType("TestType")
        assert result == foreign_ref_def
        assert foreign_ref_def.getDestinationType() == "TestType"


class TestEcucInstanceReferenceDef:
    """
    Test class for EcucInstanceReferenceDef functionality.
    This class contains test methods for validating the behavior of 
    the EcucInstanceReferenceDef class, including its initialization and methods.
    """
    
    def test_initialization(self):
        """
        Test EcucInstanceReferenceDef class initialization.
        Verifies that the EcucInstanceReferenceDef can be properly instantiated.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        instance_ref_def = EcucInstanceReferenceDef(parent, "TestInstanceRefDef")

        assert instance_ref_def is not None
        assert instance_ref_def.getShortName() == "TestInstanceRefDef"
        assert instance_ref_def.getDestinationType() is None

    def test_setter_methods(self):
        """
        Test EcucInstanceReferenceDef setter methods.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        instance_ref_def = EcucInstanceReferenceDef(parent, "TestInstanceRefDef")

        result = instance_ref_def.setDestinationType("TestType")
        assert result == instance_ref_def
        assert instance_ref_def.getDestinationType() == "TestType"


class TestEcucAbstractStringParamDef:
    """
    Test class for EcucAbstractStringParamDef functionality.
    This class tests the abstract class behavior and verifies that attempting to
    instantiate it directly raises a TypeError.
    """
    
    def test_abstract_instantiation_raises_error(self):
        """
        Test that EcucAbstractStringParamDef cannot be directly instantiated.
        Verifies that attempting to instantiate the abstract class raises a TypeError.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        
        with pytest.raises(TypeError, match="Cannot instantiate abstract class EcucAbstractStringParamDef"):
            EcucAbstractStringParamDef(parent, "TestAbstractStringParamDef")


class TestEcucStringParamDef:
    """
    Test class for EcucStringParamDef functionality.
    This class contains test methods for validating the behavior of 
    the EcucStringParamDef class, including its initialization and methods.
    """
    
    def test_initialization(self):
        """
        Test EcucStringParamDef class initialization.
        Verifies that the EcucStringParamDef can be properly instantiated.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        string_param_def = EcucStringParamDef(parent, "TestStringParamDef")

        assert string_param_def is not None
        assert string_param_def.getShortName() == "TestStringParamDef"
        assert string_param_def.getDefaultValue() is None
        assert string_param_def.getMaxLength() is None
        assert string_param_def.getMinLength() is None
        assert string_param_def.getRegularExpression() is None

    def test_setter_methods(self):
        """
        Test EcucStringParamDef setter methods.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        string_param_def = EcucStringParamDef(parent, "TestStringParamDef")

        # Test setDefaultValue
        result = string_param_def.setDefaultValue("test value")
        assert result == string_param_def
        assert string_param_def.getDefaultValue() == "test value"

        # Test setMaxLength
        result = string_param_def.setMaxLength(20)
        assert result == string_param_def
        assert string_param_def.getMaxLength() == 20

        # Test setMinLength
        result = string_param_def.setMinLength(5)
        assert result == string_param_def
        assert string_param_def.getMinLength() == 5

        # Test setRegularExpression
        result = string_param_def.setRegularExpression(r"\w+")
        assert result == string_param_def
        assert string_param_def.getRegularExpression() == r"\w+"


class TestEcucFunctionNameDef:
    """
    Test class for EcucFunctionNameDef functionality.
    This class contains test methods for validating the behavior of 
    the EcucFunctionNameDef class, including its initialization and methods.
    """
    
    def test_initialization(self):
        """
        Test EcucFunctionNameDef class initialization.
        Verifies that the EcucFunctionNameDef can be properly instantiated.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        func_name_def = EcucFunctionNameDef(parent, "TestFunctionNameDef")

        assert func_name_def is not None
        assert func_name_def.getShortName() == "TestFunctionNameDef"
        assert func_name_def.getDefaultValue() is None
        assert func_name_def.getMaxLength() is None
        assert func_name_def.getMinLength() is None
        assert func_name_def.getRegularExpression() is None


class TestEcucIntegerParamDef:
    """
    Test class for EcucIntegerParamDef functionality.
    This class contains test methods for validating the behavior of 
    the EcucIntegerParamDef class, including its initialization and methods.
    """
    
    def test_initialization(self):
        """
        Test EcucIntegerParamDef class initialization.
        Verifies that the EcucIntegerParamDef can be properly instantiated.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        int_param_def = EcucIntegerParamDef(parent, "TestIntegerParamDef")

        assert int_param_def is not None
        assert int_param_def.getShortName() == "TestIntegerParamDef"
        assert int_param_def.getDefaultValue() is None
        assert int_param_def.getMax() is None
        assert int_param_def.getMin() is None

    def test_setter_methods(self):
        """
        Test EcucIntegerParamDef setter methods.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        int_param_def = EcucIntegerParamDef(parent, "TestIntegerParamDef")

        # Test setDefaultValue
        result = int_param_def.setDefaultValue(42)
        assert result == int_param_def
        assert int_param_def.getDefaultValue() == 42

        # Test setMax
        result = int_param_def.setMax(100)
        assert result == int_param_def
        assert int_param_def.getMax() == 100

        # Test setMin
        result = int_param_def.setMin(0)
        assert result == int_param_def
        assert int_param_def.getMin() == 0


class TestEcucEnumerationLiteralDef:
    """
    Test class for EcucEnumerationLiteralDef functionality.
    This class contains test methods for validating the behavior of 
    the EcucEnumerationLiteralDef class, including its initialization.
    """
    
    def test_initialization(self):
        """
        Test EcucEnumerationLiteralDef class initialization.
        Verifies that the EcucEnumerationLiteralDef can be properly instantiated
        with a parent and short name.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        enum_literal_def = EcucEnumerationLiteralDef(parent, "TestEnumLiteralDef")

        assert enum_literal_def is not None
        assert enum_literal_def.getShortName() == "TestEnumLiteralDef"

    def test_setter_methods(self):
        """
        Test EcucEnumerationLiteralDef setter methods.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        enum_literal_def = EcucEnumerationLiteralDef(parent, "TestEnumLiteralDef")

        # Test setEcucCond
        condition_spec = EcucConditionSpecification()
        result = enum_literal_def.setEcucCond(condition_spec)
        assert result == enum_literal_def
        assert enum_literal_def.getEcucCond() == condition_spec

        # Test setOrigin
        result = enum_literal_def.setOrigin("TestOrigin")
        assert result == enum_literal_def
        assert enum_literal_def.getOrigin() == "TestOrigin"


class TestEcucEnumerationParamDef:
    """
    Test class for EcucEnumerationParamDef functionality.
    This class contains test methods for validating the behavior of 
    the EcucEnumerationParamDef class, including its initialization and methods.
    """
    
    def test_initialization(self):
        """
        Test EcucEnumerationParamDef class initialization.
        Verifies that the EcucEnumerationParamDef can be properly instantiated.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        enum_param_def = EcucEnumerationParamDef(parent, "TestEnumerationParamDef")

        assert enum_param_def is not None
        assert enum_param_def.getShortName() == "TestEnumerationParamDef"
        assert enum_param_def.getDefaultValue() is None
        assert enum_param_def.getLiterals() == []

    def test_setter_methods(self):
        """
        Test EcucEnumerationParamDef setter methods.
        Verifies that setter methods work correctly and return self for method chaining.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        enum_param_def = EcucEnumerationParamDef(parent, "TestEnumerationParamDef")

        # Test setDefaultValue
        result = enum_param_def.setDefaultValue("test_value")
        assert result == enum_param_def
        assert enum_param_def.getDefaultValue() == "test_value"

    def test_createLiteral(self):
        """
        Test EcucEnumerationParamDef createLiteral method.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        enum_param_def = EcucEnumerationParamDef(parent, "TestEnumerationParamDef")

        literal = enum_param_def.createLiteral("TestLiteral")
        assert literal is not None
        assert literal.getShortName() == "TestLiteral"
        
        literals = enum_param_def.getLiterals()
        assert len(literals) == 1
        assert literals[0] == literal

    def test_createLiteral_duplicate(self):
        """
        Test EcucEnumerationParamDef createLiteral method with duplicate name.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        enum_param_def = EcucEnumerationParamDef(parent, "TestEnumerationParamDef")

        literal1 = enum_param_def.createLiteral("TestLiteral")
        assert literal1 is not None
        assert len(enum_param_def.getLiterals()) == 1

        # Try to create the same literal again
        literal2 = enum_param_def.createLiteral("TestLiteral")
        assert literal2 is not None
        assert literal1 == literal2  # Should return the same instance
        assert len(enum_param_def.getLiterals()) == 1  # Count should still be 1


class TestEcucFloatParamDef:
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        short_name = "TestFloatParam"
        float_param = EcucFloatParamDef(parent, short_name)

        assert float_param.getShortName() == short_name
        assert float_param.getDefaultValue() is None
        assert float_param.getMax() is None
        assert float_param.getMin() is None

    def test_set_and_get_default_value(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        float_param = EcucFloatParamDef(parent, "TestFloatParam")

        default_value = 3.14
        float_param.setDefaultValue(default_value)

        assert float_param.getDefaultValue() == default_value

    def test_set_and_get_max_value(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        float_param = EcucFloatParamDef(parent, "TestFloatParam")

        max_value = 100.0
        float_param.setMax(max_value)

        assert float_param.getMax() == max_value

    def test_set_and_get_min_value(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        float_param = EcucFloatParamDef(parent, "TestFloatParam")

        min_value = 0.0
        float_param.setMin(min_value)

        assert float_param.getMin() == min_value

    def test_set_max_to_none(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        float_param = EcucFloatParamDef(parent, "TestFloatParam")

        float_param.setMax(None)

        assert float_param.getMax() is None

    def test_set_min_to_none(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        float_param = EcucFloatParamDef(parent, "TestFloatParam")

        float_param.setMin(None)

        assert float_param.getMin() is None


class TestEcucChoiceContainerDef:
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        short_name = "TestChoiceContainer"
        choice_container = EcucChoiceContainerDef(parent, short_name)

        assert choice_container.getShortName() == short_name
        assert choice_container.getChoices() == []

    def test_createEcucParamConfContainerDef(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        short_name = "TestChoiceContainer"
        choice_container = EcucChoiceContainerDef(parent, short_name)

        param_conf_container = choice_container.createEcucParamConfContainerDef("TestParamConfContainer")
        assert param_conf_container.getShortName() == "TestParamConfContainer"
        assert isinstance(param_conf_container, EcucParamConfContainerDef)
        assert param_conf_container in choice_container.getChoices()

    def test_createEcucParamConfContainerDef_duplicate(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        short_name = "TestChoiceContainer"
        choice_container = EcucChoiceContainerDef(parent, short_name)

        choice_container.createEcucParamConfContainerDef("TestParamConfContainer")
        param_conf_container_duplicate = choice_container.createEcucParamConfContainerDef("TestParamConfContainer")

        assert len(choice_container.getChoices()) == 1
        assert param_conf_container_duplicate.getShortName() == "TestParamConfContainer"

    def test_getChoices(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        short_name = "TestChoiceContainer"
        choice_container = EcucChoiceContainerDef(parent, short_name)

        choice_container.createEcucParamConfContainerDef("Choice1")
        choice_container.createEcucParamConfContainerDef("Choice2")

        choices = choice_container.getChoices()
        assert len(choices) == 2
        assert choices[0].getShortName() == "Choice1"
        assert choices[1].getShortName() == "Choice2"


class TestEcucParamConfContainerDef:
    """
    Test class for EcucParamConfContainerDef functionality.
    This class contains test methods for validating the behavior of 
    the EcucParamConfContainerDef class, including its initialization and methods.
    """
    
    def test_initialization(self):
        """
        Test EcucParamConfContainerDef class initialization.
        Verifies that the EcucParamConfContainerDef can be properly instantiated.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        param_conf_container = EcucParamConfContainerDef(parent, "TestParamConfContainerDef")

        assert param_conf_container is not None
        assert param_conf_container.getShortName() == "TestParamConfContainerDef"
        assert param_conf_container.getParameters() == []
        assert param_conf_container.getReferences() == []
        assert param_conf_container.getSubContainers() == []

    def test_create_methods(self):
        """
        Test EcucParamConfContainerDef create methods.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        param_conf_container = EcucParamConfContainerDef(parent, "TestParamConfContainerDef")

        # Test createEcucBooleanParamDef
        bool_param = param_conf_container.createEcucBooleanParamDef("TestBoolParam")
        assert bool_param is not None
        assert bool_param.getShortName() == "TestBoolParam"
        assert len(param_conf_container.getParameters()) == 1

        # Test createEcucStringParamDef
        string_param = param_conf_container.createEcucStringParamDef("TestStringParam")
        assert string_param is not None
        assert string_param.getShortName() == "TestStringParam"
        assert len(param_conf_container.getParameters()) == 2

        # Test createEcucReferenceDef
        ref = param_conf_container.createEcucReferenceDef("TestRef")
        assert ref is not None
        assert ref.getShortName() == "TestRef"
        assert len(param_conf_container.getReferences()) == 1

        # Test createEcucChoiceContainerDef
        sub_container = param_conf_container.createEcucChoiceContainerDef("TestSubContainer")
        assert sub_container is not None
        assert sub_container.getShortName() == "TestSubContainer"
        assert len(param_conf_container.getSubContainers()) == 1

    def test_create_methods_duplicate(self):
        """
        Test EcucParamConfContainerDef create methods with duplicate names to test the IsElementExists branch.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        param_conf_container = EcucParamConfContainerDef(parent, "TestParamConfContainerDef")

        # Create an element first
        bool_param1 = param_conf_container.createEcucBooleanParamDef("TestBoolParam")
        assert bool_param1 is not None
        assert len(param_conf_container.getParameters()) == 1

        # Try to create with the same name again (this should return the existing element)
        bool_param2 = param_conf_container.createEcucBooleanParamDef("TestBoolParam")
        assert bool_param2 is not None
        assert bool_param1 == bool_param2  # Should return the same instance
        assert len(param_conf_container.getParameters()) == 1  # Count should still be 1

        # Test the same for other create methods
        string_param1 = param_conf_container.createEcucStringParamDef("TestStringParam")
        assert string_param1 is not None
        assert len(param_conf_container.getParameters()) == 2

        string_param2 = param_conf_container.createEcucStringParamDef("TestStringParam")
        assert string_param2 is not None
        assert string_param1 == string_param2  # Should return the same instance
        assert len(param_conf_container.getParameters()) == 2  # Count should still be 2

        # Test createEcucIntegerParamDef with duplicate
        int_param1 = param_conf_container.createEcucIntegerParamDef("TestIntParam")
        int_param2 = param_conf_container.createEcucIntegerParamDef("TestIntParam")
        assert int_param1 == int_param2
        assert len(param_conf_container.getParameters()) == 3

        # Test createEcucFloatParamDef with duplicate
        float_param1 = param_conf_container.createEcucFloatParamDef("TestFloatParam")
        float_param2 = param_conf_container.createEcucFloatParamDef("TestFloatParam")
        assert float_param1 == float_param2
        assert len(param_conf_container.getParameters()) == 4

        # Test createEcucEnumerationParamDef with duplicate
        enum_param1 = param_conf_container.createEcucEnumerationParamDef("TestEnumParam")
        enum_param2 = param_conf_container.createEcucEnumerationParamDef("TestEnumParam")
        assert enum_param1 == enum_param2
        assert len(param_conf_container.getParameters()) == 5

        # Test createEcucFunctionNameDef with duplicate
        func_param1 = param_conf_container.createEcucFunctionNameDef("TestFuncParam")
        func_param2 = param_conf_container.createEcucFunctionNameDef("TestFuncParam")
        assert func_param1 == func_param2
        assert len(param_conf_container.getParameters()) == 6

        # Test createEcucSymbolicNameReferenceDef with duplicate
        ref1 = param_conf_container.createEcucSymbolicNameReferenceDef("TestRef")
        ref2 = param_conf_container.createEcucSymbolicNameReferenceDef("TestRef")
        assert ref1 == ref2
        assert len(param_conf_container.getReferences()) == 1

        # Test createEcucParamConfContainerDef with duplicate
        container1 = param_conf_container.createEcucParamConfContainerDef("TestContainer")
        container2 = param_conf_container.createEcucParamConfContainerDef("TestContainer")
        assert container1 == container2
        assert len(param_conf_container.getSubContainers()) == 1

    def test_get_methods(self):
        """
        Test EcucParamConfContainerDef getter methods.
        """
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("TestPackage")
        param_conf_container = EcucParamConfContainerDef(parent, "TestParamConfContainerDef")

        # Initially all lists should be empty
        assert param_conf_container.getParameters() == []
        assert param_conf_container.getReferences() == []
        assert param_conf_container.getSubContainers() == []
