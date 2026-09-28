from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import UdpNmNode


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


class TestUdpNmNode:
    def test_initialization(self):
        node = UdpNmNode(MockParent(), "UdpNmNode")
        assert node.getShortName() == "UdpNmNode"
        assert node.getAllNmMessagesKeepAwake() is None
        assert node.getNmMsgCycleOffset() is None

    def test_get_set_booleans(self):
        node = UdpNmNode(MockParent(), "UdpNmNode")
        value = _bool(True)
        assert node.setAllNmMessagesKeepAwake(value) is node
        assert node.getAllNmMessagesKeepAwake() is value
        node.setAllNmMessagesKeepAwake(None)
        assert node.getAllNmMessagesKeepAwake() is value

    def test_get_set_times(self):
        node = UdpNmNode(MockParent(), "UdpNmNode")
        value = _time("0.02")
        assert node.setNmMsgCycleOffset(value) is node
        assert node.getNmMsgCycleOffset() is value
        node.setNmMsgCycleOffset(None)
        assert node.getNmMsgCycleOffset() is value
