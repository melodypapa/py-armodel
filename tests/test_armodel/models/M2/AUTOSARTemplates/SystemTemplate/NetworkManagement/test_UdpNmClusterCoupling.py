from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import UdpNmClusterCoupling


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestUdpNmClusterCoupling:
    def test_initialization(self):
        coupling = UdpNmClusterCoupling()
        assert coupling.getCoupledClusterRefs() == []
        assert coupling.getNmImmediateRestartEnabled() is None

    def test_add_get_coupled_cluster_refs(self):
        coupling = UdpNmClusterCoupling()
        ref = _ref("ETHERNET-CLUSTER", "/Clusters/Eth1")
        assert coupling.addCoupledClusterRef(ref) is coupling
        assert coupling.getCoupledClusterRefs() == [ref]

    def test_get_set_nm_immediate_restart_enabled(self):
        coupling = UdpNmClusterCoupling()
        value = _bool(True)
        assert coupling.setNmImmediateRestartEnabled(value) is coupling
        assert coupling.getNmImmediateRestartEnabled() is value
        coupling.setNmImmediateRestartEnabled(None)
        assert coupling.getNmImmediateRestartEnabled() is value
