import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, Integer, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmNode, NmCoordinatorRoleEnum
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


def _integer(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _positive_integer(value):
    positive_integer = PositiveInteger()
    positive_integer.setValue(value)
    return positive_integer


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _vp(label):
    vp = VariationPoint()
    vp.setShortLabel(Identifier().setValue(label))
    return vp


def _new_node():
    node = CanNmNode(MockParent(), "CanNmNode")
    node.setControllerRef(_ref("COMMUNICATION-CONTROLLER", "/Topology/Can1/Controller"))
    node.setNmCoordCluster(_positive_integer("2"))
    role = NmCoordinatorRoleEnum()
    role.setValue(NmCoordinatorRoleEnum.ACTIVE)
    node.setNmCoordinatorRole(role)
    node.setNmIfEcuRef(_ref("NM-ECU", "/Ecus/Can1/NmEcu"))
    node.setNmNodeId(_integer(16))
    node.setNmPassiveModeEnabled(_bool(True))
    node.addRxNmPduRef(_ref("NM-PDU", "/Pdus/NmPdu1"))
    node.addTxNmPduRef(_ref("NM-PDU", "/Pdus/NmPdu2"))
    return node


_XSD_ELEMENT_ORDER = [
    "CONTROLLER-REF",
    "NM-COORD-CLUSTER",
    "NM-COORDINATOR-ROLE",
    "NM-IF-ECU-REF",
    "NM-NODE-ID",
    "NM-PASSIVE-MODE-ENABLED",
    "RX-NM-PDU-REFS",
    "TX-NM-PDU-REFS",
]


class TestWriteNmNode:
    def test_write_nm_node_element_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmNode(parent, _new_node())
        tags = [child.tag for child in parent if child.tag != "SHORT-NAME"]
        assert tags == _XSD_ELEMENT_ORDER
        rx_element = parent.find("RX-NM-PDU-REFS")
        assert rx_element.find("RX-NM-PDU-REF").text == "/Pdus/NmPdu1"
        assert rx_element.find("RX-NM-PDU-REF").attrib["DEST"] == "NM-PDU"
        assert parent.find("TX-NM-PDU-REFS/TX-NM-PDU-REF").text == "/Pdus/NmPdu2"

    def test_write_nm_node_empty(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmNode(parent, CanNmNode(MockParent(), "Empty"))
        tags = [child.tag for child in parent if child.tag != "SHORT-NAME"]
        assert tags == []

    def test_write_nm_node_empty_ref_wrappers_omitted(self):
        """
        Empty RX/TX-NM-PDU-REFS wrappers are not emitted.
        """
        parent = ET.Element("PARENT")
        node = CanNmNode(MockParent(), "NoRefs")
        node.setNmNodeId(_integer(16))
        ARXMLWriter().writeNmNode(parent, node)
        assert parent.find("RX-NM-PDU-REFS") is None
        assert parent.find("TX-NM-PDU-REFS") is None
        assert parent.find("NM-NODE-ID").text == "16"

    def test_write_nm_node_round_trip_field_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeNmNode(parent, _new_node())
        parent.set("xmlns", NS)
        root = ET.fromstring(ET.tostring(parent, encoding="unicode"))
        parsed = CanNmNode(MockParent(), "CanNmNode")
        ARXMLParser().readNmNode(root, parsed)
        assert parsed.getControllerRef().getValue() == "/Topology/Can1/Controller"
        assert parsed.getControllerRef().getDest() == "COMMUNICATION-CONTROLLER"
        assert parsed.getNmCoordCluster().getValue() == 2
        assert parsed.getNmCoordinatorRole().getValue() == "ACTIVE"
        assert parsed.getNmIfEcuRef().getValue() == "/Ecus/Can1/NmEcu"
        assert parsed.getNmNodeId().getValue() == 16
        assert parsed.getNmPassiveModeEnabled().getValue() is True
        assert parsed.getRxNmPduRefs()[0].getValue() == "/Pdus/NmPdu1"
        assert parsed.getTxNmPduRefs()[0].getValue() == "/Pdus/NmPdu2"

    def test_write_nm_node_writes_variation_point_last(self):
        """
        VARIATION-POINT (XSD sequenceOffset=10000) is emitted by the concrete-element
        writer after all base and subclass elements.
        """
        node = _new_node()
        node.setVariationPoint(_vp("VP1"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanNmNode(parent, node)
        node_element = parent.find("CAN-NM-NODE")
        tags = [child.tag for child in node_element if child.tag != "SHORT-NAME"]
        assert tags == _XSD_ELEMENT_ORDER + ["VARIATION-POINT"]
        assert node_element.find("VARIATION-POINT/SHORT-LABEL").text == "VP1"

    def test_write_nm_node_round_trips_variation_point(self):
        node = _new_node()
        node.setVariationPoint(_vp("VP1"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCanNmNode(parent, node)
        parent.set("xmlns", NS)
        root = ET.fromstring(ET.tostring(parent, encoding="unicode")).find("{%s}CAN-NM-NODE" % NS)
        parsed = CanNmNode(MockParent(), "CanNmNode")
        ARXMLParser().readCanNmNode(root, parsed)
        assert parsed.getVariationPoint() is not None
        assert parsed.getVariationPoint().getShortLabel().getValue() == "VP1"
        assert parsed.getNmNodeId().getValue() == 16
