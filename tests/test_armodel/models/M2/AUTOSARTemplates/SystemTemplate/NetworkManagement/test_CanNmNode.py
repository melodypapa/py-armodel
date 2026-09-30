from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmNode


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


class TestCanNmNode:
    def test_initialization(self):
        node = CanNmNode(MockParent(), "CanNmNode")
        assert node.getShortName() == "CanNmNode"
        assert node.getAllNmMessagesKeepAwake() is None
        assert node.getNmCarWakeUpFilterEnabled() is None
        assert node.getNmCarWakeUpRxEnabled() is None
        assert node.getNmMsgCycleOffset() is None
        assert node.getNmMsgReducedTime() is None

    def test_get_set_booleans(self):
        node = CanNmNode(MockParent(), "CanNmNode")
        pairs = [
            (node.setAllNmMessagesKeepAwake, node.getAllNmMessagesKeepAwake),
            (node.setNmCarWakeUpFilterEnabled, node.getNmCarWakeUpFilterEnabled),
            (node.setNmCarWakeUpRxEnabled, node.getNmCarWakeUpRxEnabled),
        ]
        for setter, getter in pairs:
            value = _bool(True)
            assert setter(value) is node
            assert getter() is value
            setter(None)
            assert getter() is value

    def test_get_set_times(self):
        node = CanNmNode(MockParent(), "CanNmNode")
        pairs = [
            (node.setNmMsgCycleOffset, node.getNmMsgCycleOffset),
            (node.setNmMsgReducedTime, node.getNmMsgReducedTime),
        ]
        for setter, getter in pairs:
            value = _time("0.02")
            assert setter(value) is node
            assert getter() is value
            setter(None)
            assert getter() is value
