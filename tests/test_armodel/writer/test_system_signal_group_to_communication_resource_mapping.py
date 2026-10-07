"""Writer round-trip tests for SystemSignalGroupToCommunicationResourceMapping (Table 5.52, p.290).

Serialized through the SYSTEM-SIGNAL-TO-COMMUNICATION-RESOURCE-MAPPING element
(AUTOSAR_00052.xsd l.119943) and the SYSTEM-SIGNAL-GROUP-TO-COM-RESOURCE-MAPPINGS wrapper
of SystemMapping (l.119723).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import SystemSignalGroupToCommunicationResourceMapping
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestWriteSystemSignalGroupToCommunicationResourceMapping:
    def test_empty(self):
        mapping = SystemSignalGroupToCommunicationResourceMapping(None, "mapping")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemSignalGroupToCommunicationResourceMapping(parent, mapping)

        node = parent.find("SYSTEM-SIGNAL-GROUP-TO-COMMUNICATION-RESOURCE-MAPPING")
        assert node is not None
        assert node.find("SOFTWARE-CLUSTER-COM-RESOURCE-REF") is None
        assert node.find("SYSTEM-SIGNAL-GROUP-REF") is None

    def test_full(self):
        mapping = SystemSignalGroupToCommunicationResourceMapping(None, "mapping")
        mapping.setSoftwareClusterComResourceRef(_ref("/Resources/MyComResource", "CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE"))
        mapping.setSystemSignalGroupRef(_ref("/SignalGroups/MySignalGroup", "SYSTEM-SIGNAL-GROUP"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemSignalGroupToCommunicationResourceMapping(parent, mapping)

        node = parent.find("SYSTEM-SIGNAL-GROUP-TO-COMMUNICATION-RESOURCE-MAPPING")
        children = [child.tag for child in node]
        assert children[-2:] == ["SOFTWARE-CLUSTER-COM-RESOURCE-REF", "SYSTEM-SIGNAL-GROUP-REF"]
        assert node.find("SOFTWARE-CLUSTER-COM-RESOURCE-REF").get("DEST") == "CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE"
        assert node.find("SYSTEM-SIGNAL-GROUP-REF").text == "/SignalGroups/MySignalGroup"

    def test_round_trip_full(self):
        mapping = SystemSignalGroupToCommunicationResourceMapping(None, "mapping")
        mapping.setSoftwareClusterComResourceRef(_ref("/Resources/MyComResource", "CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE"))
        mapping.setSystemSignalGroupRef(_ref("/SignalGroups/MySignalGroup", "SYSTEM-SIGNAL-GROUP"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemSignalGroupToCommunicationResourceMapping(parent, mapping)

        reloaded = SystemSignalGroupToCommunicationResourceMapping(None, "mapping")
        ARXMLParser().readSystemSignalGroupToCommunicationResourceMapping(_with_ns(parent)[0], reloaded)

        assert reloaded.getSoftwareClusterComResourceRef().getValue() == "/Resources/MyComResource"
        assert reloaded.getSystemSignalGroupRef().getValue() == "/SignalGroups/MySignalGroup"

    def test_round_trip_via_system_mapping_empty_wrapper(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingSystemSignalGroupToComResourceMappings(parent, system_mapping)

        assert parent.find("SYSTEM-SIGNAL-GROUP-TO-COM-RESOURCE-MAPPINGS") is None

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = SystemSignalGroupToCommunicationResourceMapping(system_mapping, "mapping")
        mapping.setSystemSignalGroupRef(_ref("/SignalGroups/MySignalGroup", "SYSTEM-SIGNAL-GROUP"))
        system_mapping.addSystemSignalGroupToComResourceMapping(mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingSystemSignalGroupToComResourceMappings(parent, system_mapping)

        wrapper = parent.find("SYSTEM-SIGNAL-GROUP-TO-COM-RESOURCE-MAPPINGS")
        assert wrapper is not None

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingSystemSignalGroupToComResourceMappings(_with_ns(parent), reloaded_mapping)
        mappings = reloaded_mapping.getSystemSignalGroupToComResourceMappings()
        assert len(mappings) == 1
        assert mappings[0].getSystemSignalGroupRef().getValue() == "/SignalGroups/MySignalGroup"
