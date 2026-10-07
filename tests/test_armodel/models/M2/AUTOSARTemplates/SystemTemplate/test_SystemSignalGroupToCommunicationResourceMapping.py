import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import SystemSignalGroupToCommunicationResourceMapping


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestSystemSignalGroupToCommunicationResourceMapping:
    """Test cases for SystemSignalGroupToCommunicationResourceMapping (Table 5.52, p.290)."""

    MEMBERS = [
        "softwareClusterComResourceRef",
        "systemSignalGroupRef",
    ]

    def test_inheritance(self):
        assert issubclass(SystemSignalGroupToCommunicationResourceMapping, Identifiable)

    def test_class_docstring_note(self):
        expected = (
            "This meta class maps a communication resource to a SystemSignalGroup. This mapping can be used in an early process stage "
            "in which the DataMapping linking the Ports and mapped CpSoftwareCluster CommunicationResource(s) to SystemSignals of a "
            "SystemSignalGroup is not yet available."
        )
        assert inspect.cleandoc(SystemSignalGroupToCommunicationResourceMapping.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert SystemSignalGroupToCommunicationResourceMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        mapping = SystemSignalGroupToCommunicationResourceMapping(MockParent(), "mapping")
        assert mapping.getSoftwareClusterComResourceRef() is None
        assert mapping.getSystemSignalGroupRef() is None

    def test_member_order(self):
        mapping = SystemSignalGroupToCommunicationResourceMapping(MockParent(), "mapping")
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_software_cluster_com_resource_ref(self):
        mapping = SystemSignalGroupToCommunicationResourceMapping(MockParent(), "mapping")
        ref = RefType()
        ref.setValue("/Resources/MyComResource")
        ref.setDest("CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE")
        result = mapping.setSoftwareClusterComResourceRef(ref)
        assert result is mapping
        assert mapping.getSoftwareClusterComResourceRef() is ref
        mapping.setSoftwareClusterComResourceRef(None)
        assert mapping.getSoftwareClusterComResourceRef() is ref

    def test_system_signal_ref(self):
        mapping = SystemSignalGroupToCommunicationResourceMapping(MockParent(), "mapping")
        ref = RefType()
        ref.setValue("/SignalGroups/MySignalGroup")
        ref.setDest("SYSTEM-SIGNAL-GROUP")
        result = mapping.setSystemSignalGroupRef(ref)
        assert result is mapping
        assert mapping.getSystemSignalGroupRef() is ref
        mapping.setSystemSignalGroupRef(None)
        assert mapping.getSystemSignalGroupRef() is ref

    def test_type_hints(self):
        hints = typing.get_type_hints(SystemSignalGroupToCommunicationResourceMapping.getSoftwareClusterComResourceRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(SystemSignalGroupToCommunicationResourceMapping.setSoftwareClusterComResourceRef)
        assert hints["return"] is SystemSignalGroupToCommunicationResourceMapping
        hints = typing.get_type_hints(SystemSignalGroupToCommunicationResourceMapping.getSystemSignalGroupRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(SystemSignalGroupToCommunicationResourceMapping.setSystemSignalGroupRef)
        assert hints["return"] is SystemSignalGroupToCommunicationResourceMapping
