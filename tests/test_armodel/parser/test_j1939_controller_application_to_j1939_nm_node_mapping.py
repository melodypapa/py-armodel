"""Parser tests for J1939ControllerApplicationToJ1939NmNodeMapping (Table 5.12, p.207).

ARObject aggregated through the J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPINGS
wrapper (XSD group J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPING,
AUTOSAR_00052.xsd l.75223: J-1939-CONTROLLER-APPLICATION-REF, J-1939-NM-NODE-REF).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import J1939ControllerApplicationToJ1939NmNodeMapping
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    xml = "<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner)
    return ET.fromstring(xml)


J1939_MAPPING = (
    "<J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPING S='checksum-1'>"
    "<J-1939-CONTROLLER-APPLICATION-REF DEST='J-1939-CONTROLLER-APPLICATION'>/J1939ControllerApplications/Ca1</J-1939-CONTROLLER-APPLICATION-REF>"
    "<J-1939-NM-NODE-REF DEST='J-1939-NM-NODE'>/Cluster/J1939NmNodes/Node1</J-1939-NM-NODE-REF>"
    "</J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPING>"
)


class TestReadJ1939ControllerApplicationToJ1939NmNodeMapping:
    def test_read_field_values_via_system_mapping(self):
        """Test that both ref field values and the S checksum survive the reader"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        root = _snip(
            "<SYSTEM-MAPPING>"
            "<SHORT-NAME>SystemMapping</SHORT-NAME>"
            "<J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPINGS>" + J1939_MAPPING + "</J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPINGS>"
            "</SYSTEM-MAPPING>"
        )
        ARXMLParser().readSystemMapping(root[0], mapping)

        j1939_mappings = mapping.getJ1939ControllerApplicationToJ1939NmNodeMappings()
        assert len(j1939_mappings) == 1
        j1939_mapping = j1939_mappings[0]
        assert isinstance(j1939_mapping, J1939ControllerApplicationToJ1939NmNodeMapping)

        ca_ref = j1939_mapping.getJ1939ControllerApplicationRef()
        assert ca_ref is not None
        assert ca_ref.getValue() == "/J1939ControllerApplications/Ca1"
        assert ca_ref.getDest() == "J-1939-CONTROLLER-APPLICATION"

        node_ref = j1939_mapping.getJ1939NmNodeRef()
        assert node_ref is not None
        assert node_ref.getValue() == "/Cluster/J1939NmNodes/Node1"
        assert node_ref.getDest() == "J-1939-NM-NODE"

        assert j1939_mapping.getChecksum().getValue() == "checksum-1"

    def test_read_empty_wrapper(self):
        """Test that an empty wrapper leaves the list empty and both fields None"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        root = _snip("<SYSTEM-MAPPING>" "<SHORT-NAME>SystemMapping</SHORT-NAME>" "<J-1939-CONTROLLER-APPLICATION-TO-J-1939-NM-NODE-MAPPINGS/>" "</SYSTEM-MAPPING>")
        ARXMLParser().readSystemMapping(root[0], mapping)

        assert mapping.getJ1939ControllerApplicationToJ1939NmNodeMappings() == []
