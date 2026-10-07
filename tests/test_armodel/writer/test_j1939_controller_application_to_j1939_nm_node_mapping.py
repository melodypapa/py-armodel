"""Writer round-trip tests for J1939ControllerApplicationToJ1939NmNodeMapping (Table 5.12, p.207).

Serialized through the J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPINGS wrapper;
child element order = XSD group J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPING
sequence (AUTOSAR_00052.xsd l.75223): J-1939-CONTROLLER-APPLICATION-REF,
J-1939-NM-NODE-REF. ARObject level carries no SHORT-NAME.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import J1939ControllerApplicationToJ1939NmNodeMapping
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestWriteJ1939ControllerApplicationToJ1939NmNodeMapping:
    def test_round_trip_via_system_mapping(self):
        """Test write -> re-parse round trip with field values, S checksum and XSD element order"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        j1939_mapping = J1939ControllerApplicationToJ1939NmNodeMapping()
        checksum = String()
        checksum.setValue("checksum-1")
        j1939_mapping.setChecksum(checksum)
        j1939_mapping.setJ1939ControllerApplicationRef(_ref("/J1939ControllerApplications/Ca1", "J-1939-CONTROLLER-APPLICATION"))
        j1939_mapping.setJ1939NmNodeRef(_ref("/Cluster/J1939NmNodes/Node1", "J-1939-NM-NODE"))
        mapping.addJ1939ControllerApplicationToJ1939NmNodeMapping(j1939_mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, mapping)

        node = parent.find("SYSTEM-MAPPING")
        assert node is not None
        wrappers = node.find("J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPINGS")
        assert wrappers is not None
        children = list(wrappers)
        assert len(children) == 1
        j1939_node = children[0]
        assert j1939_node.tag == "J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPING"
        assert [child.tag for child in j1939_node] == ["J-1939-CONTROLLER-APPLICATION-REF", "J-1939-NM-NODE-REF"]

        ca_node = j1939_node.find("J-1939-CONTROLLER-APPLICATION-REF")
        assert ca_node.text == "/J1939ControllerApplications/Ca1"
        assert ca_node.attrib["DEST"] == "J-1939-CONTROLLER-APPLICATION"
        node_element = j1939_node.find("J-1939-NM-NODE-REF")
        assert node_element.text == "/Cluster/J1939NmNodes/Node1"
        assert node_element.attrib["DEST"] == "J-1939-NM-NODE"
        assert j1939_node.attrib["S"] == "checksum-1"

        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)
        reloaded = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        ARXMLParser().readSystemMapping(root[0], reloaded)

        reloaded_mappings = reloaded.getJ1939ControllerApplicationToJ1939NmNodeMappings()
        assert len(reloaded_mappings) == 1
        round_tripped = reloaded_mappings[0]
        assert round_tripped.getChecksum().getValue() == "checksum-1"
        assert round_tripped.getJ1939ControllerApplicationRef().getValue() == "/J1939ControllerApplications/Ca1"
        assert round_tripped.getJ1939ControllerApplicationRef().getDest() == "J-1939-CONTROLLER-APPLICATION"
        assert round_tripped.getJ1939NmNodeRef().getValue() == "/Cluster/J1939NmNodes/Node1"
        assert round_tripped.getJ1939NmNodeRef().getDest() == "J-1939-NM-NODE"

    def test_empty_wrapper_not_emitted(self):
        """Test that a childless SystemMapping emits no J-1939-...-MAPPINGS wrapper"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, mapping)

        node = parent.find("SYSTEM-MAPPING")
        assert node is not None
        assert node.find("J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPINGS") is None

    def test_fields_absent_not_emitted(self):
        """Test that unset optional fields emit no elements on a populated mapping"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        mapping.addJ1939ControllerApplicationToJ1939NmNodeMapping(J1939ControllerApplicationToJ1939NmNodeMapping())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, mapping)

        j1939_node = parent.find("SYSTEM-MAPPING/J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPINGS/J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPING")
        assert j1939_node is not None
        assert len(list(j1939_node)) == 0
