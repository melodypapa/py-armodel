"""
This module contains comprehensive tests for the PortPrototypeBlueprint.py file
in the AUTOSAR CommonStructure StandardizationTemplate BlueprintDedicated module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import (
    PortPrototypeBlueprint,
    PortPrototypeBlueprintInitValue,
    PortPrototypeBlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

# Table 4.10 Note (AUTOSAR_FO_TPS_StandardizationTemplate, p.60), verbatim.
PPBIV_NOTE = (
    "This meta-class represents the ability to express init values in PortPrototypeBlueprints. " "These init values act as a kind of blueprint from which for example proper ComSpecs can be derived."
)


def _norm(doc):
    return " ".join(doc.split())


class TestPortPrototypeBlueprintInitValue:
    def test_initialization(self):
        """Test PortPrototypeBlueprintInitValue default values (Table 4.10)."""
        init_value = PortPrototypeBlueprintInitValue()

        assert isinstance(init_value, ARObject)
        assert init_value.getDataPrototypeRef() is None
        assert init_value.getValue() is None

    def test_issubclass(self):
        """Base per Table 4.10 is ARObject."""
        assert issubclass(PortPrototypeBlueprintInitValue, ARObject)

    def test_docstring(self):
        """Class docstring is the Table 4.10 Note verbatim; member Notes on accessors."""
        assert PortPrototypeBlueprintInitValue.__doc__.strip() == PPBIV_NOTE
        assert PortPrototypeBlueprintInitValue.__init__.__doc__ is None

        assert _norm(PortPrototypeBlueprintInitValue.getDataPrototypeRef.__doc__) == "This is the data prototype for which the init value applies Tags: xml.sequenceOffset=30"
        assert _norm(PortPrototypeBlueprintInitValue.setDataPrototypeRef.__doc__) == (
            "This is the data prototype for which the init value applies Tags: xml.sequenceOffset=30 A None value is a no-op and does not overwrite an existing dataPrototypeRef."
        )
        assert _norm(PortPrototypeBlueprintInitValue.getValue.__doc__) == "This is the init value for the particular data prototype. Tags: xml.sequenceOffset=40"
        assert _norm(PortPrototypeBlueprintInitValue.setValue.__doc__) == (
            "This is the init value for the particular data prototype. Tags: xml.sequenceOffset=40 A None value is a no-op and does not overwrite an existing value."
        )

    def test_get_set_data_prototype_ref(self):
        """Test setDataPrototypeRef/getDataPrototypeRef round-trip and chaining."""
        init_value = PortPrototypeBlueprintInitValue()
        test_ref = RefType().setValue("/Pkg/Blueprint/Dp")
        result = init_value.setDataPrototypeRef(test_ref)
        assert result is init_value
        assert init_value.getDataPrototypeRef() == test_ref

    def test_set_data_prototype_ref_none(self):
        """Test setDataPrototypeRef with None value"""
        init_value = PortPrototypeBlueprintInitValue()
        init_value.setDataPrototypeRef(RefType().setValue("/Pkg/Blueprint/Dp"))
        result = init_value.setDataPrototypeRef(None)
        assert result is init_value
        assert init_value.getDataPrototypeRef().getValue() == "/Pkg/Blueprint/Dp"

    def test_get_set_value(self):
        """Test setValue/getValue round-trip and chaining."""
        init_value = PortPrototypeBlueprintInitValue()
        test_value = TextValueSpecification()
        test_value.setValue("42")
        result = init_value.setValue(test_value)
        assert result is init_value
        assert init_value.getValue() is test_value

    def test_set_value_none(self):
        """Test setValue with None value"""
        init_value = PortPrototypeBlueprintInitValue()
        keep = TextValueSpecification()
        init_value.setValue(keep)
        result = init_value.setValue(None)
        assert result is init_value
        assert init_value.getValue() is keep


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
        assert hasattr(blueprint, "providedComSpecs")
        assert hasattr(blueprint, "requiredComSpecs")

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
        assert hasattr(blueprint, "providedComSpecs")

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
        assert hasattr(blueprint, "requiredComSpecs")

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


class TestPortPrototypeBlueprintMapping:
    """
    Test class for PortPrototypeBlueprintMapping functionality.
    """

    def test_initialization(self):
        obj = PortPrototypeBlueprintMapping()
        assert isinstance(obj, PortPrototypeBlueprintMapping)
        assert obj.getPortPrototypeBlueprintRef() is None
        assert obj.getDerivedPortPrototypeRef() is None

    def test_get_set_port_prototype_blueprint_ref(self):
        obj = PortPrototypeBlueprintMapping()
        ref = RefType()
        ref.setDest("PORT-PROTOTYPE-BLUEPRINT")
        ref.setValue("/Pkg/BlueprintPort")
        obj.setPortPrototypeBlueprintRef(ref)
        assert obj.getPortPrototypeBlueprintRef() is ref
        assert obj.getPortPrototypeBlueprintRef().getDest() == "PORT-PROTOTYPE-BLUEPRINT"
        assert obj.getPortPrototypeBlueprintRef().getValue() == "/Pkg/BlueprintPort"

    def test_get_set_derived_port_prototype_ref(self):
        obj = PortPrototypeBlueprintMapping()
        ref = RefType()
        ref.setDest("P-PORT-PROTOTYPE")
        ref.setValue("/Pkg/Swc/DerivedPort")
        obj.setDerivedPortPrototypeRef(ref)
        assert obj.getDerivedPortPrototypeRef() is ref
        assert obj.getDerivedPortPrototypeRef().getDest() == "P-PORT-PROTOTYPE"
        assert obj.getDerivedPortPrototypeRef().getValue() == "/Pkg/Swc/DerivedPort"

    def test_set_ref_none_is_noop(self):
        obj = PortPrototypeBlueprintMapping()
        obj.setPortPrototypeBlueprintRef(None)
        obj.setDerivedPortPrototypeRef(None)
        assert obj.getPortPrototypeBlueprintRef() is None
        assert obj.getDerivedPortPrototypeRef() is None

    def test_set_ref_chaining(self):
        obj = PortPrototypeBlueprintMapping()
        ref = RefType()
        returned = obj.setPortPrototypeBlueprintRef(ref)
        assert returned is obj
        returned = obj.setDerivedPortPrototypeRef(ref)
        assert returned is obj

    def test_is_atp_blueprint_mapping(self):
        obj = PortPrototypeBlueprintMapping()
        assert isinstance(obj, AtpBlueprintMapping)
