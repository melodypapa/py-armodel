import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import ApplicationPartitionToEcuPartitionMapping, SwcToImplMapping


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_SWmapping:
    """Test cases for SWmapping-related classes."""

    def test_SwcToImplMapping(self):
        """Test SwcToImplMapping class functionality."""
        parent = MockParent()
        mapping = SwcToImplMapping(parent, "test_sw_impl_mapping")

        assert isinstance(mapping, Identifiable)

        # Test default values
        assert mapping.getComponentIRefs() == []
        assert mapping.getComponentImplementationRef() is None

        # Test setter/getter methods
        mock_impl_ref = "mock_impl_ref"
        mapping.setComponentImplementationRef(mock_impl_ref)
        assert mapping.getComponentImplementationRef() == mock_impl_ref

        # Test adding component IRefs
        mock_comp_ref = ComponentInSystemInstanceRef()
        mapping.addComponentIRef(mock_comp_ref)
        assert mapping.getComponentIRefs() == [mock_comp_ref]

        # Test multiple component refs
        mock_comp_ref2 = ComponentInSystemInstanceRef()
        mapping.addComponentIRef(mock_comp_ref2)
        assert mapping.getComponentIRefs() == [mock_comp_ref, mock_comp_ref2]

    def test_ApplicationPartitionToEcuPartitionMapping(self):
        """Test ApplicationPartitionToEcuPartitionMapping class functionality."""
        parent = MockParent()
        mapping = ApplicationPartitionToEcuPartitionMapping(parent, "test_app_ecu_part_mapping")

        assert isinstance(mapping, Identifiable)

        # Test default values
        assert mapping.getApplicationPartitionRefs() == []
        assert mapping.getEcuPartitionRef() is None

        # Test setter/getter methods
        mock_ecu_part_ref = "mock_ecu_part_ref"
        mapping.setEcuPartitionRef(mock_ecu_part_ref)
        assert mapping.getEcuPartitionRef() == mock_ecu_part_ref

        # Test adding application partition refs
        mock_app_part_ref1 = "app_part_ref1"
        mock_app_part_ref2 = "app_part_ref2"
        mapping.addApplicationPartitionRef(mock_app_part_ref1)
        mapping.addApplicationPartitionRef(mock_app_part_ref2)
        assert mapping.getApplicationPartitionRefs() == [mock_app_part_ref1, mock_app_part_ref2]


class Test_ApplicationPartitionToEcuPartitionMappingSpec:
    """Test cases for ApplicationPartitionToEcuPartitionMapping (Table 5.6, p.201)."""

    MEMBERS = [
        "applicationPartitionRefs",
        "ecuPartitionRef",
    ]

    def test_inheritance(self):
        assert issubclass(ApplicationPartitionToEcuPartitionMapping, Identifiable)
        assert issubclass(ApplicationPartitionToEcuPartitionMapping, VariationPointCapable)

    def test_class_docstring_note(self):
        expected = (
            "Maps ApplicationPartitions to EcuPartitions. With this mapping an OEM has the option to predefine "
            "an allocation of Software Components to EcuPartitions in the System Design phase. The final and "
            "complete assignment is described in the OS Configuration."
        )
        assert inspect.cleandoc(ApplicationPartitionToEcuPartitionMapping.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert ApplicationPartitionToEcuPartitionMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        parent = MockParent()
        mapping = ApplicationPartitionToEcuPartitionMapping(parent, "test_app_ecu_part_mapping")
        assert mapping.getApplicationPartitionRefs() == []
        assert mapping.getEcuPartitionRef() is None

    def test_member_order(self):
        parent = MockParent()
        mapping = ApplicationPartitionToEcuPartitionMapping(parent, "test_app_ecu_part_mapping")
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_add_application_partition_ref(self):
        parent = MockParent()
        mapping = ApplicationPartitionToEcuPartitionMapping(parent, "test_app_ecu_part_mapping")
        ref = RefType()
        ref.setValue("/ApplicationPartitions/AP1")
        result = mapping.addApplicationPartitionRef(ref)
        assert result is mapping
        assert mapping.getApplicationPartitionRefs() == [ref]
        ref2 = RefType()
        ref2.setValue("/ApplicationPartitions/AP2")
        mapping.addApplicationPartitionRef(ref2)
        assert mapping.getApplicationPartitionRefs() == [ref, ref2]
        mapping.addApplicationPartitionRef(None)
        assert mapping.getApplicationPartitionRefs() == [ref, ref2]

    def test_get_set_ecu_partition_ref(self):
        parent = MockParent()
        mapping = ApplicationPartitionToEcuPartitionMapping(parent, "test_app_ecu_part_mapping")
        value = RefType()
        value.setValue("/EcuInstances/Ecu1/PARTITIONS/P1")
        result = mapping.setEcuPartitionRef(value)
        assert result is mapping
        assert mapping.getEcuPartitionRef() is value
        mapping.setEcuPartitionRef(None)
        assert mapping.getEcuPartitionRef() is value

    def test_type_hints(self):
        hints = typing.get_type_hints(ApplicationPartitionToEcuPartitionMapping.getApplicationPartitionRefs)
        assert hints.get("return") == typing.List[RefType]
        hints = typing.get_type_hints(ApplicationPartitionToEcuPartitionMapping.addApplicationPartitionRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is ApplicationPartitionToEcuPartitionMapping
        hints = typing.get_type_hints(ApplicationPartitionToEcuPartitionMapping.getEcuPartitionRef)
        assert hints.get("return") == typing.Optional[RefType]
        hints = typing.get_type_hints(ApplicationPartitionToEcuPartitionMapping.setEcuPartitionRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is ApplicationPartitionToEcuPartitionMapping
