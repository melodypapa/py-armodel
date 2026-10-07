import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import SystemSignalToCommunicationResourceMapping


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestSystemSignalToCommunicationResourceMapping:
    """Test cases for SystemSignalToCommunicationResourceMapping (Table 5.51, p.289)."""

    MEMBERS = [
        "softwareClusterComResourceRef",
        "systemSignalRef",
    ]

    def test_inheritance(self):
        assert issubclass(SystemSignalToCommunicationResourceMapping, Identifiable)

    def test_class_docstring_note(self):
        expected = (
            "This meta class maps a communication resource to a SystemSignal. This mapping can be used in an early process stage "
            "in which the DataMapping linking the Ports and mapped CpSoftwareCluster CommunicationResource(s) to the SystemSignal "
            "is not yet available."
        )
        assert inspect.cleandoc(SystemSignalToCommunicationResourceMapping.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert SystemSignalToCommunicationResourceMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        mapping = SystemSignalToCommunicationResourceMapping(MockParent(), "mapping")
        assert mapping.getSoftwareClusterComResourceRef() is None
        assert mapping.getSystemSignalRef() is None

    def test_member_order(self):
        mapping = SystemSignalToCommunicationResourceMapping(MockParent(), "mapping")
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_software_cluster_com_resource_ref(self):
        mapping = SystemSignalToCommunicationResourceMapping(MockParent(), "mapping")
        ref = RefType()
        ref.setValue("/Resources/MyComResource")
        ref.setDest("CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE")
        result = mapping.setSoftwareClusterComResourceRef(ref)
        assert result is mapping
        assert mapping.getSoftwareClusterComResourceRef() is ref
        mapping.setSoftwareClusterComResourceRef(None)
        assert mapping.getSoftwareClusterComResourceRef() is ref

    def test_system_signal_ref(self):
        mapping = SystemSignalToCommunicationResourceMapping(MockParent(), "mapping")
        ref = RefType()
        ref.setValue("/Signals/MySignal")
        ref.setDest("SYSTEM-SIGNAL")
        result = mapping.setSystemSignalRef(ref)
        assert result is mapping
        assert mapping.getSystemSignalRef() is ref
        mapping.setSystemSignalRef(None)
        assert mapping.getSystemSignalRef() is ref

    def test_type_hints(self):
        hints = typing.get_type_hints(SystemSignalToCommunicationResourceMapping.getSoftwareClusterComResourceRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(SystemSignalToCommunicationResourceMapping.setSoftwareClusterComResourceRef)
        assert hints["return"] is SystemSignalToCommunicationResourceMapping
        hints = typing.get_type_hints(SystemSignalToCommunicationResourceMapping.getSystemSignalRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(SystemSignalToCommunicationResourceMapping.setSystemSignalRef)
        assert hints["return"] is SystemSignalToCommunicationResourceMapping
