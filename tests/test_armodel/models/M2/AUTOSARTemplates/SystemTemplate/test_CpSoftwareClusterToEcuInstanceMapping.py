import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import CpSoftwareClusterToEcuInstanceMapping


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestCpSoftwareClusterToEcuInstanceMapping:
    """Test cases for CpSoftwareClusterToEcuInstanceMapping (Table 5.47, p.283)."""

    MEMBERS = [
        "ecuInstanceRef",
        "machineId",
        "swClusterRefs",
    ]

    def test_inheritance(self):
        assert issubclass(CpSoftwareClusterToEcuInstanceMapping, Identifiable)

    def test_class_docstring_note(self):
        expected = "This meta class maps a CpSoftwareCluster to a EcuInstance."
        assert inspect.cleandoc(CpSoftwareClusterToEcuInstanceMapping.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert CpSoftwareClusterToEcuInstanceMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        mapping = CpSoftwareClusterToEcuInstanceMapping(MockParent(), "mapping")
        assert mapping.getEcuInstanceRef() is None
        assert mapping.getMachineId() is None
        assert mapping.getSwClusterRefs() == []

    def test_member_order(self):
        mapping = CpSoftwareClusterToEcuInstanceMapping(MockParent(), "mapping")
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_ecu_instance_ref(self):
        mapping = CpSoftwareClusterToEcuInstanceMapping(MockParent(), "mapping")
        ref = RefType()
        ref.setValue("/EcuInstances/MyEcu")
        ref.setDest("ECU-INSTANCE")
        result = mapping.setEcuInstanceRef(ref)
        assert result is mapping
        assert mapping.getEcuInstanceRef() is ref
        mapping.setEcuInstanceRef(None)
        assert mapping.getEcuInstanceRef() is ref

    def test_machine_id(self):
        mapping = CpSoftwareClusterToEcuInstanceMapping(MockParent(), "mapping")
        machine_id = PositiveInteger()
        machine_id.setValue(1)
        result = mapping.setMachineId(machine_id)
        assert result is mapping
        assert mapping.getMachineId() is machine_id
        mapping.setMachineId(None)
        assert mapping.getMachineId() is machine_id

    def test_add_sw_cluster_ref(self):
        mapping = CpSoftwareClusterToEcuInstanceMapping(MockParent(), "mapping")
        ref1 = RefType()
        ref1.setValue("/Clusters/Cluster1")
        ref1.setDest("CP-SOFTWARE-CLUSTER")
        ref2 = RefType()
        ref2.setValue("/Clusters/Cluster2")
        ref2.setDest("CP-SOFTWARE-CLUSTER")
        result = mapping.addSwClusterRef(ref1)
        assert result is mapping
        mapping.addSwClusterRef(ref2)
        assert mapping.getSwClusterRefs() == [ref1, ref2]
        mapping.addSwClusterRef(None)
        assert len(mapping.getSwClusterRefs()) == 2

    def test_type_hints(self):
        hints = typing.get_type_hints(CpSoftwareClusterToEcuInstanceMapping.getEcuInstanceRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(CpSoftwareClusterToEcuInstanceMapping.setEcuInstanceRef)
        assert hints["return"] is CpSoftwareClusterToEcuInstanceMapping
        hints = typing.get_type_hints(CpSoftwareClusterToEcuInstanceMapping.getMachineId)
        assert hints["return"] == typing.Optional[PositiveInteger]
        hints = typing.get_type_hints(CpSoftwareClusterToEcuInstanceMapping.getSwClusterRefs)
        assert hints["return"] == typing.List[RefType]
        hints = typing.get_type_hints(CpSoftwareClusterToEcuInstanceMapping.addSwClusterRef)
        assert hints["return"] is CpSoftwareClusterToEcuInstanceMapping
