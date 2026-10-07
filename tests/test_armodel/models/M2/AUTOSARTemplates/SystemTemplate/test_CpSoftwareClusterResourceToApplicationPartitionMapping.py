import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import CpSoftwareClusterResourceToApplicationPartitionMapping


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestCpSoftwareClusterResourceToApplicationPartitionMapping:
    """Test cases for CpSoftwareClusterResourceToApplicationPartitionMapping (Table 5.48, p.284)."""

    MEMBERS = [
        "applicationPartitionRef",
        "resourceRef",
    ]

    def test_inheritance(self):
        assert issubclass(CpSoftwareClusterResourceToApplicationPartitionMapping, Identifiable)

    def test_class_docstring_note(self):
        expected = "This meta class maps a Software Cluster resource to an Application Partition to restrict the usage."
        assert inspect.cleandoc(CpSoftwareClusterResourceToApplicationPartitionMapping.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert CpSoftwareClusterResourceToApplicationPartitionMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        mapping = CpSoftwareClusterResourceToApplicationPartitionMapping(MockParent(), "mapping")
        assert mapping.getApplicationPartitionRef() is None
        assert mapping.getResourceRef() is None

    def test_member_order(self):
        mapping = CpSoftwareClusterResourceToApplicationPartitionMapping(MockParent(), "mapping")
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_application_partition_ref(self):
        mapping = CpSoftwareClusterResourceToApplicationPartitionMapping(MockParent(), "mapping")
        ref = RefType()
        ref.setValue("/Partitions/MyPartition")
        ref.setDest("APPLICATION-PARTITION")
        result = mapping.setApplicationPartitionRef(ref)
        assert result is mapping
        assert mapping.getApplicationPartitionRef() is ref
        mapping.setApplicationPartitionRef(None)
        assert mapping.getApplicationPartitionRef() is ref

    def test_resource_ref(self):
        mapping = CpSoftwareClusterResourceToApplicationPartitionMapping(MockParent(), "mapping")
        ref = RefType()
        ref.setValue("/Resources/MyResource")
        ref.setDest("CP-SOFTWARE-CLUSTER-RESOURCE")
        result = mapping.setResourceRef(ref)
        assert result is mapping
        assert mapping.getResourceRef() is ref
        mapping.setResourceRef(None)
        assert mapping.getResourceRef() is ref

    def test_type_hints(self):
        hints = typing.get_type_hints(CpSoftwareClusterResourceToApplicationPartitionMapping.getApplicationPartitionRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(CpSoftwareClusterResourceToApplicationPartitionMapping.setApplicationPartitionRef)
        assert hints["return"] is CpSoftwareClusterResourceToApplicationPartitionMapping
        hints = typing.get_type_hints(CpSoftwareClusterResourceToApplicationPartitionMapping.getResourceRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(CpSoftwareClusterResourceToApplicationPartitionMapping.setResourceRef)
        assert hints["return"] is CpSoftwareClusterResourceToApplicationPartitionMapping
