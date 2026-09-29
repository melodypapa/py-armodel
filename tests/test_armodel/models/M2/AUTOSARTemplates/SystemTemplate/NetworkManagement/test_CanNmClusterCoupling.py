from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmClusterCoupling


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestCanNmClusterCoupling:
    def test_initialization(self):
        coupling = CanNmClusterCoupling()
        assert coupling.getCoupledClusterRefs() == []
        assert coupling.getNmBusloadReductionEnabled() is None
        assert coupling.getNmImmediateRestartEnabled() is None

    def test_add_get_coupled_cluster_refs(self):
        coupling = CanNmClusterCoupling()
        ref = _ref("CAN-CLUSTER", "/Clusters/Can1")
        assert coupling.addCoupledClusterRef(ref) is coupling
        assert coupling.getCoupledClusterRefs() == [ref]

    def test_get_set_nm_busload_reduction_enabled(self):
        coupling = CanNmClusterCoupling()
        value = _bool(True)
        assert coupling.setNmBusloadReductionEnabled(value) is coupling
        assert coupling.getNmBusloadReductionEnabled() is value
        coupling.setNmBusloadReductionEnabled(None)
        assert coupling.getNmBusloadReductionEnabled() is value

    def test_get_set_nm_immediate_restart_enabled(self):
        coupling = CanNmClusterCoupling()
        value = _bool(False)
        assert coupling.setNmImmediateRestartEnabled(value) is coupling
        assert coupling.getNmImmediateRestartEnabled() is value
        coupling.setNmImmediateRestartEnabled(None)
        assert coupling.getNmImmediateRestartEnabled() is value
