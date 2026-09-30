from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmCluster


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


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


class TestCanNmCluster:
    def test_initialization(self):
        cluster = CanNmCluster(MockParent(), "CanNmCluster")
        assert cluster.getShortName() == "CanNmCluster"
        assert cluster.getNmBusloadReductionActive() is None
        assert cluster.getNmCarWakeUpBitPosition() is None
        assert cluster.getNmCarWakeUpFilterNodeId() is None
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

    def test_get_set_nm_busload_reduction_active(self):
        cluster = CanNmCluster(MockParent(), "CanNmCluster")
        value = _bool(True)
        assert cluster.setNmBusloadReductionActive(value) is cluster
        assert cluster.getNmBusloadReductionActive() is value
        cluster.setNmBusloadReductionActive(None)
        assert cluster.getNmBusloadReductionActive() is value

    def test_get_set_positive_integers(self):
        cluster = CanNmCluster(MockParent(), "CanNmCluster")
        pairs = [
            (cluster.setNmCarWakeUpBitPosition, cluster.getNmCarWakeUpBitPosition),
            (cluster.setNmCarWakeUpFilterNodeId, cluster.getNmCarWakeUpFilterNodeId),
            (cluster.setNmImmediateNmTransmissions, cluster.getNmImmediateNmTransmissions),
        ]
        for setter, getter in pairs:
            value = _pos_int("4")
            assert setter(value) is cluster
            assert getter() is value
            setter(None)
            assert getter() is value

    def test_get_set_integers(self):
        cluster = CanNmCluster(MockParent(), "CanNmCluster")
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
        cluster = CanNmCluster(MockParent(), "CanNmCluster")
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
