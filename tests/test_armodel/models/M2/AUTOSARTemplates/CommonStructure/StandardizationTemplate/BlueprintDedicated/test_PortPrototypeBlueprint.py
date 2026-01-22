"""
This module contains comprehensive tests for the PortPrototypeBlueprint.py file
in the AUTOSAR CommonStructure StandardizationTemplate BlueprintDedicated module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import (
    PortPrototypeBlueprintInitValue,
    PortPrototypeBlueprint
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestPortPrototypeBlueprintInitValue:
    def test_initialization(self):
        """Test PortPrototypeBlueprintInitValue initialization"""
        init_value = PortPrototypeBlueprintInitValue()
        
        assert init_value is not None
        assert init_value.dataPrototypeRef is None
        assert init_value.value is None

    def test_get_data_prototype_ref(self):
        """Test getDataPrototypeRef method"""
        init_value = PortPrototypeBlueprintInitValue()
        assert init_value.getDataPrototypeRef() is None

    def test_set_data_prototype_ref(self):
        """Test setDataPrototypeRef method"""
        init_value = PortPrototypeBlueprintInitValue()
        test_ref = RefType().setValue("TestRef")
        result = init_value.setDataPrototypeRef(test_ref)
        assert result is init_value
        assert init_value.getDataPrototypeRef() == test_ref

    def test_set_data_prototype_ref_none(self):
        """Test setDataPrototypeRef with None value"""
        init_value = PortPrototypeBlueprintInitValue()
        result = init_value.setDataPrototypeRef(None)
        assert result is init_value
        assert init_value.getDataPrototypeRef() is None

    def test_get_value(self):
        """Test getValue method"""
        init_value = PortPrototypeBlueprintInitValue()
        assert init_value.getValue() is None

    def test_set_value(self):
        """Test setValue method"""
        init_value = PortPrototypeBlueprintInitValue()
        # Create a mock ValueSpecification for testing
        class MockValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()
        
        test_value = MockValueSpecification()
        result = init_value.setValue(test_value)
        assert result is init_value
        assert init_value.getValue() == test_value

    def test_set_value_none(self):
        """Test setValue with None value"""
        init_value = PortPrototypeBlueprintInitValue()
        result = init_value.setValue(None)
        assert result is init_value
        assert init_value.getValue() is None

    def test_all_properties(self):
        """Test setting all properties"""
        init_value = PortPrototypeBlueprintInitValue()
        
        test_ref = RefType().setValue("TestRef")
        class MockValueSpecification(ValueSpecification):
            def __init__(self):
                super().__init__()
        
        test_value = MockValueSpecification()
        
        init_value.setDataPrototypeRef(test_ref)
        init_value.setValue(test_value)
        
        assert init_value.getDataPrototypeRef() == test_ref
        assert init_value.getValue() == test_value


class TestPortPrototypeBlueprint:
    def test_initialization(self):
        """Test PortPrototypeBlueprint initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")
        
        assert blueprint is not None
        assert blueprint.getShortName() == "TestBlueprint"
        assert blueprint.initValues == []
        assert blueprint.interfaceRef is None
        # These are lists but will be empty initially since we're not importing the real classes
        assert hasattr(blueprint, 'providedComSpecs')
        assert hasattr(blueprint, 'requiredComSpecs')

    def test_get_init_values(self):
        """Test getInitValues method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")
        assert blueprint.getInitValues() == []

    def test_set_init_values(self):
        """Test setInitValues method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")
        
        init_val = PortPrototypeBlueprintInitValue()
        test_values = [init_val]
        result = blueprint.setInitValues(test_values)
        assert result is blueprint
        assert blueprint.getInitValues() == test_values

    def test_set_init_values_none(self):
        """Test setInitValues with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")
        result = blueprint.setInitValues(None)
        assert result is blueprint
        # Should keep the original empty list when None is passed
        assert blueprint.getInitValues() == []

    def test_get_interface_ref(self):
        """Test getInterfaceRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")
        assert blueprint.getInterfaceRef() is None

    def test_set_interface_ref(self):
        """Test setInterfaceRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")
        test_ref = RefType().setValue("InterfaceRef")
        result = blueprint.setInterfaceRef(test_ref)
        assert result is blueprint
        assert blueprint.getInterfaceRef() == test_ref

    def test_set_interface_ref_none(self):
        """Test setInterfaceRef with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")
        result = blueprint.setInterfaceRef(None)
        assert result is blueprint
        assert blueprint.getInterfaceRef() is None

    def test_get_provided_com_specs(self):
        """Test getProvidedComSpecs method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")
        # Since PPortComSpec is not imported, we'll just test that the attribute exists
        assert hasattr(blueprint, 'providedComSpecs')

    def test_set_provided_com_specs(self):
        """Test setProvidedComSpecs method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")
        
        # Create a mock PPortComSpec for testing
        class MockPPortComSpec:
            pass
        
        spec = MockPPortComSpec()
        test_specs = [spec]
        result = blueprint.setProvidedComSpecs(test_specs)
        assert result is blueprint
        assert blueprint.getProvidedComSpecs() == test_specs

    def test_set_provided_com_specs_none(self):
        """Test setProvidedComSpecs with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")
        result = blueprint.setProvidedComSpecs(None)
        assert result is blueprint
        # Should keep the original empty list when None is passed
        assert blueprint.getProvidedComSpecs() == []

    def test_get_required_com_specs(self):
        """Test getRequiredComSpecs method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")
        # Since RPortComSpec is not imported, we'll just test that the attribute exists
        assert hasattr(blueprint, 'requiredComSpecs')

    def test_set_required_com_specs(self):
        """Test setRequiredComSpecs method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")
        
        # Create a mock RPortComSpec for testing
        class MockRPortComSpec:
            pass
        
        spec = MockRPortComSpec()
        test_specs = [spec]
        result = blueprint.setRequiredComSpecs(test_specs)
        assert result is blueprint
        assert blueprint.getRequiredComSpecs() == test_specs

    def test_set_required_com_specs_none(self):
        """Test setRequiredComSpecs with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")
        result = blueprint.setRequiredComSpecs(None)
        assert result is blueprint
        # Should keep the original empty list when None is passed
        assert blueprint.getRequiredComSpecs() == []