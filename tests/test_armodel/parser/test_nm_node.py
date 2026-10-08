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


def _parse_nm_node(xml):
    root = ET.fromstring(xml)
    node = CanNmNode(MockParent(), "CanNmNode")
    ARXMLParser().readNmNode(root, node)
    return node


class TestParseNmNode:
    def test_parse_nm_node_field_values(self):
        xml = (
            "<NM-NODE xmlns='%s'>"
            "<SHORT-NAME>CanNmNode</SHORT-NAME>"
            "<CONTROLLER-REF DEST='COMMUNICATION-CONTROLLER'>/Topology/Can1/Controller</CONTROLLER-REF>"
            "<NM-COORD-CLUSTER>2</NM-COORD-CLUSTER>"
            "<NM-COORDINATOR-ROLE>ACTIVE</NM-COORDINATOR-ROLE>"
            "<NM-IF-ECU-REF DEST='NM-ECU'>/Ecus/Can1/NmEcu</NM-IF-ECU-REF>"
            "<NM-NODE-ID>16</NM-NODE-ID>"
            "<NM-PASSIVE-MODE-ENABLED>true</NM-PASSIVE-MODE-ENABLED>"
            "<RX-NM-PDU-REFS><RX-NM-PDU-REF DEST='NM-PDU'>/Pdus/NmPdu1</RX-NM-PDU-REF></RX-NM-PDU-REFS>"
            "<TX-NM-PDU-REFS><TX-NM-PDU-REF DEST='NM-PDU'>/Pdus/NmPdu2</TX-NM-PDU-REF></TX-NM-PDU-REFS>"
            "</NM-NODE>" % NS
        )
        node = _parse_nm_node(xml)
        assert node.getControllerRef().getDest() == "COMMUNICATION-CONTROLLER"
        assert node.getControllerRef().getValue() == "/Topology/Can1/Controller"
        assert node.getNmCoordCluster().getValue() == 2
        assert node.getNmCoordinatorRole().getValue() == "ACTIVE"
        assert node.getNmIfEcuRef().getDest() == "NM-ECU"
        assert node.getNmIfEcuRef().getValue() == "/Ecus/Can1/NmEcu"
        assert node.getNmNodeId().getValue() == 16
        assert node.getNmPassiveModeEnabled().getValue() is True
        rx_refs = node.getRxNmPduRefs()
        assert len(rx_refs) == 1
        assert rx_refs[0].getDest() == "NM-PDU"
        assert rx_refs[0].getValue() == "/Pdus/NmPdu1"
        tx_refs = node.getTxNmPduRefs()
        assert len(tx_refs) == 1
        assert tx_refs[0].getDest() == "NM-PDU"
        assert tx_refs[0].getValue() == "/Pdus/NmPdu2"

    def test_parse_nm_node_empty(self):
        xml = "<NM-NODE xmlns='%s'/>" % NS
        node = _parse_nm_node(xml)
        assert node.getControllerRef() is None
        assert node.getNmCoordCluster() is None
        assert node.getNmCoordinatorRole() is None
        assert node.getNmIfEcuRef() is None
        assert node.getNmNodeId() is None
        assert node.getNmPassiveModeEnabled() is None
        assert node.getRxNmPduRefs() == []
        assert node.getTxNmPduRefs() == []

    def test_parse_nm_node_ignores_xsd_only_ap_tag(self):
        """
        MACHINE-REF is the XSD-only AP variant (mmt.RestrictToStandards="AP") absent from
        the CP Table 6.303 — not modeled, ignored on read.
        """
        xml = "<NM-NODE xmlns='%s'>" "<MACHINE-REF DEST='MACHINE-DESIGN'>/Machines/M1</MACHINE-REF>" "<NM-NODE-ID>16</NM-NODE-ID>" "</NM-NODE>" % NS
        node = _parse_nm_node(xml)
        assert not hasattr(node, "machineRef")
        assert node.getNmNodeId().getValue() == 16
