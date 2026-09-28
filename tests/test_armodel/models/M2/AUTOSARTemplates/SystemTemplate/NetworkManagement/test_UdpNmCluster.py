from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import UdpNmCluster


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _int(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _pos_int(value):
    positive_integer = PositiveInteger()
    positive_integer.setValue(value)
    return positive_integer


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


class TestUdpNmCluster:
    def test_initialization(self):
        cluster = UdpNmCluster(MockParent(), "UdpNmCluster")
        assert cluster.getShortName() == "UdpNmCluster"
        assert cluster.getNmCbvPosition() is None
        assert cluster.getNmImmediateNmCycleTime() is None
        assert cluster.getNmImmediateNmTransmissions() is None
        assert cluster.getNmMessageTimeoutTime() is None
        assert cluster.getNmMsgCycleTime() is None
        assert cluster.getNmNetworkTimeout() is None
        assert cluster.getNmNidPosition() is None
        assert cluster.getNmRemoteSleepIndicationTime() is None
        assert cluster.getNmRepeatMessageTime() is None
        assert cluster.getNmWaitBusSleepTime() is None
        assert cluster.getVlanRef() is None

    def test_get_set_integers(self):
        cluster = UdpNmCluster(MockParent(), "UdpNmCluster")
        pairs = [
            (cluster.setNmCbvPosition, cluster.getNmCbvPosition),
            (cluster.setNmNidPosition, cluster.getNmNidPosition),
        ]
        for setter, getter in pairs:
            value = _int("3")
            assert setter(value) is cluster
            assert getter() is value
            setter(None)
            assert getter() is value

    def test_get_set_times(self):
        cluster = UdpNmCluster(MockParent(), "UdpNmCluster")
        pairs = [
            (cluster.setNmImmediateNmCycleTime, cluster.getNmImmediateNmCycleTime),
            (cluster.setNmMessageTimeoutTime, cluster.getNmMessageTimeoutTime),
            (cluster.setNmMsgCycleTime, cluster.getNmMsgCycleTime),
            (cluster.setNmNetworkTimeout, cluster.getNmNetworkTimeout),
            (cluster.setNmRemoteSleepIndicationTime, cluster.getNmRemoteSleepIndicationTime),
            (cluster.setNmRepeatMessageTime, cluster.getNmRepeatMessageTime),
            (cluster.setNmWaitBusSleepTime, cluster.getNmWaitBusSleepTime),
        ]
        for setter, getter in pairs:
            value = _time("0.05")
            assert setter(value) is cluster
            assert getter() is value
            setter(None)
            assert getter() is value

    def test_get_set_nm_immediate_nm_transmissions(self):
        cluster = UdpNmCluster(MockParent(), "UdpNmCluster")
        value = _pos_int("4")
        assert cluster.setNmImmediateNmTransmissions(value) is cluster
        assert cluster.getNmImmediateNmTransmissions() is value
        cluster.setNmImmediateNmTransmissions(None)
        assert cluster.getNmImmediateNmTransmissions() is value

    def test_get_set_vlan_ref(self):
        cluster = UdpNmCluster(MockParent(), "UdpNmCluster")
        ref = _ref("ETHERNET-PHYSICAL-CHANNEL", "/Topology/Vlan1")
        assert cluster.setVlanRef(ref) is cluster
        assert cluster.getVlanRef() is ref
        cluster.setVlanRef(None)
        assert cluster.getVlanRef() is ref
