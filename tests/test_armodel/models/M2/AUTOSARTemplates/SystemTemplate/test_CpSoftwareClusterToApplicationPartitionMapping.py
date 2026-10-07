import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import CpSoftwareClusterToApplicationPartitionMapping


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestCpSoftwareClusterToApplicationPartitionMapping:
    """Test cases for CpSoftwareClusterToApplicationPartitionMapping (Table 5.50, p.287)."""

    MEMBERS = [
        "applicationPartitionRefs",
        "softwareClusterRef",
    ]

    def test_inheritance(self):
        assert issubclass(CpSoftwareClusterToApplicationPartitionMapping, Identifiable)

    def test_class_docstring_note(self):
        expected = "This meta class defines ApplicationPartitions that are applicable for the CpSoftwareCluster."
        assert inspect.cleandoc(CpSoftwareClusterToApplicationPartitionMapping.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert CpSoftwareClusterToApplicationPartitionMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        mapping = CpSoftwareClusterToApplicationPartitionMapping(MockParent(), "mapping")
        assert mapping.getApplicationPartitionRefs() == []
        assert mapping.getSoftwareClusterRef() is None

    def test_member_order(self):
        mapping = CpSoftwareClusterToApplicationPartitionMapping(MockParent(), "mapping")
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_add_application_partition_ref(self):
        mapping = CpSoftwareClusterToApplicationPartitionMapping(MockParent(), "mapping")
        ref1 = RefType()
        ref1.setValue("/Partitions/Partition1")
        ref1.setDest("APPLICATION-PARTITION")
        ref2 = RefType()
        ref2.setValue("/Partitions/Partition2")
        ref2.setDest("APPLICATION-PARTITION")
        result = mapping.addApplicationPartitionRef(ref1)
        assert result is mapping
        mapping.addApplicationPartitionRef(ref2)
        assert mapping.getApplicationPartitionRefs() == [ref1, ref2]
        mapping.addApplicationPartitionRef(None)
        assert len(mapping.getApplicationPartitionRefs()) == 2

    def test_software_cluster_ref(self):
        mapping = CpSoftwareClusterToApplicationPartitionMapping(MockParent(), "mapping")
        ref = RefType()
        ref.setValue("/Clusters/MyCluster")
        ref.setDest("CP-SOFTWARE-CLUSTER")
        result = mapping.setSoftwareClusterRef(ref)
        assert result is mapping
        assert mapping.getSoftwareClusterRef() is ref
        mapping.setSoftwareClusterRef(None)
        assert mapping.getSoftwareClusterRef() is ref

    def test_type_hints(self):
        hints = typing.get_type_hints(CpSoftwareClusterToApplicationPartitionMapping.getApplicationPartitionRefs)
        assert hints["return"] == typing.List[RefType]
        hints = typing.get_type_hints(CpSoftwareClusterToApplicationPartitionMapping.addApplicationPartitionRef)
        assert hints["return"] is CpSoftwareClusterToApplicationPartitionMapping
        hints = typing.get_type_hints(CpSoftwareClusterToApplicationPartitionMapping.getSoftwareClusterRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(CpSoftwareClusterToApplicationPartitionMapping.setSoftwareClusterRef)
        assert hints["return"] is CpSoftwareClusterToApplicationPartitionMapping
