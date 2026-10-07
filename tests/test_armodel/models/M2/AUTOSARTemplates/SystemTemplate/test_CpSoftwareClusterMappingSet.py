import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    CpSoftwareClusterToResourceMapping,
    PortElementToCommunicationResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import (
    CpSoftwareClusterMappingSet,
    CpSoftwareClusterResourceToApplicationPartitionMapping,
    CpSoftwareClusterToApplicationPartitionMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import SwcToApplicationPartitionMapping


class TestCpSoftwareClusterMappingSet:
    """Test cases for CpSoftwareClusterMappingSet (Table 5.49, p.285)."""

    MEMBERS = [
        "portElementToComResourceMappings",
        "resourceToApplicationPartitionMappings",
        "softwareClusterToApplicationPartitionMapping",
        "softwareClusterToResourceMappings",
        "swcToApplicationPartitionMappings",
    ]

    def _new_set(self) -> CpSoftwareClusterMappingSet:
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        pkg = document.createARPackage("pkg")
        return pkg.createCpSoftwareClusterMappingSet("mapping_set")

    def test_inheritance(self):
        assert issubclass(CpSoftwareClusterMappingSet, ARElement)

    def test_class_docstring_note(self):
        expected = (
            "This meta-class represents the ability to aggregate a collection of CP Software Cluster relevant mappings. "
            "This is applicable if a CP Software Cluster is described besides a concrete System, e.g. a reusable CP Software Cluster. "
            "Tags: atp.recommendedPackage=CpSoftwareClusterMappingSets"
        )
        assert inspect.cleandoc(CpSoftwareClusterMappingSet.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert CpSoftwareClusterMappingSet.__init__.__doc__ is None

    def test_initialization_defaults(self):
        mapping_set = self._new_set()
        assert mapping_set.getPortElementToComResourceMappings() == []
        assert mapping_set.getResourceToApplicationPartitionMappings() == []
        assert mapping_set.getSoftwareClusterToApplicationPartitionMapping() is None
        assert mapping_set.getSoftwareClusterToResourceMappings() == []
        assert mapping_set.getSwcToApplicationPartitionMappings() == []

    def test_member_order(self):
        mapping_set = self._new_set()
        members = [k for k in vars(mapping_set) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_create_port_element_to_com_resource_mapping(self):
        mapping_set = self._new_set()
        mapping = mapping_set.createPortElementToComResourceMapping("mapping1")
        assert isinstance(mapping, PortElementToCommunicationResourceMapping)
        assert mapping_set.createPortElementToComResourceMapping("mapping1") is mapping
        assert mapping_set.getPortElementToComResourceMappings() == [mapping]

    def test_create_resource_to_application_partition_mapping(self):
        mapping_set = self._new_set()
        mapping = mapping_set.createResourceToApplicationPartitionMapping("mapping1")
        assert isinstance(mapping, CpSoftwareClusterResourceToApplicationPartitionMapping)
        assert mapping_set.createResourceToApplicationPartitionMapping("mapping1") is mapping
        assert mapping_set.getResourceToApplicationPartitionMappings() == [mapping]

    def test_create_software_cluster_to_application_partition_mapping(self):
        mapping_set = self._new_set()
        mapping = mapping_set.createSoftwareClusterToApplicationPartitionMapping("mapping1")
        assert isinstance(mapping, CpSoftwareClusterToApplicationPartitionMapping)
        assert mapping_set.createSoftwareClusterToApplicationPartitionMapping("mapping2") is mapping
        assert mapping_set.getSoftwareClusterToApplicationPartitionMapping() is mapping

    def test_create_software_cluster_to_resource_mapping(self):
        mapping_set = self._new_set()
        mapping = mapping_set.createSoftwareClusterToResourceMapping("mapping1")
        assert isinstance(mapping, CpSoftwareClusterToResourceMapping)
        assert mapping_set.createSoftwareClusterToResourceMapping("mapping1") is mapping
        assert mapping_set.getSoftwareClusterToResourceMappings() == [mapping]

    def test_create_swc_to_application_partition_mapping(self):
        mapping_set = self._new_set()
        mapping = mapping_set.createSwcToApplicationPartitionMapping("mapping1")
        assert isinstance(mapping, SwcToApplicationPartitionMapping)
        assert mapping_set.createSwcToApplicationPartitionMapping("mapping1") is mapping
        assert mapping_set.getSwcToApplicationPartitionMappings() == [mapping]

    def test_type_hints(self):
        hints = typing.get_type_hints(CpSoftwareClusterMappingSet.getPortElementToComResourceMappings)
        assert hints["return"] == typing.List[PortElementToCommunicationResourceMapping]
        hints = typing.get_type_hints(CpSoftwareClusterMappingSet.getResourceToApplicationPartitionMappings)
        assert hints["return"] == typing.List[CpSoftwareClusterResourceToApplicationPartitionMapping]
        hints = typing.get_type_hints(CpSoftwareClusterMappingSet.getSoftwareClusterToApplicationPartitionMapping)
        assert hints["return"] == typing.Optional[CpSoftwareClusterToApplicationPartitionMapping]
        hints = typing.get_type_hints(CpSoftwareClusterMappingSet.getSoftwareClusterToResourceMappings)
        assert hints["return"] == typing.List[CpSoftwareClusterToResourceMapping]
        hints = typing.get_type_hints(CpSoftwareClusterMappingSet.getSwcToApplicationPartitionMappings)
        assert hints["return"] == typing.List[SwcToApplicationPartitionMapping]
