import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import SwcToApplicationPartitionMapping


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestSwcToApplicationPartitionMapping:
    """Test cases for SwcToApplicationPartitionMapping (Table 5.4, p.200)."""

    MEMBERS = [
        "applicationPartitionRef",
        "swComponentPrototypeIRef",
    ]

    def test_inheritance(self):
        assert issubclass(SwcToApplicationPartitionMapping, Identifiable)
        assert issubclass(SwcToApplicationPartitionMapping, VariationPointCapable)

    def test_class_docstring_note(self):
        expected = "Allows to map a given SwComponentPrototype to a formally defined partition at a point in time " "when the corresponding EcuInstance is not yet known or defined."
        assert inspect.cleandoc(SwcToApplicationPartitionMapping.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert SwcToApplicationPartitionMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        parent = MockParent()
        mapping = SwcToApplicationPartitionMapping(parent, "test_swc_app_partition_mapping")
        assert mapping.getApplicationPartitionRef() is None
        assert mapping.getSwComponentPrototypeIRef() is None

    def test_member_order(self):
        parent = MockParent()
        mapping = SwcToApplicationPartitionMapping(parent, "test_swc_app_partition_mapping")
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_application_partition_ref(self):
        parent = MockParent()
        mapping = SwcToApplicationPartitionMapping(parent, "test_swc_app_partition_mapping")
        value = RefType()
        value.setValue("/ApplicationPartitions/AP1")
        value.setDest("APPLICATION-PARTITION")
        result = mapping.setApplicationPartitionRef(value)
        assert result is mapping
        assert mapping.getApplicationPartitionRef() is value
        mapping.setApplicationPartitionRef(None)
        assert mapping.getApplicationPartitionRef() is value

    def test_get_set_sw_component_prototype_iref(self):
        parent = MockParent()
        mapping = SwcToApplicationPartitionMapping(parent, "test_swc_app_partition_mapping")
        iref = ComponentInSystemInstanceRef()
        result = mapping.setSwComponentPrototypeIRef(iref)
        assert result is mapping
        assert mapping.getSwComponentPrototypeIRef() is iref
        mapping.setSwComponentPrototypeIRef(None)
        assert mapping.getSwComponentPrototypeIRef() is iref

    def test_type_hints(self):
        hints = typing.get_type_hints(SwcToApplicationPartitionMapping.getApplicationPartitionRef)
        assert hints.get("return") == typing.Optional[RefType]
        hints = typing.get_type_hints(SwcToApplicationPartitionMapping.setApplicationPartitionRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is SwcToApplicationPartitionMapping
        hints = typing.get_type_hints(SwcToApplicationPartitionMapping.getSwComponentPrototypeIRef)
        assert hints.get("return") == typing.Optional[ComponentInSystemInstanceRef]
        hints = typing.get_type_hints(SwcToApplicationPartitionMapping.setSwComponentPrototypeIRef)
        assert hints.get("value") == typing.Optional[ComponentInSystemInstanceRef]
        assert hints.get("return") is SwcToApplicationPartitionMapping
