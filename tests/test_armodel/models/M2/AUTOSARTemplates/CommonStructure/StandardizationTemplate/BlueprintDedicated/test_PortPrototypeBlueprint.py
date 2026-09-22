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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NonqueuedReceiverComSpec, NonqueuedSenderComSpec

# Table 4.10 Note (AUTOSAR_FO_TPS_StandardizationTemplate, p.60), verbatim.
PPBIV_NOTE = (
    "This meta-class represents the ability to express init values in PortPrototypeBlueprints. " "These init values act as a kind of blueprint from which for example proper ComSpecs can be derived."
)

# Table 4.9 Note (AUTOSAR_FO_TPS_StandardizationTemplate, p.60), verbatim;
# markdown word-split "Port Interfaces" corrected against the XSD "PortInterfaces".
PPB_NOTE = (
    "This meta-class represents the ability to express a blueprint of a PortPrototype by referring to a particular PortInterface. "
    "This blueprint can then be used as a guidance to create particular PortPrototypes which are defined according to this blueprint. "
    "By this it is possible to standardize application interfaces without the need to also standardize software-components with "
    "PortPrototypes typed by the standardized PortInterfaces. Tags: atp.recommendedPackage=PortPrototypeBlueprints"
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
        """Test PortPrototypeBlueprint default values (Table 4.9)."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")

        assert isinstance(blueprint, AtpStructureElement)
        assert blueprint.getShortName() == "TestBlueprint"
        assert blueprint.getInitValues() == []
        assert blueprint.getInterfaceRef() is None
        assert blueprint.getProvidedComSpecs() == []
        assert blueprint.getRequiredComSpecs() == []

    def test_issubclass(self):
        """Base per Table 4.9 is AtpStructureElement (deepest of the Base closure in the model)."""
        assert issubclass(PortPrototypeBlueprint, AtpStructureElement)
        assert issubclass(PortPrototypeBlueprint, Identifiable)
        assert issubclass(PortPrototypeBlueprint, ARObject)

    def test_docstring(self):
        """Class docstring is the Table 4.9 Note verbatim; member Notes on accessors."""
        assert PortPrototypeBlueprint.__doc__.strip() == PPB_NOTE
        assert PortPrototypeBlueprint.__init__.__doc__ is None

        assert _norm(PortPrototypeBlueprint.getInitValues.__doc__) == "This specifies the init values for the dataElements in the particular PortPrototypeBlueprint."
        assert _norm(PortPrototypeBlueprint.setInitValues.__doc__) == (
            "This specifies the init values for the dataElements in the particular PortPrototypeBlueprint. A None value is a no-op and does not overwrite the existing initValues list."
        )
        assert _norm(PortPrototypeBlueprint.addInitValue.__doc__) == (
            "This specifies the init values for the dataElements in the particular PortPrototypeBlueprint. A None value is a no-op and does not extend the initValue list."
        )
        assert _norm(PortPrototypeBlueprint.getInterfaceRef.__doc__) == "This is the interface for which the blueprint is defined. It may be a blueprint itself or a standardized PortInterface"
        assert _norm(PortPrototypeBlueprint.setInterfaceRef.__doc__) == (
            "This is the interface for which the blueprint is defined. It may be a blueprint itself or a standardized PortInterface A None value is a no-op and does not overwrite an existing interfaceRef."
        )
        assert _norm(PortPrototypeBlueprint.getProvidedComSpecs.__doc__) == "Provided communication attributes per interface element (data element or operation)."
        assert _norm(PortPrototypeBlueprint.addProvidedComSpec.__doc__) == (
            "Provided communication attributes per interface element (data element or operation). A None value is a no-op and does not extend the providedComSpec list."
        )
        assert _norm(PortPrototypeBlueprint.getRequiredComSpecs.__doc__) == "Required communication attributes, one for each interface element."
        assert _norm(PortPrototypeBlueprint.addRequiredComSpec.__doc__) == (
            "Required communication attributes, one for each interface element. A None value is a no-op and does not extend the requiredComSpec list."
        )

    def test_get_set_init_values(self):
        """Test setInitValues/getInitValues round-trip and chaining."""
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
        assert blueprint.getInitValues() == []

    def test_add_init_values(self):
        """Test addInitValue aggregation."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")

        first = PortPrototypeBlueprintInitValue()
        second = PortPrototypeBlueprintInitValue()
        assert blueprint.addInitValue(first) is blueprint
        assert blueprint.addInitValue(second) is blueprint
        assert blueprint.addInitValue(None) is blueprint
        assert blueprint.getInitValues() == [first, second]

    def test_get_set_interface_ref(self):
        """Test setInterfaceRef/getInterfaceRef round-trip and chaining."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")
        test_ref = RefType().setDest("SENDER-RECEIVER-INTERFACE").setValue("/AUTOSAR/If")
        result = blueprint.setInterfaceRef(test_ref)
        assert result is blueprint
        assert blueprint.getInterfaceRef() == test_ref

    def test_set_interface_ref_none(self):
        """Test setInterfaceRef with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")
        blueprint.setInterfaceRef(RefType().setValue("/AUTOSAR/If"))
        result = blueprint.setInterfaceRef(None)
        assert result is blueprint
        assert blueprint.getInterfaceRef().getValue() == "/AUTOSAR/If"

    def test_add_provided_com_specs(self):
        """Test addProvidedComSpec aggregation."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")

        spec = NonqueuedSenderComSpec()
        assert blueprint.addProvidedComSpec(spec) is blueprint
        assert blueprint.addProvidedComSpec(None) is blueprint
        assert blueprint.getProvidedComSpecs() == [spec]

    def test_set_provided_com_specs(self):
        """Test setProvidedComSpecs round-trip and None no-op"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")

        spec = NonqueuedSenderComSpec()
        result = blueprint.setProvidedComSpecs([spec])
        assert result is blueprint
        assert blueprint.getProvidedComSpecs() == [spec]
        assert blueprint.setProvidedComSpecs(None) is blueprint
        assert blueprint.getProvidedComSpecs() == [spec]

    def test_add_required_com_specs(self):
        """Test addRequiredComSpec aggregation."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")

        spec = NonqueuedReceiverComSpec()
        assert blueprint.addRequiredComSpec(spec) is blueprint
        assert blueprint.addRequiredComSpec(None) is blueprint
        assert blueprint.getRequiredComSpecs() == [spec]

    def test_set_required_com_specs(self):
        """Test setRequiredComSpecs round-trip and None no-op"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        blueprint = PortPrototypeBlueprint(ar_root, "TestBlueprint")

        spec = NonqueuedReceiverComSpec()
        result = blueprint.setRequiredComSpecs([spec])
        assert result is blueprint
        assert blueprint.getRequiredComSpecs() == [spec]
        assert blueprint.setRequiredComSpecs(None) is blueprint
        assert blueprint.getRequiredComSpecs() == [spec]


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
