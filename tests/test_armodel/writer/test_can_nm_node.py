import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmNode
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


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


def _new_node():
    node = CanNmNode(MockParent(), "CanNmNode")
    node.setAllNmMessagesKeepAwake(_bool(True))
    node.setNmCarWakeUpFilterEnabled(_bool(True))
    node.setNmCarWakeUpRxEnabled(_bool(False))
    node.setNmMsgCycleOffset(_time("0.02"))
    node.setNmMsgReducedTime(_time("0.05"))
    return node


_XSD_ELEMENT_ORDER = [
    "ALL-NM-MESSAGES-KEEP-AWAKE",
    "NM-CAR-WAKE-UP-FILTER-ENABLED",
    "NM-CAR-WAKE-UP-RX-ENABLED",
    "NM-MSG-CYCLE-OFFSET",
    "NM-MSG-REDUCED-TIME",
]


class TestWriteCanNmNode:
    def test_write_can_nm_node_element_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanNmNode(parent, _new_node())
        node_element = parent.find("CAN-NM-NODE")
        tags = [child.tag for child in node_element if child.tag != "SHORT-NAME"]
        assert tags == _XSD_ELEMENT_ORDER
        assert node_element.find("CAN-XL-NM-PROPS") is None
        assert node_element.find("NM-RANGE-CONFIG") is None

    def test_write_can_nm_node_empty(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanNmNode(parent, CanNmNode(MockParent(), "Empty"))
        node_element = parent.find("CAN-NM-NODE")
        tags = [child.tag for child in node_element if child.tag != "SHORT-NAME"]
        assert tags == []

    def test_write_can_nm_node_round_trip_field_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanNmNode(parent, _new_node())
        parent.set("xmlns", NS)
        root = ET.fromstring(ET.tostring(parent, encoding="unicode")).find("{%s}CAN-NM-NODE" % NS)
        node = CanNmNode(MockParent(), "CanNmNode")
        ARXMLParser().readCanNmNode(root, node)
        assert node.getAllNmMessagesKeepAwake().getValue() is True
        assert node.getNmCarWakeUpFilterEnabled().getValue() is True
        assert node.getNmCarWakeUpRxEnabled().getValue() is False
        assert node.getNmMsgCycleOffset().getValue() == 0.02
        assert node.getNmMsgReducedTime().getValue() == 0.05
