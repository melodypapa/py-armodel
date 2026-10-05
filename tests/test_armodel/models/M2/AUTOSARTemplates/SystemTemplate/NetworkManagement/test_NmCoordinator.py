from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import NmCoordinator


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _integer(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestNmCoordinator:
    def test_initialization(self):
        coordinator = NmCoordinator()
        assert coordinator.getIndex() is None
        assert coordinator.getNmCoordSyncSupport() is None
        assert coordinator.getNmGlobalCoordinatorTime() is None
        assert coordinator.getNmNodes() == []

    def test_get_set_index(self):
        coordinator = NmCoordinator()
        value = _integer(1)
        assert coordinator.setIndex(value) is coordinator
        assert coordinator.getIndex() is value
        coordinator.setIndex(None)
        assert coordinator.getIndex() is value

    def test_get_set_nm_coord_sync_support(self):
        coordinator = NmCoordinator()
        value = _bool(True)
        assert coordinator.setNmCoordSyncSupport(value) is coordinator
        assert coordinator.getNmCoordSyncSupport() is value
        coordinator.setNmCoordSyncSupport(None)
        assert coordinator.getNmCoordSyncSupport() is value

    def test_get_set_nm_global_coordinator_time(self):
        coordinator = NmCoordinator()
        value = _time("2.5")
        assert coordinator.setNmGlobalCoordinatorTime(value) is coordinator
        assert coordinator.getNmGlobalCoordinatorTime() is value
        coordinator.setNmGlobalCoordinatorTime(None)
        assert coordinator.getNmGlobalCoordinatorTime() is value

    def test_add_get_nm_nodes(self):
        coordinator = NmCoordinator()
        ref = _ref("NM-NODE", "/Clusters/Can1/node")
        assert coordinator.addNmNode(ref) is coordinator
        assert coordinator.getNmNodes() == [ref]
        coordinator.addNmNode(None)
        assert coordinator.getNmNodes() == [ref]
