"""Writer round-trip tests for SystemSignalToCommunicationResourceMapping (Table 5.51, p.289).

Serialized through the SYSTEM-SIGNAL-TO-COMMUNICATION-RESOURCE-MAPPING element
(AUTOSAR_00052.xsd l.120004) and the SYSTEM-SIGNAL-TO-COM-RESOURCE-MAPPINGS wrapper
of SystemMapping (l.119735).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import SystemSignalToCommunicationResourceMapping
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


class TestWriteSystemSignalToCommunicationResourceMapping:
    def test_empty(self):
        mapping = SystemSignalToCommunicationResourceMapping(None, "mapping")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemSignalToCommunicationResourceMapping(parent, mapping)

        node = parent.find("SYSTEM-SIGNAL-TO-COMMUNICATION-RESOURCE-MAPPING")
        assert node is not None
        assert node.find("SOFTWARE-CLUSTER-COM-RESOURCE-REF") is None
        assert node.find("SYSTEM-SIGNAL-REF") is None

    def test_full(self):
        mapping = SystemSignalToCommunicationResourceMapping(None, "mapping")
        mapping.setSoftwareClusterComResourceRef(_ref("/Resources/MyComResource", "CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE"))
        mapping.setSystemSignalRef(_ref("/Signals/MySignal", "SYSTEM-SIGNAL"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemSignalToCommunicationResourceMapping(parent, mapping)

        node = parent.find("SYSTEM-SIGNAL-TO-COMMUNICATION-RESOURCE-MAPPING")
        children = [child.tag for child in node]
        assert children[-2:] == ["SOFTWARE-CLUSTER-COM-RESOURCE-REF", "SYSTEM-SIGNAL-REF"]
        assert node.find("SOFTWARE-CLUSTER-COM-RESOURCE-REF").get("DEST") == "CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE"
        assert node.find("SYSTEM-SIGNAL-REF").text == "/Signals/MySignal"

    def test_round_trip_full(self):
        mapping = SystemSignalToCommunicationResourceMapping(None, "mapping")
        mapping.setSoftwareClusterComResourceRef(_ref("/Resources/MyComResource", "CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE"))
        mapping.setSystemSignalRef(_ref("/Signals/MySignal", "SYSTEM-SIGNAL"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemSignalToCommunicationResourceMapping(parent, mapping)

        reloaded = SystemSignalToCommunicationResourceMapping(None, "mapping")
        ARXMLParser().readSystemSignalToCommunicationResourceMapping(_with_ns(parent)[0], reloaded)

        assert reloaded.getSoftwareClusterComResourceRef().getValue() == "/Resources/MyComResource"
        assert reloaded.getSystemSignalRef().getValue() == "/Signals/MySignal"

    def test_round_trip_via_system_mapping_empty_wrapper(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingSystemSignalToComResourceMappings(parent, system_mapping)

        assert parent.find("SYSTEM-SIGNAL-TO-COM-RESOURCE-MAPPINGS") is None

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = SystemSignalToCommunicationResourceMapping(system_mapping, "mapping")
        mapping.setSystemSignalRef(_ref("/Signals/MySignal", "SYSTEM-SIGNAL"))
        system_mapping.addSystemSignalToComResourceMapping(mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingSystemSignalToComResourceMappings(parent, system_mapping)

        wrapper = parent.find("SYSTEM-SIGNAL-TO-COM-RESOURCE-MAPPINGS")
        assert wrapper is not None

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingSystemSignalToComResourceMappings(_with_ns(parent), reloaded_mapping)
        mappings = reloaded_mapping.getSystemSignalToComResourceMappings()
        assert len(mappings) == 1
        assert mappings[0].getSystemSignalRef().getValue() == "/Signals/MySignal"
