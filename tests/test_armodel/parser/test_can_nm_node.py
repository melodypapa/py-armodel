import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmNode
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _parse_can_nm_node(xml):
    root = ET.fromstring(xml)
    node = CanNmNode(MockParent(), "CanNmNode")
    ARXMLParser().readCanNmNode(root, node)
    return node


class TestParseCanNmNode:
    def test_parse_can_nm_node_field_values(self):
        xml = (
            "<CAN-NM-NODE xmlns='%s'>"
            "<ALL-NM-MESSAGES-KEEP-AWAKE>true</ALL-NM-MESSAGES-KEEP-AWAKE>"
            "<NM-CAR-WAKE-UP-FILTER-ENABLED>true</NM-CAR-WAKE-UP-FILTER-ENABLED>"
            "<NM-CAR-WAKE-UP-RX-ENABLED>false</NM-CAR-WAKE-UP-RX-ENABLED>"
            "<NM-MSG-CYCLE-OFFSET>0.02</NM-MSG-CYCLE-OFFSET>"
            "<NM-MSG-REDUCED-TIME>0.05</NM-MSG-REDUCED-TIME>"
            "</CAN-NM-NODE>" % NS
        )
        node = _parse_can_nm_node(xml)
        assert node.getAllNmMessagesKeepAwake().getValue() is True
        assert node.getNmCarWakeUpFilterEnabled().getValue() is True
        assert node.getNmCarWakeUpRxEnabled().getValue() is False
        assert node.getNmMsgCycleOffset().getValue() == 0.02
        assert node.getNmMsgReducedTime().getValue() == 0.05

    def test_parse_can_nm_node_empty(self):
        xml = "<CAN-NM-NODE xmlns='%s'/>" % NS
        node = _parse_can_nm_node(xml)
        assert node.getAllNmMessagesKeepAwake() is None
        assert node.getNmCarWakeUpFilterEnabled() is None
        assert node.getNmCarWakeUpRxEnabled() is None
        assert node.getNmMsgCycleOffset() is None
        assert node.getNmMsgReducedTime() is None

    def test_parse_can_nm_node_ignores_xsd_only_tags(self):
        xml = (
            "<CAN-NM-NODE xmlns='%s'>"
            "<CAN-XL-NM-PROPS/>"
            "<NM-RANGE-CONFIG><LOWER-CAN-ID>1</LOWER-CAN-ID><UPPER-CAN-ID>2</UPPER-CAN-ID></NM-RANGE-CONFIG>"
            "<NM-CAR-WAKE-UP-RX-ENABLED>true</NM-CAR-WAKE-UP-RX-ENABLED>"
            "</CAN-NM-NODE>" % NS
        )
        node = _parse_can_nm_node(xml)
        assert not hasattr(node, "nmRangeConfig")
        assert not hasattr(node, "canXlNmProps")
        assert node.getNmCarWakeUpRxEnabled().getValue() is True
        assert node.getNmMsgCycleOffset() is None
